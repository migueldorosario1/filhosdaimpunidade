// Teste server-side do api/drive.js (Kimi K3, 2026-08-07)
// Importa o handler ESM real e dirige req/res falsos + fetch stubado.
// Foco: guardas anti-incidente (shape validation, auth, retry de quota).
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
  const r = key ? routes[key] : { status: 404, body: { erro: 'rota não stubada: ' + url } };
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

console.log(results.join('\n'));
const fails = (results.join('').match(/❌/g) || []).length;
console.log('---');
console.log(fails === 0 ? `✅ TODOS OS ${results.length} TESTES PASSARAM` : `❌ ${fails}/${results.length} FALHARAM`);
process.exit(fails ? 1 : 0);
