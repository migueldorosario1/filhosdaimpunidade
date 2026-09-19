---
name: Blindagem universal anti-alucinação de atribuição (corrigir_ancoras_inconsistentes)
description: Pós-processador em util_fonte.py que cruza domínio do href com texto-âncora antes do POST WP. Plugado em motor_publicador + agente_eleicoes_produtor. Protege ~20 agentes monolíticos retroativamente. Deployado Tencent 2026-04-24 19h.
type: project
originSessionId: 7b364031-59bc-4cee-8526-b9521b506352
---
## Bug que motivou

Post #239383 (Agente Eleições) saiu com `<a href="cartacapital.com.br/...">portal Folha de S.Paulo</a>` — texto-âncora errado porque o LLM tinha visto "Folha" mencionada no snippet e usou esse nome no âncora, mesmo a URL canônica sendo de outro veículo.

## Fix universal

Função `corrigir_ancoras_inconsistentes(html, log_corrigidos=None)` em `util_fonte.py`:
1. Para cada `<a href>...</a>`, extrai domínio + texto-âncora.
2. Resolve nome canônico via `nome_amigavel_fonte(href)`.
3. Se âncora menciona OUTRO veículo conhecido e não o canônico → troca pelo canônico.
4. **Exceção:** ignora links pra domínios internos do enxame (`_DOMINIOS_INTERNOS_DO_PROJETO`) — interlinks internos usam título do post como âncora.

## Pontos de integração (deployados Tencent)

- `motor_publicador.py` linha ~1320 (antes do `requests.post(WP_URL, ...)`) — Trindade + temáticos.
- `agente_eleicoes_produtor.py` linha ~1056 (antes do POST) — Pilar 1.

Log: `🛡️ [ANCORAS] corrigidas N inconsistências de atribuição`.

## Cobertura retroativa

Pega ~20 agentes monolíticos sem alterar prompt nenhum:
- Trindade (motor_coletor + motor_publicador + masters)
- Temáticos premium (lula, ia, latam, sheinbaum, mercado, matriz, inflacao)
- Nicho (ferroviario, fantastico, feminino, china, militar, crime, turismo, singularidade)
- Eleições (produtor v1.1 + v2 quando migrar pra Two-Pass)

## Falso positivo conhecido (já corrigido em v2)

V1 da função NÃO tinha exceção pra domínios internos. Aplicada no #239383 trocou o âncora do interlink interno (título do post citado) por "OCAFEZINHO". V2 (deployada) tem `_eh_dominio_interno()` que pula esses links.

## MD5 deployado em 2026-04-24 19h

```
7d1d67bf2dd42a3e67c317c5c955dea7  util_fonte.py
69b2241be36bc71730cad569fb9860db  motor_publicador.py
d8e416a3b9d093a82dd7b4370d033e9b  agente_eleicoes_produtor.py
```

## Backups pré-deploy

`/root/*.bkp-pre-blindagem-20260424_1907`

## Documentação

- `forum_eleicoes_teste_cruzado_analise_20260424.md` — relato completo + smoke test + aplicação retroativa.
- `forum_agenteanalise.md` §14 — relatório dos 2 testes do Análise (sem este bug, porque Análise usa Two-Pass).
