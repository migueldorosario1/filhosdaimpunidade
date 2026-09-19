---
name: feedback-wp-meta-update-json-grava-vazio-20260817
description: "NUNCA usar `wp post meta update <id> <key> --format=json < arquivo.json` para escrever _cafezinho_img_check — grava 0 bytes silenciosamente e post cai no gate fail-close. Usar `wp eval \"update_post_meta($id, 'key', file_get_contents('/tmp/arq.json'));\"` (string JSON direta)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

**🚨 REGRA (Claude 17/08/2026 10:57 BRT — bug crítico auto-diagnosticado):**

Nunca gravar `_cafezinho_img_check` (ou qualquer meta protegida `_*`) via:
```bash
wp post meta update <post_id> <key> --format=json < /tmp/arq.json  # ❌ NÃO — grava 0 bytes
```
Mesmo com `Success: Updated custom field` no output, o valor persiste como **string vazia** na tabela `wp_postmeta`. O warning `PHP Warning: strlen() expects parameter 1 to be string, array given in class-wp-block-parser.php` é o sintoma — WP interpretou o JSON como array e algum filtro Gutenberg limpou.

**Método correto (validado 17/08 10:55):**
```bash
scp /tmp/recibo_XXX.json cafezinho-wp:/tmp/
ssh cafezinho-wp 'cd /var/www/ocafezinho && wp eval "update_post_meta(XXX, \"_cafezinho_img_check\", file_get_contents(\"/tmp/recibo_XXX.json\"));" --allow-root'
```
Valida com:
```bash
wp db query 'SELECT LENGTH(meta_value) FROM wp_postmeta WHERE post_id=XXX AND meta_key="_cafezinho_img_check"'
# Deve retornar >1000 bytes, não 0
```
Confirma que o gate reconhece:
```bash
wp eval 'require_once WPMU_PLUGIN_DIR."/cafezinho-gate-imagem-checada.php"; echo cafezinho_gate_img_tem_checagem(XXX)?"PASS":"FAIL";'
# Deve retornar PASS
```

**Why:** O gate fail-close `cafezinho-gate-imagem-checada.php` (ZCode/Qwen 3.8 16/08 17:58) roda `cafezinho_gate_img_tem_checagem` que:
1. `get_post_meta($id, '_cafezinho_img_check', true)` — se `empty()` → busca `_cafezinho_img_isenta` (isenção humana)
2. Se meta é array — verifica `!empty($check['ok'])`
3. Se string — tenta `json_decode` e verifica `!empty($dec['ok'])`
4. String vazia = `empty() == true` → **cai para busca de isenção** que também não existe → **PASS=false → post rebaixado a pending 52 segundos após publish agendado**

**Incidente 17/08:** eu gravei recibos ok:true para 266238 (dengue), 266239 (China IA), 266244 (TRE) via `wp post meta update --format=json`. Todos os 3 ficaram 0 bytes. 266238 tentou publicar 10:15:00 → gate rebaixou 10:15:52 → **descoberto por mim no ciclo 10:46 quando vi o post ainda como `pending`**. Corrigido via `wp eval + file_get_contents`; validado (recibo=OK_JSON_STR, gate=PASS); reagendado para 12:15. 266239 e 266244 corrigidos preventivamente antes de 11:00/11:45.

**How to apply:** Sempre depois de gravar `_cafezinho_img_check`, validar com o script de 2 linhas acima. Se `LENGTH(meta_value)=0`, corrigir imediatamente. Nunca confiar no output `Success: Updated custom field` — pode ser vazio silencioso.

**Investigação futura:** entender por que Gutenberg block parser está sendo chamado num `wp post meta update` (via CLI, sem editor). Provavelmente algum hook `updated_post_meta` ou `pre_update_post_meta` filtra e limpa arrays. Escalar ZCode se acontecer com outros metas protegidas.

Ver também: [[feedback-contrato-integridade-imagens-v1-homologado-20260816]] (formato do recibo), [[feedback-hotlink-vs-upload-local-verificar-url-antes-de-rotular-20260817]] (validação pós-gravação em geral).
