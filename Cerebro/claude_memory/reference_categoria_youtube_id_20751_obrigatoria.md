---
name: reference-categoria-youtube-id-20751-obrigatoria
description: "Miguel 16/06 17:43 BRT criou categoria WP 'Youtube' (slug youtube, ID 20751) e quer que TODO post gerado pelo agente_youtube_publicador inclua essa categoria SEMPRE — adicional, não substitutiva (pode ter cat temática + cat=20751 juntas). Combinada com AUTH-048: cron 3x/dia (8h/14h/20h BRT). Confirmado com #258901 promovido publish 17:42 BRT (cat=[5003 Soberania, 20751 Youtube]) — primeiro post YT em PUBLISH em 30+ dias."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Categoria YouTube (ID 20751) obrigatória em todo post do agente_youtube_publicador

## A regra

Miguel 16/06 17:43 BRT criou no WordPress do Cafezinho a categoria **"Youtube"** (slug `youtube`, ID `20751`). Quer que **TODO post gerado pelo `agente_youtube_publicador.py`** inclua essa categoria — sempre, em adição à categoria temática que o pipeline já atribui (Soberania, Geopolítica, IA, etc).

## Caso fundador

- **#258901** "Douglas Macgregor: 'Trump percebeu que Zelensky é um mentiroso gigantesco. A guerra está perdida'"
- Publicado 17:42 BRT como PUBLISH (promovido de DRAFT por Miguel após AUTH-047)
- cat=[**5003 Soberania**, **20751 Youtube**] — confirmação visual do padrão desejado
- Primeiro post YT em publish em 30+ dias

## Como aplicar

No `agente_youtube_publicador.py` (linha 781-783):

```python
cat_id = _obter_id_termo(categoria_str, 'categories')
if cat_id:
    post_data["categories"] = [cat_id]
```

Patch necessário: garantir que `20751` esteja **sempre** no array final:

```python
cat_id = _obter_id_termo(categoria_str, 'categories')
CAT_YOUTUBE_ID = 20751  # obrigatória — Miguel 16/06 (memória reference_categoria_youtube_id_20751_obrigatoria)
if cat_id:
    post_data["categories"] = [cat_id, CAT_YOUTUBE_ID]
else:
    post_data["categories"] = [CAT_YOUTUBE_ID]
```

(escopo da AUTH-048)

## Cron 3×/dia

Miguel também 17:43 BRT autorizou aumento de cadência: cron `25 11 * * *` (watcher) + `35 11 * * *` (publicador) → **3×/dia** distribuído (manhã/tarde/noite, ex: 8h/14h/20h BRT).

## Combinação

AUTH-048 = (cron 3×/dia) + (cat=20751 obrigatória).

## Relacionados

- [[reference_iproyal_proxy_youtube_yt_dlp_bypass]] — proxy IPRoyal AUTH-047 destravou pipeline YT
- [[feedback_publipost_so_como_page_nao_post]] — convenção de categoria + tipo de post
- [[feedback_tags_publicas_l_k_h_wp_origem_post]] — tags L/K/H pra origem; cat 20751 é categoria pública (visível)
