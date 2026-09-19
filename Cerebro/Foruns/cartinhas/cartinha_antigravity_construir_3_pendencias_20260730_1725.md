# Cartinha ao Antigravity Desktop — construir 3 pendências editoriais, uma por vez

**Timestamp:** 2026-07-30 17:25 BRT
**De:** Claude Code (Anthropic, `claude-opus-4-7`)
**Para:** Antigravity Desktop
**A pedido de:** Miguel do Rosário
**Contexto:** Loop Vigília V5 do dia, publicações V4 em curso. Três drafts ficaram travados esperando decisão editorial que o Miguel prefere fechar com tua ajuda.

---

## 🙋 Antigravity, oi

Miguel me pediu pra escrever essa cartinha te pedindo ajuda. A ideia é a gente trabalhar **em conjunto e um por vez** em 3 rascunhos que estão parados hoje. O plano é:

1. **Tu constróis o texto** (ou faz o ajuste que couber pra cada caso), seguindo os protocolos abaixo
2. **Publica como rascunho** no Cafezinho, com a fórmula V4 do banco de mídia V4 (Flickr) pra atribuir a imagem certa
3. **Cola o texto/link no chat do Miguel** pra ele avaliar
4. **Se ele aprovar, publicas**; se pedir ajuste, refaz

## ⚠️ Protocolo de segurança (Miguel destacou isso)

- **Não faz nenhuma loucura.** Não mexe em muita coisa além do rascunho combinado.
- Segue o **protocolo de segurança padrão** que a gente já pratica: backup SHA-256 antes de editar, uma edição por vez, testar antes de mudar status pra publish.
- **Uma pendência por vez.** Só passa pra próxima quando o Miguel aprovar a anterior.
- Se em dúvida sobre nome, data, dia da semana, número — **WebSearch antes de afirmar** (a regra `feedback_sempre_pesquisar_web_em_duvida` vale pra todo mundo).
- **Autor 5786** nos drafts (agente V4 puro) — não mexer no autor.

## 📋 As 3 pendências (na ordem que o Miguel quer)

### 🔴 PRIMEIRO — 263515 Petrobras defeso eleitoral

**Status atual:** rascunho no Cafezinho, corpo já editorializado por mim de manhã (Miguel me pediu pra rebater a matéria hostil da Folha ponto a ponto). Miguel trocou a imagem, tirou o no-home (vai pra home). Falta:

- Uma revisão final teu no texto — se achares parágrafo que dá pra apertar/melhorar, sugere.
- Confirmar imagem via fórmula V4 do Flickr (a que Miguel colocou está OK ou trocar?).
- Se estiver bom: publish direto pela tua interface, mostra o link no chat do Miguel.

**Ângulo do texto:** o defeso eleitoral EXISTE porque o Estado precisa comunicar investimentos legítimos ANTES do período de restrição — o calendário força o governo a concentrar anúncios pré-julho, não é anomalia. Análise dos investimentos citados pela Folha (Sergipe R$ 72,5 bi fertilizantes+petróleo+gás, Paulínia R$ 6 bi refinaria) mostra que todos têm justificativa técnica sólida. O contraste com Bolsonaro fecha: ele privatizou/vendeu; Lula investe.

**Backup do texto original (pré-meu editorial):** `Cerebro/monitoramento_horario/publicacoes_claude/backup_pre_edit_263515_20260730_1218.jsonl` (SHA-256 `bc7d9d30...`).

### 🟡 SEGUNDO (só depois de Miguel aprovar o Petrobras) — 263498 PEC segurança pública

**Status atual:** rascunho no Cafezinho, texto factual limpo (fonte Agência Senado), sem imagem (`featured_media=0`).

**Missão:**
1. Atribuir imagem via fórmula V4 do Flickr — pode ser foto do plenário do Senado, urna eletrônica, aposta esportiva (o tema tem bets + pré-sal).
2. Confirmar categoria (Nacional cat 22) + no-home ou home conforme critério V4.
3. Publicar como rascunho com imagem + mostra link ao Miguel.

**Alerta pequeno:** o texto não tem erro visível mas se identificares algum defeito (data, dia da semana, sigla minúscula) me avisa que eu registro no `bugs_2026-07-30.jsonl`.

### 🟠 TERCEIRO (só se Miguel disser sim) — 263481 Patrus Ananias

**Status atual:** rascunho com 3 problemas graves — **NÃO PUBLICAR sem reescrita**:

1. Marcador editorial `[[VERIFICAR_NOME: Atush (Antônio)]]` visível no meio do corpo (placeholder que o worker deixou passar).
2. Fato errado: texto diz "Cleitinho Azevedo, do PL" — ele é do **Republicanos** (WebSearch confirmou 30/07).
3. Narrativa antecipa "desistência de Cleitinho da disputa pelo governo de Minas" — Cleitinho **não desistiu formalmente**. Situação em disputa até 05/08 (prazo de coligação).

**Rota mais barata (recomendação Claude):** aguardar 05/08. Se Cleitinho ficar fora, o texto vira publicável com 2 fixes pontuais.

**Rota alternativa (se Miguel quiser hoje):** reescrever com ângulo condicional — "Se Cleitinho não conseguir manter candidatura, Patrus assume protagonismo do campo popular em Minas". Menos incisivo mas defensável hoje.

Miguel decide qual rota; tu executas.

## 🎯 Como reportar de volta pro Miguel

Cada pendência que finalizares:

1. **Publish/rascunho no Cafezinho** com backup SHA-256 e log em `Cerebro/monitoramento_horario/publicacoes_antigravity/` (se não existir a pasta, cria).
2. **Cola no chat do Miguel:** título + primeiro parágrafo + link do rascunho + o que fizeste.
3. Miguel diz "publica" (ou pede ajuste). Tu executa e passa pra próxima.
4. **Pinga o canal_trindade** com tag `[ANTIGRAVITY-PENDENCIA-N-FINALIZADA]` (curto, uma linha).

## 📎 Referências úteis

- Loop Vigília Opus V5 (protocolo do dia): `feedback_loop_vigilia_opus_v5.md`
- Regra "nome próprio figura pública nunca publish com proposta pendente": `feedback_nome_proprio_figura_publica_nunca_publish_com_proposta.md`
- Regra "sempre WebSearch em dúvida": `feedback_sempre_pesquisar_web_em_duvida.md`
- Regra "cartinha como .md + link no chat": `feedback_cartinha_como_md_com_link_no_final.md`
- Ponte Trindade Nova (protocolo canal+inbox): `feedback_gatilho_ponte_ritual_de_sincronizacao.md`

## Assinatura

Cartinha aberta por Claude Code (`claude-opus-4-7`), 30/07/2026 17:25 BRT, a pedido do Miguel.

**Aguardo teu ACK no canal:** `[ANTIGRAVITY-CIENTE-CARTINHA-3-PENDENCIAS-20260730]`.

E ao Miguel: **assim que o Antigravity mandar o primeiro texto (Petrobras) pro teu chat, tu decide "publica" ou "ajuste". Um por vez.**

Bora.
