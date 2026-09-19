# Fórum — Reunião de trabalho e novo contrato do Cafezinho/V4

**Data:** 9 de agosto de 2026  
**Estado:** reunião e auditoria em andamento; nenhuma decisão desta ata ativa mudanças por si só  
**Convocação:** Miguel do Rosário  
**Escopo:** O Cafezinho e seu pipeline editorial V4

## 1. Objetivo da reunião

Renovar o contrato de trabalho do Cafezinho, restaurar uma fronteira inequívoca entre V4 e legado, verificar a saúde operacional do pipeline em Nova York e definir a arquitetura de revisão, publicação, espelhamento e failover.

Nesta primeira reunião, o trabalho é diagnóstico e contratual. Mudanças adicionais de cron, publicação, failover ou autoridade editorial exigem deliberação posterior.

## 2. Mapa dos produtos

- **O Cafezinho (`ocafezinho.com`)**: produto editorial canônico, principal e público.
- **Rio Carta**: subsidiário ativo, com contrato editorial e infraestrutura próprios.
- **Global South News**: subsidiário ativo, com contrato editorial, idioma e infraestrutura próprios.
- **Demais sites temáticos**: ativos internos ainda não divulgados; não devem ser expostos em inventários ou telemetria públicos.

Produtos e aplicativos fora da produção editorial do `ocafezinho.com` não integram esta reunião e serão tratados em suas frentes próprias.

## 3. Definição do V4

O V4 não é um modelo isolado. É o pipeline autônomo de produção de notícias do Cafezinho, composto por:

1. coletores;
2. intake e bancos de conteúdo;
3. pesquisa e curadoria;
4. redator;
5. bancos e seleção de mídia;
6. revisão e checagem internas da redação;
7. gates editoriais e técnicos do rascunho;
8. publicador de rascunho no WordPress;
9. observabilidade, memória, autolimpeza e rollback.

**Fronteira de missão:** o V4 conclui seu ciclo ao entregar no WordPress um rascunho bem escrito, pesquisado, ilustrado e tecnicamente válido. Revisão tripla, correção editorial posterior, aprovação e publicação pública formam um fluxo externo ao V4.

O V4 deve possuir código, configurações, filas, bancos, logs, contratos e identidades próprias. Integrações compartilhadas só podem ocorrer por adaptadores V4 versionados.

## 4. Incidente que motivou a reunião

Foi confirmado em 9 de agosto que o worker de produção V4 chamava `/root/agente_controlado.py`, componente legacy, para redigir e criar drafts. Isso contornava partes do núcleo `v4_labs`, inclusive roteamento, recibos e contratos do V4.

Durante o diagnóstico, a referência foi removida do worker ativo de Nova York e substituída por `codigo.v4_vertical_redactor_runtime`, ligado ao `V4LLMAdapter` e ao `V4ModelRouter`. O roteador genérico alterado indevidamente durante a investigação foi restaurado byte a byte ao backup anterior.

**Princípio proposto:** nenhum componente V4 pode importar, executar, ler fila ou depender silenciosamente de componente legacy. Legacy permanece desligado e somente para consulta histórica ou rollback documental.

## 5. Topologia verificada nesta reunião

### Nova York

- Host operacional: `198.199.121.136` (`Cafezinho-failover-vigia`).
- É hoje o único writer autônomo identificado do V4 para o Cafezinho.
- Nacional roda aos minutos 20 e 50 de cada hora.
- Geopolítica roda aos minutos 00 e 30.
- Ciência roda aos minutos 10 e 40.
- Regional possui intake horário e worker em seis janelas diárias, via `/etc/cron.d/v4_regional`.
- Mídia possui promotor mecânico a cada seis horas e expansor diário.

### Espelho local

- O núcleo `v4_labs/codigo`, `config` e `contratos` apresenta sete divergências conhecidas em relação a Nova York.
- O worker principal local está desatualizado em relação a Nova York.
- Os três arquivos operacionais do Regional (`v4_regional_draft_worker.py`, `v4_regional_intake.py` e `v4_regional_db_archiver.py`) estão ausentes do espelho local de topo.
- Portanto, o local **não é atualmente um espelho íntegro**.

### Tencent

- Host verificado: `43.156.151.165` (`VM-0-6-ubuntu`).
- Não possui `v4_labs`, worker V4, cron V4 ou publicador V4 ativo.
- Possui apenas código antigo, inclusive `/root/agente_controlado.py` datado de junho, e um painel editorial.
- Portanto, Tencent **não é atualmente failover nem espelho operacional do V4**.

## 6. Saúde operacional preliminar

| Componente | Estado | Evidência/observação |
|---|---|---|
| Cron Nacional | Operante | draft `264918` confirmado autonomamente às 09:50 UTC |
| Cron Geopolítica | Operante com degradação de mídia | draft `264902` confirmado; passou antes por `image_pending` e reparo |
| Cron Ciência | Coleta operante, redação sem draft recente | último draft confirmado observado: `264852`, 8/8 23:10 UTC |
| V4 Regional intake | Operante | cinco bancos atualizados às 09:17 UTC |
| V4 Regional worker | Operante em baixa frequência | último draft regional confirmado observado: `264828`, Acre, 8/8 19:05 UTC |
| Integridade SQLite das verticais | Saudável | `PRAGMA quick_check=ok` em nacional, geopolítica, ciência e cinco bancos regionais |
| Banco de mídia Ouro | Operante com degradação | atualizado em 9/8; cerca de 52,6 MB; Kimi visual retorna limite de uso e o fallback Qwen-VL segue operante |
| Promotor/expansor de mídia | Ponte paralela | executaram hoje, mas alimentam o acervo S9 legado, não diretamente o Banco Ouro canônico usado pelo worker |
| Índice histórico de mídia | Atenção | aproximadamente 1,29 GB; última modificação observada em 19/7; auditoria de integridade/uso ainda pendente |
| Autolimpeza dos oito bancos | Saudável | execução diária 07:35 UTC; nacional, geopolítica, ciência e cinco bancos regionais passaram 8/8, sem erros e com `integrity_check=ok`; 23 manifestos e 26 MB arquivados |
| Rota de redação V4 | Saudável no health check | classe externa `v4_super_luxo_redacao`, três candidatos válidos, sem modelo no Python |
| Busca web do redator | Operante | smoke real Gemini grounded; evento passado corretamente tratado como passado no teste completo |
| Entrega de rascunho V4 | Operante | a missão canônica termina em `draft`; o Nacional comprovou o ciclo completo no post `264918` |
| Revisão tripla externa | Fora do perímetro V4 | ocorre depois da entrega, coordenada pelo Claude com DeepSeek e GPT como assessores |
| Publicação pública | Fora do perímetro V4 | aprovação e mudança posterior de estado não são responsabilidade do pipeline V4 |
| Espelho local | Divergente | núcleo com 7 diffs; worker e Regional fora de paridade |
| Espelho Tencent | Ausente | nenhum runtime V4 operacional encontrado |

## 7. V4 Regional

O V4 Regional é a quarta vertical canônica e a mais recente. Seu objetivo é cobrir:

- política estadual e municipal;
- calendário eleitoral em cada estado;
- pesquisas para governador e Senado;
- candidaturas, alianças, partidos e fatos eleitorais estaduais;
- notícias políticas relevantes dos estados e municípios brasileiros.

A arquitetura atual possui cinco bancos por macrorregião e seleção por UF. O worker Regional reutiliza o worker central.

**Divergência encontrada durante a auditoria:** o briefing usava `section=regional`, mas o mapa editorial V4 não definia alias/editoria nobre `v4_regional`. No novo runtime, isso poderia cair no fallback `v4_repetidor`. A coleta era regional, mas o contrato editorial de redação ainda não estava formalmente tipado como Regional Super Luxo.

**Correção deliberada durante a reunião:** criado o contrato `v4_regional_v1.md`, registrada a editoria nobre `v4_regional` e adicionado o alias `regional → v4_regional`. Validação em Nova York: contexto `v4_super_luxo_redacao`, três candidatos válidos e health check sem issues. Essa correção elimina a queda em `v4_repetidor`, mas não encerra a dívida de independência: o worker Regional ainda importa e reutiliza o worker central.

## 7.1 Linha do tempo do desvio legacy

- O backup mais antigo preservado do worker, de **19/07/2026 22:48 UTC**, já contém `AGENT = "/root/agente_controlado.py"`.
- O fórum de ativação registra a implantação do worker em 19/7.
- Todos os 20 backups examinados, de 19 a 26/7, preservam a mesma chamada legacy.
- Registros posteriores descrevem explicitamente `agente_controlado.py` como “redator subprocesso do V4” e chegam a tratar sua migração para o coração do V4 como sprint futuro.
- Conclusão: não foi regressão recente. O desenho híbrido existiu **desde a ativação produtiva das verticais em 19/7 até 9/8**, cerca de três semanas.

O desvio não significa que todo o V4 fosse legacy. Coleta, intake, bancos, fila, gates de mídia e confirmação de draft eram V4. A fronteira violada era crítica: redação, revisão e criação inicial do post atravessavam o agente antigo.

## 8. Minuta do novo contrato de trabalho

### 8.1 Todo post nasce rascunho

Todo post V4 deve nascer obrigatoriamente como `draft`. Coletor, redator, gate interno, reparador e agente de imagem do V4 não podem criar diretamente `publish` ou `future`.

Máquina de estados do V4:

`intake → pesquisado → curado → redigido → gates_do_rascunho → draft_wp → missão_v4_concluída`

Fluxo editorial externo posterior:

`draft_wp → revisão_tripla_externa → correção_editorial → aprovação → publicação`

Exceções explícitas: `quarentena_factual`, `quarentena_editorial`, `bloqueado_fonte`, `bloqueado_temporal`, `erro_técnico` e `rejeitado_editor`.

### 8.2 Revisão tripla externa

Depois que o V4 entrega o rascunho e conclui sua missão, Claude coordena externamente a revisão tripla, usando DeepSeek e GPT como assessores, com acesso de busca web/app homologado. Esse processo não integra o runtime nem a máquina de estados do V4.

Proposta de funcionamento:

- os três recebem o mesmo snapshot do draft e do pacote de evidências;
- cada parecer informa `aprovar`, `corrigir` ou `bloquear`, com achados, severidade, evidências e patch proposto;
- revisores não escrevem diretamente no WordPress;
- um executor separado aplica as correções;
- qualquer mudança em título, corpo, fonte, mídia, legenda, categoria ou data invalida as aprovações anteriores;
- a versão corrigida volta aos três revisores;
- timeout, busca indisponível, resposta vazia ou parse inválido não contam como aprovação.

**Arquitetura esclarecida por Miguel:** Claude é o coordenador da revisão externa e consulta DeepSeek e GPT como assessores para produzir a correção conjunta.

### 8.3 Pesquisa e evidência

Pesquisa precede redação. Fatos atuais, datas, cargos, números, eleições e eventos recorrentes exigem web/app search. O resultado deve formar um `evidence_bundle` versionado, com URLs finais, fontes primárias quando disponíveis, data/hora e fatos travados.

Tese é campo interno de curadoria e nunca pode virar automaticamente título.

### 8.4 Gates externos pré-publicação

Os gates externos rodam depois da última alteração editorial e imediatamente antes da publicação. São `fail-closed` e não pertencem ao V4.

Mínimos propostos:

- título com um único fato central, sem truncamento ou reticências;
- temporalidade e cargos;
- fatos contra o pacote de evidências;
- política central de fontes;
- links e HTML;
- negrito e ritmo de parágrafos;
- imagem, crédito, licença e antirreuso;
- categoria, autor, idioma e SEO;
- três pareceres válidos para o hash exato da versão;
- integridade do ledger.

### 8.5 Publicador externo e autoridade

O V4 não possui autoridade para mudar `draft→publish` ou `draft→future`. Essa transição pertence ao fluxo editorial externo e deve carregar hashes do título, corpo, mídia, evidências e pareceres.

Vigílias e reparadores trabalham em leitura e proposta. Correção pós-publicação exige snapshot, pareceres, executor separado e novos gates. Despublicação emergencial permanece autoridade humana autorizada.

### 8.6 Modelos dinâmicos

Python solicita uma classe/tier, como `super_luxo`; não contém nome de modelo. Provedores, modelos, ordem, capacidades de busca, saúde e fallback vivem em configuração externa versionada. Fallback fora da rota é proibido.

### 8.7 Espelhos e failover

- NYC é produção e writer único.
- Local e Tencent devem receber espelhos por manifesto e SHA-256.
- Segredos vêm de cofres próprios de cada ambiente e não são copiados em arquivos comuns.
- Failover exige promoção explícita, teste de paridade e fencing que desative NYC antes de Tencent escrever.
- Dois publicadores ativos simultaneamente são proibidos.

## 9. Questões abertas para a próxima rodada

1. Quem aplica a correção consolidada no fluxo externo?
2. Quem concede a autorização final de publicação: Miguel, editor delegado ou regra externa automática?
3. Qual mecanismo de web/app search é homologado para cada assessor externo e qual é o fallback quando a busca cai?
4. Quais dados podem ser espelhados integralmente em local/Tencent e quais exigem sanitização?
5. O limite final de título continua 80 caracteres, com ideal de 55–75?
6. O corpo terá zero negrito automático ou um teto pequeno de destaques editoriais?
7. Qual política será aplicada ao índice histórico de mídia?

## 10. Próximos testes propostos, ainda não autorizados por esta ata

1. Criar contrato/editoria `v4_regional` e fixture eleitoral por UF.
2. Reconciliar NYC→local por manifesto, sem `--delete` automático.
3. Montar Tencent shadow sem credenciais de publicação.
4. Testar externamente a revisão tripla e reproduzir os incidentes de 9/8, sem acoplá-la ao V4.
5. Testar mutação pós-aprovação invalidando os três pareceres.
6. Testar indisponibilidade de cada revisor e de cada mecanismo de busca.
7. Promover somente após canário e janela de observação de 24–48 horas.

## 11. Registro de participantes e contribuições

- **Miguel do Rosário:** convocação, definição do Cafezinho canônico, definição do V4 como pipeline, exigência de drafts, revisão tripla e topologia NYC/local/Tencent; esclarecimento do escopo Regional.
- **Codex:** inspeção de NYC, Tencent e espelho local; diagnóstico do desvio legacy; matriz preliminar de saúde.
- **Pascal:** auditoria operacional de roteamento e componentes V4 em Nova York.
- **Volta:** minuta contratual, segregação de funções, gates e questões para deliberação.

## 12. Plano de correção das degradações do V4

### 12.1 Limites da intervenção

O plano cobre somente o ciclo canônico do V4, encerrado na entrega de um rascunho bem escrito no WordPress. Revisão tripla e publicação pública permanecem externas. Nova York continua writer único durante toda a correção; local e Tencent não recebem autoridade de escrita.

### 12.2 Fase 0 — linha de base e proteção

1. Congelar um manifesto SHA-256 do código, contratos, configuração e cron ativos em Nova York.
2. Registrar por vertical o funil `coletado → elegível → selecionado → redigido → imagem_aprovada → draft_wp`.
3. Criar um canário controlado para Nacional, Geopolítica, Ciência e Regional, sem aumentar frequência de publicação.
4. Proibir por teste automatizado importação, subprocesso ou fallback para `agente_controlado.py` e outros componentes legacy.

**Aceite:** linha de base reproduzível, quatro recibos de canário e nenhuma referência executável a legacy.

### 12.3 Fase 1 — mídia, gargalo prioritário

Problemas confirmados:

- Kimi visual retorna HTTP 403 por limite de uso;
- Qwen-VL mantém o serviço, mas a operação está degradada;
- falhas `cota_ia_bloco_30pct_estourada` e `vertical_sem_ia` bloqueiam Geopolítica e Regional;
- promotor e expansor alimentam o acervo S9 paralelo, enquanto o worker consome o Banco Ouro V3;
- seleção depende sincronicamente do painel de mídia em Tencent;
- índice histórico de aproximadamente 1,29 GB ainda não teve integridade e utilidade verificadas.

Correção proposta:

1. Tratar Kimi como indisponível no health state até a cota voltar, sem repetir chamadas 403 em cada imagem.
2. Formalizar Qwen-VL como fallback saudável por configuração externa, com circuit breaker, recibo e métrica de qualidade.
3. Corrigir o cadastro de capacidades por vertical para que `regional` tenha rota visual válida; eliminar `vertical_sem_ia` por configuração, não por condição hardcoded.
4. Separar cota de geração de imagem da análise/seleção visual. A cota de 30% não pode bloquear o uso de fotografia válida já existente.
5. Fazer promotor e expansor escreverem por um adaptador canônico no Banco Ouro V3, com idempotência e deduplicação. S9 fica somente como fonte de migração até ser aposentado.
6. Introduzir cache local de metadados e bytes aprovados para que uma indisponibilidade curta do painel Tencent não paralise o draft.
7. Rodar `quick_check`, inventário, duplicidade, licenças e órfãos no índice histórico antes de decidir migração ou arquivamento.

**Aceite:** três ciclos consecutivos de Geopolítica e Regional sem `vertical_sem_ia`, sem bloqueio indevido pela cota de geração e com imagem/legenda/crédito anexados ao rascunho.

### 12.4 Fase 2 — estoque do V4 Ciência

Problema confirmado: coleta e cron estão vivos, mas não há candidatos novos elegíveis para redação.

Correção proposta:

1. Medir perdas por estágio e motivo: duplicidade, idade, fonte, escopo, qualidade, ausência de mídia ou gate factual.
2. Auditar as fontes científicas atuais e sua última coleta bem-sucedida; reparar fonte quebrada antes de ampliar o universo.
3. Revisar janela de frescor e limiares somente com amostra dos itens rejeitados, para não trocar falta de estoque por baixa qualidade.
4. Adicionar fontes primárias e institucionais de ciência, tecnologia e IA, preservando o contrato de linguagem acessível.
5. Criar alerta de estoque mínimo antes de chegar a zero.

**Aceite:** estoque elegível sustentado, ao menos um canário científico aprovado pelos gates internos e nenhum relaxamento global de qualidade.

### 12.5 Fase 3 — autonomia do V4 Regional

Problemas confirmados: o contrato editorial Regional foi corrigido, mas o worker ainda reutiliza o worker central e a mídia falha com frequência.

Correção proposta:

1. Manter o núcleo compartilhado como biblioteca V4, mas dar ao Regional entrypoint, configuração, locks, recibos, métricas e filas próprios.
2. Validar os cinco bancos por macrorregião e a seleção por UF, impedindo concentração automática nos estados com maior volume.
3. Aplicar o contrato `v4_regional_v1.md` em fixtures de política estadual, municipal, pesquisas para governador e Senado.
4. Integrar a rota visual Regional corrigida na Fase 1.
5. Testar deduplicação entre Regional e Nacional para evitar dois rascunhos sobre o mesmo fato.

**Aceite:** canários de pelo menos três macrorregiões, recibos `v4_regional`, nenhuma queda em `v4_repetidor` e nenhuma colisão com Nacional.

### 12.6 Fase 4 — espelhos e failover

Problemas confirmados: o espelho local diverge; Tencent não possui runtime V4 e não é failover.

Correção proposta:

1. Definir manifesto canônico de código/configuração/contratos e uma política separada para bancos, mídia, logs e segredos.
2. Reconciliar primeiro NYC → local sem `--delete`, revisar as divergências e validar hashes/testes.
3. Instalar o mesmo artefato em Tencent no modo shadow, sem credenciais nem cron de escrita no WordPress.
4. Executar coletores e workers shadow com saída em banco/WordPress simulado e comparar recibos com Nova York.
5. Só desenhar promoção de failover após paridade; exigir fencing que desative o writer de Nova York antes de ativar Tencent.

**Aceite:** local com hashes canônicos; Tencent produz recibos shadow equivalentes; teste de failover documentado sem dois writers simultâneos.

### 12.7 Observabilidade e encerramento

Painel mínimo por vertical:

- último ciclo e duração;
- idade e quantidade do estoque elegível;
- drafts entregues e motivos de não entrega;
- provedor/modelo/capacidade escolhidos pelo roteador dinâmico;
- taxa de fallback e erro dos LLMs;
- cobertura de imagem, reutilização, licença e falhas por motivo;
- integridade e crescimento dos bancos;
- divergência dos espelhos.

O incidente só pode ser encerrado quando Nacional, Geopolítica, Ciência e Regional completarem três ciclos esperados consecutivos dentro de seus próprios horários, com recibos válidos, sem dependência legacy e sem erro crítico de mídia.

## 13. Estratégia editorial do Banco de Mídia V4

### 13.1 Diagnóstico quantitativo de 9/8

O Banco Ouro V3 possui 767 mídias, 103 entidades distintas e somente 252 itens liberados para uso automático. A cobertura está concentrada em política nacional: 402 itens de política e 156 de Congresso, contra 79 de geopolítica e apenas um classificado como tecnologia.

Cobertura textual encontrada no acervo:

| Núcleo | Total encontrado | Uso automático |
|---|---:|---:|
| Estreito de Hormuz/Ormuz | 3 | 1 |
| Irã | 31 | 7 |
| China | 18 | 1 |
| Mapas | 1 | 0 |
| Ciência/tecnologia | 13 | 7 |

Há ainda 716 itens esperando catalogação humana e 35.340 rejeições. Destas, 21.390 têm como motivo `gemini_vision_erro`: indisponibilidade técnica foi gravada como rejeição editorial, destruindo capacidade útil e impedindo retentativa adequada.

### 13.2 Princípio do acervo antecipado

O Banco de Mídia V4 deve manter cobertura antes de a notícia chegar. A seleção em tempo de redação consulta um acervo editorial previamente licenciado, catalogado e aprovado. Busca emergencial continua existindo, mas serve para fatos novos, não para entidades e lugares recorrentes.

O banco terá cinco famílias canônicas:

1. **pessoas:** chefes de Estado, ministros, parlamentares, cientistas e candidatos;
2. **lugares:** países, estados, cidades, estreitos, portos, bases, usinas, laboratórios e universidades;
3. **instituições e objetos:** partidos, tribunais, Forças Armadas, empresas, satélites, chips, telescópios e equipamentos;
4. **mapas, diagramas e infográficos:** produzidos de forma determinística com dados geográficos citados, nunca por IA generativa sem controle cartográfico;
5. **eventos:** fotografias específicas de reuniões, campanhas, conflitos, lançamentos e descobertas.

### 13.3 Geopolítica

Criar dossiês permanentes por país, ator e ponto estratégico. A primeira carga prioritária será:

- Estreito de Hormuz: mapas de localização e rotas, imagens de satélite, petroleiros, costa iraniana e omanense, portos e ilhas estratégicas;
- Irã: lideranças, Parlamento, governo, Forças Armadas, Teerã, instalações energéticas e nucleares, infraestrutura e população;
- China: lideranças, Pequim, instituições, indústria, portos, semicondutores, ciência, Forças Armadas e infraestrutura;
- demais países e corredores que aparecem continuamente na pauta.

Cada dossiê deve misturar retratos, fotografia contextual, paisagens, infraestrutura e mapas. Uma matéria sobre Hormuz não pode depender sempre da mesma fotografia de petroleiro.

### 13.4 Ciência, tecnologia e IA

A ordem de preferência será:

1. fotografia real da pesquisa, laboratório, pesquisador, instituição ou equipamento;
2. imagem científica primária: microscopia, telescópio, satélite, gráfico ou visualização produzida pela pesquisa;
3. diagrama ou infográfico editorial verificável;
4. ilustração artificial, quando não houver imagem real relevante e licenciada.

Imagem artificial é permitida em Ciência, mas deve ser identificada como ilustração, registrar gerador/modelo/prompt/data e nunca se apresentar como fotografia documental de pessoa ou acontecimento real. Mapas e gráficos factuais devem vir de dados e templates determinísticos, não de geração livre.

O acervo será organizado por núcleos recorrentes: espaço, clima, energia, saúde, biologia, física, computação quântica, semicondutores, robótica, IA, universidades e indústria científica.

### 13.5 Regional e eleições de 2026

Criar um cadastro eleitoral canônico alimentado por fonte oficial, com:

- pessoa e aliases;
- UF e município quando aplicável;
- cargo disputado;
- partido, federação ou coligação;
- situação precisa: nome cogitado, pré-candidatura, candidatura registrada, deferida, indeferida, substituída ou retirada;
- identificador oficial, período de validade e data da última confirmação.

O banco deve cobrir todos os candidatos a governador e ao Senado das 27 unidades da Federação. Para cada pessoa, a meta inicial é duas imagens utilizáveis e a meta editorial é quatro ou mais: retrato identificável, atividade pública/campanha, fotografia contextual e alternativa horizontal para destaque.

Identidade de candidato exige confirmação por metadados oficiais ou revisão humana. Visão computacional auxilia catalogação, mas não pode sozinha identificar uma pessoa nem liberar automaticamente uma fotografia eleitoral.

### 13.6 Modelo de dados e busca

O campo único `entidade` não é suficiente. Preservando compatibilidade com `midia_ouro`, o banco ganhará tabelas normalizadas para:

- entidades e aliases;
- relação muitos-para-muitos entre mídia e entidades;
- lugares e coordenadas;
- eleições, cargos e candidaturas com validade temporal;
- taxonomia temática e tipo visual;
- direitos, licença, fonte e restrições de uso;
- histórico de uso e desempenho editorial.

A busca ranqueia entidade, lugar, tema, tipo visual, data, direitos, formato, qualidade e histórico de reutilização. O título não será mais a única fonte de entidades: título, tese, pacote de evidências e metadados estruturados alimentarão a consulta.

### 13.7 Aquisição, direitos e catalogação

Ordem de aquisição:

1. fontes oficiais com termos de reutilização verificáveis;
2. Wikimedia Commons e repositórios institucionais com licença explícita;
3. agências e acervos contratados pelo Cafezinho;
4. produção própria, mapas e infográficos editoriais;
5. geração artificial permitida pelo contrato da vertical.

Crédito, licença e URL de origem são obrigatórios. Imagem encontrada na internet sem direito comprovado pode ser referência de busca, mas não entra em `uso_automatico`.

Erros de rede, timeout ou falha de provedor visual passam para `erro_tecnico_retry`, nunca para `rejeicoes_ouro`. Rejeição editorial fica reservada a inadequação real. A fila existente de erros Gemini deve ser reclassificada e reprocessada pelo tribunal visual saudável.

### 13.8 Rotação e cobertura mínima

O ledger impedirá repetição próxima da mesma imagem e favorecerá diversidade de enquadramento. Exceções serão permitidas para fotografia exclusiva do fato, com justificativa no recibo.

Um painel de lacunas mostrará, por vertical e entidade:

- quantidade total e quantidade liberada;
- tipos visuais disponíveis;
- orientação e resolução;
- idade da mídia;
- direitos e revisão pendentes;
- data do último uso;
- demanda recente sem cobertura.

As lacunas alimentam automaticamente a fila de aquisição. A prioridade é determinada por frequência editorial, calendário eleitoral, atualidade e quantidade de alternativas já disponíveis.

## 14. Decisão editorial — fontes públicas no corpo

**Decisão de Miguel do Rosário em 9 de agosto de 2026:** pesquisa multifonte é uma etapa interna de apuração e checagem. Quando duas ou mais fontes independentes confirmarem um fato corrente, o Cafezinho o apresenta como informação pública verificada, com voz própria, sem escrever “Segundo A, B e C”, sem enumerar veículos e sem publicar uma coleção de links.

Atribuição nominal e link no corpo ficam reservados a material cuja autoria jornalística seja relevante para o próprio fato: furo ou informação exclusiva, coluna assinada, entrevista, documento obtido por uma redação, reportagem investigativa original ou dado proprietário. Institutos, órgãos e autores de declarações continuam identificados quando isso for necessário à compreensão, mas a checagem complementar não vira bibliografia pública.

Essa regra vale igualmente para:

- redator e acabamento do V4 Nacional, Geopolítica, Ciência e Regional;
- busca web nativa e pesquisa complementar;
- revisão tripla externa coordenada pelo Claude;
- correção, enriquecimento e publicação posteriores ao rascunho.

O recibo interno conserva as fontes consultadas para auditoria. A revisão externa não pode reintroduzir listas de veículos, links de corroboração ou chamadas artificiais de fonte que o V4 removeu.

## 15. Diagnóstico e proposta de ciclo de vida dos bancos

### 15.1 Estado encontrado em 9 de agosto de 2026

Existe autolimpeza diária às 07:35 UTC. Antes de remover linhas terminais do SQLite quente, o agente gera arquivos `jsonl.zst`, manifesto, checksums, teste de restauração, recibo e tombstone. A política atual, porém, mantém indefinidamente os estados `new`, `processing`, `drafted` e `image_pending`; portanto ela controla parte do crescimento, mas não completa o ciclo de vida editorial.

Os arquivos frios estavam apenas no disco de Nova York. Os crons gerais de Backblaze estavam desativados no nó de produção e o caminho V4 não aparecia no B2. Logo, havia arquivo local verificável, mas ainda não backup externo do arquivo V4.

No V4 ativo, o banco de candidatos preserva principalmente material coletado e sua linhagem. O produto redigido fica no WordPress como rascunho e é ligado ao banco por `draft_events`; não existe hoje um “banco auditado” V4 independente equivalente aos bancos antigos do V3. Bancos V3 com esse nome são legado e não devem voltar à rota operacional.

### 15.2 Política proposta — quente, morno e frio

1. **Quente:** somente pautas dentro da janela de frescor e rascunhos dentro do SLA de revisão.
2. **Morno:** material vencido que ainda pode servir a dossiê, contexto, cronologia, perfil, eleição ou atualização futura. Não volta a ser notícia sem nova checagem temporal.
3. **Frio:** duplicatas, bloqueios editoriais, rejeições, execuções antigas e rascunhos não aproveitados. Tudo é compactado com conteúdo, fonte, mídia, modelo, prompts/recibos, decisão editorial e hashes.
4. A remoção do banco quente só ocorre depois de `archive → checksum → restore-test → cópia externa confirmada → tombstone`.
5. A cópia externa usa operação `copy` append-only, nunca `sync`, para não propagar exclusões acidentais. Destinos recomendados: Backblaze B2 e espelho Tencent.

### 15.3 Aproveitamento sem publicar material ruim

“Usar tudo” não significa publicar tudo. Material velho, duplicado, fraco ou proveniente de fonte proibida pode ser aproveitado como sinal de pauta, contexto privado, cronologia, dossiê de personagem, treinamento editorial e prevenção de repetição. Publicar notícia vencida apenas porque houve custo anterior transforma custo afundado em novo erro editorial.

Rascunhos que ultrapassarem o SLA devem seguir uma das saídas: atualizar e revalidar; decompor em contexto para outra pauta; ou arquivar integralmente. Nenhum deles deve permanecer eternamente na fila ativa nem desaparecer sem recibo.

### 15.4 Teste de atualidade — data da fonte não é data do fato

Antes de liberar qualquer rascunho, o V4 e a revisão externa devem responder:
**“o que aconteceu agora e justifica publicar isto hoje?”** A data recente do
RSS, da coluna ou da coleta não comprova atualidade do evento central.

Fonte recente que apenas reconta fato antigo deve gerar `sem_gancho_atual`, ou
ser transformada em análise/cronologia com datas explícitas e uma novidade
real. Títulos no presente ficam bloqueados quando fundem eventos ocorridos em
datas diferentes. A regra operacional completa está em
`diretrizes/regra_teste_atualidade_v4_loop_miguel_20260815.md`.

## 16. Fechamento operacional — arquitetura, visão e incidente editorial

### 16.1 Fluxo ativo confirmado

O V4 termina sua responsabilidade no rascunho: coleta e estoque temporário → banco de candidatos da vertical → seleção por frescor → briefing → roteador dinâmico de redação → rascunho no WordPress → associação de mídia → recibo em `draft_events`. A revisão tripla e a publicação são externas ao V4. Não existe um “banco auditado de textos” separado no caminho ativo; o texto produzido fica no WordPress, enquanto o SQLite preserva candidatos, estados e linhagem.

### 16.2 Roteador visual dinâmico

O trabalhador V4 deixou de carregar provedores, modelos, endpoints e chaves de visão diretamente. Agora chama um roteador visual único, orientado por contrato, com esta cascata: Kimi assinatura → Kimi API pay-as-you-go → Qwen Vision → Gemini Vision. O roteador mantém saúde persistente, identifica troca de chave por impressão digital, aplica cooldown a credenciais sem cota e retenta automaticamente quando elas voltam a funcionar.

Os quatro caminhos foram verificados: a assinatura Kimi está temporariamente sem cota; Kimi pay-as-you-go, Qwen e Gemini responderam corretamente. O espelho Tencent ainda não executa o pipeline V4 completo e, portanto, não deve ser descrito como failover operacional até receber serviço, contratos, bancos e testes equivalentes aos de Nova York.

### 16.3 Aprendizagem e Banco de Mídia

O suposto ciclo de autoaprendizagem não estava ativo. O contrato encontrado está em modo `lab_fail_closed`, a ativação por feedback está desabilitada e não há manifesto humano aprovado nem arquivo recente de feedback editorial. O trabalho anterior pode ter classificado ou gerado ativos, mas não alterou autonomamente o comportamento do V4. Qualquer retomada desse mecanismo exige métricas, amostra de validação, aprovação explícita e recibo de ativação.

O Banco Ouro é consumido em Nova York, mas seus arquivos são servidos pelo painel Tencent. O incidente mostrou que inserir apenas no índice de Nova York produz referência quebrada; promoção futura deve ser transacional nos dois lados, com verificação HTTP antes de liberar `uso_automatico`. Também foi identificada uma corrida em que um trabalhador antigo substituiu uma foto real já corrigida por uma imagem artificial. A correção foi restaurada, mas o publicador precisa de trava de versão para impedir que uma execução atrasada sobrescreva curadoria mais nova.

### 16.4 Incidente do texto sobre Mendonça

O post foi reescrito e republicado sem negritos, sem links externos e sem enumeração de veículos. Foram removidos apartes, repetições, tangentes e conclusões não sustentadas. A alegação do PL permanece apresentada como alegação, não como decisão judicial. O título e o endereço foram encurtados, a mídia existente foi preservada e o endereço anterior redireciona para o novo.
