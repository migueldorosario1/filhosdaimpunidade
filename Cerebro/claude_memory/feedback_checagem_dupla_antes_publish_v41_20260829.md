---
name: feedback-checagem-dupla-antes-publish-v41-20260829
description: "Antes de publicar QUALQUER draft, checagem dupla obrigatória: _v4_versao=4.1 + frescor <72h + thumb + img_check APROVADA + dedup + Regional=pesquisa/bastidor. Nunca publicar autor 5786 sem v4_versao (legacy)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9597853d-470e-434b-a836-f9a921a9a387
---

**REGRA:** Antes de rodar `wp post update <ID> --post_status=publish`, aplicar CHECAGEM DUPLA por meta obrigatória:
1. **`_v4_versao` = "4.1"** (OBRIGATÓRIO). Se AUSENTE ou diferente = draft LEGACY V4 antigo → **NÃO PUBLICA**. Ordem Miguel 24/08: "só V4.1".
2. **`post_date` dentro de 72h** (frescor). Se >72h = velharia → aplicar meta `_cafezinho_descartado_velharia` + cat no-home 20699.
3. **`_thumbnail_id`** preenchido (não vazio). Sem capa = fail §86 v1.1.0 HTTP 400. Não publica.
4. **`_cafezinho_img_check`** com `"veredicto":"APROVADA"` (juiz visão passou). Se AUSENTE ou reprovada = não publica.
5. **Dedup 72h limpo**: `wp db query "SELECT ID FROM wp_posts WHERE post_status='publish' AND post_date >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND post_title LIKE '%<termo>%' AND ID != <ID>"`. Se hit = canibal, meta `_cafezinho_canibalizado`.
6. **Regional** (cats 4986 + estaduais): só pesquisa eleitoral OU bastidor de disputa por poder. Burocracia contábil e figura desconhecida BANIDAS.

**Se QUALQUER 1 falhar → NÃO PUBLICA.** Descarta, segura, ou reporta ao dono resolver.

**Why:** Miguel ordenou 29/08 13:55 "revisa bem. não publica velharia. prioriza frescor. faz checagem dupla antes de subir qq post". Contexto: hoje 29/08 13:29 publiquei 267770 e 267743 (autor 5786, sem `_v4_versao`, cat Regional) — sem checar a meta `_v4_versao=4.1`. Eram LEGACY V4 regional que Miguel mandou parar 24/08 ("só V4.1"). O pipeline `/etc/cron.d/v4_regional` escapou da faxina (auditoria ZCode 26/08). Publiquei contra ordem. Precisei aplicar cat no-home 20699 + meta `_cafezinho_recolhido_legacy_pos_publish` pra corrigir sem perder SEO. Também tinha caído em erro raiz: assumi que "autor 5786 = V4" quando na verdade V4.1 usa **autor 5470** e escreve como `draft` (não `pending`). Meta `_v4_versao=4.1` é a ÚNICA distinção confiável.

**How to apply:**
1. **Checagem manual antes de todo publish** (helper `checagem_dupla.sh` a criar):
   ```bash
   ID=<post_id>
   ssh cafezinho-wp "cd /var/www/ocafezinho && \
     v41=\$(wp post meta get \$ID _v4_versao --allow-root 2>/dev/null); \
     thumb=\$(wp post meta get \$ID _thumbnail_id --allow-root 2>/dev/null); \
     img=\$(wp post meta get \$ID _cafezinho_img_check --allow-root 2>/dev/null | grep -oE '\"veredicto\":\"[A-Z]*\"'); \
     age=\$(wp post get \$ID --field=post_date --allow-root | xargs -I{} date -d '{}' +%s | awk -v n=\$(date +%s) '{print int((n-\$1)/3600)}'); \
     [ \"\$v41\" = \"4.1\" ] && [ -n \"\$thumb\" ] && echo \"\$img\" | grep -q APROVADA && [ \"\$age\" -lt 72 ] && echo GO || echo FAIL"
   ```
2. **Publish só se todas as 6 checagens PASS.** V4.1 é automático — mas automático DENTRO dos gates, não fora.
3. **Se draft é V4 legacy** (autor 5786 sem `_v4_versao`): NÃO publica. Aplicar `_cafezinho_descartado_legacy_v4` + cat no-home se já publicou por engano.
4. **Fila V4.1 real:** buscar por `wp post list --post_status=draft --meta_key=_v4_versao --meta_value=4.1 ...` — NÃO por `--post_status=pending` (V4.1 fica em draft) nem por autor. Meta é fonte da verdade.
5. **Confusão fila pending vs draft:** V4.1 gera drafts (autor 5470, status `draft`). V4 legacy gera pending (autor 5786, status `pending`). Nunca misturar.
6. **Regional específico**: além do `_v4_versao=4.1`, checar categoria — se cat 4986 (Regional) + tema não é pesquisa eleitoral nem bastidor de disputa por poder → descartar (regra Miguel 22/08).
7. **Registro obrigatório pós-publish**: meta `_cafezinho_publicado_por_cm` com JSON `{ts, agente, gates_pass:{v41,thumb,img,age,dedup,regional_ok}}` — auditoria futura consegue provar checagem foi feita.

Meta lição: erro repetido é reincidência de Emenda TENSÃO 26/08 e da Emenda Gate Visível 18/08. Esta memória tem que barrar publish futuro que não passe pelas 6 checagens. Se detectar-me publicando sem checar → PARA.

Ver também: [[feedback-tensao-constante-autoaprendizado-memoria-bugs-20260826]] · [[feedback-alerta-ponte-cafezinho-telegram-autocura-v4-20260829]] · [[feedback-ponte-canonica-cerebro-miguel-20260829]] · [[feedback-defasagem-temporal-e-saturacao-tema-20260820]] · [[feedback-regional-pesquisa-eleitoral-ou-bastidor-20260822]] · [[feedback-gate-img-check-valida-filename-e-title-attachment-20260822]] (Gate 267037).
