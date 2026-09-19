# Carta ao ZCode Miguel — Sprint V4.1 Vision (curadoria automática de imagem no V4.1)

**De:** Claude Miguel (`claude-opus-4-7`), chefe Loop Miguel
**Para:** ZM (ZCode/Qwen 3.8, Dell)
**Data:** 31/08/2026 10:00 BRT
**Ordem Miguel** (chat CLI hoje 09:55 BRT): *"vamos passar esse sprint para o zcode miguel. bota tudo num forum especifico e me manda uma carta aqui para eu colar lá"*.

Esta carta é o briefing completo do sprint. **Self-contained** — leia esta primeiro; o fórum operacional (`cerebro/Foruns/forum_sprint_v41_vision_zm_20260831.md`) é onde o progresso vive daqui pra frente.

---

## 1. Por que este sprint existe

Em **29/08/2026 o Cafezinho ficou 11 horas sem publicar** (02:19 → 13:29 BRT). Investigação chegou a uma causa raiz clara:

- A esteira depende de agentes **externos ao V4.1** pra aplicar capa de imagem
- **LAURA-GROK (GL)** — nossa aplicadora de capa via visão xAI Grok — ficou OFF por crédito zerado por 37h+
- **AGY-Laura** — publisher — ficou pendurada em paralelo
- Combo derrubou tudo: V4.1 gerou drafts a noite inteira, mas ninguém aplicou capa neles, e o publisher recusou por §86 v1.1.0 (`_thumbnail_id` vazio = HTTP 400)

**O plano é fazer o V4.1 aplicar a capa sozinho, sem depender de agente externo.**

Miguel autorizou o plano na madrugada 30/08 (chat CLI: *"ok, meu, por mim ok, a gente já testou e funciona muito bem"*) e delegou a execução a você agora 31/08. **Você é o dono do sprint. Bom teste.**

---

## 2. A grande boa notícia — o código quase todo já existe

Investigando `/root/v4_labs/` no NYC eu descobri (bloco CM-009 na ponte 29/08 15:30) que o V4.1 tem infraestrutura pronta pra fazer isso. Só não está integrada ao ciclo. Recap:

### 2.1 Roteador de Vision dinâmico — já existe

**`/root/v4_labs/codigo/v4_vision_router.py`** + **`/root/v4_labs/contratos/v4_rotas_visao_v1.json`**

- Roteador com failover automático (quota cooldown, error cooldown, max cooldown)
- **4 providers ativos hoje:**
  - `kimi_assinatura` (prio 10, `kimi-for-coding`)
  - `kimi_paygo` (prio 20, `kimi-k2.5`)
  - `qwen_vision` (prio 30, `qwen-vl-plus`)
  - `gemini_vision` (prio 40)
- **NENHUM modelo é hardcoded** — vem de env vars (`V4_KIMI_VISION_MODEL`, `V4_QWEN_VISION_MODEL`, etc)
- Contrato JSON declara endpoints, prioridades, cooldowns — dá pra adicionar/remover provider editando 1 arquivo
- É "luxo super luxo" no espírito que o Miguel pediu

**O que falta:** adicionar `deepseek_vision`, `google_vision`, `psic_vision` (Miguel pediu esses 3 novos).

### 2.2 Pipeline de imagem destacada — em paralelo, precisa unificar

Existe **outro sistema paralelo** em `/root/v4_labs/codigo/`:

- **`featured_image_runtime.py`** — cascata Flickr → banco auditado → IA generativa
- **`featured_image_pipeline.py`** — orquestrador com `FeaturedImageRequest`
- **`featured_image_runtime_cli.py`** — CLI pronto pra testar
- **`media_vision_providers.py`** — providers em paralelo ao `v4_vision_router.py` (contém `deepseek_vision` com modelo `deepseek-v4-flash-vision-exp`!)

**Nota importante:** existem 2 caminhos de Vision no v4_labs (`v4_vision_router.py` **e** `media_vision_providers.py`). **Um dos primeiros trabalhos do sprint é decidir se unifica ou mantém 2 caminhos.** Minha sugestão é unificar tudo no `v4_vision_router.py` (mais completo com failover/cooldown) e o `featured_image_runtime.py` só chama o router.

### 2.3 Fonte de imagem — Flickr allowlist oficial já configurada

**`/root/v4_labs/config/v4_flickr_official_accounts.json`** já contém contas oficiais brasileiras:

`senado`, `lula`, `planalto`, `agencia_brasil`, `camara`, `stf`, `tse`, `governo_rio`, `governo_sp`, `governo_rs`, `governo_ms`, `governo_sc`, `governo_amapa`, `prefeitura_manaus`, `prefeitura_rio` (extensível).

**Ordem hierárquica que a curadoria deve seguir** (Miguel + CL-V42 29/08):
1. Flickr oficial (allowlist) — sempre primeiro
2. Banco de mídia próprio (V4AuditedMediaStore) — barato
3. Wikimedia — só se foto for datada e relevante ao fato (nunca institucional antiga genérica)
4. IA generativa — último recurso, sempre com crédito "Ilustração: Cafezinho / <gerador> — gerada por IA" (Emenda 11)

### 2.4 Banco de mídia auditado próprio — já modelado, precisa ativar

- **`V4AuditedMediaStore`** — store com hash MD5 e auditoria
- **`V4MediaScoutAgent`** — varre Flickr, classifica com Vision, promove aprovadas ao banco

Miguel mencionou que **não conseguia rodar a "aprovação anual" do banco V4** — provavelmente algum gargalo dependente do GL ou pipeline manual quebrado. F4 do sprint resolve isso.

### 2.5 Credenciais prontas

- `DEEPSEEK_API_KEY` está em `/root/.env` no NYC
- Env vars pra Kimi, Qwen, Gemini já configuradas (senão o `v4_vision_router.py` atual não rodaria)
- Google Vision e Psic Vision — Miguel precisa confirmar credenciais disponíveis

---

## 3. Regras não-negociáveis do V4.1 Vision (destilado ordens Miguel)

Todas as ordens transcritas de áudios/chats Miguel entre 29/08 e 31/08:

1. **Sem hardcode.** Modelo, endpoint e ordem vêm de contrato JSON ou env. Mudar provedor = editar 1 arquivo, sem redeployment.
2. **Cascata multi-Vision.** Kimi, Qwen, Gemini, DeepSeek, Google, Psic — todos como fallback uns dos outros. Prioridade por qualidade × custo × latência (a definir com dados F1).
3. **Curadoria por tese.** Vision recebe a tese dinâmica do artigo (V4.1 já produz `tese_dinamica_aprovada`) e o título — não só o tema genérico.
4. **Curadoria por nome no título.** Se há nome próprio no título → **prioridade máxima é foto jornalística RECENTE dessa pessoa** (Emenda 12 reforçada). Emenda 8: nunca logo de empresa como capa.
5. **Imagem jornalística fresca.** Frescor é fundamental. NÃO Wikimedia institucional antiga (fachada Palácio Planalto genérica etc — Miguel 29/08 15:20). Data máxima aceitável depende do tema — a definir na F1.
6. **Gate visão DUPLO.** 2 providers Vision concordam APROVADA antes de aplicar. Se divergem, terceiro tie-breaker. Se todos os 3 divergem, humano (CM/CL) revisa. Fail-closed.
7. **Legenda com autor + fonte + licença + ano.** O ano é o que salva a foto institucional (parecer CL 29/08 21:13). Meta obrigatória: `_cafezinho_capa_source_url`, `_cafezinho_capa_license`, `_cafezinho_capa_year`, `_cafezinho_capa_provider`.
8. **Blacklist figuras políticas datadas.** Ricardo Barros, Osmar Terra, Mandetta, Teich, Pazuello, Queiroga em posts breaking de outro tema — bloqueio automático (Gate 267037).
9. **§86 v1.1.0 respeitado.** MD5 preso barra publish — Vision precisa checar MD5 disponível antes de propor. Se todos MD5 travados, escalar Miguel.
10. **Escrita em produção só depois de F1 aprovada por CM+Miguel.** Espelho/dry-run primeiro. Regra dura.

---

## 4. As 4 fases do sprint

### F1 — POC curadoria de imagem (2-4h estimadas, deadline sugerido 02/09 EOD)

**Objetivo:** provar que o pipeline existente produz capa jornalística aprovada por Vision pra 1 draft V4.1 real.

**Passos técnicos:**

1. **Escolher 1 draft V4.1 recém-nascido** — query WordPress: `wp post list --post_status=draft --meta_key=_v4_versao --meta_value=4.1 --posts_per_page=5 --orderby=date --order=DESC` no cafezinho-wp
2. **Montar JSON** `FeaturedImageRequest` (formato em `/root/v4_labs/codigo/featured_image_pipeline.py` — dataclass `FeaturedImageRequest`):
   ```json
   {
     "item_id": "<draft_id>",
     "title": "<título draft>",
     "primary_entity": "<pessoa/lugar principal>",
     "editoria": "<vertical>",
     "target_status": "draft",
     "frame_visual": {"prioridade": "pessoa|lugar|conceito"},
     "requires_person": <bool>,
     "image_required_for_publication": true
   }
   ```
3. **Rodar CLI:**
   ```bash
   cd /root/v4_labs
   python3 -m codigo.featured_image_runtime_cli /tmp/request.json --root . --env-file /root/.env --allow-network --execute
   ```
   - `--execute` persiste auditoria + decisão local, mas NÃO faz upload no WP
4. **Verificar output:**
   - (a) Flickr retornou candidato? De qual conta allowlist?
   - (b) Vision router validou? Quantos providers foram consultados? Custo?
   - (c) MD5 disponível (não preso)?
   - (d) Cascata funciona ou algum provider falha silencioso?
5. **Escrever adapter Python** (novo módulo, chamar de `codigo/wp_apply_featured_image.py`):
   - Baixa a imagem sugerida
   - `wp media import <url_ou_path>` via SSH cafezinho-wp
   - `wp post meta update <ID> _thumbnail_id <media_id>`
   - `wp post meta update <ID> _cafezinho_img_check` com JSON verdadeiro contendo:
     ```json
     {
       "ok": true,
       "ts": "<iso>",
       "checker": "V4_VISION_ROUTER",
       "veredicto": "APROVADA",
       "media_id": <id>,
       "provider_a": "kimi_paygo",
       "provider_b": "gemini_vision",
       "acordo": true,
       "source_url": "<flickr_url>",
       "license": "CC BY 2.0",
       "year": "2026-08-15",
       "author": "<foto autor>",
       "alt_text": "<descrição pixels>",
       "caption": "<autor / fonte / licença / ano>"
     }
     ```
   - NÃO fabricar como GL fez no bug 267037 (foto Ricardo Barros aplicada em post SUS) — Vision precisa ter rodado de verdade
6. **Testar em 1 draft real.** CM ou CL fazem checagem dupla (`_v4_versao=4.1` + frescor <72h + thumb + img_check APROVADA + dedup 72h + Regional=pesquisa/bastidor se aplicável) antes de publish. Publish sai HTTP 200.
7. **Reportar no fórum** com métricas: tempo total, providers usados, custo, capa escolhida, aprovação.

**Critério de sucesso F1:**
- 1 draft V4.1 recebe capa Flickr oficial aprovada por 2 Vision providers
- Meta `_cafezinho_img_check` gravada com JSON verdadeiro
- Gates §86/checagem dupla passam
- Publish sai HTTP 200 no cafezinho.com
- Capa é fresca, jornalística, sem canibal MD5

### F2 — Integração ao v41_ciclo (4-8h estimadas, deadline sugerido 04/09)

**Objetivo:** V4.1 aplicar capa sozinho no fim de cada ciclo, sem depender de agente externo.

**Passos:**

1. **Modificar `codigo/v41_ciclo.py`** (ou wrapper novo): após redator produzir draft com sucesso, chamar `featured_image_runtime` → adapter da F1
2. **Se Vision retorna capa aprovada** → aplica no WP como F1
3. **Se falha** → draft fica sem capa + flag `_cafezinho_capa_pendente_v4=1` pra revisão manual (CM/CL/DS-N)
4. **Cron NYC opcional** (`*/30 * * * *`): varredura de drafts órfãos pra retentar
5. **Meta rastreabilidade obrigatória:** `_cafezinho_capa_provider`, `_cafezinho_capa_source_url`, `_cafezinho_capa_license`, `_cafezinho_capa_year`, `_cafezinho_capa_author`
6. **Testar em 5-10 drafts consecutivos** antes de deixar rodando em produção
7. **Toggle `_v4_espelho_v42=1` ou cat no-home 20699** durante teste de estabilidade (2-3 dias)

**Critério de sucesso F2:**
- Ciclo V4.1 completa em <5min por vertical
- Drafts saem com capa 80%+ das vezes
- Capa jornalística e recente
- Zero canibal MD5
- Nenhum publish acontece automaticamente sem CM/CL aprovar durante fase de teste

### F3 — Banco próprio V4AuditedMediaStore + Scout (8-16h estimadas, deadline sugerido 08-10/09)

**Objetivo:** reduzir dependência de bater Flickr toda hora + garantir só imagens de fontes confiáveis.

**Passos:**

1. **Ativar V4AuditedMediaStore** — SQLite ou similar no NYC (path `/root/agent_data/v4_verticals/media_audit.sqlite3` sugerido)
2. **Cron dedicado V4MediaScoutAgent** — varredura Flickr allowlist a cada 2-4h:
   - Puxa novas fotos das contas oficiais
   - Roda Vision router pra classificar (o que é? pessoa nomeada?)
   - Aprovadas com metadata boa vão pro banco
3. **`featured_image_runtime` consulta primeiro o banco** (barato + rápido, <100ms), depois Flickr como fallback
4. **Meta:** banco cresce organicamente 100-500 imagens/dia; consultas em ms

**Critério de sucesso F3:**
- Banco tem 1000+ imagens auditadas em 2 semanas
- Custo Vision API cai 50%+ (menos calls por publish)
- Latência total de "produzir capa" cai pra <10s

### F4 — Aprovação anual banco V4 (2-4 semanas, deadline sugerido 25/09)

**Objetivo:** resolver o bloqueio antigo que Miguel mencionou ("não estou conseguindo fazer aprovação anual do banco V4").

**Passos:**

1. **Investigar o processo anual antigo** — logs, scripts, memórias no cerebro-miguel
2. **Substituir dependência LAURA-GROK** por V4.1 Vision próprio (já feito na F1-F2)
3. **Rerun aprovação em lote** com pipeline novo
4. Reportar resultado ao Miguel

---

## 5. Interface com V4.2 (paralelo — DS-Miguel lidera)

Existe um fórum paralelo (`cerebro/Foruns/forum_v42_curadoria_imagem_e_arquitetura_20260829.md`) onde DS-Miguel está desenhando o V4.2, que será o V4.1 melhorado. **Suas descobertas no sprint V4.1 Vision devem alimentar o V4.2.**

**Ideia nova que Miguel lançou 31/08:** um agente separado só de imagem, ficando na nuvem (Tencent), que recebe tese + título e devolve imagem — depois camada externa (agentes) revisa.

- Isso pode ser F2 evoluído do teu sprint (chamada em rede pro agente de imagem) OU núcleo do V4.2 (agente independente)
- Aberto pra debate direto entre você (ZM) e DS-Miguel no fórum V4.2

---

## 6. Recursos disponíveis pra ti (ZM)

- **DS-N (Tencent 43.156.151.165)** — 24/7, 17 credenciais LLM, clone cerebro-miguel. Pode testar/rodar pipelines pesados sem gastar teu contexto local. Peça ajuda via bloco `ZM-SPRINT-V41V-XXX` na ponte.
- **AGY-M (Dell)** — SSH nyc, wp-cli, engenharia. Pode aplicar o adapter WordPress.
- **CM (eu)** — coordenação editorial, gate final antes de qualquer ação afetar V4.1 vivo, checagem dupla nos publish. Consulto sempre que precisar.
- **CL / Loop Laura** — contraponto editorial, gate visual, Consenso Duplo pra migrações.
- **XM (Codex)** — revisão de código quando sair do HOLD atual (divergência clone/canônico).
- **DS-Miguel** — consultoria V4.2 (paralelo, não concorrência).

---

## 7. Cronograma sugerido (você pode contrapropor)

| Fase | Duração estimada | Deadline sugerido |
|---|---|---|
| F1 POC | 2-4h ativa | 02/09/2026 EOD |
| F2 Integração | 4-8h ativa | 04/09/2026 |
| F3 Banco próprio | 8-16h ativa | 08-10/09/2026 |
| F4 Aprovação anual | 2-4 semanas totais | 25/09/2026 |

Se algo aqui não bater com tua carga (contexto/RAM/GLM crédito), contrapropõe no bloco de abertura. Miguel decide finais.

---

## 8. Reporte

- **Ronda 30/30 tua** (quando ativa): incluir 1 linha "Sprint V4.1 Vision: fase X, próxima Y"
- **Fórum operacional** (`forum_sprint_v41_vision_zm_20260831.md`): bloco `ZM-SPRINT-V41V-YYYYMMDD-NNN` por milestone
- **Telegram Miguel** (`ponte_cafezinho.py --send`): quando bater bloqueador ou marco importante
- **Ponte `de_dell.md`**: quando ação afeta outros agentes (ex: pipeline vai rodar em produção — precisa aviso 4h antes)

---

## 9. Bloco de abertura sugerido (você posta quando aceitar)

```
## [YYYY-MM-DD HH:MM BRT · ZCode/Qwen 3.8 — Dell] ZM-SPRINT-V41V-20260831-001 — 🎯 SPRINT V4.1 VISION ACEITO — abertura

Ordem Miguel via CM (carta_para_zcode_miguel_sprint_v41_vision_20260831.md) recebida e lida.
Aceito o sprint. Contraproposta cronograma: <manter ou contrapropor>.

Primeiro passo F1: <o que vou fazer primeiro — ex: rodar CLI dry-run em draft 268XXX>.

Bloqueios que preciso confirmar antes:
- <credenciais Google Vision / Psic Vision disponíveis? — pedir Miguel>
- <SSH nyc funcional pro meu ambiente>

CHECK ZM sprint_v41_vision inicio=YYYY-MM-DD_HH:MM
```

---

## 10. Palavra final de coordenação

Sprint é teu. Executa como quiser dentro dessas regras. Se precisar de contexto histórico do V4.1 (como chegou aqui, por que essas decisões foram tomadas), consulta o Cérebro (`cerebro/CEREBRO_NODE_ATUALIZACOES.md` + memórias) ou me pergunta.

Se detectar algo problemático na arquitetura V4.1 que não consegue resolver dentro do sprint, escala pra mim + Miguel via ponte.

Boa sorte. **Cai um, entra outro** — se você travar, DS-Miguel/AGY-M/eu cobrimos. Mas o oficial deste sprint é teu.

— Claude Miguel (`claude-opus-4-7`) · 31/08/2026 10:00 BRT · chefe Loop Miguel · repo `cerebro-miguel` branch `main`
