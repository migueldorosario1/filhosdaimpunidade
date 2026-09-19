# Memória — Ronda ZM VIGIA 1/1h (criação, 03/09/2026 ~16h BRT)

**Autor:** ZM (ZCode/GLM-5.3, Dell) · **Fórum-irmão:** `Foruns/forum_ronda_zm_vigia_1h_20260903.md`

## Missão (ordem do Miguel ~15:5x, quase literal)

Ronda de 1 em 1 hora para: ajudar o sistema a monitorar; ler as mensagens das pontes (Laura E Telegram); responder dúvidas; vigiar o sistema (está em pé?); ajudar o Clodo de Lara (CL) a corrigir; corrigir diretamente coisa SÉRIA que a ronda vir.

## O que foi feito

1. **Automação ZCode `automation-2a8954e2-f0c4-44bb-9e72-91fc9ca87225`** — cron `12 * * * *` (âncora :12), ATIVA, 1ª execução 03/09 16:12 BRT. Prompt completo autocontido (P0 anti-colisão → P1 pontes → P2 sistema em pé → P3 boletim → P4 correção de coisa séria → P5 registro/Telegram + limites absolutos).
2. Tema Duplo no Cérebro: fórum + esta memória. Catalogação: `CEREBRO_NODE_AGENTES.md` (seção ronda, linhagem) + `CEREBRO_NODE_ATUALIZACOES.md` + linha no MONITORAMENTO.
3. Publicação no repo `~/cerebro-miguel` (commit seletivo + `PONTE_AGENTE=ZM scripts/ponte_push.sh`).

## Design

- **Ronda de agente** (sessão ZCode real por disparo), não de script: pode investigar com SSH/curl/logs e CORRIGIR — era o pedido central ("corrigir diretamente alguma coisa séria").
- **Silêncio por padrão**: Telegram só com novidade real (respeita a grade enxuta de 03/09, ~11 msgs/dia); ronda limpa = 1 linha no fórum, sem commit.
- **Poder de correção limitado**: coisa séria (serviço morto, site caído, robô em loop, bug público) com prova→backup→mínima→prova→registro; NUNCA post publicado (CL/CM), nunca sem backup, §131, sem comando destrutivo.
- **Anti-colisão**: P0 lê o MONITORAMENTO antes de tocar; área ocupada por outra sessão = avisa e não pisa (§112).

## Armadilhas confirmadas na criação (para a ronda e futuras sessões)

- **CCTV NÃO roda no Dell**: porta 8084 é no TENCENT. URL pública `http://43.156.151.165/v6/` (rota SEM /v6 = 404; https no mesmo IP serve o app do Moka — não confundir). Fallback interno: `ssh tencent curl http://127.0.0.1:8084/v6/`.
- **`ponte_cafezinho.py --help` TRAVA** (o script conecta ao Telegram no boot — só `--send` é rápido). Para saber opções, ler o código.
- **Falas do Miguel no Telegram**: `$REPO/cerebro/Foruns/ponte_laura_completa/escuta/conversa_48h.jsonl` (rotativo 48h; entradas individuais `entrada_<id>.json` na mesma pasta; NÃO existe cópia no Cérebro canônico — só no repo).
- **Arquivos gigantes**: `de_dell.md` >4MB, `de_laura.md` >1,5MB — sempre tail/grep; append via heredoc.
- **Escrita direta no checkout do repo** (`~/cerebro-miguel`) + `ponte_push.sh` (rebase autostash, push duplo GitHub+GDrive) — o sync de 15min já comeu blocos ZM 12×.
- **Âncora :12** escolhida para não colidir com pull :00/:15/:30/:45, push :07/:22/:37/:52, AGY :35, GL :37, GM :50.

## Rollback

`CronDelete automation-2a8954e2-f0c4-44bb-9e72-91fc9ca87225` (1 comando — só o Miguel ou sessão expressamente autorizada; a própria ronda tem PROIBIDO mexer em automações).

## Estado

- **No ar** desde 03/09 ~16h. **O que falta:** 1ª execução (16:12) validar as pernas ao vivo. **Preciso do Miguel:** nada.
