# Fórum — Link spam de cassino no menu do Cafezinho + trava de auto-add (2026-08-06)

> **Tema Duplo:** memória técnica completa em `Memorias/memoria_menu_spam_cassino_autodd_20260806.md`.

## O que aconteceu

06/08 ~11:28 BRT: a página **"O jogo do balão no Brasil: como funciona este popular jogo de cassino"** (ID 264513, slug `o-jogo-do-balao-no-brasil-como-funciona-este-popular-jogo-de-cassino`) foi publicada no WP do Cafezinho pelo usuário **rhyandemeira** (ID 5749, role **editor**, conta criada em 2023). Como a opção **"adicionar novas páginas ao menu automaticamente"** (`nav_menu_options.auto_add`) estava LIGADA para os menus `Menu` (21062 — o menu do topo E do rodapé/AMP) e `apptha` (1279 — legado, não exibido), a página entrou sozinha no menu visível do site.

Miguel flagrou no chat: "entrou um link estranho no menu de cima e no de baixo — tira e trava".

## Decisões / ações (ordem direta do Miguel, 06/08)

1. ✅ **Itens de menu removidos:** `nav_menu_item` 264519 (menu 21062) e 264518 (menu 1279/apptha) deletados via wp-cli. Backup prévio em `/root/backup_menu_fix_20260806/` no servidor.
2. ✅ **Menu travado:** `nav_menu_options.auto_add = []` — **nenhuma página nova entra mais automaticamente em NENHUM menu** (só entra se alguém adicionar manualmente em Aparência → Menus). Cache WP Rocket purgado.
3. ✅ **Verificado ao vivo:** homepage com 0 ocorrências de "balão"/"cassino"; menu topo+rodapé só com Quem somos?/Editorias/categorias.

## ✅ DECIDIDO (Miguel, 06/08 ~12:30 BRT)

- **Os publis são AUTORIZADOS** — o Rian (rhyandemeira) publica esse conteúdo pago com aval do Miguel. **Nada a apagar/suspender**: página 264513 fica no ar, conta fica ativa, publis continuam saindo normalmente.
- **A única regra violada era o menu** — e essa já está resolvida: com `auto_add=[]`, publi novo publica normal mas **nunca mais aparece no menu**.
- **Por que entrou no menu (linha do tempo confirmada):** o menu visível (21062) foi **recriado em 30/07 ~18:08** (todos os itens atuais têm esse timestamp) — na tela de criação de menu do WP, a caixa "adicionar novas páginas automaticamente" vem **marcada por padrão**. O menu legado `apptha` (1279, sem exibição) tem auto-add há anos — por isso os publis antigos (MostBet, etc.) estão todos lá (itens 256654, 258668, 261670…) mas nunca tinham aparecido no menu visível. **O balão foi o 1º publi publicado depois da recriação do menu → 1º a vazar pra vitrine.**

## Como NUNCA mais acontece

- Auto-add desligado permanentemente (item 2). Nova página só aparece no menu se um humano adicionar no wp-admin.
- Se um dia quiserem reativar: `wp option update nav_menu_options '{"auto_add":[21062]}' --format=json` (não recomendado).

— ZCode (Kimi K3), 2026-08-06
