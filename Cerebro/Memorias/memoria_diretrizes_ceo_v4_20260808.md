# MEMÓRIA — Diretrizes do CEO (nova aba do painel CCTV V6) — 2026-08-08

> [!CAUTION]
> **ARQUITETURA SUPERADA EM 09/08/2026.** Este arquivo preserva o retrato histórico anterior ao corte V4. Toda afirmação abaixo que trate `agente_controlado.py` como redator, subprocesso ou componente do V4 perdeu validade operacional. A referência canônica atual é `memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

> **Tema Duplo:** log técnico companion do `Foruns/forum_diretrizes_ceo_v4_20260808.md`.
> **Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan) — chat direto — 2026-08-08 ~03:30 BRT.

## 1. Contexto da missão

O Miguel (CEO/diretor-geral) quer um **espaço de interação entre ele e os prompts/diretrizes espalhados pelo V4**, via uma nova aba do painel CCTV. Ele fala (áudio) ou escreve uma ordem editorial → uma IA interpreta → identifica quais slots de inteligência do V4 são afetados → propõe patch → ele confirma → aplica no arquivo físico certo, com rollback e registro.

Ver fórum companion para decisões e desenho. Esta memória guarda o **mapeamento técnico** (comando para reproduzir) e o **estado executável**.

## 2. Mapeamento da inteligência do V4 (~25 slots) — COMANDOS PRA REPRODUZIR

### Grupo A — V4-canônico (orquestrador + imagem)

**`/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_vertical_draft_worker.py`** (107 KB / 2032 linhas):
- `write_briefing` (~linha 1664) — briefing central: originalidade, atribuição, voz própria, regra Lula/Poder360, formato de título, **ramo POR-VERTICAL** (tecnologia→ângulo geopolítico). Global + ramo vertical.
- `factual_late_gate` (~1607) — fact-gate tardio: system+user prompt do verificador factual final (evidências vencem). Global + modo "crisis" só geopolítica.
- `extract_factual_claims` (~1442) — extrai claims via regex (não-LLM).
- `_verifier_llm_json` (~1466) — helper verificador com cadeia GLM→DeepSeek→Moonshot.
- `_audit_original_photo` (~633) — juiz foto original (logo/banner/genérica/pessoa errada).
- `audit_generated_cartoon` (~857) — juiz cartoon IA; contém "REGRA DE TEXTO INQUEBRÁVEL". Global.
- `_visual_judge`/`_kimi_visual`/`_qwen_visual` (~165/75/117) — helpers juízes multimodais (sem prompt próprio).
- Diretiva de retry (~761-765) — "evite bandeiras/mapas/brasões" em tentativas 2+. Global.

**`/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/gerador_imagem_editorial.py`** (26 KB / 561 linhas):
- `SYSTEM_PROMPT_VISUAL` (~76) — system prompt visual + **3 estilos editoriais** (A: política; B: tecnologia; C: geopolítica). Por-vertical.
- `_gerar_prompt_visual` (~130) — gera prompt visual em inglês. Global (seção repassada).
- `fallbacks` (~134-155) — prompts hardcoded por seção (politica/geopolitica/tecnologia). Por-vertical.
- `_chamar_dalle` (~352) — sufixo "No text, no letters, no words". Global.

**`/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_vertical_intake.py`** (12 KB / 243 linhas): 100% heurístico (regex/keyword). Sem LLM. `ROOT = Path("/root/agent_data/v4_verticals")`.

### Grupo B — Redator subprocesso (`agente_controlado.py`) — invocado pelo V4 como subprocesso (`AGENT="/root/agente_controlado.py"`, worker linha 65)

⚠️ Apesar do nome V1, **é o redator de produção atual** do V4. A maior parte dos botões de inteligência mora nele e nos JSONs externos. Caminho local (legacy snapshot): `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/` (se existir) ou buscar em legacy.
- `load_estilo_master` (~2188) → carrega `/root/agent_data/estilo_master.json` (system_redacao, system_revisao, system_media_reader, system_redacao_opiniao_extra). Global.
- `_estilo_master_fallback` (~2212) — fallback inline. Global.
- `system_prompt()` (~2264) — compositor central: estilo_master + editorial_notes + diretriz_controlado + extra opiniao + diretriz_geral + override do dia.
- `SECTIONS[*]['editorial_notes']` (~297/374/454/559) — notas editoriais POR-VERTICAL (politica/economia/ciencia/geopolitica).
- `load_prompt_override` (~2246) → carrega `/root/prompts/{section}_{hoje}.txt`, `{section}.txt`, `geral_{hoje}.txt`, `geral.txt`. Global + por-vertical.
- `current_diretriz_text`/`DIRETRIZ_GERAL_FILE` (~1131/198) → `/root/agent_data/diretriz_geral.json`. Global.
- `DIRETRIZ_CONTROLADO_FILE` (~199) → `/root/agent_data/diretriz_controlado.json`. Global.
- `gerar_noticia` (~3052) — user prompt de redação principal: originalidade, regras de vídeo/transcrição, alerta de alucinação geopolítica, **regras de TÍTULO** (8 palavras, sentence case, exemplos). Global.
- Revisão (~2073) — "editor final reescreve"; auditoria editorial (~2101); correção (~2140). Global.
- Queries de busca (~1272). Por-vertical.
- Triagem relevância (~2839). Por-vertical.
- `classify_metadata`/`classify_categories_keywords`/`classify_tags_keywords` (~3120/3181/3240). Por-vertical.
- `extract_themes_for_image` (~3448), `llm_choose_image` (~3509), `generate_image_prompt` (~3567). Global.

### JSONs/TXT externos (servidor `/root/agent_data/` e `/root/prompts/`; só legacy snapshot local de 09/jun)
- `estilo_master.json` (21 KB) — keys: versao/updated_at/identidade/titulo/...
- `diretriz_geral.json` (9,2 KB) — keys: versao/linha_editorial/enquadramento/...
- `diretriz_controlado.json` (2,4 KB) — keys: versao/modo/linha_editorial/flexibilidades_permitidas/...
- `briefing_execucao.json` — sem cópia limpa local; usar `briefing_execucao_reconstruido_d67ec.json` do legacy como mock.
- `prompts/*.txt` — não existe local.

## 3. Arquitetura do painel CCTV (alvo da feature)

- **V6 (`painel_cctv_v6.py`, porta 8084) = VIVO.** nginx redireciona quase tudo pra V6 em `/v6/`. V5 (8082) obsoleto/quebrado.
- **V6 = somente-leitura** (sem `do_POST`, sem `/api/`). Toda escrita está no V5.
- Python puro (`http.server.BaseHTTPRequestHandler`, `ThreadingHTTPServer`), sem framework. Roteamento: dict `ROUTES` (V6 ~linha 1419). Nav bar: constante `NAV` (~419-430). Renderização: `chrome(titulo, active, conteudo)` (~502-525). HTML/CSS/JS 100% inline em f-strings.
- Padrão de POST (no V5, pra copiar): `do_POST` (~2628), `int(self.headers.get("Content-Length",0))`+`self.rfile.read(...)`, `parse_qs`, `_send_json(self,data)` (~2805), persiste JSON em `agent_data/`.
- **Áudio Mural = placeholder morto:** `_handle_mural_audio` (V5 ~2696) retorna "não implementado"; `launchRecorder()` nem existe. → construir `getUserMedia`+`MediaRecorder` do zero.
- `BASE_DIR` default V6 = `/home/ubuntu/cafezinho/...` (servidor); local é cópia de trabalho. `AGENT_DATA = BASE_DIR/"root"/"agent_data"`.

## 4. Estrutura a criar/modificar

```
ZCodeProject/painel_fix/
├── painel_cctv_v6.py              ← MODIFICAR: +aba, +do_POST, +handlers
└── ceo/                           ← NOVO módulo
    ├── registry.yaml              ← mapa de inteligência (~25 slots)
    ├── ceo_engine.py              ← leitores/escritores/interprete/patch
    └── ceo_data/                  ← estado (runtime)
        ├── interpretacoes.json
        ├── fila_patches.json
        └── rollbacks/
```

## 5. Schema do Registry (resumo)

```yaml
version: 1
verticais: [geral, politica, geopolitica, ciencia, regional]
etapas: [coleta, triagem, tese_angulo, titulo, draft_corpo, revisao, verificacao, imagem, finalizacao]
slots:
  - id: <único>
    etapa: <etapa>
    escopos: [<escopos>]
    titulo: "<humano>"
    alvo:
      kind: py_inline | json_file | txt_file
      arquivo: "<path relativo>"
      simbolo: <nome função>     # py_inline
      marker: "<id>"             # py_inline sentinel
      chave: <json key>          # json_file
```

## 6. Endpoints (novo `do_POST` no V6)

| Método+Path | Função |
|-------------|--------|
| `GET /diretrizes-ceo` | Página (matriz + modos) |
| `GET /api/ceo/registry` | slots + texto atual lido em tempo real |
| `POST /api/ceo/audio` | blob `.webm` → Whisper → texto |
| `POST /api/ceo/interpretar` | `{texto}` → `{slots_afetados[], patches[]}` |
| `POST /api/ceo/patch/aprovar` | adiciona à fila |
| `POST /api/ceo/patch/aplicar` | aplica fila (backup+write+diff) → `{resultado, rollback_id}` |
| `POST /api/ceo/patch/rollback` | reverte |

## 7. Estado da missão (executável)

- **O que aconteceu:** desenho aprovado; mapeamento completo; fórum+memória+nodos+monitor criados.
- **O que falta:** executar FASE 1 (Registry + leitores + UI leitura + sentinel-markers em cópia shadow) → FASE 2 (IA Intérprete + texto) → FASE 3 (Patch Engine) → FASE 4 (Áudio).
- **Risco ativo:** sessão "V4 Home 10%/20%" mexe no `v4_vertical_draft_worker.py` hoje → FASE 1 sentinel-markers em **cópia shadow**; ler MONITORAMENTO antes de qualquer apply ao vivo.
- **Reversão (do checkpoint de desenho):** N/A — ainda não houve modificação em código de produção.

## 8. Próximo passo da próxima conversa

Retomar pela **FASE 1**: criar `painel_fix/ceo/registry.yaml` (mapear os ~25 slots), `ceo_engine.py` (leitores por kind), e estender `painel_cctv_v6.py` com a aba `/diretrizes-ceo` + `do_POST` + `GET /api/ceo/registry`. Sentinel-markers em cópia shadow de `v4_vertical_draft_worker.py` (NÃO ao vivo).

---

## ✅ ATUALIZAÇÃO FINAL (08/08 ~03:58) — MISSÃO COMPLETA, 4 FASES ENTREGUES

**Todas as 4 fases construídas e testadas via HTTP.** Ver fórum companion §9-13 para detalhes completos de cada fase.

### Resumo executivo do que foi entregue

Nova aba `/diretrizes-ceo` no painel CCTV V6 onde o Miguel (CEO) interage com os prompts espalhados do V4:

1. **FASE 1 (Registry + leitura):** matriz ETAPA × ESCOPO de botões; 19 slots indexados; leitura exata via sentinel-markers (9 slots do Grupo A) + âncora/json/txt (resto). V4 ao vivo intocado (cópias shadow).
2. **FASE 2 (IA Intérprete):** Miguel escreve uma ordem → IA (DeepSeek) interpreta, identifica slot, propõe patch → aprova → fila.
3. **FASE 3 (Patch Engine):** aplicar fila no shadow como comentário editorial (`# EDITORIAL CEO [ts]: <regra>`) — **sintaxe sempre válida, V4 nunca quebra**. Backup + rollback via HTTP.
4. **FASE 4 (Áudio Whisper):** 🎙️ grava → Whisper transcreve (pt-BR) → insere na caixa de texto → alimenta FASE 2.

### Arquivos finais
- **Criados (6):** `painel_fix/ceo/registry.yaml`, `ceo_engine.py`, `ceo_llm.py`, `aplicar_markers.py`, `shadow_v4/` (2 arq c/ markers), `ceo_data/` (fila + rollbacks).
- **Modificado (1):** `painel_fix/painel_cctv_v6.py` (+aba, +`do_POST` novo no V6, +8 endpoints API, +UI completa).

### Como rodar
```bash
cd /home/migueldorosario/ZCodeProject/painel_fix
CCTV_BASE="/home/migueldorosario/Downloads/Antigravity Google" \
CEO_PROJECT_ROOT="/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes" \
python3 painel_cctv_v6.py
# abre http://127.0.0.1:8084/diretrizes-ceo
```

### Decisão técnica crítica registrada
Patch inline entra como **comentário editorial** (não como texto solto) — isso garante que a sintaxe Python do V4 nunca quebra por edição do CEO. Um passo separado promove comentário → regra de prompt ativa.

### Próximos passos (não bloqueiam uso)
- Deploy no servidor NYC (copiar `ceo/`, ajustar env paths, TLS no nginx pro microfone funcionar em produção).
- Migração comentário-editorial → regra ativa (quando o Miguel quiser efetivar).
- Migrar redação de `agente_controlado.py` (V1-nome) pro coração do V4 (sprint separado; Registry torna indolor).
