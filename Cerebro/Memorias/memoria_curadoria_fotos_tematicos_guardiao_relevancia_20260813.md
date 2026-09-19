# Memória — Curadoria de fotos temáticos + guardião de relevância de hero (log técnico)

**Data:** 2026-08-13 ~19:59 BRT · **Sessão:** ZCode (GLM-5.2)
**Fórum gêmeo:** `Foruns/forum_curadoria_fotos_tematicos_guardiao_relevancia_20260813.md`

## Contexto / gatilho
Miguel apontou hero errado no ceara.digital (reflorestamento no Acre em matéria eleitoral Ciro×Elmano) e pediu boa curadoria de fotos em **todos** os sites temáticos.

## Arquitetura confirmada (importante p/ próximas sessões)
- `ceara.digital` = **Astro + Vercel** (NÃO é WP). Repo: `Projeto Cafezinho Agentes/sites-v4/ceara`, remote `git@github.com:migueldorosario1/ceara-v4.git` (branch `main`).
- Posts: `src/content/blog/*.md`; heroes: `public/hero/*.jpg`. Frontmatter: `heroImage`/`hero_credit`/`hero_legenda`.
- **Deploy = `git push` → Vercel constrói** (não há SSH próprio do site; `vercel.json` reescreve `/admin` etc. p/ droplet rio-ag `159.89.185.209:5001`).
- **Corrigir hero de temático ≠ SSH+WP-CLI** (que é só do canônico `ocafezinho.com`). Fluxo temático: editar `.md` + trocar `.jpg` + `padronizar_hero` + commit/push.
- Os 8 temáticos seguem o MESMO padrão (um repo em `sites-v4/<site>`, motor compartilhado `agentes_tematicos/v4/`).
- Motor de imagem ao vivo: `publicador.py::_buscar_hero` (chamado em L731). `agente_kimi_busca_imagem.py` **não** está ligado à produção.

## Causa raiz do bug
`publicador.py::_buscar_hero`, FASE A (Commons): gate exigia 1 token genérico do termo de busca no título do arquivo (`tokens_termo and not any(t in titulo_arq.lower()...)`). Termo trazia "pesquisa" → casou com "Pesquisas do INPA" (reflorestamento). Juiz visual (`nucleo_visao.py`) aprova em dúvida (bug #34) + fail-open → passou. Agravante: heroes "do Ciro 2026" no disco eram stock Pixabay, **não o Ciro real**.

## Arquivos tocados

### (A) Post ceara.digital — correção
- `sites-v4/ceara/public/hero/atlas-intel-ciro-lidera-com-49-3-e-elmano-tem-44-6-no-ceara.jpg` → **substituído** por foto real do Ciro (Caxias/MA 2018, Julimar Silva, CC BY 3.0, baixada do Commons, `padronizar_hero` 1200×675, 291 KB).
- `sites-v4/ceara/src/content/blog/20260813-atlas-intel-...md` → `hero_credit`/`hero_legenda` reescritos.
- **Commit `4e093ef`** (`fix(ceara): troca hero errado...`), push `ceara-v4`, HEAD==origin. Deploy Vercel confirmado (curl: "Ciro Gomes em campanha / Caxias / Julimar Silva").
- Backups: `Projeto Cafezinho Agentes/agent_data/backups_ceara_heroes/*bak_pre_hero_20260813_1949` (jpg+md). `.bak` movidos **para fora do repo** (não commitados).

### (B) Guardião de relevância — motor (NÃO commitado, ativo localmente; `.bak` preservado)
- `agentes_tematicos/v4/publicador.py` (bak `publicador.py.bak_pre_guardiao_20260813_1956`):
  - `import unicodedata` (após `import time`).
  - Novas funções `_normalizar_txt()` e `_entidades_titulo()` (antes de `_buscar_hero`); stoplist `_ENT_STOP` de descritores genéricos.
  - `entidades = _entidades_titulo(titulo_materia)` antes do loop de termos.
  - Gate reescrito: se há entidades, exige ≥1 no título do arquivo (`_normalizar_txt`); senão mantém gate genérico (1 token).
- `agentes_tematicos/v4/nucleo_visao.py` (bak `nucleo_visao.py.bak_pre_guardiao_20260813_1957`):
  - Novo item "PESSOA/LOCAL NOMEADO, OUTRO ASSUNTO" na lista REJEITE do `_PROMPT` (aditivo; calibração "em dúvida aprove" intocada).

## Comandos / provas
- `python3 -m py_compile publicador.py nucleo_visao.py` → **OK**.
- Teste isolado do gate: `_entidades_titulo("Atlas Intel: Ciro lidera com 49,3% e Elmano tem 44,6% no Ceará")` = `{atlas, ceara, ciro, elmano, intel}`; arquivo reflorestamento → **REJEITADO**; `File:Ciro Gomes em Caxias (MA) em 2018.jpg` → **ACEITO**; título genérico → entidades ~vazias → fallback token gate (sem regressão).
- `git rev-parse HEAD == origin/main` = `4e093ef4088666b8a1ac22751b8e57fa9e57e4d7`.
- Verificação ao vivo: `curl https://ceara.digital/blog/20260813-atlas-intel-.../ | grep` → nova legenda no ar, "reflorestamento" sumiu.

## Por que NÃO commitei o motor
Regra "commit/push só quando o Miguel pede". O deploy do ceara.digital exigiu commit+push (mecanismo de deploy) — feito e autorizado no plano. O patch do motor é **ativo localmente** (cron dos temáticos roda em `agentes_tematicos/v4/`), `.bak` preservado. Padrão do ecossistema (auditoria V4 também aplicou patches in-place c/ `.bak`).

## Pendências / próximos passos
1. Confirmar se há **gêmeo NYC** do motor (`/root/agentes_tematicos/v4/`?) rodando o cron V4 — se sim, replicar o patch lá.
2. **Stock Pixabay ≠ pessoa real** (FASE B/cascata): herdar o gate de entidade p/ a cascata, ou restringir stock a temas sem pessoa nomeada; checar identidade.
3. **Auditoria** de heroes recentes (7–15d) dos 8 temáticos (follow-up, se o Miguel pedir).
4. Melhorar geração do **`visual_prompt`** no `produtor.py` p/ já incluir o nome da pessoa (defesa em profundidade).
5. Teste ao vivo do pipeline completo (produtor→publicador) quando houver crédito de visão (Qwen 🔴 esgotado hoje).

## Lições
- **Sites temáticos são Astro+Vercel, não WP** — não confundir com o canônico; correção de hero é markdown+push, não WP-CLI.
- **Gate determinístico por entidade > juiz LLM** para evitar disparates: o LLM aprova em dúvida/fail-open; entidade no título do arquivo é checagem barata e robusta.
- **Recência vs. autenticidade:** quando não há foto recente licenciada da pessoa, foto REAL mais antiga > stock que não é a pessoa.
