# Escalação Claude → Kimi K3 · Decisão arquitetural (2026-07-25 10:50 BRT)

**Miguel autorizou 10:49 BRT** ("pode escalar pro kimi k3 fazer a mudança na arquitetura como voce disse") a escalar decisão de arquitetura sobre `youtube_cafezinho.py`. Você é o decisor.

---

## Contexto: bug #31 fechado, mas com camada arquitetural pendente

**Bug #31** (publicação com erro factual em nome próprio de ministro STF): FECHADO em três camadas hoje:

1. **Downstream (09:33 BRT):** 262873 corrigido in-place via `wp_post` — janela de exposição: ~2min.
2. **Upstream Sentinela (10:44 BRT, autorização Miguel):** patch `~/ferramentas/sentinela/config/prompts.md` +29 linhas seção "LEITURA DUPLA". Nova regra "⛔ REGRA INVIOLÁVEL": `propor_correcao_semantica` + `publicar_drafts` no mesmo ciclo para nome próprio de figura pública = PROIBIDO. Backup `prompts.md.bak_pre_claude_bug31_nomeproprio_20260725_1042` SHA-256 `00d092ab...c957b405`.
3. **Camada de origem (esta escalação):** ainda pendente.

## Origem real do erro (cadeia)

| # | Agente/LLM | O que fez |
|---|---|---|
| 1 | YouTube speech-to-text (Google) | Transcreveu "Marques" → "Marcos"/"Max". Fonte do erro. |
| 2 | Kimi K3 (`youtube_cafezinho.py` `analisar()` + `redigir()`, chave `KIMI_PAYGO_API_KEY`) | Recebeu transcrição errada, redigiu post do jeito. NÃO detectou "Nunes Marcos" como nome inexistente. |
| 3 | DeepSeek V4 Pro (Sentinela) | Detectou erro no draft mas escolheu ações erradas. Fix aplicado 10:44. |

A **camada 2 é o ponto de origem** que ainda não tem defesa. Você mesmo (Kimi K3 via `youtube_cafezinho.py` em `/agentes_cafezinho/`) redigiu o post errado antes do Sentinela ver.

## Proposta arquitetural pra você avaliar

Adicionar em `youtube_cafezinho.py` (especificamente na função `redigir()` linha 407 ou como camada intermediária pré-`redigir()`) um **fact-check contra lista de nomes próprios de figuras públicas conhecidas** antes de emitir o draft. Se transcrição tem nome que não bate com lista canônica, gerar alerta ou passar a lista pro prompt e forçar LLM a verificar antes de escrever.

**Formas possíveis:**

- **(a) Lista estática no repo:** JSON com nomes canônicos ("Kassio Nunes Marques", "Alexandre de Moraes", "Lula", "Fernando Haddad", "Flávio Bolsonaro" etc). Regex simples detecta variantes próximas via distância de Levenshtein e propõe correção antes do LLM redigir. **Prós:** determinístico, barato, rápido. **Contras:** lista precisa manutenção contínua, cobre só quem está listado.

- **(b) LLM checa contra sua base de conhecimento:** passa lista de nomes próprios extraídos da transcrição pro Kimi K3 e pede validação em uma chamada separada antes de redigir. Se algum nome parece suspeito (Nunes Marcos, Nunes Max, "Fernando Henrique" no lugar de Haddad, etc), Kimi devolve correção. **Prós:** cobertura ampla, sem manutenção de lista. **Contras:** custo extra (~$0.02/post), risco de falso-positivo (nome real desconhecido pelo LLM).

- **(c) Grounding com Google/DuckDuckGo:** query rápida ("Nunes Marcos ministro STF" retorna 0 hits vs "Nunes Marques ministro STF" retorna milhões). **Prós:** precisão alta, sem depender de LLM ter memorizado. **Contras:** exige API/scraping, latência alta.

- **(d) Combinação (a)+(b):** lista canônica pra top 100 nomes brasileiros de figuras públicas em política/judiciário/esporte + fallback LLM quando nome não está na lista. Custo baixo pra caso comum, cobertura ampla pra edge cases.

- **(e) NADA — aceitar defesa em 2 camadas apenas:** já temos (Sentinela pega + Claude corrige). Adicionar fact-check upstream é over-engineering se a taxa desses erros for baixa.

**Meu voto:** entre (a) e (d). (a) porque nomes propriamente publicáveis do Cafezinho são um universo relativamente pequeno e estável (ministros STF, presidentes, ministros governo Lula, principais governadores, top do agrobusiness, top do capital, líderes internacionais mais citados) — dá pra ter lista de ~200 nomes que cobre 95% dos casos. (d) porque LLM fallback pega o long tail sem manutenção.

**Contra-argumento pra (e):** taxa observada é apenas 1 caso em ~2 meses de operação (bug #31 hoje). Se acontecer 1-2×/mês, defesa em 2 camadas talvez seja suficiente. Custo/benefício de adicionar 3ª camada precisa ser calculado.

## O que preciso de você (Kimi K3)

Avalie e me dê passos concretos:

1. **Vale a pena adicionar 3ª camada agora?** Ou defesa em 2 camadas (Sentinela + Claude patch aplicado) é suficiente pra taxa observada?
2. **Se vale, qual rota?** (a) lista estática, (b) LLM check, (c) grounding, (d) combinação, (e) nada.
3. **Se rota exige patch em `youtube_cafezinho.py`** (NYC), tem 2 caminhos operacionais: você mesmo aplica via SSH (você fechou 3 bugs upstream V4 dia 24/07 desse jeito), OU Claude aplica com você guiando o patch em detalhe.
4. **Estimativa de custo/benefício:** se você concordar com implementar, quanto isso agrega ao custo por post publicado?

Sem urgência crítica — bug #31 já está fechado em 2 camadas. Isso é pra reduzir chance de recorrência do padrão em qualquer post futuro.

## Contexto complementar

Você conhece o `youtube_cafezinho.py` porque redige seus próprios posts (linha 280 do arquivo: `"model": cfg.get("model", "kimi-k3")`). Se aplicar a checagem no ponto onde você já roda como analisador+redator, adiciona camada de auto-verificação — Kimi K3 checa próprio output antes de emitir. Pattern conhecido como "self-correction" ou "guardrail".

---

*— Claude Code (engenheiro-chefe Anthropic claude-opus-4-7), escalação autorizada por Miguel 10:49 BRT*
