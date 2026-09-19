# 📰 Fórum — V4 Home: só nota top na capa, 10% home / 90% no-home, dia=noite

**Data:** 2026-08-08 ~01:55 BRT
**Executor:** ZCode (GLM-5.2, builtin:zai-coding-plan)
**Autoridade:** pedido do Miguel (madrugada 08/08), aplicação PENDENTE confirmação
**Memória pareada:** `Memorias/memoria_v4_home_top_10pct_dia_noite_20260808.md`

---

## 1. O que o Miguel pediu (transcrição estruturada)

- "Volta a fazer o V4, deixar **tudo no home**."
- "Só assim que eu tiver **nota máxima, máxima, top, top**, deixa ele sair no home."
- "Só deixa um caso assim, uns **10% à noite**. A mesma cota do dia. Todo dia."
- "o V4 está produzindo, qual a quantidade?"
- "**deixa então só 10% home 90% no home** à noite. De dia, quanto?"
- "qual é o percentual de visibilidade na capa?"

**Interpretação operacional (consolidada):** só a **nata** (score no topo de cada vertical) sai na capa (~10%); os demais ~90% vão No Home e **FICAM** (não voltam após 4h). Mesma regra de dia e de noite, todo dia — acaba a janela 22h-06h separada de geo/ciência.

## 2. Situação ATUAL do V4 (números reais lidos do NYC em 08/08 ~01:55 BRT)

### Produção (draft_confirmed, últimos 7 dias)

| Vertical | 7d | média/dia | capa | % capa | No Home |
|---|---:|---:|---:|---:|---:|
| Nacional | 107 | ~15 | ~25 | ~23% | ~82 |
| Geopolítica | 95 | ~14 | ~2 | ~2% | ~93 |
| Ciência/Tec/IA | 27 | ~4 | ~2 | ~7% | ~25 |
| Regional Sudeste | 6 | (novo) | 0 | 0% | 6 |
| **Total** | **~229** | **~33/dia** | ~29 | ~13% | ~200 |

### Scores REAIS observados (candidates, máximos por vertical)

| Vertical | score MÁX | score médio | n candidatos |
|---|---:|---:|---:|
| Nacional | **24,5** | 9,13 | 648 |
| Geopolítica | **25,0** | 8,12 | 1506 |
| Ciência/Tec/IA | **21,5** | 10,82 | 119 |
| Regional N | 9,8 | 4,19 | 463 |
| Regional SE | 10,0 | 4,23 | 296 |
| Regionais CO/NE/S | 6,0 | ~4 | 1180 |

### Thresholds de capa ATUAIS (`no_home_score_policy.json` no NYC)

| Vertical | cover_min atual | observado max |
|---|---:|---:|
| nacional | 13,0 | 24,5 |
| geopolitica | 12,0 | 25,0 |
| ciencia | 10,0 | 21,5 |
| repetidor_estatal | 95,0 (+ nota_llm 90) | 95 |

### Mecanismo `force_no_home` + janela (worker linhas 49/59/199-208/2064-2073)

- **geopolitica e ciencia** têm `force_no_home: True` → TODO rascunho novo nasce No Home.
- **EXCEÇÃO (`_janela_home_geo_ciencia`):** 22h→06h BRT **E** sáb/dom → o force_no_home NÃO se aplica; decide só a policy de score. (Ordem Miguel 06/08.)
- Resultado: geo/ciência só escapam pra home de madrugada/fds → daí os ~2%/~7% de capa delas.
- **Removedor (`remover_no_home.py`, cron `0 */2 * * *`):** tira a tag 20699 **4h depois** → o post "sobe" pra home mesmo sem nota. ⚠️ Isso faz o No Home ser **temporário** hoje.

## 3. O que PRECISA mudar pra "10% home / 90% no-home definitivo, dia=noite"

Para os 90% ficarem fora da capa de verdade (e não voltarem após 4h):

1. **Parar/desligar o removedor** (`remover_no_home.py`) — ou o no-home vira permanente. Hoje ele libera tudo.
2. **Acabar com a janela 22h-06h** (`_janela_home_geo_ciencia`) — geo/ciência passam a ter a MESMA regra dia e noite.
3. **Subir thresholds** pra só a nata (~10%) passar.
4. Manter `force_no_home` de geo/ciência DESLIGADO (igual nacional — decide só por nota).

### Thresholds propostos (calibrados pros ~10% de capa, baseados no score real)

| Vertical | cover_min atual | cover_min proposto | nota |
|---|---:|---:|---|
| nacional | 13,0 | **15,0** | ~top 10% (max real 24,5) |
| geopolitica | 12,0 | **16,0** | ~top 10% (max real 25,0) |
| ciencia | 10,0 | **13,0** | ~top 10% (max real 21,5) |
| repetidor_estatal | 95 + 90 | mantém | já é restritivo |

(Backup criado: `/root/v4_vertical_draft_worker.py.bak_pre_v4_home_top_20260808`.)

## 4. Estado: o que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** diagnóstico completo ao vivo (números reais do NYC + policy + mecanismo), backup do worker criado, patch desenhado.
- **Falta (PENDENTE confirmação do Miguel):** aplicar as 4 mudanças acima no NYC + ajustar contrato JSON + parar o removedor. Tudo mexe em produção/WordPress.
- **Preciso do Miguel:** 1 palavra — **"aplica"** (10%/90% dia=noite), **"tudo home"** (100% na capa), ou **"só ver"** (não muda nada).

## 5. Governança

- Backup pré-mudança criado no servidor (Regra "nenhum arquivo pode se perder").
- Não mexi em produção/WordPress sem confirmação (madrugada, sem resposta).
- Nodo: registrar em `CEREBRO_NODE_ARQUITETURA.md` ou nodo de diretrizes de coletores.
- Log: `CEREBRO_NODE_ATUALIZACOES.md`.

— ZCode (GLM-5.2), 2026-08-08 ~01:55 BRT
