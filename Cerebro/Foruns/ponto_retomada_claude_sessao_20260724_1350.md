# Ponto de Retomada — Claude Code / sessão 24/07/2026

**Timestamp:** 2026-07-24 13:50 BRT
**Sessão:** `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020` (continuação após compaction, ativa desde 03:51 BRT hoje)
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`), engenheiro-chefe do ecossistema

---

## 1. Estado operacional agora (13:50 BRT)

- **Loop Sentinela Cafezinho:** rodando via `/loop` (cron 30min dia / 1h noite + comando manual). Último ciclo `20260724_1347` · 🟢 normal · 0 publish · cap 2h ativo bloqueando ~90 drafts antigos.
- **Publicações do dia:** 20+ posts (00:46 → 13:14 BRT), média ~1 post/40min, rate limit R1 respeitado. 2 em HOME (262768 Tarifácio, 262773 Flávio/PF/STF), demais NO-HOME.
- **Baleia Azul do dia:** ✅ existe (cron 06:00 criou).
- **Health:** 10/10 providers OK.
- **`v4_pipeline_imagem`:** verde estável 5/5 desde fix Kimi (UA `SentinelaCafezinho/1.0` + retry).

---

## 2. Trabalhos concluídos hoje

### 2.1 Kimi K3 fechou 3 bugs upstream V4 (11:00 BRT)
- **#META** — chapéu editorial `<em>Categoria+tópico</em>` vazando no corpo. Causa real em `agente_controlado.py` (não no worker): `validar_editorial` só rejeitava rótulo EXATO. Fix: prefixo-marcador + guarda final em `html_para_wp`. 11/11 testes. Scan 7d/272 posts: só 2 afetados (262211 limpo, 262713 draft).
- **#24 dedup V4** — draft 262741 duplicava 262704 (12h antes). Causa: 3 falhas combinadas (janela 2h no briefing, `per_page=5` sem filtro data, Jaccard 0.40 no par real). Fix: `duplicate_recent_topic()` no worker antes do LLM + janela 24h + contenção de tokens semântica. 8/8 testes.
- **#23 WP 403** — não era `_fields`, era UA `Python-urllib` bloqueado por Cloudflare bot-scoring. Fix: UA `SentinelaCafezinho/1.0` + retry 2s/4s.
- Backups: `.bak_pre_kimi_*_20260724_1007` SHA-256 registrado. Memória: `project_kimi_bugs_upstream_v4_fechados_20260724.md`.

### 2.2 Bug #25 — assinatura estagiário Agência Brasil (11:35 BRT)
- **Sintoma:** posts do repetidor estatal com `<p>*Estagiário da Agência Brasil sob supervisão de X`. Miguel: *"não interessa se foi estagiário que escreveu"*.
- **Fix upstream** (NYC `/root/agente_repetidor_estatal.py`): 3 regex em `extrair_html_e_titulo()` antes do return (`</p>` fechado, sem fechar, linha nua). Backup `.bak_pre_claude_estagiario_20260724_1132` SHA-256 `b52ea08a...c9227`. 4/4 testes.
- **Fix downstream:** 3 posts limpos in-place (status=publish preservado, CHURN OK): 262732, 262726, 262249.
- Memória: `feedback_cortar_assinatura_estagiario_agencia_brasil.md`.

### 2.3 Bug #26 — charge Flux com texto DENTRO da imagem (12:10 BRT)
- **Sintoma:** post 262721 (Lula/Flávio/PP) com texto truncado dentro da charge Flux. Miguel: *"não pode ter jamais texto dentro da imagem porque em geral trunca"*.
- **CAUSA GRAVE:** função `_prompt_flux_com_texto_permitido()` em `/root/gerador_imagem_editorial.py` (NYC) EXPLICITAMENTE removia `ABSOLUTELY NO TEXT` do prompt e adicionava permissão para "editorial lettering". Bug estrutural afetando TODA imagem Flux desde X data (auditoria pendente).
- **Fix upstream:** função revogada (nome mantido pra não quebrar única call site linha 542), agora só REFORÇA anti-texto com lista longa. Backup `.bak_pre_claude_notext_20260724_1150` SHA-256 `2f18c2a0...c89c`.
- **Fix downstream:** imagem 262721 regenerada via gerador corrigido → media 262764, `featured_media` trocada in-place, `status=publish` preservado.
- Memória: `feedback_charges_sem_texto_dentro_flux.md`. Lição arquitetural: funções com nome `permitido`/`allow`/`enable`/`unlock`/`relaxed` em pipeline editorial são bandeira vermelha.

### 2.4 Nova rotina: ciclo Temáticos ~3h manual via /loop (10:55 BRT)
- Miguel: a cada ~6 loops Cafezinho (~3h), substituir 1 ciclo por CICLO TEMÁTICOS vigiando 7 sites satélites: Rio Carta+Mapa Rio, Global South, Discover Brazil, Aiatolah, Ceará Digital, Mundo Trilhos, Rail Post.
- **1º ciclo temáticos rodado 11:05 BRT:** 7/8 sites saudáveis. Detalhes em `Cerebro/monitoramento_horario/tematicos/tematicos_2026-07-24.jsonl`.
  - ✅ Rio Carta, Global South, Discover Brazil, Aiatolah, Mundo Trilhos, Rail Post — HTTP 200 + commits recentes
  - ⚠️ **Mapa Rio** — repo tem só 2 commits totais (migração V4 + 1 fix); home é 429 bytes de esqueleto (app Vite SPA, não Astro SSG). PRECISA CONFIRMAÇÃO com Miguel se está em estágio esperado ou se agente parou/nunca começou.
  - ✅ Ceará Digital — DNS 000 esperado (pré-lançamento).
- Padrão de correção: tento sozinha primeiro → fallback Kimi K3 via fórum.
- Memória: `feedback_ciclo_tematicos_3h_manual_via_loop.md`.
- Próximo ciclo temáticos previsto: **~14:00 BRT** (regra: se último foi >2.5h, rodar temáticos ao invés de Cafezinho no próximo `/loop`).

### 2.5 Ciclos Sentinela Cafezinho contínuos
- ~20 ciclos rodados hoje (03:51 → 13:47 BRT).
- Correções automáticas: 6 fontes coladas auto-corrigidas no passo [4.5/6].
- Nenhum ABORT-antigo indevido (cap 2h funcionando corretamente).
- Único incidente: WP API 403 intermitente entre 06:14-07:14 BRT (resolvido por Kimi).

---

## 3. Pendências

### 3.1 Confirmar com Miguel
- **Mapa Rio (`mapario.vercel.app`)** está em estado esperado ou o agente que popula posts parou? Repo tem apenas 2 commits totais; home é HTML esqueleto Vite SPA sem conteúdo.

### 3.2 Auditoria pendente (baixa urgência)
- **Git-blame quem adicionou `_prompt_flux_com_texto_permitido()`** originalmente em `/root/gerador_imagem_editorial.py`. Pode ter sido teste que ficou em prod; entender contexto pra evitar regressão futura.
- **Auditar UA explícito** nos demais scripts que falam com WP via urllib (sugestão Kimi 11:00) — mesma classe de bug #23 pode estar dormente em outros lugares.

### 3.3 Já sabia antes de hoje, ainda pendente
- Bug #20 (Redir agregador → veículo real) — downstream corrigido, upstream Codex/Kimi
- Bug #22 (fonte colada camelcase) — downstream corrigido, upstream Codex/Kimi
- Score policy home/no-home entregando 60-90% HOME em vez de ~20% (Codex investigar `decide_no_home()`)
- Baleia Azul email delivery — precisa App Password Gmail do Miguel
- Ubuntu upgrade final de semana pra HiveTerm
- Script `relatorio_semanal_bugs.py` sexta 23:00 BRT

---

## 4. Arquivos criados/editados hoje

**Cérebro:**
- `Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md` — tabelas atualizadas com #23, #24, #25, #26
- `Cerebro/CEREBRO_NODE_ATUALIZACOES.md` — 2 entradas novas (11:34 bug #25, 11:52 bug #26)
- `Cerebro/monitoramento_horario/bugs_encontrados/bugs_2026-07-24.jsonl` — 23 instâncias registradas
- `Cerebro/monitoramento_horario/tematicos/tematicos_2026-07-24.jsonl` — 8 linhas (1 por site)
- `Cerebro/Foruns/forum_kimi_bugs_persistentes_upstream_v4_20260724.md` — carta ao Kimi + resposta 11:00 BRT
- `Cerebro/Foruns/ponto_retomada_claude_sessao_20260724_1350.md` — **este arquivo**
- `Cerebro/Foruns/canal_trindade.md` — linha `[BUGS-UPSTREAM-V4-KIMI]`
- `Cerebro/Foruns/inbox_trindade/kimi.md` — 3 bugs upstream V4

**Manual bugs:**
- `Outros/manual_de_bugs.md` — entradas #23, #24, #25, #26 (1370 linhas)

**Memórias permanentes (`~/.claude/.../memory/`):**
- `project_kimi_bugs_upstream_v4_fechados_20260724.md`
- `feedback_ciclo_tematicos_3h_manual_via_loop.md`
- `feedback_cortar_assinatura_estagiario_agencia_brasil.md`
- `feedback_charges_sem_texto_dentro_flux.md`
- `MEMORY.md` — 4 novas entradas no topo (índice)

**Código NYC (`/root/`):**
- `agente_controlado.py` — patch Kimi 11:00 (#META + #24 dedup briefing). Backup `.bak_pre_kimi_meta_dedup_20260724_1007` SHA-256 `abe71204...d4c280`, deploy `bb9e3fc9...4ab37`.
- `v4_vertical_draft_worker.py` — patch Kimi 11:00 (#24 dedup pré-LLM). Backup `.bak_pre_kimi_meta_dedup_20260724_1007` SHA-256 `18271cb1...c070a5`, deploy `df110da0...1b0f2`.
- `agente_repetidor_estatal.py` — patch Claude 11:34 (bug #25 estagiário). Backup `.bak_pre_claude_estagiario_20260724_1132` SHA-256 `b52ea08a...c9227`.
- `gerador_imagem_editorial.py` — patch Claude 11:52 (bug #26 texto dentro charge). Backup `.bak_pre_claude_notext_20260724_1150` SHA-256 `2f18c2a0...c89c`.

**Código local:**
- `~/ferramentas/sentinela/sentinela_ciclo.py` — patch Kimi 11:00 (UA `SentinelaCafezinho/1.0` + retry). Backup `.bak_pre_kimi_wp403_20260724_1007` SHA-256 `235116c2...e0a7`.

**WordPress in-place (regra CHURN preservada):**
- 262732, 262726, 262249 — assinatura estagiário removida
- 262211 — sujeira `<em>Tecnologia, disputa corporativa</em>` removida (Kimi 11:00)
- 262721 — `featured_media` trocada (media 262722 → 262764) sem tocar status

---

## 5. Regras editoriais em vigor hoje (relembrar)

- **Cap 2h** — Sentinela nunca publica draft V4 >2h de idade (regra inviolável, defesa dupla prompt+Python)
- **CHURN** — NUNCA rebaixar publish→draft (Google Index punição)
- **Rate limit R1** — máx 1 publish/ciclo = ~2/hora
- **D0-D4** — sem agregador como fonte, siglas partido maiúscula, dois pontos com moderação, ZERO ponto e vírgula em título
- **SEMANT** — Trump=imperialista, Bolsonaro=entreguista (nunca confundir)
- **Governos de esquerda** — cobertura factual, nunca crítica moral (Nicarágua/Venezuela/Cuba/Bolívia/Honduras/México/Brasil/Colômbia/Chile)
- **SEO Pruning** — requer autorização Miguel explícita a cada uso
- **Título com autonomia** — corrigir sem pedir permissão a cada ciclo (drafts + publicados <2h)
- **Charges** — sem texto DENTRO, texto vai embaixo no HTML (regra hoje 12:10 BRT)
- **Estagiário Agência Brasil** — cortar rodapé no repetidor estatal (regra hoje 11:35 BRT)

---

## 6. Sessão anterior (retomada de contexto)

Sessão começou 19/07 10:20 BRT quando Miguel transferiu engenharia-chefe do Codex pra Claude Code. Desde então: reforma Sentinela cron 24/7, catalogação bugs #18-#26, 3 camadas de memória de bugs, protocolo "ler antes de agir + guardar tudo em 3 camadas" (24/07 01:20 BRT).

---

## 7. Continuidade

Próxima sessão Claude Code deve:
1. Ler `MEMORY.md` (índice está no topo — últimas entradas 24/07)
2. Ler este ponto de retomada
3. Verificar estado atual: `tail -5 ~/ferramentas/sentinela/logs/ciclos.jsonl`
4. Continuar rotina `/loop` — Cafezinho a cada 30min; Temáticos a cada ~3h substituindo 1 Cafezinho
5. Se algum bug novo aparecer → protocolo `feedback-protocolo-memoria-bugs-ler-antes-agir` (consultar 3 lugares, aplicar fix, guardar 3 camadas)

## Assinatura

Ponto de retomada gravado por Claude Code (Anthropic, `claude-opus-4-7`), engenheiro-chefe do ecossistema, sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-24 13:50 BRT.
