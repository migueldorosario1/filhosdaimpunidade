# 🧠 Memória técnica — Moka TopNav: estouro com fonte ampliada × zoom (14/09 23:3x → 15/09 00:2x BRT)

Log técnico completo da cura `a7f05a3`. Fórum de decisões: `Foruns/forum_moka_topnav_fonte_estouro_20260915.md`.

## 1. Arquivos e pontos exatos (repo `~/ZCodeProject/moka-app`, branch `ousadia`)

- `apps/web/src/app/globals.css`
  - ~3730–3747: `body { zoom: var(--ui-font-scale, 1) }` + fallback `@supports not (zoom:1)` com `transform: scale` (intocados).
  - ~67: `--ui-font-scale: 1` (default no `:root`).
  - ~9063–9069 (1ª `.topnav`, reforma 31/08) e ~9748–9757 (2ª `.topnav`, padronização — prevalece): `margin-inline: calc(50% - 50vw)` → **cura**: `calc(50% - 50vw / var(--ui-font-scale, 1))`.
  - ~9073/9079 (`.topnav-hidden` antigos, `flex-end`) eram neutralizados pela 2ª `.topnav` (`space-between`, mesma especificidade, vem depois) → **cura**: nova declaração `.topnav-hidden { justify-content: flex-end }` logo após a 2ª `.topnav` (~9760–9766).
  - `body { overflow-x: clip }` (~227): por que o estouro era CORTADO sem scroll (usuário não alcança nada).
- `apps/web/src/components/A11yControls.tsx` — slider 0.85–1.4 step 0.05; aplica `document.documentElement.style.setProperty("--ui-font-scale", …)` + `localStorage moka.uiFontScale` (intocado).
- `apps/web/src/components/TopNav.tsx` — modo oculto: `HIDDEN_KEY = "moka.navHidden"`; reforma 31/08: nasce ESCONDIDO (`hidden=true` default), olhinho ABRE o menu; `useState(true)` + `useEffect` lê storage (evita flash de hidratação).
- `apps/web/src/app/configuracoes/page.tsx` — usa `<TopNav right={<TopNavActions />} />` (voltar, AuthGate/Entrar, LangSwitcher, engrenagem, TelemetryIconButton).

## 2. Mecânica do bug (por que vw × zoom estoura)

`zoom` do Chrome escala o used value de comprimentos, mas `vw/vh/dvw` resolvem contra a viewport CSS REAL e depois são multiplicados pelo zoom → `50vw` com zoom 1.4 ocupa 70% da viewport física. O hack full-bleed `calc(50% - 50vw)` (margens negativas pros 2 lados) virou `calc(50% - 1.4×50vw)` ⇒ largura fantasma 1629px numa janela de 1164 ⇒ cortes simétricos. Dividir por `var(--ui-font-scale)` dentro do calc anula exatamente a multiplicação do zoom (conta fecha em qualquer escala; `calc` aceita divisão de comprimento por número).

## 3. Medições crudas (getBoundingClientRect, produção canônica antes do fix — mesma árvore do ousadia)

Viewport 1164px, `--ui-font-scale: 1.4`, `zoom` computado 1.4:
- `.topnav`: `{left: -237.26, right: 1391.80, width: 1629.06}` (estouro 237 esq / 228 dir)
- brand: `{left: -209.3, right: -84.3}` — fora à esquerda
- lastBtn (ações): `{left: 1302.2, right: 1363.8}` — fora à direita
- Modo oculto: `.topnav-eye` `{left: -209.26, right: -147.67}` — 100% fora da tela (olho inclicável, menu irrecuperável sem resetar storage)
- Escala 1 (referência): topnav `-4.5…1159` = viewport; olho `15.45…59.45` visível.

Injetando o CSS da cura (`!important` num `<style id="fix-teste">`) na MESMA página:
- topnav: `-4.5…1159.1` (= viewport) · brand `23.5…148.4` · lastBtn `1069.5…1131.1` — tudo dentro.
- Modo oculto: olho `23.5…85` — dentro; clique (`.click()` sintético; locator/cua click falhou por intercepção intermitente de loading) alternou `topnav topnav-hidden` + `moka.navHidden 0↔1` corretamente.
- Viewport 390×844 @1.4: ANTES topnav `-83…463`, brand `-63.4`, lastBtn `443.4`; DEPOIS topnav `-5…385`, brand `14.6…139.6`, lastBtn `298.2…365.4`, flag `tudoDentro: true`.
- Escala 0.85 @1280: topnav `-5…1275` (full-bleed cobre a viewport também pra fonte menor).

## 4. Git / deploy

- Commit `a7f05a3` (branch `ousadia`, em cima de `5d80145`): 14 insertions, 3 deletions, só `globals.css`.
- Push: `git push ousadia-mirror ousadia` E `git push ousadia-mirror ousadia:main` (fast-forward `5d80145..a7f05a3`).
- 🔴 **Lições de deploy:** (1) projeto Vercel `moka-ousadia` tem **productionBranch = main** — push só no branch `ousadia` NÃO deploya (perdemos ~10 min de loop de sondagem nisso); sempre espelhar no `main` do ousadia-mirror. (2) Sondagem de deploy tem que grep a string NOVA exata (`50vw/var(--ui-font-scale`) — grep de `ui-font-scale` bate na regra antiga do `body{zoom}` e gera falso positivo.
- Sondagem do no-ar: loop curl no chunk CSS de `/configuracoes` até aparecer `margin-inline:calc(50% - 50vw/var(--ui-font-scale,1))` (resultado no §6).
- Estado dos remotes na largada: `origin/main` (canônico) = `5d80145`, `mirror/main` (espelho) = `1a1bd6c`, `ousadia-mirror/{main,ousadia}` = `5d80145`; branch `main` LOCAL estava 1 atrás (cosmético, sem ação).
- Pendente do rito: OK do Miguel → espelho `merge -s ours` + canônico FF (igual ontem).

## 5. Reprodutor manual (pra qualquer bug de zoom futuro)

1. Abrir `/configuracoes` (ou qualquer página interna com TopNav).
2. Console: `document.documentElement.style.setProperty('--ui-font-scale','1.4')` (equivale ao slider Aa 140%).
3. Medir: `[...document.querySelectorAll('.topnav,.topnav-eye')].map(e=>e.getBoundingClientRect())` — se `left<0` ou `right>innerWidth`, é estouro.
4. Modo oculto: clicar no 👁 e conferir o rect do olho.

## 6. Resultado no ar (moka-ousadia.vercel.app, 15/09 ~00:0x BRT)

- Deploy via push `ousadia-mirror ousadia:main` (FF `5d80145..a7f05a3`); chunk novo **`5994fd94df61e1f8.css`** contém `margin-inline:calc(50% - 50vw / var(--ui-font-scale, 1))` e `.topnav-hidden{justify-content:flex-end}` (curl provado; ⚠️ minificador MANTÉM espaços ao redor do `/` — grep sem espaço dá falso negativo).
- **Menu completo @140% (browser real, SEM injeção):** topnav -4,5…1159,1 (= viewport 1164); TODOS os 7 controles medidos um a um e `visivel: true` — Moka 23,5–148,4 · olho 664,7–726,3 · Voltar 737,5–799,1 · Entrar 810,3–912,7 · Português 923,9–985,5 · Configurações 996,7–1058,3 · telemetria 1069,5–1131,1.
- **Modo oculto @140%:** olhinho 1069,5–1131,1 — dentro da tela E no canto direito (`olhoNoCantoDireito: true`); clique reabre o menu.
- Prints: `Memorias/provas_moka_topnav_20260915/print_ousadia_menu_aberto_fonte140_20260915.png` + `print_ousadia_modo_oculto_olho_direita_fonte140_20260915.png`. (Nota: uma análise visual automatizada do print sugeriu corte à direita — refutada pela medição DOM botão a botão acima; o modelo de imagem confundiu proximidade da borda com corte.)

## 7. Pendências / riscos anotados

- `.reader:fullscreen { width: 100vw; height: 100vh }` (~6201): mesmo padrão vw/vh × zoom — potencial corte em tela cheia com fonte ampliada; NÃO tocado (fora da queixa; fica registrado).
- `.igot-topbar { max-width: 100vw }` (~421): com zoom o limite passa da viewport física, mas só limita (não empurra); sem queixa, não tocado.
- Fallback `@supports not (zoom:1)` (transform) não retestado com o fix — navegadores sem zoom são raros (comportamento igual ao pré-fix).
- Sessão do browser deixou `localStorage.moka.uiFontScale`/`navHidden` alterados NA MINHA janela de teste (IAB), não na do Miguel.

---
*ZM (GLM-5.3), 15/09/2026 00:2x BRT.*
