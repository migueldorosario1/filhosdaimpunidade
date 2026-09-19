# 🖼️ Fórum EMENDA 11 — capa de imagem IA em tecnologia + caso LNCC (267719)

**Data:** 2026-08-26 ~11:35–12:00 BRT · **Autor:** ZCode/Kimi K3 · **Gatilho:** ordem direta do Miguel
**Refs:** ZM-20260826-021 (ponte de_dell) · canal_trindade · inbox claude/codex · diretriz_qualidade_viva.md (NYC)

## O que aconteceu

1. Miguel apontou que o post **267719** ("LNCC assume supercomputador em pacote de IA com Huawei", publicado 26/08 07:19, cat 30 Tecnologia, autor 5470) estava **sem imagem destacada** (`featured_media: 0`).
2. Ordem do Miguel: "uma matéria assim de tecnologia pode ter imagem IA (sem texto interno). Informe ao loop, ao Cérebro, a todo mundo, que matérias de tecnologia, especialmente sobre IA e supercomputadores, podem ter imagens IA".
3. **Capa aplicada via pipeline canônico do NYC** (`/root/gerador_imagem_editorial.py`): banco de mídia real (Flickr) tentado primeiro — 7 candidatas REPROVADAS pelo Tribunal Visual (comportamento correto) → prompt visual escrito por gpt-5.5 (estilo futurista, "ABSOLUTELY NO TEXT") → gerada por **Flux Pro** (fal.ai). Inspeção visual humana/agente: datacenter futurista + nuvem brilhante + chave ao centro (tese do controle de dados da matéria), silhuetas anônimas, **zero texto interno**. ✅
4. **Aplicação no WP (ordem canônica do procedimento de capa publicada):** upload REST (mídia **267763**, legenda com crédito "Ilustração: Cafezinho / Flux Pro — gerada por IA") → carimbo `_cafezinho_img_check` `{"ok":true, via:"zcode_kimi_k3_emenda11", generator:"flux-pro", image_kind:"ia_gerada", media_id:267763}` **ANTES** de `_thumbnail_id` → readback `_thumbnail_id=267763` ✅ → Yoast reindexado via `wp_update_post` → caches limpos.
5. **Gotcha novo de cache:** o WP Rocket grava as páginas como `index-https.html` e `index-mobile-https.html` (não `index.html`) — `find -name index.html` não acha NADA e a página pública segue velha. Cura: `grep -rl "<trecho do título>" wp-content/cache/ | xargs rm -f`. (Atualizar a memória do procedimento de troca de capa.)
6. **Provas ao vivo:** body do post com a capa ×3, `og:image` = `.../2026/08/capa-lncc-267719.jpg`, card da home com a capa nova.

## A EMENDA 11 (regra viva)

> Matérias de tecnologia — especialmente IA, supercomputadores e infraestrutura digital — **PODEM** ter capa gerada por IA quando não houver foto real adequada. Condições: **sem texto interno** na imagem, sem rostos reconhecíveis, crédito "Ilustração: Cafezinho / <gerador> — gerada por IA". **NUNCA deixar matéria de tecnologia sem capa:** se o banco real for reprovado pelo Tribunal Visual, o gerador editorial (`forcar_ia_cartoon`) é caminho LEGÍTIMO, não último recurso.

## Onde a emenda foi gravada (broadcast)

- NYC `/root/v4_labs/dados/diretriz_qualidade_viva.md` (entra no briefing de toda matéria V4.1; backup `.bak_pre_emenda11_20260826`)
- Ponte `Foruns/ponte_laura_completa/de_dell.md` — **ZM-20260826-021** (ACK de CM/AGY pendente)
- `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` + `Foruns/inbox_trindade/{claude,codex}.md`
- Cérebro: este fórum + `Memorias/memoria_emenda11_capa_ia_tecnologia_lncc_20260826.md` + NODE_PUBLICACAO_WP_CAFEZINHO + NODE_ATUALIZACOES

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** capa Flux Pro no 267719 provada ao vivo; Emenda 11 gravada na diretriz viva do loop + ponte + canais + Cérebro.
- **Falta:** ACK de CM/AGY ao ZM-021 (cobrar nas rondas).
- **Preciso de você:** nada urgente.
