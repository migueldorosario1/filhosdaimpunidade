# Ponto de Retomada — Claude Code / sessão 04/08/2026 16:01 BRT

**Código da sessão:** `zizi`
**Timestamp:** 2026-08-04 16:01 BRT
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`)
**Substitui:** `ponto_retomada_claude_sessao_20260731_2215.md` (obsoleto)

---

## 1. Estado operacional agora

- **19 posts publicados hoje (04/08)** — breakdown: 8 Nacional, 6 Geo, 4 Ciência, 1 YT-esteira (cat 2403).
- **Loop Vigília V5 rodando** — DIA `*/30 :17/:47` 07-22h + NOITE `:17` 23-06h. Único loop editorial V4 é Opus 4.7.
- **Pipeline revisão tripla ATIVO** (retomado hoje 10:51 no post 264219): DeepSeek → GPT → Claude+WebSearch → publish.
  - DeepSeek: 7 calls hoje / US$ 0.007
  - GPT (cap 10/dia): 2 calls hoje / US$ 0.007 (`gpt_enabled.txt = on`)
- **Sentinela publish OFF** desde 27/07 17:15 — último ciclo em `ciclos.jsonl` é 27/07 16:00 (esperado).

## 2. Pendências operacionais visíveis

1. **Baleia Azul parado há 8 dias** — último `boletim_baleia_azul_20260727.md` (27/07 06:01). Deveria gerar diário 06:00-07:45 BRT (regra 01/08).
2. **Relatórios diários dos revisores nunca rodaram** — diretório `Cerebro/monitoramento_horario/relatorios_revisores/` vazio. Regra criada 03/08 14:15 (script `relatorio_diario_revisores.py`) não foi disparado.
3. **8 pending do bug §86 (31/07)** — status remoto não verificado nesta retomada (DNS indisponível na sessão). IDs: 263498, 263635, 263571, 263638, 263653, 263574, 263634, 263654. Kimi K3 Desktop tinha delegação para gerar imagem+publish (cartinha `cartinha_kimi_pending_delegados_20260731_1120.md`).

## 3. Regras vigentes recuperadas (topo MEMORY.md — 04/08)

- 📊 Relatório diário revisores (DS+GPT) no 1º ciclo BRT
- 🤖 GPT REVISOR camada tripla, cap 10/dia, horas pico BRT {8-11, 14-19}
- 🔍 DeepSeek REVISOR camada extra em cada publish V4
- ✍️ Checagem título: gênero da fonte + semântica/regência + tempo verbal x data + peso editorial
- 🏠 Fim de semana (sáb/dom): remover cat 20699 de TODOS os V4; segunda volta ao normal
- 🐋 Baleia Azul editor-chefe (Claude) — boletim diário 06:00-07:45
- 🎬 Gatilho `zizi` = este ritual (leia SEMPRE o ponto de retomada mais recente via `ls -t`)
- 🌉 Gatilho `ponte` = sincronização triangular Trindade Nova
- 🔁 Loop Vigília Opus V5 DIA/NOITE
- 🎯 Autonomia total na checagem dupla editorial V4 (reportar depois, não pedir OK a cada caso)
- 🔎 WebSearch obrigatório em autoridades cutoff / datas / números
- 🔐 Nunca chave literal em fórum/memória — usar referência simbólica
- 📮 Canal+inbox = ponteiro curto; carta = chat + fórum + .md com link
- 🎭 Diferenciar LLM Desktop vs CLI vs Mobile ao mencionar

## 4. O que a próxima sessão Claude (retomando via `zizi`) deve fazer

1. `date` + `ls -t ponto_retomada_claude_*.md | head -1` — sempre pega este arquivo (ou substituto mais novo).
2. `tail -3 bugs_$(date +%Y-%m-%d).jsonl` + contar `status_final=publish` do dia por vertical.
3. Ver contadores `state/{deepseek,gpt}_counter_$(date).json` e switch `gpt_enabled.txt`.
4. Checar se Baleia + Relatório diário revisores rodaram hoje (diretórios de saída).
5. Reportar em ≤ 20 linhas e esperar comando — NÃO rodar ciclo Vigília automaticamente.

## Assinatura

Ponto de retomada gravado por Claude Code (Anthropic, `claude-opus-4-7`), 2026-08-04 16:01 BRT. Código de retomada: **`zizi`**.
