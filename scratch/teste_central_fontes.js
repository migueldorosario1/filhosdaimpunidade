const fs = require('fs');
const lines = fs.readFileSync('index.html', 'utf8').split('\n');
// localiza o bloco principal: o ÚLTIMO <script> simples (sem src) antes de </body>
const startLine = lines.findIndex(l => l.trim() === '<script>' && lines[lines.indexOf(l) - 1] !== undefined && true);
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
const customCheckboxes = [];
global.customCheckboxes = customCheckboxes;
global.__store = store;
function makeEl(id) {
  return {
    id, innerHTML: '', value: '', checked: false, textContent: '', className: '',
    classList: {
      _s: new Set(['modal-database', 'fontes-subpanel', 'add-source-panel', 'as-new-category'].includes(id) ? ['hidden'] : []),
      add(c) { this._s.add(c); }, remove(c) { this._s.delete(c); },
      toggle(c, f) { if (f === undefined) { this._s.has(c) ? this._s.delete(c) : this._s.add(c); } else if (f) this._s.add(c); else this._s.delete(c); },
      contains(c) { return this._s.has(c); }
    },
    querySelectorAll: () => [], appendChild: () => {}, focus: () => {},
    getAttribute: () => null, setAttribute: () => {}
  };
}
global.document = {
  getElementById: id => (elements[id] = elements[id] || makeEl(id)),
  querySelectorAll: sel => (sel === '.chk-fonte-custom' || sel === '.chk-fonte-parte, .chk-fonte-custom') ? customCheckboxes : [],
  querySelector: () => null,
  createElement: () => makeEl('tmp'), addEventListener: () => {}, body: makeEl('body')
};
global.window = { addEventListener: () => {} };
global.localStorage = {
  getItem: k => (k in store ? store[k] : null),
  setItem: (k, v) => { store[k] = String(v); },
  removeItem: k => { delete store[k]; },
  key: i => Object.keys(store)[i],
  get length() { return Object.keys(store).length; }
};
global.navigator = { clipboard: { writeText: async () => {} } };
global.alert = () => {};
global.confirm = () => true;
global.marked = { parse: s => s };
global.fetch = async () => ({ ok: false, json: async () => ({}) });

const test = code + fs.readFileSync('scratch/_snippet.js', 'utf8');
(async () => {
  try {
    const r = await new Function('return (async () => {' + test + '})()')();
    console.log(r);
  } catch (e) { console.log('❌ ERRO:', e.message); console.log(e.stack.split('\n').slice(0, 4).join('\n')); process.exit(1); }
})();
