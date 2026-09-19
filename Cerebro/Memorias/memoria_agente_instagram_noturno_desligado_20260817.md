# 📸 Memória Técnica — Agente Noturno Instagram desligado (2026-08-17)

**Data:** 2026-08-17 · **Autor:** ZCode/DeepSeek · **Fórum pareado:** `Foruns/forum_agente_instagram_noturno_desligado_20260817.md`

## 1. O que foi feito (passo a passo)

1. Localizado o disparador: crontab local, linha `0 22 * * * /usr/bin/python3 "…/scratch/card_v2/agente_instagram_cron.py"` (bloco "AGENTE NOTURNO INSTAGRAM — 1 post/noite da matéria principal do dia").
2. Backup do crontab inteiro: `scratch/card_v2/crontab_backup_pre_instagram_off_20260817.txt` (116 linhas).
3. Linha removida e substituída por comentário de desativação auditável (com caminho do backup).
4. Verificações: `crontab -l | grep -in instagram` → só o comentário de desativação; `ps aux | grep instagram` → 0 processos; systemd → nada; automações ZCode (CronList) → nenhuma de Instagram.
5. Servidores: NYC tem `agente_instagram.py` e `gerenciador_fila_redes.py` já **PAUSADOS desde 20/07/2026**; china e cafezinho-wp sem nenhum cron de Instagram.

## 2. Provas — posts citados pelo Miguel = últimas execuções do cron

| Data/hora | Post WP | Título | Permalink IG |
|---|---|---|---|
| 15/08/2026 22:03 | 265915 | Polícia Federal dos EUA amplia cooperação com China e Rússia | https://www.instagram.com/p/DcFPtQ_F1Il/ |
| 16/08/2026 22:03 | 266116 | Na Vila Euclides, Lula liga a campanha ao trabalho e à soberania | https://www.instagram.com/p/DcH0eXqANkQ/ |

Ambas as execuções constam do `cron_night.log` com `status: success`.

## 3. Observações técnicas (para o futuro, se religar)

- Pipeline: `scratch/card_v2/agente_instagram_cron.py` → `publicar_instagram_demand_v2.py` → Graph API IG Business (IG ID 17841400848520269). Card sobe para a biblioteca WP de `controle.ocafezinho.com` antes de publicar.
- Trava anti-duplicata por similaridade de título (limiar 0.51) — ex.: em 16/08 travou "Justiça autoriza busca contra suspeito de ameaçar Flávio Bolsonaro" vs "Mais uma pesquisa ruim para Flávio Bolsonaro".
- Gotcha visto no log de 16/08: roteador LLM tentou `gpt-5-chat-latest` → **404 deprecado** → caiu para `claude-sonnet-4-6` (funcionou). Se o agente voltar, atualizar a sequência de ataque do roteador.
- `historico_instagram.json` (histórico de publicações) e os cards `.jpg` foram preservados — nada apagado.
- Arquivos intactos em `scratch/card_v2/`; apenas a linha do cron foi desativada.
