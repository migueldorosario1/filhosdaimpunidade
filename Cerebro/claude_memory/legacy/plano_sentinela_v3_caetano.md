---
name: Plano Sentinela V3 com bot Caetano+Chico (a implementar)
description: Arquitetura human-in-the-loop aprovada 2026-04-18 02h. Sentinela detecta mas não rebaixa; Caetano bot entrega trecho+botões pro Miguel decidir.
type: project
originSessionId: 45d53b87-5aea-4ee1-bde2-cc8f6a6aec6e
---
Plano fechado em 2026-04-18 02h após falha do Sentinela V2 (rebaixou 7 posts bons em 20s com falsos-positivos de `gpt-5-search-api`).

**Why:** filosofia do Cafezinho é PUBLICAR, não guilhotinar. Ver memória `feedback_publicar_os_melhores.md`. Sentinela automático é perigoso. Human-in-the-loop resolve.

**How to apply (amanhã 18/04 quando Miguel estiver acordado):**

1. **Sentinela reescrito** (`/root/agente_observador.py`):
   - Lê últimos 10 posts `publish`
   - Auditor: `claude-sonnet-4-6` (NÃO usar gpt-5-search-api — alucina fact-check; NÃO usar Perplexity — já é chamado no pipeline de publicação)
   - Procura só lixo textual: metalinguagem (`As an AI`, `TÍTULO:`, ```json``, `Aqui está`), HTML quebrado, parágrafos vazios, citações cruas `([domain](url))`.
   - **NUNCA** chama `requests.post({status: draft})` — só escreve em `/root/agent_data/suspeitos_caetano.json`.
   - Manda Telegram pro `@caetanoechicobot` (token `8530517301:AAHJYsZlNJp5ZG7STNMWlnmnshdG4r730so`, chat_id do Miguel = `1894890759`) com:
     - post_id + título
     - **trecho literal do problema** (máx 400 chars, copy-paste do HTML)
     - diagnóstico estruturado (categoria + parágrafo)
     - link do editor WP
     - **7 botões inline**:
       - `📝 Curar com IA` → chama `agente_corretor_autonomo.curar_post_unico(pid)` (higieniza preservando palavras)
       - `📱 Editar rápido` → bot envia HTML atual em mensagem; Miguel responde (reply) com texto corrigido; bot salva via WP API
       - `💻 Abrir no WP` → link clicável pro editor de `controle.ocafezinho.com/wp-admin/post.php?post=<pid>&action=edit`
       - `📥 Rebaixar` → `requests.post({status: draft})`
       - `🗑️ Deletar` → `requests.delete(post)`
       - `✅ Manter` → adiciona `pid` a `/root/agent_data/ignorados_sentinela.json`, nunca mais alerta
       - `🔍 2ª Opinião` → chama roteador com contexto `auditor_segunda_opiniao` (fila Perplexity→GPT-search→Grok→Gemini→Claude). Após retorno, bot reposta o mesmo menu SEM o botão `2ª Opinião` (pra não girar em loop).

**Fluxo em 3 estágios após primeira cura:**

Estágio 1 (alerta inicial) — menu completo 7 botões acima.

Estágio 2 (após curar por IA ou manual, `cura_attempts=1`):
- Bot manda: "✅ Post corrigido e republicado! 📄 [link da matéria]" + novo menu:
  - `✅ Aprovado!` → remove do `posts_para_conserto.json` + adiciona ao `ignorados_sentinela.json`
  - `📥 Rebaixar a draft`
  - `📱 Editar rápido`
  - `🔄 Curar com outra IA` → chama roteador passando `excluir_modelo=<modelo_usado_antes>` pra FORÇAR LLM diferente. Incrementa `cura_attempts`.

Estágio 3 (após segunda tentativa de cura, `cura_attempts>=2`):
- Bot manda: "✅ Post re-corrigido! 📄 [link]" + menu reduzido:
  - `✅ Aprovado`
  - `📥 Rebaixar`
  - `💻 Abrir no WP`
- Bot NÃO oferece mais cura automática. Miguel decide definitivo.

**Controle de estado** em `/root/agent_data/posts_para_conserto.json`:
- campo novo `cura_attempts: int`
- campo novo `modelos_usados: list[str]` (pra passar ao roteador como exclusão)
- quando `cura_attempts >= 2` → próxima vez nasce em Estágio 3.

2. **Bot Caetano** (achar script: `grep -rl caetanoechicobot /root/*.py`):
   - Adicionar handlers dos 4 callbacks
   - `Curar` → chama `agente_corretor_autonomo.curar_post_unico(post_id)` (função a extrair do run_correcao_autonoma)
   - `Rebaixar` → `requests.post({status: draft})`
   - `Deletar` → `requests.delete(post)`
   - `Manter` → adiciona post_id ao `ignorados_sentinela.json` pra não alertar mais

3. **Corretor refatorado** (`/root/agente_corretor_autonomo.py`):
   - Expor `curar_post_unico(pid, motivo)` chamável sob demanda
   - Modo higienizar preservando 100% das palavras (já existe no código V2, linha 178-196)
   - REMOVER run automático em loop

4. **Crontab**:
   - Sentinela: `*/30 * * * * cd /root && /usr/bin/python3 agente_observador.py ...`
   - Corretor: **remover** do cron (só chamado sob comando do bot)

5. **Testar com 1 post falso** (criar rascunho com "As an AI, I cannot" propositalmente, rodar Sentinela, verificar Telegram, clicar botão, conferir ação).

**Cadência aprovada:** 30min, últimos 10 posts.
**Auditor aprovado:** Claude Sonnet 4.6 com **FALLBACK COMPLETO** via roteador LLM. Duas filas novas a criar em `agente_roteador_llm.py`:

- `auditor_sentinela` (1ª passada, SEM web): Claude Sonnet → GPT-4o → Grok 4.20 → Gemini 2.5 Flash → Mistral Large. Usa só análise textual (padrões de lixo de IA, HTML quebrado, metalinguagem).
- `auditor_segunda_opiniao` (2ª passada SOB DEMANDA, COM web): Perplexity sonar-reasoning-pro → gpt-5-search-api → Grok 4.20 → Gemini 2.5 Pro → Claude Sonnet. Chamada só quando Miguel clica botão "2ª Opinião" no Telegram.
**Bot escolhido:** @caetanoechicobot.

**Estado atual (para retomar amanhã):**
- Sentinela V2 (over-skeptic): DESATIVADO no crontab (linha com prefixo `# DESATIVADO V2 over-skeptical`)
- 7 posts que V2 rebaixou: já restaurados a `publish`
- `posts_para_conserto.json` tem entradas spurious de 01:51 — revisar e limpar amanhã
- Corretor V2 deployado mas não rodará (sem Sentinela alimentando fila)
- Backups `.bak_v1` preservados pro rollback se preciso
