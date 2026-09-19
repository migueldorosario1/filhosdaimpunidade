---
name: Todo loop (trindade ou operacional) lê canal + checa áudios Augusto
description: Regra universal Miguel 2026-05-11 08:54 BRT — qualquer loop que eu criar deve incluir leitura do canal_trindade.md + verificação de áudios Miguel via Augusto no Tencent (filtro 30min). Vale pra loops trindade, operacional, ou qualquer outro tipo futuro.
type: feedback
originSessionId: bd54c85a-5148-4101-8101-b84b4598e99a
---
**Regra universal de loops (Miguel 2026-05-11 08:54 BRT):** Qualquer loop que eu criar (trindade, operacional, ou novo tipo) deve incluir **2 verificações obrigatórias** no prompt do tick:

1. **Ler tail do `Foruns/canal_trindade.md`** (60-150 linhas) e responder novidades Codex/AG via append atômico §39.3.

2. **Verificar áudios Miguel via Augusto** no Tencent — SSH `tail /root/audio_uploads/processing_log.jsonl`, filtrar últimos 30min (`date -d '-30 min'`). Áudios >30min, ignorar silenciosamente.

**Why:** Miguel deixou claro que essas 2 fontes são canais primários de input dele pro sistema (texto via canal Trindade, voz via Augusto). Loop que não checa essas 2 fontes não cumpre função de "ficar ligado" no projeto. **Refinamento 11/05 08:55:** Miguel quer que Trindade não tenha que ir até o Tencent buscar áudio — eu trago o conteúdo pra eles.

**Como postar quando achar áudio Miguel <30min (refinamento 11/05 08:55):**

PASSO 1 — **Transcrição ÍNTEGRA no fórum** (não no canal):
- Se áudio é sobre tema com fórum existente (ex: bug Zizi, Twitter, Caçador YouTube) → append no fórum dessa frente
- Se áudio é genérico/multi-tópico → criar/append em fórum geral do dia: `Foruns/forum_audios_miguel_YYYY_MM_DD.md`
- Formato no fórum: header com hora BRT + transcrição completa (sem cortar) + resposta Augusto/Kimi íntegra

PASSO 2 — **Aviso curto no canal_trindade.md** (append §39.3):
```
🎙️ Claude → Trindade (áudio Miguel via Augusto — JÁ TROUXE AQUI):
> "<resumo curto até 200 chars>"
🤖 Augusto/Kimi respondeu: <resumo curto>

**Transcrição íntegra no fórum:** `Foruns/forum_<correspondente_ou_audios_miguel_YYYY_MM_DD>.md`
**Ninguém mais precisa ir ao Tencent buscar — já está aqui.**
```

PASSO 3 — Se STT falhou ou Augusto não respondeu, marcar "⚠️" no post.

**Outras regras:**
- Filtro 30min INEGOCIÁVEL (Miguel: "não vale pegar áudio antigo")
- Não duplicar — verificar antes se áudio já foi postado
- Fórum geral do dia segue convenção: `Foruns/forum_audios_miguel_2026_05_11.md` (snake_case com ano/mês/dia)

**Casos:**
- Loop operacional Cafezinho `c567a955` (11/05 08:54): já incluído.
- Próximo loop trindade ou outro: aplicar mesma regra.
