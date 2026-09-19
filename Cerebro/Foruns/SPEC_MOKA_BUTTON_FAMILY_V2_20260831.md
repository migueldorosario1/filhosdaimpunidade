# 🎨 MOKA BUTTON FAMILY v2 — Spec do Diretor de Design (Claude, 31/08 ~22:2x)
> Resposta ao PROMPT A de padronização (Foruns/PROMPT_PADRONIZACAO_BOTOES_MOKA_20260831.md).
> Base: código real @ obra/memoria 49e5ddf (gist privado). Paleta Amanhecer Azul permanece.

## 1 · ESCALA (alturas FIXAS, nunca "padding que dá quase isso")
- **sm 36px** (padding 14, font 13/600, emoji 15) — SÓ desktop denso; PROIBIDO como alvo único no celular
- **md 44px** (18, 14.5/600, 18) — padrão universal (piso tátil)
- **lg 52px** (24, 16/700, 20) — ação PRINCIPAL no celular (Enviar/Adicionar/Salvar/CTA modal)
- **xl 64px+** (28, 17.5/700, 34) — SÓ 6 cards da capa + 3 pílulas do leitor
- **icon-sm 36×36 / icon-md 44×44 (gear já certo; emoji 19px) / icon-lg 52×52 (módulos TopNav mobile; emoji 23px)**
- Altura por `height`/`min-height` explícito — `.cloud-btn` (~41px) e `.bib-btn` (~36px) furaram por padding

## 2 · VARIANTES (tokens --btn-* v1.0 mantidos + --btn-danger-* + estados active/disabled)
- **primary**: grad 180deg #1e40af→#1e3a8a, texto #fff, borda rgba(255,255,255,.18); hover #2563eb→#1d4ed8 + translateY(-1.5px); active #172554 + scale(0.98); disabled opacity .45
- **secondary**: #fff/#0f172a/#e2e8f0; hover surface-alt #e2ebf6 + borda accent; active #dbeafe/#172554; dark #16161a/#2e2e36
- **ghost**: transparente, texto #475569, SEM sombra nunca; hover #dbeafe/#1e40af; active rgba(30,64,175,.14)+scale(.94)
- **danger (novo, outline)**: #fff/#b42318/borda rgba(180,35,24,.35); hover rgba(180,35,24,.06); dark texto #f87171 borda rgba(248,113,113,.4)
- **icon-chip**: quadrados acima + comportamento ghost; `.selected` = surface + --btn-shadow-rest (padrão do section-switch.active)
- Estados universais: hover -1.5px + shadow-hover (exceto ghost); active scale(.98); focus-visible 2px accent offset 2; disabled .45 sem sombra

## 3 · GEOMETRIA
- **UM raio de botão: 12px** (--btn-radius-md). Pílula 999 SÓ leitor + trilho section-switch. Cards 16px. Fim de 8/10/14/20.
- Sombras do kit (tingidas #0f172a, NUNCA preto nem o marrom rgba(60,40,15) que sobrevive em .llm-chip e capa-launch velho — extirpar)
- Transição 0.18s cubic-bezier(0.16,1,0.3,1) em TODOS (aposentar 0.15s ease avulsos)

## 4 · MENU 2 LINHAS NO CELULAR (aberto pelo 👁)
- Linha 1 (56px): [logo] [flex] [ações icon-chip 44×44, gap 8px]
- Linha 2 (64px): **grid repeat(5,1fr)** largura útil (100%−28px), gap 10px, célula centra icon-chip 52×52; separador 1px border-soft
- Ótica dos 5: font 23px/line-height 1 na caixa 52; scale: 📖×1.04 🎬×1.0 🧠×1.0 💬×0.97 ✍️×1.0 (faixa .95–1.05)
- Ativo: surface + shadow-rest + opacity 1; inativo .55. Desktop: caixas 46, gap 8, margem 20

## 5 · MAPA DE MIGRAÇÃO
| Velha | Vira | Nota |
|---|---|---|
| .section-switch-btn | icon-chip 46/52 | manter .active=selected |
| .gear + icon-btns topo | icon-chip md ghost | ok, herdar tokens |
| .topbar-help (34!) | icon-chip md | 34→44 |
| .shelf-icon-btn (40) | icon-chip md | 40→44 |
| .cfg-close-btn (36) | icon-chip md | 36→44 mobile |
| .cloud-btn | md secondary (.primary→md/lg primary) | |
| .cloud-provider-btn | md secondary r12; .active #dbeafe+borda accent | |
| .memoria-btn | md secondary; .big→lg; .primary→primary; .danger→danger | LIMPAR fallback #ff9e3d morto |
| .add-book-btn/.shelf-add-btn | lg primary mobile / md primary desktop | perde pílula |
| .clear-shelf-btn | md danger | |
| .bib-btn/.bib-btn-abrir | md primary/secondary | MORRE o teal #0f7680 e preto #1a1a1a |
| .book-memory-btn | md secondary | altura 44 |
| .llm-chip | md secondary | sombra marrom→kit; .none=borda danger |
| .tut-link | NÃO migrar (é link) | |
| .auth-signin | md secondary | |
| .topbar-about | link/tag ≥32 visual, alvo 44 por padding | |
| .summary-go/.paste-btn/.key-refresh-btn/.models-close-btn/.actions button | md (primary/ghost/secondary por papel) | |
| .video-delete-btn/.book-delete-btn (32 sobre thumb) | visual 36 + toque 44 via pseudo | |
| .reader-nav-bar button (38) | 44×44 na bandeja | |
| .tool-btn | icon-chip md c/ rótulo, min-w 72, alt ≥44 | |
| **EXCEÇÕES**: .capa-launch-btn (card xl r16), .reader-big-btn (pílula lg), .section-switch (trilho), .reader-nav-bar (bandeja) | mantêm forma, HERDAM tokens | |

## 6 · REGRAS DE OURO E ERROS
1. Todo botão novo nasce `moka-btn`+tamanho+variante; classe própria exige justificativa escrita.
2. Altura explícita + raio 12 + transição do kit — sempre os três juntos.
3. Cor SÓ por tokens do tema (nenhum hex direto — dark/contrast/sépia de graça).
ERROS: (1) migrar cor e esquecer o alvo; (2) viver de !important (ponte ok, destino = trocar classe no TSX e apagar a velha); (3) "consertar" as exceções.

Restrições: 5 módulos idênticos · capa sem menu · zero degradê no leitor · Amanhecer intacta · emojis seguem · i18n intocado · mobile-first.
