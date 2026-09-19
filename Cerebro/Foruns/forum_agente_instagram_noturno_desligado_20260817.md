# 📸 Fórum — Agente Noturno Instagram (cards) DESLIGADO

**Data:** 2026-08-17 · **Autor:** ZCode/DeepSeek (ordem do Miguel) · **Memória técnica pareada:** `Memorias/memoria_agente_instagram_noturno_desligado_20260817.md`

## A ordem do Miguel

"O agente instagram ainda está publicando. Pode desligar ele por favor. Ele publicou sobre eua e vila euclides."

## O que era

Agente noturno de cards para o feed do Instagram do O Cafezinho (pipeline `scratch/card_v2/`): todo dia às **22:00 BRT** escolhia a matéria mais lida/principal do dia no WP (`controle.ocafezinho.com`), gerava legenda via LLM (roteador SuperLuxo), criava card v2.7 (logo vazada + chapéu "GOVERNO"), subia a imagem para a biblioteca WP e publicava via Graph API (IG Business).

## Decisão

- **DESLIGADO em 17/08/2026 por ordem do Miguel.** Linha do crontab local comentada, com backup do crontab inteiro em `scratch/card_v2/crontab_backup_pre_instagram_off_20260817.txt` (116 linhas).
- NYC (`agente_instagram.py` e `gerenciador_fila_redes.py`): já estavam **pausados desde 20/07/2026** (linhas comentadas `PAUSADO_CLAUDE_MIGUEL_20260720_INSTAGRAM` / `PAUSADO_CODEX_MIGUEL_20260720_PIPELINE_INSTAGRAM`) — nada a fazer.
- Verificações pós-desligamento: nenhum processo Instagram ativo; nenhuma automação ZCode de Instagram; `crontab -l | grep instagram` só mostra o comentário de desativação.

## Como religar (se o Miguel quiser no futuro)

Restaurar a linha no crontab local (linha original está no backup):

```
0 22 * * * /usr/bin/python3 "/home/migueldorosario/Downloads/Antigravity Google/scratch/card_v2/agente_instagram_cron.py" >> "/home/migueldorosario/Downloads/Antigravity Google/scratch/card_v2/cron_night.log" 2>&1
```

## Estado

- ✅ Cron local desativado e verificado.
- ✅ Registrado no monitor de trabalho + nodo AGENTES + ATUALIZACOES.
- ⏳ Nada pendente para o Miguel.
