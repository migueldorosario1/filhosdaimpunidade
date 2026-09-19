# 🧠 Memória — Baleia Azul: consertos e upgrade de audiência (2026-08-06)

> Log técnico completo da sessão ZCode (Kimi K3), 06/08 13:20→14:00 BRT.
> Fórum resumido: `Foruns/forum_baleia_azul_melhorias_audiencia_20260806.md`.
> Ordem: Miguel, via chat, sobre o e-mail Baleia das 08:00.

## 1. Contexto e estado antes

Emissor canônico `scratch/enviar_baleia_azul_v2.sh` (cron local 8h/18h, sem PATH no crontab).
O e-mail de 06/08 08:00 saiu com: `Saúde UptimeRobot indisponível`, `Auditor de títulos indisponível`,
placeholder cru "O último diagnóstico disponível deve entrar com data e comparação..." e a
"REGRA EDITORIAL: ..." impressa como texto. Audiência sem comparativos; custos sem LLMs.

## 2. Investigação (evidências)

- `crontab -l`: sem `PATH=` → cron usa `/usr/bin:/bin`.
- `which python3` interativo = `/home/migueldorosario/.pyenv/shims/python3` (3.10.13); `/usr/bin/python3` = **3.8.10**.
- Reprodução com `env -i HOME=$HOME PATH=/usr/bin:/bin bash -c '... coletores ...'`:
  `ModuleNotFoundError: No module named 'zoneinfo'` nos coletores de saúde e auditor (zoneinfo entrou no Python 3.9).
  O emissor chamava os coletores com `2>/dev/null || true` → erro invisível, caía no fallback "indisponível".
- Log `/tmp/baleia_azul_envios.log`: 05/08 08:00 e 18:00 falharam em `scp: ambiguous target` (bug BUG-20260805-BALEIA-SCP-ESPACO, corrigido de madrugada pela sessão vigília); 06/08 08:00 enviou.
- `coletar_sinal_google_baleia.py` existia desde 20/07, funcional, **mas não era referenciado no emissor** — o template tinha o placeholder + REGRA EDITORIAL hardcoded.
- Bug secundário de CWD: coletores com `--output-dir` default relativo (`Projeto Cafezinho Agentes/dados_baleia_azul`); no cron (CWD=$HOME) recibos iam para `/home/migueldorosario/Projeto Cafezinho Agentes/dados_baleia_azul/` (achados arquivos de 25-27/07 lá; movidos ao canônico, pasta removida).

## 3. Estado das fontes em NYC (198.199.121.136) — tudo VIVO

| Fonte | Evidência 06/08 |
|---|---|
| `auditor_titulos_gpt` | cron `*/10` (flock, `--modo poll`) + relatório `:58 * * * *` (`--relatorio-diario`); `RODADA_ATUAL.md` mtime 16:10 UTC; `RELATORIO_ATUAL.md`: 26 auditados, 0 correções, 5 alertas, 0 falhas, US$ 0.001628 |
| GSC | cron `0 10 * * * util_cron_gsc_diario.py`; 33 `diario_*.json`, último 06/08 10:00 UTC |
| PageSpeed/CrUX | cron `0 9 * * * util_cron_pagespeed_diario.py`; `diario_20260806.json` com LCP/INP/CLS/TTFB mobile+desktop (`cls` = centésimos: 4 → 0,04) |
| GA4 | venv `/root/venv/bin/python3` com `google.analytics.data_v1beta` OK; SA `/root/keys/ga4.json`; property 374552425 (O Cafezinho); semanal em `/root/agent_data/ga4/semanal_*.json` |
| Audiência editorial | `agente_performance.py` cron `52 * * * *` → `/root/agent_data/analise_performance.json` (janela 14d, top5, macrotema, alertas) |
| Custos | `/root/agent_data/custos_consolidados/AAAA-MM-DD.json` com `por_modelo` ({modelo:{custo_usd, chamadas}}) |

**Conclusão credenciais (pedido explícito do Miguel):** Search Console e PageSpeed/Vitals seguem com credenciais válidas e dados frescos diários. Nada expirado.

## 4. Alterações de código (workspace local `scratch/`)

Backup: `enviar_baleia_azul_v2.sh.bak_pre_melhorias_20260806`.

1. **Fallback de timezone nos 3 coletores** (compat py3.8):
   ```python
   try:
       from zoneinfo import ZoneInfo
       BRT = ZoneInfo("America/Sao_Paulo")
   except ModuleNotFoundError:
       BRT = timezone(timedelta(hours=-3), "BRT")
   ```
2. **`coletar_auditor_titulos_baleia.py` reescrito** — fonte principal `RELATORIO_ATUAL.md`; parser dos bullets (`Posts efetivamente auditados` etc.) + tabela de alertas (`| hora | post | categoria | motivo |`, motivo truncado em 110 chars); header do relatório define a data; se ≠ hoje BRT, marca "⚠️ (desatualizado)". Envelope JSON virou `baleia_auditor_titulos.v2`. Fallback: rodada crua. Saída impressa = resumo (vai no e-mail); bruto salvo como `auditor_titulos_relatorio_YYYYMMDD.md`.
3. **`coletar_sinal_google_baleia.py`** — uma sessão SSH só traz GSC (últimos 14) + PageSpeed (últimos 8); novo subbloco CWV mobile (LCP/INP/CLS/TTFB + comparativo datado, `cls/100`); header "📈 SINAL DE RECUPERAÇÃO GOOGLE:".
4. **`coletar_audiencia_baleia.py` (NOVO)** — SSH único, `/root/venv/bin/python3 -` via stdin:
   - GA4 `runReport` #1: dim `date`, métricas `screenPageViews`+`activeUsers`, 30d até ontem, ordem asc;
   - GA4 `runReport` #2: dims `pageTitle`+`pagePath`, só ontem, top 15 (pagePath serve para excluir a home "/" — o título dela, "O Cafezinho | Contrainformação é Poder", apareceu como "top post" no primeiro teste);
   - lê `analise_performance.json`;
   - local monta: ontem vs anteontem; 7d vs 7d anteriores; 14d vs 14d anteriores (janelas equivalentes — regra editorial anti-janela-enganosa); média/dia; top post de ontem (filtro: path "/" e títulos genéricos/<12 chars); top5 14d (sufixo " - O Cafezinho" removido ANTES de truncar 70 chars); macrotema + 1 alerta;
   - fallback honesto se GA4 falhar (bloco reduzido + motivo técnico, sem inventar).
   - Recibos: `audiencia_YYYYMMDD.json` + `audiencia_atual.md` em `dados_baleia_azul/`.
5. **`enviar_baleia_azul_v2.sh`**:
   - `DADOS="$PROJETO/dados_baleia_azul"` absoluto passado a todos os coletores;
   - stderr dos coletores → `2>>"$LOG"` (falhas deixam rastro em `/tmp/baleia_azul_envios.log`);
   - chama os 4 coletores (saúde, auditor, sinal google, audiência) com fallbacks honestos;
   - custos: agrega `por_modelo` dos 7 consolidados → "LLMs mais usados ontem" (top5, custo+chamadas) e "Top LLMs 7d";
   - removidos do corpo: placeholder GSC e "REGRA EDITORIAL:" (a regra segue canônica em `CEREBRO_NODE_BALEIA_AZUL.md` e é aplicada pelos comparativos);
   - link `/v5/baleia` → `/v6/baleia` (v5 é 301);
   - Telegram: removido `parse_mode: HTML` ("&" de "Custos & LLMs" e títulos com aspas quebravam o envio) e payload via `json.dumps` em python;
   - `BALEIA_DRY_RUN=1`: monta e imprime o corpo sem scp/e-mail/Telegram;
   - assinatura "— Cheng (DeepSeek)" → "— Baleia Azul · boletim automático do Cafezinho (fontes: GA4, Search Console, PageSpeed/CrUX, UptimeRobot, banco_custos NYC)" — decisão registrada no fórum para ciência do Miguel.

## 5. Validação

- Coletores individuais (py3.10 interativo): OK.
- **Dry-run completo em ambiente cron** (`cd $HOME && env -i HOME=$HOME PATH=/usr/bin:/bin BALEIA_DRY_RUN=1 bash scratch/enviar_baleia_azul_v2.sh`): exit 0, corpo completo com todos os blocos REAIS:
  - Audiência: ontem 5.292 views/3.631 usuários (−8,1% vs 04/08 ⚠️), 7d 53.139 (+16,5% ✅), 14d 98.768 (+7,1% ✅), top post ontem "Irã destrói base de lançamento de mísseis Patriot no Iraque" (127);
  - Custos: LLMs ontem fal-ai US$2,13 (61 ch.), deepseek-v4-pro US$0,40...; 7d fal-ai US$22,86, qwen-max US$5,62, ideogram US$3,20...
  - Saúde: online, 1 queda 03:31 BRT (1min5s, CloudFlare Timeout — coincide com reboot diário ServerDo 03:31, ver mapa de servidores);
  - Auditor: 26 posts, 5 alertas detalhados;
  - Google: posição 1,83→1,67 (+8,7%), 3.715 cliques/89.110 impressões, CWV LCP 1604ms (−1,6% vs 30/07 ✅).
- Números de milhar padronizados PT-BR (ponto) nos blocos novos.

## 6. Lições

1. **Cron ≠ shell interativo:** pyenv esconde o python do sistema; testar SEMPRE com `env -i PATH=/usr/bin:/bin`.
2. **`2>/dev/null || true` em coletor é fábrica de "indisponível" mudo.** Stderr vai para o log desde hoje.
3. **Script existente ≠ script chamado:** o coletor do sinal Google estava pronto desde 20/07 e nunca foi ligado ao emissor — o checklist de integração é: quem chama, com que CWD, com que PATH, com que python.
4. **`--output-dir` relativo + cron (CWD=$HOME) = recibo no lugar errado.** Sempre absoluto em job de cron.

— ZCode (Kimi K3), 2026-08-06 ~14:00 BRT
