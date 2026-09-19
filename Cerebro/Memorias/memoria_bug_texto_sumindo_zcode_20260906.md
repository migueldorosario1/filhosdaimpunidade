# Memória — Bug do texto sumindo no ZCode Desktop 3.6.5: log técnico completo da investigação

**Data:** 06/09/2026 08:22→08:35 BRT · **Agente:** ZM/ZCode (GLM-5.3, Dell) · **Sessão-alvo:** `sess_a9274860-8a59-4b87-9f3a-23e8bcc24a9f`
Fórum-irmão: `Foruns/forum_bug_texto_sumindo_zcode_20260906.md` (veredito resumido).

## 1. Mapa do store (não óbvio — vale para próximas investigações)

- Store principal: `~/.zcode/cli/db/db.sqlite` (1,6 GB; tabelas `session`(501), `message`(72.662), `part`(270.177), `turn_usage`, `model_usage`, `tool_usage`, `session_entry`).
- Sem `sqlite3` CLI no Dell — usar `python3` com `sqlite3.connect("file:...?mode=ro", uri=True)` (SOMENTE-LEITURA; o app roda com WAL ativo).
- `message.data` (JSON): `role`, `time{created,completed}`, `finish` (`tool-calls`/`stop`), `semantics{uiVisibility, providerVisibility, transcriptVisibility}`, `modelID`.
- `part.data` (JSON): tipos vistos = `text`, `reasoning`, `step-start`, `step-finish`, `tool` (chaves `callID`, `tool`, `state{status,input,output,title,metadata,time}`), `timeline`, `compaction`, `file`.
- Uma mensagem assistant por RODADA do modelo dentro do turno (cada `step-start`...`step-finish`); `sequence` da mensagem ordena o transcript.
- Rollout do I/O do modelo: `~/.zcode/cli/rollout/model-io-sess_<id>.jsonl` — cada linha = 1 request (campos `response.text`, `response.toolCalls`, `response.finishReason`, `response.reasoningText`, `requestId`, `turnId`). É a prova do que o modelo EMITIU vs o que o store GRAVOU.
- Logs do app (Electron): `~/.zcode/v2/logs/AAAA-MM-DD.log` (main+renderer+host) e `~/.zcode/cli/log/zcode-AAAA-MM-DD.jsonl`.

## 2. Queries que provaram o caso (receita)

```python
# reconstruir turno: mensagens + parts em ordem, com tamanhos de texto
import sqlite3, json, datetime
con = sqlite3.connect("file:/home/migueldorosario/.zcode/cli/db/db.sqlite?mode=ro", uri=True)
sid = "sess_<id>"
for mid, tc, seq, data in con.execute(
    "SELECT id,time_created,sequence,data FROM message WHERE session_id=? ORDER BY sequence", (sid,)):
    d = json.loads(data)
    parts = con.execute("SELECT sequence,data FROM part WHERE message_id=? ORDER BY sequence", (mid,)).fetchall()
    desc = []
    for _, pd in parts:
        p = json.loads(pd)
        desc.append(f"text[{len(p.get('text',''))}c]" if p.get("type")=="text" else p.get("type"))
    print(seq, d.get("role"), d.get("finish"), " | ".join(desc))
```

Estado dos turnos: `SELECT turn_id,status,error_type,context_exceeded,completed_at FROM turn_usage WHERE session_id=?`. Compactações: parts com `json_extract(data,'$.type')='compaction'`.

## 3. Achados-chave

1. **Persistência ilesa:** 187 mensagens assistant na sessão, TODAS `uiVisibility=visible`; textos de 665c/1434c/4332c/1187c que "sumiram" estão gravados.
2. **Padrão do turno doente:** `text[conteúdo] + toolCalls[Bash date rodapé]` na MESMA resposta do modelo (`finishReason=tool-calls`) → rodada seguinte emite SÓ o rodapé de 194c (`finish=stop`). Turno termina com stub-final.
3. **Mecanismo da UI (decodificado do bundle):** `assistantHistoryDefaultOpen = !timelineOnly && (forceOpenHistory || isLastTurn && workStatus.state==='running' || ...)` em `out/renderer/assets/styles-DyAcaLKy.js` (app.asar 3.6.5 extraído com `npx asar extract`). Histórico intermediário do turno = Collapsible com chevron; aberto por default SÓ enquanto roda; ao completar, colapsa e deixa só `latestAssistantTextRow`.
4. **Sintoma match:** queixas do Miguel (08:04:12, 08:09:03, 08:18:05) caem 30-90s DEPOIS de turnos com stub-final; turno com conteúdo-final (07:50, 524c) não gerou queixa.
5. Descartes: compactação (1× às 23:10 de 05/09), `context_exceeded=0`, turnos `completed` limpos, `proto.staleRevision` (19× às 08:21/08:24) posteriores às queixas e ligados à projecção de file-changes, injeções ambiente (943c = lembrete TodoWrite) inócuas.

## 4. Cura aplicada nesta própria sessão (auto-teste vivo)

- Buscar `date` ANTES de escrever a resposta final (no início do turno) — feito às 08:22.
- Última mensagem do turno = relatório completo + assinatura, NENHUMA ferramenta depois.

## 5. Pendências / próximo passo

- Propagar regra "conteúdo essencial só na MENSAGEM FINAL do turno; rodapé: date antes, assinatura junto com o conteúdo" para AGENTS.md/perfis dos agentes (aguarda "vai" do Miguel — mudança em prompt compartilhado).
- Opcional: reportar à Z.ai (melhor UX do colapso pós-turno).
- Extraído `~/tmp_zcode_asar/` foi REMOVIDO após a análise (307MB); re-extrair com `npx asar extract /opt/ZCode/resources/app.asar .` se precisar reabrir.
