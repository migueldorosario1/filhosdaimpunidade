# Memória — Moka: fix do slider que travava em "Carregando página…" (técnica completa)

> Data: 2026-08-09 · Autor: ZCode (Qwen 3.8 Max) · Commit: `000762e` (push `23f521d..000762e`, deploy Vercel)
> Bug: `BUG-20260809-MOKA-SLIDER-RENDER-RACE` · Fórum par: `Foruns/forum_moka_fix_slider_carregando_20260809.md`
> Backup: `Outros/Aplicativos/Moka/backups/moka_lab_pre_slider_fix_20260809/` (PdfPageCanvas.tsx + Reader.tsx pré-fix)

## Reporte (Miguel, voz, 09/08 ~11:55)

Na leitura de um livro PDF, girar a barra de baixo (slider de navegação rápida) deixava a página presa em "Carregando página…" para sempre; avançar/voltar página resolvia. Miguel intuía "problema de cache/memória".

## Diagnóstico

Arquivos envolvidos:
- `apps/web/src/components/PdfPageCanvas.tsx` — renderiza UMA página do PDF (canvas + text-layer pdf.js).
- `apps/web/src/components/Reader.tsx` — navegação; slider `.nav-slider` (`<input type="range">`) com `onChange → goToGlobalPage(g)`; em PDF cada valor do slider = `setChapterIdx(g)` = `pageNum={chapterIdx+1}` no canvas.
- pdf.js: **4.10.38** (hoisted do monorepo; `packages/parser` declara `^4.7.76`).

Mecânica do bug (corrida):
1. Slider girando dispara dezenas de `onChange` → dezenas de re-execuções do effect de render em sequência, cada uma cancelando a anterior.
2. O cleanup do effect cancelava `localRenderTask` — mas se a corrida ainda estivesse em `await doc.getPage(pageNum)` (render não iniciado, `localRenderTask === null`), **nada era cancelado de fato**.
3. A corrida "cancelada" continuava o fluxo e chamava `page.render()` no **mesmo canvas** → **render zumbi**.
4. A corrida atual, ao chamar `page.render()` no canvas ocupado, recebia o throw síncrono do pdf.js 4.10.38 (`pdf.mjs:13119`): *"Cannot use the same canvas during multiple render() operations. Use different canvas or ensure previous operations were cancelled or completed."* — ou ficava aguardando um render interno que nunca completava.
5. Resultado visível: `pageReady=false` sem trabalho pendente → spinner eterno. O watchdog de 20 s (adendo de 28/07, commit `a35a066`) não salvava porque cada nova corrida do effect o reiniciava, e o retry único por página (`lastRetryPage`) nunca chegava a agir.
6. Avançar/voltar curava: nova corrida limpa, zumbi antigo já finalizado.

Histórico relacionado: watchdog de render criado em `a35a066` (Moka 3.0.1) para travamento semelhante sem slider; worker pdf.js movido p/ local em `739abe9` (Moka 1.6).

## Correção (2 arquivos)

### `PdfPageCanvas.tsx`
1. **`renderSeqRef` + `stale()`**: cada execução do effect faz `const seq = ++renderSeqRef.current; const stale = () => cancelled || seq !== renderSeqRef.current;`. Checagem `if (stale()) return;` inserida após CADA await: `getPage`, antes do `page.render`, após `task.promise`, após `getTextContent`, após `textLayer.render`/endOfContent, e no `catch`. Corrida velha morre antes de tocar no canvas — impossível novo zumbi.
2. **Clamp**: `const numPages = (doc as { numPages?: number }).numPages; const target = numPages ? Math.min(pageNum, numPages) : pageNum;` antes do `getPage` (slider usa `max(chapters.length, pdfNumPages)`; se chapters > numPages, não pede página inexistente).
3. **Retry único em colisão**: `page.render()` envolvido em try/catch; se a mensagem casar com `/same canvas/i`, aguarda 180 ms (tempo de o ocupante terminar) e tenta UMA vez de novo, respeitando `stale()`; outro erro é relançado pro catch existente.
4. **Watchdog**: sucesso no render faz `lastRetryPage.current = null` (devolve o crédito de retry da página).

### `Reader.tsx`
5. **Debounce do slider**: novo estado `sliderDraft` + `sliderTimerRef`. `handleSliderChange(v)`: knob segue o dedo (`setSliderDraft(v)`) e agenda commit com 120 ms de silêncio (`setTimeout → setSliderDraft(null); goToGlobalPage(v)`); timer limpo a cada movimento e no unmount (useEffect cleanup). Slider usa `value={sliderDraft ?? globalPageIdx}`; contador da nav bar acompanha o rascunho. Efeito colateral bom: durante o arrasto o app para de desperdiçar renders completos de páginas intermediárias (CPU/bateria).

## Provas

```bash
npx tsc --noEmit                      # exit 0
npx next build                        # ✓ Compiled successfully, 23 rotas
git push origin main                  # 23f521d..000762e main -> main
```

## Reversão

- `git revert 000762e` (ou restaurar `backups/moka_lab_pre_slider_fix_20260809/`).
- O comportamento pré-fix era estritamente pior (travamento); o debounce não muda o resultado final do slider, só o momento do commit.

## Estado da missão

- **O que aconteceu:** causa-raiz identificada (corrida de renders com zumbi de canvas), correção dupla (guarda seq + debounce), build verde, deploy no ar.
- **O que falta:** teste real do Miguel girando o slider depressa (browser-use segue bloqueado nesta CLI).
- **O que preciso do Miguel:** abrir um PDF, girar a barrinha várias vezes e confirmar que não trava mais.
