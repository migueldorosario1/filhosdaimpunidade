# Fórum — Nova rodada V4: imagem destacada, vertical tecnologia, arquitetura híbrida e diretrizes externas

**Data:** 2026-07-07  
**Autor:** Miguel (Chairman)  
**Destinatários:** Trindade editorial, agentes LLM, roteador, auditores, publicadores  
**Status:** ativo (nova rodada de trabalho)  
**Fórum base:** `Cerebro/Foruns/forum_nova_rodada_v4_arquitetura_imagem_tecnologia_20260707.md`

---

## 1. Carta de convocação do Miguel (Cartinha para rodar com a Trindade)

Agentes da Trindade,

Estamos abrindo uma nova rodada sobre a arquitetura do sistema V4. A discussão anterior consolidou Política/Economia, Cultura, Internacional, Repetidor e GSN. Agora entram quatro pontos estruturais novos:

1. resolver definitivamente o problema da imagem destacada;
2. avaliar a criação de um V4 Ciência, Tecnologia e IA;
3. decidir se o sistema V4 deve ser integrado, vertical independente ou híbrido;
4. desenhar diretrizes externas, dinâmicas, sem hardcode editorial nos agentes.

Atenção ao protocolo: resposta curta no próprio inbox. Nada de debate longo em inbox. Nada de diário, log bruto ou duplicação de fórum. Fórum é decisão e memória estrutural. Canal é convocação. Inbox é resposta objetiva. Todo agente deve manter inbox limpo, curto e com status claro.

### Questão 1: Imagem destacada

O problema da imagem destacada precisa entrar como parte estrutural do V4. Não pode ser gambiarra final do publicador. A imagem é parte da edição.

Responder:
- onde deve acontecer a escolha da imagem?
- como impedir imagem genérica, errada, artificial indevida, repetida ou quebrada?
- como registrar origem, fallback, validação e correção?
- como fazer o sistema aprender com erros de imagem?

### Questão 2: V4 Ciência, Tecnologia e IA

Devemos criar uma nova vertical nobre: V4 Ciência, Tecnologia e IA.

Escopo possível: ciência, IA, Big Tech, soberania tecnológica, regulação digital, plataformas, semicondutores, dados, cibersegurança, pesquisa pública, automação e impactos sociais da tecnologia.

Responder:
- deve ser vertical própria ou subeditoria de Internacional/Repetidor?
- quais vícios editoriais essa vertical precisa evitar?
- quais fontes, gates e validações são obrigatórios?

### Questão 3: arquitetura integrada, vertical ou híbrida

Avaliar três opções:
- **Integrada**: núcleo comum, classificador comum, telemetria comum, memória de bugs comum, diretrizes externas por editoria.
- **Vertical independente**: cada V4 tem pipeline próprio e máxima autonomia.
- **Híbrida**: núcleo técnico comum, diretrizes externas por vertical, memória de bugs comum com tags, validadores comuns + validadores específicos.

Minha hipótese inicial: o melhor caminho parece ser híbrido. Núcleo técnico comum, diretrizes externas dinâmicas e verticais editoriais fortes.

Responder com prós, contras, risco principal e recomendação.

### Questão 4: diretrizes externas e dinâmicas

Princípio obrigatório:
> Os agentes V4 devem ser técnicos. Nenhuma diretriz editorial, regra de LLM ou preferência de modelo deve ficar hardcoded no agente.

As diretrizes precisam ser externas, versionadas, legíveis, carregadas dinamicamente, conectadas à memória de bugs, sensíveis aos comentários do editor e capazes de autocura.

Responder:
- como separar motor técnico, diretriz editorial, freios LLM, memória de bugs e comentários do editor?
- como uma correção do Miguel vira aprendizado?
- quando um bug recorrente deve virar nova regra de diretriz?
- como testar mudança de diretriz antes de produção?

---

## 2. Formato obrigatório da resposta no inbox

```md
Status: respondido

## Resposta curta

- recomendação:
- impacto:
- risco:
- próximo passo:

## Pontos específicos

1. imagem destacada:
2. V4 Ciência/Tecnologia/IA:
3. arquitetura integrada/vertical/híbrida:
4. diretrizes externas/autocura:
```

---

## 3. Respostas dos Agentes

### Resposta — ANTIGRAVITY

Status: respondido

#### Resposta curta

- recomendação: Implementar a arquitetura híbrida com motor comum, diretrizes editoriais externas por vertical e validador cego de imagens destacadas na camada de produção.
- impacto: Desacoplamento total da lógica técnica das regras de tom político, eliminando o inchaço de código e reduzindo erros de publicação de imagem e desvios editoriais.
- risco: A complexidade do roteador dinâmico de pautas e a latência de validação dupla por visão computacional (Vision/OCR).
- próximo passo: Validar as novas diretrizes em shadow e implementar o esquema de diretrizes externas no runner da nuvem Tencent.

#### Pontos específicos

1. **imagem destacada**: A escolha deve ocorrer na camada de produção (Redator) baseada nas entidades identificadas. Para impedir erros/gambiarras, adotar um validador cego de mídia em runtime (OCR/Vision contra o texto) e uma lista negra de reuso recente de imagens no banco SQLite (`midias_publicadas`). fallbacks devem ser imagens institucionais limpas pré-aprovadas.
2. **V4 Ciência/Tecnologia/IA**: Deve ser uma vertical nobre própria (V4-5) focado em regulação, soberania tecnológica de dados e concorrência geopolítica de Big Techs e semicondutores. Deve evitar o vício de didatismo escolar simplista e focar na tese de disputa distributiva do capital e infraestrutura de rede.
3. **arquitetura integrada/vertical/híbrida**: Recomendação Híbrida. Prós: reuso de infraestrutura comum (telemetria, logs, conexões) com total independência nas regras de escrita e tom de cada editoria. Contra: maior complexidade do roteamento dinâmico. Risco: falha no roteador enviando pauta técnica para o repetidor ou vice-versa.
4. **diretrizes externas/autocura**: As regras de prompt e os freios de LLM devem ser arquivos Markdown/JSON compilados dinamicamente em runtime. Correções manuais do editor entram como override prioritário (`feedback_editor.json`). Bugs recorrentes de auditoria (3x em 48h) devem ser programaticamente promovidos a regras do sistema. Testes shadow cegos comparando lado a lado antes de deploy.

