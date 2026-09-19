---
name: Pendências de bugs descobertas durante força-tarefa 01/05
description: 3 bugs separados (não relacionados aos Bugs A/B/C) descobertos durante diagnóstico hoje. Cada um ataca 1 agente premium e mata o slot diário.
type: project
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
Durante a sprint força-tarefa Bugs Import (2026-05-01), descobri 3 bugs separados que estão matando temáticos premium. **Nenhum foi corrigido nesta sprint** — registrar pra atacar em sprints futuras.

## 1. `BRAPI_TOKEN` ausente no `.env.unificado` (mata agente_mercado)

**Sintoma:** `agente_mercado` cron 15:30 BRT aborta com `❌ FAIL-FAST: faltou Ibovespa ou Dólar (ibov=False, dolar=True)`.

**Causa:** chave `BRAPI_TOKEN` faltando em `/root/.env.unificado` (Tencent).

**Why:** desde quando? Não sei. Provavelmente já estava assim há dias/semanas. Cobre Cat 43 (Economia) — perde 1 post/dia.

**How to fix:** adicionar `BRAPI_TOKEN=<token>` em `/root/.env.unificado`. Token obtém-se em https://brapi.dev (free tier dá 100 req/dia, suficiente).

## 2. `master_lula` pauta vetada por anacronismo

**Sintoma:** `agente_master_lula` cron 09:30 BRT aborta após 3 tentativas. Perplexity veta com "ERRO GRAVE: Evento que NÃO ACONTECEU (Lula em grande reunião de governos progressivos em Barcelona em abril 2026)".

**Causa:** o coletor (`robo_coleta_lula.py`) está coletando pautas inexistentes / com data futura. Em 2026-05-01, pegou matéria do "Svensk-Kubanska Föreningen" sobre Lula em Barcelona com data de coleta `2026-04-23` mas evento não aconteceu.

**Why:** filtragem do coletor está deixando passar pautas alucinadas. Pode estar afetando outros temáticos premium também (precisa investigar).

**How to fix:** investigar `robo_coleta_lula.py` — filtros de data/coerência factual no momento da coleta. Aumentar nota de corte na fase pré-LLM.

## 3. Temáticos premium SEM retry quando abortam

**Sintoma:** quando `agente_master_lula` (09:30), `agente_latam` (11:30), `agente_sheinbaum` (13:30), `agente_mercado` (15:30), `agente_matriz_energetica` (17:00) abortam por qualquer razão, **perdem o slot do dia inteiro**. Sem retry automático.

**Causa:** cron padrão dispara 1x. Sem retry script.

**Why:** em 2026-05-01, 4/5 temáticos premium abortaram (latam+sheinbaum por Bug A, lula por anacronismo, mercado por BRAPI). Só matriz_energetica publicou. Cat 22 (Política), Cat 5003 (Geopolítica via temáticos), Cat 43 (Economia via mercado) ficaram sem post premium do dia.

**How to fix:**
- Adicionar wrapper retry no cron: `agente_X.py || sleep 1800 && agente_X.py` (retry 30min depois).
- Ou: agente registra status em `/root/agent_data/<nome>_lock.json` e cron executa via wrapper que detecta aborto e reagenda.
- Ou: separar coleta (que pode ter pauta ruim) de publicação — quando coleta retornar vazia, agente NÃO marca slot consumido.

## Como retomar

Próxima sessão Claude pode atacar 1 destes em sprint dedicada. Ordem sugerida (impacto vs esforço):
1. **#1 BRAPI_TOKEN** — fix de 1 linha no .env, ressuscita Cat 43 hoje mesmo.
2. **#3 Retry mechanism** — fix arquitetural, salva ~3-5 posts/dia em janelas onde 1 agente aborta.
3. **#2 master_lula filtro de coleta** — investigação maior, mas evita propagação de alucinação editorial.

---

## ✅ Pendência #1 (China parser) RESOLVIDA 2026-05-02 11:32 BRT

### Fixes deployados em `/root/agente_china.py` (MD5 `a62a761d429113f34f329f01d14e45d8`)

#### Bug 1 — Fallback inseguro de auditoria LLM (CRÍTICO, linha 538-541 → 537-541)
Quando `chamada_llm_segura` retornava None (toda cadeia LLM caída), o código aprovava cegamente o top score local. **Bypassava a REGRA POLÍTICA INVIOLÁVEL.** Em 09:00 BRT 2026-05-02 isso aprovou pauta sobre Suu Kyi/Myanmar (anti-regime). 
**Fix Opção A (fail closed)** decidido por Antigravity: log + `return []`. Filtro keyword local não pega nuance geopolítica, melhor abortar.

#### Bug 2 — `UnboundLocalError: html` (CRÍTICO, linha 721)
`publicar_wordpress` referenciava variáveis `html` e `media_id` que nunca existiram. Os parâmetros corretos eram `texto_html` e `featured_media`. Bug existia há tempos — só explodia quando o agente chegava na publicação (cota china = 0/5 últimos dias).
**Fix:** `html = injetar_figcaption_do_media(texto_html, featured_media) if featured_media else texto_html` + `payload["content"] = html`.

#### Bug 3 — Filtro de texto silencia rejeições (linhas 836-857)
`REJEITADO_VAZIO` (texto < 400 chars) era silencioso (só status no DB). Mensagem "Nenhum candidato sobreviveu" não dizia POR QUÊ.
**Fix:** log `📭 Texto vazio/curto` + contadores `descartados_vazio`/`descartados_veto` + breakdown na mensagem final.

#### Bug 4 — `except (ValueError, IndexError): continue` (linha 560-561)
Linhas LLM fora do padrão `[N] NOTA: X | VEREDITO: Y` eram silenciosamente ignoradas.
**Fix:** log `⚠️ Linha auditoria malformada (ignorada): ...`.

### Lições críticas pra futuras sprints
1. **Variáveis fantasma em funções nunca executadas** podem ficar dormentes anos. `agente_china.py` falhava antes de chegar na linha 721 (Bug 1 derrubava por outras vias). py_compile não pega `UnboundLocalError`.
2. **"Garantir continuidade" pode anular missão editorial.** Quando o agente tem regra inviolável (REGRA POLÍTICA), fallback "sempre publica algo" é pior que abortar. **Fail closed > fail loud > fail silent.**
3. **Filtro keyword determinístico não pega nuance.** Suu Kyi/Myanmar não tem palavras-veto óbvias (Hong Kong/Tiananmen/Xinjiang). LLM é necessário pra captar tom crítico geral. Sem LLM = sem auditoria = não publica.
4. **`except` sem log mascara bugs que só aparecem em produção.** Mesmo numa "guarda defensiva", **sempre logar** a exceção pra forensics.

### Backup pra rollback
`/root/agente_china.py.bkp_pre_4bugs_20260502_1131`

---

## ✅ Pendência #3 (BRAPI_TOKEN) RESOLVIDA 2026-05-02 11:38 BRT

### Procedimento
1. Antigravity recuperou token (`ms3yBBAnfXDpUqheGFoaay`) de `relatorio_monitoramento_24h_20260422.md:1173`.
2. Claude Code (líder técnico, infra é minha) executou:
   - Curl prévio brapi.dev → token válido, IBOV R$ 187.317,64.
   - Backup `/root/.env.unificado.bkp_pre_brapi_20260502_1135` (MD5 `49e4196250d9a2a2e67017039a44220b`).
   - `tee -a` (append, jamais overwrite) com newline pré-emptive.
   - 145 → 147 linhas; MD5 novo `efa99cd8adf6795edb7b17632d8fb951`.
   - Teste real: `import carregar_chaves` + `os.environ.get("BRAPI_TOKEN")` → "ms3yBBAn..." len=22, API 200, IBOV 187317.64 ✓.

### Lição crítica
- **NUNCA `open(w)`/HEREDOC/Edit no `.env.unificado`** — só `tee -a` ou `sed -i` com sudo via SSH. Precedente: 21/04 02:36 Antigravity destruiu `/root/.env`, Cafezinho parou 1h17min.
- **Sempre validar token contra a API ANTES do write.** Token vazado em arquivo .md pode estar revogado/rotacionado. Curl simples = 5 segundos, descarta hipótese de nada feito por nada.
- **Sempre backup com MD5 antes do write.** Rollback em 1 comando: `sudo cp <backup> /root/.env.unificado`.

### Validação pendente (apenas confirmação)
- 15:30 BRT cron `agente_mercado` → primeira publicação Cat 43 (Economia) restaurada.

---

## ✅ Achado importante 2026-05-02 11:55 BRT — `agente_energias.py` e `agente_petroleo.py` são órfãos pós-fusão

### Histórico
Em **2026-04-20 (forumtematicos.md Q7 Antigravity)** os agentes `agente_petroleo.py` + `agente_energias.py` foram **fundidos** num único `agente_matriz_energetica.py` que alterna FOSSIL (dias ímpares) / TRANSICAO (dias pares) às 17:00 BRT.

### Lição pra futuras sessões
- ❌ **NÃO restaurar** cron de `agente_energias.py` ou `agente_petroleo.py` — eles são órfãos legacy.
- ✅ **A cobertura está ATIVA** via `agente_matriz_energetica` cron `0 17 1-31/2 * *` + `0 17 2-30/2 * *`.
- ✅ Se o objetivo for aumentar cobertura energética: discutir com Antigravity sobre cadência do agente_matriz, NÃO ressuscitar os agentes velhos.

### Ação pendente
Mover os 2 .py órfãos pra `/root/legacy/agentes_fundidos_20260502/` na próxima sprint de cleanup.

---

## 🔴 Problemas reais descobertos no diagnóstico amplo 2026-05-02 11:55 BRT

### Problema 1 — `master_trends` parado 7.5 dias
- Último publish: 2026-04-24 23:32 BRT ID 239483
- `robo_coleta_trends.py` cron `33 * * * *` continua rodando
- `master_trends.py` SEM cron próprio + `maestro_editorial.py` só despacha geopolitica/nacional no log
- Pipeline quebrou entre coleta e publicação em 24/04

### Problema 2 — `agente_pet_run` parado 48h
- Último publish: 2026-04-30 11:00 BRT ID 241481 (crueldade em mage)
- Investigar se cron sumiu, bug ou desligamento intencional

### Problema 3 — Volume editorial -54% vs semana passada
- 24h: 46 posts (vs 100 mesma janela 7d atrás)
- Pico 11h BRT (5 posts), espalhamento OK mas volume baixo
- Hipótese: efeito combinado dos 3 bugs fixados hoje + master_trends parado

---

## ✅ Sprint Tarefa B (master_trends starvation) FECHADA 2026-05-02 13:40 BRT

### Causa raiz documentada
Master_trends parou em 24/04 23:32 BRT — MESMO DIA da redução do maestro 6/h → 2/h. Fórmula `escolher_editoria` (motor_publicador) tem `SLOTS_POR_HORA=6` hardcoded mas o cron só executa 2 slots/h. Resultado matemático: slots 1+2 sempre vão pra geo+nac (cotas maiores), trends precisaria do slot 4 que nunca chega. Trends foi vítima colateral da otimização de custo por 7.5 dias.

### Solução aplicada (Opção A — cron dedicado)
- Crontab Tencent: `35 0,6,12,18 * * * cd /root && source chaves.sh && /root/venv/bin/python3 agente_master_trends.py >> /root/agent_data/master_trends.log 2>&1`
- 4x/dia: 00:35, 06:35, 12:35, 18:35 BRT
- Backup pré-deploy: `/root/crontab_backup_pre_trends_dedicado_20260502_1338.txt`

### Trindade unânime
- Antigravity: aprovou editorial (4x/dia equilibra capilaridade viral × custo). Confirmou contexto histórico forum_custos_qualidade §B2 já decidira cron dedicado.
- Codex: aprovou técnico (locks fcntl independentes, sem race condition).
- Miguel: aval explícito 13:38 BRT.

### Pendência colateral resolvida
Detectei desencaixe entre espelho local `crontab_server.txt` e Tencent (3 mudanças minhas de hoje não propagadas: maestro 8,38, robo_coleta_nacional 18, agente_china 0 *). Sincronizei o espelho local com o estado real.

### Lição arquitetural
Quando reduzimos cadência do maestro futuramente, ajustar `SLOTS_POR_HORA` ou `escolher_editoria` proporcionalmente, ou adicionar exceção pra editoria não-publicada há X horas. Caso contrário, qualquer editoria com cota baixa pode entrar em starvation determinística.

### Validação pendente
18:35 BRT (em ~5h) — primeira execução real do cron dedicado. Esperado master_trends.log com novo ID > 241000.

---

## ✅ Pendência C (agente_pet_run) RESOLVIDA — falso alarme 2026-05-02 13:46 BRT

### Verdade descoberta
O `agente_pet_v1.py` foi **DESATIVADO DELIBERADAMENTE por Miguel em 2026-04-30** (decisão §10 forum_diagnostico_agentes.md, motivo: "FANTASMA — sem audiência").

Linha do cron está comentada:
```
# Agente Pet (1x ao dia às 11h)
# [DESATIVADO 2026-04-30] FANTASMA — sem audiência (decisão Miguel §10 forum_diagnostico_agentes.md)
# 0 11 * * * cd /root && /root/venv/bin/python3 agente_pet_v1.py >> /root/agent_data/agente_pet_run.log 2>&1
```

### Lição (terceiro caso do mesmo padrão hoje)
Logs estagnados há vários dias podem indicar **desativação intencional**, não bug. Antes de propor ressuscitar, sempre conferir comentários no cron + forums antigos. Casos similares hoje:
1. `agente_energias.py` + `agente_petroleo.py` — fundidos em `agente_matriz_energetica` (Antigravity Q7 forumtematicos.md 20/04)
2. `agente_tiktok.py` — SUSPENSO "a pedido do CEO"
3. `agente_pet_v1.py` — DESATIVADO 30/04 (decisão Miguel forum_diagnostico_agentes.md §10)

Diagnóstico amplo deve sempre incluir busca por `# DESATIVADO`, `# SUSPENSO`, `# FANTASMA` no crontab + forum_diagnostico_agentes.md antes de tratar inatividade como bug.

---

## ✅ Pendência D (volume -72%) DIAGNOSTICADA + Etapa 3 ativada 2026-05-02 14:20 BRT

### Causa-raiz consolidada (Trindade unânime)
1. **Maestro reduzido 24/04** (6/h → 2/h, decisão de custo) = -96 posts/dia teóricos
2. **master_trends starvation 7.5 dias** (causa: matemática do escolher_editoria — ver `forum_master_trends_starvation_20260502.md`) — ✅ fixado hoje 13:40
3. **Bugs Lula+China+BRAPI** matando agentes na manhã de hoje — ✅ fixes da manhã
4. **Inércia de drafts** que sustentavam 150-195/dia esgotou em 30/04→01/05

### Cat 1271 (Esporte) zerada
**NÃO existe `agente_esporte.py`.** Cobertura dependia de:
- Master Trends (paralisado 7.5d) ← fix Sprint B
- Classificação genérica do maestro ← capado 67%

Por isso zerou: perdeu ambas as vias de entrada simultaneamente.

### Plano Etapa 3 (Antigravity+Codex unânime)
- ⏰ Aguardar 24h pra mensurar recuperação pós-fixes
- ❌ NÃO escalar maestro 6/h de volta (decisão de custo mantida)
- ⚠️ Considerar criar `agente_esporte.py` SE 24h depois ainda baixo

### Lição arquitetural
Diretriz "Aumento Agressivo de Volume" de 30/04 (forum_diagnostico_agentes.md §11) escalou agentes secundários (China, Fantástico, Turismo +11 posts/dia) MAS não reverteu redução do maestro 24/04. Combinação assimétrica resultou em queda mascarada por inércia de drafts. Próxima decisão de "agressividade" deve verificar TODA cadeia (incluindo maestro + cotas GA4).

---

## ✅ Maestro restaurado pra 6/h 2026-05-02 14:40 BRT

### Decisão Miguel (autorizada após confirmar material)
Aumentar maestro de 2x/h → 6x/h (reverter integralmente a redução de 24/04). Custo LLM 3x mas volume editorial recupera.

### Mudança no crontab Tencent
- `8,38 * * * *` → `8,18,28,38,48,58 * * * *`
- Backup: `/root/crontab_backup_pre_maestro_6h_20260502_1439.txt`
- Total 244 linhas, sentinelas íntegros

### Material em estoque confirmado pré-deploy
- Geopolítica: 3.090 não processados
- Nacional: 5.675 não processados
- Trends: 5.613 não processados
- Total 14.378 — sustenta 6/h × 24h × 100 dias

### Lição arquitetural
Toda mudança de cadência do maestro deve incluir:
1. Verificação de material em estoque (`processado_v9 = false`)
2. Sintonia com fórmula `escolher_editoria` (SLOTS_POR_HORA hardcoded = 6)
3. Sincronização espelho local após push pro Tencent

### Próximas 24h — esperar
- Volume deve subir de 48/dia (hoje) pra >100/dia
- Cat Internacional, Ciência/Tec, Esporte devem reaparecer (slot 3+ existe agora)
- Validar via tick :14/:44 do loop monitoramento

---

## ✅ Cleanup V8/bot_mayrag_v3 CONCLUÍDO 2026-05-02 14:48 BRT

### O que foi removido do /root/ (top-level)
- `bot_mayrag_v3.py` (com "g") — bot Telegram zumbi PID 510069 rodando 10 dias com `telegram.NetworkError`
- `agente_cafezinho_unificado_v8.py` — monolito legado V8 (substituído por V9 Trindade)
- `agente_cafezinho_unificado_v8_backup_20260330_0939.py` — backup pré-migração

### Onde foram parar
`/root/legacy/v8_mayrag_v3_20260502/` (com INDEX.md de manifesto)

### Backups vivos (3 caminhos de rollback)
1. `/root/cleanup_v8_mayrag_v3_20260502_1446.tar.gz` (MD5 `b1afa9c06e6753d183ff0066c728bd09`)
2. `/root/legacy/v8_mayrag_v3_20260502/` (cópia movida, INDEX.md tem comandos reversos)
3. Cópias em `cingapura_workspace/`, `_arquivo_velho/`, `test/`, `backups_codex_*/` (reservas históricas intocadas)

### Mayra V9 (Joia da Coroa) confirmada intocada
- PM2 `mayra_api` online 10D, 17.7MB ✅
- PM2 `mayra_zap` online 10D, 67.8MB ✅
- `mayra_core/`, `mayra_*.py`, WhatsApp, mayra_brain — todos preservados em /root/ ✅

### Lição aplicada
Operações destrutivas em infra crítica (kill processo + mv arquivos) precisam de:
1. Backup tar.gz pré-deploy (independente do mv pra legacy)
2. Manifesto INDEX.md com motivo + rollback explícito
3. Confirmação prévia de NÃO impactar componentes adjacentes (Mayra V9)
