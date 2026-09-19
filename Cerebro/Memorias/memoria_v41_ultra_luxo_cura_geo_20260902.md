# MEMÓRIA — V4.1 ultra-luxo + cura geo/tec + manual v2.1.0 (02/09/2026)

> Log técnico completo do sprint. Fórum-irmão:
> `Foruns/forum_v41_ultra_luxo_cura_geo_20260902.md`. Sessão ZCode/Qwen 3.8 (Dell).

## 1. Ultra-luxo (NYC `/root/v4_labs/`)

Arquivos tocados (todos com backup):
- `config/llm_ratings.json` — +`gpt-5.6-sol` (qualidade 5, ativo, $4/$20,
  reasoning true, exige_temperature_01 false, funcoes: redacao/revisao/
  auditoria/fact_check/perifericos/curadoria). Luna mantida (fora da rota).
- `contratos/v4_pricing_llm_v1.json` — +sol {openai,4,20}; **bug corrigido**:
  claude-fable-5 provider openai→anthropic.
- `config/llm_providers.json` — fallback luxo openai = [sol, gpt-5.5, 5.4, 5].
- `contratos/v4_rotas_llm_limpas_v1.json` — contextos novos:
  `v4_ultra_luxo_redacao` (sol → gpt-5.5 → opus → gemini-3.6-flash →
  deepseek-v4-pro → moonshot-v1-32k) e `v4_ultra_luxo_redacao_nacional`
  (fable-5 → sol → gpt-5.5 → opus → cauda).
- `contratos/mapa_v4_contexto_llm.json` — redação de todas as editorias →
  ultra_luxo; nacional → ultra_luxo_nacional.
- `dados/ultra_luxo.json` — knob `{ativo, geral: gpt-5.6-sol, nacional:
  claude-fable-5, fallback_padrao: gpt-5.5}`.
- `scripts/aplica_ultra_luxo.py` (chmod 755) — `--status|--geral X --nacional Y|
  --desligar`; valida modelo ativo no ratings; backup datado antes de reconstruir.
- `scripts/monitor_ultra_luxo.py` — relatório 1/1h (knob, artefatos ≤70min,
  chamadas/custo frontier na janela e no dia, alertas >$1,5/h, >40 chamadas,
  geo >6h sem post).
- `codigo/test_contracts.py` (.bak_pre_sol_20260902) — 2 asserts atualizados
  (condicional ultra-luxo ON/OFF; 5 tiers no super luxo c/ moonshot_luxo).
  Dívida pré-existente documentada: assert `"deepseek-v4-pro" not in
  operational_code` falha por COMENTÁRIO no runtime (23/08) — não tocado.

Lógica do router provada: `_fila(item)` ordena por (posição na rota, custo
DESC dentro do tier) — ordem da rota = fila; tier é metadado. Por isso cada
modelo em tier próprio.

Provas: chave sol 200 OK ao vivo; dry-run 12/12; post 268674 (digital,
18:08 UTC, sol, $0,0228); decisions em `agent_data/v4/llm_decisions/
decisions_20260902.jsonl`.

## 2. Cura geopolítica/tecnologia (`codigo/v41_ciclo.py`, .bak_pre_cura_geo_20260902)

1. `_tese_frontier(env, system, user)` — modelo do env `V4_TESE_FRONTIER_MODEL`
   ou knob `geral` (default sol); POST api.openai.com, `max_completion_tokens`
   2500, SEM temperature (família gpt-5 rejeita), timeout 240; qualquer falha →
   None → cadeia verificadora (GLM→DeepSeek→Moonshot).
2. `_tese_dinamica` — system novo (editor-chefe de esquerda, soberania, direito
   internacional, multipolaridade) + regra de guerra existente + **REGRA PARA
   PAUTAS AFIRMATIVAS** (BRICS/SCO/integração/Sul Global sem vilão; protagonista
   constrói; nunca inventar vilão onde não há conflito); contexto = linha
   editorial viva + manual de escrita ("a linha editorial prevalece sobre tudo").
3. Dedup: item sem post_id que falhou só retorna à fila após 6h (V41_FILA_SEM_CLOG).
4. Motivo anti-repetição movido p/ `else:` (V41_MOTIVO_HONESTO) — juiz visível.

Anatomia da seca (diagnóstico): mesmo item SCO falhando de hora em hora (tese
exigia vilão; pauta afirmativa não tem) + dedup só excluía post_id (item
falho entupia a fila) + motivo sobrescrito escondia rejeição do juiz. Coleta
sempre foi rica (28 feeds geo).

Coleta reforçada: `/root/coletor.py` (.bak_pre_temas_ia_20260902) +3 Brave
queries geo/IA/BRICS; `dados/temas_prioritarios_geo.txt` (.bak) +23 keywords.

Prova ao vivo (pré-patch 14:58 BRT mostrava a doença; pós-patch): pauta SCO
passou com `vilao:""` e herói Sitharaman; pauta de guerra passou com vilão
"United States Navy". Teste de resiliência: modelo inválido na tese → fallback
rodou 108s, retornou llm_sem_tese_valida (não quebra; degrada).

## 3. Manual v2.1.0 (regras ditatoriais → diretrizes editoriais)

- Oficial `Cerebro/Estilo/MANUAL_DE_ESCRITA.md` (.bak_pre_diretrizes_20260902)
  v2.0.0→v2.1.0: +seção "1. Princípios (o resto é ofício)" (5 princípios);
  §6 pontuação suavizada (ponto e vírgula/dois-pontos/travessão/conectivo
  inicial/parênteses = preferência com justificativa); checklist item 2
  (metalinguagem+frase vazia seguem ZERO; resto é régua de preferência);
  apêndice = "auditoria, não bloqueio".
- Portal NYC `dados/MANUAL_DE_ESCRITA_PORTAL.md` (.bak_pre_diretrizes_20260902)
  v2.0.1-P→v2.1.0-P: mesmas mudanças + §8 "parágrafo curto é a régua" (fim do
  "máximo duas frases" mecânico). Patch 7/7 aplicado via
  `/root/patch_manual_portal.py`; 1ª tentativa falhou em 3 trechos (header real
  tem 2 blocos de citação + quebra de linha diferente) — fail-safe NÃO gravou
  nada; 2ª tentativa OK, seção 1 conferida no arquivo.

## 4. Monitoramento e avisos

- Automação ZCode `automation-d6095d3d-...` cron `15 * * * *`: ssh nyc →
  monitor → Telegram (🟢/🟠/🔴, assinado "— ZCode/Qwen 3.8", read-only).
- ZM-20260902-043 em: `Foruns/ponte_laura_completa/de_dell.md`,
  `Foruns/inbox_trindade/claude.md`, `Foruns/canal_trindade.md`,
  `Foruns/ponte_zm_dsc/de_zm.md` (todos grep-verificados).
- 2 auditorias na MEMORIA_VIVA do `cerebro_dsn/dsn_ideias/` (ultra-luxo:
  "algo quebra a produção se o frontier falhar?"; cura geo: "regra afirmativa
  gera viés de repetição? fail-closed intacto?").
- Linha editorial viva espelhada nos mini-cérebros R1/R2/Chefe.

## 5. Rollback

`ROLLBACK_INDEX.md` (NYC): V41_ULTRA_LUXO_SOL (`aplica_ultra_luxo.py --desligar`)
e V41_CURA_GEO_TEC (3 .bak nomeados). ATUALIZACOES: conflitos de merge limpos
(2 blocos, lado nyc/main vazio; HEAD preservado) antes deste registro.

## 6. Pendências

1. Prova do ciclo geo 18:55 UTC (1º pós-cura).
2. Auditorias DSN Ideias + opinião CL/CM.
3. Miguel mede gasto do ultra-luxo → decisão de voltar ao super luxo.
4. V4.2 (depois, por ordem do Miguel).
5. Verificador de estilo do pipeline ainda usa régua antiga em código
   (verifica_estilo.py) — manual agora é auditoria, não bloqueio; alinhar se
   a auditoria do DSC Ideias recomendar.

## 7. Telemetria detalhada dos LLMs do V4.1 (02/09 ~16:3x BRT — ordem do Miguel)

**Ordem:** "importante manter telemetria detalhada de todos os llms do v4.1".

### Arquivos (NYC)
- `/root/telemetria_api.py` — PATCH `_extrair_usage_response`: agora lê
  anthropic `input_tokens`/`output_tokens`, gemini `usageMetadata`
  (`promptTokenCount`/`candidatesTokenCount`) além do padrão
  `prompt_tokens`/`completion_tokens`. Backup `.bak_pre_extrator_20260902`.
  Marcador V41_EXTRATOR_20260902.
- `/root/v4_labs/codigo/telemetria_v41.py` — NOVO. `registrar(site, provider,
  model, status, tokens_in, tokens_out, duration_ms, editoria, ref,
  error_class, extra) -> bool` (fail-never, fcntl lock, JSONL
  `agent_data/v4/llm_calls/calls_YYYYMMDD.jsonl` data BRT; override
  `V4_TELEMETRIA_DIR` p/ teste) + `chamadas_dia()`.
- `/root/v4_labs/codigo/v41_ciclo.py` — PATCH (backup
  `.bak_pre_telemetria_20260902`): import `_tel` (fallback no-op);
  `_tese_frontier` registra site=tese_frontier (ok/sem_json/erro + tokens);
  FC: `_FC_PROV` (sonnet→anthropic/claude-sonnet-4-6, gemini→google/
  gemini-3.6-flash, gpt→openai/gpt-5.5) + cada função registra site=fc com
  uso real do provedor; exceções da cascata registram erro; call-sites do
  verificador com `site="tese_fallback"` e `site="juiz"`.
- `/root/v4_vertical_draft_worker.py` — PATCH (mesmo backup): import `_tel`
  com sys.path `/root/v4_labs`; `_verifier_llm_json(..., site="verificador")`;
  os 3 blocos (GLM/DeepSeek/Moonshot) registram ok (tokens do usage),
  sem_json, http_N e erro (com error_class e duração).
- `/root/v4_labs/scripts/relatorio_llms_v41.py` — NOVO. Consolidado diário:
  banco_custos (agentes `v4_1_*` por modelo + subtotal + contexto da casa),
  llm_calls por site/modela/status (falhas incluídas), decisions por modelo,
  drafts por modelo selecionado. `--dia YYYY-MM-DD` e `--compacto`.
- `/root/v4_labs/scripts/monitor_ultra_luxo.py` — PATCH (backup
  `.bak_pre_tel_20260902`): seção 5 chama o relatório `--compacto` via
  subprocess (timeout 30s, falha → "TEL: relatório indisponível"), linhas
  `TEL:` antes dos alertas → flui no Telegram :15 (automação existente).

### Provas
- 11/11 substituições do wiring aplicadas de primeira (fail-safe por contagem).
- py_compile 4/4 (telemetria_api, v41_ciclo, worker, relatorio, monitor).
- Smoke do registrar com `V4_TELEMETRIA_DIR=/tmp/tel_smoke` → OK, campo completo.
- Relatório real 02/09: V4.1 178 ch/$2,58 (glm-5-turbo 110×/$0,37 ·
  deepseek-v4-pro 48×/$0,29 · gpt-5.5 11×/$1,74 · gpt-5.6-sol 8×/$0,18);
  outros agentes da casa 56 ch/$0,80; router gpt-5.5 15× + sol 3×; 15 drafts.
- Monitor com seção TEL imprimindo OK.

### Comportamento garantido
- Zero mudança de comportamento na produção: toda instrumentação é
  fail-open/fail-never (exceção engolida, fallback no-op).
- Falhas (sem_json/http_N/erro) e subsistema agora visíveis — antes só
  chamadas com tokens>0 apareciam, e tudo do ciclo era "ciclo session:POST".

### Rollback
`ROLLBACK_INDEX.md` NYC seção V41_TELEMETRIA_DETALHADA_20260902: cp dos 4 .baks
+ rm dos 2 arquivos novos.

### Pendência adicionada
6. Verificar no próximo ciclo (19:35 UTC economia / 19:55 UTC geo) se o
   `llm_calls` ganhou entradas reais dos subsistemas.

> **Atualização ~17:0x BRT (item 6 resolvido):** smoke controlado registrado
> (site=smoke_wiring, depois limpo) + binding do registrar real confirmado nos
> 2 módulos + **5 chamadas GLM reais de produção** já etiquetadas no
> relatório (20:00 UTC). Ciclo geo 19:55 UTC saiu cedo por fila vazia
> (`todas_pautas_ja_rascunhadas_24h`); etiquetas tese_frontier/fc/juiz
> aparecem no próximo ciclo com pauta nova.

## 8. Autocura da fila de pautas (~18:3x BRT) — ordem do Miguel (REPOSTO 21:3x após clobber de escrita paralela)

### Diagnóstico (fila vazia não era bug, era fome estrutural)
- Fila = sqlite por vertical `/root/agent_data/v4_verticals/*.sqlite3`
  (tabela `candidates`: status new/drafted + score + collected_at).
- Suprimento = crons de coleta+intake em BURSTS: geo 1/1h, tec 2/1h, eco 1/4h,
  pol 1/6h, cul 1/4h, amb/esp/sad/dig 3-4x/dia. Entre bursts o ciclo (1/1h-2h)
  consome + dedupe (item_key[:16] de artefatos c/ post_id <24h ou falha <6h)
  bloqueia re-tentativa → saída `todas_pautas_ja_rascunhadas_24h` → monitor
  mostrava "fila vazia". Prova: janela 19:1x→20:2x UTC se resolveu sozinha
  com os intakes de esporte (19:15) e ciência (:40).

### Cura — guardião `scripts/autocura_fila_v41.py` (NYC)
- Cron `*/20 * * * *` c/ flock `/tmp/v41_autocura_fila.lock` (backup
  `/root/crontab.bak_pre_autocura_fila_20260902`).
- `VERTS`: 9 verticais → (banco, grupo_coletor, nome_intake, frescor_h, lock),
  mesma tabela do ciclo. `SOFT` = saude/esporte/meio_ambiente/digital (lêem
  'new' frescas; as demais lêem drafted+new).
- `contagem_tentaveis()`: réplica exata da régua do ciclo — frescor por
  vertical + dedupe de `_usados` (artefatos `dados/v41_ciclo/*.json` <24h c/
  post_id + `falhas_v41.jsonl` <6h, chave `item_key[:16]`). Fail-open:
  ilegível → -1.
- `reforcar_coleta(vertical)`: roda `flock -n <lock> bash -lc 'cd /root && .
  /root/chaves.sh && coletor <grupo>; intake <vertical>'` (timeout 420s) —
  mesmos comandos/flocks dos crons. Mínimo 25 min entre reforços da mesma
  vertical (estado `agent_data/v4/autocura_fila/estado.json`).
- Incidentes: ainda 0 tentáveis após reforço → JSONL `incidentes.jsonl` +
  alerta no monitor (vazio legítimo = visível, nunca silencioso).
- Flags: `--check` (só conta), `--compacto` (1 linha p/ monitor), `--min N`.
  Main inteiro fail-open (erro → log + exit 0).

### Monitor
- `scripts/monitor_ultra_luxo.py` ganhou seção FILA (backup
  `.bak_pre_fila_20260902`): subprocess `autocura_fila_v41.py --check
  --compacto`, prefixo `FILA:`; contagem <2 em alguma vertical vira alerta.

### Provas
- `--check` nas 9 verticais; corrida completa com fila cheia = 0 curas;
  caminho de cura REAL provado: `reforcar_coleta("cultura")` → coleta+intake
  rc=0; py_compile OK; crontab grep=1.

### Rollback
`ROLLBACK_INDEX.md` NYC seção V41_AUTOCURA_FILA_20260902.

## 9. Conserto das falhas sem_json (~21:2x BRT) — V41_JSONFIX_20260902

### Evidência (llm_calls 02/09)
- juiz zhipu glm-5-turbo sem_json 18:43 BRT — duração 50,7s.
- verificador zhipu glm-5-turbo sem_json 20:31 BRT — 52,9s.
- verificador deepseek-v4-pro sem_json 20:31 BRT — 43,5s.
- verificador moonshot kimi-k2.5 http_429 20:31 BRT — 0,4s.
- Durações 43-53s ≈ geração completa do teto max_tokens=2500 → JSON
  truncado no meio. 429 = rate limit transitório (3ª perna; só chamada
  porque as duas primeiras falharam).

### Mudança (único arquivo)
`/root/v4_vertical_draft_worker.py` (backup `.bak_pre_jsonfix_20260902`):
- Helper `_extrair_primeiro_json(content)`: (a) regex gulosa `\{.*\}` primeiro
  — se parsear, comportamento 100% igual ao antigo; (b) senão, varredura por
  chaves balanceadas (c/ estado de string/escape) coletando TODOS os objetos
  válidos e retornando o ÚLTIMO (modelo que ecoa exemplo antes do veredito).
- Substituições fail-safe por contagem (3/3 cada): `m = re.search(...)` →
  `_cand = _extrair_primeiro_json(content)`; `if m:` → `if _cand:`;
  `json.loads(m.group(0))` → `json.loads(_cand)`.
- `"max_tokens": 2500` → `4000` nas 3 pernas.
- v41_ciclo.py NÃO precisou de mudança: chama `v4w._verifier_llm_json`
  (linhas 152 e 476) — juiz e tese_fallback cobertos pela mesma cura.

### Testes
py_compile OK; `/tmp/teste_jsonfix.py` (exec do helper via ast, sem importar
o módulo pesado) → 6/6: json puro · fence+prosa com chave depois · truncado
(None) · eco de exemplo + veredito (pega o último) · chaves dentro de string ·
vazio (None).

### Rollback
ROLLBACK_INDEX NYC seção V41_JSONFIX_20260902 (1 cp do .bak).

### Acompanhamento
Próximos ciclos: telemetria deve mostrar sem_json zerado; se persistir, o
registro de duração indica se ainda é truncamento (aí sobe max_tokens de novo)
ou outro modo (helper permite capturar snippet depois se precisar).

## 10. Robôs coletores de 15 min (~22:3x BRT) — V41_ROBOS_COLETORES_20260902

### Ordem e arquitetura
Miguel ~22:1x: falta de notícia; criar robôs coletores rodando de 15 em 15
minutos para todas as verticais; arquitetura a meu critério. Decisão: UM robô
com módulo por vertical (não N scripts). Config viva em
`/root/v4_labs/dados/robos_coletores.json` (ativo geral + por vertical:
grupo/intake/cadencia_min/ligado). Padrão: pol/geo 15, eco/tec/esp 30, dig 45,
sad/amb/cul 60 min.

### Diagnóstico da fome (causa raça)
`/root/coletor.py` tem ESTOQUE_TTL {politica:6h, geopolitica:3h, tecnologia:6h}
e pula recoleta com estoque válido; crons legados ativos: pol `20 */6`, eco
`35 */4`, cul `5 */4`, geo `0 *`, tec `10,40 *`, sad/amb/esp 3-4×/dia (todos
com trailing `# V4_DESLIGADO_20260824` mas ATIVOS — trailing é só comentário).
Resultado: pol só coletava 4×/dia → mesma pauta repetida 7×/12h (caso do
fable). Robô usa `--forcar` para ignorar o TTL.

### Implementação (NYC)
- `/root/v4_labs/scripts/robos_coletores_v41.py` (novo; py_compile OK):
  ronda cada vertical vencida pela cadência; comando por vertical =
  `flock -n /tmp/v4_<v>.lock bash -lc 'cd /root && . /root/chaves.sh &&
  export BRAVE_API_KEY= && timeout 540 python3 /root/coletor.py <grupo>
  --forcar >> <vertical>_cron.log; python3 /root/v4_vertical_intake.py
  <intake> >> <vertical>_cron.log'` (MESMOS locks do legado/guardião;
  rc=1 do flock = lock ocupado → skip fail-open, sem atualizar estado).
- Sem Brave nas corridas do robô: `export BRAVE_API_KEY=` após o source do
  chaves.sh; coletor lê os.environ → collect_brave retorna [] (protege cota;
  profundidade segue nos crons legados).
- Estado: `agent_data/v4/robos_coletores/{estado.json, robos.log,
  entregas.jsonl, cron.log}`; entrega registra rc/dur_s/novos (candidatas com
  collected_at >= início da corrida) por vertical.
- Cron NYC: `*/15 * * * * /usr/bin/flock -n /tmp/v41_robos_coletores.lock
  /root/venv/bin/python3 /root/v4_labs/scripts/robos_coletores_v41.py >>
  .../cron.log 2>&1 # V41_ROBOS_COLETORES_20260902` (flock próprio impede
  empilhamento de rondas; backup crontab:
  /root/crontab.bak_pre_robos_coletores_20260902.txt).

### Provas (02/09 noite)
- `coletor.py pol --forcar` manual sem Brave: 145s, 18 extrações ok, estoque
  salvo; intake politica: fila nacional 302→319 status='new' (+17).
- `robos_coletores_v41.py --vertical geopolitica`: rc=0, 263,8s, novos=11
  (entregas.jsonl 2026-09-03T01:27:47+00:00).
- Varredura inicial das 9 verticais lançada ~22:32 BRT (nohup PID 3346043).

### Riscos vigiados
- Brave quota preservada (robô não usa); Google News RSS e feeds sob circuito
  breaker + fontes_metrics do coletor (alerta de fonte silenciosa já existe).
- Pior caso de ronda cheia ≈ 25-30 min (9 coletas sequenciais) — cron */15
  seguinte pula no flock; cadências escalonadas evitam isso no regime normal.
- ROLLBACK_INDEX NYC seção V41_ROBOS_COLETORES_20260902: remover 1 linha de
  crontab ou ativo=false no JSON. Robô só insere status='new' na fila existente.

## 11. Integração curador + multiidioma (~23:5x BRT) — V41_CURADOR_MULTIIDIOMA_20260903

### Ordem (Miguel ~23:2x BRT)
"Tem que ter nota... nota de frescor... integrar com o sistema de curadoria
do V4.1... as notícias têm que vir com tamanho decente... não pode ter
alucinação nenhuma... bota ele para fazer pesquisa em todas as línguas —
alemão, chinês, coreano, japonês... um robô vai dar conta de tudo?... cuida
pra não quebrar a lógica do V4.1 (não é só notícia, é criação de tese)... o
V4.1 está lendo diretrizes, inclusive as políticas? e o manual novo?"

### Mapeamento da seleção do v41_ciclo (linhas 330-400)
- Hard verticals (nac/eco/geo/cie/cul): 6 'drafted' frescas + 3 SOBRAS 'new'
  ORDER BY score ASC (F1b: institucionais que o worker legado não pega logo).
- Soft (sad/esp/amb/dig): 9 'new' ORDER BY collected_at DESC.
- Janela de frescor por vertical: 24h hard, 48h (cie/sad/esp/amb/dig), 72h cul
  (V41_FRESCOR_20260828). Dedupe próprio: rascunhada <24h ou falhou <6h não
  roda (V41_FILA_SEM_CLOG). Freio de estoque >80 itens.
- Tese dinâmica `_tese_dinamica`: frontier lê NOTÍCIA (texto[:5000]) + linha
  editorial + MANUAL (V41_TESE_FRONTIER_20260902); âncoras devem existir
  LITERALMENTE no texto ou a tese reprova (fail-closed). Sem tese aprovada =
  status sem_tese_ancorada_nao_escreve.
- Briefing do redator: instrucoes 21.863 chars com viv = linha (3.914c) +
  nucleo (1.311c) + manual portal (11.284c) + diretriz viva (4.200c) =
  20.709c + cláusula "a LINHA EDITORIAL prevalece sobre tudo" (prova real no
  briefing_execucao_v41.json).

### Implementação (NYC, tudo com backup)
- `scripts/robos_coletores_v41.py` v2 (backup .bak_pre_curador_multiidioma_20260903):
  - MÓDULO CURADOR `curar_fila`: nota_frescor por idade do fato (≤3h=10,
    ≤6h=9, ≤12h=7, ≤24h=5, ≤36h=3, ≤48h=2, >48h=1; sem data=4); nota_importancia
    = 3 + 1.2×hits keywords da curadoria da casa (foco_pauta.json +
    curadoria_diaria.json + curadoria_geral.json, extraídas em runtime) +
    0.8×hits LEXICO_GEO (guerra/sanções/BRICS/OTAN/petróleo/chips/IA...),
    cap 10; nota_texto por tamanho (≥2000=10, ≥1200=8, ≥800=6, ≥500=4,
    ≥300=2, <300=0); nota_curadoria = 0.4f + 0.4i + 0.2t. Gravadas em
    raw_json["curadoria_v41"] (merge preservando chaves; UPDATE por item_key;
    fail-open por linha; escopo: new+drafted 48h sem a chave, LIMIT 200/vertical).
  - MÓDULO MULTIIDIOMA `coleta_multiidioma`: 19 feeds RSS diretos em 8
    línguas (FEEDS_MULTI; todos sondados vivos do NYC em 02/09: tagesschau/
    DW-de/ZDF · BBC zhongwen/NYT cn · BBC korean/Yonhap en · NHK/BBC ja ·
    Le Monde intl/France24 · TASS/RT ru · BBC mundo/El Mundo intl ·
    Al Jazeera/BBC world/Guardian world); máx 3 itens por feed; requests
    trust_env=False (padrão da casa); trafilatura no HTML final; GATE ≥800
    chars (fininhos descartados e contados); INSERT OR IGNORE candidates
    (item_key sha1[:16] da URL final, source_type='multiidioma',
    source_name='<idioma>:<feed>', score=nota, text_sha256, raw_json com
    idioma/feed/notas); roda sob fcntl.flock NB no MESMO
    /tmp/v4_geopolitica.lock (lock ocupado = skip).
    DESCARTADO c/ diagnóstico: Google News RSS (links /rss/articles/
    criptografados no formato novo; googlenewsdecoder toma 429/captcha do
    IP de datacenter; provado ao vivo) e Bing News RSS (apiclick resolve,
    mas veículos retornam 403 de botwall na extração).
  - Ronda normal agora: multiidioma (cadência 30 min) → verticais vencidas →
    curador após cada vertical. Flags novas: --multiidioma, --curar.
- `dados/robos_coletores.json`: bloco {"multiidioma": {"ligado": true,
  "cadencia_min": 30}}.

### Provas
- py_compile OK. 1ª passada do curador: 555 candidatas com nota em 9 verticais
  (geo 200 · nac 83 · eco 65 · esp 64 · amb 58 · cul 29 · dig 23 · sad 22 ·
  cie 11). Amostras geo: Maduro/US court frescor 10 imp 6.3 txt 10 = 8.5;
  Trump/Israel = 10.0.
- Multiidioma: teste lançado ~23:5x (resultado registrado na linha do tempo).
- Diretriz-prova: briefing_execucao_v41.json instrucoes=21.863 chars, contém
  "DIRETRIZES DA CASA", "LINHA EDITORIAL prevalece sobre tudo", "BRIEFING DA
  CURADORIA"; soma dos 4 arquivos = 20.709 chars (viv ≈ 20.905 com separadores).

### O que NÃO mudou (garantia ao Miguel)
Zero alteração em v41_ciclo.py, v4_vertical_draft_worker.py, tese dinâmica,
FC, intake ou cron legado. O robô só INSERE candidatas e metadata. Notas não
mudam a ordenação atual (score ASC das sobras segue com o score do coletor;
a nota_curadoria vai só no raw_json — auditável e disponível p/ evoluções).
Publicação segue exigindo revisão (gate standby_contrato; só CL/CM).

### Rollback
cp robos_coletores_v41.py.bak_pre_curador_multiidioma_20260903 → script;
remover bloco multiidioma do JSON (ou ligado=false). Notas já gravadas são
inertes (ciclo não lê raw_json).

---

## 12. V41_EQUIPE_NACIONAL_20260903 — equipe de coleta nacional (prospector + coletor direto + curador c/ nota da fonte + enriquecedor)

(REPOSTO ~00:0x de 03/09 após clobber de escrita paralela às 23:57:02/23:57:58 de 02/09 — conteúdo íntegro abaixo, verificado por grep antes do clobber.)

### Ordem (Miguel, voz, 02/09 ~23:1x→23:4x BRT)

Para a vertical nacional: acompanhar Metrópoles, G1, ICL, Revista Fórum, Folha,
Veja etc. e extrair o conteúdo deles OU buscar o conteúdo anunciado em outras
fontes (problema paywall/botwall). Desenho do Miguel: equipe de robôs
especializados — (1) um que só acha RSS que funciona (aposenta mortos, reintegra
os que voltam: "às vezes um não funcionava, mas volta a funcionar"); (2) um que
só coleta dos feeds funcionando; (3) o curador dando NOTA DA FONTE; (4) um que
pega as maiores notas com texto fino, busca na internet e MONTA O MATERIAL
BRUTO. "tudo tem que ser indexado no cérebro"; "as fontes têm que ter a nota da
fonte"; diretrizes respeitadas na redação. Arquitetura delegada ao ZM ("talvez a
sua ideia seja melhor fazer um só").

### Arquitetura escolhida (delegada → decisão ZM)

Os 4 papéis do Miguel viraram módulos 4-6 do robô único
`robos_coletores_v41.py` (1 script, 1 cron */15, cadências internas no config,
mesmos flocks — sem quebrar o V4.1). Razões: ponto único de observação, sem
novos crons, fail-open herdado, rollback de 1 alavanca.

### Implementação (módulos novos no script — backup `.bak_pre_equipe_nacional_20260903`, py_compile OK; local de trabalho `/tmp/robos_coletores_v41_novo.py`)

- **Módulo 4 — PROSPECTOR NACIONAL** (`prospector_nacional(cfg)`, cadência
  30 min): sonda `FEEDS_NACIONAIS` (20 dicts {nome,url}: metropoles ×2, g1 ×2,
  icl ×2, forum, folha ×2, veja, uol, cnn_brasil, poder360, brasil247,
  cartacapital, agencia_brasil, congresso_foco, intercept, bbc_portugues,
  sputnik_brasil). Vivo = status<400 e entradas>0. Estados:
  sondagem/ativo/degradado/aposentado; `seguidos_falha ≥ 6` → aposentado;
  aposentado re-sondado após `retry_aposentado_h=6`. Saúde persistida em
  `dados/feeds_nacionais_saude.json`; transições em `feeds_eventos.jsonl`.
  UA de navegador completo (`UA_NAV`).
- **Módulo 5 — COLETOR NACIONAL DIRETO** (`coleta_nacional_direta(cfg)`,
  cadência 15 min): flock `LOCKS["nacional"]` não-bloqueante (pula se ocupado);
  só feeds "ativo"; máx `max_por_feed=5`; checa `SELECT 1 FROM candidates WHERE
  item_key=?` ANTES de baixar o artigo; `INSERT OR IGNORE` com chave
  `sha1(link)[:16]`; extração trafilatura; `MIN_TEXTO_NAC=300` (fininho não
  entra); <800 marcado `texto_curto`; `source_type='nac_direto'`,
  `source_name`=nome da fonte; meta grava nota_fonte + curadoria_v41 completa.
- **Módulo 6 — ENRIQUECEDOR** (`enriquecer(cfg)`, cadência 30 min, máx 10
  buscas/ronda): `SELECT ... WHERE status='new' AND 24h AND length(text)<800
  AND raw_json LIKE curadoria_v41 AND NOT LIKE enriquecimento_v41 AND score >=
  nota_min(6.0) ORDER BY score DESC LIMIT 10`. Chave Brave lida por regex de
  `/root/chaves.sh` (`_brave_key()`); busca
  `api.search.brave.com/res/v1/web/search` com q=título; até 3 blocos, 1 por
  domínio, cada um ≥300 chars truncado a 3000; monta
  `=== MATERIAL BRUTO ... ===` com `[MATERIAL BRUTO n — domínio | título |
  URL]`; atualiza text_content/text_sha256/score e re-grava curadoria
  (nota_texto/nota_curadoria recomputadas do nf/ni armazenados); sem fonte →
  marca `sem_material:true`; fail-open.

### Tabela FONTE_NOTA (no script, editável — valores iniciais ZM)

forum/icl 9.0 · brasil247/cartacapital 8.5 · agencia_brasil 8.0 ·
intercept/congresso_foco/poder360/metropoles/g1/folha/bbc_portugues 7.5 ·
cnn_brasil/uol/estadao/sputnik_brasil 7.0 · veja 6.5. Fórmula composta NÃO
mudou (0.4 frescor + 0.4 importância + 0.2 texto); nota_fonte vai na meta e no
briefing via raw_json.

### Config (`dados/robos_coletores.json`, backup `.bak_pre_equipe_nacional_20260903`)

Seções novas: `prospector` {ligado, cadencia_min 30, falhas_para_aposentar 6,
retry_aposentado_h 6} · `nacional_direto` {ligado, cadencia_min 15,
max_por_feed 5} · `enriquecedor` {ligado, cadencia_min 30, max_por_ronda 10,
nota_min 6.0, limite_texto 800} + multiidioma existente + 9 verticais intactas.
Flags novas no main: `--prospector`, `--nacional-direto`, `--enriquecer`.
Ordem da ronda: multi → verticais vencidas → prospector → nacional_direto +
curar → enriquecedor. Estado: chaves ultimo_prospector/ultimo_nacional_direto/
ultimo_enriquecedor.

### Provas E2E (NYC, 02/09 ~23:3x→23:5x BRT)

1. Sondagem: **16/20 feeds vivos** (ficam no ciclo de retry: Estadão,
   CartaCapital 403, Agência Brasil 404, ICL 0 entradas, DW pt 0 entradas, 2
   com erro de conexão).
2. 1ª colheita: **+73 candidatas de 13 fontes** (metropoles 10, g1 8, icl 5,
   forum 5, folha 5, veja 5, uol 5, cnn_brasil 5, poder360 5, brasil247 5,
   congresso_foco 5, bbc_portugues 5, sputnik_brasil 5); 1 fininho (<300)
   descartado pela régua.
3. Enriquecedor (teste temporário com limite_texto=2600/max=2, config restaurado
   exatamente depois): "Quaest: Lula 37%×29%" **+8.345 chars**
   (operamundi.uol.com.br / jc.uol.com.br / portaldeprefeitura.com.br, nota→8.8)
   e "Cientista política...Flávio×Lula" **+9.103 chars**
   (grupoportaldenoticias / brasildefato / valor.globo.com, nota→7.2) — todos
   os blocos citados com fonte+URL, ZERO invenção (só texto extraído de página
   real).
4. Fila: nacional 320→393 new (+73); geo 1.134+ (+7 multilíngue na mesma hora).

### O que NÃO mudou (garantias)

Ciclo/tese/redator/FC/publicação intactos. ZERO cron alterado (mesmo */15).
Robô segue só INSERINDO/enriquecendo candidatas — V4.1 RASCUNHO-ONLY;
publicação é da CL (gate standby_contrato MODO CONTRATO). Diretrizes lidas no
briefing (prova 21.863c c/ os 4 documentos, adendo §10).

### Rollback

`V41_EQUIPE_NACIONAL_20260903` no `/root/v4_labs/ROLLBACK_INDEX.md`:
`ligado=false` nas 3 seções do config (prospector/nacional_direto/enriquecedor);
backups `.bak_pre_equipe_nacional_20260903` (script + config); crons não mudam.

### Riscos observados

Paywall Folha/Veja: trafilatura pega o que o feed entrega; quando fino, o
enriquecedor cobre via busca. Brave é gargalo (máx 10/30min) — suficiente para
a cadência atual. Aposentadoria de feed é conservadora (6 falhas seguidas) para
não matar fonte que só oscilou.
