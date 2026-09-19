# 🔧 PROMPT — ANTIGRAVITY: acabamento do MENU (logo padronizado + ícones iguais + estabilidade)

> Pedido do Miguel (31/08 ~22h): "a xícara Moka está muito encostada no canto em
> algumas páginas e não está padronizado — no Writer está diferente; o menu tem
> que ficar ESTÁVEL em todas as páginas; os ícones do menu têm que ter todos o
> MESMO tamanho." Diagnóstico do ZM incluído (com números) — cirúrgico.

---

PROMPT (cole no Antigravity Desktop):

Você é o acabador de interface do **Moka** (repo `/home/migueldorosario/ZCodeProject/moka-app`, branch `obra/memoria`, app em `apps/web/src`). Missão: **padronizar o menu de topo (TopNav) em TODAS as páginas** — a queixa do Miguel: o logo (xícara Moka) fica colado no canto esquerdo em algumas páginas, em outras não, e no Moka Writer está diferente; o menu precisa ficar ESTÁVEL; os ícones do menu precisam ter TODOS o mesmo tamanho.

## 🆕 CONTEXTO NOVO (31/08 ~22h, commit `7466fe4` — NÃO reverta)
O menu agora **nasce ESCONDIDO por padrão** (o olhinho 👁 ABRE; quem já tinha escolhido, mantém a preferência). O acabamento abaixo vale para o menu **ABERTO** — quando a pessoa abrir, ele tem que estar perfeito.

## 🔍 DIAGNÓSTICO já feito (confira e corrija na raiz)
O `TopNav` é renderizado DENTRO do `<main>` de cada página, e cada página tem container próprio com largura/padding diferentes — por isso o menu "dança":
- `.estante-page`: **sem max-width e sem padding** → logo encostado no canto (0px)
- `.memoria-page`: max-width **1080px**, padding 16px
- `.writer-page`: max-width **880px**, padding 16px ← a queixa "no Writer está diferente"
- `.harness-page`: max-width **820px**, padding 16px
- `/video` usa outro esquema (`.igot-shell`); `/biblioteca` e `/ajuda` também têm os seus.

## 🎯 SOLUÇÃO ALVO (implemente assim)
1. **TopNav full-bleed com padding próprio, igual em TODAS as páginas:** no `.topnav` (em `app/globals.css`), use o truque de vazar do container pai sem editar página por página:
   `margin-inline: calc(50% - 50vw); width: 100vw; box-sizing: border-box; padding: 8px 20px 6px;` (mobile ≤640px: padding lateral 14px). O menu passa a ocupar a tela inteira com a MESMA margem interna em qualquer página — os containers de 1080/880/820 continuam valendo só pro CONTEÚDO (abaixo do menu).
2. **Logo + conjunto sempre no mesmo lugar:** logo (`.cafezinho-mark`/`.brand`) alinhado à esquerda a essa margem fixa; os 5 ícones (`SectionSwitcher`) logo ao lado; ações à direita — idêntico página a página. Confira visualmente uma a uma: `/estante`, `/memoria`, `/writer`, `/harness`, `/video`, `/biblioteca`, `/ajuda`, `/configuracoes`.
3. **Simetria de LINHAS (pedido novo do Miguel ~22h: "primeira e segunda linha, tudo mais simétrico"):** em telas estreitas o TopNav quebra em 2 linhas (linha 1: logo + ícones; linha 2: resto) — organize como GRADE: botões com a MESMA caixa e o MESMO espaçamento nas duas linhas, alinhados à esquerda (ou centrados, mas iguais), altura total previsível; nada de linha solta/desalinhada. Use flex/grid com `row-gap` uniforme.
4. **Ícones do menu TODOS do mesmo tamanho:** `.section-switch-btn` já tem caixa 46×46px (52px no mobile) — garanta que os 5 emojis renderizem do MESMO tamanho visual: `font-size` idêntico (ex.: 22px), `line-height: 1`, centralizados por flex (já tem). Se algum emoji ainda parecer maior/menor por desenho da fonte, corrija o alinhamento óptico individual com `transform: scale()` pequeno (0.95–1.05) — sem mudar a caixa. O estado ativo (pílula `active`) deve ter o MESMO tamanho nos 5.
5. **Não quebre:** capa (`/`) não usa TopNav (é limpa, só a bandeirinha — mantenha); o olhinho 👁 de esconder menu continua funcionando; o leitor tem menu próprio (não mexa).

## REGRAS
- Edite apenas CSS (de preferência só o bloco do `.topnav`/`.section-switch-btn`) — se precisar de JSX, mínimo possível; **zero texto novo em português** (i18n 12 idiomas).
- **SEM push/deploy** — o ZCode revisa e publica no Ousadia. Retorno: tag `ousadia-memoria-nuvem-20260831`.
- `npx next build` (em `apps/web`) sem erro.

## ENTREGA
1. Prints ANTES/DEPOIS de PELO MENOS: estante, memória, writer, harness, vídeo, biblioteca, ajuda, configurações — desktop ~1366px e celular ~375px (o antes você tira do site https://moka-ousadia.vercel.app; o depois do seu `next dev` local).
2. Sobreposição lado a lado provando que o logo está na MESMA posição x em todas as páginas (menu ABERTO, após clicar no 👁).
3. Lista do que mudou + adendo no fórum `Downloads/Antigravity Google/Cerebro/Foruns/forum_obra_moka_chefia_zm_20260830.md` (sem valores de credencial).

---
