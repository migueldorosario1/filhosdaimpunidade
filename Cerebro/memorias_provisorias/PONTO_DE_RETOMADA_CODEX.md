# PONTO DE RETOMADA — Codex
# Baseado em: CEREBRO_NODE_SPRINTS_ATIVOS.md

## RETOMADA MAIS RECENTE — 2026-07-21 10:00 BRT

- Ponto detalhado: `Cerebro/Foruns/ponto_retomada_codex_operacao_20260721_1000.md`.
- A ordem de diagnóstico automático a cada 10 minutos foi **cancelada**. Não criar cron, daemon ou tarefa Scheduled para ela.
- Frente: auditoria/limpeza operacional do Cafezinho e verificação dos pipelines V4, imagens, Instagram e Baleia Azul.
- Ao retomar, primeiro conferir o servidor em modo somente leitura e comparar estado real com as decisões registradas; não presumir que mudanças relatadas em conversa continuam implantadas.
- Claude Code permanece engenheiro-chefe; Codex atua como auditor/executor por escopo delegado.

VOCE ESTAVA TRABALHANDO EM:

## S2 — Bug Flavio (posts sem featured_media) 🟡 P2
- Diagnostico feito (Fase 0). Aguardando voce codar Fix A (~25 linhas)
- Completar _resolver_imagem(): og:image → IA Flux/Ideogram → fallback 227448
- Forum: Foruns/forum_sprint2_flavio_bug_featured_media_20260527.md

## S8 — Auditor Titulos GPT 🔴 P1
- Correcoes revertidas pelo WP, logs sobrescritos
- Miguel pediu: append-only, contadores monotonico
- Forum: Foruns/forum_sprint_auditor_titulos_persistencia_e_logs_20260528.md

## CHECKUP-001 — Pausa Tencent
- Voce coordena rollback. Nao religar sem ordem do Miguel.
- Forum: Foruns/forum_investigacao_deterioracao_publicacao_20260601.md

## 2026-06-29 — Banco Ouro + V3 coleta/producao
- Frente ativa de hoje: integrar Banco Ouro ao V3 como semente de coleta e como gate de imagem antes da producao.
- Painel publico protegido do Banco Ouro: `http://43.156.151.165/midia-ouro/revisao`; usuario `cafezinho_revisor`; senha entregue no chat, nao registrar aqui.
- Estado Banco Ouro apos reversao da rodada errada: `midia_ouro=479`; hashes da rodada errada removidos; execucao 46 removida; nenhum robo de midia rodando.
- Correção aplicada: `classificar_banco_ouro_midia.py` preserva decisao humana (`approve`, `block`, `reviewed`) e nao sobrescreve aprovacao humana em reclassificacao.
- V3 coleta: `gerar_queries_coleta_banco_ouro.py` gera `/root/V3/config/queries_banco_ouro_politica.json` a partir de entidades aprovadas. `agente_coletor_fontes_v3.py` prepende queries Banco Ouro e preextrai texto dessas candidatas. `agente_coleta_v3.py` passa `query_origem` ao gate de imagem.
- Teste real finalizado: pauta `curadoria_d8d4466e6fa92553`, WP draft `260959`, titulo final `Flávio Bolsonaro ameaça transformar o STF em campo de batalha diário`, imagem Banco Ouro de Lula hash `d55db8832be56a8fbb0e562b0ef4ade5260305abf4a7d1adcd7c4ffa638a3038`, auditoria final aprovada.
- Bug aberto: `BUG-OBS-V3-001` em `memoria_bugs_ativa.md`. Requisito: alertas de texto curto/tese fragil/truncamento devem registrar tamanho, titulo, inicio do texto, tese, etapa, motivo e decisao.
- Forum atualizado: `Outros/Foruns/forum_banco_midia.md`.

### Correcao 2026-06-29 00:30 BRT — imagem pos-tese
- Miguel apontou erro correto: titulo sobre Flavio Bolsonaro nao pode usar foto de Lula.
- Patch remoto em `/root/V3/executar_midia_v3_real.py`: depois da tese, a midia reavalia a imagem Ouro herdada da bruta contra o personagem visual principal. Se nao bater, tenta substituir por outra imagem aprovada no Banco Ouro.
- Backup remoto: `/root/V3/executar_midia_v3_real.py.bak_pos_tese_imagem_ouro_20260629_002022`.
- Caso validado: `pos_tese.status=substituida_pos_tese`, `entidade_original=Lula`, `entidade_substituta=Flavio Bolsonaro`, `match_score_substituta=92.41`.
- WP draft `260959` atualizado: `featured_media=260961`, mídia V3 `midia_v3_c56126531b0120b561aa4cf0`, foto de Flavio Bolsonaro, crédito `EBC/Agência Brasil Oficial`, licença `Flickr oficial - uso editorial com crédito`.
- Auditoria final depois da troca: `auditada`, revisão aprovada, fact-check aprovado, imagem aprovada.
- Bug registrado: `BUG-MIDIA-V3-027` em `memoria_bugs_ativa.md`.

### Segundo teste 2026-06-29 00:55 BRT — pauta Lula/Quaest
- Pauta nova inserida: `curadoria_664e83a7598a1a59`.
- Titulo bruto: `Lula tem aprovação de 51% entre os que não se declaram nem petistas nem bolsonaristas`; fonte `brasildefato.com.br`; texto bruto 364 caracteres.
- Tese inicial alertou corretamente: `status_tese=pendente_auditoria_humana`, porque havia vilão abstrato (`mídia corporativa`) sem pessoa nominal.
- Brutas Plus melhorou lastro: `grau_aderencia=0.95`, `decisao_tese=confirmada`, fontes Brasil de Fato + Agência IBGE Notícias.
- Mídia aprovada: `midia_v3_129bf541e704b37cb5ad32fe`, foto de Lula Banco Ouro.
- Acabamento SEO inicialmente bloqueou por `yoast_meta_description` longa; corrigido como `BUG-SEO-V3-008`. Patch: `/root/V3/passo2e_taxonomia_seo/v3_acabamento_seo_taxonomia.py`; backup `/root/V3/passo2e_taxonomia_seo/v3_acabamento_seo_taxonomia.py.bak_codex_autocura_meta_desc_20260629_004648`.
- Mídia mostrou bug de personagem visual: plano LLM dizia Lula, determinístico dizia Instituto Genial/Quaest. Corrigido como `BUG-MIDIA-V3-028`. Patch: `/root/V3/executar_midia_v3_real.py`; backup `/root/V3/executar_midia_v3_real.py.bak_personagem_plano_visual_20260629_005217`.
- Resultado final: **sem draft WordPress**. Auditoria final ficou `bloqueada` por `vilao_identificavel=false`; fact-check e imagem estavam aprovados. Publicar só após reescrita editorial ou decisão humana de aceitar análise sem vilão personificado.

## 2026-07-09 09:35 BRT — V4 labs: Fase 4 auditfix apos parecer do Fable
- Fonte viva de trabalho: `Projeto Cafezinho Agentes/root/v4_labs/`. Nao usar `Cerebro/Foruns` como fonte viva; fóruns ficam para discussão. Futuro final auditado: `Projeto Cafezinho Agentes/root/v4/`.
- Decisão Miguel: redação nobre usa frente superluxo/frontier habilitada; DeepSeek V4 Pro é **luxo/fallback**, não primeira opção. Rota atual `v4_super_luxo_redacao`: `openai_luxo -> anthropic_luxo -> gemini_luxo -> deepseek_luxo`. xAI/Grok fica fora da rota ativa enquanto provider estiver desabilitado.
- DeepSeek V4 Pro permanece cadastrado por JSON externo, sem hardcode, com `temperature=0.1`, custo oficial DeepSeek 2026-07-09 e recibos com tokens reais. Smoke real anterior validou DeepSeek como fallback; não tratar aquele artefato histórico como rota atual.
- Agentes V4 atuais no labs: `coletor`, `processador`, `auditor`, `curador`, `produtor`, `revisor`, `fact_checker`, `imagem`, `publicador`, `observabilidade`.
- Novos módulos desta sessão: `codigo/revisao.py`, `codigo/fact_check.py`, `codigo/auditoria_final.py` e CLIs correspondentes. Novos contratos: `v4_revisao_v1.json`, `v4_fact_check_v1.json`, `v4_auditoria_final_v1.json`.
- Fluxo local atual: `curadoria_dry_run -> produzir_dry_run -> revisar_dry_run -> fact_check_dry_run -> auditar_final_dry_run -> publicar_dry_run`.
- Correção crítica: se qualquer agente gera `issues`, status bloqueado ou required field ausente, o fluxo para e `ok=false`. Artefato inválido não pode mais parecer sucesso.
- Ajustes incorporados da auditoria Fable Fase 4:
  1. `regenera_artefato_fixture_invalido=true` ficou explicitamente restrito ao laboratório; contrato de promoção exige `false` em produção e preservação append-only de artefato bloqueado.
  2. `fact_checker` agora declara `check_type=metadata_plus_text_presence_heuristic`, bloqueia fato obrigatório ausente do `texto_revisado`, preserva tokens numéricos curtos e exige números do fato travado no texto.
  3. `wordpress_publicador` registra `collection_request`; coleta pendente ou ausente vira warning no rascunho e segura apenas publicacao final/promocao.
- Política `recommended` vs `required`: documentada como provisória. Ambos compartilham gate mecânico por estágio; diferem na severidade editorial declarada. Ratificar antes de abrir publicação real.
- Validação atual: `PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts` retorna `OK 74 contract tests`; `python3 -m codigo.agentes_cli --strict` passa; `python3 -m codigo.fluxo_cli --execute` passa localmente sem WordPress real.
- Pacote de auditoria atualizado: `Projeto Cafezinho Agentes/root/v4_labs_fase4_agents_pipeline_auditfix2_20260709.tar.gz`; tamanho 156K; SHA256 `057db9a6c4259822f2ceb97fec64261d54b66f33bc3174b970113929acea7422`. Extração limpa em `/tmp/v4_labs_auditfix2_check` rodou `OK 74 contract tests`, `agentes_cli --strict` e `fluxo_cli --execute` OK.
- Auditoria Fable do auditfix2: aprovada sem ressalvas bloqueantes. Fase 4 fechada do lado técnico. Observação não bloqueante: `numeric_tokens_must_match` pode gerar falso bloqueio quando fatos travados usam datas numéricas e o texto escreve datas por extenso; observar nos próximos casos antes de mexer.
- Gates ainda fechados: `wordpress_real=false`; publicação real bloqueada; caso 261439 ainda requer confirmação/citação prudente do comentário escrito no docket USTR-2026-0331 antes de publicação real.
- Próximo passo seguro: continuar Fase 5 em shadow/dry-run ou pedir auditoria GPT 5.5 do mesmo tarball. Não promover para `root/v4/` sem auditoria e ordem explícita.

## 2026-07-09 13:15 BRT — V4 labs: Fase 5 promocao/preflight
- Fase 5 implementada em `v4_labs`, sem promover para `root/v4`, sem chamada LLM real e sem WordPress real.
- Novos arquivos: `contratos/v4_promocao_preflight_v1.json`, `codigo/promocao.py`, `codigo/promocao_cli.py`, `AUDITOR_NOTE_FASE5_PROMOCAO_PREFLIGHT_20260709.md`.
- Agente tecnico novo: `promotor`, validado em `agentes_cli --strict`, sem leitura/escrita de camadas e sem promocao automatica.
- Preflight checa: caminhos obrigatorios, ausencia de symlink/cache/env/segredos, min de testes, WordPress real fechado, gate de `collection_request`, fact-check textual/numerico, clausula de regeneracao proibida em producao e politica `recommended/required` documentada.
- Estado atual correto: `promocao_pendente_de_cura`, com issues `recommended_required_policy_ratified` e `collection_request_publicacao_real_resolvida`; warning `gpt55_audit_recommended_before_promotion`.
- Interpretacao: todos os gates tecnicos passam, mas promocao para `root/v4` esta pendente de cura por pendencias editoriais reais. Isso nao impede rascunho editorial.
- Validacao local e standalone: `OK 76 contract tests`; `agentes_cli --strict` OK; `fluxo_cli --execute` OK; `promocao_cli --execute` retorna bloqueado pelos dois gates esperados.
- Pacote Fase 5: `Projeto Cafezinho Agentes/root/v4_labs_fase5_promocao_preflight_20260709.tar.gz`; tamanho 164K; SHA256 `042024384d987f05f9b7bbb077b15951f1a7e3f6836387b704be09011fa9d77b`.
- Proximo passo: mandar pacote Fase 5 para Fable/GPT 5.5 se Miguel quiser auditoria, ou resolver pendencias editoriais (ratificar `recommended/required`; resolver/citar limite do docket USTR-2026-0331).

### Auditfix Fase 5 — 2026-07-09
- Auditoria adversarial apontou: secret scan nao pegava `sk-` generico; `decisions.*=true` nao exigia evidencia; `contract_tests_min` era nome impreciso para contagem estatica.
- Corrigido: padrao `sk-[A-Za-z0-9_\\-]{20,}`; evidencia obrigatoria para decisoes true (`by`, `at`, e `forum_doc`/`audit_doc`/`reason`); check renomeado para `contract_tests_defined_min`.
- Validacao local e standalone: `OK 78 contract tests`; `agentes_cli --strict` OK; `fluxo_cli --execute` OK; `promocao_cli --execute` segue bloqueado por `recommended_required_policy_ratified` e `collection_request_publicacao_real_resolvida`.
- Pacote auditfix: `Projeto Cafezinho Agentes/root/v4_labs_fase5_promocao_preflight_auditfix_20260709.tar.gz`; tamanho 164K; SHA256 `68f7d1eb9f025be2f19383368219e6b93856d444f3162c71e601adce315cd976`.
- Auditoria Fable do auditfix: aprovada sem ressalvas. Fable confirmou os seis pontos da carta e repetiu os ataques de `sk-` generico e flip de decision sem evidencia; ambos agora bloqueiam corretamente.
- Fable considera defensavel a politica atual `recommended`/`required` com mesmo gate mecanico e severidade editorial diferente. Alternativa registrada, se Miguel quiser diferenciar: `recommended` liberavel por editor-chefe com justificativa auditavel; `required` so libera com pendencia factual resolvida.

### Correcao de cultura V4 — rascunho primeiro / autocura — 2026-07-09
- Miguel corrigiu a tendencia da Trindade de transformar pendencias em bloqueios demais. Nova regra operacional: rascunho editorial deve seguir com relatorio, warnings e cura/autocura sempre que nao houver risco irreversivel.
- Bloqueio duro fica reservado para publicacao final, promocao para `root/v4`, acao destrutiva, segredo/credencial exposta, credencial necessaria ausente para acao real de rede, ou risco juridico/operacional irreversivel.
- Fonte viva: `Projeto Cafezinho Agentes/root/v4_labs/`.
- Novo contrato: `contratos/v4_rascunho_primeiro_v1.json`.
- Ajustes aplicados:
  - `wordpress_publicador.py`: `WordPressPublishAttempt` agora inclui `warnings`; rascunho/dry-run sem `featured_media` ou `curadoria_id` vira warning, nao erro fatal.
  - `fluxo.py`: publicar dry-run sem midia auditada segue com `imagem_destacada_pendente` e `featured_media_id=None`.
  - `promocao.py`: status com pendencias virou `promocao_pendente_de_cura`, para deixar claro que e gate de promocao, nao de rascunho.
  - Contratos atualizados: `v4_wordpress_publicador_v1.json`, `v4_fluxo_dry_run_v1.json`, `v4_promocao_preflight_v1.json`.
- Validacao atual: `OK 79 contract tests`; `agentes_cli --strict` OK; `fluxo_cli --execute` OK; `promocao_cli --execute` retorna `promocao_pendente_de_cura`.
- Pacote validado em extracao limpa: `Projeto Cafezinho Agentes/root/v4_labs_fase5_rascunho_primeiro_20260709.tar.gz`; SHA256 `82a1542e995b042f75521eb8cde8f535a2ed428653a06b5dadde1d2039c607f9`; tamanho 165K.
- Forum: `Cerebro/Foruns/forum_v4_rascunho_primeiro_autocura_20260709.md`.

### Auditfix Fable do rascunho-primeiro — 2026-07-09
- Retificacao de proveniencia: Fable nao diagnosticou "cultura de bloqueio"; a filosofia rascunho-primeiro veio da orientacao do Miguel e foi adotada por merito proprio. Fable vinha defendendo gates duros em pontos criticos.
- Fable aprovou a parte dry-run/lab, mas vetou o afrouxamento do caminho real WordPress. O pacote `v4_labs_fase5_rascunho_primeiro_20260709.tar.gz` esta substituido e nao deve ser usado para auditoria.
- Corrigido em `v4_labs`: qualquer chamada real ao WordPress (`draft`, `pending`, `publish`) mantem gates duros para `collection_request`, `curadoria_id`, `featured_media`, `manifesto`, encoding e env. Rascunho-primeiro vale para dry-run/laboratorio.
- `pending` removido de `real_publish.draft_statuses`; continua permitido como status real, mas com gates duros.
- `v4_rascunho_primeiro_v1.json` agora declara escopo: `dry_run_laboratorio=pendencias_viram_warnings`; `wordpress_real_draft_pending_publish=gates_duros_ate_ratificacao_explicita_do_forum`.
- Testes adversariais adicionados: real draft com campos criticos ausentes nao chama `_post_wordpress`; real draft com `collection_request required/publicacao_real` nao chama `_post_wordpress`.
- Validacao atual: `OK 81 contract tests`; agentes OK; fluxo OK; preflight `promocao_pendente_de_cura`.
- Pacote novo validado em extracao limpa: `Projeto Cafezinho Agentes/root/v4_labs_fase5_rascunho_primeiro_auditfix_fable_20260709.tar.gz`; SHA256 `d46fdbe7b78e4f25930417166cc08f16da4dbf25afcfe3b030a3eee8fe24124c`; tamanho 166K.
- Adendo Fable: proveniencia/autoria resolvida. Se Miguel quiser liberar rascunho real WordPress com pendencias no futuro, isso deve ser ratificado no forum com decision evidence. Estado atual segue conservador: tolerancia so dry-run/lab; WordPress real duro.

### Ratificacao da politica conservadora — 2026-07-09
- Miguel aceitou explicitamente sermos conservadores. `recommended_required_policy_ratified=true` em `contratos/v4_promocao_preflight_v1.json`, com evidencia apontando para `Cerebro/Foruns/forum_v4_rascunho_primeiro_autocura_20260709.md`.
- Preflight atual nao tem mais issue de politica. Issue restante: `collection_request_publicacao_real_resolvida`. Warning: `gpt55_audit_recommended_before_promotion`.
- Validacao em pacote limpo: `OK 81 contract tests`; agentes OK; fluxo OK; preflight `promocao_pendente_de_cura`.
- Pacote valido mais recente: `Projeto Cafezinho Agentes/root/v4_labs_fase5_rascunho_primeiro_policy_ratified_20260709.tar.gz`; SHA256 `bdbccf94821f5f41ba18367f51694a893806cc79caa3c811cb1d1437d573bee1`; tamanho 166K.
- O que falta antes de promocao para `root/v4`: resolver/tratar `collection_request` do caso 261439 e decidir se quer auditoria GPT 5.5. Depois disso, promocao exige `human_promotion_authorized=true` com evidencia.

### Auditfix fail-closed collection_request — 2026-07-09
- Fable auditou o pacote ratificado e aprovou dry-run/lab. Achado novo: `collection_request` com `status` desconhecido ou `required_before` desconhecido passava em silencio no publicador/preflight.
- Corrigido: `wordpress_publicador._collection_request_issues` e `promocao._collection_gates` agora falham fechado para valores desconhecidos.
- Valores conhecidos: `status={none,resolved,recommended,required}`; `required_before={none,shadow_redacao,redator_real_llm,publicacao_real}`.
- Testes adicionados:
  - `test_wordpress_publicador_collection_request_fail_closed_valores_desconhecidos`
  - `test_promocao_preflight_collection_request_fail_closed_valores_desconhecidos`
- Validacao: `OK 83 contract tests`; agentes OK; fluxo OK; preflight ainda tem apenas `collection_request_publicacao_real_resolvida`.
- Pacote valido mais recente: `Projeto Cafezinho Agentes/root/v4_labs_fase5_collection_failclosed_20260709.tar.gz`; SHA256 `2041b7e3f582af11a22b638a20e9ac2f21ac6b4744f216ffa22aa56f268d2c9d`; tamanho 167K; validado em extracao limpa.

### Auditfix F5.2 tipos invalidos — 2026-07-09
- Fable aprovou F5.1 e achou residual menor: `collection_request.status` ou `required_before` nao-string causava TypeError/stack trace.
- Corrigido: publicador e preflight validam tipo antes de `in`/pertencimento. Valor malformado vira issue auditavel, nao derruba o relatorio.
- Testes adicionados:
  - `test_wordpress_publicador_collection_request_nao_string_vira_issue`
  - `test_promocao_preflight_collection_request_nao_string_vira_issue`
- Validacao: `OK 85 contract tests`; agentes OK; fluxo OK; preflight ainda tem apenas `collection_request_publicacao_real_resolvida`.
- Pacote valido mais recente: `Projeto Cafezinho Agentes/root/v4_labs_fase5_collection_typefix_20260709.tar.gz`; SHA256 `9f7954dfe07ae148d2e3f6068372e5bc4b7c0769d65b0020d3415534b901db65`; tamanho 167K; validado em extracao limpa.

### Fechamento mecanico Fase 5 por Fable — 2026-07-10
- Carta: `Cerebro/Foruns/carta_fable_adendo_final_fase5_typefix_20260710.md`.
- Fable verificou o pacote `v4_labs_fase5_collection_typefix_20260709.tar.gz` e encerrou formalmente a auditoria mecanica da Fase 5.
- Contrato atualizado: `decisions.fable_fase5_mechanical_closed=true` com `audit_doc` apontando para a carta.
- Preflight atual: issue unico `collection_request_publicacao_real_resolvida`; warning `gpt55_audit_recommended_before_promotion`; WordPress real fechado; promocao real nao executada.
- Proximo passo critico nao e codigo: decisao editorial sobre docket `USTR-2026-0331` do caso 261439, registrada com evidencia de cura (`by`, `at`, documento, razao). Depois, 2-3 casos reais adicionais em dry-run antes de promocao.
- Pacote vigente: `Projeto Cafezinho Agentes/root/v4_labs_fase5_mechanical_closed_20260710.tar.gz`; SHA256 `0e509a1c679a7b0dd935ef7eb1dd707af86452fd9f7ca2a3f23b4bbd6cd19e18`; tamanho 167K; validado em extracao limpa.
- Confirmacao final Fable: pacote `mechanical_closed` verificado em 2026-07-10; incorporacao fiel, escopo minimo, 85 testes executados, evidencia validada pelo gate. Nao pedir nova auditoria mecanica F5 salvo mudanca de codigo/contrato.

### Decisao editorial USTR-2026-0331 — 2026-07-10
- Miguel escolheu a opcao 2: seguir com prudencia sem depender do comentario escrito detalhado do docket `USTR-2026-0331`.
- Regra editorial aplicada ao caso `v4_real_001`: usar transcricao oficial do USTR, Federal Register e fontes auditadas; nao afirmar conteudo do comentario escrito nao localizado; se o docket for citado, declarar a limitacao.
- `collection_request` nos 4 artefatos do caso foi curado para `status=resolved`, `required_before=none`, `resolved_by=Miguel`, `resolution_type=editorial_prudence`.
- Validacao local apos cura: `OK 85 contract tests`; agentes OK; fluxo OK; preflight `promocao_shadow_aprovada`, `issues=[]`, warning `gpt55_audit_recommended_before_promotion`; WordPress real falso; promocao real nao executada.
- Pacote curado gerado e validado em extracao limpa: `Projeto Cafezinho Agentes/root/v4_labs_fase5_collection_cured_20260710.tar.gz`; SHA256 `580384b8898e3ee0f740271c1dd2dbf6256dec7dd05b20589f5c5f95a0576081`; tamanho 168K.
- Validacao do pacote curado: `OK 85 contract tests`; agentes OK; fluxo OK; preflight `promocao_shadow_aprovada`; `issues=[]`; warning `gpt55_audit_recommended_before_promotion`; WordPress real falso; external_call falso; promocao real nao executada.
- Proximo passo: rodar 2-3 casos reais adicionais em dry-run antes de qualquer promocao para `root/v4`; auditoria GPT 5.5 continua opcional/recomendada pelo preflight.

### Fase 6 multi-case dry-run — 2026-07-10
- Rodados 3 casos adicionais: `v4_real_002` Jason Miller/documentos judiciais, `v4_real_003` IBGE PIM abril 2026, `v4_real_004` IBGE PIA-Produto 2024.
- Resultado: 3/3 `ok=true`; fluxo completo `curadoria -> producao -> revisao -> fact_check -> auditado_final -> publicado_dry_run`; `issues=[]`; warnings apenas de imagem auditada ausente.
- Achados corrigidos: curadoria confundia `industria` com `USTR` por substring; pauta economica herdava linguagem de pressao externa; produtor mock nao passava fatos travados suficientes ao fact-check.
- Validacao em extracao limpa: `OK 88 contract tests`; agentes OK; fluxo OK; preflight `promocao_shadow_aprovada`; `issues=[]`; warning `gpt55_audit_recommended_before_promotion`; WordPress real falso; external_call falso; promocao real nao executada.
- Pacote vigente: `Projeto Cafezinho Agentes/root/v4_labs_fase6_multicase_dryrun_20260710.tar.gz`; SHA256 `44a937265590639e88884f1d6de446e1a4c64a13f7a7ad9e8aefdc217e0424f8`; tamanho 197K.
- Proximo passo sugerido: pedir auditoria Fable/GPT 5.5 do pacote Fase 6 ou iniciar Fase 7 com um gerenciador multi-item mais formal, sem contratos temporarios.

### Retomada Codex — 2026-07-10 01:21 BRT
- Retomada revalidou o pacote Fase 6 localmente em `Projeto Cafezinho Agentes/root/v4_labs/`.
- Checks rodados: `OK 88 contract tests`; `agentes_cli --strict` OK; `fluxo_cli --execute` OK; `promocao_cli --execute` retornou `promocao_shadow_aprovada`, `issues=[]`, warning unico `gpt55_audit_recommended_before_promotion`.
- SHA confirmado do pacote vigente: `44a937265590639e88884f1d6de446e1a4c64a13f7a7ad9e8aefdc217e0424f8`.
- Nao houve edicao de codigo, WordPress real, external call, publicacao externa nem promocao para `root/v4`.
- Forum atualizado: `Cerebro/Foruns/forum_v4_fase6_multicase_dryrun_20260710.md`.
- Carta de auditoria criada: `Cerebro/Foruns/carta_fable_gpt55_auditoria_fase6_multicase_20260710.md`; canal pontuado em `Cerebro/Foruns/canal_trindade.md`.
- Pedido de veredito: `APROVADO_PARA_FASE7_LAB` ou `BLOQUEADO_PARA_FASE7_LAB`; nao e pedido de producao.
- Proximo passo seguro permanece: aguardar/receber auditoria Fable/GPT 5.5 do pacote Fase 6 ou iniciar Fase 7 em laboratorio com gerenciador multi-item formal, mantendo WordPress real fechado.

### Auditoria Fable Fase 6 recebida — 2026-07-10
- Carta local: `Cerebro/Foruns/carta_fable_auditoria_fase6_multicase_20260710.md`.
- Veredito: `APROVADO_PARA_FASE7_LAB`, nao para producao.
- F6.1: Fable pediu confirmacao verbatim de Miguel e `resolution_doc` correto nos 4 artefatos do caso `v4_real_001`.
- Miguel confirmou: "sim a decisão editorial foi minha." Declaracao registrada em `Cerebro/Foruns/forum_v4_fase6_multicase_dryrun_20260710.md`.
- `resolution_doc` corrigido em:
  - `Projeto Cafezinho Agentes/root/v4_labs/dados/curadoria/v4_real_001.curadoria.json`
  - `Projeto Cafezinho Agentes/root/v4_labs/dados/producao_shadow/v4_real_001.shadow_redacao.json`
  - `Projeto Cafezinho Agentes/root/v4_labs/dados/producao_shadow/v4_real_001.redator_real_preflight.json`
  - `Projeto Cafezinho Agentes/root/v4_labs/dados/producao_shadow/v4_real_001.redator_real.json`
- F6.1 fechado para Fase 7 lab.
- F6.2 permanece como criterio de Fase 7: provar generalizacao com `curadoria_tese.py` congelado e casos novos entre editorias.
- Correcao de reporte: houve chamadas LLM externas em laboratorio; o correto e declarar `wordpress_real=false`, `external_publish=false`, `promocao_real_executada=false`, nao "sem LLM real".
- Pacote F6.1 fechado: `Projeto Cafezinho Agentes/root/v4_labs_fase6_f61_closed_20260710.tar.gz`; SHA256 `9e53151554fa912d6e3bca5374fecf24e997ff0fe543b684538637a7b1dc0440`; tamanho 197K.
- Diff de `v4_labs` contra pacote Fase 6 auditado esta restrito aos 4 artefatos acima, com troca unica de `resolution_doc`.
- Validacao em extracao limpa do pacote F6.1 fechado: `OK 88 contract tests`; agentes OK; fluxo OK; preflight `promocao_shadow_aprovada`, `issues=[]`, warning `gpt55_audit_recommended_before_promotion`; WordPress real falso; promocao real nao executada.

### Follow-up USTR-2026-0331 — PDF integral localizado — 2026-07-10
- Nova busca localizou PDF integral do comentario escrito atribuido a Flavio Bolsonaro no docket `USTR-2026-0331`.
- Portal oficial `comments.ustr.gov/s/` continua inacessivel por leitura simples (`CSS Error`); nao afirmar download direto do USTR.
- Duas copias jornalisticas baixadas sao byte a byte identicas:
  - `https://conexaomt.com/wp-content/uploads/2026/07/FLAVIO_BOLSONARO_USTR-2026-0331-00130718-CAT-17865-Public-Document.pdf`
  - `https://img.band.com.br/static/2026/07/02/carta-de-flavio-aos-eua-131626.pdf`
- SHA256 do PDF: `129b1a648c5567070fd73429d4cac2f05c81190a89febffa6da1ddb5745049cd`; 86 paginas; 1782765 bytes.
- Artefatos adicionados:
  - `Projeto Cafezinho Agentes/root/v4_labs/dados/auditado/v4_real_001.ustr_2026_0331_written_comment.pdf`
  - `Projeto Cafezinho Agentes/root/v4_labs/dados/auditado/v4_real_001.ustr_2026_0331_written_comment.json`
- Prudencia F6.1 permanece valida; nao reabrir os 4 `collection_request` curados sem ordem explicita.
- Follow-up registrado como `collection_followup`: PDF integral obtido por espelhos; URL/recibo oficial direto ainda pendente; usar para upgrade editorial e comparar carta escrita x testemunho oral do Painel 8.
- Pacote follow-up: `Projeto Cafezinho Agentes/root/v4_labs_fase6_ustr0331_pdf_followup_20260710.tar.gz`; SHA256 `33d047800d5d2e8b53147fadd09c95236e82f552e1ac9720afa1094b94c284cc`; tamanho 989K.
- Diff contra F6.1 fechado restrito a `dados/auditado/v4_real_001.ustr_2026_0331_written_comment.pdf` e `.json`.
- Validacao em extracao limpa: `OK 88 contract tests`; agentes OK; fluxo OK; preflight `promocao_shadow_aprovada`, `issues=[]`, warning `gpt55_audit_recommended_before_promotion`.

### Fase 7 multi-item lab — 2026-07-10
- Fonte viva continua: `Projeto Cafezinho Agentes/root/v4_labs/`. Nao promover para `root/v4` sem ordem explicita.
- Objetivo da fase: produzir evidencia mecanica do F6.2 com casos novos e `curadoria_tese.py` congelado.
- Novos arquivos:
  - `contratos/v4_multi_item_lab_v1.json`
  - `codigo/multi_item.py`
  - `codigo/multi_item_cli.py`
- Ajustes:
  - `codigo/test_contracts.py` agora cobre gerenciador multi-item e deteccao de curadoria alterada.
  - `codigo/fluxo.py` preserva `fontes` quando o fixture traz esse campo; nao volta a preencher `fontes: null` em fixture antiga.
- Casos rodados: `v4_real_005` (`v4_internacional`), `v4_real_006` (`v4_ciencia_tecnologia_ia`), `v4_real_007` (`v4_cultura`).
- Resultado do lote: `multi_item_lab_ok`; 3/3 OK; `issues=[]`; warnings apenas de imagem auditada ausente no dry-run.
- Curadoria congelada:
  - `codigo/curadoria_tese.py`: `c1c5f3f592a537089030328fbd8906209de727ae5a8e4ae965eda3256c52a521` antes/depois.
  - `contratos/v4_curadoria_tese_v1.json`: `c06885ce89cb4ef5f227c378f6257d67a57ce48155002afeb519beb9a9e8dc3f` antes/depois.
- Validacao limpa: `OK 90 contract tests`; agentes strict OK; fluxo OK; promocao shadow aprovada; `issues=[]`; sem pycache/pyc.
- Seguranca: houve roteamento/recibos LLM em laboratorio; nao declarar "sem LLM real". Declarar corretamente: `external_publish=false`, `wordpress_real=false`, `promocao_real_executada=false`, `root/v4` intocado.
- Pacote Fase 7: `Projeto Cafezinho Agentes/root/v4_labs_fase7_multi_item_lab_20260710.tar.gz`; SHA256 `22e1e452c192a32a3bd55c7ec73d025066345c77ddbad2638a05aff475c2b2ef`; tamanho 1011K.
- Forum: `Cerebro/Foruns/forum_v4_fase7_multi_item_lab_20260710.md`.
- Proximo passo seguro: pedir auditoria Fable/GPT 5.5 do pacote Fase 7. Ainda nao promover para producao.

### Auditoria Fable Fase 7 — 2026-07-10
- Carta local: `Cerebro/Foruns/carta_fable_auditoria_fase7_multi_item_20260710.md`.
- Veredito: `APROVADO para continuidade em laboratório`.
- F6.2 mecanico fechado: Fable verificou SHA do pacote, congelamento da curadoria contra copias auditadas da Fase 6, batch `multi_item_lab_ok` reexecutado, `OK 90 contract tests`, agentes/fluxo/preflight OK.
- Guards seguem: sem publicacao externa, sem WordPress real, sem promocao real; houve roteamento/recibos LLM em laboratorio, reportar assim.
- F6.1: auditor marcou provisoriamente porque nao teve acesso ao forum da Fase 6; localmente o forum existe e contem a decisao verbatim de Miguel. Em nova auditoria externa, anexar/fornecer esse forum.
- USTR follow-up: PDF confirmado, mas metadados sugerem reexportacao por espelho (`LibreOffice 24.2`, criacao 2026-07-02). Manter busca de URL/recibo oficial direto.
- Achado novo F7.1, medio/editorial: curadoria heuristica congelada nao generalizou para editorias fora da familia politica/economia. `v4_real_007` cultura/streaming recebeu tese de template industrial/IBGE, e o pipeline reportou `ok=true` sem flagrar incoerencia.
- Decisao F7.1 ratificada por Miguel em 2026-07-10: "ok, ratifico". Politica interina aceita: ate existir curadoria propria por editoria ou gate forte de coerencia, teses fora-de-familia sao rascunho obrigatoriamente revisado por humano, sem promocao como `ok` editorial automatico.
- Recomendacao minima de codigo para a proxima rodada lab: gate de coerencia tese x editoria/tema, para desalinhamento virar issue/warning auditavel.

### Forum de linguagem cultural — 2026-07-10
- Forum criado: `Cerebro/Foruns/forum_v4_linguagem_analise_objetos_culturais_20260710.md`.
- Objetivo: construir linguagem propria para analise de objetos culturais antes de transformar em contrato/gate.
- Direcao editorial: ler objeto cultural como obra primeiro, com roteiro, direcao, autoria, producao, atuacao, dramaturgia, forma audiovisual, comparacao estetica e tradicao de genero; industria/mercado entram como contexto quando relevante.
- Refino externo incorporado:
  - gate por keyword e apenas warning barato, nao prova de coerencia;
  - arquitetura deve ser parametrizada por editoria, nao `if cultura` isolado;
  - separar `fatos_verificaveis` de `juizos_esteticos_fundamentados`;
  - `risco_spoiler` obrigatorio por item;
  - dialogos/letras devem ter citacao minima, preferindo parafrase e analise;
  - `v4_real_007` vira regressao canonica.
- Ratificacao de Miguel registrada no forum: "ok, ratifico". F7.1 deixa de ser pendencia de decisao e vira diretriz de desenvolvimento em laboratorio.

### Gate F7.1 implementado em lab — 2026-07-10
- Novo contrato: `Projeto Cafezinho Agentes/root/v4_labs/contratos/v4_editoria_coerencia_v1.json`.
- Novo modulo: `Projeto Cafezinho Agentes/root/v4_labs/codigo/coerencia_editorial.py`.
- Integracao: `codigo/multi_item.py` carrega a curadoria gerada e anexa `editorial_coherence` ao relatorio do lote.
- Testes adicionados em `codigo/test_contracts.py`; contagem atual `OK 92 contract tests`.
- Gate e parametrizado por editoria, warning-only em laboratorio, e avalia o miolo da tese depois de `revela-se que`.
- `curadoria_tese.py` nao foi alterado; curadoria politica/economia nao foi mexida.
- Resultado do batch: `multi_item_lab_ok`, `issues=[]`, `editorial_review_required_items=["v4_real_006","v4_real_007"]`.
- Warnings:
  - `v4_real_006`: `tese_ia_desalinhada_com_objeto`;
  - `v4_real_007`: `tese_cultura_desalinhada_com_objeto`.
- Pacote: `Projeto Cafezinho Agentes/root/v4_labs_fase7_f71_editorial_coherence_gate_20260710.tar.gz`; SHA256 `6a67d25e64483347aed443fb590833466d4e82c7c6c6295744752729edda549c`; tamanho 1015K.
- Validacao limpa: sem pycache/pyc; `OK 92 contract tests`; agentes strict OK; fluxo OK; preflight `promocao_shadow_aprovada`; batch multi-item OK com warnings editoriais.
- Proximo passo: criar curadoria propria por editoria, com foco inicial em `v4_curadoria_cultura_v1.json` ou rota LLM de curadoria cultural; re-rodar `v4_real_007` ate nao disparar `tese_cultura_desalinhada_com_objeto`.

### F7.1 aprovado e F7.2 `tese_ausente` corrigido — 2026-07-10
- Auditoria externa do gate F7.1 aprovada: SHA `6a67d25e64483347aed443fb590833466d4e82c7c6c6295744752729edda549c`, curadoria congelada, gate lateral, batch `multi_item_lab_ok`, revisao humana sinalizada para `v4_real_006` e `v4_real_007`.
- Miguel ratificou formalmente a politica interina: teses fora das familias calibradas sao rascunho com revisao humana obrigatoria ate existir curadoria propria por editoria ou gate forte de coerencia.
- F7.2 corrigiu edge warning-only: tese vazia ou `teses_candidatas` ausente agora gera warning `tese_ausente`, com `human_review_required=true` quando aplicavel.
- Arquivos alterados no lab: `contratos/v4_editoria_coerencia_v1.json`, `codigo/coerencia_editorial.py`, `codigo/test_contracts.py`, alem dos relatorios reexecutados em `dados/promocao/`.
- Validacao local: `OK 93 contract tests`; agentes strict OK; fluxo OK; preflight `promocao_shadow_aprovada`, `issues=[]`; batch `multi_item_lab_ok`, `issues=[]`; sem WordPress real, sem publicacao externa, sem promocao real.
- Pacote F7.2: `Projeto Cafezinho Agentes/root/v4_labs_fase7_f72_tese_ausente_gate_20260710.tar.gz`; SHA256 `46254c849f3cd656f61bc1d8f8e429436820c0f255b5aaf46f9e979e06fcdb5c`; tamanho `1015K`.
- Validacao em extracao limpa: sem `__pycache__`/`.pyc`; `OK 93 contract tests`; agentes OK; fluxo OK; preflight OK; `multi_item_lab_ok`; `editorial_review_required_items=["v4_real_006","v4_real_007"]`.
- Proximo passo seguro: iniciar curadoria propria por editoria, primeiro cultura, usando `v4_real_007` como regressao canonica. Nao promover para `root/v4` sem ordem humana explicita.

### Dossie V4 para GPT 5.6 Sol — 2026-07-10
- Criado subdiretorio: `Cerebro/Foruns/gpt_5_6_sol/v4_qualidade_texto_curadoria_20260710/`.
- Foco: qualidade do texto, curadoria forte, tese editorial, linguagem por editoria, curadoria cultural e criterios de aceite.
- Conteudo: 138 arquivos; foruns essenciais, auditorias, contratos editoriais, codigo minimo de contexto, amostras reais `v4_real_001` a `v4_real_007`, relatorios lab e instrucoes.
- Arquivos orientadores: `00_instrucoes/LEIA_PRIMEIRO.md`, `00_instrucoes/CARTA_DE_ABERTURA_PARA_GPT_5_6_SOL.md` e `00_instrucoes/PROMPT_PARA_GPT_5_6_SOL.md`.
- Zip para upload no ChatGPT normal: `Cerebro/Foruns/gpt_5_6_sol/v4_qualidade_texto_curadoria_20260710.zip`.
- SHA256 do zip: `13609692d54037b19d9b313ce8d5dee4c1db3bc4578beaee5d8ae72a2d53fe7e`.
- Instrucao central ao GPT 5.6: nao propor publicacao real; avaliar e melhorar curadoria/texto em laboratorio.

### Fase 8 — fundacao da curadoria cultural forte — 2026-07-10
- Parecer GPT 5.6 Sol incorporado em laboratorio lateral. Diagnostico operacional: validade mecanica nao equivale a julgamento editorial.
- Fonte viva permanece `Projeto Cafezinho Agentes/root/v4_labs/`; `root/v4`, WordPress real, publicacao externa e promocao real seguem intocados.
- Novos contratos: `v4_claims_v1.json`, `v4_curadoria_cultura_v1.json`, `v4_avaliacao_curadoria_v1.json` e `v4_cultura_lab_v1.json`.
- Novos modulos: `claims.py`, `evidencias.py`, `curadoria_cultura.py`, `avaliacao_curadoria.py`, `cultura_lab.py` e CLI.
- Taxonomia separa fato, declaracao, hipotese, juizo interpretativo, juizo estetico, instrucao e lacuna. Apenas fato/declaracao com evidencia resolvida podem ser travados.
- `v4_real_007` foi classificado como `politica_cultural_plataformas` e terminou honestamente em `estado_editorial=coleta_obrigatoria`, zero teses, escolha nula e nenhuma tentativa F8 de redacao/producao.
- Lacunas do 007: `regra_ou_documento_concreto`, `mecanismo_de_circulacao_documentado`, `dois_objetos_ou_criadores_afetados` e `posicao_de_ator_relevante`.
- O avaliador e modulo separado e resolve evidencia novamente, mas ainda e estrutural: `semantic_evaluation_complete=false` e os oito escores ficam `null`. Teto automatico com material suficiente: `rascunho_revisao_humana`.
- Guards adversariais cobrem referencia fantasma, URL sem snapshot, locator invalido, evidencia duplicada, tese clonada, keyword stuffing, tipos malformados e manifestos de obra sem hash/conteudo.
- Redatores shadow e real bloqueiam `coleta_obrigatoria` antes de gerar titulo, prompt ou texto.
- Validacao local e em extracao limpa: `OK 114 contract tests`; 11 agentes validos; fluxo OK; lote F7 3/3; cultura lab OK; 17/17 fontes congeladas; sem symlink/cache/pyc/env/segredo.
- Preflight esperado: `promocao_pendente_de_cura`, issue unica `collection_request_publicacao_real_resolvida`, warning `gpt55_audit_recommended_before_promotion`; WordPress real falso.
- Revisoes adversariais separadas de codigo e artefatos aprovaram a fundacao estrutural sem hard issue. Isto nao e aprovacao semantica/editorial.
- Pacote: `Projeto Cafezinho Agentes/root/v4_labs_fase8_curadoria_cultura_foundation_20260710.tar.gz`; SHA256 `60198c4e8a07bdb9af5ede63380921b6aa012d5bde3fef6713fdf5ffba3d1825`; tamanho `1072162 bytes`.
- Forum: `Cerebro/Foruns/forum_v4_fase8_curadoria_forte_cultura_20260710.md`.
- Proximo passo seguro: coletar os quatro elementos reais faltantes do 007 e materializa-los como claims auditaveis; em paralelo, montar pacotes auditados para os outros cinco casos culturais. Nao gerar tese nem texto do 007 antes disso e nao promover para `root/v4`.

### Fase 9A curta — prova de retorno do 007 — 2026-07-10
- Escopo foi reduzido por decisao editorial: somente duas correcoes mecanicas, coleta/reexecucao do 007 e parada para auditoria. Fases 9B a 9E nao foram iniciadas.
- Correcoes mecanicas concluidas: check renomeado para `collection_request_pendencias_por_estagio`; cultura e multi-item usam a lista unica `contratos/v4_frozen_sources_v1.json`, com 37 fontes nos dois relatorios novos.
- Coleta F9A materializada em `dados/auditado/v4_real_007.coleta_f9a.json`, com snapshots locais, URLs, data de acesso, hashes e locators. Regra, mecanismo e posicao historica de ator foram documentados.
- A primeira passagem produziu falso 4/4 ao confundir circulacao medida de `Caramelo` e `Os Donos do Jogo` com prova de efeito de cota, destaque ou recomendacao. Auditoria adversarial recusou o rotulo; erro corrigido antes do fechamento.
- Resultado final legitimo B: `estado_editorial=coleta_obrigatoria`; satisfeitos 3/4; falta exatamente `dois_objetos_ou_criadores_afetados`; `teses_candidatas=[]`; coleta requerida antes de `shadow_redacao`; nenhuma redacao, producao, publicacao ou promocao.
- Guard anti-falso-positivo: objeto afetado exige `affected_by` com claim de mecanismo resolvido, tipo de efeito controlado e enunciado do efeito. Curador e avaliador independente reaplicam a regra. Relabelagem simples e proposta forjada sem relacao ficam em coleta.
- Revisao interna final aprovou o caminho corrigido sem achados no escopo. Claims de regra/status estao atomicos; contrato aceita A/B e nao predetermina resultado.
- Validacao local e em extracao limpa: `OK 118 contract tests`; 11 agentes validos; fluxo OK; F9A reproduz resultado B; multi-item 3/3; sem cache/pyc/symlink. Preflight esperado: `promocao_pendente_de_cura`, issue unica `collection_request_pendencias_por_estagio`.
- Pacote: `Projeto Cafezinho Agentes/root/v4_labs_fase9a_curta_retorno_007_20260710.tar.gz`; SHA256 `c7b0cca474ec1c5bd7c708140cd6287e3e36d888e26f960279be7102cd627db0`; tamanho `5676914 bytes`.
- Forum: `Cerebro/Foruns/forum_v4_fase9a_curta_retorno_007_20260710.md`.
- Gate atual: parar e entregar para Claude/Miguel. Proibido iniciar 9B–9E sem nova autorizacao. Proxima coleta do 007, se autorizada, precisa de dois objetos/criadores com evidencia individual de efeito, nao apenas views ou presenca em catalogo.
- Auditoria Claude recebida e formalizada em `Cerebro/Foruns/carta_claude_auditoria_fase9a_retorno_007_20260710.md`: Fase 9A aprovada mecanicamente, adversarialmente e contra a fonte viva; SHA, 118/118, 11 agentes, batch 3/3 e Resultado B reproduzidos.
- Decisao editorial ainda pendente de Miguel: A) apuracao classica com produtores/criadores; B) redefinicao formal para exposicao documentada de menor confianca; C) estacionar ate novo ato do PL. Nenhuma opcao deve ser inferida. 007 segue em coleta e 9B-9E seguem bloqueadas.
- Em 2026-07-10 20:00 BRT, Miguel escolheu A de forma provisoria e reversivel, verbatim no forum: pode mudar de opiniao. Escopo autorizado agora e apenas preparar apuracao, contatos, perguntas e criterios. Nao enviar outreach, nao mudar claims/contratos/estado e nao iniciar 9B-9E sem confirmacao posterior.
- Preparacao A concluida em `Cerebro/Foruns/plano_apuracao_f9a_opcao_a_provisoria_007_20260710.md`: fontes publicas, contatos institucionais, perguntas, criterios, timebox e minuta nao enviada. Ha pistas para ambos os objetos, mas nenhuma virou claim. Proximo ato e irreversivel: so enviar outreach com nova confirmacao explicita de Miguel.
- Miguel autorizou o envio com `pode seguir`, mas Gmail retornou `reauthentication required`. Zero mensagens enviadas; timebox nao iniciado. Tres mensagens finais e destinatarios institucionais estao no plano. Retomar apenas apos reconectar Gmail e confirmar a identidade do remetente; nao usar conta alternativa.
- Retry em 2026-07-11 01:17 BRT: apos nova reconexao, Gmail passou a retornar `Mcp error -32603: Internal error` em perfil e labels. Ainda zero envios/drafts e timebox nao iniciado. Bloqueio e do conector, nao editorial.
- Regra posterior e definitiva de Miguel: `emails so podem ser manuais`. Nao usar Gmail/API/conector, nao criar draft remoto e nao enviar follow-up. Agentes podem apenas preparar minutas locais. Zero emails foram enviados nas tentativas anteriores.

### Proveniência V2 do 007 e nova canônica — 2026-07-13

- Fonte viva continua `Projeto Cafezinho Agentes/root/v4_labs/`; `root/v4`, publicação externa, promoção real, email e WordPress real seguem fechados.
- A coleta anterior `dados/auditado/v4_real_007.coleta_publica_20260711.json` foi preservada com SHA `b603e5680b47afb6ec5fec08acd84ee6892cdc47f7c8a981e02d0b5d7c7db411`.
- Nova coleta append-only: `dados/auditado/v4_real_007.coleta_publica_v2_20260713.json`, SHA `97afdacc89ae7a3268a93e23236937f72326b87d21807dd2ed03432fd540e91a`, escopo somente `proveniencia_e_locators_fact_check_v2`, `semantic_review_performed=false`.
- Dos 14 claims canônicos, os oito usados pelo template shadow/fact-check possuem `source_sha256`, `locator` e `fact_check_v2`; os dois claims do PL registram a linhagem texto extraído → PDF upstream.
- Novo fluxo dedicado: `contratos/v4_fluxo_dry_run_v3.json`. Nova canônica: `run_ea5eb32931ca37e4efef`; curadoria SHA `38cf164a09529e235f76981104c77f86bdf308d55b8fa072c01c80e4b2e605c2`; state SHA `96b17b24b50b0971ad3102233da92a279ba38cc747700c2a18ad47d01433f742`.
- Estado vigente do 007: `rascunho_revisao_humana`, `human_review_required=true`, `semantic_evaluation_complete=false`. A execução parou em `gate_shadow_selection_ausente`, com warning `avaliacao_semantica_humana_pendente`.
- A seleção anterior aponta para `run_f34...`; o shadow `run_ac46010ba6a46394778b` é histórico. Não reutilizar nem inferir essa autorização para `run_ea5...`.
- Prova contratada: binding 8/8, Fact-check V2 `issues=[]`, resultado inconclusivo apenas por oito segmentos interpretativos. Nenhum novo bound input, shadow, revisão ou fact-check foi persistido para a nova canônica.
- Validação final: `OK 272 contract tests`; 11 agentes strict válidos; recibo `dados/testes/suite_receipt_ad870d471b1e5f166e02ba9c45a3defd62000fd2644d852fbac1f615f67e0d85.json`; tree SHA `ad870d471b1e5f166e02ba9c45a3defd62000fd2644d852fbac1f615f67e0d85`; 599 arquivos; sem cache/pyc no preflight.
- Preflight V3 atual: `promocao_pendente_de_cura`; bloqueios genuínos de autorização humana, coleta por estágio, semântica, etapas obrigatórias e linhagem shadow atual. `wordpress_real=false`; `promocao_real_executada=false`.
- Fórum: `Cerebro/Foruns/forum_v4_proveniencia_007_20260713.md`.
- Próximo passo exato: obter novo ateste humano vinculado ao caminho e SHA da curadoria `run_ea5...`; depois usar `prepare_bound_input` para gerar um input append-only e executar shadow, revisão e fact-check. Não atravessar qualquer gate externo.
