# 🧠 MEMÓRIA TÉCNICA — Aiatolah bilíngue: corpo no idioma errado (09/09/2026)

> Log técnico completo da missão. Decisões e estado: `Foruns/forum_aiatolah_bilingue_corpo_idioma_errado_20260909.md`.
> Autor: ZCode (Qwen3.8-Max). Janela: 09/09/2026 05:5x → 07:1x BRT.

---

## 1. Linha do tempo

| Hora (BRT) | Evento |
|---|---|
| ~05:5x | Ordem do Miguel: conferir o site + solução estrutural (URL /en/posts/20260825-auto-mode...). |
| ~06:0x | Conferência ao vivo (curl): corpo PT sob frontmatter EN confirmado. Monitor: linha EM ANDAMENTO (06:12). |
| ~06:1x | Mapeamento: repo vivo = aiatolah-v4 (clone de análise em /tmp/aiatolah-v4); publisher real = NYC V4 (crontab grep; 159.89.185.209 é Rio-Carta, NÃO é o aiatolah). |
| ~06:2x | Varredura dos 403 posts: 11 defeituosos (9 EN c/ corpo PT + 2 PT c/ conteúdo EN) + ~38 legendas PT em página EN. Causa-raiz tripla fechada no `_traduzir()`. |
| ~06:3x-06:5x | Patch construído em /tmp/nyc_v4/ + 3 iterações dos detectores (ver §3). Teste local 403: 11/11 + 0 FP. |
| ~06:5x | Instalação no NYC: backups `.bak_pre_bilingue_20260909` + scp + py_compile + import c/ venv + teste remoto de gates (9+2 PASS). |
| ~07:0x | Retrofit no NYC: Fase B (38 legendas) + Fase A (11 corpos deepseek, retry×2 fail-closed). Varredura pós: 0 flags em 403. Commit 5f0d5e3 push (03aa82c..5f0d5e3), 48 arquivos, 175+/175−. |
| ~07:0x-07:1x | Verificação ao vivo pós-deploy (auto-mode, wasmtime, sam-altman, muse-glimmer). Monitor ✅. Tema Duplo + nodos + index AIATOLAH retificado. |

## 2. Mapa da infraestrutura (verificado nesta missão)

- Repo vivo: `github.com/migueldorosario1/aiatolah-v4` — Astro SSG, deploy Vercel automático na push da main (~60-75s). Repo velho `aiatolah` + pasta local `/home/migueldorosario/Downloads/Antigravity Google/aiatolah/` CONGELADOS (migração 20/07). `CEREBRO_INDEX_AIATOLAH.md` estava preso em 24/05.
- Posts: `src/pages/{pt,en}/posts/*.md`, 403 arquivos no total. Frontmatter estilo "pages" V4: `layout/title(single-quoted)/date/category/lang("pt-br"|"en")/excerpt(double-quoted)/source/heroImage/[hero_credit]/[hero_legenda(double-quoted)]`.
- `hero_legenda` renderiza VISÍVEL: `src/layouts/PostLayout.astro:73` (alt da img) e `:78` (`.post-hero-caption-text`); `:79` crédito "Foto"/"Photo" por isPt.
- Pipeline: NYC (`ssh nyc` = 198.199.121.136) `/root/tematicos/agentes_tematicos/v4/` — orquestrador.py + wrappers finos + produtor.py/publicador.py genéricos. Checkout do site: `/root/tematicos/sites-v4/aiatolah`. Python: `/root/venv/bin/python3`. Chaves: `. /root/chaves.sh`. Cron: `0 12 * * *` (12:00 UTC = 09:00 BRT), lock por site `v4_<site>` via `acquire_lock_or_exit`.
- aiatolah = único bilíngue dos 8 sites V4 → mudanças no `_traduzir` só o afetam; o gate pré-write é conservador p/ monolíngues (ambíguo passa = comportamento atual).
- Git dos posts defeituosos: autores "Refatoracao V4" e "AIATOLAH KIMI" (mesmo motor). Shallow clone escondia autoria → `git fetch --deepen 300`.

## 3. Causa-raiz tripla + desenho da cura

### 3.1 O que estava errado no `publicador._traduzir()` (código velho)

```python
# (1) FAIL-OPEN POR CAMPO — campo ausente no JSON do LLM mantinha o original:
trad.update({k: j[k] for k in (...) if r["json"].get(k)})
#     max_tokens=4096 comido por reasoning (BUG-DS-102) → JSON truncado →
#     corpo PT original sobrevivia sob frontmatter EN traduzido, EM SILÊNCIO.
# (2) CÓPIA CEGA — presumia original sempre PT:
if lingua_alvo == "pt": return dict(artigo)
#     artigo nascido EN (produtor sem gate em site pt-BR) → versão "PT" 100% EN.
# (3) gates _veto_publicacao/_parece_portugues rodam ANTES da tradução e só
#     para sites EN-only — espelho bilíngue nunca revalidado.
# (4) hero_legenda fora do prompt de tradução → ~38 legendas PT em página EN.
```

### 3.2 Iterações dos detectores (3 versões até o desenho final)

- **v1:** só `_PT_STOPWORDS` pré-existente (vocabulário de NOTÍCIA do GSN: segundo|disse|afirmou|governo|presidente..., ≥5 hits) → flagrou 7/9: prosa técnica PT não usa "segundo/disse" (corpo do 500-fine-tuning: 3 hits em 2636 chars). Cura: `_PT_STOPWORDS_GERAL` (function words PT) + `_parece_portugues_geral`.
- **v2:** 8/9 — corpo do entropy-markov 100% PT (115 hits gerais) mas 4 hits EN... todos o "as" português ("as cadeiras") casando com `_EN_STOPWORDS`. Cura: **"as" removido da lista EN** (único overlap real; prosa EN atinge ≥8 sem ela).
- **v3:** ainda 8/9 — os 3 hits EN restantes eram of/from/to do próprio TÍTULO inglês concatenado. Cura: `_versao_no_idioma` amostra **SÓ O CORPO** para os detectores gerais (o detector estreito de notícia mantém title+body, não tem condição cruzada). Teste final: **11/11 + 0 falso-positivo**.
- Armadilha de auto-checagem: `'as' in _EN_STOPWORDS.pattern` imprime True mesmo após remoção — substring de "was"/"has". A evidência real são as contagens de hits, não grep no pattern.
- Comportamento documentado: textos curtos (<~500 chars) ficam abaixo dos limiares = "ambíguo passa" (fail-soft deliberado; falso-positivo só adiaria pauta, falso-negativo_publicaria idioma errado — assimetria aceita para não travar sites monolíngues).

### 3.3 Código final instalado (bloco V4_PATCH_BILINGUE_IDIOMA_20260909)

produtor.py (após o bloco GSN, sem tocá-lo):

```python
_EN_STOPWORDS = re.compile(
    r"\b(the|and|of|to|in|is|are|was|were|for|with|that|this|from|by|has|have|"
    r"it|its|at|on|be|been|will|would|not|but|or|than|then|when|while|which|"
    r"who|their|there|these|those|about|into|over|after|before|also|more|most|"
    r"other|some|such|only|just|said|says|according|both|each|many|much)\b", re.I)

_PT_STOPWORDS_GERAL = re.compile(
    r"\b(de|da|dos|das|um|uma|na|nos|nas|ao|aos|à|às|pelo|pela|pelos|pelas|"
    r"com|sem|sob|sobre|para|por|mais|muito|como|quando|onde|porque|não|já|só|"
    r"também|então|está|estão|foi|foram|ser|são|tem|têm|tinha|isso|isto|esse|"
    r"essa|este|esta|seu|sua|seus|suas|pode|podem|ainda|apenas|mesmo|cada|"
    r"todo|toda|todos|todas|qual|quais|quem|que|é|os|após|desde|durante)\b")

def _parece_ingles(texto):     # >=8 EN E <3 PT-geral, amostra 3000 chars
def _parece_portugues_geral(texto):  # >=8 PT-geral E <3 EN
```

publicador.py — import estendido (linha 38), `_CAMPOS_OBRIGATORIOS_TRADUCAO = ("title","description","body_markdown")`, e:

```python
def _versao_no_idioma(art, lingua):
    titulo = art.get("title", ""); corpo = art.get("body_markdown", "")
    if lingua == "en":
        return not (_parece_portugues(titulo + "\n" + corpo)
                    or _parece_portugues_geral(corpo))   # corpo-only p/ geral
    if lingua == "pt":
        return not _parece_ingles(corpo)                 # corpo-only
    return True
```

`_traduzir` novo: atalho por detecção (`_versao_no_idioma(artigo, lingua_alvo)` → `dict(artigo)`, vale p/ PT nato E EN nato); prompt com category + hero_legenda; `for tentativa in (1, 2)`; `gerar_json(prompt, tarefa="coleta", max_tokens=8000)`; checagem de campos obrigatórios → continue; fallback `hero_legenda = title traduzido`; gate `_versao_no_idioma(trad, ...)` → continue; esgotou → log "tradução ESGOTADA ... (fail-closed)" → `return None`.

`rodar()`: detecção de versão bilíngue faltando + `_alertar(f"Versão bilíngue faltando ({site_id})", chave=f"traducao_{site_id}", horas=6)`; loop de gate pré-write montando `versoes_ok` (`alvo = lingua or _idioma_esperado(cfg)`; falhou → log "GATE IDIOMA" + `_alertar(chave=f"gate_idioma_{site_id}_{alvo}")` + continue, NUNCA write); `versoes` vazio → "nenhuma versão no idioma certo — publicação ADIADA" + continue (item fica pendente, sem marcar banco).

## 4. Os 11 arquivos defeituosos (todos corrigidos no commit 5f0d5e3)

EN com corpo PT (9): `en/posts/20260726-fedora-45-a-study-on-package-manufacturing.md` · `en/posts/20260726-openai-launches-gpt-5-6-sun-with-a-54-increase-in-token-effi.md` · `en/posts/20260726-prof-hannah-fry-receives-the-leelavati-prize-for-mathematics.md` · `en/posts/20260726-textual-fingerprint-analysis-reveals-similarity-between-kimi.md` · `en/posts/20260726-wasmtime-47-releases-support-for-gc-and-exceptions-in-webass.md` (1 bloco de código) · `en/posts/20260802-500-fine-tuning-surpasses-frontier-models-in-catalog-review.md` · `en/posts/20260802-google-fixed-more-chrome-bugs-in-june-than-in-two-years-with.md` · `en/posts/20260812-entropy-of-markov-chains-from-physics-to-artificial-life.md` · `en/posts/20260825-auto-mode-becomes-default-in-claude-code-for-pro-max-and-tea.md` (o denunciado).

PT com conteúdo EN (2): `pt/posts/20260726-sam-altman-reveals-ai-2026-predictions-for-openai-and-tech-i.md` · `pt/posts/20260804-ripgrep-musl-binaries-crash-on-large-searches.md`.

## 5. Retrofit — `retro_idioma_20260909.py` (NYC, staging `/tmp/staging_bilingue_20260909/`)

- `BASE = /root/tematicos/sites-v4/aiatolah/src/pages`; `BACKUP = /root/tematicos/agent_data/backup_idioma_20260909/` (flat, `<lang>__<nome>`).
- `split_arquivo`: `fim = txt.index("\n---", 4); bloco_fm = txt[4:fim]` — 🔴 bug intermediário: `txt[3:fim]` guardava o `\n` inicial → linha fantasma após o `---` de abertura (diff +76/−38); corrigido p/ `txt[4:]` → diff cirúrgico +38/−38 na Fase B.
- `fm_get`/`fm_set` preservam estilo de aspas original (single→escape `''`, double→escape backslash); `remontar = "---\n" + linhas + "\n---" + corpo`.
- **Fase B (38 legendas, determinística):** mapa de títulos-twin PT por PREFIXO DE DATA (twins PT/EN têm filenames DIFERENTES — slug do respectivo título; matching por nome nunca casava). Regras: R1-twin (legenda == qualquer título PT da data), R2-diacrit ([ãõçáéíóúâêôà] + ≥1 func word PT, re.I — "Não" escapava case-sensitive), R3-func (≥3 func PT e 0 EN) → legenda = título EN do próprio arquivo. Limítrofes: print "?? SUSPEITA MANTIDA" (new-mexico tag-dump EN mantido).
- **Fase A (11 corpos, LLM deepseek):** idempotência (corpo já no idioma → pula); prompt espelha o `_traduzir` patcheado ("Keep ALL markdown formatting, headings (##/###), code blocks byte-for-byte"; "Also translate title and excerpt (max 155 chars)" nos 2 PT); validação `(faltando or len(corpo_novo) < 0.4*len(corpo) or corpo_novo.count(fence) != fences_orig or not corpo_no_idioma(...))` → retry → esgotou = "FAIL-CLOSED: NÃO tocado"; corpo gravado com "\n" inicial único garantido.
- Rodada: Fase B 38 trocas + Fase A 11/11 traduzidos (0 fail-closed); `git add -A && git commit` = **5f0d5e3** (48 arquivos, 175+/175−), push `03aa82c..5f0d5e3`. Varredura pós: `total=403 flags_en=0 flags_pt=0`.

## 6. Testes e provas

- `/tmp/nyc_v4/teste_detectores_20260909.py` (local): executa FATIAS REAIS do fonte (regex `_PT_STOPWORDS = re.compile(` até o marcador FIM; `_CAMPOS_OBRIGATORIOS_TRADUCAO =` até `def _traduzir(`), varre `/tmp/aiatolah-v4/src/pages/{en,pt}/posts/*.md`, espera 9+2. PASS.
- `/tmp/nyc_v4/teste_gates_remoto.py` (NYC): importa `_versao_no_idioma` do publicador INSTALADO, varre `/root/tematicos/sites-v4/aiatolah/src/pages`. Pré-retrofit: 9+2 PASS. Pós-retrofit: zeros (o assert 9+2 imprime "DIVERGIU" — os zeros SÃO a prova de sucesso).
- Fakes de LLM p/ teste do retrofit: textos sintéticos curtos (~230 chars) caem abaixo dos limiares (detector False = "ambíguo passa", NÃO é bug); fakes padded (`BASE*18` + cercas) exercitam a validação real — rodada 1 com fakes curtos: 11 rejeitados pelo guard de comprimento ≥40% (funcionando como desenhado).
- `py_compile` dos 2 arquivos + import do publicador com `/root/venv/bin/python3` (chaves via `. /root/chaves.sh`): OK.
- md5 pós-instalação: produtor `670b492b48dc83b343a6621819d127bf`, publicador `268ac3b570bf89b8e8f868039da80420`. Backups: produtor `.bak_pre_bilingue_20260909` md5 `66ef84ec11fa9ac458098a6b67901e61`, publicador md5 `c5b5736d9e14f3b3b8660df038061e30`. (Re-verificados 07:1x: md5 bate + marcadores presentes: `_PT_STOPWORDS_GERAL` ×3, "as" fora da lista EN (`it|its|at|on`), `_parece_portugues_geral(corpo)` na linha 180, `max_tokens=8000` na linha 209.)

### Provas ao vivo (09/09 ~07:0x-07:1x BRT, pós-deploy)

- auto-mode: HTTP 200 22069B; "vira padrão" ausente; primeira frase PT antiga ausente; `grep -c "Anthropic announced that auto mode becomes the default"` = 1; legenda EN no ar.
- wasmtime: HTTP 200 22108B; 3 `<code>/<pre>`; `<title>` = "Wasmtime 47 Releases Support for GC and Exceptions in WebAssembly | Aiatolah"; H2 "Wasmtime 47 Expands WebAssembly with GC and Exception Support" presente.
- sam-altman PT: título "Sam Altman Revela IA 2026: Previsões para OpenAI e Indústria de Tecnologia"; corpo "A inteligência artificial conti...".
- muse-glimmer EN: legenda "Meta launches Muse Glimmer: open 30B model for local agents".
- Primeira frase traduzida no repo NYC: auto-mode "Anthropic announced that auto mode becomes the default in Claude Code for Pro, Max, and Te..."; wasmtime "## Wasmtime 47 Expands WebAssembly with GC and Exception Support" (fences=2 no fonte).

## 7. Armadilhas de Bash/ssh encontradas (receita p/ futuras missões)

1. cwd do shell RESETA p/ /home/migueldorosario/ZCodeProject a cada chamada — usar caminhos absolutos.
2. Heredoc python via ssh com aspas simples internas quebra (`ruins['en']` → NameError 'en') — escrever o teste como arquivo local + scp + executar remoto.
3. Crase dentro de pattern de grep em aspas DUPLAS executa como command substitution — usar aspas simples ou `chr(96)` no python.
4. `tee` para diretório que o script cria durante a corrida falha na abertura do pipe ("No such file or directory") — stdout ficou no resultado da ferramenta; números capturados.
5. WebFetch timeout → fallback curl/urllib (já registrado em `pesquisa-noticias-rss-bing-webfetch-fallback-20260908`).
6. Shallow clone esconde autoria de commits → `git fetch --deepen 300`.
7. Pós-compaction de contexto, Edit exige Read novo do arquivo na conversa corrente (Reads replanejados via system-reminder não contam).

## 8. Escopo e compatibilidade

- `_PT_STOPWORDS` (GSN, ≥5, vocabulário de notícia) NÃO tocado — patches GSN 29/07+05/08 intactos.
- Sites monolíngues: gate pré-write passa ambíguo (comportamento = atual); proteção extra conservadora sem risco de travar publicação.
- "Soltar posts, não prender": mantido — bloqueio só de versão FORA DO IDIOMA, com alerta Telegram visível (throttle por chave) e item pendente p/ próxima rodada.

## 9. Pontas soltas registradas (próximos sprints)

- Relevância de `hero_legenda` (tag-dump de stock: entropy-markov×Plaza de España, kitesurf×outro assunto) — gate de pertinência legenda×título é candidato natural.
- Prova do patch em corrida real: cron 12:00 UTC (09:00 BRT) de 09/09 — conferir log do orquestrador (`/root/tematicos/agentes_tematicos/v4/` → logs da corrida aiatolah) e ausência de alertas `gate_idioma_aiatolah_*`/`traducao_aiatolah`.
- Índice `CEREBRO_INDEX_AIATOLAH.md` retificado nesta missão (banner V4); pendências antigas dele (KIMI_API_KEY expirada etc.) referem-se ao stack congelado — não bloqueiam o V4.
