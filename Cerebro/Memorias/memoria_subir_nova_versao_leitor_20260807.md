# 🧠 MEMÓRIA — SUBIR NOVA VERSÃO NO LEITOR (log técnico completo)

**Data:** 2026-08-07 ~10:12→10:35 BRT · **Agente:** ZCode/Kimi K3 · **Repo:** `filhosdaimpunidade` (clone de trabalho: `~/ZCodeProject/filhosdaimpunidade`) · **Commit:** `0ce3556` → push → Vercel **AO VIVO** (HTTP 200; `modal-upload-version` ×3 e "Subir Nova Versão" servidos no HTML de produção). HEAD==origin verificado.

## 1. Contexto e mapa do código (antes)

- App monolítico: `index.html` (~6.900 linhas; script clássico principal começa na linha 1297).
- **Barra de versões do leitor ("capa")** = `#app-subheader` → `#single-version-tabs`, renderizada por `renderVersionTabs()` (~linha 3050): dropdown 📜 Histórico de Versões (selecionar/apagar 🗑️ por versão, 🧹 Faxina em massa) + botão 👑 Tornar Canônica. Edição de versões acontece no Estúdio (💾 Gravar Revisão R#).
- **Lacuna (pedido Miguel):** existia apagar (deleteRevisionVersion/bulkDeleteSelectedVersions) e editar/gravar a partir do Estúdio, mas **não existia** como injetar uma versão INTEIRAMENTE nova vinda de fora (arquivo/texto) — só dava para gerar via IA ou editar manualmente o texto ativo.
- Revisões persistem em localStorage `miguel_book_revisions_<vol>_<cap>` via `safeLocalSet` (quota→poda legados); chave nova por `nextRevisionKey` (máximo+1 — anti-colisão pós-faxina). Shape da revisão: `{title, author, versionTag, badge, content, engineSlug, rawInstruction, summarizedRule}`.
- Helpers reutilizados: `loadPdfJs`/`pdfjs-dist@3.11.174` (mesmo da Central de Fontes, commit `da37afd`), `TEXT_FILE_RE`, `fmtSize`, `switchVersion`, `refreshStudioTitle`, `setStudioSaveStatus`, `showStudioToast`, `updateUrlHashRoute`.

## 2. O que foi implementado (tudo no `index.html`)

### 2.1 Modal `modal-upload-version` (HTML, após `modal-git-sync`)
Tema sky/azul (família visual dos modais emerald/git e amber/database). Conteúdo:
- Banner explicativo fixo: "entra no histórico DESTE capítulo como R# nova, sem apagar nem alterar versão existente; nome do capítulo não muda; canônica só se você quiser".
- Subtitle dinâmico `#upload-version-subtitle` (nome limpo do capítulo + próximo R#) e chip `#upload-version-nextr`.
- **Passo 1:** `<input type="file" id="upload-version-file" accept=".md,.markdown,.txt,.pdf">` + linha de status `#upload-version-file-info`.
- **Passo 2:** `<textarea id="upload-version-text" oninput="updateUploadVersionCharcount()">` + contador `#upload-version-charcount`.
- **Rótulo opcional** `#upload-version-label` (máx 40 chars, parênteses sanitizados).
- Ações: Cancelar / 💾 Gravar como nova versão.

### 2.2 Funções JS (após `bulkDeleteSelectedVersions`)
- `UPLOAD_VERSION_MAX_CHARS = 400000` — teto de segurança do localStorage (~5MB/origem; R#s acumulam).
- `openUploadVersionModal()` — guarda `full_book`/`00_frontmatter` (toast e sai); calcula `nextRevisionKey(getSavedRevisions(currentChapterKey))` e preenche subtitle/nextr; limpa estado anterior; abre modal + `lucide.createIcons()`.
- `closeUploadVersionModal()` / `updateUploadVersionCharcount()`.
- `onUploadVersionFileChange()` — TXT/MD via `FileReader.readAsText` (texto INTEGRAL ao textarea, sem o cap de 30k da Central — aqui é versão de capítulo, não fichamento de prompt; cap = 400k com aviso); PDF → `extractPdfForUploadVersion` (até 200 páginas, join com `\n`, cap 400k, mensagens de status: lendo/extraindo/sem texto extraível→cole manualmente); tipo não suportado → aviso.
- `saveUploadedVersion(btnEl)` — valida texto não-vazio (alert+toast) e capítulo específico; monta revisão `{title:'Versão Enviada (upload)', author:'Miguel do Rosário', versionTag:'R# (upload)' | 'R# (upload: <rótulo>)', badge:'Enviada em <data>', content, engineSlug:'upload', rawInstruction, summarizedRule}`; `safeLocalSet`; em quota/blocked → status+toast+`storageFullHelpMessage` e **não muda nada**; sucesso → fecha modal, `switchVersion(rKey)` (re-render total: abas, métricas, visão, URL `&ver=R#`), `refreshStudioTitle()`, status+toast de confirmação.

### 2.3 Fiação UI
- `renderVersionTabs()`: botão **⬆️ Subir Nova Versão** (`upload-cloud` lucide, sky-600) após o botão canônica — aparece em todo capítulo normal (full_book/roteiro saem antes no early-return, nem mostram o botão).
- Dropdown 📜: mini-botão **⬆️ Subir** no header ao lado do 🧹 Faxina (`closeVersionDropdown(); openUploadVersionModal();`).

## 3. Decisões de design (por quê assim)

1. **Canônica intocada de propósito:** subir versão é ato de ACERVO, não de DECISÃO editorial — o ponteiro 👑 só muda pelo botão específico (coerente com a "verdade editorial" do commit `15a979e`).
2. **Versão nova vira a ativa:** feedback imediato de que o upload funcionou (o editor vê o texto na hora); as demais seguem intactas no histórico.
3. **Sem cap de 30k:** o cap de 30.000 chars da Central de Fontes existe para caber em PROMPT de IA; versão de capítulo é texto completo — teto de 400k protege o localStorage sem cortar capítulo real (capítulos atuais: 30–90k).
4. **Mesmo shape das revisões do Estúdio:** compatível com dropdown, Duelo, compilado, sync GitHub (`revisions.json`) e faxina — nenhum caminho novo de dados.

## 4. Testes

`scratch/teste_upload_versao.js` (harness DOM-stub do repo, mesmo padrão de `teste_central_fontes.js`) — **14/14 ✅**:
1. modal abre e anuncia próximo R# (R3) + nome do capítulo · 2. gravar colado→`R3 (upload)`, ativa, R1/R2 intactas, modal fecha · 3. rótulo "Sônia"→`R3 (upload: Sônia)` · 4. vazio não grava · 5. full_book bloqueado (abrir e gravar) · 6. anti-colisão: R2 apagada + R3 existente → sobe R4 · 7. canônica inalterada · 8. quota→não grava nem ativa · 9. contador de chars · 10. `getVersionLabelForKey` resolve o tag · 11–14. checagens de fonte (modal, botão barra, mini-botão menu, accept do input).
Regressão: `teste_central_fontes.js` 23/23 ✅. Duas limitações de stub contornadas nos testes (querySelector retornando null; `currentViewMode` é global implícito criado por `setMode` no boot real) — limitações do harness, não do código.

## 5. Verificação ao vivo

- `git push` → `0ce3556` (HEAD==origin).
- `curl https://filhosdaimpunidade.vercel.app/` → HTTP 200, `modal-upload-version` ×3, "Subir Nova Versão" presente no HTML de produção.
- URL de trabalho do Miguel (`#leitor?vol=vol1_v7&cap=01_estarei_vingado&ver=R28`) segue válida — feature está na mesma barra.

## 6. Incidente de processo (registrado para aprendizado)

Ao inserir minha linha no `MONITORAMENTO_DE_TRABALHO.md`, um Edit mal-ancorado **apagou a linha da sessão Qwen (LIGA O CADERNO)**. Detectado na hora (grep de confirmação) e **restaurada integralmente** via Python (conteúdo preservado no contexto). Lição: em arquivo-tabela compartilhado, confirmar com `grep` após cada Edit — feito.
