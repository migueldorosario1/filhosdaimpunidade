# Fórum — Unificação Prometheus na conta aiatolahnews (descarte dos cofres Beijing)

**Data:** 2026-08-09 ~04:20 BRT · **Agente:** ZCode/Qwen 3.8 · **Memória par:** `Memorias/memoria_unificacao_prometheus_conta_aiatolah_20260809.md`
**Autorização Miguel:** "sim, pode unificar tudo numa só conta prometheus, mas tem que ser o prometheus instalado na conta alibaba aiatolahnews" (msg desta sessão).

## Decisão / estado
- ✅ **4 cofres Prometheus unificados** — todos apontam agora para o workspace `Prometheus-Aiatolah` (conta `aiatolahnews@gmail.com`, Singapura, `default-cms-5083281701361235-ap-southeast-1`).
- ✅ **2 cofres Beijing velhos descartados** (md5 `4ea87513...`, workspace `5799673946330755-cn-beijing` desativado) e substituídos pelo novo (md5 `7988651c...`).
- ✅ Backups datados preservados em ambos servidores (Regra 4 — nada se perde).
- ✅ Read ao vivo confirmado no workspace aiatolah (HTTP 200, dados com timestamp atual).

## Antes vs depois (md5 dos cofres)
| Servidor | Path | Antes (Beijing) | Depois (aiatolah) |
|---|---|---|---|
| Tencent | `cafezinho/.../chaves/alibaba_prometheus.env` | `4ea87513...` ❌ | `7988651c...` ✅ |
| Tencent | `prometheus_agent/alibaba_prometheus.env` | `7988651c...` ✅ (já era) | `7988651c...` ✅ |
| NYC | `prometheus_agent/alibaba_prometheus.env` | `7988651c...` ✅ (já era) | `7988651c...` ✅ |
| NYC | `portal_cafezinho/chaves/alibaba_prometheus.env` | `4ea87513...` ❌ | `7988651c...` ✅ |

## Backups criados
- Tencent: `cafezinho/.../chaves/alibaba_prometheus.env.bak_pre_unificacao_20260809_041959`
- NYC: `portal_cafezinho/chaves/alibaba_prometheus.env.bak_pre_unificacao_20260809_072038`

## Segurança
- Verificado antes: nenhum script ativo nem cron referencia os paths velhos (só documentação/git). Substituição segura.
- Nenhum valor de segredo exposto neste registro (Regra do Cofre intacta).

## Estado da missão
- **Aconteceu:** unificação completa, 4/4 cofres alinhados na conta aiatolah, read ao vivo OK.
- **Falta:** nada desta tarefa. (Lacunas de telemetria — NYC/rio-ag sem node_exporter ativo — seguem como Plano 1 pendente, aguardando decisão separada do Miguel.)
