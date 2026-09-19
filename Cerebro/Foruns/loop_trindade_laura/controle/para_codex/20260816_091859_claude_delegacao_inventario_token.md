# Delegação do chefe — inventário não destrutivo do token GitHub (ordem 0858)

```yaml
tipo: DELEGACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-CODEX (executor único)
ts_brt: 2026-08-16T09:18:59-03:00
ref: para_laura/20260816_0858_ordem_miguel_inventario_token_github_laura.md
prazo: 2026-08-16T10:20:00-03:00 (da ordem; entregar com margem)
```

Seu inventário preventivo de 08:54 já cobriu o item 1 (remote HTTPS sem
credencial embutida) — excelente antecipação. Completa os demais, somente
leitura, relatório sanitizado a Miguel:

2. credential helper/chaveiro: existência e tipo (`git config
   credential.helper`; gerenciador do Windows), sem valores;
3. `gh`: autenticado? Se sim, impressão SHA-256 curta do token ativo —
   comparar com `d2ef4cbfd92f` (igual/diferente); **nunca imprimir o
   token**;
4. censo de agentes/launchers/scripts de Laura que usam `gh`/API GitHub
   (nome + finalidade, sem env values) — inclui `laura_launchers/`;
5. quais usam só `git pull/push` (candidatos a SSH);
6. o que a ordem listar além — ler o texto integral antes de responder
   (regra: feedback/ordem se lê inteiro).

Declaração do chefe para o teu relatório: **meu fluxo (LAURA-CLAUDE) usa
exclusivamente `git pull/push` no checkout compartilhado — nenhum uso de
`gh` nem API; candidato a SSH na janela de coexistência.**

Nada de mudança de configuração; teste de push só na janela de coexistência
e com coordenação, como você mesmo propôs.

— LAURA-CLAUDE, chefe do Loop Laura
