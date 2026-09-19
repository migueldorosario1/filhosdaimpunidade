---
name: feedback-gate-110-anacronismo-hard-pre-publish
description: "Gate §110: autocura defensiva sem LLM no motor_publicador.py linha 2568 que rebaixa pra draft qualquer publish com ano antigo no título ou lide+verbo atual, salvo palavra histórica explícita. Última trincheira após incidente #259974."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 94bb006f-7e8f-4abb-a70e-312694d7ec88
---

**Gate §110 = última trincheira anti-anacronismo no motor_publicador.py, independente de LLM. Sancionado por Miguel 2026-06-20 14:08 BRT após incidente #259974 onde 5 camadas de auditoria LLM aprovaram "Análise de 2020: Irã desafia coerção dos EUA".**

## Arquitetura

- **Arquivo novo**: `/root/util_gate_anacronismo.py` (heurística regex pura, sem LLM, sem rede)
- **Injeção em**: `/root/motor_publicador.py` linha 2568, ANTES de `requests.post(WP_URL, ...)` linha 2575 (fora do try interno do POST)
- **Pattern §92**: backup `/root/motor_publicador.py.bak_pre_gate_110_anacronismo_20260620_1647` + try/except fail-open + log GRAVE

## Lógica do gate

```
REGRA 1 (título): ano < (atual-1) no TÍTULO sem palavra histórica → BLOQUEIA
REGRA 2 (lide):   ano < (atual-1) na 1ª frase + verbo atual sem palavra histórica → BLOQUEIA
DEMAIS: LIBERA (referências históricas em contexto são OK)
```

- `_PALAVRAS_HISTORICAS`: "história", "aniversário", "memória", "passado", "década", "guerra fria", "ditadura militar", etc — autoriza ano antigo
- `_VERBOS_ATUAIS_TIPICOS`: "anuncia", "afirma", "declara", "publica", etc — combinado com ano antigo = padrão tóxico
- `_REGEX_ANO`: `\b(19[89]\d|20[0-2]\d)\b` (1980-2029)

## Comportamento na falha

- Quando bloqueia: `payload["status"] = "draft"` + log `🛑 [§110 ANACRONISMO] publish rebaixado para draft. {motivo}`
- Idempotente: chamadas repetidas no mesmo payload não duplicam ação
- Fail-open: exception interna não bloqueia produção (retorna sem alterar)

## Smoke real validado no Tencent (4/4 PASS)

| Caso | Esperado | Got |
|---|---|---|
| "Análise de 2020: Irã desafia coerção dos EUA" (caso fundador #259974) | draft | ✅ draft |
| "Lula assina decreto em 2026 sobre clima" | publish | ✅ publish |
| "Aniversário de 2008: 18 anos da crise global" | publish | ✅ publish (palavra-gatilho) |
| "Putin defende posição" + lide "anunciou em 2019" | draft | ✅ draft |

## Why

Diagnóstico do incidente #259974 (cadeia de 5 LLMs aprovando):
1. gpt-4o produtor preservou "2020" no título
2. gemini-2.5-flash auditor APROVOU
3. gemini-2.5-flash revisor swarm APROVOU
4. **claude-haiku-4-5-20251001 com WebSearch como Auditor Elite APROVOU** ← grave
5. gemini-2.5-flash VETO fact-check APROVOU

Apesar de TODAS receberem `obter_contexto_temporal()` no prompt e existir `factcheck_noticia_atual` com regra TEMPORALIDADE rodando (linha 1760 motor_publicador.py). Os LLMs ignoraram contexto temporal sistematicamente. Conclusão: defesa por LLM é insuficiente sozinha — precisa camada determinística final.

## How to apply

1. **Não desligar nunca o gate §110** — é última linha de defesa. Se houver bloqueio falso positivo, refinar `_PALAVRAS_HISTORICAS` (adicionar palavra-gatilho) em vez de desligar.
2. **TODO agente que publica via motor_publicador** ganha proteção automática (soberania, latam, china, ia, fantástico, militar, eleicoes, lula, flavio, crime, repetidor, sheinbaum, turismo, etc).
3. **YT V2 publicador** NÃO usa motor_publicador.py — usa pipeline próprio. Aplicar gate equivalente lá se anacronismo aparecer (vídeos antigos podem virar matéria atual). Considerar quando Kimi for ativar Fase 1 PT/EN.
4. **REFORMA/Política V2 publicador** (futuro, Kilo) — replicar mesmo padrão antes de produção real.
5. **Falsos positivos** podem aparecer em matérias sobre balanços anuais ("dados de 2025 mostram", "comparativo 2024 vs 2026") — monitorar e adicionar palavras como "dados de", "balanço de", "comparativo" se virar problema recorrente.

## Decisões editoriais correlatas (mesma sessão Miguel 20/06)

- **claude-haiku-4-5-20251001** rebaixado: `ANTHROPIC_WEBSEARCH_MODEL` default trocado de haiku → `claude-sonnet-4-6` em `agente_roteador_llm.py:1174`. Backup `*.bak_pre_rebaixar_haiku_auditor_20260620_1557`. Auditor Elite com WebSearch agora vai pra sonnet.
- **Misantropia #259980 + Macanao #259977** receberam cat 20699 (no_home) via WP API direta. Ambos eram matérias regionais/leves indevidamente em home.

Relacionado: [[feedback-yt-v2-4-regras-cap-sentence-canal-cat]], [[feedback-creditos-apis-primeiro-item-diagnostico-lentidao]], [[feedback-corrigir-na-raiz-nao-no-auditor]]
