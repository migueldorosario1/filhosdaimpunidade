---
name: feedback-gate-img-check-valida-filename-e-title-attachment-20260822
description: "Gate _cafezinho_img_check é AUTO-DECLARADO — bug 267037 (22/08/2026 08:28 BRT) AGY-LAURA assinou ok:true com caption falsa \"aplicação de doses\" quando mídia 267038 era foto Ricardo Barros/Temer 2016-2018. Filename enganoso `campanha-vacinacao-brasil-sus.jpg` mas post_title attachment revelava \"Ministro da Saúde faz balanço da vacinação da febre amarela\". Precisa validação cruzada 3 fontes + Grok imagem ANTES do publish + blacklist figuras datadas."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1224239f-8425-4baf-9da7-68a0f08ae109
---

## Incidente-raiz 267037 (22/08/2026)

**Fato:** Miguel corrigiu manualmente ~08:58 BRT o post 267037 "Dia D de vacinação mobiliza postos para menores de 15 anos" que havia sido publicado 08:28 pela AGY-LAURA com foto de **Ricardo Barros** (ministro da saúde do Temer, 2016-2018) como se fosse cena de aplicação de vacina em posto SUS.

**Timeline:**
- 08:28:00 AGY-LAURA assinou recibo `_cafezinho_img_check ok:true` com `media_id:267038`, `caption:"Aplicação de doses em unidade SUS"` e `alt_text:"Profissional de saúde aplicando dose"` — 100% FALSO
- 08:28:29 publish 267037 com capa 267038
- 08:42 Grok Laura (única com `read_imagem:SIM`) detectou: "267038 é Ricardo Barros (ABr 2014), não aplicação de doses" (GL-015) — 14min TARDE
- ~08:58 Miguel corrigiu (mídia 267040 substituiu)

**Raiz técnica dupla:**

1. **AGY-LAURA confiou em filename, não em conteúdo:**
   - Mídia 267038 filename: `campanha-vacinacao-brasil-sus.jpg` (enganoso)
   - Mídia 267038 `post_title`: **"Ministro da Saúde faz balanço da vacinação da febre amarela"** (denuncia)
   - AGY leu filename, escreveu caption inventada sem cotejar post_title do attachment

2. **Gate `_cafezinho_img_check` é auto-declarado:**
   - Verifica apenas se existe recibo `ok:true` — confia cegamente no que o agente aplicador declara
   - Sem verificação cruzada filename × post_title attachment × imagem real × contexto do post
   - Grok Laura é o único com visão real, mas entra DEPOIS do publish (cadência 1h)
   - Meu papel CM ("gate final") também não olha a mídia — confiei no recibo AGY sob Consenso Duplo

## Correção estrutural — 5 mudanças propostas

**Why:** Bug 267037 é sintomático — recibo auto-declarado + filename enganoso é combinação recorrente que passa por todos os gates atuais. Já aconteceu antes com capa fm=0 (Grok flagrou), diferença é que aqui tinha capa mas ERRADA.

**How to apply:**

1. **Gate `_cafezinho_img_check` valida 3 fontes concordantes** antes de aceitar `ok:true`:
   - `wp_posts.post_title` do attachment
   - filename (guid)
   - campo `caption`/`alt_text` declarado pelo agente
   - Regra: se post_title do attachment cita **figura pública nomeada** (Ministro X, Presidente Y, Deputado Z, Governador W) mas post é sobre outro tema (política eleitoral atual, campanha vacinal do dia) → **FAIL HARD**, não publica

2. **Idade do attachment vs breaking news:**
   - Se `attachment.post_date > 6 meses` E post é breaking news do dia → exige verificação humana OU Grok visão bloqueante
   - Ex: attachment Ricardo Barros importado em 2016 sendo usado em campanha vacinal 2026 = red flag automático

3. **Grok Laura entra ANTES do publish, não depois:**
   - Fluxo atual: V4 draft → AGY aplica capa → publish → Grok valida (tarde) → CM corrige
   - Fluxo proposto: V4 draft → AGY aplica capa → **Grok valida imagem×texto (bloqueante)** → CM libera publish
   - Cadência Grok subir de 1h pra 15min ou trigger-por-evento (assim que AGY grava recibo, Grok recebe ping)

4. **CM (eu) obrigado a ler `wp post get <media_id>` antes de aprovar publish:**
   - Não confio só no recibo — puxo `post_title` + `post_date` do attachment + comparo com contexto do post
   - Se filename e post_title do attachment divergem, ping pro Grok validar imagem

5. **Blacklist figuras políticas datadas em attachments recentes:**
   - Ricardo Barros, Osmar Terra, Luiz Henrique Mandetta, Nelson Teich, Eduardo Pazuello, Marcelo Queiroga (ex-ministros saúde Temer/Bolsonaro)
   - Se `wp_posts.post_title` do attachment cita esses nomes E post atual é breaking >2024 → red flag automático
   - Lista pode expandir por vertical (ex-governadores, ex-presidentes, ex-ministros datados)

**Detalhes:** [[project-correcao-estrutural-gate-imagem-pos-267037-20260822]]
