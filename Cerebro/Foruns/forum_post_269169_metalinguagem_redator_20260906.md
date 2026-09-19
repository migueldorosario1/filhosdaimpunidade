# FÓRUM — Post 269169: a "matéria-metalinguagem" (parecer de revisão virou conteúdo) — quem fez, por quê, e o estado das travas

**Data:** 06/09/2026 ~23:3x–23:5x BRT · **Agente:** ZCode (Qwen3.8-Max, Dell) · **Ordem do Miguel:** "verificar qual inteligência alucinou e publicou isso… quem foi? foi o V4 de tecnologia? por quê? cadê as travas?"

## O que era o post 269169

Título «Matéria aguarda confirmação do Google», conteúdo = 3 parágrafos de PARECER DE REVISÃO ("Não há fonte pública verificável no material fornecido que confirme a existência do Gemini Spark… A matéria deve permanecer como rascunho até que uma página oficial do Google confirme…"). Não é matéria jornalística: é o veredito interno de uma revisão escrito DENTRO do campo de conteúdo, com título de aviso de status. Metalinguagem pura.

## Veredito (cadeia de provas)

1. **Autoria:** usuário WP 5470 = "Redator"/"Redação" (user de robô). Criação em **05/09 21:45:57** via REST (`python-requests/2.32.5`), meta `_cafezinho_origem`. Access log nginx: `POST /wp-json/wp/v2/posts/269169` em 05/09 21:46:24.
2. **Esteira:** meta `zizi_job_id=v41_ciencia_d139f5fb1c7b` + `_v4_versao=4.1` → **V4.1, vertical ciência/tec** (NÃO é o V4.2 Investimento). Ciclo `/root/v4_labs/dados/v41_ciclo/20260905_2145.json` (NYC): pauta «Google Fotos ganha IA que edita, organiza e compartilha fotos sozinha»; `curadoria_estado=tese_dinamica_aprovada`; **`redator_out={"ok": true, "id": 269169, "status": "draft", "title": "Matéria aguarda confirmação do Google", "content_chars": 971, "model": "gpt-5.6-sol"}`**.
3. **Quem alucinou:** o **REDATOR gpt-5.6-sol (OpenAI)** do V4.1 ciência. Recebeu tese aprovada com material fraco (mobilebit.com.br + TechCrunch 04/09, sem fonte oficial do Google) e, em vez de falhar (`ok=false`), devolveu `ok=true` com o PRÓPRIO VEREDITO de cautela como conteúdo e um título de status. Falha de contrato do redator, não do fact-check.
4. **Fact-check e revisores agiram CERTO:** `fc_websearch.ok=False` (fc_por=sonnet, claims "contradita"); `_cafezinho_txt_check` r1 = **glm-5.3+web** 06/09 23:10 ok=false ("rascunho 269169 não é matéria jornalística, é parecer de revisão… sugiro retorno ao fluxo de pauta"); r2 = **gpt-5** 06/09 23:20 ok=false (e ainda sugeriu título meta: "O Cafezinho mantém matéria em rascunho por falta de confirmação do Google"). POSTs de write-back no access log: 23:10:52 e 23:20:15.
5. **Nunca foi publicado:** `_wp_trash_meta_status=draft` (nasceu rascunho, morreu rascunho); Statistics 0 views; capa 0 (`capa_candidatas=0`, gate de imagem fail-close: `draft_allowed=true` só para draft). Miguel abriu no wp-admin 23:30:41 e **moveu para a lixeira 23:34:15** (access log + `_wp_trash_meta_time`).
6. **Sem revisões WP registradas** (updates via REST sem revision) e **sem irmãos**: varredura SQL de rascunhos/pending com cara de parecer ("permanecer como rascunho", "Não há fonte pública", "aguarda confirmação", "parecer de revisão") = 0 resultados. Caso isolado.

## Cadê as travas? Tudo se perdeu?

**NÃO.** As travas de PUBLICAÇÃO seguraram tudo: fact-check reprovou, gate de imagem fail-close sem isenção, txt_check r1/r2 fail-close, slot/gates mantiveram status draft, 0 views no front. O buraco é ANTES: (a) não existe gate de FORMA/contrato na saída do redator (aceitou `ok=true` com conteúdo-parecer e título-meta); (b) o rascunho dormiu ~26h numa fila de **2.431 rascunhos** até a revisão encostar nele (23:10 de 06/09); (c) nenhuma regra de título barra padrões meta ("aguarda confirmação", "mantém em rascunho").

## Saúde do site e créditos (23:3x)

- Site: home 200 em 0,99s · wp-login 200 · arquivo do dia 200 (3,9s) · 0 PHP Fatal hoje · **31 publicados hoje** (esteira viva) · 2.431 rascunhos · 111 na lixeira.
- Créditos: 🟢 Kimi K3 4% da janela · 🟢 Qwen3.8 14% · 🟢 DeepSeek US$ 25,48 · 🟢 Grok US$ 7,99 · **🔴 GLM: semana 94% consumida** (janela 5h livre, 3%; renova ~09/09) — único provedor em zona de risco; r1 dos revisores usa glm-5.3+web, atenção se a semana estourar.

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** forense completa (autor, esteira, modelo, horários, logs); post já na lixeira por decisão sua; provas preservadas aqui e na memória-irmã; caso catalogado em `CEREBRO_NODE_BUGS_ATIVOS.md` (BUG-20260906-V41-REDATOR-METALINGUAGEM).
- **Falta (aguarda seu "vai"):** (1) gate de FORMA no redator V4.1 (rejeitar `ok=true` quando o conteúdo tiver marcadores de parecer/metalinguagem ou o título tiver padrão de status — fail-closed com alarme no Telegram); (2) varredura única dos 2.431 rascunhos com a mesma régua; (3) SLA/alarme de rascunho velho sem revisão (fila grande esconde anomalia).
- **Preciso de você:** dizer se aplico os 3 itens acima (mexem em código no NYC/canônico) ou se só vigio. Se quiser restaurar o post para leitura, ele está na lixeira (`wp post update 269169 --post_status=draft`); para sumir de vez, esvaziar a lixeira.

**Tema Duplo:** memória-irmã `Memorias/memoria_post_269169_metalinguagem_redator_20260906.md` (log técnico completo com comandos e evidências brutas).
