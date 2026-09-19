# V4 — nota 1–5, aprendizado editorial e autocura

**Direção:** Miguel | 18/07/2026  
**Coordenação:** Codex | `CODEX-V4-FEEDBACK-20260718`  
**Dificuldade:** média. Interface simples; integração e proteção contra distorção exigem cuidado.

## Decisão de escopo — backlog pós-lançamento

Este recurso **não faz parte do caminho crítico para ativar o V4**. Só deverá ser implementado depois que o V4 estiver pronto, testado e funcionando. Não criar agora dependências, trabalho adicional ou novos pontos de falha no lançamento.

A avaliação **não poderá ficar dentro do corpo do post**. Quando a ideia for retomada, o componente deverá ocupar uma área externa da página, no mesmo espaço estrutural dos módulos **Leia mais** e **Newsletter**, preservando a separação entre matéria e interface do site.

**Status:** `ADIADO — NÃO IMPLEMENTAR AGORA`.

## Experiência do leitor

Futuramente, na área externa posterior à matéria, junto de Leia mais/Newsletter:

> Que nota você dá para esta matéria?

`1  2  3  4  5`

Um clique envia a nota e mostra apenas `Obrigado pela avaliação`. Sem formulário, justificativa, login ou recarregar a página.

## O que gravar

- `post_id` e URL canônica;
- nota 1–5;
- data/hora;
- versão do widget;
- identificador anônimo com hash/salt ou cookie local para limitar repetição;
- origem aproximada da visita e dispositivo, somente se já permitido pela política de privacidade.

O dado público não expõe autor interno, modelo ou custo. O painel interno cruza o `post_id` com:

- agente/redator;
- provedor e modelo;
- prompt/diretriz versionados;
- editoria e tipo de pauta;
- origem da imagem, fotografia/charge e modelo visual;
- custo e tempo;
- audiência, permanência, compartilhamento e retorno.

## Proteção contra ditadura da audiência

1. Nota não muda linha editorial sozinha.
2. Não comparar posts com menos de uma amostra mínima; sugestão inicial: 10 votos.
3. Usar média suavizada, não média crua, para um post com dois votos não vencer um com cem.
4. Separar qualidade de popularidade: audiência alta não absolve erro factual; audiência baixa não invalida tema público importante.
5. Manter piso de diversidade editorial e pautas estratégicas.
6. Mudança automática só mecânica e reversível; mudança de estilo vira proposta para revisão humana.

## Relatório de aprendizado

Diário: votos, média, distribuição e anomalias.  
Semanal: top e bottom com amostra suficiente, comparados por editoria e formato.  
Mensal: quais modelos, agentes, estruturas de texto e tipos de imagem têm melhor combinação de nota, leitura e compartilhamento.

Para post nota 5, registrar o que pode explicar o resultado: abertura, subtítulo, novidade, análise, ritmo, modelo, autor, imagem e origem da audiência. Para nota baixa, procurar padrão; não punir automaticamente um agente por uma matéria.

## Ciclo de autocura

```text
PUBLICAR → MEDIR → AGRUPAR PADRÕES → PROPOR MUDANÇA
        → TESTAR EM SHADOW → REVISÃO HUMANA → VERSIONAR DIRETRIZ
```

- Diretrizes editoriais e visuais ficam fora do agente, em arquivos versionados.
- O observador cria uma proposta de mudança com evidências.
- O sistema testa a proposta contra casos históricos e canário.
- Somente depois ela vira nova versão ativa.
- Rollback é troca para a versão anterior da diretriz.

## Implementação sugerida

### Fase 1 — leve

- pequeno widget no artigo;
- endpoint próprio do WordPress ou serviço mínimo;
- tabela `cafezinho_post_ratings`;
- proteção de repetição e rate limit;
- painel/CSV interno por `post_id`.

### Fase 2 — ligação com V4

- `post_id` associado ao recibo de produção;
- relatório por agente/modelo/prompt/imagem;
- alertas de amostra e fraude;
- propostas automáticas, nunca promoção editorial automática.

### Fase 3 — aprendizagem controlada

- testes A/B pequenos de diretrizes externas;
- comparação com audiência e tempo de leitura;
- atualização versionada da linha após decisão humana.

## Esforço estimado

- Protótipo local do clique + armazenamento: pequeno.
- WordPress seguro + antispam + painel: médio.
- Ligação completa com telemetria V4 e autocura: médio/alto.

O MVP pode ser lançado antes do sistema completo: primeiro coletamos notas confiáveis; depois ligamos ao aprendizado do V4.
