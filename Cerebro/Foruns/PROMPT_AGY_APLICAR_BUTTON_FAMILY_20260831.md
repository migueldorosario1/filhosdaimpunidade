# 🎨 PROMPT — ANTIGRAVITY: aplicar a MOKA BUTTON FAMILY v2 (spec do diretor Claude)

> Fase final da padronização (31/08 ~22h). A spec integral está em
> `Downloads/Antigravity Google/Cerebro/Foruns/SPEC_MOKA_BUTTON_FAMILY_V2_20260831.md`
> — o prompt abaixo aponta o arquivo (você tem acesso local) e traz as salvaguardas.

---

PROMPT (cole no Antigravity Desktop):

Você é o implementador-chefe de interface do **Moka** (repo `/home/migueldorosario/ZCodeProject/moka-app`, branch `obra/memoria`, app `apps/web/src`). O diretor de design (Claude) entregou a **Moka Button Family v2** — leia e sigue INTEGRALMENTE esta spec: `Downloads/Antigravity Google/Cerebro/Foruns/SPEC_MOKA_BUTTON_FAMILY_V2_20260831.md` (escala sm/md/lg/xl com alturas explícitas, variantes primary/secondary/ghost/danger/icon-chip com estados completos, geometria comum — raio único 12px pra botão, sombras do kit tingidas de #0f172a, transição do kit —, menu de 2 linhas em grade `repeat(5,1fr)` com correção ótica dos 5 emojis, e o MAPA DE MIGRAÇÃO de ~25 classes).

## COMO TRABALHAR (ordem que protege a obra)
1. **Fase CSS primeiro:** complete o kit no fim do `globals.css` com o que falta da spec (`--btn-danger-*`, estados `active`/`disabled` universais, classes de tamanho `.moka-btn--sm/--md/--lg/--xl` e `icon-chip`) SEM remover nada do que existe.
2. **Migração TELA POR TELA, na ordem do mapa** (estante → memória → harness → writer → configuracoes → biblioteca → ajuda → vídeo → capa/leitor conferência das exceções): troque a classe no TSX e APAGUE a regra antiga do CSS (a spec manda: não viver de `!important`). Um commit mental por tela — se algo quebrar, você sabe exatamente onde.
3. **Menu TopNav 2 linhas:** grade `repeat(5,1fr)` na linha dos módulos no mobile (gap 10px, caixas 52, linha 1 com ações icon-chip 44 gap 8, separador 1px), correção ótica por emoji via scale (📖×1.04, 💬×0.97) SEM mudar caixa.
4. **Extirpar:** fallback laranja morto `var(--accent, #ff9e3d)`, sombras marrons `rgba(60,40,15,…)`, teal `#0f7680` e preto `#1a1a1a` dos botões da biblioteca — cor só por token.
5. **Nas 4 EXCEÇÕES** (cards da capa, pílulas do leitor, trilho do menu, bandeja de navegação): mantêm a forma própria, só HERDAM sombra/transição/estados do kit.

## INEGOCIÁVEIS
- `npx next build` (em `apps/web`) SEM erro; **SEM push/deploy** (o ZCode revisa e publica no Ousadia; retorno = tag `ousadia-memoria-nuvem-20260831`).
- Zero texto novo em componentes (i18n 12 idiomas); nada de hex direto em botão; focus-visible jamais suprimido.
- 5 módulos idênticos; capa sem menu; zero degradê no leitor; Amanhecer Azul intacta.

## ENTREGA
1. Tabela "classe velha → nova" com check das migradas (na ordem do mapa da spec).
2. Prints ANTES (Ousadia) × DEPOIS (seu `next dev` local): **celular 375px e desktop 1366px** de: estante, memória, harness, writer, configurações (formulário da nuvem), biblioteca, capa e livro aberto (menu dos 3 botões + submenus).
3. Print do menu 👁 ABERTO no celular mostrando a grade de 5 simétrica.
4. Adendo no fórum `Downloads/Antigravity Google/Cerebro/Foruns/forum_obra_moka_chefia_zm_20260830.md` com a tabela + caminhos dos prints (sem valores de credencial).

---
