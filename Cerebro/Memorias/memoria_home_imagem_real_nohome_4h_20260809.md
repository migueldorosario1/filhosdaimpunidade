# Memória — Home com imagem real e No Home temporário

Em 9 de agosto de 2026, Miguel definiu que imagens artificiais recebem `No Home` durante a janela editorial de quatro horas, após a qual o removedor histórico pode desmarcar a categoria. A home deve usar imagens boas e reais; a Manchete nunca pode usar imagem artificial.

O removedor foi reativado no NYC (`0 */2 * * *`, limiar 4h; efeito prático 4–6h). O V4 passou a persistir `cafezinho_image_kind` e `cafezinho_image_generator` no post e na mídia. O MU plugin `cafezinho-real-image-gate.php` filtra IA da front page e bloqueia sua escolha como Manchete.

O primeiro teste real encontrou a Manchete 264832 com ilustração Flux Pro e a retirou da renderização da capa, sem promover substituta automaticamente.

Detalhes, backups e rollback: `Cerebro/Foruns/forum_home_imagem_real_nohome_4h_20260809.md`.
