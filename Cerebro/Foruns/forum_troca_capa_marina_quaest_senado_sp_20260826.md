# 🖼️ Fórum — Troca de capa do post 267686 (Quaest Senado SP): fachada do Senado → Marina Silva na COP30

**Data:** 26/08/2026 ~09:20–09:45 BRT · **Agente:** ZCode/GLM-5.3 (chat direto com o Miguel) · **Memória irmã:** `Memorias/memoria_troca_capa_marina_quaest_senado_sp_20260826.md`

## O pedido (Miguel, 26/08 ~09:20)

> "acha foto jornalistica recente da Marina Silva. fica feio essa imagem aí de Senado Federal"
> — sobre `https://www.ocafezinho.com/2026/08/26/quaest-mostra-empate-triplo-pelo-senado-em-sao-paulo/` (post 267686, publicado 01:19, agente LAURA-AGY), cuja capa era a fachada do Congresso/Senado (mídia 267513).

## Decisão de imagem (inspeção visual de 15 candidatas)

| Candidata | Por que não / por que sim |
|---|---|
| Foto oficial TSE "MARINA SILVA CANDIDATA SENADORA SP" | ❌ 161×225 px — minúscula p/ destaque |
| Convenção Federação Brasil da Esperança, 25/07/2026 (Campinas, Ricardo Stuckert, 12 fotos) | ❌ Marina sempre coadjuvante (foto grupal c/ bandeira), de costas (abraço c/ Lula) ou só no banner |
| COP30 retrato, 18/11/2025 (Xuthoria, obra própria) | ✅ **ESCOLHIDA** — Marina é O sujeito: sorrindo, rosto pleno, colar vermelho, 3376×6000, CC BY-SA 4.0 |
| "Encontro sociedade civil e povos indígenas", 19/11/2025 | ❌ Lula e Sônia Guajajara dominam o quadro |
| 5ª Conf. Nacional Meio Ambiente, ago/2025 | ⚠️ reserva — Marina ao púlpito mas com cabeça desfocada em 1º plano |

**Arquivo Commons:** `File:COP30 - Marina Silva 01.jpg` — legenda aplicada: *"Marina Silva (Rede), candidata ao Senado por São Paulo, durante a COP30 em Belém, em novembro de 2025. Foto: Xuthoria/Wikimedia Commons (CC BY-SA 4.0)"*.

## Execução (tudo no canônico `cafezinho-wp`)

1. Download da original + `ImageOps.exif_transpose` (a foto tem EXIF orientation — crua é 6000×3376 de lado) + crop 16:9 centrado no rosto → **1600×900** (`marina-silva-cop30-belem-2025.jpg`).
2. Upload REST (conta "Redacao nova") → **mídia 267739** com title/caption/alt/description preenchidos.
3. Carimbo `_cafezinho_img_check` {ok:true, media_id:267739, agent:"ZCode/GLM-5.3 (ordem Miguel — troca de capa)", source/license/alt/caption} — **antes** do thumbnail (ver lição abaixo).
4. `wp post meta update 267686 _thumbnail_id 267739` (wp-cli `--allow-root`) — aceito pelo gate.
5. Cache: post não estava em Rocket; `index.html` da home removido (card usa a capa).
6. Yoast: `wp_update_post` via `wp eval` p/ disparar save_post → indexable reconstruído → og:image + JSON-LD com a foto nova.

## Estado da missão

- **O que aconteceu:** capa trocada, carimbada, com crédito correto e provada ao vivo (screenshot headless Chrome: foto da Marina grande no post; body 3×; og:image/JSON-LD/home 1× com `marina-silva-cop30-belem-2025.jpg`).
- **O que falta:** nada. Espelho (159.65.177.60) sequer tem o post (404) — fora do fluxo público.
- **O que preciso de você (Miguel):** nada — só conferir se gostou da escolha. Se preferir outra (ex.: Marina ao púlpito na 5ª CNMA), troco em 2 minutos.

## Lições (valem p/ toda troca de capa)

1. **Gate visão-capa (Emenda 7):** o mu-plugin `cafezinho-gate-visao-capa.php` intercepta update de `_thumbnail_id` e exige carimbo `_cafezinho_img_check` ok:true com **media_id IGUAL ao novo** — portanto **carimbo PRIMEIRO, thumbnail DEPOIS**. Ordem inversa = "Failed to update custom field".
2. **Yoast indexable guarda og:image:** trocar `_thumbnail_id` por meta direta NÃO atualiza og:image/JSON-LD. Solução: `wp eval 'wp_update_post(["ID"=>...])'` (save_post reindexa).
3. **REST `featured_media` silenciosamente ignorado** quando o gate barra (HTTP 200 mas não aplica) — conferir `_thumbnail_id` depois, não confiar no 200.
4. **EXIF orientation:** foto do Commons pode vir "deitada" (3376×6000 declarado × 6000×3376 crua) — sempre `ImageOps.exif_transpose` antes de crop.
5. **Commons API:** buscar por `srsearch="<nome> <ano>"` + categorias `Category:<Nome>_in_<ano>` cobre fotos recentes de políticos; thumb 800px pode dar 400 em arquivo grande — pedir 1280px.
