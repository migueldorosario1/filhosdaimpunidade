# Errata da ronda 126 — superfície REST de `CONTENT END`

```yaml
identidade: LAURA-CODEX
tipo: ERRATA_IMUTAVEL
ts_brt: 2026-08-18T01:10:50-03:00
artefato_corrigido: 20260818_002931_codex_ronda_126.md
estado: VERIFICADO
```

Onde a ronda 126 diz `rest_ce=0/9`, leia-se:

- conteúdo armazenado pela E1-RO: **0/9**;
- JSON REST bruto: **9/9**;
- `content.rendered` decodificado: **9/9**;
- `<article>` público fresco: **0/9**.

IDs rechecados às 01:09: 266142, 266346, 266133, 266224, 266291, 266285,
266275, 266258 e 266297. Cada resposta REST contém uma ocorrência de
`<!-- CONTENT END 1 -->` no fim de `content.rendered`.

A conclusão correta é: marcador ausente do conteúdo canônico, presente na API
REST e ausente do artigo visto pelo leitor. A medição divergente anterior está
retirada. Sua causa fica `SEM_DADOS` porque a ronda 126 não preservou comando e
resposta bruta suficientes para reconstruí-la.

— LAURA-CODEX, 18/08/2026 01:10:50 BRT
