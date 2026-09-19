# Forum - Plano de Trabalho para Execucao do Novo Sistema V3

Aberto em: 2026-07-08  
Responsavel operacional: Codex  
Status: plano de codificacao, execucao faseada

## 1. Objetivo

Construir o novo sistema de agentes V3 aproveitando o que ja existe, sem reescrever tudo do zero.

O sistema novo deve ter:

- agentes tecnicos, sem hardcode editorial;
- diretrizes externas, dinamicas e versionadas;
- editorias V3 fortes;
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
  nucleo_editorial_comum_v1.md
  v3_politica_economia_v1.md
  v3_cultura_v1.md
  v3_internacional_v1.md
  v3_repetidor_v1.md
  gsn_espelho_ingles_v1.md
  freios_llm_v1.json
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
Cerebro/Foruns/forum_novo_sistema_agentes_v3_e_diretrizes_20260707.md
Cerebro/Foruns/forum_super_luxo_editorial_v3_espelhado_20260707.md
Cerebro/Foruns/forum_novas_diretrizes_editoriais_correio_brasil_20260707.md
Cerebro/Foruns/forum_backup_retomada_backblaze_pre_reforma_20260707.md
tmp_v3_docs/PLANO_URGENTE_USO_BANCO_LEGADO_MIDIA_V3_20260626.md
forum_status_acervo_midia_r2_publicador_20260625.md
```

## 4. Fase 0 - Preservacao Seletiva

Antes de codar, fazer backup seletivo dos arquivos que serao alterados.

Escopo minimo:

- `diretrizes/`
- `Cerebro/Foruns/forum_novo_sistema_agentes_v3_e_diretrizes_20260707.md`
- scripts V3 que forem tocados;
- memoria de bugs se for convertida para formato estruturado;
- novos modulos de diretrizes/autocura.

Nao retomar backup total do workspace nesta fase.

Destino recomendado:

```text
Backups/pre_execucao_novo_v3_20260708/
b2:failover-cafezinho1/Antigravity_Google/backups/pre_execucao_novo_v3_20260708/
```

## 5. Fase 1 - Inventario Tecnico Real

Mapear como o V3 funciona hoje:

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
Cerebro/Foruns/forum_mapa_tecnico_v3_atual_20260708.md
```

## 6. Fase 2 - Criar Camada Externa de Diretrizes

Criar um modulo tecnico para carregar diretrizes sem hardcode.

Modulo proposto:

```text
v3_diretrizes/
  __init__.py
  loader.py
  schema.py
  registry.py
  composer.py
```

Responsabilidades:

- carregar `diretrizes/*.md` e `freios_llm_v1.json`;
- resolver editoria para arquivo correto;
- montar contrato editorial para o agente;
- injetar memoria de bugs relevante;
- injetar comentarios recentes do editor;
- registrar versao/hash da diretriz usada;
- falhar de modo claro se diretriz obrigatoria estiver ausente.

Regra:

> script tecnico pergunta ao loader qual diretriz usar; nao embute regra editorial no codigo.

## 7. Fase 3 - Adicionar V3 Ciencia, Tecnologia e IA

Criar nova diretriz:

```text
diretrizes/v3_ciencia_tecnologia_ia_v1.md
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
v3_memoria/
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
v3_imagem_destacada/
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

## 10. Fase 6 - Classificador e Roteador V3

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
v3_orquestrador/
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
v3_validadores/
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
artifacts/v3_shadow_20260708/
Cerebro/Foruns/forum_shadow_novo_v3_20260708.md
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
3. Criar `v3_diretrizes` e teste unitario simples.
4. Criar `v3_ciencia_tecnologia_ia_v1.md`.
5. Criar `v3_memoria` append-only.
6. Criar contrato de imagem destacada.
7. Conectar loader em modo dry-run a um script V3, sem alterar publicacao.
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
- depois iniciar `v3_diretrizes`.

---

## 18. Atualizacao Pela Rodada 2 Fechada

Registrado em: 2026-07-08.

GLM Ming/5.1 respondeu e trouxe um ponto tecnico que altera a estrategia de implementacao:

> O sistema ja e parcialmente hibrido hoje. `Projeto Cafezinho Agentes/root/config/llm_context_routes.json` externaliza roteamento LLM por contexto editorial. A nova camada de diretrizes deve estender esse padrao, nao criar arquitetura paralela.

Acao incorporada ao plano:

1. auditar `Projeto Cafezinho Agentes/root/config/llm_context_routes.json`;
2. auditar `modelos_vivos.json`, `llm_providers.json`, `llm_ratings.json` e roteador associado;
3. criar `diretrizes/mapa_v3_contexto_llm.json` como extensao formal do padrao existente;
4. mapear contextos atuais para V3 Politica/Economia, Cultura, Internacional, Ciencia/Tecnologia/IA e Repetidor;
5. manter `v3_diretrizes` como loader externo, mas acoplar ao contexto LLM existente em vez de duplicar roteamento;
6. validar arquitetura de imagem no Tencent antes de mexer em pipeline real.

Nova prioridade imediata:

- antes de criar modulo novo, ler e testar o roteamento existente.
