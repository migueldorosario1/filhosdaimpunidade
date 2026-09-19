# Fórum — Auditoria integral dos V4 do Cafezinho (sprint handoff Codex/Miguel)

**Data:** 13/08/2026 · **Agente:** ZCode (Kimi K3) · **Sprint:** auditoria independente de TODOS os V4
**Carta-mãe:** `Foruns/forum_handoff_zcode_auditoria_todos_v4_padrao_ouro_20260813.md`
**Memória técnica irmã:** `Memorias/memoria_auditoria_v4_todas_verticais_20260813.md`
**Evidências locais:** `ZCodeProject/auditoria_v4_20260813/fase0/` (crontab, hashes, contagens, logs, código vivo)

---

## Estado da missão (vivo)

- **Fase 0 (congelar verdade operacional): ✅ CONCLUÍDA 13/08 ~12:35 BRT** — crontab, hashes sha256, processos, locks, esquemas/contagens dos 13 bancos, inventário WP canônico.
- **Fase 1 (auditoria só-leitura, seguir pauta RSS→WP): ✅ SUBSTANCIALMENTE CONCLUÍDA** — cadeia completa traçada (coletor→estoque→intake→candidates→select→briefing→redator→draft→taxonomia→staging pending→imagem→draft_confirmed) + posts das 5 novas rastreados no WP.
- **Fases 2/3 (comparação fronteiras + plano de correção): 🔄 EM REDAÇÃO** — dados coletados, matriz em construção.
- **Fases 4/5 (correção/homologação): ⏸️ AGUARDAM Miguel** — nenhum patch será aplicado sem aprovação do plano.
- **Zero escrita em código/servidor/WP até aqui** (só leitura + este registro).

## Vereditos provisórios (com prova)

| Vertical | Veredito provisório | Prova |
|---|---|---|
| Nacional | **V4 estrutural maduro, mas degradado AGORA** | 296 drafted; 19 repair_preflight_failed/24h; post 265482 pending preso por imagem |
| Geopolítica | **V4 estrutural maduro, degradado AGORA** | 309 drafted; 38 repair_preflight_failed/24h; cota IA 50% estourada; 265504 preso |
| Tecnologia/Ciência | **V4 estrutural, instável** | 104 drafted mas 33 failed/24h (redator rc=1); taxonomy_not_confirmed |
| Cultura | **V4 estrutural, BLOQUEADO** | 0 drafted; post 265473 criado→preso; política SEM_IA absoluta = válvula nunca abre |
| Economia | **V4 estrutural, BLOQUEADO** | 0 drafted; 265454 preso (resolvido p/ publish pela ponte Kimi+Claude) |
| Meio Ambiente | **V4 estrutural, frágil** | 0 drafted; só 2 eventos, ambos rc=1; sem bloqueio de fila, falha na redação |
| Esporte | **V4 estrutural, BLOQUEADO** | 0 drafted; 265439 preso (publicado pela ponte); freshness 12h expira pautas |
| Saúde | **V4 estrutural, instável** | 0 drafted; editorial_blocked (acrônimo no título); sem fila presa |
| Regional Sudeste | híbrido maduro | 11 drafted, worker próprio (`v4_regional_*`) |
| Regional Norte | híbrido, pouca produção | 3 drafted + 1 image_pending |
| Regional Nordeste | **sem redação** | tabela draft_events NÃO EXISTE; 1.481 new acumulados |
| Regional Centro-Oeste | **sem redação** | tabela draft_events NÃO EXISTE; 758 new |
| Regional Sul | híbrido, bloqueado | 0 drafted + 1 image_pending |

## Confirmações e correções ao diagnóstico do Codex

1. ✅ **Confere:** 8 verticais no cron (geo 0,30 · nacional 20,50 · ciência 10,40 · econ 35*/4 · cultura 5*/4 · amb/esp/sad 15 1,9,17/2,10,18/3,11,19 UTC).
2. ✅ **Confere:** 5 novas usam o encanamento canônico (mesmo CONFIG, intake, worker, redator) — V4 por arquitetura, não homologadas.
3. ✅ **Confere (contagens ~iguais):** drafted nacional 296 / geo 309 / ciência 104 / 5 novas ZERO.
4. ⚠️ **CORREÇÃO:** a chamada duplicada de `repair_pending_image` **NÃO existe no código vivo** (worker mtime 13/08 12:14 UTC, sha256 `49c2bf5f…`): def em 1961, chamada única em 2530. O Codex viu versão pré-patch de idempotência.
5. ⚠️ **NUANCE:** o desvio do espelho está morto no runtime (`if False`, linha 2510 — `V4_MIGRADO_CANONICO_20260812`), MAS o comentário do cron ainda diz "5 verticais publicando DRAFT no espelho" (dívida documental) e **há logs vivos de timeout para cafezinho.news** do período pré-migração — separado rigorosamente: histórico ≠ runtime.
6. ✅ **Confere e é PIOR:** bloqueio de cabeça de fila é **por design** (`return 4` quando reparo falha; `return 0` quando repara) — uma imagem pendente congela a vertical. Cultura: congelamento **permanente** (`_VERTICAL_SEM_IA={cultura}` — nem a válvula final libera).
7. ✅ **Confere:** `wp_created`/`wp_created_failed` sem caminho de retomada (reparo só cobre outcome `image_pending`).
8. ✅ **Confere:** lock global não bloqueante — mas quantificado: só 9 rodadas perdidas hoje. O dano real é o loop de reparo (187/210 preflight_failed acumulados nacional/geo).
9. 🆕 **NOVO (Codex não viu):** as 5 novas **redigem com sucesso** (receipts: 265431/265439/265454/265471/265473 via gemini-3.6-flash, 1º attempt). O gargalo é 100% imagem+fila, não redação.
10. 🆕 **NOVO:** 4 posts das 5 novas já foram **publicados pelo caminho sancionado** (imagens Kimi 11:15 + revisão/promoção Claude) — o contrato draft→revisão→publish FUNCIONA.
11. 🆕 **NOVO:** `quarantena_invented_date` (21 pautas nas 5 novas) **não existe em nenhum código vivo** — foi quarentena pontual de manutenção (11/08). O gate vivo é `missing_or_invalid_source_date` no intake (fail-closed) + fix Brave sem data.
12. 🆕 **NOVO:** as 5 novas **não têm gate de nexo editorial no intake** (só tecnologia e política têm) → poluição de pauta: páginas de seção CNN/INPE, "IPCA Hoje" (página viva), "ao vivo" de jogos, releases CONASS.
13. 🆕 **NOVO:** factual gate quase sempre pulado (`sem_claims` / `llm_indisponivel`) — existe mas é quase inócuo hoje.
14. ✅ **Segurança de publicação:** redator cria SOMENTE `draft` (runtime linha 174); worker move para `pending`; nenhum caminho automático chega a `publish`. 738 publishes com zizi_job_id desde 19/07 são promoções externas (revisão humana/Claude/Sentinela) — 15 desde 12/08.

## O que falta

- Fase 2: tabela campo a campo novas×fronteiras (dados já coletados, redação).
- Fase 3: plano de correção priorizado em 4 grupos, com backup/teste/rollback por item.
- Manifesto do backlog WP (74 pending + 42 draft com zizi_job_id; ~25 órfãos cross-vertical com dias de fila).
- Veredito final individual + critérios de homologação por vertical.

## O que preciso de você (Miguel)

1. **Sinal verde para o plano de correção (Fase 3→4)** quando eu entregar — nenhum patch antes.
2. **Decisão editorial pendente:** cultura SEM IA absoluta trava a vertical para sempre quando não há foto real — manter assim (ponte humana/Claude caça foto) ou abrir válvula final também para cultura?
3. **Nordeste/Centro-Oeste sem worker regional** (tabela draft_events inexistente): ligar redação regional nessas macrorregiões ou é decisão consciente?
