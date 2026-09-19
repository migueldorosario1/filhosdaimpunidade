# Nota de laboratorio V4

Este diretorio e uma copia de teste do V4 em `Projeto Cafezinho Agentes/root/v4_labs/`.

Ele nao e o diretorio final de producao. Serve para validar caminhos, contratos e testes antes da promocao para:

```text
Projeto Cafezinho Agentes/root/v4/
```

Escopo atual:

```text
- Fase 3 preflight;
- sem chamada LLM externa;
- sem WordPress real;
- sem publicacao real;
- coleta USTR/Federal Register e transcricao oficial USTR Day 2 registradas para 261439;
- redator_real_llm nao e mais bloqueado por coleta;
- chamada LLM real foi autorizada somente em laboratorio e tentou as rotas canonicas disponiveis;
- a tentativa final com Gemini gerou texto real completo apos smoke real e ajuste de thinking_budget.
```

Nota factual:

```text
A audiencia USTR ocorreu em 6 e 7 de julho de 2026. A transcricao oficial do Dia 2 registra Flavio Bolsonaro no Painel 8 em 7 de julho de 2026. A publicacao real segue bloqueada ate confirmar o comentario escrito no docket USTR-2026-0331 ou citar essa limitacao com prudencia.
```

Resultado da chamada real:

```text
achado: healthcheck local anterior nao detectava billing/credito;
smoke real Gemini: OK apos recarga;
ajuste tecnico: thinking_budget=0 para evitar saida truncada por MAX_TOKENS invisivel;
gate novo: saida curta/interrompida vira redator_real_llm_incompleto;
resultado final: gemini/gemini-3.5-flash -> redator_real_llm_pronto.

Artefatos:
dados/producao_shadow/v4_real_001.redator_real_attempts.jsonl
dados/producao_shadow/v4_real_001.redator_real.json

wordpress_real=false em todas as tentativas.
texto_real=5526 caracteres.
```

Validacao:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
```

Resultado esperado:

```text
OK 56 contract tests
```

Observacao de caminhos:

```text
config/ e uma copia de laboratorio da config LLM.
O codigo resolve providers, ratings e rotas por config/ local; nao ha shim de compatibilidade.
```
