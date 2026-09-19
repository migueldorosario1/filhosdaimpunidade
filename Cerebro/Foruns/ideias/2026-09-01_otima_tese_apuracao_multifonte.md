# ✍️ IDEIA_PRO_DSNUVEM_IDEIAS-007 — A ÓTIMA TESE: apuração multi-fonte + retroalimentação de audiência (as duas raízes JÁ EXISTEM no Cérebro — verifiquei e liguei no desenho)

> **Encomenda:** DSC (Terminal celular do Miguel) · 01/09/2026 ~23:0x BRT · via `ponte_laura_completa/de_ideias.md`. Contexto Miguel↔DSC (~22:5x-23:0x): "não só uma tese — uma ÓTIMA tese, é por aí que a gente constrói". Coletores novos = COMPLEMENTO, não substituição ("não quero quebrar o sistema"). NADA ASSINA sem a palavra dele.
> **Natureza:** DESENHO (arquitetura) + VERIFICAÇÃO de fatos no Cérebro (as 3 dúvidas do DSC). Rascunhos aqui, NUNCA em produção. Execução exige ✓ do Miguel.
> **Refs lidas:** `forum_transicao_v5_eeat_antigravity_20260820.md` (piloto 266751) · `cerebro/acoplamento_performance_audiencia_v5.md` (20/08) · `cerebro/Foruns/PAINEL_PERFORMANCE_V5.md` · `cerebro/Foruns/ponte_laura_completa/esteira/buffer_pautas_agy.json` (PoC 20/08) · `cerebro/Memorias/memoria_failover_nyc_tencent_inventario_20260826.md` (cron agente_performance) · `cerebro/Memorias/memoria_auditoria_custos_telemetria_recuperacao_crons_20260729.md` (auditoria crons) · meus 005 (`2026-09-01_v42_redator_que_escreve_melhor.md`) e 006 (`2026-09-01_contrato_v3_constituicao.md`) · `forum_titulo_kast_investigacao_autoria_20260901.md` (prova 31/08, banco geo cheio de Irã/China) · pontes de_laura/de_dell (nenhuma menção recente ao loop rodando).

---

## 0. SÍNTESE EXECUTIVA (o que verifiquei e o que proponho)

**As duas raízes existem e eu VERIFIQUEI o estado de cada uma:**

1. **Apuração multi-fonte — PILOTADA E PROVADA, mas não é o default.** O default de hoje é MONO-FONTE (coletor round-robin RSS/Brave/Jina → 1 matéria por feed → o redator reescreve 1 matéria = tradução). O piloto do post **266751** (20/08, fórum de transição V5 E-E-A-T) apurou com **5 fontes cruzadas** (Middle East Monitor, Al Jazeera, Asian News Network, IISS, Arab Center Washington) em 4 camadas analíticas e **foi publicado e blindado** (decreto editorial V5 12:35, Painel V5 grade) — a prova de que a casa já fez e funciona.
2. **Retroalimentação de audiência — o protocolo existe, a métrica vive, o LOOP dorme.** `acoplamento_performance_audiencia_v5.md` (20/08) define as 4 métricas + Score de Tração + Loop de Retroalimentação de Pautas (30 min). **A métrica está viva** (`agente_performance.py` roda no NYC no cron `52 * * * *` e alimenta `performance_weights.json` — inventário 26/08). **O LOOP de pauta não roda**: o `buffer_pautas_agy.json` foi PoC ÚNICA (20/08 13:10, ZCode/Kimi K3, fase 0; fases 1-2 prometiam patch no agente_performance.py — sem registro de execução); o `PAINEL_PERFORMANCE_V5.md` nasceu estático ("Apurando..."); e nenhuma ponte menciona o ciclo 30 min rodando desde as reorganizações (era LAURA-AGY no papel). **A raiz (GA4) está viva; a árvore (pauta orientada por sinal) dorme — o V4.2 deve ligá-la.**

**A tese do desenho:** a ÓTIMA tese nasce de (a) **apuração multi-fonte no modo valor** (3-5 fontes, síntese + pontos de discordância + consequência pro leitor) e (b) **retroalimentação de audiência religada** (sinais → tese → coleta orientada → artigo elaborado), com **tese-antes-da-coleta** em 2 modos roteados pelo curador — SEM quebrar nada: modo quente segue mono-fonte rápido; modo valor usa apuração. Custo: a apuração SUBSTITUI 1 web_search no orçamento do 005 (não soma).

---

## 1. VERIFICAÇÃO 1 — como a vertical trabalha HOJE (1 ou N matérias por artigo?)

**Resposta: MONO-FONTE é o default.** Evidências no repo:

- **Coletor é round-robin RSS/Brave/Jina** com fontes Sul Global (Asia Times, Sputnik, SCMP, TRT World — a allowlist geo) — cada item entra por feed separado, sem cruzamento entre feeds no mesmo item.
- **O redator reescreve 1 matéria** (a pauta entra com 1 link-fonte e o briefing pede o artigo sobre ELA) — isso é tradução/reescrita, não apuração. O Kimi notou o sintoma: "duplicatas multi-fonte" (a mesma tese chegando por feeds diferentes em posts separados).
- **Meu 005 §1.4 confirmou o custo disso:** China-IA **4×** (267129/267138/267165 + par 267033×267132), bitcoin **3×**, comício Bangu **3×** — o dedupe L13 existe mas é de PAUTA, não de TESE; e a repetição vem de verticais DIFERENTES (o dedup transversal é do curador do 006A).
- **Exceção que prova a regra:** o piloto 266751 (abaixo) foi o único caso registrado de apuração cruzada em produção.

## 2. VERIFICAÇÃO 2 — a apuração multi-fonte JÁ FOI PILOTADA (266751, 20/08)

`forum_transicao_v5_eeat_antigravity_20260820.md` (o DSC chamou de v4_1; o arquivo é o V5):

- **Post 266751** («Arábia Saudita, Turquia e Paquistão firmam pacto de defesa mútua», categoria 5003 Geopolítica, 66 caracteres de título, capa 266750 ≥1200px) — **status: pending → publicado 20/08 15:06** (Painel V5 grade) com **fontes cruzadas**: Middle East Monitor · Al Jazeera · Asian News Network · IISS · Arab Center Washington.
- **4 camadas analíticas** (modelo E-E-A-T do fórum): Lead Factual → Contexto Histórico → Impacto Sul Global/Brasil → Cenários Futuros — hoje o perfil do portal já exige as 4 camadas (camada 3 = impacto Sul Global; o E6 do 006 sobe essa camada a REGRA DE TESE para IA).
- **Blindagem Google Spam Update:** o modelo V5 foi aprovado como decreto editorial (12:35, LAURA-AGY & Miguel) e o post entrou no painel de monitoramento. É a prova operacional: **apuração multi-fonte funciona, passa nos gates da casa e blindou o portal.**

**Conclusão da verificação:** o DSC acertou — "estuda torná-la DEFAULT do V4.2 (sem quebrar: modo quente segue mono-fonte rápido; modo valor usa apuração)". O desenho abaixo é exatamente isso.

## 3. VERIFICAÇÃO 3 — retroalimentação de audiência: RODANDO ou DORMINDO?

**Protocolo (existe):** `cerebro/acoplamento_performance_audiencia_v5.md` (20/08): 4 métricas (pageviews · tempo de leitura com metas 90s hard-news / 180s análise · scroll depth · recorrência) · **Score de Tração** = V·0.40 + T·0.30 + S·0.20 + C·0.10 · **Loop de Retroalimentação de Pautas** (30 min): top matérias 2h/24h → temas com score ≥75 → pauta de desdobramento com ângulo NOVO (ex.: Ormuz → impacto no comércio marítimo BR).

**Execução (verifiquei nos 4 lugares onde ela viveria):**

| Onde | Estado verificado |
|---|---|
| `agente_performance.py` (NYC) | ✅ **VIVE** — cron `52 * * * *` (auditoria 29/07; inventário 26/08: "NYC 52 * * * * × Tencent 50 5 * * * — frequências DIFERENTES (horária × diária)"; o da Tencent é DUPLICADO/divergente) — alimenta `performance_weights.json` (GA4, janela 14d) |
| `buffer_pautas_agy.json` (esteira) | 🟡 **PoC ÚNICA** — gerado 20/08 13:10:00 por ZCode Miguel/Kimi K3, fase 0; "T e S entram na fase 1 via patch no agente_performance.py; C na fase 2" — **sem registro de execução das fases 1/2** |
| `PAINEL_PERFORMANCE_V5.md` | 🟡 **ESTÁTICO** — data_criação 20/08, matriz com "Apurando..." — nunca virou painel vivo |
| Pontes de_laura/de_dell (pós-reorganizações) | 🔴 **SILÊNCIO** — nenhuma menção ao loop 30 min rodando; a LAURA-AGY (dona do papel) não reporta execução |

**Diagnóstico honesto:** o loop está **DORMINDO como processo, VIVO como métrica**. A casa coleta GA4 (agente_performance), mas ninguém transforma os sinais em pauta de desdobramento. O V4.2 deve LIGAR o anel: **audiência → sinais → tese → coleta orientada → artigo elaborado** — com o cuidado médico do DSC: o loop serve à LINHA EDITORIAL (Sul Global, anti-imperialista), não persegue clique puro — régua do tripé (segurança/estabilidade/qualidade).

---

## 4. ARQUITETURA — a ÓTIMA TESE no V4.2 (sem quebrar o V4.1)

### 4.1 Apuração multi-fonte como DEFAULT em 2 modos (roteados pelo curador)

| Modo | Gatilho (curador roteia) | Fluxo | Custo |
|---|---|---|---|
| **QUENTE** (atual) | frescor ≤24h, fato em desenvolvimento, velocidade manda | coleta 1 fonte → redação (mono-fonte rápido, o ciclo de hoje) | igual ao V4.1 |
| **VALOR** (novo) | sinais de audiência (score ≥75) OU tema de espaço vazio (geo/tec) OU pauta de desdobramento | **engenharia da tese → apuração 3-5 fontes → síntese + discordâncias + consequência → artigo elaborado** (4 camadas do 266751) | a apuração SUBSTITUI 1 web_search do FC (mesmo orçamento do 005); +1 chamada de coleta de fontes (~500 tokens) |

**Como o redator apura (briefing da camada 4 do 005, modo valor):** recebe o fato central + **quadro de fontes** (a 1ª descoberta pelo coletor + 2-4 da allowlist por entidade — o mapa de fontes canônicas P4 do caçada 13) e responde 3 perguntas no corpo: (1) o que as fontes CONCORDAM (o fato sólido); (2) onde DISCORDAM (a dúvida honesta — vira nuance, não furo); (3) o que isso MUDOU para o leitor agora (consequência material — lição do Tribunal). **Regra anti-furo:** discordância entre fontes nunca é apagada em silêncio — vira linha explícita ou o FC reprova (P5 do 005 já liga o FC ao texto).

### 4.2 Retroalimentação religada (o anel completo)

1. **Sinais:** o `agente_performance.py` (já vivo no NYC) continua medindo; **corrigir o duplicado da Tencent** (`50 5 * * *`) e definir DONO ÚNICO do cron (NYC) — pendência já anotada no inventário 26/08.
2. **Tese orientada:** a cada 30 min, o curador (006A) consulta o top de tração (score ≥75, janelas 2h/24h) e gera **pauta de desdobramento com ângulo NOVO** (a mecânica do acoplamento v5, que hoje dorme) — o ângulo respeita a linha editorial (Sul Global) e a régua do tripé.
3. **Coleta orientada:** a pauta de desdobramento entra no coletor da vertical como alvo (não como mais um item do round-robin) — modo valor (§4.1).
4. **Artigo elaborado:** V4.2 escreve com apuração; a audiência mede o resultado; o anel fecha.
5. **Fecho do anel no relatório:** métrica diária de funil (colhidas → priorizadas → rascunhos → publicadas) ganha a coluna `fonte_do_sinal: coletor|curador|retroalimentação` — dono: eu (já sou dono da métrica no 006 §6.2).

### 4.3 Tese-antes-da-coleta (inversão do funil que o Miguel propôs)

- **(a) pauta quente:** coleta → redação (atual, velocidade) — inalterado.
- **(b) pauta de valor:** **sinais de audiência → engenharia da tese → coleta ORIENTADA pela tese → artigo elaborado.** A tese deixa de ser gerada no briefing (depois da coleta) e passa a ser gerada ANTES da coleta, como alvo. O curador roteia entre os modos (meta `modo: quente|valor` na saída do curador — rascunho no 006A).

### 4.4 Caçador de fontes (papel, não cargo novo)

O coletor (rotativo) ganha a tarefa de **expandir/rodar a allowlist e alimentar o banco de fontes canônicas (P4)**: toda fonte nova validada (2+ usos com FC ok) sobe ao mapa `fonte_prevista` por entidade — dá variabilidade e frescor de fonte sem cargo novo (1 linha no prompt do coletor; o mapa já existe como esqueleto do caçada 13).

---

## 5. PLANO DE EXECUÇÃO (passos numerados, riscos, reversibilidade)

| Fase | O quê | Risco | Saída |
|---|---|---|---|
| **0 (papel)** | Este desenho entra como emenda ao dossiê da noite (008b) → ZM redige; Miguel lapida | zero | insumo da Constituição/V4.2 |
| **1 (espelho, 48-72h)** | Modo valor em espelho: 5 posts/dia com apuração multi-fonte, rascunhos `_v42_apuracao=multifonte`, NADA publica; relatório de custo vs mono-fonte | zero (espelho) | quadro de fontes provado no orçamento |
| **2 (canário)** | Retroalimentação religada em canário: o curador emite 2 pautas de desdobramento/dia (score ≥75) e a geo/tec escreve 1 delas; A/B no rito do comparativo | contido (canário) | anel prova na vertical |
| **3 (promoção)** | Modo valor assume com régua: ≥80% das teses de valor com discordância honesta citada + FC 100% + custo ≤5-8% acima; retroalimentação ligada por padrão | contido | rollback = flag `_v42_apuracao` + comentar cron |
| **4 (oficial)** | V4.2 com apuração + anel religado; mono-fonte vira o modo rápido do modo quente | — | oficial |

**Regras de ouro:** a esteira nunca para · o modo quente NUNCA é tocado · rollback de 1 arquivo/cron · nada em produção sem a régua + ✓ do Miguel.

### Riscos e reversibilidade (protocolo: backup → prova → registro → rollback escrito)
- **R1 — Apuração infla o custo:** a regra é SUBSTITUIR 1 web_search, nunca somar; se o custo por post subir >8%, o modo valor volta ao espelho (flag `_v42_apuracao`).
- **R2 — Discordância de fontes vira furo:** regra explícita (linha de discordância ou FC reprova) + R1 do DSN Revisor confere o quadro de fontes (já é o ofício dele).
- **R3 — Retroalimentação vira caça ao clique:** a régua do tripé e a linha editorial (Sul Global) filtram o ângulo ANTES da coleta; score ≥75 é condição necessária, não suficiente (o curador julga).
- **R4 — Cron duplicado da Tencent (agente_performance):** antes de ligar o anel, definir dono único (NYC) e comentar o da Tencent com backup — pendência do inventário 26/08, não minha para executar (ZM).

---

## 6. O QUE PRECISO DO MIGUEL (respostas curtas bastam)

1. **✓ do desenho** — apuração multi-fonte como DEFAULT do V4.2 em 2 modos (quente mono-fonte · valor com apuração 3-5 fontes), roteados pelo curador?
2. **Retroalimentação religada** — autoriza o canário (2 pautas de desdobramento/dia na geo/tec com score ≥75)? (a raiz GA4 já vive no NYC; só o LOOP dorme)
3. **Tese-antes-da-coleta** — endossa a inversão do funil no modo valor (sinais → tese → coleta orientada)?
4. **Caçador de fontes** — confirma como PAPEL do coletor (rotativo), não cargo novo, alimentando o mapa P4?
5. **Cron do agente_performance** — alinho com o ZM a unificação (NYC dono único; Tencent comentado com backup)?

---

**Rascunho (esqueleto — para discussão, NUNCA em produção):**

```text
# Camada 4 (pauta) — modo VALOR (apuração multi-fonte)
Você é o redator-editor do O Cafezinho. FATO CENTRAL: {tese + ângulo}.
QUADRO DE FONTES (3-5, coletadas por entidade): {lista com link, veículo, linha editorial}.
Escreva o artigo em 4 camadas (Lead Factual → Contexto Histórico → Impacto Sul Global/Brasil
→ Cenários Futuros). No corpo, responda em 3 pontos EXPLÍCITOS:
1) O que as fontes CONCORDAM (o fato sólido);
2) Onde DISCORDAM (dúvida honesta — vira nuance, NUNCA apagada em silêncio);
3) O que isso MUDOU para o leitor agora (consequência material — nunca dado frio no lide).
Zero metalinguagem. Fecho = a pergunta que importa. Máx. 2 frases/parágrafo.

# Retroalimentação (curador, a cada 30 min — mecânica do acoplamento v5 religada)
Top matérias 2h/24h → Score de Tração ≥75 → 1 pauta de desdobramento com ângulo NOVO
(respeitando linha editorial Sul Global e o tripé segurança·estabilidade·qualidade)
→ modo VALOR para a vertical dona do tema.
```

**Refs de apoio (para o ZM redigir e o DS-Miguel incorporar):** `forum_transicao_v5_eeat_antigravity_20260820.md` (piloto 266751, 4 camadas) · `cerebro/acoplamento_performance_audiencia_v5.md` (4 métricas + Score + Loop) · `cerebro/Foruns/esteira/buffer_pautas_agy.json` (PoC fase 0) · `cerebro/Memorias/memoria_failover_nyc_tencent_inventario_20260826.md` (cron agente_performance: NYC 52 * * * * × Tencent 50 5 * * *) · meus 005/006/006A · `forum_titulo_kast_investigacao_autoria_20260901.md` (prova 31/08).

— DS Nuvem Ideias (DS-N Ideias) · 20260901 23:18 BRT
