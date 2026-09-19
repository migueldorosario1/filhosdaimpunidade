# ✍️ IDEIA_PRO_DSNUVEM_IDEIAS-005 — V4.2: O REDATOR QUE ESCREVE MELHOR (desenho de arquitetura)

> **Encomenda:** DSC (Terminal celular do Miguel) · 01/09/2026 ~20:2x BRT · via `ponte_laura_completa/de_ideias.md` · **prazo da síntese: 21:45** (alimenta a sessão das 22:00).
> **Ordem do Miguel (conversa ~20:0x):** "não manda estudar em particular isso — manda estudar o V4 e desenhar um V4.2 mais moderno" · o V4.2 tem que **ESCREVER MELHOR** — ser o redator mais talentoso da casa — custando **A MESMA COISA em tokens** que o V4.1.
> **Refs lidas:** `FORUM-V4.md` (→ `forum_transicao_v5_eeat_antigravity_20260820.md`) · `forum_v42_curadoria_imagem_e_arquitetura_20260829.md` (consolidação DS-V42-001) · `carta_para_ds_miguel_liderar_v42_20260829.md` · `plano_trabalho_contrato_v3_lancamento_v42_20260901.md` (§4.A) · `forum_v4_labs_subida_pipeline_llm_tudo_20260822.md` (histórico L1-L19 do v41_ciclo) · `forum_manual_estilo_unificado_20260830.md` (MEU v1.1.0 + INTELIGÊNCIA_TOTAL) · `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md` (EMU-1..5, 8 regras de título, C3) · `forum_titulo_kast_investigacao_autoria_20260901.md` (268457) · `forum_titulo_villatoro_emenda_emu2_20260901.md` (268482) · `forum_frescor_regra_dura_v41_sabatina_lula_jn_20260828.md` (268033, régua frescor) · `forum_auditoria_gasto_openai_v4_superproducao_20260824.md` (funil de custo) · `forum_auditoria_v4_x_v41_o_que_parar_20260826.md` · `v41_vereditos_loops.md` · `CEREBRO_NODE_ARQUITETURA.md` (§Arquitetura de Publicação V4.1) · `cerebro/cerebro_light/CEREBRO_NODE_CATALOGO_MODELOS_LLM.light.md` · `v41_comparativo_loops.md` · de_ideias.md (histórico do ofício).
> **Natureza:** DESENHO (arquitetura) — rascunhos de prompt/código AQUI no arquivo, NUNCA em produção. Execução exige ✓ do Miguel.

---

## 0. SÍNTESE EXECUTIVA (o que é este desenho)

O V4.1 **já escreve bem o corpo** (vereditos 8,0-8,5 × 5,0-6,7 no switch; FC em cascata; tese dinâmica ancorada). Onde ele **perde qualidade é no TÍTULO** (tradução literal, sobrenome solto, 2 nomes próprios, sigla) e na **ESTRUTURA do fecho** (metalinguagem, frase vazia) — e os 2 casos do dia 01/09 (268457 Kast, 268482 Villatoro) provam que o problema é **de método, não de modelo**: o título nasce por compressão da manchete estrangeira NO FIM da redação, e os gates de título são sintáticos (80c, sem `:`) — nenhum lê CLAREZA.

**Tese do desenho:** o V4.2 não é outro modelo nem mais tokens — é **o mesmo orçamento com o título nascendo CERTO antes do corpo, prompts em camadas (não briefing monolítico), 1 par ❌/✅ calibrado por regra de risco, e self-review programático antes de entregar** (verifica_estilo.py v2 automático, que já existe e provou 87 alertas na v1 do cap. 2). Custo total estimado: **igual ou ≤5-8% acima** do V4.1 por post — dentro da faixa pedida.

---

## 1. (a) DIAGNÓSTICO HONESTO — onde o texto do V4.1 perde qualidade

### 1.1 TÍTULO: o ponto nº 1 do Miguel — e é real (2 casos no mesmo dia, 01/09)

| Caso | Título que saiu | O que o leitor não entende | Causa provada |
|---|---|---|---|
| **268457** (geo, 14:31, gpt-5.5, job `1a30c106bd88`) | «Cocaína em transferência expõe falha em **prisão vitrine** de Kast» | "prisão vitrine" = tradução literal de "cárcel vitrina" (jargão chileno); não diz QUEM carregava a cocaína | pauta original em INGLÊS ("Chile fines Chinese mafia inmate…"); redator comprime a manchete estrangeira no fim; `gate_titulo.py` é **sintático** (62c, sem `:`/`—` → passaria); auditor advisor cobre só autor 5786, esteira publica pelo **5470** → passa batido; **`_v41_fc` veio `ok:false`** (claim contradita) e o post subiu mesmo assim — o título herdou a ambiguidade do FC reprovado |
| **268482** (nac, 12:39, job `9b39f2cf2c57`) | «Villatoro defende exceção de Bukele e restringe imagens do Cecot» | Quem é Villatoro? O que é Cecot? 2 assuntos num título | **EMU-1** (sigla não consagrada) e **EMU-2** (pessoa pouco conhecida entra pelo cargo) JÁ EXISTIAM no manual e o auditor deixou passar; "e" concatenando 2 notícias viola a regra 2 |

Correções in place (17:36/17:52, slug preservado): «Ministro de Bukele defende regime de exceção do país» e «Preso é flagrado com cocaína antes de ir para cadeia de segurança máxima de Kast» — **as duas vieram de HUMANO**. O robô não tem cinto de clareza.

**Leitura estrutural:** o corpo do 268457 era bom (factual, fonte chilena). **Só o título degenerou** — porque título é a ÚNICA peça que nasce por compressão de texto estrangeiro no fim do prompt, sem âncora própria e sem auditor de clareza. Este é o defeito nº 1 a desenhar.

### 1.2 ESTRUTURA/FECHO: metalinguagem e frase vazia (EMU-4/5 já são lei — falta enforcement no ciclo)

- `verifica_estilo.py` v2 flagrou **87 alertas** na v1 do cap. 2 do Origens, incluindo **5 frases de metalinguagem** que o Miguel reprovaria — aprovou a v2. **O verificador NÃO roda automático no ciclo** (chamada manual; pendência anotada no fórum do manual).
- Caso 267033 (par V4×V4.1): estrutura "bloco factual seguido de `<strong>O que o projeto prevê</strong>`" — sub-título anúncio = metalinguagem leve. Os intertítulos `<h3>` (regra da casa) às vezes nascem como legenda do próprio texto.
- Fecho "com a pergunta que importa" (pedido do Miguel): **não existe regra no prompt** — os fechos analíticos bons (267132, 267078) saíram por sorte de briefing, não por desenho.

### 1.3 FRESCOR: a régua existe (2 camadas, 28/08) — mas a ESCOLHA da pauta ainda premia o drama

- 268033 (Lula/Record, fato de domingo publicado quinta): a cadeia do atraso foi corrigida (régua 24/48/72h + juiz `pauta_fria`). ✅
- Porém a prova do 31/08 (`dados/v41_ciclo/20260831_2156.json`): o banco geo ESTAVA cheio de Irã/China (hard news de guerra) e a geo escreveu Kast — porque o critério "tese com vilão NOMEADO + consequência material" **favorece crime/escândalo/personagem** e penaliza guerra (antagonista = Estado, impessoal). O boost de temas (Adendo 3, ~19:0x) já ataca isso; **falta a régua de frescor virar critério de ESCOLHA com peso** (ver §3).

### 1.4 ENTRADA: redundância chega ao redator (e custa tokens à toa)

- China-IA **4×** (267129/267138/267165 + par 267033×267132), bitcoin **3×** (267124/267153/267119), comício Bangu **3×** (267227…). O dedupe próprio L13 (24h) existe, mas é **dedupe de pauta, não de TESE** — a mesma pauta com ângulos diferentes continua entrando. O capítulo Coleta do contrato v3 (§1.3) já prevê "dedup de pauta/tese JÁ NA CAPTURA" — **dono deste desenho** (ver §3).

### 1.5 CUSTO (a restrição de ouro — o que NÃO pode subir)

| Item (semana 20-24/08, org "O Cafezinho") | Volume | Custo |
|---|---|---|
| gpt-5.5 (redação + FC web_search) | 364 reqs · 8,8M in · 814k out | US$ ~21/dia no pico (23/08) |
| gpt-4o-mini (coletor/intake) | 1.920 reqs | barato, 24/7 |
| Briefing INTELIGÊNCIA_TOTAL | ~28.074 chars (~7k tokens)/post | ~1 centavo/dia pay-as-you-go |
| Teto proposto (R3, 24/08) | US$ 5/dia | aguarda implementação |

**Consequência de desenho:** self-review em "2ª redação completa" DOBRARIA o custo de redação → **proibido**. O V4.2 só pode gastar ~5-8% a mais (verificação + patch cirúrgico), ou zero quando o verificador programático estiver silencioso (fail-fast).

---

## 2. (b) ARQUITETURA DO V4.2 — mesma faixa de tokens, método melhor

**Princípio:** o V4.2 é o **MESMO ciclo V4.1** (`v41_ciclo.py` → `v42_ciclo.py`, mesma coleta, mesma tese dinâmica, mesma cascata deepseek-v4-pro/gpt-5.5, mesmo FC em 3 provedores, mesmo carimbo `_v4_versao`) — **mudam 5 pontos de MÉTODO dentro da redação**. Nada de trocar de motor.

### 2.1 P1 — TÍTULO-PRIMEIRO (mata a compressão degenerada na raiz)

Hoje: briefing → corpo → título por compressão (fim). **V4.2: título ANTES do corpo, e o corpo escreve PARA o título.**

1. **Etapa A (título):** 1 chamada barata (~600-900 tokens in) gera **3-5 candidatos** já na régua: ≤80c · uma ideia · sem `:`/`—`/`...` · sentence case · verbo concreto · **EMU-1** (sigla só consagrada) · **EMU-2** (cargo p/ pessoa pouco conhecida) · máx. 1 nome próprio (Emenda 9) · zero jargão/tradução literal.
2. **Etapa A2 (auditor de clareza):** o próprio `_title()` (sintático) + **`_title_clareza()` novo** (LLM curta, ~300 tokens): "o leitor brasileiro médio entende este título em 2 segundos? há jargão/tradução literal/sobrenome solto/sigla não consagrada?" → escolhe 1 candidato **fail-closed** (se todos reprovarem, refaz 1×; se refazer falhar, não escreve — rascunho marcado `titulo_sem_clareza`).
3. **Etapa B (corpo):** o briefing recebe o **título aprovado como âncora de tese** ("a tese é o título expandido") — o redator escreve o lide provando o título, nunca o contradizendo. O título NÃO pode mais degenerar no fim porque ele já nasceu validado.
4. **Custo:** +1 chamada curta (~1,2k tokens) por post ≈ **+1-2%** — dentro da faixa. Elimina a classe inteira dos casos 268457/268482/268305.

### 2.2 P2 — PROMPTS EM CAMADAS (não briefing monolítico)

O V4.1 injeta 28.074 chars fixos (núcleo + manual completo + diretriz completa). Funciona, mas **metade do sinal é ruído para aquele post** (o redator de geo não precisa do perfil B3 do Origens). V4.2 monta o briefing **por camadas selecionadas**:

| Camada | Conteúdo | Sempre? | ~tokens |
|---|---|---|---|
| 0 | Papel: redator-editor do O Cafezinho, voz da casa (1 parágrafo) | sim | ~150 |
| 1 | `estilo_nucleo_fixo.md` (10 regras telegráficas E14/15/16 + Núcleo A) | sim | ~700 |
| 2 | EMU-1..5 + emendas da diretriz **da vertical** (não todas) | sim | ~800 |
| 3 | Perfil B1 do portal (8 regras de título + 4 camadas E-E-A-T) | sim | ~600 |
| 4 | Pauta: tese dinâmica aprovada + âncoras + CONTEXTO TEMPORAL (L19) + frescor + fontes + FC | sim | ~1.500 |
| 5 | **Exemplos calibrados** (1 par ❌/✅ por regra de risco) — §2.3 | sim | ~800 |
| 6 | Específico da vertical (contrato `v4_*_v1.md`) | sim | ~300 |

Total **≤5k tokens de briefing** (MENOS que os 7k de hoje) — sobra orçamento para o self-review §2.4 **sem estourar a faixa**. As camadas 2/3 vivem em arquivos versionados (mesmo fluxo de espelho GitHub+NYC do manual) — emenda nova = 1 arquivo, próximo ciclo lê (cadência de atualização já testada 2× hoje).

### 2.3 P3 — EXEMPLOS CALIBRADOS (o que mais ensina "escrever melhor" por token)

Regra editorial da casa: **1 par ❌/✅ por regra de risco, com caso real da casa** (não inventado):

- **Título:** ❌ «Villatoro defende exceção de Bukele e restringe imagens do Cecot» → ✅ «Ministro de Bukele defende regime de exceção do país» (caso 268482, EMU-2).
- **Título 2:** ❌ «Cocaína em transferência expõe falha em prisão vitrine de Kast» → ✅ «Preso é flagrado com cocaína antes de ir para cadeia de segurança máxima de Kast» (caso 268457).
- **Lide:** ❌ abrir pelo dado frio → ✅ abrir pela consequência material ("seu imposto vai mudar" — lição do Tribunal).
- **Metalinguagem:** ❌ "A metáfora é reveladora" / "O que o projeto prevê" → ✅ o texto demonstra (EMU-4).
- **Fecho:** ❌ resumo do que foi dito → ✅ a pergunta que importa (deixar no ar a consequência).
- **Frescor na escolha:** pauta de guerra com antagonista-Estado PODE ter tese (Adendo 3 do Kast).

Custo: fixo no prompt (≈800 tokens), **não cresce por post**. É o melhor custo-benefício de qualidade disponível.

### 2.4 P4 — SELF-REVIEW ANTES DE ENTREGAR (verificação + patch, não 2ª redação)

1. **Verificador programático pós-escrita:** `verifica_estilo.py` v2 (JÁ EXISTE, provado: 87 alertas na v1 do cap. 2) roda **automático** no fim da redação — repetição (regex A2), metalinguagem (E15), frase vazia (E15b), spoiler (E14), dois-pontos/travessão (A4), ≤2 frases/parágrafo (P2), título (8 regras).
2. **Se silencioso → entrega** (custo zero adicional).
3. **Se acusar → passada de patch** (~400-600 tokens): o redator recebe SÓ os alertas com localização e corrige cirurgicamente (não reescreve o texto). 
4. **Se reincidir nos MESMOS alertas → rejeita** (rascunho marcado `estilo_falhou`, vai para revisão humana — fail-closed, nunca publica com marca).
5. Custo real: **0% na maioria dos posts, ≤5-8% nos que precisam de patch** — a média fica dentro da faixa do V4.1.

### 2.5 P5 — FC LIGADO AO TEXTO (fecha o buraco do 268457)

- Rascunho com `_v41_fc.ok:false` nasce marcado `fc_reprovado` e o título NÃO pode herdar a ambiguidade: o briefing do título-primeiro recebe a claim reprovada e é **proibido de usar o fato contradito no título/lide** (reescreve ou cai para o próximo candidato). 
- O spot-check do DSN Revisor (plano já existente: "se `_v41_fc` reprovado ou ausente → reprova") entra no gate do rascunho, não só na revisão.

**Arquitetura de dados (deliverable do rascunho):** metas novas no post: `_v42_titulo_aprovado` (título validado), `_v42_titulo_candidatos` (3-5), `_v42_estilo_verificado` (`ok`/`patched`/`falhou`), `_v42_fc_linkado` (`sim`/`nao_aplica`), `_v4_versao=4.2` (espelho). Tudo privado (lista do `cafezinho-rest-meta-privada.php`), como `_v41_fc`.

---

## 3. (c) COLETA/CURADORIA MAIS INTELIGENTE NA ENTRADA (capítulo Coleta do contrato v3)

1. **DEDUP DE TESE NA CAPTURA (não de pauta):** o intake passa a comparar o **núcleo factual** (evento E + data + personagem central) com os últimos 50 do banco; ângulo distinto passa, mas **4× China-IA / 3× bitcoin não chegam ao redator**. Meta: menos repetição na entrada = menos tokens gastos à toa = mesmo orçamento rendendo mais qualidade.
2. **FRESCOR COMO CRITÉRIO DE ESCOLHA COM PESO:** além do teto (24/48/72h), a **seleção** ordena por `frescor × interesse-declarado` (lista viva `temas_prioritarios_geo.txt` já existe; estender para editorial geral, editável sem deploy) — a guerra Irã/China deixa de perder para o drama de personagem (prova 31/08).
3. **FONTE PREVISTA POR ENTIDADE** (P4 do caçada 13, mapa de fontes canônicas): a coluna `fonte prevista` alimenta o briefing do redator (citação esperada e legenda/crédito na ORIGEM — mata o caption "default" do 268511 na causa).
4. **MÉTRICA DIÁRIA DA COLETA** (contrato v3 §1.3, dono DS Nuvem Ideias): colhidas → rascunhos → publicadas; mortas e por quê — entra no relatório do dia. Dá o número para decidir a régua de entrada.

---

## 4. (d) PLANO DE TRANSIÇÃO SUAVE — o V4.1 NUNCA PARA

| Fase | O quê | Risco | Saída |
|---|---|---|---|
| **0 (hoje→22:00)** | Este desenho vira anexo executivo do contrato v3 (§4.A) | zero (papel) | ✓ do Miguel na sessão |
| **1 (espelho, 48-72h)** | Fork `v4_labs_v42/` (ou branch) do `v41_ciclo.py` → `v42_ciclo.py` com P1-P5; rascunhos `_v4_versao=4.2` + cat `no-home` (20699) ou flag `_v4_espelho_v42=1`; cadência baixa (1-2 posts/dia por vertical); custo por post idêntico ao V4.1 | zero (espelho; nada publica) | rascunhos V4.2 legíveis pelos loops |
| **2 (canário)** | 1 vertical canário (sugiro **geo** — é onde nasceu o 268457 e onde o boost de temas já está) em produção paralela; **A/B por pares** no rito do `v41_comparativo_loops` (título/tese/frescor/estrutura/FC); quórum: ≥2 loops + CM/CL | contido (canário) | régua de promoção |
| **3 (promoção)** | V4.2 assume verticais com métrica; V4.1 vira fallback congelado | contido | rollback = cron + meta `_v4_versao` |
| **4 (oficial)** | V4.2 principal; V4.1 desligado com backup documentado | — | V4.2 oficial |

**Régua de promoção (Fase 2→3):** ≥3 vitórias do V4.2 em pares (com ≥2 loops votando) + 0 títulos com erro de clareza na amostra + FC 100% `ok` + `_v42_estilo_verificado` sem `falhou`. **Regra de ouro:** a esteira nunca para; rollback sempre de 1 arquivo/cron; nada em produção sem a régua.

**Pendências que NÃO são minhas mas o desenho depende:** enforcement EMU-2 no v41_ciclo (ZM, já pendente) · auditor advisor estendido p/ autor 5470 (ZM) · verifica_estilo.py automático (ZM, aguarda "vai") · `_v41_fc` lido pelo publicador (Publicador/ZM, já é direção do DSN Revisor).

---

## 5. (e) O QUE PRECISO DO MIGUEL (decisões da sessão das 22:00)

1. **✓ do desenho** (ou ajuste nos eixos: título-primeiro · camadas · exemplos · self-review · FC ligado).
2. **Orçamento do self-review:** autoriza a passada de patch (~5-8% tokens) quando o verificador acusar? (ou restringe a "só verificação programática, sem patch" — perde ~metade do ganho).
3. **Espelho:** autoriza o fork `v4_labs_v42/` no NYC (Fase 1) com cadência 1-2 posts/dia por vertical?
4. **Canário:** concorda com **geo** como 1ª vertical canário + rito A/B por pares (quórum ≥2 loops)?
5. **FC ligado ao título:** rascunho com `_v41_fc ok:false` nasce marcado e o título é proibido de usar o fato contradito — endossa? (já é direção do DSN Revisor).
6. **Lista viva de temas:** autoriza estender `temas_prioritarios_geo.txt` para prioridades editoriais gerais (1 arquivo editável, não toca código)?
7. **DS-Miguel segue líder da implementação** (carta 29/08) — este desenho é o insumo de arquitetura dele; nada executa sem o "vai" dele + o seu.

**Rascunhos (PROMPS em esqueleto, só para discussão — NUNCA em produção):**

```text
# Camada 4 (pauta) — adendo título-primeiro
ETAPA A — TÍTULO (antes do corpo):
Gere 3-5 títulos para a pauta abaixo. Regras OBRIGATÓRIAS:
1) ≤80 caracteres; 2) uma ideia só (nunca "e/mas/enquanto"); 3) sem dois-pontos,
travessão, reticências; 4) sentence case; 5) verbo concreto no presente/passado;
6) sigla só se consagrada (PF, STF, TSE, ONU, UE, EUA, PIB, SUS, INSS, BNDES);
7) pessoa pouco conhecida entra pelo CARGO (nunca sobrenome solto);
8) máx. 1 nome próprio; 9) zero jargão ou tradução literal de outro idioma;
10) o leitor médio entende em 2 segundos.
CONTEXTO TEMPORAL: hoje é {dia}, {data}. FATO CENTRAL: {tese dinâmica + âncoras}.
CLAIM REPROVADA NO FC (não usar no título): {claim}.
Caso a pauta seja de guerra/sanções/disputa entre Estados, o antagonista pode ser
um ESTADO nomeado (ex.: Irã, China, OTAN) — não exige pessoa física.

ETAPA A2 — CLAREZA: para cada candidato, responda JSON:
{entende_em_2s: bool, jargao_ou_traducao_literal: bool, sobrenome_solto: bool,
 sigla_nao_consagrada: bool, nomes_proprios: int}. Se TODOS falharem, refaça 1×.
Fail-closed: se refazer falhar, marque titulo_sem_clareza e NÃO escreva o corpo.

ETAPA B — CORPO: escreva o post provando O TÍTULO APROVADO (é a sua tese).
Lide abre pela consequência material (nunca pelo dado frio). Zero metalinguagem
(nunca anuncie o texto). Fecho = a pergunta que importa (a consequência em aberto),
nunca um resumo. Máx. 2 frases por parágrafo. Intertítulos <h3> que AVANÇAM a tese.
```

```text
# Self-review (pós-escrita, verifica_estilo.py v2 — JÁ EXISTE, tornar automático)
1. rode o verificador programático (regex + heurísticas do manual v1.1.0);
2. silencioso → entrega (custo zero);
3. com alertas → devolva APENAS os trechos acusados + a correção cirúrgica;
4. reincidência nos mesmos alertas → marque estilo_falhou e rejeite o rascunho.
```

---

**Refs de apoio (para o DS-Miguel, líder da implementação):** `forum_v4_labs_subida_pipeline_llm_tudo_20260822.md` (L1-L19: tese dinâmica, FC cascata, sanitizador, juiz inter-vertical, calendário) · `forum_manual_estilo_unificado_20260830.md` (ADENDOS 1-2: INTELIGÊNCIA_TOTAL + verifica_estilo v2) · `forum_titulo_kast_investigacao_autoria_20260901.md` (Adendo 2-3: prova 31/08 + boost de temas + tese de guerra + geo horária) · `forum_auditoria_gasto_openai_v4_superproducao_20260824.md` (funil de custo e teto R3) · `v41_comparativo_loops.md` (rito A/B por pares).

— DS Nuvem Ideias (DS-N Ideias) · 20260901 20:3x BRT
