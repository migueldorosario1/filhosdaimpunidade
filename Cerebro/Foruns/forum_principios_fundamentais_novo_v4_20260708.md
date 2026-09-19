# Forum - Principios Fundamentais do Novo Sistema V4

Aberto em: 2026-07-08 12:06:40 -03  
Origem: orientacao direta do Miguel  
Status: principio de arquitetura para guiar a codificacao

## 1. Tese Central

O novo V4 deve separar rigorosamente:

- agentes tecnicos;
- diretrizes editoriais;
- gestao de LLMs;
- bancos de dados;
- produtores/publicadores;
- memoria de bugs;
- camada de imagem destacada.

Regra principal:

> Agente nao carrega diretriz hardcoded. Agente executa. Diretriz orienta. Banco auditado alimenta. Publicador publica apenas o que passou por camadas confiaveis.

## 2. Separacao Obrigatoria

### 2.1 Agentes

Agentes produtores, coletores, revisores e publicadores devem ser tecnicos.

Eles podem:

- coletar;
- classificar;
- consultar banco;
- carregar diretriz externa;
- chamar LLM conforme roteamento;
- validar;
- registrar telemetria;
- produzir artefato.

Eles nao devem:

- embutir linha editorial;
- embutir preferencia fixa de modelo;
- conter prompt editorial longo;
- decidir regra de estilo dentro do codigo;
- publicar usando banco bruto;
- improvisar imagem destacada no final.

### 2.2 Diretrizes

Diretrizes devem ficar fora dos agentes.

Devem ser:

- externas;
- limpas;
- sem redundancia;
- versionadas;
- reutilizaveis;
- carregadas em runtime;
- organizadas por camada:
  - nucleo editorial comum;
  - estilo;
  - sintaxe;
  - titulo;
  - editoria;
  - freios por familia de LLM;
  - regras de imagem;
  - memoria de bugs promovida.

Objetivo:

> aproveitar o que ja existe, pesquisar diretrizes antigas aproveitaveis e consolidar sem duplicar.

## 3. Bancos de Dados em Camadas

Conceito fundamental:

> bancos de dados ficam de um lado; produtores ficam de outro.

O V4 deve trabalhar com camadas para evitar contaminacao.

### 3.1 Banco Inicial

Contem material bruto:

- pautas coletadas;
- fontes;
- imagens candidatas;
- metadados iniciais;
- links;
- registros ainda nao confiaveis.

Produtor final nao deve publicar direto daqui.

### 3.2 Banco Intermediario

Contem material processado:

- pautas classificadas;
- entidades extraidas;
- imagens candidatas filtradas;
- deduplicacao;
- checagens preliminares;
- contexto editorial preliminar.

Ainda precisa auditoria.

### 3.3 Banco Final / Auditado

Contem apenas material aprovado:

- pauta auditada;
- fonte validada;
- imagem aprovada;
- direitos/credito quando aplicavel;
- entidade visual confirmada;
- contexto pronto para redacao;
- historico de validacao.

Regra:

> produtores e publicadores lidam apenas com bancos finais/auditados.

## 4. Gestao Limpa de LLMs

LLMs devem ficar em camada propria, separada dos agentes e das diretrizes.

Requisitos:

- roteamento externo;
- fallback forte;
- tiers de qualidade;
- logs de qualidade;
- custo controlado;
- degradacao controlada;
- nunca prender o produtor a modelo inferior por economia cega.

O erro historico a evitar:

> trocar qualidade editorial por custo/volume e perder audiencia.

Prioridade nova:

> menos quantidade, mais confiabilidade e texto muito melhor.

## 5. Qualidade Editorial e Criatividade

O V4 atual ficou preso demais e sem criatividade. O novo sistema precisa preservar liberdade de escrita dentro de um contrato editorial claro.

Diretriz:

- nao engessar a prosa;
- nao matar criatividade com checklist excessivo;
- usar diretriz como orientacao e freio, nao como camisa de forca;
- usar melhores modelos para producao nobre;
- usar fallback barato apenas quando a pauta permitir;
- testar continuamente qual LLM escreve melhor.

Categorias de qualidade a mapear/reaproveitar:

- super luxo;
- luxo;
- padrao;
- economico;
- revisor;
- auditor;
- ensemble/assembleia de modelos quando a pauta justificar.

Pendencia:

- localizar a pesquisa de qualidade de LLM feita no Tencent;
- recuperar ratings e criterios;
- conectar isso ao roteamento externo existente.

## 6. Assembleia / Ensemble de LLMs

Quando a pauta for nobre ou sensivel, usar composicao inteligente de modelos.

Possivel fluxo:

1. melhor modelo redige;
2. segundo modelo critica pontos fracos;
3. revisor aplica freios;
4. auditor factual valida;
5. publicador recebe artefato final.

Regra:

> ensemble deve aumentar qualidade, nao multiplicar burocracia.

## 7. Banco de Midia e Imagem Destacada

O problema de imagem destacada continua critico.

Fontes a estudar e integrar:

- imagens do WordPress do Cafezinho;
- banco de midia do WordPress;
- imagens ja auditadas no R2;
- banco ouro de midia;
- Flickr;
- fontes oficiais;
- imagens auditadas manualmente;
- novas auditorias com Gemini Vision.

Hipotese nova:

> agora, com acesso direto ao servidor WordPress, pode ser possivel usar o proprio banco de imagens do WordPress como fonte auditavel ou semi-auditavel.

Tarefa:

1. estudar acesso ao banco de dados WordPress;
2. mapear anexos/imagens existentes;
3. identificar imagens ja usadas em posts bons;
4. extrair metadados, creditos, tamanhos e relacao com entidades;
5. cruzar com R2 e banco ouro;
6. promover imagens confiaveis para camada auditada.

## 8. Regra Visual Para Personagens

Para imagem destacada de pessoa publica:

> o personagem citado no titulo deve aparecer grande, claro e preferencialmente central na imagem.

Exemplos:

- se o titulo fala de Lula, Lula deve aparecer claramente;
- se fala de Flavio Bolsonaro, Flavio Bolsonaro deve aparecer claramente;
- evitar imagem em que a pessoa esteja pequena, lateral, desfocada, irreconhecivel ou substituida por simbolo generico.

Uso de Gemini Vision:

- validar se a pessoa aparece;
- validar se esta grande no centro;
- validar se a imagem e adequada ao titulo;
- rejeitar thumbnail, foto generica, montagem ruim ou IA indevida;
- se aprovado, enviar/registrar no R2.

## 9. Aproveitamento do Que Ja Existe

Nao reescrever tudo.

Pesquisar e reaproveitar:

- diretrizes antigas;
- linhas editoriais de estilo;
- regras de titulo;
- regras de sintaxe;
- `diretrizes/` atual;
- `llm_context_routes.json`;
- pesquisa de qualidade de LLM;
- bancos de midia existentes;
- imagens auditadas R2;
- memoria de bugs;
- validadores ja criados.

Meta:

> consolidar, limpar e reduzir redundancia.

## 10. Decisao de Arquitetura

O sistema pode ser hibrido:

- nucleo tecnico comum;
- diretrizes externas por editoria/camada;
- LLMs externos e roteados por qualidade;
- bancos em camadas;
- produtores consumindo apenas banco auditado;
- validadores comuns e especificos;
- memoria de bugs comum com tags;
- imagem destacada como pipeline proprio.

Esta e a base para a codificacao do novo V4.

## 11. Proximas Acoes

1. Indexar este forum no forum central do novo V4.
2. Auditar `llm_context_routes.json` e pesquisa antiga de qualidade.
3. Pesquisar diretrizes antigas aproveitaveis.
4. Mapear bancos existentes por camada.
5. Estudar banco de imagens do WordPress.
6. Criar mapa de diretrizes externas sem redundancia.
7. Criar mapa de bancos: inicial, intermediario, final/auditado.
8. Criar contrato de produtor: produtor so le banco auditado.
