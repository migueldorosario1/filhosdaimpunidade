const fs = require('fs');
const lines = fs.readFileSync('index.html', 'utf8').split('\n');
const code = lines.slice(1237, 6400).join('\n');
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
try { console.log(new Function(test)()); } catch (e) { console.log('❌ ERRO:', e.message); console.log(e.stack.split('\n').slice(0, 4).join('\n')); }
