// Teste server-side do api/drive.js (Kimi K3, 2026-08-07)
// Importa o handler ESM real e dirige req/res falsos + fetch stubado.
// Foco: guardas anti-incidente (shape validation, auth, retry de quota)
// + reforço 2ª onda (retry no status/token, cache 60s do status).
process.env.FDI_SYNC_SECRET = 'chave-teste';
process.env.GDRIVE_REFRESH_TOKEN = 'rt-falso';
process.env.GITHUB_TOKEN = 'gh-falso';
process.env.FDI_RETRY_WAITS = '0,1,1';

const results = [];
const T = (n, f) => { try { f(); results.push('✅ ' + n); } catch (e) { results.push('❌ ' + n + ' — ' + e.message); } };
const Ta = async (n, f) => { try { await f(); results.push('✅ ' + n); } catch (e) { results.push('❌ ' + n + ' — ' + e.message); } };
const eq = (a, b, m) => { if (a !== b) throw new Error((m ? m + ': ' : '') + 'esp=' + JSON.stringify(b) + ' obt=' + JSON.stringify(a)); };
const ok = (v, m) => { if (!v) throw new Error(m || 'falhou'); };

let fetchCalls = [];
let routes = {};
global.fetch = async (url, opts = {}) => {
  fetchCalls.push({ url: String(url), opts });
  const key = Object.keys(routes).find(k => String(url).includes(k));
  let r = key ? routes[key] : { status: 404, body: { erro: 'rota não stubada: ' + url } };
  if (typeof r === 'function') r = r(String(url), opts); // stub stateful (1ª chamada falha, 2ª ok)
  return {
    ok: (r.status || 200) < 400,
    status: r.status || 200,
    json: async () => r.body,
    text: async () => (typeof r.body === 'string' ? r.body : JSON.stringify(r.body))
  };
};

function fakeRes() {
  return {
    statusCode: 200, body: null, headers: {},
    setHeader(k, v) { this.headers[k] = v; },
    status(c) { this.statusCode = c; return this; },
    json(o) { this.body = o; return this; },
    end() { return this; }
  };
}

const handler = (await import('../api/drive.js')).default;

await Ta('1. push sem chave → 401 e zero chamadas de rede', async () => {
  fetchCalls = []; routes = {};
  const res = fakeRes();
  await handler({ method: 'POST', query: { op: 'push' }, headers: {}, body: { revisions: {}, customRules: [] } }, res);
  eq(res.statusCode, 401);
  eq(fetchCalls.length, 0, 'não pode chamar rede sem auth');
});

await Ta('2. push com chave + revisions LIXO (payload de erro) → 400, nada gravado', async () => {
  fetchCalls = [];
  routes = { 'oauth2.googleapis.com': { body: { access_token: 'tok' } } };
  const res = fakeRes();
  await handler({ method: 'POST', query: { op: 'push' }, headers: { 'x-sync-key': 'chave-teste' },
    body: { revisions: { error: { code: 403, message: 'quota' } }, customRules: [] } }, res);
  eq(res.statusCode, 400, 'lixo tem que ser recusado');
  ok(res.body.error.includes('RECUSADA'), 'mensagem de recusa ausente');
  ok(!fetchCalls.some(c => c.url.includes('upload/drive')), 'NÃO pode gravar lixo no Drive');
  ok(!fetchCalls.some(c => c.url.includes('api.github.com')), 'NÃO pode gravar lixo no GitHub');
});

await Ta('3. push válido → snapshot + 2 uploads Drive + 2 commits GitHub', async () => {
  fetchCalls = [];
  routes = {
    'oauth2.googleapis.com': { body: { access_token: 'tok' } },
    '/copy': { body: { name: 'revisions_snapshot_X.json' } },
    'upload/drive': { body: { id: 'f', name: 'f.json', size: '10', modifiedTime: '2026-08-07T15:00:00Z' } },
    'api.github.com/repos': { status: 200, body: { sha: 's1', commit: { sha: 'abcdef123456' } } }
  };
  const res = fakeRes();
  await handler({ method: 'POST', query: { op: 'push' }, headers: { 'x-sync-key': 'chave-teste' },
    body: { revisions: { cap1: { R1: { content: 'texto' } } }, customRules: ['regra'] } }, res);
  eq(res.statusCode, 200);
  ok(res.body.ok, 'resposta ok');
  eq(res.body.snapshot, 'revisions_snapshot_X.json');
  eq(res.body.github.revisions.commit, 'abcdef1', 'commit curto');
  eq(fetchCalls.filter(c => c.url.includes('upload/drive')).length, 2, '2 uploads Drive');
  eq(fetchCalls.filter(c => c.url.includes('api.github.com')).length, 4, 'GET+PUT ×2 no GitHub');
});

await Ta('4. pull com quota (res.ok=false, msg quota) → retenta e 502 no fim, sem repassar lixo', async () => {
  fetchCalls = [];
  routes = {
    'oauth2.googleapis.com': { body: { access_token: 'tok' } },
    'alt=media': { status: 403, body: { error: { message: 'Quota exceeded for Queries per minute' } } }
  };
  const res = fakeRes();
  await handler({ method: 'GET', query: { op: 'pull' }, headers: {} }, res);
  eq(res.statusCode, 502, 'quota persistente → 502 honesto');
  ok(res.body.error.includes('revisions.json') || res.body.error.includes('Drive download'), 'erro claro');
  eq(fetchCalls.filter(c => c.url.includes('alt=media')).length, 3, 'retentou 3× (FDI_RETRY_WAITS=0,1,1)');
});

await Ta('5. pull com conteúdo de shape errado (mas HTTP 200) → 502 shape guard', async () => {
  fetchCalls = [];
  routes = {
    'oauth2.googleapis.com': { body: { access_token: 'tok' } },
    'alt=media': { status: 200, body: '<html>virus scan warning</html>' }
  };
  const res = fakeRes();
  await handler({ method: 'GET', query: { op: 'pull' }, headers: {} }, res);
  eq(res.statusCode, 502, 'HTML no lugar de JSON → 502');
});

await Ta('6. pull feliz → ok + dados', async () => {
  fetchCalls = [];
  let n = 0;
  routes = {
    'oauth2.googleapis.com': { body: { access_token: 'tok' } },
    'alt=media': { status: 200, body: { cap1: { R1: { content: 'x' } } } }
  };
  // rules precisa ser array: stub distinto por fileId
  const res = fakeRes();
  routes = {
    'oauth2.googleapis.com': { body: { access_token: 'tok' } },
    'files/1_4bU2bc0o30lOOdN6REWjuAs6FxxE-Jh': { status: 200, body: { cap1: { R1: { content: 'x' } } } },
    'files/1QOgSBRc9UNfNFtKcKoFUuowH9SipYviF': { status: 200, body: ['regra A'] }
  };
  await handler({ method: 'GET', query: { op: 'pull' }, headers: {} }, res);
  eq(res.statusCode, 200);
  ok(res.body.ok && res.body.revisions.cap1.R1.content === 'x' && res.body.customRules[0] === 'regra A', 'dados íntegros');
});

// --- Reforço 2ª onda (quota no op=status): retry no status/token + cache 60s ---
const STATUS_ROTAS_FELIZ = () => ({
  'oauth2.googleapis.com': { body: { access_token: 'tok' } },
  'files/1MGdnx': { body: { id: '1MGdnx', name: 'novo livro' } },
  'files/1_4bU2': { body: { id: 'r', name: 'revisions.json', size: '5145', modifiedTime: '2026-08-07T14:28:39Z' } },
  'files/1QOgS': { body: { id: 'g', name: 'custom_rules.json', size: '184', modifiedTime: '2026-08-07T14:28:40Z' } },
  'files?q=': { body: { files: [{ name: 'livro_backup_20260807_040001.zip', modifiedTime: '2026-08-07T07:00:00Z' }] } }
});

await Ta('7. status feliz (nocache) → 200 + payload completo + 4 queries Drive', async () => {
  fetchCalls = []; routes = STATUS_ROTAS_FELIZ();
  const res = fakeRes();
  await handler({ method: 'GET', query: { op: 'status', nocache: '1' }, headers: {} }, res);
  eq(res.statusCode, 200);
  ok(res.body.ok && res.body.folder.name === 'novo livro', 'pasta certa');
  eq(res.body.revisions.size, '5145');
  eq(res.body.latestBackup.name, 'livro_backup_20260807_040001.zip');
  ok(!res.body.cached, 'resposta ao vivo não é cache');
  eq(fetchCalls.filter(c => c.url.includes('googleapis.com/drive')).length, 4, '4 queries Drive');
});

await Ta('8. status com quota na 1ª tentativa → retenta e 200 (status coberto pelo retry)', async () => {
  fetchCalls = [];
  let nFolder = 0;
  routes = STATUS_ROTAS_FELIZ();
  routes['files/1MGdnx'] = () => (++nFolder === 1
    ? { status: 403, body: { error: { message: 'Quota exceeded for quota metric Queries' } } }
    : { body: { id: '1MGdnx', name: 'novo livro' } });
  const res = fakeRes();
  await handler({ method: 'GET', query: { op: 'status', nocache: '1' }, headers: {} }, res);
  eq(res.statusCode, 200);
  eq(res.body.folder.name, 'novo livro');
  eq(nFolder, 2, '1ª tentativa quota + 2ª ok');
});

await Ta('9. status com quota persistente → 502 honesto + quotaCongested (sem pânico de env var)', async () => {
  fetchCalls = [];
  routes = {
    'oauth2.googleapis.com': { body: { access_token: 'tok' } },
    'googleapis.com/drive': { status: 403, body: { error: { message: 'Quota exceeded for quota metric Queries per minute' } } }
  };
  const res = fakeRes();
  await handler({ method: 'GET', query: { op: 'status', nocache: '1' }, headers: {} }, res);
  eq(res.statusCode, 502);
  eq(res.body.quotaCongested, true, 'flag de congestionamento p/ o cliente');
  eq(fetchCalls.filter(c => c.url.includes('files/1MGdnx')).length, 3, 'retentou 3× (FDI_RETRY_WAITS=0,1,1)');
});

await Ta('10. cache 60s do status: 2ª chamada não gasta quota; nocache força leitura viva', async () => {
  fetchCalls = []; routes = STATUS_ROTAS_FELIZ();
  const r1 = fakeRes();
  await handler({ method: 'GET', query: { op: 'status', nocache: '1' }, headers: {} }, r1);
  eq(r1.statusCode, 200);
  const n1 = fetchCalls.length;
  const r2 = fakeRes();
  await handler({ method: 'GET', query: { op: 'status' }, headers: {} }, r2);
  eq(r2.statusCode, 200);
  eq(r2.body.cached, true, 'marca de cache');
  eq(r2.body.folder.name, 'novo livro', 'dados do cache íntegros');
  eq(fetchCalls.length, n1, '2ª chamada: ZERO novas chamadas de rede (economia de quota)');
  const r3 = fakeRes();
  await handler({ method: 'GET', query: { op: 'status', nocache: '1' }, headers: {} }, r3);
  ok(fetchCalls.length > n1, 'nocache força leitura ao vivo');
});

await Ta('11. token OAuth com rate-limit → retenta e consegue (getDriveToken no retry)', async () => {
  fetchCalls = [];
  let nTok = 0;
  routes = STATUS_ROTAS_FELIZ();
  routes['oauth2.googleapis.com'] = () => (++nTok === 1
    ? { status: 429, body: { error: 'rate_limit_exceeded', error_description: 'Rate limit exceeded' } }
    : { body: { access_token: 'tok' } });
  const res = fakeRes();
  await handler({ method: 'GET', query: { op: 'status', nocache: '1' }, headers: {} }, res);
  eq(res.statusCode, 200);
  eq(nTok, 2, 'token retentado');
});

// ---- Reforço 2 (incidente 2, mesmo dia): push sem conteúdo é RECUSADO ----
// O fallback antigo (`body.revisions || {}`) deixava payload SEM o campo cair
// como `{}` e o shape-guard aprovava VACUAMENTE — um teste com chave certa
// chegou a gravar `{}` (2 bytes) por cima do revisions.json real no Drive.
await Ta('12. push com chave + body SEM revisions (caso real do incidente) → 400, nada gravado', async () => {
  fetchCalls = [];
  routes = { 'oauth2.googleapis.com': { body: { access_token: 'tok' } } };
  const res = fakeRes();
  await handler({ method: 'POST', query: { op: 'push' }, headers: { 'x-sync-key': 'chave-teste' },
    body: { lixo: 'proposital' } }, res);
  eq(res.statusCode, 400, 'push sem revisions tem que ser recusado');
  ok(res.body.error.includes('ausente ou vazio'), 'mensagem de recusa ausente');
  ok(!fetchCalls.some(c => c.url.includes('upload/drive')), 'NÃO pode gravar no Drive');
  ok(!fetchCalls.some(c => c.url.includes('/copy')), 'NÃO pode tirar snapshot');
  ok(!fetchCalls.some(c => c.url.includes('api.github.com')), 'NÃO pode gravar no GitHub');
});

await Ta('13. push com chave + revisions {} vazio → 400 (shape-guard não passa mais vacuamente)', async () => {
  fetchCalls = [];
  routes = { 'oauth2.googleapis.com': { body: { access_token: 'tok' } } };
  const res = fakeRes();
  await handler({ method: 'POST', query: { op: 'push' }, headers: { 'x-sync-key': 'chave-teste' },
    body: { revisions: {}, customRules: [] } }, res);
  eq(res.statusCode, 400, '{} vazio tem que ser recusado');
  ok(!fetchCalls.some(c => c.url.includes('upload/drive')), 'NÃO pode gravar no Drive');
});

console.log(results.join('\n'));
const fails = (results.join('').match(/❌/g) || []).length;
console.log('---');
console.log(fails === 0 ? `✅ TODOS OS ${results.length} TESTES PASSARAM` : `❌ ${fails}/${results.length} FALHARAM`);
process.exit(fails ? 1 : 0);
