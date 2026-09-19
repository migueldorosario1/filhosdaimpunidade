# 🧠 Memória — Mapa da arquitetura de publicação + bloco TECNOLOGIA (log técnico)

```yaml
tipo: MEMORIA (Tema Duplo com forum_mapa_arquitetura_publicacao_20260825.md)
autor: ZCode/GLM-5.3
data: 2026-08-25 12:25 BRT
missao: tripla (mapa + mistério Tecnologia + ronda loops), ordem Miguel 25/08 ~12:10
restricao: leitura-only em produção; escrita só Cérebro; FAROL/painel_cctv_v6.py intocados
```

## Comandos e provas (trilha de auditoria)

### Mapa
1. `ssh nyc 'crontab -l'` — 105 linhas comentadas + ativas. Ativas relevantes: v41_ciclo (25/35/45/55 */2 por vertical), coletas V4 por vertical (com `# V4_DESLIGADO_20260824` INLINE — continuam rodando; prova `ciencia_cron.log` run 25/08 14:40 UTC), repetidor estatal `7 */2`, YouTube `0 11,17` UTC, temáticos `0 12,18`, tendencias intake `*/30`, indexador `*/30`, tribunal `23:30`, promote_estatal PAUSADO, maestro PAUSADO 19/07.
2. `systemctl list-timers` NYC — nenhum publicador (só sistema). Único crontab: root.
3. `ssh tencent 'crontab -l'` — só telemetria/painel/FAROL (intocados).
4. `ssh root@159.89.185.209 'crontab -l'` — Rio Carta/Cícero: `cicero_remote_publish.sh 23 *`, coleta rotativa 0,30 com janelas.
5. `ssh cafezinho-cm` — `command_denied` até para `echo` (whitelist rígida) → CM mapeado pelos fóruns.
6. `/root/v4_labs/codigo/v41_ciclo.py` — docstring "Nunca publica (publicação = CM/AGY)"; linha 366 `_patch_v41["categories"] = [30, 2403]` sob `if a.vertical == "ciencia"` (diretriz Miguel 24/08 "ciência é a tecnologia").
7. `/root/v4_vertical_draft_worker.py` — cfg category_ids: ciencia `[735,30,5008]`, economia `[43]`, geopolitica `[5003]`, nacional `[22]`; `enforce_draft_taxonomy` confirma cats no draft.
8. `cat /root/agente_repetidor_estatal.py` (head) — filosofia Opção D, auditor veto-only threshold 40, publish direto.
9. Fóruns: `MOTOR_V5.md` → aponta `diretrizes_coleta_curadoria_frescor_v5.md` (motor V5/AGY); `forum_auditoria_gasto_openai_v4_superproducao_20260824.md` linha 52 — pipeline canônico "…rascunho 4.1 → 3º checador (libera/retém) → publicação CM/AGY".

### Mistério Tecnologia (provas numéricas)
1. Banco `ciencia_tecnologia_ia.sqlite3` (python sqlite3, CLI indisponível): candidates TOTAL drafted=134, editorial_blocked=12, new=1; últimos 3d por collected_at: 22/08 drafted=1, 24/08 new=1. `draft_events`: último draft_confirmed V4 = 22/08 (267033); repairs falhando 521/503/500 (19-21/08).
2. `/root/v4_labs/dados/v41_ciclo/2026082[2-5]*.json` (script /tmp/q3.py): ciencia 16 rascunhos (22/08: 267129,267138 · 23/08: 267165,267189,267212,267232,267256,267262 · 24/08: 267407,267441,267450,267486,267503,267512,267524 · 25/08: 267577) + 3 redator_falhou + sem_tese/bloqueios.
3. WP (`wp db query`, prefixo `wp_`, path `/var/www/ocafezinho`):
   - term map: 30→tax 31 (Tecnologia 4916), 735→tax 740 (Ciência 1152), 5008 (IA 626), 2403 (Redação 37573), 5003 (Geopolítica 6124), 43 (Economia), 19936 INEXISTENTE.
   - Publicados cat 30 desde 22/08: 11 (IDs 267033,267407,267411,267441,267467,267486,267512,267524,267577,267597,267615) — 10 V4.1 autor 5470 (Redator); 267615 autor 5780 (redator2) sem meta v4; 267411/267467 criados pelo ciclo GEOPOLITICA; 267597 pelo ECONOMIA (cross-cat por conteúdo).
   - Status dos 16 ciencia: 10 publish, 6 draft (267129,267138,267165,267232,267256,267262 — todos 22-23/08 pré-patch, cat só 2403; 3 = variantes dedup Brasil-China IA).
   - Cats dos publicados ciencia: 267189/267212 = SÓ 2403 (invisíveis); 267450/267503 = 2403+5003 (bloco Geopolítica); 267407/267441/267486/267512/267524 = 30,43,2403 (elegíveis a Economia ANTES na home → canibalizados); 267577 = 30,2403 (limpo).
   - drafts_v41 (post_status=draft com meta _v4_versao=4.1): 52.
4. Tema `ocafezinho-portal/front-page.php`: bloco Tecnologia `category__in [19936,735,30,5008]`, `category__not_in [28,20751,20699,1271,1426]`, `post__not_in $excludes` (ordem blocos: Nacional→Geo→Economia→Coluna→Regional→Tecnologia); 1 hero + 5 cards.
5. Conta final: 16 gerados → 10 publicados → 6 com cat do bloco → <6 exibidos após excludes. 23/08 = dia ZERO no bloco (2 posts saíram sem cat editorial).

### Ronda
- `canal_trindade.md` tail: AGY rondas 22-25 (23/08) slots ~30min; ZM-20260824-012/013/014 emendas 8/9/10; ZM-20260825-016 convocação publicadores (hoje 10:48) — item 2 já manda preservar cat Tecnologia.
- `inbox_trindade/{claude,codex,zcode}.md` tails: auditor de títulos diário; ticket HOLD × esteira imagens; pings ponte.
- `forum_v4_labs_subida_pipeline_llm_tudo_20260822.md` adendos 123-134 (hoje): 22 publicadas até 11:52, slots 30min, anti-repetição barrou OpenAI ciencia 2×, adendo 130 (sumiço por cat órfã), adendo 133 (V4.1 Tendências não existe).
- `proposta_v41_cinco_gates_packaging_20260823.md` — 5 gates (Claude Laura).
- `log/loop_codex_miguel/last_message.md` — Codex em HOLD desde 19/08.
- ESCRITA: `inbox_trindade/de_zcode.md` CRIADO (ZM-20260825-018) — pergunta sobre sabedoria não-registrada; respostas futuras consolidar no fórum.

## Riscos/observações operacionais
- Consultas SQL no WP deste ocafezinho: SEMPRE juntar `wp_terms` por `term_id` (nunca filtrar por `term_taxonomy_id` direto).
- Mudar o tema (bloco Tecnologia) exige cuidado: 19936 é referência morta — remover requer revisão (não fiz, leitura-only).
- A anotação `# V4_DESLIGADO_20260824` inline não desativa cron; se um dia quiser parar a coleta V4 de vez, comentar a LINHA INTEIRA.
- Zero mudanças em produção nesta missão (nenhum arquivo de servidor foi alterado; backups N/A).

— ZCode/GLM-5.3 · 25/08/2026 12:25 BRT
