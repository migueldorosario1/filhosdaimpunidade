# 📰 Fórum — Título incompreensível 268457 (Kast/"prisão vitrine"): investigação de autoria + correção + mapa da checagem dupla de títulos

**Data:** 2026-09-01 17:4x→18:0x BRT · **Sessão:** ZCode/GLM-5.3 (Dell) · **Origem:** queixa do Miguel no chat ("Pode ver quem está escrevendo os textos? Qual é a LLM? Está saindo títulos estranhos… a gente não tinha um auditor de título? manda todo mundo apertar a revisão, manda a Laura ver se tem checagem dupla nos títulos, nos textos")
**Irmão do mesmo dia:** post 268482 (Villatoro) → fórum EMU-2 `forum_titulo_villatoro_emenda_emu2_20260901.md` (sessão 17:36).

## 1. O que o Miguel pegou

Post **268457** publicado 01/09 **14:31 BRT** pelo DS-N Publicador (Tencent, origem "fluxo fresco (fábrica ≤12h)"):
- Título: «**Cocaína em transferência expõe falha em prisão vitrine de Kast**» — hermético: "cocaína em transferência" sem dizer QUEM carregava, e "prisão vitrine" = **tradução literal de "cárcel vitrina"** (jargão jornalístico chileno), sem explicação.
- URL: `https://www.ocafezinho.com/2026/09/01/cocaina-em-transferencia-expoe-falha-em-prisao-vitrine-de-kast/` (slug PRESERVADO na correção).

## 2. Quem escreveu (a investigação)

| Camada | Responsável | Prova |
|---|---|---|
| **Geração do texto** | **Redator V4.1, vertical Geopolítica** — cascata LLM `deepseek-v4-pro` / `gpt-5.5` (não é GLM/ZCode; caso análogo saúde 26/08 saiu `gpt-5.5`) | meta `zizi_job_id = v41_geopolitica_1a30c106bd88` (REST context=edit) + fórum V4.2 29/08 ("hoje V4.1 usa deepseek-v4-pro / gpt-5.5") |
| Conta WP | "Redação" (ID **5470**, compartilhada por agentes V4.1) | REST `author=5470`; mapa de autores do Cérebro |
| Capa | worker (mídia 268496) + olho robótico duplo | meta `_cafezinho_img_check` ok, pernas `tribunal_qwen`+`deepseek` APROVADA |
| Fact-check | `_v41_fc` CONFIRMA (fonte **24Horas Chile**, 7º Juzgado de Garantía) | meta no post |
| Publicação | **DS-N Publicador** (Tencent) 14:31 | canal `de_nuvem_publicador.md` |
| Esteira | rascunho criado pela fábrica V4.1 (esteira da Laura) antes de 13:16 | fila do publicador 13:16 |

**Qualidade:** o CORPO é bom (factual, claro, fonte chilena confirmada) — **só o título degenerou** (compressão da manchete original em espanhol). Resposta à pergunta do Miguel "é o ChatGPT 5.5?": o redator V4.1 é cascata `deepseek-v4-pro`/`gpt-5.5` — é um dos DOIS; o log do modelo exato por job fica na máquina da Laura (worker V4.1), pedido anotado na ponte ZM-20260901-031.

## 3. Correção aplicada (17:52, in place, slug preservado)

- Rota canônica da sessão-irmã: `ssh cafezinho-wp` + `sudo -u www-data -- wp post update 268457 --path=/var/www/ocafezinho --post_title='Preso é flagrado com cocaína antes de ir para cadeia de segurança máxima de Kast'`
- **80 caracteres** (teto ideal do gate), sentence case, 1 nome próprio (Kast, explicado no 1º parágrafo como "presidente José Antonio Kast"), sem dois-pontos/travessão, jargão zero.
- Cache: `wp eval 'rocket_clean_domain(); rocket_clean_minify();'` → provas públicas: `<title>` novo, `og:title` novo, `h1 itemprop=headline` novo, home exibindo (contagem 1), slug antigo intacto.

## 4. Por que passou — mapa da checagem dupla de títulos HOJE (a pergunta do Miguel)

1. **`gate_titulo.py` (NYC, 09/08)** — plugado SÓ no `motor_publicador.py` (publicador VELHO, fora da esteira atual); regras **sintáticas** (80c, sem `:`, sem travessão). O título do 268457 (62c, sem `:`/`—`) **passaria mesmo plugado** — não existe regra de CLAREZA.
2. **Auditor Títulos GPT — modo advisor (13/08, cron */30, gpt-4o-mini)** — audita `draft/pending` **SÓ do autor 5786**. A esteira V4.1 publica pelo **5470** → **passa batido**. (Também o auditor `poll` histórico é 5786.)
3. **DS-N Publicador (Tencent, quem publica hoje)** — audita **CAPA** (olho robótico duplo), **não título**.
4. **Manual EMU-2** (hoje 17:36) — diretriz correta, mas **enforcement no v41_ciclo ainda é pendência** (a própria sessão-irmã anotou).

## 5. Estado / o que falta / o que preciso de você (Miguel)

- **Pronto:** título corrigido e provado no ar; autoria e cadeia de responsabilidade mapeadas com provas; ponte ZM-20260901-031 enviada (CL + AGY + DS-N) com a ordem de apertar revisão; este fórum + memória + monitor.
- **Falta:** (a) **enforcement EMU-2 no v41_ciclo (NYC `/root/v4_labs`)**: estender o advisor para autores 5470+5801 (drafts `v41_*`) e adicionar regra de clareza (jargão/tradução literal/sobrenome solto) — sessão com frente NYC, **após o patch da sessão urgente no dsn_publicador** (anti-colisão §112); (b) confirmar com a Laura o **modelo exato do job** `1a30c106bd88` (log do worker V4.1 lá) para fechar "deepseek-v4-pro OU gpt-5.5" com prova; (c) revisão amostral humana de título pré-publish pela CL enquanto o fix não sobe.
- **Do Miguel:** nada obrigatório — validar o título novo no ar (mesma URL).

---

## Adendo 2 — Quem ESCOLHEU a pauta (pergunta do Miguel ~18:2x "por que essa notícia? qual o interesse?") — 18:4x

**Resposta curta:** NINGUÉM humano escolheu. A escolha é 100% automática no `v41_ciclo` (NYC `/root/v4_labs/codigo/v41_ciclo.py`, geo a cada 2h no minuto 55): coletor RSS+Google News+Brave de hora em hora enche o banco geo → o ciclo pega as pautas mais frescas (geo = hard news ≤24h) → a curadoria **"tese dinâmica"** (criada por ordem do Miguel 22/08: "nada hardcode; a tese nasce da notícia") usa uma LLM como editora-chefe que exige **vilão com nome OU herói resistindo + consequência material para o leitor + âncoras textuais** → a PRIMEIRA pauta com tese aprovada é escrita.

**Prova documental (artefato `dados/v41_ciclo/20260831_2156.json`):**
- Pauta original coletada EM INGLÊS: *"Chile fines Chinese mafia inmate after cocaine found at maximum-security prison"* — o gancho geopolítico era a **máfia CHINESA** (ângulo China), não o preso.
- `curadoria_estado: tese_dinamica_aprovada` · **redator: `model: gpt-5.5`** (fecha a pendência "deepseek-v4-pro OU gpt-5.5" → **era GPT-5.5**).
- **🔴 Buraco novo descoberto:** o fact-check `_v41_fc` ficou **`ok: false`** (a claim "cocaína encontrada NA prisão de segurança máxima" foi **CONTRADITA** — foi no Santiago Uno na véspera) e o post foi **publicado assim mesmo** — o publicador não lê o `_v41_fc`. O corpo do texto foi corrigido pelo redator, mas o título herdou a ambiguidade. (O plano do DSN Revisor já prevê: "spot-check factual: se `_v41_fc` reprovado ou ausente → reprova" — este caso PROVA a necessidade.)

**Por que não Irã/China:** o banco geo ESTÁ cheio (31/08 16:00 BRT: RT/SCMP/The Hindu com "US launches new strikes on Iran", "Trump advierte que Irán será aniquilado", "China adapta su movilización de defensa", "China warns of consequences for Taiwan" — tudo `new`). Mas: (1) a geo escreve só **1 pauta a cada 2h**; (2) o critério tese-com-vilão-nomeado favorece pautas de crime/escândalo/instituição com personagens (Kast, CIA, juíza, cartel) e **penaliza hard news de guerra** (mais impessoal — várias rodadas morrem em `llm_sem_tese_valida`/`anti_repeticao`, visível no histórico de artefatos). Resultado: Irã/China SAEM no site (01/09 sanções/Ormuz; 30/08 "Irã nunca se renderá"; Xi/Quirguistão), porém em cadência baixa (~3-5/dia na categoria 5003) e competindo com pautas "dramáticas".

**Opções de ajuste (propsta — aguarda decisão do Miguel + casa NYC):** (a) **ponderação de temas** na fila da geo (boost para Irã/China/guerra/eixos de interesse — lista viva de prioridades do Miguel; base: `Outros/pautas editoriais o cafezinho`); (b) relaxar a tese dinâmica para hard news de guerra (guerra pode ter tese sem vilão individual); (c) subir a cadência geo (2h→1h) para caber mais Irã/China no dia. NADA implementado sem ordem.

---

## Adendo 3 — "VAI" do Miguel ~19:0x EXECUTADO: boost de temas + tese de guerra + geo horária (19:1x)

Implementado no NYC (backups `v41_ciclo.py.bak_pre_temas_20260901` + `crontab.bak_pre_geo1h_20260901`, `py_compile` OK):
1. **Boost de temas prioritários (geo):** pautas cujo título contém keyword da **lista viva** `nyc:/root/v4_labs/dados/temas_prioritarios_geo.txt` (Irã/Irán, China, Taiwan, guerra/war, Gaza, Israel, Ucrânia, Rússia/Rusia, petróleo) sobem para o TOPO da ordem de tentativa de tese no `v41_ciclo`. A lista decide **prioridade, não aprovação** — tese dinâmica/anti-repetição/juiz inter-vertical seguem intactos (fail-closed preservado). Editável sem deploy.
2. **Tese de guerra:** prompt da tese dinâmica ganhou regra para hard news de guerra/sanções/disputa entre Estados — antagonista pode ser ESTADO nomeado (EUA, Irã, China, OTAN) sem pessoa física; consequência material pode ser global (petróleo/comércio/preços) ancorada na notícia.
3. **Geo horária:** cron `55 */2` → `55 * * * *` (dobra a capacidade da vertical).
**Prova da simulação pós-boost (banco real 19:00 UTC):** topo da fila vira "US launches new strikes on Iran", "China adapta su movilización de defensa", Rússia/Gaza — o Chile/Kast despencou. Primeiro ciclo real que exercita: **hoje 19:55 UTC (~16:55 BRT? não — 19:55 UTC = 16:55 BRT já passou; próximo = 20:55 UTC = 17:55 BRT... conferir no log `v41_ciclo.log`**). MODO CONTRATO preservado: fábrica segue rascunho-only (publicação segue parada até a promulgação).
