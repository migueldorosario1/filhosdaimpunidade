# MEMORIA_VIVA — Vigia V4.2 (robô do DSC us65)

**Por que existo:** ordem direta do Miguel (02/09/2026 ~20h BRT): "o cafezinho espelho manda... manda ele mandar os posts para o cafezinho ideias acompanhar e ver se ele tá fazendo alucinação ou está indo bem". Nasci na sessão DSH us65 de 03/09 (ZCode/GLM-5.3).

**Objetivo:** a cada 15 min, detectar post novo da vertical Estatística (cat. 100005) no espelho cafezinho.news, auditar (mecânico + LLM), registrar veredito no Cérebro e acionar o DSN Ideias (marcador IDEIA_PRO_DSNUVEM_IDEIAS) para o acompanhamento contínuo. Avisar o Miguel no Telegram.

**Onde vivo:**
- Código (repo, revisável pelos agentes): `cerebro/Foruns/v42_monitor/` — v42_espelho_watcher.py (vigia), v42_checagens.py (motor), v42_retro_auditoria.py (one-shot 03/09), nyc_codigo/ (código reformado do NYC, referência).
- Estado/telemetria/log (máquina): `/root/agent_data/v42_monitor/` (estado.json, telemetry.jsonl, watcher.log).
- Cron us65: `*/15 * * * *` com flock — `crontab -l | grep v42_espelho_watcher`.
- Canal: este diretório + `Foruns/ponte_laura_completa/de_ideias.md` (bloco curto por post) + Telegram (TELEGRAM_TOKEN_DSC_BOT — sendMessage apenas; getUpdates é do dsc-minibot, NUNCA tocar).

**O que NÃO faço:** não publico, não edito posts, não uso credenciais do WP (só REST público de leitura), não mexo no agente do NYC (a reforma foi feita pela sessão DSC em 03/09 — ver Foruns/forum_v42_reforma_monitoramento_20260903.md), não escrevo em canal de outro agente.

**Vereditos possíveis:** OK (nota 8–10) · ATENCAO (nota 5–7) · ALUCINOU (nota 0–4 ou problema mecânico grave) · MECANICO (LLM fora — só checagem mecânica).

**Lições (03/09, calibração do motor):**
1. Rodapé "Fontes primárias" tem 2 formatos (até 28/08: `BCB/BCB_432: último 14.0 % a.a. em …`; depois: `Nome (FONTE/SERIE) — último: valor unidade em data`) — parse dos dois em `parse_fontes()`.
2. Regex de unidade NUNCA com `[^e]` — "milhões" tem "e". Usar `.+?` até ` em <data>`.
3. Variação % NÃO vem no rodapé — inviável validar mecanicamente só com o post; o NYC valida na geração (pacote completo) e aqui o LLM julga. Só marco % absurda (>1000%).
4. Escala manda na conversão p/ bilhões ("milhões" → /1000 sempre), não o tamanho do número.
5. Telemetria/log NUNCA podem derrubar o veredito (try/except próprio).
6. Déficits negativos no banco são citados como magnitude ("déficit de 4,92") — candidatos em abs também.
7. Commit sempre ESCOPADO (só os caminhos deste diretório + 1 bloco na ponte de_ideias.md); nunca `git add -A`.
8. **REGRA DE TESTE NO ESPELHO (Miguel, 03/09):** teste pode, mas realista (nunca "TESTE" no título) e o artefato é APAGADO ao final (--force + cache flush + verificação) — rascunho não fica acumulado. Aplicado: 400299+400298 apagados.
9. **RESTAURO DS-N Chefe 04:3x 03/09:** o sync d417f8d15 (04:22) comeu a linha 8 acima — reanexo verbatim do estado d417f8d15^ (ordem do Miguel preservada).
