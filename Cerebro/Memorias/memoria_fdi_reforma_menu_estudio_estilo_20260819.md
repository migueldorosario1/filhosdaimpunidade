# 🧠 MEMÓRIA TÉCNICA — FdI: Reforma menu + Estúdio do Estilo + cópia c/ caixinhas (19/08/2026)

**Agente:** ZCode/Kimi K3 (sessão interativa) · **Commit:** `1cf8684` (HEAD==origin, AO VIVO ~11:50, HTTP 200)
**Backup pré-reforma:** `index.html.bak_pre_reforma_20260819` (local, gitignored via `*.bak*`)
**Fórum-irmão:** `Foruns/forum_fdi_reforma_menu_estudio_estilo_20260819.md` (pedido, plano, adendo final)

## Arquivos tocados
- `index.html` (+903/−65 linhas) — único arquivo de código
- `.gitignore` — adicionado `*.bak*`
- Testes: `/tmp/teste_reforma_fdi_20260819.js` — **41/41 ✅** (sintaxe 2 blocos inline via vm + funcionais c/ stubs)

## O que foi implementado (mapa técnico)

### Fase A — Menu enxuto (header)
- ~15 botões → 5 dropdowns: `fdi-menu-livro` / `fdi-menu-estudio` / `fdi-menu-memoria` / `fdi-menu-exibicao` / `fdi-menu-sincronia` (classe `.fdi-menu`).
- Ficam fora: brand + badge volume + ◀ `#chapter-select` ▶.
- **Decisão-chave:** `switchVolume()` e `setMode()` **reescrevem className inteiro** dos botões por ID → botões legados (`btn-vol1-v7`, `btn-vol2-v1`, `btn-mode-single`, `btn-mode-compare`, `theme-toggle-btn`+icon/label) foram movidos para um `<div class="hidden">` pai (o JS reescreve filhos à vontade; o pai continua escondendo). Itens de menu novos chamam as mesmas funções — zero patch em JS existente.
- `fdiToggleMenu(id, ev)` (stopPropagation + fecha outros) / `fdiCloseMenus()` / listener global de clique fora.

### Fase B — Estúdio do Estilo (`#page-estudio-estilo`, z-9997)
- 4 abas (`fdiEstiloTab`): 📜 Constituição · 📰 Diretriz Editorial · 🎵 Diretriz de Estilo · 🎼 Prompts.
- Documentos: `ESTILO_DOCS_DEFAULT` (3 chaves) + `getActiveEstiloDoc(key)` (override `fdi_estilo_doc_<key>`) + editar/salvar/cancelar/restaurar(confirm)/copiar/baixar + `fdiEstiloBaixarTudo()` (ESTILO_COMPLETO_FDI.md: 3 docs + todos os prompts).
- Prompts: `PROMPTS_ESTILO_DEFAULT` (8, ids p1–p8) + cabeçalho/fechamento compartilhados (`PROMPTS_ESTILO_PADRAO_CABECALHO/FECHAMENTO` — incluem "obedeça a Constituição" + "800 e 1.000 palavras"). Override lista inteira em `fdi_prompts_estilo_v1` (JSON). CRUD: `fdiPromptNovo` (id `px<timestamp>`, já abre em edição), `fdiPromptSalvar`, `fdiPromptApagar` (2 toques via dataset.armed + timeout 3s; piso de 1), `fdiPromptsRestaurar` (confirm), `fdiPromptVer/Editar/Copiar`. Render via `renderPromptsEstilo()` com `fdiEsc` (escape) + `marked.parse`.
- Conteúdo v1 destilado de `Kimi K3/MANUAL_DE_ESTILO.md` (#1–#34), `REFERENCIA_LITERARIA.md` (medidas Machado 23,7 palavras/frase × Thompson 32,1; adjetivo 14/mil; -mente 6/mil), `TESE_CENTRAL.md` (3 pernas), protocolos do Contrato.

### Fase C — Memória do Projeto (`#page-memoria-projeto`)
- `MEMORIA_PROJETO_DEFAULT` (8 seções: identidade, 3 documentos, acervo, primários, produção, governança, infra, fluxo) + override `fdi_memoria_projeto_v1` + editar/copiar/baixar/restaurar.
- open/close seguem o padrão `openManualPage` (escondem app-header/subheader/main).

### Fase D — Cópia com caixinhas (Estúdio do Capítulo)
- Faixa sob os botões do painel do capítulo: `#chk-copy-prompt` + `#copy-prompt-select-wrap`>`#copy-prompt-select` + `#chk-copy-memoria`.
- Estado em `fdi_copy_cfg_v1` ({prompt, promptId, memoria}); `fdiCopyCfgChanged()` persiste e mostra/esconde o seletor; `openAiAuditModal()` restaura estado + `fdiPopulateCopyPromptSelect()` (único patch em função existente, bloco try próprio no fim).
- `copyEntireChapterText()`: 1 patch de 3 linhas — `text = fdiMontarBlocoCopia(text)` antes de copiar. Montagem: corpo do prompt → `---` → memória → `---` → `## TEXTO PARA TRABALHAR` → texto. Sem caixinhas = texto puro.

### Fase E — API recuada
- Card "🔁 Ciclo principal — copiar & colar" (5 passos) no painel esquerdo do Estúdio.
- Botão `runDeepSeekV4Instruction()` envelopado em `<details>` "⚡ Modo API (exceção — gasta créditos das chaves)" (label do span virou "…(API)"). Dropdown de motores do topo do Estúdio **mantido** (serve ao modo exceção).

## Armadilhas para quem mexer depois
- **IDs legados ocultos:** não remover o div.hidden do header — `switchVolume/setMode/toggleThemeMode` quebram (getElementById → null.className).
- **localStorage é a persistência**: overrides novos são `fdi_*`; não há backend novo. Sync GitHub/Drive do app cobre revisões de capítulos, não estes overrides (exportar = botões 📥 Baixar).
- **`fdiPopulateCopyPromptSelect()`** deve rodar após qualquer mudança na lista de prompts (savePromptsEstilo já chama).
- Teste de regressão: rodar `node /tmp/teste_reforma_fdi_20260819.js` (lê o index.html do repo).

## Fase futura registrada (NÃO implementada — ordem Miguel "isso você faz depois")
FdI vira **gerador de livros**: botão no alto "🧹 Limpar / Iniciar novo projeto", "usar estilo antigo" (importar Constituição/Diretrizes/Prompts de outro projeto), nome do projeto variável. Terreno preparado: todos os dados novos já vivem em namespace `fdi_*` (trocável por `<projeto>_*` quando chegar a hora).
