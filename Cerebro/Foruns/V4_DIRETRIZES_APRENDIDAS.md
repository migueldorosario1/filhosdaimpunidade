# V4 — Diretrizes aprendidas (síntese viva de erros → regras permanentes)

**Criado:** 15/08/2026 11:40 BRT
**Autor:** Claude Miguel, seguindo ordem Miguel 11:35 BRT
**Propósito:** todo erro operacional grave vira diretriz aqui. Consumido por Claude/ZCode/Grok/Codex em Miguel e Laura. Adendo direto aos contratos `v4_*_v1.md` do NYC.

---

## Como usar este arquivo

- **Novo erro grave detectado**: adicionar entrada no formato abaixo
- **Consulta por qualquer agente**: `cat V4_DIRETRIZES_APRENDIDAS.md` no início de cada ciclo ou quando surgir dúvida
- **Sincronizado via `cerebro-miguel`** → todos os PCs (Miguel + Laura) recebem

## Formato de entrada

```markdown
## <ID> — <TÍTULO CURTO> (data BRT)

**Causa raiz:** o que aconteceu tecnicamente
**Fase que falhou:** [modelo | worker | claude | grok | ponte | §86 | outro]
**Fix estrutural:** o que muda no código/prompt/gate pra nunca mais
**Fix paliativo (client-side):** o que rodo enquanto o estrutural não fecha
**Como verificar:** teste manual que prova que o fix funciona
**Referência**: link pra `memory/feedback_*.md` correspondente
```

---

## Diretrizes vigentes (ordem cronológica reversa — mais novo em cima)

## D-2026-08-15-05 — V4 sempre entra na home, NUNCA cat 20699 (15/08 13:35 BRT)

**Causa raiz:** minha regra 14/08 16:38 aplicava cat 20699 quando fila estourava teto (via "válvula NO-HOME"). Vinha de repasse indireto ZCode via inbox velha, mas conflitava com regra Miguel.
**Fase que falhou:** Claude editor (regra incorreta na memória)
**Fix estrutural:** nunca aplicar cat 20699. Se fila estourou teto 12h → manter `pending` com log ("SKIP: fila estourou teto"). Publish só normal ou pra gancho vivo (votação/morte/tragédia).
**Fix paliativo:** N/A (é remoção de comportamento)
**Como verificar:** grep `valvula_no_home` no bugs_YYYY-MM-DD.jsonl a partir de 15/08 13:35 = 0 ocorrências
**Referência:** `feedback_v4_entra_normalmente_na_home_nao_cat_20699_20260815.md`

## D-2026-08-15-04 — Processo de autoaprendizado 5 fases (15/08 11:35 BRT)

**Causa raiz:** erros graves recorrem porque não viram infra — ficam só no log
**Fase que falhou:** meta-processo
**Fix estrutural:** todo erro → 5 fases: registro JSONL + índice MEMORY.md + diretriz feedback_*.md + integração aqui + LER antes do ciclo
**Fix paliativo:** N/A (é a meta-regra)
**Como verificar:** revisão semanal de cada bug JSONL confirma que tem os 4 artefatos + gate ativo
**Referência:** `feedback_processo_autoaprendizado_ler_memoria_todo_ciclo_20260815.md`

## D-2026-08-15-03 — Gate metalinguagem deve olhar hrefs (15/08 11:32 BRT)

**Causa raiz:** post 265876 (Mendonça STF) publicou com 6 `utm_source=openai` em `href`. Regex de metalinguagem só olhava texto renderizado, não atributos de link
**Fase que falhou:** worker V4 (não sanitizou) + Claude editor (gate só texto) + Grok Miguel observador (mesma limitação)
**Fix estrutural:** worker V4 deve `parse_url() + strip TRACKING_KEYS (utm_*|fbclid|gclid|_ga|mc_*|ref) + preservar params funcionais (idConteudo|lei|q|id)` antes de persistir. Cobrir markdown E HTML href.
**Fix paliativo:** pipeline `agendar()` Claude v5 strip `?utm_*` + grep expandido `utm_source=(openai|anthropic|deepseek|gemini)` + domínios IA (chatgpt.com|claude.ai|etc)
**Como verificar:** `curl -s https://ocafezinho.com | grep -c 'utm_source=\(openai\|anthropic\|deepseek\|gemini\)'` deve retornar 0
**Referência:** `feedback_gate_metalinguagem_deve_inspecionar_href_nao_so_texto_20260815.md` + `Foruns/forum_incidente_grave_265876_vazamento_processo_responsabilidades_20260815.md`

## D-2026-08-15-02 — Metalinguagem sutil: variantes "fonte-base/original/etc" (15/08 02:07 + 07:36)

**Causa raiz:** worker V4 (GPT-5.5) inventa variantes de metalinguagem sutil expondo processo interno ("A fonte-base deste rascunho é X", "material-fonte publicado em Y", "data da fonte original Z"). LLM tem instrução no prompt que induz cita fonte com data
**Fase que falhou:** worker V4 (prompt) + Claude editor (regex incompleto) + Grok observador
**Fix estrutural:** ZCode aplicou 15/08 02:25 no worker regex `(fonte[- ](base|analisada|original|primária)|material[- ]fonte|pauta original|fonte de referência)`. Também: investigar PROMPT do worker pra remover instrução tipo "cite a fonte da pauta"
**Fix paliativo:** pipeline `agendar()` v4-v5 mesmo regex
**Como verificar:** grep em drafts pending do 5786 — 0 ocorrências
**Referência:** entradas fila_para_zcode entre 02:07-07:36 15/08 + `feedback_gate_metalinguagem_deve_inspecionar_href_nao_so_texto_20260815.md`

## D-2026-08-14-04 — Priorizar ZCode por custo + fallback ativo Grok (14/08 02:45+02:50)

**Causa raiz:** decisão de qual agente usa qual tarefa afeta custo total
**Fase que falhou:** N/A (regra operacional)
**Fix estrutural:** tarefa mecânica → ZCode primeiro (GLM-5.2 mais barato). Grok = fallback ATIVO após 2h sem resposta ZCode. Claude Opus = editorial/decisão/publish
**Fix paliativo:** N/A
**Como verificar:** planilha de custos por agente / semana
**Referência:** `feedback_priorizar_zcode_por_custo_mais_barato_20260815.md`

## D-2026-08-14-03 — Teto fila 12h (14/08 12:50) — ⚠️ parte NO-HOME REVOGADA (ver D-2026-08-15-05)

**Causa raiz:** eu agendava posts 24-48h à frente, poluindo fila e afastando pauta do gancho
**Fase que falhou:** Claude editor
**Fix estrutural:** antes de agendar, ler fila REAL do WP. Se `último + cadência < NOW+12h` → agenda. Se estourou → **~~válvula NO-HOME~~** [REVOGADO 15/08 13:35] manter `pending` (ver D-2026-08-15-05)
**Fix paliativo:** N/A
**Como verificar:** monitor `wp post list --post_status=future` — nenhum >12h à frente
**Referência:** `feedback_teto_fila_12h_cadencia_valvula_nohome_20260814.md` + `feedback_v4_entra_normalmente_na_home_nao_cat_20699_20260815.md`

## D-2026-08-14-02 — Protocolo reserva anti-atropelo Trindade (14/08 12:30)

**Causa raiz:** 2+ daemons mexendo no mesmo post causavam conflito
**Fase que falhou:** coordenação
**Fix estrutural:** livros de reserva `ponte_imagens_RESERVA.md` (fm) e `RESERVA_TRABALHO.md` (patch). Reserva alheia <2h = ninguém pisa. Loops sincronizados: ZCode :00/:30, Claude :02/:32, Grok :17/:47
**Fix paliativo:** N/A (regra)
**Como verificar:** grep colisões em log rsync/git — 0 ocorrências pós-13/08
**Referência:** `feedback_protocolo_reserva_e_loops_sincronizados_trindade_20260814.md`

## D-2026-08-14-01 — Bug estrutural, não paliativo (14/08 12:13 + fix aplicado 12:52)

**Causa raiz:** erros reincidentes ficavam só na rede de segurança client-side, nunca fechavam upstream
**Fase que falhou:** meta-processo
**Fix estrutural:** ≥2 reincidências = fix upstream obrigatório. Delegar se não é meu escopo (ZCode pra fábrica, Grok pra observação/imagem, Miguel pra editorial)
**Fix paliativo:** N/A
**Como verificar:** contador de reincidências por bug — sempre decrescente após fix upstream
**Referência:** `feedback_erros_reincidentes_correcao_estrutural_nao_paliativa.md`

## D-2026-08-13-01 — Bug #1: nunca vazar metalinguagem IA (13/08 12:15)

**Causa raiz:** worker V4 pode vazar termos como "Claude/ChatGPT/GPT/DeepSeek/Gemini/Kimi/LLM/worker V4" em texto público
**Fase que falhou:** worker V4 + Claude editor
**Fix estrutural:** grep obrigatório antes de todo `wp_update_post` que toque conteúdo público
**Fix paliativo:** N/A (regra permanente)
**Como verificar:** grep no post_content pré-agendamento — 0 ocorrências
**Referência:** `feedback_nunca_vazar_metalinguagem_ia_bug_numero_1.md`

---

## Como worker V4 (ZCode) consome estas diretrizes

Ao aplicar fix upstream num regex do worker, verificar aqui se existe diretriz correspondente. Se não existe, criar quando o fix for aplicado.

Ao criar nova diretriz aqui, considerar se o worker precisa ser atualizado.

---

## Ritual de leitura obrigatório (todo agente Trindade)

Todo ciclo Vigília/loop, primeira ação:
```bash
cat "Cerebro/Foruns/V4_DIRETRIZES_APRENDIDAS.md" | head -80  # top 5 diretrizes
```
+
```bash
cat "~/.claude/projects/<path>/memory/MEMORY.md" | head -40   # top ~10 entradas
```

Custo ~200 linhas de texto por ciclo. Ganho: sistema não repete erro de ontem.
