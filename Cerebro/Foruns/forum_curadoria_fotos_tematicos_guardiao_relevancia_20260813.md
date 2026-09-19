# Fórum — Curadoria de fotos dos sites temáticos + guardião de relevância de hero

**Data:** 2026-08-13 ~19:59 BRT · **Sessão:** ZCode (GLM-5.2) · **Gatilho:** ordem do Miguel ao ver foto errada no ceara.digital
**Tag:** `ZCODE-CURADORIA-FOTOS-TEMATICOS-GUIA-RELEVANCIA-20260813-1959-BRT`
**Relacionados:** `forum_auditoria_v4_*_20260813`, `forum_banco_links_midia_jornalistica_20260813`, `forum_diretriz_correcao_posts_ssh_wpcli_trindade_20260813`

---

## O que aconteceu (resumo executivo)

O Miguel apontou que o post **"Atlas Intel: Ciro lidera com 49,3% e Elmano tem 44,6% no Ceará"** (ceara.digital) estava com **foto errada**: uma imagem de **reflorestamento no Acre** (crédito "Ministério da Ciência, Tecnologia e Inovação"), totalmente alheia à matéria eleitoral. E pediu: **"o ceará digital tem que ter uma boa curadoria de fotos, assim como todos os sites temáticos".**

Foram feitas duas coisas: **(A) correção imediata do post** e **(B) guardião de relevância sistêmico** para os 8 sites temáticos.

## Descoberta de arquitetura

`ceara.digital` **NÃO é WordPress** — é site **Astro + Vercel** (deploy via `git push` no repo `sites-v4/ceara`, remote `ceara-v4`). O hero é um arquivo local em `public/hero/`, referenciado no frontmatter (`heroImage`, `hero_credit`, `hero_legenda`). Logo, a correção NÃO usa SSH+WP-CLI (que é só do canônico `ocafezinho.com`); é editar markdown + trocar arquivo + push → Vercel redeploy. Os 8 temáticos seguem o mesmo padrão (um repo em `sites-v4/<site>`, motor em `agentes_tematicos/v4/`).

## Causa raiz (sistêmica, `agentes_tematicos/v4/publicador.py`, função `_buscar_hero`)

1. **Gate de relevância fraco** (`publicador.py` ~L394): exigia **só 1 token de 4+ caracteres** do termo de busca no título do arquivo do Commons. O termo trazia "pesquisa" (pesquisa eleitoral), que casou com "Núcleo de Apoio à **Pesquisas** do INPA" (reflorestamento) → passou.
2. **Juiz visual calibrado para aprovar em dúvida** (`nucleo_visao.py` L64, remédio do bug #34 de super-rejeição) + **fail-open** se Gemini/Qwen-VL caírem → disparate bonito escorapa.
3. **Agravante descoberta:** as fotos "do Ciro 2026" já no disco eram **stock do Pixabay** ("Photo by MAURICIO_BR on Pixabay", "renatolaky on Pixabay") — **não são o Ciro de verdade**. Problema correlato (FASE B/cascata), não resolvido neste sprint.

## (A) Correção imediata do post — ✅ CONCLUÍDO E NO AR

- **Hero trocado:** `public/hero/atlas-intel-ciro-lidera-com-49-3-e-elmano-tem-44-6-no-ceara.jpg` (reflorestamento) → foto real de campanha do **Ciro Gomes em Caxias (MA), 2018**, **Julimar Silva, Wikimedia Commons, CC BY 3.0** (licença limpa, sem NC/ND, 1728×972 → padronizada 1200×675 blur-fill).
- Frontmatter atualizado (`heroImage` no mesmo caminho; `hero_credit` e `hero_legenda` reescritos).
- **Commit `4e093ef`** + push no `ceara-v4` (HEAD==origin). Deploy Vercel **confirmado ao vivo** (curl mostra "Ciro Gomes em campanha / Caxias / Julimar Silva", sem "reflorestamento").
- Backups: `Projeto Cafezinho Agentes/agent_data/backups_ceara_heroes/` (jpg+md `.bak_pre_hero_20260813_1949`).
- **Nota editorial:** não existe foto recente (≤3 anos) do Ciro com licença limpa no Commons; as únicas de 2026 no disco eram stock Pixabay (não o Ciro). Usada a **melhor foto REAL e licenciada** disponível (campanha 2018) — limite conhecido sinalizado ao Miguel.

## (B) Guardião de relevância — ✅ IMPLEMENTADO E VALIDADO (determinístico)

Patch em `publicador.py` + `nucleo_visao.py` (`.bak_pre_guardiao_20260813_1956/1957`):

1. **Helper `_entidades_titulo()`** (`publicador.py`): extrai **nomes próprios + acrônimos** do título da matéria (sinal forte: Ciro, Elmano, Ceará, Atlas, Intel; PT, PSDB, INPA, TRE…), com stoplist de descritores genéricos (Pesquisa, Governo, Eleição…).
2. **Gate por entidade** em `_buscar_hero` (FASE A/Commons): se a matéria nomeia entidades, **exige ≥1 entidade no título do arquivo**; sem entidades, mantém o gate genérico (1 token) — sem regressão.
3. **Cláusula anti-disparate no juiz** (`nucleo_visao.py`): novo item "PESSOA/LOCAL NOMEADO, OUTRO ASSUNTO" na lista de REJEITE (aditivo; **não** mexe na calibração "em dúvida aprove" → não reativa bug #34).
4. **Validado:** entidades {atlas, ceara, ciro, elmano, intel}; reflorestamento **REJEITADO**; foto do Ciro **ACEITA**; caso genérico cai no fallback (sem regressão). `py_compile` verde nos 2 arquivos. A cascata (FASE B) garante que **nenhum post fica sem imagem**.

## Estado da missão

- **Feito:** post corrigido e no ar; guardião determinístico + cláusula no juiz implementados, validados e ativos localmente (o cron dos temáticos roda neste dir).
- **Falta / próximo:** (1) **sync do patch p/ o espelho NYC** se houver gêmeo do motor rodando lá (confirmar onde o cron V4 roda de fato); (2) resolver o **stock Pixabay ≠ pessoa real** (FASE B/cascata) — exige checagem de identidade ou restringir stock a temas sem pessoa nomeada; (3) **auditoria** dos heroes recentes (7–15 dias) dos 8 temáticos buscando outras fotos erradas (follow-up, faço se o Miguel pedir); (4) melhorar a **geração do `visual_prompt`** no `produtor.py` para já incluir o nome da pessoa (defesa em profundidade).
- **Preciso de você (Miguel):** confirmar se a foto de campanha 2018 agrada (ou se prefere outra abordagem p/ o Ciro); e dizer se quer a auditoria de heroes antigos agora.
