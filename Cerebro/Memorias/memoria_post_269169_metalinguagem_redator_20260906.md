# MEMÓRIA TÉCNICA — Forense do post 269169 ("matéria-metalinguagem") — redator gpt-5.6-sol do V4.1 ciência

**Data:** 06/09/2026 23:33→23:5x BRT · **Agente:** ZCode (Qwen3.8-Max, Dell) · **Fórum-irmão:** `Foruns/forum_post_269169_metalinguagem_redator_20260906.md`

## Linha do tempo (provas)

| Quando (BRT) | O quê | Prova |
|---|---|---|
| 05/09 21:45:57 | Criação do draft 269169 via REST (python-requests/2.32.5, user 5470) | meta `_cafezinho_origem`; nginx `POST /wp-json/wp/v2/posts/269169` 21:46:24 |
| 05/09 21:45 | Ciclo V4.1 ciência job `d139f5fb1c7b5ad4`: curadoria aprova tese; redator **gpt-5.6-sol** devolve ok=true, title «Matéria aguarda confirmação do Google», 971 chars; fc sonnet ok=False; capa 0; status `rascunho_v41_curto` | NYC `/root/v4_labs/dados/v41_ciclo/20260905_2145.json` |
| 06/09 23:10:52 | Revisão r1 **glm-5.3+web** ok=false + write-back de meta (parecer identificado como não-matéria) | meta `_cafezinho_txt_check.r1`; nginx POST 23:10:52 |
| 06/09 23:20:15 | Revisão r2 **gpt-5** ok=false + sugestão de título meta + write-back | meta `_cafezinho_txt_check.r2`; nginx POST 23:20:15 |
| 06/09 23:30:41 | Miguel abre o post no wp-admin (GET edit) | nginx access log |
| 06/09 23:34:15 | Miguel move para a lixeira (`action=trash`) | nginx 302 + meta `_wp_trash_meta_status=draft`, `_wp_trash_meta_time=1788748453` |

## Evidências brutas (essenciais)

- `wp post get 269169`: post_author=5470 (user_login "Redator", display "Redação"); post_status=trash (antes: draft); post_title «Matéria aguarda confirmação do Google»; sem revisões (`wp post list --post_type=revision --post_parent=269169` vazio).
- Metas decisivas: `zizi_job_id=v41_ciencia_d139f5fb1c7b`; `_v4_versao=4.1`; `_v41_fc` (claims confirma/contradita sobre Gemini Spark); `_cafezinho_txt_check` (r1 glm-5.3+web 23:10, r2 gpt-5 23:20, ambos ok=false); `_cafezinho_frescor` nota 4 (29,2h); `_wp_trash_meta_status=draft`.
- Ciclo (NYC): `redator_out={"ok": true, "id": 269169, "status": "draft", "title": "Matéria aguarda confirmação do Google", "content_chars": 971, "model": "gpt-5.6-sol"}`; `fc_websearch.ok=False`, `fc_por=sonnet`; `capa_candidatas=0`; `curadoria_estado=tese_dinamica_aprovada`; vertical `ciencia`.
- Gate de mídia (`agent_data/v4/media/pipeline_decisions/ad9008…json`): `no_eligible_image`, `blocked=false`, `draft_allowed=true` → draft sem capa permitido; publish exigiria capa (nunca chegou lá).
- Conteúdo no trash = 3 parágrafos de parecer ("Não há fonte pública verificável… A matéria deve permanecer como rascunho até que uma página oficial e pública do Google confirme…").

## Comandos usados (receita de forense WP)

```bash
ssh cafezinho-wp 'cd /var/www/ocafezinho && sudo -u www-data wp post get 269169 --fields=ID,post_author,post_date,post_modified,post_status,post_title'
ssh cafezinho-wp 'cd /var/www/ocafezinho && sudo -u www-data wp post meta list 269169'
ssh cafezinho-wp 'cd /var/www/ocafezinho && sudo -u www-data wp post list --post_type=revision --post_parent=269169 --fields=ID,post_author,post_date,post_title'
ssh cafezinho-wp 'zcat -f /var/log/nginx/access.controle.ocafezinho.com.log* | grep 269169'   # logs POR DOMÍNIO (access.log genérico não existe)
ssh nyc 'cat /root/v4_labs/dados/v41_ciclo/20260905_2145.json'   # ciclo completo da esteira V4.1
# varredura de irmãos:
ssh cafezinho-wp 'cd /var/www/ocafezinho && sudo -u www-data wp db query "SELECT ID, post_title FROM wp_posts WHERE post_status IN (\"draft\",\"pending\") AND (post_content LIKE \"%permanecer como rascunho%\" OR post_content LIKE \"%Não há fonte pública%\" OR post_title LIKE \"%aguarda confirmação%\")"'
```

Armadilhas encontradas: wp-cli como root exige `--allow-root` ou `sudo -u www-data`; `wp revision list` NÃO existe (usar `wp post list --post_type=revision --post_parent=`); `wp post list --after` retornou o total (não filtrou) — usar SQL direto; logs nginx são por domínio (`access.controle.ocafezinho.com.log*`); IPs no log são bordas Cloudflare (a origem real só via meta `_cafezinho_origem.ua`).

## Diagnóstico final

- **Quem alucinou:** redator **gpt-5.6-sol (OpenAI)** da esteira **V4.1 vertical ciência** (user 5470). Não foi V4.2.
- **Por quê:** tese aprovada pela curadoria com material sem fonte primária; o redator, incapaz de afirmar fatos não confirmados, escreveu o próprio veredito de cautela como se fosse matéria e marcou `ok=true` (deveria ter falhado fail-closed). A esteira aceitou `ok=true` sem checagem de FORMA do conteúdo.
- **Travas:** as de publicação TODAS funcionaram (fc sonnet ok=False; gate de imagem fail-close; txt_check r1/r2 fail-close; status draft do nascimento à lixeira; 0 views). Faltam travas ANTERIORES: gate de forma/contrato do redator, régua de título anti-meta, alarme de rascunho velho (fila de 2.431 drafts escondeu o caso por ~26h).
- **Saúde:** home 200/0,99s; wp-login 200; arquivo do dia 200/3,9s; 0 PHP Fatal hoje; 31 publicados hoje; esteira V4.1 viva (ciclos 21:45/22:05/22:35/23:22 de 06/09).
- **Créditos (vigília 23:35):** kimi 4% ok · qwen 14% ok · DeepSeek US$ 25,48 · Grok US$ 7,99 · **GLM semana 94% (🔴 na régua da casa; janela 5h 3%, renova ~09/09)**.

## Estado / próximos passos

Post na lixeira (decisão do Miguel). Provas preservadas (este arquivo + fórum + print do Miguel em `Outros/passagem/Captura de tela de 2026-09-06 23-32-48.png`). Cura proposta (AGUARDA "vai" do Miguel): (1) gate de FORMA na saída do redator V4.1 (marcadores de parecer/metalinguagem ou título-status ⇒ ok=false + alarme); (2) varredura única dos 2.431 rascunhos com a régua; (3) SLA/alarme de rascunho sem revisão. Catalogado: `CEREBRO_NODE_BUGS_ATIVOS.md` (BUG-20260906-V41-REDATOR-METALINGUAGEM) + `CEREBRO_NODE_ATUALIZACOES.md` + monitor ✅.
