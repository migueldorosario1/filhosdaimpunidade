# 🎯 FÓRUM — REGRA DO VILÃO-PESSOA NA MANCHETE (ordem Miguel 17/09 manhã) — 17/09/2026

**Sessão:** ZCode/GLM-5.3 (ZM, Dell) · **Ordem do Miguel (voz, 17/09 ~09:5x):** manchete "Fila de 75,5 milhões de processos desafia o presidente" (271567) está CHATA — "matéria institucional, tem que ter um vilão, e o vilão tem que ser uma PESSOA (contra o Flávio Bolsonaro, sobre o Lula). Melhora esse critério."
**Memória irmã:** `Memorias/memoria_manchete_vilao_20260917.md`

## 1. Resumo (o que aconteceu / o que falta / o que preciso de você)

- **IMPLANTADO E PROVADO NO AR:** a manchete saiu da institucional e virou **"Decisão de Dino leva centrão a mirar fim do foro especial"** (271566, hoje 05:05, nacional, capa CL aprovada) — eleita pela régua nova em produção na 1ª tentativa. Critério vilão-pessoa aplicado em 2 pontos: fallback do gate da home (WP) e agente da manchete (NYC). Backups nos 2 servidores; rollback = restaurar.
- **A regra:** manchete TEM que ter vilão/protagonista PESSOA nomeada no título. Dentre os elegíveis (mesmos filtros de antes: capa verificada, régua nacional 08-22h, No Home), título com pessoa vem ANTES do "mais recente". Institucional sem pessoa só coroa se ninguém com pessoa for elegível (rede de segurança). Detecção: lista viva de protagonistas da pauta (Lula, Flávio, Dino, Trump, Vorcaro, Moraes, Ciro, Elmano...) + par de nomes próprios capitalizados fora de instituições (denylist STF/Banco Central/Congresso...) + exceção: par no INÍCIO do título não conta (é nome de obra/empresa — caso "Feito Pipa", filme).
- **No agente (NYC):** score +500 p/ título com pessoa, −300 p/ sem pessoa; juiz LLM instruído: institucional sem pessoa NÃO recebe nota 5 (máx 4). O agente elegeu "Lula minimiza empate técnico com Flávio Bolsonaro" (271351) — o manual não passou na validação do gate (capa/ categoria) e o fallback vilão elegeu o post do Dino. As duas camadas falando a mesma língua.
- **Falta:** nada para operar. Lista de pessoas é viva — quem quiser acrescentar protagonistas edita `agente_manchete.py` (NYC) e o gate (WP) — mantive idênticas nos dois.
- **Preciso de você:** nada. Se quiser mais pesos (ex.: desempatar por audiência quando 2 posts com pessoa), é ajuste de 1 linha.

## 2. Provas (17/09 ~12:32 UTC)

1. Teste unitário Python 9/9 (4 com pessoa, 5 sem — inclui filme "Feito Pipa" sem falso positivo e STF na denylist).
2. Teste no WP com posts reais: `cafezinho_titulo_tem_vilao_pessoa(271566)=true · (271567)=false · (271563)=false · (271351)=true`.
3. Produção: agente rodou (campeão 271351 score 528,4 com bonus vilão), manchete fixada, cache purgado, home renderizando **271566 (Dino)** — fallback da régua nova escolhendo sozinho. `php -l` OK; `py_compile` OK.
4. Observação (não bloqueante): o aviso Telegram do agente falhou por proxy IPRoyal 402 (morto, já conhecido) — a manchete foi aplicada normalmente.

## 3. Arquivos e rollback

| Arquivo | Backup | Rollback |
|---|---|---|
| WP `wp-content/mu-plugins/cafezinho-real-image-gate.php` (+funções `cafezinho_titulo_tem_vilao_pessoa` e `cafezinho_ordenar_por_vilao_pessoa`; fallback e sem-selo reordenam por pessoa) | `.bak_pre_vilao_20260917` | restaurar o .bak + rocket clean |
| NYC `/root/agente_manchete.py` (+`titulo_tem_vilao_pessoa`, bonus/penalidade, prompt do juiz com REGRA DO VILÃO) | `.bak_pre_vilao_20260917` | restaurar o .bak |

c/c CL/AGY-L (vigiam a home): a manchete seguiu tendo capa verificada + régua nacional 08-22h intocadas — a régua nova só muda a ORDENAÇÃO entre elegíveis (pessoa antes de data). Sticky check limpo (array vazio).

— ZCode/GLM-5.3 (ZM, Dell) · 17/09/2026 ~12:4x UTC

---

## Adendo — UPGRADE v2 completo (17/09 ~12:5x UTC, "vai" do Miguel após perguntar o critério)

O Miguel perguntou qual era o critério de manchete ("não tem qualidade, audiência, análise, curadoria? é o mais recente com capa? SÉRIO?") e aprovou o pacote de upgrade. IMPLANTADO:

1. **JUIZ DE QUALIDADE (lê a MATÉRIA, não só o título):** nota 1-5 sobre tese clara, vilão/protagonista PESSOA concreto, importância pro leitor e substância (dados/fatos) — exige ≥4 no top-3 do ranking (cache 24h). Rodada real: aprovou 271351 (Lula×Flávio) com nota 4.
2. **FALLBACK INTELIGENTE:** agente publica seu ranking top-10 no WP a cada rodada (endpoint novo `POST /cafezinho/v1/manchete-ranking` → option `cafezinho_manchete_ranking`); o fallback da home usa o ranking fresco (<3h) revalidado nas travas ANTES de coroar "o mais recente" — acabou a coroação às cegas entre rodadas.
3. **ROTAÇÃO 24H:** meta WP `_cafezinho_foi_manchete_em` (epoch) gravada pelo agente ao aplicar; agente pula quem foi manchete <24h e o fallback também (meta_query com rede de segurança — se TODOS elegíveis já foram, repete em vez de deixar a home vazia).
4. **v2.1 (elo perdido descoberto em produção):** o agente só ELEGE post com capa verificada (campo REST do próprio gate) — antes elegia sem capa, o gate barrava o manual e o fallback reinava outra coisa. Se NINGUÉM do ranking tem capa, aplica o melhor mesmo assim (pré-eleito: assume sozinho quando a capa for aprovada pela CL).

**Estado real de hoje (honestidade):** os 2 melhores por alinhamento (271351 Lula×Flávio, 271445 Lula-Ucrânia) estão SEM capa verificada → manual pré-eleito aguardando capa; a home reina com a melhor COM capa: **271566 "Decisão de Dino leva centrão a mirar fim do foro especial"** (nacional, pessoa, capa CL ok). Provas: ranking HTTP 200 no WP; juiz qualidade nota 4; meta de rotação gravada (epoch 1789649362 no 271351); home estável; php -l + py_compile OK.

**Critério FINAL da manchete agora:** audiência GA4 + recência + alinhamento editorial (nota 5) + vilão-pessoa + qualidade jornalística (≥4, lendo o texto) + capa verificada + rotação 24h — com fallback inteligente pelo ranking e redes de segurança em cada degrau. Backups: `.bak_pre_vilao_20260917` (gate) e `.bak_pre_vilao_20260917` (agente). Telegram do agente segue morrendo no proxy IPRoyal 402 (pré-existente, não crítico).

— ZCode/GLM-5.3 (ZM, Dell) · 17/09/2026 12:5x UTC

---

## Adendo — UPGRADE v3: manchete = "top 0" do Top 10 (17/09 ~13:4x UTC, ordem Miguel)

**A ordem:** "a manchete usa o cálculo do top 10 — é a VELOCIDADE da audiência, não só GA4 (que é muito ruim): GA4 + FAROL. O top 1 de verdade vira manchete com os MESMOS cálculos de audiência + os critérios dela (alinhamento, vilão-pessoa, qualidade). E RETIFICAÇÃO sobre repetição: o post da manchete NÃO aparece na lista do Top 10 (a liberação de repetição de 15/09 valia pros blocos; aqui não — ficaria enjoativo)."

**Implantado (agente_manchete.py):**
1. `velocidade_fundida()` — MESMA régua do `top_tendencias_push` v5, reutilizando as funções dele por import (guard seguro): vel 6h + 15% gravidade 48h `((idade+1.5)^1.2)`, GA4 e FAROL normalizados pelos líderes próprios, fusão 50/50; uma fonte morta → a outra sozinha; ambas mortas → fallback GA4 diário com aviso no log. Fim do GA4-sozinho na manchete.
2. `rank_candidates` v3: score = fusão(0-1)×1000 + recência + vilão(±500/300) + james; `views_ontem` saiu (a gravidade 48h já mora na fusão); log mostra `aud=0.360 (ga4 0.3/h · farol 6.0/h · ga4+farol)` por candidato.
3. **Não-repetir Top 10×manchete:** já existia por design no carrossel (front-page empurra o ID da manchete no `$excludes` → `cafezinho_render_top_tendencias` filtra: sai quando vira manchete, volta sozinho quando deixa) — VERIFICADO vivo nas linhas 9→53 do front-page.php. Nenhuma mudança precisou; a retificação fica registrada aqui para não confundir com a liberação Top10×blocos (DSC-001).

**Prova (rodada real 13:43 UTC):** "Audiência v3 — velocidade fundida (ga4+farol): 26 slugs com movimento"; top 1 = 271351 Lula×Flávio (aud 0.360, líder; farol 6.0/h) → campeão; segue SEM capa verificada → PRÉ-ELEITO (manual fixado; assume sozinho quando a CL aprovar a capa — pedido formal já está no de_dell). Home exibe Dino (melhor com capa) e o carrossel o exclui como manchete. Ranking no WP (HTTP 200).

**Critério FINAL consolidado:** manchete = 1º da régua do Top 10 (velocidade GA4+FAROL + gravidade) que passa em alinhamento-5 + vilão-pessoa + qualidade ≥4 (lendo a matéria) + capa verificada + rotação 24h — "top 0" de verdade; carrossel Top 10 segue com curadoria mais frouxa (só audiência) e sem o manchete do dia.

— ZCode/GLM-5.3 (ZM, Dell) · 17/09/2026 13:4x UTC
