// Teste Node DOM-stub — Task 3 "Roteiro + Livro Inteiro" (Kimi K3, 2026-08-07)
// Pedidos do Miguel: anotações com Ver/Editar/Apagar, editar roteiro, Ler vs
// Compilar separados, editar livro inteiro, Estúdio (não auto-revisão),
// contraste do card compilado (.fdi-ui), Baixar respeitando edição manual.
// Mesmo harness de teste_upload_versao.js.
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
function __makeEl(id) {
  return {
    id, innerHTML: '', value: '', checked: false, textContent: '', className: '', title: '',
    dataset: {}, style: {},
    classList: {
      _s: new Set(['modal-editar-roteiro', 'modal-editar-livro'].includes(id) ? ['hidden'] : []),
      add(c) { this._s.add(c); }, remove(c) { this._s.delete(c); },
      toggle(c, f) { if (f === undefined) { this._s.has(c) ? this._s.delete(c) : this._s.add(c); } else if (f) this._s.add(c); else this._s.delete(c); },
      contains(c) { return this._s.has(c); }
    },
    querySelectorAll: () => [], querySelector: () => __makeEl('qs-tmp'), appendChild: () => {}, removeChild: () => {},
    remove: () => {}, focus: () => {}, scrollIntoView: () => {}, click: () => {},
    getAttribute: () => null, setAttribute: () => {}, onclick: null
  };
}
global.document = {
  getElementById: id => (elements[id] = elements[id] || __makeEl(id)),
  querySelectorAll: () => [],
  querySelector: () => null,
  createElement: () => __makeEl('tmp'), addEventListener: () => {}, body: __makeEl('body')
};
global.window = { addEventListener: () => {}, location: { hash: '' }, scrollTo: () => {} };
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
global.confirm = () => { throw new Error('confirm() não deveria ser usado (suprimido em webviews)'); };
global.marked = { parse: s => s };
global.fetch = async () => ({ ok: false, json: async () => ({}) });
global.requestAnimationFrame = () => {};
global.__elements = elements;
global.__store = store;
global.__makeEl = __makeEl;

const snippet = `
// ================= TESTES: ROTEIRO + LIVRO INTEIRO =================
const __results = [];
function __T(name, fn) { try { fn(); __results.push('✅ ' + name); } catch(e) { __results.push('❌ ' + name + ' — ' + e.message); } }
function __eq(a, b, msg) { if (a !== b) throw new Error((msg ? msg + ': ' : '') + 'esperado=' + JSON.stringify(b) + ' obtido=' + JSON.stringify(a)); }
function __ok(v, msg) { if (!v) throw new Error(msg || 'asserção falhou'); }

// Captura de downloads (Blob + link)
let __blobs = [], __downloadNames = [];
global.Blob = class { constructor(parts, opts) { this.content = (parts || []).join(''); this.type = opts && opts.type; } };
global.URL = { createObjectURL: b => { __blobs.push(b); return 'blob:fake_' + __blobs.length; } };
const __origCreate = document.createElement;
document.createElement = tag => {
  const el = __makeEl('dl-' + tag);
  const origSet = el.setAttribute;
  el.setAttribute = (k, v) => { if (k === 'download') __downloadNames.push(v); origSet(k, v); };
  return el;
};

const ANOT_KEY = 'miguel_roteiro_anotacoes_v1';
const EDIT_LIVRO_KEY = () => 'miguel_fullbook_manual_edit_' + currentVolume;
const EDIT_LIVRO_TS = () => 'miguel_fullbook_manual_edit_ts_' + currentVolume;
const ROT_KEY = () => 'miguel_roteiro_texto_override_' + currentVolume;

function __seed() {
  Object.keys(__store).forEach(k => delete __store[k]);
  window._roteiroEditingId = null;
  currentVolume = 'vol1_v7';
  currentChapterKey = '00_frontmatter';
  currentVersionKey = 'oficial';
  currentViewMode = 'single';
  __blobs = []; __downloadNames = [];
}

// ---------- ANOTAÇÕES (Ver / Editar / Apagar) ----------
__T('1. migração: caixa antiga vira a 1ª anotação (nada se perde)', () => {
  __seed();
  localStorage.setItem('miguel_roteiro_observacoes', 'texto antigo do Miguel');
  const list = loadRoteiroAnotacoes();
  __eq(list.length, 1, 'deveria ter migrado 1 anotação');
  __ok(list[0].migrada === true, 'flag migrada ausente');
  __eq(list[0].text, 'texto antigo do Miguel');
  __eq(localStorage.getItem('miguel_roteiro_anotacoes_migrada'), '1', 'flag de migração única ausente');
});

__T('2. salvar cria NOVA anotação na lista (não sobrescreve)', () => {
  __seed();
  document.getElementById('roteiro-obs-textarea').value = 'primeira anotação';
  saveRoteiroObs();
  document.getElementById('roteiro-obs-textarea').value = 'segunda anotação';
  saveRoteiroObs();
  const list = loadRoteiroAnotacoes();
  __eq(list.length, 2, 'duas anotações distintas');
  __eq(list[1].text, 'segunda anotação');
});

__T('3. anotação vazia não salva', () => {
  __seed();
  document.getElementById('roteiro-obs-textarea').value = '   ';
  saveRoteiroObs();
  __eq(loadRoteiroAnotacoes().length, 0);
});

__T('4. Editar: carrega a anotação na caixa e Salvar Edição atualiza a mesma (não cria nova)', () => {
  __seed();
  document.getElementById('roteiro-obs-textarea').value = 'anotação original';
  saveRoteiroObs();
  const id = loadRoteiroAnotacoes()[0].id;
  editRoteiroAnotacao(id);
  __eq(window._roteiroEditingId, id, 'modo edição não ativado');
  __eq(document.getElementById('roteiro-obs-textarea').value, 'anotação original', 'caixa não carregou o texto');
  document.getElementById('roteiro-obs-textarea').value = 'anotação corrigida';
  saveRoteiroObs();
  const list = loadRoteiroAnotacoes();
  __eq(list.length, 1, 'editar não pode criar duplicata');
  __eq(list[0].text, 'anotação corrigida');
  __ok(list[0].editada === true, 'flag editada ausente');
  __eq(window._roteiroEditingId, null, 'modo edição não encerrou');
});

__T('5. Apagar em 2 toques: 1º arma o botão, 2º apaga', () => {
  __seed();
  document.getElementById('roteiro-obs-textarea').value = 'para apagar';
  saveRoteiroObs();
  const id = loadRoteiroAnotacoes()[0].id;
  const btn = __makeEl('btn-del');
  btn.innerHTML = '🗑️ Apagar';
  deleteRoteiroAnotacao(id, btn);
  __eq(loadRoteiroAnotacoes().length, 1, '1º toque não pode apagar');
  __eq(btn.dataset.confirming, '1', 'botão não foi armado');
  deleteRoteiroAnotacao(id, btn);
  __eq(loadRoteiroAnotacoes().length, 0, '2º toque deveria apagar');
});

__T('6. Cancelar edição limpa o modo edição', () => {
  __seed();
  document.getElementById('roteiro-obs-textarea').value = 'x';
  saveRoteiroObs();
  editRoteiroAnotacao(loadRoteiroAnotacoes()[0].id);
  cancelRoteiroAnotacaoEdit();
  __eq(window._roteiroEditingId, null);
});

// ---------- EDITAR ROTEIRO ----------
__T('7. getRoteiroText: sem override retorna o frontmatter original', () => {
  __seed();
  const orig = getCurrentVolumeDataset()['00_frontmatter'].mainContent;
  __ok(orig && orig.length > 100, 'frontmatter original existe no dataset');
  __eq(getRoteiroText(), orig);
});

__T('8. salvar edição do roteiro cria override + ts e passa a valer', () => {
  __seed();
  openEditarRoteiroModal();
  __ok(!document.getElementById('modal-editar-roteiro').classList.contains('hidden'), 'modal não abriu');
  document.getElementById('editar-roteiro-text').value = '# ROTEIRO EDITADO PELO MIGUEL';
  saveRoteiroTexto();
  __eq(getRoteiroText(), '# ROTEIRO EDITADO PELO MIGUEL');
  __ok(!!localStorage.getItem('miguel_roteiro_texto_override_ts_' + currentVolume), 'ts da edição ausente');
  __ok(document.getElementById('modal-editar-roteiro').classList.contains('hidden'), 'modal não fechou');
});

__T('9. roteiro vazio não salva', () => {
  __seed();
  document.getElementById('editar-roteiro-text').value = '   ';
  saveRoteiroTexto();
  __eq(localStorage.getItem(ROT_KEY()), null);
});

__T('10. Restaurar Original em 2 toques descarta o override', () => {
  __seed();
  localStorage.setItem(ROT_KEY(), 'edição qualquer');
  localStorage.setItem('miguel_roteiro_texto_override_ts_' + currentVolume, new Date().toISOString());
  const btn = __makeEl('btn-rest');
  restoreRoteiroTexto(btn);
  __ok(localStorage.getItem(ROT_KEY()) === 'edição qualquer', '1º toque não pode restaurar');
  restoreRoteiroTexto(btn);
  __eq(localStorage.getItem(ROT_KEY()), null, 'override deveria ser removido');
  __eq(getRoteiroText(), getCurrentVolumeDataset()['00_frontmatter'].mainContent);
});

// ---------- LIVRO INTEIRO (editar / compilar / baixar) ----------
__T('11. sem edição manual: exibição = compilação canônica', () => {
  __seed();
  const disp = getFullBookDisplayText();
  __eq(disp.edited, false);
  __ok(disp.text.includes('CAPÍTULO'), 'compilação deveria conter capítulos');
});

__T('12. Editar Livro Inteiro: override fica na frente, banner/ts registrados', () => {
  __seed();
  openEditarLivroModal();
  __ok(!document.getElementById('modal-editar-livro').classList.contains('hidden'), 'modal não abriu');
  __ok(document.getElementById('editar-livro-text').value.includes('CAPÍTULO'), 'modal deveria carregar o texto exibido');
  document.getElementById('editar-livro-text').value = 'LIVRO COM EDIÇÃO MANUAL DO MIGUEL';
  saveLivroEditado();
  const disp = getFullBookDisplayText();
  __eq(disp.edited, true);
  __eq(disp.text, 'LIVRO COM EDIÇÃO MANUAL DO MIGUEL');
  __ok(!!disp.ts, 'ts ausente');
});

__T('13. livro vazio não salva', () => {
  __seed();
  document.getElementById('editar-livro-text').value = '';
  saveLivroEditado();
  __eq(localStorage.getItem(EDIT_LIVRO_KEY()), null);
});

__T('14. Voltar à compilação (descartar edição) em 2 toques', () => {
  __seed();
  localStorage.setItem(EDIT_LIVRO_KEY(), 'edição');
  localStorage.setItem(EDIT_LIVRO_TS(), new Date().toISOString());
  const btn = __makeEl('btn-disc');
  discardFullBookEdit(btn);
  __ok(localStorage.getItem(EDIT_LIVRO_KEY()) === 'edição', '1º toque não pode descartar');
  discardFullBookEdit(btn);
  __eq(getFullBookDisplayText().edited, false, 'edição deveria ser descartada');
});

__T('15. ⚡ Atualizar Compilação SEM edição: recompile direto', () => {
  __seed();
  atualizarCompilacao(__makeEl('btn-atualiza'));
  __eq(currentChapterKey, 'full_book', 'deveria abrir o livro inteiro');
  __eq(getFullBookDisplayText().edited, false);
});

__T('16. ⚡ Atualizar Compilação COM edição: 2 toques (1º preserva, 2º descarta e recompila)', () => {
  __seed();
  localStorage.setItem(EDIT_LIVRO_KEY(), 'edição ativa');
  localStorage.setItem(EDIT_LIVRO_TS(), new Date().toISOString());
  const btn = __makeEl('btn-atualiza2');
  atualizarCompilacao(btn);
  __ok(localStorage.getItem(EDIT_LIVRO_KEY()) === 'edição ativa', '1º toque não pode descartar a edição');
  __eq(btn.dataset.confirming, '1', 'botão não foi armado');
  atualizarCompilacao(btn);
  __eq(localStorage.getItem(EDIT_LIVRO_KEY()), null, '2º toque deveria descartar a edição');
  __eq(currentChapterKey, 'full_book');
});

__T('17. Baixar Livro Inteiro baixa o texto EXIBIDO (edição → sufixo _editado)', () => {
  __seed();
  downloadFullBook();
  __ok(__blobs[0].content.includes('CAPÍTULO'), 'sem edição: baixa compilação');
  __ok(!__downloadNames[0].includes('_editado'), 'nome sem sufixo quando canônico');
  __blobs = []; __downloadNames = [];
  localStorage.setItem(EDIT_LIVRO_KEY(), 'texto editado para baixar');
  localStorage.setItem(EDIT_LIVRO_TS(), new Date().toISOString());
  downloadFullBook();
  __eq(__blobs[0].content, 'texto editado para baixar', 'com edição: baixa a edição');
  __ok(__downloadNames[0].includes('_editado'), 'nome deveria ter _editado');
});

__T('18. Baixar Roteiro baixa getRoteiroText (com override quando editado)', () => {
  __seed();
  downloadRoteiro();
  __eq(__blobs[0].content, getCurrentVolumeDataset()['00_frontmatter'].mainContent);
  __blobs = []; __downloadNames = [];
  localStorage.setItem(ROT_KEY(), 'roteiro editado');
  downloadRoteiro();
  __eq(__blobs[0].content, 'roteiro editado');
});

// ---------- FONTE (HTML/CSS) ----------
__T('19. fonte: Ler e Compilar separados — barra de topo vira "📖 Ler Livro Inteiro"', () => {
  __ok(__SOURCE__.includes('<span>📖 Ler Livro Inteiro</span>'), 'botão da barra de topo não renomeado');
  __ok(!__SOURCE__.includes('Ler / Compilar'), 'botão combinado ainda existe');
});

__T('20. fonte: capa do compilado tem Baixar | Atualizar Compilação | Editar Livro | Estúdio', () => {
  __ok(__SOURCE__.includes('📥 Baixar Livro Inteiro (.md)'), 'baixar ausente');
  __ok(__SOURCE__.includes('⚡ Atualizar Compilação'), 'atualizar ausente');
  __ok(__SOURCE__.includes('✏️ Editar Livro Inteiro'), 'editar livro ausente');
  __ok(__SOURCE__.includes('🎬 Estúdio do Livro Inteiro'), 'estúdio ausente');
  __ok(__SOURCE__.includes('atualizarCompilacao(this)'), 'atualizar não usa 2 toques');
});

__T('21. fonte: anotações têm 👁️ Ver / ✏️ Editar / 🗑️ Apagar', () => {
  __ok(__SOURCE__.includes("viewRoteiroAnotacao('"), 'Ver ausente');
  __ok(__SOURCE__.includes("editRoteiroAnotacao('"), 'Editar ausente');
  __ok(__SOURCE__.includes("deleteRoteiroAnotacao('"), 'Apagar ausente');
});

__T('22. fonte: contraste — cards de UI usam .fdi-ui + CSS anula .prose-book', () => {
  __ok(__SOURCE__.includes('.prose-book .fdi-ui h1'), 'CSS .fdi-ui ausente');
  __ok(__SOURCE__.includes('class="fdi-ui bg-gradient-to-r from-amber-600'), 'card do compilado sem fdi-ui');
  __ok(__SOURCE__.includes('class="fdi-ui bg-gradient-to-r from-slate-900'), 'header do roteiro sem fdi-ui');
});

__T('23. fonte: Estúdio do livro NUNCA revisa sozinho (abre o estúdio)', () => {
  __ok(__SOURCE__.includes('triggerAiAuditWithTokenWarning()'), 'botão do estúdio ausente');
  __ok(__SOURCE__.includes('não revisa sozinho'), 'tooltip de não-auto-revisão ausente');
  __ok(__SOURCE__.includes('Abrir Estúdio para Revisar Livro Inteiro'), 'modal de alerta do estúdio ausente');
});

__T('24. fonte: modais editar-roteiro e editar-livro existem', () => {
  __ok(__SOURCE__.includes('id="modal-editar-roteiro"'), 'modal roteiro ausente');
  __ok(__SOURCE__.includes('id="modal-editar-livro"'), 'modal livro ausente');
  __ok(__SOURCE__.includes('id="editar-livro-text"'), 'textarea do livro ausente');
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
