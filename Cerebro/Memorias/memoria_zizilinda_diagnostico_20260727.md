# 🤖 Memória Técnica — Diagnóstico Zizilinda (por que o vídeo ficou sem resposta)

**Data:** 2026-07-27 · **Autor:** ZCode/Kimi · **Fórum pareado:** `Foruns/forum_zizilinda_diagnostico_20260727.md`

## 1. Sintoma relatado por Miguel

Miguel mandou um vídeo para a Zizilinda (`@Zizilindabot`) dias atrás e não recebeu resposta nenhuma.

## 2. Diagnóstico executado (sessão ZCode, 27/07)

Verificações no Tencent (`ssh tencent`, usuário ubuntu) e no código local (`ZCodeProject/painel_fix/zizi_fix/`):

| Item | Estado encontrado |
|---|---|
| `zizi.service` (systemd, Tencent) | **inactive (dead)** + `disabled` — ninguém escutando o bot |
| Processos `zizi`/`controlado` no Tencent | nenhum rodando |
| `agente_controlado.py` no Tencent | arquivo existe (`/root/`, 07/jun, 223 KB), mas **sem processo, sem service, sem cron** (root e ubuntu) |
| Versão do bot no Tencent | `/root/bot_zizi_linda.py` de **31/05** — **não contém `handle_video`** |
| Versão do bot local | `zizi_fix/bot_zizi_linda.py` de **25/07** (237 KB) — **contém `handle_video`** (handler novo) |
| `journalctl -u zizi.service` | sem entradas |

**Conclusão:** o vídeo caiu no vazio por dois motivos empilhados: (1) serviço desligado; (2) mesmo ligado, a versão do servidor (31/05) não tem handler de vídeo — mensagens com vídeo caíam no silêncio (o próprio docstring do handler novo, de 25/07, registra isso).

## 3. Fluxo de vídeo na versão nova (local, 25/07) — como fica quando religada

Handler `handle_video` (`bot_zizi_linda.py:4594`):

1. Miguel manda o vídeo no chat (sem comando), **até 20 MB** (limite da Bot API para download).
2. Bot responde "🎬 Vídeo recebido!", baixa o arquivo e **transcreve o áudio** (`transcribe_voice`).
3. Devolve a transcrição no chat e alimenta o texto no fluxo de pauta/instrução (`handle_text`, `from_voice=True`).
4. Acima de 20 MB: bot avisa e pede trecho menor/compactado.

**Corte de silêncio:** NÃO é feito pelo bot. Miguel assinou serviço externo de corte de silêncio — o vídeo deve ser enviado já limpo (decisão registrada no fórum de 23/07).

**Pipeline completo multirrede** (R2 → legenda assada Creatomate → 5 textos por rede → kit de aprovação → disparo paralelo FB/IG/TikTok/YT/X/WP) **segue como sprint separada** (memória de 23/07). O handler de 25/07 cobre entrada + transcrição; a esteira de publicação ainda não está dentro do bot.

## 4. Limpeza documental pedida por Miguel (27/07)

A pedido de Miguel ("tira esse aviso de duplicata... não me interessa"), foram removidos os avisos de "dois consumidores de `getUpdates`" de:

- `MEMORIA/memoria_video_diario_multirrede_20260723.md` (decisão de entrada)
- `Foruns/forum_video_diario_multirrede_20260723.md` (pendência técnica da Fase 1)

## 5. Decisão de Miguel (27/07)

**Vamos usar a Zizilinda para o fluxo de vídeo para as redes.** Religamento implica:

1. Subir a versão nova do bot (local 25/07) para o Tencent.
2. Subir apenas o bot oficial como consumidor do token (deploy padrão, consumidor único).
3. `systemctl enable --now zizi.service`.
4. Fase 0 da sprint multirrede (espelhamento de credenciais FB/IG/X/Creatomate/R2 no `/root/.env.unificado`) continua bloqueante para a esteira completa; TikTok e YouTube têm bloqueios próprios já mapeados na memória de 23/07.

## 6. Prova de controle (27/07)

Mensagem "alô" enviada por ZCode via API do bot (`TELEGRAM_TOKEN_ZIZI`, cofre local) para o chat do Miguel, demonstrando controle operacional da Zizilinda. `chat_id` do Miguel capturado via `getUpdates` e guardado no cofre local como `TELEGRAM_CHAT_ID_MIGUEL` (pendência da Fase 0 cumprida).

## 7. Atualização de estado — 2026-08-03 17:00 BRT (ZCode)

Re-verificado a pedido do Miguel ("comunicador intenso de vídeo ligado ao Telegram — está ativo?"): **`zizi.service` segue `inactive` + `disabled` no Tencent; `/root/bot_zizi_linda.py` continua sendo a versão de 31/05 (sem `handle_video`)**. Ou seja: desde o diagnóstico de 27/07 nada mudou no servidor — o bot permanece fora do ar e qualquer vídeo enviado continua caindo no vazio.

**Decisão do Miguel (03/08): manter desligada por enquanto.** Caminho de reativação quando autorizado: deploy da versão 25/07 (`ZCodeProject/painel_fix/zizi_fix/bot_zizi_linda.py`, com `handle_video`) + `systemctl enable --now zizi.service` + smoke `getMe`/update simulado (~10 min). A esteira multirrede completa (R2 → Creatomate → 5 textos → disparo FB/IG/TikTok/YT/X/WP) segue como sprint separada (memória de 23/07).
