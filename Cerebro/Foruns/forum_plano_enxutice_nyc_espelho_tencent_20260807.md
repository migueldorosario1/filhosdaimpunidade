# Fórum — Plano de Enxutice NYC + Espelho/Failover Tencent + Telemetria no Baleia Azul

> Par técnico (log completo): [memorias_plano_enxutice_nyc_espelho_tencent_20260807.md](../Memorias/memorias_plano_enxutice_nyc_espelho_tencent_20260807.md)
> Regra mãe: §115 (retenção universal) + "não jogar nada fora" (Miguel, 07/08)
> Autor: ZCode/Qwen 3.8 · 2026-08-07

## Origem
Ordens por voz do Miguel (07/08 ~11:40 BRT): plano para deixar os sites leves; agente automático levando o que não é funcional para o Backblaze (Cloudflare como opção futura); servidor de Nova York enxuto; fim de semana: plano do espelho Tencent completo (failover — temáticos + canônico); no Baleia Azul: percentual de enchimento dos discos (semana vs semana) + bloco dos temáticos; e uma revisão dos temáticos (quebrados × autorizados).

## Decisões registradas
1. **NYC está em 79% (38G/48G).** O peso real NÃO são os bancos do pipeline (limpos hoje): é `/tmp` 7,4G (exports esquecidos ~5,6G), **venv com 4,3G de CUDA sem GPU**, dumps remotos 3,7G (gsn/cicero), backups+legacy 2,2G, cache pip ~1,5G.
2. **Plano em fases**: A) ganho imediato **~14G** (dry-run já feito: pip cache 4,2G · exports /tmp 5,6G ⚠️ recentes/05-08, confirmar redundância · gsn_remote 1,9G pipeline desligado · cicero_remote SÓ o subdir `root/` 226M — **cicero_remote é VIVO, tem 2 crons diárias** · backups/legacy 2,2G · puppeteer 627M; arquivo no B2 antes de remover — rito "não jogar nada fora"); B) dieta do venv ~6G (torch→CPU, com teste e aprovação); C) **agente automático diário** (`storage_janitor`, mesmo rito do arquivador V4: dry-run padrão, `--execute` exige autorização, B2 + manifest + recibo no ledger); D) Baleia Azul ganha seções 💾 Discos (semana vs semana) e 🗞️ Temáticos; E) fim de semana: espelho/failover Tencent completo.
3. **Cloudflare** fica como opção futura para servir mídia; arquivamento sai primeiro no B2 (credenciais e espelhos já existem — Cofre).
4. **Baleia Azul**: o assento editor é ZCode/Kimi K3 (desde hoje 10:05). Esta sessão entrega o **coletor de dados** (arquivo novo) + contrato; a inclusão no corpo do e-mail é do assento editor (§112 — não pisar no trabalho de outra sessão; há bug ativo de envio de e-mail hoje).
5. **Revisão dos temáticos**: 5/8 domínios no ar (discoverbrazil, mapario, aiatolah, globalsouth, railpost); **3/8 sem DNS nenhum: ceara.com.br, mundotrilhos.com.br, riocarta.com.br**; aiatolah no ar mas parado há 17 dias (Vigília/Kimi K3 no caso); lista formal de "autorizados" não existe no Cérebro — pendência com Miguel.

## Estado
- ✅ Plano escrito (Tema Duplo), censo medido, revisão dos temáticos entregue.
- ✅ **Dry-run Fase A feito** (lista exata + correções: cicero_remote vivo, exports /tmp de 05/08).
- ✅ **Coletor Baleia implementado e testado com dados reais** (`scratch/coletar_disco_tematicos_baleia.py` + helper NYC `/root/baleia_coleta_tematicos.py`): gera `disco_tematicos_AAAAMMDD.md/.json` + histórico jsonl (teto 70 linhas, §115). 1ª saída real: NYC 79% (37G/47G), Tencent 64% (72G/118G), 3 temáticos + regionais + status da limpeza 04:35. Comparação semanal aparece a partir da próxima semana (histórico começou hoje). Integração no emissor = handoff ao assento editor (ZCode/Kimi K3).
- ⏳ Fase A: aguarda "pode aplicar" do Miguel.
- ⏳ Fase E: fim de semana 08–09/08.

## Pendências / decisões do Miguel
- "Pode aplicar" da Fase A (lista exata virá antes).
- Lista formal dos sites temáticos autorizados (quais domínios devem existir/DNS a apontar).
- Fase B (torch CPU) quando chegar lá.
