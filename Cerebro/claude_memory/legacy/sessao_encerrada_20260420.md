---
name: Sessão 2026-04-20 — encerrada com pausa, retomar depois
description: Resumo completo da sessão de segunda-feira 20/04. Cross-linking LIVE, temáticos premium prontos mas dormentes no crontab, Sprints 3+4 da Autocura codados local, 4 bugs de publicação corrigidos, MundoTrilhos verificado no GSC.
type: project
originSessionId: c4ce2046-925d-4cef-9df8-6970e904a43e
---
**Pausa ~14:30 BRT em 2026-04-20 (segunda-feira). Miguel vai desligar o PC.**

## Entrou em PRODUÇÃO hoje

### Cross-linking interno (Tarefa Domingo 1)
- `interlink_interno.py` → bloco "Leia também" ao final do corpo
- Plugado em `motor_publicador.py` (Trindade completa) + `agente_historiador.py`
- `INTERLINK_DRY_RUN=0` global no topo do crontab — cobre todos os chamadores
- Já apareceu nos posts reais da Trindade (evidência no log 03:42-04:12 UTC)

### Ferroviário v2 — patches operacionais
- Fix https: `/root/.env` tinha `MUNDO_TRILHOS_WP_SITE=http://` → redirect 301 convertia POST em GET → WP devolvia lista de posts antigos → `wp_id=12` sempre. Corrigido `.env` + default do código.
- Fix Google Indexing 403: criada whitelist em `util_indexing.py` (NOVO módulo). `INDEXING_ALLOWED_DOMAINS = ("ocafezinho.com",)` — MundoTrilhos pula silenciosamente.
- Fix imagem cross-post: fallback chain `FEATURED_IMAGE_ID_CAFEZINHO` → `FEATURED_IMAGE_ID` → 227448 (default). Cafezinho nunca fica sem imagem destacada.
- Fix comentarista: trigger subprocess no cross-post (igual motor_publicador).

### Sprint 2 da Proposta B (Autocura — Loop de Aprendizado)
- `autocura_licoes.py` + `agente_correcao.py` deployados
- Hook `rb:<post_id>` no Caetano bot: Miguel clicar `📥 Rebaixar` → `condensar_motivo_para_principio()` via Mistral → `adicionar_licao(origem="miguel_escalacao")`
- Backups `.bak_pre_sprint2_20260420_0937` preservados
- Caetano restartado via `setsid` (truque do `sudo bash -c` com `nohup &` não pegava)
- **Aguardando 1º clique humano real em produção pra validar**

### Fixes de bugs de publicação
- **Fantástico parser:** gpt-4o-mini colava avaliações numa linha só → parser perdia 100% PUBLICAR silencioso. Agora regex robusta via `(?=NOTA:\s*\d)`. Prompt também reforçado.
- **Analytics loop:** artigo "Grandes Lagos" monopolizava escolha. Criada blacklist `analytics_tentativas_falhadas.json` (3 falhas → bloqueio 24h). Artigo seedado bloqueado.
- **Repetidor estatal:** mesmo bug parse-linha-única do Fantástico. Fix idêntico aplicado.
- **Agente Crime:** abortava 100% com "matéria curta". Google News RSS dá link intermediário que não extrai texto via JS. Agora tenta 5 candidatos + RSS summary como fallback.

## LOCAL (não deployado ainda)

### Sprint 3 da Proposta B — RLHF Reverso
Callbacks `v4rev` e `v4rep` do Caetano bot agora usam `inverter_licao_por_post(pid)` em vez de `remover_licao_por_post(pid)`. Função já existia no Sprint 1, carimba `origem="miguel_rlhf_reverso"` + vira polaridade `tolerar` com prefixo "⚠️ ORDEM DO CEO".

**Deploy só depois de 1 validação real do Sprint 2.**

### Sprint 4 da Proposta B — Quórum de Consistência
Módulo novo `autocura_quarentena.py` (~280 linhas). API:
- `registrar_em_quarentena(principio, origem, post_id, motivo_original)`
- `promover_se_quorum(principio, tipo)` — chama `adicionar_licao(evento_historico="quorum_2x")` se count ≥ 2 E todos dentro janela 7 dias
- `decair_quarentena()`, `registrar_e_promover()`, `estado_atual()`

Parâmetros fixos validados no fórum Seção 10: `QUARENTENA_JANELA_DIAS=7`, `JACCARD_LIMITE_PROMOCAO=0.7`, `QUORUM_MIN=2`. Hash do princípio é SHA-256[:16] **normalizado** (Antigravity aprovou Seção 15).

10/10 testes unitários em `/tmp/test_autocura_quarentena.py`.

**Gatilhos NÃO integrados ainda** em `agente_autocura_v4.py` (decisão deliberada — aguarda Sprint 2 amadurecer em produção conforme parecer do Antigravity).

### Temáticos Premium (Caminho C do forumtematicos.md)
Pipeline **equivalente ao motor_publicador**. Refatorações:
- `publicador_tematicos.py` ganhou `publicar_wp_premium()` com cascata completa:
  1. Sanitizador pré-publicação
  2. Imagem cascata (og:image → banco SQLite + Tribunal Visual → Flux/Ideogram/DALL-E → FEATURED_IMAGE_ID fallback)
  3. Atribuição "Com informações de [Fonte]" (só se LLM não citou inline)
  4. Cross-link "Leia também" via `interlink_interno`
  5. Newsletter `CAIXA_NEWSLETTER_AJAX` do motor_publicador
  6. Comentarista bot (subprocess, só em publish)
  7. `util_indexing.disparar_indexacao`
- `factcheck_cascata`: Perplexity fail-open → se reprovar, apela pra Claude via `auditar_com_claude` do motor_publicador
- `primeira_fonte_do_bruto(texto)`: extrai URL da fonte principal do material coletado
- Prompt V9 reforçado: regra 1 de tamanho agora é **proporcional ao material primário** (alinhado com Trindade, sem limite numérico); regra 3b manda LLM encaixar link HTML casual no lide ("conforme apurou o X") — só cai no rodapé "Com informações de" se LLM não usar.
- `agente_matriz_energetica.py` (NOVO — fusão petróleo+energias): foco rotativo via env `MATRIZ_FOCO=FOSSIL|TRANSICAO`
- `agente_petroleo.py` + `agente_energias.py` → DORMENTES (não deletados, rollback disponível)
- `agente_ia.py`, `agente_mercado.py`, `agente_inflacao.py` → chamam `publicar_wp_premium`
- **Fail-fast yfinance/SIDRA**: mercado aborta sem rascunho se Ibovespa+dólar vazios; inflação aborta se SIDRA não trouxer ≥ 2 períodos
- **Crontab dos 4 temáticos NÃO reativado.** Dormente até Miguel autorizar staging 48h.

## Validações manuais de teste (drafts pra Miguel apagar no painel)

- `237194` — Crime (teste do extractor com fallback RSS summary)
- `237233` — Matriz Energética primeiro teste (sem og:image ainda)
- `237243` — Matriz Energética teste do premium (sem url_fonte ainda; imagem Flux gerada)
- `237249` — Matriz Energética FINAL com pipeline completo (og:image da OilPrice + atribuição + cross-link). **Mais bem-acabado.**

Sandbox bloqueou DELETE via API em todos. Miguel apaga via `/wp-admin/edit.php?post_status=draft`.

## Documentos atualizados nesta sessão

- `Projeto Cafezinho Agentes/tarefasdomingo3.md` — Sprint 1+2 deployados, Sprints 3+4 local, rollback commands.
- `Projeto Cafezinho Agentes/forumtematicos.md` — diagnóstico + 7 perguntas + parecer Antigravity (Seção 5) + plano execução (Seção 6).
- `Projeto Cafezinho Agentes/FORUM_AUTOCURA.md` — Seções 9-15: parecer do Opus → Antigravity validou os 4 parâmetros do Quórum → Sprints 3+4 codados local.

## MundoTrilhos — Google Search Console

Miguel verificou o domínio via Code Snippets + meta tag Google (código `a6Xmw_LcM6fPhjhXteYJqiFsZatOOivSvfmaSz8A_aU`). Próximo passo: adicionar service account `indexing-cafezinho@gen-lang-client-0200069757.iam.gserviceaccount.com` (chave em `/root/agent_data/indexing_key.json`, project `gen-lang-client-0200069757`) como **Owner** no GSC do mundotrilhos.com → incluir `"mundotrilhos.com"` na tupla `INDEXING_ALLOWED_DOMAINS` do `util_indexing.py`. **Atenção:** o SA é `indexing-cafezinho`, NÃO o `agente-ga4` (esse último é só pro GA4 Analytics). Confirmado 2026-04-20 via `urlNotifications.publish` probe: ocafezinho.com retorna OK; mundotrilhos.com retorna HTTP 403 "Failed to verify the URL ownership".

## Pendências reais pra próxima sessão

### Atualização 2026-04-20 (pós-sessão, via diagnóstico direto no servidor)
- ✅ Sprint 2 validado (2 lições via clique Miguel) — ver `deploy_sprint3_autocura_20260420.md`
- ✅ Sprint 3 deployado ~16:46 BRT — hook `v4rev/v4rep` agora usa `inverter_licao_por_post`
- ✅ Draft `237249` apagado no WP (404)
- ✅ Draft `237236` (Pezeshkian) REPUBLICADO (status=publish) — decisão tomada
- ❌ Drafts `237194` / `237233` / `237243` seguem como draft no WP
- ❌ Sprint 4 (`autocura_quarentena.py`) NÃO presente em `/root/` — segue só local
- ❌ Crontab temáticos premium DORMENTE (sem `agente_ia/mercado/inflacao/matriz_energetica`)
- ❌ `sync_nyc.sh` existe em `/root/` (mtime 18/04 21:01) mas SEM cron `*/5` — Etapa 3 pendente
- ❌ MundoTrilhos em `INDEXING_ALLOWED_DOMAINS` ainda comentado (linha 20 de `util_indexing.py`)
- ❌ `gerador_imagem_editorial.py` mtime 17/04 — bug `list indices` não fixado
- ❌ Sentinela V3/V4 Autocura só auditam Cafezinho — MundoTrilhos sem auditoria automatizada

## Primeiro comando ao retomar

```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 "
  sudo tail -20 /root/agent_data/agente_correcao_bot.log | grep -i 'CALLBACK rb'
"
```

Se encontrar linha `[CALLBACK rb] lição gravada pid=... origem=miguel_escalacao:` — Sprint 2 validou! Pode deployar Sprint 3.
Se não encontrar — V3 não pegou nada relevante ou Miguel ainda não clicou. Aguardar mais.
