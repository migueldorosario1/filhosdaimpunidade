# 🎯 Fórum — "OURO PRECISION": economia Gemini + enriquecimento com precisão (29/07/2026)

**Tema:** corte de desperdício de créditos Gemini na esteira Banco Ouro + V4, sem matar o enriquecimento diário do banco.
**Decisões de Miguel (chat Kimi Desktop, 29/07 ~02:10 BRT):** "botei carga de novo, mas vamos economizar… mais seletivos… banco tem várias fotos praticamente iguais… isso gasta gemini vision à toa" + "tem que ter um budget diário, para a gente ter imagens novas diárias. E o v4 precisa privilegiar fotos novas do v4, além de tentar pegar flickr".
**Memória técnica irmã:** `Cerebro/Memorias/memoria_ouro_precision_economia_gemini_20260729.md`

## Diagnóstico (dados reais do banco, 29/07 ~02:20)

- Tempestade de retentativas: **20.248 tentativas de visão em 7d para 153 fotos únicas** (132× por foto). `gemini_quarentena_humana`: 4.128 chamadas pagas para 125 fotos únicas (33× cada). Recorde: 1 foto reprocessada 302× (`dimensao_baixa`).
- Near-dup no acervo: **só 4%** (618 fotos → 594 clusters, dHash Hamming ≤5). A sensação de "muitas iguais" vem da fila humana (Lula 26/06: 7 cards do mesmo evento).
- Concentração: Alckmin 95 / Lula 93 / Haddad 88 vs Putin 1, Macron 2, Pichai 1.
- Causa raiz: o robô não tinha **memória de processamento** — o único dedup (hash no banco) acontecia DEPOIS da visão.

## Estratégia aprovada (5 camadas) e estado

| # | Camada | Estado 29/07 03:40 |
|---|---|---|
| M1 | Tombstone `ouro_processadas` (permanente nunca re-tenta; transitório backoff 1h→6h→24h→7d→30d) + dedup por URL pré-visão | ✅ DEPLOYADO + backfill 407 URLs (269 perm/138 trans) |
| M2 | Cascata **Qwen-first** no robô (Gemini só em falha/moderação/inválido do Qwen) | ✅ DEPLOYADO — A/B ao vivo: **92% paridade (11/12)**, divergência conservadora (segura) |
| M3 | Portão pHash na ingestão | 🟡 em modo sombra 48h (não ativado — aguarda calibração) |
| M4 | Quota de cobertura por entidade (≥12 frescas → manutenção; lacunas prioritárias) | ⏸️ aguardando (não aprovado ainda) |
| M5 | **Budget diário Gemini** (`BANCO_OURO_GEMINI_BUDGET_DIARIO=40`, tabela `ouro_visao_diaria`, log por ciclo) | ✅ DEPLOYADO |

**Extra aprovado na mesma conversa:** V4 prioriza fotos novas — bônus de frescor (≤7d +30 · ≤14d +20 · ≤30d +10 · ≤60d +5) na ordenação do `ouro_sqlite` e do `V4AuditedMediaStore.search`. Só afeta ordem de seleção, nunca score visual. Suite V4: 566/566.

## Prova do corte (ciclo supervisionado 03:01 BRT)

- Antes (ciclo 01:52, pré-patch): 154 candidatas → 100 rejeitadas = **~100 chamadas de visão**
- Depois (ciclo 03:01): 154 candidatas → **101 duplicadas + 52 tombadas + 1 processada** = **1 chamada Gemini** (foto do Xi — Qwen moderou, Gemini decidiu dentro do budget, como desenhado)
- Redução de ~99% nas chamadas por ciclo.

## Regras vivas derivadas

1. **Veredito permanente é permanente:** quarentena/dimensão/bytes/título/moderação nunca reprocessam (custo zero de revisita).
2. **Gemini é sniper, não metralhadora:** Qwen-first em tudo; Gemini só onde Qwen não consegue (moderação, falha, inválido) e dentro do budget diário.
3. **Frescor é critério de seleção, não de qualidade:** o bônus ordena; a régua visual decide.
4. **Falha de provedor ≠ veredito editorial:** (reafirma a regra do patch V4 melhor-esforço) erros transitórios têm backoff, nunca tombstone permanente.

## Pendências conhecidas

- Deploy NYC do patch V4 (melhor-esforço + frescor) — protocolo ouro.
- M3 pHash sombra → calibrar limiar (5/6/8) → ativar. M4 aguarda OK de Miguel.
- Moderação Qwen de Xi (data_inspection): coberta pelo fallback Gemini; monitorar se Putin/Kim etc. também são moderados.
- Painel: exibir "💰 visão hoje: X Qwen / Y Gemini" (dados já estão na tabela `ouro_visao_diaria`).
