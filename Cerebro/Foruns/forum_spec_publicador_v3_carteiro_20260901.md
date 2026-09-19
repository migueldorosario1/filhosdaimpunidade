# 📮 SPEC — PUBLICADOR v3 "O CARTEIRO" (Art. 2 do Contrato da Casa v3)

> Rascunho ZM p/ mesa das 22:00 (01/09/2026) — Miguel lapida e promulga. Alinhado ao plano do DSC (`plano_trabalho_contrato_v3_lancamento_v42_20260901.md`), ao parecer DSC 19:43 e às lições do dia (268553, CL-011, face 2 do quirk).

## 0. Berço e princípio
- Nasce do Contrato v3 como **primeiro cidadão**: primeiro a lei, o cidadão já conforme. Substitui o Publicador v2 na promulgação (v2 congela como rollback).
- **Princípio: o carteiro não lê o recado, ele CARIMBA.** Publica só com autorização assinada verificável; na dúvida, **fail-close** (não publica, registra e segue a fila).

## 1. Gate de publicação — 3 travas em SÉRIE, em TODAS as vias
*(vias: esteira V4.x · resgate de slot · DS YouTube · futuro V4.2 — robô-fonte 5801 JAMAIS automático)*

**T1 — REF ASSINADA (Emenda E2):**
- Refs válidas: `CL-NNN` · `CM-NNN` · `ordem-Miguel` com **registro datado na ponte** (nunca "ordem verbal" sem carimbo) · `AL-NNN` **só** com delegação explícita da CL citada na própria AL. `GM-` FORA (parecer DSC).
- Cada ref carrega **hash SHA-256** (título + ID do post no momento da decisão) + **TTL 30 min** — expirou, revalida com 1 linha nova (não reusa carimbo velho).
- Regex ANTI-CONDICIONAL: só publica com "TEXTO APROVADO—publique INCONDICIONAL"; "condicionado / aguardar / revisar / depois de" = **BLOQUEIA** (lição 268553: 23 min no ar lendo condicional como consenso).

**T2 — MÍDIA COMPLETA (a capa é parte do item, não retoque):**
- Featured image presente + **legenda pt-BR** + **crédito/licença** + **alt** + `_cafezinho_img_check` válido.
- CC BY / CC BY-SA **sem crédito = inelegível** (CL-011 vira código). Institucional genérica antiga = inelegível (capítulo IMAGENS nível 2).

**T3 — SANIDADE DO POST:**
- Autor mapeado (5470 esteira / 5801 DS YouTube — nunca automático / humano nominado); título na régua EMU-2 (1 frase, sem sigla, cargo p/ desconhecido); categorias; **`post_date=now`, NUNCA futuro** (face 2 do quirk — 5 casos/24h); dedup (nada igual no ar nas últimas 24h).

## 2. Fluxo (ciclo 30 min, flock)
scan fila → T1 → T2 → T3 → publish → **PROVA** (REST: permalink REAL por ID — nunca chutar slug — + cabeçalho X-WP-Total) → **readback ≤ 5 min** (confere título/autor/data publicada) → registro de 1 linha (ref + hora + permalink) no canal do Publicador → **health-check E5 a cada 15 min** (gate respondendo? fila andando? alerta 10 min se não).

## 3. Canário (antes de produção — ZERO publicação de teste, regra do Miguel)
3 casos, todos em **draft/private**: (a) ref condicional ambígua → tem que BLOQUEAR; (b) mídia CC sem crédito → tem que BLOQUEAR; (c) ref com TTL expirado → tem que revalidar/não publicar. Critério de aceite: 3/3 bloqueando certo.

## 4. Compatibilidade V4.2 + Fase 0 (dono ZM)
- Campos prontos desde o nascimento: `_v42_fc` (evolução do `_v41_fc`), `zizi_job_id`, licença/crédito **capturados na origem**, dedup de tese já na captura, logs legíveis pelas R1/R2.
- **Fase 0 dispara na promulgação**: integrar `featured_image_runtime.py` + `media_vision_providers.py` (NYC) ao ciclo do V4.1 — esteira autossuficiente em capa, matando a dependência que derrubou 11h em 29/08. **Esteira NUNCA para.**

## 5. Freios e emergência (Emenda E1 — emergência blindada)
- Resgate de slot furado >60 min só com **consenso antecipado da CL**; freio **3 resgates/dia**; retry com backoff 2/4/8s + jitter; hardstop US$3/dia (freio estado em json, nunca loop).
- **Isenção de autor humano** (risco apontado pelo DSC): texto do Miguel/colunista não passa T1 (não exige ref de robô — a assinatura é dele), mantém T2/T3.

## 6. Implantação e rollback
- Roda em `standby_contrato` até a promulgação (mu-plugin já endurece o WP hoje).
- Deploy com ritual da casa: backup `.bak_pre_*` → `py_compile` **na Tencent (Python 3.12)** → restart → prova HTTP → linha no monitor.
- **Rollback = 1 arquivo** (v2 congelado). Toda decisão de gate loga linha `GATE:` no topo do bloco (padrão da ouvidoria).

## 7. Aceite
Spec assinada pelo ZM na mesa das 22:00; implementação começa após promulgação + Fase 0.

— ZCode/GLM-5.3 · 20260901 20:25:00 BRT
