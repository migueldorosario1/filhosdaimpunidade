// ============================================================================
// Proxy serverless — Sincronização Google Drive (Filhos da Impunidade)
// ----------------------------------------------------------------------------
// Kimi K3, 2026-08-07 (pedido do Miguel: "bota um botão de sincronizar com o
// Google Drive... procure onde é que tem a gravação, o backup do livro,
// confere se é o backup certo").
//
// Backup certo verificado: pasta gdrive:novo livro (espelho diário 04:30 via
// rclone do espelho local; revisions.json md5 idêntico ao do GitHub).
//
// Ops:
//   GET  ?op=status → estado vivo do backup (arquivos, datas, último zip)
//   GET  ?op=pull   → baixa revisions.json + custom_rules.json do Drive
//   POST ?op=push   → grava os 2 JSONs no Drive (snapshot prévio em backups/)
//                     + espelha no GitHub (Contents API → redeploy Vercel)
//
// Segredos (NUNCA no código): GDRIVE_REFRESH_TOKEN, GITHUB_TOKEN,
// FDI_SYNC_SECRET — todos em env vars da Vercel (e no cofre .env.unificado).
// O client OAuth abaixo é o PÚBLICO do rclone (constante do fonte aberto,
// backend/drive/drive.go) — o segredo dele é distribuído ofuscado pelo
// próprio rclone (pacote fs/config/obscure, AES-256-CTR) e revelado aqui em
// runtime, exatamente como o binário do rclone faz.
// ============================================================================

import crypto from 'crypto';

export const config = { maxDuration: 60 };

const ALLOWED_ORIGINS = [
  'https://filhosdaimpunidade.vercel.app',
  'http://localhost:3000',
  'http://127.0.0.1:3000',
  'http://localhost:8000',
  'http://127.0.0.1:8000'
];

// Identidade do backup (IDs públicos — os 2 JSONs já são públicos via repo/Vercel)
const ROOT_FOLDER_ID = '1MGdnx-6jg3nhulk1AC8J4KivViMwFVe2';      // gdrive:novo livro
const BACKUPS_FOLDER_ID = '1aQDV2fvqKViAlXklPj2pSuIcxpJY_elU';    // gdrive:novo livro/backups
const REVISIONS_FILE_ID = '1_4bU2bc0o30lOOdN6REWjuAs6FxxE-Jh';    // revisions.json
const RULES_FILE_ID = '1QOgSBRc9UNfNFtKcKoFUuowH9SipYviF';        // custom_rules.json
const GH_REPO = 'migueldorosario1/filhosdaimpunidade';

// Cache do op=status (best-effort, por instância serverless): cada status
// consome 4 queries da quota COMPARTILHADA do projeto público do rclone —
// abrir o modal 2× seguidas não precisa consultar o Drive de novo.
const STATUS_CACHE_TTL_MS = 60 * 1000;
let statusCache = { at: 0, data: null };

const RCLONE_CLIENT_ID = '202264815644.apps.googleusercontent.com';
const RCLONE_ENCRYPTED_SECRET = 'eX8GpZTVx3vxMWVkuuBdDWmAUE6rGhTwVrvG9GhllYccSdj2-mvHVg';

// rclone fs/config/obscure: AES-256-CTR, chave pública fixa, IV = 16 primeiros
// bytes do payload decodificado (base64url).
const OBSCURE_KEY = Buffer.from([
  0x9c, 0x93, 0x5b, 0x48, 0x73, 0x0a, 0x55, 0x4d,
  0x6b, 0xfd, 0x7c, 0x63, 0xc8, 0x86, 0xa9, 0x2b,
  0xd3, 0x90, 0x19, 0x8e, 0xb8, 0x12, 0x8a, 0xfb,
  0xf4, 0xde, 0x16, 0x2b, 0x8b, 0x95, 0xf6, 0x38
]);

function obscureReveal(x) {
  const raw = Buffer.from(x, 'base64url');
  const iv = raw.subarray(0, 16);
  const ct = raw.subarray(16);
  const d = crypto.createDecipheriv('aes-256-ctr', OBSCURE_KEY, iv);
  return Buffer.concat([d.update(ct), d.final()]).toString('utf8');
}

async function getDriveToken() {
  const refreshToken = process.env.GDRIVE_REFRESH_TOKEN || '';
  if (!refreshToken) throw new Error('GDRIVE_REFRESH_TOKEN ausente nas env vars da Vercel');
  // O endpoint de token do projeto público do rclone também sofre rate-limit
  // → retry aqui também (erro real tipo invalid_grant falha na hora).
  return withQuotaRetry(async () => {
    const res = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        client_id: RCLONE_CLIENT_ID,
        client_secret: obscureReveal(RCLONE_ENCRYPTED_SECRET),
        refresh_token: refreshToken,
        grant_type: 'refresh_token'
      })
    });
    const data = await res.json();
    if (!res.ok || !data.access_token) {
      throw new Error('OAuth Google falhou: ' + (data.error_description || data.error || res.status));
    }
    return data.access_token;
  }, 'token OAuth');
}

async function driveGet(token, url) {
  const res = await fetch(url, { headers: { Authorization: 'Bearer ' + token } });
  const data = await res.json();
  if (!res.ok) throw new Error('Drive API ' + res.status + ': ' + (data.error && data.error.message || JSON.stringify(data)).slice(0, 300));
  return data;
}

// --- HARDENING 2026-08-07 (incidente de quota do projeto OAuth público do rclone) ---
// O client OAuth público do rclone divide a quota "Queries per minute" com
// TODOS os usuários de rclone do planeta — 403 de quota é rotina. Sem retry,
// o 1º push real falhou no meio; sem validação de shape, um payload de ERRO
// JSON do Google chegou a ser gravado por cima do revisions.json (restaurado
// via rclone + git, md5 conferido). As duas guardas abaixo impedem reprise.
// REFORÇO (mesmo dia, 2ª onda — Miguel pegou 403 de quota no op=status): o
// retry cobria só download/upload/snapshot; agora cobre também o token OAuth
// e as 4 chamadas de metadados do status, e o status ganhou cache de 60s pra
// consumir menos quota (bypass: ?nocache=1, usado pelo "↻ atualizar").
function isQuotaError(e) {
  return /quota|rate.?limit|429/i.test(String(e && e.message || e));
}

// Budget default: ~39s de esperas em 4 tentativas — cabe no maxDuration=60
// (pior caso c/ jitter ~47s + a última chamada em si). Jitter ±20% quando no
// default pra não sincronizar as retentativas com o resto do planeta.
const RETRY_WAITS_DEFAULT = [0, 5000, 12000, 22000];

async function withQuotaRetry(fn, label) {
  const waits = process.env.FDI_RETRY_WAITS
    ? process.env.FDI_RETRY_WAITS.split(',').map(Number)
    : RETRY_WAITS_DEFAULT.map(w => (w ? Math.round(w * (0.8 + Math.random() * 0.4)) : 0));
  let lastErr;
  for (let i = 0; i < waits.length; i++) {
    if (waits[i]) await new Promise(r => setTimeout(r, waits[i]));
    try { return await fn(); }
    catch (e) {
      lastErr = e;
      if (!isQuotaError(e)) throw e; // erro real: falha na hora
      console.warn(label + ': quota estourada, tentativa ' + (i + 1) + '/' + waits.length);
    }
  }
  throw lastErr;
}

// Shape esperado do revisions.json: { cap: { R#: { content: string, ... } } }
function validaShapeRevisions(revs) {
  if (!revs || typeof revs !== 'object' || Array.isArray(revs)) return false;
  for (const cap of Object.keys(revs)) {
    const entradas = revs[cap];
    if (!entradas || typeof entradas !== 'object' || Array.isArray(entradas)) return false;
    for (const rk of Object.keys(entradas)) {
      const rev = entradas[rk];
      if (!rev || typeof rev !== 'object' || typeof rev.content !== 'string') return false;
    }
  }
  return true;
}

function validaShapeRegras(rules) {
  return Array.isArray(rules) && rules.every(r => typeof r === 'string');
}

async function driveDownloadJson(token, fileId, nome) {
  const txt = await withQuotaRetry(async () => {
    const res = await fetch('https://www.googleapis.com/drive/v3/files/' + fileId + '?alt=media', { headers: { Authorization: 'Bearer ' + token } });
    const t = await res.text();
    if (!res.ok) throw new Error('Drive download ' + nome + ' falhou (' + res.status + '): ' + t.slice(0, 200));
    return t;
  }, 'download ' + nome);
  let data;
  try { data = JSON.parse(txt); }
  catch (e) { throw new Error('Drive download ' + nome + ': conteúdo não é JSON (' + txt.slice(0, 80) + ')'); }
  return data;
}

async function githubUpsertFile(path, contentStr, message) {
  const token = process.env.GITHUB_TOKEN || '';
  if (!token) return { skipped: 'GITHUB_TOKEN ausente' };
  const base = 'https://api.github.com/repos/' + GH_REPO + '/contents/' + path;
  const headers = { Authorization: 'Bearer ' + token, 'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json' };
  let sha;
  const cur = await fetch(base, { headers });
  if (cur.ok) { const j = await cur.json(); sha = j.sha; }
  const body = { message, content: Buffer.from(contentStr, 'utf8').toString('base64') };
  if (sha) body.sha = sha;
  const res = await fetch(base, { method: 'PUT', headers, body: JSON.stringify(body) });
  const data = await res.json();
  if (!res.ok) throw new Error('GitHub Contents ' + res.status + ': ' + (data.message || '').slice(0, 200));
  return { commit: (data.commit && data.commit.sha || '').slice(0, 7) };
}

export default async function handler(req, res) {
  const origin = req.headers.origin || '';
  if (ALLOWED_ORIGINS.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, x-sync-key');
  if (req.method === 'OPTIONS') return res.status(204).end();

  const op = (req.query && req.query.op) || 'status';

  try {
    if (op === 'push') {
      const secret = process.env.FDI_SYNC_SECRET || '';
      const sent = req.headers['x-sync-key'] || '';
      if (!secret || sent !== secret) {
        return res.status(401).json({ ok: false, error: 'Chave de sincronização ausente ou incorreta.' });
      }
    }

    if (op === 'status') {
      const nocache = String((req.query && req.query.nocache) || '') === '1';
      if (!nocache && statusCache.data && (Date.now() - statusCache.at) < STATUS_CACHE_TTL_MS) {
        return res.status(200).json({ ...statusCache.data, cached: true });
      }
    }

    const token = await getDriveToken();

    if (op === 'status') {
      const fields = 'id,name,size,modifiedTime';
      const folder = await withQuotaRetry(() => driveGet(token, 'https://www.googleapis.com/drive/v3/files/' + ROOT_FOLDER_ID + '?fields=id,name'), 'status pasta');
      const rev = await withQuotaRetry(() => driveGet(token, 'https://www.googleapis.com/drive/v3/files/' + REVISIONS_FILE_ID + '?fields=' + fields), 'status revisions');
      const rules = await withQuotaRetry(() => driveGet(token, 'https://www.googleapis.com/drive/v3/files/' + RULES_FILE_ID + '?fields=' + fields), 'status rules');
      const q = encodeURIComponent("'" + BACKUPS_FOLDER_ID + "' in parents and name contains 'livro_backup_' and trashed=false");
      const bak = await withQuotaRetry(() => driveGet(token, 'https://www.googleapis.com/drive/v3/files?q=' + q + '&orderBy=name%20desc&pageSize=1&fields=files(' + fields + ')'), 'status backups');
      const payload = {
        ok: true,
        folder,
        revisions: rev,
        customRules: rules,
        latestBackup: (bak.files && bak.files[0]) || null,
        serverTime: new Date().toISOString()
      };
      statusCache = { at: Date.now(), data: payload };
      return res.status(200).json(payload);
    }

    if (op === 'pull') {
      const revisions = await driveDownloadJson(token, REVISIONS_FILE_ID, 'revisions.json');
      const customRules = await driveDownloadJson(token, RULES_FILE_ID, 'custom_rules.json');
      if (!validaShapeRevisions(revisions)) {
        return res.status(502).json({ ok: false, error: 'revisions.json do Drive com formato inesperado — NADA foi repassado (proteção pós-incidente de quota).' });
      }
      if (!validaShapeRegras(customRules)) {
        return res.status(502).json({ ok: false, error: 'custom_rules.json do Drive com formato inesperado — NADA foi repassado (proteção pós-incidente de quota).' });
      }
      return res.status(200).json({ ok: true, revisions, customRules });
    }

    if (op === 'push') {
      if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'use POST' });
      const body = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
      const revisions = body.revisions && typeof body.revisions === 'object' ? body.revisions : {};
      const customRules = Array.isArray(body.customRules) ? body.customRules : [];
      // Guarda anti-lixo (incidente 07/08): nunca gravar payload que não tenha
      // o shape editorial esperado — um JSON de erro do Google passou por aqui.
      if (!validaShapeRevisions(revisions)) {
        return res.status(400).json({ ok: false, error: 'revisions com formato inválido (esperado {cap: {R#: {content}}}) — gravação RECUSADA.' });
      }
      if (!validaShapeRegras(customRules)) {
        return res.status(400).json({ ok: false, error: 'customRules com formato inválido (esperado array de strings) — gravação RECUSADA.' });
      }
      const revStr = JSON.stringify(revisions, null, 2);
      const rulesStr = JSON.stringify(customRules, null, 2);
      if (revStr.length + rulesStr.length > 4 * 1024 * 1024) {
        return res.status(413).json({ ok: false, error: 'Pacote grande demais (>4MB).' });
      }

      // 1) Snapshot de segurança do revisions.json atual em backups/
      const ts = new Date().toISOString().replace(/[-:T]/g, '').slice(0, 14);
      let snapshotName = null;
      try {
        const copy = await withQuotaRetry(() => drivePost(token, 'https://www.googleapis.com/drive/v3/files/' + REVISIONS_FILE_ID + '/copy', {
          name: 'revisions_snapshot_' + ts + '.json',
          parents: [BACKUPS_FOLDER_ID]
        }), 'snapshot');
        snapshotName = copy.name || null;
      } catch (e) { snapshotName = 'falhou: ' + e.message; }

      // 2) Atualiza os 2 arquivos no Drive (mesmo ID = mesmo arquivo, histórico preservado)
      const upFields = 'id,name,size,modifiedTime';
      const revUp = await withQuotaRetry(() => driveUpload(token, REVISIONS_FILE_ID, revStr, upFields), 'upload revisions');
      const rulesUp = await withQuotaRetry(() => driveUpload(token, RULES_FILE_ID, rulesStr, upFields), 'upload rules');

      // 3) Espelha no GitHub (mantém o site GitHub-sync fresco e dispara redeploy)
      let github;
      try {
        const m = 'sync: app FdI → Drive+GitHub ' + new Date().toISOString().slice(0, 16).replace('T', ' ');
        const g1 = await githubUpsertFile('revisions.json', revStr, m + ' (revisions)');
        const g2 = await githubUpsertFile('custom_rules.json', rulesStr, m + ' (rules)');
        github = { revisions: g1, customRules: g2 };
      } catch (e) { github = { erro: e.message }; }

      return res.status(200).json({
        ok: true,
        drive: { revisions: revUp, customRules: rulesUp },
        github,
        snapshot: snapshotName
      });
    }

    return res.status(400).json({ ok: false, error: 'op desconhecida: ' + op });
  } catch (e) {
    // quotaCongested deixa o cliente distinguir "quota compartilhada cheia"
    // de erro real de configuração (env vars ausentes etc.) sem regex.
    return res.status(502).json({ ok: false, error: String(e.message || e).slice(0, 400), quotaCongested: isQuotaError(e) });
  }
}

async function drivePost(token, url, jsonBody) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify(jsonBody)
  });
  const data = await res.json();
  if (!res.ok) throw new Error('Drive POST ' + res.status + ': ' + (data.error && data.error.message || '').slice(0, 200));
  return data;
}

async function driveUpload(token, fileId, contentStr, fields) {
  const res = await fetch('https://www.googleapis.com/upload/drive/v3/files/' + fileId + '?uploadType=media&fields=' + fields, {
    method: 'PATCH',
    headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json; charset=utf-8' },
    body: contentStr
  });
  const data = await res.json();
  if (!res.ok) throw new Error('Drive upload ' + res.status + ': ' + (data.error && data.error.message || '').slice(0, 200));
  return data;
}
