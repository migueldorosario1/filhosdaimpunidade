---
name: feedback-teto-fila-12h-cadencia-valvula-nohome-20260814
description: "SUPERSEDE regra antiga \"distribuir madrugada+dia seguinte 60-90min\". Nova regra 14/08/2026 12:50 BRT (Miguel via ZCode): TETO 12h à frente + cadência 30min gerais / 1h Nacional+Regional + madrugada LIBERADA + válvula NO-HOME (publish agora + cat 20699) quando fila estourar teto. Cleaner devolve à home 3h depois."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

**SUPERSEDE:** [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]] a partir de 14/08/2026 12:50 BRT (regra antiga Miguel 12/08 23:15 "distribuir madrugada+dia seguinte 60-90min").

## Nova regra vigente

**Antes de agendar QUALQUER draft:**

1. **Ler fila REAL do WP** (não estado em memória de ciclo anterior):
   ```
   wp post list --post_status=future --fields=ID,post_date --orderby=date --order=DESC | head -3
   ```
2. **Se `final_da_fila + 30min < NOW + 12h`** → agendar normalmente (cadência: 30min gerais / 1h Nacional+Regional)
3. **Se `final_da_fila >= NOW + 12h`** → NÃO empurrar mais pra frente. Aplicar **VÁLVULA NO-HOME**:
   ```php
   wp_update_post([
     "ID" => $id,
     "post_status" => "publish",
     "post_date" => current_time("mysql"),
     "post_date_gmt" => get_gmt_from_date(current_time("mysql")),
     "edit_date" => true,
   ]);
   $cats = wp_get_post_categories($id);
   wp_set_post_categories($id, array_merge($cats, [20699]), false);
   ```
   Cleaner horário devolve o post à home 3h depois (rotação automática). Post no-home aparece em Linha do Tempo + Recentes.

## Cadência

- **Geral (geo/tec/economia/cultura/meio-amb/esporte/saúde):** 30min entre posts
- **Nacional (cat 22) + Regionais:** 1h entre posts (mais grosso porque tema quente aguenta mais tempo no topo)
- **Madrugada (00-06 BRT):** LIBERADA. Pode agendar/publicar. Cadência mantida.
- **24/7 sem gap forçado**

## Por que a mudança

Miguel 14/08 12:50: "ainda tem muito texto agendado para o dia 16, não faz sentido agendar com tanta antecedência... joga no home, mas não joga tanto para frente assim". Backlog atual: 87 pending do V4. Produção ~33/dia vs consumo ~48/dia → backlog drena sozinho na cadência 30min; nunca precisa empurrar >12h.

Meu erro 14/08 12:32-16:02: continuei aplicando regra antiga (agendei 265780/265789/265791/265794/265797/265803/265808 pra 16/08 05:20→13:20). ZCode teve que puxar os 7 pra caber no teto. Motivo do erro: Miguel deixou diretiva 12:55/13:10 na `inbox_trindade/claude.md` velha (que eu tinha abandonado — bug já registrado em [[feedback-migracao-canal-fechar-loop-no-antigo]]).

## Correção estrutural derivada

**A partir de 14/08 16:38:** todo ciclo Vigília DEVE ler ambos os canais antes de agir:
- `Cerebro/Foruns/ponte_trindade_daemon/fila_para_claude.md` (canal ativo)
- `Cerebro/Foruns/inbox_trindade/claude.md` (canal antigo — Miguel ainda usa)

Se aparecer diretiva nova em qualquer um, ABSORVER antes de continuar ciclo. Consequência de ignorar: 4h de trabalho retrabalhado + ZCode teve que corrigir manualmente.

## Como aplicar na revisão editorial

- Cabeçalho de cada Slot A/B: rodar `wp post list --post_status=future | head -3` como primeira coisa após pipe
- Comparar último `post_date` com `NOW + 12h`
- Escolher entre "agendar" ou "NO-HOME publish"
- Nunca chutar `NOW + 80min * N` sem verificar teto

Relacionados: [[feedback-migracao-canal-fechar-loop-no-antigo]], [[feedback-no-home-remover-se-tem-imagem-real]], [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]]
