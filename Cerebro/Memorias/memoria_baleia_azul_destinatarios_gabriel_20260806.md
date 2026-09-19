# Memória técnica — Baleia Azul: inclusão do Gabriel Barbosa nos destinatários (06/08/2026)

**Data:** 2026-08-06 ~19:00 BRT · **Sessão:** ZCode (Kimi K3), chat direto, workspace ZCodeProject
**Arquivos tocados:** `scratch/enviar_baleia_azul_v2.sh` (editado), `/tmp/baleia_azul_envios.log` (linha de recibo), Cérebro (nodo Baleia, fórum, ATUALIZACOES, BUGS_ATIVOS, monitor)

## Contexto

Miguel perguntou no chat se o Baleia Azul estava indo por e-mail também para o Gabriel Barbosa ("tem e-mail dele aí"). Verificação:

1. **Script canônico** (`scratch/enviar_baleia_azul_v2.sh`, linha do `mail` via Tencent): enviava **apenas** para `migueldorosario@gmail.com`.
2. **Todos os backups do script** (`pre_nyc_20260710`, `pre_scp_fix_20260719`, `pre_melhorias_20260806`) tinham o mesmo destinatário único — o Gabriel **nunca** esteve na lista do emissor v2 local.
3. **Cérebro tinha a ordem permanente** desde 21/07 (`Foruns/ponto_retomada_codex_operacao_20260721_1000.md`): "destinatários permanentes informados por Miguel são `migueldorosario@gmail.com`, `gabrielbarbosa9001@gmail.com` e `gabrielbarbosa@ocafezinho.com`". A lista existia também em versões antigas (inbox Kimi, backup 24/07: "Destinatários hardcoded" com os 3; variante Python com `To: miguel,gabriel`). **Lacuna:** na reescrita/localização do emissor (v2, a partir de 10/07), a lista ficou para trás.
4. **Log `/tmp/baleia_azul_envios.log`:** envios de 06/08 às 08:00 e 18:00 registrados como "enviada" (e-mail OK; Telegram falhou às 18:00 — ver bug abaixo).

## Mudança aplicada

```bash
# Antes (linha única):
echo "$CORPO" | ssh ... "mail -s '$ASSUNTO' migueldorosario@gmail.com" 2>>"$LOG"

# Depois:
DESTINATARIOS="${BALEIA_DESTINATARIOS:-migueldorosario@gmail.com gabrielbarbosa9001@gmail.com gabrielbarbosa@ocafezinho.com}"
echo "$CORPO" | ssh ... "mail -s '$ASSUNTO' $DESTINATARIOS" 2>>"$LOG"
```

- Backup: `scratch/enviar_baleia_azul_v2.sh.bak_pre_destinatarios_gabriel_20260806`
- Validação: `bash -n` OK. `mail` (heirloom/mailutils) aceita múltiplos destinatários separados por espaço.
- Override de teste documentado: `BALEIA_DESTINATARIOS="a@b.com" bash enviar_baleia_azul_v2.sh`.

## Prova imediata

- Corpo da edição 06/08 ("Boa tarde") montado via `BALEIA_DRY_RUN=1` (todos os 5 blocos OK — audiência, custos, UptimeRobot, auditor, sinal Google) e enviado aos 2 endereços do Gabriel pela mesma rota (`ssh -p 38422 ubuntu@43.156.151.165 "mail -s ..."`), exit 0. Sem re-disparo de Telegram nem scp.
- Recibo no log: `[qui 06 ago 2026 19:0x] Cópia 06/08 enviada p/ Gabriel (2 endereços)`.
- Próximo envio agendado (07/08 08:00) já sai para os 3 automaticamente.

## Achado lateral — Telegram 400 (virou bug ativo)

Medindo o corpo do dry-run: **4.470 caracteres** — acima do limite de 4.096 do `sendMessage` do Telegram. Casa com o log: 06/08 18:00 `curl: (22) ... error: 400` + "AVISO: falha no envio Telegram" (08:00 passou — corpo menor). O e-mail não tem esse limite e segue íntegro. Registrado como `BUG-20260806-BALEIA-TELEGRAM-400` em `CEREBRO_NODE_BUGS_ATIVOS.md` (sugestão: truncar/dividir o texto do Telegram ou mandar só o resumo + link).

## Lição

Ordem registrada no Cérebro ≠ ordem aplicada no código. A conferência de hoje fechou uma lacuna de 16 dias (21/07 → 06/08). Vale o padrão: ao mudar emissor/pipeline, checar se as "ordens permanentes" do nodo correspondem ao que está no script.
