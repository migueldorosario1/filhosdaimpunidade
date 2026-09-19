# Fórum — Post Lula/Governador Valadares: foto real de hoje + no-home + auditoria de autoria (21/08/2026)

**Sessão:** ZCode (Dell), modelo DeepSeek · **Ordem do Miguel (22:14):** "acha uma foto de lula hoje em minas para esse post, e bota ele em categoria no-home. é um post muito fraco. quem fez isso?"

**URL:** https://www.ocafezinho.com/2026/08/21/lula-vai-a-minas-para-vistoriar-obra-em-governador-valadares/ · **Post ID 266972** · publicado 21/08/2026 21:28 BRT.

## O que aconteceu (resumo)

1. **Foto trocada ✅** — imagem genérica ("agenda oficial de infraestrutura") substituída pela **capa oficial do álbum "21.08.2026 - Visita às Obras de Duplicação da Ponte São Raimundo (BR-116/251/MG)"** do Flickr **Lula Oficial** (NSID 157736962@N05, álbum 72177720335231507), foto **Ricardo Stuckert, CC BY-SA 2.0**. Lula de capacete no canteiro, rio Doce e estrutura da ponte ao fundo. **Validada por visão antes de subir (nota 9/10).** Novo attachment **266980** (1600×923) como imagem destacada, com alt text e caption creditados. Meta `_cafezinho_img_check` atualizada (agent "ZM-manual (ordem Miguel)", trilha da aprovação anterior LAURA-AGY preservada na nota e em backup).
2. **Categoria no-home ✅** — adicionada pelo **slug** `no-home` (term **20699**, o verdadeiro — não caiu na espúria 21164). Home verificada sem cache: slug **0 ocorrências** — post saiu da home. Cache WP Rocket purgado (rm + `rocket_clean_domain()`).
3. **Quem fez (auditoria)** — ver seção abaixo.

## Quem fez o post

- **Redação: agente V4 Nacional** — meta `zizi_job_id = v4d_nacional_6855a4d21e2c4651`; autor WP = conta genérica "Redacao nova" (ID 5786, cafezinhov4@gmail.com).
- **Aprovação de imagem + publicação: LAURA-AGY** — metas `_cafezinho_img_check` (agent "LAURA-AGY", media 266973) e `_cafezinho_img_isenta` ("aprovacao_laura_agy_consenso_duplo", user **gabrielbarbosa/5735**) com ts 21:28, mesmo minuto da publicação.

## Por que o post é fraco (diagnóstico)

- **Texto pré-evento publicado tarde:** todo escrito no futuro ("visitaria", "estava prevista", "dependia do cumprimento") e publicado às **21h28**, ~6h DEPOIS da vistoria (15h30). É pauta de agenda, não cobertura do que aconteceu.
- **🔴 Erro factual suspeito (BUG registrado):** o texto cita "**ministro George Santoro, dos Transportes**". Fontes oficiais do dia — gov.br/Transportes, TMC, DRD — reportam quem acompanhou Lula na obra foi o ministro **Alexandre Silveira**. Nome "George Santoro" não bate com nenhuma fonte; provável alucinação de redação. Registrado em `CEREBRO_NODE_BUGS_ATIVOS.md`. **Não corrigi sem ordem** (conteúdo editorial é domínio CL/CM; post já está fora da home).
- Imagem era genérica (corrigida nesta sessão).

## Ressalva menor

`og:image` (preview social) ainda serve a imagem antiga numa variante de cache que sobreviveu a `wp cache flush`, `rm -rf wp-rocket/*` e `rocket_clean_domain()`; em geração fresca (testado com query única) já sai a foto nova, e a meta `_yoast_wpseo_opengraph-image` foi gravada com a URL nova — auto-corrige quando a variante expirar. Hero do post (o que o leitor vê) já está com a foto nova.

## O que falta / o que preciso de você (Miguel)

1. **Decidir sobre "George Santoro" → "Alexandre Silveira"** (1 palavra; posso corrigir em 1 min com ordem, ou deixar para CL/CM pelo protocolo v2.2).
2. Nada mais — foto, crédito, categoria e home já aplicados e verificados.

## Provas

- Termos do post: `20699/no-home` + `22/politica-2` (wp post term list).
- Thumbnail: `_thumbnail_id = 266980`; hero do single servindo `lula-obra-capa-20260821` (2 ocorrências no HTML).
- Home sem o slug (grep = 0) em 2 UAs distintos.
- Backups no servidor: `/root/backup_metas_266972_pre_foto_20260821.json` + `/root/backup_content_266972_pre_20260821.txt`; foto original em `/tmp/lula_obra_capa_20260821.jpg` (servidor e Dell).
