// Teste Node DOM-stub — feature "Renomear Versão" (K3, 2026-08-07)
// Pedido do Miguel: "Tem que ter o comando para mudar o nome. Botei o nome
// errado, está Gemini 3.6." Mesmo harness de teste_upload_versao.js: extrai o
// bloco <script> principal do index.html, roda com stubs e executa asserções.
const fs = require('fs');
const lines = fs.readFileSync('index.html', 'utf8').split('\n');
let scriptStart = -1, scriptEnd = -1;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].trim() === '<script>') scriptStart = i; // fica com o último
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
    dataset: {},
    classList: {
      _s: new Set(),
      add(c) { this._s.add(c); }, remove(c) { this._s.delete(c); },
      toggle(c, f) { if (f === undefined) { this._s.has(c) ? this._s.delete(c) : this._s.add(c); } else if (f) this._s.add(c); else this._s.delete(c); },
      contains(c) { return this._s.has(c); }
    },
    querySelectorAll: () => [], querySelector: () => makeEl('qs-tmp'), appendChild: () => {},
    insertBefore: () => {}, focus: () => {}, select: () => {},
    getAttribute: () => null, setAttribute: () => {}, onclick: null, firstChild: null
  };
}
global.document = {
  getElementById: id => (elements[id] = elements[id] || makeEl(id)),
  querySelectorAll: () => [],
  querySelector: () => null,
  createElement: () => makeEl('tmp'), addEventListener: () => {}, body: makeEl('body')
};
global.window = { addEventListener: () => {}, location: { hash: '' } };
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
global.fetch = async () => ({ ok: false, json: async () => ({}) });
global.__store = store;

const snippet = `
// ================= TESTES: RENOMEAR VERSÃO =================
const __results = [];
function __T(name, fn) { try { fn(); __results.push('✅ ' + name); } catch(e) { __results.push('❌ ' + name + ' — ' + e.message); } }
function __eq(a, b, msg) { if (a !== b) throw new Error((msg ? msg + ': ' : '') + 'esperado=' + JSON.stringify(b) + ' obtido=' + JSON.stringify(a)); }
function __ok(v, msg) { if (!v) throw new Error(msg || 'asserção falhou'); }

const REV_KEY = 'miguel_book_revisions_vol1_v7_01_estarei_vingado';
function __seed() {
  Object.keys(__store).forEach(k => delete __store[k]);
  currentVolume = 'vol1_v7';
  currentChapterKey = '01_estarei_vingado';
  currentVersionKey = 'R33';
  currentViewMode = 'single';
  versionRenamingKey = null;
  localStorage.setItem(REV_KEY, JSON.stringify({
    R32: { versionTag: 'R32 (Kimi)', content: 'texto trinta e dois' },
    R33: { versionTag: 'R33 (upload: Gemini 3.6)', content: 'texto trinta e três' }
  }));
  const inp = document.getElementById('version-rename-input');
  inp.value = '';
}
function __revs() { return JSON.parse(__store[REV_KEY]); }
function __edit(newLabel) { document.getElementById('version-rename-input').value = newLabel; }

__T('1. renomear troca só o rótulo (o caso real do Miguel: "Gemini 3.6" errado)', () => {
  __seed();
  startRenameVersion('R33');
  __eq(versionRenamingKey, 'R33', 'estado de edição armado');
  __edit('R33 (upload: Gemini 2.5 Pro)');
  confirmRenameVersion('R33');
  const revs = __revs();
  __eq(revs.R33.versionTag, 'R33 (upload: Gemini 2.5 Pro)');
  __eq(revs.R33.content, 'texto trinta e três', 'texto intacto');
  __ok(revs.R32, 'R32 intacta');
  __eq(versionRenamingKey, null, 'estado limpo após confirmar');
  __eq(getVersionLabelForKey(currentChapterKey, 'R33'), 'R33 (upload: Gemini 2.5 Pro)', 'rótulo do histórico acompanha');
});

__T('2. nome vazio cancela sem gravar', () => {
  __seed();
  startRenameVersion('R33');
  __edit('   ');
  confirmRenameVersion('R33');
  __eq(__revs().R33.versionTag, 'R33 (upload: Gemini 3.6)', 'nada mudou');
});

__T('3. nome igual ao atual não regrava (no-op limpo)', () => {
  __seed();
  const antes = __store[REV_KEY];
  startRenameVersion('R33');
  __edit('R33 (upload: Gemini 3.6)');
  confirmRenameVersion('R33');
  __eq(__store[REV_KEY], antes, 'store intocado');
});

__T('4. rótulo é truncado em 40 caracteres (mesmo teto do upload)', () => {
  __seed();
  startRenameVersion('R32');
  __edit('X'.repeat(60));
  confirmRenameVersion('R32');
  __eq(__revs().R32.versionTag.length, 40, 'teto de 40');
});

__T('5. versão CANÔNICA pode ser renomeada (ponteiro 👑 não muda)', () => {
  __seed();
  safeLocalSet(storageKeyVol('miguel_book_canonical', currentChapterKey), 'R33');
  startRenameVersion('R33');
  __edit('R33 (a boa)');
  confirmRenameVersion('R33');
  __eq(__revs().R33.versionTag, 'R33 (a boa)');
  __eq(getCanonicalVersionKey(currentChapterKey), 'R33', 'canônica continua a mesma versão');
});

__T('6. falha de quota no localStorage NÃO grava', () => {
  __seed();
  const origSet = localStorage.setItem;
  startRenameVersion('R33');
  __edit('nome novo');
  localStorage.setItem = () => { const e = new Error('quota'); e.name = 'QuotaExceededError'; throw e; };
  confirmRenameVersion('R33');
  localStorage.setItem = origSet;
  __eq(__revs().R33.versionTag, 'R33 (upload: Gemini 3.6)', 'quota: nada gravado');
});

__T('7. cancelar restaura sem gravar', () => {
  __seed();
  startRenameVersion('R33');
  __edit('desisto');
  cancelRenameVersion();
  __eq(__revs().R33.versionTag, 'R33 (upload: Gemini 3.6)', 'nada mudou');
  __eq(versionRenamingKey, null, 'estado limpo');
});

__T('8. renomear versão sem rótulo anterior usa a chave R# como base', () => {
  __seed();
  const revs = __revs();
  delete revs.R32.versionTag;
  localStorage.setItem(REV_KEY, JSON.stringify(revs));
  startRenameVersion('R32');
  __edit('R32 revisada pela Sônia');
  confirmRenameVersion('R32');
  __eq(__revs().R32.versionTag, 'R32 revisada pela Sônia');
  __eq(getVersionLabelForKey(currentChapterKey, 'R32'), 'R32 revisada pela Sônia');
});

// ---- checagens de fonte (fiação da UI no index.html) ----
const __src = (typeof __SOURCE__ !== 'undefined') ? __SOURCE__ : '';
__T('9. fonte: input inline id="version-rename-input" com teto 40', () => {
  __ok(__src.includes('id="version-rename-input"'), 'input ausente');
  __ok(__src.includes('maxlength="40"'), 'teto 40 ausente');
});
__T('10. fonte: botão ✏️ chama startRenameVersion na linha da revisão', () => {
  __ok(__src.includes('startRenameVersion(v.key)'), '✏️ não ligado à linha');
  __ok(__src.includes('Renomear a versão'), 'title do ✏️ ausente');
});
__T('11. fonte: Enter salva / Esc cancela no input', () => {
  __ok(__src.includes("if (ev.key === 'Enter') { ev.preventDefault(); confirmRenameVersion(v.key); }"), 'Enter ausente');
  __ok(__src.includes("if (ev.key === 'Escape') cancelRenameVersion()"), 'Esc ausente');
});
__T('12. fonte: loadChapter fecha edição pendente (anti-vazamento entre capítulos)', () => {
  __ok(/function loadChapter\\(chapKey\\) \\{\\s*\\n\\s*versionRenamingKey = null;/.test(__src), 'reset no loadChapter ausente');
});

return __results.join('\\n');
`;

const test = 'const __SOURCE__ = ' + JSON.stringify(fs.readFileSync('index.html', 'utf8')) + ';\nconst __store = ' + 'global.__store_dummy;\n' + code + snippet;
// expõe o store real para dentro da Function
global.__store_dummy = store;
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
