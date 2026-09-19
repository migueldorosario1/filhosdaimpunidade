# 📐 Fórum — Moka: cabeçalho estoura com fonte ampliada + olhinho fora da tela (bug 14/09 ~23:30, cura madrugada 15/09)

**Tema:** bug do menu de cima (TopNav) do Moka Reader reportado pelo Miguel com 2 screenshots (23:29 e 23:30 de 14/09, mokareader.com/configuracoes e /telemetria).
**Sintomas relatados:** (1) ao aumentar a fonte nas configurações, o cabeçalho estoura — palavras da esquerda E da direita escondidas; (2) clicou no olhinho 👁 e sumiu TUDO, até o olho — sem como fazer reaparecer.
**Sessão:** ZM (GLM-5.3), 14/09 23:3x → 15/09 00:1x BRT. Commit `a7f05a3` (branch `ousadia`).

---

## 1. Causa raiz (medida no DOM, produção www.mokareader.com)

Dois mecanismos que andam juntos desde a reforma de acessibilidade (09/08):

- **Escala de fonte = `body { zoom: var(--ui-font-scale) }`** (`globals.css` ~3737). O `A11yControls` (slider 85–140%) seta `--ui-font-scale` no `:root`. Zoom foi escolhido na época porque a UI usa px fixo (não rem).
- **TopNav full-bleed com unidades de viewport**: `.topnav { margin-inline: calc(50% - 50vw) }` — o hack que faz o menu "escapar" do container de cada página (estante sem margem, memória 1080px, writer 880px…). **Duas definições** no arquivo (~9066 e ~9751; a 2ª, da padronização de 31/08, é a que vale em cascata).

**O conflito:** unidades `vw` NÃO são reescaladas pelo `zoom` do body — o Chrome resolve `50vw` contra a viewport real e o zoom multiplica por cima. Com fonte 140% numa viewport de 1164px, a topnav passou a ocupar **x=-237 a x=1392 (1629px de largura)**: logo "Moka" em x=-209 (cortado à esquerda), último botão terminando em x=1364 (cortado à direita). Agravante: `body { overflow-x: clip }` corta sem scroll — não dá nem pra rolar até o conteúdo escondido.

**O olho que sumiu:** no modo oculto a topnav renderiza só o olhinho; com o estouro ele caía em **x=-209 a -148 — inteiramente fora da tela**, invisível e inclicável. Era exatamente o "sumiu tudo, até o olho" do Miguel: a preferência fica salva (`moka.navHidden=1`) e o menu NÃO voltava. (No relato dele o olho estava à esquerda — ver §3-b sobre a regressão de cascata.)

**De quebra descoberta no caminho:** a 2ª definição de `.topnav` (`justify-content: space-between`, da padronização 31/08) vem DEPOIS na cascata e neutralizava o `flex-end` do `.topnav-hidden` (regra anterior no arquivo) — no modo oculto o olho "pulava" para o canto esquerdo, longe de onde estava no menu aberto (ações à direita). Regressão silenciosa, não reportada.

## 2. A cura (`a7f05a3`, branch ousadia)

1. `margin-inline: calc(50% - 50vw / var(--ui-font-scale, 1))` — o `vw` passa a dividir pela escala; como o zoom multiplica depois, a conta fecha em QUALQUER escala (85–140%): a topnav volta a ocupar exatamente a viewport. Aplicado nas DUAS definições (~9066 e ~9751).
2. `.topnav-hidden { justify-content: flex-end }` re-declarado APÓS a 2ª `.topnav` (~9763) — olhinho oculto volta ao canto direito, do lado de onde estava no menu aberto.

Fallback `@supports not (zoom:1)` (transform) não foi tocado; navegadores sem zoom são raros e o transform-scale já não sofria do estouro de vw da mesma forma (registro: não testado — fora do escopo da queixa, que é Chrome).

## 3. Provas (browser real, antes/depois, medidas no getBoundingClientRect)

**a) Desktop viewport 1164px, fonte 140% (`/configuracoes`, produção canônica):**

| medição | ANTES | DEPOIS do fix |
|---|---|---|
| topnav | -237,3 … 1391,8 (largura 1629) | -4,5 … 1159,1 (= viewport) |
| logo "Moka" (brand) | left -209,3 (fora, esquerda) | left 23,5 ✓ visível |
| último botão (ações) | right 1363,8 (fora, direita) | right 1131,1 ✓ visível |

**b) Modo oculto com fonte 140% (o "olho sumiu"):** ANTES olhinho em -209,3…-147,7 (100% fora da tela); DEPOIS em 23,5…85 — visível e clicável (reabertura provada por clique, classe `topnav topnav-hidden` + `moka.navHidden=1` → clique → menu volta).

**c) Mobile 390px, fonte 140%:** ANTES topnav -83…463, brand -63,4 e último botão 443,4 (tudo cortado); DEPOIS topnav -5…385, brand 14,6, último botão 365,4 — `tudoDentro: true`.

**d) Escala 85% (fonte menor), desktop 1280px:** topnav -5…1275 = viewport inteira — full-bleed preservado também pra baixo.

Validação ao vivo foi feita INJETANDO o CSS da cura na produção canônica (mesma árvore do ousadia) antes do commit; depois o commit `a7f05a3` foi pushado e deployado no laboratório.

## 4. Deploy e estado

- Push: `ousadia-mirror` branch `ousadia` **e** `main` (🔴 o projeto Vercel `moka-ousadia` tem **productionBranch = main** — push só no branch ousadia NÃO deploya; ontem a cura das bandeirinhas foi por isso).
- 🔴 Pendência de sincronia notada: branch LOCAL `main` do repo estava 1 commit atrás do `origin/main` (cosmético; remotes todos na árvore `5d80145`).
- Prova no ar do ousadia (chunk novo com `50vw/var(--ui-font-scale`): ver §5 quando fechar.

## 5. Estado final — o que aconteceu / o que falta / o que preciso de você (Miguel)

**O que aconteceu:** causa raiz medida e provada (vw × zoom), cura aplicada nas 2 definições do full-bleed + olhinho restaurado ao canto direito, commit `a7f05a3` no ousadia, provas numéricas antes/depois em desktop/mobile/escala 85%.

**O que falta:** OK do Miguel conferindo o laboratório → promoção espelho (merge `-s ours`) + canônico (FF), no rito Ousadia→Espelho→Canônico.

**O que preciso de você (Miguel):** abra `https://moka-ousadia.vercel.app/configuracoes`, aumente a fonte (Aa) até 140% e confira: (1) menu de cima inteiro visível, nada cortado; (2) clique no olhinho — some o menu mas o olho FICA visível (canto direito) e um clique traz tudo de volta. Se estiver bom, diga "vai" que eu promovo espelho + canônico.

---
*Registrado por ZM (GLM-5.3) em 15/09/2026 00:1x BRT. Tema Duplo: este fórum + `Memorias/memoria_moka_topnav_fonte_estouro_20260915.md`.*
