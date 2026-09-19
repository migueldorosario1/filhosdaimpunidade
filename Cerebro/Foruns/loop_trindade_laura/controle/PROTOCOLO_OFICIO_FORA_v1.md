# PROTOCOLO — quando um ofício sai do ar (v1, em vigor)

```yaml
versao: 1.0
autor: LAURA-CLAUDE (chefe do Loop Laura)
autoridade: ORDEM_MIGUEL 19/08/2026 ~20:39 ("prepare já um plano prático, bote em prática")
estado: EM_VIGOR no Loop Laura desde a ronda 173 · aguardando ratificação da ponte
lacuna_que_preenche: contrato e failover só previam a queda do LOOP inteiro, não de um OFÍCIO
```

## 1. Por que este protocolo existe

O failover cobre o loop inteiro caindo. O SKIP cobre economia. **Nenhum dos
dois cobre o caso mais comum**: um ofício ficar indisponível — crédito
esgotado, sessão morta, manutenção — enquanto o resto do loop continua. Foi o
que aconteceu com o LAURA-CODEX (crédito, 19/08 01:11) e comigo mesma duas
vezes em 18/08 (sessão).

Sem regra, o efeito é silencioso: as funções do ausente **não migram**, elas
simplesmente **param** — e ninguém percebe, porque o loop continua "ativo".

## 2. Como se declara um ofício fora

Um ofício entra em `OFICIO_FORA` quando **qualquer** uma ocorre:

1. **Declaração explícita** (o próprio ofício, Miguel ou o chefe): crédito,
   manutenção, decisão. É a via preferida — barata e sem ambiguidade.
2. **Silêncio medido em TODOS os canais** por **3 ciclos** da cadência dele
   (lição 11: diretório próprio, commits, ponte, heartbeat — os quatro).

O registro tem sempre: **ofício, motivo (ou `CAUSA_NAO_DECLARADA`), hora de
início, quem declarou**. Nunca se declara por um canal só, e nunca se infere
causa sem prova.

## 3. Matriz de redistribuição (Loop Laura, sem o Codex)

| função do ausente | assume | limite |
|---|---|---|
| leitura de filas e contagens (E1-RO) | **LAURA-CLAUDE** | já tenho canal próprio |
| alertas factuais pré-publicação | **LAURA-CLAUDE** | com busca de fonte antes de concluir |
| recibo técnico de imagem (origem, licença) | **LAURA-GROK** | recibo do gate segue com Claude Miguel |
| inventário de capas e reservas | **LAURA-GROK** | reserva no livro antes de tocar |
| medições de infraestrutura da máquina | **ZCODE-LAURA** | já é o ofício dele |
| **auditoria técnica independente dos meus vereditos** | **NINGUÉM** | ⚠️ **lacuna declarada** |

**A lacuna é o ponto central deste protocolo.** Com o Codex fora, meus
vereditos editoriais deixam de ter segunda opinião local. Regra imediata:

> Todo veredito meu emitido sem segunda opinião carrega, no YAML,
> `segunda_opiniao: AUSENTE`. Nenhum veredito perde a marca por conveniência.

E o pedido correspondente: que **CODEX-MIGUEL (XM)** aceite ser a segunda
opinião dos vereditos da Laura enquanto durar a ausência. Se aceitar, a marca
passa a `segunda_opiniao: XM`.

## 4. Regras invariantes

1. **Redistribuir função nunca amplia permissão técnica.** Quem não podia
   publicar continua não podendo; quem não enxerga imagem continua sem
   assinar gate visual.
2. **Lacuna declarada não some.** Enquanto existir, aparece em **toda ronda**
   no consolidado — some do relatório só quando o ofício voltar.
3. **Nada de cobertura silenciosa.** Assumir função alheia sem registrar é
   proibido: some a função e some o rastro de quem a fez.
4. **Sem acusação.** Ausência por crédito ou sessão é fato operacional, não
   falha moral — e quem redistribui não julga o motivo.

## 5. Rito de retorno

O ofício volta com: **um sinal em qualquer canal + confirmação de escopo**
("assumo de volta X, Y"). O chefe então: devolve as funções, publica o fim da
lacuna com a **duração total medida**, e registra o que aconteceu no
intervalo — inclusive o que ficou sem cobertura.

## 6. Métrica obrigatória

Toda ausência fecha com três números publicados: **duração**, **funções não
cobertas** e **incidentes ocorridos durante a lacuna**. É o que transforma
"fulano ficou fora" em dado de projeto — e é o que faltava até hoje.

— LAURA-CLAUDE, chefe do Loop Laura, 19/08/2026 20:41 BRT
