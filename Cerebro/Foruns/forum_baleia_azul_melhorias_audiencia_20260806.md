# 🐋 Fórum — Baleia Azul: consertos e upgrade de audiência (2026-08-06)

> **Ordem do Miguel (06/08 ~13:15 BRT, sobre o e-mail das 08:00):** "Saúde UptimeRobot indisponível — tem que acertar. Auditor de títulos: vê se está funcionando, se é legacy, se a gente precisa — se não precisar, tira do Baleia. Sinal de recuperação Google: está repetindo o mesmo texto-gabarito toda vez — por que o diagnóstico não entra? Verifica se ainda temos as credenciais do Search Console/Vitals. A REGRA EDITORIAL não é para aparecer escrita no Baleia — é uma dica de como mostrar o ponto bom com comparativo. Audiência: eu quero COMPARATIVO — vs 15 dias atrás, vs semana passada, post mais visto ontem. Custos: tem que falar quais LLMs foram mais usados."

**Executor:** ZCode (Kimi K3), sessão chat direto, 06/08 13:20→14:00 BRT.

## Diagnóstico (causas-raiz reais)

1. **"Saúde indisponível" e "Auditor indisponível" = mesmo bug:** o cron local roda `/usr/bin/python3` = **Python 3.8.10**, que não tem `zoneinfo` (entrou no 3.9). Os coletores importavam `ZoneInfo` no topo → `ModuleNotFoundError` → o emissor engolia o erro (`2>/dev/null || true`) e caía no texto "indisponível". Manualmente (pyenv 3.10) tudo funcionava — por isso o bug era invisível fora do cron.
2. **Sinal Google repetindo gabarito:** o coletor `coletar_sinal_google_baleia.py` existia desde 20/07 e funciona — **mas o emissor nunca o chamava**; o texto-gabarito + a REGRA EDITORIAL estavam hardcoded no template do e-mail.
3. **Credenciais Google: VIVAS.** GSC (`util_cron_gsc_diario.py`, 10:00 UTC) e PageSpeed/CrUX (`util_cron_pagespeed_diario.py`, 09:00 UTC) geraram arquivos HOJE em NYC. Nada a renovar.
4. **Auditor de títulos: VIVO e necessário** — cron `*/10` em NYC + relatório diário no minuto :58. Hoje: 26 posts auditados, 5 alertas reais (cargo de Gideon Sa'ar, título×lide Ormuz, Ideb "sob governo Lula"...). Custo irrisório (US$ 0,0016/dia). **Decisão: MANTER** — mas a fonte do Baleia passa a ser o relatório diário (a rodada crua de 10min quase sempre dizia "sem novidades").
5. **Bug secundário:** os coletores usavam `--output-dir` relativo; no cron (CWD=$HOME) os recibos iam para `/home/migueldorosario/Projeto Cafezinho Agentes/` (diretório errado, criado em 25-27/07 — recibos movidos ao canônico e pasta removida).

## O que mudou (tudo em `scratch/`, workspace local)

| Arquivo | Mudança |
|---|---|
| `coletar_saude_baleia_azul.py` | fallback BRT sem zoneinfo (py3.8) + data de medição legível |
| `coletar_auditor_titulos_baleia.py` | reescrito: fonte = relatório diário; gera resumo (auditados/correções/alertas/custo + alertas resumidos); marca "desatualizado" se o relatório não for de hoje; recibo bruto salvo em disco |
| `coletar_sinal_google_baleia.py` | ganhou **Core Web Vitals** (LCP/INP/CLS/TTFB mobile, comparativo datado) ao lado do GSC; header "📈 SINAL DE RECUPERAÇÃO GOOGLE" |
| `coletar_audiencia_baleia.py` | **NOVO.** GA4 via NYC (1 sessão SSH): views/usuários por dia (30d), top post de ontem (exclui home por pagePath), + analise_performance (top5 14d, macrotema, alertas). Comparativos: ontem vs anteontem, 7d vs 7d anteriores, 14d vs 14d anteriores |
| `enviar_baleia_azul_v2.sh` | chama os 4 coletores com output-dir absoluto; stderr dos coletores vai para o log (fim do silêncio); custos ganham "LLMs mais usados ontem" + "Top LLMs 7d" (por_modelo); placeholder + REGRA EDITORIAL cruas **removidos do corpo**; link `/v5/baleia`→`/v6/baleia`; Telegram sem `parse_mode HTML` (o "&" de "Custos & LLMs" quebrava o envio) e payload via `json.dumps`; `BALEIA_DRY_RUN=1` para teste seguro; assinatura neutra (era "Cheng (DeepSeek)") |

Backup: `scratch/enviar_baleia_azul_v2.sh.bak_pre_melhorias_20260806`.

## Validação

Dry-run completo em **ambiente de cron simulado** (`env -i`, PATH=/usr/bin:/bin, CWD=$HOME, python 3.8): corpo montado com TODOS os blocos reais — audiência 7d **+16,5%** ✅ e 14d **+7,1%** ✅, ontem −8,1% ⚠️ (honesto), top post de ontem (Irã/Patriot, 127 views), GSC posição 1.83→1.67 (+8,7%), CWV com comparativo, saúde online, auditor com 5 alertas. Regra editorial agora é **aplicada** (melhor sinal comprovado + quedas não escondidas), não **escrita**.

## Decisões pendentes para Miguel

- Assinatura do e-mail passou de "— Cheng (DeepSeek)" para "— Baleia Azul · boletim automático do Cafezinho" (factual: quem emite é o script; o editor-chefe Claude não gera edições desde 28/07). Se preferir outra assinatura, é uma linha.
- Queda breve de hoje 03:31 BRT (1min5s, CloudFlare Timeout) coincide com o reboot diário do ServerDo flagrado na auditoria de servidores — vale alinhar janela do reboot ou avisar o UptimeRobot (fora do escopo de hoje).

**Próximo envio real:** hoje 18:00 (cron local), já no formato novo.

— ZCode (Kimi K3), 2026-08-06 ~14:00 BRT
