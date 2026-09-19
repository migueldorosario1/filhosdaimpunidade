# Forum - Novo Sistema de Agentes V4 e Suas Diretrizes

Aberto em: 2026-07-07 22:38:33 -03  
Responsavel operacional: Codex  
Status: forum-mãe da reforma V4, aguardando execução faseada

## 1. Carta aos Agentes

Agentes da Trindade e agentes auxiliares,

Este forum consolida a orientação para o novo sistema de agentes V4 e suas diretrizes editoriais. A reforma deve produzir um sistema mais nítido, mais jornalístico e mais controlável: cada agente com função própria, cada editoria com diretriz própria, cada decisão registrada em forum, e nenhum debate estrutural perdido em chat solto ou inbox longo.

A regra principal é simples:

> O V4 deve escrever melhor porque pensa melhor, apura melhor e corta melhor. Não porque acumula prompt.

Todos devem seguir estritamente os protocolos de comunicação:

- Forum é lugar de decisão, consolidação e memória estrutural.
- Canal é mural de convocação e aviso curto.
- Inbox individual é resposta curta, objetiva e acionável.
- Inbox não é arquivo morto, não é debate longo, não é duplicação de forum.
- Manter inbox limpo, curto e com status claro.
- Se uma resposta virar decisão, ela deve ser consolidada no forum.
- Se houver divergência, registrar no forum com proposta de conciliação.
- Se houver pendência, registrar em uma lista curta com responsável e próximo passo.

Nenhum agente deve iniciar mudança operacional em prompt, pipeline, publicador, roteador ou cron sem:

1. identificar o forum de referência;
2. registrar o arquivo que será mexido;
3. preservar rollback;
4. fazer teste shadow quando houver risco editorial;
5. atualizar o forum ao final.

## 2. Fóruns e Arquivos de Referência

Forum central da rodada anterior:

```text
Cerebro/Foruns/forum_super_luxo_editorial_v4_espelhado_20260707.md
```

Forum de novas diretrizes:

```text
Cerebro/Foruns/forum_novas_diretrizes_editoriais_correio_brasil_20260707.md
```

Forum de backup/retomada:

```text
Cerebro/Foruns/forum_backup_retomada_backblaze_pre_reforma_20260707.md
```

Diretrizes já existentes:

```text
diretrizes/v4_nucleo_editorial_comum_v1.md
diretrizes/v4_politica_economia_v1.md
diretrizes/v4_cultura_v1.md
diretrizes/v4_internacional_v1.md
diretrizes/v4_repetidor_v1.md
diretrizes/v4_gsn_espelho_ingles_v1.md
diretrizes/v4_freios_llm_v1.json
```

Inbox:

```text
Cerebro/Foruns/inbox_trindade/
```

## 3. Estrutura Editorial do Novo V4

O novo V4 deve ser organizado como sistema de editorias, não como um agente único tentando resolver tudo.

Estrutura base aprovada:

1. V4 Política/Economia
2. V4 Cultura
3. V4 Internacional
4. V4 Repetidor, em modo frio
5. Espelho Global South News, como adaptação editorial em inglês

### 3.1 Núcleo Editorial Comum

Todas as editorias devem obedecer ao mesmo núcleo:

- lead direto;
- fato concreto antes de tese;
- título em Sentence Case;
- parágrafo com função própria;
- ritmo humano, sem cadência mecânica;
- tese proporcional à força da apuração;
- fonte rastreável;
- menos fórmula, menos solenidade, menos transição escolar;
- revisão que melhora texto, não que engessa;
- corte de generalidade sem sujeito, cargo, dado ou consequência material.

### 3.2 Política/Economia

Função:

- cobrir poder, Estado, economia, Congresso, governo, mercado, instituições, soberania e disputa política.

Diretriz:

- texto com malícia institucional;
- consequência material clara;
- nomes, cargos e relações de poder;
- tese forte só quando houver fonte primária, consequência clara e alinhamento editorial;
- evitar editorialização vazia quando o fato ainda pede descrição proporcional.

### 3.3 Cultura

Função:

- cobrir cultura como disputa simbólica, produção material, memória, linguagem, indústria, estética e política cultural.

Diretriz:

- texto com sensibilidade e concretude;
- evitar release, resenha automática e elogio genérico;
- situar artista, obra, público, contexto e conflito;
- preservar voz humana sem virar ornamentação.

### 3.4 Internacional

Função:

- cobrir geopolítica, Sul Global, guerras, diplomacia, multipolaridade, sanções, integração regional e disputa de narrativas globais.

Diretriz:

- contexto brasileiro e latino-americano quando relevante;
- cargos e países na primeira menção;
- cuidado com viés automático de modelo;
- não transformar análise internacional em comunicado diplomático;
- não suavizar fato duro por neutralidade falsa.

### 3.5 Repetidor em Modo Frio

Função:

- absorver pauta transacional, factual, rápida, republicação, serviço e nota curta.

Diretriz:

- não competir com as editorias nobres;
- não contaminar Política, Cultura e Internacional;
- operar com gate explícito;
- permitir veto humano para pauta morna;
- texto seco, limpo, sem ambição falsa.

### 3.6 Espelho Global South News

Função:

- adaptar editorialmente conteúdos para inglês, não traduzir mecanicamente.

Diretriz:

- título original em inglês;
- briefing separado com contexto brasileiro;
- direito de recusar pauta doméstica demais;
- primeira menção com cargo + país;
- links diluídos no começo quando fizer sentido;
- HTML restrito;
- flexibilizar parágrafos para 2 a 4 períodos, respeitando ritmo jornalístico.

## 4. Sistema de Agentes V4 a Construir

O sistema deve ser construído como pipeline de decisão editorial, roteamento e revisão, não como chamada única de LLM.

Fluxo recomendado:

1. Entrada da pauta
2. Classificador editorial
3. Roteamento para editoria V4
4. Seleção de modelo por função
5. Injeção de diretriz específica
6. Injeção de freios por família de LLM
7. Redação
8. Validação editorial objetiva
9. Revisão final ou shadow
10. Publicação controlada
11. Telemetria e registro

### 4.1 Classificador de Entrada

O classificador deve decidir:

- editoria correta;
- se a pauta é nobre ou repetidor;
- risco editorial;
- necessidade de contexto adicional;
- se a pauta deve ser recusada, segurada ou enviada para humano.

### 4.2 Roteador de Modelos

O roteador deve respeitar auto-limitações:

- Claude: freio anti-solenidade, anti-parágrafo redondo, anti-conclusão bonita.
- GPT/Codex: freio anti-fórmula, anti-transição escolar, anti-arquitetura sem prosa.
- Grok: freio anti-gracinha, anti-sarcasmo performático.
- DeepSeek: freio anti-relatório, anti-enumeração implícita, anti-cadência rígida.
- GLM/Qwen/Kimi: freio contra abstração, generalidade, perda de nuance brasileira e diplomatização.
- Nenhum modelo deve ser default universal.

### 4.3 Gates

Gates obrigatórios:

- gate de editoria;
- gate de Repetidor;
- gate de fonte;
- gate de tese forte;
- gate de GSN;
- gate de publicação;
- gate de custo/telemetria.

### 4.4 Shadow Antes de Deploy

Antes de mexer no pipeline real:

- testar com matérias reais;
- comparar texto atual versus texto novo;
- registrar resultado em forum;
- manter rollback;
- só então promover para produção.

## 5. Plano de Trabalho

### Fase 0 - Preservação

- Backup seletivo dos arquivos que serão mexidos: `diretrizes/`, fóruns centrais, inbox e agentes/pipelines afetados.
- Não retomar backup total agora, salvo decisão específica.

### Fase 1 - Inventário

- Listar agentes V4 reais.
- Listar prompts, roteadores, publicadores e crons que usam V4.
- Identificar onde `diretrizes/` deve ser injetado.

### Fase 2 - Contrato Editorial

- Revisar `v4_nucleo_editorial_comum_v1.md`.
- Revisar quatro diretrizes V4.
- Revisar `v4_gsn_espelho_ingles_v1.md`.
- Revisar `v4_freios_llm_v1.json`.

### Fase 3 - Roteamento

- Construir ou ajustar classificador.
- Separar pipeline nobre e Repetidor.
- Definir seleção de modelo por editoria e risco.

### Fase 4 - Validação

- Criar validadores objetivos:
  - título;
  - lead;
  - fonte;
  - parágrafo;
  - tese;
  - vício por família de LLM.

### Fase 5 - Shadow

- Rodar teste com pelo menos:
  - uma matéria de Política/Economia;
  - uma de Cultura;
  - uma de Internacional;
  - uma nota Repetidor;
  - uma adaptação GSN.

### Fase 6 - Deploy Gradual

- Ativar em modo controlado.
- Monitorar publicação, custo, tempo e qualidade.
- Registrar anomalias no forum.

### Fase 7 - Consolidação

- Atualizar documentação final.
- Fechar inboxes.
- Consolidar decisão no forum.
- Remover pendências falsas.

## 6. Protocolo de Comunicação

Este é o protocolo obrigatório desta reforma:

- Toda decisão estrutural deve ir para forum.
- Toda resposta individual deve ir para inbox próprio.
- Todo inbox deve ser curto, limpo e com status.
- Toda convocação deve ir para canal.
- Todo arquivo alterado deve aparecer no forum da tarefa.
- Toda divergência deve vir com proposta.
- Toda pendência deve ter dono e próximo passo.
- Nenhum agente deve transformar inbox em diário, log bruto ou debate comprido.

Modelo de inbox limpo:

```text
# Inbox Trindade - NOME

Status: respondido | pendente | aguardando teste

## Resposta curta

- decisão:
- ajuste:
- risco:
- próximo passo:

## Ponteiros

- forum:
- arquivo:
```

## 7. Decisão Operacional

A reforma V4 deve seguir esta ordem:

1. preservar arquivos-alvo;
2. revisar diretrizes;
3. mapear agentes e pipelines;
4. implementar roteamento/freios;
5. testar shadow;
6. validar em forum;
7. só então publicar.

Fim da carta.

---

## 8. Adendo 1 - Imagem Destacada, V4 Ciência/Tecnologia/IA e Diretrizes Externas

Registrado em: 2026-07-07  
Origem: orientação editorial do Miguel  
Status: enviar nova rodada à Trindade

### 8.1 Problema da Imagem Destacada

A reforma V4 não pode tratar imagem destacada como detalhe final de publicação. O problema da imagem destacada precisa entrar como componente estrutural do sistema.

Pendência:

- diagnosticar onde a imagem destacada é escolhida hoje;
- separar escolha editorial de imagem, fallback técnico e validação antes de publicar;
- impedir imagem genérica, errada, artificial indevida, repetida, quebrada ou sem relação direta com a pauta;
- registrar no post a origem da imagem quando aplicável;
- criar telemetria de falhas de imagem;
- permitir correção rápida por comentário do editor;
- integrar a memória de bugs para que erro de imagem não se repita.

Diretriz inicial:

> Nenhum V4 deve publicar como se imagem destacada fosse responsabilidade externa. A imagem é parte da edição.

### 8.2 Novo V4 Ciência, Tecnologia e IA

Adicionar uma quinta vertical nobre:

```text
V4 Ciência, Tecnologia e IA
```

Escopo:

- ciência;
- tecnologia;
- inteligência artificial;
- regulação digital;
- plataformas;
- soberania tecnológica;
- Big Tech;
- semicondutores;
- dados;
- cibersegurança;
- pesquisa pública;
- inovação industrial;
- impactos sociais e trabalhistas da automação.

Diretriz editorial:

- explicar sem didatismo escolar;
- evitar deslumbramento tecnológico;
- evitar tecnofobia automática;
- ligar tecnologia a poder, Estado, capital, trabalho, soberania e vida cotidiana;
- diferenciar paper, release, hype, produto, lobby e política pública;
- exigir fonte primária sempre que possível;
- contextualizar limitações, conflito de interesse e incerteza técnica;
- traduzir complexidade sem transformar texto em tutorial.

### 8.3 Sistema Integrado versus Verticais Independentes

A Trindade deve avaliar se o V4 deve ser um sistema integrado com estruturas compartilhadas ou um conjunto de verticais independentes.

#### Opção A - Sistema Integrado com Estruturas Compartilhadas

Descrição:

- todos os V4 compartilham núcleo técnico;
- diretrizes são externas e carregadas dinamicamente;
- classificador, telemetria, validação, memória de bugs e protocolo de publicação são comuns;
- cada editoria recebe apenas sua diretriz específica e seus gates.

Prós:

- menos duplicação;
- manutenção mais simples;
- telemetria comparável;
- memória de bugs unificada;
- custo operacional menor;
- correções de infraestrutura beneficiam todas as editorias;
- facilita roteamento e shadow test padronizado.

Contras:

- risco de acoplamento excessivo;
- bug em componente comum pode afetar todos;
- tendência a uniformizar voz se as diretrizes específicas forem fracas;
- exige arquitetura inicial mais disciplinada;
- mudanças no núcleo precisam de mais cuidado.

#### Opção B - Verticais Independentes e Autônomas

Descrição:

- cada V4 tem pipeline próprio, agentes próprios, prompt/diretriz própria e validação própria;
- pouca dependência de núcleo comum.

Prós:

- isolamento forte;
- falha em uma vertical não derruba as outras;
- cada editoria pode evoluir com máxima liberdade;
- voz editorial pode ficar mais distinta;
- experimentos são mais seguros em uma vertical específica.

Contras:

- duplicação de código e lógica;
- risco de divergência caótica;
- manutenção mais cara;
- memória de bugs fragmentada;
- protocolos podem se perder;
- telemetria fica menos comparável;
- melhora em uma vertical não se propaga automaticamente.

#### Opção C - Arquitetura Híbrida Recomendada para Debate

Descrição:

- núcleo técnico compartilhado;
- diretrizes totalmente externas e específicas por vertical;
- validadores comuns + validadores editoriais por vertical;
- memória de bugs comum, mas com tags por editoria;
- agentes técnicos sem hardcode editorial;
- publicação e telemetria padronizadas;
- autonomia editorial via arquivos de diretriz, não via fork caótico de código.

Prós:

- preserva consistência operacional;
- reduz duplicação;
- mantém diferença editorial entre verticais;
- permite autocura e aprendizado comum;
- facilita rollback;
- permite que comentário do editor afete a diretriz sem alterar código.

Risco:

- exige disciplina real na separação entre motor técnico e camada editorial.

Hipótese inicial para a Trindade avaliar:

> O melhor caminho parece ser arquitetura híbrida: núcleo técnico comum, diretrizes externas dinâmicas e verticais editoriais fortes.

### 8.4 Diretrizes Externas, Dinâmicas e Sem Hardcode

Princípio solicitado pelo Miguel:

> Os agentes V4 devem ser inteiramente técnicos. Nenhuma diretriz editorial, regra de LLM ou preferência de modelo deve ficar hardcoded no agente.

O sistema deve separar:

- motor técnico;
- diretrizes editoriais;
- freios por família de LLM;
- memória de bugs;
- comentários do editor;
- regras de publicação;
- telemetria;
- rollback.

Diretrizes devem ser:

- externas;
- versionadas;
- legíveis;
- carregadas dinamicamente;
- testáveis;
- conectadas à memória de bugs;
- sensíveis aos comentários do editor;
- capazes de autocorreção;
- capazes de sugerir atualização quando erro se repete;
- capazes de distinguir erro técnico, erro editorial, erro de imagem, erro de fonte e erro de tom.

### 8.5 Memória de Bugs, Autocura e Feedback Editorial

O novo V4 precisa aprender com:

- bugs de publicação;
- erros de imagem destacada;
- falhas de fonte;
- títulos ruins;
- leads burocráticos;
- tom inadequado;
- comentários do Miguel;
- correções humanas;
- rejeições de pauta;
- falhas de roteamento;
- custo excessivo;
- alucinação ou generalidade.

Estrutura desejável:

```text
memoria_bugs/
  bugs_editoriais.jsonl
  bugs_imagem_destacada.jsonl
  bugs_fontes.jsonl
  comentarios_editor.jsonl
  decisoes_correcao.jsonl
```

Cada registro deve guardar:

- data;
- editoria;
- agente;
- modelo;
- arquivo/post;
- tipo de erro;
- comentário do editor;
- correção aplicada;
- regra sugerida;
- status: aberto, corrigido, recorrente, promovido_para_diretriz.

Fluxo de autocura:

1. erro ou comentário é registrado;
2. sistema classifica o tipo de problema;
3. sugere ajuste de diretriz ou freio;
4. ajuste entra em shadow test;
5. se aprovado, vira nova versão externa da diretriz;
6. forum registra a decisão.

### 8.6 Nova Consulta à Trindade

Perguntas para resposta curta nos inboxes:

1. Devemos criar o V4 Ciência, Tecnologia e IA como vertical nobre independente?
2. Para arquitetura geral, vocês preferem integrado, vertical independente ou híbrido?
3. Como resolver imagem destacada dentro do V4 sem deixar como gambiarra final do publicador?
4. Como desenhar diretrizes externas dinâmicas sem hardcode editorial nos agentes?
5. Como a memória de bugs e os comentários do editor devem promover mudanças nas diretrizes?

Regra da rodada:

- resposta curta no inbox próprio;
- decisão consolidada no forum;
- nada de debate longo em inbox;
- toda proposta precisa indicar impacto, risco e próximo passo.

---

## 9. Index - Principios Fundamentais do Novo V4

Novo forum de principio arquitetural:

```text
Cerebro/Foruns/forum_principios_fundamentais_novo_v4_20260708.md
```

Este forum registra a orientacao central do Miguel para a codificacao:

- zero hardcode editorial nos agentes;
- diretrizes externas, limpas e sem redundancia;
- LLMs em camada propria, com roteamento/fallback/qualidade;
- bancos de dados em camadas para evitar contaminacao;
- produtores/publicadores usando apenas bancos finais/auditados;
- reaproveitamento das diretrizes, validadores, pesquisa de qualidade e midia ja existentes;
- prioridade a menos volume e muito mais qualidade editorial;
- estudo do banco de imagens do WordPress como possivel fonte para imagem destacada;
- regra visual: personagem citado no titulo deve aparecer grande e claro, preferencialmente central, validado por Gemini Vision quando aplicavel.
