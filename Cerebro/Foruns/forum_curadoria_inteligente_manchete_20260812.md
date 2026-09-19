# FÓRUM — Curadoria inteligente do Agente Manchete (audiência + temperatura editorial) — 12/08/2026

**Data:** 2026-08-12 ~19:35 BRT
**Autor:** ZCode (GLM-5.2, Z.ai coding plan — fallback final; Kimi/Qwen 🔴🔴)
**Status:** 🟡 PROPOSTA/DESIGN (para debate e aprovação do Miguel). Sem mudança em código nesta fase.
**Relacionado:** `CEREBRO_NODE_MANCHETE.md` (seção Redatores/Authors) · `forum_manchete_comentario_soh_nacional_ate_2turno_20260812.md`

---

## 1. O diagnóstico (por que mudar)

O `agente_manchete.py` escolhe a manchete de forma **puramente determinística** (zero LLM, zero critério editorial):

```
score = views_hoje + (views_ontem × 0.3) + bonus_recencia + bonus_james
```
- `bonus_recencia`: degraus por idade (≤3h→+50, ≤6h→+30, ≤12h→+15, ≤18h→+5).
- `bonus_james`: ⚠️ **hardcode** +1.000.000 se autor=`james2017`(2018) e idade ≤8h (sempre vence).

**Problema:** a manchete é só "o post mais lido" (+ 1 exceção hardcoded). Falta **curadoria editorial** e **priorização da redação humana**.

## 2. A direção do Miguel (ordem 12/08)

> *"temos que priorizar posts humanos, tirar o repetidor estatal da manchete. focar em posts mais quentes. curadoria inteligente, que misture audiência no ga4 com outros elementos: calor da notícia, frescor, polêmicas, denúncias contra flavio bolsonaro, escândalos, posts com boa tese, reviravoltas, grandes performances de lula, denúncias contra o papel imperialista. o post precisa ser interessante, ter informações novas. dois redatores principais: Miguel e Gabriel."*

**Redatores humanos principais:** Miguel + **Gabriel (author_id 5780)**.

## 3. Os elementos editoriais a somar ao GA4 (critérios do Miguel)

| Categoria | Sinais (exemplos) |
|---|---|
| **Calor da notícia** | urgência, está "pegando fogo" agora |
| **Frescor** | recência (já parcialmente no `bonus_recencia`) |
| **Polêmica / tese forte** | post tem uma **boa tese**, gera debate |
| **Denúncia** | contra **Flávio Bolsonaro**, escândalos |
| **Anti-imperialismo** | denúncias do **papel imperialista** (EUA/Israel/etc.) |
| **Performance progressista** | grandes **performances de Lula** / governo |
| **Reviravolta** | mudança de cenário, fato novo inesperado |
| **Informação nova** | exclusiva, dado inédito, ângulo original |

## 4. Design proposto — nova função de scoring

```
novo_score = score_ga4                                  # bases: views_hoje + views_ontem*0.3 + bonus_recencia
           + BONUS_HUMANO      se autor ∈ {Miguel, Gabriel}      # prioriza redação humana
           - PENALTY_REPETIDOR  se autor = repetidor_estatal      # tira o repetidor estatal
           + temperatura_editorial_llm                          # LLM avalia o "calor editorial" (0..TETO)
```

### 4.1 `temperatura_editorial_llm` (a inovação)
Um **LLM barato** (DeepSeek-V4-Flash) avalia cada candidato (título + resumo + trecho) e devolve uma **nota de temperatura editorial** estruturada, ponderando os critérios do §3. Exemplo de saída:
```json
{"temperatura": 720, "motivos": ["denuncia_flavio", "reviravolta", "tese_forte"], "info_nova": true}
```
Essa nota vira um bônus (ex.: `+temperatura`, calibrado pra competir com views sem esmagar). **Critério editorial transparente e auditável** (loga os motivos).

### 4.2 Whitelist humana + veto do repetidor
- **Whitelist** (`BONUS_HUMANO`): posts de **Miguel + Gabriel** ganham bônus fixo (prioriza redação própria mesmo com menos views iniciais).
- **Veto** (`PENALTY_REPETIDOR`): posts do **repetidor estatal** nunca viram manchete (penalidade > qualquer score).

### 4.3 `bonus_james` — rever
O hardcode +1M pro author 2018 (james2017) **sempre força manchete** nas 1ªs 8h. Com a curadoria inteligente, isso perde sentido. **Decidir:** remover, manter, ou converter num `BONUS_HUMANO` (se James for redator humano relevante).

## 5. Prompt de avaliação (esboço — temperatura editorial)

```
Você é o editor-chefe do portal O Cafezinho (progressista, anti-imperialista, focado em política nacional).
Avalie a TEMPERATURA EDITORIAL deste post como candidato à manchete (0 a 1000), ponderando:
- Calor/urgência da notícia (está pegando fogo agora?)
- Tese forte / polemica / angulo original
- Denúncia (Flávio Bolsonaro, escândalos, corrupção, papel imperialista)
- Performance progressista (Lula, governo)
- Reviravolta / fato novo
- Informação nova / exclusiva
Retorne SÓ JSON: {"temperatura": int, "motivos": [...], "info_nova": bool}
Título: ...
Resumo: ...
```
(Calibrar: a linha editorial vinculante do Cafezinho já existe nos prompts do `motor_publicador` — herdar.)

## 6. Pendências (pra implementar)

1. **Mapear author_ids:** Miguel (a confirmar) + repetidor estatal (a confirmar) — via wp-cli/banco do canônico ou o Miguel informa. *(Gabriel=5780 ✅)*
2. **Decidir o `bonus_james`**: remover / manter / converter.
3. **Escolher LLM** da temperatura editorial (DeepSeek-V4-Flash, barato) + **calibrar o teto** (pra não esmagar o GA4 nem ser irrelevante).
4. **Custo:** +1 chamada LLM por candidato por rodada (a cada 2h, ~7 candidatos) = baixo (~few calls/2h).
5. **Decidir pesos finais** (após teste cego de algumas rodadas).

## 7. Próximos passos

1. Miguel confirma os 2 author_ids (dele + repetidor) e a decisão sobre `bonus_james`.
2. Implemento a nova função de scoring (backup + py_compile): whitelist humana, veto repetidor, e o `temperatura_editorial_llm`.
3. Teste cego: rodar o agente em modo "diagnóstico" comparando o ranking antigo vs. novo em algumas rodadas, pra calibrar pesos.
4. Validar ao vivo e ajustar.

---

— **ZCode (GLM-5.2, Z.ai coding plan)**, 12/08/2026 ~19:35 BRT
