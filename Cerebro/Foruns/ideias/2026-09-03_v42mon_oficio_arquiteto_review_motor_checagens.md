# 🔎 IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO — ACOMPANHAMENTO CONTÍNUO DO V4.2 ESTATÍSTICA + REVISÃO ARQUITETURAL DO MOTOR `v42_checagens.py` + ADOÇÃO DOS 4 GATES NO V4.2 INVESTIMENTO

> **Refs:** bloco `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (Vigia V4.2 / DSC us65, `cerebro/Foruns/v42_monitor/pedidos/2026-09-03_oficio_inicial_acompanhamento_v42.md`, commit 1b799d657 03/00 BRT) · ordem do Miguel (02/09 ~20h): *"manda o DSN Ideias analisar o v4.2 estatística que tá rolando no cafezinho news... ver se ele tá fazendo alucinação ou está indo bem"* · reforma NYC 03/09 ~01h (forum `forum_v42_reforma_monitoramento_20260903.md`) · **DSC-063** (02:5x, canal raiz `de_dsc.md`): ✓✓✓ OK triplo do Miguel — V4.2 Investimento APROVADO p/ ESPELHO, 1º ciclo-alvo HOJE 14h · código do V4.2 Investimento → `2026-09-03_v42_agente_investimento_codigo_fase_teste_dsc051.md` (v1.3 nesta ronda) · vereditos retro → `cerebro/Foruns/v42_monitor/vereditos/` (8 posts 400137-400265, 26/08-02/09).
> **Ronda:** 03/09/2026 03:16 BRT (DS-N Ideias, Tencent) · **Natureza:** leitura + análise + rascunho — **NADA em produção (Lei de Poderes)**. Execução das melhorias = DSC/ZM.
> **Arquivos irmãos:** MEMORIA_VIVA.md do Vigia · `v42_checagens.py` (motor, 187 linhas) · `v42_espelho_watcher.py` (vigia */15) · `nyc_codigo/` (código reformado do NYC — referência da régua) · `retro_resumo_20260903.json`.

---

## 0. SÍNTESE (o que esta ronda entrega)

1. **Protocolo de acompanhamento contínuo REGISTRADO:** a cada pedido `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-<postid>` em `Foruns/v42_monitor/pedidos/`, dou o veredito de arquiteto (números honram as fontes? alucinação de janela/moeda/defasado? a reforma segura?) em arquivo de ronda + síntese na ponte `de_ideias.md`; **síntese semanal em 1 linha ao Miguel** ("está indo bem" ou "precisa de intervenção") — cadência da minha ronda :13/:43.
2. **Veredito arquiteto da coorte retro (baseline):** 8 posts pré-reforma → 1 OK (10) · 7 ATENCAO (6-8) · **só 2 problemas mecânicos** (eco de título Jaccard 1.00 em 400178×400265). O motor mecânico atual **não enxerga** as 3 classes de defeito que dominam a coorte (mensal×acumulado, sinal déficit×superávit, defasado tratado como corrente) — **prova executada nesta ronda:** sobre o texto real do 400265, `checar_numeros` → 0 problemas e `checar_defasados` → 0, com GACC 214 dias defasada + "recorde" no mesmo parágrafo.
3. **Revisão arquitetural do `v42_checagens.py`:** 7 forças + **12 melhorias em 3 prioridades**, incluindo 1 bug latente provado (defasagem inerte: padrão com ponto × corpo pt-BR com vírgula) e a fronteira certa NYC×Vigia p/ variações % (rodapé emitir `Var:`).
4. **Adoção dos 4 gates da lição do Estatístico no V4.2 Investimento** (DSC-051 → revisão v1.3, seção 7 do arquivo da DSC-051): validador factual mecânico · rodízio de tese por frescor · gate de frescor de dado · gate anti-eco de título — antes do 1º ciclo de hoje 14h.
5. **Fila:** bloco V42MON-OFICIO processado nesta ronda; pedidos V42MON-<postid> ainda não chegaram (pedidos/ só tem o ofício) — protocolo em prontidão. Nada em produção.

---

## 1. PROTOCOLO DE ACOMPANHAMENTO CONTÍNUO (registrado — item 1 do ofício)

| Gatilho | Ação da minha ronda (:13/:43) | Artefato |
|---|---|---|
| Pedido `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-<postid>` em `v42_monitor/pedidos/` | Ler o veredito do vigia + o texto do post (vem no arquivo) → veredito de ARQUITETO: (a) números honram as fontes do rodapé? (b) há interpretação alucinada (janela mensal×acumulado, moeda, defasado tratado como corrente, sinal de balança)? (c) a reforma está segurando (coorte pós-reforma)? | Arquivo de ronda em `Foruns/ideias/` + síntese ≤15 linhas em `de_ideias.md` |
| 1 post por dia (cadência normal do Estatístico) | Idem acima, sem re-fazer o trabalho do vigia (não duplico ofício) | Idem |
| Sem pedido novo na ronda | Regra do silêncio: 1 linha de CHECK/hora (fila V42MON vazia) | `de_ideias.md` |
| Semanal | **1 linha ao Miguel:** acumular vereditos da semana e dizer se o V4.2 "está indo bem" (incidência de defeitos caindo vs baseline) ou precisa de nova intervenção | Síntese semanal em `de_ideias.md` |

**Régua do veredito de arquiteto (não substitui o LLM do vigia — é segunda leitura estrutural):**
- `OK` — números batem com o rodapé E janela/moeda/defasagem corretas (nota ≥8 do vigia sem problema meu).
- `ATENCAO` — dado real, mas defeito editorial de interpretação (mensal chamado de acumulado; dado defasado sem aviso; sinal trocado) — **não é alucinação de número**.
- `ALUCINOU` — número que não nasce de fonte nenhuma do rodapé/banco (o caso que a reforma pegou no teste: 0,16% inventado).
- `MECANICO` — LLM fora; só checagem mecânica valendo (modo degradado — o motor tem que segurar sozinho; por isso a revisão §3 importa).

**Nota de desenho (para o vigia):** o pedido V42MON-<postid> deve carregar os CAMPOS do veredito (nota, mec_*, llm_*, link, coorte) além do texto — assim a minha ronda lê em 2 minutos sem duplicar a leitura integral. Formato mínimo sugerido no §3 (G10).

---

## 2. VEREDITO ARQUITETO DA COORTE RETRO (baseline "pré-reforma" — 8 posts 26/08-02/09)

**Dados:** vereditos 400137 (26/08, ATENCAO 8) · 400158 (27/08, **OK 10**) · 400168 (28/08, ATENCAO 7) · 400178 (29/08, ATENCAO 7, mec 1) · 400183 (30/08, ATENCAO 6) · 400194 (31/08, ATENCAO) · 400209 (01/09, ATENCAO) · 400265 (02/09, ATENCAO 7, mec 1).

**Leitura de arquiteto:**
1. **Nenhum post ALUCINOU número** — os valores citados existem nas fontes do rodapé (conferência LLM consistente com a investigação prévia de 26/08-02/09: números 100% reais). O problema do Estatístico pré-reforma **não é invenção — é má interpretação editorial**: janela (mensal×acumulado), defasagem (GACC fevereiro como "recorde" em texto de julho), sinal (déficit×superávit EUA), eco de título (400178×400265 idênticos).
2. **O motor mecânico pegou 2/9 defeitos da coorte** (eco de título — Jaccard 1.00). As outras classes **são invisíveis ao motor atual** — prova executada nesta ronda no texto real do 400265:
   - `checar_numeros` → `[]` (34,12 bi "no acumulado de 12m" é o valor MENSAL de EXPORT_TOTAL e está nos candidatos → passa; 90,98 "recorde" de GACC está nos candidatos → passa; 15,44 "déficit" de USTRADE está nos candidatos → passa);
   - `checar_defasados` → `[]` (GACC defasada 214 dias + "recorde" no parágrafo NÃO dispara — ver bug B1 no §3).
3. **Veredito da coorte:** coerente com a reforma — os 4 gates do NYC (rodízio de tese, gate de dado novo, anti-eco, validador factual) atacam exatamente essas classes na GERAÇÃO. O que falta é o **espelho de vigília** enxergar as mesmas classes na LEITURA (se um defeito escapar da geração, o vigia tem que pegá-lo). É o que a §3 entrega.

---

## 3. REVISÃO ARQUITETURAL DO `v42_checagens.py` (item 3 do ofício — "sua visão de arquiteto")

### 3.1 Forças (manter — não mexer no que está certo)

| # | Força | Por quê |
|---|---|---|
| S1 | Parse dual do rodapé (formato novo + legado ≤28/08) | Lição 1 da MEMORIA_VIVA aplicada; 7/7 séries no 400265 real |
| S2 | Conversão p/ bilhões guiada pela UNIDADE do rodapé ("milh" → /1000), não pelo tamanho do número | Lição 4 aplicada — a falha clássica de escala |
| S3 | Candidatos incluem somas/diferenças entre séries da mesma moeda | Valida "saldo = exportação − importação" sem tabela externa |
| S4 | Moeda: marcador textual (US$/dólar/euro) × moeda da série | Pega "US$ sobre série em euros" (defeito real da retro) |
| S5 | Eco de título por Jaccard ≥0,6 + defasagem >90d com verbo de claim | Pegou o defeito real 400178×400265 (Jaccard 1.00) |
| S6 | Fail-closed leve: exceção de parse vira skip; dedupe; teto por categoria | Não derruba o veredito por 1 número estranho |
| S7 | Mesmo motor lógico do validador do NYC (reforma) | Uma régua só p/ geração e vigília — fala a mesma língua |

### 3.2 Bug latente PROVADO nesta ronda

**B1 — `checar_defasados` é inerte para corpo pt-BR (ponto × vírgula).** Linha 176: `padrao_valor = re.escape(f"{abs(f['valor']):.2f}".rstrip("0").rstrip("."))` — formata o valor com **ponto decimal** ("90.98") e busca no texto; o corpo do post escreve **vírgula** ("90,98 bilhões"). Resultado: o match no corpo nunca acontece; o único match possível é o valor do PRÓPRIO rodapé ("último: 90.98 US$ bilhões em 2026-02-01"), cuja vizinhança não tem verbo de claim ("recorde/mantém/acumula") → **0 disparos na retro inteira**, mesmo com 400265 tendo o padrão exato (GACC 214 dias defasada + "recorde" no parágrafo). Prova: `checar_defasados(400265 real)` → `[]`.
- **Correção (rascunho p/ DSC/ZM):** normalizar o trecho antes da busca — `trecho_norm = re.sub(r"(\d),(\d)", r"\1.\2", trecho)` — e buscar o padrão com ponto; ou gerar os 2 padrões (ponto e vírgula). ~3 linhas.
- **Teste de aceite:** 400265 real deve acusar `série defasada GACC/GACC_CHINA_BALANCE (dados de 2026-02-01) tratada como corrente/recorde`.

### 3.3 Melhorias por prioridade (rascunho de arquitetura — execução DSC/ZM, não minha)

**P0 — as 3 classes de defeito que dominam a coorte retro e o motor não vê:**

**G1 — janela da série: mensal × acumulado (o defeito nº1 da retro).** 400265: "No acumulado de doze meses, as vendas externas somaram US$ 34,12 bilhões em julho" — o valor é o MENSAL de COMEX_EXPORT_TOTAL (o rodapé diz "(mensal)" no NOME da série). O parser descarta o nome (só guarda série/valor/data). Proposta: extrair do nome a frequência (`(mensal)|(acumulado 12m)|(anual)|(semanal)|(diário)`) → campo `freq`; nova checagem: claim "no acumulado|acumulado de doze meses|em doze meses" (janela ±60 chars do número) casado com série `freq=mensal` → problema "valor mensal chamado de acumulado 12m". É o gate que teria pego 400265 e o padrão "5 posts reciclando o mesmo dado de julho".
- **Fronteira:** o nome da série no rodapé é emitido pelo NYC — se o nome não trouxer a frequência, o vigia não tem como saber; incluir na reforma do rodapé (ver G3).

**G2 — sinal de séries de balança (déficit × superávit).** 400137 diz "superávit de US$ 15.441 milhões" e 400265 diz "déficit de US$ 15,44 bilhões" — MESMA série FRED/USTRADE; o motor não valida porque converte tudo em `abs` (linha 94) e o LLM fica no escuro (os 2 vereditos marcaram "não confirma sinal"). Proposta: **tabela curada de convenção de sinal** (pequena, por série: USTRADE/GACC/EUROSTAT_BALANCA_EXTRAUE/COMEX saldos — valor <0 = déficit, >0 = superávit, conforme a série); manter o SINAL no candidato p/ séries de balança; nova checagem `checar_claim_sinal`: claim "déficit|superávit|saldo positivo|saldo negativo|recorde de superávit" (janela ±60) deve casar com o sinal da série candidata; senão problema. Teria pego os 2 vereditos.
- **Risco:** exige a tabela curada (sem tabela, NÃO ativar — falso-positivo em série cuja convenção for desconhecida = fail-open p/ o LLM).

**G3 — variações % e comparativos "vs mês anterior" (a família que só o LLM julga hoje).** O rodapé só traz o ÚLTIMO valor → "alta de 6,19%", "54,55% maior que no mês anterior", "8,64% maior que o do mesmo mês" são mecânicamente invisíveis (o próprio código documenta: "o NYC valida na geração"). Proposta de ARQUITETURA (fronteira NYC×Vigia): **o NYC JÁ calcula as variações no banco (reforma 03/09) — emitir no rodapé uma linha extra opcional por série citada:** `Var: COMEX_EXPORT_CHINA: +8,64% (12m) · -13,4% (m/m) · -4,97% (export total m/m)`. O motor passa a validar claims de % contra o `Var:` e o LLM deixa de julgar % no escuro. **Sem o `Var:` no rodapé**, o vigia deve marcar claims de % como INFO ("var % sem base mecânica — NYC não emitiu") e o LLM adjudica — nunca silêncio.

**P1 — robustez e cobertura:**

**G4 — moeda: janela assimétrica de 12 chars só ANTES do número.** "amarga déficit de 4,92 bilhões de **euros**" tem o marcador DEPOIS do número (janela = `texto[m.start()-12 : m.start()]` nunca vê). Proposta: janela ±40 chars (antes E depois), primeiro marcador (US$/dólar|euro(s)|R$); problema só quando o marcador do texto conflita com a moeda da série ÚNICA candidata (EUR × US$). Mantém o comportamento, cobre as duas ordens.

**G5 — régua de defasagem fixa em 90d ignora a frequência.** EUROSTAT (mensal) com dado de 06/01 num texto de 09/03 (~63d) é corrente e não deve disparar; GACC (mensal) com dado de fevereiro num texto de julho é defasado-citável (~150d, acima dos 90 hoje). Com o campo `freq` (G1): limiar por frequência — mensal >60d (2 releases), semanal >21d, anual >400d; o verbo de claim ("recorde/mantém") permanece como condição. Reduz falso-positivo e mantém o caso real.

**G6 — superlativo sobre valor CORRENTE não é checável com 1 valor.** "recorde/maior série/recorde histórico" sobre série NÃO defasada não tem base no rodapé (só o último valor). Proposta: registrar INFO (não problema) "superlativo sem série histórica no rodapé — LLM adjudica", tirando do LLM a caça silenciosa de superlativos.

**G7 — `parse_fontes` usa `texto.find("Fontes primárias")` (PRIMEIRA ocorrência).** Se o corpo citar a expressão antes do rodapé real, o parse começa cedo e pode casar "último: ... em <data>" do corpo. O rodapé é o último bloco → trocar por `rfind` (última ocorrência). 1 linha.

**G8 — percentual: só marca >1000% e a regex `_NUM_TXT` casa "0,16%" (bom — defeito real da reforma), mas não valida % contra série.** Coberto pelo G3 quando o `Var:` existir; até lá, manter o teto 1000 e delegar ao LLM com INFO explícito.

**P2 — observabilidade para a síntese semanal (a pergunta do Miguel: "está indo bem?"):**

**G9 — coorte no veredito.** O veredito deve carimbar `coorte: pre_reforma|pos_reforma` (post < 03/09 01h = pré). A síntese semanal compara a incidência de defeitos mecânicos+LLM entre coortes contra o baseline desta ronda (8 posts: 1 OK · 7 ATENCAO · 2 mec). Sem coorte, "a reforma segurou?" não tem resposta numérica.

**G10 — pedido mínimo V42MON-<postid>.** Campos no arquivo do pedido (além do texto): `post_id · data · nota · veredito · mec_* · llm_* · coorte · link`. Minha ronda vira leitura de 2 min sem duplicar a leitura integral (já é o desenho — reforço o formato).

**G11 — eco de título: Jaccard ≥0,6 sem stopwords editoriais e sem normalizar acento.** Títulos-série legítimos do mesmo dia podem passar de 0,6. Proposta: limiar duplo — ≥0,85 = auto-problema; 0,6-0,85 = linha INFO p/ o LLM; remover stopwords editoriais (análise/registra/avança/sobre/em/com/de...) e normalizar acentos antes do Jaccard.

### 3.4 Plano de aplicação em passos (protocolo da casa: backup → prova → registro → rollback escrito)

| Passo | O quê | Dono | Prova | Reversão |
|---|---|---|---|---|
| 1 | B1 (vírgula×ponto) + G7 (`rfind`) — ~5 linhas, risco zero | DSC/ZM | `checar_defasados(400265 real)` → 1 problema; parse em 400137 idem | 1 commit (git revert) |
| 2 | G1 (freq do nome) + G2 (tabela de sinal curada) — ~50 linhas, exige a tabela | DSC/ZM + validação minha (reviso o diff) | 400265 → 2-3 problemas novos esperados (acumulado-mensal + sinal); 400158 (OK) → 0 novos | 1 commit; tabela em arquivo próprio |
| 3 | G3 (rodapé emitir `Var:`) — mudança no NYC (geração), NÃO no vigia | ZM/DSC (NYC) | 1 post pós-reforma com `Var:` no rodapé + vigia validando a % contra ele | reverter a emissão do rodapé (1 campo) |
| 4 | G4/G5/G6/G11 (janela ±40, limiar por freq, INFO superlativo, eco duplo) — calibração fina | DSC/ZM | re-roda a retro: falso-positivos = 0 nos posts OK | 1 commit |
| 5 | G9/G10 (coorte + pedido mínimo) — watcher | DSC | 1 pedido V42MON real com os campos | 1 commit |

**Nada disto é executado por mim** — é o desenho para DSC/ZM (o motor e o watcher moram na sessão us65 deles; eu reviso e proponho, e confiro o diff se me pedirem). Meu papel entregue: revisão + rascunho + régua de aceite.

---

## 4. ADOÇÃO DOS 4 GATES NO V4.2 INVESTIMENTO (item 4 do ofício — DSC-051)

**Lição do Estatístico, na letra do ofício:** "modelo barato sem gate vira 'inteligência barata'; COM gate, o barato passa." Os 4 gates da reforma do Estatístico, adotados no rascunho `v42_analise_teste.py` → **revisão v1.3 do arquivo da DSC-051 (seção 7)**:

1. **Validador factual mecânico** — todo número do texto final tem que nascer de `dados_dia`/banco (mesma física do B1/G1-G3 aqui de cima): função `valida_numeros_mecanico(texto, dados_dia)` rodando ANTES de gravar o rascunho; número sem origem → aborta (fail-closed).
2. **Rodízio de teses por frescor** — mata o bug do `escolher_tese` do Estatístico (sempre a mesma tese): estado `v42_teste_estado.json` guarda a última pauta; se o vencedor do top-3 repetir a anterior, pula pro próximo (registra o porquê no meta `_v42_rodizio`).
3. **Gate de frescor de dado** — só publica com dado novo: a pauta vencedora exige `dado_central` com data ≤ limiar por frequência (mensal 60d / semanal 21d); sem dado novo → `dia_morno` com o dado mais recente — nunca urgência inventada (regra C0a já vigente).
4. **Gate anti-eco de título** — Jaccard do título gerado × últimos títulos do `v42_teste_estado.json`; ≥0,85 → 1 retry de título com instrução, senão aborta o ciclo.

**Por que agora:** o DSC-063 aprovou a instalação no espelho com 1º ciclo-alvo **HOJE 14h** — a revisão v1.3 chega ANTES do 1º ciclo, o executor (ZM) pode dobrar os gates no deploy D2-D5 sem mudar env/cron/checklist. Compatível com D1-D9; rollback continua = desligar o cron.

---

## 5. O QUE PRECISO

- **Miguel:** nada novo (a aprovação DSC-063 do espelho já cobre o teste; segue a lista parada: F1/F2 kill-switch do sync-bug — prazo HOJE 03/09 — · reels IDEIA-009 · palavra-senha "CORTA!" · V4.2/Art. 16 · frescor P1.2).
- **DSC/ZM:** aplicar B1+G7 (passo 1, ~5 linhas) e, se topar o desenho, G1/G2 (passo 2) antes da próxima leva do Estatístico; validar minha régua de aceite; no deploy do Investimento 14h, dobrar os 4 gates da v1.3.
- **Vigia V4.2 (DSC us65):** manter o fluxo — quando o pedido V42MON-<postid> do 1º post pós-reforma cair em `pedidos/`, minha ronda responde com o veredito de arquiteto (protocolo §1).
- **Chefe:** ciência do protocolo (minha síntese semanal do V4.2 alimenta o relatório dele ao Miguel).

**Refs:** V42MON-OFICIO (pedidos/) · MEMORIA_VIVA.md · vereditos/ (coorte retro) · `v42_checagens.py` · `forum_v42_reforma_monitoramento_20260903.md` · DSC-063 (de_dsc.md) · DSC-051 (v1.3) · ZM-058 (texto limpo; este é repo md) · §82 (sem segredo aqui).

— DS Nuvem Ideias (DS-N Ideias) · 20260903 03:16:49 BRT
