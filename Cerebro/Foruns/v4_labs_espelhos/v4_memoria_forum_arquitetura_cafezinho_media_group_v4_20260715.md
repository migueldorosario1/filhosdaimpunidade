# Fórum de arquitetura — Cafezinho Media Group e V4

Data: 15 de julho de 2026  
Status: arquitetura operacional de referência

## 1. Escopo do V4 do Cafezinho

O V4 ativo do Cafezinho possui quatro editorias principais:

1. Política e Economia
2. Geopolítica e Internacional
3. Ciência, Tecnologia e IA
4. Cultura

Essas quatro editorias compartilham o mesmo núcleo editorial, o mesmo padrão de revisão, o mesmo fact-check, o mesmo gate de segurança e o mesmo contrato de diretrizes editoriais unificadas.

O V4 trabalha em modo shadow e draft-only até que os testes de autonomia, autocura, imagem, infraestrutura e publicação sejam concluídos. Nenhuma diretriz editorial autoriza publicação pública automática.

## 2. Repetidor

O Repetidor é uma função ou rota de adaptação e republicação que ainda está em teste.

Ele não constitui uma quinta editoria. Enquanto estiver em validação, deve herdar o núcleo editorial V4, preservar proveniência e passar pelos mesmos gates de revisão, fact-check, imagem e segurança. Não pode criar uma política editorial paralela.

## 3. Agentes temáticos

Os agentes temáticos anteriores foram aposentados.

Eles não fazem parte da operação atual e não devem ser reativados como fontes independentes de diretrizes. Quando o V4 estiver testado e funcional, agentes temáticos poderão ser reconstruídos como projeções especializadas do V4.

Um futuro agente temático poderá acrescentar conhecimento técnico de um campo, como clima, energia, trabalho, saúde ou IA, mas deverá herdar:

- o contrato editorial unificado
- a diretriz comum V4
- as regras de pontuação
- as regras de tensão, contraditório e suspense invisíveis
- a revisão e o fact-check
- o gate de publicação
- a política de imagens e proveniência

O agente temático não poderá criar uma nova doutrina editorial autônoma.

## 4. GSN e sites temáticos

GSN significa Global South News. Ele pertence ao ecossistema de sites temáticos e não ao núcleo V4 do Cafezinho.

Os sites temáticos utilizam infraestrutura própria e não devem ser confundidos com as quatro editorias V4. A exceção operacional é o Cafezinho.News, que funciona como espelho e permanece fora de indexação conforme sua política própria.

GSN, Cafezinho.News e outros sites temáticos não são editorias adicionais do V4 e não devem ser incluídos na contagem de editorias V4.

## 5. Hierarquia do Cafezinho Media Group

### Núcleo V4 do Cafezinho

Quatro editorias principais com contrato editorial unificado e publicador WordPress blindado.

### Rotas auxiliares do núcleo

Repetidor em teste, bancos de dados, agentes de coleta, agentes de imagem, revisão, fact-check e autocura. Essas rotas servem ao V4 e não criam editorias novas.

### Ecossistema temático externo

GSN, Cafezinho.News e futuros sites temáticos com infraestrutura e políticas próprias. Eles podem aproveitar componentes técnicos do V4 quando apropriado, mas não alteram a governança editorial do Cafezinho V4.

## 6. Regra de herança

O V4 é a fonte editorial do núcleo do Cafezinho.

O Repetidor herda do V4.

Futuros agentes temáticos poderão herdar do V4 por projeção explícita.

Sites temáticos externos não são editorias V4 e não devem ser usados para inferir o estado de prontidão do V4.

## 7. Decisão arquitetural

O Cafezinho Media Group não deve voltar à arquitetura anterior, na qual agentes temáticos, rotas de publicação e editorias acumulavam diretrizes fragmentadas em contratos e códigos diferentes.

A arquitetura canônica é:

`V4 unificado → quatro editorias → funções auxiliares controladas`

Em paralelo, existe:

`ecossistema temático externo → sites próprios → políticas próprias`

As duas camadas podem compartilhar infraestrutura técnica quando isso for auditado, mas não compartilham automaticamente identidade editorial, status de publicação ou critérios de prontidão.

## 8. Estado atual

- Quatro editorias V4 ativas
- Diretrizes editoriais unificadas em consolidação
- Repetidor em teste
- Agentes temáticos aposentados
- GSN fora do núcleo V4
- Sites temáticos fora da contagem de editorias V4
- Publicação autônoma ainda não autorizada

Esta arquitetura passa a ser a referência para novos fóruns, contratos, testes e decisões de lançamento.
