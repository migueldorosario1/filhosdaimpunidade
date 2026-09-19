# PRONTO — Moka Reader: uma barra de menu só quando o livro está aberto (ordem do Miguel, 18/09/2026)

**Pedido do Miguel (voz, 18/09 ~10:3x):** "os menus — eu tinha falado para colocar sempre o menu; a gente tem basicamente dois menus agora, duas linhas de menu. Quando a gente está lá dentro da página de trabalho, com o livro aberto, ficam dois menus lá de cima: o de cima tem a opção (marca, vídeo, Moka, pensamento e tudo) e tem a linha de baixo, que a gente conseguiu simplificar — agora tá juntando tudo só em três itens de menu que abre submenu. A primeira linha de menu lá em cima ficou feia quando abre o livro. Quando abre o livro era bom não ter mais essa barra de menu: ficar uma barra só, que o menu de trabalho não fica repetitivo."

**Objetivo:** dentro do leitor de livro, UMA barra de menu só. A barra de trabalho (a de cima) não aparece durante a leitura; a barra simplificada (3 itens + submenu) permanece e continua dando acesso a tudo.

## Hipótese de causa (a confirmar pelo dono do código)

O leitor é a rota `book/[id]` do Moka Reader (mokareader.com · Next.js/Vercel · branches `main` e `ousadia`). Pelo fórum de 15/09 (`forum_moka_topnav_global_20260915.md`):

- antes, `book/[id]` era `workspace-no-topbar` por design — a prateleira do livro não tinha menu nenhum;
- a cura de 15/09 **acrescentou o TopNav** na `book/[id]` (com `active="reader"`) no return principal e nos 3 estados antecipados;
- resultado provável: hoje o leitor empilha DUAS camadas de navegação — a barra de trabalho (TopNav) + a barra simplificada de 3 itens com submenu — que é exatamente a duplicação relatada.

## Prescrição (o que fazer)

1. Na rota do leitor (`book/[id]`, incluindo os estados loading / loadStuck / notFound), renderizar **apenas a barra simplificada** (os 3 itens com submenu).
2. A barra de trabalho (a de cima, com os itens de ferramenta) **não renderiza** durante a leitura — nem em versão reduzida, nem como sobra de layout.
3. Manter alcançáveis, na barra que fica: 🏠 (voltar à página central), 🏳️ idioma, ⚙️ configurações e o olhinho 👁️ de mostrar/ocultar — a regra de 15/09 ("a prateleira nunca fica sem menu") continua valendo, só que com UMA barra.
4. A preferência de mostrar/ocultar menu (`moka.navHidden2`) continua respeitada: se o leitor escondeu o menu, o livro aberto abre limpo como sempre.
5. Ao sair do livro (voltar para estante/biblioteca/home), a barra de trabalho volta ao normal — a mudança vale só dentro da leitura.
6. Não mexer no conserto de 15/09 da fonte ampliada: o `.topnav` usa `margin-inline: calc(50% - 50vw / var(--ui-font-scale, 1))` e o `.topnav-hidden { justify-content: flex-end }` re-declarado depois da segunda `.topnav` — a barra única tem que herdar essas duas curas, senão o estouro com fonte grande volta.

## Testes de aceitação (provar com print/screenshot)

1. Abrir um livro no celular: contar as barras — **uma só**, e é a de 3 itens com submenu.
2. Nas configurações, subir a fonte para 140% e depois descer para 85% com o livro aberto: a barra não estoura, nada fica fora da tela, o olhinho continua clicável no canto.
3. Com o livro aberto: chegar em 🏠, idioma, ⚙️ e no submenu dos 3 itens em no máximo dois toques.
4. Esconder o menu (olhinho) com o livro aberto, fechar e reabrir o app: a preferência sobrevive e o livro abre limpo.
5. Sair do livro para a estante: a barra de trabalho reaparece inteira, sem item faltando e sem duplicação.
6. Nos três estados de exceção (carregando, travado, livro não encontrado): uma barra só, com a saída (🏠) acessível.

## Observação de escopo

O pedido é de navegação, não de conteúdo: nenhum item de menu é removido do produto — a barra de trabalho continua existindo em todas as outras páginas. Dentro do livro ela só deixa de se repetir.

— registrado por DSH-us65 (DSC) · 18/09/2026 · para o ZM executar
