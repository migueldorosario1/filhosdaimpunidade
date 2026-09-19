# FÓRUM — Editorial Semanal LOGIS (a casa de notícia do portal)

**Criado:** 22/08/2026 ~23:10 BRT · **Agente fundador:** ZCode/GLM-5.3 · **Dono:** Instituto de Logística e Sustentabilidade (responsável: jornalista Miguel do Rosário)
**Modelo:** adaptado do V4.1 do Cafezinho para o LOGIS (ordem do Miguel) — **coleta → tese → imagem → texto**.
**Automação:** ritual embutido na automação diária `automation-6b58cdb8` (09:00) — **aos sábados executa o editorial antes do ritual do Instituto** (o workspace limita 1 automação por sessão; ordem Miguel fica: 1 editorial/semana, **alternando Nacional ↔ Internacional**).

## 1. O método (regras do Miguel, 22/08 ~23:00)

1. **Coleta primeiro**: varrer a semana de notícias de logística (escopo do nº: nacional ou internacional). Nacional: PNL, ANTAQ, ANTT, DNIT, Receita, portos, ferrovias, fronteiras. Internacional: os 8 feeds de `src/data/rss.ts` (FreightWaves, Loadstar, Splash247, Supply Chain Dive, RailFreight, JOC, SupplyChainBrain, gCaptain) + buscas complementares.
2. **A tese nasce da notícia** (regra de ouro herdada do Cafezinho): a tese é formulada DEPOIS da coleta, com âncoras literais nas notícias lidas — nunca um conceito imposto antes. A tese é a alma do editorial e orienta texto E imagem.
3. **Imagem de acordo com a tese**: procurar foto real e licenciada (Wikimedia Commons / Flickr CC BY / CC BY-SA — **nunca NC nem ND**; verificar com os próprios olhos antes de aplicar; crédito + licença obrigatórios). Sem foto segura → ilustração SVG própria (nunca publicar imagem sem verificação).
4. **Texto de acordo com a tese**: editorial ~8-10 parágrafos em PT + versões completas EN e ES. Toda afirmação factual vem da coleta com fonte na nota final.
5. **Publicar**: atualizar `src/content/pages.ts` (home `manchete` + `editorial`) → `npm run build` → `python3 /tmp/vercel_deploy_logis.py logis-magazine` → commit/push no repo `logis` (checar `git log` antes — o Antigravity trabalha em paralelo!). Antes de substituir, **arquivar o editorial anterior no §3 deste fórum** (histórico nunca se perde).

## 2. Estado da rotação

| Nº | Data | Escopo | Tese | Status |
|---|---|---|---|---|
| 1 | 23/08/2026 | **Nacional** | "Abrir o corredor, vigiar a porta" — obra e vigilância assinadas juntas (Chancay/bioceânica/PNL × fronteiras/TSE) | ✅ publicado (commit `a116d6a`) |
| 2 | 29/08/2026 (sáb) | **Internacional** | — | ⏳ automação 08:00 |

## 3. Histórico (arquivar o texto integral de cada edição ao substituir)

- **Nº 1 (23/08/2026, nacional):** "Abrir o corredor, vigiar a porta" — texto integral em `src/content/pages.ts` (editorial) até a edição nº 2; fontes: Chancay em operação comercial, agenda bioceânica, GloboNews/TSE fronteiras, O Globo R$ 500 bi.

## 4. 📡 PROJETO PENDENTE — RSS TRADUZIDO (a ideia inteligente do Miguel)

"Ninguém fez: pegar um RSS bom de logística e TRADUZIR o RSS para a língua do site, publicando os textos traduzidos na língua do usuário." Pipeline proposto: cron (2×/dia?) → fetch dos 8 feeds (`src/data/rss.ts`) → dedup → LLM traduz títulos+resumos (PT/EN/ES) → gera página "Do mundo, traduzido" (`/pt/mundo/`) no build → créditos e links à fonte original. **Status: ideia registrada; implementar em sessão dedicada** (usar crons do Dell tipo Cafezinho; zero custo além do LLM).

## 5. Diário

| Data | Evento |
|---|---|
| 22/08 ~23:10 | Fórum criado; editorial nº 1 (nacional) publicado na manchete da home; automação semanal sáb 08:00 criada; seção RSS com 8 fontes no ar; projeto RSS-traduzido registrado (§4). |
| 31/08 | ⚠️ ATRATO detectado: a edição nº 2 (internacional, agendada sáb 29/08 08:00) NÃO rodou (automação não disparou sessão de sábado). Pendência: publicar em atraso (domingo) ou pular para 05/09 — decisão do Miguel. |
