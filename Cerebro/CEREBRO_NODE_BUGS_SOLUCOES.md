# 🐛 CÉREBRO NODE — Bugs, Erros & Soluções

**Função:** nodo canônico consolidando toda a memória de bugs do Cafezinho. Ponto único de consulta para qualquer agente (Claude Code, Codex, Kimi, GLM, futura sessão) antes de aplicar correção.

**Regra editorial de Miguel (2026-07-24 01:20 BRT):**
> "A cada loop, você encontrar qualquer coisa, você guarda. E você tem que, a cada correção, ler a memória de bugs para identificar se tem algum erro se repetindo e para encontrar a solução. O cérebro tem que ter uma sessão muito bem organizada de bugs, erros e soluções. Você tem que aprender, ter memória dos erros, encontrar os erros e consertar. Guardar tudo — depois a gente roda outra inteligência para te ajudar, tudo tem que estar no cérebro."

## 🎯 Protocolo obrigatório de correção

**ANTES de aplicar qualquer correção:**
1. Consultar este nodo (`CEREBRO_NODE_BUGS_SOLUCOES.md`) — ver se o padrão já foi identificado
2. Consultar `Outros/manual_de_bugs.md` — ver se tem entrada estruturada com fix validado
3. Consultar `Cerebro/monitoramento_horario/bugs_encontrados/bugs_*.jsonl` — ver frequência do bug em instâncias
4. Se bug conhecido → aplicar solução já validada (não reinventar)
5. Se bug novo → investigar + aplicar fix + REGISTRAR nas 3 camadas abaixo

**DEPOIS de aplicar qualquer correção:**
1. Anexar no JSONL do dia (`bugs_YYYY-MM-DD.jsonl`) — instância individual
2. Se for padrão novo → criar entrada no `manual_de_bugs.md` — padrão estrutural
3. Se for regra editorial/arquitetural → memória permanente em `~/.claude/.../memory/feedback_*.md`
4. Se for fix estrutural (código, prompt) → linha em `CEREBRO_NODE_ATUALIZACOES.md`
5. Atualizar contadores neste nodo

---

## 🗂️ Estrutura de armazenamento (3 camadas)

| Camada | Onde | Granularidade | Consumidor |
|---|---|---|---|
| **1. Instâncias** | `Cerebro/monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl` | Cada bug individual (data, post_id, link, tipo, detalhe, solução) | Análise de frequência, relatórios agregados |
| **2. Padrões** | `Outros/manual_de_bugs.md` (canônico) | Bug estrutural + causa raiz + fix validado + lição arquitetural | Consulta antes de reinventar fix |
| **3. Aprendizados** | `~/.claude/projects/-.../memory/feedback_*.md` + `MEMORY.md` | Regras editoriais/comportamentais derivadas de bugs | Sessões futuras de agente (memória de longo prazo) |

**Índice mestre:** este arquivo (`CEREBRO_NODE_BUGS_SOLUCOES.md`) — sempre atualizado.

---

## 📊 Bugs catalogados (padrões estruturais)

| # | Padrão | Descoberto | Status | Fix Downstream | Fix Upstream | Manual | Memória |
|---|---|---|---|---|---|---|---|
| 1-17 | Bugs históricos V3 (2026-04 a 2026-06) | vários | ✅ resolvidos | vários | — | `manual_de_bugs.md` | — |
| **18** | V4 gera drafts sem `featured_media` | 2026-07-21 | ✅ RESOLVIDO | Sentinela fallback fal.ai | ✅ Kimi patch consultivo + `repair_orphan_wp_draft` (22/07) | #18 | `project_esteira_youtube_cafezinho_20260721.md` |
| **19** | DeepSeek ignora cap dinâmico do código | 2026-07-21 | ✅ RESOLVIDO | prompt sincronizado com código | N/A | #19 | `feedback_sentinela_nunca_publicar_rascunhos_antigos.md` |
| **20** | V4 usa "Redir" como âncora (Folha) | 2026-07-22 | ⚠️ downstream corrigido, upstream pendente | Sentinela substitui via mapa | ⏳ Codex | #20 | — |
| **21** | DeepSeek substitui título por palavra corrigida | 2026-07-23 | ✅ RESOLVIDO | guarda-corpo + prompt | ✅ prevenção em código | #21 | — |
| **22** | V4 nomes de fonte colados/CAIXA ALTA | 2026-07-23 | ⚠️ downstream corrigido, upstream pendente | passo [4.5/6] auto-corrige 14 padrões | ⏳ Codex/Kimi | #22 | — |
| **D4** | Título com `;` (Cafezinho editorial) | 2026-07-23 | ✅ RESOLVIDO | prompt D4 + correção manual | N/A (padrão editorial) | (seção D4 no prompt) | `feedback_titulos_sem_ponto_virgula_com_autonomia.md` |
| **CHURN** | Rebaixar publish→draft (SEO ruim) | 2026-07-21 | ✅ REGRA | proibido em código | N/A | (regra) | `feedback_nunca_churn_publish_draft_seo.md` |
| **CAL** | LLM aluça dia da semana | 2026-07-23 | ✅ REGRA | conferir `date` sempre | N/A | (regra) | `feedback_conferir_calendario_antes_opinar.md` |
| **SEMANT** | Confundir "imperialismo" vs "entreguismo" | 2026-07-23 | ✅ REGRA | prompt Sentinela | N/A | (seção linha editorial) | `feedback_diretriz_editorial_governos_esquerda.md` |
| **META** | Sujeira `<em>Categoria</em>` no primeiro parágrafo | 2026-07-20 | ✅ RESOLVIDO upstream | prompt (grupo B) | ✅ Kimi: prefixo-marcador em `validar_editorial` + guarda em `html_para_wp` (24/07) | `feedback_sujeira_metadata_pipeline_v4.md` | idem |
| **23** | WP 403 intermitente health `v4_pipeline_imagem` (Cloudflare vs UA urllib) | 2026-07-24 | ✅ RESOLVIDO | UA explícito + retry backoff em `wp_get`/`wp_post` | N/A (Sentinela) | #23 | — |
| **24** | V4 dedup falhou: 262741 duplicou 262704 ~12h depois | 2026-07-24 | ✅ RESOLVIDO | DeepSeek segurava downstream | ✅ Kimi: `duplicate_recent_topic` no worker (corte pré-LLM, status terminal) + janela 24h + contenção de tokens no agente (24/07) | #24 | — |
| **SCORE** | Score policy home/no-home mal aplicada | 2026-07-22 | ⚠️ investigação em curso | — | ⏳ Codex investigar `decide_no_home()` | — | `project_no_home_score_policy_v1_20260721.md` |
| **TRIB** | Tribunal Kimi visual reprovava 4x | 2026-07-21 | ✅ RESOLVIDO | — | ✅ Kimi patch consultivo (22/07 05:53 UTC) | #18 relacionado | — |
| **37** | LLM juiz sem gate WebSearch acusou erro factual em post CORRETO (Fachin/STF, post 262949) | 2026-07-26 | ✅ RESOLVIDO | gate Wikipedia→Brave→SearchAPI + cache SQLite no hook `propor_correcao_semantica` (fail-safe: só DESCARTADO-web-contradiz bloqueia) | ✅ regra "⚠️ knowledge cutoff" em prompts.md (`fact_check_required` + entidade + afirmacao_do_texto) — Kimi K3 | #37 | — |
| **38** | "Brave desativado no V4" — diagnóstico refutado (evidência era de agente legado); causa real dos 0-itens ceara = RSS G1 servindo 2018 + gov.br morto | 2026-07-26 | ✅ RESOLVIDO | +2 feeds frescos em ceara.json (cearaagora + g1/politica): coletor 0→16 itens | ✅ busca.py blindado: `chaves.get_key` central em vez de os.environ direto — Kimi K3 | #38 | — |
| **META-39** | Smoke offline (`--status`) diz "verde" mas modelo/endpoint não existe no wire — casca de banana clássica ao integrar API externa | 2026-07-28 | ✅ REGRA + memória | Kimi K3 Desktop pegou bug P0 no `consulta_kimi_memoria_total.py` do Claude (`kimi-k2-turbo-preview` não existe em nenhum canal Moonshot) via `GET /models` ao vivo; AUTOCURA 6 edições + backup SHA-256 + smoke real de 2 centavos | ✅ REGRA daqui pra frente: **smoke de script API precisa 1 chamada real de centavos**, não só `--status`. Validação offline pega 30% dos bugs; online pega 90% — diferença = bugs de contrato entre sistemas | — | [`Cerebro/Memorias/memoria_smoke_api_chamada_real_20260728.md`](Memorias/memoria_smoke_api_chamada_real_20260728.md) (espelhado do `feedback_smoke_de_api_precisa_chamada_real_de_centavos` na memória privada Claude) |
| **EVENTO-40** | Agente confunde evento principal com etapa paralela e mistura datas/quantidades (Guarnicê, post 266143) | 2026-08-17 | 🔴 CORREÇÃO DO POST PENDENTE; ✅ REGRA CRIADA | revisão humana do 266143 | §124 + ficha factual e gate WebSearch em `regra_evento_principal_etapas_paralelas_v4_20260817.md` | EVENTO-40 | regra canônica em `Foruns/diretrizes/` |

## 📈 Métricas agregadas por dia (JSONL)

Atualização automática pelo Sentinela.

| Data | Instâncias registradas | Tipos mais comuns |
|---|---:|---|
| 2026-07-21 | 2 | agregador_como_fonte_visivel |
| 2026-07-22 | 1 | agregador_como_fonte_visivel |
| 2026-07-23 | 46 | fonte_colada_camelcase (20+), proposta_correcao (14+), ponto_virgula_titulo (3) |
| 2026-07-24 | 18 | fonte_colada_camelcase (auto), proposta_correcao, fixes upstream #23/#24/META |

---

## 🔍 Tipos de bug e mapeamento pra manual/memória

Quando registrar novo bug no JSONL, usar `tipo_bug` desta lista canônica (evita fragmentação):

| tipo_bug | Descrição | Manual | Solução automatizada? |
|---|---|---|---|
| `sujeira_metadata_slug` | `<em>Categoria</em>` no primeiro parágrafo | #META | ✅ upstream Kimi 24/07 (validar_editorial + html_para_wp) |
| `fonte_colada_camelcase` | Nome de veículo colado (TheHindu, agenciabrasil) | #22 | ✅ passo [4.5/6] auto-corrige |
| `agregador_como_fonte_visivel` | Âncora "Redir" em vez de "Folha" | #20 | ✅ passo [4.5/6] (Redir mapeado) |
| `ponto_virgula_titulo` | `;` em título editorial | D4 | ✅ prompt DeepSeek + manual |
| `nome_proprio_sem_contexto` | Vorcaro/Hugging Face sem contextualizar | D2 | ⚠️ DeepSeek marca, Miguel decide |
| `partido_minuscula` | Pt/Pp/Psdb em minúsculas | D3 | ✅ prompt DeepSeek |
| `dia_semana_alucinado` | LLM aluça calendário | CAL | ✅ regra `date` obrigatório |
| `titulo_truncado_elipse` | `…` HTML no título | D4 | ✅ prompt DeepSeek |
| `titulo_substituido_por_correcao_parcial` | diff_titulo.new curto demais | #21 | ✅ guarda-corpo Python |
| `fact_check_grave` | Cargo/data/valor errado (V4 Nacional) | (prompt) | ⚠️ DeepSeek escala, humano decide |
| `evento_etapa_confundida` | Evento principal confundido com mostra/etapa paralela; datas ou universo contado fundidos | EVENTO-40 | ✅ gate editorial: fonte oficial + ficha factual; dúvida fica pending |
| `duplicata_publish` | Mesmo tema já publicado <24h | #24 | ✅ upstream Kimi 24/07 (worker pré-LLM + agente 24h) |
| `wp_api_403_intermitente_health_v4_imagem` | Cloudflare bloqueia UA Python-urllib | #23 | ✅ UA explícito + retry (24/07) |
| `assinatura_estagiario_agencia_brasil` | `*Estagiário da Agência Brasil sob supervisão de X` no rodapé | #25 | ✅ upstream repetidor estatal 3 regex + limpeza in-place (24/07) |
| `texto_dentro_charge_flux` | Charge fal.ai/Flux com texto dentro (truncado). Função tóxica `_prompt_flux_com_texto_permitido` no gerador | #26 | ✅ função revogada + reforço anti-texto + regeneração in-place (24/07) |
| `texto_dentro_cartao_v4_regressao` | Tribunal V4 (`audit_generated_cartoon`) PERMITIA texto em flux-pro/fal.ai + juiz Kimi com chave 401 e auditoria fail-open | #26R | ✅ REGRA DE TEXTO inquebrável (qualquer texto = hard_block, todo gerador) + juiz em cadeia Kimi→Qwen-VL; validado ao vivo (29/07) |
| `image_pending_sem_recovery` | Draft V4 sem featured_media | #18 | ✅ Kimi repair_orphan |
| `framing_editorial_errado` | "entreguismo de Trump" (troca imperialismo) | SEMANT | ⚠️ regex + prompt (novo) |
| `proposta_correcao` | Genérico — DeepSeek propôs mas não aplicou | — | (revisão humana) |
| `outro` | Não categorizado ainda | — | — |

Se tipo novo aparecer, adicionar aqui + criar entrada no manual.

---

## 🎬 Como novos agentes usam este nodo

**Ao começar sessão nova (Claude, Kimi, Codex):**
1. Ler `CEREBRO_NODE_BUGS_SOLUCOES.md` (este arquivo) — panorama geral
2. Se for tocar em correção editorial → ler `Outros/manual_de_bugs.md` (padrões)
3. Se for tocar em código Sentinela → ler `~/ferramentas/sentinela/config/prompts.md` (regras)
4. Se detectar bug novo → registrar nas 3 camadas + atualizar tabelas deste nodo

**Ao aplicar correção específica:**
1. Grep no JSONL (`grep -h 'tipo_bug' bugs_*.jsonl | wc -l`) — ver frequência
2. Se >5 instâncias históricas → provavelmente já tem padrão no manual, procurar
3. Se manual tem fix validado → aplicar direto
4. Se manual não tem → criar entrada nova depois do fix

---

## 📅 Ritual semanal (a partir de 26/07)

Toda sexta-feira 23:00 BRT, script agregador gera:
- `Cerebro/Foruns/bugs_semana_YYYY-WW.md` — relatório da semana
- Top 5 tipos_bug por frequência
- Fixes aplicados (downstream + upstream)
- Bugs recorrentes que precisam atenção estrutural
- Anexo em `CEREBRO_NODE_ATUALIZACOES.md`

Script pendente de criação: `~/ferramentas/sentinela/relatorio_semanal_bugs.py`

---

## Assinatura

Nodo criado por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-24 01:25 BRT.

Manutenção: qualquer agente que registrar bug novo DEVE atualizar as tabelas acima. Se a manutenção decair, Miguel me lembra.
