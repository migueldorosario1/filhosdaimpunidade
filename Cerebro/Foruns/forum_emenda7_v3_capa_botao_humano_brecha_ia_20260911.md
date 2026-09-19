# Fórum — Emenda 7 v3: botão do humano + brecha IA na troca de capa (11/09/2026 ~23h)

**Ordem do Miguel (chat ZCode, 11/09 ~23h):** "tinha que botar um botão no wordpress para o humano mudar isso, e também botar uma brecha para a IA a serviço do humano mudar. não pode travar. tem como? mas nesse caso é melhor experimentar antes no espelho, para não corrermos risco."

**Contexto gatilho:** Miguel tentou 7× trocar a capa do post 270135 ("Lula emerge mais forte de uma semana difícil", autor 5786, publish) entre 21:16 e 22:57 de 11/09 — todas bloqueadas em silêncio pelo gate da Emenda 7 (`capa_sem_visao_casada_emenda7` no log, sempre `por:2018`). Até a isenção manual do gate-imagem-checada falhou porque ela não grava `media_id` (a Emenda 7 exige carimbo CASADO com a mídia nova).

## O que estava acontecendo (causa raiz)

O `cafezinho-gate-visao-capa.php` (Emenda 7 v2) protege posts de AGENTE publicados (publish/future/pending): troca de `_thumbnail_id` só passa com `_cafezinho_img_check.ok:true + media_id igual à nova mídia` (ou isenta com media_id igual). O editor do WP salva troca de imagem destacada via AJAX/REST sem carimbo → filtro `update_post_metadata` retorna 0 → WP descarta a troca SEM mensagem nenhuma — a foto "volta sozinha" e ninguém explica. O humano (§130) não tinha caminho nenhum. Casos anteriores no log: 268406 (31/08, por 2018) e 268763 DiCaprio (03/09, por 2018 e 5470).

## O que foi feito — Emenda 7 v3 (versão 1.2.0)

Arquivo: `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-gate-visao-capa.php` (produção, Tencent café alias `cafezinho-wp` = 190.89.239.65). Backup: `.bak_pre_v3_20260911` (md5 0dd466bc… = v2 original). Rollback = restaurar o .bak (e opcionalmente `wp post meta delete <id> _cafezinho_capa_liberacao`).

Quatro caminhos de decisão (em ordem):
1. **Carimbo casado / isenta casada** (original, intacto) — fluxo da fábrica (Tribunal Visual) segue igual.
2. **§130 AÇÃO HUMANA (novo):** usuário logado fora das contas-agente + `current_user_can('edit_others_posts')` → passa, com log `acao_humana_130`. Lista de contas-agentes: [5786, 5742, 5785, 5470, 5486, 5801, 5787–5798] (todas as contas-agentes são administrator no WP — capability NÃO filtra robô, a lista explícita filtra).
3. **Brecha IA-a-serviço (novo):** meta `_cafezinho_capa_liberacao` = {ts, expira, media_id (0=qualquer), por, motivo}, janela máx 24h (teto validado na leitura), log `brecha_ia_liberacao`. Gravável pela metabox do editor OU por wp-cli (sessão IA documentando a ordem); contas-agente NÃO gravam via REST (auth_callback).
4. **Bloqueio** (original) — log `capa_sem_visao_casada_emenda7`, idêntico à v2.

**O "botão":** metabox lateral "Capa — Emenda 7 (visão casada)" no editor de posts: mostra capa atual + carimbo casado/sem carimbo, explica a regra, e tem checkbox "Liberar troca de capa por 24h (IA a serviço, qualquer mídia)" + campo motivo. Post não protegido mostra 🟢 "troque à vontade".

## Provas

**Espelho primeiro (ordem do Miguel):** espelho vivo = `root@159.65.177.60:/var/www/cafezinho-news` (WP 7.0, DB própria `cafezinho_news`; o caminho antigo /var/www/cafezinho-news NO MESMO host de produção NÃO existe mais). Espelho estava desatualizado (não tinha o plugin) — instalado v2 de produção → **reprodução do bug: robo=false humano(2018)=false thumbnail_final=0**. Depois v3 → **bateria 10/10**: T1 robô sem nada BLOQUEIA · T2 humano §130 PASSA · T3 conta-agente(5786) logada BLOQUEIA · T4 brecha válida PASSA · T5 brecha expirada BLOQUEIA · T6 carimbo casado PASSA · T7 post autor humano PASSA · T8a alvo específico PASSA · T8b mídia fora do alvo BLOQUEIA · T9 janela 48h (teto 24h) BLOQUEIA. Posts de teste apagados.

**Produção (não-destrutivo, post 270135 real):** P1 uid0 → 0 (bloqueia) · P2 uid2018 → NULL (libera §130) · P3 uid5786 → 0 (bloqueia) · P4 metabox true · P5 capa intocada (270133) · P6 uid0 com liberação → NULL (libera brecha). Log registrou `23:11:46 por:2018 acao_humana_130` e `23:11:47 por:0 brecha_ia_liberacao` (consultas da prova; nenhuma troca real foi feita por nós).

**Estado do 270135:** capa continua 270133 (a escolha é do Miguel); brecha de 24h gravada (`expira 2026-09-12 23:11`, media_id 0, por wp-cli:ZCode-GLM-5.3, motivo com a ordem). Miguel agora troca direto no wp-admin sem precisar de nada.

## Como usar (receita)

- **Miguel/editores humanos:** abrir o post, trocar a imagem destacada normalmente e salvar — funciona em qualquer post (fica logado `acao_humana_130`). O espelho café ficou com a v3 instalada também.
- **IA a serviço (ZCode/CL/etc.):** gravar liberação via wp-cli e trocar: `wp post meta update <id> _cafezinho_capa_liberacao '{"ts":"…","expira":"…≤24h","media_id":0,"por":"wp-cli:<sessão>","motivo":"ordem Miguel <data> <origem>"}'` (datas com `current_time` do WP) → `wp post meta update <id> _thumbnail_id <midia>`.
- **Robôs da fábrica:** inalterado — precisam do carimbo casado (Tribunal Visual), como sempre.

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** trava diagnosticada com prova (log), v3 escrita, provada no espelho 10/10, aplicada em produção com backup, brecha 24h ativa no 270135, tudo auditável no log `_cafezinho_gate_visao_log`.
- **Falta:** nada bloqueante. Oportunidades: (a) os bloqueios de 3h do robô no post 268379 (desde 08/09) mostram um worker que tenta trocar capa sem carimbo casado — fluxo dele a revisar em outra ronda; (b) espelho café está desatualizado nos demais mu-plugins (só gate-img velho + agora o visão-capa v3) — sincronizar quando houver próxima manutenção.
- **Preciso do Miguel:** só confirmar que a troca no 270135 fluiu no wp-admin (2 cliques). Se quiser, a isenção `_cafezinho_img_isenta` antiga (sem media_id) pode ser limpa — ela não atrapalha, é só redundante.

— ZCode/GLM-5.3 · 11/09/2026 ~23:12 BRT
