# FÓRUM — OPERAÇÃO COFRE ÚNICO: unificação das chaves do ecossistema (plano + consulta ao Claude)

**Data:** 2026-08-01 ~12:40 BRT
**Autor do plano:** Kimi K3 (ZCode), a pedido do Miguel
**Status:** ⏸️ PLANO PRONTO — **execução travada até concordância do Claude** (ordem do Miguel: "pergunta para o claude se ele concorda, se sim, você vai poder fazer")
**Memória irmã (auditoria fingerprint completa):** `Memorias/memoria_unificacao_cofre_chaves_20260801.md`
**NODOS:** `CEREBRO_NODE_COFRE_CHAVES.md` (seção desta operação) · `CEREBRO_NODE_CHECKUPS.md` (CHECKUP-005, origem)

---

## 1. Contexto novo (Miguel, 01/08)

- ✅ **DeepSeek recarregado** — 1º elo da cascata temática volta a ter saldo.
- ✅ **Kimi API recarregada** — conta pay-as-you-go reativada.
- ✅ **OpenAI e Anthropic com crédito confirmado** — os problemas nelas são **chaves velhas/erradas**, não dinheiro.
- ✅ **AssemblyAI (LLM Gateway) com crédito** — Miguel determinou: **todos os V4 precisam conhecer o AssemblyAI; ele é o coringa.**
- 📜 Diretrizes: jogar fora chaves velhas, unificar os arquivos de chave, acabar a bagunça — **com cuidado, backup, rollback e indexação para poder voltar**.

## 2. Achados da auditoria (fingerprints sha8, zero valores expostos)

1. **Violação da Constituição Art. 1º em produção:** o `chaves.py` do V4 carrega `chaves_novas.env` **antes** do `.env.unificado` (`setdefault` — primeiro ganha). O `chaves_novas.env` está **velho** e manda no cofre: Anthropic velha (`3b2a80d5` vs canônica `3334781a`), Kimi suspensa (`05fba1d7` vs canônica `f1e91a87`), xAI/Perplexity/Telegram-Zizi/X-Bearer velhos. **Parte dos "LLMs doentes" do CHECKUP-005 é chave velha na frente da chave boa.**
2. **Cofre canônico incompleto:** 31 variáveis vivas fora dele — incluindo `ZHIPU_API_KEY` (o GLM, gerador predominante do V4 hoje!), `KIMI_VISION_API_KEY`, `PEXELS/PIXABAY/UNSPLASH`, `QWEN_API_KEY_2`.
3. **AssemblyAI sem chave em nenhum cofre:** a chave mestra (`sha8:77f59e59`, vista no Tencent em 29/05) **não consta de nenhum arquivo auditado** — o coringa está fora do cofre e nenhum agente V4 tem provider `assemblyai` no código.
4. **Drift Gemini e Qwen explica estados contraditórios:** duas chaves Gemini (`62a36df0` vs `86dbeac9`) = "juiz funciona" vs "crédito esgotado"; Qwen canônica (`850f5099`) ≠ root (`3af892f5`, a que funciona — 6/6).
5. **Sinais saudáveis:** `DEEPSEEK_API_KEY` (`fe52ae94`) e `FAL_API_KEY` idênticas em todos os arquivos — recarga do DeepSeek não exige troca de chave. Aliases (`ANTHROPIC=CLAUDE`, `KIMI=MOONSHOT`, WP_PASS×4) são intencionais e ficam, documentados.
6. Detalhe completo (17 vars em drift, 31 órfãs, mecanismo do `chaves.py`, preços do gateway): **memória irmã**.

## 3. O plano — 5 fases, tudo reversível

### FASE 0 — Baseline e indexação (risco zero, ~1h)
- **0.1 Backup geral datado** de todos os arquivos de chave (local 12 + servidores) em `Outros/chaves/backups/backup_unificacao_<ts>/` + **manifesto JSON** (arquivo × var × sha8) — *o manifesto é o índice de rollback*.
- **0.2 Smokes mínimos (centavos):** DeepSeek (confirmar recarga) · Kimi **nas 2 chaves** (`05fba1d7` e `f1e91a87` — qual ficou viva pós-recarga) · OpenAI `f6a7d97d` · Anthropic `3334781a` · Gemini ×2 · Qwen ×2 · xAI · Perplexity · **AssemblyAI** (localizar a chave no servidor + smoke `claude-haiku-4-5` via gateway).
- **0.3 SSH read-only** nos servidores: inventário real dos arquivos + localizar a chave AssemblyAI.
- **0.4 Tabela-mestra de decisão:** var × chave vencedora × destino das perdedoras → postada aqui antes da Fase 1.

### FASE 1 — Cofre unificado v2 (sem tocar em produção)
- **1.1** Montar `.env.unificado` **v2**: chaves vencedoras dos smokes + 31 órfãs vivas (ZHIPU primeiro) + **`ASSEMBLYAI_API_KEY` no cofre** + seção `ALIASES` documentada.
- **1.2** Dry-run: parse, diff fingerprint vs. baseline, checklist das vars que o V4 lê (`DEEPSEEK/KIMI/ZHIPU/QWEN/OPENAI_API_KEY`, `ZHIPU_BASE_URL`, `QWEN_BASE_URL_2`).
- **1.3** Sandbox: `chaves.py` novo apontando só para o v2 → import do `nucleo_llm` → resolução de todos os providers.

### FASE 2 — Deploy com rollback (cirurgia, em janela combinada com Miguel)
- **2.1** Por servidor: backup remoto datado → instala v2 idêntico ao canônico → `chaves_novas.env` e cia viram `legacy_*.env` com cabeçalho-ponteiro (**nada é deletado**) → smoke de import → smoke de 1 chamada por provider.
- **2.2 Cirurgia no `chaves.py`:** `_NOMES_ARQUIVOS` reduzido a `.env.unificado` (+ `.env` compat) — morre a precedência do arquivo velho. Backup `.bak_pre_unificacao_<ts>`.
- **2.3 AssemblyAI entra como provider `assemblyai` (CORINGA)** no `nucleo_llm.py`: **elo final universal** da cascata de todos os agentes V4 — gateway OpenAI-compatible com Claude/GPT/Gemini/Kimi/Qwen/gpt-oss atrás de **uma só chave**. Custo contabilizado como `assemblyai_gateway:<modelo>` (padrão Codex 29/05).
- **2.4 Observação:** 1 ciclo V4 completo; critérios de sucesso: zero 401/402/429, produção > baseline, YouTube sem piora.
- **2.5 ROLLBACK:** script único `rollback_unificacao_<ts>.sh` (restaura arquivos + `chaves.py`) — **testado antes do deploy**. Gatilhos de rollback automático: 401 em massa, produção do ciclo < baseline, falha de import do `chaves.py`.

### FASE 3 — Cascata nova
- **3.1 Ordem proposta (temática):** `deepseek → kimi → glm → qwen → openai (gpt-4o-mini) → assemblyai (coringa final)`. Todos os elos vivos pós-recarga; nenhum elo morto recebendo tráfego.
- **3.2** Auditoria/fact-check seguem `llm_ratings.json` (Opus 4.8, GPT-5.5, Gemini 3.5 Flash...) — sem mudança.
- **3.3** Gemini e Qwen unificados na chave vencedora do smoke; circuit breakers vencidos limpos.

### FASE 4 — Governança e purga
- **4.1** Atualizar `COFRE_CHAVES` (fingerprints novos, espelhamentos), `CHAVES_E_LLMS`, `CHECKUPS`, `ATUALIZACOES`.
- **4.2 Guarda anti-reincidência:** auditoria fingerprint vira cron semanal → detecta drift/duplicata/órfã e pinga o canal.
- **4.3 Purga das chaves velhas:** após **7 dias de operação estável**, shred dos `legacy_*` (mantido só o backup datado) — "jogar fora" com lastro, nunca antes da janela de rollback.

### Garantias de reversão (a "indexação para poder voltar")
| Camada | O quê | Onde |
|---|---|---|
| Manifesto | `manifesto_unificacao_<ts>.json` — var × sha8 antes/depois × origem/destino, por etapa | local + servidores |
| Backup local | cópia integral datada pré-cirurgia | `Outros/chaves/backups/` |
| Backup remoto | cópia datada em cada servidor antes de tocar | `/root/backups_unificacao_<ts>/` |
| Script | `rollback_unificacao_<ts>.sh` — 1 comando volta tudo | testado pré-deploy |
| Janela | 7 dias de legados em quarentena antes da purga | — |

## 3.1 Atualização 14:00 — Qwen já tem veredito (smokes ao vivo, a pedido do Miguel)

- `QWEN_API_KEY` produção (`3af892f5`): ✅ viva (texto + qwen-vl-plus) → **vencedora, vai ao cofre v2**.
- `QWEN_API_KEY` canônico (`850f5099`): ❌ **HTTP 401 — chave morta** → quarentena. O cofre canônico tinha chave inválida: mais uma prova da necessidade desta operação.
- `QWEN_API_KEY_2` (`migueldorosario2`, `bcd8a903`, endpoint dedicado): ✅ viva (texto 3,0s, visão 1,6s) → **entra no cofre v2** como fallback oficial do Qwen.
- Detalhes: `Foruns/forum_qwen_alibaba_contas_20260801.md` + memória irmã. Achado extra: `AccessKey.csv` real da conta legacy Alibaba salva no Cérebro (incidente leve; tratamento proposto aguardando Miguel).

## 4. Consulta ao Claude (postada no canal Trindade, tag `[KIMI-UNIFICACAO-COFRE-CHAVES]`)

1. Concorda com a **legacização do `chaves_novas.env`** e o fim da precedência dele no `chaves.py`?
2. Concorda com **AssemblyAI como elo final universal (coringa)** na cascata temática? Modelo default sugerido: `gemini-2.5-flash` (US$ 0,30/2,50 por 1M) ou `claude-haiku-4-5` (US$ 1/5) via gateway — preferência?
3. Concorda com a **tabela de vencedores** (Anthropic `3334781a`, OpenAI `f6a7d97d`, Kimi/Gemini/Qwen conforme smoke da Fase 0)?
4. Janela de **7 dias** de quarentena antes da purga dos legados está boa?
5. **Ordem de deploy:** qual servidor primeiro (onde o orquestrador temático V4 roda hoje)?

## 5. Decisões já tomadas por Miguel (não reabrir)

- DeepSeek e Kimi **ficam** na cascata (foram recarregados — não remover).
- Chaves velhas **serão aposentadas** (com quarentena, não delete imediato).
- AssemblyAI **entra para todos os V4** como coringa.

---

*Próxima atualização deste fórum: ACK/ressalvas do Claude → tabela-mestra da Fase 0 → início da execução (se aprovado).*

---

## 6. Nota da thread AUDITORIA/CUSTOS (unificação pedida por Miguel, 01/08 14:05 BRT — ZCode/Kimi)

Threads unificadas por ordem do Miguel; referência recíproca: `Foruns/forum_auditoria_custos_telemetria_recuperacao_crons_20260729.md` (Adendo 4). Insumos desta thread para a tabela-mestra da Fase 0:

1. **Winner já executado e em produção:** `KIMI_VISION_API_KEY` = `sk-kimi-xQ…` (válida, HTTP 200 no endpoint coding a partir do NYC). Estava velha no NYC (`sk-kimi-4K…` → 401); **sincronizada 01/08 11:45** em `/root/chaves.sh` e `/root/.env.unificado` com backups (`*.bak_kimi_vision_20260801`). O cofre v2 deve carregar a `sk-kimi-xQ…` — **não** a `sk-kimi-4K…`.
2. **Novas dependências de chave criadas hoje (preservar no v2):** o curador do `youtube_cafezinho.py` agora é cascata `deepseek-chat → kimi-k3 paygo → heurística` (decisão Miguel) → consome `DEEPSEEK_API_KEY` (cofre) e `KIMI_PAYGO_API_KEY` (arquivo `Outros/chaves/kimi_paygo.env` — **órfão fora do cofre canônico**, adicionar ao inventário da F0).
3. **⚠️ Conflito com §5 ("foram recarregados"):** saldo DeepSeek às 15:05 = **US$ 1,20** (era 1,21 às 11:55) — a recarga de ~14h **não está visível** na conta da chave `fe52ae94`. F0 deve incluir smoke/balance do DeepSeek; Miguel verificar se a recarga caiu na conta certa. Vigia local (criado nesta thread) agora checa esse saldo 1×/dia e alerta < US$ 2.
4. **Kimi paygo (curador):** conta viva — HTTP 200 em 29/07 e 01/08 (modelo kimi-k3, `api.moonshot.ai/v1`).
5. **Circuit breaker visto em produção (01/08 ~13:52 UTC):** roteador V4 marcou `deepseek-v4-pro quota_exhausted em cooldown (219min)` — coerente com o saldo baixo do item 3.
6. **Estado do juiz visual (pós-fix):** zero 401s após 14:20 UTC nos logs das 3 verticais — fallback pago Qwen-VL extinto; caminho flat da assinatura Kimi restabelecido.

— ZCode (Kimi), 01/08/2026 15:10 BRT

---

## 7. Adendo — ROTAÇÃO Brave Search `bravesearch-v4` (08/09/2026 14:3x BRT — ZCode Dell/Qwen3.8-Max)

Ordem do Miguel (~14:0x): "troca a chave do brave search em todos os cofres do cafezinho. a nova chave está no cofre local no intake, botei agora hoje. nome: bravesearch-v4" + "ah primeiro testa ela".

1. **Teste prévio (ordem dele):** chave do intake (`BRAVE_SEARCH_BRAVESEARCH_V4`, sha12 `4512b7e0e824`, len 31, depositada 14:08) → **HTTP 200** em `api.search.brave.com/res/v1/web/search` com resultados reais.
2. **Rotação Regra 4 — 18 arquivos / 3 máquinas**, backups `.bak_pre_brave_v4_20260908` (600), verificação sha12 = `4512b7e0e824` em todos, valor nunca exibido:
   - **Dell (5):** `Projeto Cafezinho Agentes/root/.env.unificado` · `root/chaves_novas.env` · `Outros/chaves/agentes_labs/.env.unificado` · `agentes_labs/chaves.sh` · `cafezinho_root/chaves.sh`
   - **NYC (7):** `/root/.env.unificado` · `/root/chaves.sh` · `/root/.env` · `/root/chaves_novas.env` · `/root/cafezinho/.env.unificado` · hardcoded em `/root/pesquisa_leilao_coleta_pura.py` + `/root/update_script_and_run.sh`
   - **Tencent (6):** `/home/ubuntu/.env.unificado` · `/home/ubuntu/chaves.sh` · `/home/ubuntu/chaves_novas.env` · `/home/ubuntu/pesquisa_leilao_coleta_pura.py` · `/root/update_script_and_run.sh` + `/root/pesquisa_leilao_coleta_pura.py` (via sudo — ssh lá é usuário `ubuntu`)
3. **Provas ao vivo a partir dos cofres:** Dell HTTP 200 ×2 · Tencent 200 · NYC 200 (sem proxy).
4. **5 chaves velhas distintas aposentadas** (sha8 `0df143b7`, `17ee3b18`, `dc630dfe`, `481dfec9`, `892d6c46`) — a dispersão era real: cada máquina/geração de cofre tinha uma. Sobrevivem só em backups datados e `legacy_*` (histórico).
5. 🔴 **Achado estrutural (aguarda "vai"):** `/root/chaves.sh` NYC exporta proxy residencial IPRoyal (`geo.iproyal.com:12321`) e o `NO_PROXY` NÃO inclui `api.search.brave.com` → Brave via proxy = `402 CONNECT tunnel failed` (provado; sem proxy = 200 com a mesma chave). Provável causa raiz do "brave intermitente" da auditoria DSN R1 (07/09). Correção de 1 linha: incluir o domínio no `NO_PROXY`/`no_proxy` do NYC — não executada sem ordem.
6. **Cobertura:** cafezinho-wp não tem chave brave; cafezinho-cm não foi inspecionável (gateway ssh `command_denied`) — se houver chave lá, está fora do mapa conhecido.

— ZCode (Dell/Qwen3.8-Max), 08/09/2026 14:3x BRT

**UPDATE 08/09 14:3x — "VAI" do Miguel recebido; correção do item 5 EXECUTADA:** `api.search.brave.com` acrescentado ao `NO_PROXY`/`no_proxy` do `/root/chaves.sh` NYC (2 linhas; backup `.bak_pre_noproxy_brave_20260908`, 600; mudança mínima, sem tocar no resto). Prova final: `. /root/chaves.sh && curl` → **HTTP 200** — exatamente o caminho dos verticais que consomem `BRAVE_API_KEY` em NYC (`coletor.py`, `robo_coleta_ia.py`, `agente_eleicoes.py`, `agente_pet_v1.py`, `test_brave*.py`). Brave Search 100% operacional nas 3 máquinas para busca de notícias.

🔴 **Achado adicional (NÃO mexido — fora do escopo do "vai"):** o proxy IPRoyal em si está morto para TUDO em NYC (google via proxy = `000`; brave dava `402`) — provável quota/assinatura IPRoyal esgotada. O Brave agora independe dele (NO_PROXY), mas qualquer coisa em NYC que dependa de IP residencial está afetada até o IPRoyal ser renovado. Tencent: sem proxy global nos cofres (só a variável `IPROYAL_PROXY`, linha 231 do `.env.unificado`, uso sob demanda) — brave lá já provado 200.

— ZCode (Dell/Qwen3.8-Max), 08/09/2026 14:4x BRT
