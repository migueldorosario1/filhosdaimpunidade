# MEMÓRIA — Portal LOGOS + Revista Logis (log técnico completo)

**Data:** 2026-08-22 · **Agente:** ZCode/Qwen 3.8 · **Fórum par:** `../Foruns/forum_portal_logos_proposta_20260822.md`
**Nodo:** `../CEREBRO_NODE_PROJETO_CASA_DA_MOEDA.md`

---

## 1. Cronológico da sessão

1. Missão do Miguel: achar projeto Casa da Moeda/Controle Logístico (feito na sessão anterior — repo `casadamoeda/`, site controlelogistico.vercel.app HTTP 200) + **nova ordem**: usar material novo (`novos edson/`) e apresentar proposta de um **portal de logística sustentável trilíngue (LOGOS) + revista trimestral LOGIS**, com geomapas, contratos, reguladores BR por estado + mundo, parte legal, centros de pesquisa, bancos de artigos, reciclagem/sustentabilidade, e MoedaLog/selo fiscal eletrônico na seção "Ideias para o Desenvolvimento".
2. Ritual: MONITORAMENTO_DE_TRABALHO lido e linha registrada (16:20).
3. **Leitura integral do material novo** (`Outros/Projeto Casa da Moeda/novos edson/`):
   - `MOEDALOG -INOVAÇÃO SEM TENDÊNCIA É INVENÇÃO.pptx` (16 slides, extraído via python-pptx): Custo Brasil R$ 1,7 tri/ano; mercado ilegal R$ 500 bi (2025); LPI; eIDAS; Selo Eletrônico ITI (31/10/2024, transição 2029, 7,3 mi e-CNPJs); Rota Brasil (2022, revogado 2025); Bioceânica Ilhéus–Chancay; definição e-SFI/MOEDALOG.
   - `PROJETO BÁSICO MOEDALOG.pdf` (pdftotext): selo passivo, 10 níveis de segurança, custo R$ 1,88 (licitação 1,38 + estatal 0,50), ICP-Brasil/blockchain/eFuse, "certidão de nascimento" na CMB.
   - `PROJETO Digital Logistics Security Blueprint.pptx` (9 slides só-imagem → convertidos soffice→PDF→PNG e lidos por visão): capa, mudança de paradigma, anatomia, tamper-evident, matriz de responsabilidades, matriz 10 níveis, ciclo de vida 7 etapas, viabilidade, soberania.
   - `PROJETO LACRE LOGÍSTICO PARA PRF.pdf`: caso PRF (rastreabilidade, alerta automático, painéis; expansão fronteiras/Mercosul/Chancay).
   - `PROTÓTIPO E PROJETO MOEDALOG.pdf` (2 pranchas renderizadas p/ PNG): memorial de design + desenho de engenharia CAD (cotas, ABS/níquel/aço, Data Matrix, brasão a laser).
   - 3 fotos WhatsApp (GloboNews): "Propostas para as fronteiras" — candidatos 2026 (Lula, Fl. Bolsonaro, Caiado, Renan Santos, Zema, Cury).
4. **Pesquisa web em 4 frentes paralelas (agentes) + verificação direta:**
   - Frentes 1/2/4 completas (portais+bases, centros, geodados). Frente 3 (reguladores/legal) perdeu a 1ª leva p/ timeout; reaberta em 2 agentes de fundo — o agente BR voltou **completo** (27 UFs verificadas + correções: ENCAT→encat.org, EPL/Infra→valec.gov.br, MPA→/portos-e-aeroportos); exterior/legal verificado direto pela sessão pai com curl (~80 URLs; estaduais 000 desta rede → marcadas no anexo c/ fonte do agente BR que as validou).
5. **Entregas escritas:** `portal_logos/PROPOSTA_PORTAL_LOGOS_20260822.md` + `ANEXO_PESQUISA_PORTAL_LOGOS_20260822.md`; Tema Duplo (este fórum+memória); catalogação no NODE_PROJETO_CASA_DA_MOEDA + NODE_ATUALIZACOES.

## 2. Arquivos criados

| Arquivo | Função |
|---|---|
| `Outros/Projeto Casa da Moeda/portal_logos/PROPOSTA_PORTAL_LOGOS_20260822.md` | proposta completa: conceito, uso do material, arquitetura (11 seções), visual/tech, revista, plano 6 fases, decisões p/ Miguel |
| `Outros/Projeto Casa da Moeda/portal_logos/ANEXO_PESQUISA_PORTAL_LOGOS_20260822.md` | tabelas curadas: benchmarks, bases de artigos, centros, reguladores (fed+27UFs+exterior+internac.), legal, geodados, stack de mapas |
| `Cerebro/Foruns/forum_portal_logos_proposta_20260822.md` | este fórum |
| `Cerebro/Memorias/memoria_portal_logos_proposta_20260822.md` | esta memória |

## 3. Estado da missão

**O que aconteceu:** proposta + pesquisa entregues; nenhum código escrito ainda (fase 0 = aprovação).
**O que falta:** respostas do Miguel (nome/domínio, migração do site atual, conselho da revista, prioridade de fases) → então Fase 1 (repo `portallogos` + Vercel + skeleton Astro i18n).
**O que preciso do Miguel:** as 5 decisões do fórum + curadoria visual das URLs "a curar".

## 4. Gotchas permanentes

- Sites estaduais/planalto bloqueiam curl sem UA de navegador ou com timeout curto desta rede — usar UA Chrome + timeout ≥15s ao re-verificar.
- GEM (dutos globais) é CC BY-**NC**-SA: revisar antes de publicar se o portal monetizar.
- OSM tiles oficiais ≠ produção; usar CARTO/MapTiler — no v1 usamos **OpenFreeMap** (tiles vetoriais grátis, sem chave, BSD) que resolve o "tudo grátis".
- `infra.gov.br` morreu; EPL/Infra S.A. = infrasa.gov.br / valec.gov.br. ENCAT = encat.org.

## 5. ADENDO — construção e publicação da v1 (22/08/2026 19:20→20:05 BRT)

**Decisões do Miguel:** tudo grátis · revista = **Logis** (com i) · projeto Vercel = `logis-magazine` · Controle Logístico antigo segue no GitHub/backups (o projeto Vercel só foi renomeado, deploys de 28-29/07 intactos).

**Código criado** (`Downloads/Antigravity Google/logis/`):
| Arquivo | Função |
|---|---|
| `package.json` + `astro.config.mjs` | Astro 5 estático, site logis-magazine.vercel.app |
| `src/content/ui.ts` | NAV 11 itens + strings UI PT/EN/ES + `langPath()` |
| `src/content/pages.ts` | conteúdo trilíngue de todas as páginas (hero/blocos/kpis/timeline) |
| `src/data/hubs.ts` · `reguladores.ts` · `legal.ts` · `pesquisa.ts` | dados curados do anexo (19 hubs + 4 fluxos O-D; 13 fed + 27 UFs + 19 ext + 12 organismos; 11+11 normas; 14 bases + 24 centros + revistas-alvo) |
| `src/layouts/Base.astro` + `Header/Footer/Section.astro` | layout, header sticky c/ seletor PT\|EN\|ES, menu mobile CSS-only, footer 3 colunas |
| `src/pages/[lang]/*.astro` | 11 seções × 3 línguas (getStaticPaths por idioma) + raiz/404 → /pt/ |
| `geomapas.astro` | MapLibre GL 5.6.1 (unpkg) + estilo OpenFreeMap liberty + malha UFs IBGE (v3 c/ fallback v2) + círculos por tipo c/ popup + linhas de fluxo tracejadas |
| `src/styles/global.css` | design system (verde-escuro/lima/areia), cards, tabelas, timeline, kpis, hero |

**Build:** `npm install` (279 pacotes, 28s) + `npm run build` → 35 páginas em 760ms, 508 KB.

**Deploy — LIÇÃO IMPORTANTE (vale p/ todo o ecossistema Vercel):**
1. **Vercel CLI quebrou neste ambiente** (v56 e v59.5.0): "Upload aborted"/AbortError no upload de arquivos mesmo com API saudável (probe curl no /v2/files respondia em <1s). Nem `--archive=tgz` resolveu.
2. **Contorno que funcionou (REST API pura):** (a) `POST https://api.vercel.com/v2/files?teamId=<team>` com headers `x-now-digest: <sha1>`, `x-now-size: <bytes>`, `Content-Type: application/octet-stream` e **body binário puro** (multipart `-F` devolve `invalid_filesize`); (b) `POST /v13/deployments?teamId=<team>` com `{name: <projeto>, target: "production", version: 2, files: [{file, sha, size}]}`. Script completo usado: `/tmp/vercel_deploy_logis.py` (urllib, lê token de `~/.local/share/com.vercel.cli/auth.json`, nunca expõe).
3. **Armadilhas pós-rename de projeto Vercel:** (a) `ssoProtection` estava `all_except_custom_domains` → site pedia login Vercel; removida com `PATCH /v9/projects/{id} {"ssoProtection": null}`; (b) renome NÃO preserva domínio .vercel.app (lista de domínios vazia; URLs antigas 404) → anexar com `POST /v10/projects/{id}/domains {"name": "<nome>.vercel.app"}` (verified: true imediato p/ subdomínio .vercel.app).
4. IDs: projeto `prj_U64icaeaxRVcWIJ0ySDQZluLYLuK` · team `team_QQzbgQTC569AoQxaur7tNLGj` · deployment `dpl_4SAECCoaGzEzkx57QbC6BeBWa5Vo`.

**Verificação final:** 9/9 URLs HTTP 200 (raiz→/pt/ redirect; PT/EN/ES home; geomapas, ideias, reguladores EN, legal ES, revista PT) + presença de MapLibre/ARTESP/MoedaLog no HTML. `controlelogistico.vercel.app` (site antigo, projeto casadamoeda) segue no ar — intacto.

**O que falta / próximos passos:** repo GitHub próprio do portal (token `gh` do Dell expirou — renovar ou criar via web) + git init no `logis/`; camadas DNIT/ANTT completas nos geomapas (Fase 2); nº 1 da Logis; domínio próprio quando o Miguel quiser.
**O que preciso do Miguel:** decidir se quer domínio próprio (.com/.com.br); renovar `gh auth` quando puder (não bloqueia nada hoje — deploy vai pela API).

## 6. ADENDO — responsável editorial da Logis (22/08/2026 ~20:10→20:20 BRT)

**Ordem do Miguel:** sem conselho editorial por ora; "botar só responsável Miguel do Rosário"; ele dará o número profissional de jornalista depois e pediu para ser cobrado.

**Mudança:** `src/content/pages.ts` — bloco novo (primeiro dos `blocos`) na seção `revista` dos 3 idiomas:
- PT `{ t: 'Responsabilidade editorial', x: 'Jornalista responsável: Miguel do Rosário.' }`
- EN `{ t: 'Editorial responsibility', x: 'Editor-in-chief: Miguel do Rosário.' }`
- ES `{ t: 'Responsabilidad editorial', x: 'Director responsable: Miguel do Rosário.' }`

**Publicação:** `npm run build` (35 páginas, 1.04s) → deploy REST API (`/tmp/vercel_deploy_logis.py`): 37 arquivos enviados, `dpl_2w2U67hSrtbxcWV1tve2JLJgev6E` READY, alias `https://logis-magazine.vercel.app`. Verificação em produção: `/pt/revista/`, `/en/revista/`, `/es/revista/` → HTTP 200 + grep confirmou o texto nos 3 idiomas.

**🔔 COBRAR DO MIGUEL DEPOIS (pedido explícito dele, "me cobra depois"):** o **número profissional de jornalista** para inserir no bloco de responsabilidade editorial da Logis e republicar.

## 7. ADENDO — gh renovado + repo portallogos + achado de contaminação (22/08/2026 ~20:25→20:45 BRT)

**1. `gh` renovado:** token antigo inválido (401 Bad credentials — "The token in keyring is invalid"). Device flow: `gh auth login --hostname github.com --git-protocol https --web` (1ª tentativa expirou — o fluxo tem deadline interno curto; na 2ª o Miguel aprovou o código `19C6-3659` em github.com/login/device). Resultado: logado como migueldorosario1, escopos `gist, read:org, repo`, git protocol https.

**2. Repo do portal:** `git init` em `logis/` (git antigo do Dell não tem `init -b`; usar `git symbolic-ref HEAD refs/heads/main`), identidade local "Miguel do Rosário" + `63256060+migueldorosario1@users.noreply.github.com`, commit `a592a20` (29 arquivos; stage conferido sem `.env*`/node_modules/dist). `gh repo create portallogos --public --source=. --remote=origin --push` → criado PÚBLICO (convenção dos sites; cérebro/infra = privados) e **renomeado em seguida para `logis`** por ordem do Miguel (~20:50): "o nome é logis com i! não é logos com o". `gh repo rename logis --repo migueldorosario1/portallogos --yes` + `git remote set-url origin https://github.com/migueldorosario1/logis.git` + push testado ("Everything up-to-date"). Repo final: **https://github.com/migueldorosario1/logis**.

**3. 🔴 Contaminação descoberta (BUG-20260822-ANTIGRAVIDADE-GIT-FILHOSDAIMPUNIDADE no NODE_BUGS_ATIVOS):** `git rev-parse --show-toplevel` de dentro de `logis/` = `/home/migueldorosario/Downloads/Antigravity Google/` — a pasta INTEIRA é checkout git, branch `deploy-main`, origin `filhosdaimpunidade.git` (PÚBLICO). Commits dos loops lá: HEAD `4279f848` CM-033 (22/08 09:57, 1 à frente de origin/main = ainda não pushado); origin/main já tem CM-007/009/032, GM-001, ponto_retomada Trindade, PILOTO-GEO (desde ≥20/08). `git status` mostra Cérebro rastreado+alterado; `.git/` mtime 20:39 durante a investigação = sessão ativa usando o checkout. **Nenhum comando de escrita foi executado naquele repo.** Repo do portal criado aninhado (`logis/.git` próprio) — isolado; o repo-pai passa a ver `logis/` como diretório com git interno (não rastreado: `?? ./`). Gotcha: quem rodar `git add -A` no repo-pai vai capturar `logis/` como gitlink.

**4. Comandos-chave (referência futura):** `gh auth status` (diagnóstico) · device flow acima (renovação) · `gh repo create <nome> --public|--private --source=. --remote=origin --push` (repo+push em 1 comando) · `git ls-files | wc -l` / `git rev-parse --show-toplevel` (detectar repo aninhado/contaminação).

## 8. ADENDO — seção Segurança Pública & Controle Logístico (22/08/2026 ~20:55→21:10 BRT)

**Ordem do Miguel:** segurança pública = um dos centros do projeto; tese abertura×controle (PNL Lula + Chancay + transoceânica → risco de pirataria/contrabando/drogas/armas → governo precisa oferecer programa de controle logístico junto à abertura); comparação internacional; solução tecnológica brasileira (chip/selo); usar o print GloboNews "Propostas para as fronteiras" (TSE 2026) com a proposta de Lula.

**Prints lidos por visão** (`novos edson/WhatsApp Image 2026-08-21 at 15.53.49*.jpeg`, 3 telas GloboNews): Lula = Forças Armadas nas fronteiras amazônicas + patrulhamento fluvial/aéreo · cooperação OTCA · radares, drones, sensores, satélite + centros integrados de comando e controle. Demais candidatos (Fl. Bolsonaro, Caiado, Renan Santos, Zema, Cury) confirmam consenso do tema.

**Arquivos tocados:** `src/content/ui.ts` (NAV +1: seguranca), `src/content/pages.ts` (interface PROG + entrada `seguranca` 3 idiomas: kpis, 4 blocos, 7 programas, nota, cta; card Confiança da home atualizado nos 3 idiomas), `src/pages/[lang]/seguranca.astro` (novo: hero+kpis, cards, tabela programas, nota, cta).

**URLs verificadas por HTTP (UA Chrome, -L):** wcoomd.org 200 · cbp.gov/.../ctpat 200 · taxation-customs.ec.europa.eu/index_en 200 · sat.gob.mx/.../neec 200 · dian.gov.co/aduanas/oea/... 200 · customs.gov.sg 200 · customs.go.jp/english 200. (404s encontrados e descartados: URLs antigas de AEO-UE/SAFE-WCO/AEO-Japão/STP — usei as páginas institucionais 200.)

**Build/deploy/verificação:** 38 páginas (879ms) → deploy REST API READY ~21:04 → /pt|en|es/seguranca/ HTTP 200 + presença de OTCA/C-TPAT/SAFE/Forças Armadas no HTML + títulos corretos nos 3 idiomas. **Commit+push no repo logis:** `1f07e78`.

## 9. ADENDO — portal renomeado LOGIS + revista expandida (22/08/2026 ~21:10→21:20 BRT)

**Ordem do Miguel:** "fazer o portal logis, logística e sustentabilidade... dentro do portal, cria uma parte da revista logis" → marca do portal = **LOGIS** (LOGOS aposentado como marca do site); revista Logis = parte editorial do portal.

**Mudanças de código:**
- `grep -rl '— LOGOS' | xargs sed -i 's/— LOGOS/— LOGIS/g'` nos títulos das 12 páginas; `SITE_NAME='LOGIS'`; rodapés PT/EN/ES ("LOGIS — Portal de Logística e Sustentabilidade" / "Logistics and Sustainability Portal" / "Portal de Logística y Sostenibilidad"); títulos da home e do institucional nos 3 idiomas; comentário do astro.config. 24 ocorrências, zero residuais (só o nome do arquivo ANEXO_PESQUISA_PORTAL_LOGOS_20260822.md ficou — é nome de arquivo real).
- Revista: +2 blocos × 3 idiomas — **Edições** (nº 1 4º tri 2026; dossiê corredores×controle: Chancay/bioceânica/fronteiras abertas — amarra com a seção Segurança) e **Submissões** (chamada no portal; artigos 6-10k, estudos de caso 4-6k, notas de dados 2-4k palavras; PT/EN/ES).

**Verificação:** build 38 páginas → deploy READY ~21:17 → homes/revistas 3 idiomas 200; "LOGIS — Logística e Sustentabilidade"/"Logistics and Sustainability"/"Logística y Sostenibilidad" presentes; LOGOS residual 0; Edições/Submissões/Issues/Submissions/Ediciones/Envíos presentes. **Commit+push: `d5c0e10`.**

**Lições:** (a) Edit do tool quebra depois de sed no mesmo arquivo — re-Read antes de Editar; (b) para trocar marca em site estático: grep case-insensitive primeiro p/ achar menções em corpo de texto, depois sed em lote + verificação de residuais no build E na produção.

## 10. ADENDO — 3 frentes: submenus+home limpa, geomapas internacionais, boneca da revista (22/08/2026 ~21:45→22:05 BRT)

**Arquivos tocados:**
| Arquivo | Mudança |
|---|---|
| `src/content/ui.ts` | +`NAV_GROUPS` (6 grupos c/ children) — NAV flat mantida p/ Footer |
| `src/components/Header.astro` | nav desktop c/ dropdowns (`li.has-sub > ul.sub`, hover/focus-within) + mobile agrupado |
| `src/styles/global.css` | dropdowns, `.mm-group`, `a.card.link`, `.map-controls`, `.download-box` |
| `src/pages/[lang]/index.astro` | home limpa (sem KPIs; cards de grupo viram links) |
| `src/data/worldLayers.ts` | NOVO — 51 rotas mundiais esquemáticas (5 categorias + CAT_STYLE) |
| `src/pages/[lang]/geomapas.astro` | vista mundial + camadas por categoria + toggles + legenda + popups |
| `src/pages/[lang]/revista.astro` | + bloco de download da boneca (3 idiomas) |
| `public/downloads/logis-edicao-0-boneca.pdf/.html` | NOVO — boneca 52 pp vetoriais + fonte HTML |

**Boneca (skill de PDF, rota Creative):** gerador `/tmp/gera_boneca_logis.py` (templates de página + pool de parágrafos temáticos + autores/afiliações fictícios; seed=7) → `/tmp/boneca_logis.html` (52 páginas A4, CSS: capa verde-950, divisores, 2 colunas, pullquotes, sidebars, gráficos de barras CSS, tabela de normas, entrevista) → `html2pdf-next.js` → PDF vetorial 264 KB (~10.900 palavras). Validação: `poster_validate.py check-html` (só warnings esperados) + visão em 3 páginas (capa/artigo/gráfico OK). **Aviso de ficção no rodapé de todas as páginas** e no expediente.

**Gotchas técnicos (novos, permanentes):**
- Linhas MapLibre cruzando a linha de data: usar longitude contínua >180 (ex.: LA = 241.8) na mesma LineString; salto +179→-170 desenha o caminho errado.
- `html2pdf-next.js`/skills de PDF neste Dell: playwright npm faltando, mas browsers em `~/.cache/ms-playwright` — solução: `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm i playwright pdf-lib` em `/tmp/pw` + symlink `node_modules` dentro de `$PDF_SKILL_DIR/scripts/` (require resolve a partir da pasta do script; NODE_PATH não serve p/ ESM).
- grep -c em HTML minificado conta LINHAS, não ocorrências — usar `grep -o ... | wc -l`.
- Edição grande em pages.ts: cuidado ao substituir blocos de 3 idiomas — sobras órfãs quebram o parse (aconteceu com blocos ES; detectado no build e corrigido).

**Verificação:** homes/geomapas/revista 200 ×3 idiomas; 0 KPIs na home; 3 submenus; 13 rotas mundiais no HTML; 6 toggles; PDF 200 application/pdf 270171 B. Commit `fb39cef`.

## 11. ADENDO — backup 3 camadas + espelho congelado (22/08/2026 ~22:03→22:10 BRT)

**Espelho:** `/tmp/vercel_deploy_logis.py` parametrizado (argv[1] = nome do projeto) → `python3 ... logis-mirror` criou o projeto Vercel `logis-mirror` + deploy `dpl_Fvrq1v1esQvrcqYV1sa8Fz1sEBP2` (alias `logis-mirror.vercel.app` veio automático; projeto novo nasce público, sem ssoProtection — verificado com 200 direto). Comparação md5 das páginas espelho×principal: IDÊNTICAS (pt/, en/, geomapas, revista, segurança, PDF). **Espelho fica congelado** — não recebe updates.

**Tarball:** `Outros/Projeto Casa da Moeda/backups/logis_backup_2026-08-22_fb39cef.tar.gz` — `tar czf ... --exclude='logis/node_modules' --exclude='logis/.astro' logis` (1,17 MB; inclui .git inteiro + dist + PDFs).

**Rollback how-to (futuro):** (a) curto prazo: usar o espelho `logis-mirror.vercel.app` como referência/para; (b) restauração: extrair tarball OU `git clone migueldorosario1/logis` no commit `fb39cef` → `npm install && npm run build` → `python3 /tmp/vercel_deploy_logis.py logis-magazine`; (c) nativo Vercel: re-promover deployment imutável de 21:59 (API: POST /v12/deployments/{id}/aliases?projectId ou painel → Promote).
