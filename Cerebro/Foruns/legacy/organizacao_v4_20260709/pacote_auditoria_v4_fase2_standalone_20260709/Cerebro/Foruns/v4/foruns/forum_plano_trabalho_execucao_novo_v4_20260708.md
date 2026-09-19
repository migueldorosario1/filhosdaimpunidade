# Forum - Plano de Trabalho para Execucao do Novo Sistema V4

Aberto em: 2026-07-08  
Responsavel operacional: Codex  
Status: plano de codificacao, execucao faseada

## 1. Objetivo

Construir o novo sistema de agentes V4 aproveitando o que ja existe, sem reescrever tudo do zero.

O sistema novo deve ter:

- agentes tecnicos, sem hardcode editorial;
- diretrizes externas, dinamicas e versionadas;
- editorias V4 fortes;
- memoria de bugs e comentarios do editor;
- autocura controlada;
- pipeline de imagem destacada como parte editorial;
- telemetria;
- shadow test antes de producao;
- rollback claro.

## 2. Principio Arquitetural

Arquitetura recomendada para execucao:

> nucleo tecnico comum + diretrizes externas por vertical + validadores comuns + validadores especificos + memoria de bugs unificada com tags por editoria.

Evitar:

- prompt gigante hardcoded;
- regra editorial dentro de script tecnico;
- duplicar pipeline inteiro por editoria;
- mudar cron/producao antes de shadow;
- publicar sem resolver imagem destacada.

## 3. Pecas Existentes a Reaproveitar

Diretrizes:

```text
diretrizes/
  v4_nucleo_editorial_comum_v1.md
  v4_politica_economia_v1.md
  v4_cultura_v1.md
  v4_internacional_v1.md
  v4_repetidor_v1.md
  v4_gsn_espelho_ingles_v1.md
  v4_freios_llm_v1.json
```

Pipeline e agentes locais:

```text
agente_coleta_v3.py
agente_coletor_fontes_v3.py
executar_publicador_wp_v3_pending.py
executar_midia_v3_real.py
executar_acabamento_seo_v3_real.py
executar_revisao_titulo_v3_real.py
agente_midia_oficial_externa_v3.py
agente_tribunal_visual_v3.py
seletor_imagem_ouro_v3.py
robo_banco_ouro_midia_v3.py
biblioteca_editorial_service.py
```

Memoria de bugs:

```text
memoria_bugs_ativa.md
memoria_bugs_ativa_v3.md
```

Documentacao e foruns:

```text
Cerebro/Foruns/forum_novo_sistema_agentes_v4_e_diretrizes_20260707.md
Cerebro/Foruns/forum_super_luxo_editorial_v4_espelhado_20260707.md
Cerebro/Foruns/forum_novas_diretrizes_editoriais_correio_brasil_20260707.md
Cerebro/Foruns/forum_backup_retomada_backblaze_pre_reforma_20260707.md
tmp_v3_docs/PLANO_URGENTE_USO_BANCO_LEGADO_MIDIA_V3_20260626.md
forum_status_acervo_midia_r2_publicador_20260625.md
```

## 4. Fase 0 - Preservacao Seletiva

Antes de codar, fazer backup seletivo dos arquivos que serao alterados.

Escopo minimo:

- `diretrizes/`
- `Cerebro/Foruns/forum_novo_sistema_agentes_v4_e_diretrizes_20260707.md`
- scripts V4 que forem tocados;
- memoria de bugs se for convertida para formato estruturado;
- novos modulos de diretrizes/autocura.

Nao retomar backup total do workspace nesta fase.

Destino recomendado:

```text
Backups/pre_execucao_novo_v4_20260708/
b2:failover-cafezinho1/Antigravity_Google/backups/pre_execucao_novo_v4_20260708/
```

## 5. Fase 1 - Inventario Tecnico Real

Mapear como o V4 funciona hoje:

- onde a pauta entra;
- onde o texto e gerado;
- onde o modelo e escolhido;
- onde prompt/diretriz aparece hardcoded;
- onde imagem destacada e escolhida;
- onde publicacao pending acontece;
- onde titulo/SEO sao revisados;
- onde telemetria e logs ficam;
- quais arquivos rodam em producao ou cron.

Saida esperada:

```text
Cerebro/Foruns/forum_mapa_tecnico_v4_atual_20260708.md
```

## 6. Fase 2 - Criar Camada Externa de Diretrizes

Criar um modulo tecnico para carregar diretrizes sem hardcode.

Modulo proposto:

```text
v4_diretrizes/
  __init__.py
  loader.py
  schema.py
  registry.py
  composer.py
```

Responsabilidades:

- carregar `diretrizes/*.md` e `v4_freios_llm_v1.json`;
- resolver editoria para arquivo correto;
- montar contrato editorial para o agente;
- injetar memoria de bugs relevante;
- injetar comentarios recentes do editor;
- registrar versao/hash da diretriz usada;
- falhar de modo claro se diretriz obrigatoria estiver ausente.

Regra:

> script tecnico pergunta ao loader qual diretriz usar; nao embute regra editorial no codigo.

## 7. Fase 3 - Adicionar V4 Ciencia, Tecnologia e IA

Criar nova diretriz:

```text
diretrizes/v4_ciencia_tecnologia_ia_v1.md
```

Atualizar:

- mapa de editorias;
- classificador;
- espelho GSN;
- validadores;
- testes shadow.

Escopo editorial:

- ciencia;
- tecnologia;
- IA;
- Big Tech;
- regulacao digital;
- soberania tecnologica;
- ciberseguranca;
- dados;
- semicondutores;
- pesquisa publica;
- automacao e trabalho.

## 8. Fase 4 - Memoria de Bugs Estruturada e Feedback do Editor

Criar camada estruturada:

```text
memoria_bugs/
  bugs_editoriais.jsonl
  bugs_imagem_destacada.jsonl
  bugs_fontes.jsonl
  comentarios_editor.jsonl
  decisoes_correcao.jsonl
```

Modulo proposto:

```text
v4_memoria/
  __init__.py
  eventos.py
  consulta.py
  promover_diretriz.py
```

Responsabilidades:

- registrar bug;
- consultar bugs por editoria/tipo/modelo;
- anexar memoria relevante ao contrato editorial;
- detectar recorrencia;
- sugerir promocao para diretriz;
- nunca alterar diretriz em producao sem forum/shadow.

## 9. Fase 5 - Imagem Destacada como Pipeline Editorial

Criar contrato claro para imagem destacada.

Modulo proposto:

```text
v4_imagem_destacada/
  __init__.py
  contrato.py
  selecionar.py
  validar.py
  memoria.py
```

Reaproveitar:

- `executar_midia_v3_real.py`
- `seletor_imagem_ouro_v3.py`
- `agente_midia_oficial_externa_v3.py`
- `agente_tribunal_visual_v3.py`
- `biblioteca_editorial_service.py`
- `robo_banco_ouro_midia_v3.py`

Gates obrigatorios:

- imagem existe;
- tamanho minimo;
- nao e thumbnail/avatar;
- nao e generica se ha entidade principal;
- fonte/licenca/credito quando aplicavel;
- relacao direta com pauta;
- nao repetida recentemente;
- fallback documentado;
- se falhar, post fica pending, nao publicado cego.

## 10. Fase 6 - Classificador e Roteador V4

Criar ou adaptar classificador para decidir:

- editoria;
- nobre versus repetidor;
- risco editorial;
- necessidade de humano;
- diretriz carregada;
- freios por LLM;
- necessidade de imagem especializada;
- espelhamento GSN.

Modulo proposto:

```text
v4_orquestrador/
  __init__.py
  classificador.py
  roteador.py
  contrato.py
  shadow.py
```

Regra:

> roteador escolhe fluxo tecnico; diretriz externa define comportamento editorial.

## 11. Fase 7 - Validadores Objetivos

Criar validadores que rodam antes de publicar:

```text
v4_validadores/
  titulo.py
  lead.py
  fontes.py
  tom.py
  paragrafos.py
  imagem.py
  gsn.py
```

Validar:

- titulo em Sentence Case;
- lead direto;
- fonte rastreavel;
- tese proporcional;
- ausencia de cheiro de prompt;
- freios por LLM;
- imagem destacada;
- HTML/estrutura GSN;
- pendencias de editor.

## 12. Fase 8 - Shadow Test

Antes de producao, rodar comparacao lado a lado:

- Politica/Economia;
- Cultura;
- Internacional;
- Ciencia/Tecnologia/IA;
- Repetidor;
- GSN;
- caso com imagem destacada dificil.

Saida:

```text
artifacts/v4_shadow_20260708/
Cerebro/Foruns/forum_shadow_novo_v4_20260708.md
```

## 13. Fase 9 - Integracao Controlada

Integrar por baixo risco:

1. loader de diretrizes em modo dry-run;
2. memoria de bugs em modo append-only;
3. classificador em modo observador;
4. validadores em modo warning;
5. imagem destacada em modo pending, sem publicar cego;
6. shadow;
7. so depois ativar publicacao real.

## 14. Fase 10 - Telemetria e Prometheus

Adicionar metricas:

- diretriz usada;
- editoria;
- modelo;
- custo;
- tempo;
- status de imagem;
- motivo de pending;
- bug registrado;
- comentario do editor incorporado;
- publicacao bloqueada por gate.

Nao depender so de log textual.

## 15. Ordem de Execucao Recomendada

1. Backup seletivo.
2. Inventario tecnico real.
3. Criar `v4_diretrizes` e teste unitario simples.
4. Criar `v4_ciencia_tecnologia_ia_v1.md`.
5. Criar `v4_memoria` append-only.
6. Criar contrato de imagem destacada.
7. Conectar loader em modo dry-run a um script V4, sem alterar publicacao.
8. Criar shadow runner.
9. Rodar smoke local.
10. Registrar resultado no forum.

## 16. Critério Para Parar e Pedir Decisão

Parar antes de:

- alterar cron;
- publicar em producao;
- apagar arquivo;
- substituir pipeline remoto;
- mudar credenciais;
- ativar novo modelo pago sem teto;
- transformar sugestao de autocura em diretriz ativa sem shadow.

## 17. Proximo Passo Imediato

Executar Fase 0 e Fase 1:

- backup seletivo dos arquivos-alvo;
- inventario tecnico real;
- forum do mapa atual;
- depois iniciar `v4_diretrizes`.

---

## 18. Atualizacao Pela Rodada 2 Fechada

Registrado em: 2026-07-08.

GLM Ming/5.1 respondeu e trouxe um ponto tecnico que altera a estrategia de implementacao:

> O sistema ja e parcialmente hibrido hoje. `Projeto Cafezinho Agentes/root/config/llm_context_routes.json` externaliza roteamento LLM por contexto editorial. A nova camada de diretrizes deve estender esse padrao, nao criar arquitetura paralela.

Acao incorporada ao plano:

1. auditar `Projeto Cafezinho Agentes/root/config/llm_context_routes.json`;
2. auditar `modelos_vivos.json`, `llm_providers.json`, `llm_ratings.json` e roteador associado;
3. criar `diretrizes/mapa_v4_contexto_llm.json` como extensao formal do padrao existente;
4. mapear contextos atuais para V4 Politica/Economia, Cultura, Internacional, Ciencia/Tecnologia/IA e Repetidor;
5. manter `v4_diretrizes` como loader externo, mas acoplar ao contexto LLM existente em vez de duplicar roteamento;
6. validar arquitetura de imagem no Tencent antes de mexer em pipeline real.

Nova prioridade imediata:

- antes de criar modulo novo, ler e testar o roteamento existente.

---

## 19. Backup Seletivo Pre-Execucao V4 Concluido

Registrado em: 2026-07-08.

Forum do backup:

```text
Cerebro/Foruns/forum_backup_seletivo_pre_execucao_v4_20260708.md
```

Pasta local:

```text
Backups/pre_execucao_novo_v4_20260708_123244/
```

Destino Backblaze:

```text
b2:failover-cafezinho1/Antigravity_Google/backups/pre_execucao_novo_v4_20260708_123244/
```

Validacao:

```text
0 differences found
48 matching files
```

Conclusao:

Backup seletivo suficiente para iniciar a codificacao do V4 sem retomar o backup gigante do workspace.

---

## 20. Primeira Entrega de Codigo V4 - Diretrizes Externas

Registrado em: 2026-07-08.

Objetivo executado:

> criar a primeira camada tecnica do V4 sem hardcode editorial, sem chamada LLM e sem tocar producao.

Arquivos novos:

```text
diretrizes/v4_ciencia_tecnologia_ia_v1.md
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/__init__.py
v4_diretrizes/schema.py
v4_diretrizes/loader.py
v4_diretrizes/registry.py
v4_diretrizes/composer.py
v4_diretrizes/smoke.py
```

Funcoes implementadas:

- carregar diretrizes externas V4;
- carregar `v4_freios_llm_v1.json`;
- carregar memoria de bugs existente em modo leitura;
- resolver alias de editoria (`politica`, `tecnologia`, `gsn` etc.);
- conectar editoria/função V4 aos contextos existentes em `llm_context_routes.json`;
- montar contrato editorial local/dry-run;
- expor smoke CLI sem publicar e sem chamar LLM.

Comandos de verificacao executados:

```bash
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m json.tool diretrizes/v4_freios_llm_v1.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.smoke --editoria v4_politica_economia --funcao redacao --json
python3 -m v4_diretrizes.smoke --editoria v4_ciencia_tecnologia_ia --funcao redacao --json
python3 -m v4_diretrizes.smoke --editoria tecnologia --funcao redacao --json
```

Resultado:

- JSON valido;
- Python compila;
- smoke passou para:
  - `v4_politica_economia`;
  - `v4_cultura`;
  - `v4_internacional`;
  - `v4_ciencia_tecnologia_ia`;
  - `v4_repetidor`;
  - `v4_gsn`;
  - aliases `politica`, `tecnologia`, `gsn`.

Limite atual:

- o loader preserva os contextos LLM existentes; ainda nao filtra provider desabilitado, custo ou disponibilidade real;
- nao chama LLM;
- nao altera publicador;
- nao altera cron;
- nao toca banco de producao.

Proximo passo tecnico recomendado:

1. adicionar validador de disponibilidade/qualidade de tiers LLM contra `llm_providers.json` e `llm_ratings.json`;
2. criar `v4_memoria` append-only;
3. criar contrato dos bancos em camadas;
4. depois iniciar imagem destacada.

---

## 21. Segunda Entrega de Codigo V4 - Validador LLM Externo

Registrado em: 2026-07-08.

Objetivo executado:

> expor, em modo seco, se as rotas LLM usadas pelo V4 batem com provedores habilitados, fallbacks cadastrados, status dos modelos, qualidade minima e funcoes permitidas.

Arquivos alterados/criados:

```text
v4_diretrizes/schema.py
v4_diretrizes/llm_validator.py
v4_diretrizes/smoke.py
```

Funcoes implementadas:

- `LLMValidationIssue`;
- `LLMValidationReport`;
- `LLMTierValidator`;
- opcao CLI `--validate-llm`;
- opcao CLI `--strict` para falhar quando a validacao LLM retornar erro.

Fontes lidas pelo validador:

```text
diretrizes/mapa_v4_contexto_llm.json
Projeto Cafezinho Agentes/root/config/llm_context_routes.json
Projeto Cafezinho Agentes/root/config/llm_providers.json
Projeto Cafezinho Agentes/root/config/llm_ratings.json
```

Comandos de verificacao executados:

```bash
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.smoke --editoria v4_ciencia_tecnologia_ia --funcao redacao --json --validate-llm
python3 -m v4_diretrizes.smoke --editoria v4_politica_economia --funcao imagem --json --validate-llm
```

Resultado tecnico:

- o codigo compila;
- o smoke monta contrato V4 normalmente;
- a validacao LLM detecta pendencias herdadas dos cadastros atuais sem chamar LLM e sem mexer em producao.

Pendencias reveladas:

- `openai_luxo`: `gpt-5.5` esta valido, mas os fallbacks `gpt-5.4` e `gpt-5` seguem com `status='bloqueado_healthcheck'`;
- `gemini_luxo`: `gemini-3.5-flash` esta valido para funcoes nobres, mas `gemini-2.5-pro` tem qualidade 4 e falha quando o V4 exige qualidade 5;
- `xai_luxo`: provedor `xai` esta desabilitado; `grok-3` tem qualidade 4; `grok-2-1212` nao existe em `llm_ratings.json`;
- `tribunal_visual_gemini_luxo`: valido parcialmente por `gemini-3.5-flash`, mas ainda carrega `gemini-2.5-pro` abaixo do piso V4 de qualidade 5;
- `padrao`/`repetidor`: ainda puxa `deepseek_luxo`, cujo fallback atual e `deepseek-chat` com `status='legado'` e sem permissao para redacao.

Conclusao:

O V4 agora tem a primeira trava objetiva para impedir que a reforma repita o erro de degradar texto nobre por fallback barato, desligado, bloqueado ou fora de funcao. A proxima etapa deve limpar/criar rotas V4 dedicadas, sem alterar as rotas legadas antes de termos consenso.

Checkpoint:

```text
Local: Backups/checkpoint_v4_llm_validator_20260708_125345/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_llm_validator_20260708_125345/
Validacao: rclone check com 0 differences found / 4 matching files.
```

---

## 22. Limpeza como Lema e Contrato Operacional V4

Registrado em: 2026-07-08.

Novo lema do V4:

> limpeza, ordem, organizacao, leveza, automacao.

Decisao:

O lema foi convertido em requisito tecnico. O V4 deve ter capacidade de:

- autolimpar;
- auto-organizar;
- auto-backupear.

Arquivos criados/alterados:

```text
diretrizes/v4_nucleo_editorial_comum_v1.md
diretrizes/v4_operacao_limpeza_ordem_backup_v1.json
diretrizes/v4_rotas_llm_limpas_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/registry.py
v4_diretrizes/llm_validator.py
v4_diretrizes/composer.py
```

Limpeza LLM executada:

- o V4 deixou de usar diretamente os contextos legados `super_luxo`, `revisao_frontier`, `fact_check`, `padrao` etc.;
- foi criado `diretrizes/v4_rotas_llm_limpas_v1.json`;
- as rotas V4 agora usam contextos `v4_*`;
- os modelos sao allowlist explicita por contexto, para nao herdar fallback bloqueado, desligado, legado ou abaixo do piso;
- `xai_luxo`, `gpt-5.4`, `gpt-5`, `grok-2-1212`, `deepseek-chat` e `gemini-2.5-pro` foram isolados do caminho limpo V4 sem alterar o roteador legado.

Rotas limpas atuais:

```text
v4_super_luxo_redacao
v4_revisao_luxo
v4_auditoria_luxo
v4_fact_check_luxo
v4_curadoria_luxo
v4_imagem_destacada_gemini
v4_repetidor_limpo
```

Validacao executada:

```bash
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m json.tool diretrizes/v4_rotas_llm_limpas_v1.json
python3 -m json.tool diretrizes/v4_operacao_limpeza_ordem_backup_v1.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.smoke --editoria v4_ciencia_tecnologia_ia --funcao redacao --json --validate-llm
```

Varredura completa:

Todas as combinacoes abaixo retornaram `ok=True` e `errors=0`:

- editorias: `v4_politica_economia`, `v4_cultura`, `v4_internacional`, `v4_ciencia_tecnologia_ia`, `v4_repetidor`, `v4_gsn`;
- funcoes: `redacao`, `revisao`, `auditoria`, `fact_check`, `imagem`.

Conclusao:

O V4 agora tem uma fonte limpa, externa e versionada para LLMs nobres, separada do roteador legado. A limpeza deixou de ser apenas orientacao editorial e virou contrato operacional.

Checkpoint:

```text
Local: Backups/checkpoint_v4_limpeza_rotas_operacao_20260708_125657/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_limpeza_rotas_operacao_20260708_125657/
Validacao: rclone check com 0 differences found / 10 matching files.
```

---

## 23. Execucao Autonoma - Base Tecnica V4

Registrado em: 2026-07-08.

Decisao de processo:

O V4 passa a ser conduzido em blocos assertivos, com plano de trabalho, validacao, forum e checkpoint seletivo. A aprovacao conceitual da Trindade ja foi considerada suficiente para iniciar construcao tecnica.

Bloco entregue:

1. executor operacional V4 em dry-run;
2. contrato de bancos em camadas;
3. memoria V4 append-only;
4. contrato de agentes tecnicos;
5. diretorios iniciais de dados V4.

Arquivos novos/alterados:

```text
diretrizes/v4_operacao_limpeza_ordem_backup_v1.json
diretrizes/v4_bancos_camadas_v1.json
diretrizes/v4_memoria_autocura_v1.json
diretrizes/v4_agentes_tecnicos_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/operacao.py
v4_diretrizes/operacao_cli.py
v4_diretrizes/camadas.py
v4_diretrizes/camadas_cli.py
v4_diretrizes/memoria.py
v4_diretrizes/memoria_cli.py
v4_diretrizes/agentes.py
v4_diretrizes/agentes_cli.py
v4_diretrizes/schema.py
v4_diretrizes/__init__.py
v4_data/bruto/
v4_data/intermediario/
v4_data/auditado/
v4_data/producao/
v4_data/publicado/
v4_data/quarentena/
v4_memoria/eventos.jsonl
```

Principio operacional:

> limpeza, ordem, organizacao, leveza, automacao.

O executor operacional agora le contrato externo e opera em escopo V4 estrito por padrao. A varredura ampla do workspace foi evitada porque gera ruido e fragmenta a operacao.

Resumo do dry-run operacional:

```text
remover_pycache:dry_run = 1
mover_para_tmp_ou_backup:needs_review = 1
catalogar_categoria:indexed = 24
verificar_indice_obrigatorio:present = 2
incluir_em_checkpoint:planned = 21
warnings = 0
```

Bancos em camadas:

```text
bruto          -> entrada inicial nao confiavel
intermediario  -> material normalizado/deduplicado
auditado       -> material aprovado para leitura de produtor/imagem/publicador
producao       -> saida gerada por produtor/imagem antes de auditoria final
publicado      -> registro final de publicacao
quarentena     -> material suspeito, duplicado ou inseguro
```

Regra central validada:

```text
produtor read bruto          = bloqueado
produtor read intermediario  = bloqueado
produtor read auditado       = permitido
produtor write producao      = permitido
publicador read bruto        = bloqueado
publicador read auditado     = permitido
coletor write auditado       = bloqueado
auditor write auditado       = permitido
```

Agentes tecnicos V4 validados:

```text
coletor
processador
auditor
produtor
imagem
publicador
observabilidade
```

Todos passaram em `python3 -m v4_diretrizes.agentes_cli --strict`.

Memoria V4:

- contrato: `diretrizes/v4_memoria_autocura_v1.json`;
- store: `v4_memoria/eventos.jsonl`;
- formato: JSONL append-only;
- primeiro evento real registrado: decisao arquitetural sobre contratos externos, leitura de produtor em `auditado` e escrita em `producao`.

Comandos de validacao executados:

```bash
python3 -m json.tool diretrizes/v4_operacao_limpeza_ordem_backup_v1.json
python3 -m json.tool diretrizes/v4_bancos_camadas_v1.json
python3 -m json.tool diretrizes/v4_memoria_autocura_v1.json
python3 -m json.tool diretrizes/v4_agentes_tecnicos_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.operacao_cli --summary
python3 -m v4_diretrizes.camadas_cli --ensure-dirs --execute
python3 -m v4_diretrizes.memoria_cli --event-type decisao --severity info --source codex --summary 'V4 estabelecido com contratos externos para operacao, camadas, memoria e agentes tecnicos' --tag v4 --tag arquitetura --tag limpeza --payload-json '{"produtor_le":"auditado","produtor_escreve":"producao","diretrizes":"externas","llms":"externas"}' --execute
python3 -m v4_diretrizes.agentes_cli --strict
python3 -m v4_diretrizes.smoke --editoria v4_ciencia_tecnologia_ia --funcao imagem --json --validate-llm
```

Proximo bloco recomendado:

Implementar o primeiro fluxo V4 real em dry-run:

```text
auditado -> produtor -> producao -> auditor -> auditado -> publicador dry-run
```

Sem chamada LLM ainda, usando manifestos locais, para validar idempotencia, permissao de camadas, memoria e checkpoint.

Checkpoint:

```text
Local: Backups/checkpoint_v4_base_tecnica_20260708_130519/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_base_tecnica_20260708_130519/
Validacao: rclone check com 0 differences found / 31 matching files.
```

---

## 24. Primeiro Fluxo V4 Real em Dry-run

Registrado em: 2026-07-08.

Objetivo:

Validar o caminho tecnico completo do V4 sem chamada LLM e sem publicacao externa:

```text
auditado -> produtor -> producao -> auditor -> auditado -> publicador dry-run
```

Arquivos novos/alterados:

```text
diretrizes/v4_fluxo_dry_run_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/fluxo.py
v4_diretrizes/fluxo_cli.py
v4_diretrizes/__init__.py
v4_data/auditado/v4_fixture_001.json
v4_data/producao/v4_fixture_001.producao.json
v4_data/auditado/v4_fixture_001.auditado_final.json
v4_data/publicado/v4_fixture_001.publicado_dry_run.json
v4_memoria/eventos.jsonl
```

Contrato:

`diretrizes/v4_fluxo_dry_run_v1.json`

Principios do fluxo:

- sem chamada LLM;
- sem publicacao externa;
- idempotente;
- manifestos obrigatorios;
- respeita camadas;
- usa contrato editorial externo apenas como metadado verificavel.

Resultado da primeira execucao materializada:

```text
produzir_dry_run       -> created
auditar_final_dry_run  -> created
publicar_dry_run       -> created
```

Resultado da segunda execucao:

```text
produzir_dry_run       -> skipped_existing
auditar_final_dry_run  -> skipped_existing
publicar_dry_run       -> skipped_existing
```

Isso confirma idempotencia basica do fluxo.

Arquivos gerados:

```text
v4_data/auditado/v4_fixture_001.json
v4_data/producao/v4_fixture_001.producao.json
v4_data/auditado/v4_fixture_001.auditado_final.json
v4_data/publicado/v4_fixture_001.publicado_dry_run.json
```

Manifestos verificados:

```text
producao:       role=produtor,   idempotency_key=61926d5b3b0ff89ca6465b04c741c589132521a047ecb5521ce03022eff83729
auditado_final: role=auditor,    idempotency_key=442750081c95041094ccaa7278741370a716c50e7d93175636744d9e0474f753
publicado:      role=publicador, idempotency_key=c140b98a13517a16470d1899989856868d3be542ff2568a8362dbad983eabf2e
```

Memoria:

O fluxo registrou eventos em `v4_memoria/eventos.jsonl` com `event_type=validacao`, `source=v4_dry_run_flow` e payload dos passos.

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_fluxo_dry_run_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.fluxo_cli
python3 -m v4_diretrizes.fluxo_cli --execute
python3 -m v4_diretrizes.fluxo_cli --execute
python3 -m v4_diretrizes.agentes_cli --strict
python3 -m v4_diretrizes.operacao_cli --summary
```

Conclusao:

O V4 agora tem um fluxo tecnico minimo funcionando de ponta a ponta, ainda sem LLM e sem publicacao externa. A arquitetura de camadas, permissao, contratos externos, manifestos, memoria e idempotencia foi validada em arquivos reais.

Proximo bloco recomendado:

Adicionar o primeiro adaptador LLM em modo `mock`/`dry-run` e depois um modo real controlado, usando apenas `diretrizes/v4_rotas_llm_limpas_v1.json`, para transformar a etapa `produzir_dry_run` em producao editorial real sem quebrar as garantias de camada.

Checkpoint:

```text
Local: Backups/checkpoint_v4_fluxo_dry_run_20260708_132129/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_fluxo_dry_run_20260708_132129/
Validacao: rclone check com 0 differences found / 38 matching files.
```

---

## 25. Adaptador LLM V4 Mock Integrado ao Fluxo

Registrado em: 2026-07-08.

Objetivo:

Adicionar o primeiro adaptador LLM do V4 sem chamadas reais, sem modelo hardcoded no agente e sem diretriz hardcoded.

Arquivos novos/alterados:

```text
diretrizes/v4_llm_adapter_v1.json
diretrizes/v4_fluxo_dry_run_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/llm_adapter.py
v4_diretrizes/llm_adapter_cli.py
v4_diretrizes/fluxo.py
v4_diretrizes/__init__.py
v4_data/auditado/v4_fixture_002.json
v4_data/producao/v4_fixture_002.producao.json
v4_data/auditado/v4_fixture_002.auditado_final.json
v4_data/publicado/v4_fixture_002.publicado_dry_run.json
v4_memoria/eventos.jsonl
```

Contrato:

`diretrizes/v4_llm_adapter_v1.json`

Decisoes:

- modo padrao: `mock`;
- `allow_real_calls=false`;
- rotas vindas de `diretrizes/v4_rotas_llm_limpas_v1.json`;
- chamadas reais seguem bloqueadas ate contrato explicito futuro;
- o produtor usa `ContractComposer` e `LLMTierValidator` antes de gerar qualquer saida.

Resultado do adapter isolado:

```text
provider=mock
model=v4-mock-local
route_context=v4_super_luxo_redacao
route_tiers=openai_luxo, anthropic_luxo, gemini_luxo
```

Resultado do fluxo com fixture nova:

```text
fixture=v4_fixture_002
primeira execucao: created
segunda execucao: skipped_existing
```

Manifesto de producao agora inclui:

```text
llm_response.mode=mock
llm_response.provider=mock
llm_response.model=v4-mock-local
llm_response.prompt_hash=1096e1e6f7b830f24da0ea7b092a5455d0ce0815855c72eea37834f2e12e0e41
llm_response.route_context=v4_super_luxo_redacao
llm_response.route_tiers=[openai_luxo, anthropic_luxo, gemini_luxo]
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_llm_adapter_v1.json
python3 -m json.tool diretrizes/v4_fluxo_dry_run_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.llm_adapter_cli
python3 -m v4_diretrizes.fluxo_cli
python3 -m v4_diretrizes.fluxo_cli --execute
python3 -m v4_diretrizes.agentes_cli --strict
python3 -m v4_diretrizes.operacao_cli --summary
```

Memoria:

Registrado evento `validacao` em `v4_memoria/eventos.jsonl`:

```text
Adaptador LLM V4 mock integrado ao fluxo produtor
```

Conclusao:

O V4 agora tem uma interface LLM realista, mas ainda segura: o agente produtor nao sabe modelo, nao guarda prompt editorial e nao chama API externa. Ele recebe contrato editorial externo, valida rota limpa e grava a resposta mock com metadados auditaveis.

Proximo bloco recomendado:

Criar o modo real controlado atras de flag e healthcheck, sem habilitar por padrao:

```text
mock -> healthcheck rota limpa -> chamada real opcional -> gravacao em producao -> auditoria
```

Checkpoint:

```text
Local: Backups/checkpoint_v4_llm_mock_20260708_132405/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_llm_mock_20260708_132405/
Validacao: rclone check com 0 differences found / 45 matching files.
```

---

## 26. Healthcheck do Modo Real LLM V4

Registrado em: 2026-07-08.

Objetivo:

Preparar o modo real do adaptador LLM sem habilitar chamadas externas por padrao.

Arquivos novos/alterados:

```text
diretrizes/v4_llm_adapter_v1.json
v4_diretrizes/llm_healthcheck.py
v4_diretrizes/llm_healthcheck_cli.py
v4_diretrizes/llm_adapter.py
v4_diretrizes/llm_adapter_cli.py
v4_diretrizes/__init__.py
v4_memoria/eventos.jsonl
```

Contrato atualizado:

```json
"real": {
  "enabled": false,
  "require_healthcheck": true,
  "healthcheck": {
    "check_env_keys": true,
    "check_provider_enabled": true,
    "check_model_rating": true,
    "network_call": false
  },
  "selection": {
    "strategy": "first_valid_by_route_order",
    "respect_route_order": true
  }
}
```

Resultado do healthcheck local:

```text
contexto_llm=v4_super_luxo_redacao
candidate=openai:gpt-5.5
provider=openai
tier=openai_luxo
quality=5
status=ativo
network_call=false
real_enabled=false
allow_real_calls=false
ok=false
```

Issues esperadas:

```text
sem env key disponivel para provider openai
real.enabled=false no contrato do adapter
allow_real_calls=false no contrato do adapter
```

Comportamento validado:

- `python3 -m v4_diretrizes.llm_healthcheck_cli` mostra candidato e bloqueios;
- `python3 -m v4_diretrizes.llm_healthcheck_cli --strict` retorna codigo 2 enquanto real estiver bloqueado;
- `python3 -m v4_diretrizes.llm_adapter_cli --mode real` retorna JSON com `ok=false`, sem traceback;
- fluxo mock continua funcionando e idempotente.

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_llm_adapter_v1.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.llm_healthcheck_cli
python3 -m v4_diretrizes.llm_healthcheck_cli --strict
python3 -m v4_diretrizes.llm_adapter_cli
python3 -m v4_diretrizes.llm_adapter_cli --mode real
python3 -m v4_diretrizes.fluxo_cli --execute
```

Memoria:

Registrado evento `validacao` em `v4_memoria/eventos.jsonl`:

```text
Healthcheck LLM real V4 implementado com chamadas reais bloqueadas por contrato
```

Conclusao:

O V4 agora sabe selecionar candidato real a partir das rotas limpas, mas ainda impede qualquer chamada externa por tres travas: `real.enabled=false`, `allow_real_calls=false` e `network_call=false`.

Proximo bloco recomendado:

Implementar um provider real piloto atras de contrato separado, preferencialmente com um item novo e limite estrito:

```text
1 chamada real -> 1 item auditado -> 1 arquivo producao -> sem publicacao externa
```

Checkpoint:

```text
Local: Backups/checkpoint_v4_llm_healthcheck_20260708_134436/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_llm_healthcheck_20260708_134436/
Validacao: rclone check com 0 differences found / 47 matching files.
```

---

## 27. Inteligencia LLM, Rotacao, Revisao Conservadora e Telemetria V4

Registrado em: 2026-07-08.

Decisoes do editor incorporadas:

- a inteligencia LLM e central para a automacao do Cafezinho;
- nada de modelo hardcoded dentro de agente;
- texto nobre deve usar `super_luxo`;
- tarefas menos nobres podem usar `luxo` ou `padrao`;
- devemos alternar entre modelos fortes para comparar qualidade por tema/editoria;
- revisao nao pode usar o mesmo provider da producao;
- revisao deve ser conservadora: nao reescrever tudo se o texto ja estiver bom;
- DeepSeek V4, Qwen e GLM entram quando o cadastro local permitir funcao editorial e passar no validador;
- telemetria e obrigatoria desde o nascimento.

Arquivos novos/alterados:

```text
diretrizes/v4_orquestracao_llm_v1.json
diretrizes/v4_telemetria_v1.json
diretrizes/v4_llm_adapter_v1.json
diretrizes/v4_fluxo_dry_run_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/llm_orchestrator.py
v4_diretrizes/llm_orchestrator_cli.py
v4_diretrizes/telemetry.py
v4_diretrizes/telemetry_cli.py
v4_diretrizes/llm_adapter.py
v4_diretrizes/llm_adapter_cli.py
v4_diretrizes/fluxo.py
v4_diretrizes/__init__.py
v4_telemetry/receipts/v4_ciencia_tecnologia_ia_20260708.jsonl
v4_data/auditado/v4_fixture_003.json
v4_data/producao/v4_fixture_003.producao.json
v4_data/auditado/v4_fixture_003.auditado_final.json
v4_data/publicado/v4_fixture_003.publicado_dry_run.json
v4_memoria/eventos.jsonl
```

Orquestracao LLM:

Contrato: `diretrizes/v4_orquestracao_llm_v1.json`

Tiers definidos:

```text
super_luxo -> redacao nobre, revisao nobre, auditoria final, fact_check sensivel
luxo       -> curadoria, imagem, repetidor melhorado, perifericos editoriais
padrao     -> tarefas mecanicas, dedupe, normalizacao, classificacao simples
```

Candidatos validos atuais para `v4_ciencia_tecnologia_ia/redacao`:

```text
openai:gpt-5.5
anthropic:claude-opus-4-8
anthropic:claude-sonnet-4-6
gemini:gemini-3.5-flash
```

Selecao:

```text
strategy=rotate_valid_by_idempotency
```

Ou seja: alterna de forma deterministica por item/chave, sem depender de hardcode no agente.

Modelos chineses:

```text
deepseek:deepseek-v4-pro -> pendente porque ratings local tem funcoes_permitidas vazio
alibaba:qwen3-max        -> pendente porque ratings local tem funcoes_permitidas vazio
zhipu:glm-5.1            -> pendente_teste; hoje permitido localmente apenas para auditoria
```

Regra:

> modelos chineses entram quando tiverem status ativo, funcao permitida e passarem pelo validador V4. Nao entram em rota nobre apenas por desejo editorial se o cadastro local ainda nao autoriza a funcao.

Revisao:

Regra implementada:

```text
revisor_diferente_do_produtor=true
must_exclude_previous_provider=true
modo=conservador
```

Teste executado:

```bash
python3 -m v4_diretrizes.llm_adapter_cli --editoria v4_ciencia_tecnologia_ia --funcao revisao --previous-provider gemini
```

Resultado:

```text
previous_provider=gemini
revisor selecionado=openai:gpt-5.5
```

Telemetria:

Contrato: `diretrizes/v4_telemetria_v1.json`

Decisao incorporada da carta Claude:

```text
JSONL detalhado por materia = obrigatorio/perene/auditavel
Prometheus = agregado, baixa cardinalidade, failure graceful
Prometheus caiu -> pipeline segue
JSONL falhou -> publicacao bloqueia
```

Recibo JSONL criado:

```text
v4_telemetry/receipts/v4_ciencia_tecnologia_ia_20260708.jsonl
```

Labels Prometheus proibidos:

```text
post_id
item_id
title
titulo
url
content
conteudo
prompt
prompt_hash
```

Teste executado:

```bash
python3 -m v4_diretrizes.telemetry_cli --check-label provider --check-label post_id
```

Resultado esperado:

```text
label proibido no Prometheus: post_id
exit_code=2
```

Fluxo com telemetria:

Fixture nova:

```text
v4_fixture_003
```

Resultado:

```text
produtor -> producao: created
auditor -> auditado_final: created
publicador -> publicado_dry_run: created
segunda execucao: skipped_existing
```

Recibos JSONL gravados para:

```text
produzir_dry_run
auditar_final_dry_run
publicar_dry_run
```

O recibo de producao inclui:

```text
provider=gemini
model=gemini-3.5-flash
tier=gemini_luxo
route_context=v4_super_luxo_redacao
prompt_hash=1e8da93935e736750b9e9802fcf55334bf0062917b942ed1654a6b630a5485af
```

Comandos de validacao executados:

```bash
python3 -m json.tool diretrizes/v4_orquestracao_llm_v1.json
python3 -m json.tool diretrizes/v4_telemetria_v1.json
python3 -m json.tool diretrizes/v4_llm_adapter_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.llm_orchestrator_cli --editoria v4_ciencia_tecnologia_ia --funcao redacao --idempotency-key rotate-001 --list-candidates
python3 -m v4_diretrizes.llm_adapter_cli --editoria v4_ciencia_tecnologia_ia --funcao revisao --previous-provider gemini
python3 -m v4_diretrizes.telemetry_cli --check-label provider --check-label post_id
python3 -m v4_diretrizes.fluxo_cli --execute
python3 -m v4_diretrizes.agentes_cli --strict
```

Conclusao:

O V4 agora tem inteligencia LLM como camada externa e auditavel: rotacao, tier, selecao por funcao, separacao produtor/revisor, revisao conservadora e telemetria obrigatoria. A comparacao futura de qualidade por tema/editoria passa a ser possivel porque cada producao deixa recibo JSONL com provider, model, tier, contexto, prompt_hash e idempotency_key.

Proximo bloco recomendado:

Implementar avaliacao do editor e comparativo de qualidade por provider/model/editoria:

```text
feedback_editor -> v4_memoria/eventos.jsonl + recibo JSONL -> ranking por tema/modelo
```

Checkpoint:

```text
Local: Backups/checkpoint_v4_orquestracao_telemetria_20260708_135353/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_orquestracao_telemetria_20260708_135353/
Validacao: rclone check com 0 differences found / 58 matching files.
```

---

## 29. Ajustes de Auditoria Claude na Telemetria V4

Registrado em: 2026-07-08.

Feedback recebido:

```text
Cerebro/Foruns/carta_claude_codex_feedback_telemetria_v4_20260708.md
```

Aplicado:

- `agent_data/v4/receipts/` como diretório canônico;
- `schema_version`, `duration_ms`, `cost_usd_estimated`, `pricing_table_version` como campos obrigatórios;
- `LLMCallDetail` tipado;
- `fcntl.flock`, `flush` e `os.fsync` no append JSONL;
- validação ISO8601 de timestamp;
- sanitização de `vertical`;
- labels Prometheus `tier`, `portal`, `outcome`, `reason_class`;
- remoção do label genérico `reason`;
- `test_contracts.py` com 8 testes.

Comandos executados:

```bash
git check-ignore agent_data/v4/receipts/teste.jsonl
python3 -m json.tool diretrizes/v4_telemetria_v1.json
python3 -m json.tool diretrizes/v4_fluxo_dry_run_v1.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.telemetry_cli --check-label provider --check-label tier --check-label portal --check-label outcome --check-label reason_class
python3 -m v4_diretrizes.telemetry_cli --check-label reason
python3 -m v4_diretrizes.fluxo_cli --execute
```

Resultado:

```text
agent_data/v4/receipts/teste.jsonl ignorado pelo git
OK 8 contract tests
reason bloqueado como label Prometheus
v4_fixture_004 criada
recibo novo gravado em agent_data/v4/receipts/v4_ciencia_tecnologia_ia_20260708.jsonl
```

Conclusao:

Os gates de auditoria pedidos pelo Claude existem agora. A invariante principal ficou testada:

```text
publicacao/saida bloqueia se record_receipt retornar ok=false
```

Checkpoint:

```text
Local: Backups/checkpoint_v4_telemetria_auditoria_claude_20260708_140655/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_telemetria_auditoria_claude_20260708_140655/
Validacao: rclone check com 0 differences found / 64 matching files.
```

---

## 30. Feedback do Editor e Ranking de Qualidade LLM

Registrado em: 2026-07-08.

Objetivo:

Fechar o ciclo de inteligencia editorial:

```text
recibo JSONL -> feedback do editor -> memoria -> ranking por provider/model/editoria
```

Arquivos novos/alterados:

```text
diretrizes/v4_feedback_editor_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/feedback.py
v4_diretrizes/feedback_cli.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/feedback/editor_feedback.jsonl
v4_memoria/eventos.jsonl
```

Contrato:

```text
diretrizes/v4_feedback_editor_v1.json
```

Store:

```text
agent_data/v4/feedback/editor_feedback.jsonl
```

Campos obrigatorios:

```text
schema_version
timestamp
item_id
vertical
editor
score
sentiment
comment
correction_class
provider
model
operation
```

Score:

```text
1 = ruim, precisa refazer
2 = fraco, muita correcao
3 = publicavel com edicao
4 = bom
5 = excelente
```

Classes de correcao:

```text
nenhuma
estilo
fato
titulo
lead
imagem
tom
juridico
estrutura
reescrita_total
```

Feedback de teste registrado:

```text
item_id=v4_fixture_004
vertical=v4_ciencia_tecnologia_ia
editor=miguel
score=4
sentiment=positivo
correction_class=nenhuma
provider=anthropic
model=claude-opus-4-8
comment=Texto bom para teste; manter autoria e revisar pouco.
```

Ranking atual:

```text
v4_ciencia_tecnologia_ia / anthropic / claude-opus-4-8 / produzir_dry_run
samples=1
avg_score=4.0
correction_classes={nenhuma: 1}
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_feedback_editor_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.feedback_cli --item-id v4_fixture_004 --score 4 --sentiment positivo --comment 'Texto bom para teste; manter autoria e revisar pouco.' --correction-class nenhuma --execute
python3 -m v4_diretrizes.feedback_cli --ranking
python3 -m v4_diretrizes.test_contracts
```

Resultado:

```text
OK 10 contract tests
```

Conclusao:

O V4 agora consegue registrar avaliacao do editor e produzir ranking por provider/model/editoria sem usar Prometheus de alta cardinalidade. Isso cria a base para descobrir, com dados, qual modelo escreve melhor por tema.

Proximo bloco recomendado:

Adicionar custos/tokens estimados reais ao `LLMCallDetail`, com tabela versionada de precos:

```text
pricing_table -> tokens/custo por chamada -> ranking qualidade/custo por modelo
```

Checkpoint:

```text
Local: Backups/checkpoint_v4_feedback_ranking_20260708_141040/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_feedback_ranking_20260708_141040/
Validacao: rclone check com 0 differences found / 67 matching files.
```

---

## 31. Pricing LLM e Ranking Qualidade-Custo

Registrado em: 2026-07-08.

Objetivo:

Adicionar custo/tokens estimados reais aos recibos JSONL e ao ranking de qualidade por modelo.

Arquivos novos/alterados:

```text
diretrizes/v4_pricing_llm_v1.json
diretrizes/v4_fluxo_dry_run_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/pricing.py
v4_diretrizes/llm_adapter.py
v4_diretrizes/fluxo.py
v4_diretrizes/feedback.py
v4_diretrizes/test_contracts.py
agent_data/v4/receipts/v4_ciencia_tecnologia_ia_20260708.jsonl
agent_data/v4/feedback/editor_feedback.jsonl
v4_memoria/eventos.jsonl
```

Tabela de preços:

```text
diretrizes/v4_pricing_llm_v1.json
version=2026-07-08-local-ratings
source=Projeto Cafezinho Agentes/root/config/llm_ratings.json
```

Modelos com preço inicial:

```text
gpt-5.5
claude-opus-4-8
claude-sonnet-4-6
gemini-3.5-flash
deepseek-v4-pro
qwen3-max
```

Estimativa:

```text
tokens ~= ceil(chars / 4)
cost = (tokens_in * input_usd_per_1m + tokens_out * output_usd_per_1m) / 1_000_000
```

Fixture nova:

```text
v4_fixture_005
```

Recibo gerado:

```text
item_id=v4_fixture_005
provider=gemini
model=gemini-3.5-flash
tier=gemini_luxo
tokens_in=33
tokens_out=71
cost_usd_estimated=0.00002378
pricing_table_version=2026-07-08-local-ratings
```

Feedback registrado:

```text
score=5
sentiment=positivo
correction_class=nenhuma
comment=Teste de custo estimado: saida boa e barata o suficiente para ranking.
```

Ranking qualidade-custo atual:

```text
gemini/gemini-3.5-flash
avg_score=5.0
avg_cost_usd_estimated=0.00002378
score_per_usd_estimated=210260.723

anthropic/claude-opus-4-8
avg_score=4.0
avg_cost_usd_estimated=0.0
score_per_usd_estimated=null
```

Observacao:

O item antigo de Claude aparece com custo 0 porque foi gerado antes do pricing versionado. A partir de `v4_fixture_005`, os recibos novos carregam custo/tokens. No futuro, um recomputador append-only pode recalcular recibos antigos sem editar historico.

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_pricing_llm_v1.json
python3 -m json.tool diretrizes/v4_fluxo_dry_run_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.fluxo_cli --execute
python3 -m v4_diretrizes.llm_adapter_cli --editoria v4_ciencia_tecnologia_ia --funcao redacao --titulo 'Teste custo' --conteudo 'Material auditado para custo.' --idempotency-key cost-test
python3 -m v4_diretrizes.feedback_cli --item-id v4_fixture_005 --score 5 --sentiment positivo --comment 'Teste de custo estimado: saida boa e barata o suficiente para ranking.' --correction-class nenhuma --execute
python3 -m v4_diretrizes.feedback_cli --ranking
```

Resultado:

```text
OK 11 contract tests
```

Conclusao:

O V4 agora consegue comparar qualidade e custo por modelo/editoria com dados locais auditaveis. Isso prepara a escolha inteligente entre GPT, Claude, Gemini e futuros chineses quando os cadastros estiverem limpos.

Proximo bloco recomendado:

Implementar recomputacao append-only de custos antigos:

```text
recibo antigo sem custo -> pricing atual -> agent_data/v4/receipts/recomputed/*.jsonl
```

Checkpoint:

```text
Local: Backups/checkpoint_v4_pricing_quality_cost_20260708_142305/
B2: b2:failover-cafezinho1/Antigravity_Google/backups/checkpoint_v4_pricing_quality_cost_20260708_142305/
Validacao: rclone check com 0 differences found / 73 matching files.
```

---

## 28. Fórum Separado — Resposta ao Claude sobre Telemetria

Registrado em: 2026-07-08.

Criado fórum específico:

```text
Cerebro/Foruns/forum_resposta_codex_claude_telemetria_prometheus_despesas_v4_20260708.md
```

Resumo da posição enviada:

```text
JSONL append-only = detalhe contábil por matéria, obrigatório e perene
Prometheus       = saúde e agregados de baixa cardinalidade, opcional/failure graceful
Prometheus caiu  -> pipeline/publicação segue
JSONL falhou     -> publicação bloqueia
```

Pedido de feedback ao Claude:

- schema do recibo JSONL;
- labels permitidos/proibidos;
- prefixo `v4_*`;
- rotação de recibos;
- diretório canônico;
- custo estimado por chamada;
- ordem de emissão JSONL/Prometheus.

---

## 29. Recomputaçao Append-Only de Custos Antigos

Registrado em: 2026-07-08.

Objetivo:

```text
Corrigir custos estimados de recibos antigos sem editar historico original.
```

Arquivos criados/alterados:

```text
diretrizes/v4_recompute_costs_v1.json
v4_diretrizes/recompute_costs.py
v4_diretrizes/recompute_costs_cli.py
v4_diretrizes/feedback.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/receipts/recomputed/recomputed_20260708.jsonl
```

Contrato:

```text
Origem: agent_data/v4/receipts/*.jsonl
Destino: agent_data/v4/receipts/recomputed/*.jsonl
Regra: append-only
Regra: nunca modificar recibo original
Regra: idempotente por source/item/operation/model/pricing_version
```

Resultado real:

```text
v4_fixture_004
provider=anthropic
model=claude-opus-4-8
tokens_in=35
tokens_out=76
old_cost_usd_estimated=0.0
new_cost_usd_estimated=0.002075
pricing_table_version=2026-07-08-local-ratings
status=recomputed
```

Execucao repetida:

```text
appended_count=0
status=skipped_already_recorded
```

Ranking qualidade-custo apos recomputacao:

```text
gemini/gemini-3.5-flash
avg_score=5.0
avg_cost_usd_estimated=0.00002378
score_per_usd_estimated=210260.723

anthropic/claude-opus-4-8
avg_score=4.0
avg_cost_usd_estimated=0.002075
score_per_usd_estimated=1927.711
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_recompute_costs_v1.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.recompute_costs_cli --execute
python3 -m v4_diretrizes.feedback_cli --ranking
```

Resultado:

```text
OK 13 contract tests
```

Conclusao:

O V4 agora consegue corrigir custo historico sem contaminar recibos originais. O ranking de feedback passa a considerar recomputacoes append-only quando existirem, mantendo a auditoria contábil limpa.

Proximo bloco recomendado:

```text
Implementar roteador de modelos por qualidade/custo:
feedback + pricing + tier externo -> escolha do melhor LLM por editoria/operação.
```

---

## 30. Roteador de Modelos por Qualidade e Custo

Registrado em: 2026-07-08.

Objetivo:

```text
Selecionar LLM por dados externos: candidatos validos + feedback do editor + custo estimado + ordem de rota.
```

Arquivos criados/alterados:

```text
diretrizes/v4_model_router_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/model_router.py
v4_diretrizes/model_router_cli.py
v4_diretrizes/llm_adapter.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
```

Contrato:

```text
weights:
  quality=0.7
  cost_efficiency=0.2
  route_order=0.1

min_samples_for_feedback_priority=3
feedback_operation_map:
  redacao -> produzir_dry_run
```

Resultado atual para `v4_ciencia_tecnologia_ia/redacao`:

```text
selection:
  provider=gemini
  model=gemini-3.5-flash
  expected_cost_usd=0.00036
  avg_score=5.0
  samples=1
  mode=exploration
  final_score=0.9
```

Resultado com `exclude_provider=gemini`:

```text
selection:
  provider=openai
  model=gpt-5.5
  mode=exploration
  final_score=0.903636
```

Adaptador:

```text
selection_strategy=quality_cost_router
provider=gemini
model=gemini-3.5-flash
pricing_table_version=2026-07-08-local-ratings
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_model_router_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.model_router_cli --editoria v4_ciencia_tecnologia_ia --funcao redacao --idempotency-key router-check
python3 -m v4_diretrizes.model_router_cli --editoria v4_ciencia_tecnologia_ia --funcao redacao --idempotency-key router-check --exclude-provider gemini
python3 -m v4_diretrizes.llm_adapter_cli --editoria v4_ciencia_tecnologia_ia --funcao redacao --titulo 'Teste roteador' --conteudo 'Material auditado para confirmar escolha do roteador V4.' --idempotency-key router-adapter-check
```

Resultado:

```text
OK 15 contract tests
```

Conclusao:

O V4 ja tem uma primeira camada objetiva de inteligencia de LLM. Ela ainda esta em modo `exploration` porque ha pouca amostra de feedback, mas ja combina qualidade observada, custo estimado e prioridade de rota sem hardcode editorial dentro dos agentes.

Proximo bloco recomendado:

```text
Registrar telemetria da decisao do roteador em JSONL/Prometheus e gerar painel local de comparacao por editoria/modelo.
```

---

## 31. Auditoria JSONL das Decisoes do Roteador LLM

Registrado em: 2026-07-08.

Objetivo:

```text
Registrar quem escolheu qual LLM, por qual regra, com qual custo esperado e qual prompt_hash.
```

Arquivos criados/alterados:

```text
diretrizes/v4_llm_decisions_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/llm_decisions.py
v4_diretrizes/llm_adapter.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/llm_decisions/decisions_20260708.jsonl
```

Contrato:

```text
JSONL decision failed -> generation blocked
Prometheus failed     -> generation not blocked
Rotacao               -> diaria
Destino               -> agent_data/v4/llm_decisions/decisions_YYYYMMDD.jsonl
```

Ultimo registro real:

```text
editoria=v4_ciencia_tecnologia_ia
funcao=redacao
idempotency_key=router-decision-check
selected_provider=gemini
selected_model=gemini-3.5-flash
selected_tier=gemini_luxo
selection_strategy=quality_cost_router
mode=exploration
expected_cost_usd=0.00036
candidate_count=4
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_llm_decisions_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.llm_adapter_cli --editoria v4_ciencia_tecnologia_ia --funcao redacao --titulo 'Teste decisao LLM' --conteudo 'Material auditado para trilha de decisao do roteador.' --idempotency-key router-decision-check
tail -n 3 agent_data/v4/llm_decisions/decisions_20260708.jsonl
```

Resultado:

```text
OK 17 contract tests
```

Conclusao:

O V4 agora tem trilha auditavel da decisao do roteador antes da geracao. Isso fecha o ciclo minimo de inteligencia LLM: candidatos externos, escolha por qualidade/custo, recibo de custo e decisao rastreavel.

Proximo bloco recomendado:

```text
Gerar painel local simples de ranking e decisoes:
feedback + receipts + recomputed + llm_decisions -> resumo por editoria/modelo.
```

---

## 32. Painel Local de Comparacao LLM

Registrado em: 2026-07-08.

Objetivo:

```text
Consolidar feedback, recibos, custos recomputados e decisoes do roteador em um painel local auditavel.
```

Arquivos criados/alterados:

```text
diretrizes/v4_llm_dashboard_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/llm_dashboard.py
v4_diretrizes/llm_dashboard_cli.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/reports/llm_dashboard_latest.json
agent_data/v4/reports/llm_dashboard_latest.md
```

Entradas:

```text
agent_data/v4/feedback/editor_feedback.jsonl
agent_data/v4/receipts/*.jsonl
agent_data/v4/receipts/recomputed/*.jsonl
agent_data/v4/llm_decisions/*.jsonl
```

Resumo atual:

```text
models_with_feedback=2
router_decisions=1
llm_receipts=2
total_cost_usd_estimated=0.00209878
```

Ranking atual:

```text
1. gemini/gemini-3.5-flash
   avg_score=5.0
   avg_cost_usd_estimated=0.00002378
   score_per_usd_estimated=210260.723

2. anthropic/claude-opus-4-8
   avg_score=4.0
   avg_cost_usd_estimated=0.002075
   score_per_usd_estimated=1927.711
```

Lacunas apontadas pelo painel:

```text
Poucas amostras de feedback para v4_ciencia_tecnologia_ia anthropic/claude-opus-4-8: 1/3
Poucas amostras de feedback para v4_ciencia_tecnologia_ia gemini/gemini-3.5-flash: 1/3
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_llm_dashboard_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.llm_dashboard_cli --execute --markdown
python3 -m json.tool agent_data/v4/reports/llm_dashboard_latest.json
```

Resultado:

```text
OK 19 contract tests
```

Conclusao:

O V4 agora tem painel local de inteligencia LLM sem depender de Prometheus, rede ou dashboard externo. Prometheus continua sendo camada de saude/agregado; o painel local usa a contabilidade JSONL auditavel.

Proximo bloco recomendado:

```text
Comecar o problema da imagem destacada V4:
contrato de banco de midia + acesso WordPress/R2 + avaliacao Gemini Vision + regra pessoa central/grande.
```

---

## 33. Imagem Destacada V4 — Contrato, Avaliador e Fonte Ouro

Registrado em: 2026-07-08.

Objetivo:

```text
Criar a base limpa da imagem destacada V4 sem hardcode no produtor.
```

Arquivos criados/alterados:

```text
diretrizes/v4_imagem_destacada_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/imagem_destacada.py
v4_diretrizes/imagem_destacada_cli.py
v4_diretrizes/media_sources.py
v4_diretrizes/media_sources_cli.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/media/decisions/featured_image_decisions_20260708.jsonl
```

Regras fundamentais do contrato:

```text
produtor_nao_busca_midia_bruta=true
publicador_usa_apenas_midia_auditada=true
direitos_obrigatorios=true
pessoa_do_titulo_deve_aparecer_grande_central=true
avaliacao_visual_obrigatoria_para_pessoa=true
metadados_nao_bastam_para_pessoa=true
```

Fontes configuradas:

```text
ouro_sqlite
biblioteca_editorial
wordpress_media
r2_catalog
flickr_candidates
```

Gate deterministico inicial:

```text
dimensao minima
aspect ratio aceitavel
sem thumbnail/avatar/logo
credito obrigatorio
licenca obrigatoria
rights_status aceito
score minimo por pessoa/tema
```

Gate visual atual:

```text
mode_default=mock
real_calls_enabled=false
provider futuro=gemini
function futura=tribunal_visual
```

Primeira decisao V4 registrada:

```text
title=Flavio Bolsonaro critica decisao do STF
primary_entity=Flavio Bolsonaro
selected=demo_flavio_001
source=ouro_sqlite
reason_class=person_central
visual_confidence=0.92
final_score=90.7
blocked=false
```

Teste do Banco Ouro real neste ambiente:

```text
db_path=/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db
ok=false
reason=db_unavailable
```

Observacao:

O caminho real do Banco Ouro aponta para `/root/...` e nao esta acessivel por este processo local. O V4 agora trata isso como indisponibilidade limpa, sem traceback e sem derrubar o texto.

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_imagem_destacada_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.imagem_destacada_cli --title 'Flavio Bolsonaro critica decisao do STF' --primary-entity 'Flavio Bolsonaro' --requires-person --execute --candidate-json '{...}'
python3 -m v4_diretrizes.media_sources_cli --source ouro_sqlite --title 'Flavio Bolsonaro critica decisao do STF' --primary-entity 'Flavio Bolsonaro' --limit 3
```

Resultado:

```text
OK 25 contract tests
```

Conclusao:

O V4 ja tem a primeira base limpa da imagem destacada: contrato externo, avaliador tecnico, decisao JSONL append-only e coletor Ouro normalizado. Ainda falta ligar fontes reais acessiveis, WordPress/R2 e Gemini Vision real.

Proximo bloco recomendado:

```text
Implementar acervo auditado local V4:
candidato aprovado -> agent_data/v4/media/audited/*.jsonl -> publicador so le audited.
```

---

## 34. Acervo Auditado Local de Midia V4

Registrado em: 2026-07-08.

Objetivo:

```text
Separar candidatos de midia da camada auditada que o publicador podera usar.
```

Arquivos criados/alterados:

```text
v4_diretrizes/media_audit.py
v4_diretrizes/media_audit_cli.py
v4_diretrizes/imagem_destacada_cli.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/media/audited/audited_media_20260708.jsonl
```

Regra implementada:

```text
avaliacao reprovada -> nao promove
avaliacao aprovada  -> grava append-only em audited
publicador futuro   -> deve ler somente audited
```

Registro auditado criado:

```text
image_id=demo_flavio_001
entity=Flavio Bolsonaro
source=ouro_sqlite
rights_status=fonte_oficial
credit=Agencia Senado
license=Fonte oficial - uso editorial com credito
reason_class=person_central
visual_confidence=0.92
final_score=90.7
safe_to_publish=true
```

Busca local:

```bash
python3 -m v4_diretrizes.media_audit_cli --entity 'Flavio Bolsonaro'
```

Resultado:

```text
records=1
image_id=demo_flavio_001
safe_to_publish=true
```

Comandos executados:

```bash
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.imagem_destacada_cli --title 'Flavio Bolsonaro critica decisao do STF' --primary-entity 'Flavio Bolsonaro' --requires-person --execute --promote-audited --candidate-json '{...}'
python3 -m v4_diretrizes.media_audit_cli --entity 'Flavio Bolsonaro'
```

Resultado:

```text
OK 27 contract tests
```

Conclusao:

O V4 agora tem uma fronteira clara para midia: candidatos podem vir de varias fontes, mas o publicador so deve consumir imagens promovidas para `audited`. Isso reduz contaminacao e impede que busca bruta vire imagem destacada diretamente.

Proximo bloco recomendado:

```text
Integrar consulta do acervo auditado ao fluxo dry-run:
materia auditada + entidade principal -> media auditada -> publicacao dry-run bloqueia se nao houver imagem.
```

---

## 35. Fluxo Dry-Run com Imagem Auditada Obrigatoria

Registrado em: 2026-07-08.

Objetivo:

```text
Impedir que a publicacao V4 avance sem imagem destacada auditada.
```

Arquivos criados/alterados:

```text
diretrizes/v4_fluxo_dry_run_v1.json
v4_diretrizes/fluxo.py
v4_diretrizes/test_contracts.py
v4_data/auditado/v4_fixture_006.json
v4_data/producao/v4_fixture_006.producao.json
v4_data/auditado/v4_fixture_006.auditado_final.json
v4_data/publicado/v4_fixture_006.publicado_dry_run.json
```

Regra implementada:

```text
publicar_dry_run:
  exige primary_entity
  consulta agent_data/v4/media/audited
  se nao houver imagem -> mode=blocked_media
  se houver imagem -> anexa featured_media e grava publicacao dry-run
```

Fixture novo:

```text
item_id=v4_fixture_006
editoria=v4_politica_economia
titulo=Flavio Bolsonaro critica decisao do STF
primary_entity=Flavio Bolsonaro
```

Resultado:

```text
featured_media.image_id=demo_flavio_001
featured_media.source=ouro_sqlite
featured_media.safe_to_publish=true
featured_media.final_score=90.7
publicacao_dry_run.featured_media_source=agent_data/v4/media/audited
manifesto.imagem_destacada_validada=true
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_fluxo_dry_run_v1.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.fluxo_cli --execute
python3 -m json.tool v4_data/publicado/v4_fixture_006.publicado_dry_run.json
```

Resultado:

```text
OK 29 contract tests
```

Conclusao:

O fluxo V4 agora respeita a fronteira de midia: texto auditado sozinho nao basta para publicacao. O publicador dry-run so avanca quando encontra imagem destacada em `media/audited`.

Proximo bloco recomendado:

```text
Criar publicador WordPress V4 em modo seguro:
dry-run por padrao, pending/draft so com flag explicita, recibo JSONL obrigatorio, featured_media obrigatorio.
```

---

## 36. Publicador WordPress V4 Seguro

Registrado em: 2026-07-08.

Objetivo:

```text
Criar publicador WordPress tecnico, dry-run por padrao, sem LLM, sem busca de imagem e sem publicacao real habilitada inicialmente.
```

Arquivos criados/alterados:

```text
diretrizes/v4_wordpress_publicador_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/wordpress_publicador.py
v4_diretrizes/wordpress_publicador_cli.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/publication/wordpress_attempts_20260708.jsonl
```

Regras implementadas:

```text
dry_run_por_padrao=true
real_publish.enabled=false
featured_media_obrigatoria=true
publicador_nao_chama_llm=true
publicador_nao_busca_imagem_bruta=true
status real permitido futuramente apenas draft/pending
status publish proibido
```

Execucao real de dry-run:

```bash
python3 -m v4_diretrizes.wordpress_publicador_cli \
  --source-path v4_data/publicado/v4_fixture_006.publicado_dry_run.json \
  --execute
```

Resultado:

```text
ok=true
outcome=dry_run
status=pending
item_id=v4_fixture_006
featured_media_image_id=demo_flavio_001
featured_media=null
```

Observacao:

`featured_media` esta `null` no payload WordPress porque ainda nao existe `wp_media_id` no registro auditado. Isso nao bloqueia dry-run, mas bloqueia modo real. A proxima etapa e reconciliar/uploadar imagem auditada para obter `wp_media_id`.

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_wordpress_publicador_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.wordpress_publicador_cli --source-path v4_data/publicado/v4_fixture_006.publicado_dry_run.json --execute
```

Resultado:

```text
OK 32 contract tests
```

Conclusao:

O V4 agora tem um publicador WordPress tecnico e seguro. Ele prepara payload, valida imagem auditada, registra tentativa append-only e mantem publicacao real bloqueada ate resolver credenciais, `wp_media_id` e contrato explicito.

Proximo bloco recomendado:

```text
Implementar reconciliacao WordPress Media:
audited image_id/url -> wp_media_id existente ou upload futuro -> audited record enriquecido append-only.
```

---

## 37. Reconciliacao WordPress Media V4

Registrado em: 2026-07-08.

Objetivo:

```text
Resolver image_id auditado para wp_media_id antes de publicacao real.
```

Arquivos criados/alterados:

```text
diretrizes/v4_wordpress_media_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/wordpress_media.py
v4_diretrizes/wordpress_media_cli.py
v4_diretrizes/wordpress_publicador.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/media/wp_mappings/wp_media_mappings_20260708.jsonl
agent_data/v4/publication/wordpress_attempts_20260708.jsonl
```

Regra implementada:

```text
audited image_id -> lookup local append-only -> wp_media_id
publicador usa wp_media_id se existir
upload real segue desabilitado inicialmente
```

Mapeamento registrado:

```text
image_id=demo_flavio_001
wp_media_id=260961
source=manual_memoria_v3
credit=Agencia Senado
license=Fonte oficial - uso editorial com credito
```

Resultado no publicador:

```text
item_id=v4_fixture_006
outcome=dry_run
payload.featured_media=260961
status=pending
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_wordpress_media_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.wordpress_media_cli --image-id demo_flavio_001 --wp-media-id 260961 --source manual_memoria_v3 --url 'https://cdn.example.com/flavio-bolsonaro-retrato.jpg' --credit 'Agencia Senado' --license 'Fonte oficial - uso editorial com credito' --operator codex --execute
python3 -m v4_diretrizes.wordpress_publicador_cli --source-path v4_data/publicado/v4_fixture_006.publicado_dry_run.json --execute
python3 -m v4_diretrizes.wordpress_media_cli --image-id demo_flavio_001 --lookup
```

Resultado:

```text
OK 34 contract tests
```

Conclusao:

O V4 ja consegue preparar payload WordPress com imagem destacada numerica (`featured_media=260961`) sem chamada real. Falta apenas habilitar upload/reconhecimento real quando as credenciais e o contrato de publicacao forem liberados.

Proximo bloco recomendado:

```text
Criar painel operacional V4:
camadas + bloqueios + publicador + midia + LLM + custos em um resumo unico.
```

---

## 38. Painel Operacional V4 Consolidado

Registrado em: 2026-07-08.

Objetivo:

```text
Gerar visao local unica de camadas, telemetria, midia, WordPress e alertas operacionais.
```

Arquivos criados/alterados:

```text
diretrizes/v4_operational_dashboard_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/operational_dashboard.py
v4_diretrizes/operational_dashboard_cli.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
agent_data/v4/reports/operational_dashboard_latest.json
agent_data/v4/reports/operational_dashboard_latest.md
```

Resumo atual:

```text
camadas:
  auditado=12
  producao=6
  publicado=6

telemetria:
  receipts=9
  recomputed_costs=6
  llm_decisions=2

midia:
  audited=1
  wp_mappings=1
  audited_without_wp_mapping=0

wordpress:
  attempts=3
  dry_run=2
  blocked=1
  posted=0
```

Alerta atual:

```text
warning: tentativas WordPress bloqueadas: 1
```

Observacao:

A tentativa bloqueada e historica/append-only: ocorreu antes do ajuste do contrato `texto_dry_run`/`conteudo`. A tentativa mais recente esta correta e saiu com `featured_media=260961`.

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_operational_dashboard_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.operational_dashboard_cli --execute --markdown
```

Resultado:

```text
OK 35 contract tests
```

Conclusao:

O V4 agora tem painel operacional local sem rede e sem Prometheus obrigatorio. Ele serve como ponto de controle rapido para retomada, limpeza, bloqueios, midia e publicador.

Proximo bloco recomendado:

```text
Antes de habilitar real publish:
1. confirmar credenciais WordPress V4;
2. trocar URLs demo por URLs reais/R2;
3. ligar upload ou lookup real da biblioteca de midia;
4. habilitar contrato real_publish apenas para draft/pending.
```

---

## 39. Publicacao Real em Rascunho WordPress

Registrado em: 2026-07-08.

Objetivo:

```text
Validar publicacao real controlada no WordPress como draft, sem publicar ao publico.
```

Credenciais:

```text
Usadas a partir de Outros/chaves/wp_cafezinho_chatbots.md
Senha nao registrada neste forum.
```

Preflight:

```text
media_id=260961 verificado via REST
slug=teste-v4-integracao-wordpress-rascunho-codex
dedupe por slug executado antes do POST
status=draft
author=5470
category=22
featured_media=260961
```

Resultado WordPress:

```text
HTTP=201
post_id=261437
status=draft
slug=teste-v4-integracao-wordpress-rascunho-codex
featured_media=260961
link=https://controle.ocafezinho.com/?p=261437
```

Observacao editorial:

O rascunho foi criado como teste tecnico, com titulo:

```text
[TESTE V4] Integração WordPress em rascunho
```

Isso evita que uma fixture tecnica pareca uma materia real dentro do WordPress.

Ledger V4:

```text
agent_data/v4/publication/wordpress_attempts_20260708.jsonl
mode=real
outcome=posted
wp_response.post_id=261437
wp_response.post_status=draft
```

Painel operacional atualizado:

```text
wordpress.attempts=4
wordpress.dry_run=2
wordpress.blocked=1
wordpress.posted=1
```

Comandos/validacoes:

```bash
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.operational_dashboard_cli --execute --markdown
```

Resultado:

```text
OK 35 contract tests
```

Conclusao:

O V4 conseguiu criar um rascunho real no WordPress com imagem destacada, mantendo o registro local append-only. Publicacao publica continua nao autorizada.

---

## 40. Smoke Test de Producao Controlado

Registrado em: 2026-07-08.

Objetivo:

```text
Executar novo teste de producao V4 com escrita real no WordPress, mantendo status draft.
```

Resultado WordPress:

```text
HTTP=201
post_id=261438
status=draft
slug=teste-v4-producao-controlada-codex
featured_media=260961
link=https://controle.ocafezinho.com/?p=261438
```

Titulo:

```text
[TESTE V4 PRODUÇÃO] Smoke test controlado
```

Validacoes:

```text
dedupe por slug antes do POST
media_id=260961 validado
author=5470
category=22
status=draft
publicacao publica nao autorizada
```

Ledger V4:

```text
agent_data/v4/publication/wordpress_attempts_20260708.jsonl
mode=real
outcome=posted
wp_response.post_id=261438
wp_response.post_status=draft
```

Painel operacional:

```text
wordpress.attempts=5
wordpress.dry_run=2
wordpress.blocked=1
wordpress.posted=2
```

Resultado:

```text
OK 35 contract tests
```

Conclusao:

O caminho V4 ate WordPress foi validado novamente com um rascunho real e imagem destacada. O sistema ainda nao deve publicar publicamente sem contrato especifico e aprovacao editorial.

---

## 41. Ingestao V4 em Tres Camadas

Registrado em: 2026-07-08.

Objetivo:

```text
Criar fluxo real de conteudo antes da producao: bruto -> intermediario -> auditado.
```

Estado anterior:

```text
bruto=0
intermediario=0
auditado tinha apenas fixtures ja auditadas
```

Arquivos criados/alterados:

```text
diretrizes/v4_ingestao_conteudo_v1.json
diretrizes/mapa_v4_contexto_llm.json
v4_diretrizes/content_ingestion.py
v4_diretrizes/content_ingestion_cli.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
v4_data/bruto/v4_ingest_001.bruto.json
v4_data/intermediario/v4_ingest_001.intermediario.json
v4_data/auditado/v4_ingest_001.json
```

Fluxo executado:

```text
coletor:
  escreve v4_data/bruto/v4_ingest_001.bruto.json
  manifesto_origem obrigatorio

processador:
  le bruto
  escreve intermediario
  normaliza conteudo
  calcula hash_conteudo
  executa dedupe_check

auditor:
  le intermediario
  escreve auditado
  manifesta fonte_validada, risco_juridico_revisado, qualidade_minima
```

Resultado operacional:

```text
bruto=1
intermediario=1
auditado=13
dedupe_check.is_duplicate=false
hash_conteudo=56f38e250465449c1056b1bee1d2d83c213842054126b8d75da06ca49bedf40e
```

Comandos executados:

```bash
python3 -m json.tool diretrizes/v4_ingestao_conteudo_v1.json
python3 -m json.tool diretrizes/mapa_v4_contexto_llm.json
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
python3 -m v4_diretrizes.content_ingestion_cli --execute
python3 -m v4_diretrizes.operational_dashboard_cli --execute --markdown
```

Resultado:

```text
OK 37 contract tests
```

Conclusao:

Agora o V4 tem coleta e bancos de conteudo nas tres camadas iniciais. O produtor continua proibido de ler `bruto` e `intermediario`; ele so pode trabalhar sobre `auditado`.

Proximo bloco recomendado:

```text
Ligar item auditado de ingestao ao fluxo produtor/publicador:
v4_ingest_001 auditado -> producao -> auditado_final -> publicado/draft.
```

## 2026-07-08 20:17 BRT — Primeiro rascunho real editorial V4 no WordPress

Atendendo ao pedido do Miguel, foi feito um teste real controlado: o V4 produziu uma materia de verdade e gravou no WordPress apenas como rascunho. Nao houve publicacao aberta ao publico.

Materia:

```text
item_id: v4_real_001
titulo: Tarifa dos EUA vira disputa entre Lula e Flavio antes da eleicao
editoria: v4_politica_economia
slug: tarifa-eua-lula-flavio-bolsonaro-eleicao-2026-v4
status WordPress: draft
post_id WordPress: 261439
featured_media: 260961
```

Fontes usadas:

```text
AP:
https://apnews.com/article/brazil-lula-bolsonaro-tariffs-d376eb50aa2b7f82b407dd0e47e8e44a

El Pais:
https://elpais.com/america/2026-07-07/bolsonaro-hijo-viaja-a-washington-para-intentar-evitar-un-nuevo-castigo-arancelario-que-dane-su-campana.html
```

Camadas gravadas:

```text
v4_data/bruto/v4_real_001.bruto.json
v4_data/intermediario/v4_real_001.intermediario.json
v4_data/auditado/v4_real_001.json
v4_data/producao/v4_real_001.producao.json
v4_data/auditado/v4_real_001.auditado_final.json
v4_data/publicado/v4_real_001.wordpress_draft.json
```

O que isso prova:

```text
1. O V4 ja tem coleta/conteudo bruto.
2. O V4 ja tem camada intermediaria normalizada.
3. O V4 ja tem camada auditada antes da producao.
4. O produtor trabalha sobre material auditado, nao sobre o bruto.
5. O publicador consegue criar rascunho real no WordPress.
6. A imagem destacada auditada foi conectada ao rascunho.
7. O estado fica registrado localmente para auditoria e retomada.
```

Validacoes executadas:

```bash
python3 -m v4_diretrizes.operational_dashboard_cli --execute --markdown
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
```

Resultados:

```text
OK 37 contract tests

Dashboard:
bruto=2
intermediario=2
auditado=15
producao=7
publicado=7
WordPress posted=3
WordPress blocked=1
```

Leitura humana do estado:

O V4 ainda nao esta pronto para rodar sozinho. Ele ja tem a espinha dorsal: diretrizes externas, camadas de dados separadas, recibos, telemetria, imagem destacada auditada e publicacao em rascunho. O que falta agora e transformar esse fluxo em agente completo, com roteador LLM real, revisao por modelo diferente do produtor, controle de custo/qualidade por modelo, selecao automatica de midia melhor e fila de producao.

Regra preservada:

```text
Sem supervisao humana, nao publicar.
Com supervisao humana, o V4 pode gerar rascunhos reais para revisao.
```

## 2026-07-08 20:22 BRT — Feedback editorial do Miguel e novo forum de curadoria

Miguel avaliou o primeiro rascunho real do V4:

```text
Materia ficou sem graca, obvia, repetitiva.
Mas gostei do texto e da maneira como as noticias foram mescladas.
```

Interpretacao:

```text
O fluxo tecnico funcionou.
A costura factual funcionou.
O problema esta na curadoria, na tese e na energia editorial.
```

Forum aberto para a Trindade e para Miguel:

```text
Cerebro/Foruns/forum_v4_curadoria_tese_editorial_20260708.md
```

Novo requisito pro V4:

```text
Antes da redacao, criar etapa de curadoria de tese.
O V4 deve escolher uma tese editorial forte antes de escrever.
Texto correto, mas obvio, deve ser tratado como bug editorial.
```

Correcao de protocolo de comunicacao:

```text
Toda comunicacao com agentes sobre o V4 deve:
1. registrar a substancia no forum apropriado;
2. pontuar de forma curta no Canal da Trindade, com link para o forum;
3. manter inboxes limpos e curtos;
4. pedir cartinha humanizada para Miguel no chat e no forum;
5. limpar o Canal da Trindade quando ficar comprido, sempre depois de backup datado.
```
