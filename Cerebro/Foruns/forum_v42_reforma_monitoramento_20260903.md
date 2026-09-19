# Fórum Tema Duplo — REFORMA DO AGENTE V4.2 ESTATÍSTICA (NYC) + MONITORAMENTO PELOS AGENTES

**Data:** 03/09/2026, ~01:40 BRT · **Autor:** ZCode/GLM-5.3 (DSH us65, sessão DSC) · **Ordem do Miguel (02/09 ~20h, por texto):** "dar uma melhorada no v4.2 estatística que você está fazendo no cafezinho News... faça uma conferência vê se ele tá alucinando... faça uma reforma nele [tirando a] inteligência barata... manda o DSN Ideias analisar o v4.2 estatística... o cafezinho espelho manda... uma boa investigação e manda ele mandar os posts para o cafezinho ideias acompanhar e ver se ele tá fazendo alucinação ou está indo bem."

---

## 1. INVESTIGAÇÃO — o agente alucina?

**Amostra:** todos os 8 posts públicos da categoria Estatística (100005) do espelho cafezinho.news, 26/08–02/09 (400137, 400158, 400168, 400178, 400183, 400194, 400209, 400265).

**Veredito NUMÉRICO: NÃO ALUCINOU NÚMERO.** Todo número publicado bate com a fonte primária:
- ComexStat consolidado de julho/2026 (conferido via imprensa — SBT News; API do MDIC bloqueada no us65 por WAF Cloudflare): exportações p/ China US$ 10,673 bi, importações US$ 6,418 bi, total US$ 34,119 bi, importações totais US$ 27,052 bi, superávit US$ 7,07 bi — exatos nos posts.
- FRED (fredgraph.csv): USTRADE 15.440,9 (jul/2026) ✓ · FEDFUNDS 3,63 ✓.
- BCB SGS: Selic (432) 14,0 ✓ · dólar (1) 5,1642 ✓.
- Eurostat: balança extra-UE −4.920,9 EUR mi (jun/2026) ✓.
- Nota: Xinhua de 07/08 trouxe números PRELIMINARES de julho (9,69 bi) — o banco do agente já tinha o CONSOLIDADO (10,67 bi); sem erro do agente.

**Mas o JORNALISMO alucinou em 9 classes de defeito** (a "inteligência barata" que o Miguel sentiu):
1. **Título duplicado**: 400178 e 400265 com título IDÊNTICO ("Brasil e China aprofundam eixo Sul-Sul com comércio recorde").
2. **Reciclagem**: 5 posts (29/08–02/09) com os MESMOS números de julho apresentados como novidade diária.
3. **Causa-raiz (bug)**: `escolher_tese()` do redator devolvia SEMPRE `comercio_sul_sul` (primeira da lista, sem critério) — todo dia a mesma pauta.
4. **Janela errada**: 400265 chama o valor MENSAL de 34,12 bi de "acumulado de doze meses".
5. **Moeda errada**: 400178/400209 dizem "US$ 4,92 bilhões" para o déficit europeu que é **EUR** (série Eurostat em euros).
6. **Defasado como corrente**: GACC de FEVEREIRO (90,98 bi, +186,82%) apresentado como "recorde" em textos de julho/agosto.
7. **Cosmético**: códigos crus de série (BCB/BCB_433) na legenda do gráfico.
8. **Redundância**: abertura com dupla sentença repetindo o mesmo fato.
9. **Enchimento infalsificável**: "cada ponto da Selic custa bilhões" — sem número, sem fonte.

## 2. REFORMA APLICADA NO NYC (produção) — 03/09 ~01h BRT

Arquivos: `redator_economia_v4.py` (513→729 linhas), `ciclo_v42.py` (385→514), `publicador_economia_v4.py`. Backups: `/root/v4_labs/codigo/agente_economia/backups_reforma_20260903/` (rollback = restaurar os 3 .bak). Cópias no repo: `Foruns/v42_monitor/nyc_codigo/`.

| # | Conserto | O que faz |
|---|----------|-----------|
| 1 | `escolher_tese()` reescrito | rodízio por tese há mais tempo sem publicar, SÓ com dado fresco (≤45 dias); fim do comercio_sul_sul eterno |
| 2 | Gate de frescor (`_gate_frescor`) | só publica se a tese tem dado mais novo que o já publicado; senão "sem_dado_novo" |
| 3 | Gate anti-repetição de título | Jaccard ≥0,60 contra últimos títulos → regenera 1× e bloqueia |
| 4 | **Validador factual mecânico** (`validar_afirmacoes_numericas`) | todo número do texto tem que nascer do pacote (valor/variação/soma-diferença de mesma moeda); pega número inventado e moeda trocada |
| 5 | Prompt: regras 12–16 | EUR≠US$; mensal≠acumulado 12m; defasado exige "dados até mês/ano" e proíbe "recorde"; proibido eco de fato; título inequivocamente distinto |
| 6 | Pacote enriquecido | `idade_dias`/`defasada`/`moeda` por série |
| 7 | Cascata 6 tentativas | gemini geo-bloqueado no NYC deixava 2 provedores úteis; agora 2 ciclos completos |
| 8 | Legenda limpa | figcaption sem código cru de série (procedência segue no rodapé "Fontes primárias") |
| 9 | Recibo auditável | seção `gates_v42_reforma_20260903` em todo recibo de ciclo |

**Provas ao vivo (03/09 04:02–04:06 UTC):**
- Dry-run `--tema auto`: validador **pegou um "0,16%" inventado** pelo deepseek na tentativa 1 e recusou (o agente antigo teria publicado); rodízio escolheu `inflacao_primaria` (nunca publicada, dado fresco); recibo com gates ✓.
- E2E `--publicar --status-post draft`: post **400299** rascunho no espelho, texto PT impecável (períodos com ano, siglas explicadas, números 100% rastreáveis), gráfico aprovado na auditoria visual, rodapé de fontes completo. Rascunho invisível ao leitor (regra §131 PORTAL LIMPO respeitada).

**Estado:** reforma ATIVA no agente de produção; cron 15:10 UTC segue. Às 12:10 BRT de 03/09 o primeiro ciclo reformado publica de verdade.

## 3. MONITORAMENTO PELOS AGENTES — Vigia V4.2 (robô DSC us65)

**Implementação:** `Foruns/v42_monitor/` (código no repo de propósito — DSN Ideias revisa e propõe melhorias).
- `v42_espelho_watcher.py` — vigia: cron */15 com flock; detecta post novo na cat. 100005 (REST público, sem credencial), roda checagens mecânicas + veredito LLM (deepseek-chat), grava veredito, gera **pedido marcado `IDEIA_PRO_DSNUVEM_IDEIAS` para o DSN Ideias acompanhar** (o marcador que a ronda dele caça), avisa o Miguel no Telegram.
- `v42_checagens.py` — motor mecânico: números × rodapé "Fontes primárias" (valor/variação/soma-diferença, 2 formatos de rodapé), moeda trocada, eco de título (Jaccard), defasado como corrente. Limitação documentada: variação % não vem no rodapé → julgada pelo veredito LLM (o NYC valida % na geração com o pacote completo).
- Estado/telemetria/logs: `/root/agent_data/v42_monitor/` (fora do repo). Telemetria por chamada LLM (tokens+custo) — regra DSC-052 ✓.
- MEMORIA_VIVA.md no diretório (por que existe · objetivo · canal) — DSC-052 ✓.

**Auditoria retroativa (prova de bancada, 03/09 ~01:3x BRT):** o motor + LLM reprocessaram os 8 posts e **acharam sozinhos os defeitos reais**: moeda US$×euro em 400178 e 400209; título duplicado 400265≈400178 (Jaccard 1,00); mensal×acumulado em 400183/400265; GACC de fevereiro sem aviso de defasamento. Vereditos: 400158 OK nota 10; demais ATENÇÃO notas 6–8 (consistente com a auditoria manual). Zero falso positivo após calibração. Arquivos em `Foruns/v42_monitor/vereditos/`.

**Fluxo contínuo a partir de agora:** V4.2 publica → vigia detecta (≤15 min) → checagem mecânica + veredito LLM → veredito no repo + **pedido ao DSN Ideias** (o "cafezinho ideias acompanhar e ver se ele tá fazendo alucinação ou está indo bem", na letra da ordem) + Telegram pro Miguel.

## 4. PENDÊNCIAS / PRÓXIMOS PASSOS

1. **DSN Ideias:** (a) processar o ofício inicial (pedido com marcador em `Foruns/v42_monitor/pedidos/`); (b) adotar os mesmos gates no código da FASE TESTE do V4.2 Investimento (DSC-051) — validador factual, rodízio de tese, gate de frescor e anti-eco valem para qualquer vertical; (c) revisar `v42_checagens.py` e propor melhorias.
2. **ZM:** registrar a reforma nos registros que mantém; validar se o gate de título deve subir para o V4.1 geral (título EMU-2 já vigora — este complementa).
3. **Miguel:** o rascunho 400299 está no espelho para apreciação (WP admin); se aprovar o estilo, é a régua do pós-reforma. Cron do vigia instalado no us65 (*/15).
4. Primeira publicação reformada: 03/09 12:10 BRT (ciclo automático) — o vigia auditará e o Ideias opina.

— ZCode/GLM-5.3 · DSH us65 · 20260903 ~01:4x BRT

---

## ADENDO 1 — 03/09 ~02:1x BRT: REGRA DE TESTE NO ESPELHO (ordem do Miguel)

"Teste no espelho pode, mas teste REALISTA — nunca 'TESTE' no título — e teste visível NÃO PODE FICAR, nem no espelho. Não é pra acostumar mal."

**Aplicado imediatamente:** rascunho de demonstração 400299 + mídia 400298 APAGADOS do espelho (wp post delete --force, cache flushed, verificação 404). Artefato zero.

**Regra registrada (vale para o V4.2 e qualquer vertical que teste no espelho):**
1. Teste de publicação no espelho: SEMPRE status draft (nunca publish) — §131.
2. Conteúdo REALISTA: título real, dado real, gráfico real — jamais "teste"/"TESTE" em título, slug ou imagem.
3. **Ao final do teste: APAGAR o post e a mídia (--force) + flush de cache + verificação.** Rascunho não fica acumulado "para ver depois".
4. Se o resultado merece apreciação do Miguel, mostrar PRINT/EXCERTO no registro (fórum/veredito), não o post em si.

*(O teste de 03/09 cumpriu 1 e 2; faltava o 3 — corrigido nesta data. O texto integral do rascunho está preservado no recibo do ciclo no NYC e no veredito 400158/400299 do vigia... exceto do 400299 que nunca foi público — o recibo NYC `gerados/ciclos/ciclo_v42_20260903_040612.json` guarda tudo.)*

**RESTAURO DS-N Chefe 04:3x 03/09:** o sync d417f8d15 (04:22) comeu este ADENDO 1 — reanexo verbatim do estado d417f8d15^ (ordem do Miguel preservada).
