# 🖼️ IDEIA_PRO_DSNUVEM_IDEIAS-008 (parte 1) — SISTEMA DE IMAGEM END-TO-END: diagnóstico do acervo inteiro + o que LIGAR (régua 3 níveis + transição em fases)

> **Encomenda:** DSC (Terminal celular do Miguel) · 01/09/2026 ~23:1x BRT · via `ponte_laura_completa/de_ideias.md`. Pedido do Miguel: **"oferecer o banco de links para o agente DSN imagem — já temos muita coisa"** · o estudo de imagem vira **capítulo forte da Constituição** (Título VII) · saída esperada: diagnóstico + o que LIGAR, na régua 3 níveis do plano DSC-016 (correta → jornalística → bonita) + transição em fases.
> **Natureza:** DIAGNÓSTICO + DESENHO (arquitetura de dados/fluxo). Rascunhos aqui, NUNCA em produção. Execução exige ✓ do Miguel. A parte 2 (Compilação Mestre/dossiê) está em `2026-09-01_compilacao_mestre_dossie_noite.md`.
> **Refs lidas:** `forum_sprint_v41_vision_zm_20260831.md` (sprint Vision: F1 fechada, fusão dsn_imagem, emenda NO-IA, ZM-SPRINT 001-015) · `relatorio_banco_ouro_dia_20260901.md` (Degraus 1/2/3) · `plano_trabalho_contrato_v3_lancamento_v42_20260901.md` (DSC-016 §1.4 e §2) · `forum_mutirao_qwen_banco_midia_v4_20260809.md` (90 SELECTED_HIGH) · `BANCO_DE_LINKS_MIDIA_CANONICO.md` (catálogo 20/08, ORDEM_MIGUEL) · `ideias/2026-08-31_autocura_3_problemas_ideia003.md` (P3 Banco Ouro) · `ideias/2026-09-01_contrato_v3_constituicao.md` (006 §5, Título VII) · `ideias/2026-09-01_cacada_13_midia_3a_chave_relogio_revisor.md` (gate mídia 3 vias) · `memoria_capas_v41_pipeline_deepseek_20260829.md` (11h paradas de 29/08).

---

## 0. SÍNTESE EXECUTIVA (o acervo inteiro em 10 linhas)

A casa tem **6 acervos/fontes de imagem** e **um sistema de aplicação já no ar** — mas eles **não conversam**: o worker caça capa 24/7 (no ar desde 31/08, visão dupla, executor único, NO-IA), enquanto o **Banco Ouro V3 (1.214 fotos aprovadas) dorme sem ser consultado**, o **catálogo canônico de links (BANCO_DE_LINKS_MIDIA_CANONICO.md) não alimenta nenhuma fila**, o **mutirão V4 (90 SELECTED_HIGH) não foi integrado ao banco consultado**, e o **runtime de visão que causou as 11h paradas de 29/08 está integrado mas com 2 das 4 fases do sprint pendentes** (F2 tese-no-nascimento, F3 Scout, F4 aprovação anual). **Diagnóstico em uma frase: o problema não é falta de ativo — é falta de CONEXÃO entre os ativos.** Este estudo cataloga os 6 acervos, o fluxo atual, e o que LIGAR em cada nível da régua (correta → jornalística → bonita), em fases com rollback.

---

## 1. MAPA DO SISTEMA HOJE (componentes, onde roda, status)

### 1.1 Aplicação (o pipeline que JÁ roda)
| Componente | Onde | Status |
|---|---|---|
| `dsn_imagem.py` (scheduler da fila WP → request de capa) | NYC, cron `*/20` com flock | 🟢 **NO AR** desde 31/08 (fusão ZM-SPRINT-V41V-006) |
| `featured_image_runtime.py` (cascata: banco próprio → Flickr allowlist → Commons/Openverse → **variação de tese** → `fila_caca.jsonl` + Telegram) | NYC (`/root/v4_labs/`) | 🟢 no ar, **SEMPRE `--no-ai`** (emenda NO-IA 31/08 11:30: IA generativa PROIBIDA como capa; `wp_apply_featured_image.py` REJEITA decisão `ai_editorial_illustration` como blindagem) |
| Visão dupla (`media_vision_providers.py`): DeepSeek Vision primário × Qwen secundário + Gemini fallback; gates identidade ≥0.90 · centralidade ≥0.72 · crop-safe · logo barrado | NYC | 🟢 no ar (F1 provada: 268380/268393/268394) |
| `wp_apply_featured_image.py` (executor ÚNICO: upload REST, carimbo `_cafezinho_img_check` casado, sha256/MD5, metas `_cafezinho_capa_*`, readback; dry-run por default) | NYC | 🟢 no ar (dry-run validado; `--execute` só com aprovação CM+Miguel) |
| **F2 restante** — ligar a tese no NASCIMENTO (`v41_ciclo.py` + `curadoria_tese.py`) e mapear categoria→editoria canônica | NYC | 🟡 pendente (mexe em produção — protocolo ZM-011) |
| **F3** — `V4AuditedMediaStore` + `V4MediaScoutAgent` (banco próprio cresce 100-500/dia, custo Vision -50%) | NYC | 🔴 pendente |
| **F4** — aprovação anual do banco V4 (o bloqueio antigo do Miguel) | NYC/Tencent | 🔴 pendente |

### 1.2 Aplicação manual (a via humana, paralela)
- **AGY-Laura (set-media)** caça/vê/aplica capas e sanea legendas sob Consenso Duplo (AL-017/018/022/030/037/039…); **CL** audita e aprova (CL-011/012/017/027…); **Tribunal Visual** como instância de decisão. Em 01/09 a via manual saneou 3 furos da classe do gate pulado (268440/268553/268511 — 268511: capa no ar 84s depois com caption "default").

### 1.3 Os 6 ACERVOS/fontes (o patrimônio) — e o estado de conexão de cada um

| # | Acervo/fonte | Conteúdo | Local | CONECTADO ao runtime? |
|---|---|---|---|---|
| 1 | **Banco Ouro V3** | **1.214 fotos aprovadas/R2** (top: Lula, Flávio Bolsonaro, Trump, Haddad, Alckmin, Alcolumbre, Bolsonaro, Moraes, Motta) | master Tencent (`banco_midia_ouro_v3.db`), réplica NYC | 🔴 **NÃO consultado** (ouro parado — IDEIA-003 P3; endossado CL-041 §12). Degrau 1+2 executados 02:20 (adapter sombra `OURO_CAMADA1=0/log/1`; `sombra_camada1.jsonl` medindo; POC 11:1x Trump/EBC: **olho duplo REPROVOU — pessoa certa, contexto errado** → lição: rank contextual). Degrau 3 (ligar) **aguarda "vai" do Miguel** com régua ≥80%/N≥20 POR VERTICAL em 2 fases |
| 2 | **Catálogo canônico de links** (`BANCO_DE_LINKS_MIDIA_CANONICO.md`) | tabela por personagem/entidade → fonte primária + links + licença (Flickr Planalto/MF/MEC/Senado/Câmara/STF/TSE, GovCE, Wikimedia Commons, Fotos Públicas candidata) | repo | 🔴 **NÃO consumido** (nenhum request de capa lê o catálogo; não existe coluna `fonte prevista` na fila) — **é o pedido do Miguel: "oferecer o banco de links para o agente DSN imagem"** |
| 3 | **Mutirão banco mídia V4** (09/08, Qwen/Z-Code) | **90 `SELECTED_HIGH`** (nome inequívoco + licença CC/PD + ≥1600×900, "pode ir a tribunal") + 31 top-1 de dossiês | manifestos em `manifestos_mutirao_midia_v4/` + banco V4 | 🔴 **não integrado ao banco consultado pelo runtime** (funil fechou 90+3+12+186+51+10+1=353 em 09/08; gate de ingest ficou AMARELO) |
| 4 | **Allowlist Flickr oficial** (`config/v4_flickr_official_accounts.json`) | senado, lula, planalto, agencia_brasil, camara, stf, tse, governos, prefeituras (extensível) | NYC | 🟢 **consultada** (2ª na cascata; provada 268393/268394) — faltam contas (mapeamento §3 DSC-016) |
| 5 | **Wikimedia Commons** | só DATADA e relevante (regra da casa) | externo | 🟡 consultado mas **HTTP 429 recorrente** (throttle por IP vs datacenter; proxy IPRoyal integrado 31/08 com kill-switch `PROXY_OFF` — melhora, não resolve) |
| 6 | **IA generativa** | PROIBIDA como capa (emenda NO-IA 31/08) | — | 🔴 desligada (blindagem dupla no executor) |

### 1.4 A régua de qualidade (o que o contrato vai exigir — DSC-016 §1.4)
**CORRETA** (pessoa/tese certa, visão dupla) → **JORNALÍSTICA** (frescor, contexto do fato, proibida institucional genérica antiga) → **BONITA** (nitidez, resolução, enquadramento, momento — "foto do Lula CERTA existe aos montes; foto do Lula BOA é outra coisa").

---

## 2. DIAGNÓSTICO — o que está LIGADO × o que está PARADO

**🟢 LIGADO (não mexer):** worker 24/7 + visão dupla + executor único + NO-IA + variação de tese + fila de caça humana (fila_caca/Telegram) + sanções manuais sob Consenso Duplo + allowlist Flickr.
**🟡 SEMI (existe, falta conexão):** tese no nascimento (F2 — o gerador ainda trabalha com "tese não definida" em alguns fluxos) · gate mídia 3 vias (a trava segurou 268412 mas NÃO 268474/268511 — virou canário 3 casos da caçada 13) · proxy IPRoyal (mitiga 429, teto GB/dia pendente) · calibração do gate de LUGAR (aguarda decisão CM+Miguel: pertinência temática vs identidade nominal).
**🔴 PARADO (o ouro):** Banco Ouro V3 (camada 1) · catálogo canônico de links (fonte prevista por entidade) · mutirão V4 (90 SELECTED_HIGH) · F3 Scout · F4 aprovação anual · métrica diária de acerto do worker (relatório DS-N Imagem com NOTA 1/2/3) · mapa de fontes canônicas P4 (coluna `fonte prevista` na fila de capas).

**Leitura honesta:** a casa aplica capa com um pipeline moderno, mas do lado de DENTRO (o acervo aprovado) o runtime quase não consulta — ele caça FORA (Flickr/Commons) o que já tem APROVADO dentro (Banco Ouro + 90 SELECTED_HIGH + catálogo). Inverter essa proporção é o objetivo do Título VII: **o acervo propõe primeiro; a visão decide; a caça externa é o fallback.**

---

## 3. O QUE LIGAR — na régua 3 níveis (correta → jornalística → bonita), em fases

### NÍVEL 1 — CORRETA (a imagem é da pessoa/tese certa)
1. **Banco Ouro como camada 1 da cascata (Degrau 3)** — ligar `OURO_CAMADA1=1` com os 3 pré-requisitos do relatório 01/09: **(a) rank contextual** (casar entidade + palavras-chave da legenda com a tese — a reprovação Trump×Lula ensinou), **(b) `url_origem` como fonte de download** (R2 fechado; alternativa: expor domínio público do portal — decisão futura), **(c) olho duplo continua juiz inalterado**. Régua de promoção POR VERTICAL: hit-rate ≥80% e N≥20/24h; Degrau 3 em 2 fases (liga só na vertical com N≥20; olho duplo = fail-closed). **Dono: ZM (runtime) + DS-N Imagem (relatório).**
2. **Catálogo canônico → `fonte prevista` por entidade (o pedido do Miguel)** — o `BANCO_DE_LINKS_MIDIA_CANONICO.md` vira o mapa P4 (fonte prevista na fila de capas): o request do worker chega com `fonte_prevista: "flickr:palaciodoplanalto"` etc. — o worker vai DIRETO à fonte canônica da entidade antes da busca livre. **É 1 tabela + 1 coluna: o maior ganho de acerto por real investido.** (O catálogo é ATIVO_E_CANONICO desde 20/08 — só não é lido.)
3. **Calibração do gate de LUGAR** — quando `prioridade=lugar/conceito`, exigir **pertinência temática** (visor confere tema) em vez de identidade nominal; identidade dura fica para `prioridade=pessoa` (Emenda 12). Aguarda decisão CM+Miguel; sem decisão o fail-closed continua (correto).

### NÍVEL 2 — JORNALÍSTICA (a imagem conta a notícia)
4. **Gate mídia 3 vias como lei (Título VII)** — publish exige legenda pt-BR + crédito + alt + `_cafezinho_img_check`; o gate_midia entra no `estado_gate` (caçada 13 P2) com canário dos 3 casos (268440/268553/268511); **legenda/crédito/alt capturados NA ORIGEM** (item de mídia entra na fila já pronto — mata o caption "default" na causa, DSC-016 §1.3.3).
5. **Mutirão V4 integrado** — os **90 SELECTED_HIGH** (09/08) entram no banco consultado pelo runtime (tribunal + ingest com readback; o gate ficou AMARELO em 09/08 — fechar o verde antes de integrar). 
6. **Frescor da foto como critério** — proibida institucional genérica antiga (fachada de palácio, arquivo desatualizado); quando o título tem nome próprio, prioridade máxima é foto RECENTE da pessoa (Emenda 12 — já é regra do sprint; vira lei do Título VII).
7. **Mapa de contas Flickr faltantes + Fotos Públicas** — tabela viva do DSC-016 §3 (prefeituras capitais, assembleias, esporte, cultura; Fotos Públicas voltou em parceria com Brasil de Fato — candidato NOVO).

### NÍVEL 3 — BONITA (a imagem vale a capa)
8. **Relatório DS-N Imagem com NOTA DE QUALIDADE 1/2/3 + taxa de acerto** — o relatório diário (prova de vida do cargo, caçada 2) passa a medir: acertos por nível (correta/jornalística/bonita), hit-rate do worker, miss → motivo (sem foto livre / contexto errado / 429). A régua de promoção (≥80%) usa esse número. **Dono: DS-N Imagem; eu consolido o bloco ao Miguel quando N≥20.**
9. **F3 Scout (banco próprio cresce)** — `V4MediaScoutAgent` varre a allowlist → classifica com Vision → aprovadas entram no `V4AuditedMediaStore`; meta 100-500/dia, custo Vision cai 50%+; o runtime consulta o banco ANTES do Flickr.
10. **F4 aprovação anual** — o bloqueio antigo do Miguel ("não consigo fazer aprovação anual do banco V4") vira fase do Título VII: reconciliar o banco antigo com a auditoria nova (readback + hash), substituindo a dependência LAURA-GROK.

### Transição em fases (protocolo da casa: backup → prova → registro → rollback escrito)
| Fase | O quê | Risco | Saída |
|---|---|---|---|
| **0 (papel)** | Este estudo vira o capítulo Imagem da Constituição (Título VII) + insumo do dossiê (008b) | zero | lei + diagnóstico |
| **1 (sombra, 24-48h)** | `OURO_CAMADA1=log` continua medindo; **catálogo→fonte_prevista em sombra** (o worker registra "se tivesse usado a fonte prevista, acertaria?") | zero (sombra) | hit-rate real POR VERTICAL + ganho do catálogo medido |
| **2 (canário)** | Banco Ouro camada 1 na vertical com N≥20 (pessoa-central provou 100% na POC); fonte_prevista ativa no canário; gate_midia 3 vias como lei | contido (canário) | régua 3 níveis calibrada |
| **3 (promoção)** | Banco Ouro por vertical com hit ≥80% + mutirão V4 integrado; F3 Scout em paralelo | contido | rollback = flag `OURO_CAMADA1` + 1 arquivo/cron |
| **4 (oficial)** | Cascata: Banco Ouro (1.214 + 90 + Scout) → catálogo/fonte prevista → Flickr allowlist → Commons → variação → caça humana; IA generativa NUNCA | — | Título VII operando |

**Regras de ouro:** a esteira nunca para · nenhuma capa pelada no ar (Lei v2) · olho duplo é o juiz inalterado · rollback sempre de 1 arquivo/cron · nada em produção sem a régua + ✓ do Miguel.

---

## 4. RISCOS E REVERSIBILIDADE (protocolo da casa)

- **R1 — Banco Ouro propõe foto de contexto errado:** o rank contextual é o pré-requisito Nº 1 do Degrau 3 (a POC Trump×Lula reprovou exatamente isso) + olho duplo juiz; se a reprovação da camada 1 >20% na vertical, a flag volta a `log` (rollback de 1 flag).
- **R2 — Catálogo com link morto/licença errada:** o catálogo é curado por ORDEM_MIGUEL (20/08) mas precisa de revisão periódica; a visão dupla barra o conteúdo errado (o link morto só custa 1 tentativa — o worker cai para a próxima fonte).
- **R3 — 90 SELECTED_HIGH com gate AMARELO:** não integrar antes do tribunal/verde (funil fechou 353 em 09/08, ingest amarela) — integrar é Fase 3, depois da régua.
- **R4 — Mutirão e Banco Ouro = 2 bancos divergentes:** unificar na F3 (Scout usa o mesmo `V4AuditedMediaStore`; o master continua Tencent, réplica NYC, sync canônico — topologia do mutirão 09/08).
- **R5 — Métrica de acerto sem dono:** o relatório DS-N Imagem é a prova de vida do cargo (caçada 2: "robô no ar mas ZERO relatórios no repo") — sem relatório diário, a régua ≥80% não existe; é requisito de Fase 1.

---

## 5. O QUE PRECISO DO MIGUEL (respostas curtas bastam)

1. **✓ do diagnóstico** (o problema é conexão, não falta de ativo) e do plano em 4 níveis/fases?
2. **Banco Ouro camada 1:** autoriza o Degrau 3 (OURO_CAMADA1=1 por vertical com N≥20 + rank contextual + url_origem + olho duplo juiz)?
3. **Catálogo → fonte prevista** (o teu pedido: "oferecer o banco de links para o agente DSN imagem"): autoriza a sombra na Fase 1?
4. **Gate mídia 3 vias como lei** (Título VII) + integração dos 90 SELECTED_HIGH após tribunal verde?
5. **Calibração do gate de LUGAR** (pertinência temática para lugar/conceito) — decide com o CM?
6. **F3 Scout + F4 aprovação anual** entram no cronograma do Título VII (08-10/09 e 25/09, do sprint Vision)?

**Refs de apoio (para o ZM redigir o Título VII e o DS-Miguel incorporar):** `forum_sprint_v41_vision_zm_20260831.md` (sprint inteiro) · `relatorio_banco_ouro_dia_20260901.md` · `plano_trabalho_contrato_v3_lancamento_v42_20260901.md` (DSC-016 §1.4/§2/§3) · `forum_mutirao_qwen_banco_midia_v4_20260809.md` (90 SELECTED_HIGH) · `BANCO_DE_LINKS_MIDIA_CANONICO.md` · `ideias/2026-08-31_autocura_3_problemas_ideia003.md` (P3) · `ideias/2026-09-01_contrato_v3_constituicao.md` (006 §5) · `memoria_capas_v41_pipeline_deepseek_20260829.md`.

— DS Nuvem Ideias (DS-N Ideias) · 20260901 23:19 BRT
