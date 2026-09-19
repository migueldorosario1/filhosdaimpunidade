# 🧠 Memória — DSC-013: verificação, integração e PONTE DORMIDA diária (R2+B2+Telegram) — 03/09/2026

> Executor: ZCode (GLM-5.3, DSH us65 — sessão direta com o Miguel).
> Ordens: 03/09 ~15h0x ("confere as credenciais, vê se resolveu o seu lado") e ~16h1x ("vai" — ligar a fiação).
> Contexto: Miguel destrancou o pacote gpg no Dell às 15:03 (senha oculta via `~/desbloqueia_dsc.sh`, nunca em chat — ZCode Dell registrou); entrega em `us65:/root/dsc_credenciais/` (3 arquivos, 600).

## O que foi feito

1. **Verificação das 5 credenciais** (sem imprimir valores):
   - gdrive: `rclone about` OK — 30 TiB totais, 29,2 TiB livres (NOTA: client_id compartilhado do rclone será aposentado pela Google durante 2026 — um dia pedirá client_id próprio).
   - Telegram ponte: `getMe` OK — bot **@pontecafezinhobot**.
   - R2: 6 baldes listados + teste de escrita/leitura/apaga em `ponte-mirror` OK.
   - B2 failover: balde `failover-cafezinho1` + escrita/apaga OK. B2 arquivo: baldes de arquivo listados OK.
2. **Integração** (a parte que faltava): remotos `r2:`, `b2:`, `b2_arquivo:` gravados no `rclone.conf` **padrão** + `TELEGRAM_TOKEN_PONTE` no `/root/.env.unificado` (backups `.bak_pre_dsc013_*` de ambos; aprovação do Miguel no sandbox DSH).
3. **Ponte dormida diária** — `scripts/ponte_dormida_dsc013.sh`:
   - Artefatos: `git bundle --all` (história completa, 128M) + `tar.gz` do worktree sem `.git` (192M) + `manifest-AAAAMMDD.json` (HEAD, sha8, tamanhos).
   - Upload para `r2:ponte-mirror/us65/cerebro/` e `b2:failover-cafezinho1/us65/cerebro/`; verificação pós-upload (`lsf` ≥ 3 arquivos do dia); retenção 30 dias.
   - Sinal de vida no Telegram: prefere `@pontecafezinhobot` (se `PONTE_CHAT_ID` existir), fallback `@dscelular_bot` (canal comprovado dos alertas da casa). Sem segredo no texto.
   - Cron: `10 4 * * *` (04:10 BRT diário) — instalado e conferido no crontab root.

## Provas

- 1ª rodada 16:21: `r2:OK(3 arquivos) b2:OK(3 arquivos)`; **bytes idênticos nos dois baldes** (bundle 134.139.787 · tar 201.022.861); manifesto lido de volta do R2 (`git_head 91220cd0e`).
- Sinais Telegram: message_id **160** (⚠️ 2 falhas — 1ª tentativa honesta) e **161** (✅ sucesso).
- Log: `scratch/ponte_dormida/run_20260903.log`.

## Lições

1. **Bug próprio na 1ª rodada**: path montado com dois-pontos duplicado (`r2:ponte-mirror:us65/...` em vez de `r2:ponte-mirror/us65/...`) → S3 respondeu `InvalidBucketName` e o B2 respondeu `you must use bucket(s) [{"a2cb..."} "failover-cafezinho1"]` — o que PROVOU que a chave B2 tem escopo correto de balde. Corrigido nos 4 pontos do script.
2. **Sinal de vida falando a verdade na 1ª tentativa** (⚠️ message_id 160) avisou o Miguel em tempo real do erro — padrão a manter: sinal honesto, não só de sucesso.
3. `@pontecafezinhobot` começou SEM conversa com o Miguel (`getUpdates` vazio) — o sinal saía pelo canal comprovado. **RESOLVIDO 03/09 ~17h1x:** o Miguel mandou "Oi DSC!" ao bot → `PONTE_CHAT_ID=1894890759` gravado no `.env.unificado` (backup `.bak_pre_pontechat_*`, aprovação Miguel) → mensagem de inauguração entregue pelo canal dedicado (**message_id 1460, ok:true**). O script migra sozinho (prefere ponte quando PONTE_CHAT_ID existe).

## Próximo

- Conferir a 1ª rodada automática de 04/09 04:10 — o sinal agora chega pelo CANAL DEDICADO @pontecafezinhobot (3 arquivos novos por destino).
— ZCode (GLM-5.3, DSH us65 — sessão direta Miguel) · 20260903 16:4x BRT
