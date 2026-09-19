# 🎨 PROMPTS — PADRONIZAÇÃO DE BOTÕES E MENUS DO MOKA (Claude + Antigravity, em paralelo)

> Miguel joga os DOIS ao mesmo tempo (31/08 ~22h). Depois traz as duas respostas pro ZCode,
> que funde num plano único e aplica no rito (ZM revisa → publica no Ousadia).
> Arquivos reais do repo ATUALIZADO (branch obra/memoria @49e5ddf) na nuvem:
> **https://gist.github.com/migueldorosario1/db727617459afe206480ad9c7f854900**
> (gist privado — cada arquivo tem botão "Raw" no canto; contém: globals.css completo,
> TopNav.tsx, SectionSwitcher.tsx, Capa.tsx)

---

## 🅰️ PROMPT A — pro CLAUDE (diretor de design; resposta 100% em TEXTO)

Você é o **diretor de design do Moka** (app de leitura com IA; a casa pede: "botões padronizados, menus, tudo padronizado e BONITO DE VER NO CELULAR"). Sua entrega é uma **especificação textual precisa** que outro agente implementa sem te ver. **Leia os arquivos reais** deste link privado (são o código atual, já com as últimas reformas): https://gist.github.com/migueldorosario1/db727617459afe206480ad9c7f854900 — em especial o `globals.css` (procure as classes listadas abaixo) e os 3 componentes.

**Estado atual (contexto das últimas 24h de reforma):**
- Paleta "Amanhecer Azul" aplicada (fundo degradê ambiente #f4f7fb→#e8eef7; dark #0b132b→#0a0f22; accent cobalto #1e40af; cards da capa com pé azul; caixinha do ícone 48px r12 com degradê gelo 135°).
- Menu TopNav: **nasce ESCONDIDO** (o 👁 abre); full-bleed com margem própria (20px desktop / 14px mobile); 5 ícones de módulos (📖🎬🧠💬✍️) em caixas 46px (52 mobile); ações à direita (voltar, conta, bandeirinha, ⚙️, telemetria).
- Capa `/` limpa (sem menu): 6 cards idênticos + 2 cartões secundários; leitor: 3 botões-pílula + submenu; kit de tokens `--btn-*` v1.0 no fim do globals.css (variantes `.moka-btn` criadas e AINDA NÃO usadas em componente nenhum).

**O PROBLEMA (inventário real — confira no CSS):** cada tela criou botões próprios ao longo do tempo, com tamanhos e humores diferentes: `.section-switch-btn` (46px), `.gear`/icon-btns (~36-44px), `.cloud-btn` (10px 16px), `.memoria-btn` (.big/.primary/.danger), `.capa-launch-btn`, `.reader-big-btn`/`.reader-big-item`, `.add-book-btn`, `.clear-shelf-btn`, `.bib-btn`/`.bib-btn-abrir`, `.cloud-provider-btn`, `.llm-chip`, `.book-memory-btn`, `.tut-link`, `.cfg-close-btn`… No **celular** isso vira: alvos de dedo de tamanhos diferentes na MESMA tela, alturas que não batem, raios misturados (8/12/14/16/20/999), estados inconsistentes.

**SUA MISSÃO — desenhar a FAMÍLIA ÚNICA de botões do Moka ("Moka Button Family v2"):**
1. **Escala de tamanhos** (sm/md/lg/xl): altura EXATA em px de cada um, respeitando alvo tátil **≥44px** (e ≥52px pra ações principais NO CELULAR), padding horizontal, font-size/peso por tamanho. Diga onde cada tamanho é usado (menu ícone / ação de página / ação principal / card).
2. **Variantes** (primary / secondary / ghost / danger / icon-chip): fundo, borda, texto e estados **rest/hover/active/focus-visible/disabled** — tudo em hex/rgba sobre a paleta Amanhecer (reaproveite os tokens `--btn-*` existentes, ajustando o que precisar).
3. **Geometria comum**: raio único por família (defenda UM raio pra botões e UM pra cards), sombras (repouso/hover, sempre tingidas de safira), transição (a cubic-bezier já usada), foco de teclado.
4. **Menu de 2 linhas no celular:** como o conjunto (logo + 5 ícones de módulos + ações) fica SIMÉTRICO e estável quando quebra em 2 linhas — grade, alinhamento, espaçamentos exatos, tamanho ótimo idêntico dos 5 emojis (incluindo correção ótica por emoji se preciso).
5. **Mapa de migração:** para CADA classe do inventário acima, diga o que vira (ex.: `.cloud-btn` → `moka-btn md secondary`; `.gear` → `moka-btn icon ghost`…). Marque as exceções que têm motivo pra existir (pílulas do leitor, cards da capa).
6. **3 regras de ouro** de padronização e **3 erros** que implementadores costumam cometer nessa migração.

**Restrições fixas:** 5 módulos visualmente idênticos em importância; capa sem menu; dentro do leitor zero degradê (texto é protagonista); Amanhecer Azul permanece a base cromática; emojis seguem como ícones; nada de texto hardcoded (i18n 12 idiomas); mobile-first.

---

## 🅱️ PROMPT B — pro ANTIGRAVITY (auditoria independente + aplicação do consenso)

Você é o **auditor e acabador de interface do Moka** (repo `/home/migueldorosario/ZCodeProject/moka-app`, branch `obra/memoria`, app em `apps/web/src`; site-laboratório https://moka-ousadia.vercel.app). O diretor de design (Claude) está produzindo uma spec em paralelo — **você NÃO vai recebê-la agora**; sua missão tem 2 fases independentes.

**Contexto recente (não reverter):** menu TopNav nasce ESCONDIDO (👁 abre) e é full-bleed com margem própria (20px/14px); paleta "Amanhecer Azul" aplicada; kit de tokens `--btn-*` v1.0 no fim do `globals.css`.

### FASE 1 — AUDITORIA DE PADRONIZAÇÃO (entregue primeiro)
Tire prints no **CELULAR ~375px** e no **desktop ~1366px** de TODAS estas telas (use o site do Ousadia): `/` (capa), `/estante` (com e sem livros), `/biblioteca`, `/ajuda`, `/video`, `/memoria`, `/harness`, `/writer`, `/configuracoes`, um **livro aberto** (menu dos 3 botões + submenus abertos) e os **modais** (☁️ Memória na nuvem; 🎤 Perguntar; orçamento/confirmação). Para cada tela, verifique e anote com print:
1. **Alvo de dedo:** todo botão clicável tem ≥44px de altura/largura no celular (principais ≥52px)? Liste os que furam.
2. **Mesma tela, mesmo tamanho:** botões que aparecem juntos têm a MESMA altura e raio? (ex.: ações da estante, abas da memória, chips do harness, formulário da nuvem).
3. **Menu aberto (👁):** as 2 linhas no celular ficam SIMÉTRICAS (grade alinhada, mesmo espaçamento)? Os 5 ícones têm o mesmo tamanho ótimo (📖 engana)?
4. **Estados:** hover/active/focusconsistentes entre botões de mesma função?
5. **Margens:** logo e conteúdo respeitando a margem cheia (20px/14px) em todas as páginas?
Entregue: **tabela de defeitos** (tela → defeito → gravidade 1-3 → conselho de correção) + os prints numerados.

### FASE 2 — APLICAÇÃO DO CONSENSO (só o que independe do diretor)
Aplique, sem redesign e SEM mexer na paleta Amanhecer:
1. **Simetria do menu de 2 linhas** no celular: transforme o conjunto em grade com caixas e espaçamentos idênticos (`.topnav`/`.section-switch`).
2. **Tamanho ótimo dos 5 ícones** idêntico (font-size + line-height iguais; correção ótica por emoji via scale 0.95–1.05 sem mudar a caixa).
3. **Unificação óbvia de touch:** todo botão de ação de página que estiver <44px sobe para ≥44px (mantendo o desenho); raios de BOTÃO convergem num único valor (o `--btn-radius-md` do kit) exceto pílulas do leitor e cards da capa.
4. Nada de texto novo hardcoded (i18n 12 idiomas); edite apenas `apps/web/src`.

**Regras:** `npx next build` limpo; **SEM push/deploy** (o ZCode revisa e publica; retorno = tag `ousadia-memoria-nuvem-20260831`); ao final, registre adendo no fórum `Downloads/Antigravity Google/Cerebro/Foruns/forum_obra_moka_chefia_zm_20260830.md` com a tabela + o que aplicou (sem valores de credencial).

---
