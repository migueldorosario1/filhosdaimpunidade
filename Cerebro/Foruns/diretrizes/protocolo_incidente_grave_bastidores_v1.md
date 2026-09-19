# Protocolo v1 — incidente grave de bastidores ou processo interno

**Autoridade:** Miguel  
**Data:** 15/08/2026  
**Aplicação:** Loop Miguel, V4, repetidores, WordPress e sites temáticos

## Quando este protocolo dispara

Dispara automaticamente quando qualquer conteúdo público revela ou sugere:

- nome de modelo, provedor, agente ou ferramenta usado internamente;
- prompt, instrução, comentário de operação ou conversa de bastidor;
- parâmetros de ferramenta em links, como `utm_source=openai`;
- metalinguagem de rascunho, “fonte-base”, “material analisado” ou equivalente;
- chave, token, senha, caminho interno, host ou dado de infraestrutura;
- HTML, metadata ou atributo invisível que revele o processo;
- reincidência de um erro que uma revisão anterior declarou resolvido.

## Regra central

**Conter primeiro; investigar profundamente logo depois; nunca encerrar sem
resposta direta e prova preventiva.** Risco ainda público é corrigido de
imediato por executor autorizado. Não se espera o fórum para tirar o vazamento
do ar. Mas a contenção não encerra o incidente.

## Etapas obrigatórias

### 1. Preservar evidência

- salvar revisão/snapshot anterior;
- registrar post ID, URL, título, status e autor;
- guardar a string exata exposta e todos os locais afetados;
- registrar hash da versão anterior;
- obter horário de publicação e de correção;
- calcular a janela pública, deixando claro quando for valor máximo estimado.

### 2. Conter

- remover somente o elemento indevido;
- preservar conteúdo editorial e parâmetros funcionais;
- purgar cache quando aplicável;
- validar conteúdo canônico e página pública;
- manter rollback recuperável.

### 3. Medir alcance

- fazer scan em modo leitura dos posts recentes e verticais relacionadas;
- criar manifesto antes de correção em lote;
- não assumir que um caso é isolado;
- separar confirmado, suspeito e limpo.

### 4. Reconstruir a cadeia

Identificar com evidência:

- coletor/candidato/origem;
- job ID e modelo que gerou;
- resposta bruta e call ID, se houver;
- worker e gates que persistiram;
- revisores internos e externos, com payload, parecer, custo e horário;
- agente que autorizou/agendou/publicou;
- observadores que marcaram como limpo;
- componente responsável pela prevenção estrutural.

O modelo que produziu o erro é origem material, não substitui a
responsabilidade editorial do agente que aprovou a publicação.

### 5. Abrir fórum exclusivo

Todo incidente grave ganha fórum próprio em `Cerebro/Foruns/`, contendo:

- cronologia;
- evidências;
- conteúdo exato exposto;
- janela pública;
- matriz de responsabilidades;
- perguntas nominais;
- correção feita;
- prevenção proposta;
- critérios de encerramento.

### 6. Resposta direta do Claude Miguel

Quando Claude Miguel for editor/aprovador ou chefe do loop, ele deve responder
em primeira pessoa, com franqueza, no fórum e no seu chat com Miguel. Deve:

- confirmar ou refutar seu papel com logs;
- dizer o que leu e o que não leu;
- identificar quais revisores externos realmente rodaram;
- fornecer call IDs/payloads/pareceres ou declarar que o rastro não existe;
- assumir a parcela editorial que lhe cabe;
- explicar a falha sem culpar apenas modelo/regex;
- propor mudança concreta e teste que dê segurança contra repetição.

### 7. Memória e índice

- adicionar evento estruturado ao JSONL diário de bugs;
- criar relatório forense Markdown para incidentes graves;
- registrar aprendizado na memória própria de bugs do Claude Miguel;
- atualizar índices;
- levar os documentos ao Cérebro canônico, GitHub e backups externos.

## Critérios para fechar

O fórum só pode passar a `FECHADO` quando houver:

1. vazamento removido e página pública validada;
2. alcance medido;
3. responsáveis identificados por função;
4. resposta direta do Claude Miguel, quando aplicável;
5. causa técnica demonstrada;
6. correção preventiva implementada ou plano com dono e prazo;
7. testes de regressão cobrindo o caso real;
8. memória e índices atualizados;
9. confirmação de backup/sincronização.

“Corrigido no post” significa apenas **contido**, não encerrado.

