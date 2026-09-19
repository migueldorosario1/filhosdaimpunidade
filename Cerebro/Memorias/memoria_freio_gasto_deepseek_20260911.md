# 🧠 MEMÓRIA — Freio de gasto DeepSeek 11/09 (log técnico completo)

Companion do `Foruns/forum_freio_gasto_deepseek_20260911.md` (decisões). Executor: ZCode/Kimi K3, sessão 11/09 09:20→. Ref ZM-20260911-FREIO-DS.

## Fontes consultadas
- `tencent:/home/ubuntu/cafezinho/v6_data/custos/` — financeiro_7d.json (09:15:13), banco_custos_2026-09.jsonl, banco_custos_tencent.jsonl, ao_vivo_tematicos.jsonl (vazio).
- Crons: Dell (`crontab -l` local), tencent ubuntu (`/var/spool/cron/crontabs/ubuntu`, mtime 11/09 01:37 — alimentador YT reativado hoje), tencent root.
- Logs: `/tmp/ronda_30min/20260911.log` (Dell), `/tmp/ronda_dsn/20260911.log` (20 rondas; 09:30 falha AUTH ****8762), `/tmp/dsh_telemetria.log`, `ds_nuvem_chefe/logs/vigia_credito.log`.
- `~/.dsh/settings.yaml` (Dell): `deepseek-v4-flash` + reasoningEffort high (o gasto por ronda). API `/models` da conta: só `deepseek-flash` e `deepseek-v4-pro`.

## Números que provam o diagnóstico
- 7d (banco): US$ 31,118 / 3.151 ch — v4_1_ciclo 21,01 (1.700 ch) · v4_1_redator 6,96 · ciclo_v42 1,42 · gerador_imagem 0,91.
- Setembro por dia (banco): 5,72/5,47 → pico 36-42 em 03-05/09 → 20-42/dia até 10/09 (41,37); 11/09 até 09:15 = 7,66 (dos quais 6,00 = transcriber).
- Transcriber: `youtube_transcriber_autonomo` · modelo `transkriptor_url_direto` · US$ 6,00 · video_id=S_Xcwpi2KHc duracao_s=3600 (1h) · seguida de `transkriptor_rejeitado_qualidade` US$ 0 (qualidade ruim — dinheiro jogado fora na 1ª).
- Âncora saldo: US$ 4,45 às 09:15; queda US$ 0,61 entre 09:00-09:15 (ritmo rondas+robôs ~US$ 2,4/h).
- Chefe hoje (banco tencent): US$ 0,15 / 25 ev → ronda do Chefe é BARATA (o custo alto estava na FREQUÊNCIA do Dell e no modelo+reasoning).
- AUTH MORREU ~09:20-30: Dell ****8062... (****806b) e Tencent ****8762 ambas `invalid` em `/chat/completions` e `/user/balance`; ronda Chefe 09:00 OK e 09:30 falha; vigia "sem leitura (resposta sem USD)". Parque DeepSeek parado desde então.

## Mudanças aplicadas (todas com .bak_pre_freio_ds_20260911 + py_compile OK)
1. Dell crontab: `*/30 * * * * ronda_30min.sh` → `0 */4 * * *` (backup `~/crontab.bak_pre_freio_ds_20260911`). Próxima ronda 12:00.
2. Dell `~/.dsh/settings.yaml`: model `deepseek-v4-flash`→`deepseek-flash`, reasoningEffort high→low (backup ao lado).
3. Tencent crontab ubuntu: ronda_dsn.sh `*/30`→`0 */4` (backup `~/crontab.bak_pre_freio_ds_20260911` no servidor).
4. Tencent `~/.dsh/settings.yaml`: CRIADO (não existia) com deepseek-flash+low — o dsh do Chefe rodava no default interno.
5. `dsn_revisor1.py`/`dsn_revisor2.py`: todos `deepseek-chat`→`deepseek-flash` (via python pathlib; 4+3 ocorrências).
6. `ds_nuvem_chefe/escuta.py`: `deepseek-chat`→`deepseek-flash` (2).
7. `dsn_router.py`: `deepseek("deepseek-v4-flash")`→`deepseek("deepseek-flash")`; MANTIDOS `deepseek-v4-pro` (complexo) e `deepseek-v4-flash-vision-exp` (visão — flash não tem visão; NODE_CHAVES_E_LLMS: ~US$0,0003/análise, é o mais barato de visão da casa).
8. `vigia_credito_deepseek.py` linha 169: `est[falhas]`→`est["falhas"]` (NameError; backup `.bak_pre_fix_falhas_20260911`); prova: log 09:32:55 "sem leitura (resposta sem USD); falhas seguidas=2" + py_compile OK.
- NOTA quoting: ssh+seds aninhados falharam 2×; solução = heredoc `ssh host 'python3 -' <<'PYEOF'`.

## Não mexido (proposto no plano, aguarda "vai")
- Transcriber sem teto (US$ 6/tacada) — cap US$/dia ou limite de duração.
- Cascata de curadoria v41 (NYC) — 1º degrau p/ flash (~US$ 10/7d); redação = mexe só com ordem.
- Chave própria Dell (fim da lacuna escritório×robôs; reporter_us65.py flag REGISTRAR_BANCO pronta).

## Provas de aceite pendentes (exigem auth volta)
- Ronda 12:00 Dell em flash+low exit=0; ronda Chefe 16:00 idem; revisor :05/:20 chamando flash 200 (se id inválido, escada cai p/ GLM e revisores seguem — fail-safe já existente); vigia volta a ler saldo.

## Estado final
Freio 100% aplicado; parque DeepSeek PARADO por auth morta (não por freio) desde ~09:30 11/09 — resolver chave/recarga é ação do Miguel. Verticais/temáticos: zero gasto DeepSeek (banco vazio desde 01/08).
