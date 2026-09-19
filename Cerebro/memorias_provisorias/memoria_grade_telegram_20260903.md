# Memória técnica — Grade de comunicação Telegram do Miguel (03/09/2026 ~15h, ZM/GLM-5.3)

**Ordem:** Miguel por voz ~15:1x ("não estou aguentando mais o Telegram") + esclarecimento ~15:2x (janelas 8h/24h/7d/30d = gastos de token consolidados; DSN-F busca onde os dados estiverem).

**Mapeamento dos emissores (prova: crontabs tencent/nyc/us65 + CronList ZCode):**
- tencent */15: dsn_financeiro.py (bot @Dsnfinancas_bot, 1×/h via bloco "TELEMETRIA_DSN_20260903")
- tencent */30: ronda_dsn.sh → dsh headless c/ ~/ronda_dsn_prompt.md (Chefe; envia Telegram ao Miguel com freq. ~quase toda ronda; Baleia 2×/dia)
- tencent 08:10: telemetria_ceo_diaria.py (só mandava msg — PAUSADA)
- ZCode automação :05/h: Ronda ZM 1/1h — DELETADA (automation-877aeabb)
- ZCode automação 09:30: Marketing Moka 1/dia — mantida
- healthchecks farol: só anomalia — mantidos; v42_autocura e v41_player: sem Telegram (provado por grep)
- NYC: nenhum emissor Telegram direto em cron (v41_ciclo etc. só publicam/gravam)

**Mudanças aplicadas (todas com .bak/rollback — ver fórum forum_grade_telegram_20260903.md):**
1. dsn_financeiro.py (tencent): bloco horário → 2×/dia (slot "08" se hora<14 senão "20"; dispara só nas horas 8 e 20, minuto<15; estado ultimo_tg_2xdia). Janelas _gasto_real_janela(h) = agregar(ini,agora) + ancora_janela, sem 2× (nyc+tem+(tenc−ds_tenc)+âncora). Função nova saldos_extras(): Grok via management-api.x.ai/v1/billing/teams/a154fa36…/prepaid/balance (MONITOR_GROK espelhado p/ tencent .env.unificado, backup .bak_pre_dscgrade_20260903) + GLM via open.bigmodel.cn/api/monitor/usage/quota/limit (ZHIPU_API_KEY da tencent funcionou). py_compile OK; PROVA E2E 15:21 enviada e recebida.
2. ronda_dsn_prompt.md (tencent .bak_pre_grade_20260903 + Dell): seção "CADÊNCIA TELEGRAM MIGUEL" — relatório só nas rondas 00/04/08/12/16/20 BRT ±30min, com linha de gasto (fonte financeiro_7d.json/canal DSN-F); exceções 🔴/resposta/PRECISA MIGUEL/Baleia; assinatura COMPLETA: robô · inteligência · AAAAMMDD HH:MM:SS BRT; lembrete DSC-013 removido também da cópia tencent.
3. CEO diária: cron comentado # PAUSADO_GRADE_TELEGRAM_20260903 (backup /tmp/cron_bak_20260903 na tencent).
4. Ronda ZM 1/1h: CronDelete automation-877aeabb (prompt preservado p/ recriação).

**Resultado:** carga fixa ~50-200 msgs/dia → ~11/dia (DSN-F 2 + Chefe 6 + Baleia 2 + Moka 1) + alertas.

**O que falta / preciso do Miguel:** nada obrigatório; opcionais = Qwen/Kimi em janela de tokens no boletim; GPT impossível via API (403); cobrança da regra "só se precisar" nos agentes Laura fica com as chefias (avisado no de_dell).
