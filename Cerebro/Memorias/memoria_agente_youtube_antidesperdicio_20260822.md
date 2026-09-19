# 🧠 Memória técnica — Agente YouTube anti-desperdício (ZM, 22/08/2026 ~21h BRT)

Missão (ordem Miguel ~20:40): terminar com o desperdício de transcrição no Agente
YouTube; quem não publica não transcreve; trabalhar em harmonia com os loops.
Fórum (decisões): `Foruns/forum_agente_youtube_antidesperdicio_20260822.md`.

## 1. Diagnóstico (provas)

- Log: `agent_data/v4_cafezinho_youtube/cron.log` (14.707 linhas).
  - `grep -c "^Traceback"` = **23**; `grep -c "JSON inválido"` = **26**.
  - Rodada 22/08 20:00: transcrição 28.554 chars (transkriptor_url_direto, order_id
    1787440829871441741) → análise deepseek OK (tese Cerimedo) → nomes OK (13, 2
    websearch) → `redigir` → `gerar_json` → `LLMError: JSON inválido de openai_gpt55:
    Expecting value: line 1 column 1 (char 0)` → Traceback → perda total.
  - Curador da mesma rodada: cascata falha (deepseek "resposta sem bloco JSON" +
    kimi HTTP 429 conta suspensa) → heurística escolheu o vídeo perdido.
- Causa raiz: `nucleo_llm.py::gerar_json` antigo chamava `gerar()` (que só cai de
  provedor em EXCEÇÃO) e fazia `json.loads` FORA do loop — resposta 200 vazia =
  "sucesso" → parse explodia depois da cascata. GLM-4.5-flash também passou a
  devolver string vazia (smoke 22/08: `glm: VIVO → ''`); qwen/deepseek/openai PONG.
- Fila WP (REST context=edit): 5 rascunhos YouTube (267114, 267087, 266745,
  266545, 266525) + 10 pending V4 — produção sem consumo.
- Forense do "visto misterioso": draft 267114 (Farinazzo) criado 20:09:15 por
  sessão MANUAL dos loops (não passou pelo cron.log); vistos.json/historico.jsonl
  20:09:16 = sucesso real dessa sessão. O vídeo perdido foi o Cerimedo (TV Fórum).
- GSN V2 NYC: cron `youtube_v2_pipeline` AUSENTE do crontab (última run 19/08
  11:16 UTC? log); `/root/agent_data/youtube_v2_pipeline.log` mostra 27 drafts +
  3 prontos; tem `youtube_transcript_cache/` (cache nativo). NÃO reativado.

## 2. Mudanças aplicadas (backups `.bak_pre_*_20260822`)

### `agentes_tematicos/v4/nucleo_llm.py` (compartilhado — falha-apenas)
- `gerar_json` reescrito: loop próprio sobre a cadeia chamando `_chat` com
  `json_mode=True`; parse de fences/JSON DENTRO do loop; JSON inválido/vazio
  entra em `erros` e segue para o próximo provedor; retorno igual
  `{"texto","provider","tarefa","json"}`; mensagem final
  `"toda a cadeia falhou → ..."` lista todos. `gerar()` intocado.
- Prova: smoke ao vivo cadeia `["glm","qwen",...]` → **qwen** entregou `{'ok': 1}`
  com glm vazia na frente. py_compile OK.

### `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py`
- `_transc_path` + `_transcrever` com CACHE: lê `BANCO_DIR/transc_<id>.json`
  (≥500 chars) antes de pagar; grava texto+meta+ts após sucesso; log
  "CACHE — custo zero". Patch AGY fail-soft de feeds (20/08) PRESERVADO.
- Bloco anti-desperdício após `_marcar_visto`: `_pendentes_path`,
  `_lista_pendentes`, `_gravar_pendentes` (teto 20), `_salvar_pendente`
  (só se cache existe), `_consumir_pendente` (mais antigo, 1/rodada, 3
  tentativas, remove visto/sem-cache, registra publicação no sucesso),
  `_fila_revisao_youtube` (REST `/posts?status=draft,pending&context=edit`,
  conta embed `youtube.com/embed/`, fail-open com log), `FILA_REVISAO_MAX`
  (env `YOUTUBE_FILA_REVISAO_MAX`, default 4), `PAUSAR_FLAG`
  (`BANCO_DIR/PAUSAR_TRANSCRICAO`), `_breaker_transcricao(contexto)`.
- `processar`: pós-transcrição inteiro em try/except → exceção vira pendente
  (`_salvar_pendente(video,"processar",repr(e))`) + log "trabalho PRESERVADO";
  devolve "" (rodada segue para o próximo candidato; nunca mais Traceback).
- `rodar_rodada` e `rodar_jornal_forum`: início = `_consumir_pendente()` →
  `_breaker_transcricao(<contexto>)` → só então coleta/curadoria/transcrição.
  Modo `--video` manual NÃO bloqueia (teste/explícito).
- py_compile OK; import limpo.

## 3. Provas E2E

1. Unitário: `_fila_revisao_youtube()` = **5**; breaker True.
2. E2E `--rodada` manual 21h: log único
   `🛑 BREAKER ANTI-DESPERDÍCIO (rodada): 5 rascunhos YouTube aguardando revisão
   dos loops (teto 4) — quem não publica não transcreve` — rodada encerrou em
   ~1s, zero transcrição, zero LLM.
3. Crons vigentes (intocados): --rodada 08/14/20h · --jornal 22:30/23:00/23:30 ·
   --forum11 14:30/15:30 — todos já rodam sob o novo regime.

## 4. Comunicação (harmonia com os loops — ZM-20260822-175)

- `Cerebro/Foruns/inbox_trindade/claude.md` (CM, chefe de publicação): recado +
  fila dos 5 + pedido de ACK.
- `Projeto Cafezinho Agentes/Foruns/canal_trindade.md`: nota curta.
- `Cerebro/Foruns/ponte_laura_completa/de_dell.md`: mesmo conteúdo p/ loops Laura.
- Monitor de trabalho: linha EM ANDAMENTO 20:50 → ✅ ao concluir.

## 5. Pendências / próximos passos

1. Loops consumirem a fila (5) → breaker libera sozinho (rodada seguinte).
2. Decisão conjunta sobre reativação do cron GSN V2 NYC (27 drafts).
3. Observar 2-3 dias: zero "transcrição perdida" esperado; qualquer perda vira
   pendente visível (`pendentes_youtube.json`).
4. Camada nomes/verifica ainda falta no GSN V2 (pendência antiga, manual §7).
5. IPRoyal proxy 402 (sem crédito) segue engolindo feeds — patch AGY mitiga com
   curl IPv4 direto; recarga é decisão do Miguel.
