# MEMÓRIA TÉCNICA — EXCERTO 300 CURA DE RAIZ (28/09/2026, ZM-CHEFIA)

Arquivos tocados:
- NYC /root/v4_labs/codigo/v4_vertical_redactor_runtime.py — backup .bak_pre_zm_excerto300_20260928; novo helper _fechar_excerto() antes de _post_draft; chamada `excerpt = _fechar_excerto(_plain(article.get("excerpt")))`; prompt (linha ~187) ganhou bloco "EXCERTO (ordem do Miguel 28/09)" exigindo material próprio ≤280 autossuficiente. py_compile OK.
- WP /var/www/ocafezinho/wp-content/mu-plugins/cafezinho-gate-dois-checks.php — backup .bak_pre_zm_excerto_gate_20260928; filtro consultivo de excerto anexado (priority 9); php -l OK.
- Banco: 42 drafts + 2 publicados (autor 5470) com post_excerpt recortado no último [.!?]; backups JSON em /root/backups_zm_excerto_{draft,publish}_20260928.json.

Comandos/provas:
- Prova unitária: exec do helper isolado → CASO1 215 chars termina "."; CASO2 295 termina "…"; curto intacto.
- Lista estoque: wp db query CHAR_LENGTH(post_excerpt) BETWEEN 250 AND 300 AND RIGHT(...,1) NOT IN ('.','!','?','…','»','”',')',']').
- Reparos: wp eval-file /tmp/fix_excertos.php com env ZM_STATUS (draft|publish) — wp eval-file NÃO passa $argv além do script.
- Pós: mesma query retorna 0 draft/0 publish (1 trash ignorado).

Armadilhas aprendidas:
- wp eval-file ignora argumentos posicionais → usar getenv.
- Cura parcial anterior (fronteira de palavra) mascarou a causa: assinatura 290-300 chars persistiu 1 dia inteiro.
- Bash heredoc via ssh com aspas PHP/regex = escrever arquivo local + scp.

Ciclo de aprendizagem (CLG item 6): regra = "gate automático + instrução do redator"; prova de incorporação = helper no redator + filtro no gate2c + prompt novo + estoque zerado.

— ZM · ZCode/qwen3.8-max · 28/09/2026 10:36
