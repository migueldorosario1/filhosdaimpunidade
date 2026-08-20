// Teste Node DOM-stub — feature "Subir Nova Versão" (Kimi K3, 2026-08-07)
// Padrão do repo (mesmo harness de teste_central_fontes.js): extrai o bloco
// <script> principal do index.html, roda com stubs e executa asserções ao final.
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
      _s: new Set(id === 'modal-upload-version' ? ['hidden'] : []),
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
global.__elements = elements;
global.__store = store;

const snippet = `
// ================= TESTES: SUBIR NOVA VERSÃO =================
const __results = [];
function __T(name, fn) { try { fn(); __results.push('✅ ' + name); } catch(e) { __results.push('❌ ' + name + ' — ' + e.message); } }
function __eq(a, b, msg) { if (a !== b) throw new Error((msg ? msg + ': ' : '') + 'esperado=' + JSON.stringify(b) + ' obtido=' + JSON.stringify(a)); }
function __ok(v, msg) { if (!v) throw new Error(msg || 'asserção falhou'); }

const REV_KEY = 'miguel_book_revisions_vol1_v7_01_estarei_vingado';
function __seed() {
  Object.keys(__store).forEach(k => delete __store[k]);
  currentVolume = 'vol1_v7';
  currentChapterKey = '01_estarei_vingado';
  currentVersionKey = 'oficial';
  currentViewMode = 'single'; // global implícito do app (criado por setMode no boot real)
  localStorage.setItem(REV_KEY, JSON.stringify({
    R1: { versionTag: 'R1 (deepseek)', content: 'texto um' },
    R2: { versionTag: 'R2 (manual)', content: 'texto dois' }
  }));
  ['upload-version-text','upload-version-label','upload-version-file-info'].forEach(id => { const el = document.getElementById(id); el.value=''; el.textContent=''; });
  document.getElementById('modal-upload-version').classList.add('hidden');
}

__T('1. modal abre no capítulo e anuncia o próximo R# (R3)', () => {
  __seed();
  openUploadVersionModal();
  __ok(!document.getElementById('modal-upload-version').classList.contains('hidden'), 'modal não abriu');
  __eq(document.getElementById('upload-version-nextr').textContent, 'R3');
  __ok(document.getElementById('upload-version-subtitle').textContent.includes('ESTAREI VINGADO'), 'subtitle sem nome do capítulo');
});

__T('2. gravar texto colado → vira R3 (upload), versão ativa, nome do capítulo intacto', () => {
  __seed();
  openUploadVersionModal();
  document.getElementById('upload-version-text').value = '# CAPÍTULO 1 — ESTAREI VINGADO\\n\\nTexto inteiramente novo.';
  saveUploadedVersion(document.getElementById('btn-tmp'));
  const revs = JSON.parse(__store[REV_KEY]);
  __eq(Object.keys(revs).length, 3, 'tinha 2, tem que ter 3');
  __eq(revs.R3.versionTag, 'R3 (upload)');
  __eq(revs.R3.content, '# CAPÍTULO 1 — ESTAREI VINGADO\\n\\nTexto inteiramente novo.');
  __eq(revs.R3.engineSlug, 'upload');
  __eq(currentVersionKey, 'R3', 'versão nova deve virar a ativa');
  __ok(document.getElementById('modal-upload-version').classList.contains('hidden'), 'modal não fechou');
  __eq(revs.R1.content, 'texto um', 'R1 intacta');
  __eq(revs.R2.content, 'texto dois', 'R2 intacta');
});

__T('3. rótulo opcional entra no versionTag', () => {
  __seed();
  openUploadVersionModal();
  document.getElementById('upload-version-text').value = 'texto novo';
  document.getElementById('upload-version-label').value = 'Sônia';
  saveUploadedVersion(null);
  const revs = JSON.parse(__store[REV_KEY]);
  __eq(revs.R3.versionTag, 'R3 (upload: Sônia)');
});

__T('4. texto vazio NÃO grava nada', () => {
  __seed();
  openUploadVersionModal();
  document.getElementById('upload-version-text').value = '   ';
  saveUploadedVersion(null);
  const revs = JSON.parse(__store[REV_KEY]);
  __eq(Object.keys(revs).length, 2, 'nada devia ter mudado');
});

__T('5. full_book/frontmatter são bloqueados (abrir e gravar)', () => {
  __seed();
  currentChapterKey = 'full_book';
  openUploadVersionModal();
  __ok(document.getElementById('modal-upload-version').classList.contains('hidden'), 'modal não devia abrir no full_book');
  document.getElementById('upload-version-text').value = 'qualquer coisa';
  saveUploadedVersion(null);
  __eq(__store['miguel_book_revisions_vol1_v7_full_book'], undefined, 'não pode gravar revisão em full_book');
});

__T('6. anti-colisão: R2 apagada, próxima sobe como R4 (máximo+1)', () => {
  __seed();
  const revs = JSON.parse(__store[REV_KEY]);
  delete revs.R2;
  revs.R3 = { versionTag: 'R3 (x)', content: 'tres' };
  localStorage.setItem(REV_KEY, JSON.stringify(revs));
  openUploadVersionModal();
  document.getElementById('upload-version-text').value = 'quatro';
  saveUploadedVersion(null);
  const after = JSON.parse(__store[REV_KEY]);
  __ok(after.R4, 'R4 devia existir');
  __eq(after.R4.versionTag, 'R4 (upload)');
});

__T('7. canônica NÃO muda ao subir versão (verdade editorial preservada)', () => {
  __seed();
  const antes = getCanonicalVersionKey(currentChapterKey);
  openUploadVersionModal();
  document.getElementById('upload-version-text').value = 'texto novo';
  saveUploadedVersion(null);
  __eq(getCanonicalVersionKey(currentChapterKey), antes, 'ponteiro canônico não pode mudar');
});

__T('8. falha de quota → NÃO grava e avisa', () => {
  __seed();
  const origSet = localStorage.setItem;
  localStorage.setItem = () => { const e = new Error('quota'); e.name = 'QuotaExceededError'; throw e; };
  openUploadVersionModal();
  document.getElementById('upload-version-text').value = 'texto novo';
  saveUploadedVersion(null);
  localStorage.setItem = origSet;
  const revs = JSON.parse(__store[REV_KEY]);
  __eq(Object.keys(revs).length, 2, 'quota: nada gravado');
  __eq(currentVersionKey, 'oficial', 'versão ativa não pode mudar em falha');
});

__T('9. contador de caracteres acompanha o textarea', () => {
  __seed();
  const ta = document.getElementById('upload-version-text');
  ta.value = 'abcde';
  updateUploadVersionCharcount();
  __eq(document.getElementById('upload-version-charcount').textContent, '5 caracteres');
});

__T('10. versão nova aparece no rótulo do histórico', () => {
  __seed();
  openUploadVersionModal();
  document.getElementById('upload-version-text').value = 'texto novo';
  saveUploadedVersion(null);
  __eq(getVersionLabelForKey(currentChapterKey, 'R3'), 'R3 (upload)');
});

// ---- checagens de fonte (fiação da UI no index.html) ----
const __src = (typeof __SOURCE__ !== 'undefined') ? __SOURCE__ : '';
__T('11. fonte: modal existe no HTML', () => {
  __ok(__src.includes('id="modal-upload-version"'), 'modal-upload-version ausente');
});
__T('12. fonte: botão na barra de versões chama openUploadVersionModal', () => {
  __ok(__src.includes('⬆️ Subir Nova Versão'), 'botão da barra ausente');
});
__T('13. fonte: mini-botão ⬆️ Subir dentro do menu de versões', () => {
  __ok(__src.includes('⬆️ Subir</button>'), 'mini-botão do menu ausente');
});
__T('14. fonte: input de arquivo aceita .md/.txt/.pdf', () => {
  __ok(__src.includes('id="upload-version-file"') && __src.includes('accept=".md,.markdown,.txt,.pdf"'), 'input de arquivo ausente/errado');
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
