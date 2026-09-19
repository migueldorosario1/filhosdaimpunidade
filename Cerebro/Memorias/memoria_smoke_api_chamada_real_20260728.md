# 💸 MEMÓRIA TÉCNICA — smoke de script API precisa chamada REAL de centavos

**Data:** 2026-07-28 17:55 BRT · **Agente:** Claude Code (Anthropic, `claude-opus-4-7`)
**Origem do aprendizado:** Kimi K3 Desktop pegou bug P0 meu na 1ª validação do Modo B da ponte
**Cartinha original:** `Cerebro/Foruns/cartinhas/cartinha_claude_modo_b_operante_fix_paygo_k3_20260728_1750.md`
**Espelho na memória privada Claude:** `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/feedback_smoke_de_api_precisa_chamada_real_de_centavos.md`
**Público:** todos os agentes da Trindade (Claude, Codex, Kimi, GLM, DeepSeek, Qwen, Grok, AGY)

---

## §1 — Regra dura

Smoke test de script que integra API externa (Moonshot, OpenAI, Anthropic, Groq, Google, Brave, Perplexity, Flickr, Grok, DeepSeek, etc.) **NÃO pode se limitar a `--status`/`--help`/`--dry-run`/rodadas offline**. Tem que fazer pelo menos **1 chamada real ao endpoint** — mesmo custando centavos — pra pegar bugs que só aparecem no wire:

- Modelo inexistente / defasado / renomeado
- Endpoint 404 (v1 → v2 sem aviso)
- Payload rejeitado (campo obrigatório novo, `temperature` proibido, etc.)
- Header errado ou faltando
- Chave sem escopo pro endpoint alvo
- Rate limit imediato (401/429)

## §2 — Protocolo (aplicar em TODO deploy que fale com API externa)

1. **Antes de declarar "pronto":** rodar 1 chamada de payload mínimo (prompt curtíssimo tipo "ping" ou "1" pra minimizar tokens output).
2. **Verificar 3 coisas:**
   - `.status_code == 200`
   - `.choices[0].message.content` não vazio
   - `.usage.prompt_tokens > 0` (prova que server viu o payload)
3. **Se disponível `GET /models`**: listar modelos ao vivo ANTES de assumir nomenclatura por docs. Docs podem estar defasadas ou nomenclatura pode diferir entre endpoints do mesmo provider.
4. **Registrar no fórum do sprint:** "smoke real executado, custo medido X, resposta OK". Não estimativa — medição.
5. **Backup + rollback trivial** obrigatório (padrão AUTOCURA `feedback_autocura_protocolo_registro_com_solucao_e_rollback`).

## §3 — Caso fundador (28/07/2026 17:50 BRT)

**Contexto:** Miguel autorizou construção da "Memória Total Ponte" pra Modo B da ponte Claude↔Kimi (chamada API autônoma quando bug grave + Miguel ausente + fila crítica). Deployei script `~/ferramentas/sentinela/consulta_kimi_memoria_total.py`.

**Bug P0 meu (silencioso):**
- `MODELO = "kimi-k2-turbo-preview"` — nome bonito, plausível, **NÃO EXISTE em nenhum canal Moonshot** (nem paygo `api.moonshot.ai/v1` nem assinatura `api.kimi.com/coding/v1`).
- Smoke `--status` retornou `{count: 0}` verde → declarei "ok, deployado".

**Efeito se ninguém pegasse:** todas as chamadas Modo B falhariam com "❌ Falha nos 2 canais" pra sempre. Ponte silenciosamente inoperante.

**Kimi K3 Desktop pegou em revisão:**
- Verificou via `GET /models` ao vivo nos 2 endpoints
- Descobriu que **nomes de modelo DIFEREM entre endpoints do mesmo provider Moonshot**:
  - Paygo: `kimi-k3`, `kimi-k2.5/2.6/2.7-code*`
  - Coding: `k3`, `k3-256k`, `kimi-for-coding`, `kimi-for-coding-highspeed`
- Nenhum dos dois tem `kimi-k2-turbo-preview`

**AUTOCURA Kimi (6 edições cirúrgicas + backup SHA-256 + smoke real):**
1. `MODELO_POR_CANAL = {"paygo": "kimi-k3", "assinatura": "k3"}`
2. Ordem invertida: paygo primário (decisão Miguel 17:40), assinatura fallback (blindar Kimi Desktop)
3. `chamar_api()` recebe modelo por parâmetro
4. `ler_chave()` levanta `RuntimeError` em vez de `SystemExit` (não mata script no fallback)
5. Salva modelo real no arquivo da consulta
6. Docstring reescrito com timestamp

Backup SHA-256 pré `17196574...` → pós `2b87d4ea...`.

**Smoke real Kimi executou:** 1ª consulta da ponte funcionou. R$ 0,0192 (2 centavos, **20× mais barato que estimativa**). Kimi identificou-se como K3 e listou as 7 seções da Memória Total.

## §4 — Métrica meta (validação offline vs online)

- Validação offline (compile, lint, `--status`, dry-run): pega ~**30%** dos bugs
- Validação online (1 chamada real): pega ~**90%** dos bugs
- **Diferença de 60% = bugs de contrato com o outro sistema** — exatamente os mais caros de descobrir em produção

## §5 — Casos de aplicação (não exaustivo)

- Deploy novo cliente HTTP/gRPC
- Migração de versão de API (v1 → v2 do provider)
- Mudança de modelo/endpoint em script pré-existente
- Rotação de chave (verificar escopo antes de assumir OK)
- Ferramentas MCP novas antes de anunciar ao usuário
- Qualquer refactor que toque payload de request/response

## §6 — Regras irmãs

- [`feedback_verificar_processo_real_antes_de_confiar_no_cerebro`](../CEREBRO_NODE_BUGS_SOLUCOES.md#verificar-processo-real) — ground truth vem de verificação viva, não de documento (28/07 16:45)
- [`feedback_autocura_protocolo_registro_com_solucao_e_rollback`](../CEREBRO_NODE_BUGS_SOLUCOES.md#autocura) — smoke faz parte do protocolo AUTOCURA obrigatório
- [`feedback_sempre_pesquisar_web_em_duvida`](../CEREBRO_NODE_BUGS_SOLUCOES.md) — verificação de realidade antes de afirmar

## §7 — Recado pros agentes da Trindade

Kimi salvou o Modo B de ser inoperante 100% do tempo. Vale pros outros agentes: **quando um par (Claude/Kimi/Codex/GLM/etc) deploya código novo que fala com API externa, façam a validação online independente** — o autor do código costuma ter viés de confirmação ("meu script tá certo"), o revisor externo com `curl` de 2 centavos pega o que o autor perdeu.

Padrão da Trindade daqui pra frente: **1 chamada real de centavos = obrigatório antes de "declarar pronto"**.

---

Ass: **Claude Code** — 2026-07-28 17:55 BRT
