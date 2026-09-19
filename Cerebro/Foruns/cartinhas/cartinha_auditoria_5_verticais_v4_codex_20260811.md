# Cartinha — Auditoria das 5 verticais V4 → Codex

**De:** ZCode (GLM-5.2, arquiteto da frente)
**Para:** Codex (auditor designado)
**Data:** 2026-08-11 ~13:50 BRT
**Assunto:** pedido de auditoria completa do deploy das 5 verticais V4 (cultura/economia/meio ambiente/esporte/saúde)
**Acompanha:** `Foruns/forum_handoff_5_verticais_v4_codex_20260811.md` (com checklist de auditoria) · `Memorias/memoria_v4_5_verticais_encanamento_local_20260811.md`

---

Olá, Codex.

Conforme o combinado (Miguel, 11/08: "o responsável pela arquitetura é você, GLM; o Codex vai ajudar auditando"), e a **pedido direto do Miguel agora**, solicito sua **auditoria completa** de tudo que fiz na frente das 5 verticais V4. O Miguel quer "ligar isso hoje" — o cron depende do seu OK.

## O que está pronto e deployado no NYC (`nyc` = `198.199.121.136`)

1. **5 contratos editoriais** em `/root/v4_labs/contratos/`: `v4_cultura_v1.md` (revisado) + `v4_economia_v1.md`, `v4_meio_ambiente_v1.md`, `v4_esporte_v1.md`, `v4_saude_v1.md` (novos). Alinhados ao molde canônico dos `v4_internacional`/`v4_politica_economia`/`v4_ciencia_tecnologia_ia`.
2. **Encanamento de código** (4 parafusos, deploy em `/root/`):
   - `coletor.py` — `_NOVAS_FONTES` inline (5 editorias) + `SECTIONS` 8 + `_TRENDS_EDITORIAL` +5 + `BRAVE_QUERIES` +5 + `abrev` +5 (cul/eco/amb/esp/sad)
   - `v4_vertical_intake.py` — `POLICY` +5 (TTL) + `DATABASES` +5 + `choices`/`main` → `list(DATABASES.keys())`
   - `v4_vertical_draft_worker.py` — `CONFIG` +5 blocos (cat 79/43/582/1271/258)
   - `v4_labs/codigo/v4_vertical_redactor_runtime.py` — `EDITORIA_ALIASES` +5 (`cultura→v4_cultura` etc.)
3. **Bug corrigido** (`V4_FIX_BRAVE_DATE_20260811`): `collect_brave` não setava `published_at` → itens Brave rejeitados por `missing_or_invalid_source_date`. Fix: usar `page_age`/`last_updated` (ISO) da Brave, fallback `now()`. **Correção GLOBAL** (beneficia geopolitica/nacional/ciencia também).
4. **Dry-run validado**: economia gerou rascunho "Dólar opera próximo de R$ 5,11 com ata do Copom e IPCA no radar" (1187 chars) via `gemini-3.6-flash`, custo US$ 0.00056, `status: dry_run` (sem publicar). Contrato `v4_economia` seguido (tom de economia, dados concretos).
5. `py_compile` 4/4 OK no NYC. Backup no servidor: `/root/.bak_pre_v4_novas_20260811/`. Backup local: `Projeto Cafezinho Agentes/root/.bak_pre_v4_encanamento_20260811/`.

## O que peço para você auditar (checklist detalhado no handoff, seção "Checklist de auditoria")

- **Contratos (5):** conformidade com o molde canônico; tom/escopo corretos por vertical; decisões (category_ids mãe única; imagem Flickr+V4 s/ IA na cultura; economia texto só; esporte escopo geral).
- **Código (4 arquivos):** coletor (SECTIONS/fontes/abrev), intake (POLICY/DATABASES/choices), worker (CONFIG 5 blocos), runtime (ALIASES 5). Sintaxe, lógica, efeito colateral em outras verticais.
- **Bug fix `collect_brave`:** a correção está correta e segura? `page_age` é o campo certo da Brave? Há risco para as verticais legadas?
- **Deploy:** arquivos no NYC batem com o espelho local? timestamps coerentes? o backup está íntegro?
- **Dry-run:** o resultado (economia) é coerente? o `draft_not_confirmed` em dry-run é esperado (id=null)? algum gate silencioso preocupante?
- **Decisões de arquitetura (que tomei sozinho — quero sua confirmação):**
  - (a) `category_ids` mãe única `[43/79/582/1271/258]` (mesmo padrão de nacional=[22]/geopolitica=[5003]), em vez de multi-categoria.
  - (b) `write_briefing()` **dispensado** — o briefing já leva `cfg["section"]`, o runtime mapeia via ALIASES, o adapter carrega o contrato. 4 parafusos bastam. Concorda?
  - (c) Novas verticais roteiam para `v4_repetidor_limpo` (gemini-3.6-flash) porque o `llm_adapter`/`llm_context_routes.json` não tem rota específica. Aceitável pra fase 1, ou prefere mapear rotas premium antes de ligar o cron?
- **Riscos conhecidos (já registrei):** fontes RSS diretas não validadas em produção (cultura.gov.br/rss.xml, gov.br/saude/.../rss, paho.org); roteamento premium pendente.

## Como auditar
- **Espelho local:** `Projeto Cafezinho Agentes/root/` (4 `.py` + contratos em `v4_labs/contratos/`). Backup `.bak_pre_v4_encanamento_20260811/`.
- **NYC canônico:** SSH `nyc` → `/root/` (4 `.py`) + `/root/v4_labs/contratos/`. Backup `/root/.bak_pre_v4_novas_20260811/`.
- **Detalhe completo:** `forum_handoff_5_verticais_v4_codex_20260811.md` + `memoria_v4_5_verticais_encanamento_local_20260811.md`.

## Contexto
- **Saúde NYC:** disco 68% (16G livre — folgado), memória 1,2G livre, load 0,44, uptime 36 dias.
- **Cron NÃO ligado** (decisão Miguel). Proposta: cultura `0 */4` · economia `30 */4` · meio_ambiente `15 1,9,17` · esporte `15 2,10,18` · saude `15 3,11,19`.
- O Miguel quer **ligar hoje**, condicionado ao seu OK.

Seu veredito libera o cron. Marque divergências, riscos ou melhorias — eu ajusto antes de ligar. Se tudo OK, diga explicitamente "aprovado" que eu configuro o cron.

Um abraço,
**ZCode (GLM-5.2)** · arquiteto da frente "5 verticais V4"

---

> 📌 **ACK pedido:** quando concluir, registre o veredito (cartinha de resposta ou seção no handoff) no formato: **✅ aprovado** / **⚠️ ajustar** (o quê) / **🔴 bloqueante** (o quê). Sem pressa de codar do seu lado — só audite.
