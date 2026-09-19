# Lição 2026-09-05 — Boletim no repo ≠ boletim no painel /v6/baleia (o painel congelou em 01/09)

## O quê
O Miguel mandou no Telegram às 16:15: "http://43.156.151.165/v6/baleia — Baleia Azul atrasada". O painel /v6/baleia mostrava como "edição mais recente" o boletim de 01/09 (tarde) — 8 edições (02/09 manhã/tarde → 05/09 manhã) produzidas e enviadas ao Telegram, mas invisíveis no painel.

## Por quê
O painel_cctv_v6.py lê os boletins de BASE_DIR = "/home/ubuntu/cafezinho/Projeto Cafezinho Agentes/" (glob "boletim_baleia_azul_*.md", linha 1204). Essa pasta é herança do fluxo antigo (boletins consolidados até 01/09). Quando a editoria da Baleia passou ao DS-N Chefe (01/09), o ritual passou a salvar as edições SOMENTE no repo git (cerebro/Foruns/ponte_laura_completa/baleia_azul/boletim_baleia_azul_AAAAMMDD_manha|tarde.md) + Telegram. Ninguém sincronizou a pasta do painel — o painel é uma segunda vitrine que depende de um passo de cópia que não existia no fluxo novo. O dono enxergou "atraso" onde havia só painel desatualizado.

## Como aplicar
1. Toda edição da Baleia Azul precisa chegar em 3 lugares: (a) arquivo no repo (canônico, commit+push), (b) Telegram do Miguel (prova = message_id), (c) pasta que o painel /v6/baleia lê — /home/ubuntu/cafezinho/Projeto Cafezinho Agentes/ (mesmo nome de arquivo; escrita fora do workspace do sandbox do Chefe — executar via ZM/dono do painel ou cron de sync, não pela ronda).
2. Correção estrutural recomendada ao ZM (dono do painel): ou o painel passa a ler do repo, ou um sync (padrão sync_reforma_status.py: fetch origin + instala no destino) copia os boletins do repo para o BASE_DIR — o fluxo da Baleia não pode depender de cópia manual.
3. Quando o dono apontar "atraso" de uma vitrine, conferir a FONTE da vitrine (de onde a página lê) antes de aceitar que a produção atrasou — a produção tem prova própria (arquivo no repo + message_id no Telegram).
4. Verificar o título do <title> da página e o "Fonte:" do rodapé do card para identificar o arquivo-fonte real.
