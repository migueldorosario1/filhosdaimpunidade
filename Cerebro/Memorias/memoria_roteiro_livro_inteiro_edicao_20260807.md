# 🧠 MEMÓRIA — ROTEIRO + LIVRO INTEIRO: ANOTAÇÕES CRUD, EDIÇÃO E SEPARAÇÃO LER/COMPILAR

**Data:** 2026-08-07 · **Agente:** ZCode/Kimi K3 · **Repo:** `filhosdaimpunidade` · **Commit:** `877f1f0` (main → Vercel produção)
**Fórum correspondente:** `Foruns/forum_roteiro_livro_inteiro_edicao_20260807.md`
**Escopo:** somente `index.html` + `scratch/teste_roteiro_livro_edit.js` (novo). Zero backend.

## 1. Contexto

Task 3 do dia no leitor FdI (tasks 1 e 2 já entregues no mesmo dia: subir nova versão `0ce3556` + sync Google Drive `6112560`/`efb9cfa`). O Miguel estava na página do roteiro (`#leitor?vol=vol1_v7&cap=00_frontmatter`) e listou 8 pedidos (transcrição por voz, ver fórum). Tudo é client-side/localStorage — o monólito continua sem backend para estas features.

## 2. Implementação (funções e chaves)

### 2.1 Anotações do roteiro (CRUD)
- **Storage:** `miguel_roteiro_anotacoes_v1` = JSON array de `{id, text, ts, migrada?, editada?, tsEdicao?}`; id = `'anot_' + Date.now().toString(36) + '_' + rand5`.
- **Funções novas:** `escapeHtml`, `fmtAnotacaoDate(ts)` (pt-BR), `loadRoteiroAnotacoes()` (c/ migração única da caixa antiga `miguel_roteiro_observacoes` → item `migrada:true`; flag `miguel_roteiro_anotacoes_migrada='1'`), `saveRoteiroAnotacoes(list)` (via `safeLocalSet` — quota), `saveRoteiroObs()` (reescrevida: cria OU atualiza `window._roteiroEditingId`), `viewRoteiroAnotacao(id)` (toggle `#anot-full-<id>`), `editRoteiroAnotacao(id)` (seta `_roteiroEditingId`, re-renderiza, carrega textarea + scrollIntoView), `cancelRoteiroAnotacaoEdit()`, `deleteRoteiroAnotacao(id, btnEl)` (2 toques; timeout 3,2s rearma o botão).
- **UI:** botão salvar muda de label conforme o modo (`💾 Salvar Anotação` / `💾 Salvar Edição`) + botão "✖️ Cancelar edição" aparece só no modo edição.

### 2.2 Editar Roteiro (frontmatter)
- **Storage:** `miguel_roteiro_texto_override_<vol>` + `..._ts_<vol>`.
- **Funções:** `getRoteiroText()` (override ∥ `dataset['00_frontmatter'].mainContent`), `openEditarRoteiroModal()` (carrega textarea + info contextual conforme existe/ não override), `closeEditarRoteiroModal()`, `saveRoteiroTexto()` (vazio não salva; `safeLocalSet`), `restoreRoteiroTexto(btnEl)` (2 toques; remove override+ts).
- **UI:** modal `modal-editar-roteiro`; seção nova na página do roteiro "📜 Texto do Roteiro (frontmatter do livro)" mostrando o texto renderizado (marked) + badge `✏️ editado em <data>` ou `texto original`.

### 2.3 Livro inteiro: Ler × Compilar × Editar
- **Storage:** `miguel_fullbook_manual_edit_<vol>` + `..._ts_<vol>`.
- **Funções:** `getFullBookDisplayText()` → `{text, edited, ts}` (override ∥ `getCompiledFullBookData().mainContent`), `openEditarLivroModal()`, `closeEditarLivroModal()`, `saveLivroEditado()`, `discardFullBookEdit(btnEl)` (2 toques), **`atualizarCompilacao(btnEl)`** (2 toques quando há edição manual — 1º toque arma "⚠️ Descartar edição e atualizar?", 2º descarta o override e re-renderiza; sem edição, recompila direto).
- `compileAndReadFullBook()` ficou só navegação/abertura (sem flag) — chamado pela barra de topo, header do roteiro e pelo final de `atualizarCompilacao`.
- **Renomeado:** barra de topo `📚 Ler / Compilar Livro Inteiro` → `📖 Ler Livro Inteiro` (title explica onde recompilar).
- **Capa do compilado (renderSingleView full_book):** 2ª linha `border-t border-amber-400/40 pt-4` flex-wrap com 📥 Baixar | ⚡ Atualizar Compilação | ✏️ Editar Livro Inteiro | 🎬 Estúdio do Livro Inteiro (roxo, `triggerAiAuditWithTokenWarning()`). Banner âmbar condicional quando `disp.edited` (data + botão descartar). Conteúdo renderiza `marked.parse(disp.text)`.
- **Downloads:** `downloadFullBook()` reescrito p/ usar `getFullBookDisplayText()` (nome ganha `_editado` quando aplicável); `downloadRoteiro()` novo (header do roteiro — antes o botão chamava `downloadFullBook`, baixando o livro em vez do roteiro).

### 2.4 Estúdio do livro inteiro (sem auto-revisão)
- Botão roxo "🎬 Estúdio do Livro Inteiro" chama `triggerAiAuditWithTokenWarning()` (existente) — abre o modal de aviso de tokens e depois o Estúdio Editorial (`openAiAuditModal`) com o livro inteiro como alvo. **Nenhuma revisão dispara sozinha.** Modal `modal-fullbook-warning` com texto reescrito ("Ao clicar abaixo você entrará na página do estúdio... pedirá confirmação final antes de consumir tokens"). Tooltip do botão: "não revisa sozinho — você decide lá dentro".

### 2.5 Contraste (.fdi-ui)
- **Diagnóstico AO VIVO (computed style):** h2 "Livro Inteiro Compilado" com classe `text-white` computava `rgb(133, 77, 14)` — `.prose-book h2 { color:#854d0e }` tem especificidade (0,1,1) > `.text-white` (0,1,0); os cards de UI são injetados dentro de `#reader-content.prose-book`.
- **Fix:** CSS `.prose-book .fdi-ui h1..h4 { color: inherit; margin: 0 }` + `.prose-book .fdi-ui p { color: inherit; margin: 0 }` (após a regra `.prose-book hr`). Classe `fdi-ui` adicionada em TODOS os cards de UI renderizados dentro do reader (header roteiro, anotações, texto do roteiro, grid, capa compilado, banner edição). Deliberadamente NÃO sobrescrevemos `font-family` (preserva Cinzel nos títulos).

## 3. Testes

- **Novo:** `scratch/teste_roteiro_livro_edit.js` — mesmo harness DOM-stub do repo (extrai último `<script>`, stubs de document/localStorage/fetch; `global.confirm` LANÇA erro para garantir que nenhum fluxo novo depende de confirm() — padrão webview). 24 testes: migração, criar/editar/apagar (2 toques) anotações, overrides roteiro/livro (salvar, vazio-não-salva, restaurar/descartar em 2 toques), `atualizarCompilacao` c/ e s/ edição, downloads (Blob capturado; sufixo `_editado`; roteiro editado), 6 asserts de fonte (labels, `.fdi-ui`, modais). **24/24 ✅.**
- **Regressões:** upload-versão 14/14, drive-sync cliente 9/9, api-drive server 6/6, central-fontes exit 0 (todos true).
- Ajustes no harness durante o desenvolvimento dos testes: `makeEl` exposto como `global.__makeEl` (snippet roda em `new Function` — escopo de módulo não visível); `removeChild` adicionado ao stub; `window.scrollTo` stubbed.

## 4. Lições / notas

1. **Especificidade CSS no monólito:** qualquer UI nova renderizada dentro de `#reader-content.prose-book` herda as regras de prosa; usar `.fdi-ui` nos cards novos (regra já documentada no comentário do CSS).
2. **confirm() proibido de fato:** qualquer confirmação nova deve nascer já em 2 toques (webview do celular suprime o diálogo — o teste lança se alguém usar).
3. **Monitor de trabalho sob escrita concorrente:** 3 sessões ativas ao mesmo tempo; edição via Edit tool conflituou 2× ("modified since read") — resolvido com troca atômica via Python (`tempfile` + `os.replace`) + verificação pós-escrita. A lição do truncamento de 05/08 segue válida: sempre verificar pós-escrita em arquivo compartilhado.

## 5. Verificação ao vivo (curl pós-deploy)

`fdi-ui` ×9 · "📖 Ler Livro Inteiro" ×2 (barra + header roteiro) · "✏️ Editar Roteiro" ×2 · "✏️ Editar Livro Inteiro" ×1 · "⚡ Atualizar Compilação" ×5 · "🎬 Estúdio do Livro Inteiro" ×1 · `modal-editar-roteiro` ×3 · `modal-editar-livro` ×3 · `atualizarCompilacao(this)` presente · **"Ler / Compilar" = 0 ocorrências** · CSS `.prose-book .fdi-ui h1` presente.
