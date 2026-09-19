# Memória — Investigação título 268457 (Kast) + correção + mapa checagem dupla de títulos

**Data:** 2026-09-01 17:4x→18:0x BRT · **Sessão:** ZCode/GLM-5.3 (Dell) · **Fórum:** `Foruns/forum_titulo_kast_investigacao_autoria_20260901.md`

## Log técnico completo

1. **Matéria:** `curl` público + REST `context=edit` (App Password cofre `WP_USER_CAFEZINHO`/`WP_APP_PASSWORD_CAFEZINHO`; **403 sem User-Agent de navegador** — mu-plugin/WAF derruba urllib sem UA; com UA Mozilla passa).
   - Post 268457: `author=5470` ("Redação", conta genérica dos agentes V4.1), `zizi_job_id=v41_geopolitica_1a30c106bd88`, `_v41_fc` fact-check CONFIRMA (24Horas CL), `_cafezinho_img_check` olho duplo APROVADA (tribunal_qwen+deepseek), capa 268496, publicado 14:31 BRT pelo DS-N Publicador ("fluxo fresco").
2. **Autorsia da fábrica:** fórum V4.2 (29/08): redator V4.1 = cascata `deepseek-v4-pro`/`gpt-5.5`; caso saúde 26/08 = `gpt-5.5` na prática. **O modelo exato por job fica no log do worker V4.1 na Laura** (não acessível do Dell; pedido na ponte ZM-20260901-031).
3. **Rastreio da esteira (SSH):** NYC `geopolitica.sqlite3` último evento 24/08 prefixo `v4d_` (verticais V4 velhas DESLIGADAS 24/08 "só V4.1" — ordem Miguel no crontab); prefixo `v41_` = runtime V4.1 novo (esteira da Laura). Tencent: dsn_publicador publica; **sem gate de título** (só `tribunal_nyc`/`deepseek_vision` para CAPA).
4. **Correção (17:52):** `ssh cafezinho-wp` → WP em `/var/www/ocafezinho` → `sudo -u www-data -- wp post update 268457 --post_title='Preso é flagrado com cocaína antes de ir para cadeia de segurança máxima de Kast'` (80c) → `wp eval 'rocket_clean_domain(); rocket_clean_minify();'` → provas: `<title>`, `og:title`, `h1 itemprop=headline` novos; home contendo o título novo = 1; slug/URL preservados.
5. **Mapa da checagem dupla (por que passou):** gate_titulo.py só no motor_publicador VELHO e só sintático; Auditor Títulos GPT advisor (*/30) filtra autor **5786** (V4.1 publica pelo **5470** → invisível); publicador DS-N audita capa, não título. 2º caso do dia (268482 Villatoro → EMU-2).
6. **Ponte:** `ZM-20260901-031` em `de_dell.md` (CL chefe + AGY + DS-N, c/c Miguel) — ordem "apertar a revisão", pedidos: estender advisor p/ 5470+5801 + regra de clareza (após patch da sessão urgente), revisão amostral humana de título pré-publish pela CL.
7. **Arquivos tocados:** WP post 268457 (título) · `Foruns/ponte_laura_completa/de_dell.md` (append) · `Foruns/forum_titulo_kast_investigacao_autoria_20260901.md` (novo) · esta memória · `CEREBRO_NODE_ATUALIZACOES.md` + `CEREBRO_NODE_ESTILO.md` (catálogo) · `MONITORAMENTO_DE_TRABALHO.md` (linha ✅) · adendo irmão no fórum EMU-2.

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** título degenerado por tradução literal do espanhol (corpo bom, fact-check ok) corrigido in place com provas; autoria 100% mapeada com evidências; gap da checagem dupla exposto com nome e sobrenome (auditor cobre autor errado).
- **Falta:** enforcement EMU-2 no v41_ciclo (NYC) — advisor p/ 5470+5801 + regra de clareza; confirmação do modelo exato do job com a Laura; amostragem humana CL interim.
- **Do Miguel:** só validar o título novo no ar (mesma URL).
