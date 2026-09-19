# O TESTE DE CONTROLE TAMBÉM ERRA: `post_date` DE RASCUNHO É MUTÁVEL POR DESIGN

**Data:** 10/09/2026 (ronda 402ª DS-Dell)
**Família:** instrumento que responde certo à pergunta errada (irma da 190/191/192/198/200/201)
**Bug:** BUG-20260910-DS-202 (novo, meu) — corrige o teste proposto em BUG-20260910-DS-192 (392ª) e repetido no BUG-195 (395ª)

## O quê

Na 392ª e na 395ª eu propus, como **detector de retrodatação**, cruzar:

    post_date  ×  _cafezinho_origem.ts     →  divergência > 5 min = peça retroagida

O teste é **válido para `post_status=publish`**. Em **rascunho**, ele **dispara sempre** — e o
motivo é do próprio WordPress, não da peça.

## Por quê (prova, colhida na mesma ronda)

**(a) Prova viva, por acidente.** O rascunho **269792** («Anistia acusa Rússia…», origem
`ts` = 16:56:39, uid 5470) tinha:

* 1ª medição (17:04) → `post_date` = **16:57:12**
* 2ª medição (17:1x) → `post_date` = **17:05:18**

Mesmo ID, mesmo dia, mesma origem, **nenhuma publicação**. A única coisa que mudou foi **um save**:
a esteira mexe no rascunho e o WordPress **regrava `post_date`** (e `post_modified`).

**(b) O quase-bug que eu ia abrir.** Os três rascunhos da **série soja** — **269630 / 269633 /
269636** — mostram `post_date` = **10/09 16:48** e `_cafezinho_origem.ts` = **09/09 15:52:33 /
15:55:48 / 15:59:03** (uid 5786): **~25 h de divergência**. Pelo meu teste, era retrodatação
grosseira. **Não é.** Os três **nasceram 09/09**, foram **re-salvos hoje às 16:48** (um deles tem
`_edit_lock` — a peça foi aberta no editor) e o WordPress regravou a data.

## Como aplicar

1. O cruzamento `post_date` × `_cafezinho_origem.ts` **só vale para `post_status=publish`**
   (onde o `_wp_old_date` e o `ts` firmam o par).
2. Em **rascunho**, o campo que diz «quando foi mexido» é **`post_modified`**;
   `post_date` de rascunho é **mutável por design** a cada save.
3. Leitura correta de «rascunho com data nova» = **«a peça foi trabalhada hoje»**,
   nunca «a peça mentiu a data».
4. **Ordem de trabalho:** antes de denunciar, **meça duas vezes** o mesmo campo, com minutos de
   intervalo, no mesmo ID. Se o valor **mudar sem publicação**, o campo é mutável e o teste é
   que está errado — não a peça.

## Régua que fica

**Um teste de controle errado é pior que nenhum: ele acusa inocente com cara de prova.**
O valor de um detector não está em ele disparar — está em **não disparar em quem não deve**.
E a pergunta que salva é sempre a mesma da série de hoje:
**não «este campo está certo?», mas «o que este campo SIGNIFICA?»**
