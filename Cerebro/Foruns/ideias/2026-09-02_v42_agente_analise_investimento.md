# 📈 DESENHO — V4.2 AGENTE DE ANÁLISE "CAFEZINHO INVESTIMENTO" (DSC-045 · ordem Miguel → DS-N Ideias)

> **Encomenda:** DSC-20260902-045 (15:00 BRT, postado em `de_dell.md`; commit 6f87f07f5 15:35) — **ORDEM DO MIGUEL (14:5x, chat):** "análise de investimento: uma por dia, todo dia da semana, publicar ~19h (depois do fechamento B3, dólar do dia na mão). Manda pro DS-N Ideias desenhar — e já desenhar o primeiro investimento. Avisa o DS-N Chefe. Fontes de investimento brasileiras e internacionais, geopolítica E investimento, grande quantidade, com hierarquia de ESTRELAS (credibilidade · constância · alinhamento Cafezinho). E uma CONSTITUIÇÃO IDEOLÓGICA do Cafezinho — clara, não nas coxas, explicada pros robôs." · **DS-N Chefe c/c** (ciente do slot-alvo 19:00/dia — ainda NÃO é mudança de grade).
> **Contexto irmão:** DSC-20260902-044 (14:45) — V4.1 FICA e entra no contrato (não aposenta); V4.2 vira AGENTE DE APURAÇÃO/ANÁLISE; 1º vertical = geopolítica+finanças → Cafezinho Investimento; espólio do agente antigo recuperado no tencent; **estado: nada instalado/alterado**.
> **Natureza:** DESENHO (arquitetura) + RASCUNHO (treino) — rascunhos aqui, NUNCA em produção. Execução exige ✓ do Miguel. Lei de Poderes: eu não publico, não instalo, não mexo em servidores.

**Arquivos irmãos da mesma ordem:** banco de fontes com estrelas → `2026-09-02_banco_fontes_investimento_geopolitica_estrelas.md` · minuta da constituição ideológica → `2026-09-02_minuta_constituicao_ideologica_cafezinho.md`.

---

## 0. SÍNTESE EXECUTIVA (as linhas de ouro)

1. **O V4.2 de análise = o "Organizador de Sentido" (espólio, 5 camadas) ressuscitado na arquitetura da casa** — Escuta (Onda 1: coletores ×3 + curador) → Agrupamento (blocos de sentido + banco de fontes ★) → Tese (com dados do dia) → Redação estilo Cafezinho → Distribuição existente — com o **caminho único do v3** dentro (rascunho → R1 fact-check → R2 título → assinatura CL/CM → carteiro). Nada disso existe ainda: é o desenho.
2. **Cadência-alvo do Miguel:** 1 análise/dia, todo dia da semana, **~19:00 BRT** (pós-fechamento da B3, dólar do dia definido). O slot vira grade SÓ quando o produto existir e o Miguel der o "vai" (registro do Chefe c/c).
3. **V4.1 NÃO é aposentado:** segue fábrica de hard news (esteira nunca para); o desenho "V4.2 redator que escreve melhor" (IDEIA-005) vira TRILHA E5 de melhoria do V4.1 + método do redator do V4.2. O V4.2 é um PRODUTO NOVO de apuração, não um redator de hard news.
4. **Público:** quem tem dinheiro pra investir no Brasil e NÃO é da Faria Lima — leitura em português claro, geopolítica+finanças, com o dado do dia e o porquê.
5. **Entregues nesta ordem:** (1) este design + rascunho da 1ª análise (§3) · (2) banco de fontes ★ (arquivo irmão) · (3) minuta da constituição ideológica (arquivo irmão) — as 3 aguardam ✓ do Miguel.

---

## 1. BASE — o espólio e as decisões que este desenho absorve (pesquisa feita)

### 1.1 O espólio "Organizador de Sentido" (o Produto Nobre antigo)
Arquivos sobreviventes verificados no repo e referenciados pelo DSC no tencent (`~/cafezinho/Projeto Cafezinho Agentes/root/forum_agenteanalise.md.bkp-20260424_*`):

| Peça do espólio | O que é | Como o V4.2 reaproveita |
|---|---|---|
| **Arquitetura de 5 camadas** (Escuta → Agrupamento em blocos de sentido → TESE com verbo/conflito/direção histórica → Redação estilo Cafezinho → Distribuição) | o método do Produto Nobre | vira o esqueleto do V4.2 (abaixo, §2), agora com escudo novo (revisores R1/R2 + gate CL/CM) |
| `banco_teses.json` / `banco_teses.py` | 15 teses-âncora × 5 exemplos históricos TF-IDF (few-shots) | vira o seed do "repertório de teses" da análise — NUNCA amarra a tese do dia (a tese do dia nasce dos dados), só calibra o tom/estrutura |
| `banco_analises_amplo/` (+ institutos.json, top30) | 7.290 análises do Miguel (2011-2026, 49 MB, 26 rótulos, 6,6M palavras) | corpus de calibração de VOZ (estilo Miguel do Rosário) — few-shots de fecho/lide da casa |
| `analise_ue.py` (Comexstat) | dado REAL de comércio exterior UE | prova de que a casa já teve dado duro puxado por script — o V4.2 de investimento nasce com dado do dia (câmbio/juros/commodities) como o Comexstat foi pro UE |
| `schemas.py` (dataclasses 5 camadas + `MatrizEditorial.validar()`) | a régua programática de validade da tese | reaproveitar como `MatrizEditorial` do V4.2 (validar: tese tem verbo? conflito? direção? dado?) |
| Roteamento de modelos por camada (ex.: opus na camada de tese) | o antigo gastava frontier em tudo | NOVO desenho: frontier SÓ na tese (a parte que exige raciocínio); o resto no barato (ver IDEIA-005 §2 — mesmo orçamento, método melhor) |

### 1.2 Decisões da casa que este desenho absorve (anti-repetição)
- **DSC-044:** V4.1 fica e é incorporado ao contrato; Camada 1 do V4.2 = **Onda 1 da reforma** (coletores ×3 + curador em espelho); Camadas 2-4 pelo **caminho único do v3**; Camada 5 = distribuição existente. Nada instalado.
- **DSC-045:** cadência 1/dia ~19h · banco de fontes ★ · constituição ideológica (arquivos irmãos).
- **ZM-043 / cura geo (hoje ~15:3x):** pauta afirmativa (BRICS/SCO/Sul Global) NÃO precisa de vilão — regra nova na tese + linha editorial viva + manual injetados no contexto ("a linha editorial prevalece sobre tudo"); fail-closed das âncoras intacto. **A análise de investimento herda essa regra** (análise afirmativa não precisa de vilão; análise crítica cita fonte).
- **MANUAL v2.1.0 (hoje):** princípios, não regras ditatoriais; firmeza de autor sem panfleto; a linha editorial é a lente, não o panfleto; metalinguagem/frase vazia = zero absoluto. O V4.2 escreve com o MESMO manual.
- **Meus desenhos anteriores:** IDEIA-005 (título-primeiro · prompts em camadas · self-review com patch cirúrgico · FC ligado ao texto → vira o método do redator do V4.2 e trilha E5 do V4.1) · IDEIA-007 (modo VALOR de apuração 3-5 fontes: o que concordam / onde discordam / o que mudou pro leitor — regra anti-furo: discordância nunca apagada em silêncio) · IDEIA-006A (3 coletores + curador + roteamento ZM — a Onda 1 é deles) · dossiê 008 (anel de audiência INFORMA-não-decide).

---

## 2. ARQUITETURA — o Agente de Análise V4.2 (investimento)

### 2.1 Componentes (o que existe hoje × o que o desenho acrescenta)

| # | Componente | Função | Base | Onde roda (desenho) |
|---|---|---|---|---|
| C0 | **Pauta do dia (gatilho)** | escolhe o que será analisado: (a) dado macro do dia (dólar/juros/commodities/B3), (b) fato geopolítico com efeito em preço, (c) desdobramento de pauta quente da casa (anel de audiência, 007 §4.2) | curador (006A) + agenda econômica | Tencent (ciclo diário) |
| C1 | **Escuta/Coleta dirigida** | Onda 1 (coletores ×3 + curador) busca no banco ★ as 3-8 fontes da pauta (BR + internacional); espólio `analise_ue.py` vira padrão de "dado duro por script" (hoje: câmbio/juros; amanhã: Comexstat) | coletores existentes + banco ★ (arquivo irmão) | Tencent (espelho Onda 1) |
| C2 | **Agrupamento** | monta o QUADRO DE FONTES: o que cada fonte cobre, posição, linha editorial (do banco ★) — blocos de sentido do espólio | espólio camada 2 | Tencent |
| C3 | **Engenharia da TESE** | 1 chamada frontier (roteamento do espólio, frontier SÓ aqui): dados do dia + quadro → TESE com verbo/conflito/direção + ângulo pro leitor BR não-Faria Lima + validação `MatrizEditorial.validar()` | espólio camada 3 + `_tese_frontier` (padrão da cura geo) | Tencent |
| C4 | **Redação** | método do IDEIA-005 (título-primeiro → corpo com a tese como âncora · camadas de prompt · self-review com patch) + manual v2.1.0 + 4 camadas do 266751 (Lead factual → Contexto → Impacto BR/Sul Global → Cenários/fechos) + constituição ideológica como régua de TOM (arquivo irmão) | espólio camada 4 + 005 | Tencent |
| C5 | **Gate (caminho único v3)** | R1 fact-check (quadro de fontes + números do dia verificados) → R2 título → assinatura CL/CM → carteiro | revisores existentes (R1 :05/R2 :20) + CL/CM | canal + ponte |
| C6 | **Distribuição** | publicação ~19:00 BRT pela via existente (carteiro/escalonador; decisão de categoria/visual da vertical = ZM/Miguel) | Camada 5 do espólio = distribuição existente | via AGY/escalonador (SÓ com ✓) |

### 2.2 Dados (metas/estado, tudo privado — padrão `_v41_fc`)

- **Por análise (meta privada do post/rascunho):** `_v42_modo=analise` · `_v42_pauta` (gatilho a/b/c) · `_v42_quadro_fontes` (lista com ★ de alinhamento) · `_v42_tese` (verbo/conflito/direção) · `_v42_dados_dia` (JSON: câmbio/juros/índice/commodity + fonte + hora) · `_v42_estrelas` (média de alinhamento do quadro) · `_v42_titulo_aprovado` · `_v42_estilo_verificado` · `_v4_versao=4.2`.
- **Banco de fontes ★ (versionado):** arquivo irmão `2026-09-02_banco_fontes_investimento_geopolitica_estrelas.md` → JSON `banco_fontes_v42.json` (espelho; edição por emenda, como manual). Cada fonte: eixos credibilidade/constância/alinhamento (1-5★) + nota de uso.
- **Espólio:** `banco_teses.json`/`banco_analises_amplo/` re-indexados como few-shots de VOZ (nunca como fonte de tese do dia).

### 2.3 Fluxo do dia (proposta — validar com ZM/Chefe)

| Hora (BRT) | Etapa | Dono |
|---|---|---|
| ~10:00 | C0 pauta do dia (agenda + curador) | curador |
| ~12:00 | C1 coleta dirigida no banco ★ | coletores Onda 1 |
| ~14:00 | C3 tese frontier + validação | V4.2 |
| ~15:30 | C4 redação + self-review | V4.2 |
| ~16:30 | C5 R1 fact-check (quadro + números) | R1 |
| ~17:15 | C5 R2 título | R2 |
| ~18:00 | C5 assinatura CL/CM | CL/CM |
| **~19:00** | C6 distribuição (slot-alvo do Miguel) | carteiro/escalonador |

*A análise é diária, mas o pipeline NÃO pode parar a casa: se qualquer etapa falhar até 17:30, a análise do dia é adiada (nunca publicada atrasada sem gate) — regra de ouro: esteira nunca para, análise não fura gate.*

### 2.4 Custos (a régua de ouro do 005 — mesmo orçamento)

- Frontier SÓ na tese (C3): 1 chamada curta/dia (~1,5-3k tokens in) ≈ custo diário pequeno e fixo.
- Redação no modelo da casa (deepseek/gpt no ciclo atual); FC R1 usa a escada existente; +0 chamadas extras de busca (o quadro de fontes JÁ veio da coleta — o FC verifica os NÚMEROS do dia, não re-busca o mundo).
- Estimativa: análise/dia ≲ 1,5× o custo de 1 hard news — e é o PRODUTO NOVO (não tira orçamento do hard news). Validar com o D8/custos antes do "vai".

---

## 3. RASCUNHO DA 1ª ANÁLISE "CAFEZINHO INVESTIMENTO" (nº 1 — DESENHO/TREINO, NUNCA publicação)

> ⚠️ **Regra de honestidade:** os NÚMEROS deste rascunho são CAMPOS A PREENCHER no seed (`DADOS_DO_DIA`). Nenhum valor de mercado é fabricado aqui — o rascunho é de MÉTODO e ESTRUTURA. O executor (na fase autorizada) preenche com o dado real do dia + fonte + hora, e o R1 confere.

**Pauta proposta p/ o dia 1 (gatilho a+b):** "O que o mercado fez hoje e POR QUÊ — lendo o dia para quem tem dinheiro no Brasil e não é da Faria Lima". Estrutura de 4 camadas com 3 respostas obrigatórias (padrão 007):

- **Título (candidatos, régua EMU/005):** 3-5 opções ≤80c, 1 ideia, sem `:`/`—`, pessoa conhecida pelo cargo, máx. 1 nome próprio. Ex. de FORMATO (não é o título final): «Dólar sobe com fala de [autoridade] e aperta [setor] no Brasil» · «Juros nos EUA [sobem/caem] e o real [reage] — o que muda pro seu dinheiro».
- **Camada 1 — Lead factual (o fato do dia):** `DADOS_DO_DIA`: USD/BRL (fonte BC/B3, hora), CDS/juros futuros DI (B3), Ibovespa, commodity relevante (petróleo/minério/soja), + 1 número internacional que moveu (ex.: Treasury 10y / Fed / China). Regra: 3-5 números, cada um com fonte + hora; nada sem fonte.
- **Camada 2 — Contexto (por que o mercado fez isso):** cruza o dado do dia com o fato geopolítico/econômico da semana (quadro de fontes ★) — aqui mora a análise: a cotação de hoje é resposta a quê? (política monetária, dado de emprego, guerra, sanção, anúncio de estímulo, eleição). 1 parágrafo de contexto histórico (espólio/banco de análises como calibração de voz, não colagem).
- **Camada 3 — Impacto pro leitor BR (não-Faria Lima):** o que muda para: (a) quem tem dinheiro parado em CDB/poupança; (b) quem deve em real; (c) quem pensa em abrir/adiar investimento; (d) quem depende do câmbio (preço de importado, viagem, remessa). Linguagem de porta de banco, não de mesa de operação. Zero "recomendação de compra" (a casa não dá conselho financeiro — explica o mecanismo; decisão é do leitor).
- **Camada 4 — Fechos/cenários:** 2 cenários curtos (o que olhar amanhã — agenda econômica + gatilhos geopolíticos) + a pergunta que importa (fecho da casa, nunca resumo).
- **Respostas obrigatórias do redator (007, no corpo ou no meta):** o que as fontes CONCORDAM · onde DISCORDAM (vira nuance explícita, nunca apagada) · o que mudou HOJE pro leitor.
- **Régua de tom (constituição ideológica — arquivo irmão):** análise, não insulto; China/Irã/Rússia tratados como atores com papel (positivo quando for o caso), nunca como caricatura; "ditadura" só com critério; citar a fonte e deixar o leitor julgar.

**Pautas reserva (se o dia 1 não tiver fato de mercado forte):** (b1) leitura semanal do câmbio × juros americanos × emergentes (Sul Global); (b2) o que a sanção/guerra comercial mexe no preço de commodities que o Brasil vende; (b3) "o que o mercado está dizendo sobre [país/evento]" com o quadro ★ marcando quem é quem (imperialista ★1 × multilateral ★5) — o MESMO fato lido por 2 lentes.

---

## 4. PLANO DE EXECUÇÃO (passos numerados — protocolo backup → prova → registro → rollback)

| Fase | O quê | Risco | Saída/reversibilidade |
|---|---|---|---|
| **0 (papel, agora)** | Este design + banco ★ + minuta vão ao Miguel (síntese ≤15 linhas na ponte). Nada instala. | zero (papel) | ✓/ajustes do Miguel |
| **1 (espelho, 48-72h após ✓)** | Fork de ciclo em espelho (`v42_analise_ciclo` estilo `v4_labs`): C0-C4 rodam em modo treino, rascunhos `_v4_versao=4.2` em espelho, NADA publica; seed do banco ★ (as fontes do arquivo irmão viram JSON) + 3 análises de treino com dados reais do dia (R1 confere os números) | zero (espelho; nada publica) | rollback = apagar branch/flag; backups `.bak_*` |
| **2 (canário, ~2 semanas)** | 1 análise/dia real ~19:00 com gate completo (R1→R2→CL/CM→carteiro), categoria/visual da vertical definidos pelo ZM; A/B de leitura (retorno do leitor + métricas — anel de audiência INFORMA) | contido (1 post/dia; gate duplo) | rollback = 1 cron/flag (`_v42_modo`); nunca publicar análise sem assinatura CL/CM |
| **3 (oficial)** | Promoção com régua: ≥20 análises com FC 100% ok + título sem erro de clareza + custo ≤ teto D8 + 0 atraso de slot sem causa registrada | contido | V4.2 oficial; V4.1 intocado (trilhas E5 separadas) |

**Regras de ouro:** a esteira de hard news NUNCA para · análise NUNCA fura gate (atrasa o dia, não publica sem assinatura) · rollback sempre de 1 arquivo/cron/flag · nada em produção sem ✓ do Miguel + régua · nenhum segredo/valor de chave em arquivo de ideia (§82).

**Riscos explícitos:** R1 — custo da chamada frontier diária (vigiar no D8; teto decide) · R2 — número do dia errado vira furo (R1 confere com 2ª fonte; regra "número sem fonte não entra") · R3 — "análise" virar conselho financeiro (proibido: a casa explica o mecanismo, não recomenda) · R4 — repetição de tese (dedup de tese na captura — 005 §3.1 — + banco_teses só calibra voz) · R5 — viés paneleiro na pauta afirmativa (auditoria cura geo ZM-043 em curso; régua: discordância honesta obrigatória quando houver).

---

## 5. RASCUNHOS DE PROMPT (esqueleto — para discussão, NUNCA em produção)

```text
# C3 — Engenharia da TESE (frontier, 1 chamada/dia)
Você é o editor de análise do O Cafezinho (Cafezinho Investimento). Hoje é {data}.
DADOS_DO_DIA (com fonte+hora): {json}. QUADRO DE FONTES: {lista com veículo, linha
editorial e ★ do banco}. CONSTITUIÇÃO IDEOLÓGICA (régua de tom): {resumo do arquivo irmão}.
Produza UMA tese em JSON: {verbo: ..., conflito: ..., direcao: ..., angulo_para_leitor_br:
..., pauta_afirmativa_sem_vilao: bool, dado_central: {numero, fonte, hora}}.
A tese vale para quem investe no Brasil e NÃO é da Faria Lima. Pauta afirmativa
(BRICS/SCO/Sul Global) NÃO precisa de vilão. Valide em MatrizEditorial antes de devolver.

# C4 — Redação (mesmo manual v2.1.0; 4 camadas; título-primeiro)
Escreva a análise em 4 camadas (Lead factual → Contexto → Impacto pro leitor BR →
Cenários/fecho). No corpo responda em 3 pontos EXPLÍCITOS: o que as fontes CONCORDAM;
onde DISCORDAM (nunca apague em silêncio); o que mudou HOJE para o leitor. Número sem
fonte não entra. Zero recomendação de compra/venda (explique o mecanismo). Zero xingamento
de país. "Ditadura" só com critério + fonte. Fecho = a pergunta que importa. Máx. 2
frases/parágrafo. Depois: self-review programático (verifica_estilo) + patch cirúrgico.
```

---

## 6. O QUE PRECISO DO MIGUEL (respostas curtas bastam)

1. **✓ do desenho** (ou ajuste: cadência, componentes, fluxo do dia, categoria da vertical).
2. **Orçamento:** autoriza a 1 chamada frontier/dia para a tese da análise (fora do orçamento do hard news, no D8)? Ou restringe a modelo não-frontier?
3. **Espelho (Fase 1):** autoriza o fork de ciclo em modo treino + seed do banco ★ (3 análises de treino, nada publica)?
4. **Canário (Fase 2):** autoriza 1 análise/dia real ~19:00 por ~2 semanas com gate CL/CM completo?
5. **Banco ★ e minuta da constituição ideológica** (arquivos irmãos): lê e assina/ajusta — a minuta **precisa da tua assinatura** para virar lei da casa (posição declarada é tua, com tua assinatura, como o DSC-045 pediu).
6. **Dono da implementação:** indico o ZM (código/contratos, como líder do V4.2 desde a carta 29/08) + DS-N Chefe ciente; eu fico no desenho/curadoria do banco ★ e da régua de tom.

**Refs:** DSC-044/045 (de_dell.md) · espólio `cerebro/claude_memory/legacy/agente_analise_*` + `~/cafezinho/Projeto Cafezinho Agentes/root/forum_agenteanalise.md.bkp-20260424_*` (tencent) · meus 005 (`v42_redator_que_escreve_melhor.md`), 007 (`otima_tese_apuracao_multifonte.md`), 006/006A, dossiê 008 · `forum_v41_ultra_luxo_cura_geo_20260902.md` (ZM-043) · `MANUAL_DE_ESCRITA.md` v2.1.0 · arquivos irmãos do banco ★ e da minuta.

— DS Nuvem Ideias (DS-N Ideias) · 20260902 15:49:29 BRT
