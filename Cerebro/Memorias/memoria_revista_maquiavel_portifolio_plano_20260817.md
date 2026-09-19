# 🧠 Memória Técnica — Revista Maquiavel: portfólio Cafezinho Media Group + plano de trabalho — 2026-08-17

**Sessão:** ZCode (workspace ZCodeProject), 17/08/2026 ~01:00–01:40 BRT
**Pedido do Miguel (literal):** "procura um site temático que eu comecei a fazer, que era a revista maquiavel. vamos dar continuidade a ela. acrescenta ela no portfólio do cafezinho media group, e faz um plano de trabalho para a gente atualizar ela, com artigos cientificos brasileiros e mundiais que a gente pesquisa na internet."
**Fórum pareado:** `Foruns/forum_revista_maquiavel_plano_trabalho_20260817.md`
**Nodo:** `CEREBRO_NODE_REVISTA_MAQUIAVEL.md`

---

## 1. Auditoria do estado (provas)

- `curl` 01:06 BRT: `revistamaquiavel.vercel.app` = HTTP 200 (EN, 0,77s), `/pt/` 200, `/es/` 200. Título PT: "Home — Maquiavel".
- `git log` local: 9 commits; último `4c513f4` (03/08 12:37, "fix(acervo & i18n): fix RBCP journal link to UnB and enforce Brazilian sentence case capitalization"); `git status`: `main...origin/main` limpo; `git ls-remote origin main` = mesmo SHA.
- Commits pós-fundação (identidade visual, 01–03/08): `97974a4` identidade completa direção Renascença (01/08 10:59) · `187d75c` emblema gráfico + painel multi-coluna (02/08) · `6bbe8c8` logo lockup + Miguel do Rosário no About + e-mail (02/08) · `4c513f4` fix acervo RBCP (03/08).
- Estrutura do repo: Astro 5 i18n (`/`, `/pt/`, `/es/`), conteúdo em `src/content/artigos/{en,pt,es}/` (só o ensaio fundador), acervo em `src/data/acervo/*.json` (6 arquivos), `agentes/fontes_curadoria.json` (10 fontes + 6 regras operacionais), `agentes/maquiavel_agente_curador.py` (esqueleto), `docs/manifesto_editorial.md`, `docs/DECISOES_VISUAIS.md`, brand SVGs em `public/brand/`.
- Home NÃO expõe datas (`grep datetime|datePublished|ISO` vazio) → métrica de frescor `git_commit`.
- `sitemap-0.xml` = 404 (sem `@astrojs/sitemap`).
- Rodada Trindade 01/08: fórum `forum_maquiavel_rodada_trindade_20260801.md` com todas as 10 seções de resposta "(aguardando)".

## 2. Alterações feitas (arquivos tocados)

| Arquivo | Mudança | Backup |
|---|---|---|
| `Projeto Cafezinho Agentes/root/ferramentas/sentinela_tematicos/site_registry.json` | + entrada `revista_maquiavel` (url `https://revistamaquiavel.vercel.app`, repo `Revista Maquiavel/maquiavel`, cadência `semanal`, limiar 192h, `git_commit`, `ativo`); `atualizado_em` 2026-08-07→2026-08-17 | `.bak_pre_maquiavel_20260817` (mesma pasta); JSON validado c/ python3 (9 sites) |
| `Cerebro/CEREBRO_INDEX_SATELITES.md` | + seção "Revista Maquiavel" em Portais atuais; override do topo: oito → nove sites + exceção de repo | git do Cérebro (sync padrão) |
| `Cerebro/CEREBRO_NODE_ECOSSISTEMA_CANONICO.md` | linha nova na tabela 1.2 + vigência 17/08 + ajuste do texto "repositórios exclusivos sites-v4" com exceção registrada | idem |
| `Cerebro/Foruns/forum_revista_maquiavel_plano_trabalho_20260817.md` | novo (plano completo) | — |
| esta memória | nova | — |
| `Cerebro/CEREBRO_NODE_REVISTA_MAQUIAVEL.md` | atualização de status + ponteiro + log (logo a seguir) | — |

**NÃO tocado (decisão registrada):** `painel_cctv_v6.py` no Tencent — às 01:12 havia sessão ativa no arquivo (backup `painel_cctv_v6.py.bak_pre_custos_brl_ranking_20260817` criado 01:12 + serviço `cctv-v6` reiniciado 01:13, `ps` PID 2738348). Regra do monitoramento de trabalho: não editar arquivo ocupado. Entrada TEMATICOS pronta no fórum §6 para aplicar depois.

## 3. Decisões técnicas tomadas

1. **Métrica de frescor `git_commit`** — home não expõe datas (prova acima); igual a aiatolah/mapario.
2. **Cadência `semanal` + limiar 192h no sentinela** — revista é online contínua mas ainda sem automação; limiar 48h geraria falso alerta imediato (último commit 03/08).
3. **Repo permanece em `Revista Maquiavel/maquiavel`** — exceção à regra "repos ativos só em sites-v4/" justificada: projeto anterior à regra (30/07 vs 11/08), é revista ensaística (não site V4 orquestrado), e mover repo agora arriscaria `.vercel`/webhook sem ganho. Exceção registrada nos 3 documentos; se o Miguel quiser padronizar, é sprint pequeno futuro.
4. **Agente não publica** — branch `rascunhos` + aprovação do Miguel + merge = publicação via webhook. Padrão do ecossistema (publish só humano/loop designado).
5. **Formatos editoriais:** curadoria integral traduzida (só licença permissiva, DOI+crédito) · "Lido na Maquiavel" (resenha+link p/ ND/paywall) · ensaios originais.

## 4. Comandos/provas reutilizáveis

```bash
# SSH Tencent: ssh tencent (43.156.151.165:38422, user ubuntu)
# Painel: /home/ubuntu/cafezinho/v6/painel_cctv_v6.py · serviço cctv-v6.service
# Dict TEMATICOS ~linha 1538 (verificar na hora de aplicar — arquivo é editado por outras sessões)
curl -s -o /dev/null -w "%{http_code}\n" https://revistamaquiavel.vercel.app/   # 200 em 01:06
cd "Revista Maquiavel/maquiavel" && git status -sb   # main...origin/main limpo
```

## 5. Estado da missão

- **O que aconteceu:** revista localizada e auditada; portfólio registrado em 3 lugares (registry sentinela, index satélites, nodo ecossistema); plano de trabalho em 4 fases escrito (fórum §3) com lista concreta de periódicos BR (SciELO: BPSR, DADOS, Lua Nova, Opinião Pública, Contexto Internacional, RSP-UFPR, Política & Sociedade, RAP/FGV, EBAPE) e motores de descoberta (SciELO OAI-PMH, DOAJ, Redalyc, BDTD); entrada CCTV preparada.
- **O que falta:** (1) decisões do Miguel (fórum §4: cadência, fluxo de revisão, prioridade BR vs BR+mundo, domínio próprio); (2) aplicar entrada CCTV quando o painel liberar; (3) executar Fase 1 (licenças + fontes + sitemap) com o "vai".
- **O que preciso de você (Miguel):** resposta às 4 decisões do fórum §4 — com "vai" genérico eu começo a Fase 1 pelos periódicos BR (SciELO).

— ZCode, 17/08/2026 ~01:40 BRT
