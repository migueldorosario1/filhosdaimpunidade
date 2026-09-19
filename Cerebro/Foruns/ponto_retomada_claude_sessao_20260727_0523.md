# Ponto de Retomada — Claude Code / sessão 26-27/07/2026

**Timestamp:** 2026-07-27 05:23 BRT
**Sessão:** continuação da retomada 25/07 22:46 BRT (~30h de trabalho contínuo)
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`), engenheiro-chefe do ecossistema
**Motivo do ponto:** Miguel vai fechar sessão pra abrir nova via wrapper `~/bin/claude` limpo e ativar delegação Sonnet/Haiku (fix PATH aplicado 16:20 BRT ontem, requer nova sessão pra propagar)

---

## 1. Estado operacional agora (05:23 BRT)

- **Loop Sentinela Cafezinho:** rodando via cron + `/loop` manual meu (agendado `92f999c4 = */30`). Último ciclo `20260727_0508` · 🟢 normal (~15min atrás).
- **Loop Temáticos:** cron `24cd4181 = 0 */3` meu + Kimi criou ponte permanente `Cerebro/ponte_kimi/`. Último ciclo `20260727_0313` · 🟢 8/8.
- **Publicações do dia 27/07 até 05h:** 263008 (Lula WaPo — publicado por MIM ciclo 03:38), 263010 (Guia El Niño).
- **Publicações do dia 26/07:** ~20 posts V4, ritmo saudável.
- **Baleia Azul do dia:** já criada.
- **Health:** 10/10 providers OK constante nas últimas 12h.
- **`v4_pipeline_imagem`:** verde 3/3 (caiu de 5/5 desde ~08:11 BRT ontem, vale observar mas não é urgente).
- **Publish 262949 Fachin (bug fundador):** publicado ontem 02:15 BRT (POST CORRETO — Fachin É presidente STF desde 29/09/2025, meu erro confirmar erro).

---

## 2. Sprints estruturais concluídos hoje (26/07)

### 2.1 Bug duplo Fact-check + Brave (Kimi K3 patchou completo)

**Trigger:** post 262949 Fachin. Sentinela+DeepSeek disseram "erro factual" quando Fachin ESTÁ correto. Eu (Claude) reportei erro pro Miguel sem WebSearch antes → Miguel me corrigiu duro.

**Bug A resolvido:** Kimi criou `lib/fact_check_gate.py` + `lib/web_search_client.py` + cache SQLite. Cascata Wikipedia → Brave → SearchAPI (5s timeout). Prompt Sentinela ganhou sub-regra ⚠️ knowledge cutoff. Caso Fachin descartaria automaticamente hoje.

**Bug B refutado:** Codex apontou (§15) que log `agente_rail_post_run.log` era de agente LEGADO 14/07 — não incidente. Kimi validou: `nucleo_tematico/__init__.py` já popula env, Brave nunca esteve desativado no V4. Fix real foi noutro lugar: RSS G1 ceara/gov.br mortos, Kimi trocou por feeds frescos + blindou `busca.py` com `chaves.get_key`.

**Deploy NYC/Tencent** (Kimi 14:26 BRT): "Código sem alvo remoto (V4 temáticos é só local; agentes server-side já usam carregar_chaves)". **Achado bônus:** DRIFT de credencial — NYC+Tencent com chave Brave ANTIGA. Sync AUTOCURA completo.

**SearchAPI voto Kimi §12:** manter como reserva 3ª camada timeout 5s. Brave é primário. Mediana Brave 1.3s vs SearchAPI 4s / p95 26s.

**Fórum:** `Cerebro/Foruns/forum_kimi_webverify_e_brave_desativado_20260726.md` (~17 seções).

### 2.2 Coleta enriquecida (Kimi trabalhando em paralelo)

**Trigger:** DeepSeek gerou FP ciclo 15:09 dizendo "workers V4 parados desde 23/07" quando publicou 5 posts hoje. Miguel: *"o DeepSeek precisa de um básico de saber que o sistema está funcionando"*.

**Escopo:** enriquecer `coletar_estado()` da Sentinela com 4 blocos (publicados_recentes, ritmo_publicacao_6h, ultimo_draft_criado, ultima_exec_worker_v4) + regra no prompt.

**Status:** Kimi acusou recebimento 15:36 BRT, criou ponte permanente `Cerebro/ponte_kimi/`. Manifesto §17 do fórum pendente confirmação de execução.

### 2.3 Ponte Kimi↔Sentinela (Kimi iniciativa própria)

Kimi criou `Cerebro/ponte_kimi/` com LEIA_PRIMEIRO + CONTRATO + ESTADO_ATUAL + HISTORICO. Sistema pra ele receber contexto/coordenar. Pediu Claude assinar contrato §4. Ainda não fiz — pendência.

### 2.4 V4 Geopolítica cartoon órfão (Codex escalou 05:06 BRT hoje)

**Detectado enquanto eu rodava madrugada:** produtor V4 Geopolítica bloqueando por `wordpress_post_content_insufficient_for_cartoon`. Codex abriu fórum `forum_kimi_v4_geopolitica_cartoon_orfao_bloqueio_20260727.md` e delegou pro Kimi via `inbox_trindade/kimi.md`. Nova identidade V4 oficial: `redacao-nova` (ID 5786). Kimi ainda não sinalizou recebimento (só ~15min).

---

## 3. Regras/memórias novas gravadas hoje

Todas em `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/` + indexadas em MEMORY.md:

1. **`feedback_sempre_pesquisar_web_em_duvida.md`** — WebSearch antes de acusar erro factual (regra fundadora bug Fachin)
2. **`feedback_canal_inbox_apenas_ponteiro_carta_no_chat_e_forum.md`** — canal = 1 linha, inbox = ponteiro, carta = chat + fórum
3. **`feedback_nunca_chave_literal_em_forum.md`** — chaves API sempre por `NOME_VAR (BSA***abc em .env)`, nunca literal
4. **`feedback_cartinha_como_md_com_link_no_final.md`** — toda cartinha vira arquivo `.md` em `Cerebro/Foruns/cartinhas/` + link no final da resposta chat
5. **`feedback_diferenciar_llm_desktop_cli_mobile.md`** — Kimi Desktop ≠ Kimi CLI; Claude browser ≠ Claude Code; Antigravity Desktop ≠ AGI CLI
6. **`feedback_reportar_economia_em_real_ao_delegar_sub_agent.md`** — bloco 💰 com cálculo tokens + BRL toda vez que delegar Sonnet/Haiku

---

## 4. Cartinhas materializadas hoje (Cerebro/Foruns/cartinhas/)

- `cartinha_kimi_webverify_brave_20260726_1300.md`
- `cartinha_trindade_webverify_brave_20260726_1312.md`
- `cartinha_trindade_protocolo_comunicacao_20260726_1400.md`
- `cartinha_kimi_coleta_enriquecida_20260726_1525.md`

---

## 5. Fix PATH aplicado (16:20 BRT) — **CRÍTICO PRA PRÓXIMA SESSÃO**

**Problema:** essa sessão está com env vars contaminadas pelo wrapper GLM:
- `ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5-turbo`
- `ANTHROPIC_DEFAULT_HAIKU_MODEL=glm-4.5-air`
- `ANTHROPIC_DEFAULT_OPUS_MODEL=glm-5.2`

Sub-agents Sonnet/Haiku via Agent tool falham porque aliases resolvem pra modelos GLM inexistentes na Anthropic API.

**Fix aplicado:** adicionei `export PATH="$HOME/bin:$PATH"` no FINAL do `~/.bashrc` pra `~/bin/claude` (wrapper limpo com `unset` das env vars GLM) virar padrão.

**Backup:** `~/.bashrc.bak_pre_claude_path_20260726_1620` (SHA `b11613d4...`). Rollback: `cp ~/.bashrc.bak_pre_claude_path_20260726_1620 ~/.bashrc`.

**Nova sessão vai:**
- `which claude` → `/home/migueldorosario/bin/claude` (não mais `.local/bin/claude`)
- Env vars GLM unsetadas
- Sub-agents Sonnet/Haiku vão resolver pros modelos Claude reais
- **Delegação com reporte de economia BRL vai funcionar**

---

## 6. Reminder ativo (Cron durable)

- `89de730d` — durable, dispara **09/08/2026 10:03 BRT** — "fórum grande de segurança" (rotação de todas as chaves, programação de segurança). Miguel adiou rotação das 3 chaves expostas ontem (Brave Web/Answer + SearchAPI) dizendo "essas chaves não valem nada, ninguém tem interesse em roubar, daqui a umas duas semanas fazer um grande fórum sobre segurança".

---

## 7. Pendências

### 7.1 Pra Claude (próxima sessão)

- **Assinar contrato §4 da ponte Kimi** em `Cerebro/ponte_kimi/CONTRATO.md`
- **Confirmar manifesto §17 Kimi** (coleta enriquecida) quando ele publicar
- **Ativar delegação Sonnet/Haiku** na primeira oportunidade (após confirmar `which claude`)
- **Continuar monitorando bug V4 Geopolítica cartoon órfão** — Codex escalou pro Kimi, aguardar manifesto

### 7.2 Pra Miguel

- Fechar sessão atual + abrir nova via `claude` (wrapper limpo)
- Confirmar `which claude` retorna `~/bin/claude`
- Sprint segurança 09/08/2026 (rotação chaves + programação)

### 7.3 Herdadas de dias anteriores (ainda pendentes)

- Baleia Azul email delivery — precisa App Password Gmail
- Ubuntu upgrade final de semana pra HiveTerm
- Script `relatorio_semanal_bugs.py` sexta 23:00 BRT
- Score policy home/no-home entregando 60-90% HOME em vez de ~20% (Codex investigar `decide_no_home()`)

---

## 8. Regras editoriais em vigor (relembrar)

Além das antigas ainda válidas (cap 2h, CHURN, R1 rate limit, D0-D4, SEMANT, governos esquerda, SEO Pruning autorização, título autonomia, charges sem texto dentro, estagiário Agência Brasil, ciclo temáticos 3h manual, protocolo memória bugs 3 camadas):

- **Fact-check gate ativo desde 26/07 13:33 BRT** — Wikipedia → Brave → SearchAPI cascata + cache 24h antes de gravar proposta_correcao_semantica
- **⚠️ Knowledge cutoff LLM juiz** — sub-regra no `prompts.md` desde 26/07 (Kimi patch)
- **Nova identidade V4 Cafezinho:** `redacao-nova` (ID 5786) desde 27/07 05:06 BRT (Codex + Miguel)

---

## 9. Continuidade

Próxima sessão Claude Code deve:

1. Ler `MEMORY.md` (índice; primeiras 30 linhas trazem regras novas de hoje)
2. Ler este ponto de retomada
3. Verificar `which claude` = `~/bin/claude` (crítico pro fluxo Sonnet/Haiku)
4. Verificar estado atual: `tail -3 ~/ferramentas/sentinela/logs/ciclos.jsonl`
5. Assinar contrato §4 da ponte Kimi
6. Continuar rotina `/loop` (Sentinela + Temáticos)
7. Se Miguel pedir "ciclo sentinela" ou similar → delegar Sonnet e reportar economia BRL

---

## Assinatura

Ponto de retomada gravado por Claude Code (Anthropic, `claude-opus-4-7`), engenheiro-chefe do ecossistema, 2026-07-27 05:23 BRT.

Sessão longa e produtiva — muita mudança estrutural, muita regra nova, muito trabalho Kimi paralelo. Próxima sessão pega tudo isso assentado + delegação Sonnet/Haiku funcional pela primeira vez.
