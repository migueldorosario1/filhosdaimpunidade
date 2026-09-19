# MEMÓRIA — Portal LOGIS: versão definitiva da capa V6 (log técnico completo)

**Data:** 09/09/2026 · **Agente:** ZCode Dell (Qwen3.8-Max) · **Fórum:** `../Foruns/forum_logis_versao_capa_v6_20260909.md`

## Contexto

Portal LOGIS (logística e sustentabilidade, Astro 5 estático trilíngue PT/EN/ES, Vercel `logis-magazine`, código em `Downloads/Antigravity Google/logis/`, repo github.com/migueldorosario1/logis). A matéria de capa `crime-organizado-controle-logistico` («A logística do crime», autor Miguel do Rosário, 28/08/2026) tinha 7 variantes V1-V7 (commits históricos: `9f13710` seletor 5 versões, `cfb6642` V6+V7 bíblicas Neemias/Ezequiel, `9e9b213` foto por versão). Seletor = pills + JS inline em `[slug].astro` trocando citações/foto via `data-v`.

## Decisão (delegada pelo Miguel)

**V6 «a obra e a arma»**: Neemias 4:17 (bíblica) + Agostinho A Cidade de Deus (clássica) + foto muralhas de Jerusalém (crime-v6.jpg, Boris Jaramazović CC BY-SA 4.0). Único mix bíblica+clássica das 7; V7 = 2 bíblicas; V1-V5 = só clássicas. Decisão PROVISÓRIA por ordem do Miguel.

## Arquivos tocados (Dell, pasta logis/)

| Arquivo | Mudança |
|---|---|
| `arquivo_versoes_capa/DECISAO_VERSAO_CAPA_20260909.md` | NOVO — documento de decisão, tabela das 7 versões, textos integrais das 9 citações, receita de reversão |
| `arquivo_versoes_capa/variantes_snapshot_20260909.ts.txt` | NOVO — bloco `variantes:[...]` original (linhas 41-76 do reportagens.ts pré-mudança) |
| `arquivo_versoes_capa/reportagens_pre_decisao_20260909.ts.bak` | NOVO — reportagens.ts integral pré-mudança (73.406 bytes) |
| `arquivo_versoes_capa/[slug]_pre_decisao_20260909.astro.bak` | NOVO — template integral pré-mudança (7.474 bytes) |
| `src/data/reportagens.ts` | interface: `variantes?:{...}[]` → `citas?:{texto,autor,obra,onde}[]`; matéria da capa: foto promovida p/ crime-v6.jpg + bloco variantes (36 linhas) → 2 citas fixas V6 |
| `src/pages/[lang]/reportagens/[slug].astro` | REESCRITO: removidos pills/seletor, spans foto-variante, JS inline de troca, estilos .seletor-versao/.pill-versao; citações epígrafe/antes:/fecho renderizadas diretas de `r.citas` (sem hidden/data-v) |
| `src/data/noticias.ts` | +2 itens no topo: Portogente (portos, set 2026, Santos/dragagem) + Gazeta do Povo (corredores, ago 2026, Chancay/«Dragão de Troia») |

âncoras das citações confirmadas no corpo pt: «Cada obra da nova malha logística é dupla por natureza» (Neemias) e «A Constituição já deu a ordem» (Agostinho). Citações só aparecem no PT (EN/ES são resumos — comportamento pré-existente, mantido). Fotos das 7 versões seguem em `public/imagens/` (nenhuma apagada).

## Notícias: curadoria com prova (regra 28/08: nada fictício)

Busca via Bing News RSS (receita da memória `pesquisa-noticias-rss-bing-webfetch-fallback-20260908`), URL direta extraída do `url=` do apiclick. Verificação HTTP (UA navegador):
- portogente.com.br/noticias/dia-a-dia/118082-acesso-ao-porto-de-santos… → **200**, title confere, pubDate RSS Sun, 06 Sep 2026
- gazetadopovo.com.br/mundo/decisao-judicial-pressao-eua-colocam-berlinda-megaporto-chines-peru/ → **200**, datePublished 2026-08-27T12:09:13Z
- (candidata extra não usada: spacemoney.com.br Chancay/Rubio 07/09 → 200)

## Build/deploy/provas

- `npm run build` → 74 páginas, 2.46s, sem erro.
- dist checado ANTES do deploy: seletor=0; Neemias=1; Agostinho=1; `src="/imagens/crime-v6.jpg"`; 2 blockquotes epigrafe visíveis (grep exato falha por `data-astro-cid-*` — usar grep flexível); home com Portogente+Gazeta do Povo.
- `python3 scripts/deploy_vercel.py` (REST API, token ~/.local/share/com.vercel.cli/auth.json) → 95 arquivos, `dpl_AEvjzTmLibZSERhw6qC1Roadz4JS` READY, alias logis-magazine.vercel.app.
- Produção: matéria PT 200 (seletor=0; «Neemias 4:17», «A Cidade de Deus», crime-v6.jpg presentes); home PT 200 (Portogente + Gazeta do Povo); EN/ES matéria+home 200.
- Git: commit `f0c2a83` (7 files, +726/-122) pushado main → github.

## Reversão (decisão provisória)

- Trocar versão: editar `citas`/`foto` da matéria em reportagens.ts com dados da tabela do DECISAO_*.md.
- Voltar ao seletor 7 versões: `cp arquivo_versoes_capa/reportagens_pre_decisao_20260909.ts.bak src/data/reportagens.ts` + `cp "arquivo_versoes_capa/[slug]_pre_decisao_20260909.astro.bak" "src/pages/[lang]/reportagens/[slug].astro"` + build + deploy.

## Pendência antiga relacionada (cobrar)

MTb (número profissional de jornalista) do Miguel para o bloco «Responsabilidade editorial» da revista Logis — promessa de 22/08 («me cobra depois»), segue pendente.


## Adendo — citações TECIDAS no texto (09/09 ~10:57)

2ª ordem do Miguel (voz): «a citação eu não quero com fonte diferente, cor diferente. Eu quero a citação integrada ao texto, colocada casualmente dentro do texto. E eu quero integrada ao contexto. Se não estiver integrada ao contexto, se for uma coisa perdida, não tem graça. […] se quiser, procura outra citação acoplada ao contexto.»

- Parágrafo pt «Cada obra da nova malha logística é dupla por natureza…» substituído IN-PLACE: abre com os muros da foto (Jerusalém) + Neemias 4:17 como regra da construção exposta, depois o texto original segue intacto. Parágrafo pt «A Constituição já deu a ordem…» substituído IN-PLACE: abre com Agostinho (ordem × ordem), resto intacto («Constituição» → «Constituição brasileira» p/ fluir).
- REMOVIDO: campo `citas?` da interface Reportagem + array do artigo (`reportagens.ts`); em `[slug].astro` a const citas, os 3 renders blockquote.epigrafe (epigrafe/antes:/fecho) e o `<style>` inteiro (.epigrafe*).
- **Receita p/ futuro:** citação no LOGIS = string dentro do próprio parágrafo, atribuição em prosa («ensinou Agostinho de Hipona», «(Neemias 4:17)»), zero formatação especial. Substituições SEMPRE in-place — inserir/remover parágrafo desloca `graficos.apos` (0-based).
- Verificação produção: artigo pt 200; `grep -c epigrafe`=0; `blockquote`=0; «seguravam a arma (Neemias 4:17)»=1; «ensinou Agostinho de Hipona»=1; en/es/home 200. Build 77 p. (2,06 s); deploy `dpl_FtQic4PRAeMTKv6SHht3QKdqnG6S`; commit `5c1701f`.
- ⚠️ **Armadilhas desta missão:** (a) grep de conferência do monitor com padrão ERRADO («CITAÇÕES INTEGRADAS» quando a linha dizia «CITAÇÕES DA CAPA: INTEGRADAS») → falso clobber + 3 inserções duplicadas, dedup feito; conferir sempre com substring literal exata da linha. (b) Clobber real existe: `sync_cerebro_from_github.sh` (cron :00/:15/:30/:45) reflete repo→Cérebro local — linha gravada só local some se não for publicada no cerebro-miguel antes do próximo tick; publicar NA HORA.
