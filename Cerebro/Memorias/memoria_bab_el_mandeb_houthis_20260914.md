# 🌊 Memória técnica — Matéria Houthis × Bab el-Mandeb (post 270884) — 14/09/2026

**Sessão:** ZM (ZCode/GLM-5.3), ordem Miguel ~17:0x 14/09/2026 · **Fórum par:** `Foruns/forum_bab_el_mandeb_houthis_20260914.md`

## 1. Timeline executada (BRT)

- 17:06 — hora real (date); MONITORAMENTO lido; linha EM ANDAMENTO escrita
- 17:0x — WebSearch ×3: ofensiva (Reuters/CNN/AJ/BBC/CFR/ISW), preço (TIME/WION/EIA), números do estreito (Kobeissi/EIA/TIME/CNN) — números ditados pelo Miguel TODOS ancorados
- 17:0x — manual do agente + manual da capa lidos; cat 2403 conferida (= Redação, assinatura §137)
- 17:08 — câmbio: R$ 5,15-5,16 (UOL/Folha/Wise 14/09); Brent hoje +4,9% US$ 109,74 (Folha)
- 17:09 — Commons: foto «Bab-el-Mandeb, outer space.jpg» (NASA JSC, ISS062-E-51223, 1263x939, PD) baixada em /tmp; análise visual: Perim ao centro do estreito
- 17:1x — matéria escrita (~520 palavras); verifica_estilo 3 passadas (3→2→1→0 alertas: trocar eco h3↔frase, «Só contra o porto», tirar «de petróleo» duplicado, «400 mil por dia» sem barris, «empurrar o preço»)
- 17:1x — scp HTML+foto → cafezinho-wp; `wp post create /tmp/materia_bab_el_mandeb.html --post_title=... --post_status=draft --post_author=5470 --post_category=2403,5003,5052 --post_excerpt=... --porcelain` → **270884**
- 17:1x — capa: `wp media import /tmp/bab_el_mandeb_nasa.jpg --post_id=270884 --featured_image --title/--caption/--alt --porcelain` → **ATT 270885** (`uploads/2026/09/bab-el-mandeb-nasa.jpg`, md5 4bf8c48558b0494e5bc055ef7d8168c6); metas img_check+carimbo+thumbnail+§136 (_publicado_por zm, _agente_origem zcode, _agente_versao glm-5.3)+capa_operador zm+capa_fonte Commons; tags via `wp post term set 270884 post_tag Iêmen,Mar Vermelho,petróleo,hutis`
- 17:2x — prova: post_author 5470, status draft, thumb 270885, URL da imagem pública OK
- 17:2x — Tema Duplo + ponte ZM-20260914-008 + sync GitHub + monitor ✅

## 2. Receitas que funcionaram

### Foto no Wikimedia Commons (namespace é OBRIGATÓRIO)
```bash
curl -s -A 'Cafezinho-V4-MediaScout/1.0' \
'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=Bab-el-Mandeb&gsrnamespace=6&gsrlimit=12&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1920&format=json'
```
- **gsrnamespace=6 = arquivos** (sem isso devolve galerias inúteis) · UA obrigatório · iiurlwidth máx 1920
- Fonte escolhida: NASA Earth Science and Remote Sensing Unit (JSC), ISS Expedição 62, frame ISS062-E-51223 — **Perim aparece ao centro** (é a ilha tomada em 11/09; a foto conta o fato)
- Extmetadata dá LicenseShortName + Artist + ImageDescription (crédito correto na legenda)

### Publicação como agente redator (§137)
1. `wp post create <arquivo.html> --post_title= --post_status=draft --post_author=5470 --post_category=2403,5003,5052 --post_excerpt= --porcelain --allow-root`
2. `wp media import <arquivo> --post_id=<PID> --featured_image --title --caption --alt --porcelain`
3. img_check ANTES de tocar thumbnail de novo; carimbo = md5 do arquivo EM uploads (via `wp eval "echo get_attached_file(<ATT>);"`)
4. metas §136 + capa_operador/capa_fonte; `wp post term set <PID> post_tag ...`
5. NUNCA publish — avisa a ponte (ref ZM-<data>-NNN em `Foruns/ponte_laura_completa/de_dell.md`) e o chefe de publicação decide

## 3. Estado

**PRONTO/AGUARDANDO:** 270884 draft completo (capa+metas+tags+estilo 0 infrações) aguardando revisão da ponte e publish (CL no comando; slot 20:01 vazio citado pela própria CL 16:4x). Tudo decidido no fórum par §3.

## 4. Atenções para a próxima sessão

- Confirmar se a ponte publicou (`wp post get 270884 --fields=post_status`); se publish e 404 → cache → `rocket_clean_post`/grep cache Rocket
- Push herda título (55 chars) — aceitável, mas monitorar corte
- Cuidado com série de vídeos «Robinson Farinazzo» (aviso CL-20260914-010) — sem relação com este post, mas mesma janela de publicação
- Atualizar o Kobeissi (X) como fonte de mercado rápida para os próximos capítulos do caso (fechamento total do estreito = próxima fronteira noticiosa)

— ZM · ZCode/GLM-5.3 · 14/09/2026 ~17:2x BRT
