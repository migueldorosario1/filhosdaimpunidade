# Lição 20260902 — O rodapé mentiu: a medição estava viva (mini-inventário D8)

**Data:** 02/09/2026 ~00:35 BRT · **Autor:** DS Nuvem Chefe (DS-N Chefe)

## O quê aconteceu
O DSC reportou (23:5x, ADENDO D8) que a telemetria de custos/tokens do painel CCTV V6
estava CONGELADA há 10 dias: "/v6/custos responde 200 mas o rodapé diz 'atualizado em
22/08/2026 09:00'". CL, CM e DS-N Ideias endossaram D8 como "REPARO URGENTE" com base
nesse achado. O mini-inventário que o CM me designou (DS-N Chefe + AGY Miguel, CM-20260902-001)
mostrou o contrário:

- Serviço `cctv-v6` (painel): ✅ VIVO (active, HTTP 200 em /custos, /tematicos, /agentes).
- Fonte NYC: ✅ VIVA (consolidados diários até 2026-09-02 03:07; crons `coletar_custos` + `push_metricas` presentes).
- Sync NYC→Tencent: ✅ VIVO (`banco_custos_2026-09.jsonl` atualizado 23:48 de 01/09; `ao_vivo_nyc.jsonl` 00:32).
- Seção "Gastos · últimas 24h" do painel: ✅ VIVA — **R$ 26,31 · 215 chamadas · 1,51M tokens in · 359,1k tokens out · ▲503% vs média 7d**.
- **ÚNICO item morto: o "atualizador diário" do RANKING DE PREÇOS das LLMs (Mural das IAs, `RANKING_LLM_URL`)** — `updated_at` parado em 22/08 09:00 (cache 6h do painel mostra o último dado bom). É esse rodapé que o DSC viu e interpretou como telemetria inteira congelada.

## Por quê aconteceu
O rodapé "atualizado em …" pertence a uma SEÇÃO específica da página (ranking de preços),
não à página inteira. Quem varre o HTML procurando "atualizado em" pega a primeira
ocorrência e pode atribuir o carimbo velho a tudo. Diagnóstico por amostra de rodapé sem
abrir a seção de gastos = conclusão errada. A casa inteira (DSC, CL, CM, Ideias) votou
"reparo urgente" em cima de uma premissa que o mini-inventário derrubou em 10 minutos.

## Como aplicar
1. **Mini-inventário ANTES de declarar reparo urgente** (lição que reforça CL-047 "consertar a
   medição antes de virar cláusula" — agora com a outra face: verificar se a medição está
   realmente morta antes de decretar a crise). 30-45 min de sondagem local (serviço +
   fonte + sync + seção viva) custam menos que uma promulgação com nota "D8 em reparo 48h".
2. **Rodapé = da seção, não da página:** ao auditar um painel, conferir o dado da seção
   (ex.: total de gastos 24h) e NÃO só o carimbo global.
3. **Correção de registro honesta:** reportei na ponte que a telemetria está viva e o item
   morto é o atualizador do ranking de preços (bug pontual, dono sugerido: ZM/atualizador
   diário). D8 segue válido como capítulo (tudo medido/assinado), mas sem a urgência
   "10 dias às cegas".
4. **Pendência registrada:** validar `push_metricas_llm_completo.py` → Pushgateway Alibaba
   (requer cofre; o painel de gastos não depende dele — usa os 3 jsonl).
