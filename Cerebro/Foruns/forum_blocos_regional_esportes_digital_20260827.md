# Fórum — Blocos Regional / Esportes / Digital (ordem Miguel 27/08 ~10:20)

**Sessão:** ZCode/GLM-5.3 · **Data:** 27/08/2026 10:22→~11:10 BRT · **Tipo:** correção + análise editorial + fix de produção

## O que o Miguel pediu

1. Post das barricadas no Rio **tinha de ir para o bloco Regional, não Saúde**.
2. Bloco **Esportes sem atualizar há dias** — analisar audiência para decidir se mantém.
3. **Quem faz os posts do bloco Digital?** Qual a diferença para o bloco Tecnologia?

## O que aconteceu (resumo das decisões)

### 1. Post 267872 movido para Regional ✅

- `wp post term set 267872 category 2403 4986 --by=id` (Redação + Regional; **Saúde 258 removida**).
- ⚠️ Pegadinha wp-cli: sem `--by=id`, o comando CRIA termos novos com nome "2403"/"4986" (term_id 21190/21191) — criados e deletados na mesma sessão, sem resíduo.
- Prova pública: home renderizada mostra o link nas 2 ocorrências dentro da seção `Regional` (h4 `m-0 text-red`), fora do bloco Saúde.

**Causa raiz do erro (e fix):** a vertical `saude` usava o **feed GERAL** da Agência Brasil (`rss/geral/feed.xml`) com filtro por keyword por SUBSTRING — a pauta policial passou porque o texto contém "**sus**peitos", "estão **sus**pensas" e "unidades estaduais de saúde" (keyword "sus" casa como substring). Fix aplicado no `/root/coletor.py` do NYC (backup `coletor.py.bak_pre_feed_saude_20260827`): feed geral → **`rss/saude/feed.xml`** (editoria 7, verificado 200 com títulos de saúde puros). 
**Risco residual:** `meio_ambiente` também usa o feed geral (linha ~192) — mesmo padrão de vazamento possível; keywords de ambiente são mais específicas mas o matching continua substring. Pendente decidir trocar por `rss/geral/feed.xml` → feed de ambiente deles.

### 2. Esportes: TEM audiência — recomendação MANTER 📊

**Por que o bloco parecia parado (2 motivos, nenhum é falta de audiência):**
1. **Gap real de produção 24–26/08** (período órfão entre a faxina "só V4.1" de 24/08 e a religação das 3 verticais em 26/08 18:40).
2. **Sequestro pelo Top 10:** o post de HOJE (267864 Vasco×Vitória, 01:55) está no Top 10 Tendências (cat 21169, ranking GA4 24h) e o renderer do Top 10 joga os IDs no `$excludes` — anti-repetição tira o post do bloco Esporte BY DESIGN (front-page.php:51). O bloco mostra até 23/08, mas o post novo está na home, só que em cima.

**Números GA4 (property 374552425, mapeamento slug×categoria, posts /2026/):**

| categoria | views 7d | posts 7d | views/post |
|---|---|---|---|
| regional | 1.817 | 58 | ~31 |
| tecnologia | 781 | 25 | ~31 |
| **esporte** | **549** | **7** | **~78 (1º lugar)** |
| meio_ambiente | 538 | 8 | ~67 |
| saude | 471 | 5 | ~94* |
| ciencia | 458 | 2 | ~229* |
| digital | 114 | 1 | ~114* |

(*) amostras pequenas. Em 30d: esporte 485 views/22 posts ≈ 22/post — no topo junto com regional (~22) e digital (~24), acima de tecnologia (~12), ciência (~13), saúde (~15), ambiente (~12).

**Leitura:** esporte é a vertical secundária com MELHOR retorno por post publicado; o gargalo é VOLUME (7 posts/semana vs 25 da tecnologia). Usuários ≈ views (543/549) = leitor único que lê e sai — típico de notícia de resultado. E o Vasco no Top 10 mostra que pauta quente de esporte repercute. **Decisão fica com o Miguel; recomendação da sessão: manter** — e se quiser crescer, o caminho é volume (a vertical já religou 3x/dia em 26/08).

### 3. Digital: quem faz e diferença para Tecnologia

**Quem faz:** a **vertical `digital` do V4.1** (criada por ordem do Miguel 26/08 ~19:35, memória `bloco-digital-home-vertical-v41-20260826`). Pipeline: coletor/intake 3x/dia (11:15/17:15/23:15 UTC) + `v41_ciclo --vertical digital` 3x/dia (12:08/18:08/00:08 UTC = 09:08/15:08/21:08 BRT); redator gpt-5.5; gates de tese + anti-repetição + juiz inter-vertical; publicação final segue pelos publicadores CM/AGY. Os 5 posts atualmente no bloco são a SEMENTE (posts antigos relacionados, 12–25/08).

**Fix importante desta sessão:** a vertical estava **muda desde o nascimento** — banco `digital.sqlite3` criado sem a tabela `draft_events`, e o gate anti-repetição é fail-closed → todos os ciclos morriam em `gate_erro:OperationalError` (vistos em 26/08 21:15 e 27/08 09:22). Tabela criada copiando o DDL do `saude.sqlite3`; gate validado (`sem_suspeito`); **ciclo manual rodado → draft 267929 "Multa contra TikTok mira desenho que expôs menores"** (cat Digital 21189+Redação, fact-check corrigiu valor R$ 153,7 mi). 1ª matéria inédita da vertical, aguarda CM/AGY publicarem.

**Diferença editorial Digital × Tecnologia:**
- **Digital (21189):** internet como **cotidiano e cultura** — plataformas, redes sociais, apps, big techs no Brasil, regulação (ANPD/Anatel), influenciadores. Fontes: Tecnoblog, Canaltech, Olhar Digital, Núcleo, Mobile Time. Caso: multa do TikTok.
- **Tecnologia (30):** tecnologia como **indústria e ciência** — IA, chips, semicondutores, laboratório, geopolítica da inovação (guerra dos chips). 26 fontes internacionais (Nature/Science/Fapesp...), ~101 posts/30d, gate temático próprio no intake. Caso: Baidu empurrando chips locais de IA.

## O que falta / próximo passo

- CM/AGY publicarem o draft 267929 (1º post inédito do Digital) e a cadência 3x/dia se provar nos próximos ciclos.
- Miguel decidir: manter Esportes (recomendação: sim) e se o bloco Esporte deve ignorar o `$excludes` do Top 10 (hoje, post novo no Top 10 não aparece no bloco da própria categoria).
- Pendente: decidir troca do feed geral no meio_ambiente (mesmo risco do vazamento de saúde).
- Ronda de acompanhamento: conferir se a vertical saúde publica só pautas de saúde nos próximos ciclos (feed novo).

## Irmãs

- Memória técnica: `Memorias/memoria_blocos_regional_esportes_digital_20260827.md`
- Memórias de apoio: `bloco-digital-home-vertical-v41-20260826`, `blocos-saude-esporte-ambiente-v41-religados-20260826` (auto-memory ZCode)

---

## ADENDO 1 — Plano de reorganização Tec/IA + Esporte + Cultura/Séries (27/08 ~11:20, aguarda "vai" do Miguel)

**Ordens:** (1) Tecnologia foca ciência/tecnologia; Digital vira bloco **Inteligência Artificial** focado em IA (ajustar coletas); (2) Esporte: aumentar um pouco a produção / cobrir buracos; (3) plano para Cultura com séries Prime Video/Netflix/Globoplay.

### Diagnóstico levantado (leitura, nada executado)

- Cat WP **"Inteligência Artificial" (5008) JÁ EXISTE** com 627 posts (slug `inteligencia-artificial`); hoje só 2 posts/7d nela — posts de IA da vertical tec saem na cat 30.
- Vertical tecnologia: 25 feeds, **5 dedicados de IA** (TechCrunch AI, ArsTechnica AI, VentureBeat AI, Google AI blog, OpenAI news) + ciência/chips/Ásia; as 6 google_queries são TODAS de IA ("China AI model", "Qwen Kimi DeepSeek"...). Gate temático duro no intake.
- Vertical digital: banco saudável (fix hoje), crons coleta 08:15/14:15/20:15 BRT + ciclo 09:08/15:08/21:08 BRT; `_CATS_NASCIMENTO digital=[21189,2403]` (v41_ciclo.py:398); bloco tema "Digital" query `category__in [21189]`.
- Esporte: coleta 10:15/16:15/22:15 BRT, ciclos 11:22/17:22/23:22 BRT; 7 posts/7d (gates filtram ~2/3); buraco de madrugada/manhã (resultados Europa) e production gap fim de semana.
- Cultura: 2 feeds (Ag.Brasil cultura + Brasil247), 0 fonte de séries/streaming, keywords sem netflix/prime/globoplay; cat "Séries" (3044) existe com 2 posts; coleta 4h; produção 18 posts/7d (~2,5/dia, consumidor a confirmar na execução — sem ciclo v41_ciclo dedicado no crontab root).

### Plano (executar só com "vai")

**A. Bloco Inteligência Artificial (ex-Digital):**
1. Tema (backup): heading "Digital"→"Inteligência Artificial", query `[21189]`→`[5008]` (front-page.php ~727).
2. Coletor seção digital: feeds ← os 5 de IA migrados da tec + tags IA BR (Tecnoblog/Canaltech/OlharDigital — validar URLs na execução); queries de IA; keywords IA com palavras longas (evitar substring "ia" sozinho!). 
3. v41_ciclo: `"digital": [5008, 2403]`.
4. Coletor seção tecnologia: remover os 5 feeds de IA; queries IA→ciência/chips/energia/espaço.
5. Conteúdo de plataforma/regulação (TikTok, ECA Digital): destino cat 30 (bloco Tecnologia); draft 267929 reclassificar [30,2403] na publicação; 5 posts-semente da 21189 migrar p/ 30 e 21189 aposentada.

**B. Esporte (+1 ciclo madrugada):** coleta 3x→4x (+04:15 BRT), ciclo 3x→4x (+05:22 BRT) — cobre resultados Europa/manhã; alvo 1,5-2 posts/dia; gates intactos.

**C. Cultura/Séries:** feeds de entretenimento BR (Purebreak/Popline/Telesérie etc — validar); queries "Netflix série", "Prime Video estreia", "Globoplay novidades", "série renovada cancelada"; keywords netflix/prime video/globoplay/temporada/estreia/trailer/max/disney+; posts de séries nascem [79, 3044, 2403]; identificar consumidor atual da cultura e garantir ciclo V4.1 cultura se for o V4 legado.

**Estado:** plano aprovado-pendente; nada executado. Próximo passo = "vai" do Miguel.

---

## ADENDO 2 — IMPLEMENTAÇÃO EXECUTADA (27/08 ~12:15 BRT, "vai" do Miguel)

### A. Bloco Inteligência Artificial ✅
- Tema (`front-page.php`, backup `.bak_pre_bloco_ia_20260827`): heading "Digital"→**"Inteligência Artificial"**; queries do bloco `[21189]`→`[5008]`; **bloco Tecnologia deixou de incluir 5008** (`[19936,735,30,5008]`→`[19936,735,30]`) — divisão limpa via $excludes anti-repetição.
- Coletor (`coletor.py`, backup `.bak_pre_ia_series_20260827`): seção digital = 5 feeds IA internacionais migrados da tec (TechCrunch AI/ArsTechnica AI/VentureBeat AI/Google AI/OpenAI) + **Olhar Digital tag IA** (validado 200); queries IA; keywords LONGAS (anti-substring). Label SECTIONS → "Inteligência Artificial".
- `config_editorial.py` (backup idem): tecnologia perdeu os 5 feeds IA e as 9 queries de IA → ganhou 6 queries de ciência/chips/energia/espaço/inovação industrial (22 feeds, 13 queries).
- `v4_vertical_intake.py` (backup `.bak_pre_desvio_ia_20260827`): **veto `desvio_vertical_ia`** — pauta com termo IA forte no título (palavra inteira, `IA_TITLE_TERMS`) é rejeitada na tecnologia (a vertical IA pega pelos feeds próprios).
- `v41_ciclo.py` (backup `.bak_pre_ia_cultura_20260827`): `"digital": [5008, 2403]`.
- WP: 5 posts-semente migrados [30,2403] (267615 precisou `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` — guarda editorial); draft 267929 TikTok reclassificado [30,2403]; cat 21189 vazia/aposentada.
- **Prova ponta a ponta:** coleta IA 27 candidatas (OpenAI feed 1154 itens!) → intake 21 new → ciclo → **draft 267948 "Texto de Pedro Spadoni expõe limite do ChatGPT sob paywall" nascendo em [5008,2403]**. Home pública (sem cache-buster) mostra bloco **Inteligência Artificial** com 6 posts.

### B. Esporte 4x/dia ✅
- Coleta `15 7,13,19,1` UTC (nova 04:15 BRT pega resultados Europa) + ciclo `22 8,14,20,2` UTC (novo 05:22 BRT). Crontab backup `/root/crontab.bak_pre_gases_20260827`. 1º ciclo madrugada roda 28/08 05:22 BRT.

### C. Cultura + Séries ✅
- Coletor: +feed Pipoca Moderna (validado 200; TV Foco descartado — feed vazio; Popline/Purebreak/Omelete/RS BR sem RSS) + 4 queries (Netflix/Prime Video/Globoplay/renovada-cancelada) + 13 keywords séries.
- `v41_ciclo`: cultura entra no V4.1 (choice+VERTS) com `_CATS_NASCIMENTO [79, 3044, 2403]`; **cron 2x/dia** `52 16,4` UTC (13:52/01:52 BRT).
- Prova: coleta 16 candidatas (Pipoca 30 itens; banco já tem "Lançamentos de filmes e séries da Netflix em setembro/2026") → ciclo → **draft 267949 Kikito/Gramado em [79,3044,2403]**.
- Nota: 3044 marca TODO post da vertical (mesmo cinema) — refinamento futuro = só marcar 3044 em pauta de série/streaming.

### O que falta / próximo
- CM/AGY publicarem 267948 (IA) e 267949 (cultura) + os próximos ciclos regulares (IA 3x/dia; cultura 2x/dia; esporte 4x/dia a partir de amanhã).
- Acompanhar 48h: bloco IA ganhando posts novos, bloco Tecnologia sem pauta de IA (veto funcionando), primeira matéria de série/streaming saindo.
- Cat 21189 vazia — decidir se deleta ou mantém aposentada.
