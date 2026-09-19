---
name: feedback-gravacao-datada-por-ciclo-e-ponte-kimi-regular
description: "Todo ciclo do loop Vigília precisa gravar registros em arquivos datados/com hora (cada bug = aprendizado); Kimi acompanha os loops de vez em quando, então ponte com ele precisa ping periódico no canal Trindade"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cf4e142a-050c-46de-b793-bee2464fc7f7
---

**📚 Duas diretrizes complementares — gravação por ciclo + ponte Kimi ativa:**

## 1. Gravação sistemática em arquivos datados com hora

Todo ciclo do loop Vigília (DIA e NOITE) deve deixar rastro em arquivos datados com timestamp preciso. **Cada bug encontrado = 1 aprendizado**, e o rastro precisa ficar acessível pra futuras sessões.

**Camadas mínimas obrigatórias por ciclo com publish/pending:**
1. `Cerebro/monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl` — 1 linha JSON por wp_post (publish/pending), com `ts_utc`, `pid`, `vertical`, `pipeline`, `fixes`, `websearch`, `revisor_deepseek`, `revisor_gpt`, `backup`, `sha256`, `status_final`.
2. `Cerebro/Backups/vigilia_v5/YYYY-MM-DD/<pid>_pre_<tag>_YYYYMMDD_HHMMSS.json` — snapshot completo do post antes da alteração.
3. `Cerebro/monitoramento_horario/relatorios_revisores/YYYY-MM-DD.md` — relatório diário DS+GPT (script `relatorio_diario_revisores.py`, rodar 1×/dia no 1º ciclo BRT).
4. **NOVO 06/08 22:xx BRT:** `Cerebro/monitoramento_horario/ciclos_vigilia/ciclos_vigilia_YYYY-MM-DD.md` — resumo MD legível consolidado do dia (breakdown por vertical, drafts publicados, pendings, decisões editoriais não-triviais, bugs padrão encontrados, aprendizados). Editar in-place ao longo do dia, 1 seção por ciclo.

**Bugs recorrentes viram regras** — quando um mesmo bug aparece 2ª ou 3ª vez, criar entrada em `memory/feedback_*.md` + pointer no MEMORY.md pra virar regra da próxima checagem dupla.

## 2. Ponte com Kimi ativa — ping periódico no canal Trindade

Kimi vai acompanhar meus loops de vez em quando (regime pós-05/08 22:55 BRT — ele é fiscal do backup + fiscal geral). Precisa saber que estou vivo + o que fiz.

**Rotina:**
- **1 ping curto/hora** no `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` com tag `[CLAUDE-VIGILIA-CICLO-HHMM-BRT]` — 3-5 linhas: publicados+pending do ciclo, C05 status se aplicável, próxima janela.
- **Não spammar** — 1 ping por hora consolidado é melhor que 1 por ciclo (a cada 30min no DIA). No NOITE (1h/ciclo), pode ser 1 por ciclo mesmo.
- Quando Kimi responder ou marcar algo no ESTADO/fórum, reconhecer no ping seguinte.
- Se algo bloqueia (draft polêmico Miguel precisa decidir, C05 travado, WebSearch inconclusivo), sinalizar CLARAMENTE no ping — Kimi pode ajudar.

**Why:** Miguel 06/08/2026 02:20 BRT (madrugada): *"não esquece de manter tudo gravado em todo o loop, ok? em arquivos datados, com hora, cada bug será um aprendizado para a gente. o kimi vai acompanhar seus loops de vez em quando, por isso não esqueça da ponte com o kimi."* Contexto: acabei de fazer 5 publish + 2 pending no início do dia 06/08 com bons registros individuais (JSONL, backups, memória do backup) mas SEM ping regular pro Kimi (última interação com ele foi 00:05 quando ele confirmou ponte) e SEM resumo consolidado do dia legível. Miguel quer os 2 hábitos permanentes.

**How to apply:**
- Ao final de cada ciclo Vigília DIA/NOITE, imediatamente após reportar pro Miguel no chat, escrever/atualizar 3 coisas:
  1. bugs_YYYY-MM-DD.jsonl (já faço — manter)
  2. ciclos_vigilia_YYYY-MM-DD.md (NOVO — criar 1 seção por ciclo com timestamp)
  3. Ping curto no canal_trindade.md com tag `[CLAUDE-VIGILIA-CICLO-HHMM-BRT]` (NOVO — 1×/hora)
- Se ciclo teve zero drafts, ping ainda vale (curtinho: "🌙 HH:MM zero drafts, C05 status Y, próxima Z").
- Toda decisão editorial não-trivial (pending por duplicata, título muito reformulado, correção de bug factual grave) — registrar no ciclos_vigilia_YYYY-MM-DD.md com 1-2 linhas explicativas.
- Regra irmã de [[feedback-canal-inbox-apenas-ponteiro-carta-no-chat-e-forum]] (canal = ponteiro curto — ping cabe no canal).
