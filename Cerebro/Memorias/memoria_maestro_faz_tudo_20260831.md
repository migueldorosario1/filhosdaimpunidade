# Memória — Maestro faz-tudo 31/08: organização do dia, diagnóstico da produção, curas da noite (log técnico)

**Data:** 31/08/2026 22:24→ · **Operador:** ZCode/GLM-5.3 (Dell) · **Irmã:** `Foruns/forum_maestro_faz_tudo_20260831.md` (decisões) · **Agenda viva:** `Cerebro/AGENDA_PENDENCIAS_MAESTRO.md`

## Provas e comandos-chave

### Diagnóstico da produção (wp-cli em cafezinho-wp /var/www/ocafezinho --allow-root)
- Publicados 31/08: **17** (`wp post list --post_status=publish | grep 2026-08-31`) · 30/08: 24 · rascunhos novos hoje: 22 · pendentes (velharia 17-25/08): ~30.
- Fila de caça: `/root/agent_data/dsn_imagem/fila_caca.jsonl` (NYC) — 268456/268457/268458/268394/268451 às 22:0x.
- Worker manual: `cd /root/v4_labs && . /root/chaves.sh && /root/venv/bin/python3 codigo/dsn_imagem.py --limite 3` (re-tenta só "não tentadas"; `--post-id N` força re-tenta com 2 variações de tese — 268394: 16 candidatas vistas, IA proibida → caça).

### 268440 (bastidor)
- Verificação: `wp post get 268440 --field=post_modified` = **2026-08-31 22:11:55** (corte pela AGY-L, CL-039); grep `checklist|conferir|checar|verificar|gate|zizi|robô` no conteúdo = VAZIO; fim do texto = seção FONTE legítima.

### Link público (o "controle.")
- Causa: a REST devolve `link` na base `https://controle.ocafezinho.com` (domínio de bastidor no .env da Tencent; siteurl/home do WP = www, correto).
- Cura: patch em `/home/ubuntu/dsn_publicador/dsn_publicador.py` (Tencent): linha `link = corpo.get(...)` envolvida com `.replace("https://controle.ocafezinho.com","https://www.ocafezinho.com")` + comentário. Backup `.bak_pre_link_publico_20260831`. py_compile OK.
- 🔴 LIÇÃO: 1ª tentativa de patch com indentação fixa (4 espaços) QUEBROU o arquivo (IndentationError; o alvo tinha 12 espaços) — restaurado do backup e re-aplicado com regex preservando indentação (`^([ \t]*)link = ...`). SEMPRE capturar a indentação real antes de replace em código de produção; e py_compile ANTES de sair.

### Seeds de capa (caça do maestro)
- Formato `capas_seed.json` (Tencent): `{"url","filename","caption" (foto: AUTOR/FONTE, LICENÇA, ANO),"alt","ref"}`; backup `.bak_pre_zm_maestro_20260831`.
- 268451 Paes: `https://upload.wikimedia.org/wikipedia/commons/a/a0/Eduardo_Paes_-_terceiro_mandato_como_prefeito.jpg` (Beth Santos, CC BY 3.0, 2024) — URL do Commons vem com `?utm_source=...` → SEMPRE limpar query.
- 268394 Natura: `.../1/17/Cerim%C3%B3nia_de_Inaugura%C3%A7%C3%A3o_da_matriz_da_Natura_Cosm%C3%A9ticos_%2836149455223%29.jpg` (Governo SP/Flickr, CC BY 2.0, 2017) — fora da janela ≤12h do fluxo autônomo do publicador (receita pronta p/ editoria).
- Caça Commons: `action=query&generator=search&gsrsearch=<termo>&gsrnamespace=6&prop=imageinfo&iiprop=url|extmetadata` (licença em LicenseShortName, autor em Artist).

### Ponte
- Bloco **ZM-20260831-024** em `de_dell.md` + linha em `de_nuvem_publicador.md` (repo ~/cerebro-miguel, commit `00e7fb9da`, push OK) + regra no `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` (append local).

### Automação
- `automation-3ad40af1` (cron `0 * * * *`): ronda leve toda hora + pendência nas horas pares + agenda do Miguel 07-09h. 🔴 LIMITAÇÃO: o host permite 1 automação por sessão (2ª/3ª CronCreate falharam: "session already belongs to a scheduled task") → tudo fundido num prompt só com camadas por hora (`date +%H`).

### Estado Moka (22:4x)
- `git log`: 49e5ddf (TopNav full-bleed — fim da logo colada) · 7466fe4 (menu CLEAN invisível por padrão) · f5292b7 (Amanhecer Azul). Padronização de botões (PROMPT_PADRONIZACAO_BOTOES_MOKA_20260831) ainda em voo.

### Pendências que ficaram
- Robô YouTube: git unmerged visto pela DS-N às 22:00 na Tencent (repo limpo quando conferi às 22:33 — "## main...origin/main"; cron 7,22,37,52 no lugar; cron.log existe) — verificar por que parado desde ~20:07 (logs ~/ds_youtube/logs/).
- 268366 (future 22:55) e 268393 (future 23:16): ronda confere virada; cura `wp eval "wp_publish_post(ID);"` se capa+img_check ok.
- Google Agenda: ZM sem acesso OAuth (não existe credencial no cofre p/ Calendar) — alternativa ativa: Telegram 08:00 + AGENDA_PENDENCIAS_MAESTRO.md.

## Adendo memória — povoação noturna 23:0x
- Bug triplo do fluxo fresco: meta não-registrada (REST descarta silenciosamente) + context=edit ausente (meta só viaja em edit) + congelamento (break 1/ciclo escolhia sempre o mais antigo; guarda 1h no processamento pulava e o ciclo morria vazio → curar na ESCOLHA, não no processamento). Provas no fórum adendo 4.
- Incidente carga cafezinho-wp: load 31 sob recorde de audiência; rajada transitória; NÃO martelar API em recuperação (checar `uptime` antes de corridas extras; régua: load 1min >10 = só cron).
- Uploads de mídia pela Tencent morrem em rajada (ReadTimeout em subir_midia) — os seeds ficam armados e o cron 15/15 aplica quando a API respira.
- Rollbacks escritos: mu-plugin = remover arquivo; patches = cp .bak_pre_*_20260831 de volta.
