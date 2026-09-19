---
name: bug-chamar-kimi-helper-reasoning-max-tokens
description: Helper /root/scripts/chamar_kimi.py por default usa kimi-k2.6 (reasoning) + max_tokens=700. Reasoning consome tudo no <think> interno e devolve resposta vazia. Pra prompts não-triviais usar --model moonshot-v1-128k --max-tokens 4000.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 42789f13-00c9-4e70-9b8c-f37d93570ab6
---

# Bug helper `chamar_kimi.py` — reasoning model + max_tokens baixo = output vazio

**Quando notei:** 2026-05-23 22:28 BRT (Sprint C — Kimi falhou 3x sucessivas, sempre output 1 byte).

**Root cause:** O helper `/root/scripts/chamar_kimi.py` no Tencent:
- Default model: `kimi-k2.6` (linha 47: `or "kimi-k2.6"`) — **reasoning model** (vimos no §66 Cérebro: kimi-k2.6 / deepseek-v4-pro / qwen3.5 / qwen3.6 são reasoning, consomem tokens em `<think>` interno antes de responder)
- Default `max_tokens=700`
- Resultado: prompt grande → reasoning consome todos 700 tokens em `<think>` → resposta vazia (LLM cortado antes de escrever output visível) → helper retorna 1 byte

**Why importante:** Sprint C tinha prompt de ~300 palavras pedindo resposta de 300 palavras. Cabia em 700 tokens DE RESPOSTA, mas não em 700 tokens de reasoning+resposta. Falhou silenciosamente — eu cheguei a substituir Kimi por Qwen como tampão (errado, Qwen não é Trindade).

**How to apply:** Sempre que chamar `chamar_kimi.py` pra parecer real (não smoke trivial), usar:
```bash
sudo python3 /root/scripts/chamar_kimi.py \
  --file /tmp/meu_prompt.txt \
  --model moonshot-v1-128k \
  --max-tokens 4000
```

- `moonshot-v1-128k` = não-reasoning, responde direto
- `--max-tokens 4000` = folga pra respostas longas
- `--file` = lê de arquivo (evita problemas de stdin/pipe quando via nohup/bash -c)

**Validado:** 2026-05-23 22:38 BRT — Sprint C entregou voto completo "APROVO COM AJUSTE" com flags acima.

**Pendência:** alguém da Trindade deveria patchear o helper pra default ser `moonshot-v1-128k` + `max_tokens=4000`. Bug está na escolha do default, não na chamada.

## Relacionado
- [[reference_cerebro_secao_66_modelos_llm]] — §66 lista reasoning models problemáticos
- [[feedback_helpers_chamar_llm_tencent]] (se existir) — outros helpers podem ter mesma armadilha
