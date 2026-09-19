# Memória técnica — EMENDA 11 (capa IA em tecnologia) + capa do post 267719 (LNCC/Huawei)

**Data:** 2026-08-26 11:36–12:00 BRT · **Agente:** ZCode/Kimi K3 · **Par:** `Foruns/forum_emenda11_capa_ia_tecnologia_lncc_20260826.md`

## Contexto
Post 267719 publicado 26/08 07:19 sem `featured_media` (cats 5087/2403/30; autor 5470). Ordem Miguel ~11:35: tecnologia pode ter imagem IA sem texto interno; comunicar ao loop, ao Cérebro e a todos.

## Comandos/arquivos tocados (log completo)

1. **Descoberta:** REST `wp-json/wp/v2/posts?slug=lncc-assume-supercomputador-em-pacote-de-ia-com-huawei` → id 267719, featured_media 0. Credencial: conta "Redacao nova" (`WP_USER_CAFEZINHO`/`WP_PASS_CAFEZINHO` do `.env.unificado`).
2. **Geração (NYC):** `cd /root && . chaves.sh && . .env` + `generate_editorial_image({'titulo':..., 'resumo':..., 'secao':'tecnologia'}, caminho_download='/tmp/capa_lncc_267719.jpg')`. Log: banco real tentado (7 candidatas Flickr reprovadas pelo Tribunal Visual) → prompt por gpt-5.5 (roteador; gemini-3.5-flash 400 location, gpt-4o sem módulo openai) → **flux-pro**. Resultado: url fal.media + `/tmp/capa_lncc_267719.jpg`.
3. **Inspeção visual:** scp para local + leitura da imagem — sem texto, sem rostos, tese do controle (chave) presente. Aprovada.
4. **Upload (NYC):** `upload_imagem_wp.upload_image_to_wp('/tmp/capa_lncc_267719.jpg', title=..., wp_url=WP_SITE, wp_user=..., wp_pass=..., legenda_externa='Ilustração editorial sobre o LNCC assumindo supercomputador no pacote de IA com Huawei. (Ilustração: Cafezinho / Flux Pro — gerada por IA)')` → **media_id 267763**; URL pública `https://www.ocafezinho.com/wp-content/uploads/2026/08/capa-lncc-267719.jpg`.
5. **WP (ssh cafezinho-wp, `--path=/var/www/ocafezinho` — o cwd default /root NÃO é WP):**
   - `wp post meta update 267719 _cafezinho_img_check '{"ok":true,"ts":...,"via":"zcode_kimi_k3_emenda11","generator":"flux-pro","image_kind":"ia_gerada","media_id":267763}'` (ANTES do thumbnail — gate `cafezinho-gate-visao-capa.php` exige media_id casado)
   - `wp post meta update 267719 _thumbnail_id 267763` → readback 267763 ✅
   - `wp eval 'wp_update_post(["ID"=>267719]);'` (reindex Yoast og:image/JSON-LD)
   - `wp cache flush` (Redis)
6. **Cache Rocket — GOTCHA NOVO:** os arquivos de página são `index-https.html` / `index-mobile-https.html` sob `wp-content/cache/wp-rocket/controle.ocafezinho.com/<path>/` (siteurl = controle.ocafezinho.com; o diretório www.ocafezinho.com também existe mas o post cacheia sob controle). `find -name index.html` NÃO acha. Cura usada: `grep -rl "LNCC assume supercomputador" wp-content/cache/ | xargs rm -f` + rm do `index-https.html` da home. Sem isso, URL sem query string servia HTML velho (com `?bust=` vinha novo — assinatura do Rocket, que não cacheia URL com query).
7. **Provas:** `curl www.ocafezinho.com/2026/08/26/lncc-.../` → capa ×3 no body; `<meta property="og:image" content=".../capa-lncc-267719.jpg">`; home com 1 ocorrência (card).

## Broadcast da EMENDA 11
- NYC `/root/v4_labs/dados/diretriz_qualidade_viva.md` (append; backup `.bak_pre_emenda11_20260826`) — é o arquivo que entra no briefing V4.1 (últimos ~700 chars).
- `Cerebro/Foruns/ponte_laura_completa/de_dell.md` ZM-20260826-021 · `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` · `Cerebro/Foruns/inbox_trindade/{claude,codex}.md`.
- NODE_PUBLICACAO_WP_CAFEZINHO + NODE_ATUALIZACOES catalogando este Tema Duplo.

## Lições reutilizáveis
- `secao: 'tecnologia'` no gerador → estilo futurista + "ABSOLUTELY NO TEXT" já no prompt canônico.
- O gerador tenta banco real ANTES da IA; para forçar IA: `forcar_ia_cartoon=True`.
- wp-cli no cafezinho-wp exige `--path=/var/www/ocafezinho` (canônico; `/var/www/rioocafezinho` é o Rio Carta).
- Pendência: ACK de CM/AGY ao ZM-20260826-021 (cobrar nas rondas).
