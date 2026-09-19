# 🤖 Rondas DS no Telegram — final cortado e assinatura "DS" solta (31/08)

**Queixa do Miguel (31/08 ~09:1x):** "recebo aqui pela ponte cafezinho a cada meia hora a ronda... tá vindo sem final, tá cortando o final... não tá assinando qual o DS. São vários: tem que falar DS Miguel, DS Celular, DS Nuvem, DS Laura. DS não é assinatura. E tá cortando sempre o final."

## Diagnóstico (provas nos scripts e logs)

1. **Quem envia a cada 30 min:** a ronda do DS do Dell (`/home/migueldorosario/Downloads/Antigravity Google/ronda_30min.sh`, cron `*/30`, dsh headless + `ronda_30min_prompt.md`) — o relatório é gerado COMPLETO pelo dsh (provado no log `/tmp/ronda_30min/20260831.log`: a ronda das 09:00 termina com a lição inteira) e depois AMBOS os defeitos eram aplicados pelo SCRIPT na hora do envio ao Telegram.
2. **Final cortado = `cut -c1-700`** no script: todo relatório era amputado em 700 caracteres, SEMPRE no meio de uma frase (o relatório de 09:00 tem ~1.400). Além disso `tr '\n' ' '` destruía a formatação (virava um bloco corrido).
3. **Assinatura = `[DS-ronda 31/08 09:00]`** — "DS-ronda" genérico, sem dizer qual DS. O DS do Dell é o **DS Miguel (Dell)** (prompt: "DS (DeepSeek/DSH, Dell), CEO em treinamento").
4. **DS Nuvem (Tencent):** o relatório da ronda 09:00 no log terminava SEM assinatura final (regra DSC-030 pede nome completo só na 1ª menção — insuficiente para o Miguel). As respostas dele via `RESPOSTAS.md` já são bem assinadas ("— DS Nuvem Chefe (DS-N Chefe) · carimbo") — o padrão certo existia, mas não era regra geral.

## Correções aplicadas (todas com backup)

| Onde | O que mudou |
|---|---|
| Dell `ronda_30min.sh` (backup `.bak_pre_assinatura_corte_20260831`) | corte cego 700 → **3.700 chars com "…"** (limite do Telegram ~3.900); **preserva quebras de linha**; **assinatura automática no fim**: `— DS Miguel (Dell) · AAAAMMDD HH:MM:SS BRT` (se o relatório já assinou, não duplica); log novo `telegram-enviado:` com os primeiros 200 chars (auditoria) |
| Dell `ronda_30min_prompt.md` | Encerramento agora exige: relatório TERMINA com `— DS Miguel (Dell) · carimbo` (date real); nunca acabar no meio de frase |
| Tencent `ronda_dsn_prompt.md` (backup `.bak_pre_assinatura_20260831`) | Regra dura nova: TODA mensagem ao Miguel termina com `— DS Nuvem Chefe (DS-N Chefe) · AAAAMMDD HH:MM:SS BRT`; nunca cortar o final (limite ~3.900; encurtar resumindo o MEIO, mantendo a última frase completa) |
| Ponte `de_dell.md` (bloco **ZM-20260831-001**, commit `becdcf316`) | Regra DS-ASSINATURA para TODOS os robôs DS (DS Miguel, DS Celular, DS Nuvem, DS Laura) — DS Laura e DSC devem aplicar nas rondas deles |

## Cura de repo no caminho (transparência)

O repo `~/cerebro-miguel` estava com **rebase interrompido** (HEAD solto, main 3 commits únicos, origin 62 à frente — os pushes da escuta/sync estavam falhando). Curado pela receita: conteúdo único do HEAD salvo em `/tmp/cerebro_head_solto_20260831_092354/` → `rebase --abort` → `reset --hard origin/main` → reaplicação dos 151 arquivos únicos (prints Moka, escuta entrada_1089/1099, conversa_48h, ciclos Codex) → marcadores de conflito do de_dell removidos (mantidos os 2 lados) → commit único + push OK (`becdcf316`).

## Adendo 09:37 — VALIDADO na ronda real ✅

A ronda das 09:30 (primeira com o script novo) saiu correta, provado no log `/tmp/ronda_30min/20260831.log`:

- Relatório termina com `— DS Miguel (Dell) · 20260831 09:36:46 BRT` (o prompt novo fez o dsh assinar; o script detectou e não duplicou).
- Envio: `telegram: enviado 09:37:41` + linha nova de auditoria `telegram-enviado: 📊 [DS Miguel (Dell) — ronda 31/08 09:37 BRT] Tudo pronto — …` — cabeçalho com o nome do DS e texto COMPLETO (sem o corte de 700, com quebras de linha preservadas).

## O que falta / o que preciso do Miguel

- **Validação automática:** a ronda das 09:30 já sai no formato novo (assinada + completa) — conferir no Telegram.
- **DS Laura e DSC:** aplicarem a regra (bloco na ponte avisa).
- Nada a fazer do Miguel — só conferir a próxima ronda e dizer se aprovou.
