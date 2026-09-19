---
id: MIGUEL-ORDEM-LAURA-SSH-RO-ADENDO-CATEGORIAS-20260816-1719
de: MIGUEL
para: LAURA-CLAUDE-CHEFE
tipo: ORDEM_MIGUEL
estado: ENVIADO
data_brt: 2026-08-16 17:19
ref: MIGUEL-ORDEM-LAURA-SSH-RO-INVENTARIO-20260816-1704
---

# Adendo de Miguel — categorias incluídas na leitura

Miguel confirmou que o Loop Laura também pode ler as categorias dos posts pelo
canal SSH read-only.

Escopo incluído:

- IDs, nomes e slugs das categorias vinculadas a cada post;
- tags vinculadas, quando úteis à revisão editorial.
- comparação entre as categorias atuais, o conteúdo, a vertical e as
  diretrizes editoriais, para concluir se a categorização está correta.

Quando houver divergência, o relatório deve registrar:

```yaml
post_id:
categorias_atuais:
avaliacao: CORRETAS | AUSENTE | ERRADA | EXCESSIVA | DUVIDA_EDITORIAL
categorias_recomendadas:
justificativa:
confianca: alta | media | baixa
```

Permanece proibido criar, renomear, excluir, atribuir ou remover categorias e
tags. A interface homologada é `taxonomy <post_id>`; não há WP-CLI livre nem
consulta arbitrária de banco.
