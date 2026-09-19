# Fórum de Revisão de Qualidade: Ecossistema de Agentes Temáticos

**Data:** 14/07/2026
**Escopo:** `MT_agente_ferroviario.py`, `agente_rail_post.py`, `agente_turismo_embratur.py`, `agente_roteador_llm.py`, `carregar_chaves.py`, `gerador_imagem_editorial.py`, `util_indexing.py`
**Referência cruzada:** `forum_explicativo_agentes_tematicos_20260714.md` (objetivos declarados)
**Método:** Leitura integral do código, verificação de consistência entre os objetivos de negócio documentados (indexação orgânica, AdSense, cadência 2/dia, antiduplicação inteligente, isolamento do Cafezinho) e o que os scripts realmente fazem.

---

## 1. Visão Geral: Objetivos vs. Implementação

| Agente | Objetivo declarado | Estado real | Veredito |
|---|---|---|---|
| Mundo Trilhos (`MT_agente_ferroviario.py`) | Crônica técnica ferroviária PT-BR, Astro/GitOps, indexação ativa | Pipeline completo e maduro, mas ainda **acoplado ao WordPress legado** e **sem a antiduplicação fuzzy documentada** | ⚠️ Funcional com dívidas graves |
| Rail Post (`agente_rail_post.py`) | Notícias ferroviárias **em inglês** para audiência internacional | Prompts de redação e revisão **em português e assinados "O Cafezinho"**, com instruções contraditórias de idioma | 🔴 Risco editorial direto |
| Discover Brazil (`agente_turismo_embratur.py`) | Turismo brasileiro em inglês, tráfego receptivo + AdSense | Pipeline mais enxuto e correto no fluxo PT→EN, mas com **risco legal de licenciamento de imagens** e bugs de robustez | ⚠️ Funcional com risco legal |
| Roteador (`agente_roteador_llm.py`) | Cascata multi-provider resiliente | Melhor módulo do pacote; hacks conscientes e documentados | ✅ Bom, com ressalvas |
| Utilitários | Chaves, imagem, indexação | `util_indexing` **não cobre os domínios dos sites temáticos**; `gerador_imagem_editorial` tem bug de argumentos e estilo visual errado para os portais técnicos | 🔴 Contradiz o objetivo de indexação |

A conclusão executiva: a arquitetura geral (busca ativa → auditoria LLM → factcheck → redação → revisão → tribunal visual → GitOps) é sólida e acima da média para agentes autônomos. Porém, há um conjunto de bugs e contradições que compromete diretamente três dos quatro objetivos de negócio declarados no fórum explicativo: **indexação**, **identidade editorial do Rail Post** e **conformidade para AdSense**.

---

## 2. Achados Críticos (P0 — corrigir antes de qualquer refatoração estética)

### 2.1 O lock de instância única não funciona (MT e Rail Post)

Em `acquire_lock()` (MT linha ~2019; Rail Post linha ~1399):

```python
try:
    pid = int(load_json(PID_FILE, {}).get("pid"))
    os.kill(pid, 0)
    raise RuntimeError(f"Já existe uma instância rodando (PID {pid})")
except OSError:
    pass
except Exception:
    pass   # ← engole o próprio RuntimeError
```

O `RuntimeError` levantado para bloquear a segunda instância é capturado pelo `except Exception: pass` logo abaixo. Resultado: **duas execuções simultâneas nunca são bloqueadas**. Combinado com o fato de `check_daily_post_limit` não usar `flock` (diferente de `util_indexing`, que usa), duas execuções concorrentes passam ambas na checagem de limite e podem publicar 3+ posts no dia — exatamente o que a diretriz "exatamente 2 posts/dia" quer impedir.

**Correção:** levantar o `RuntimeError` fora do bloco try, ou usar `fcntl.flock` num arquivo de lock (padrão já existente em `util_indexing.py`). O fórum explicativo inclusive menciona "refatoração de concorrência com flock" como pendência — confirmo que é a pendência mais urgente.

### 2.2 Rail Post: conflito de idioma e identidade nos prompts

O Rail Post é declarado como veículo **100% em inglês** (`lang: "en"` no frontmatter, domínio railpost.news). Porém:

- `write_article()` (linha ~949): *"Escreva uma crônica técnica original e maciça **para o portal O Cafezinho**, no projeto Mundo dos Trilhos"* — prompt inteiro em português, herdado do MT sem adaptação.
- `synthesize_notes()` (linha ~140): pede para *"identificar o melhor ângulo para uma crônica técnica **em português**"*.
- `review_article()` (linha ~1005): *"Você é revisor chefe de estilo do portal **O Cafezinho**. Mantenha a linha editorial desenvolvimentista, **anti-imperialista**..."*.
- `QUOTES` (citação obrigatória no primeiro terço do texto) são frases em **português** ("A velocidade também é uma forma de civilização") injetadas num artigo que deveria sair em inglês.
- `default_diretriz_ferroviaria()` injeta missão e regras em PT no system prompt.

A única instrução de inglês é uma linha em `build_master_system()` ("must be written entirely in ENGLISH"). O modelo recebe, portanto, instruções contraditórias: system diz inglês, user prompt diz português, revisor opera em português. O resultado depende de qual instrução o modelo de plantão prioriza — ou seja, **a língua do site está entregue à sorte do fallback do roteador**. Isso explica potenciais posts em PT ou híbridos no railpost.news.

Além do idioma, a linha "anti-imperialista" no revisor contradiz o comentário do próprio código ("a linha editorial anti-imperialista/política dura foi dispensada") e é um risco para a aprovação no AdSense de um site que se apresenta como técnico e neutro.

**Correção:** reescrever `write_article`, `review_article`, `synthesize_notes` e `QUOTES` do Rail Post integralmente em inglês, removendo qualquer menção ao O Cafezinho e à linha política. Alternativa mais barata: adotar o fluxo do agente de turismo (redigir em PT + etapa explícita `redigir_en` de tradução), que é o único dos três com separação de idiomas limpa.

### 2.3 Indexação Google: a whitelist não inclui os sites temáticos

`util_indexing.py`:

```python
INDEXING_ALLOWED_DOMAINS = (
    "ocafezinho.com",
    "mundotrilhos.com",
)
```

Problemas em cadeia:

1. **railpost.news e discoverbrazil.news não estão na whitelist** — e, de fato, nenhum dos dois agentes sequer chama `disparar_indexacao` no fluxo Astro. O objetivo nº 1 do fórum explicativo ("Indexação Orgânica Total... conteúdos indexados imediatamente") não tem implementação para 2 dos 3 sites.
2. **Divergência de domínio no Mundo Trilhos:** a whitelist e o `MUNDO_TRILHOS_WP_SITE` default usam `mundotrilhos.com`, mas o fórum explicativo declara o portal como `https://mundodostrilhos.com` (com "dos"). Se o domínio canônico for o do fórum, **todos os pings de indexação do MT estão sendo silenciosamente pulados** com status `dominio_nao_autorizado`. É preciso auditar o `indexing_calls.jsonl` no servidor para confirmar qual dos dois está valendo.
3. Bug clássico de `lstrip`: `host.lower().lstrip("www.")` remove *caracteres* do conjunto {w, .}, não o prefixo. Um domínio hipotético `wagner.com` viraria `agner.com`. Correção: `host.removeprefix("www.")` (Python 3.9+).

### 2.4 Discover Brazil: licenciamento de imagem juridicamente incorreto

Em `main()` do agente de turismo (linha ~600):

```python
img_meta = {
    "credit": cand_aprovado.get("origem_site", "Brave Search Source"),
    "license": "cc-by-sa"
}
```

A imagem candidata é o `og:image` raspado de **sites arbitrários encontrados via Brave Search** (blogs de turismo, portais comerciais, agências). Rotular esse material como `cc-by-sa` no frontmatter público do site é uma declaração de licença falsa: og:image de portais comerciais quase nunca é Creative Commons. Isso cria:

- risco de reclamação de direitos autorais (DMCA) contra o domínio;
- risco direto na revisão do AdSense (violação de política de direitos autorais é motivo de reprovação/banimento);
- crédito inútil ("Brave Search Source" não identifica o autor).

Compare com o MT, que faz isso corretamente: `buscar_wikimedia()` do MT extrai `Artist`, `LicenseShortName`, `LicenseUrl` e `Credit` reais do extmetadata do Commons. **Correção:** ou restringir a captação de imagem do turismo a fontes com licença verificável (Wikimedia, Flickr institucional, banco próprio), ou marcar honestamente como `license: "unknown/source"` e não publicar sem verificação. Dado o objetivo AdSense, a primeira opção é a única segura.

### 2.5 `search_brave` do turismo sem timeout

`agente_turismo_embratur.py`, linha ~159: o `requests.get` da Brave API **não tem parâmetro `timeout`**. O default do requests é bloquear indefinidamente. Um engasgo de rede congela o agente para sempre (e, como não há lock nem watchdog nesse agente, um cron seguinte empilharia processos). Os outros dois agentes usam `timeout=30` — mais um sintoma de código divergente. Correção trivial: `timeout=30`.

### 2.6 Ordem de argumentos invertida no gerador de imagem

`gerador_imagem_editorial.py`, `_chamar_llm()` (linha ~109):

```python
resposta, modelo = gerar_texto(prompt_usuario, SYSTEM_PROMPT_VISUAL)
```

A assinatura do roteador é `gerar_texto(sys_prompt, prompt, ...)`. Os argumentos estão **trocados**: o pedido do usuário vira system prompt e as regras visuais viram mensagem de usuário. Efeitos colaterais: (a) as "Regras Editoriais Aprendadas (Sentinela V4)" da autocura são concatenadas ao SYSTEM_PROMPT_VISUAL em vez do pedido; (b) o cache Anthropic (`cache_control` só no bloco system, exige system estável e ≥1024 tokens) nunca engata, porque o "system" agora é o texto variável do artigo. Funciona por tolerância dos modelos, mas é um bug real com custo financeiro.

### 2.7 Estilo visual errado para o Rail Post

Em `generate_featured_image()` do Rail Post (linha ~1156), o fallback de IA monta:

```python
artigo_data = {"titulo": title, "resumo": prompt_img or body[:400], "secao": "geopolitica"}
```

`secao="geopolitica"` no `gerador_imagem_editorial` aciona o **ESTILO C: charge satírica vintage de jornal, alegoria política sarcástica, Tio Sam/Urso/Dragão**. Ou seja: quando Wikimedia e og:image falham, um portal técnico de infraestrutura ferroviária ganha como hero image uma **charge política satírica** — o oposto do briefing fotojornalístico realista que `gerar_prompt_imagem_ferroviario()` acabou de construir com tanto cuidado (o prompt técnico é passado como "resumo", mas o `_gerar_prompt_visual` gera um NOVO prompt por cima dele, aplicando as tags de cartoon). Correção: criar no gerador um estilo "editorial fotorrealista técnico" e passar `secao="tecnologia"` ou um novo cluster próprio; ou aceitar o prompt pronto via parâmetro, pulando o cérebro visual.

### 2.8 DRY_RUN consome a cota diária

`salvar_post_astro` do Rail Post grava no `PUB_MEMORY_FILE` **mesmo em DRY_RUN** (linha ~1361, com flag `"dry_run": True`), e `check_daily_post_limit` conta qualquer linha com `published_at` de hoje, sem filtrar `dry_run`. No MT, o `append_jsonl` do `publish_post` tem o mesmo comportamento. Consequência: dois testes DRY_RUN de manhã **bloqueiam as duas publicações reais do dia**. Correção: filtrar `row.get("dry_run")` na contagem, ou não gravar memória em DRY_RUN.

---

## 3. A antiduplicação "inteligente": o que existe de verdade

O fórum explicativo afirma que o sistema de dupla camada (fuzzy 70% + MD5) protege "os portais". A auditoria do código mostra cobertura desigual:

| Proteção | Discover Brazil | Rail Post | Mundo Trilhos |
|---|---|---|---|
| Slug exato no repo | ✅ `post_already_exists_astro` | ❌ | ❌ |
| Fuzzy 70% nos títulos do repo Astro | ✅ | ❌ (só na memória JSONL) | ❌ |
| Fuzzy 70% na memória de publicações | ❌ (não tem PUB_MEMORY) | ✅ `title_already_published` | ❌ (**só match exato normalizado**) |
| MD5 de imagem vs `public/hero/` | ✅ | ✅ | ❌ (não verificado no `salvar_post_astro` do MT)* |

\* O MT tem o pipeline de imagem mais sofisticado (Tribunal Visual, banco próprio, R2), mas não localizei checagem MD5 equivalente à do Rail Post no seu `salvar_post_astro`; se ela existir em trecho não coberto, vale confirmar — se não existir, portar.

Observações qualitativas sobre o mecanismo em si:

1. **`SequenceMatcher` a 0.7 sobre o título inteiro tem risco duplo.** Falso positivo: títulos jornalísticos formulaicos de nicho ("Metrô de São Paulo anuncia expansão da Linha X" vs "Metrô de São Paulo anuncia expansão da Linha Y") facilmente passam de 70% de similaridade de caracteres e bloqueiam pauta legítima. Falso negativo: reordenar palavras ou traduzir derruba o ratio abaixo de 0.7 mesmo com conteúdo idêntico. Uma melhoria de baixo custo: comparar sobre `normalize_title()` (já existe) e complementar com Jaccard de tokens; o fuzzy do Rail Post hoje compara `title.lower()` cru, com acentos e pontuação, o que enviesa o ratio.
2. **MD5 só pega duplicata byte-idêntica.** A mesma foto redimensionada, recomprimida ou com EXIF removido passa. Se o objetivo é "evitar reuso visual" de verdade, o próximo passo é hash perceptual (pHash via `imagehash`, ~10 linhas). O MD5 atual resolve o caso mais comum (mesmo og:image em rodadas seguidas) e é honesto chamá-lo de "camada 1", não de solução completa.
3. **Custo O(n) crescente:** a cada rodada, todos os `.md` do repo são abertos e todos os heros re-hasheados. Com 2 posts/dia isso leva anos para doer, mas um cache de hashes em JSON (`agent_data/*_hashes.json`) elimina o problema por definição.
4. **Colisão de nome de arquivo hero:** o hero é salvo como `{slug}{ext}`. Dois posts com slugs iguais em datas diferentes (o `.md` tem prefixo de data, o hero não) fazem o segundo **sobrescrever silenciosamente a imagem do primeiro post publicado**. Prefixar o hero com o mesmo `stamp` do post resolve.

---

## 4. Achados por agente (P1)

### 4.1 Mundo Trilhos (`MT_agente_ferroviario.py`)

**Pontos fortes** (e são muitos): fail-fast de título com comentário forense do incidente #238517 (excelente prática de registrar o porquê no código); Tribunal Visual com metadados completos de licença do Wikimedia; pipeline de imagem em 4 camadas (fonte real → banco próprio → Wikimedia → IA); memória editorial estruturada com fichas técnicas; upload R2 com taxonomia bilíngue.

**Problemas:**

- **Acoplamento Astro↔WordPress invertido em relação ao objetivo.** O fórum declara o MT como "Headless Astro + GitOps", mas em `run()` → `publish_post()`, a publicação Astro (`salvar_post_astro`) só acontece **depois** e **dentro** do fluxo WordPress, e `_publicar_em_site` do primário faz `raise RuntimeError` em falha. Ou seja: se o WP legado do mundotrilhos cair, o post Astro (o canal declarado como principal) **nunca é gerado**. O canal principal está refém do canal legado. Inverter a ordem (Astro primeiro, WP como replica best-effort) alinha o código à arquitetura declarada.
- **Featured media mockada (id 99999)** — `upload_image_to_wp` retorna 99999 fake para o MundoTrilhos e esse id segue como `featured_media` no payload do WP. Se o WP ainda estiver ativo, é um id inexistente sendo enviado; se não estiver, é código morto perigoso. Decidir: ou o WP saiu do jogo (remover o caminho inteiro), ou não saiu (não mockar).
- `title_already_published` sem fuzzy (ver tabela da seção 3) — o incidente que motivou o fail-fast de título mostra que o MT é justamente o site com histórico de publicação lixo; merece a mesma proteção do Rail Post.
- `log()` usa prefixo `[FER]` — idêntico ao do Rail Post. Em logs agregados/journald é impossível distinguir os dois agentes. Trocar para `[MT]` e `[RP]`.
- Token do GitHub embutido na URL de push (`https://{token}@github.com/...`): o token pode vazar em `ps`, em mensagens de erro do git e no `push_r.stderr` que é logado. O turismo já usa o formato `x-access-token:{token}@` (melhor), mas o ideal nos três é `git -c http.extraheader="AUTHORIZATION: ..."` ou credential helper — e **nunca logar stderr cru de push com URL autenticada**.

### 4.2 Rail Post (`agente_rail_post.py`)

Além do achado crítico 2.2:

- **Docstring completamente desatualizada**: diz "crônica técnica em português", cita credenciais WP do Cafezinho e se autodescreve como "Agente ferroviário do Mundo dos Trilhos". Para um arquivo que será refatorado por terceiros (Fable), o cabeçalho ativamente desinforma.
- **Vestígio de acesso ao Cafezinho viola o isolamento declarado.** `SITE = os.environ.get("WP_SITE", "https://controle.ocafezinho.com")` com `WP_USER_CAFEZINHO`/`WP_PASS_CAFEZINHO`, e `upload_image_to_wp()` aponta para esse SITE. Hoje a função parece código morto (o fluxo Astro não a chama), mas o fórum explicativo afirma "os scripts dos agentes temáticos não interagem e não compartilham chaves com a infraestrutura do mirror/portal". O código contradiz a governança: remover `SITE/USER/PASSWORD` e `upload_image_to_wp` inteiros.
- **A correção fail-fast de título do MT não foi portada.** O Rail Post ainda faz `title = title[:108].strip()` e segue — exatamente o comportamento que causou a publicação do título-lixo no MT em abril. É o exemplo canônico do custo da duplicação de código.
- Link registrado na memória usa formato errado: `railpost.news/blog/{pub_date.lower().replace(' ','-')}-{slug}` gera `july-14-2026-slug`, enquanto o Telegram/arquivo real usam `{stamp}-{slug}` (`20260714-slug`). Os links gravados no JSONL estão quebrados.
- `choose_topic()` calcula `brasil_gap` e não usa (dead code); a probabilidade Brasil é 0.15 fixa — ok para a linha internacional, só remover a variável.
- `country="us"` minúsculo como default do `search_brave` (o mapeamento usa "US"); a Brave aceita, mas padronizar.

### 4.3 Discover Brazil (`agente_turismo_embratur.py`)

**Pontos fortes:** é o único agente com separação limpa PT (redação) → EN (tradução/adaptação); prompts editoriais de título excelentes (proibição explícita de adjetivos vagos com lista negra, exemplos bons/maus, sentence case — o melhor prompt de título do ecossistema); `normalize_meta` com whitelist rígida de categorias/tags (evita taxonomia inventada pelo LLM); Tribunal Visual iterando candidatas.

**Problemas além dos críticos 2.4 e 2.5:**

- **Sem lock nenhum** (nem o PID quebrado dos irmãos). Duas execuções simultâneas competem pelo repo git.
- **Escapes literais nos prompts:** `f"TÍTULO: {l['title']}\\nCONTEUDO: {txt}"` e `"\\n\\n".join(textos)` inserem a sequência literal `\n` (barra + n) no texto do prompt, não quebras de linha. Os modelos toleram, mas é sujeira que degrada a legibilidade do prompt e denuncia copy/paste com dupla escapagem. Trocar por `\n` real.
- `check_daily_post_limit` com `STATE_FILE` .json conta **no máximo 1** post da memória (só existe `ultimo_post_sucesso`, um timestamp único). O limite de 2 fica dependendo exclusivamente da contagem de arquivos no repo — que funciona, mas se o repo estiver dessincronizado (pull falhou), o limite fura. Sugestão: trocar o estado para uma lista `posts_sucesso_hoje` ou adotar JSONL como os irmãos.
- Rotação de pauta por `random.choice(TOPICOS)` sem memória: pode repetir "praias nordeste" três dias seguidos. Os irmãos têm rotação com histórico (`last_topics`); portar são ~5 linhas.
- `post_already_exists_astro`: o teste `if slug in f` (substring) dá falso positivo para slugs curtos contidos em slugs maiores; usar igualdade após remover o prefixo de data.
- Chat ID do Telegram hardcoded no código como default (`"-1002279934759"`, comentário "augusto ou zizi") — mover para .env e limpar o comentário.
- `load_dotenv(".env.unificado")` relativo ao CWD **e** `carregar_chaves` na sequência: redundante e dependente do diretório de execução; `carregar_chaves` já resolve.

### 4.4 Roteador (`agente_roteador_llm.py`)

O módulo mais maduro do pacote: cascata intra e cross-família com raciocínio documentado, cache Anthropic com threshold correto, downgrade automático para Haiku em gate-calls ≤20 tokens (ótima otimização de custo), tratamento diferenciado de `max_completion_tokens` e de modelos sem `temperature`, tribunal visual com cross-check de segunda passada contra contradição título/legenda (defesa em camadas genuína) e contabilização de tokens em todos os caminhos. Ressalvas:

- `decidir_ordem_ias(contexto, tema)` ignora `tema` — parâmetro fantasma na API pública.
- Monkey-patch global de `obter_modelos_candidatos` em `gerar_texto_modelo_especifico` — o próprio comentário admite o hack. Não é thread-safe; como os agentes rodam em processos separados hoje, não explode, mas é uma mina para o dia em que algo virar thread. A refatoração sugerida no comentário (aceitar lista de modelos como parâmetro) é simples e vale fazer junto com a revisão do Fable.
- Fallback REST do Gemini ignora `temperature` e `max_tokens` (payload só tem contents) — comportamento silenciosamente diferente do SDK.
- `limpar_citacoes_llm` remove qualquer `[1]`, `[2]` do texto — se algum artigo legitimamente usar notas numeradas, elas somem. Aceitável para o caso de uso, mas documentar.
- **Política de falha inconsistente entre chamadores:** o tribunal visual do roteador é fail-closed (erro → REPROVADA), mas `_tribunal_visual_aprovou` do MT é fail-open (erro → aprova). Decidir uma política por tipo de risco (sugestão: imagem de fonte externa fail-closed; imagem do banco próprio fail-open) e uniformizar.
- Divergência com a documentação: o fórum explicativo diz que o roteador escala "DeepSeek, Gemini, **Qwen**, GPT, Mistral". Qwen não existe no código; DeepSeek só aparece na fila de comentarista. Atualizar o fórum.

### 4.5 `carregar_chaves.py`

- **Docstring mente sobre a prioridade:** diz que `chaves_novas.env` vem primeiro, mas `_CANDIDATOS` começa por `/root/.env.unificado`. Como `setdefault` faz o primeiro arquivo vencer, a ordem real importa — corrigir a docstring (ou a lista).
- Sanity check verifica `WP_USER`/`WP_USER_CAFEZINHO` — variáveis do ecossistema Cafezinho — dentro de um módulo compartilhado pelos agentes temáticos, que por governança não deveriam depender dessas chaves. Nos temáticos, esse aviso é ruído permanente; condicionar o check ou movê-lo para os agentes que realmente usam WP.
- Parse de .env não trata valores com `=` embutido corretamente? Trata (split com maxsplit=1) ✅ — mas remove aspas de forma ingênua (`strip('"').strip("'")`) que corrompe valores legitimamente entre aspas mistas; caso raro, registrar apenas.

### 4.6 `gerador_imagem_editorial.py`

Além do 2.6 e 2.7:

- Docstring do pipeline desatualizada: declara "1. Ideogram (primário) 2. Flux (fallback)", o código faz Flux → Ideogram → DALL-E. Atualizar.
- `sys.path.append` para `"Projeto Cafezinho Agentes/root"` relativo ao arquivo — acoplamento frágil à estrutura de pastas de outro projeto; no servidor NYC esse caminho provavelmente nem existe e o import cai no fallback silenciosamente.
- O módulo se declara "para o Agente Cafezinho v8" mas é dependência direta dos temáticos; se os temáticos vão viver em servidor próprio, esse módulo precisa de uma versão neutra (sem filosofia de charge política como default).

### 4.7 `util_indexing.py`

Além do crítico 2.3: módulo bem escrito (flock correto, dedupe diário, cota, fila para daemon, logs estruturados). A arquitetura "síncrono + fila" com justificativa da mudança de 08/06 é exemplar. Só precisa: incluir os domínios temáticos (após confirmar o domínio canônico do MT), corrigir o `lstrip`, e — importante — **os agentes Astro precisam chamá-lo** após o push (a URL final é determinística: `https://dominio/blog/{stamp}-{slug}`), senão o módulo continua perfeito e inútil para 2 dos 3 sites.

---

## 5. Segurança e Segredos (transversal)

1. **Credenciais em texto plano na documentação:** o fórum explicativo publica usuário/senha do mirror (`cafezinho / 000`) e o IP do servidor. Documentos de governança circulam (foram zipados para revisão externa); recomendo remover credenciais de qualquer .md e referenciá-las como "ver .env.unificado". E, francamente, a senha `000` num endpoint exposto à internet só se sustenta se o noindex + o conteúdo espelhado não tiverem nenhum valor de ataque — como o mirror compartilha máquina/infra com o resto, trocar por senha real custa um minuto.
2. Token GitHub na URL de push + stderr logado (seção 4.1) — vale para os três agentes.
3. Chave Gemini na query string (`?key=...`) é o padrão da API do Google, mas garantir que nenhuma URL completa vá para log em caso de erro (hoje `r.text` é logado, não a URL — ok).
4. `POST_STATUS = "publish"` com justificativa "WP bloqueia drafts com categorias (401)" — significa que qualquer execução acidental publica direto em produção. O DRY_RUN mitiga, mas como visto em 2.8, ele tem efeito colateral na cota. Consertar juntos.

---

## 6. Duplicação de código: a raiz de metade dos problemas

`MT_agente_ferroviario.py` e `agente_rail_post.py` compartilham cerca de 70–80% do corpo: helpers idênticos, `BASE_QUERIES` idênticos (byte a byte, 100 linhas duplicadas), `search_brave`, `fetch_and_extract`, `score_source`, `select_best_sources`, `auditoria_llm_fontes`, `validate_*`, `acquire_lock`, lógica git. As divergências observadas não são features — são **correções que ficaram para trás**:

- fail-fast de título: só no MT;
- fuzzy dedupe de título: só no Rail Post;
- `search_lang` no request Brave: só no MT (o Rail Post não envia o parâmetro);
- `detect_lang_country` do MT mapeia vi/hu para US "não suportado", o do Rail Post mapeia VN/HU direto — um dos dois está errado;
- checagem MD5 de hero: só no Rail Post/Turismo.

**Recomendação estrutural (para a refatoração do Fable):** extrair um pacote `nucleo_tematico/` com módulos `busca.py` (Brave + extração + scoring), `dedupe.py` (título fuzzy + hash de imagem, com política única), `publicacao_astro.py` (frontmatter + git com lock e push seguro), `limites.py` (cota diária com flock e filtro de dry_run) e `locks.py`. Cada agente vira um arquivo de ~300 linhas com apenas: tópicos, prompts, idioma e taxonomia. Isso elimina a classe inteira de bugs "corrigido num, esquecido no outro", que é hoje o padrão dominante de defeito do ecossistema.

---

## 7. Qualidade dos Prompts (avaliação editorial)

**O que está muito bom:**
- Prompt de título do turismo (lista negra de adjetivos + exemplos positivos/negativos + sentence case): referência; portar o padrão para MT/Rail Post.
- Auditoria de fontes em batch com formato de saída estruturado por linha e parser tolerante: barato e eficaz.
- Tribunal Visual: as 6 checagens + exemplos bons/maus de legenda + cross-check de entidade são o mecanismo anti-alucinação visual mais robusto do pacote.
- Factcheck de anacronismo com contexto temporal explícito: boa ideia; ressalva abaixo.

**O que precisa de atenção:**
- O factcheck hardcoda titulares de cargos ("Donald Trump é presidente; Lula é o atual presidente") em string de código. Isso apodrece: qualquer mudança política transforma o factchecker no próprio gerador de anacronismo. Mover para um JSON de contexto temporal atualizável (ou para a `diretriz_geral.json` que já existe).
- Todos os gates LLM são fail-open ("sem resposta → aprovando por default"). Coerente com a filosofia "a máquina não pode parar", mas significa que nos dias em que as APIs degradam, **todas as proteções desligam simultaneamente**. Sugestão mínima: quando 2+ gates falharem na mesma rodada, abortar a publicação em vez de aprovar tudo.
- Parsers de veredito por posição de substring ("quem aparece primeiro ganha") funcionam, mas o mesmo problema já foi resolvido de forma mais limpa no tribunal (normalização + negações explícitas); unificar num helper `parse_veredito()`.

---

## 8. Divergências Código × Fórum Explicativo (para atualizar a documentação)

1. §3-A afirma fuzzy 70% "nos agentes" — o MT não tem (seção 3).
2. §3-A afirma varredura de títulos "em `src/content/blog/` **e** no log de memória" — o Rail Post só olha a memória; o turismo só olha o repo.
3. §1 lista o domínio `mundodostrilhos.com`; o código usa `mundotrilhos.com` (crítico 2.3).
4. §5 descreve o roteador com "DeepSeek, Gemini, **Qwen**, GPT, Mistral" — Qwen inexiste no código; xAI/Grok e Anthropic (que são centrais nas filas revisor/auditor) nem são citados.
5. Metas de indexação (§ Metas Estratégicas) não têm implementação para Rail Post e Discover Brazil (crítico 2.3).
6. §4 declara isolamento total do Cafezinho — o Rail Post carrega credenciais e endpoint do Cafezinho como default (seção 4.2).

---

## 9. Plano de Ação Priorizado

**P0 — esta semana (bugs que corrompem os objetivos de negócio):**
1. Corrigir `acquire_lock` nos dois agentes ferroviários (flock) e adicionar lock ao turismo. (2.1)
2. Reescrever prompts do Rail Post em inglês e remover identidade O Cafezinho/linha política. (2.2)
3. Confirmar domínio canônico do Mundo Trilhos; incluir os três domínios temáticos na whitelist; corrigir `lstrip`; fazer os agentes Astro dispararem `notificar_e_logar` pós-push. (2.3)
4. Eliminar o `license: "cc-by-sa"` falso no turismo; restringir fontes de imagem a licença verificável. (2.4)
5. `timeout=30` no `search_brave` do turismo. (2.5)
6. Filtrar `dry_run` na contagem da cota diária. (2.8)

**P1 — próximas duas semanas:**
7. Inverter ordem Astro/WP no MT (Astro primário) e decidir o destino do caminho WordPress. (4.1)
8. Portar fail-fast de título ao Rail Post e fuzzy dedupe + MD5 ao MT (tabela §3).
9. Corrigir ordem de argumentos em `gerador_imagem_editorial._chamar_llm` e criar estilo visual fotorrealista para os portais técnicos. (2.6, 2.7)
10. Push git via header/credential helper; parar de logar stderr com URL autenticada; remover vestígios WP-Cafezinho do Rail Post.
11. Corrigir link gravado na memória do Rail Post; prefixos de log distintos; hero com prefixo de data.

**P2 — junto com a refatoração do Fable:**
12. Extrair `nucleo_tematico/` compartilhado (seção 6).
13. pHash para dedupe visual; Jaccard complementar no dedupe de título; cache de hashes.
14. Contexto temporal do factcheck em arquivo de dados; política unificada de fail-open/closed com circuit-breaker.
15. Atualizar o fórum explicativo (seção 8) e remover credenciais da documentação.

---

## 10. Conclusão

O ecossistema está bem acima do "script de spam de blog": há memória editorial, auditoria multi-modelo, tribunal visual com defesa em camadas, contabilidade de custos e registro forense de incidentes no próprio código — práticas raras em agentes autônomos. O que compromete a nota final é a **execução desigual entre os três agentes**: o mesmo pipeline existe em três versões que envelheceram separadas, e cada correção importante (fail-fast, fuzzy, MD5, timeout, idioma) vive em apenas um deles. O Rail Post, em particular, ainda é um clone do MT com a pintura trocada pela metade — e é o único cujo defeito (idioma/identidade) é visível diretamente ao leitor e ao Google.

Nota de qualidade por componente (0–10, critério: alinhamento ao objetivo declarado + robustez + segurança):

- Roteador LLM: **8,0**
- util_indexing (módulo em si): **7,5** — mas **3,0** em efetividade para o ecossistema até a whitelist/integração serem corrigidas
- Mundo Trilhos: **6,5**
- Discover Brazil: **6,0** (desconto pesado pelo risco legal de licença)
- Rail Post: **4,5** (conflito de identidade/idioma é falha de missão)
- gerador_imagem_editorial: **5,5** (bom motor, briefing errado para os temáticos)
- carregar_chaves: **6,5**

*Documento gerado para servir de insumo à rodada de refatoração do Fable, em conjunto com `agentes_tematicos.zip` e o fórum explicativo de 14/07/2026.*
