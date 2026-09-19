# Alerta pré-publicação — 266398 é duplicado compilado de pautas existentes

```yaml
identidade: LAURA-CODEX
tipo: ALERTA_PRE_PUBLICACAO_DEDUP
ts_brt: 2026-08-18T06:10:00-03:00
post_id: 266398
status: pending
featured_media_id: 0
classificacao: HOLD_DUPLICADO_COMPILADO
wordpress_mutations_laura_codex: 0
```

## Achado

O pendente 266398, criado às 06:02:17, não é apenas uma pauta do mesmo tema.
Ele recompila o núcleo e os desdobramentos de pelo menos cinco posts já
existentes na fila:

| Trecho/assunto de 266398 | Post já existente | Estado às 06:10 |
|---|---:|---|
| expiração do prazo EUA–Irã sem acordo | 266364 | `future` 07:45, mídia 266375 |
| ameaça de Trump de bombardear Omã e negociação marítima Irã–Omã | 266388 | `pending`, mídia 266390 |
| poucas semanas e possível escalada militar iraniana | 266267 | `pending`, mídia 266276 |
| fim do memorando e postura ofensiva do Irã | 266286 | `pending`, mídia 266293 |
| redução de exercícios EUA–Coreia do Sul | 266392 | `pending`, mídia 266395 |

O primeiro par é duplicação direta de pauta: 266398 tem o título “Prazo de
negociação entre Estados Unidos e Irã expira sem acordo final”; 266364 já está
agendado como “Trump deixa expirar prazo de acordo de paz com o Irã”. Ambos
narram o fim do prazo de 60 dias, ausência de acordo final, tensão em Ormuz e
ameaça contra Omã.

Além disso, 266398 agrega ataques no Líbano, Gaza/Cisjordânia, resoluções do
Comitê Nacional Democrata e Coreia do Sul. Esses blocos não sustentam o título
e formam um resumo multitemático em vez de uma matéria focalizada.

## Recomendação

`HOLD_DUPLICADO_COMPILADO`: não agendar, não aplicar imagem e não promover
266398 antes de o owner editorial decidir entre:

1. manter 266364 como a versão focalizada do evento e descartar/arquivar o
   compilado 266398; ou
2. se houver fato realmente novo, reescrever 266398 apenas com esse delta,
   removendo todos os blocos já cobertos pelos cinco posts acima.

Também recomendo que o gate de deduplicação trate compilados: comparar cada
bloco temático, não apenas título ou similaridade global. Um texto costurado
pode ter baixa similaridade total e ainda duplicar várias pautas simultâneas.

LAURA-CODEX permaneceu no E1-RO e não alterou status, conteúdo, mídia ou fila.

— LAURA-CODEX, 18/08/2026 06:10 BRT
