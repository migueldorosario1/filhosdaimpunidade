# LAURA-CODEX → Miguel — sync apagou presença durante lock

```yaml
ts_brt: 2026-08-18T10:11:00-03:00
incidente: PA-2_RECORRENTE_SYNC_STALE
commit_causal: 479dea0499db3e7a32b2fe202ddfe948290a43d2
perda_final: NAO
wordpress_mutations: 0
```

O sync remoto das 10:07 apagou quatro linhas da presença própria de
LAURA-CODEX enquanto o lock local estava ativo. O push da ronda 141 parou em
conflito; preservei o remoto e restaurei apenas minhas entradas únicas. Nenhum
conteúdo alheio foi descartado e não houve perda final.

Isso confirma que o problema não é só `git add` amplo: uma cópia canônica stale
está sobrescrevendo arquivos append-only antes do commit e o sync remoto não
consegue observar o lock local. Gate proposto: pull/integração antes da
exportação, união append-only por identidade/ref e aborto de remoção sem
manifesto. Evidência: `git show 479dea04` e rebase da ronda 141.

— LAURA-CODEX
