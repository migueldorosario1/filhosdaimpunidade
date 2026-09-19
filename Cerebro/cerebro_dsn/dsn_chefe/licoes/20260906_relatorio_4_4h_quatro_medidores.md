# Lição — Relatório 4/4h com os QUATRO medidores (GA4 · FAROL · LUMINA · SOL)

**Data:** 06/09/2026 (~12:30 BRT) · **Origem:** áudios do Miguel 12:07/12:08/12:22 ("cadê o GA4?", "usa o sol", "são quatro")

## O quê
O relatório de 4 em 4 horas ao Miguel deve trazer SEMPRE os quatro medidores de audiência, cada um com o número da hora: GA4 (Google Analytics 4), FAROL, LUMINA e SOL. No relatório 12:00 vieram FAROL e LUMINA; faltaram GA4 e SOL — o Miguel cobrou nos dois áudios seguidos (e no terceiro reforçou que SOL não é LUMINA, "são quatro, tá?").

## Por quê
O Miguel acompanha a audiência por quatro fontes independentes e quer o quadro completo de uma vez, sem ter que caçar cada medidor. A constelação está documentada no próprio painel (comentário do bloco sol_dados em painel_cctv_v6.py): GA4 · FAROL · LUMINA · SOL. Fonte nova: SOL = WP Statistics no us65, contador batizado em 01/09/2026 por ordem dele ("página no CCTV, como tenho GA4, FAROL, etc." — forum_sol_painel_cctv_20260901.md, commit 5bbdd153d), página pública http://43.156.151.165/v6/sol, dados via endpoint privado controle.ocafezinho.com/sol_cctv.php (token sol_token), invisível no site público.

## Como aplicar
- Em TODO relatório 4/4h (00/04/08/12/16/20): uma linha com os quatro — GA4 (views_ga4 da última ts do farol_audiencia.db · online/hoje do LUMINA (lumina_audiencia.jsonl) · online/humanos+robôs do FAROL (db ts) · online/visitas hoje/total do SOL (curl no endpoint privado com o token local, sem expor o token).
- Fonte dos números por medidor: GA4 = coluna views_ga4 da tabela medicoes (farol_audiencia.db); FAROL = extra JSON da mesma tabela (online_30min_humanos/bots, hoje_navegacoes); LUMINA = última linha de v6_data/lumina_audiencia.jsonl (coletado_em é o ts confiável); SOL = endpoint sol_cctv.php (mesmos números da página /v6/sol).
- SOL ≠ LUMINA: LUMINA é o medidor de visitas ao vivo (Matomo/Umami do servidor do site, 🌙); SOL é o WP Statistics (us65, ☀️, conta desde 01/09). FAROL é o que separa humanos de robôs (👤+🤖).
- 400490 (vigília DSC-064) é post V4.2 que mora SÓ no espelho cafezinho.news — 404 no canônico www é NORMAL (não é alarme).
