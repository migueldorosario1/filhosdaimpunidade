# 🧠 MEMÓRIA — CENTRAL DE FONTES VIVA (log técnico completo)

**Data:** 2026-08-06 ~18:00→18:45 BRT · **Agente:** ZCode/Kimi K3 · **Repo:** `filhosdaimpunidade` (clone de trabalho: `~/ZCodeProject/filhosdaimpunidade`) · **Commit:** `8c3f335` → push→Vercel **AO VIVO** (HTTP 200, marcadores da feature servidos).

## 1. Contexto e mapa do código (antes)

- App monolítico: `index.html` (~5.900 linhas; 1 script clássico linhas 1237–6401).
- **Central de Fontes** = `#modal-database`; dados no array `sourcesDatabase` (44 entradas, 7 categorias: livros, yt, stf, eua, tarifaco, dinheiro, x); render `renderSourceCenterCards()`; abas estáticas no HTML.
- **Memória de fontes do Estúdio** = checkbox `chk-consult-canonical-memory` → subpanel com 4 partes fixas (transcrições→`fonteTranscricoes`, reportagens→`bancoLinksMarkdown`, histórico→`fonteHistorico`, resumo→`fonteResumo`), injetadas no system prompt em `callRealLlmApi()`. Seleção persistida em `miguel_fontes_banco_selection`.
- Helpers existentes reutilizados: `safeLocalSet` (quota→poda legados), `storageFullHelpMessage`, `flashButtonFeedback`.

## 2. O que foi implementado (tudo no `index.html`)

### 2.1 Taxonomia (pedido do Miguel)
`SOURCE_CATEGORIES_BASE` — registro central c/ ícone/label/cor:
`livros` 📚 Livros & Bibliografia · `pdfs` 📄 PDFs Variados & Referência · `yt` 🎥 · `stf` ⚖️ · **`justica_usa` 🦅 Justiça USA** · **`governo_usa` 🏛️ Governo USA** · `tarifaco` 📰 · `dinheiro` 💰 · **`redes` 📱 Postagens Redes Sociais** · `outros` 🗂️.
`BUILTIN_CATEGORY_REMAP` (na leitura, acervo intacto): 5 PDFs genéricos `livros→pdfs`; `pdf_acordao_stf_ap2782→stf`; `eua_*` (EO 14323, OFAC, USTR) `→governo_usa`; `x_post_*→redes`. `justica_usa` e `livros` nascem vazias, prontas p/ receber.

### 2.2 Overlays de persistência (localStorage)
- `miguel_fontes_custom_v2`: fontes criadas pelo editor (shape do sourcesDatabase + `custom:true, studio:bool, items:[]`).
- `miguel_fontes_hidden_v1`: ids embutidos ocultados ("apagar" embutida = ocultar, restaurável).
- `miguel_fontes_items_v1`: `{builtinId: [itens]}` — itens anexados a fontes embutidas (custom guarda itens inline).
- `miguel_fontes_custom_cats_v1`: `{cat_key: {icon,label}}` — categorias criadas na hora.
- `getAllSources()` = embutido (−ocultas, +remap, +itens overlay) concat custom. IDs: `custom_<ts>_<rand>` / `it_<ts>_<rand>` (anti-colisão — bug real achado nos testes: mesmo ms = mesmo id → checkbox do Estúdio resolvia errado).

### 2.3 UI da Central
- Header: botão **➕ Adicionar Fonte** (esmeralda) + contador dinâmico no título (`#database-total-count`).
- `#add-source-panel`: form 2 colunas (título*, fonte/autor*, categoria+nova, data, link, resumo, fichamento, status, selo) + checkbox **🧠 Entrar automaticamente no Estúdio** (default on).
- Abas: `#source-filter-tabs` render dinâmico (`renderSourceFilterTabs()`) — toda categoria (inclusive recém-criada) vira aba c/ contagem; aba ♻️ "N apagadas — restaurar" quando há ocultas.
- Cartões: 🗑️ topo-direito (`confirmDeleteSource`), bloco "📎 Itens anexos" (lista c/ link+nota+🗑️), mini-form inline por cartão (`toggleItemForm`/`saveSourceItem`/`deleteSourceItem`). Escape `escH()` em todo campo do editor; `safeHref()` só http/https.

### 2.4 Integração Estúdio (ênfase do Miguel)
- `#fontes-custom-list` no `fontes-subpanel` → `renderFontesCustomCheckboxes()` lista fontes custom (`studio!==false`) + TODOS os itens anexos (de fontes suas E embutidas).
- `getSelectedFontesParts()` ganha `custom:[{label,text}]` (resolve checkboxes marcados por `data-fc-id`); `callRealLlmApi()` injeta bloco `--- ➕ FONTES & ITENS ACRESCENTADOS PELO EDITOR ---` no system prompt.
- "Marcar todos"/sync/contagem incluem `.chk-fonte-custom`; persistência no mesmo `miguel_fontes_banco_selection` (`custom:{id:bool}`); default marcado; re-render após qualquer CRUD.
- `openTranscriptById` passou a buscar em `getAllSources()` (fichamento funciona p/ fontes novas).

## 3. Testes

- Sintaxe: `new Function()` nos 5 blocos de script → OK.
- Suíte funcional Node c/ DOM-stub (`scratch/teste_central_fontes.js` + `_snippet.js`): **18/18** — abas novas, contagem 44, criar fonte c/ categoria nova, itens em fonte sua e embutida, entries do Estúdio (3), injeção no prompt (fichamento + nota de item), apagar item/fonte, ocultar/restaurar embutida, persistência ×3 chaves.
- Browser IAB do ambiente: **clique quebrado globalmente** (falhou até no botão do Manual; "Browser broker response id mismatch") → verificação visual completa fica p/ o navegador real do Miguel. Deploy conferido via curl (marcadores da feature servidos, 200).

## 4. Governança

- Monitor: linha "FdI Central de Fontes" marcada ✅.
- Clone de trabalho novo em `~/ZCodeProject/filhosdaimpunidade` (não havia clone local; GitHub é a fonte da verdade).
- Fórum deste tema: `Foruns/forum_central_fontes_viva_20260806.md`.
- Nodo do livro: ponteiro adicionado em `CEREBRO_NODE_LIVRO_FILHOS_DA_IMPUNIDADE.md`.

## ADENDO 06/08 ~19:00 — UPLOAD DE ARQUIVO (log técnico)

Commit `da37afd` (AO VIVO, Vercel 200). Implementação:
- **IDB wrapper:** `idbOpen/idbSaveFile/idbGetFile/idbDeleteFile` (db `fdi_fontes_files`, store `files` keyPath `id`); guarda `idbSupported()` p/ ambientes sem IndexedDB.
- **Fluxo fonte:** `onAsFileChange` guarda `asPendingFile` → `saveNewSource` (agora async) grava blob (`file_<ts>_<rand>`) ANTES de criar a fonte; falha de IDB = fonte criada sem anexo + alerta. Meta no objeto: `fileId/fileName/fileSize/fileType`.
- **Fluxo item:** `saveSourceItem` async, input `#ni-file-<sourceId>`, mesma mecânica.
- **Leitura de texto:** `TEXT_FILE_RE` (txt/md/markdown/csv/json/srt/vtt/log) ou mime text/* → FileReader → textarea fichamento (cap 30k, aviso de truncamento). PDF → `extractPdfText` (pdf.js 3.11.174 CDN carregado sob demanda, worker CDN, até 40 págs / 30k chars, status no span `#as-file-info`). PDF digitalizado → aviso "sem texto extraível".
- **Abrir:** `openSourceFile` → object URL + `window.open`, revoke 60s; blob ausente → alerta "armazenamento limpo, anexe de novo".
- **Limpeza:** `confirmDeleteSource` (custom) apaga blobs da fonte + itens; `deleteSourceItem` apaga blob do item.
- **Estúdio:** entries mencionam "Arquivo anexo: <nome>".
- **Testes:** suite migrou p/ wrapper async (saveNewSource/saveSourceItem agora async); extração do script principal agora dinâmica (último `<script>` puro); 21/21 ✅.

## ADENDO 2 — 06/08 ~19:40 — UX FORM + AUDITORIA YOUTUBE (log técnico)

Commit `0b80101` (AO VIVO, 200). Implementação:
- `toggleAddSourcePanel`: ganhou controle de `#btn-add-source-label`/cor (esmeralda↔ardósia), esconde `#source-grid-wrapper` + `#database-modal-filters` com o form aberto; painel vira área rolável `flex-1`.
- **Auditoria:** script oEmbed (`youtube.com/oembed?url=`) nos 23 IDs → 9×200 originais, 14×400/404 + 2×404 adicionais = 16 mortos. Caça de links reais: scraping YouTube results (`"videoId":"..."`), validação de candidatos via oEmbed (título+canal). Matches confirmados: Tucker `fRXhn0UN-_4` ("TUCKER CARLSON entrevista EDUARDO BOLSONARO e PAULO FIGUEIREDO..."), Fox `mTziWNvuOco` ("Lou Dobbs na FOX", canal oficial Eduardo — título/fonte do card corrigidos), Monark `-rvebyRe7QY` ("MONARK DEBATENDO COM O EDUARDO BOLSONARO | Cortes do Flow" — título honesto de corte). Demais buscas bloqueadas (rate-limit YouTube, anti-bot DDG, Bing vazio) → 13 marcados `broken: true` na entrada (comentário QA-AUDIT no código).
- **Renderer:** `item.broken` → badge desabilitado "⚠️ Link indisponível" (cursor not-allowed) + tooltip explicando; `<a>` normal só p/ links vivos.
- **Testes:** suite agora valida toggle (rótulo/lista/filtros), 13 broken, 3 URLs substituídas → **30/30** ✅ + oEmbed 200 das 3 substituições.
