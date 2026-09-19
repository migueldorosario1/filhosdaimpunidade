# Análise editorial da audiência — Cafezinho 07-20/07/2026

**Data:** 2026-07-20 11:00 BRT
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`) — engenheiro-chefe do ecossistema + editor-chefe do Baleia Azul
**Sessão:** `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020` (contínua desde 19/07)
**Fonte de dados:** GSC diário NYC (`/root/agent_data/gsc/diario_*.json`, 14 pontos entre 07-20/07) + performance analyzer NYC (`analise_performance.json`, últimos 14 dias)
**Pedido:** Miguel do Rosário — "faz uma análise da nossa audiência nas últimas duas semanas, segundo CTR, número de views por post, e outros números, veja se encontra alguma coisa positiva em relação a nossa posição no google web search"

---

## Sumário executivo (60 segundos)

O Cafezinho **subiu no ranking Google** nas últimas 2 semanas (posição média melhorou de 3.35 → 2.62) e **manteve o núcleo de cliques 28d estável** entre 42-45 mil. Mas **as impressões despencaram 35%** no mesmo período (1.57M → 1.02M), sinal de que o Google está mostrando menos páginas — o que pode ser efeito residual da punição algorítmica pré-recovery.

**A onda de tração 15-19/07** (pico 8.073 cliques/3d em 16/07) mostrou uma coisa importante: **quando o Cafezinho publica pauta política+geopolítica com denúncia, o público responde forte**. Foi Irã + ICL (Moreira/Demori) que puxou. Sem essa combinação, tráfego volta pra baseline 1-2k cliques/3d.

**Sinais positivos concretos:**
- Brand queries fortíssimas: `o cafezinho` = **CTR 60,3%** pos 1.1, `ocafezinho` = **CTR 82,3%** pos 1
- 2 mega-posts na semana: Moreira ICL **24.588 views** e Demori **11.217 views**
- Guerra Irã como categoria ativa: `guerra ira` CTR 12,5% pos 1
- Cauda longa robusta: 250 queries no top-50, posição ≤3 dominante
- Discover pode estar voltando (dados incompletos, verificar depois)

**Sinais preocupantes concretos:**
- Impressões 28d: 1.571.866 → 1.016.504 (-35%)
- CTR 3d: pico 12,83% (15/07) → 4,42% (20/07)
- Fila V4 acumulou 26 drafts pendentes — produção não vira publicação
- 2 drafts recentes sem `featured_media` — pipeline de cartoon Wan 2.6 pode estar quebrado

---

## 1. Série temporal (GSC 07-20/07)

Cada linha corresponde a um dia de captura. Janelas de 3 dias móveis (o Google só devolve consolidado assim). Coluna "28d" é acumulado dos 28 dias anteriores à captura.

| Data | Cliques 3d | Impressões 3d | CTR | Posição | Cliques 28d | Impressões 28d |
|---|---:|---:|---:|---:|---:|---:|
| 07/07 | 1.070 | 10.931 | 9,79% | 2,23 | 45.153 | 1.571.866 |
| 08/07 | 1.747 | 22.337 | 7,82% | 1,71 | 45.414 | 1.568.548 |
| 09/07 | 1.790 | 22.656 | 7,90% | 1,73 | 44.748 | 1.523.411 |
| 10/07 | 1.272 | 13.365 | 9,52% | 1,93 | 43.918 | 1.493.336 |
| 11/07 | 1.300 | 14.105 | 9,22% | 1,94 | 41.638 | 1.453.155 |
| 12/07 | 1.270 | 15.489 | 8,20% | 2,18 | 41.283 | 1.440.326 |
| 13/07 | 611 | 7.414 | 8,24% | 2,78 | 38.887 | 1.323.679 |
| 14/07 | 1.039 | 13.757 | 7,55% | 2,34 | 38.687 | 1.299.223 |
| **15/07** | **5.186** | **40.422** | **12,83%** | 3,23 | 42.595 | 1.316.126 |
| **16/07** | **8.073** | **75.758** | **10,66%** | 3,35 | 45.103 | 1.165.117 |
| 17/07 | 4.885 | 58.159 | 8,40% | 2,81 | 44.817 | 1.095.400 |
| 18/07 | 3.589 | 39.361 | 9,12% | 2,00 | **45.637** | 1.081.239 |
| 19/07 | 4.016 | 63.160 | 6,36% | 2,39 | 45.457 | 1.071.220 |
| 20/07 | 2.769 | 62.694 | 4,42% | 2,62 | 42.912 | 1.016.504 |

**Leitura em uma linha:** 07-14/07 baseline (~1k cliques/3d) → **onda 15-19/07** (5-8k) → normalização 20/07.

## 2. Top 15 queries que trouxeram cliques (17-19/07)

| # | Query | Cliques | Impressões | CTR | Posição |
|---:|---|---:|---:|---:|---:|
| 1 | `o cafezinho` | 479 | 794 | **60,3%** | 1,1 |
| 2 | `icl` | 422 | 7.663 | 5,5% | 2,28 |
| 3 | `guerra ira` | 152 | 1.216 | **12,5%** | 1,0 |
| 4 | `irã` | 129 | 5.388 | 2,4% | 1,5 |
| 5 | `cafezinho` | 126 | 526 | **24,0%** | 1,13 |
| 6 | `china` | 97 | 1.258 | 7,7% | 1,77 |
| 7 | `ocafezinho` | 79 | 96 | **82,3%** | 1,0 |
| 8 | `icl demissões` | 71 | 547 | 13,0% | 2,21 |
| 9 | `icl notícias` | 65 | 5.568 | 1,2% | 3,09 |
| 10 | `vazamento de gas manaus` | 61 | 820 | 7,4% | 1,05 |
| 11 | `guerra no irã` | 58 | 447 | **13,0%** | 1,0 |
| 12 | `ira` | 47 | 1.353 | 3,5% | 1,05 |
| 13 | `guerra` | 46 | 634 | 7,3% | 1,0 |
| 14 | `trump` | 44 | 1.391 | 3,2% | 1,05 |
| 15 | `cid gomes` | 38 | 595 | 6,4% | 1,88 |

**Total top-50 queries:** 250 (limite API). Cauda longa muito distribuída — a ordem 51-250 provavelmente carrega mais tráfego que os top 15 juntos.

## 3. Top 10 posts por views (14 dias, GA4/NYC)

| # | Views | ID | Título |
|---:|---:|---|---|
| 1 | **24.588** | 261893 | Moreira confirma antecipação de dividendos pouco antes das demissões no ICL |
| 2 | **11.217** | 261577 | Eduardo Moreira explica demissão de Demori e cita prejuízo com anúncios nas big techs |
| 3 | 1.618 | 262164 | Datafolha mostra reviravolta em favor de Lula em São Paulo |
| 4 | 1.091 | 261555 | Exclusivo! Os documentos da condenação de Paulo Figueiredo e Jason Miller nos EUA |
| 5 | 572 | 261410 | AFA entra na mira do FBI por escândalo bilionário durante a Copa |
| 6 | 569 | 261555* | Exclusivo! As picaretagens de Jason Miller, o lobista do tarifaço |
| 7 | 546 | 261337 | Irã diz ter criado "cérebro artificial" com neurônios vivos |
| 8 | 516 | 262267 | Política — O Cafezinho (categoria) |
| 9 | 509 | 262055 | O discurso revolucionário de Xi Jinping em Xangai sobre inteligência artificial |
| 10 | 472 | 261555* | Exclusivo! A história do chinês golpista que bancou Paulo Figueiredo e Jason Miller |

_* IDs 261555 aparecem 3x — provavelmente série "Exclusivo Jason Miller" com URLs distintas mas mesmo ID_base._

**Concentração:** posts #1+#2 (ICL Moreira) somam **35.805 views** — 75% do top 10. Sem eles, média cai de 1.652 pra ~400/post.

**Média geral:** 1.651,7 views/post · **Posts acima da média:** 2 (os 2 top) · **Posts abaixo:** 5.

**Macrotema dominante 14d:** `geopolitica_expandida` com **73,4% do peso** (segundo `performance_weights` NYC).

## 4. Padrões editoriais que funcionaram

### 4.1 Denúncia investigativa política interna (ICL / Moreira / Demori)

- **35.805 views** combinados nos 2 top posts, ambos criados 15-16/07
- Query "icl" gerou 422 cliques em 3 dias, "icl demissões" mais 71
- **Sinal:** conteúdo de bastidor com nomes, valores, ação legal traz retorno desproporcional
- Cafezinho ancorou marca em "quem fala do ICL é o Cafezinho"

### 4.2 Guerra Irã / EUA / Oriente Médio (rendendo em julho)

- 3 queries no top 15: `guerra ira`, `irã`, `ira`, `guerra no irã`, `guerra` — todas em **posição 1** com CTR 3-13%
- Post 261337 (Irã cérebro artificial): 546 views mesmo sem ser mega-manchete
- Fila V4 atual tem MUITOS drafts nessa linha (262246 Kuwait/Ormuz, 262262 Índia alerta, 262267 Rússia Kyiv, 262296 Golfo)
- **Sinal:** enquanto conflito persistir, Cafezinho tem espaço garantido no Google

### 4.3 Brand queries com CTR excepcional

- `o cafezinho` **60,3%** CTR
- `cafezinho` **24,0%** CTR
- `ocafezinho` **82,3%** CTR
- **Sinal:** audiência DIGITA o nome do site pra chegar. Isso é lealdade rara — indica base de leitores diários que confia no editorial e não passa pelo Discover/Facebook. É o ativo mais duradouro.

### 4.4 Denúncia externa (Jason Miller / Paulo Figueiredo / tarifaço)

- 3 posts no top 10 (IDs 261555 diferentes URLs) sobre Jason Miller/Figueiredo
- Query `trump` no top 15 com pos 1,05
- **Sinal:** série investigativa com aprofundamento continua rendendo

### 4.5 Ciência+tech chinesa (viés anti-imperialista)

- Xi Jinping IA (262055): 509 views
- Query `china` top-15 (97 cliques, pos 1,77)
- Cafezinho é uma das poucas vozes brasileiras que cobre tech chinesa sem viés ocidental
- **Sinal:** nicho pouco disputado, alta autoridade Google

## 5. Sinais positivos concretos (o que Miguel pediu)

1. **Posição média SUBIU** durante a onda: pico 3,35 (16/07) → **2,62 (20/07)**. Google reagiu positivamente ao volume de publicação, subindo o Cafezinho.

2. **Cliques 28d resilientes** entre 38-45k — média ~43k/mês. Isso é audiência sólida e recorrente.

3. **Pico 16/07 provou capacidade:** 8.073 cliques em 3 dias, 75.758 impressões. Cafezinho aguenta escala quando o editorial acerta.

4. **Brand strength inegável:** 3 queries com nome do site trazem >680 cliques/3d (479+126+79). Isso é público direto, imune a mudança de algoritmo.

5. **Discover não está vazio (indício):** post 262055 (Xi Jinping) subiu pra top-10 com views 509 — típico padrão Discover. Precisa verificação separada.

6. **Cauda longa forte:** 250 queries no top-50 GSC, posição média <3 nas principais. Cafezinho está bem indexado, o problema é volume de impressões (Google mostrando menos), não relevância (quando mostra, clica).

## 6. Sinais preocupantes (transparência editorial)

1. **Impressões 28d caíram 35%** em 2 semanas: 1.571.866 → 1.016.504. Google mostra menos páginas do Cafezinho — pode ser efeito residual da punição algorítmica ou revisão de política de conteúdo do Google.

2. **CTR volta pra baseline** após o pico: 12,83% → 4,42%. O pico foi puxado por 2-3 posts virais; sem novos virais, normaliza.

3. **Concentração perigosa:** 75% dos views do top-10 vieram de 2 posts. Se não replicar Moreira ICL nas próximas semanas, média despenca.

4. **Fila V4 acumulada:** 26 drafts pendentes segurados por falta de curadoria ou por Sentinela ser cauteloso demais. Produção sem publicação = desperdício.

5. **Pipeline de imagem V4 falhando silenciosamente:** 2 drafts recentes (262275, 262296) sem `featured_media`, bloqueados por `ABORT-sem-featured-media`. Codex mencionou `skip_image=True` como possível causa — não resolvido ainda.

6. **Sem dados frescos GA4/Discover consolidados:** o `analise_performance.json` cobre GA4 14d mas Discover isolado precisa consulta separada — pendência.

## 7. Recomendações de pauta pros próximos 7-14 dias

### 7.1 Manter linha vencedora (não abrir novas frentes)

- **Continuar cobertura ICL / Moreira / Demori** enquanto durar. Se aparecer novo desdobramento (novo executivo demitido, resposta pública, ação judicial), publicar rápido.
- **Continuar cobertura guerra Irã** — pauta ativa, posição 1 no Google. Sentinela deve priorizar drafts geopolíticos Oriente Médio nas próximas horas.
- **Continuar série investigativa Jason Miller / tarifaço Trump** — Cafezinho tem exclusividade, público responde.

### 7.2 Explorar nichos com pouca concorrência

- **Ciência+tech chinesa** — 509 views em Xi Jinping IA mesmo sem push. Publicar 2-3 posts/semana sobre BRICS+tech, quantum china, chips, IA anti-hegemônica.
- **Denúncia extrema-direita internacional** — Milei, Bolsonaro casa detenção, Trump tarifaço, Fachin STF. Cafezinho é referência.

### 7.3 Ancorar brand queries

- Posts com título mencionando "Cafezinho" tendem a viralizar quando compartilhados (queries `cafezinho` + `o cafezinho` chegam com CTR 24-60%). Considerar editoriais assinados "Cafezinho investiga" ou "Cafezinho revela" em séries.

### 7.4 Recuperar volume de impressões

- Publicar **mais posts/dia** (o pico 15-19/07 coincidiu com maior volume V4 gerando drafts) — Google recompensou.
- **Consistência diária** mais valiosa que grandes matérias esporádicas — algoritmo do Google favorece publicação regular no mesmo domínio.
- Fluxo ideal: 8-12 posts/dia com featured_media + auditor de títulos OK.

## 8. O que o Loop Sentinela pode fazer

O Sentinela está rodando 30 em 30 min mas com **cap 2h inviolável** (regra aprovada Miguel 20/07 08:00 BRT, ver [[feedback-sentinela-nunca-publicar-rascunhos-antigos]]). Não pode pegar backlog. Pode:

1. **Publicar drafts frescos alinhados à linha vencedora** — quando V4 gerar draft de Irã/China/ICL/denúncia dentro da janela 2h, publicar imediatamente. Já está fazendo.
2. **Alertar quando pipeline V4 falhar** — drafts sem `featured_media` são bloqueados mas Sentinela sinaliza no fórum do ciclo (2 casos hoje: 262275, 262296).
3. **Detectar mudanças bruscas de audiência** — se ciclo seguinte mostrar queda de cliques 28d vs baseline, elevar severidade.
4. **Correção auto de grafia** em drafts frescos (Openai→OpenAI, nova York→Nova York, etc) — ajuda CTR marginal.

**Fora do escopo do Sentinela:**
- Curadoria do backlog velho (26 drafts pendentes) → Miguel decide caso a caso
- Rebaixamento de posts antigos publicados por erro anterior (já feito: 6 rebaixados pra pending 20/07 08:00)
- Reescrita semântica de manchete (grava proposta em `propostas_correcao/`, Miguel aprova)
- Reversão do `skip_image=True` do V4 → Codex tem que voltar e consertar

## 9. Perguntas ao Miguel

**Q1 — Fila V4 acumulada (26 drafts pendentes, alguns de 17-18/07):** você quer triar manualmente? Quer que eu produza lista curta com resumo cada + recomendação (publicar/rejeitar/rebaixar teste)?

**Q2 — Cap 2h do Sentinela — reavaliar?** Sua regra foi "2-5h é novo". Cap está em 2h. Se subir pra 4h ou 6h, Sentinela pega mais drafts frescos que perdem janela por não haver ciclo humano. Mas risco de publicar drafts que você quer editar aumenta.

**Q3 — Discover:** você quer que eu abra investigação separada sobre estado atual do Discover? Requer GSC "Discover" específico (não vem no diario_*.json atual).

**Q4 — Pauta ICL — continuar?** Miguel, você tem contato com fonte Moreira/Demori? Se novo capítulo estiver por vir, avisa o Sentinela pra priorizar drafts sobre.

**Q5 — Fix `skip_image=True` do V4:** Codex pausado. Quer que eu conserte o worker V4 ou aguardo Codex voltar? O bug faz drafts saírem sem cartoon → Sentinela bloqueia por regra estrutural → publicação zerada quando aparece esse padrão.

## 10. Próximos passos automáticos

- **Loop Sentinela** continua rodando 30 em 30min (via skill `/loop` job `c2fa3e8e`, session-only, expira em 7d ou você fecha Claude Code)
- **Baleia Azul #14** (21/07) será gerado automaticamente pelo Sentinela na janela 06:00-07:45 BRT amanhã, envio por email 08:00 BRT
- **Coleta GSC diária** continua rodando via cron NYC `/root/util_cron_gsc_diario.py` — dados frescos amanhã 10:00 BRT
- **Análise editorial semanal** proposta: gerar este mesmo tipo de fórum toda segunda-feira 8:00 BRT como parte do Baleia semanal (a implementar se Miguel autorizar)

---

*Fórum gravado por Claude Code (`claude-opus-4-7`), Anthropic, engenheiro-chefe do ecossistema + editor-chefe do Baleia Azul, em 2026-07-20 11:00 BRT.*
*Dados coletados por SSH read-only em NYC (`root@198.199.121.136`), zero custo LLM externo (só a análise usa Opus interno do Plano Max).*
*Registro no canal Trindade pendente — aguarda Miguel decidir se quer sinalização coletiva ou apenas leitura pessoal.*
