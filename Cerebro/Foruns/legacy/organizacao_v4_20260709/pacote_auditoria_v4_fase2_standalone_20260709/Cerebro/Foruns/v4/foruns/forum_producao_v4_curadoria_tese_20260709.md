# Forum de Producao V4 — curadoria de tese

## Estado atual apos limpeza de organizacao — 2026-07-09

Regra corrigida:

```text
Cerebro/Foruns/v4/ e diretorio de discussao/auditoria, nao fonte viva de producao.
Nao deve conter copias descompactadas de diretrizes/, v4_diretrizes/ ou v4_data/.
```

Fontes vivas/canonicas:

```text
diretrizes/
v4_diretrizes/
v4_data/
```

Material para Fable/GPT 5.5/AGY:

```text
Cerebro/Foruns/v4/auditoria/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

Copias intermediarias antigas foram movidas para:

```text
Cerebro/Foruns/legacy/organizacao_v4_20260709/
```

Nao usar instrucoes historicas abaixo que apontem para `Cerebro/Foruns/v4/diretrizes/`; esse espelho descompactado foi removido.

Criado em: 2026-07-09  
Responsavel de execucao inicial: Codex  
Status: implementacao autorizada em fatia fina, sem publicacao real.

## Origem

Forum de concepcao e consenso:

```text
Cerebro/Foruns/v4/foruns/forum_v4_curadoria_tese_editorial_20260708.md
```

Diretorio de diretrizes canônico:

```text
diretrizes/
```

Pacote zipado para auditoria externa:

```text
Cerebro/Foruns/v4/auditoria/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

Regra importante:

```text
Arquivos canonicos ficam em diretrizes/, v4_diretrizes/ e v4_data/.
Cerebro/Foruns/v4/ contem apenas discussao, cartas e pacote zipado de auditoria.
```

## Martelo final

Fable:

```text
Aprovo com ajustes.
```

GPT 5.5 Pro:

```text
Aprovo com ajustes bloqueantes minimos.
```

## Bloqueantes incorporados antes da codagem

```text
1. v4_curadoria_tese_v1.json precisa nascer enxuto.
2. curadoria_id vira gate tecnico real.
3. modo_experimento permite versao A sem curadoria apenas em dry-run, logado, nunca rascunho real.
4. leitura_corrente_timestamped precisa ter fonte/proveniencia.
5. produtor nao le auditado cru em editoria nobre.
6. publicador bloqueia rascunho real sem curadoria_id.
7. imagem recebe frame_visual da curadoria.
8. A/B do 261439 e parte da Fase 1.
9. testes nascem junto com contrato/gates.
```

## Ordem de implementacao

```text
contrato -> camada/agente -> testes -> modulo dry-run -> fixture -> A/B
```

## Fase 1 autorizada

```text
- criar contrato de curadoria;
- criar camada curadoria;
- criar agente curador;
- criar gates de produtor/publicador;
- criar frame_visual;
- criar advogado do obvio simples;
- registrar BUG-EDITORIAL-V4-001 como caso;
- rodar A/B dry-run do 261439.
```

## Fora de escopo agora

```text
- publicacao real;
- dashboards sofisticados;
- autocura autonoma;
- fusao ampla dos arquivos;
- upload real de midia;
- Prometheus avancado;
- institucionalizar a curadoria antes do A/B.
```

## Registro de execucao

### 2026-07-09 — Inicio Codex

Codex vai implementar a fatia fina no repositorio local, mantendo:

```text
- canonical source em diretrizes/ e v4_diretrizes/;
- espelho de auditoria em Cerebro/Foruns/v4/diretrizes/;
- testes de contrato antes de considerar a etapa pronta;
- forum atualizado a cada bloco relevante.
```

### 2026-07-09 — Fatia fina implementada

Status: primeira fatia tecnica pronta em dry-run. Sem publicacao real, sem chamada LLM real, sem upload de midia.

Arquivos canonicos criados:

```text
diretrizes/v4_curadoria_tese_v1.json
diretrizes/v4_feedback_casos_editoriais_v1.json
v4_diretrizes/curadoria_tese.py
v4_diretrizes/curadoria_tese_cli.py
v4_diretrizes/ab_experiment.py
v4_diretrizes/ab_experiment_cli.py
```

Arquivos canonicos alterados:

```text
diretrizes/v4_agentes_tecnicos_v1.json
diretrizes/v4_bancos_camadas_v1.json
diretrizes/v4_fluxo_dry_run_v1.json
diretrizes/v4_wordpress_publicador_v1.json
diretrizes/v4_imagem_destacada_v1.json
v4_diretrizes/fluxo.py
v4_diretrizes/wordpress_publicador.py
v4_diretrizes/test_contracts.py
v4_diretrizes/__init__.py
```

O que entrou:

```text
- camada curadoria entre auditado e producao;
- agente curador;
- produtor de editoria nobre lendo curadoria, nao auditado cru;
- publicador exigindo curadoria_id;
- frame_visual vindo da curadoria para imagem;
- contrato enxuto de curadoria;
- leitura_corrente_timestamped com fonte/proveniencia;
- aliases de entrada aceitos e normalizados;
- advogado do obvio simples;
- modo_experimento permitindo ausencia de curadoria_id somente em dry-run;
- caso BUG-EDITORIAL-V4-001 registrado como seed de memoria editorial;
- A/B dry-run do 261439 gerado localmente.
```

Validacoes executadas:

```text
python3 -m json.tool ...              # contratos JSON alterados validos
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
Resultado: OK 44 contract tests
python3 -m v4_diretrizes.fluxo_cli
Resultado: fluxo planejado auditado -> curadoria -> producao -> auditado -> publicado
python3 -m v4_diretrizes.ab_experiment_cli --case 261439 --execute
Resultado: pacote A/B dry-run gravado, sem WordPress
```

Artefatos gerados para o smoke test A/B:

```text
v4_data/curadoria/v4_real_001.curadoria.json
v4_data/producao/v4_real_001.variant_b.producao.json
agent_data/v4/ab_experiments/ab_261439_curadoria_v4_fase_1.json
```

Espelho para auditoria externa:

```text
Cerebro/Foruns/v4/diretrizes/v4_curadoria_tese_v1.json
Cerebro/Foruns/v4/diretrizes/v4_feedback_casos_editoriais_v1.json
Cerebro/Foruns/v4/diretrizes/v4_agentes_tecnicos_v1.json
Cerebro/Foruns/v4/diretrizes/v4_bancos_camadas_v1.json
Cerebro/Foruns/v4/diretrizes/v4_fluxo_dry_run_v1.json
Cerebro/Foruns/v4/diretrizes/v4_wordpress_publicador_v1.json
Cerebro/Foruns/v4/diretrizes/v4_imagem_destacada_v1.json
Cerebro/Foruns/v4/diretrizes/v4_real_001.curadoria.json
Cerebro/Foruns/v4/diretrizes/v4_real_001.variant_b.producao.json
Cerebro/Foruns/v4/diretrizes/ab_261439_curadoria_v4_fase_1.json
```

Observacao editorial:

```text
A versao B do A/B ainda e uma saida deterministica de smoke test, nao uma materia final para publicar.
O objetivo e testar se o contrato de curadoria muda a hierarquia editorial e se os auditores aprovam os gates.
```

Pendencias imediatas antes de seguir para Fase 2:

```text
1. Fable e GPT 5.5 Pro auditarem contrato, gates, testes e pacote A/B.
2. Decidir se o texto B precisa passar por redator LLM real/super_luxo em uma rodada controlada.
3. Integrar leitura corrente real por busca/API depois do primeiro A/B manual.
4. Evoluir o advogado do obvio de heuristica simples para comparacao mais robusta.
5. Separar qualidade por funcao no dashboard depois de haver massa critica.
```

### 2026-07-09 — Ajustes pos-re-auditoria Fable

Fable aprovou a fatia fina com ajustes e pediu cinco correcoes antes do redator LLM real/super_luxo:

```text
1. fatos_travados como lista estruturada;
2. guarda anti-eco de template;
3. esclarecer escopo dos bloqueios de camada;
4. normalizacao/validacao de encoding antes de payload WordPress real;
5. espelhar os .py para auditoria real.
```

Alteracoes incorporadas:

```text
- v4_curadoria_tese_v1.json agora exige fatos_travados;
- curadoria_tese.py exporta fatos_travados como array estruturado;
- ab_experiment.py carrega fatos_travados na variante B;
- validacao anti-eco bloqueia prefixos genericos como fato_novo;
- v4_bancos_camadas_v1.json declara fase_1_toda_producao_passa_por_curadoria e scope=fase_1_global nos bloqueios;
- wordpress_publicador.py valida mojibake e payload portugues ASCII-only antes de publicacao real;
- variante B foi regenerada com acentuacao normal;
- arquivo cego separado criado para Miguel;
- .py centrais espelhados em Cerebro/Foruns/v4/diretrizes/.
```

Validacao:

```text
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
Resultado: OK 45 contract tests
```

Novos/atualizados no espelho:

```text
Cerebro/Foruns/v4/diretrizes/ab_261439_julgamento_cego_miguel.md
Cerebro/Foruns/v4/diretrizes/ab_261439_artigos_para_auditoria.md
Cerebro/Foruns/v4/diretrizes/v4_diretrizes_curadoria_tese.py
Cerebro/Foruns/v4/diretrizes/v4_diretrizes_ab_experiment.py
Cerebro/Foruns/v4/diretrizes/v4_diretrizes_test_contracts.py
Cerebro/Foruns/v4/diretrizes/v4_diretrizes_fluxo.py
Cerebro/Foruns/v4/diretrizes/v4_diretrizes_wordpress_publicador.py
```

### 2026-07-09 — Correcao da brecha Fable rodada 3

Fable rodou probes adversariais e encontrou uma brecha real:

```text
Contrato dizia publicacao_real_exige_fonte_nao_manual: true,
mas validate_gate nao bloqueava leitura_corrente_timestamped.fonte=manual_editor em modo real.
```

Correcao aplicada:

```text
v4_diretrizes/curadoria_tese.py
- validate_gate agora verifica fonte da leitura corrente antes de liberar modo real;
- modo real/draft real bloqueia fonte manual_editor;
- modo real/draft real tambem bloqueia leitura corrente sem fonte.

v4_diretrizes/test_contracts.py
- adicionado test_publicacao_real_bloqueia_fonte_manual.
```

Validacao:

```text
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
Resultado: OK 46 contract tests

Probe manual:
manual_real_ok=False
manual_real_issues=['leitura_corrente_manual_bloqueada_publicacao_real']
```

Espelho atualizado:

```text
Cerebro/Foruns/v4/diretrizes/v4_diretrizes_curadoria_tese.py
Cerebro/Foruns/v4/diretrizes/v4_diretrizes_test_contracts.py
Cerebro/Foruns/v4/diretrizes/v4_curadoria_tese_v1.json
```

### 2026-07-09 — Reconciliacao do espelho apos parecer externo

Novo parecer externo informou que o pacote recebido ainda tinha:

```text
- v4_fluxo_dry_run_v1.json saindo de auditado direto para producao;
- v4_agentes_tecnicos_v1.json sem curador e com produtor/imagem lendo auditado;
- v4_feedback_casos_editoriais_v1.json ausente.
```

Verificacao local mostrou que o espelho atual nao esta assim. O parecer provavelmente leu pacote antigo/cacheado.

Resultado da comparacao fonte viva vs espelho:

```text
diretrizes/v4_fluxo_dry_run_v1.json == Cerebro/Foruns/v4/diretrizes/v4_fluxo_dry_run_v1.json
diretrizes/v4_agentes_tecnicos_v1.json == Cerebro/Foruns/v4/diretrizes/v4_agentes_tecnicos_v1.json
diretrizes/v4_feedback_casos_editoriais_v1.json == Cerebro/Foruns/v4/diretrizes/v4_feedback_casos_editoriais_v1.json
diretrizes/v4_bancos_camadas_v1.json == Cerebro/Foruns/v4/diretrizes/v4_bancos_camadas_v1.json
diretrizes/v4_wordpress_publicador_v1.json == Cerebro/Foruns/v4/diretrizes/v4_wordpress_publicador_v1.json
diretrizes/v4_curadoria_tese_v1.json == Cerebro/Foruns/v4/diretrizes/v4_curadoria_tese_v1.json
```

Novo teste adicionado:

```text
test_espelho_diretrizes_reconciliado_com_fonte_viva
```

Esse teste falha se o espelho exportado estiver diferente da fonte viva ou se:

```text
- o fluxo espelhado nao comecar com curadoria_dry_run;
- produzir_dry_run nao ler curadoria;
- agente curador nao existir;
- produtor/imagem nao lerem curadoria.
```

Validacao:

```text
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
Resultado: OK 47 contract tests
```

Manifesto criado:

```text
Cerebro/Foruns/v4/diretrizes/MANIFESTO_RECONCILIACAO_ESPELHO_V4_20260709.md
```

### 2026-07-09 — Fase 2 shadow implementada

Itens implementados:

```text
- curadoria agora gera consequencia_material estruturada;
- curadoria agora gera collection_request;
- quando detecta USTR sem fonte primaria USTR/Federal Register, emite collection_request recommended antes de redator_real_llm;
- advogado do obvio usa ancoras concretas alem de sobreposicao lexical;
- contrato novo: diretrizes/v4_redator_shadow_v1.json;
- modulo novo: v4_diretrizes/redator_shadow.py;
- CLI novo: v4_diretrizes/redator_shadow_cli.py;
- redator shadow gera prompt e texto local sem chamada externa;
- redator shadow marca route_context=v4_super_luxo_redacao;
- redator shadow grava gates: allow_wordpress_real=false, allow_external_llm_call=false.
```

Artefatos gerados:

```text
v4_data/curadoria/v4_real_001.curadoria.json
v4_data/producao_shadow/v4_real_001.shadow_redacao.json
Cerebro/Foruns/v4/diretrizes/v4_real_001.shadow_redacao.json
```

Resultado do caso 261439:

```text
curadoria_id: cur_63d2d34a351a7e9c
collection_request.status: recommended
collection_request.required_before: redator_real_llm
shadow_status: shadow_redacao_pronta
external_call: false
route_context: v4_super_luxo_redacao
```

Testes novos:

```text
test_curadoria_tem_consequencia_material_e_collection_request
test_redator_shadow_gera_prompt_sem_chamada_externa
```

Validacao:

```text
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
Resultado: OK 49 contract tests
```

Limite mantido:

```text
Fase 2 ainda e shadow/dry-run. Nenhum WordPress real. Nenhuma chamada LLM real. O collection_request recomenda buscar USTR/Federal Register antes de redator real no caso 261439.
```

### 2026-07-09 — Ajustes finos antes de auditoria Fase 2

Revisao interna apontou quatro riscos antes de enviar aos auditores:

```text
1. curadoria publicada podia ser confundida com pacote antigo;
2. semantica de collection_request.status=recommended estava ambigua;
3. texto_shadow tinha meta-linguagem de placeholder;
4. fato travado sobre USTR herdava fonte_ref ambiguo.
```

Correcoes aplicadas:

```text
- criado alias espelhado v4_real_001_curadoria.json alem de v4_real_001.curadoria.json; depois, na limpeza de 2026-07-09, aliases duplicados foram movidos para legacy;
- collection_request agora declara semantica: recommended nao bloqueia shadow, mas bloqueia no estagio required_before e posteriores;
- V4ShadowRedator.collection_blocks_stage implementa essa regra;
- texto_shadow removeu "segundo a curadoria" e "promessa editorial";
- fatos_travados passam a preservar a fonte ativa por frase;
- "A reportagem registra..." agora vira "A Associated Press registra..." quando a fonte ativa e AP;
- validacao trata dict vazio {} como campo ausente.
```

Testes adicionados:

```text
test_curadoria_dict_vazio_em_required_bloqueia
test_curadoria_fatos_travados_preservam_atribuicao
test_collection_recommended_bloqueia_no_estagio_indicado
```

Validacao:

```text
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
Resultado: OK 52 contract tests
```

Checagem do pacote 261439:

```text
curadoria top fields: consequencia_material, collection_request, fatos_travados presentes
fato travado USTR: "A Associated Press registra que Flavio enviou documento ao USTR..."
fonte_ref: AP
texto_shadow meta_leak: false
```

## Fase 2 — shadow/dry-run autorizada

Autorizacao do Miguel:

```text
ok, vamos para fase 2, depois a gente pede mais auditorias
```

Escopo aprovado agora:

```text
- preparar redator shadow/super_luxo;
- manter tudo em dry-run/shadow;
- sem WordPress real;
- sem publicacao real;
- sem institucionalizar antes de novos A/B e julgamento cego;
- manter auditorias posteriores como gate.
```

Prioridades tecnicas da Fase 2:

```text
1. collection_request quando a curadoria depender de documento/fato primario ausente;
2. consequencia material explicita: quem ganha, quem perde, custo/setor/instituicao/documento;
3. advogado do obvio menos lexical e mais adversarial;
4. redator shadow/super_luxo lendo curadoria, fatos_travados e casos editoriais;
5. nenhuma saida shadow pode ir ao publicador real.
```

### 2026-07-09 — Pacotes intermediarios de auditoria externa

Problema detectado:

```text
auditoria externa viu um /mnt/project desatualizado, ainda com 45 testes, curadoria antiga, meta-linguagem no redator shadow e fato USTR ambiguo.
```

Estado local verificado:

```text
grep -c "def test_" v4_diretrizes_test_contracts.py => 52
grep "segundo a curadoria|promessa editorial" *.py *.json => vazio
grep "Associated Press registra" v4_real_001*.json => encontrado nos arquivos atuais
```

Acao historica tomada:

```text
criado pacote limpo Cerebro/Foruns/legacy/organizacao_v4_20260709/diretrizes_sync_fase2_20260709/
criado CHECKLIST_PRE_AUDITORIA_FASE2_20260709.md
criados aliases com ponto e underscore para curadoria, shadow e variantes A/B
criado pacote compactado Cerebro/Foruns/legacy/organizacao_v4_20260709/diretrizes_sync_fase2_20260709.tar.gz
```

Regra atual para proximas auditorias apos organizacao:

```text
nao auditar diretrizes_sync_fase2_20260709; ele ficou em legacy.
usar somente Cerebro/Foruns/v4/pacotes/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

### 2026-07-09 — Pacote standalone executavel

Achado da pre-auditoria:

```text
o pacote leve permitia ler e comparar os artefatos, mas nao permitia executar a suite de 52 testes porque nao continha o package Python completo nem a config LLM usada pelo model_router.
```

Correcao:

```text
criado pacote standalone descompactado, depois movido para legacy para evitar confusao;
criado compactado ativo em Cerebro/Foruns/v4/pacotes/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
incluidos diretrizes/, v4_diretrizes/, v4_data/, Cerebro/Foruns/v4/diretrizes/ e Projeto Cafezinho Agentes/root/config/
adicionada AUDITOR_NOTE_FASE2_20260709.md
```

Comando executado dentro do pacote standalone:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado:

```text
OK 52 contract tests
```

Ajuste adicional:

```text
texto_shadow deixou de usar frase com concordancia ruim ("ganha/fica exposto") e agora usa formula neutra:
"Esse deslocamento favorece X. Ao mesmo tempo, expoe Y ao custo..."
```

Regra de entrega aos auditores:

```text
- para leitura: Cerebro/Foruns/v4/diretrizes/
- para reproduzir testes: Cerebro/Foruns/v4/pacotes/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
- redator_real_llm segue bloqueado no 261439 por collection_request USTR/Federal Register
- publicacao real segue bloqueada
```
