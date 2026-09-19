# Memória — Post Lula/Valadares 266972: foto + no-home + auditoria (21/08/2026)

**Fórum gêmeo:** `Foruns/forum_20260821_post_lula_valadares_foto_no_home.md` · Sessão ZCode/DeepSeek 22:14→22:40 BRT.

## Log técnico

### Ação 1 — Foto real de hoje (troca da imagem destacada)

- Fonte: Flickr **Lula Oficial** `flickr.com/photos/lulaoficial/` (NSID `157736962@N05`, descoberto via HTML da página do perfil).
- Feed público (`/services/feeds/photos_public.gne`) só lista 20 últimas — todas do ato de BH; fotos da obra ficaram fora → **fallback: página de álbuns** (`/albums`, grep `721777\d+` perto de "São Raimundo") → **2 IDs**: `72177720335231507` = **álbum da obra** (o `…33732` é o álbum de BH — confirmar pelo `<title>`!).
- Capa do álbum extraída do HTML: única URL completa embutida é a capa em `_h.jpg` (1600px): `https://live.staticflickr.com/65535/55479200949_61cd26216f_h.jpg`.
- **Gotcha Flickr:** montar sufixos de tamanho na mão (`_z` etc.) devolve **410 "File not found"** para este álbum — usar a URL completa já embutida no HTML.
- Visão remota falhou com URL direta do staticflickr (erro 1210 do gateway); **workaround**: `Read` local sobe p/ CDN e a URL da CDN funciona no `analyze_image`. Veredito 9/10 (Lula reconhecível, capacete, canteiro, rio, ponte).
- Import no canônico (`ssh cafezinho-wp`, wp-cli `--allow-root`, path `/var/www/ocafezinho`):
  - `wp media import /tmp/lula_obra_capa_20260821.jpg --post_id=266972 --featured_image --title=... --caption="...Foto: Ricardo Stuckert / Flickr Lula Oficial (CC BY-SA 2.0)"` → **attachment 266980**.
  - WP **normaliza underscores → hífens** no filename: `lula_obra_capa` virou `lula-obra-capa-20260821` — grep de prova precisa usar HÍFEN.
  - `_wp_attachment_image_alt` no attachment + `_cafezinho_img_check` regravada no post (agent `ZM-manual (ordem Miguel)`, nota preservando trilha LAURA-AGY).
- Backups pré-mudança no servidor: `/root/backup_metas_266972_pre_foto_20260821.json` + `/root/backup_content_266972_pre_20260821.txt`.

### Ação 2 — Categoria no-home

- `wp post term add 266972 category no-home` (**sempre o slug**; caiu no term 20699 correto, não na espúria 21164). Políticas mantidas (term add ≠ term set).

### Ação 3 — Cache WP Rocket (a saga)

- Sintomas pós-mudança: home/post servindo conteúdo antigo.
- `wp cache flush` limpa só object cache (Redis) — **não** o page cache. Plugin de página = **WP Rocket** (`wp-content/cache/wp-rocket/`). `wp rocket clean` NÃO existe nesta versão.
- `rm -rf wp-content/cache/wp-rocket/*` + `wp eval 'rocket_clean_domain();'` (API oficial) — ambos usados.
- Home e hero do single: corrigidos e provados.
- **`og:image` persistiu antigo** na URL limpa mesmo com: meta `_yoast_wpseo_opengraph-image` nova gravada, thumbnail novo, `rocket_clean_domain()`. Em geração fresca com query única (`?zz=$RANDOM`) sai a URL NOVA → há variante de cache interna (provavelmente Redis/variante Rocket por UA) que resiste; expectativa de auto-correção no TTL. Investigado e descartado: filtro `wpseo_opengraph_image` do plugin `serverdoin-cdn/rewrite.php` (é só `str_replace` publicador→principal, inocente), mu-plugins `cafezinho_meta_credito_pendente` (só registra meta) e `cafezinho-seo-pruning` (noindex/410).

### Ação 4 — Auditoria de autoria (quem fez)

- `zizi_job_id = v4d_nacional_6855a4d21e2c4651` → **agente V4 Nacional** redigiu (autor WP "Redacao nova"/5786).
- `_cafezinho_img_isenta = {"motivo":"aprovacao_laura_agy_consenso_duplo","user_id":5735}` (conta `gabrielbarbosa`) → **LAURA-AGY** aprovou imagem e publicou às 21:28.
- **Erro factual suspeito no texto:** "ministro **George Santoro**, dos Transportes" vs fontes do dia (gov.br/Transportes, TMC, DRD): **Alexandre Silveira** acompanhou a vistoria. Registrado em `CEREBRO_NODE_BUGS_ATIVOS.md`; correção pendente de decisão do Miguel (editora = CL/CM).

## O que falta / preciso do Miguel

1. Ordem sobre corrigir "George Santoro"→"Alexandre Silveira" no 266972.
2. (Menor) og:image auto-corrige; sem ação.
