# 📡 ESTADO ATUAL — radiografia Kimi do ecossistema

**Última leitura:** 2026-07-28 14:45 BRT (Kimi K3) — anterior: 2026-07-27 14:26

## Semáforo geral: 🟢 SAUDÁVEL (com 2 pontos de atenção não-críticos)

## Cafezinho principal (site + Sentinela)

- **Site:** 🟢 online, 543ms médio, 2 microquedas na madrugada (3min46s total, Cloudflare timeout) — irrelevante.
- **Publicação 24h:** 18 posts. Audiência: estável.
- **Loop Sentinela:** 41 ciclos hoje, todos exit=0. Últimos 5 ciclos sem ações (normal — esteira limpa).
- **Gate fact-check (bug #37, instalado hoje 13:33):** ativo, primeiro ciclo 100% pós-patch foi 14:00 exit=0. Ainda não houve proposta factual real pro gate exercer — Claude observa (contrato §2.5).
- **WARN do ciclo 15:09 ("sem drafts V4 há 48h") — INVESTIGADO: alarme falso com nuance.**
  - Workers NYC ATIVOS: geopolítica gerou drafts hoje 08:41 (262958→262972, todos publicados dentro do cap 2h ✅); nacional 14:22 BRT dedupando corretamente (`duplicate_aborted`/`duplicate_blocked` contra convenção PL/Milei/Datafolha — proteção bug #24 funcionando ✅); ciência `no_candidate` (normal).
  - Os "90 drafts de 23/07" são **backlog morto** — nunca vão passar no cap 2h. O detector do Sentinela conta só drafts novos pendentes e vai alertar pra sempre enquanto o backlog existir.
  - **Pendência editorial pro Miguel:** purgar ou reprocessar os 90 drafts mortos? (decisão dele, não executo sem OK)
  - **Sugestão pro Claude (carta enviada):** detector deve cruzar com `draft_confirmed` recentes nos logs NYC antes de alarmar.

## Temáticos V4 (8 sites, local)

- **Coleta 13h:** aiatolah 7, discoverbrazil 11, globalsouth 19, riocarta 1, mapario 1 — saudável.
- **ceara:** curado hoje (bug #38 — feeds 2018/mortos trocados; 0→16 itens). Próxima coleta */8h confirma recorrência.
- **railpost/mundotrilhos:** 0 itens 13h = saturação normal (URLs conhecidas), não bug.
- **Sem sinais de Brave quebrado** — bug B original refutado hoje (ver manual #38).

## Servidores (NYC + Tencent)

- **Chave Brave rotacionada sincronizada nos 2** (14:25 BRT, smoke HTTP 200 de cada um). Drift eliminado.
- Tencent: standby (Chairman decide reativar; failover scripts prontos).
- NYC: workers V4 ativos (ver acima), cron saudável.

## Estado da ponte (27/07 14:12)

- ✅ **PONTE ESTRUTURADA APROVADA (28/07 14:45):** cartinha Claude 14:40 respondida (§8 por instância Desktop paralela + §9 adendo técnico desta sessão). `MEMORIA_TOTAL_PONTE.md` v1 aprovado: 15-25KB, tabela markdown, Modo B API autorizado com guardrails (20/dia, log BRL, revogável por Miguel; omitir `temperature` — k3 trava em 1). Claude constrói no próximo ciclo vigília; Kimi valida na primeira leitura.
- **Contrato ASSINADO por Claude 05:31** (aceite integral + emenda [FACT-CHECK-DESCARTE], aceita por mim 14:05). Ponte em uso real: 2 escalas Claude→Kimi hoje (travas V4 10:05 ✅ resolvida 13:30; dup 263072 13:20 em tratamento).
- ✅ **263072 RESOLVIDO:** foi o Miguel quem publicou manualmente (pipeline inocente). REGRA NOVA permanente (14:20): duplicata/hold em publicado → **status=pending** (um degrau abaixo), não draft, não trash. Aplicado: 263072 publish→pending 14:26.
- 🟡 Gate #37: sugestão Claude de estender pra gate de publicação (casos Yellen→Bessent, Barroso→Fachin de hoje) — candidata de sprint, aguarda Miguel.

## Pendências abertas (ordem de prioridade)

1. ✅ **90 drafts mortos (página 1) purgados** — trash WP + memória permanente (`Cerebro/Backups/drafts_v4_purge_20260726_1534.json` + índice + restore script, indexado no BACKUPS node). Regra "nada morre nunca" cumprida.
1b. 🔴 **DESCOBERTA MAIOR — aguardando Miguel:** o WP só devolve 100 drafts/página e o Sentinela não pagina → os "90" eram só a página 1. Backlog real do author 5470: **659+ drafts** (o mais velho de **2019** — author 5470 não é só V4, é conta-robô histórica). Purga estendida NÃO autorizada ainda — decisão do Miguel com escala na mesa.
2. 🟡 **Claude:** ajustar detector `sem_drafts_v4_recentes` (carta na inbox dele) + relatório semanal sexta 23h (dele).
3. 🟢 Quota real SearchAPI/plano Brave: Miguel confirma no dashboard quando puder (não bloqueia nada).
4. 🟢 Feed g1/ceara zumbi (2018): auditoria de feeds-zumbis nos demais sites → candidata a checkup semanal do Claude.
