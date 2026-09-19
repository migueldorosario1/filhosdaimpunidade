# Fórum — Repetidor Estatal Opção D (auditor veto-only, threshold 40)

> **Data:** 2026-07-17 00:13 BRT
> **Autor:** GLM/Ming (glm-5.1 via wrapper Claude Code CLI)
> **Continuação de:** `forum_repetidor_estatal_redeploy_nyc_20260714.md` (deploy inicial)
> **Status:** ✅ Opção D deployada e validada — primeira matéria real publicada (post 261812, draft)
> **Decisão sancionada por:** Miguel do Rosário (16/07/2026)

---

## 🎯 TL;DR

Reforma data-driven do `agente_repetidor_estatal.py` ajustada após 3 iterações de design nesta sessão:

1. **Opção B** (proposta e revertida): remover `auditoria_llm_batch()` completamente
2. **Opção D** (sancionada): manter auditor + **threshold 65→40** + **prompt veto-only** ("na dúvida aprove, você não é editor-chefe")

**Princípio Miguel (regra canonizada):** "auditor não é curador. ele tem que ver se a matéria é publicável, ponto."

Resultado: primeira publicação real saiu às 04:44 BRT de 16/07 (post 261812, draft, "Rodoviários do Rio não chegam a acordo com patrões"). Cron `27 * * * *` NYC religado em produção, uma matéria nova por hora como draft.

---

## 📜 Timeline da sessão (15/07 22:22 → 17/07 00:13 BRT)

### Fase 1 — Diagnóstico shadow mode (15/07 22:25)

Confirmei estado do NYC:
- `DRY_RUN=1` ativo desde deploy 14/07 (30h+ de shadow)
- 9 rodadas consecutivas executadas
- 8 matérias aprovadas, 14 descartadas (taxa 36%)
- Pipeline estável, sem tracebacks
- Cascata LLM funcional: `deepseek-v4-pro` (ranker) → `deepseek-v4-flash` (auditor) → `deepseek-v4-pro` (reescritor)

Apresentei 8 matérias que o script "publicaria" em DRY_RUN. Miguel leu e estranhou: matéria "Senado aprova educação financeira" (PLC 2.979/2023) tinha sido descartada pelo auditor com Nota 15 "impacto difuso" — sendo matéria factual institucional legítima.

### Fase 2 — Opção B (16/07 ~01:00)

Propus 3 caminhos:
- A: manter auditor, baixar threshold 65→45-50
- B: **remover `auditoria_llm_batch()` completamente** (top 1 do ranker publica direto)
- C: reverter tudo (8 heurísticas removidas voltam)

Miguel escolheu **B**. Apliquei:
- Removi função `auditoria_llm_batch()` (114 linhas)
- Removi função `_threshold_dinamico()` (30 linhas)
- Substituí loop de publish: iterar top 3 do ranker direto, sem crivo
- Arquivo: 895 → 744 linhas (-151)
- Deploy: backup NYC `.bak_pre_opcaoB_20260716_033731`, rsync, py_compile OK, smoke test passou

**Resultado do smoke test:** matéria "Plenário aprova educação financeira nas escolas" (a mesma que o auditor barrava com Nota 15) publicou direto como score=95.

### Fase 3 — Reconsideração (16/07 ~03:30)

Miguel leu a matéria que passou e ponderou: *"deixa eu ler essa matéria, não sei se a solução de remover auditoria foi a melhor. talvez fosse melhor manter auditoria, porém, ajustar outro ponto para manter a qualidade das publicacoes."*

Propus 4 caminhos alternativos:
- D: **auditor veto-only (threshold 40 em vez de 65)** — mantém o crivo mínimo mas aprova quase tudo
- E: auditor exigente + fallback "se descarta tudo, publica top 1 mesmo assim"
- F: auditor com prompt recalibrado (sem "manchete do dia")
- G: híbrido (D + threshold dinâmico)

Miguel escolheu **D**. Antes de aplicar, enviou diretriz canonizada:

> **"a gente vai melhorar a qualidade pela coleta e curadoria. o auditor não pode ser curador. ele tem que ver se a matéria é publicável, ponto"**

### Fase 4 — Opção D aplicada (16/07 04:00)

Restaurei versão pré-Opção B do backup NYC, depois ajustei:

1. **Docstring topo:** substituí "Curadoria LLM rigorosa: threshold PUBLICAR >= 65" pela nova filosofia (auditor = pergunta binária)
2. **Constante nova:** `THRESHOLD_PUBLICAVEL = 40` substituiu `_threshold_dinamico()` (função de 30 linhas removida — bootstrap 65 / percentile 30 dinâmico não faz mais sentido)
3. **Prompt sys_prompt reescrito:** trocou "Você é um editor rigoroso" por "Você é um AUDITOR de publicação". Removeu "Seja EXIGENTE", "manchete do dia", "CALIBRAGEM média 40-45". Adicionou "NA DÚVIDA, APROVE" e "você NÃO é o editor-chefe".
4. **Prompt user_prompt reescrito:** trocou "Seja RIGOROSO" por "Audite" + esclarecimento do que é PUBLICÁVEL vs INPUBLICÁVEL.
5. **Lógica de validação:** `limiar_publicar = _threshold_dinamico()` → `limiar_publicar = THRESHOLD_PUBLICAVEL`

Deploy: backup NYC `.bak_pre_opcaoD_20260716_042407`, rsync, py_compile OK. Arquivo final: 870 linhas / 42198 bytes / md5 `dc061781d454619f43d1832f5d7cd5f7`.

### Fase 5 — Smoke test Opção D (16/07 04:24)

Rodada manual DRY_RUN=1:
- Coleta: 117 pendentes
- Ranking top 3: `[(151,95), (133,90), (124,80)]`
- **Auditor veto-only aprovou 3/3** com justificativas coerentes:
  - [1] Nota 95: "Aprovação de projeto de lei no Plenário com votação nominal é fato jornalístico claro"
  - [2] Nota 90: "Aprovação de projeto que prorroga linha de crédito para hospitais filantrópicos constitui decisão legislativa concreta"
  - [3] Nota 80: "Aprovação de protocolo de atendimento de infarto em comissão do Senado é avanço legislativo identificável"
- PUBLICARIA: "Senado aprova uso de emendas da saúde para atendimento feito por bombeiros"

### Fase 6 — Religar produção (16/07 04:41)

Miguel pediu "vamos fazer uns testes?" → escolheu "Religar produção (DRY_RUN=0 + draft)".

- Backup `/root/.env.unificado.bak_pre_dryrun0_20260716_044151`
- Edit NYC: `DRY_RUN=1` → `DRY_RUN=0`
- Script `publicar_wordpress()` mantém `status="draft"` hardcoded (linha 566, legado da fase homologação 14/07)
- Rodada manual às 04:42 BRT publicou primeira matéria real

---

## 🎉 Primeira publicação real

**Post ID 261812** — criado 04:44:17 BRT (16/07)

| Campo | Valor |
|---|---|
| Título | Rodoviários do Rio não chegam a acordo com patrões |
| Status | `draft` |
| Categoria | Mobilidade Urbana (1650) ✅ |
| Featured media | 261811 (full-res EBC 4333 KB → 2560px) |
| Score | rank=85, auditor=85, dedup=0.382 |
| Fonte original | Agência Brasil |
| Indexação | Google Indexing pingado (quota 55/200) |
| Link admin | https://controle.ocafezinho.com/wp-admin/post.php?post=261812&action=edit |
| Preview público | https://controle.ocafezinho.com/?p=261812 |

Conteúdo: lide factual curto (45 palavras) + texto integral da agência preservado + "Fonte: Agência Brasil" com link. Sem chapa branca.

---

## 🐛 2 pendências conhecidas (não bloqueantes)

### P1 — Bug tags sumiram

LLM devolveu tags em linhas separadas:
```
rio de janeiro
mobilidade urbana
direitos humanos
```

Script esperava vírgula (`extrair_html_e_titulo()` L540 faz `tag_line.split(",")`). Filtro pegou como UMA string inválida e dropou tudo. Post 261812 ficou com `tags: []`.

**Fix proposto:** trocar `split(",")` por regex tolerante (vírgula OU newline) no parser:
```python
tags = [t.strip() for t in re.split(r"[,\n]", tag_line) if t.strip()]
```

### P2 — Bug capitalização (pré-existente)

`corrigir_capitalizacao_titulo()` (em `titulo_utils.py`) regrediu em matérias com nomes próprios:
- "Marielle" → "marielle"
- "Domingos Brazão" → "domingos brazão"
- "TCE-RJ" → "tce-rj"

Apareceu na rodada 01:29 BRT 15/07 (matéria "Mandante da morte de marielle, domingos brazão perde cargo no TCE-RJ"). Não apareceu nas rodadas seguintes porque os títulos não tinham nomes próprios problemáticos. Vai voltar a aparecer.

**Diagnóstico pendente:** ler `titulo_utils.py` e achar onde o dicionário `_NOMES_PROPRIOS` perde efetividade.

---

## 📦 Backups criados nesta sessão

### NYC (`/root/`)
- `agente_repetidor_estatal.py.bak_pre_opcaoB_20260716_033731` (43514 bytes, versão com auditor threshold 65)
- `agente_repetidor_estatal.py.bak_pre_opcaoD_20260716_042407` (35609 bytes, versão Opção B sem auditor)
- `.env.unificado.bak_pre_dryrun0_20260716_044151` (DRY_RUN=1)

### Local (`~/.claude/`)
- `settings.json.bak_pre_glm52_20260715_233734` (mapeamento Opus=glm-5.1)

### Rollback procedure (se necessário)
```bash
# Reverter Opção D → Opção B (sem auditor)
ssh root@198.199.121.136 'cp /root/agente_repetidor_estatal.py.bak_pre_opcaoD_20260716_042407 /root/agente_repetidor_estatal.py'

# Reverter Opção D → original (com auditor threshold 65)
ssh root@198.199.121.136 'cp /root/agente_repetidor_estatal.py.bak_pre_opcaoB_20260716_033731 /root/agente_repetidor_estatal.py'

# Desligar produção de volta pra shadow mode
ssh root@198.199.121.136 'sed -i "s/^DRY_RUN=.*/DRY_RUN=1/" /root/.env.unificado'
```

---

## 🧠 Decisões sancionadas

1. **Auditor veto-only com threshold 40** (Opção D) — Miguel 16/07/2026
2. **`status="draft"`** no publish (homologação no wp-admin antes de `status="publish"`)
3. **DRY_RUN=0** religado em produção (16/07 04:41 BRT)
4. **Mapeamento Claude Code Opus → glm-5.2** (15/07 23:37 BRT) — válida só na próxima sessão

## 🚧 Decisões pendentes

- **Promover `status="draft"` → `status="publish"`** após quantas matérias homologadas? (Miguel decide ao longo dos próximos dias)
- **Bug tags P1** — quando corrigir (próxima sessão ou janela dedicada)
- **Bug capitalização P2** — diagnóstico completo do `titulo_utils.py`

---

## 🔗 Memórias relacionadas

- `feedback_auditor_nao_e_curador.md` — filosofia Miguel canonizada (auditor = pergunta binária)
- `project_repetidor_estatal_redeploy_nyc_20260714.md` — deploy anterior
- `project_repetidor_estatal_reforma_data_driven_20260715.md` — estado da reforma

## 📚 Arquivos alterados nesta sessão

| Arquivo | Tipo | Mudança |
|---|---|---|
| `Outros/Agentes Labs/agente_repetidor_estatal.py` | local | Opção D aplicada (870 ln, threshold 40 + prompt veto-only) |
| `/root/agente_repetidor_estatal.py` | NYC | idem (rsync) |
| `/root/.env.unificado` | NYC | `DRY_RUN=1` → `DRY_RUN=0` |
| `~/.claude/settings.json` | local Claude | `ANTHROPIC_DEFAULT_OPUS_MODEL`: `glm-5.1` → `glm-5.2` |
| `memory/feedback_auditor_nao_e_curador.md` | auto-memory | NOVO |
| `memory/MEMORY.md` | auto-memory | índice atualizado |

---

## 🔍 Comandos úteis

```bash
# Ver últimas rodadas em produção
ssh root@198.199.121.136 'tail -80 /root/agent_data/repetidor_estatal.log'

# Listar drafts recentes do repetidor no WP
curl -s -u "Redator:[CREDENCIAL_WP_ANTIGA_REMOVIDA_2026-07-27]" \
  "https://controle.ocafezinho.com/wp-json/wp/v2/posts?status=draft&per_page=10&orderby=date&order=desc" \
  | jq '[.[] | {id, title: .title.rendered, date}]'

# Forçar rodada manual agora
ssh root@198.199.121.136 'cd /root && /root/venv/bin/python3 agente_repetidor_estatal.py 2>&1 | tail -40'

# Voltar pra shadow mode (pause)
ssh root@198.199.121.136 'sed -i "s/^DRY_RUN=.*/DRY_RUN=1/" /root/.env.unificado'
```

---

**Assinado:** GLM/Ming (glm-5.1 via wrapper Claude Code CLI)
**Identidade canônica:** `Cerebro/IDENTIDADE_CANONICA.md` linha 26

---

## Alternância persistente 50% No Home — 21/07 11:52 BRT

- Ordem de Miguel: deixar 50% dos posts do Repetidor Estatal na categoria `No Home` 20699.
- Implantado no worker vivo de NYC (`/root/agente_repetidor_estatal.py`) um estado SQLite persistente em `estatal_runtime_state`.
- A alternância avança somente depois de o WordPress confirmar que o post foi criado: primeiro `No Home`, próximo capa normal, repetindo após reinícios.
- Previsão do Tempo (5102) continua sempre `No Home`. Como o estado registra o resultado efetivo, o post não meteorológico seguinte fica normal, compensando a exceção sempre que possível.
- Teste isolado da máquina de estados: Política → `No Home`; Política → normal; Previsão do Tempo → `No Home` obrigatório; Política → normal.
- Nenhuma matéria foi publicada durante o teste. Cron preservado em `7 */2 * * *`.
- Backup: `/root/agente_repetidor_estatal.py.backup_pre_nohome50_20260721_1152`.
- Observação de fonte: `Outros/Agentes Labs/agente_repetidor_estatal.py` está defasado em relação ao worker vivo e não foi sobrescrito, para não apagar correções posteriores de data, imagem e taxonomia. O deploy foi feito sobre a versão viva após backup.

## Reteste Brave Search — 21/07 11:50 BRT

- Consulta mínima repetida por pedido de Miguel.
- Resultado confirmado: HTTP 422, `SUBSCRIPTION_TOKEN_INVALID`, zero resultados.
- Não é oscilação transitória; a credencial precisa ser substituída.
- O coletor Ciência/Tecnologia continua com RSS e Google News e encerra Brave após a primeira falha de autenticação por rodada, evitando repetição inútil.
