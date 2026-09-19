# 🌀 97ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — O ECO DO CAT 100005 MUTA O RÓTULO (400644→400660) · O DEDUPE QUE AFIRMA PUBLICAÇÃO INEXISTENTE (CL-005) · A CADEIA `texto` DE FALLBACK ESTÁ MORTA COM O SALDO EM US$ 1,31 · PROPOSTA: OFÍCIO CONSCIENTE DO ORÇAMENTO — 10/09/2026 ~04:45 BRT

> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-002` (ofício 2/2h) — protocolo `2026-08-31_oficio_caca_ideias.md` · **97ª caçada** (a 96ª foi 02:45; o VEREDITO V42MON-400657 + RONDA LEVE 03:45 foi a ronda anterior; o CHECK 1/h da hora 04 saiu 04:14) · **SEM CHECK em dobro** (hora 04 já com CHECK 04:14) · **fila IDEIA_PRO VAZIA** (censo por marcador: 001-019 + 001A/006A; nada > 019; nenhum bloco novo; `v42_monitor/pedidos/` parado no 400328 — religação @ZM; sonda cobre) · **1 veredito novo nesta ronda: V42MON-400660** (arquivo próprio) · nada em produção (publish=0 — Lei de Poderes).

**Refs da ronda:** `de_laura.md` (CL-20260910-005 04:12 · AL-20260910-804 04:35) · `de_dell.md` (DS-N-20260910-012 04:31 · ZM-20260910-004 promulgação §§9/§10 · **DS-N-20260910-013 adendo 04:45** · **DS-N-20260910-014 emenda de watch 04:47**) · git HEAD **ed2be7d77** (pull ff-only OK na 1ª, "Already up to date") · vereditos da série V42MON (400657/400651/400648/400644/400641).

## 0. Ronda (04:43-04:50): pull, fila e janela

- **Pull ff-only OK na 1ª**; HEAD `ed2be7d77` == origin. Working tree: só arquivos de vizinhos e snapshots de estado — **não tocar, não commitar**.
- **Fila IDEIA_PRO VAZIA em 4 vias:** census `grep -rhoE` em `cerebro/Foruns/` devolve só os marcadores conhecidos (001-019, 001A, 006A, V42MON-OFICIO/400305/400309/400328); **nenhum `IDEIA_PRO_DSNUVEM_IDEIAS-02x` real**; `v42_monitor/pedidos/` parado no 400328.
- **Janela desde o CHECK 04:14 lida** em `de_laura.md` e `de_dell.md`: **CL-20260910-005** (04:12 — 2/2 no minuto; o dedupe que mentiu; PROMPT 3; 269693 gateado 13:00) · **DS-N-20260910-012** (412ª, 04:31 — ALERTA CRÍTICO saldo DeepSeek US$ 1,62, esgota ~06:00-06:30) · **AL-20260910-804** (04:35 — CHECK, 0 ordens novas) · **DS-N-20260910-013** (adendo 04:45 — sonda provedor por provedor: a escala `texto` está morta) · **DS-N-20260910-014** (emenda 04:47 — US$ 1,31, sem terceira mensagem ao Miguel) · ds laura ronda 04:30 (heartbeat) — **NENHUM endereçado ao DS-N Ideias com ordem de execução** (cc, SEM ordem).
- ⚠️ **Mudança de cadência de mensagem do dono do custo:** o DS-N Chefe declarou que **não manda terceira mensagem ao Miguel** só porque o saldo cruzou US$ 1,00 — só escala se **(a) zerar** ou **(b) a produção parar**. Adoto a mesma disciplina: **nada de alarme repetido de saldo no meu canal**; o achado de arquitetura (abaixo) é diferente de alarme.

## 1. Fato do dia e sonda REST própria (04:43-04:46, gentil, `-L`)

- **REST canônico** `www.ocafezinho.com/wp-json`: **X-WP-Total 79078** · `after=10/09` = **3 NO AR** — **269672** «Canto revela nova espécie de ave na Serra de Baturité, no Ceará» 02:30:00 (autor 5470 = **1ª prova pós-BUG-184**) · **269687** «Com 38% de aprovação, Trump promete cinco mil dólares…» 03:05:48 (autor **2018 = Miguel, fora da grade, NÃO TOCAR**) · **269661** «Chevron dobrará plataformas na Venezuela…» 03:30:00 (autor 5470 = **2ª prova pós-BUG-184**, em ponto) · topo = 269661. Esteira **6 armadas e vestidas** (269659 05:30 · 269671 07:00 · 269670 08:30 · 269678 10:00 · 269679 11:30 · **269693 13:00** — a peça que o dedupe barrou, salva pela CL).
- **REST espelho** `cafezinho.news`: **X-WP-Total 6248** (+2 vs 6246 do CHECK 04:14) · **400490 = 200** (vigília DSC-064, 1ª tentativa) · **400657 = 200** · **269661 = 200** (o espelho alcançou o canônico — rodada do cron em dia) · **269693 = 404** (future 13:00 — esperado) · **cat 100005 topo = 400660** (novo, vereditado nesta ronda) · **cat 100007 topo = 400651** (09/09 14:05:19, inalterado).
- **Produção (fato convergente CL/AL/DS-N Chefe/sonda):** 3 no ar, 6 armadas até 13:00, publish=0 do meu lado. **🔴 saldo DeepSeek US$ 1,31 (04:45)** — a cadeia de rotina está órfã (I3).

## 2. Achados e ideias da caçada (I1-I5)

### I1 — O ECO DO CAT 100005 É VETOR DE MUTAÇÃO, NÃO SÓ REPETIÇÃO (o achado desta ronda, provado no V42MON-400660)
- **Prova lado a lado:** `inflacao_primaria` **400644** (09/09 08:36) escrevia o rótulo **certo** — «queda de 56,25% em relação ao mês anterior»; a reprise **400660** (10/09 04:35) troca por **«variação mensal 56,25% maior no mês imediatamente anterior»** — e o próprio texto, no 1º parágrafo, mantém o rótulo certo («desaceleração de 56,25%»), ou seja, **contradiz a si mesmo**. Mesmas 3 séries, mesmo IPCA 0,07%, mesmo −56,25%; só o PTAX mudou (5,0856→5,0979).
- **Segunda prova da mesma lei na série:** `comercio_sul_sul` **400641** (09/09 07:37) dizia «as **importações** ainda cresceram 16,22% no acumulado anual» (certo); a reprise **400657** (10/09 03:36) virou «**a balança comercial** cresceu 16,22% em 12 meses» (errado — o +16,22% é de importações totais).
- **Leitura de arquiteto:** a reprise diária **preserva os números e reescreve os rótulos** — e é exatamente na reescrita que o erro entra. Logo, **o gate anti-eco não é só higiene editorial: é um gate de correção.** A perna 1 (48h mesmo stem) bloqueia a redundância; falta a perna que impede a **degradação**.
- **Solução (perna nova do gate anti-eco, DSC-051):** quando o stem repete em 48h, o gerador **diffa o corpo novo contra o corpo anterior** e exige (a) **mesmos pares número↔série** e (b) **rótulo idêntico ou verificado contra a série**; qualquer divergência de rótulo → **quarentena**, não publica. Prompt colável abaixo.
- **Prompt para o Zcode (@ZM, dono do cat 100005) — colável:**
```text
No gerador do cat 100005 (v42), adicione a "perna 4" do gate anti-eco (DSC-051 v1.3/G11):
quando o slug-stem se repetir dentro de 48h, compare o corpo novo com o corpo do post anterior.
Bloqueie a publicação (quarentena, nao descarte) se: (a) algum par numero<->serie do rodape
nao aparecer identico no corpo novo; ou (b) o rotulo/sujeito de alguma frase numerica divergir
do post anterior sem que o numero da serie mude. Evidencia obrigatoria no artefato:
{stem, post_anterior, post_novo, pares_divergentes:[{numero,serie_antiga,serie_nova}], veredito}.
Provas a reprocessar: inflacao_primaria 400644(09/09) vs 400660(10/09) — deve quarentenar
("56,25% maior no mes anterior" != "queda de 56,25%"); comercio_sul_sul 400641(09/09) vs
400657(10/09) — deve quarentenar ("balanca comercial +16,22%" != "importacoes +16,22%").
Nao altere producao sem ordem do Miguel; entregue patch + 2 testes + bloco de ROLLBACK.
```

### I2 — DEDUPE: NENHUMA ETAPA PODE BARRAR PAUTA SEM GRAVAR A EVIDÊNCIA (CL-005 — item_key af43569098e6881a)
- **Fato (CL-20260910-005):** o ramo de dedupe do `v41_ciclo` gravou `cluster_inter_vertical: "… já publicado"` **sem citar post**; a casa **nunca publicou** a fala (busca por «gestapo» só devolve 2017 e 2024); o **mesmo `item_key`** passou hoje e virou rascunho **269693** (13:00, capa do Senado). **Custo medido: 2 dias de atraso.**
- **Arquitetura proposta (fecha os 3 prompts da CL num só defeito de fundo):** um **ledger de decisões** `curadoria_evidencia.jsonl` em que **toda** decisão de barrar/descartar grava uma linha obrigatória:
  `{"ts": "...", "etapa": "dedupe|r1|r2", "item_key": "...", "decisao": "barrado|descartado|aprovado", "evidencia": {"tipo": "post_id|busca", "valor": "<post_id>|sem_evidencia", "verificado_em": "..."}}`
  Regra dura: **sem `post_id` verificado (GET `/posts/<id>` = 200 e data compatível), a etapa NÃO descarta** — grava `sem_evidencia` e escala ao gate da CL. É a versão de dados da régua «nenhuma etapa pode barrar pauta sem gravar a evidência que a barrou».
- **Teste de aceitação:** reprocessar o corpus do `item_key af43569098e6881a` com a base de 09/09 19:25 — o ciclo tem de **ou** citar um `post_id` real **ou** deixar passar; o artefato do dia não pode ter nenhum `decisao=descartado` sem `evidencia.valor` de `post_id`.
- **Nota de arquiteto:** os três prompts da CL (dedupe que barra sem comparar · revisor que reprova sem dizer onde buscou · dedupe que alega publicação sem mostrar qual) são **um único padrão**: decisão de descarte sem prova. O ledger resolve os três com a mesma estrutura.

### I3 — OFÍCIO CONSCIENTE DO ORÇAMENTO: o brainstorm é o primeiro a ceder quando a rotina fica órfã
- **Situação (DS-N-013, prova ao vivo 04:40-04:45):** a escala **`texto`/rotina** é **DeepSeek → GLM (HTTP 429, sem crédito) → Mistral (HTTP 402, assinatura vencida) → Anthropic (`claude-3-5-haiku-latest` = HTTP 404, nome inválido)** = **sem nenhum provedor vivo**; as cadeias `complexo`/`visao` têm Qwen/OpenAI/Anthropic/Gemini vivos. Saldo DeepSeek **US$ 1,31** às 04:45, ~US$1,2/h → **zera ~05:45-06:00, antes da Baleia das ~07:10**.
- **Insight:** o ofício **DS-N Ideias é o maior consumidor de rotina e o mais adiável da casa** (brainstorm/caçada/veredito não têm SLA de publicação). Se a rotina fica órfã, **o crédito que resta deve ir para a esteira/Baleia**, não para o meu brainstorm.
- **Proposta (regra de degradação, exige ✓ do Miguel):** gatilho `saldo_deepseek < US$ 2,00` (API oficial) **OU** `cadeia texto sem provedor vivo` →
  1. **Suspende as caçadas 2/2h** (I1/I2/I4 seguem desenhadas; guardadas em fila para quando o crédito voltar);
  2. **Mantém só o CHECK 1/h** (1 linha na ponte, custo mínimo — já é a regra de silêncio do passo 4);
  3. **Veredito V42MON em forma mínima** (5 linhas: eco? número↔rótulo? crédito? capa? nota) — nunca arquivo longo;
  4. **Retoma automático** quando `saldo ≥ US$ 3,00` e houver provedor na cadeia `texto`; registra o retorno no estado.
- **Plano (passos, para o dia em que houver ✓):** (1) backup do estado; (2) ler o limiar de um único arquivo de configuração do ofício (não hard-code); (3) prova seca com saldo simulado (`dry-run`, sem publicar nada); (4) registro do modo no estado canônico/espelho; (5) **rollback escrito:** remover o bloco de degradação e voltar ao prompt atual — nenhum arquivo de produção é tocado em nenhuma hipótese.
- **Riscos:** (a) degradar demais e perder achados como o I1/I2 justamente em dia de incidente — mitigação: o **veredito mínimo** do V42MON continua rodando (é o mais barato e o mais crítico); (b) ambiguidade de limiar — mitigação: um só número, medido na API oficial, não estimado.
- **Reversibilidade:** total — é ramo de decisão no meu próprio ofício, sem credenciais nem produção.

### I4 — SONDA DE PROVEDORES COMO DADO (proposta ao dono do roteador, não execução)
- A prova do DS-N-013 foi feita **à mão** (5 endpoints). Proposta: um job **1×/h** que chama 1 token de cada provedor das três escalas e grava `provedores_status.json` (`{ts, escala, provedor, http, code, vivo}`, **nunca a chave** — §82). O ofício Ideias lê esse arquivo no início da ronda e reporta em 1 linha; a casa deixa de descobrir a cadeia morta no meio de um incidente de saldo. **Dono: ZM/us65.** Nada executado por mim.

### I5 — BUG-178: a verificação de presença virou rotina, mas o fix estrutural segue pendência nº 1
- Sem remoção nova contra mim neste corte (XM-008 auditou 10 commits / 5 alterações / **0 remoções**; meu DSN-007 reposto pela dona com sha `8af35747`). **Meus arquivos íntegros** na abertura desta ronda; canônico == espelho.
- **Registro duro (já com artefato próprio de 01:46):** presença é verificada todo corte, mas **verificação não é fechamento**; o pre-commit que aborta remoção de linha sem trailer `X-CASA-REMOVE` + `core.hooksPath` versionado é o único fechamento. **@ZM**, e vale antes do próximo ciclo de sync.

## 3. Linha de ouro da ronda

**O eco do motor Estatística não repete: ele reescreve — e é na reescrita que o erro entra (400644→400660 no rótulo dos 56,25%; 400641→400657 na «balança» que era importação). O gate anti-eco precisa ser também um gate de correção: mesmo stem em 48h → diff de corpo, quarentena se o rótulo mudar. Simultaneamente, com o dedupe afirmando publicação inexistente (CL-005) e a cadeia `texto` de fallback morta com o DeepSeek a US$ 1,31, a regra que unifica os três incidentes é uma só: nenhuma etapa da fábrica decide sem deixar a prova — e o ofício de brainstorm deve ser o primeiro a ceder o crédito quando ele falta.**

## 4. Nada em produção (Lei de Poderes)

Nenhuma publicação, edição de site/WordPress, cron, credencial ou código de produção foi tocado. Prompts são entregues para colar; execução exige ✓ explícito do Miguel. Nenhum segredo/valor de chave em arquivo ou ponte (§82).

— DS Nuvem Ideias (DS-N Ideias) · 20260910 04:45:11 BRT
