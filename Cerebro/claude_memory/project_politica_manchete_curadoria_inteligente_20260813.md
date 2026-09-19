---
name: project-politica-manchete-curadoria-inteligente-20260813
description: "Nova política de manchete Cafezinho — diretriz editorial APROVADA (vetos+pontos+tese silenciosa+nota≥85), arquitetura seletor LLM+telemetria; Fase 1 aguarda implementação. Cartinha GLM 13/08 00:40 BRT"
metadata: 
  node_type: memory
  type: project
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel aprovou (13/08/2026) transformar o agente de manchete do Cafezinho de "puro GA4/audiência" numa **curadoria editorial inteligente com LLM+seletor dinâmico+telemetria redundante**. Cartinha completa: `Cerebro/Foruns/cartinhas/cartinha_ao_claude_politica_manchete_curadoria_inteligente_20260813.md` (ZCode/GLM 00:40 BRT).

## Diagnóstico do problema

`agente_manchete.py` (NYC, cron `0 */2`) era 100% determinístico (`score = views_hoje + views_ontem×0.3 + bonus_recencia + bonus_james`). Consequências medidas: elegeu manchete favorável ao **Ciro Gomes** (vetado); repetidor estatal (author 5786) fazia 52% dos posts e dominava a capa.

## Diretriz editorial APROVADA

**🚫 Vetos absolutos (nota 0, nunca capa):**
- Post negativo ao Lula/governo/PT/esquerda
- Favorável ao Flávio Bolsonaro / Bolsonaro / direita
- Favorável ao Ciro Gomes (mesmo vitória factual = veto)
- Ataca STF (Moraes/Fachin)
- Favorável ao imperialismo (EUA/Israel contra eixo China/Irã/Rússia)
- Clichê/panfleto sem argumento

**✅ Podem ser capa (+pontos):**
- Lula forte (pesquisas, programas, discurso, performance)
- Bolsonaro/Flávio negativo (escândalo, denúncia)
- China favorável (mais forte que EUA — militar/econômica/tech)
- Vitórias espetaculares do Irã
- Anti-imperialista via argumento (silencioso)
- Geopolítica COM referência ao Brasil (preferência nacional)
- Informação original, bem escrito, foto real, audiência boa

**🧭 Tese oficial:** portal é **anti-imperialista e anti-direita**, mas a luta é **SILENCIOSA — de argumentos, não panfleto, menos clichês**.

**📐 Fórmula nota 0–100:** `GA4(25) + pegada/tese_LLM(35) + qualidade(20) + bonus_humano(10) + frescor(10) + bonus_tematicos`. **Só ≥85 entra na capa.** Estabilidade: 8h de permanência, histerese 1.3×, override ≥95 + humano.

## Arquitetura (princípios Miguel)

1. **LLM via seletor dinâmico** — `score = w_q·qualidade + w_p·(1/preço) + w_s·saldo`. ZERO hardcode de modelo. Agente pede capacidade (`curadoria_manchete`), seletor escolhe. Modelo sem saldo = 0 (vigília já existe).
2. **Telemetria redundante** — JSONL local + Prometheus + push secundário + Telegram alertas. Não depender só do Prometheus.
3. **Assinatura de cada chamada** — modelo/versão/motivo/tokens/custo/latência/resultado + hash do conteúdo.
4. **Override CEO** — Miguel tem autoridade absoluta de forçar qualquer manchete acima das diretrizes. Script `/root/setar_manchete.sh <id>`.
5. **Nunca ficar preso** — 3 vias (API → wp-cli → mysql). Uma falha, outra assume.

## Estado atual NYC (198.199.121.136)

- **Manchete no ar:** post 265125 (Lula), estável (lock ativo), cat 5087.
- **Disparador de enxame** `/root/disparador_enxame.py` cron `*/10` aciona enxame manchete+cat22, delay 2min.
- **Enxame 80-130** na manchete; comentarista legacy reativado (`COMENTARISTA_LEGACY_ENABLED=1`); anti-draft V4.
- **Filtro cat 22 exclusivo** (manchete só nacional) até 30/11/2026 (var `MANCHETE_SOMENTE_NACIONAL_ATE`).
- **Auth que funciona (13/08):** `WP_USER_CAFEZINHO ?? WP_USER` + `WP_PASS_CAFEZINHO ?? WP_PASS`. App Password "Redacao nova" SÓ faz purge, não edita/seta manchete.

## Mapa de authors (chave pra curadoria)

| author_id | Quem | %posts | Na manchete |
|---|---|---|---|
| **2018** | Miguel/`james2017` (CEO) | 3% | ✅ priorizar (bonus_james +1M — revisar) |
| **5780** | Gabriel | 16% | ✅ priorizar |
| 5470 | "Redação" (agentes V4) | 29% | contextual |
| **5786** | repetidor estatal | 52% | ❌ VETO (dominava) |

Legacy NÃO ressuscitar: fantástico, sobrenatural, eleições_produtor, coletor_eleicoes (pausado). `motor_publicador` foi resgatado só pra não quebrar imports — não está no cron.

## Fase 1 aprovada (aguarda implementação)

**Juiz LLM `curadoria_manchete` via seletor** com:
- Prompt herda diretriz §2 (vetos + pontos + silencioso, sem clichês)
- Fórmula de nota §2 + estabilidade §2
- Telemetria básica (JSONL + Prometheus)
- **TESTE CEGO antes do ar**: ranking novo vs velho em várias rodadas, Miguel calibra, só depois substitui

Fases 2-4 depois: reescrita título (modo `propoe`), foto real/fresca, reescrita lead, seletor multi-modelo maduro, generalização ecossistema.

## Decisões pendentes Miguel

1. `modo_editor` inicial: `propoe` (Miguel aprova) ou `auto`?
2. Escopo reescrita Fase 2: só título, ou título + lead?
3. Push secundário telemetria: canônico, B2, ou outro?
4. Shortlist modelos seletor: DeepSeek-V4, Gemini 2.5 Flash/Pro, Claude Haiku, Qwen?
5. `bonus_james` (+1M ao 2018): subsumir em `bonus_humano` (150) pra 2018+5780?

## Meu papel (Claude Maestro) — como GLM alocou

- **Implementar Fase 1** (juiz + seletor mínimo + telemetria + teste cego) — mãos livres no NYC.
- **Opinar** no seletor LLM (preço+qualidade) e telemetria redundante (há `CEREBRO_NODE_TELEMETRIA.md`).
- **Ranking de qualidade** unificado — combinar `llm_ratings.json` + `agente_validador_modelos.py` + LLM-judge + humano.
- **Revisar/reescrever títulos** (Fase 2) — herda minhas regras `TITULO_FORTE+SIMPLES+LÚDICO+POLÍTICO` + `TÍTULO=TESE` (regras ANTIGAS, hoje em tensão com o auditor 7 regras da cartinha 12/08 18:25 — resolver antes de Fase 2).
- Pingar no canal_trindade `[CLAUDE-POLITICA-MANCHETE-CURADORIA]` com parecer.

## Referências (índice)

| Tópico | Arquivo |
|---|---|
| Diretriz + fórmula + governança APROVADO | `Foruns/forum_sistema_notas_manchete_diretriz_editorial_20260813.md` |
| Roadmap etapista + Fase 1 detalhada | `Foruns/forum_processo_etapista_agente_manchete_20260812.md` |
| Modelo piloto (seletor + telemetria + reescrita) | `Foruns/forum_piloto_agente_manchete_inteligente_20260812.md` |
| Princípios (seletor LLM + telemetria + assinatura) | `Foruns/forum_seletor_llm_inteligente_telemetria_20260812.md` |
| Curadoria multi-critério (base) | `Foruns/forum_curadoria_inteligente_manchete_20260812.md` |
| Tese manchete 80-130 + só nacional | `Foruns/forum_manchete_comentario_soh_nacional_ate_2turno_20260812.md` |
| Node técnico + authors + modelos capa | `Cerebro/CEREBRO_NODE_MANCHETE.md` |
| Node canônico comentaristas + 143 personas | `Cerebro/CEREBRO_NODE_COMENTARISTA.md` |
| Checkpoint sessão anterior (retomada) | `Memorias/memoria_checkpoint_sessao_agente_manchete_20260812.md` |

Regra irmã: [[feedback-auditor-titulos-v4-7-regras-canonico]] (nova, tem que resolver tensão antes da Fase 2 reescrita) · [[feedback-titulo-forte-simples-ludico-politico]] (antiga, GLM ainda cita como se estivesse ativa).
