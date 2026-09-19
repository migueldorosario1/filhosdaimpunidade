# FÓRUM — V4: mesma hero image em vários posts (29/07/2026)

**Data:** 2026-07-29 ~16:20–17:10 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel (chat, com screenshot da home riocarta.com): "tem varios posts com a mesma imagem. pode codar para evitar isso?"

## 1. O problema

A home do riocarta.com mostrava 3 posts seguidos com **a mesma foto do Cristo Redentor ao pôr do sol** ("Posse na Alerj…", "Paes lidera com 42%…", "Prefeitura do Rio leva ações contra dengue…"). Auditoria no repo (`sites-v4/riocarta/public/hero`, MD5):

- A foto do Cristo (Pixabay, usuário `heibe`, id 1303951) estava em **10 posts** publicados entre 25/07 e 29/07 — byte a byte idêntica.
- 7 grupos de duplicatas no Rio Carta (27 arquivos).
- Nos 8 sites V4: **724 heroes no acervo, só 618 únicas → 106 cópias duplicadas publicadas** (o problema era da rede inteira, não só do Rio Carta).

## 2. Causa raiz (provada, não hipótese)

O pipeline já tinha dedup anti-reuso (`heroes_usadas.json`, desde 25/07) — **mas por URL**. Teste empírico: duas queries idênticas ao Pixabay retornam a mesma foto com **`largeImageURL` diferentes** (URL assinada/expirável do CDN). Ou seja: para Pixabay o dedup por URL **nunca casava** — cada rodada baixava a mesma foto como se fosse nova. O juiz visual aprovava (a foto é boa e genérica o suficiente para pautas da cidade) e o post ia ao ar com imagem repetida.

## 3. Correção (duas camadas independentes)

Patch `V4_PATCH_DEDUP_HERO_20260729` — `agentes_tematicos/v4/` (backups `.bak_zcode_20260729_dedup_hash`):

1. **ID estável por fonte (pré-download):** `nucleo_visao_fallback.py` passa a devolver o id imutável de cada banco (`pixabay:<id>`, `pexels:<id>`, `unsplash:<id>`, `openverse:<uuid>`); Wikimedia ganha chave `wm:<File:title>`. `publicador.py` checa E registra essas chaves junto com a URL em `heroes_usadas.json` (formato novo é retrocompatível — o arquivo aceita qualquer string).
2. **Hash de conteúdo (pós-download, pré-juíz):** novo registry `agent_data/heroes_hash_usadas.json` com MD5 (exato) + **aHash 16×16 perceptual** (casa a mesma foto em resolução/re-encode diferente). Candidata duplicada é descartada **antes** de chamar o juiz visual → economiza visão-LLM (regra anti-token). Limiar Hamming **16/256 bits**, calibrado com o acervo real: mesma foto raw×padronizada = 13; foto diferente mais próxima = 47 (stock); conceitos IA similares ≥ 19.
3. **`resgate_hero.py`** atualizado para o mesmo funil (ele é usado para trocar hero de posts já publicados — sem o patch poderia reintroduzir duplicata).
4. `retrofit_hero_mundotrilhos.py`: corrigido unpacking de retorno (já estava quebrado de antes, 2 valores para tupla de 3).

## 4. Backfill

Registry de hash semeado com **todas as 724 heroes publicadas** dos 8 sites V4 (618 únicas) → nenhuma imagem já no ar pode ser reutilizada daqui pra frente. O registry é **compartilhado entre os sites** (mesmo `agent_data/`), o que também impede a mesma foto em portais diferentes.

## 5. Validação

- `py_compile` OK nos 4 arquivos.
- Smoke end-to-end (juiz mockado, sem gastar LLM): cascata com a foto proibida do heibe → **camada 1 pula por ID**; segunda cópia da mesma foto com ID diferente → **camada 2 pula por hash**; pipeline aceita a terceira candidata (foto diferente) e registra `pixabay:<id>` para o futuro.
- Controle negativo: foto diferente fica a Hamming 47 → não é bloqueada.
- Registry limpo de artefatos de teste (rebuild final a partir dos arquivos publicados).

## 6. Pendências / decisões abertas

- ~~**Heroes duplicadas JÁ PUBLICADAS**~~ → **EXECUTADO (Miguel: "sim", 29/07 ~17:20 BRT)** — ver §7.
- Observar a próxima rodada do orquestrador (`--site riocarta` roda a cada 8h, minuto :10) confirmando variedade de heroes.

## 7. Retrofit executado (29/07 17:20–18:15 BRT)

**Ferramenta:** `agentes_tematicos/v4/retrofit_hero_duplicadas.py` (novo) — varre heroes por MD5, mantém a do post mais antigo de cada grupo e busca imagem nova para as demais pelo mesmo funil do publicador (Wikimedia → cascata stock → juiz visual). Segurança: busca em TEMP DIR (rejeição do juiz jamais apaga a hero viva), só sobrescreve após aprovação, `heroImage` (URL) não muda, sem imagem aprovada = mantém a duplicata, commit/push por site.

**Achado durante o retrofit (bug na cura):** a 1ª troca baixou uma foto que ficou byte-idêntica a outra hero já publicada APÓS a padronização blur-fill — a raw escapava do check (aHash raw × publicada-padronizada > limiar). Cura da cura: **2ª checagem de hash pós-padronização** + registro duplo (raw + padronizada) no `publicador.py`.

**Resultado final (rede V4):**

| Site | Trocas | Órfãs removidas | Estado |
|---|---|---|---|
| riocarta | 18 | 3 | ✅ 0 duplicatas (validado no ar) |
| ceara | 7 | 4 | ✅ 0 duplicatas |
| railpost | 6 | — | ✅ 0 duplicatas |
| discoverbrazil | 5 | — | ✅ 0 duplicatas |
| mundotrilhos | 2 | 3 | ✅ 0 duplicatas |
| aiatolah | 3 | — | ✅ 0 duplicatas |
| mapario | 1 | — | ✅ 0 duplicatas |
| globalsouth | 0 (só órfãs) | 41 | ✅ 0 duplicatas |

- **42 posts** receberam imagens novas e únicas (todas aprovadas pelo juiz visual; 0 falhas "sem imagem").
- **51 arquivos órfãos** (heroes mortas, sem referência) removidos dos repos.
- Os 8 sites terminaram com **0 grupos de duplicatas**; todos os commits pushados (GitHub → Vercel). Validação no ar: hero trocada do riocarta servida pela CDN com MD5 igual ao local.

**Memória técnica:** `Memorias/memoria_v4_hero_duplicada_pixabay_20260729.md` · **Bug:** `BUG-20260729-V4-HERO-DUPLICADA-PIXABAY` (BUGS_RESOLVIDOS)
