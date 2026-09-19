---
name: Estreia pública dos 7 agentes temáticos — atenção reforçada
description: Primeira vez que Lula/IA/Latam/Sheinbaum/Mercado/Matriz/Inflação publicam AO VIVO em status=publish. Miguel pediu flag especial de monitoramento nas primeiras publicações.
type: project
originSessionId: aa80db10-86be-445e-a416-a07e41c62677
---
Em 2026-04-21 15:54 BRT o crontab passou a ter os 7 novos agentes temáticos como LIVE (status=publish, 1/dia). Miguel pediu **atenção especial reforçada nas primeiras publicações de cada um** — é o teste público de estreia.

**Why:** agentes temáticos novos estão em produção real pela primeira vez. Bugs editoriais ou técnicos agora afetam o site público. Erros de estreia custam credibilidade.

**How to apply:** em cada ciclo de monitoramento 24h, priorizar os temáticos novos acima de qualquer outra checagem até a primeira publicação saudável de cada um ser confirmada. Se achar bug, corrigir IMEDIATAMENTE (autocorreção autorizada) e registrar em `Outros/manual_de_bugs.md`.

## Agenda de estreias

| Data        | Hora   | Agente                     | Status no crontab                       |
|-------------|--------|----------------------------|-----------------------------------------|
| 2026-04-21  | 17:00  | Matriz Energética FOSSIL   | 1ª estreia (dia ímpar)                  |
| 2026-04-21  | 18:30  | Inflação                   | 2ª estreia (aborta se dia>15 + SIDRA antigo) |
| 2026-04-22  | 09:30  | Lula                       | 3ª estreia                              |
| 2026-04-22  | 10:30  | IA                         | 4ª estreia                              |
| 2026-04-22  | 11:30  | Latam                      | 5ª estreia                              |
| 2026-04-22  | 13:30  | Sheinbaum                  | 6ª estreia                              |
| 2026-04-22  | 15:30  | Mercado                    | 7ª estreia                              |
| 2026-04-22  | 17:00  | Matriz Energética TRANSICAO| variante par (dia 22)                   |

## Checklist observacional por estreia

Para cada primeira publicação, verificar no log do agente + WP:

1. **Disparo cron** — syslog tem `CRON CMD` do script no horário.
2. **Sem traceback** — `tail logs/<agente>.log` não tem `Traceback`/`Exception`.
3. **Status=publish** — não ficou draft. `wp_posts.post_status='publish'`.
4. **Título não robótico** — sem padrões tipo "Nesta segunda-feira, 21 de abril de 2026" (bug #237300/237297 de 20/04, `feedback_data_chumbada_link_tangencial`).
5. **Fecho natural** — sem "E daí?", "Em resumo", "Por fim" (`feedback_fecho_natural_sem_e_dai`).
6. **Imagem real** — og:image da fonte ou banco SQLite ou Flickr live; nunca cartoon se houver foto real.
7. **Tribunal Visual aprovou** — sem reprovação silenciosa.
8. **Interlink "Leia também"** — bloco final com hr + link (`deploy_interlink_historiador_20260419`).
9. **Sem citação crua** — regra de 2026-04-21: `publicador_tematicos._limpar_citacoes_ia` removeu `([fonte.com](url))`.
10. **Categoria correta** — Lula→Nacional, IA→Ciência/Tech, Latam/Sheinbaum→Internacional (pendência Pátria Grande ainda aberta), Mercado→Economia, Matriz→Energia, Inflação→Economia.
11. **Newsletter** — Mailchimp recebeu (caixa injetada em 20/04).
12. **Comentarista** — disparou background.
13. **Cross-post redes** — entrou na `fila_redes` pra Facebook/Twitter.
14. **Específico Inflação** — se dia>15 e SIDRA ainda é do mês anterior, DEVE abortar com mensagem clara (não publicar com dado estale).
15. **Específico Matriz** — log do env MATRIZ_FOCO bate com paridade do dia (ímpar=FOSSIL, par=TRANSICAO).

## Ação se bug detectado na estreia

- **Técnico (traceback, DB, API)**: corrigir via `sed` ou edit local + `rsync` (sem `-a`), registrar em manual_de_bugs.md, re-executar manualmente.
- **Editorial (título, fecho, foto, link)**: pausar o agente (comentar cron), corrigir prompt/regra, redeploy, rodar manual pra validar.
- **Em caso de sequência de falhas**: acionar Miguel via memória e marcar agente como QUARENTENA.
