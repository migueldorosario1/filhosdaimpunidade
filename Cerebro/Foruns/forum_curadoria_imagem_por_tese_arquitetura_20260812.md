# 🎨 Fórum: Arquitetura de Curadoria de Imagem por Tese (V4 + Banco Ouro)

> **Tema Duplo:** este fórum (decisões) + `Memorias/memoria_curadoria_imagem_por_tese_arquitetura_20260812.md` (log técnico).
> **Origem:** ordem do Miguel (voz, 12/08/2026 ~07:40 BRT) — "a gente tem que desenvolver uma inteligência mais forte para escolher imagem... tem que criar uma tese para a imagem... sistema híbrido... quando não encontra, manda e-mail... e a gente escolhe e o sistema aprende".
> **Estado:** 📄 **ARQUITETURA DOCUMENTADA — execução pausada aguardando autorização do Miguel.** Zero código alterado nesta sessão.

---

## 🎯 Estado da missão (Regra Nº 3 §3 — sempre explícito)

### O que aconteceu
- Miguel questionou se `entidade` + `pessoas_identificadas` são redundantes na grade `/midia-ouro/grade`. Propôs unificar.
- Miguel PAUSOU a execução e ordenou: "antes de fazer qualquer coisa, tem que olhar o V4, ver se não quebra nada". Fiz 3 diagnósticos em paralelo (V4 / infra-e-mail / Cérebro).
- **Veredito:** é seguro derivar `entidade = pessoas_identificadas[0]` — o V4 **não lê `entidade`** (prova: `v4_vertical_draft_worker.py:776-920`, docstring *"jamais o campo entidade"*).
- Miguel escolheu: **(1) só documentar nesta sessão** (nada de código agora); **(2) entidade sempre editável** (pré-preenchida com `pessoas[0]`, campo visível pra correção); **(3) loop humano nos 3 canais** (Telegram + painel + e-mail).

### O que falta
- **Autorização do Miguel** pra executar a Fase 0 (unificar entidade — bloqueador, baixo risco).
- Decisão sobre a regra canônica de `pessoas[0]` em fotos com 3+ pessoas (hoje: o 1º nome digitado; futuro: pode ser proeminência visual).
- Coletar contato do **Rian** (e-mail/chat_id) — não está no cofre; loop humano hoje só alcança Miguel + Gabriel.

### O que preciso de você (Miguel)
1. **Autorizar Fase 0** quando quiser (cirúrgica, ~1h, não toca V4).
2. **Confirmar prioridade** entre Fase 1 (motor tese→imagem, aproveitando visão grátis até 15/09) e Fase 2 (loop humano multi-canal).
3. **Fornecer contato do Rian** (e-mail ou chat_id Telegram) se quiser incluí-lo no loop.

---

## ✅ Decisões canônicas (fechadas em 12/08)

1. **`entidade` = híbrida editável** — pré-preenchida com `pessoas_identificadas[0]` (estende a regra atual `painel_midia_ouro.py:374-378` que já faz isso quando há 1 pessoa); **campo permanece visível e editável** na grade pra correção em casos ambíguos (3+ pessoas, instituições).
2. **Fallback NOT NULL obrigatório** — quando `pessoas_identificadas` está vazia (instituições/locais/temas: Estreito de Hormuz, CERN, Irã...), a entidade digitada é **preservada** (não derivada). Evita violação `entidade TEXT NOT NULL`.
3. **V4 intocável nesta arquitetura** — confirmado por diagnóstico: o V4 ignora `entidade`, logo qualquer mudança lá tem impacto zero na redação.
4. **Loop humano = 3 canais em camadas:** Telegram inline buttons (push rápido, bot Augusto → Miguel+Gabriel) → painel web `/midia-ouro/grade` (fonte canônica da verdade, status `revisao_humana`) → e-mail (`enviar_baleia_azul_v2.sh` reaproveitado, fallback robusto).
5. **Sem действий automáticas destrutivas** — IA nunca bloqueia imagem sozinha; divergência → quarentena humana (alinhado ao `forum_banco_midia_v4_real_vision_autoaprendizado_20260806.md`).
6. **Aprendizado é ingestão de gold** — escolha humana vira `gold_source:human_explicit` no Corpus Ouro (mecanismo já especificado), alimenta replay/shadow/canário.

---

## 🗺️ As 4 fases (roadmap)

### 🟢 FASE 0 — Unificar entidade (bloqueador, baixo risco)
**Objetivo:** remover a sensação de redundância na grade sem quebrar nada.
**Escopo:**
- Estender regra no `painel_midia_ouro.py`: `if len(nomes)==1: entidade_override=nomes[0]` → `if nomes: entidade_override=nomes[0]` (mas só aplicar quando `pessoas_identificadas` não-vazio; se vazio, preservar entidade digitada).
- Garantir `NOT NULL` no INSERT (COALESCE p/ tema/fonte_nome quando ambos vazios).
- Backfill auditoria das ~15 linhas `uso_automatico=1` sem pessoas (confirmar entidade-instituição preservada).
- Reconciliar `midia_ouro_indice` + `midia_ouro_fts` no mesmo UPDATE.
- UI grade: campo "entidade" continua visível (decisão Miguel), pré-preenchido.
**Risco:** 🟢 baixo. Zero impacto no V4. **Esforço:** ~1h.

### 🟡 FASE 1 — Motor de tese→imagem (semântico, shadow)
**Objetivo:** escolher imagem pela **tese editorial**, não pela entidade crua.
**Entradas:** `v4_curadoria_tese` (já produz `frame_visual`, `consequencia_material`, `promessa_ao_leitor`) + título/lead da matéria.
**Pipeline:**
1. Curador formula a tese → gera uma **consulta semântica** (descrição do "visual que comunica a tese").
2. Recuperação no Banco Ouro: hoje por `entity_id`/alias → **estender com embeddings** (texto da tese ↔ descrição/legenda/tags da imagem). *Greenfield: não há CLIP/embeddings hoje.*
3. Tribunal Visual (já desenhado, `forum_banco_midia_v4_real_vision_autoaprendizado_20260806.md` §5): Qwen Vision (composição) + Gemini Vision (pertinência tese↔imagem) → score de "comunicação editorial".
4. Top-K≤3 → escolha final (auto se score alto, senão loop humano Fase 2).
**Stack:** `qwen3-vl-32b-thinking` (**grátis até 15/09**) + `gemini-2.5-flash` ($0.30 cross-check).
**Modo:** **shadow** primeiro (compara com escolha atual, não publica) → canário (10%) → promoção versionada.
**Risco:** 🟡 médio (nova camada semântica). **Esforço:** semanas. **Janela:** até 15/09 (free quota).

### 🟠 FASE 2 — Loop humano multi-canal + aprendizado
**Objetivo:** quando o motor não acha imagem com score≥limiar, acionar humano e **aprender** com a escolha.
**Canais (em camadas):**
- **(A) Telegram inline** (push): bot Augusto manda foto + tese + `reply_markup` 3 botões (`imagem_concordo_<hash>` / `imagem_outra_<hash>` / `imagem_discordo_<hash>`) → Miguel + Gabriel. Reaproveita padrão `agente_controlado.py:139-151`. **Gap:** construir listener `callback_query` (lado receptor).
- **(B) Painel web** (canônico): IA marca `status_editorial='revisao_humana'`; humano abre `/midia-ouro/grade` e aprova foto-a-foto. Já roda.
- **(C) E-mail** (fallback): `enviar_baleia_azul_v2.sh` (msmtp Gmail, já configurado) manda tese+imagem pra Miguel+Gabriel. **Gap:** link no e-mail precisa HTTPS confiável + auth.
**Auth:** endpoint `POST /api/midia-ouro/review/<hash>` hoje é **aberto** — adicionar HMAC ou token unguessable por imagem.
**Aprendizado:** escolha humana → `correcoes_YYYY-MM-DD.jsonl` → `RuleProposal` → replay no Corpus Ouro → shadow → promoção L3 (Miguel decide).
**Risco:** 🟠 médio-alto (auth + callback listener + cert HTTPS). **Esforço:** ~1 sprint.

### 🔵 FASE 3 — Teoria de escolha por vertical (documento de referência)
**Objetivo:** formalizar "quando usar mapa vs foto vs ilustração" por vertical.
**Entrega:** `Foruns/teoria_escolha_imagem_por_vertical_20260812.md` (já criado nesta sessão).
**Conteúdo:** taxonomia de tipos visuais comunicativos + regras por vertical (Geo: mapa oficial/satélite; Ciência: microscópio/telescópio; Nacional: foto real pessoa) + policy IA generativa (cota 20%, só Geo/Ciência — já existe).
**Schema:** criar coluna `tipo_entidade` (`pessoa|instituicao|local|tema|evento`) — hoje **não existe** (`PRAGMA table_info` confirma). É a chave pra o motor distinguir "foto de pessoa" de "mapa".
**Risco:** 🟢 baixo (documental). Schema novo é migração leve.

---

## ⚠️ Riscos & mitigações

| Risco | Nível | Mitigação |
|---|---|---|
| `entidade NOT NULL` violado p/ 15 linhas sem pessoas | 🔴 | Fallback: preservar entidade digitada (instituição/local/tema); nunca forçar `pessoas[0]` quando vazio |
| Endpoint `/api/midia-ouro/review/<hash>` sem auth | 🔴 | HMAC ou token por imagem antes do loop humano em produção |
| Cert HTTPS só válido p/ `43.156.151.165.sslip.io` | 🟡 | Registrar Let's Encrypt pra domínio próprio (ex: `painel.ocafezinho.com`) ou limitar botão ao sslip.io |
| `callback_query` listener não existe | 🟡 | Construir no serviço que faz `getUpdates` (ponte_cafezinho é esqueleto) |
| Ordem de `pessoas[0]` ambígua em 3+ pessoas | 🟡 | Regra canônica: 1º nome digitado (controle humano); futuro opcional: proeminência visual por IA |
| Rian sem contato no cofre | 🟡 | Coletar e-mail/chat_id; loop hoje só Miguel+Gabriel |
| Free quota `qwen3-vl` expira 15/09 | 🟡 | Construir Fase 1 em shadow antes da data; depois ouro orçamento (~$0.26/M) |

---

## 🔁 Reaproveitável vs Greenfield

### ✅ JÁ EXISTE (não reinventar)
- **`v4_curadoria_tese`** (shadow, `v4_curadoria_tese_v1.json`, `curadoria_tese.py`, 52 contract tests) — motor de tese de TEXTO com `frame_visual`.
- **Banco Ouro master** (864 mídias, schema rico: `entidade`, `pessoas_identificadas_json`, `tags`, `tema`, `metadados_json`, `hash_sha256`).
- **Tribunal Visual cooperativo desenhado** (Qwen+Gemini+Kimi vision, recibos `run_id`, fail-closed, quarentena).
- **Endpoint `POST /api/midia-ouro/review/<hash>`** (approve/reviewed/block) — **no ar**.
- **Funil C0–C7 + taxonomia `reason_code`** + **autoaprendizado governado** (ledger append-only, Corpus Ouro, replay, gates L0–L3).
- **Painel `/midia-ouro/grade`** com seleção + aprovação em lote + lightbox.
- **`enviar_baleia_azul_v2.sh`** (msmtp Gmail, SPF ok, destinatários Miguel+Gabriel).
- **Padrão Telegram inline button** provado (`agente_controlado.py`, `agente_instagram.py`).
- **Modelos vision grátis até 15/09** (`qwen3-vl-32b-thinking`, `qwen3-vl-235b-a22b-thinking`, `qwen-vl-ocr`).
- **Guarda §86** (imagem destacada obrigatória) + regra imagem única + cota IA por vertical.

### 🆕 GREENFIELD (precisa construir)
- **Match semântico tese↔imagem** (embeddings/CLIP cruzado) — o coração do pedido.
- **Coluna `tipo_entidade`** — não existe; criar + popular.
- **Teoria de escolha por vertical** — sem documento (criado nesta sessão).
- **Pipeline "tese→prompt→gerar imagem IA→validar→legenda 'ilustração'"** — hoje IA é fallback solto.
- **Campo `score_editorial` formal** p/ "quão bem comunica a tese" — conceito espalhado, sem campo canônico.
- **UI de "1 clique humano pra escolher entre N candidatas da tese"** com ingest gold (`gold_source:human_explicit`).
- **Listener `callback_query`** no Telegram.

---

## 🔗 Links canônicos (leitura obrigatória antes de executar)

- Base V4 atual: `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`
- Diagnóstico imagem + funil + autoaprendizado: `Foruns/forum_banco_midia_v4_real_vision_autoaprendizado_20260806.md`
- Consenso Trindade imagem híbrida: `Foruns/forum_arquitetura_v4_imagem_ciencia_hibrido_diretrizes_20260707.md`
- Motor de tese (texto): `Foruns/forum_v4_curadoria_tese_editorial_20260708.md` + `gpt_5_6_sol/v4_qualidade_texto_curadoria_20260710/03_contratos_editoriais/v4_curadoria_tese_v1.json`
- Guarda §86: `Memorias/memoria_sec86_guarda_imagem_obrigatoria_20260730.md`
- Mutirão Banco Mídia: `Foruns/forum_mutirao_qwen_banco_midia_v4_20260809.md`
- Teoria por vertical (criado agora): `Foruns/teoria_escolha_imagem_por_vertical_20260812.md`
- Log técnico completo desta arquitetura: `Memorias/memoria_curadoria_imagem_por_tese_arquitetura_20260812.md`

---

## 📜 Autoria
- **Quem:** ZCode (GLM-5.2 Z.ai, fallback final — Kimi/Qwen 🔴🔴 esgotados).
- **Quando:** 2026-08-12 ~10:08 BRT.
- **Origem da ordem:** Miguel (voz, sessão chat direto, workspace ZCodeProject).
- **Próxima revisão:** quando Miguel autorizar Fase 0 ou pedir detalhamento de Fase 1.
