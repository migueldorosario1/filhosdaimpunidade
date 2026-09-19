# Memória técnica — Legenda obrigatória nos sites temáticos (2026-08-06 ~23:00→00:50 BRT)

Sessão: ZCode (Kimi K3), workspace ZCodeProject, chat direto. Ordem do Miguel: "as imagens precisam ter legenda — bota essa instrução em todos os sites temáticos" + pergunta "a imagem desse post está errada, não?" (post não identificado; ver §6).

## 1. Contratos editoriais (cérebro editorial dos sites)

`agent_data/contratos/{aiatolah,ceara,mapario,mundotrilhos,riocarta}.md` (PT) e `{discoverbrazil,globalsouth,railpost}.md` (EN): novo **item 7** na "Política de imagens", após o item 6 (juiz visual). Texto PT:
> 7. **TODA imagem publicada precisa de LEGENDA visível** (ordem do editor, 06/08/2026). Legenda = frase curta e factual descrevendo o que a imagem mostra (quem/o quê/onde), seguida do crédito/licença. A legenda é gravada no frontmatter (`hero_legenda`) e exibida sob a imagem no site. Imagem sem legenda factual NÃO entra no ar — se a cena não puder ser descrita com fidelidade, a imagem está errada e deve ser trocada.

Backups: `<arquivo>.bak_pre_legenda_obrigatoria_20260806` (×8).

## 2. Engine V4 local (`agentes_tematicos/v4/`)

- `publicador.py` (backup `.bak_pre_legenda_obrigatoria_20260806` — feito após helper+docstring, antes dos retornos; arquivos não são versionados no git):
  - Novo helper `_limpar_legenda(txt, max_len=220)`: tira HTML (extmetadata Wikimedia), prefixo `File:`, extensão, underscores; "" se <4 chars.
  - `_buscar_hero` passa a retornar **4-tupla** `(path, credit, keys, legenda)`. Legenda por fonte: Banco de Mídia → `cand["title"]`; Wikimedia → `extmetadata.ImageDescription` → fallback título do File:; cascata (pixabay/pexels/openverse/unsplash) → `c.get("tags")` quando há; IA e acervo default → "" (caller cai no fallback).
  - Caller (único, ~linha 707): `artigo["hero_legenda"] = hero_legenda or ""`; e guarda estrutural nova: **se tem hero_path e não tem legenda → legenda = título da matéria** (cobre hero pré-resolvida, ex.: thumbnail YouTube).
- `nucleo_frontmatter.py` (backup idem): grava `hero_legenda` nos dois estilos ("collection" e "pages"); **"pages" também passou a gravar `hero_credit`** (não gravava — descumpria o item 3 do contrato).
- Teste: `py_compile` OK + script de 4 asserts (helper, collection, pages, ausência limpa) — todos verdes.

## 3. Templates e schemas (8 repos em `Projeto Cafezinho Agentes/sites-v4/`)

- **Schemas** (`src/content.config.ts`): `hero_legenda: z.string().optional()` nos 7 collection-sites; `hero_credit` adicionado onde faltava (ceara, mapario, riocarta). Aiatolah é pages-style (sem schema).
- **Layouts**: legenda + crédito sob o hero.
  - riocarta/ceara/mapario/discoverbrazil (`BlogPost.astro`): novo `<p class="image-caption">` (legenda em `<span class="image-caption-text">` + `Foto:|Photo: <hero_credit>`), CSS novo; `.hero-image` de ceara/riocarta era `display:flex` (linha) → virou coluna (`flex-direction: column; align-items: center`) para a legenda ficar EMBAIXO; alt do img agora `hero_legenda || title`.
  - mundotrilhos/railpost: `<p class="image-credit">` existente ganhou a linha de legenda (condição ampliada para `hero_legenda || hero_credit`) + CSS `.image-caption-text`.
  - globalsouth: `<span class="hero-credit">` existente ganhou `hero-caption-text` prefixado ("legenda — Photo: ...").
  - aiatolah (`PostLayout.astro`, bilíngue): `<p class="post-hero-caption">` fora do wrapper (overflow:hidden), "Foto:"/"Photo:" conforme `isPt`, CSS dark-theme.
- Props fluem via `<BlogPost {...post.data}>` (collection) e `frontmatter` (pages) — sem mudança de páginas.
- **Builds: 8/8 OK** (riocarta com post sintético de teste → HTML provou `<span class="image-caption-text">Cães brincam em gramado — imagem de teste</span>Foto: Photo by AnjaGh on Pixabay`; post removido depois).
- **Pushes (HEAD==origin verificado, regra pós-incidente):** aiatolah `3865c0a`, ceara `f07f068`, discoverbrazil `d787df3`, globalsouth `19da5b3`, mapario `f6fc6f3`, mundotrilhos `ab93a8a`, railpost `03f7d88`, riocarta `d04f5f6`. Commit: "feat: legenda obrigatoria sob a imagem de capa (hero_legenda + figcaption) — ordem do editor 2026-08-06". Só `src/layouts/` + `src/content.config.ts` staged (repos têm crons vivas — nunca `git add -A`).
- **Ao vivo (Vercel):** riocarta.com e ceara.digital já renderizam o crédito sob o hero nos posts de hoje.

## 4. Droplet utilitário (142.93.48.252) — agentes-servidor

Script: `ZCodeProject/scratch/patch_legenda_droplet.py` (idempotente, com backups e asserts de ocorrência). Aplicado:
- `agentes/ferroviario/agente_ferroviario_v2.py` — 2 writers (Mundo Trilhos PT ~1751; Rail Post EN ~1958): cálculo `hero_legenda` (img_meta title/description → alt → título; strip HTML/quotes; 220c) + linha no frontmatter. 
- `agentes/turismo/agente_turismo_embratur.py` — 1 writer (Discover Brazil EN), mesmo padrão.
- `aiatolah/agentes/aiatolah_agente_youtube.py` — legendas PT/EN para thumbnail YouTube ("Thumbnail oficial do vídeo no YouTube — <título>" / "Official YouTube thumbnail — <title>") nos 2 templates de frontmatter. Ordem de definição das variáveis verificada (titulo_en:122 / titulo_pt:135 < inserção:187).
- `diretrizes_editoriais.py` (ferroviário PT + turismo EN): nova constante `REGRA_LEGENDA_OBRIGATORIA` anexada (documenta a regra para futuros prompts).
- `py_compile` OK nos 3 agentes. **Prova real pendente:** próximos posts (ferroviário 1 em 1h ímpar?:15 — cron `15 */2`; turismo 9/13/17/21:42) devem sair com `hero_legenda` no frontmatter — checar logs/posts na próxima janela.

## 5. PENDENTE — pipelines legados cicero/GSN (rio-ag 159.89.185.209 + NYC 198.199.121.136)

Writers de md desses pipelines NÃO gravam `hero_credit`/`hero_legenda`. Pontos exatos para retrofit (rio-ag):
- `/root/cicero_publicador_tematicos.py:672` (`md_content += f"heroImage: ..."`)
- `/root/cicero_smoke_markdown.py:809`, `/root/cicero_agente_opiniao.py:293`, `/root/cicero_admin.py:797`
- `/root/gsn_publicador_tematicos.py:688`, `/root/gsn_smoke_markdown.py:693`
- NYC roda cópias em `/root/cicero_remote/` (crons `ceara_hourly_cron.sh` 9:15 e `cicero_hourly_cron.sh` 10:00).
Observação arquitetural: V4 local (orquestrador cron `0 3,13 --all` + ceara/riocarta `*/8h`) já cobre ceara e globalsouth com a regra — avaliar migração definitiva desses sites para o V4 em vez de remendar o legado.

## 6. Diagnóstico "imagem errada" (aguardando o Miguel dizer qual post)

Auditoria visual dos 2 posts mais novos da rede (06/08):
- **ceara** `20260806-pf-cumpre-mandados-em-fortaleza-camocim-e-granja-contra-facc` — hero P&B de viatura **CHOQUE/POLÍCIA MILITAR** (Pexels, "João Saplak") em cidade com estações-tubo (arquitetura sugere Curitiba). Matéria é de operação da **Polícia Federal** no Ceará → força errada + lugar errado. **Errada.**
- **riocarta** `20260806-vacinacao-antirrabica-comeca-sabado-no-rio-com-125-postos` — hero Pixabay ("AnjaGh") de **cães correndo no gramado**; matéria é campanha de VACINAÇÃO com 125 postos → sem vacina/posto/ato de vacinar. **Fraca/errada.**
Troca NÃO executada (Miguel não confirmou o post). Ritual pronto (o de 06/08 14:15): candidata real auditada visualmente → backup → swap → rollback jsonl.

## 7. Aprendizados

1. **A legenda é ferramenta anti-imagem-errada**: o crédito "Pexels" sob a foto do "CHOQUE" já denuncia o erro editorial sem abrir o código.
2. `git add` com pathspec inexistente (content.config.ts no aiatolah) aborta o add INTEIRO — add por arquivo explícito quando os repos diferem.
3. `.hero-image` com `display:flex` em linha joga qualquer irmão da `<img>` para o LADO da foto — legenda exige coluna.
4. Verificação de deploy = HEAD==origin + grep no HTML ao vivo (não basta "push OK").
