# 🧠 MEMÓRIA — Moka Reader: Tradução de Livro Inteiro em Volumes (2026-07-21)

> Log técnico completo da ideia do Miguel. Fórum resumido: `Foruns/forum_moka_traducao_livro_volumes_20260721.md`.
> Nodo (Camada 2): `CEREBRO_INDEX_MOKA_LOG.md`.

## 1. Origem
Pedido do Miguel por voz→texto em 2026-07-21, sessão ZCode/Kimi. Transcrição bruta (trechos):
- "um ícone, a gente está com espaço sobrando lá para o ícone, que é para traduzir livro inteiro"
- "quando o livro for grande, você traduz em dois volumes. Aí você cria dois arquivos"
- "a gente pode criar em volumes até volumes de 50 páginas... volume 1, volume 2, 50 p"
- "depois o programa pode integrar... a gente coloca no aplicativo para integrar os volumes"
- "para traduzir é melhor de 50 em 50... epub e pdf"

## 2. Especificação derivada

### 2.1 Entrada / UX
- **Novo ícone na toolbar do `Reader.tsx`** (Miguel afirma haver espaço sobrando na barra de ícones).
- Ao tocar: modal de confirmação (padrão AskModal/SummaryModal) com:
  - idioma de destino (default = `targetLang` das configurações);
  - estimativa de volumes (páginas totais ÷ 50) e **aviso de custo em tokens** ("mais páginas = mais tokens", padrão já existente);
  - escolha de saída: EPUB e/ou PDF;
  - botão iniciar (confirmação obrigatória).

### 2.2 Segmentação em volumes
- Base: a **paginação global** já implementada em V 1.1 (`paginateBlocks()` ~2200 chars/página) — os volumes são fatias de 50 páginas globais.
- Volume = `{ volumeIdx, pageStart, pageEnd, title: "<Livro> — Vol. N (págs X–Y)" }`.
- Livro ≤ 50 páginas → volume único (fluxo simples).

### 2.3 Tradução
- Chamadas sequenciais por volume via `packages/ai-providers` (provider ativo do usuário, BYOK — chave fica no dispositivo).
- Dentro do volume, traduzir página a página (ou blocos) com streaming, reaproveitando a lógica de `translateStream` do ai-client.
- **Checkpoint/resume**: estado salvo no IndexedDB (`db.ts`) — se o app fecha no volume 7/20, retoma do checkpoint. Padrão desejável: `translationJobs` store.
- Progresso visível: reaproveitar padrão `.tts-prep-bar` (pílula flutuante com etapa, barra e cancelar) — aqui com progresso determinado "Volume 7/20 · página 31/50".

### 2.4 Geração de EPUB (por volume)
- `packages/parser` já usa JSZip para **ler** EPUB; para **escrever**, gerar EPUB 3 mínimo:
  - `mimetype`, `META-INF/container.xml`, `OEBPS/content.opf`, `toc.xhtml` (nav), capítulos XHTML.
  - Metadados: título com sufixo de volume, autor original, idioma de destino, `dc:source` apontando o original.
- Salvar na **biblioteca local** (IndexedDB) como livro novo, agrupado por `seriesId` = livro original + idioma destino.

### 2.5 Geração de PDF
- MVP: exportação via renderização HTML → print/jsPDF no cliente.
- Alternativa a avaliar: deixar PDF para fase posterior e entregar só EPUB no MVP (questão aberta do fórum).

### 2.6 Integrador de volumes ("juntar tudo")
- Ação na biblioteca sobre uma série de volumes: **"Integrar volumes"**.
- Gera EPUB único: concatena capítulos na ordem, TOC unificado com entradas por volume, metadados do livro completo.
- Volumes individuais permanecem (usuário decide se apaga).

## 3. Restrições e regras herdadas
- **Backup antes de deploy** (regra permanente Miguel 2026-07-20): zip datado do modelo no ar em `Moka/backups/` antes de qualquer deploy da feature.
- **Custo**: sempre aviso explícito de tokens antes de iniciar; tradução integral de livro grande é a operação mais cara do app até aqui.
- **i18n**: todas as strings novas × 12 idiomas (padrão: script de chaves como `/tmp/add-i18n-keys.js` da V 1.1).
- **Nunca traduzir "livro inteiro num prompt só"** — sempre em pedaços (coerente com a regra V 1.1 de tradução por página).
- Código em `Moka-Lab` (clone git canônico `migueldorosario1/moka`), `npx tsc --noEmit` + `npx next build` verdes antes de deploy.

## 4. Dependências existentes no código (V 1.3)
| Peça | Arquivo | Reuso |
|---|---|---|
| Paginação global | `apps/web/src/components/Reader.tsx` (`paginateBlocks()`) | fatiar volumes de 50 págs |
| Tradução streaming | `apps/web/src/lib/ai-client.ts` (`translateStream`) | motor da tradução por volume |
| Providers BYOK | `packages/ai-providers/` | chamadas sequenciais |
| Leitura EPUB | `packages/parser/` (JSZip) | base para escrita EPUB |
| IndexedDB | `apps/web/src/lib/db.ts` | checkpoint de job + volumes na biblioteca |
| Barra de progresso | `.tts-prep-bar` (Reader) | padrão visual do progresso |
| Aviso de tokens | `SummaryModal.tsx` | padrão do modal de confirmação |

## 5. Estado
- **2026-07-21 (tarde):** ideia registrada (fórum + memória + nodo).
- **2026-07-21 (18:00 BRT):** ✅ **IMPLEMENTADO E DEPLOYADO (Moka V 1.4)** — Miguel autorizou a sprint na hora. Arquivos: `apps/web/src/lib/paginate.ts` (helpers extraídos do Reader), `apps/web/src/lib/book-translate.ts` (motor + retomada + integrador), `apps/web/src/components/TranslateBookModal.tsx` (UI), `packages/parser/src/epub-writer.ts` (escritor EPUB 3), Reader.tsx (ícone 🌍 + render), ui-strings.ts (21 chaves × 12 idiomas). Commit `6390121` → auto-deploy `moka-keioxuga0` → www.mokareader.com (200 ✓). Backups: `moka_V1.4_lab_2026-07-21_1801.zip` + `moka_V1.4_producao_DEPLOYADO_2026-07-21_1803.zip`; rollback imediato V 1.3.9 (`a08b752`).
- **Diferenças vs especificação original (§2):** saída PDF ficou fora do MVP (só EPUB); tamanho do volume fixo em 50; idioma = `targetLang` das Configurações; tradução por página usa `translatePage` (não-streaming) com checkpoint a cada página; origem PDF não suportada nesta versão (só EPUB).

— ZCode/Kimi, 2026-07-21
