# Fórum — Baleia Azul: Gabriel Barbosa entra nos destinatários do e-mail (06/08/2026)

**Data:** 2026-08-06 ~19:00 BRT · **Executante:** ZCode (Kimi K3), chat direto · **Ordem:** Miguel ("o Baleia Azul tem que ir pra ele também — Gabriel Barbosa")

## Decisão

O Baleia Azul (boletim diário por e-mail, cron 8h/18h) passa a ser enviado também ao **Gabriel Barbosa**, nos dois endereços registrados no Cérebro:

- `gabrielbarbosa9001@gmail.com`
- `gabrielbarbosa@ocafezinho.com`

Miguel (`migueldorosario@gmail.com`) segue como destinatário. A lista de 3 já era a **ordem permanente registrada em 21/07** (`Foruns/ponto_retomada_codex_operacao_20260721_1000.md`: "destinatários permanentes informados por Miguel"), mas nunca tinha sido aplicada ao emissor v2 — o e-mail ia só para o Miguel desde pelo menos 10/07 (confirmado em todos os backups do script).

## O que foi feito

1. `scratch/enviar_baleia_azul_v2.sh`: variável `DESTINATARIOS` com os 3 endereços (override de teste `BALEIA_DESTINATARIOS`). Backup `.bak_pre_destinatarios_gabriel_20260806`. Sintaxe OK.
2. Cópia da edição de hoje (06/08, "Boa tarde") enviada na hora ao Gabriel (2 endereços) pela mesma rota Tencent `mail` — sem re-disparar Telegram nem scp.
3. A partir do próximo envio agendado (07/08 08:00) o Gabriel recebe automaticamente.

## Achado lateral (registrado em BUGS_ATIVOS)

O Telegram do Baleia **falhou às 18:00 de hoje** (erro 400): o corpo novo ficou com ~4.470 caracteres, acima do limite de 4.096 do Telegram. O e-mail não é afetado. Bug `BUG-20260806-BALEIA-TELEGRAM-400`.

## Fontes

- Emissor: `scratch/enviar_baleia_azul_v2.sh` (linha do envio, via Tencent 43.156.151.165)
- Ordem original 21/07: `Foruns/ponto_retomada_codex_operacao_20260721_1000.md`
- Memória técnica: `Memorias/memoria_baleia_azul_destinatarios_gabriel_20260806.md`
