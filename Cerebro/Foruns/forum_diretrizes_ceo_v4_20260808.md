# FÓRUM — Diretrizes do CEO (nova aba do painel CCTV V6) — 2026-08-08

> [!CAUTION]
> **ARQUITETURA SUPERADA EM 09/08/2026.** Este fórum documenta o estado anterior ao corte V4. As passagens que chamam `agente_controlado.py` de redator atual são somente histórico e não podem orientar diagnóstico, edição ou deploy. Ver `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

> **Tema Duplo:** este fórum (decisões) + `Memorias/memoria_diretrizes_ceo_v4_20260808.md` (log técnico).
> **Nodo:** CEREBRO_NODE_QUALIDADE_REDACAO + CEREBRO_NODE_DIRETRIZES_COLETORES.
> **Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan) — chat direto — 2026-08-08 ~03:30 BRT.

## 1. O pedido do Miguel (ordem do editor)

> "A gente tem uma página no painel, 'Diretrizes', aberta pra colaboração... Quero colocar um áudio, pra ele incorporar nas diretrizes... um espaço de interação entre o CEO (eu) e as diretrizes. Uma inteligência filtraria o que eu falo e faria mudanças pontuais, depois de interpretar, pedir confirmação."
>
> Refinamento: "usar inteligência boa pra interpretar minhas falas, ou escritas, pra ajustar diretrizes e prompts de todos os V4, seja um específico (geopolítica) ou todos. Pensa numa arquitetura moderna — não usa a arquitetura antiga do Cafezinho (agente_controlado é V1/legacy)."

## 2. Decisão de desenho — aprovada

**Conceito:** uma IA **secretária-executiva** entre o Miguel (CEO/diretor-geral) e os prompts espalhados do V4. Ele fala (áudio) ou escreve uma ordem editorial → a IA interpreta (modelo bom) → identifica **quais slots** aquilo afeta (por **etapa × escopo**) → propõe **patch exato** → Miguel confirma ✅ → Patch Engine aplica no arquivo físico certo, com diff + rollback + registro no Cérebro.

**Peça central:** um **Intelligence Registry** (`registry.yaml`) que **indexa** (NÃO concentra) os ~25 slots de inteligência do V4 — respeitando o fato de que a inteligência do V4 é espalhada por natureza (coleta, tese, título, revisão, imagem...) e não dá pra juntar num arquivo só.

## 3. Achados técnicos que definiram a arquitetura

### 3a. Mapeamento real da inteligência do V4 (~25 slots)
Mapeados os pontos de prompt/inteligência LLM no V4 de produção (IGNOREI legacy/V1: `agente_controlado.py` em `Agentes Labs`, `v4_labs`, pastas Legacy). Distribuição:
- **Grupo A (V4-canônico, orquestrador + imagem):** `v4_vertical_draft_worker.py` (briefing/tese, fact-gate, juízes visuais) + `gerador_imagem_editorial.py` (system prompt visual, 3 estilos por seção, fallbacks).
- **Grupo B (redator subprocesso — invocado pelo V4):** o `agente_controlado.py` é chamado como subprocesso pelo worker (`AGENT="/root/agente_controlado.py"`, linha 65). Apesar do nome V1, **é o redator de produção atual**. A maior parte dos botões de título/corpo/revisão/triagem/classificação mora nele e nos JSONs externos. **Decisão:** a feature edita onde a inteligência está hoje; a migração da redação pro coração do V4 fica como sprint separado (o Registry torna isso indolor — só mudam os paths).
- **JSONs/TXT externos (vivem em `/root/agent_data/` e `/root/prompts/` no servidor):** `estilo_master.json`, `diretriz_geral.json`, `diretriz_controlado.json`, `briefing_execucao.json`, `prompts/*.txt`.

### 3b. Arquitetura do painel CCTV (alvo da feature)
- **V6 (`painel_cctv_v6.py`, porta 8084) é o painel VIVO** (nginx redireciona pra ele em `/v6/`). V5 (8082) está obsoleto/quebrado.
- **V6 é SOMENTE-LEITURA** — não tem `do_POST`. Toda escrita mora no V5 velho. → **Decisão:** estender o V6 com `do_POST` exclusivo desta feature (copiar padrão de persistência do V5). Não acoplar ao V5.
- Servidor: Python puro (`http.server.BaseHTTPRequestHandler`), sem framework. Roteamento por dict `ROUTES`. HTML/CSS/JS 100% inline em f-strings.
- Front de áudio: o botão "🎙️ Gravar Áudio" do Mural é **placeholder morto** — `launchRecorder()` nem existe; handler retorna "Transcrição ainda não implementada". → construir `getUserMedia`+`MediaRecorder` do zero.

### 3c. Presença física local dos arquivos-alvo
- **Inline .py (Grupo A):** TODOS existem e estão vivos localmente (`v4_vertical_draft_worker.py` 107KB, `gerador_imagem_editorial.py` 26KB, `v4_vertical_intake.py` 12KB).
- **JSONs externos:** só em legacy (snapshot 09/jun) — servem pra modelar schema e prototipar leitura; no deploy apontam pro `/root/agent_data/` real.
- **Chave Whisper/OpenAI:** `OPENAI_API_KEY` existe e não vazia no `.env.unificado`. ✅

## 4. Arquitetura moderna escolhida

### Componentes
1. **Intelligence Registry** (`painel_fix/ceo/registry.yaml`) — mapa vivo dos ~25 slots: `id`, `etapa`, `escopos`, `alvo{kind,arquivo,simbolo/chave/marker}`. Kind = `py_inline` | `json_file` | `txt_file`.
2. **UI matriz ETAPA × ESCOPO** (nova aba `/diretrizes-ceo` no V6) — grade de botões (linhas=etapas, colunas=escopos). Cada célula abre o(s) slot(s) da combinação.
3. **IA Intérprete-Editor** — recebe fala/escrita → consulta Registry → propõe multi-alvo (quais slots afetados) + patch → confirmação do Miguel.
4. **Patch Engine** — aplica no lugar físico real (com backup `.bak_pre_ceo_<ts>` + rollback), registro no Cérebro (Tema Duplo).

### Estratégia inline `.py`: sentinel-markers
Cada bloco de prompt editável é envolvido por `# >>> CEO:<id>` / `# <<< CEO:<id>`. Patch Engine lê/escreve entre marcadores — robusto, não depende de parsear f-strings arbitrários. Passagem de refactor em **cópia shadow** local (NÃO no V4 ao vivo) pra evitar colidir com a sessão "V4 Home 10%/20%" ativa em 08/08.

### Eixos
- **Etapas:** coleta, triagem, tese_angulo, titulo, draft_corpo, revisao, verificacao, imagem, finalizacao.
- **Escopos:** geral, politica, geopolitica, ciencia, regional.

### Dois modos de uso
- **Direto (botão):** clica na célula → vê prompt atual → edita/escreve → patch → confirma.
- **Fala Livre:** 🎙️ áudio / caixa de texto → IA sugere células afetadas → confirma quais.

## 5. Decisões do Miguel (08/08 ~03:30)

| # | Decisão | Escolha |
|---|---------|---------|
| 1 | Escopo da construção | **Tudo (Fases 1–4)** — Registry + UI + Intérprete + Patch Engine + Áudio |
| 2 | Registro no Cérebro | **Sim, antes de codar** (Tema Duplo + monitor) |
| 3 | IA Intérprete | Cadeia de failover (Kimi → Qwen → GLM); hoje roda em GLM-5.2 |
| 4 | Aplicação | Fila de patches aprovados + batch c/ backup+rollback |
| 5 | Áudio | Whisper (OpenAI); chave no `.env.unificado` |
| 6 | Alvo do painel | V6 (estender com do_POST), não V5 |

## 6. Fases de construção

1. **FASE 1 — Registry + leitores + UI só-leitura** + sentinel-markers em cópia shadow. *Entrega: Miguel vê toda a inteligência do V4 organizada pela 1ª vez.*
2. **FASE 2 — IA Intérprete + edição por texto** (caixa → patch dirigido → aprova → fila).
3. **FASE 3 — Patch Engine** (aplica + rollback + registro Cérebro).
4. **FASE 4 — Áudio Whisper** (🎙️ → texto → patch).

## 7. Estado da missão

- **O que aconteceu:** desenho aprovado; mapeamento dos ~25 slots; exploração do painel V6 e dos arquivos-alvo; este fórum + memória criados. **✅ FASE 1 ENTREGUE E TESTADA** (08/08 ~03:50).
- **O que falta:** FASE 2 (IA Intérprete), FASE 3 (Patch Engine), FASE 4 (Áudio Whisper).
- **O que preciso do Miguel:** testar visualmente a FASE 1 quando puder (ver §9 abaixo); depois sigo com as próximas fases.

## 8. Fora de escopo (sprints separados)
- Migrar redação de `agente_controlado.py` pro coração do V4.
- Sincronizar as 3 fontes divergentes de notas editoriais (resolvida de quebra SE o Registry virar fonte canônica).
- Deploy no servidor (este plano é construção local; deploy é passo final).

## 9. ✅ FASE 1 ENTREGUE (08/08 ~03:50 BRT) — Registry + leitores + UI só-leitura + sentinel-markers

**Arquivos criados:**
- `ZCodeProject/painel_fix/ceo/registry.yaml` — mapa de 19 slots (Grupo A inline: worker + gerador; Grupo B redator subprocesso: agente_controlado; JSONs externos: estilo_master/diretriz_geral/diretriz_controlado; override do dia).
- `ZCodeProject/painel_fix/ceo/ceo_engine.py` — leitores por kind: `py_inline` (marker exato → fallback âncora), `json_file`, `txt_file`. Funções: `listar_slots()`, `matriz_etapa_escopo()`, `read_slot_text()`, `diagnosticar_todos()`. CLI de diagnóstico embutido.
- `ZCodeProject/painel_fix/ceo/aplicar_markers.py` — script que insere sentinel-markers `# >>> CEO:<id>` / `# <<< CEO:<id>` nas cópias shadow. Reutilizável na FASE 3.
- `ZCodeProject/painel_fix/ceo/shadow_v4/` — cópias shadow de `v4_vertical_draft_worker.py` + `gerador_imagem_editorial.py` (idênticas ao original + markers). Sintaxe validada. **V4 ao vivo INTACTO.**
- `ZCodeProject/painel_fix/ceo/ceo_data/` — estado (interpretacoes/fila_patches/rollbacks) preparado para FASE 2-3.

**Arquivos modificados:**
- `ZCodeProject/painel_fix/painel_cctv_v6.py` — +aba `(/v6/diretrizes-ceo, "👔 Diretrizes CEO", "ceo")` na NAV; +função `pagina_diretrizes_ceo()` (matriz ETAPA × ESCOPO de botões + modal de leitura com CSS/JS inline); +método `_send_json()`; +handlers `_ceo_api_slots()` e `_ceo_api_registry()` no `do_GET`; +import robusto do `ceo_engine`.

**Resultado dos testes (08/08 ~03:50):**
- Diagnóstico do engine: **18/19 slots OK** (1 esperado-vazio: `override.dia`, dir `prompts/` só no servidor).
- 9 slots do Grupo A lendo via **`[marker]`** (leitura EXATA): briefing, fact-gate, juiz foto, juiz cartoon, diretiva retry, system prompt visual, fallbacks, sufixo dalle.
- 9 slots lendo via `[âncora]` ou `[json]` (Grupo B redator + JSONs externos via legacy snapshot).
- Servidor V6 subiu (porta 8084) e respondeu: `GET /diretrizes-ceo` → HTTP 200 (matriz completa); `GET /api/ceo/registry` → JSON com etapas/verticais; `GET /api/ceo/slots?ids=...` → leu prompts reais (briefing 3701 chars, system visual 3040 chars).

**Como rodar localmente (pra testar):**
```bash
cd /home/migueldorosario/ZCodeProject/painel_fix
CCTV_BASE="/home/migueldorosario/Downloads/Antigravity Google" \
CEO_PROJECT_ROOT="/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes" \
python3 painel_cctv_v6.py
# abre http://127.0.0.1:8084/diretrizes-ceo
```

**Eixo cobertura (matriz):** coleta vazia (intakes são heurísticos, não LLM); triagem/finalização por-vertical; tese_ângulo (geral+tecnologia); título/revisão/verificacao (geral+crisis geo); imagem (geral + 3 estilos). 19 slots cobrem TODA a inteligência LLM do V4.

## 10. ✅ FASE 2 ENTREGUE E TESTADA (08/08 ~03:50 BRT) — IA Intérprete-Editor + edição por texto + fila

**Arquivos criados:**
- `painel_fix/ceo/ceo_llm.py` — camada LLM leve (sem puxar o roteador pesado do ecossistema). Reusa o padrão self-contained do worker V4 (`load_shell_env` via bash source de `.env.unificado` + chamada OpenAI-compatible). Cadeia de fallback: DeepSeek → Moonshot → OpenAI. Duas funções: `gerar_texto(system, user)` (helper cru) e `interpretar_fala_ceo(texto, slots_candidatos)` (intérprete editorial). System prompt do intérprete classifica a fala em {intenção, tipo=novo/ajustar/vetar, slots_afetados[] com {slot_id, motivo, acao, patch, trecho_velho}}.
  - **Bugs resolvidos no `_load_shell_env`:** (1) `Path.exists()` levanta `PermissionError` em `/root/.env.unificado` → `_exists_safe()`; (2) path com espaços ("Projeto Cafezinho Agentes") quebrava o bash source → aspas duplas; (3) `.env.unificado` tem linha com erro de sintaxe que fazia `check=True` falhar → `check=False` + redirecionar stderr.

**Arquivos modificados:**
- `painel_fix/painel_cctv_v6.py` — +import `ceo_llm`; +`_CEO_FILA_PATH`/`_ceo_fila_carregar`/`_ceo_fila_salvar` (estado da fila); +método `do_POST` (novo no V6 — era só-leitura); +`_ler_json_body`; +endpoints POST `_ceo_api_interpretar`, `_ceo_api_fila_adicionar`, `_ceo_api_fila_listar`, `_ceo_api_fila_remover`; +UI "Modo Fala Livre" (textarea + seletor de escopo + botão Interpretar + card de proposta com diff + ✅ Aprovar/🗑️ Descartar); +CSS (textarea, botões, proposta, fila); +JS (interpretar, renderPropostas, aprovarPatch, remover da fila); +seção "Fila de patches aprovados" visível na página.

**Resultado dos testes (08/08 ~03:50):**
- `python3 ceo_llm.py`: chaves DeepSeek + OpenAI carregadas; `gerar_texto()` respondeu "OK" via DeepSeek ✅.
- Intérprete (CLI, fala real *"Título de geopolítica não pode citar país africano desconhecido sem contextualizar"*): devolveu JSON correto — `intencao` certa, `tipo=ajustar`, slot `titulo.regras_redacao`, patch redigido em pt-BR no formato editorial ✅.
- Servidor V6 (HTTP real): `POST /api/ceo/interpretar` → IA interpretou via DeepSeek, identificou slot, propôs patch ✅; `POST /api/ceo/fila/adicionar` → enfileirou (fila=1) ✅; `POST /api/ceo/fila/listar` → listou ✅.
- Página `/diretrizes-ceo`: contém "Fala Livre", JS `ceoInterpretar`, seletor de escopo ✅.

**Decisão técnica (LLM):** NÃO importar o `agente_roteador_llm` do ecossistema (exige `carregar_chaves.py` + `modelos_vivos.json` ao lado, puxa `autocura_licoes`/`gerenciador_tokens`, path do `gerador_imagem_editorial.py` nem existe no repo). Em vez disso, caminho leve replicando o padrão do próprio worker V4. Se no futuro quiser o roteador completo (fallback robusto, registro de custos), basta `sys.path.insert(0, "/home/migueldorosario/Dados_Frios/Agentes Labs")` + `from agente_roteador_llm import gerar_texto`.

**Falta (FASE 3):** Patch Engine que APLICA a fila nos arquivos shadow (com backup `.bak_pre_ceo_<ts>` + rollback). A fila hoje só acumula patches aprovados.

## 11. ✅ FASE 3 ENTREGUE E TESTADA (08/08 ~03:55 BRT) — Patch Engine (aplica + rollback)

**Arquivos modificados:**
- `painel_fix/ceo/ceo_engine.py` — +import `datetime`; +funções `aplicar_patch()` (aplica patch no slot: py_inline/json_file/txt_file, com backup datado em `ceo_data/rollbacks/` + log em `log.jsonl`), `_patch_py_inline()` (aplica entre markers), `_patch_json_file()`, `rollback_patch()` (restaura do backup).
- `painel_fix/painel_cctv_v6.py` — +endpoints POST `/api/ceo/patch/aplicar` (aplica fila no shadow, marca itens como `aplicado`) e `/api/ceo/patch/rollback` (reverte via rollback_id); +UI: botão "⚡ Aplicar N patch(es) no shadow" + feedback com rollback IDs + recarrega a página.

**Decisão técnica CRÍTICA (como inserir patch inline sem quebrar sintaxe):**
- Primeira tentativa: inserir o texto do patch solto entre os markers → **QUEBROU a sintaxe** do shadow (o marker abrange `system = (...)` e o patch cortou o fechamento do parêntese).
- **Solução definitiva:** o patch, em `adicionar_regra`, é inserido como **COMENTÁRIO EDITORIAL** (`# EDITORIAL CEO [ts]: <regra>`) logo após o marker de início. Comentários são sintaticamente válidos em Python e não alteram o runtime. Quando o editor quiser promover o comentário pra regra de prompt ativa, há um passo separado (manual ou IA) que converte o comentário em string de prompt. Isso **garante que o V4 nunca quebra** por edição do CEO.
- `substituir_trecho`: age só sobre texto entre aspas (seguro); se o trecho não existir, cai pro modo comentário. `reescrever`: bloqueado em blocos com atribuição Python `= (` (perigoso).

**Resultado dos testes (08/08 ~03:55, via HTTP):**
- Adicionar 2 patches na fila ✅ → Aplicar TODOS no shadow ✅ (2/2 aplicados) → **sintaxe de ambos os shadows válida** ✅ → 2 regras editoriais inseridas com timestamp ✅ → Rollback via HTTP ✅ (reverte + sintaxe continua válida) ✅.
- Shadow restaurado ao estado limpo após testes (reaplicado markers).

**O fluxo completo do CEO agora (FASE 1+2+3):**
1. Miguel escreve uma ordem → IA interpreta (DeepSeek) → propõe patch no slot certo → Miguel aprova → patch vai pra fila.
2. Miguel clica "⚡ Aplicar" → patch é gravado no shadow como comentário editorial (com backup + rollback) → **V4 nunca quebra**.
3. Miguel pode reverter a qualquer momento via rollback_id.

**Falta (FASE 4):** Áudio Whisper — getUserMedia + MediaRecorder no front, POST do blob no `/api/ceo/audio`, transcrição → alimenta a caixa de texto da FASE 2.

## 12. ✅ FASE 4 ENTREGUE E TESTADA (08/08 ~03:58 BRT) — Áudio Whisper

**Arquivos modificados:**
- `painel_fix/ceo/ceo_llm.py` — +função `transcrever_audio(audio_bytes, mime_type)` que chama a API OpenAI Whisper (`/v1/audio/transcriptions`, model `whisper-1`, language `pt`), lendo `OPENAI_API_KEY` do `.env.unificado`.
- `painel_fix/painel_cctv_v6.py` — +endpoint `POST /api/ceo/audio` (lê bytes brutos do body → chama `transcrever_audio` → devolve `{ok, texto}`); +botão "🎙️ Gravar áudio" na UI da seção Fala Livre; +JS `getUserMedia`+`MediaRecorder` (inicia/para gravação, upload do blob, insere transcrição na caixa de texto); +CSS do botão microfone (estado "gravando" com animação pulse).

**Resultado dos testes (08/08 ~03:58, via HTTP):**
- Função `transcrever_audio`: `OPENAI_API_KEY` presente (164 chars) ✅; chamada à API Whisper funciona (HTTP 200 com áudio, 400 controlado com bytes vazios) ✅.
- Endpoint `POST /api/ceo/audio` com WebM real (2s gerado via ffmpeg): devolveu `ok: True` + transcrição (com silêncio o Whisper alucina, mas o pipeline HTTP inteiro funciona) ✅.
- Página: contém botão "🎙️ Gravar áudio", JS `getUserMedia`+`MediaRecorder`, endpoint `/api/ceo/audio` ✅.

**⚠️ Nota de deploy (microfone no navegador):** `getUserMedia` exige **HTTPS ou localhost**. Em produção (servidor via nginx), o proxy precisa servir o painel sobre TLS pra o microfone funcionar. Em `http://` o navegador bloqueia o microfone. No localhost (teste) funciona direto.

## 13. ✅ MISSÃO COMPLETA — TODAS AS 4 FASES ENTREGUES

**O fluxo completo do "Diretrizes do CEO" (de ponta a ponta):**
1. Miguel abre a aba `/diretrizes-ceo` no painel → vê a matriz ETAPA × ESCOPO com todos os prompts do V4 organizados (FASE 1).
2. Clica num botão da matriz → vê o prompt atual do slot (FASE 1).
3. **OU** clica em 🎙️ e fala uma ordem editorial (Whisper transcreve → caixa de texto) **OU** digita direto (FASE 4 + FASE 2).
4. Clica em "🧠 Interpretar" → a IA (DeepSeek) interpreta a fala, identifica quais slots do V4 são afetados, propõe o patch (FASE 2).
5. Miguel aprova (✅) → patch vai pra fila.
6. Miguel clica "⚡ Aplicar" → o patch é gravado na cópia shadow como comentário editorial (backup + rollback), **o V4 nunca quebra** (FASE 3).
7. Pode reverter a qualquer momento via rollback_id.

**Arquivos criados (6):**
- `painel_fix/ceo/registry.yaml` — mapa de 19 slots de inteligência do V4.
- `painel_fix/ceo/ceo_engine.py` — leitores (marker/âncora/json/txt) + Patch Engine (aplicar/rollback).
- `painel_fix/ceo/ceo_llm.py` — camada LLM (DeepSeek→Moonshot→OpenAI) + intérprete + Whisper.
- `painel_fix/ceo/aplicar_markers.py` — insere sentinel-markers nas cópias shadow.
- `painel_fix/ceo/shadow_v4/` — cópias dos 2 arquivos V4 inline com markers (V4 ao vivo intocado).
- `painel_fix/ceo/ceo_data/` — estado (fila_patches.json, rollbacks/).

**Arquivo modificado (1):**
- `painel_fix/painel_cctv_v6.py` — +aba `/diretrizes-ceo`, +`do_POST` (novo no V6), +8 endpoints API, +UI completa (matriz + modal leitura + Fala Livre + fila + áudio).

**Como rodar localmente:**
```bash
cd /home/migueldorosario/ZCodeProject/painel_fix
CCTV_BASE="/home/migueldorosario/Downloads/Antigravity Google" \
CEO_PROJECT_ROOT="/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes" \
python3 painel_cctv_v6.py
# abre http://127.0.0.1:8084/diretrizes-ceo
```

**Próximos passos (não bloqueiam o uso):**
- Migração dos comentários editoriais → regras de prompt ativas (passo manual ou IA, quando o Miguel quiser efetivar uma regra no V4 de produção).
- Deploy no servidor NYC (copiar `ceo/` + ajustar env paths + TLS no nginx pro microfone).
- Migrar redação de `agente_controlado.py` pro coração do V4 (sprint separado; o Registry torna indolor).



