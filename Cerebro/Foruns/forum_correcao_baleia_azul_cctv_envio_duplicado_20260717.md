# Fórum de Correção do Baleia Azul, CCTV e Envio Duplicado

Data 17/07/2026

Responsável Codex, editor interino do Baleia Azul e mantenedor interino do CCTV

## Incidente

Miguel recebeu às 10h um email datado de 17/07 que apontava para uma página com a edição #8, de 15/07.

## Causas confirmadas

1. O watchdog remoto no Tencent executava `/root/scripts/enviar_baleia_azul.sh` às 10h.
2. Esse script antigo enviava o endereço estático `/painel/baleia_azul.html`.
3. O HTML estático estava congelado na edição #8.
4. O CCTV dinâmico também estava na edição #8 porque a edição local mais recente não havia sido sincronizada com a base remota.
5. O token do bot Telegram estava gravado diretamente nos scripts local e remoto.

## Correções aplicadas

- Preservados scripts, painel, HTML e crontabs antes das mudanças.
- Retirado o disparo das 10h do watchdog remoto.
- Watchdog remoto reiniciado e mantido para suas outras funções.
- Emissor remoto antigo substituído por stub inativo.
- Script local `enviar_baleia_azul.sh` convertido em compatibilidade para o `v2`.
- Script local `v2` passou a sincronizar a edição mais recente antes do envio.
- O envio é interrompido se a sincronização falhar, evitando link para edição velha.
- Token Telegram removido dos scripts.
- Telegram passa a depender de `TELEGRAM_BOT_TOKEN` no ambiente.
- Resposta integral da API Telegram deixou de ser gravada no log.
- Edição extraordinária #11 sincronizada com o CCTV.
- Página estática substituída por encaminhamento para `/v5/baleia`.
- Backups contendo o token antigo foram sanitizados e protegidos com permissão restrita.

## Estado observado após a correção

- `/v5/baleia` mostra a edição extraordinária #11.
- Watchdog remoto está ativo sem disparo do Baleia Azul.
- Painel CCTV remoto continua ativo na porta 8082.
- Cron local permanece como emissor canônico às 8h e 18h.
- Telegram fica suspenso até a rotação do token.

## Pendência humana de segurança

O token exposto deve ser revogado e substituído no BotFather. Depois da rotação, o novo valor deve ser armazenado fora dos scripts e carregado como `TELEGRAM_BOT_TOKEN`.

## Rollback

Backup local

`Cerebro/Backups/baleia_cctv_fix_20260717_1050/`

Backup remoto

`/home/ubuntu/backups/baleia_cctv_fix_20260717_1050/`

Os backups dos emissores foram deliberadamente sanitizados. O token comprometido não faz parte do rollback.

Para rollback seguro, restaurar painel, HTML, watchdog e crontab individualmente. Não restaurar o emissor remoto antigo nem credenciais hardcoded.

## Comunicação

Este fórum deve ser consultado antes de qualquer mudança no Baleia Azul, CCTV, cron, email ou Telegram.

