# 🧠 Memória: Curadoria de Imagem por Tese — Diagnóstico Técnico Completo

> **Tema Duplo:** este log técnico + `Foruns/forum_curadoria_imagem_por_tese_arquitetura_20260812.md` (decisões).
> **Data:** 2026-08-12 ~10:08 BRT.
> **Autor:** ZCode (GLM-5.2 Z.ai — fallback final; Kimi/Qwen 🔴🔴 esgotados na janela 5h).
> **Origem:** ordem Miguel (voz): desenvolver inteligência forte de escolha de imagem por tese + loop humano híbrido + teoria por vertical; diagnosticar V4 ANTES de qualquer mudança.
> **Estado:** 📄 arquitetura documentada; execução pausada aguardando Miguel.

---

## 0. Resumo executivo

3 diagnósticos em paralelo (agentes Explore) confirmaram:
1. **V4 não lê `entidade`** → seguro derivar `entidade = pessoas_identificadas[0]`.
2. **Muito reaproveitável** (motor de tese em shadow, endpoint review no ar, tribunal desenhado, visão grátis 15/09).
3. **Greenfield real:** match semântico tese↔imagem (embeddings), `tipo_entidade` (coluna nova), teoria por vertical, gold-ingest humano.

Correções honestas a pistas anteriores:
- `gerenciador_imagens.py` (NYC) é **legado V3**, lê banco FTS separado, **não é o seletor do V4**. O seletor V4 é `_extract_v4_bank_photo()` em `v4_vertical_draft_worker.py:776-920`.
- `tipo_entidade` **NÃO existe** como coluna (`PRAGMA table_info(midia_ouro)` confirma). Seria nova.

---

## 1. Diagnóstico V4 × `entidade` × `pessoas_identificadas`

### 1.1 O seletor real do V4
**Arquivo:** `/root/v4_vertical_draft_worker.py` (servidor **NYC**), função `_extract_v4_bank_photo(title, summary)` linhas **776-920**.

Query-chave (linhas 793-810):
```sql
SELECT hash_sha256, entidade, pessoas_identificadas_json, titulo, r2_url, r2_portal_url,
       url_origem, fonte_url, fonte_nome, credito, licenca, data_foto, largura, altura, score
FROM midia_ouro
WHERE COALESCE(uso_automatico,0)=1
  AND pessoas_identificadas_json IS NOT NULL
  AND trim(pessoas_identificadas_json) NOT IN ('', '[]')
  AND (r2_url IS NOT NULL OR r2_portal_url IS NOT NULL)
ORDER BY ... retrato oficial ..., COALESCE(data_foto,'') DESC, score DESC
```

**Prova de que `entidade` é ignorada:**
- SELECT lista `entidade` mas **WHERE não filtra por `entidade`** (zero `=`, `IN`, `LIKE` em entidade).
- Filtra por `uso_automatico=1` + `pessoas_identificadas_json` não-vazio + tem R2.
- Depois faz parse de `pessoas_identificadas_json` → nomes → aliases (nome completo, sobrenome ≥4 letras, primeiro nome ≥5 letras) → regex word-boundary contra o **título dobrado** (linhas 812-842).
- Docstring (linhas 783-784): *"pessoa identificada explícita no TÍTULO (mais longo primeiro), **jamais o campo entidade**"*.
- `_same_person()` (683-696): *"Compara formas canônicas e formas civis **sem usar o campo entidade**"*.

### 1.2 De onde vem a "entidade" do V4?
**Não vem parâmetro.** Assinatura é `_extract_v4_bank_photo(title, summary)`. A entidade é **extraída do TÍTULO em runtime**. `select_candidate` (linha 1575) escolhe pauta por score/frescor no SQLite da vertical, sem ler `entidade`.

### 1.3 Mapa entidade→vertical — só no painel, NÃO no V4
- Presente em `/root/painel_midia_ouro.py:101-113` (Tencent) como `_SQL_VERTICAL_CASE`, comentário *"Espelha ENTIDADES_VERTICAL_V4 do robo_banco_ouro_midia_v3.py"*.
- Source-of-truth: `ENTIDADES_VERTICAL_V4` em `/root/V3/robo_banco_ouro_midia_v3.py:335` (Tencent), lista de dicts Python.
- **grep no NYC** (`v4_vertical_draft_worker.py` + `v4_labs/codigo/*.py` + `agente_controlado.py`) por `ENTIDADES_VERTICAL_V4`/`_SQL_VERTICAL_CASE`/`THEN .geopolitica` → **vazio**. O V4 decide vertical pelo DB de intake (`CONFIG` linhas 35-63), não pela entidade.

Entidades mapeadas (Tencent, só exibição de fila):
- **geopolitica:** Trump, Xi Jinping, Milei, Macron, Putin, Zelensky, Sheinbaum, Guterres, Pezeshkian, Netanyahu, Starmer, Khamenei, Modi, Erdogan, Merz, Rubio, Lavrov, Vance, Wang Yi, Araghchi, Sybiha, Rutte, Hegseth, Bessent.
- **tecnologia:** Elon Musk (+ Altman/Huang/Nadella/Zuckerberg/Cook/Pichai; Tesla/Nvidia/Meta).
- **ciencia:** **NENHUMA** no mapa. Cai no `ELSE 'nacional'`.

### 1.4 Classificação de risco — `entidade = pessoas[0]`

| Ponto de consumo | Localização | Class | Justificativa |
|---|---|---|---|
| `_extract_v4_bank_photo` | NYC draft_worker:793-826 | 🟢 | V4 ignora `entidade`; casa por pessoas×título |
| `v4_vertical_redactor_runtime` | NYC | 🟢 | grep `midia_ouro`/`entidade`/`pessoas_identificadas` → vazio |
| `_registrar_falta_banco` | NYC draft_worker:756 | 🟢 | Grava **título** em `/root/agent_data/banco_ouro_faltas.jsonl`, não entidade |
| `_extract_wp_library_photos` | NYC draft_worker:1106-1166 | 🟢 | Extrai entidade do TÍTULO localmente, sem DB |
| Mapa entidade→vertical | — | 🟢 | Fora do V4 |
| `review_payload` PARTITION BY entidade | painel:143,147,152,183 | 🟡 | Reshuffle visual da fila; não V4 |
| `_SQL_VERTICAL_CASE` (exibição) | painel:101-113 | 🟡 | String nova precisa bater nos CASEs p/ rótulo vertical no painel |
| `active_search_payload` LIKE | painel:236,251-257 | 🟡 | Continua funcionando (OR em vários campos) |
| `entidade TEXT NOT NULL` p/ 15 linhas sem pessoas | schema | 🔴 | Se forçar `pessoas[0]` com pessoas vazia → viola NOT NULL |

### 1.5 As 15 linhas não-pessoa (`uso_automatico=1`, sem pessoas)
`Estreito de Hormuz`×3, `CERN`×2, `Energia solar`, `Estação Espacial Internacional`, `Fiocruz`, `Fusão nuclear`, `Instituto Butantan`, `Irã`, `James Webb Space Telescope`, `Microscopia`, `Satélite Copernicus`, `arroz`.

Estas **já são invisíveis ao V4** (cláusula `WHERE pessoas_identificadas_json NOT IN ('','[]')` as exclui), mas o INSERT/UPDATE do catálogo quebra se a migração forçar entidade de pessoas vazias. **Solução:** fallback preserva entidade digitada.

### 1.6 Entidades compostas (~15 linhas, risco 🟡 p/ display)
`Donald Trump e Lula`×3, `Lula e Trump`×2, `Boulos, Alckmin e Lula`, `Xi Jinping, Lula e Janja`, `Claudia Sheinbaum, Lula`, `Flávio Bolsonaro e Marcos Rogério`. Para estas, `pessoas[0]` depende da ordem digitada — regra canônica necessária (definida: 1º nome digitado).

### 1.7 BÔNUS CRÍTICO — o painel já faz `entidade = nomes[0]`
`/root/painel_midia_ouro.py:374-378` (Tencent):
```python
# 2026-08-06 (Kimi K3, ordem Miguel): 1 pessoa identificada → a ENTIDADE segue a pessoa
entidade_override = None
if len(nomes) == 1:
    entidade_override = nomes[0]
```
**A proposta do Miguel é estender `len(nomes)==1` → `if nomes:`.** Evolução de comportamento existente, não virada de chave.

### 1.8 Stats do banco (Tencent, ao vivo 12/08)
- 864 linhas totais; **420** com `uso_automatico=1`; **109** entidades distintas.
- 405 com pessoas identificadas / **15** sem pessoas.
- `tipo_entidade` **NÃO EXISTE** (`PRAGMA table_info(midia_ouro)`).

---

## 2. Diagnóstico infra (e-mail / notificação / endpoint)

### 2.1 E-mail — a memória do Miguel estava incorreta
**Não há `info@mokareader` SMTP.** `mokareader.com` é app Next.js (Vercel), não remetente. O SMTP real:
- **`/etc/msmtprc`** no Tencent (43.156.151.165): account `cafezinho`, host `smtp.gmail.com:587`, `from migueldorosario@gmail.com`. Senha (app password Gmail) no arquivo — não exibida.
- `.env` local e `.env.unificado` (Tencent) **zero** chaves `SMTP_`/`MAIL_`/`RESEND`/etc. Só LLMs.
- MTA: `msmtp` + `mail` (BSD mailutils) + `sendmail`. Log `/var/log/msmtp.log`.

### 2.2 Único emissor SMTP do ecossistema
`/home/migueldorosario/Downloads/Antigravity Google/scratch/enviar_baleia_azul_v2.sh` (boletim Baleia Azul, 2×/dia). Linha 188:
```bash
echo "$CORPO" | ssh -p 38422 ubuntu@43.156.151.165 "mail -s '$ASSUNTO' -a 'From: migueldorosario@gmail.com' $DESTINATARIOS"
```
- Método: SSH→Tencent→`mail`→msmtp→Gmail.
- From real no envelope desde 07/08 (antes `ubuntu@...` caía no spam).
- Destinatários hardcoded (linha 182): `migueldorosario@gmail.com gabrielbarbosa9001@gmail.com gabrielbarbosa@ocafezinho.com`.
- Também envia pro Telegram (linhas 194-224) via `curl api.telegram.org`.
- Tem `BALEIA_DRY_RUN=1`.

### 2.3 Endpoint webhook — JÁ EXISTE, público, no ar
`POST /api/midia-ouro/review/<hash_sha256>` → proxy_pass nginx `127.0.0.1:8091` (Tencent). Função `apply_review()` (`painel_midia_ouro.py:364`):
- `action:"approve"` → marca `uso_automatico`
- `action:"reviewed"` → `revisao_humana`
- `action:"block"` → `bloqueada`

**Gaps de segurança:**
- **Sem auth** — `BaseHTTPRequestHandler` puro, sem token/API-key. Quem souber o `<hash>` (SHA256 da imagem — previsível) consegue forjar approve/block. 🔴
- **HTTPS:** cert Let's Encrypt só válido p/ `43.156.151.165.sslip.io`. IP cru = 404/mismatch; HTTP funciona mas e-mail bloqueia link suspeito.

### 2.4 Telegram inline buttons — padrão provado
- `ponte_cafezinho.py` **NÃO** suporta inline keyboards (só texto/foto, whitelist rígida só Miguel).
- **MAS** o padrão é provado em:
  - `scratch/reuniao_trindade_v4_20260809/agente_controlado.py:139-151` — 3 botões `wp_audit_publish_/draft_/trash_<post_id>` via `reply_markup`+`callback_data`.
  - `.codex_work/agente_instagram.py:332-337` — `social_approve:instagram:/cancel:`.
- Ambos usam bot **Augusto** (`TELEGRAM_TOKEN_AUGUSTO`) → `chat_id 1894890759` (Miguel).
- **Gap:** não encontrei listener `answerCallbackQuery`/`getUpdates` com `callback_query` ativo. O envio do teclado é provado; o handler do clique precisa ser construído.

### 2.5 Bots no cofre (`.env.unificado`)
`AUGUSTO`, `GABRIEL`, `MAPARIO_MAIRA`, `MAYRA_PRAIA`, `MILLER`, `MUNDO_TRILHOS`, `ZIZI`. **Não há** `TELEGRAM_TOKEN_RIAN` nem `TELEGRAM_TOKEN_MIGUEL` (chat_id Miguel hardcoded).

### 2.6 Quem são Gabriel e Rian
- **Gabriel Barbosa** — editor Cafezinho. E-mail `gabrielbarbosa9001@gmail.com` + `gabrielbarbosa@ocafezinho.com` (já destinatários Baleia Azul). Tem bot próprio (`TELEGRAM_TOKEN_GABRIEL`). ✅ no loop.
- **Rian** — handle `rhyandemeira`, autor de publis no ocafezinho (página WP 264513). **Sem e-mail/chat_id no cofre.** 🔴 precisa coletar.

---

## 3. Diagnóstico Cérebro (histórico + modelos)

### 3.1 Documentos base (leitura obrigatória)
1. `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md` — cadeia viva V4.
2. `Foruns/forum_banco_midia_v4_real_vision_autoaprendizado_20260806.md` — 13 lições + funil C0-C7 + tribunal + autoaprendizado. **O mais rico.**
3. `Foruns/forum_arquitetura_v4_imagem_ciencia_hibrido_diretrizes_20260707.md` — consenso Trindade (imagem como etapa editorial).
4. `Foruns/forum_v4_curadoria_tese_editorial_20260708.md` — motor de tese aprovado em shadow.
5. `Memorias/memoria_sec86_guarda_imagem_obrigatoria_20260730.md` — guarda 4 camadas.

### 3.2 Mutirão Banco Mídia V4 (~09/08)
- Master = Tencent `/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db` (SQLite WAL). Réplica NYC read-only. Sync Tencent→NYC.
- Estado 09/08: 841 mídias / 265 `uso_automatico` (depois Etapas 0-4).
- Funil 353/353 FECHADO p/ Senado.
- Tribunal visual vivo: Qwen Vision + Gemini Vision, budget 120 chamadas/dia, quarentena em divergência.
- Pendências: 21.390 linhas `gemini_vision_erro` (taxonomia pendente), Etapa 5 pausada.

### 3.3 Motor de tese `v4_curadoria_tese`
Contrato: `gpt_5_6_sol/v4_qualidade_texto_curadoria_20260710/03_contratos_editoriais/v4_curadoria_tese_v1.json`.
- Princípio `"imagem_le_frame_visual_da_curadoria": true`.
- Campo `frame_visual` = `{entidade_principal, conflito_visual, evitar, prioridade}`, `prioridade_enum: [pessoa, instituicao, documento, setor_produtivo, infraestrutura]`.
- Etapa `curadoria` entre `auditado` e `producao`; agente `imagem` lê de `curadoria`, não de `auditado` cru.
- **A arquitetura JÁ prevê que a imagem vem da tese** — mas `frame_visual` hoje é só declaração de prioridade. O motor "tese→varrer Banco Ouro→achar imagem que comunica" **não existe** = greenfield.
- Código: `curadoria_tese.py` (espelho `gpt_5_6_sol/.../04_codigo_contexto/`).

### 3.4 Embeddings — ZERO implementação
- "embedding" aparece como **proposta** em 2 lugares (texto, não imagem): `forum_v4_curadoria_tese_editorial_20260708` (sentence-transformers p/ repetição de parágrafo) e `forum_banco_midia_v4_real_vision_autoaprendizado_20260806 §4.4 Fase B`.
- **Não há CLIP, não há qwen3-vl embedding cruzado, não há índice vetorial do Banco Ouro.** Greenfield confirmado.

### 3.5 Policy de imagem (vinculante)
- `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` **§86**: imagem destacada OBRIGATÓRIA; regra imagem única (não repetir no corpo).
- IA generativa: **só Geopolítica/Ciência** (cota 20%/4h Geo, livre Ciência); **zero IA em Nacional/Regional/temáticos**; rostos políticos sensíveis nunca por IA. Mapa factual = oficial ou determinístico, **não IA** (`forum_mutirao_qwen_banco_midia_v4_20260809 §7-8`).
- Identidade: visão computacional **não prova** identidade nem licença; exige metadado oficial/legenda; homônimos tratados explicitamente.

### 3.6 Modelos LLM multimodais disponíveis (catálogo)
- **Visão composição (GRÁTIS até 15/09):** `qwen3-vl-32b-thinking`, `qwen3-vl-235b-a22b-thinking` (conta `aiatolahnews`).
- **OCR:** `qwen-vl-ocr-2025-11-20` (grátis até 15/09).
- **Pertinência semântica:** `gemini-2.5-flash` ($0.30) / `gemini-2.5-pro` ($1.00).
- **Curador/tese:** `qwen3-max`, `gemini-2.5-pro`, `gpt-4o`.
- **Visão primária atual:** `qwen-vl-plus` ($0.26, free quota esgotou 09/08) / `qwen-vl-max` (NÃO usar `-latest`, dá 403).
- **Editor top-3:** `kimi-vision` (`KIMI_VISION_API_KEY`, sincronizada 01/08).
- **A evitar:** `glm-4.6v-flash` (inútil p/ PT), `moonshot-v1-8k-vision` (vazamento chinês).

### 3.7 Baleia Azul (contexto)
- Boletim diário 2×/dia (08h/18h), e-mail Miguel+Gabriel. Editor integral = assento ZCode (modelo-agnóstico) desde 07/08. **Não é motor de decisão**; é síntese/diagnóstico. Pode ser canal de telemetria do motor de tese (reportar pendências), não o motor.

---

## 4. Schema proposto (Fase 3)

Nova coluna em `midia_ouro`:
```sql
ALTER TABLE midia_ouro ADD COLUMN tipo_entidade TEXT;
-- valores: 'pessoa' | 'instituicao' | 'local' | 'tema' | 'evento' | 'documento'
```
- **População:** default `'pessoa'` quando `pessoas_identificadas_json` não-vazio; `'instituicao'`/`'local'`/`'tema'` para as 15 linhas conhecidas (backfill manual); NULL enquanto não classificado.
- **Uso futuro:** o motor de tese lê `tipo_entidade` pra saber se busca "foto de pessoa" vs "mapa" vs "documento". É a chave que falta pra `frame_visual.prioridade` ser acionável.
- **Compatibilidade:** coluna nova nullable → não quebra nada existente.

Campo canônico de score de comunicação (greenfield):
- `score_editorial` formal (conceito espalhado hoje). Proposta: `score_comunicacao_tese INTEGER` preenchido pelo motor Fase 1, 0-100, "quão bem esta imagem comunica a tese".

---

## 5. Decisões técnicas concretas (recap)

1. **Regra pessoas[0] híbrida:** `if nomes: entidade_override=nomes[0]` (estende linha 374-378 do painel), campo editável permanece.
2. **Fallback NOT NULL:** quando `pessoas` vazio, entidade digitada preservada; nunca gravar NULL/''.
3. **3 canais em camadas:** Telegram (A, push) > painel web (B, canônico) > e-mail (C, fallback). Endpoint comum: `POST /api/midia-ouro/review/<hash>` + HMAC (a adicionar).
4. **Shadow primeiro:** motor Fase 1 nunca publica direto; compara com escolha atual, depois canário 10%, depois promoção L3 (Miguel decide).
5. **Fail-closed:** divergência IA → quarentena humana, nunca block automático.

---

## 6. Próximos passos acionáveis (quando Miguel autorizar)

**Fase 0 (~1h, bloqueador):**
1. Backup datado local + Tencent do `painel_midia_ouro.py`.
2. Editar linha 374-378: `if len(nomes)==1` → `if nomes:`.
3. Garantir fallback NOT NULL no INSERT/UPDATE.
4. Auditoria SELECT das 15 linhas não-pessoa (confirmar preservadas).
5. Reconciliar `midia_ouro_indice` + `midia_ouro_fts`.
6. Restart `midia-ouro-panel.service`; smoke curl; confirmar V4 intacto.

**Fase 1 (semanas, até 15/09):**
1. Definir contrato do `motor_curadoria_imagem_tese` (consome `frame_visual`).
2. Prototipar embeddings (CLIP ou `qwen3-vl` embedding) + índice vetorial Banco Ouro.
3. Implementar score de "comunicação editorial" (Gemini cross-check).
4. Shadow mode: comparar top-3 do motor vs escolha atual, logar divergências.
5. Canário 10% → promoção L3.

**Fase 2 (~1 sprint):**
1. Auth HMAC no endpoint review.
2. Listener `callback_query` (serviço novo ou extensão da ponte).
3. Template do inline keyboard (3 botões) reaproveitando `agente_controlado.py`.
4. Template do e-mail fallback reaproveitando `enviar_baleia_azul_v2.sh`.
5. Ingest gold (`gold_source:human_explicit`) no Corpus Ouro.

**Fase 3 (documental + schema leve):**
1. `teoria_escolha_imagem_por_vertical_20260812.md` (✅ já criado).
2. `ALTER TABLE midia_ouro ADD COLUMN tipo_entidade` + backfill.
3. `score_comunicacao_tese` (com Fase 1).

---

## 7. Incidentes / correções honestas

- **Pista errada corrigida:** `gerenciador_imagens.py` foi descrito (por agente anterior) como seletor do V4. **Falso** — é legado V3, lê banco FTS separado, não é importado pelo V4. Seletor real: `_extract_v4_bank_photo`.
- **Pista errada corrigida:** `tipo_entidade` foi descrita como coluna existente. **Falso** — `PRAGMA table_info` nega. É coluna nova a criar.
- **Bug já corrigido:** `gerenciador_imagens.py` truncava `candidatas[:4]` → corrigido para `[:8]` em 06/08 (backup `.bak_pre_truncamento_20260806`).

---

## 📜 Autoria
ZCode (GLM-5.2 Z.ai, fallback final — Kimi/Qwen 🔴🔴). 2026-08-12 ~10:08 BRT. Workspace ZCodeProject. Origem: ordem Miguel (voz). Diagnósticos via 3 agentes Explore em paralelo. Nenhuma alteração em código/banco/servidor — só documentação.
