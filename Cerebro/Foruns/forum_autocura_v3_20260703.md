# Fórum — Autocura V3 Produção e Mídia

**Data de abertura:** 2026-07-03  
**Hora de abertura:** 22:29 BRT  
**Responsável:** Codex  
**Escopo:** testar o V3 com autocura ativa, registrar cada pauta tentada em relatórios numerados, diagnosticar gargalos de produção/mídia/auditoria e consolidar correções cirúrgicas.

## Protocolo da rodada

- Servidor: Tencent (`/root/V3`).
- Execução controlada: `executar_lote_publicacao_v3_real.py --total 1 --modo ponta-a-ponta --wp-status pending`.
- Publicação WordPress: proibida nesta rodada; validar ledger após cada teste.
- Autocura ativa já aplicada: `redator_llm_v3.py` com até 3 tentativas de expansão quando `corpo_html < min_chars`.
- Backup remoto da autocura de produção: `/root/V3/redator_llm_v3.py.bak_autocura_expansao_v2_20260703_200545`.
- Evidências obrigatórias por relatório: data/hora, pauta, título original, etapa de falha/sucesso, mensagem técnica, mídia, auditoria, ledger WP e decisão.

## Relatórios

### Relatório 001 — 2026-07-03 22:29 BRT — Pré-checagem

**Objetivo:** garantir que a nova rodada não concorresse com processo V3 ativo e que os arquivos principais estivessem sintaticamente íntegros.

**Comandos/evidências:**
- `ps` remoto: sem lote V3 ativo antes da execução.
- `py_compile`: OK para `redator_llm_v3.py`, `executar_lote_publicacao_v3_real.py`, `executar_producao_editorial_v3_real.py`, `executar_midia_v3_real.py`, `v3_preparar_midia_pronta.py`.

**Decisão:** autorizado rodar lote controlado.

### Relatório 002 — 2026-07-03 22:29-22:34 BRT — Coleta inicial

**Log remoto:** `/root/V3/logs/lotes_publicacao/lote_publish_20260703_222939.jsonl`

**Resultado da coleta:**
- Duração: `233272 ms`.
- `aprovadas_total=1`.
- `inseridas=0` porque houve dedup para a candidata aprovada.
- `imagens_bloqueadas_reuso_30d=22`.
- Várias candidatas relevantes foram descartadas antes da produção por `bloqueada_sem_imagem_ouro`.

**Candidata aprovada pela coleta:**
- Título: `PT decide direcionar R$ 127 milhões do Fundo Eleitoral à campanha de Lula`.
- Fonte: `g1.globo.com`.
- Texto: `3256` caracteres.
- Imagem Ouro prévia: Lula, `match_score=94.58`, `ouro_portal/politica/lula/...`, `1600x900`, `209682 bytes`, licença `CC BY-SA 4.0`, crédito `Lula Oficial/Flickr`.

**Diagnóstico:** a coleta está conservadora e depende fortemente de imagem Ouro. Isso protege contra imagem errada, mas reduz o número de candidatas aproveitáveis.

### Relatório 003 — 2026-07-03 22:34 BRT — Falha de mídia em `curadoria_3f6111d99d403def`

**Pauta:** `Quem são os membros da bancada das bets no Congresso`.

**Etapa:** mídia.

**Resultado:** falha.

**Mensagem técnica:** `preflight não executável para mídia real`.

**Diagnóstico:** a pauta já havia sido tentada em rodada anterior. O V3 descartou imagem desalinhada pós-tese: a imagem herdada apontava para `Davi Alcolumbre`, mas o personagem principal era `Dr. Luizinho`, sem substituta Ouro suficiente.

**Decisão:** manter bloqueada; não relaxar regra de entidade humana. Próxima correção possível é ampliar Banco Ouro/R2 para personagens legislativos de nicho.

### Relatório 004 — 2026-07-03 22:34 BRT — Falha de mídia em `curadoria_972a461623e67872`

**Pauta:** `CCJ do Senado aprova projeto que permite ao STJ paralisar processos de 'relevância' em todo o país`.

**Etapa:** mídia.

**Resultado:** falha.

**Mensagem técnica:** `preflight não executável para mídia real`.

**Diagnóstico:** a imagem Ouro herdada era `Geraldo Alckmin`, mas a tese/personagem visual principal apontava `Veneziano Vital do Rêgo`. O descarte pós-tese funcionou corretamente.

**Decisão:** manter bloqueada; o bug de imagem errada está protegido. Pendência de acervo: foto aprovada para `Veneziano Vital do Rêgo`.

### Relatório 005 — 2026-07-03 22:35-22:39 BRT — Falha de produção em `curadoria_8368012894d519d3`

**Pauta:** `Governo não abre mão do PIX, mas apresenta novas medidas aos EUA para evitar tarifaço`.

**Etapa:** produção.

**Resultado:** falha após autocura.

**Mensagens:**
- Autocura 9 fontes: `chars=3266, min_chars=5200, base_editorial_chars=6478, paragrafos=8`.
- Autocura 12 fontes: `chars=3719, min_chars=5200, base_editorial_chars=6544, paragrafos=8`.

**Diagnóstico:** a autocura v2 por reescrita inteira melhora um pouco, mas modelos continuam resumindo demais quando a base editorial passa de 6000 caracteres.

**Decisão:** abrir correção adicional no redator: complemento editorial anexado ao melhor corpo, em vez de nova reescrita completa.

### Relatório 006 — 2026-07-03 22:40-22:43 BRT — Falha de produção em `curadoria_db70019b5434a172`

**Pauta:** `'Lula é o único que quer o tarifaço', responde Flávio após presidente atribuir à família Bolsonaro nova taxa dos EUA`.

**Etapa:** produção.

**Resultado:** falha após autocura.

**Mensagens:**
- Autocura 9 fontes: `chars=3859, min_chars=4200, base_editorial_chars=5899, paragrafos=7`.
- Autocura 12 fontes: `chars=3378, min_chars=5200, base_editorial_chars=6126, paragrafos=8`.

**Diagnóstico:** a mudança de 9 para 12 fontes elevou a base editorial acima de 6000 e subiu o piso para 5200, mas a produção ficou ainda menor. O mecanismo de autocura precisa crescer texto sem depender de reescrita total.

**Decisão:** coberto pela mesma correção do Relatório 005.

### Relatório 007 — 2026-07-03 22:43-22:48 BRT — Falha de produção em `curadoria_0979c3951d7c81ba`

**Pauta:** `PT decide direcionar R$ 127 milhões do Fundo Eleitoral à campanha de Lula`.

**Etapa:** produção.

**Resultado inicial:** falha após autocura.

**Mensagens:**
- Autocura 9 fontes: `chars=3248, min_chars=4200, base_editorial_chars=5838, paragrafos=6`.
- Autocura 12 fontes: `chars=3529, min_chars=5200, base_editorial_chars=6223, paragrafos=7`.

**Diagnóstico:** bom caso de validação porque tinha imagem Ouro alinhada e fonte factual clara; o único bloqueio era o tamanho do texto.

**Decisão:** usar esta pauta como caso de regressão para a autocura v3.

### Relatório 008 — 2026-07-03 22:49-22:51 BRT — Falha de produção em `curadoria_fa5ec207a48f51a2`

**Pauta:** `Justiça italiana anula decisão que autorizava extradição de Carla Zambelli no caso da arma; novo julgamento será realizado`.

**Etapa:** produção.

**Resultado:** falha após autocura.

**Mensagens:**
- Autocura 9 fontes: Brutas Plus falhou.
- Autocura 12 fontes: `chars=2861, min_chars=5200, base_editorial_chars=6026, paragrafos=8`.

**Diagnóstico:** outro caso de base longa com texto final curto. Reforça que o problema é sistêmico no redator/autocura, não em uma pauta isolada.

**Decisão:** lote interrompido manualmente para evitar consumo repetitivo de LLM e aplicar correção.

### Relatório 009 — 2026-07-03 22:52 BRT — Correção 1 aplicada: autocura de complemento editorial

**Arquivo remoto:** `/root/V3/redator_llm_v3.py`.

**Backup remoto:** `/root/V3/redator_llm_v3.py.bak_autocura_complemento_v3_20260703_225252`.

**Patch:** quando a reescrita inteira continuar abaixo de `min_chars`, o redator agora chama uma autocura final que pede apenas 2 a 4 parágrafos complementares e anexa esses parágrafos ao melhor corpo já obtido.

**Por que isso corrige:** o modelo vinha respondendo com outra versão curta. O complemento força crescimento incremental sem jogar fora o melhor rascunho.

**Validação sintática:** `py_compile` OK.

### Relatório 010 — 2026-07-03 22:53 BRT — Validação focada da produção em `curadoria_0979c3951d7c81ba`

**Comando:** `executar_producao_editorial_v3_real.py --pauta-id curadoria_0979c3951d7c81ba --confirmar`.

**Resultado:** sucesso.

**Antes da correção:** `chars=3529`, `min_chars=5200`.

**Depois da correção:** `chars=6242`, `modelo_usado=gpt-4o (via redator_llm_v3)`.

**Título final produzido:** `PT destina R$ 127 milhões do Fundo Eleitoral para enfrentar desinformação na campanha de Lula`.

**Decisão:** correção de produção curta validada no caso de regressão.

### Relatório 011 — 2026-07-03 22:54 BRT — Validação de mídia em `curadoria_0979c3951d7c81ba`

**Etapa:** `executar_midia_v3_real.py`.

**Resultado:** sucesso.

**Mídia escolhida:** `midia_v3_93b62d62272911b9c42b8fa9`.

**Fonte da mídia:** `r2_ouro_pre_aprovado`.

**Personagem visual:** `Lula`.

**Validação pós-tese:** `imagem_bruta_alinhada_pos_tese`.

**Crédito/licença:** `Foto: Ricardo Stuckert / PR`, `CC BY-SA 4.0`.

**Decisão:** mídia aprovada e vinculada; bug de imagem errada não apareceu.

### Relatório 012 — 2026-07-03 22:54 BRT — Validação de mídia pronta e acabamento

**Mídia pronta:** OK.

**Resultado `v3_preparar_midia_pronta.py`:**
- `status=pronta`.
- `motivo=midia_atual_auditada_fora_cooldown`.
- `media_id=midia_v3_93b62d62272911b9c42b8fa9`.

**Acabamento SEO:** OK após executar com `POLITICA_V3_ALLOW_LLM_REAL=1`.

**Categorias finais:** `[22, 5088, 5711]`.

**Tags finais:** `[134, 264, 5602, 4024, 715, 2976]`.

**Yoast:**
- Focus: `fundo eleitoral campanha Lula`.
- Title: `PT destina R$ 127 milhões à campanha de Lula em 2026`.
- Meta description dentro da faixa.

**Observação:** a primeira execução manual de acabamento bloqueou porque faltou `POLITICA_V3_ALLOW_LLM_REAL=1`; o runner de lote deve sempre carregar esse env.

### Relatório 013 — 2026-07-03 22:55 BRT — Auditoria bloqueou por fonte original sem link

**Etapa:** `executar_auditoria_final_v3_real.py`.

**Resultado inicial:** `status_final=bloqueada`.

**Erro:** `fonte original não citada/linkada no corpo`.

**Diagnóstico:** contradição de código:
- `executar_auditoria_final_v3_real.py.validar_final()` exige que a fonte apareça no corpo.
- `v3_editor_final.inserir_atribuicao_fonte()` retornava o corpo sem inserir nada, por uma regra antiga de não adicionar rodapé automático.

**Decisão:** corrigir `v3_editor_final.py` para inserir atribuição discreta no primeiro parágrafo quando a fonte estiver ausente.

### Relatório 014 — 2026-07-03 22:56 BRT — Correção 2 aplicada: link determinístico da fonte original

**Arquivo remoto:** `/root/V3/v3_editor_final.py`.

**Backup remoto:** `/root/V3/v3_editor_final.py.bak_autocura_fonte_link_20260703_225612`.

**Patch:** `inserir_atribuicao_fonte()` agora:
- não mexe se a fonte já está citada;
- insere no primeiro parágrafo um link discreto para `url_fonte`;
- usa `target="_blank"` e `rel="noopener"`;
- preserva o corpo existente.

**Validação sintática:** `py_compile` OK.

### Relatório 015 — 2026-07-03 22:56 BRT — Reauditoria final aprovada

**Pauta:** `curadoria_0979c3951d7c81ba`.

**Comando:** `executar_auditoria_final_v3_real.py --forcar-reauditoria --confirmar`.

**Resultado:** `status_final=auditada`.

**Status finais:**
- `revisao_status=aprovada`.
- `fact_check_status=aprovado`.
- `imagem_status=aprovada`.
- Corpo final: `6473` caracteres.
- Parágrafos: `14`.

**Linha em `auditadas`:**
- `status=auditada`.
- `titulo_final=PT destina R$ 127 milhões do Fundo Eleitoral para enfrentar desinformação na campanha de Lula`.
- `media_escolhida_id=midia_v3_93b62d62272911b9c42b8fa9`.
- `auditada_em=2026-07-04 01:55:09 UTC`.

**Ledger WordPress:** `0` linhas para essa pauta. Nada foi publicado.

**Observação de risco:** fact-check LLM com websearch caiu em fallback não bloqueante por indisponibilidade/rota:
- Gemini sem crédito (`RESOURCE_EXHAUSTED`).
- `claude-sonnet-5` rejeitou `temperature`.
- Google News RSS forneceu contexto e a publicação permaneceria `pending`.

## Correções fechadas nesta rodada

1. **BUG-PROD-V3-009 reforçado:** produção curta agora tem autocura por complemento editorial anexado.
2. **BUG-AUD-V3-010 aberto/fechado:** auditoria exigia fonte original, mas editor final não inseria link; corrigido com link determinístico no primeiro parágrafo.

## Pendências após a rodada

1. **Acervo Banco Ouro/R2:** faltam imagens aprovadas para personagens legislativos e jurídicos de nicho (`Dr. Luizinho`, `Veneziano Vital do Rêgo`, etc.).
2. **Roteamento LLM da auditoria:** `gemini-flash-lite-latest` sem crédito e `claude-sonnet-5` com erro de `temperature`; precisa ajuste de rota/modelo para auditoria com websearch.
3. **Coleta muito dependente de imagem Ouro:** protege contra erro visual, mas descarta pautas boas quando não há imagem aprovada. Próxima autocura possível: buscar/cadastrar imagem sob demanda em fila humana, sem liberar automaticamente.

## Rodada de Autocura V3 — 2026-07-04

### Relatório 016 — 2026-07-04 14:23 BRT — Pré-checagem lenta antes dos 3 testes reais

**Ambiente:** remoto Tencent em `/root/V3`.

**Hora local/remota:** `2026-07-04 14:23 BRT`.

**Checagens:**
- Sem processo de lote V3 ativo antes da rodada.
- `py_compile` OK para `redator_llm_v3.py`, `v3_editor_final.py`, `executar_lote_publicacao_v3_real.py`, `executar_producao_editorial_v3_real.py`, `executar_midia_v3_real.py`, `executar_auditoria_final_v3_real.py` e `v3_preparar_midia_pronta.py`.
- Todos os testes foram executados com `--wp-status pending`.

**Regra de segurança:** validar sempre por `pauta_id` no ledger `banco_publicacao_ledger_politica_v3.db`, tabela `publicacao_ledger`.

### Relatório 017 — 2026-07-04 14:24 BRT — Teste real 1 ponta-a-ponta

**Comando:** `executar_lote_publicacao_v3_real.py --total 1 --modo ponta-a-ponta --wp-status pending --max-candidatas 80 --max-aprovadas-coleta 20 --max-por-fonte 5 --score-corte 5.5`.

**Log:** `/root/V3/logs/lotes_publicacao/lote_publish_20260704_142404.jsonl`.

**Resultado:** `preparadas=1`.

**Matéria auditada:** `curadoria_db70019b5434a172`.

**Título final:** `Flávio Bolsonaro culpa Lula por tarifaço para desviar foco de carta prejudicial aos EUA`.

**Mídia:** `midia_v3_6201ea7ec99b34e9fc8da1fc`.

**Auditoria:** `status=auditada`, `auditada_em=2026-07-04 17:28:49 UTC`.

**Ledger WordPress:** `0` linhas para a pauta. Nada publicado.

**Falha nova observada:** a produção de `curadoria_8368012894d519d3` foi bem-sucedida, mas o runner registrou `json=null` porque o stdout continha logs do roteador antes do JSON final.

### Relatório 018 — 2026-07-04 14:30 BRT — Correção 3 aplicada: parser robusto do JSON final do runner

**Arquivo remoto:** `/root/V3/executar_lote_publicacao_v3_real.py`.

**Backup remoto:** `/root/V3/executar_lote_publicacao_v3_real.py.bak_autocura_json_tail_20260704_1430`.

**Bug:** `_run()` usava regex gulosa para ler `{...}` no fim do stdout. Com logs antes do JSON, a regex capturava trecho inválido e `json.loads()` falhava.

**Patch:** criado `_json_final(stdout)`, com `json.JSONDecoder().raw_decode()` a partir das chaves finais do stdout, aceitando apenas objeto completo que termina no fim da saída.

**Validação local:** stdout com ruído antes do JSON retornou `{'status': 'executado', 'resultado': {'status': 'sucesso'}}`.

**Validação remota:** `py_compile` OK.

### Relatório 019 — 2026-07-04 14:32 BRT — Correção 4 aplicada: quarentena automática para mídia inexistente

**Arquivo remoto:** `/root/V3/executar_lote_publicacao_v3_real.py`.

**Backups remotos:**
- `/root/V3/executar_lote_publicacao_v3_real.py.bak_autocura_midia_quarentena_20260704_1438`.
- `/root/V3/executar_lote_publicacao_v3_real.py.bak_autocura_midia_descartada_20260704_1436`.

**Bug:** duas pautas antigas reapareciam em toda rodada com `preflight não executável para mídia real`.

**Causa:** `executar_midia_v3_real.py` retornava `executaria=false`, `imagens_encontradas=0` e `fonte_midia=sem_imagem_ouro_r2_aprovada_pending`.

**Primeira tentativa de cura:** status `bloqueada_midia_v3`.

**Erro revelado:** schema de `brutas.status` tem `CHECK` e aceita apenas `nova`, `classificada`, `pontuada`, `descartada`, `promovida`.

**Cura final:** usar `status='descartada'` e gravar `rejeicao_motivo='autocura_v3_midia_indisponivel: preflight não executável para mídia real'`.

**Validação:** `py_compile` OK e helper só dispara quando há erro definitivo de mídia com zero imagens.

### Relatório 020 — 2026-07-04 14:35 BRT — Teste real 2 ponta-a-ponta com autocura ativa

**Log:** `/root/V3/logs/lotes_publicacao/lote_publish_20260704_143536.jsonl`.

**Resultado:** `preparadas=1`, `falhas=10`.

**Autocuras registradas:** 5 descartes por mídia indisponível.

**Pautas antigas curadas:**
- `curadoria_3f6111d99d403def`: `status=descartada`, motivo `autocura_v3_midia_indisponivel`.
- `curadoria_972a461623e67872`: `status=descartada`, motivo `autocura_v3_midia_indisponivel`.

**Matéria auditada:** `curadoria_7aeb9896d6025f31`.

**Título final:** `Flávio Bolsonaro pede aos EUA adiamento do tarifaço e tenta minar governo Lula`.

**Mídia:** `midia_v3_ce2efe4fdee33a2174446266`.

**Auditoria:** `status=auditada`, `auditada_em=2026-07-04 17:50:30 UTC`.

**Ledger WordPress:** `0` linhas para `curadoria_7aeb9896d6025f31`. Nada publicado.

### Relatório 021 — 2026-07-04 14:51 BRT — Teste real 3 após limpeza de mídia inexistente

**Log:** `/root/V3/logs/lotes_publicacao/lote_publish_20260704_145132.jsonl`.

**Resultado:** `preparadas=0`, `falhas=5`.

**Melhora confirmada:** as pautas antigas sem nenhuma mídia não voltaram.

**Novo gargalo isolado:** cinco pautas produzidas reapareciam apenas na etapa `midia_pronta`.

**Motivos retornados por `v3_preparar_midia_pronta.py`:**
- `cooldown:4d<14d attachment=261009`.
- `cooldown:3d<14d attachment=261106`.
- `cooldown:4d<14d attachment=261009`.
- `cooldown:5d<14d attachment=260961`.
- `cooldown:2d<14d attachment=261178`.

**Diagnóstico:** não era falha transitória nem crash; eram pautas com mídia tecnicamente auditada, mas bloqueada por cooldown duro de 14 dias e sem alternativa disponível.

### Relatório 022 — 2026-07-04 14:56 BRT — Correção 5 aplicada: autocura de `midia_pronta` em cooldown definitivo

**Arquivo remoto:** `/root/V3/executar_lote_publicacao_v3_real.py`.

**Backup remoto:** `/root/V3/executar_lote_publicacao_v3_real.py.bak_autocura_midia_pronta_cooldown_20260704_1458`.

**Patch:** criado `_midia_pronta_indisponivel_definitiva(resultado)`.

**Critério de disparo:**
- `status=erro`.
- `mensagem='sem alternativa de mídia pronta'`.
- `motivo` começa com `cooldown:`.

**Ação:** marcar a pauta como `status='descartada'` e gravar `rejeicao_motivo='autocura_v3_midia_pronta_cooldown: sem alternativa de mídia pronta'`.

**Validação local:** cooldown definitivo retornou `True`; ausência genérica de mídia retornou `False`.

**Validação remota:** `py_compile` OK.

### Relatório 023 — 2026-07-04 14:56 BRT — Validação pós-cura do teste 3

**Log:** `/root/V3/logs/lotes_publicacao/lote_publish_20260704_145622.jsonl`.

**Resultado da rodada:** `preparadas=0`, `falhas=5`.

**Leitura correta do resultado:** as cinco falhas ainda aparecem no resumo da rodada porque foram tentadas antes da cura dentro do próprio ciclo; após a tentativa, todas foram removidas da fila por `status=descartada`.

**Autocuras registradas:**
- `curadoria_8368012894d519d3`.
- `curadoria_186b686ec57de39b`.
- `curadoria_7076ee24e4f13990`.
- `curadoria_c3e69dec1844b10c`.
- `curadoria_10fc2aab792159e9`.

**Status final no banco:** todas `descartada`, com motivo `autocura_v3_midia_pronta_cooldown`.

**Ledger WordPress:** `0` linhas para todas as cinco pautas. Nada publicado.

### Relatório 024 — 2026-07-04 15:00 BRT — Estado final da rodada

**Testes reais executados:** 3 testes principais mais 1 validação pós-cura.

**Matérias auditadas geradas nos testes principais:**
- `curadoria_db70019b5434a172`.
- `curadoria_7aeb9896d6025f31`.

**Correções remotas aplicadas em produção V3:**
- Parser robusto de JSON final no runner.
- Autocura de mídia real sem imagem elegível.
- Autocura de mídia pronta bloqueada por cooldown sem alternativa.

**Backups remotos criados:**
- `executar_lote_publicacao_v3_real.py.bak_autocura_json_tail_20260704_1430`.
- `executar_lote_publicacao_v3_real.py.bak_autocura_midia_quarentena_20260704_1438`.
- `executar_lote_publicacao_v3_real.py.bak_autocura_midia_descartada_20260704_1436`.
- `executar_lote_publicacao_v3_real.py.bak_autocura_midia_pronta_cooldown_20260704_1458`.

**Publicação:** nenhuma pauta nova dos testes entrou no ledger WordPress; os testes permaneceram seguros em `pending`.

## Correções fechadas em 2026-07-04

1. **BUG-RUN-V3-011:** runner não lia JSON final quando stdout tinha logs antes; fechado com `_json_final()`.
2. **BUG-SCHEMA-V3-012:** autocura tentou status fora do `CHECK` de `brutas.status`; fechado usando `descartada` com motivo técnico.
3. **BUG-MIDIA-V3-013:** pautas sem nenhuma mídia elegível reapareciam indefinidamente; fechado com descarte automático quando `executaria=false` e `imagens_encontradas=0`.
4. **BUG-MIDIA-V3-014:** pautas em cooldown duro de mídia pronta reapareciam indefinidamente; fechado com descarte automático quando `motivo` começa com `cooldown:`.

## Pendências após 2026-07-04

1. **Acervo R2/Ouro insuficiente:** ainda limita a taxa de conclusão. O lote agora deixa de travar, mas descarta pautas boas quando não há imagem segura.
2. **Resumo do lote ainda conta falhas autocuradas:** funcionalmente correto, mas pode ser melhorado para separar `falhas` de `autocuradas`.
3. **Fila de imagem sob demanda:** próxima evolução recomendada é abrir uma fila humana/curadoria para imagens ausentes, sem liberar publicação automática com imagem fraca.
