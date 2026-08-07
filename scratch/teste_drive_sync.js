// Teste Node DOM-stub — feature "Sincronizar Google Drive" (Kimi K3, 2026-08-07)
// Mesmo harness de teste_upload_versao.js: extrai o <script> principal do
// index.html, roda com stubs (fetch simulado por rota) e executa asserções.
const fs = require('fs');
const lines = fs.readFileSync('index.html', 'utf8').split('\n');
let scriptStart = -1, scriptEnd = -1;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].trim() === '<script>') scriptStart = i; // último
}
for (let i = lines.length - 1; i >= 0; i--) {
  if (lines[i].trim() === '</script>') { scriptEnd = i; break; }
}
if (scriptStart < 0 || scriptEnd <= scriptStart) { console.log('bloco principal não achado'); process.exit(1); }
const code = lines.slice(scriptStart + 1, scriptEnd).join('\n');
const store = {};
const elements = {};
function makeEl(id) {
  return {
    id, innerHTML: '', value: '', checked: false, textContent: '', className: '', title: '',
    dataset: {}, style: {},
    classList: {
      _s: new Set(id === 'modal-drive-sync' ? ['hidden'] : []),
      add(c) { this._s.add(c); }, remove(c) { this._s.delete(c); },
      toggle(c, f) { if (f === undefined) { this._s.has(c) ? this._s.delete(c) : this._s.add(c); } else if (f) this._s.add(c); else this._s.delete(c); },
      contains(c) { return this._s.has(c); }
    },
    querySelectorAll: () => [], querySelector: () => makeEl('qs-tmp'), appendChild: () => {}, focus: () => {},
    getAttribute: () => null, setAttribute: () => {}, onclick: null
  };
}
global.document = {
  getElementById: id => (elements[id] = elements[id] || makeEl(id)),
  querySelectorAll: () => [], querySelector: () => null,
  createElement: () => makeEl('tmp'), addEventListener: () => {}, body: makeEl('body')
};
global.window = { addEventListener: () => {}, location: { hash: '' }, prompt: () => '' };
global.localStorage = {
  getItem: k => (k in store ? store[k] : null),
  setItem: (k, v) => { store[k] = String(v); },
  removeItem: k => { delete store[k]; },
  key: i => Object.keys(store)[i],
  get length() { return Object.keys(store).length; }
};
global.history = { replaceState: () => {} };
global.navigator = { clipboard: { writeText: async () => {} } };
global.alert = () => {};
global.confirm = () => true;
global.marked = { parse: s => s };
global.__elements = elements;
global.__store = store;

// fetch simulado por rota — configurável por teste
let FETCH_ROUTES = {};
global.__setFetchRoutes = r => { FETCH_ROUTES = r; };
global.__lastFetch = null;
global.__fetchLog = [];
global.fetch = async (url, opts) => {
  global.__lastFetch = { url, opts };
  global.__fetchLog.push({ url, opts });
  const key = Object.keys(FETCH_ROUTES).find(k => url.includes(k));
  const payload = key ? FETCH_ROUTES[key] : { ok: false, error: 'rota não simulada: ' + url };
  const status = payload.__status || 200;
  return { ok: status >= 200 && status < 300, status, json: async () => payload, text: async () => JSON.stringify(payload) };
};

const snippet = `
// ================= TESTES: SYNC GOOGLE DRIVE =================
const __results = [];
function __T(name, fn) { try { fn(); __results.push('✅ ' + name); } catch(e) { __results.push('❌ ' + name + ' — ' + e.message); } }
async function __Ta(name, fn) { try { await fn(); __results.push('✅ ' + name); } catch(e) { __results.push('❌ ' + name + ' — ' + e.message); } }
function __eq(a, b, msg) { if (a !== b) throw new Error((msg ? msg + ': ' : '') + 'esperado=' + JSON.stringify(b) + ' obtido=' + JSON.stringify(a)); }
function __ok(v, msg) { if (!v) throw new Error(msg || 'asserção falhou'); }

const REV_KEY = 'miguel_book_revisions_vol1_v7_01_estarei_vingado';
function __seed() {
  Object.keys(__store).forEach(k => delete __store[k]);
  currentVolume = 'vol1_v7';
  currentChapterKey = '01_estarei_vingado';
  currentVersionKey = 'oficial';
  currentViewMode = 'single';
  localStorage.setItem(REV_KEY, JSON.stringify({ R2: { versionTag: 'R2 (local)', content: 'local dois' } }));
  const m = document.getElementById('modal-drive-sync'); m.classList.add('hidden');
  document.getElementById('drive-sync-status').textContent = '';
  document.getElementById('drive-sync-log').textContent = '';
  document.getElementById('drive-sync-log').classList.add('hidden');
}

const STATUS_OK = { ok: true, folder: { id: '1MG', name: 'novo livro' },
  revisions: { id: 'r', name: 'revisions.json', size: '5146', modifiedTime: '2026-08-07T13:00:00.000Z' },
  customRules: { id: 'c', name: 'custom_rules.json', modifiedTime: '2026-08-07T13:00:00.000Z' },
  latestBackup: { name: 'livro_backup_20260807_040001.zip', modifiedTime: '2026-08-07T07:00:00.000Z' },
  serverTime: '2026-08-07T14:00:00.000Z' };

await __Ta('1. abrir modal dispara verificação de status (op=status)', async () => {
  __seed();
  __setFetchRoutes({ 'op=status': STATUS_OK });
  openDriveSyncModal();
  await new Promise(r => setTimeout(r, 20));
  __ok(!document.getElementById('modal-drive-sync').classList.contains('hidden'), 'modal não abriu');
  __ok(__lastFetch && __lastFetch.url.includes('/api/drive?op=status'), 'não chamou op=status: ' + (__lastFetch && __lastFetch.url));
  const st = document.getElementById('drive-sync-status').textContent;
  __ok(st.includes('✅ BACKUP CERTO'), 'sem veredito de backup certo: ' + st.slice(0, 80));
  __ok(st.includes('revisions.json') && st.includes('20260807_040001'), 'status incompleto: ' + st.slice(0, 200));
});

await __Ta('2. status com erro mostra aviso honesto', async () => {
  __seed();
  __setFetchRoutes({ 'op=status': { ok: false, error: 'GDRIVE_REFRESH_TOKEN ausente' } });
  await loadDriveSyncStatus();
  __ok(document.getElementById('drive-sync-status').textContent.includes('⚠️'), 'sem aviso de erro');
});

await __Ta('3. puxar do Drive mescla com prioridade LOCAL', async () => {
  __seed();
  // remoto tem R1 e R2-remoto; local tem R2-local → R1 entra, R2 fica o LOCAL
  __setFetchRoutes({ 'op=pull': { ok: true,
    revisions: { '01_estarei_vingado': { R1: { versionTag: 'R1 (drive)', content: 'remoto um' }, R2: { versionTag: 'R2 (drive)', content: 'remoto dois' } } },
    customRules: ['regra A', 'regra B'] },
    'op=status': STATUS_OK });
  localStorage.setItem('miguel_manual_de_estilo_custom_rules', JSON.stringify(['regra B', 'regra C']));
  await pullFromGoogleDrive(null);
  const revs = JSON.parse(__store[REV_KEY]);
  __eq(Object.keys(revs).sort().join(','), 'R1,R2', 'mescla incompleta');
  __eq(revs.R2.content, 'local dois', 'local tinha que vencer');
  __eq(revs.R1.content, 'remoto um', 'R1 do drive tinha que entrar');
  const rules = JSON.parse(__store['miguel_manual_de_estilo_custom_rules']);
  __eq(rules.join('|'), 'regra A|regra B|regra C', 'união de regras errada');
  __ok(document.getElementById('drive-sync-log').textContent.includes('✅ Puxado'), 'log sem confirmação');
});

await __Ta('4. enviar ao Drive: coleta R#s locais, manda chave, mostra snapshot+commit', async () => {
  __seed();
  localStorage.setItem('fdi_drive_sync_key', 'chave-teste');
  localStorage.setItem('miguel_manual_de_estilo_custom_rules', JSON.stringify(['regra X']));
  __setFetchRoutes({ 'op=push': { ok: true,
    drive: { revisions: { modifiedTime: '2026-08-07T14:00:00.000Z', size: '999' }, customRules: { modifiedTime: '2026-08-07T14:00:00.000Z' } },
    github: { revisions: { commit: 'abc1234' }, customRules: { commit: 'abc1234' } },
    snapshot: 'revisions_snapshot_20260807_1400.json' },
    'op=status': STATUS_OK });
  await pushToGoogleDrive(null);
  const pushCall = __fetchLog.find(f => f.url.includes('op=push'));
  __ok(pushCall, 'não chamou op=push');
  __eq(pushCall.opts.headers['x-sync-key'], 'chave-teste', 'chave não foi no header');
  const sent = JSON.parse(pushCall.opts.body);
  __ok(sent.revisions['01_estarei_vingado'].R2, 'revisões não coletadas');
  __eq(sent.customRules.join(''), 'regra X', 'regras não coletadas');
  const log = document.getElementById('drive-sync-log').textContent;
  __ok(log.includes('✅ ENVIADO') && log.includes('revisions_snapshot') && log.includes('abc1234'), 'log de sucesso incompleto: ' + log.slice(0, 120));
});

await __Ta('5. push 401 esquece a chave e avisa', async () => {
  __seed();
  localStorage.setItem('fdi_drive_sync_key', 'chave-errada');
  __setFetchRoutes({ 'op=push': { __status: 401, ok: false, error: 'Chave de sincronização ausente ou incorreta.' } });
  await pushToGoogleDrive(null);
  __eq(localStorage.getItem('fdi_drive_sync_key'), null, 'chave inválida tinha que ser esquecida');
  __ok(document.getElementById('drive-sync-log').textContent.includes('recusada'), 'log sem aviso de chave recusada');
});

await __Ta('6. push sem nada para enviar nem chama a rede', async () => {
  __seed();
  localStorage.removeItem(REV_KEY); // zero revisões locais
  __lastFetch = null;
  await pushToGoogleDrive(null);
  __eq(__lastFetch, null, 'não devia ter chamado fetch');
  __ok(document.getElementById('drive-sync-log').textContent.includes('Nada para enviar'), 'sem aviso de vazio');
});

// ---- checagens de fonte ----
__T('7. fonte: botão no header ao lado do GitHub', () => {
  __ok(__SOURCE__.includes('openDriveSyncModal()'), 'botão ausente');
  __ok(__SOURCE__.includes('☁️ Sincronizar Google Drive'), 'rótulo do botão ausente');
});
__T('8. fonte: modal + 4 ações', () => {
  __ok(__SOURCE__.includes('id="modal-drive-sync"'), 'modal ausente');
  __ok(__SOURCE__.includes('pullFromGoogleDrive') && __SOURCE__.includes('pushToGoogleDrive'), 'ações ausentes');
  __ok(__SOURCE__.includes('drive.google.com/drive/folders/1MGdnx-6jg3nhulk1AC8J4KivViMwFVe2'), 'link da pasta ausente');
});
__T('9. fonte: api/drive.js referenciado só via /api/drive (sem segredos no cliente)', () => {
  __ok(__SOURCE__.includes("'/api/drive?op="), 'chamadas /api/drive ausentes');
  __ok(!__SOURCE__.includes('GDRIVE_REFRESH_TOKEN'), 'segredo vazou no cliente!');
});

return __results.join('\\n');
`;

const test = 'const __SOURCE__ = ' + JSON.stringify(fs.readFileSync('index.html', 'utf8')) + ';\n' + code + snippet;
(async () => {
  try {
    const r = await new Function('return (async () => {' + test + '})()')();
    console.log(r);
    const fails = (r.match(/❌/g) || []).length;
    const total = (r.match(/✅/g) || []).length + fails;
    console.log('---');
    console.log(fails === 0 ? `✅ TODOS OS ${total} TESTES PASSARAM` : `❌ ${fails}/${total} FALHARAM`);
    process.exit(fails === 0 ? 0 : 1);
  } catch (e) {
    console.log('❌ ERRO:', e.message);
    console.log(e.stack.split('\n').slice(0, 5).join('\n'));
    process.exit(1);
  }
})();
