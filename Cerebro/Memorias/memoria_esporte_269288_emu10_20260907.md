# MEMÓRIA TÉCNICA — Caso 269288 (US Open na vertical economia, puxado do slot) + EMU-10

**Data:** 07/09/2026 00:1x→00:2x BRT · **Agente:** ZCode (Qwen3.8-Max, Dell) · **Fórum-irmão:** `Foruns/forum_esporte_269288_emu10_20260907.md`

## Forense (provas)

- `wp post get 269288`: author 5470; status future post_date 07/09 00:30; post_modified 06/09 23:16:51; título velho «Alcaraz vence Tommy Paul por 3 sets a 0 e avança às quartas do US Open».
- Metas: `zizi_job_id=v41_economia_a4f926b85438` (**vertical economia!**), `_v4_versao=4.1`, origem REST 22:36:07 python-requests; `_v41_fc` ok=true (placar 6-4/6-3/6-4 4ª rodada 06/09, Arthur Ashe); `_cafezinho_txt_check.r1` = **qwen-max+search** ok=false INCERTO (escada de busca); `_cafezinho_txt_isenta` + `cl_manual` = **CL-20260906-032** (23:1x, fact-check próprio + capa APROVADA + "agendado para a madrugada de 07/09"); `_cafezinho_img_check` APROVADA (CL visão própria).
- Ciclo NYC `/root/v4_labs/dados/v41_ciclo/20260906_2235.json`: `vertical=economia`, pauta «Alcaraz supera pressão contra da torcida e Tommy Paul e está nas quartas do US O», `curadoria_estado=tese_dinamica_aprovada`, `redator_out={ok:true, id:269288, title:"Alcaraz vence Tommy Paul e avança às quartas do US Open", content_chars:1871, model:"gpt-5.6-sol"}`, status `rascunho_v41_curto`.
- Leitura: a curadoria de tese dinâmica NÃO filtra pauta por vertical (tênis entrou na economia); a isenção manual (CL) cobre factual, não editorial; não existe gate de tradução de nome de torneio.

## Ação (00:1x)

- Backup: `Cerebro/Backups/posts_editados/269288_pre_fix_20260907.md`.
- `wp post update 269288 --post_status=draft --post_title="Alcaraz vence norte-americano e avança às quartas do Aberto dos EUA" --post_name="alcaraz-vence-norte-americano-e-avanca-as-quartas-do-aberto-dos-eua"` → prova: status draft, 67 chars.
- Ponte `Foruns/ponte_laura_completa/de_dell.md` bloco 13: slot 00:30 aberto por ordem do dono (grade/colchão = CL/DS); isenção não cobre editorial.

## EMU-10 — onde foi gravada

- `Estilo/MANUAL_DE_ESTILO_UNIFICADO.md`: bullet novo em B1 "Lições" (esporte: Brasil primeiro/futebol, europeu e brasileiros no exterior depois, resto só c/ protagonista BR ou impacto global; torneio EUA sem BR não abre slot; torneio traduzido no título; esporte nunca em vertical errada) + entrada EMU-10 no registro (backup .bak_pre_emu9/10).
- `Estilo/MANUAL_DE_ESCRITA_PORTAL.md` seção 8: bullet espelho (briefing do redator V4.1, v41_ciclo.py:587).
- Espelho NYC md5 **97099f345ff6efd4235fb13317001c03** (idêntico; backup .bak_pre_emu10_20260907 lá).
- `CEREBRO_NODE_ESTILO.md` + `CEREBRO_NODE_ATUALIZACOES.md` + monitor ✅.

## Pendências (aguardam "vai" do Miguel)

1. Gate de curadoria no código v41_ciclo: bloquear pauta de esporte fora da vertical de esporte + filtro de prioridade Brasil/Europa na tese dinâmica.
2. Tradução mecânica de nome de torneio estrangeiro no título (pós-redator).
3. Destino do draft 269288 (guardar traduzido ou lixeira) — decisão do dono.

## Padrão dos 3 casos da noite (269169, 269279, 269288)

Mesma anatomia: (a) esteira V4.1 nasce com defeito de FORMA/EDITORIAL que os gates factuais não pegam (fc/img/txt cobrem FATO, não forma nem pauta); (b) revisão manual da CL isenta/agenda sem passar pelo checklist de estilo (regras 1/8/9/10); (c) auditor de títulos NYC (07:37) não cobre status future nem slots da manhã. Curas de código propostas nos 3 casos aguardam "vai"; as regras EMU-9/EMU-10 já vivem nos manuais e no briefing do redator.
