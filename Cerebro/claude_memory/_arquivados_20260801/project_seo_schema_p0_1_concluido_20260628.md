---
name: seo-schema-p0-1-concluido-20260628
description: "P0-1 schema NewsArticle CONCLUÍDO 28/06 ~21:40 BRT — era wpseo-local injetando LocalBusiness errado, desativado."
metadata: 
  node_type: memory
  type: project
  originSessionId: 595de6c5-a613-4f51-b42d-e3bc009de9ef
---

# P0-1 Schema NewsArticle — CONCLUÍDO 28/06 ~21:40 BRT

**Status**: ✅ resolvido em ~5 min via `wp plugin deactivate wpseo-local`

## O que aconteceu

- Auditoria inicial indicou "schema NewsArticle AUSENTE em matérias" — **falso negativo** por grep malfeito
- Investigação real (28/06 21:30 BRT): `wpseo-news` 13.3 JÁ estava gerando `NewsArticle` em todas as matérias, com headline/datePublished/dateModified/author/CommentAction/ImageObject/BreadcrumbList
- Problema real identificado: `wpseo-local` 15.8 injetava `OpeningHoursSpecification` (schema de LocalBusiness — horário de loja física) em TODAS as páginas

## Decisão

Miguel confirmou: "Não, sou só veículo jornalístico" — sem endereço físico, loja, ou atendimento presencial que justifique schema LocalBusiness.

## Ação

- Backup config: `/root/backup_wpseo_local_20260628.json` no ServerDo.in
- `wp plugin deactivate wpseo-local`
- Cache nginx limpo
- Validado homepage + matéria amostra (`/2026/06/28/china-e-a-grande-vencedora...`): `OpeningHoursSpecification` **sumiu**, `NewsArticle` preservado

## Schema outputado pós-fix (matéria amostra)

```
@type":NewsArticle ✅ (headline, datePublished, dateModified, author:Redação)
@type":CommentAction ✅
@type":Person ✅ (autor)
@type":ImageObject ✅
@type":BreadcrumbList ✅
@type":WebPage, WebSite ✅
@type":Organization ✅ (publisher)
```

## Schema restante NÃO problema

`QuantitativeValue` e `PropertyValueSpecification` ainda aparecem — são legítimos do schema.org para ImageObject (width/height), **não** de LocalBusiness.

## Rollback

`wp plugin activate wpseo-local` reativa se necessário.

## Por que isso importa

- Remove sinal de "empresa local" para o Google (que apareceria em buscas erradas — horário, endereço)
- Preserva NewsArticle (essencial para Google News e Knowledge Graph)
- Sem IA, sem código novo — só desativar plugin errado

## Cross-references

- Snapshot: `Projeto Cafezinho Agentes/Ponto de Retomada/GLM Coding/20260629_015600_sessao.md`
- Fórum auditoria: `Projeto Cafezinho Agentes/Foruns/forum_auditoria_wordpress_seo_20260628.md`
- Fórum execução: `Projeto Cafezinho Agentes/Foruns/forum_execucao_p0_wordpress_seo_20260628.md`
- [[project-seo-monitoramento-fase0-20260628]] — contexto
