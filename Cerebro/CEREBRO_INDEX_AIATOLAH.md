# 🧠 CÉREBRO INDEPENDENTE: Portal Aiatolah — Índice Canônico

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Resolução de Atalhos:** Qualquer link relativo no formato `../Cerebro/` aponta para esta pasta unificada, funcionando de maneira idêntica tanto localmente quanto nos servidores.
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.


> Última atualização: 2026-05-24 22:30 BRT — Claude Maestro  
> Reescrito e expandido com tudo que foi feito na sessão 24/05. Fonte de verdade do Aiatolah.

> [!WARNING]
> **RETIFICAÇÃO 09/09/2026 (ZCode Qwen3.8-Max — missão aiatolah bilíngue):** este índice estava DEFASADO (preso em 24/05, anterior à migração V4 de 20/07). Fatos atuais:
> - **Domínio vivo:** `aiatolah.com` (não mais só `aiatola.vercel.app`).
> - **Repo vivo:** `github.com/migueldorosario1/aiatolah-v4` (Astro → Vercel, deploy automático ~60-75s após push na main). O repo velho `aiatolah` e a pasta local `Antigravity Google/aiatolah/` estão **CONGELADOS**.
> - **Publicação automática:** orquestrador **V4 no NYC** (`ssh nyc`) em `/root/tematicos/agentes_tematicos/v4/` — cron `0 12 * * *` UTC (09:00 BRT), checkout do site em `/root/tematicos/sites-v4/aiatolah`, python `/root/venv/bin/python3`, chaves `. /root/chaves.sh`. Posts em `src/pages/{pt,en}/posts/*.md` (403 arquivos em 09/09).
> - **Bilíngue PT+EN com tradução automática** e gates determinísticos de idioma (`V4_PATCH_BILINGUE_IDIOMA_20260909`, fail-closed) — ver `Foruns/forum_aiatolah_bilingue_corpo_idioma_errado_20260909.md`.
> - Abaixo desta linha = registro HISTÓRICO de 24/05 (mantido para rastreabilidade; detalhes técnicos do stack velho superados).

---

## 🎯 O Que é o Aiatolah

Portal bilíngue (PT + EN, futuro: ZH) de inteligência artificial, geopolítica tecnológica e guerra dos chips. Nome é provocação deliberada: o "aiatolah da IA" que julga modelos sem reverência ao Ocidente. Linha editorial: **anti-imperialismo tecnológico**, Sul Global como protagonista.

- **URL viva:** `aiatola.vercel.app`
- **Domínio futuro:** `aiatolah.com` (registrado GoDaddy)
- **Repo público:** `github.com/migueldorosario1/aiatolah`
- **Dir local:** `/home/migueldorosario/Downloads/Antigravity Google/aiatolah/`

---

## 📐 Stack Técnico (Decisões Fechadas)

| Componente | Tecnologia | Decisão |
|---|---|---|
| Framework | **Astro** (Static Site Generator) | Estático, rápido, gratuito no tier Vercel |
| Deploy | **Vercel** (auto via push `main`) | Git push → rebuild ~30-60s, sem VERCEL_TOKEN |
| CMS | **GitHub** headless (Markdown) | Arquivos `.md` com frontmatter em `src/pages/en/posts/` |
| Build | `npm run build` → `dist/` | Detectado automaticamente pelo Vercel |
| Idiomas | PT + EN (ZH Fase 3) | IP detection futuramente; por ora seleção manual por bandeira |
| Dados ranking | `src/data/ranking.json` | JSON estático, atualizado manualmente por ora |
| Observabilidade | `agent_data/publicacoes_metricas.jsonl` + Prometheus pushgateway | Recibo por publicação — spec pronta, cron pendente |

### ⚠️ Decisão técnica crítica — Astro v6
`Astro.glob()` foi **removido** no Astro v6. Usar **obrigatoriamente**:
```js
const modules = import.meta.glob('./en/posts/*.md', { eager: true });
const posts = Object.entries(modules).map(([path, mod]: [string, any]) => ({
  ...mod.frontmatter,
  url: '/en/posts/' + path.replace('./en/posts/', '').replace('.md', '')
}));
```

### ⚠️ GitHub token — usar token clássico
Fine-grained PAT deu HTTP 403 mesmo com permissão `push:true`. Token clássico (`ghp_...`) funciona. Variável: `GITHUB_TOKEN_AIATOLAH_CLAUDE` no cofre Tencent.

---

## 📁 Estrutura de Arquivos

```
aiatolah/
├── src/
│   ├── pages/
│   │   ├── index.astro          ← homepage EN (3 colunas: China | Notícias | EUA)
│   │   ├── about.astro          ← missão, perspectiva multilateral
│   │   ├── rankings.astro       ← tabela de preços (USD + BRL por M tokens)
│   │   ├── news.astro           ← grid de artigos (card-featured = último)
│   │   ├── pt/index.astro       ← homepage PT (espelho)
│   │   └── en/posts/            ← artigos editoriais Markdown
│   ├── components/
│   │   └── NavMenu.astro        ← menu dropdown + logo crescent persa SVG
│   ├── layouts/
│   │   └── Layout.astro         ← layout base com SEO, hreflang, dark theme
│   └── data/
│       └── ranking.json         ← 15 modelos com preços USD + BRL, qualidade S/A/B
├── public/
│   └── favicon.svg              ← crescent dourado + "AI" ciano em fundo preto
├── agentes/
│   ├── aiatolah_agente_coletor_ia.py   ← parcialmente implementado (feedparser + LLM)
│   └── aiatolah_metricas_publicacao.py ← recibos Prometheus por publicação
├── agent_data/
│   └── publicacoes_metricas.jsonl
├── forums/                      ← comunicação Trindade, NÃO vai pro site
│   ├── aiatolah_canal_trindade.md
│   ├── aiatolah_forum_trindade.md
│   ├── aiatolah_forum_sprint_kimi_01.md
│   └── aiatolah_mural_trindade.md
├── producao/
│   ├── aiatolah_conceito.md     ← conceito editorial completo
│   ├── aiatolah_engenharia.md   ← stack, deploy, decisões técnicas registradas
│   └── aiatolah_prompts_miguel.md ← prompts do agente coletor
├── GPT Producao/                ← conversas e resumos consolidados do ChatGPT
├── Modelos para projeto ChatGPT/ ← onboarding em 12 arquivos para o ChatGPT
├── .env.local                   ← chaves reais (GITIGNORED — NUNCA COMMITAR)
├── .env.example                 ← template seguro
├── CHAVES_AIATOLAH_MANIFESTO.md ← mapa de variáveis e fontes do cofre
├── PROMETHEUS_DESDE_NASCENCA.md ← spec de telemetria e recibos
└── arquitetura_aiatolah.md      ← documento base de visão
```

**Fórum principal (no Cafezinho):**
`Projeto Cafezinho Agentes/Foruns/forum_arquitetura_aiatolah.md`

---

## 🔐 Cofre de Chaves (Nomes das Variáveis — Valores NUNCA aqui)

| Variável | Localização | Para que serve | Status |
|---|---|---|---|
| `GITHUB_TOKEN_AIATOLAH_CLAUDE` | `.env.unificado` Tencent | Claude escreve no repo | ✅ Ativo (token clássico ghp_...) |
| `GITHUB_TOKEN_AIATOLAH_KIMI` | Cofre Beijing `/root/cerebro_trindade/cofre/env_cofre_backup` | Kimi CEO escreve no repo | ✅ Ativo |
| `GITHUB_TOKEN_AIATOLAH_CHATGPT` | `.env.unificado` Tencent | ChatGPT escreve no repo | ✅ Ativo |
| `DEEPSEEK_API_KEY` | `.env.local` local + `.env.unificado` Tencent | Redação artigos EN | ✅ |
| `KIMI_API_KEY` / `MOONSHOT_API_KEY` | `.env.local` local | Contexto longo, revisão | ⚠️ **EXPIRADA — HTTP 401** (renovar em platform.moonshot.cn) |
| `QWEN_API_KEY` / `DASHSCOPE_API_KEY` | `.env.local` local | Fallback redação | ✅ |
| `ZHIPU_API_KEY` | `.env.local` local | Modelos GLM | ✅ |
| `BRAVE_API_KEY` | `.env.local` local | Busca de pautas | ⚠️ Compartilhada com Cafezinho (quota finita) |
| `PERPLEXITY_API_KEY` | `.env.local` local | Fact-check | ✅ |
| `FAL_API_KEY` | `.env.local` local | Geração imagem (Flux) | ✅ |
| `IDEOGRAM_API_KEY` | `.env.local` local | Geração imagem | ✅ |
| `FLICKR_API_KEY` | `.env.local` local | Busca foto ao vivo | ✅ |
| `VERCEL_TOKEN` | A adicionar | Deploy manual via API | ❌ Não necessário (deploy automático via GitHub) |
| `AIATOLAH_PROMETHEUS_PUSHGATEWAY` | A adicionar | Métricas ao Prometheus | ❌ Deploy pendente autorização |

---

## 📋 Linha Editorial (5 Pilares + Regras)

1. **Anti-imperialismo tecnológico** — sanções a Huawei, TSMC sob pressão, ASML proibida: Aiatolah nomeia isso
2. **Sul Global como protagonista** — Brasil, China, Índia, Irã, Rússia cobertos com mesmo rigor que Silicon Valley
3. **IA como ferramenta de soberania** — DeepSeek, Qwen, GLM, programas indianos/iranianos documentados e celebrados
4. **Transparência radical sobre custos** — preços reais, quem pode pagar, quem fica de fora
5. **Boletim Aiatolah** — relatório semanal bilíngue: 5 fatos da semana + 1 análise profunda + custos reais

**O que NÃO é:** blog de tutoriais genéricos, newsletter de investidores, neutro.

**Público:** jornalistas/analistas BR (PT), devs/pesquisadores IA (EN), ativistas soberania digital (PT/EN), comunidade Sul Global tech (EN).

---

## 🚀 Sprint History — O Que Foi Entregue

### Sessão 2026-05-22 (Antigravity + Codex)
- `agentes/aiatolah_agente_coletor_ia.py` — script de coleta RSS + pipeline LLM (não operacional ainda)
- `agentes/aiatolah_metricas_publicacao.py` — utilitário Prometheus (smoke dry-run OK)
- `.env.example`, `CHAVES_AIATOLAH_MANIFESTO.md`, `PROMETHEUS_DESDE_NASCENCA.md`
- `agent_data/publicacoes_metricas.jsonl` — smoke local OK
- `Modelos para projeto ChatGPT/09_PROMETHEUS_E_CHAVES_DESDE_NASCENCA.md`

### Sessão 2026-05-23 (Codex + Claude)
- `forum_arquitetura_aiatolah.md` registrado (pareceres Kimi + DeepSeek sobre loop Google Doc 30min)
- Decisão: loop Google Doc aguarda Miguel identificar o Doc oficial antes de qualquer implementação
- Prometheus spec finalizada, deploy pendente autorização

### Sessão 2026-05-24 (Claude Maestro — principal)

| Commit | Entrega |
|---|---|
| `9340f23` | NavMenu dropdown dark — LLMs China/EUA/Outras, Imagem, Rankings, links API |
| `648c32e` | Site em inglês, "AI" destacado em ciano `#00d4ff` no logo |
| `fa5f14f` | Página `/about` em inglês — missão, multilateral, open source |
| `4058549` | Flags 🇺🇸/🇧🇷 funcionais, homepage EN 3 colunas, `/pt` espelho PT |
| `4d92d54` | Logo crescent persa SVG no NavMenu + favicon.svg |
| `9924ca4` | Rota `/rankings` — tabela de preços USD + BRL por M tokens, 15 modelos |
| `ca1536a` | `/teste` promovido para `/rankings` (rota oficial no menu) |
| `8bd4069` | Página `/news` com grid de artigos + 4 artigos editoriais EN |

#### Logo Persian Crescent (SVG inline no NavMenu)
```html
<svg class="logo-crescent" width="22" height="22" viewBox="0 0 22 22">
  <defs>
    <mask id="crescent-mask">
      <circle cx="11" cy="11" r="9" fill="white"/>
      <circle cx="15.2" cy="10" r="7.2" fill="black"/>
    </mask>
  </defs>
  <circle cx="11" cy="11" r="9" fill="#e8b84b" mask="url(#crescent-mask)"/>
</svg>
```
Drop-shadow dourado `#e8b84b`, glow no hover. Funciona em qualquer fundo via `<mask>`.

#### Artigos publicados (en/posts/)
- `us-china-chip-war-2026.md` (2026-05-18, Chip Wars)
- `qwen3-235b-alibaba-open-source.md` (2026-05-19, Open Source)
- `kimi-k2-moonshot-agentic-ai.md` (2026-05-21, China AI)
- `deepseek-v3-beats-gpt4o-in-coding-benchmarks.md` (2026-05-23, Rankings)

#### ranking.json — 15 modelos
- Ordenados por preço input (mais barato primeiro)
- GLM-4 Flash $0.07 → GPT-4o-1 $15.00
- Campos: `input_usd`, `output_usd`, `quality` (S/A/B), `speed`, `open_source`, `tags`, `country`, `flag`
- `usd_brl: 5.80` (configurável)
- Categorias: S = Frontier (cyan), A = Excellent (purple), B = Capable (gray)

---

## ⏳ Pendências Abertas (Próximas Sessões)

| Item | Estado | Bloqueio |
|---|---|---|
| Agente coletor de notícias (RSS → LLM → Markdown → Git push) | Parcialmente codado | Sem cron, sem prod. Precisa: ativar RSS, testar pipeline, autorizar cron |
| Loop Google Doc 30min (pauta viva) | Aguardando | Miguel deve identificar o Doc oficial antes de qualquer implementação |
| KIMI_API_KEY renovação | ⚠️ URGENTE | Acessar platform.moonshot.cn → renovar → atualizar `.env.local` e `.env.unificado` Tencent |
| Chatbot (Darius/Cyrus/Shirin) | Fase 2 | Após MVP consolidado |
| Prometheus pushgateway deploy | Spec pronta | Aguarda autorização Miguel |
| ElevenLabs voice clone Miguel (inglês) | Fase 2 | Multimídia — vídeos automatizados |
| Mandarim (3ª língua) | Fase 3 | — |
| CCTV v3/v4 | ❄️ FROZEN | AG-VIOLATION grave Tick 2 — aguarda decisão Miguel (opções α/β/γ) |
| Artigos em `src/pages/en/posts/` vindos do coletor automático | Não iniciado | Depende do coletor operacional |

---

## 🏛️ Governança Aplicável ao Aiatolah

- **§47:** Antigravity **não coda, não deploya** — só arquitetura + diagnóstico
- **§82:** Credenciais NUNCA no fórum, canal, ou CEREBRO — sempre no cofre
- **§51:** Bug simples (≤30 linhas, sem motor/cron) = corrige sozinho; complexo = ≥2 OKs
- **§55.7:** Rio Carta é laboratório (2 votos bastam); Aiatolah segue **3/5** por padrão
- **Soltar posts, não prender:** qualquer autocura detecta → corrige silenciosamente → publica. Proibido detectar → enfileirar → esperar humano.
- **Protocolo deploy obrigatório:** backup timestamp + autor + rollback documentado + entrada no Cérebro
- `.env.local` é gitignored — **NUNCA commitar**. Verificar `git status` antes de qualquer push.

---

## 🖥️ Como Publicar Artigo (Agente ou Manual)

### Via Markdown direto (padrão)
```bash
# Criar artigo em src/pages/en/posts/YYYY-MM-DD-slug.md
# Frontmatter obrigatório:
---
title: "Título do Artigo"
date: 2026-05-24
category: "China AI"   # Rankings | China AI | Open Source | Chip Wars | Nvidia
lang: "en"
excerpt: "Resumo de 1-2 frases"
source: "https://fonte.com"
---
```

### Via API GitHub (agentes automatizados)
Usar script em `producao/aiatolah_engenharia.md §3` com variável `GITHUB_TOKEN_AIATOLAH_CLAUDE`.  
Push para `main` → Vercel rebuild automático (~30-60s).

---

## 🔗 Referências Cruzadas

| Documento | Local | Conteúdo |
|---|---|---|
| `aiatolah_conceito.md` | `aiatolah/producao/` | Linha editorial completa, pilares, tom, público |
| `aiatolah_engenharia.md` | `aiatolah/producao/` | Stack, deploy, schema ranking.json, decisões técnicas |
| `aiatolah_prompts_miguel.md` | `aiatolah/producao/` | Prompts base do agente coletor |
| `CHAVES_AIATOLAH_MANIFESTO.md` | `aiatolah/` | Mapa de variáveis e fontes do cofre |
| `PROMETHEUS_DESDE_NASCENCA.md` | `aiatolah/` | Schema de recibos Prometheus |
| `forum_arquitetura_aiatolah.md` | `Foruns/` (Cafezinho) | Sprint history completo + pareceres Trindade |
| `aiatolah_forum_sprint_kimi_01.md` | `aiatolah/forums/` | Sprint 01 — layout 3 colunas + menu rico |
| `aiatolah_canal_trindade.md` | `aiatolah/forums/` | Canal rápido de comunicação Trindade |
| `aiatolah_forum_trindade.md` | `aiatolah/forums/` | Fórum técnico + decisões arquiteturais |
| `aiatolah_mural_trindade.md` | `aiatolah/forums/` | Espaço livre de ideias (versos chineses + reflexões) |
| `Aiatolah-resumo-consolidado.md` | `aiatolah/GPT Producao/` | Resumo consolidado das conversas com ChatGPT |
| `forum_aiatolah_ordem_home_noticias_frente_videos_20260809.md` | `Foruns/` (Cerebro) | Ordem da home: notícias na frente, vídeos (broadcasts) embaixo (EN+PT) — commit `af32846`, no ar |
| `memoria_aiatolah_ordem_home_noticias_frente_videos_20260809.md` | `Memorias/` (Cerebro) | Log técnico: arquivos, build, deploy Vercel manual (auto-deploy não disparou) |
| `forum_aiatolah_bilingue_corpo_idioma_errado_20260909.md` | `Foruns/` (Cerebro) | Página /en/ com corpo PT: causa-raiz tripla no `_traduzir()`, patch fail-closed V4_PATCH_BILINGUE_IDIOMA_20260909, retrocorreção 11 posts + 38 legendas (commit `5f0d5e3`) |
| `memoria_aiatolah_bilingue_corpo_idioma_errado_20260909.md` | `Memorias/` (Cerebro) | Log técnico completo: detectores (3 iterações, armadilha do "as"), retrofit, testes 403 posts, md5/rollback, provas ao vivo |

---

## 💡 Ideias Registradas (Não Implementadas)

- **Mandarim como 3ª língua** (ZH) — IP chinês → conteúdo em mandarim, via DeepSeek/Qwen
- **Chatbot persona iraniana:** Shirin (fem) — sugestão Claude; Darius/Cyrus (masc) — sugestão Miguel. Widget glassmorphic canto inferior direito. LLM: DeepSeek/Kimi (linha anti-imperialista)
- **RAG nos artigos:** `/api/chat` serverless na Vercel fazendo busca nos Markdowns publicados
- **Newsletter semanal bilíngue:** 5 fatos da semana + 1 análise + custos reais de IA
- **ElevenLabs voice clone Miguel:** voz em inglês fluente para vídeos automatizados (YT Shorts)
- **Menu rico com links APIs:** cada modelo → link direto ao playground/API oficial
- **Google News integration:** robots.txt, sitemap XML, meta tags NewsArticle schema.org, hreflang
- **Roteador LLM 3D para Aiatolah:** scores Q/E/V por modelo, seleção semântica de tarefa
- **IP-based language detection:** IP BR → PT, IP internacional → EN (por ora só flags manuais)

---

*Documento vivo — atualizar sempre que sprint, decisão técnica, ou chave mudar.*  
*Mantido pela Trindade. Claude Maestro responsável pela versão canônica.*

| GitHub SSH key `Meu computador` | Local `~/.ssh/id_ed25519.pub` | Fingerprint `SHA256:wB+pG1u1dDKyxP9bQSRDIzl+4Uxj6QD45Px6AL/dQqI` | ✅ Ativa |
