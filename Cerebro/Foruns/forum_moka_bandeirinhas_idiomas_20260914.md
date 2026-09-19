# 🌐 Fórum — Moka: sincronização canônico→espelho→ousadia + cura do seletor de idiomas (14/09/2026)

> **Pedido do Miguel (14/09, voz→texto):** no Moka Reader, o menu de idiomas (clica na bandeirinha) está com a "fonte estourada — cortando as duas primeiras letras" e "nos últimos idiomas, índia e árabe, a bandeirinha também está cortada". Ordem de serviço: **(1) sincronizar canônico → espelho → ousadia** (todos iguais ao canônico); **(2) consertar as bandeirinhas NO OUSADIA primeiro**; Miguel confere; **(3) só depois** copiar para espelho e canônico. Menção a telemetria no painel ficou "só isso por enquanto" (não era desta leva).

## 1. Sincronização canônico → espelho → ousadia (✅ no ar nos 3)

Estado encontrado (após `git fetch --all`):

| Ambiente | Repo/branch | Antes | Depois |
|---|---|---|---|
| Canônico | `migueldorosario1/moka` main | `2164349` (fonte, intocado) | `2164349` |
| Espelho | `migueldorosario1/moka-espelho` main | `eb24cdd` (cherry-picks 03/09 + sync 02/09) | `428c570` (merge de sync) |
| Ousadia | `migueldorosario1/moka-ousadia` main+ousadia | `5b2d739` (ancestral do canônico) | `2164349` (fast-forward) |

- **Espelho:** mesmo rito do sync de 02/09 — `git merge -s ours` a partir de origin/main (árvore = canônico, histórico do espelho preservado como segundo pai; `git diff origin/main sync_espelho` vazio). Branch local `espelho` atualizada.
- **Ousadia:** fast-forward limpo `5b2d739→2164349` nas duas branches (main + ousadia).
- **Prova:** os 3 domínios (`www.mokareader.com`, `moka-espelho.vercel.app`, `moka-ousadia.vercel.app`) servem `/estante` HTTP 200 com o link `/privacidade` do commit `2164349` presente.

## 2. Causa-raiz do menu de idiomas estourado (diagnóstico numérico, DOM real)

Componente: `apps/web/src/components/LangSwitcher.tsx` (12 idiomas; CSS em `globals.css` §"CSS migrado de LangSwitcher").

**Dois problemas emparelhados:**

1. **Guerra de especificidade 2** — a regra de grupo `.igot-topbar-actions button { width: 44px !important; height: 44px !important; font-size: 20px !important; justify-content: center !important; … }` (padrão de ícones da topbar, ~linha 9808) atinge TODOS os `<button>` descendentes — inclusive as opções do dropdown (`.lang-option`), porque o `LangSwitcher` mora dentro de `.igot-topbar-actions` (TopNav.tsx). Medido ANTES: cada opção **44×44px, fonte 20px, centralizada** → "Português" (~90-100px de texto) transbordava e era cortado nas primeiras letras. É a MESMA família do bug do botão "Entrar" de 06/09 (commit `babea59`), curado naquela vez só para o `auth-signin` — os botões do dropdown ficaram fora.
2. **Lista picada no fundo** — `.lang-dropdown { max-height: 320px; overflow-y: auto }` comportava só ~6 itens de 44px; medido ANTES: `clientHeight 318 × scrollHeight 558` → os últimos idiomas (coreano, árabe 🇸🇦, híndi 🇮🇳) ficavam picados na borda com scroll. É o "a bandeirinha também está cortada".

## 3. A cura (commit `5d80145`, branch ousadia — SÓ o Ousadia)

Em `apps/web/src/app/globals.css`:

1. **Regra de escape de alta especificidade** para as opções (mesma técnica da guerra de 06/09, agora cobrindo o dropdown):
   ```css
   .igot-topbar-actions .lang-switcher .lang-option,
   .lang-switcher .lang-option {
     width: 100% !important; min-width: 0 !important;
     height: auto !important; min-height: 0 !important;
     display: flex !important; justify-content: flex-start !important;
     font-size: 14px !important; line-height: 1.25 !important;
     padding: 8px 12px !important; border: none !important;
     background: transparent !important; box-sizing: border-box !important;
   }
   ```
   Seletor triplo (0,3,0) vence o grupo (0,1,1) em qualquer ordem do arquivo; o par simples cobre capa/Reader (`.capa-lang`, `.reader-row-right` — nesses contextos o bug não existia).
2. **Dropdown que comporta os 12 idiomas:** `max-height: min(70vh, 460px)` + `overscroll-behavior: contain` (era 320px). Em telas normais a lista inteira (≈438px) aparece; em telas baixas rola sem picar item no meio.

## 4. Provas

- **tsc** 0 erros · **next build** verde (exit 0).
- **Local (dev :3199, /estante):** ANTES opções 44×44/20px/center, dropdown 318×558 (cortava ~240px) → DEPOIS opções **170×34/14px/flex-start**, dropdown **438=438, lista inteira visível**.
- **Produção Ousadia ao vivo** (badge 🎢 OUSADIA confirmada): após deploy (CSS chunk `7abde1d80e4df49a.css` contendo a regra nova), mesmas medidas DEPOIS: 12 opções, árabe 🇸🇦 e híndi 🇮🇳 inteiros, `listaInteiraVisivel: true`.
- Nota: screenshot do IAB falhou neste ambiente ("capture failed for guest"); a prova é numérica (getBoundingClientRect/getComputedStyle do DOM real), auditável.

## 5. Estado / o que falta / o que preciso do Miguel

- **O que aconteceu:** 3 ambientes sincronizados no canônico `2164349` (provado) + cura das bandeirinhas NO AR no Ousadia (`5d80145`, provado ao vivo).
- **O que falta:** (1) Miguel CONFERIR em https://moka-ousadia.vercel.app (abrir uma página interna com topbar — ex.: /estante —, olhinho 👁️ se o menu estiver fechado, clicar na bandeirinha); (2) com o OK dele, promover `5d80145` para espelho (mirror main) e canônico (origin main) — rito Ousadia→Espelho→Canônico; (3) telemetria no painel citada de passagem — novo sprint quando o Miguel detalhar.
- **O que preciso do Miguel:** o "tá consertado" (ou print do que ainda estiver errado) para liberar a promoção.
