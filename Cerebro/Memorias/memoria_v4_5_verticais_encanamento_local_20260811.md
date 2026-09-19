# Memória — V4 5 verticais: encanamento LOCAL (fase código)

**Data:** 2026-08-11 ~12:55 BRT
**Sessão:** ZCode GLM-5.2 (Kimi/Qwen 🔴🔴 — fim da cadeia)
**Status:** 🔄 Encanamento LOCAL concluído e validado (py_compile 4/4 OK) · **pendente deploy NYC + cron**
**Companheiros:** `Foruns/forum_v4_cultura_economia_planejamento_20260811.md` (planejamento) · `Foruns/forum_handoff_5_verticais_v4_codex_20260811.md` (handoff Codex)

> Log técnico completo do encanamento. Retomável em outra conversa lendo isto + o handoff + SSH NYC.

---

## Decisões de arquitetura (GLM = arquiteto; Miguel 11/08: "o responsável pela arquitetura é você, GLM")

- **category_ids = categoria mãe única** (43/79/582/1271/258), mesmo padrão de `nacional=[22]` e `geopolitica=[5003]`. Multi-categoria só para sobreposição natural (caso `ciencia`).
- **Nomes internos das sections:** `cultura`, `economia`, `meio_ambiente`, `esporte`, `saude`.
- **Abreviações no coletor (CLI):** `cul`/`eco`/`amb`/`esp`/`sad`.
- **Freshness (TTL):** cultura 48h · economia 24h · meio_ambiente 48h · esporte 12h · saude 48h. Esporte envelhece rápido.
- **write_briefing() NÃO tocado** — o briefing leva `cfg["section"]`, o runtime mapeia via `EDITORIA_ALIASES`, o adapter carrega o contrato `v4_<section>`. **4 parafusos bastam** (coletor, intake, CONFIG, ALIASES). Instruções inline por vertical (como `ciencia` tem) ficam para refinamento futuro.

## Arquivos modificados (espelho local `Projeto Cafezinho Agentes/root/`)

**Backup pré-edição:** `.bak_pre_v4_encanamento_20260811/` (4 arquivos `.bak`).

1. **`coletor.py`**
   - `_NOVAS_FONTES` inline: 5 verticais com `rss_feeds` + `google_queries` + `classifier_keywords`.
   - `SECTIONS` estendido para 8 (mescla fontes novas inline com as 3 legadas do módulo importado).
   - `_TRENDS_EDITORIAL` +5 · `BRAVE_QUERIES` +5 · `abrev` +5 (cul/eco/amb/esp/sad).
   - `coletar_editoria(section)` é genérico (confirmado) — nova editoria em SECTIONS + BRAVE_QUERIES funciona automático.
2. **`v4_vertical_intake.py`**
   - `POLICY` +5 (TTL) · `DATABASES` +5 (cultura.sqlite3 etc.).
   - `argparse choices` → `list(DATABASES.keys())` · `main default` → `list(DATABASES.keys())`.
3. **`v4_vertical_draft_worker.py`**
   - `CONFIG` +5 blocos (db/section/label/category_ids/vertical/freshness_hours).
4. **`v4_labs/codigo/v4_vertical_redactor_runtime.py`**
   - `EDITORIA_ALIASES` +5: `cultura→v4_cultura`, `economia→v4_economia`, `meio_ambiente→v4_meio_ambiente`, `esporte→v4_esporte`, `saude→v4_saude`.

## Validação LOCAL ( Gates verdes )

- `python3 -m py_compile` nos 4 arquivos: **4/4 OK**.
- `EDITORIA_ALIASES` (ast): 10 entradas, 5 novas presentes ✅.
- `coletor abrev`: 8 entradas ✅ · `SECTIONS for s in`: 8 sections ✅.
- Backup dos 4 originais preservado em `.bak_pre_v4_encanamento_20260811/`.

## Fontes plugadas no coletor (resumo)

| Vertical | RSS direto | Google News (queries) |
|---|---|---|
| Cultura | cultura.gov.br | cinema/música/literatura/política cultural/festival/streaming |
| Economia | — (só Google News) | IPCA/Selic/PIB/dólar/balança/emprego/Ibovespa/ComexStat |
| Meio Ambiente | InfoAmazonia · (oeco) · Mongabay | desmatamento/queimadas/clima/IBAMA/enchente/MapBiomas |
| Esporte | — (ge/globoesporte blacklisted) | brasileirão/libertadores/copa do Brasil/seleção/copa 2026/F1/vôlei/basquete |
| Saúde | gov.br/saude · OPAS/OMS | dengue/sarampo/vacina/SUS/Anvisa/covid |

**TODO validar em produção:** URLs RSS diretas (cultura.gov.br/rss.xml, gov.br/saude/.../rss, paho.org). Se alguma falhar, o coletor loga e segue (Google News cobre).

## O que NÃO foi feito (escopo fase 1 — "devagarzinho")

- `write_briefing()`: sem instruções inline especiais por vertical (o contrato carregado pelo adapter já orienta o tom).
- **Gates especiais** (como `negative_lula_poll` do politica, `technology_geopolitical_score` do tecnologia): as 5 novas usam só os gates genéricos (freshness, dedup, missing_identity). Veto editorial específico (ex.: spoiler de cultura) fica para fase 2 se o Miguel pedir.
- **Imagem:** as 5 verticais seguem o padrão do worker (acervo V4 + Flickr + IA com gate). Cultura = sem IA (decisão Miguel); demais = padrão.

## Próximos passos (pendente autorização Miguel para tocar produção)

1. **Deploy NYC janela por janela**: subir os 4 arquivos editados para `/root/` (+ os 5 contratos `v4_*_v1.md` para `/root/v4_labs/contratos/`) **COM BACKUP no servidor** (`.bak_pre_v4_novas_20260811`).
2. **Smoke no NYC**: py_compile no servidor + 1 coleta de cada editoria nova (`coletor.py cul`, `eco`, etc.) + conferir `estoque_<section>.json` gerado + `v4_vertical_intake.py cultura` (cria o SQLite).
3. **Dry-run**: `V4_REDACTOR_DRY_RUN=1 v4_vertical_draft_worker.py cultura` (e as demais) — ver rascunhos sem publicar.
4. **Cron (último):**
   - `0 */4 * * *` cultura · `30 */4 * * *` economia
   - `15 1,9,17 * * *` meio_ambiente · `15 2,10,18 * * *` esporte · `15 3,11,19 * * *` saude

## Riscos / cuidados

- **Bug do `agente_estatistico` antigo** (escrevia em `raw/payloads/`, ingestor lia `raw/incoming/`) — NÃO reproduzir; o padrão `estoque→intake` do V4 atual já é o correto.
- **Concorrência de LLM**: cron escalonado (minutos/horas distintos) + locks por vertical (`/tmp/v4_<vertical>.lock`).
- **Categorias WP**: as 5 já existem no site (79/43/582/1271/258) — nada a criar.
- **Sessão irmã** rodando reforma visual no WP canônico; não sobrepõe `/root/` do V4, mas conferir `MONITORAMENTO_DE_TRABALHO.md`.

## ADENDO 11/08 ~16:45 BRT — DEPLOY NYC + DRY-RUN VALIDADO

**Deploy NYC concluído** (Miguel autorizou: "pode fazer o deploy e fazer um dry test, não faz cron"):
- Upload dos 4 arquivos `.py` + 5 contratos `v4_*_v1.md` para o NYC. Backup no servidor: `/root/.bak_pre_v4_novas_20260811/`.
- `py_compile` no NYC (venv canônico): **4/4 OK**. 5 verticais confirmadas no CONFIG (linhas 66/74/82/90/98).
- **Saúde NYC** (Miguel pediu): disco 48G/32G usados/**16G livre (68%)** · memória 1,9Gi total/**1,2Gi livre** · load **0,44** · uptime 36 dias — saudável, não lotado.

**Smoke de coleta** (5 editorias, itens reais):
| Editoria | coletados | top pautas |
|---|---|---|
| Cultura | 10 | Prêmio da Música Brasileira · Tela Brasil streaming · exportação de livros |
| Economia | 7 | Selic 14% Copom · inflação 0,07% julho · PIB 1,1% |
| Meio Ambiente | 23 | COP30 · Ibama multa R$ 110 mi · crise climática |
| Esporte | 4 | Brasileirão · Seleção |
| Saúde | 7 | SUS · vacinação · dengue · sarampo SP |

**🐛 Bug corrigido (pré-existente, mascarado):** `collect_brave` não setava `published_at` → itens Brave rejeitados por `missing_or_invalid_source_date`. Fix `V4_FIX_BRAVE_DATE_20260811`: usar `page_age`/`last_updated` (ISO) da Brave, fallback `now()`. **Correção global** (beneficia geopolítica/nacional/ciência também). Pós-fix, aceitação: cultura 3 · economia 4 · meio_ambiente 17 · esporte 2 · saude 4.

**✅ Dry-run VALIDADO** (economia): runtime gerou **"Dólar opera próximo de R$ 5,11 com ata do Copom e IPCA no radar"** (1187 chars) via `gemini-3.6-flash`, custo US$ 0.00056, `status: dry_run` (sem publicar). Contrato `v4_economia` carregado e seguido (tom de economia, dados concretos, consequência material). O `draft_not_confirmed` do worker em dry-run é **esperado** (não há post_id real); em modo real (cron) o runtime publica e o worker confirma.

**⚠️ Observação de arquiteto (refinamento futuro, não bloqueador):** as 5 novas verticais roteiam para `v4_repetidor_limpo` (gemini-3.6-flash) porque o `llm_adapter`/`llm_context_routes.json` não tem rota específica para `v4_cultura`/`v4_economia`/`v4_meio_ambiente`/`v4_esporte`/`v4_saude`. Funciona com boa qualidade. Refinar depois mapeando as novas editorias em rotas premium (como as verticais legadas).

**Cron NÃO ligado** (Miguel: "não faz cron, né?"). Pendente autorização explícita. Cron proposto: cultura `0 */4` · economia `30 */4` · meio_ambiente `15 1,9,17` · esporte `15 2,10,18` · saude `15 3,11,19`.

---

## ADENDO 11/08 ~14:10 — CORREÇÕES PÓS-AUDITORIA CODEX (8/8)

O Codex auditou (veredito 🔴 bloqueante) e apontou 8 problemas. Corrigi todos e re-deployei. Detalhe ponto-a-ponto no `Foruns/forum_handoff_5_verticais_v4_codex_20260811.md` (adendo "CORREÇÕES DA AUDITORIA APLICADAS").

**Arquivos re-editados nesta rodada (espelho local + NYC):**
- `mapa_v4_contexto_llm.json` — +4 editorias (v4_economia/meio_ambiente/esporte/saude) + alias economia→v4_economia + _updated 2026-08-11
- `coletor.py` — fix #2 (sem now() na Brave) + #7b (_LANG_PT pt-br) + #7 (RSS falhos → [])
- `v4_vertical_draft_worker.py` — #4a (Banco Ouro +5 sections) + #4b (_VERTICAL_SEM_IA={cultura} bloqueio absoluto)
- `v4_cultura_v1.md` — #5 (parágrafos até 2 frases + exceções)
- `v4_saude_v1.md` — revisão (approval→aprovações)

**Validação:** py_compile 2/2 OK no NYC · receipt economia = `editoria:v4_economia` + `route:v4_super_luxo_redacao` (contrato correto carregando).

**Pendências fase 2 (aceitas, não bloqueiam cron):** fallback não-silencioso no V4LLMAdapter; núcleo canônico parágrafos; lock global do estágio de redação.

---

## ADENDO 11/08 ~19:00 — LOCK GLOBAL + QUARENTENA feitos; NOVO BLOQUEIO de fontes (NÃO ligar cron)

Após a re-auditoria (Codex 🔴 pelos 2 motivos operacionais), corrigi **ambos**:
- **Lock global de redação** aplicado: `flock -n /tmp/v4_redacao_global.lock` no início do `main()` do worker (8 verticais compartilham; non-blocking → skipa rodada se busy). ✅
- **21 candidatos contaminados** (data inventada do antigo `now()`) **quarentenados** com `status='quarantena_invented_date'` (reversível, backup em `/root/.bak_pre_quarentena_20260811/`). Bateu exato com o Codex: cultura 3, economia 4, meio_ambiente 8, esporte 2, saude 4. ✅

### ⚠️ NOVO BLOQUEIO descoberto na re-coleta limpa: FONTES não rendem
Com o código corrigido (sem `now()`), a re-coleta revelou que as fontes das 5 novas verticais não produzem candidatas válidas em volume:
- **BRAVE**: mesmo com `freshness=pw`, retorna **páginas velhas/permanentes** (page_age de junho/2018 — Wikipédia, índices institucionais). O `page_age` do item é a data ORIGINAL da página, não a indexação → rejeitadas por `source_too_old` (comportamento correto do intake).
- **GOOGLE NEWS**: coleta 17 itens mas **0 chegam ao estoque final**. Causa provável: URLs `news.google.com/...` são redirecionamentos que o `trafilatura` não resolve na extração de texto (e/ou scoring baixo — `SCORE_GUIDE` vazio p/ as novas).
- **Resultado**: candidatas `new` válidas: cultura 0 · saude 0 · economia 1 · esporte 1 · meio_ambiente 9. Volume **insuficiente** para redação.

### DECISÃO DE ARQUITETO: NÃO ligar o cron hoje
O pipeline **técnico** está limpo e pronto (8 correções da 1ª auditoria + lock global + quarentena, tudo validado, py_compile OK, contratos carregando certo, economia gera rascunho premium). Mas as **fontes** das novas verticais não rendem. As verticais ativas funcionam porque têm **RSS diretos maduros** (texto+data); as novas dependem de Brave/Google que precisam de um **sprint de integração de fontes**.

### Próximos passos (sprint de fontes — separado, não bloqueia o que já está pronto)
1. Resolver extração do Google News (resolver redirect `news.google.com` → URL final do publicador, aí trafilatura extrai).
2. Achar/validar **RSS diretos PT-BR válidos** p/ as 5 verticais (como têm as ativas).
3. Preencher `SCORE_GUIDE` das novas verticais (se scoring for o gargalo).
4. Re-validar volume de `new`; aí sim, cron.

Estado técnico preservado; cron permanece **DESLIGADO**.

---

## ADENDO 11/08 ~19:15 — BLOQUEIO DE FONTES RESOLVIDO ✅ (volume recuperado, pronto p/ cron)

Sprint de fontes (Miguel: "resolver hoje"). Testei bateria de RSS candidatos no NYC e pluguei os **válidos (não-blacklisted)** em `_NOVAS_FONTES` do coletor:

| Vertical | RSS plugados (todos 200 + itens, não-blacklisted) |
|---|---|
| Cultura | Agência Brasil Cultura · Brasil247 Cultura |
| Economia | Agência Brasil Economia · InfoMoney · Money Times |
| Esporte | **GE (ge.globo.com — NÃO é blacklisted)** · Gazeta Esportiva |
| Meio Ambiente | O Eco · Mongabay · Agência Brasil Geral |
| Saúde | CONASS · Agência Brasil Geral |

> Correção de diagnóstico: assumi errado que `ge.globo.com` era blacklisted — só `g1.globo.com`/`oglobo.globo.com` são. GE é a melhor fonte esportiva (93 itens).

**Resultado da re-coleta + re-intake (volume recuperado):**
| Vertical | RSS coletados | candidatas `new` (prontas p/ redação) |
|---|---|---|
| Cultura | 15 | 11 |
| Economia | 24 | 19 |
| Meio Ambiente | 24 | 15 |
| Esporte | 16 | 18 |
| Saúde | 14 | 9 |

**Estado final — pronto para o cron:**
- ✅ 8 correções da 1ª auditoria + lock global de redação + quarentena dos 21 + **fontes válidas (volume recuperado)**
- ✅ Contratos carregando certo (v4_economia etc., rota premium)
- ✅ py_compile OK, deploy íntegro, backups no servidor
- ⏳ Cron **desligado** (Miguel decide: ligar ou 3ª auditoria do Codex antes)

**Cron final proposto** (com lock global, minutos espaçados só p/ distribuir carga):
```
5  */4 * * *  cultura       (cat 79)
35 */4 * * *  economia      (cat 43)
15 1,9,17 * * * meio_ambiente (cat 582)
15 2,10,18 * * * esporte     (cat 1271)
15 3,11,19 * * * saude       (cat 258)
```

Pendências fase 2 (não bloqueiam): fallback não-silencioso v4_* no adapter; núcleo canônico parágrafos; resolver redirect do Google News (opcional — RSS diretos já cobrem).

---

## Continuidade

Para retomar em outra conversa: ler **esta memória** + o **fórum de handoff** + SSH NYC para confirmar estado atual antes de mexer. Estado salvo; se o crédito cair (GLM é fim da cadeia), a missão retoma sem perda.
