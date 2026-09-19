# 📱 GRADE DE COMUNICAÇÃO TELEGRAM DO MIGUEL — reforma 03/09/2026 ~15h (ZM)

> Ordem do Miguel (voz, ~15:1x): "estou recebendo muito Telegram, não estou aguentando mais — organiza, faz a grade com antes e depois, reduz drasticamente, pode ir limpando". Esclarecimento (~15:2x): as janelas 8h/24h/7d/30d são GASTOS de token consolidados — todos os sistemas mandam seus gastos ao DSN Finanças (ou ele vai buscar onde estiverem).

## ✅ O QUE MUDOU (executado e provado)

| # | Mudança | Onde | Rollback |
|---|---------|------|----------|
| 1 | Ronda ZM 1/1h DESLIGADA (automation-877aeabb deletada) | ZCode Dell | Prompt integral preservado no Anexo A → CronCreate |
| 2 | DSN-F: 1×/h → 2×/dia (manhã ~08:0x, noite ~20:0x) com janelas 8h/24h/7d/30d + créditos (DeepSeek+Grok+GLM) + assinatura completa | tencent ~/dsn_financeiro/dsn_financeiro.py (.bak_pre_2xdia_20260903) | restaurar .bak |
| 3 | DS-N Chefe: relatório ao Telegram SÓ de 4/4h (00/04/08/12/16/20 BRT), com linha de gasto; demais rondas só CHECK na ponte | ~/ronda_dsn_prompt.md (tencent .bak_pre_grade_20260903 + Dell) | restaurar .bak |
| 4 | Assinatura COMPLETA em toda mensagem de robô: `— <robô> · <inteligência em uso> · AAAAMMDD HH:MM:SS BRT` | prompt do Chefe (tencent+Dell) + regra casa (anunciada na ponte) | editar prompt |
| 5 | CEO diária 08:10 PAUSADA (redundante com DSN-F manhã) | crontab tencent (# PAUSADO_GRADE_TELEGRAM_20260903; /tmp/cron_bak_20260903) | descomentar 1 linha |
| 6 | MONITOR_GROK espelhado Dell→tencent .env.unificado (Regla 4; .bak_pre_dscgrade_20260903) para o DSN-F ler saldo Grok | tencent | remover linha |
| 7 | Ponte Laura e todos os agentes: Telegram ao Miguel SÓ se precisar | regra publicada no de_dell.md | — |

## 📊 ANTES → DEPOIS (mensagens/dia no Telegram do Miguel)

| Emissor | ANTES | DEPOIS |
|---------|-------|--------|
| DSN Finanças (@Dsnfinancas_bot) | 24/dia (1×/h, só 7d) | **2/dia** (08h+20h; janelas 8h/24h/7d/30d + créditos) |
| DS-N Chefe (@dscelular_bot) rondas | dezenas/dia (relatos de 30/30; msg nº157 hoje 15:20) | **6/dia** (4/4h: 00/04/08/12/16/20, com gasto) |
| Ronda ZM 1/1h (Ponte Cafezinho) | até 24/dia | **0 — desligada** |
| CEO diária | 1/dia (08:10) | **0 — pausada** (DSN-F manhã cobre) |
| Baleia Azul (Chefe) | 2/dia (07:10/19:15) | **mantida 2/dia** (jornal — ordem própria do Miguel) |
| Marketing Moka | 1/dia (09:30) | **mantida 1/dia** (ordem de 03/09 ~15h) |
| Alarmes (saldo <2, healthcheck, incidentes) | eventuais | **mantidos — só alerta real** |
| Respostas conversacionais (Loop A/DSC/plantação) | quando o Miguel fala | **mantidas** |
| Ponte Laura e demais agentes | relatos variados | **só se precisar** (alerta/decisção urgente) |
| **TOTAL fixo** | **~50-200+/dia** | **~11/dia** (2+6+2+1) + eventuais |

## 💰 Boletim 2×/dia do DSN-F — formato provado ao vivo (03/09 15:21)
Gasto real do ecossistema em token: 8h US$ 11.40 · 24h US$ 39.43 · 7d US$ 71.52 · 30d US$ 181.90 · Créditos: DeepSeek US$ 50.14 · Grok US$ 7.99 · GLM janela 5h 33% usada · assinatura: — DSN Finanças (DSN-F) · inteligência: contador determinístico (zero LLM, custo US$ 0) · 20260903 15:21:19 BRT

## ⚠️ Pendências honestas
- GPT/OpenAI: saldo INACESSÍVEL por API (403 comprovado na vigília 29/08 — billing exige session key de navegador). Não entra no boletim.
- Qwen/Kimi no boletim: Qwen token plan e Kimi assinatura não expõem saldo em US$ por API — pendência de plugue se o Miguel quiser janela de tokens.
- "Ponte Laura só se precisar" depende dos agentes Laura (CL/AGY/CM) cumprirem — regra anunciada no de_dell; cobrar nas rondas se vazar.
- Monitor V4.1 ":15" de 02/09: verificado HOJE — não existe mais cron ativo (nada a desligar).

## Anexo A — prompt da Ronda ZM 1/1h (rollback = CronCreate com este prompt, cron "5 * * * *")
(Retirado da automação automation-877aeabb ao deletá-la — integral no histórico do fórum ronda_zm_loop_ecossistema e no arquivo .json de automações do ZCode; para recriar, pedir ao ZM que reconstitui do fórum forum_ronda_zm_loop_ecossistema_20260903.md.)

## Adendo 1 — 03/09/2026 ~15:3x (ZM): links completos + fim do "DS Miguel"

**Pedido:** mensagens com LINK COMPLETO clicável (nunca rota interna) + emojis; cancelar de vez o "DS Miguel" (o Miguel notou a assinatura errada — é o ZM/ZCode, não um "DS").

**Descoberta da URL pública do painel CCTV (v6):** o `https://43.156.151.165.sslip.io` (certbot) proxy para **127.0.0.1:8420 = app do MOKA pontos** (por isso 404 `{"detail":"Not Found"}`); quem serve `/v6/` é o server default `_` do nginx — acessível por **http://43.156.151.165/v6/** (200 provado ao vivo: /v6/agentes, /v6/custos/ao-vivo). LINK OFICIAL DA CASA nos Telegrams: `http://43.156.151.165/v6/<rota>`. PENDÊNCIA: domínio HTTPS próprio p/ o CCTV (novo server block + certbot) — não usar o sslip.io p/ painel.

**Aplicado:** dsn_financeiro.py — 2 ocorrências "Painel: /v6/custos/ao-vivo" → "📊 Painel de custos: http://43.156.151.165/v6/custos/ao-vivo · agentes: http://43.156.151.165/v6/agentes" (py_compile OK); ronda_dsn_prompt.md (tencent+Dell) — regra "LINKS sempre COMPLETOS e clicáveis + emojis". Prova enviada 15:3x (link clicável recebido pelo Miguel).

**"DS Miguel" cancelado de vez:** a Ronda ZM 1/1h rodou pela ÚLTIMA vez às 15:05 (mensagem vista pelo Miguel ~15:2x era essa) e foi DELETADA às ~15:13 — a partir das 16:05 não existe mais execução. Auditoria completa pós-delete: nenhum cron/timer/serviço emissor além dos mapeados (systemd tencent = só Loop A escuta; relatorio_llms_v41 extinto; dsn_revisor1/2 e dsn_ideias sem Telegram; Dell sem timers; nenhum automation ZCode ativo além de Marketing Moka 1/dia). Assinatura da casa passa a ser sempre o nome verdadeiro do agente (ZCode/GLM-5.3 (ZM), DS Nuvem Chefe etc.) — nunca "DS Miguel".
