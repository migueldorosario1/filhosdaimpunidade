# MEMÓRIA TÉCNICA — MISSÃO QUALIDADE: JUIZ DE QUALIDADE V4.1 + R2 (07/09/2026)

Log técnico completo (decisões resumidas no fórum irmão
`Foruns/forum_qualidade_curadoria_juiz_v41_20260907.md`). Execução: ZCode/Qwen3.8-Max
(ZM, Dell), 07/09 00:2x→01:3x BRT.

## 1. Diagnóstico (provas)

- Ledger LLM NYC `agent_data/v4/llm_calls/calls_20260906.jsonl`: tese_frontier
  gpt-5.6-sol 52 ok / 0 erro; fc sonnet 33 ok + 1 sem_json; juiz deepseek-chat 47 ok;
  verificador deepseek-chat 37 ok. → crédito NÃO é causa.
- Curadoria da coleta hoje: (a) `_tese_dinamica` (v41_ciclo.py:164) — frontier gpt-5.6-sol
  lê `dados/linha_editorial_viva.md` + `dados/MANUAL_DE_ESCRITA_PORTAL.md`, cria teses,
  valida âncoras; fallback `_verifier_llm_json`; (b) "juiz" deepseek = SÓ anti-canibalização
  inter-vertical + frescor (v41_ciclo.py:~514-540); (c) notas `curadoria_v41`
  (robos_coletores_v41.py, determinísticas por keyword) — o docstring diz: "a seleção do
  ciclo NÃO muda".
- Seleção do ciclo (v41_ciclo.py:~430): verticais órfãs (saude/esporte/meio_ambiente/
  digital) = 9 'new' mais recentes; demais = 6 'drafted' + 3 'new' **ORDER BY score ASC**
  ("sobras" do tempo em que o worker V4 vivo pegava as de nota alta). V4 desligado 24/08
  → sobras viraram a fila principal.
- Roteamento errado (bancos `/root/agent_data/v4_verticals/*.sqlite3`, leitura 30h):
  economia ← «Alcaraz supera... US Open» + «Emmy Bad Bunny»; meio_ambiente ← «Mirassol
  vence», «Mega-Sena acumula», «dicas desfile 7 de Setembro», «Golpe do sósia»; nacional ←
  «Anderson Barros/Palmeiras», «Brasileirão: melhores momentos» (fonte: robos_coletores_
  nacional_direto, feed metropoles.com/feed GERAL); ciencia ← 派早报 (sspai.com/feed),
  anime-players рунета (habr.com/ru) — fonte robos_coletores_tec_multiidioma.
  Itens com item_key de 48 hex sem campo fonte = legado `coletor.py` + `v4_vertical_intake.py`
  (crons ativos: eco 4/4h, amb 12/18/0, esp 7/13/19/1, tec 10,40/h, geo 0/h, pol 20/6h...).
- Coletor externo IDEIA-012 (`scripts/dsn_adapter_v41.py`) escreve SÓ em nacional.sqlite3
  (Senado) — não é o culpado.

## 2. Implementação juiz de qualidade (NYC /root/v4_labs)

- Patch via `/tmp/patch_juiz.py` (Dell) → scp → execução remota (heredoc direto quebrou
  quoting: aspas simples internas desligaram a quoting do ssh e striparam aspas duplas —
  SyntaxError; cura = arquivo local + scp; arquivo restaurado do backup antes, md5
  87f5984b0e4f2d9d5dc13e2cbe79b79b conferido idêntico).
- Backup: `codigo/v41_ciclo.py.bak_pre_juiz_qualidade_20260907`. py_compile OK.
- 4 âncoras: (A1) funções `_JUIZ_CFG_PADRAO/_juiz_cfg/_juiz_llm/_JUIZ_CRITERIOS/
  _juiz_qualidade` inseridas antes de `def _tese_dinamica`; (A2) hook juiz1 no loop de
  candidatas ANTES da tese (com `_jq_hist`/`_jq_ok`); (A3) `saida["juiz_qualidade"]` +
  `saida["juiz_historico"]` no artefato; (A4) juiz2 após `pid = post.get("id")`/bloco de
  recusa, antes de "# 3) metas 4.1 + FC-2" — reprova → DELETE force do rascunho (padrão
  da recusa do redator) + status `juiz_qualidade2_reprovou`.
- Cascata `_juiz_llm`: deepseek-chat (api.deepseek.com) → qwen-plus (QWEN_BASE_URL
  compatible-mode) → `_verifier_llm_json(site=..._fb)`. timeout 75s, max_tokens 2000,
  temperature 0.2. Telemetria `_tel(site, provedor, modelo, status, ptok, ctok, ms)`.
- Aprovação (objetiva, não confia no bool do LLM): total ponderado ≥ `min_total` (6.0) E
  `interesse_br` ≥ 5 E `encaixe_vertical` ≥ 5 (juiz1); total ≥ 6 E clareza ≥ 5 (juiz2).
- Config viva: `dados/juiz_qualidade.json` (criado) — pesos {clareza 1.0, interesse_br
  2.0, importancia_global 1.0, importancia_economia 0.8, audiencia 1.5, encaixe_vertical
  1.5, linha_casa 1.2}, mínimos, modelos, `ativo`. Critério vivo:
  `dados/PADRAO_CURADORIA_QUALIDADE.md` (criado; lido pelo juiz, máx 4000 chars).
- Teste standalone `/tmp/teste_juiz.py` (importa o módulo, sem WP): 5/5 conforme fórum
  (Alcaraz 2,11 repr · anime RU 1,11 repr · Shopee 2,09 repr · metalinguagem 0,00 repr ·
  minerais críticos 9,02 APROV). Modelo usado: deepseek:deepseek-chat.

## 3. R2 (tencent /home/ubuntu/dsn_revisor2/dsn_revisor2.py)

- Patch `/tmp/patch_r2.py` (scp): (A1) fim do bolo do título += "(7) CONTAGEM EMU-9...
  EMU-10"; (A2) após item 3) OLHO → item "4) QUALIDADE DA PAUTA" (padrão Metrópoles/Fórum;
  serviço/listicle/loteria, esporte estrangeiro sem brasileiro, tech estrangeira de nicho,
  metalinguagem = CORRECOES + «FORA DO PADRÃO DE QUALIDADE»).
- Backup `.bak_pre_juiz_qualidade_20260907`; py_compile + ast.parse OK com /usr/bin/python3
  (o mesmo do cron 20 * * * *). Sem restart (cron = processo novo).
- R1 (`dsn_revisor1`) intocado: missão = fact-check externo; qualidade pré-rascunho agora
  é do juiz 2.

## 4. WP (canônico, wp-cli www-data)

- `wp post update` 269228 (título 61c) + 269275 (69c) + 269305 (72c, future mantido) +
  269279 → draft. `wp post term remove`: 269155 categoria economia; 269144 economia;
  269183 esporte (ficou Redação). Todos conferidos pós (título/status/categorias).
- `wp rocket clean --confirm` NÃO existe no canônico ("not a registered wp command") —
  purge de cache pendente de verificação matinal (TTL).
- 269021 (autor 5786) future travado desde 04/09 12:00 — NÃO tocado (§112 linha alheia),
  reportado na ponte.
- Backup antes/depois + rollback: `Cerebro/Backups/posts_editados/20260907_missao_qualidade_pre_fix.md`.
- Cópia dos patch scripts: `Cerebro/Backups/posts_editados/scripts_juiz_20260907/`.

## 5. Rollback geral

- NYC: `cp codigo/v41_ciclo.py.bak_pre_juiz_qualidade_20260907 codigo/v41_ciclo.py` (ou
  `juiz_qualidade.json` → `"ativo": false` desliga sem deploy).
- Tencent: `cp dsn_revisor2.py.bak_pre_juiz_qualidade_20260907 dsn_revisor2.py`.
- WP: 1 comando por post (valores no backup).

## 6. O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** diagnóstico completo (não foi crédito, não foi o coletor externo; foi
  roteamento legado + fontes sem filtro + ausência de juiz de interesse + notas
  decorativas); juízes 1+2 no ar e testados; R2 reforçado (EMU-9/10 no bolo + gate de
  qualidade); auditoria das 50 publicadas + 6 future com correções não-drásticas e
  receita SEO (fora da home sem sair do ar); ponte para CL.
- **Falta:** prova ao vivo nos artefatos de ciclo (próximas horas); calibração 48h;
  correção do roteamento legado (proposta no fórum §5.2).
- **Preciso do Miguel:** "vai" para o guarda de roteamento/aposentadoria do `coletor.py
  eco/amb`; destino de 269279/269288 (rascunhos); quem destrava 269021 (CL/DS?).
