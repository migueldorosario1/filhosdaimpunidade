# FÓRUM — MODELO PILOTO: Agente Manchete Inteligente (seletor de LLM dinâmico + telemetria redundante + reescrita ativa) — 12/08/2026

**Data:** 2026-08-12 ~20:05 BRT *(na linha do tempo UTC)*
**Autor:** ZCode (GLM-5.2, Z.ai coding plan — fallback final; Kimi/Qwen 🔴🔴)
**Status:** 🟡 DESIGN do piloto (para aprovar e implementar). Piloto = agente manchete; se der certo, **reproduz pro ecossistema todo**.
**Origem:** Miguel — *"telemetria precisa ser redundante, não só prometheus. vamos fazer um modelo dessa arquitetura inteligente para o agente manchete. a llm será escolhida dinamicamente, por um seletor que mistura preço e qualidade. dando certo a gente reproduz pra todo o ecossistema. pra escolher a manchete é preciso também ser capaz de, eventualmente, reescrever, ajustar e alterar a manchete e até mesmo o post da manchete."*
**Relacionado:** `forum_seletor_llm_inteligente_telemetria_20260812.md` (princípios) · `forum_arquitetura_curadoria_manchete_estavel_20260812.md` (curadoria) · `forum_curadoria_inteligente_manchete_20260812.md` · `CEREBRO_NODE_MANCHETE.md` (Redatores/Authors)

---

## 0. Escopo do piloto

Construir o **agente manchete inteligente** como **piloto** de 3 capacidades novas do ecossistema:
1. **LLM escolhida dinamicamente** por um seletor (preço+qualidade+saldo) — **zero hardcode**.
2. **Telemetria REDUNDANTE** (não só Prometheus).
3. **Editoração ativa**: escolher **E** reescrever/ajustar a manchete e o post.

**Critério de generalização:** o piloto é validado (métricas §8) → o mesmo padrão (seletor + telemetria redundante + assinatura) é reproduzido nos demais agentes (comentarista, redação, revisão, títulos...).

## 1. Seletor de LLM dinâmico (resumo — detalhe no fórum-irmão)

```
escolher_modelo(capacidade, contexto) → {modelo, motivo, score}
score = w_q·qualidade + w_p·(1/preço) + w_s·saldo_disponível
```
- Modelo sem saldo = **0** (vigília já existe).
- **Capacidades do agente manchete** (cada uma pede ao seletor, cada uma pode usar modelo diferente):
  - `curadoria_manchete` (avalia candidato, nota 0-1000)
  - `reescrita_titulo_manchete` (deixa o título com tese mais forte)
  - `reescrita_lead_post` (ajusta abertura/ângulo do post)
  - `classificacao_risco_editorial` (fere a linha? veto?)

## 2. Editoração ATIVA (reescrita) — capacidades + salvaguardas

O agente manchete não só **escolhe** — pode **melhorar** o post escolhido. Sub-capacidades:
- **(a) Reescrever o título da manchete** → tornar mais forte/tese/lúdico (herda as 2 regras-mãe FORTE+SIMPLES+LÚDICO+POLÍTICO e TÍTULO=TESE já usadas pelo conselheiro de títulos).
- **(b) Ajustar o lead/abertura do post** → ângulo mais incisivo.
- **(c) (futuro) Gerar manchete a partir do post** quando não houver título forte.

### Salvaguardas (editoriação ativa é sensível — muda o que o leitor vê)
| Salvaguarda | Como |
|---|---|
| **Revisões WP** | toda alteração passa pela `wp_revision` (WP guarda histórico automático) — **rollback sempre possível** |
| **Diff registrado** | guarda **antes→depois** (hash + diff) na assinatura; notifica o Miguel |
| **Aprovação humana (modos)** | `modo_editor = auto` (aplica) / `propoe` (cria rascunho/revisão, Miguel aprova) / `off`. Default começa em **`propoe`** até calibrar |
| **Regras editoriais** | nunca alterar **fato**; só aprimorar título/lead/ângulo; respeitar linha vinculante (proibido atacar STF/Lula/Irã/Rússia) — o `classificacao_risco_editorial` veta se fere |
| **Auditoria** | toda reescrita assinada (modelo/motivo/diff) + telemetrada |
| **Rate-limit** | no máx N reescritas/post/dia (não fica mexendo sem parar) |

## 3. Telemetria REDUNDANTE (multi-canal — não depender só do Prometheus)

**Princípio:** cada evento importante é gravado em **≥2 canais independentes**, pra sobreviver a falha de qualquer um.

| Canal | O que guarda | Por quê |
|---|---|---|
| **1. JSONL local assinado** (append, `/root/agent_data/telemetria_llm.jsonl`) | toda chamada LLM + toda decisão (escolha/reescrita) | canônico, imutável, sobrevive a tudo |
| **2. Prometheus** (Alibaba, já existe) | métricas agregadas (counters/histograms/gauges §5) | consulta/painel/alertas |
| **3. Push secundário** (POST pra endpoint backup — ex: espelho no servidor canônico, ou B2) | eventos críticos (decisões de manchete, reescritas, custos altos) | redundância geográfica |
| **4. (opcional) Telegram** | alertas de exceção (modelo sem saldo, custo > teto, reescrita aplicada) | visibilidade imediata do Miguel |

> Cada evento crítico grava no **JSONL + Prometheus + push secundário** (3 canais). Métricas leves só JSONL+Prometheus. Falha num canal **não** perde o dado (outros têm).

## 4. Assinatura (registro de cada ação LLM/decisão) — schema

Append-only JSONL, uma linha por ação:
```json
{"ts":"...","agente":"agente_manchete","capacidade":"curadoria_manchete",
 "modelo":"...","versao":"...","provider":"...",
 "motivo_escolha":"score=0.87 top1/5 (q=0.9,p=0.8,saldo=ok)",
 "tokens_in":312,"tokens_out":88,"custo_usd":0.00012,"latencia_ms":1840,
 "ok":true,"erro":null,
 "acao":{"tipo":"escolha_manchete"|"reescrita_titulo"|"reescrita_lead",
         "post_id":265426,"antes_hash":"sha8:...","depois_hash":"sha8:...",
         "diff_titulo":"...→...","nota_curadoria":720,"motivos":["denuncia_flavio","tese"]},
 "telemetria_canais":["jsonl","prometheus","push_secundario"]}
```
> **Regra do Cofre:** guarda **hash** do conteúdo (não o texto), salvo debug com TTL. Tokens/custo/diff sempre.

## 5. Métricas Prometheus (piloto)

`llm_chamadas_total{agente,capacidade,modelo,ok}` · `llm_tokens_total{modelo,direcao}` · `llm_custo_usd_total{modelo,capacidade}` · `llm_latencia_ms{modelo,capacidade}` · `manchete_escolhas_total{motivo}` · `manchete_reescritas_total{tipo,modo}` · `manchete_estabilidade_seg` (gauge: tempo que a manchete atual está no topo) · `seletor_modelo_score{modelo,capacidade}` (gauge).

## 6. Fluxo completo do agente manchete inteligente (piloto)

```
cron 0 */2 * * *  (agente_manchete_v2.py)
 1. fetch_recent_posts (cat 22, 24h) — veto author 5786 (repetidor)
 2. para cada candidato: capacidade=curadoria_manchete → seletor escolhe LLM → nota 0-1000 + motivos
 3. threshold ≥600; estabilidade (permanência 6h / histerese 1.25× / override 900+humano)
 4. se trocar manchete:
      a. capacidade=reescrita_titulo_manchete → seletor → propõe título (modo_editor=propoe default)
      b. capacidade=reescrita_lead_post → seletor → propõe lead
      c. classificacao_risco_editorial → veto se ferir linha
      d. aplica (ou cria revisão p/ aprovação) + registra diff + assina + telemetria 3-canais
      e. set-manchete + apply_headline(cat 5087) + registra desde_quando
 5. disparador_enxame (cron 10min) cuida do enxame 80-130 nela
```

## 7. Decisões pendentes (pra eu implementar o piloto)

1. **`modo_editor` inicial:** `propoe` (Miguel aprova) — recomendado pra calibrar — ou `auto`?
2. **Reescrita:** só **título**, ou **título + lead** desde o início?
3. **Seletor pesos** p/ capacidades do manchete: curadoria (qualidade pesa +), reescrita (qualidade ++), classificação (barato).
4. **Canal push secundário:** espelho no canônico, B2, ou outro?
5. **Modelos elegíveis** p/ o piloto (shortlist): DeepSeek-V4, Gemini 2.5 Flash/Pro, Claude Haiku, Qwen — confirmar conjunto.

## 8. Métricas de sucesso do piloto (pra decidir generalização)

- Repetidor estatal (5786) **some da manchete**.
- Manchetes **estáveis** (median ≥6h no topo).
- Manchetes = redação humana (2018/5780) ou quentes, com **temperatura editorial alta**.
- Custo do piloto **dentro do esperado** (~$0.01-0.10/dia) — telemetria confirma.
- **Zero** reescrita que fira a linha editorial (classificador veta).
- Telemetria redundante: **nenhum evento perdido** (JSONL = Prometheus = push).
- Miguel aprova as reescritas-proposta (modo `propoe`) → confiança p/ `auto`.

## 9. Próximos passos

1. Miguel decide §7 (modo_editor, escopo reescrita, pesos, canal, shortlist).
2. Sprint piloto: seletor mínimo + assinatura JSONL + telemetria (JSONL+Prometheus+push) + curadoria + reescrita (propoe) no `agente_manchete_v2.py` (novo, ao lado do legado).
3. Validar §8 → se OK, **generalizar** o padrão (seletor + telemetria redundante + assinatura) pros demais agentes.
4. Tema Duplo (memória) quando implementado.

---

— **ZCode (GLM-5.2, Z.ai coding plan)**, 12/08/2026
