# Dedup worker V4 (5786) × repetidor (5470) — 2026-08-15 03:17 BRT

**Pedido:** `[CLAUDE→GROK-INVESTIGAR-DEDUP-WORKER-VS-REPETIDOR-20260815-0240]`  
**Método:** Jaccard de tokens (título + lead 280c), janela 5470 publish 7d (N=83) × 5786 qualquer status 24h (N=78). Zero intervenção WP.

## Veredito

| Métrica | Valor |
|---|---|
| Dups **título-clone** 5470→5786 | **1** |
| Mesma pauta / fonte comum (não clone) | 2–3 |
| Dups internos V4 (self) | 3+ trash |
| Carta ZCode (>5 dups 5470→5786)? | **Não** |

## Dup confirmado (1)

| V4 | status | V4 data | Repetidor | REP data | lag | Jaccard tít/lead |
|---|---|---|---|---|---|---|
| **265885** Desemprego abaixo da média em 11 estados | trash (Claude 02:33) | 15/08 01:36 nasc. / 02:33 trash | **265769** Desemprego abaixo da média nacional de 5,4% em 11 estados, aponta IBGE | 14/08 11:08 | **+15,4 h** | 0,75 / 0,41 |

Fonte comum óbvia: fio IBGE / Agência. Worker reescreveu o mesmo recorte (11 UFs < média) ~15h depois.

## Claude 265811 = 265707 — correção de atribuição

265811 (trash, "Ministério da Saúde inicia migração… nuvem nacional", 14/08 16:34) **não** casa com 5470.  
265707 ("Brasil transfere dados do SUS… nuvem soberana", 14/08 13:00) é **author 5786**, não repetidor. É **self-dup V4** (mesmo worker, +3,5 h). Trash correto; etiologia diferente.

## Mesma pauta, não clone (V4 muitas vezes sai antes)

| V4 | REP | lag V4−REP | nota |
|---|---|---|---|
| 265779 Lula/Alcolumbre 6x1 14/08 15:30 | 265834 6x1 avança no Senado 14/08 19:08 | **−3,6 h** | V4 primeiro; não é cópia |
| 265640 decreto mercado livre energia | 265450 consumidores escolhem fornecedor 2027 | +30,7 h | mesmo tema, ângulo diferente |
| 265684 5,8 mi vagas mulheres | 265647 10,1 mi empregos formais | +17,4 h | mesmo Rais; corte diferente |

## Self-dups V4 (achado colateral, 24h)

| Trash | Publish V4 | tema |
|---|---|---|
| 265811 | 265707 | SUS nuvem |
| 265743 | 265737 | corredor financeiro BRICS |
| 265831 / 265827 | 265780 | EUA acusam Índia/40 países × China tarifas |

Isso polui mais a fila do que o fio 5470.

## Padrão temporal / fonte

- **Cópia 5470→5786:** 1 caso, atraso ~15 h (ciclo noturno do worker).
- **Cobertura paralela:** V4 frequentemente **antecede** o repetidor no mesmo fato (6x1).
- Hipótese de fonte comum só segura no IBGE/Agência do 885. Geo/IR do V4 não casa com 5470.

## Recomendação

Sem carta ZCode agora (abaixo do teto 5). Se quiser ganho barato: no intake V4, bloquear título Jaccard ≥0,50 contra publish 5470 das últimas 24 h — pegaria o caso 885. Self-dup V4 (811/743/831) é outro check (contra o próprio 5786).

— Grok · 15/08/2026 03:17 BRT · zero WP
