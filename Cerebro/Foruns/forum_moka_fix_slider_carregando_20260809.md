# Fórum — Moka: slider de páginas travava em "Carregando página…" (corrida de renders)

> Data: 2026-08-09 · Autor: ZCode (Qwen 3.8 Max) · Status: ✅ CORRIGIDO E NO AR (commit `000762e`, deploy Vercel)
> Repo: `Outros/Aplicativos/Moka/Moka-Lab` · Bug: `BUG-20260809-MOKA-SLIDER-RENDER-RACE` (resolvido)
> Backup pré-mudança: `Outros/Aplicativos/Moka/backups/moka_lab_pre_slider_fix_20260809/`

## Reporte do Miguel (voz, 09/08 ~11:55)

"Quando a gente usa a barra de baixo de rolar a página… rodei, ficou travado, carregando página. Se eu clicar, passar a página, voltar, volta ao normal. Ele está com algum problema de cache, de memória, fica sempre carregando página."

## Causa-raiz

Girar o slider dispara um salto de página por micromovimento; cada salto manda o `PdfPageCanvas` **cancelar o render em curso e começar outro**. A falha: se o cancelamento chegava enquanto o componente ainda esperava `await doc.getPage()` (render ainda não tinha começado), a corrida cancelada **seguia em frente mesmo assim** e iniciava um **render zumbi** no canvas compartilhado. A página atual então colidia — pdf.js 4.10.38: *"Cannot use the same canvas during multiple render() operations"* — ou ficava esperando um render que nunca completava → **spinner "Carregando página…" eterno**. Passar/voltar página curava porque iniciava uma corrida nova, limpa (e o zumbi já tinha terminado). O watchdog de 20s não salvava porque cada nova corrida o reiniciava.

## Correção (commit `000762e`)

1. **Guarda anti-zumbi** (`PdfPageCanvas.tsx`): cada corrida de render recebe um nº de sequência (`renderSeqRef`); depois de CADA `await` (getPage, render, textContent, textLayer) a corrida verifica se ficou velha — e para **antes de tocar no canvas**. Corrida velha não inicia mais render.
2. **Clamp de página**: `pageNum` limitado ao `numPages` real do PDF (o slider usa o maior valor entre chapters e numPages; se chapters fosse maior, pedia página inexistente).
3. **Retry único em colisão de canvas**: se um zumbi ainda ocupar o canvas, espera 180 ms e tenta de novo UMA vez, em vez de mostrar erro cru ao leitor.
4. **Debounce do slider** (`Reader.tsx`): o knob segue o dedo na hora (estado `sliderDraft`), mas o salto real só é commitado após **120 ms de silêncio** — elimina a chuva de renders cancelados (e ainda economiza CPU/bateria durante o arrasto). Contador da nav bar acompanha o rascunho.
5. **Watchdog**: render que completa com sucesso devolve o "crédito" de retry da página (`lastRetryPage` resetado) — se travar de novo no futuro, re-tenta em vez de dar erro direto.

## Provas

- `tsc --noEmit` + `next build` verdes (23 rotas).
- Push `23f521d..000762e` → deploy Vercel (`www.mokareader.com`).

## Estado da missão

- **O que aconteceu:** diagnóstico + correção + deploy no ar.
- **O que falta:** teste real do Miguel (browser-use segue bloqueado nesta CLI — IAB não despacha cliques).
- **O que preciso de você (Miguel):** abrir um livro PDF, girar a barrinha de baixo depressa (várias vezes, pra frente e pra trás) e confirmar que NUNCA mais trava em "carregando página".
