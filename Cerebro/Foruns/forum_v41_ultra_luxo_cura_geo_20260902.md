# FÓRUM — V4.1 ULTRA-LUXO (gpt-5.6-sol + fable-5) + CURA GEOPOLÍTICA/TECNOLOGIA + MANUAL v2.1.0

> 02/09/2026 · sessão ZCode/Qwen 3.8 (Dell) · ref ponte ZM-20260902-043
> Ordem do Miguel (falas empilhadas 13:5x→15:5x BRT): fim do debate, "pode colocar
> para funcionar"; recuperar diretrizes políticas (Irã/China/Sul Global); verticais
> como "jornalista de verdade, humano, de esquerda"; manual completo sem ambiguidade
> mas "princípios, diretrizes editoriais, não regras ditatoriais"; "capricha no
> Geopolítica... e o Tecnologia"; ultra-luxo como EXPERIÊNCIA de gasto c/ troca
> simples de modelo ("mudei de ideia: gpt-5.6-sol, não luna; fable-5 pro nacional").

## Decisões (resumo)

1. **Ultra-luxo NO AR** (NYC `/root/v4_labs/`): geral = `gpt-5.6-sol` (OpenAI
   frontier $4/$20 promo até 21/11); nacional = `claude-fable-5` ($10/$50) com
   sol de fallback imediato. Contextos novos `v4_ultra_luxo_redacao` e
   `v4_ultra_luxo_redacao_nacional` em `contratos/v4_rotas_llm_limpas_v1.json`
   + knob `dados/ultra_luxo.json`. Fila inteira preservada (gpt-5.5 → opus →
   gemini → deepseek → moonshot): frontier falhou, produção segue.
2. **Dispositivo de troca** (pedido expresso do Miguel): `scripts/aplica_ultra_luxo.py`
   `--status | --geral X --nacional Y | --desligar` (valida no ratings, backup
   datado, reconstrói contextos). Voltar ao "grau abaixo" = `--desligar`
   (restaura rotas do `.bak.pre_ultra_luxo_20260902` = contexto super luxo).
3. **Tese com frontier**: `_tese_frontier()` no v41_ciclo lê o knob; pauta
   afirmativa (BRICS/SCO/Sul Global) NÃO precisa mais de vilão — regra nova no
   system prompt da tese + linha editorial viva + manual injetados no contexto
   da tese ("a linha editorial prevalece sobre tudo"). Fail-closed intacto.
4. **Cura geopolítica/tecnologia** (a seca era tese+fila, não coleta):
   V41_FILA_SEM_CLOG (item sem post_id que falha só volta em 6h) +
   V41_MOTIVO_HONESTO (anti-repetição não sobrescreve motivo do juiz) +
   coleta reforçada (+23 keywords geo/IA/BRICS em `temas_prioritarios_geo.txt`,
   +3 queries Brave). Provada AO VIVO: pauta SCO que falhava desde 12:01 UTC
   passou com vilão vazio; pauta de guerra passou com vilão nomeado.
5. **Manual v2.1.0** (oficial + extração do portal em NYC): nova seção
   "1. Princípios (o resto é ofício)"; proibições mecânicas (ponto e vírgula
   zero, parágrafo máx. 2 frases, conectivo proibido) viraram DIRETRIZES de
   preferência — metalinguagem e frase vazia seguem zero absoluto. Ordem do
   Miguel: criatividade dentro da linha é bem-vinda.
6. **Monitoramento 1/1h**: `scripts/monitor_ultra_luxo.py` (NYC) + automação
   ZCode :15 reportando no Telegram do Miguel (assinado, read-only, nunca patcha).
7. **Avisos**: ZM-20260902-043 em de_dell/inbox claude/canal_trindade/ponte
   DSC + 2 auditorias pedidas ao DSN Ideias (ultra-luxo e cura geo) + opinião
   CL/CM solicitada. Linha editorial viva também nos mini-cérebros R1/R2/Chefe.

## Provas

- Dry-run router 12/12 editorias (nacional→fable-5; demais→sol).
- 1º post ultra-luxo: **268674** (digital, 18:08 UTC, sol, $0,0228 esperado).
- Chaves testadas ao vivo: sol/fable/luna (luna descartada por ordem do Miguel).
- Manual NYC: 7/7 substituições aplicadas, seção 1 conferida no arquivo.

## Estado

**Pronto:** tudo acima no ar; backups `.bak_*` em cada arquivo tocado; entradas
no `ROLLBACK_INDEX.md` (V41_ULTRA_LUXO_SOL, V41_CURA_GEO_TEC).

**Falta:** (a) prova do 1º ciclo geo pós-cura (18:55 UTC); (b) as 2 auditorias
do DSN Ideias; (c) opinião CL/CM; (d) **Miguel medir o gasto** do ultra-luxo e
decidir quando voltar ao super luxo (`--desligar`).

**Vulnerabilidade conhecida:** cadeia verificadora (GLM/DeepSeek/Moonshot) como
fallback da tese é FRACA em pauta afirmativa (retorna llm_sem_tese_valida) —
não quebra, mas degrada; o frontier é o caminho principal.

**Próximos passos:** conferir ciclo geo; aguardar auditorias; V4.2 depois,
por ordem do Miguel.

## Adendo ~16:1x BRT — PROVA DO CICLO GEO PÓS-CURA (18:55 UTC / 15:55 BRT)

- **Geopolítica ESCREVEU DE NOVO**: artefato `dados/v41_ciclo/20260902_1556.json`,
  vertical geopolitica, `curadoria: tese_dinamica_aprovada`, FC ok (claims
  confirmados), **draft 268682** (autor 5470, job `v41_geopolitica_b66300c0baf7`),
  redator = **gpt-5.6-sol** ✅.
- Pauta: reivindicações do Marrocos sobre Ceuta e Melilla (fonte em espanhol).
- 🟡 **Comportamento do Sol a registrar**: a fonte estava truncada (número de
  141 mortos sem origem, sem autoridades citadas) e o redator NÃO inventou —
  escreveu recusa fundamentada apontando o anacronismo (crise de Ceuta é 2021,
  governo Meloni só começou em 2022; a fonte confundia Melilla com Meloni).
  Jornalismo correto (zero invenção), mas o draft não é matéria: entra no fluxo
  de revisão/descarte normal. É a cura funcionando como desenhada — matéria
  cheia no próximo ciclo bom.
- **Custo do dia (decisions)**: 17 chamadas — gpt-5.5 15×/$0,495 (manhã,
  pré-ultra-luxo) · **gpt-5.6-sol 2×/$0,046** (268674 + 268682). Ultra-luxo
  começou ~18:08 UTC; base de gasto para o Miguel medir a experiência.

## Adendo ~16:3x BRT — TELEMETRIA DETALHADA DE TODOS OS LLMs DO V4.1 (ordem do Miguel)

Ordem do Miguel 02/09: "ah por falar em telemetria. importante manter telemetria
detalhada de todos os llms do v4.1". Executado no mesmo turno:

1. 🐛 **Bug achado e corrigido**: o extrator de uso do ponto único
   (`/root/telemetria_api.py::_extrair_usage_response`) só lia
   `prompt_tokens`/`completion_tokens` → chamadas **Anthropic** (FC sonnet),
   **Gemini** e **OpenAI Responses** saíam com 0 tokens e NUNCA entravam no
   `banco_custos`. Corrigido (lê `input_tokens`/`output_tokens` e
   `usageMetadata` também). À prova de futuro claude-fable-5 no nacional.
2. 🆕 **`codigo/telemetria_v41.py`** (fail-never): registra TODA chamada LLM do
   pipeline em `agent_data/v4/llm_calls/calls_YYYYMMDD.jsonl` — site
   (tese_frontier/fc/tese_fallback/juiz/verificador), provedor, modelo, status
   (ok/sem_json/http_N/**erro**), tokens, duração. O que o banco_custos não
   pegava (falhas e subsistema) agora fica visível.
3. 🔌 **Wiring**: `_tese_frontier`, cascata FC (sonnet/gemini/gpt c/ uso real),
   `_verifier_llm_json` (GLM/DeepSeek/Moonshot) nos dois arquivos do pipeline,
   11/11 substituições, py_compile 4/4, backups `.bak_pre_telemetria_20260902`.
4. 📊 **`scripts/relatorio_llms_v41.py`**: consolidado diário por modelo
   (banco_custos + llm_calls + decisions + vertical_runtime).
5. 📲 **Monitor do ultra-luxo ganhou seção TEL** — a telemetria consolidada
   flui automaticamente no Telegram :15 (automação existente, assinada).

**Prova real (dia 02/09 até ~16:3x)**: V4.1 = 178 chamadas/$2,58 — glm-5-turbo
110×/$0,37 · deepseek-v4-pro 48×/$0,29 · gpt-5.5 11×/$1,74 · gpt-5.6-sol 8×/$0,18;
router 18 seleções; 15 drafts. Detalhamento por subsistema estreia no próximo
ciclo (19:35 UTC economia / 19:55 UTC geopolítica). ROLLBACK_INDEX registrado
(4 backups + 2 arquivos novos). Nada na produção muda de comportamento —
instrumentação é fail-open/fail-never.

### Prova viva final (~17:0x BRT)

- Smoke controlado do `_verifier_llm_json` com `site=smoke_wiring` registrado
  com todos os campos (tokens 31/47, 1.958 ms) — binding do registrar real nos
  dois módulos confirmado (não o fallback no-op); linha do smoke depois limpa.
- **Chamadas REAIS de produção já entrando**: às 20:00 UTC o relatório
  `--compacto` mostrava `subsistemas: verificador(glm) ok:5` — 5 chamadas GLM
  reais etiquetadas com tokens e duração.
- O ciclo geo 19:55 UTC saiu cedo (`todas_pautas_ja_rascunhadas_24h` — fila
  vazia, estado saudável pós-sprint); as etiquetas `tese_frontier`/`fc`/`juiz`
  aparecem no próximo ciclo que processar pauta nova. Instrumentação provada
  nos 3 caminhos (smoke, binding, produção real).

## Adendo ~17:2x BRT — TESTE GEMINI 3.7 NO ULTRA-LUXO (Miguel: "vê se funciona")

Miguel propôs 3º frontier: **Gemini 3.7 na vertical Tecnologia** (Fable 5 no
Nacional, Sol no Geopolítica). Testado antes de implementar:

- **gemini-3.7-flash EXISTE na chave da casa** (listagem via Dell: a linha Pro
  parou em 3.1-pro-preview; 3.5→3.8 são Flash; existe até gemini-3.8-flash).
- ✅ **Funciona de rede residencial**: teste do Dell com a mesma chave →
  HTTP 200, respondeu "ok" (modelo pensante, traz thoughtSignature).
- ❌ **NÃO funciona do NYC (onde o V4.1 roda)**: `generateContent` e a listagem
  retornam **400 "User location is not supported for the API use"** — Google
  bloqueia IP de datacenter (DigitalOcean NYC) para essa chave/tier. As duas
  variáveis da casa (`GEMINI_API_KEY`/`GOOGLE_GEMINI_API_KEY`) são a MESMA chave.
- 🔍 **Achado colateral**: a perna gemini da cascata de fact-check NUNCA
  funcionou do NYC (falha silenciosa → caía no gpt). A telemetria detalhada
  instalada hoje é que vai expor isso como erro etiquetado.
- Conclusão: ligar gemini-3.7-flash no redator só faria os drafts de tecnologia
  falharem e caírem no fallback gpt-5.5 (o experimento não mediria nada).
- Opções dadas ao Miguel: (A) trocar o 3º frontier por modelo que funciona do
  NYC — recomendação **kimi-k2.5** (assinatura paga, custo marginal zero =
  contraste puro de custo vs sol/fable) ou gpt-5.6-luna; (B) insistir no
  Gemini via relay residencial (frágil) ou Vertex AI (exige GCP/billing,
  decisão dele).
- Wiring para um 3º slot por vertical é trivial quando o modelo estiver
  escolhido (contexto `v4_ultra_luxo_redacao_tecnologia` + mapa + knob +
  `aplica_ultra_luxo.py --tecnologia` + registro no llm_ratings). Aguardando
  decisão do Miguel — nada foi mudado na produção.

## Adendo ~18:3x BRT — FEIRA DE PAUTAS: diagnóstico da fila vazia + AUTOCURA NO AR (REPOSTO 21:3x — uma escrita paralela ~19:08 sobrescreveu o arquivo com cópia antiga)

Miguel viu "fila de pautas vazia" no monitor e ordenou: "Não quero ver nada
vazio aí... sistema de autocura bem forte... qualquer problema você cura."

### Diagnóstico (causa raiz)
- A fila do V4.1 são os bancos sqlite por vertical (`agent_data/v4_verticals/`),
  alimentados pelos crons de coleta+intake: geo 1/1h, ciência 2/1h, economia
  1/4h, nacional 1/6h, cultura 1/4h, meio_ambiente/esporte/saude/digital 3-4x/dia.
- Entre um intake e outro o ciclo V4.1 (horário/2h) consome as candidatas e o
  dedupe (pauta rascunhada <24h, falha <6h) bloqueia re-tentativa — o ciclo sai
  com "todas_pautas_ja_rascunhadas_24h" e o monitor mostrava "fila vazia".
- Não era bug: era **janela de fome estrutural** entre os bursts de coleta.

### Cura (V41_AUTOCURA_FILA_20260902)
1. **Guardião** `scripts/autocura_fila_v41.py` (cron */20, flock próprio):
   conta candidatas FRESCAS e TENTÁVEIS por vertical com a MESMA régua do
   v41_ciclo (frescor + dedupe). Abaixo de 2 → roda **coleta+intake extra na
   hora** (mesmos comandos/flocks do cron, mínimo 25 min entre reforços da
   mesma vertical). Ainda zero → INCIDENTE registrado (`incidentes.jsonl`) e
   exposto no monitor — o único vazio legítimo (mundo sem fato novo) fica
   VISÍVEL com motivo, nunca silêncio. Fail-open total.
2. **Monitor ganhou seção FILA** — contagem por vertical em toda mensagem
   horária do Telegram.
3. Provas: check nas 9 verticais OK; corrida com fila cheia = 0 curas;
   **reforço real da cultura executado** (coleta+intake rc ok). Backup do
   crontab + .bak do monitor + ROLLBACK_INDEX seção V41_AUTOCURA_FILA_20260902.

## Adendo ~21:2x BRT — FALHAS DA TELEMETRIA: DIAGNOSTICADAS E CONSERTADAS (ordem do Miguel: "houve falhas? conserta então?")

A telemetria nova mostrou 4 falhas no dia (monitor 21:15 BRT): 3 `sem_json`
+ 1 `http_429`.

### Diagnóstico (com prova nos registros llm_calls)
- `sem_json` (juiz GLM 18:43 BRT; verificador GLM + DeepSeek 20:31 BRT):
  respostas de 43-53s de geração = saída batendo no teto `max_tokens=2500`
  → JSON cortado no meio → parse falha. A regex gulosa `\{.*\}` também quebra
  quando o modelo cerca o JSON de prosa/fences com chaves depois.
- `http_429` (moonshot/kimi-k2.5, verificador 20:31 BRT): rate limit
  TRANSITÓRIO na 3ª perna da cascata — absorvido pelo desenho fail-open.
  Com o conserto abaixo as pernas 1-2 voltam a responder e a 3ª quase não é chamada.
- Nenhum rascunho foi perdido: fail-open segurou (economia 268709 saiu às 23:36
  UTC mesmo com o verificador indisponível naquele ciclo).

### Conserto (V41_JSONFIX_20260902)
- Só um lugar precisava mudar: `_verifier_llm_json` no
  `/root/v4_vertical_draft_worker.py` — v41_ciclo usa a MESMA função
  (verificador, juiz e tese_fallback cobertos de uma vez).
- (1) Helper novo `_extrair_primeiro_json`: tenta primeiro a regex gulosa
  antiga (comportamento idêntico nos casos que já funcionavam) e, se ela
  falhar, varredura por chaves balanceadas que prefere o ÚLTIMO JSON válido
  (modelo que ecoa o exemplo antes do veredito).
- (2) `max_tokens` 2500 → 4000 nas 3 pernas (GLM/DeepSeek/Moonshot).
- Provas: py_compile OK; 6/6 casos-limite (json puro, fence+prosa com chave,
  truncado, eco de exemplo, chaves dentro de string, vazio). Backup
  `.bak_pre_jsonfix_20260902` + ROLLBACK_INDEX seção V41_JSONFIX_20260902.
- Acompanhamento: próximo ciclo com veredito deve zerar os sem_json
  (telemetria mostra).

## Adendo ~21:5x BRT — MISTÉRIO DO FABLE RESOLVIDO + LEITURA DA PONTE (CL-090) + RESPOSTA DO ZM

1. **Fable 5 JÁ ESTREOU** (respondendo ao Miguel "ainda não veio nacional fable 5, por quê?"):
   post **268715** "Câmara aprova Pacheco no TCU por 404 votos após Alcolumbre
   dispensar sabatina", ciclo 21:26 BRT, `model: claude-fable-5` confirmado no
   artefato. A demora NÃO foi bug/cota: entre o knob (15:08 BRT) e 21:26, todos
   os ciclos nacionais saíram sem pauta tentável (curadoria recusou 9 ciclos;
   coletor `pol` repetiu a mesma pauta 7× em 12h). O monitor não mostrava a
   chamada porque conta pelo `llm_decisions` datado por dia UTC (virou 21:00
   BRT, 11 min antes da chamada) — aparece no próximo relatório.
2. **Ponte lida (ordem do Miguel)**: CL-20260902-090 formalizou as críticas
   construtivas — fórum `forum_critica_v41_ultra_luxo_20260902.md` (7 posts
   ultra-luxo auditados, média 7,3 corrigida; defeitos de pipeline: recusa
   salva como post, número local sem lugar, capa, frescor) + rodada comparativa
   de títulos EMU-2 (13/57 violações ~23%, fórum próprio ainda chegando pelo
   sync) + pedido do Miguel de robôs coletores DSN para as verticais famintas.
3. **Resposta do ZM postada na §6.2 do fórum de crítica**: (d) fable explicado
   acima; (a) recusa → flag explícita `recusa=true`, sem rascunho, métrica de
   pipeline separada; (b) campo `frescor` 0-10 + `fato_principal_data` no meta
   `_cafezinho_frescor` p/ o escalonador; (c) capa candidata não-bloqueante no
   ciclo (escolha segue da CL); extras: regra anti-release na tese dinâmica,
   categoria `inconclusivo_por_falta_de_lugar` no FC, investigação do caso
   Astra 268674 (evento due sem wp-cron disparar — verificador de virada ×
   gate standby_contrato). **Formato dos coletores DSN definido** (JSONL:
   item_key sha1[:16] da URL, title, url, source_name, source_type=dsn,
   published_at ISO UTC, text_content ≥800 chars; adapter meu insere no sqlite
   com status=new + log de entrega).
4. **Compromisso**: compilação §7 às 10:00 de 03/09 (após prazo de opiniões
   09:12) com aplicação das correções via rito backup/SHA/rollback; itens que
   dependem do Miguel marcados [PEN. MIGUEL]. ⚠️ **PENDÊNCIA EXPLÍCITA**: esta
   sessão é de automação e NÃO conseguiu criar o agendamento (CronCreate
   bloqueado). Qualquer sessão do ZCode aberta na manhã de 03/09 deve executar
   a compilação às ~09:5x-10:00 — roteiro completo na §6.2 do
   `forum_critica_v41_ultra_luxo_20260902.md` + adendo acima. Se nenhuma
   sessão estiver aberta, o Miguel pode cobrar pela ponte ou abrir um chat.
5. Nota colateral: Astra 268674 publicado 21:40:47 (contenção DS-Dell rodando
   o evento de cron vencido; post_date 21:37:53 preservado, permalink 200).

### Adendo ~22:3x BRT — ROBÔS COLETORES NO AR (V41_ROBOS_COLETORES_20260902)

Ordem do Miguel (~22:1x BRT): "tá com falta de notícia... vamos criar robôs
coletores... roda de 15 em 15 minutos... pega notícia de política... pra tudo".

1. **Pergunta do Miguel — um robô ou vários?** Decisão ZM: **UM robô com um
   módulo por vertical** (9 módulos: política, geopolítica, tecnologia/IA,
   economia, esporte, digital, saúde, meio ambiente, cultura). Motivos: a
   infraestrutura é a mesma para todos (coletor.py → estoque → intake →
   sqlite); um ponto só de vigília, com liga/desliga geral E por vertical;
   os MESMOS flocks do cron legado e do guardião = zero colisão. N robôs
   separados seriam 9× código/log/pontos de falha sem ganho. Cada módulo tem
   cadência e chave próprias no JSON de config.
2. **Diagnóstico da fome (prova)**: o coletor.py tem TTL de estoque (pol 6h,
   geo 3h, tec 6h) que PULA a recoleta enquanto o estoque vale — por isso a
   política repetia pauta 7× em 12h mesmo com cron ativo. Cura = o robô chama
   `coletor.py <grupo> --forcar` (coleta de verdade) + intake, sob flock.
3. **O que está no ar (NYC)**: `scripts/robos_coletores_v41.py` + config
   `dados/robos_coletores.json` (ativo=true; cadências: pol/geo 15 min,
   eco/tec/esp 30, dig 45, sad/amb/cul 60 — tudo editável num arquivo só) +
   cron `*/15` com flock próprio + estado/log/entregas em
   `agent_data/v4/robos_coletores/`. Corridas do robô são SEM Brave
   (export BRAVE_API_KEY= vazio; protege a cota; a profundidade Brave segue
   nos crons legados) — RSS + Google News RSS dão o frescor de 15 min.
   Fail-open total: erro numa vertical não para as outras; lock ocupado =
   pula a rodada e pega na próxima.
4. **Provas E2E**: coleta pol --forcar sem Brave = 145s / 18 candidatas novas
   com fatos frescos (STF/Mendonça/Vorcaro, Pacheco) → intake: fila nacional
   302→319. Robô `--vertical geopolitica`: rc=0, 264s, +11 candidatas.
5. **Rollback**: remover a linha V41_ROBOS_COLETORES_20260902 do crontab
   (backup `/root/crontab.bak_pre_robos_coletores_20260902.txt`) — ou só
   ativo=false no JSON. O robô só INSERE candidatas status='new' na fila que
   o V4.1 já consome; nada mais toca. ROLLBACK_INDEX atualizado.
6. Varredura inicial das 9 verticais disparada ~22:32 (nohup); a partir do
   próximo :00/:15/:30/:45 UTC o cron assume sozinho. A seção FILA do monitor
   :15 vai mostrar o crescimento da feira.

### Adendo ~23:5x BRT — ROBÔ INTEGRADO À CURADORIA + MULTIIDIOMA (V41_CURADOR_MULTIIDIOMA_20260903)

Ordem do Miguel (~23:2x BRT): integrar o robô "da forma mais inteligente
possível" — nota de frescor e importância, notícias com tamanho decente
("não pode vir coisa vazia... zero alucinação"), coleta geopolítica em todas
as línguas (alemão, chinês, coreano, japonês...), e "cuidado para não se
afastar do original V4.1 — não é só notícia, é criação de tese".

1. **Como integra sem quebrar a lógica do V4.1 (resposta à pergunta do
   Miguel)**: o robô entrega CANDIDATAS na mesma fila sqlite que o ciclo já
   consome (INSERT OR IGNORE por item_key). Quem decide tudo segue sendo o
   V4.1: curadoria por TESE DINÂMICA (frontier lê a notícia + linha editorial
   + manual, exige vilão/herói/consequência e ÂNCORAS literais no texto —
   âncora fora da notícia reprova a tese, fail-closed), depois redação com
   briefing completo, FC em cascata, revisão e gate de publicação. O robô
   não pula NENHUMA etapa. Notas são SINAL DE ENTRADA da curadoria, nunca
   substituem a tese.
2. **Módulo curador no ar**: nota_frescor 0-10 (idade do fato: ≤3h=10,
   ≤6h=9, ≤12h=7, ≤24h=5...), nota_importancia 0-10 (keywords VIVAS da
   curadoria da casa — foco_pauta.json + curadoria_diaria/geral — + léxico
   geo) e nota_texto 0-10 (tamanho), compostas em nota_curadoria. Gravadas
   no raw_json (chave curadoria_v41) de cada candidata. 1ª passada: 555
   candidatas com nota (geo 200, nac 83, eco 65, esp 64, amb 58, cul 29,
   dig 23, sad 22, cie 11). Seleção do ciclo NÃO foi alterada (hard: 6
   drafted + 3 sobras score ASC; soft: 9 new por frescor) — lógica intacta.
3. **Gate de tamanho ("nada vazio")**: candidata com texto <800 chars é
   marcada texto_curto=true + penalizada na nota; coleta multilíngue SÓ
   insere ≥800 (fininhos são descartados). O coletor da casa já descarta
   extrações falhas (MIN_TEXTO 300). Prova da coleta real: política trouxe
   textos de 2.109 a 6.193 caracteres — material suficiente pro redator sem
   alucinar; o sistema de complemento do V4.1 (FC/busca) segue enriquecendo.
4. **Multiidioma no ar (geopolítica)**: 19 feeds RSS DIRETOS da imprensa
   internacional em 8 línguas (inglês: Al Jazeera/BBC/Guardian; alemão:
   Tagesschau/DW/ZDF; chinês: BBC中文/NYT中文; coreano: BBC Korean/Yonhap;
   japonês: NHK/BBC Japanese; francês: Le Monde/France24; russo: TASS/RT;
   espanhol: BBC Mundo/El Mundo), todos provados VIVOS do NYC. Google News
   foi descartado com diagnóstico: links /rss/articles/ agora vêm
   CRIPTOGRAFADOS e o decodificador toma 429/captcha de IP de datacenter;
   Bing resolve a URL mas cai em botwall dos veículos (403). RSS direto = a
   base RSS-first que já funciona na casa. Cada matéria só entra na fila com
   ≥800 chars de texto extraído (trafilatura), source_type='multiidioma',
   idioma+notas no raw_json, sob o MESMO flock da geopolítica. Cadência
   30 min (config). Zero Brave, zero custo de API.
5. **Resposta à pergunta das diretrizes (com prova)**: SIM — o briefing do
   redator carrega os 4 documentos INTEIROS (21.863 chars de instruções;
   linha_editorial_viva 3.914c + estilo_nucleo_fixo 1.311c +
   MANUAL_DE_ESCRITA_PORTAL v2.1.0-P 11.284c + diretriz_qualidade_viva
   4.200c = 20.709c de diretrizes), com a cláusula "a LINHA EDITORIAL
   prevalece sobre tudo"; e a TESE dinâmica (curadoria) também lê linha +
   manual (V41_TESE_FRONTIER_20260902). Única lacuna conhecida: revisores
   externos R1/R2 (Tencent) ainda não leem linha/manual — wiring pronto,
   aguardando o "vai" do Miguel.
6. **Anti-fake news (o que ele pediu)**: fontes = feeds estabelecidos +
   Google News (só veículos indexados); tese fail-closed de âncoras (nada de
   conceito imposto); FC em cascata; nada é publicado sem revisão (gate
   standby_contrato — só CL/CM publicam). O robô alimenta; o V4.1 julga.
7. **Arquivos**: `scripts/robos_coletores_v41.py` (v2, backup
   `.bak_pre_curador_multiidioma_20260903`) + `dados/robos_coletores.json`
   (bloco multiidioma). Rollback: restaurar o .bak + remover bloco
   multiidioma do JSON; notas no raw_json são inertes pro ciclo.

---

## Adendo ~23:1x BRT (02/09) — confirmação da regra "V4.1 só rascunho; CL publica" (REPOSTO 23:5x após clobber de escrita paralela)

Miguel lembrou a regra: zero teste público, zero publicação pelo V4.1; posts analisados pela Claude Laura antes de publicar. Confirmado com prova:

1. **Robôs coletores/curador/multilíngue desta sprint = zero WP**: só INSERT de candidatos (status='new') na fila sqlite do NYC. Nenhuma ação de publicação em momento algum.
2. **Cadeia do único post publicado hoje (268715, Pacheco/TCU)**: V4.1 (claude-fable-5, autor 5470) criou o rascunho 21:27 BRT via REST → R1 marcou INCERTO (escada de busca indisponível; fail-close: "não deve ser publicado ainda") → **Claude Laura fez revisão manual integral com fontes próprias (CL-20260902-091: camara.leg.br + senado.leg.br), aprovou texto + capa (visão própria) + título EMU-2 + frescor 10/10 e publicou ~22:06 BRT**. Fluxo exatamente como o Miguel descreveu.
3. **Gate duro ativo**: mu-plugin `cafezinho-gate-dois-checks.php` em MODO CONTRATO (backup `bak_pre_modo_contrato_20260901`) — só CL/CM publicam.
4. 268717 (SCO/Índia-Rússia) está `future` (escalonado; passa pelo verificador de virada + gate).

Estado: regra intacta, nenhum ajuste necessário.

---

## Adendo ~23:3x BRT (02/09) — EQUIPE DE COLETA NACIONAL NO AR (V41_EQUIPE_NACIONAL_20260903) (REPOSTO 23:5x após clobber de escrita paralela)

Ordem do Miguel (voz, ~23:1x→23:4x BRT): acompanhar Metrópoles, G1, ICL, Revista Fórum, Folha, Veja etc.; extrair o conteúdo deles OU buscar o conteúdo anunciado em outras fontes (paywall/botwall); equipe especializada — batedor de fontes, coletor, curador com NOTA DA FONTE, e um enriquecedor que pega as maiores notas e MONTA O MATERIAL BRUTO pesquisando a notícia na internet. Decisão de arquitetura (Miguel delegou): os 4 papéis viraram módulos do robô único (mesma carcaça, 1 ponto de observação, sem quebrar o V4.1).

1. **PROSPECTOR** (cadência 30 min): sonda 20 feeds nacionais; feed com 6 falhas seguidas = APOSENTADO; aposentado é re-sondado a cada 6h ("volta a funcionar"). Saúde em `dados/feeds_nacionais_saude.json`, transições em `feeds_eventos.jsonl`. Prova: 16/20 vivos na 1ª sondagem (ficam no ciclo de retry: Estadão, CartaCapital 403, Agência Brasil 404, ICL 0 entradas, DW pt 0 entradas, 2 com erro de conexão).
2. **COLETOR NACIONAL DIRETO** (cadência 15 min): colhe SÓ dos feeds ativos, extrai artigo com trafilatura, régua da casa ≥300 chars (fininho não entra), marca `texto_curto` <800. Prova 1ª colheita: **+73 candidatas de 13 fontes** (metropoles 10, g1 8, icl 5, forum 5, folha 5, veja 5, uol 5, cnn_brasil 5, poder360 5, brasil247 5, congresso_foco 5, bbc_portugues 5, sputnik_brasil 5), 1 fininho descartado.
3. **CURADOR**: já existia; agora grava também `nota_fonte` (tabela no script, valores iniciais ZM, editáveis: Fórum/ICL 9.0, 247/CartaCapital 8.5, Agência Brasil 8.0, Metrópoles/G1/Folha 7.5, Veja 6.5 etc.). Fórmula composta não mudou (0.4 frescor + 0.4 importância + 0.2 texto).
4. **ENRIQUECEDOR** (cadência 30 min, Brave, máx 10 buscas): pega as maiores notas com texto <800, busca a notícia e monta MATERIAL BRUTO com até 3 fontes externas (1 por domínio), cada bloco com fonte+URL; atualiza text_content/hash/score e re-grava curadoria. Prova E2E real: "Quaest: Lula 37%×29%" +8.345 chars (Operamundi/JC/Portal de Prefeitura), "Cientista política...Flávio×Lula" +9.103 chars (Portal de Notícias/Brasil de Fato/Valor). ZERO invenção: só texto extraído de página real, citado.
5. **O que NÃO mudou**: ciclo/tese/redator/FC/publicação intactos; cron nenhum alterado (mesmo */15, cadências internas no config); robô segue só INSERINDO/enriquecendo candidatas — rascunho-only, publicação é da CL (regra confirmada no adendo anterior).
6. **Rollback**: `V41_EQUIPE_NACIONAL_20260903` no ROLLBACK_INDEX do NYC (ligado=false nas 3 seções do config; backups `.bak_pre_equipe_nacional_20260903`).
7. **Resposta ao "como está indo?"**: fila nacional 320→393 new (+73); geo segue 1.134+ (multi +7 na mesma hora); o desenho de equipe do Miguel foi implementado 1:1, dentro do robô único.
