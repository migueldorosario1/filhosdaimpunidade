# Lição 2026-09-02 · Escada do R1: HTTP 200 ≠ busca executada

## O quê
A CL-064 (10:21) reportou a escada de busca do R1 "caída inteira no ciclo ~10:0x" e pediu
verificação de chaves/endpoints. Sonda perna a perna (sem imprimir segredos) revelou o quadro
real: **GLM glm-5.3+web responde HTTP 200 mas o modelo devolve "não consigo realizar buscas na
web"** (a ferramenta web_search não devolve resultados) — e como o R1 para na 1ª perna com texto
não-vazio, qwen/grok nunca são tentados; **qwen-max+search idem** (200, "não tenho como realizar
buscas em tempo real"); **grok-4+live devolve HTTP 410 Gone com `search_parameters`** (sem o
parâmetro, grok-4/grok-4-fast/grok-3 respondem 200 — formato do payload mudou/foi desligado);
**deepseek-chat devolve 401 com a chave do `.env.unificado` do R1 (velha) vs 200 com a chave
canônica de `~/.dsh/llm_env`**. O log do R1 mostra `ok=False modelo=glm-5.3+web` desde ~22h de
01/09 — ou seja, a escada não caiu "só no 10:0x": caiu inteira na véspera e o R1 vem fazendo
fail-close correto (CORREÇÕES sem busca) o dia todo, com o fluxo coberto pelo check manual da CL.

## Por quê
(1) HTTP 200 do provedor só diz que a chamada chegou — não que a BUSCA aconteceu; um modelo que
responde "não consigo buscar" é texto não-vazio e o R1 (desenho atual) aceita a 1ª perna com texto
como resposta final. (2) Chaves vivem em DOIS lugares (`.env.unificado` dos robôs DSN e
`~/.dsh/llm_env` canônico) e podem dessincronizar — a chave velha do DeepSeek no `.env.unificado`
é 401, a canônica é 200. (3) Payloads de busca proprietários (xAI search_parameters) mudam sem
aviso — 410 Gone é o sintoma típico.

## Como aplicar
- Antes de decretar "escada caída por falta de crédito/chave", SONDE perna a perna com prompt curto
  (custa centavos): separa "chave morta" (401/402/429) de "tool sem retorno" (200 sem busca) de
  "payload obsoleto" (410/400).
- Correção recomendada (dono R1/ZM): (1) R1 não para na 1ª perna que devolve texto sem evidência
  de busca — detecta "sem busca" e cai pra próxima; (2) ajustar payload do grok (remover
  search_parameters obsoleto) ou trocar a perna; (3) sincronizar DEEPSEEK_API_KEY do
  `.env.unificado` com a canônica do `llm_env`.
- Enquanto a escada não volta, o check MANUAL da CL (fontes citadas, Art. 3 do contrato v3) cobre —
  fail-close do R1 está funcionando como desenhado (nada aprova sem fonte); o custo é só o fluxo
  depender da CL.
- Regra de ouro: HTTP 200 do LLM ≠ tarefa executada — validar o CONTEÚDO (busca deu resultado?)
  antes de confiar na perna.
