# 🏛️ Fórum — Revista Maquiavel: entrada no portfólio + plano de trabalho (artigos científicos BR & mundo)

**Data:** 2026-08-17 ~01:00–01:40 BRT
**Sessão:** ZCode (workspace ZCodeProject), a pedido do Miguel ("vamos dar continuidade a ela")
**Tema-mãe:** nodo `CEREBRO_NODE_REVISTA_MAQUIAVEL.md` · fórum fundador `Foruns/forum_revista_maquiavel_20260730.md` · rodada Trindade `Foruns/forum_maquiavel_rodada_trindade_20260801.md`
**Memória pareada:** `Memorias/memoria_revista_maquiavel_portifolio_plano_20260817.md`

---

## 1. Estado encontrado (auditoria 01:05 BRT)

| Item | Estado |
|---|---|
| Site | ✅ no ar — `https://revistamaquiavel.vercel.app` — EN/PT/ES HTTP 200 (~0,8s) |
| Repo | ✅ `Revista Maquiavel/maquiavel` limpo e sincronizado com `origin/main` (GitHub `migueldorosario1/maquiavel`, branch `main`, webhook git→Vercel ativo) |
| Último commit | `4c513f4` 03/08 12:37 (fix acervo RBCP + sentence case BR) |
| Identidade visual | ✅ aplicada 01–03/08 (4 commits: direção Renascença, emblema gráfico, painel editorial multi-coluna, logo lockup + Miguel do Rosário na página About) |
| Conteúdo | ⚠️ **só o ensaio fundador** ("Why a Journal Named Machiavelli?" em 3 línguas) — é isso que o plano resolve |
| Automação | ⚠️ esqueleto `agentes/maquiavel_agente_curador.py` documentado + `fontes_curadoria.json` (10 fontes com status legal) — **sem cron, sem AUTH** (desenho correto, aguardando este plano) |
| Acervo | ✅ v1: 77 entradas (13 revistas BR, 20 mundo, 16 repositórios, 24 universidades, 8 substacks, 10 vídeos) |
| Rodada Trindade (01/08) | ⚠️ convocada mas **sem respostas registradas** — todas as seções "(aguardando)" |
| Sitemap | ❌ 404 — site não tem `@astrojs/sitemap` (afeta SEO e leitura pelo painel CCTV) |

**Conclusão:** a revista está 100% pronta de infraestrutura e identidade; falta conteúdo e o motor de curadoria. Perfeita para retomar.

## 2. O que foi feito hoje — entrada no portfólio Cafezinho Media Group

1. ✅ **Registry oficial dos temáticos** (`Projeto Cafezinho Agentes/root/ferramentas/sentinela_tematicos/site_registry.json`): 9º site `revista_maquiavel` — cadência `semanal`, limiar 192h, métrica `git_commit` (home não expõe datas). Backup `.bak_pre_maquiavel_20260817`.
2. ✅ **`CEREBRO_INDEX_SATELITES.md`**: seção própria "Revista Maquiavel" + override do topo atualizado (oito → nove sites, exceção de repo registrada).
3. ✅ **`CEREBRO_NODE_ECOSSISTEMA_CANONICO.md`**: linha nova na tabela 1.2 (face visível) + vigência + nota de exceção do repo.
4. ⏸️ **Painel CCTV / Central dos Temáticos (Tencent): ADIADO por colisão.** Às 01:12, outra sessão estava editando `painel_cctv_v6.py` (backup `bak_pre_custos_brl_ranking_20260817` + serviço reiniciado 01:13). Regra do monitor: não pisar em arquivo ocupado. **Entrada pronta para aplicar quando o arquivo liberar** (ver §6).

## 3. Plano de trabalho — atualizar a revista com artigos científicos BR & mundo

**Conceito operacional:** a Maquiavel publica **3 formatos**:
- **Curadoria integral traduzida** — artigo acadêmico com licença aberta (CC BY/BY-SA/BY-NC), adaptado em formato ensaístico nas 3 línguas, com DOI + crédito + link canônico. É o coração da revista ("varrer o Brasil e o mundo de artigos inteligentes", ordem original do Miguel).
- **"Lido na Maquiavel"** — resenha crítica curta + link para fontes sem licença de tradução (CC BY-ND, paywalls, Foreign Affairs etc.).
- **Ensaios originais** — da casa (Miguel + agentes sob revisão), como o fundador.

**Regra absoluta (herdada do ecossistema):** agente **não publica**. Agente gera rascunho em branch `rascunhos`; Miguel (ou quem ele delegar) aprova → merge na `main` → Vercel publica via webhook. Fact-check com websearch real antes de qualquer merge.

### Fase 1 — Base de fontes científicas (próxima sessão, ~1 sprint)

Expandir `agentes/fontes_curadoria.json` (hoje 10 fontes) com os motores de descoberta e periódicos-alvo, verificando licença NA PÁGINA de cada um antes de usar:

**Motores de descoberta (meta-fontes):**
| Fonte | Por quê | Licença esperada |
|---|---|---|
| SciELO OAI-PMH (`scielo.br/oai/`) | API de coleta de todos os periódicos SciELO | CC BY na maioria |
| DOAJ (Directory of Open Access Journals) | filtro por disciplina "Political Science" → lista mundial de revistas CC | metadado de licença por revista |
| Redalyc | LatAm/ES — equivalente ao SciELO | aberto (verificar por revista) |
| BDTD/CAPES | teses e dissertações BR em ciência política | resenha+link (direito autoral do autor) |

**Periódicos brasileiros (alvo curadoria integral, via SciELO):**
`Brazilian Political Science Review` (ABCP) · `DADOS` (IESP-UERJ) · `Lua Nova` (CEBRAP) · `Opinião Pública` (CESOP/Unicamp) · `Contexto Internacional` (PUC-Rio) · `Revista de Sociologia e Política` (UFPR) · `Política & Sociedade` (UFSC) · `RAP — Revista de Administração Pública` (FGV) · `Cadernos EBAPE.BR` (FGV) — **licença de cada um a confirmar na página antes do 1º uso** (regra 1 do fontes_curadoria).

**Periódicos/fontes internacionais (acréscimos aos já cadastrados):**
`E-International Relations` (open access, verificar CC) · `The Conversation` demais edições (ES/FR/CA/AU) · `Chatham House`, `Brookings`, `Carnegie`, `IPEA`, `CEBRAP`, `FGV` (relatórios abertos = resenha+link) · `Nueva Sociedad` e `Revista de Ciencia Política` (já cadastradas) · periódicos APSA/Cambridge/Oxford = **só resenha+link** (paywall).

**Tarefas técnicas da Fase 1:**
- [ ] Verificar licença nas páginas dos periódicos acima e cadastrá-las no `fontes_curadoria.json` (campo `licenca` + `acao`).
- [ ] Instalar `@astrojs/sitemap` no repo (SEO Google + leitura pelo painel CCTV) — commit pequeno.
- [ ] Expandir `src/data/acervo/` com os periódicos novos (acervo é vitrine pública: toda fonte curada deve estar lá).

### Fase 2 — Piloto do agente curador (semi-automático, ~1 semana)

Implementar de fato o `maquiavel_agente_curador.py` (esqueleto já desenhado), em etapas curtas:

1. **Coleta:** SciELO OAI-PMH + feeds já mapeados (`theconversation.com/articles.atom`, LSE, ECPR Loop) → banco local `agent_data/maquiavel_coleta.jsonl`.
2. **Gate de escopo:** LLM classifica "ciência política?" (comunicação/sociologia/IA só como fenômenos do poder — manifesto v0.2) → descarta fora de escopo.
3. **Gate de licença:** cruza com `fontes_curadoria.json`; só avança curadoria integral com licença permissiva; ND/paywall → formato "Lido na Maquiavel".
4. **Seleção ensaística:** LLM ranqueia por relevância/qualidade (nota ≥ corte, como na Manchete).
5. **Produção trilíngue:** adaptação ensaística EN/PT/ES (não tradução literal — a revista é ensaística), com `par_trilingue`, `fonte_curadoria`, `licenca_fonte`, `doi`, autor original.
6. **Fact-check** com websearch real (regra consolidada do ecossistema).
7. **Commit na branch `rascunhos`** + aviso ao Miguel (Telegram/ZCode) para revisão.
8. **Dedup:** registry `agent_data/curadoria_ja_usada.json` (URL canônica + DOI).

**Cadência proposta do piloto:** 2–3 artigos/semana (1 curadoria + 1 resenha + eventual original), sem cron até o piloto provar qualidade — rodadas manuais disparadas por mim a pedido do Miguel.

### Fase 3 — Regime contínuo + divulgação (após 2–3 semanas de piloto aprovado)

- Cron diário de coleta + fila (padrão V4, executor a definir: NYC ou local) — **só depois do piloto aprovado pelo Miguel**.
- Divulgação cruzada: O Cafezinho (teaser PT + link, padrão Revista Fórum) · GSN (EN) · Moka (sinergia O Príncipe/Biblioteca Livre).
- Página "Curation" já prevista no manifesto identifica publicamente o que é curadoria traduzida.

### Fase 4 — Trilha científica (médio prazo, quando houver corpo editorial)

ISSN via IBICT (exige periodicidade documentada + conselho editorial) → DOI/Crossref → revisão por pares → Qualis. A Fase 2–3 constrói o lastro (corpo, regularidade, reputação) que o IBICT exige. Sem promessa pública de credenciamento antes de obtê-lo (regra do nodo).

## 4. Decisões que preciso do Miguel

1. **Cadência inicial:** 2–3 artigos/semana no piloto está bom? (sugestão: sim)
2. **Fluxo de revisão:** eu mando os rascunhos prontos (3 línguas) aqui/ZCode e você dá o "merge"? Ou delega ao Loop Miguel/Claude?
3. **Prioridade da Fase 1:** começar pelos periódicos BR (SciELO) ou equilibrar BR+mundo desde a primeira rodada?
4. **Domínio próprio:** `revistamaquiavel.vercel.app` segue provisório; pesquisar `revistamaquiavel.com/.com.br/.org` quando você quiser.

## 5. Pendências herdadas

- **Rodada Trindade 01/08 sem respostas:** as contribuições dos agentes nunca chegaram ao fórum da rodada. Opção: re-convocar na Fase 1 (fontes é exatamente o que se pediu) ou encerrar a rodada e seguir sozinho. Sugestão: encerrar — o plano acima cobre o que se pedia.
- **Visual Antigravity:** a identidade foi aplicada 01–03/08; se o Miguel quiser refinamento, o brief `docs/PROMPT_ANTIGRAVITY_VISUAL.md` continua no repo.

## 6. Coordenação — entrada pronta para o painel CCTV (aplicar quando liberar)

Às 01:12 de 17/08 a sessão do sprint "custos BRL ranking" ocupava `painel_cctv_v6.py` (Tencent). Quando o arquivo liberar, aplicar no dict `TEMATICOS` (~linha 1538) + backup `.bak_pre_maquiavel_<data>` + restart do `cctv-v6.service`:

```python
"maquiavel": {
    "nome": "Revista Maquiavel", "url": "https://revistamaquiavel.vercel.app", "icone": "🏛️",
    "desc": "Revista internacional de ciência política — ensaios trilíngue (en/pt/es)",
    "post_re": r"/(essays|pt/ensaios|es/ensayos)/[a-z0-9-]+",
    "agentes": ["Agente Curador Maquiavel (Fase 2 do plano 17/08/2026)"],
},
```

Sem `ga4` (propriedade ainda não existe). Posts detectados via fallback de homepage até o sitemap existir (Fase 1).

## 7. Próximo passo imediato

Com o "vai" do Miguel (ou direto, se ele aprovar o plano): **Fase 1** — verificação de licenças + cadastro das fontes + sitemap.

— ZCode, 17/08/2026 ~01:40 BRT
