# MEMÓRIA TÉCNICA — V4: hero image duplicada em vários posts (2026-07-29)

**Bug:** BUG-20260729-V4-HERO-DUPLICADA-PIXABAY ✅ RESOLVIDO (preventivo)
**Fórum (decisões):** `Foruns/forum_v4_hero_duplicada_pixabay_20260729.md`
**Agente:** ZCode/Kimi K3 · **Duração:** ~16:10–17:10 BRT

## Cadeia de diagnóstico (passo a passo)

1. **Cérebro primeiro (Regra Nº 1):** `CEREBRO_INDEX_RIOCARTA.md` — Rio Carta legado = Droplet DO `159.89.185.209`. Verificado por SSH: clone `/root/riocarta_remote/rio_carta` **parado em 30/06** (último commit `c0c16473`), sem linhas riocarta no crontab. Site porém com posts de 28–29/07 → publicação migrou.
2. **Pipeline vivo encontrado:** `crontab -l` LOCAL → `orquestrador.py --site riocarta` a cada 8h (minuto :10) em `~/Downloads/Antigravity Google/agentes_tematicos/v4/` (V4, 8 sites). Repo Astro: `Projeto Cafezinho Agentes/sites-v4/riocarta` (git→GitHub `riocarta-v4`→Vercel). Confirmado pela memória `memoria_auditoria_custos_telemetria_recuperacao_crons_20260729.md`.
3. **Prova da duplicata:** os 3 posts do screenshot apontam heroes de slugs diferentes, mas `md5sum` idêntico (`0ddcf0926ab36b24189cebb40fcd6d92`). A mesma imagem em **10 posts** (25/07→29/07); 7 grupos/27 arquivos duplicados no Rio Carta; **106 cópias nos 8 sites** (724 arquivos, 618 únicas).
4. **Origem da imagem repetida:** `hero_credit` dos 10 posts = "Photo by heibe on Pixabay" (foto do Cristo ao pôr do sol, Pixabay id **1303951**). Começou em 25/07 — data da autorização da cascata Pixabay/Pexels/Openverse/Unsplash (fórum 25/07).
5. **Causa raiz:** dedup existente (`heroes_usadas.json`, 179 URLs) compara **URL**. Teste empírico: 2 queries idênticas `buscar_pixabay('rio de janeiro christ redeemer')` → mesmas fotos, **`largeImageURL` diferentes em cada chamada** (URL assinada `pixabay.com/get/g<hash>_1280.jpg`, hash muda a cada query). Dedup por URL estruturalmente incapaz de casar → mesma foto baixada/aprovada/publicada em loop.

## Patch aplicado — `V4_PATCH_DEDUP_HERO_20260729`

Backups: `publicador.py.bak_zcode_20260729_dedup_hash`, `nucleo_visao_fallback.py.bak_zcode_20260729_dedup_hash` (em `agentes_tematicos/v4/`).

### `nucleo_visao_fallback.py` — ids estáveis nas 4 buscas
- `buscar_pixabay`: `"id": hit.get("id")` (id numérico imutável — comentário no código registra o bug da URL assinada);
- `buscar_pexels`: `"id": photo.get("id")`;
- `buscar_unsplash`: `"id": photo_id`;
- `buscar_openverse`: `"id": item.get("id")` (UUID).

### `publicador.py` — duas camadas de dedup
- `_registrar_hero_usada(repo_path, chaves)`: aceita **lista** de chaves (URL + ids `"fonte:id"`); retrocompatível com str; teto do arquivo subiu 5000→8000.
- Novos helpers: `_heroes_hash_path`, `_carregar_hash_usadas`, `_ahash_arquivo` (aHash 16×16=256 bits, PIL), `_hashes_arquivo` (MD5+aHash), `_hash_ja_usado`, `_registrar_hash_usado`. Registry: `Projeto Cafezinho Agentes/agent_data/heroes_hash_usadas.json` (compartilhado pelos 8 sites; teto 8000 entradas).
- **`AHASH_LIMIAR = 16`** — calibragem com dados reais do acervo:
  - mesma foto raw (Pixabay 1280×853) × versão publicada padronizada (blur-fill 1200×675): Hamming **13**;
  - foto diferente (controle): **47**;
  - pares publicados mais próximos: conceitos IA/thumbnails YouTube a 9–22 (são imagens diferentes com estilo similar — limiar 16 não os funde, e falha benigna = pular candidata).
- `_buscar_hero(...)` ganha `hashes_usadas` e `repo_path` e **retorna lista de chaves** (não mais URL única):
  - Fase A (Wikimedia): chave estável `wm:<titulo do File:>`; download → **hash check antes do `julgar_imagem`** (economiza visão-LLM); aceite registra URL+wm_key+hashes.
  - Fase B (cascata): chave `"<src>:<id>"` checada antes do download; hash check pós-download pré-juíz; aceite registra URL+id+hashes; regra Unsplash (trigger download) intacta.
  - Fase C (IA/acervo default): retornos adaptados; **acervo default continua multiuso por design** (não entra em nenhum registry — decisão anterior preservada).
- `rodar()`: carrega os dois registries, passa para `_buscar_hero`, persiste todas as chaves no aceite.

### `resgate_hero.py` e `retrofit_hero_mundotrilhos.py`
- Resgate usa o mesmo funil com os 2 registries (ferramenta de troca retroativa de hero — sem o patch reintroduziria duplicata).
- Retrofit: unpacking corrigido para 3 valores (estava quebrado desde antes — tupla de 3 em 2 variáveis).

## Backfill do registry

Script único varreu `sites-v4/*/public/hero/*.jpg`: **724 arquivos → 618 imagens únicas registradas** (MD5+aHash), 106 cópias duplicadas ignoradas. Rebuild final após os smokes para remover artefato de teste. Resultado: toda imagem já publicada na rede V4 está bloqueada contra reuso futuro.

## Validação executada

1. `py_compile` OK: `publicador.py`, `nucleo_visao_fallback.py`, `resgate_hero.py`, `retrofit_hero_mundotrilhos.py`.
2. Prova da URL instável: 2 queries idênticas → 3 fotos iguais com `largeImageURL` todas diferentes (`urls_iguais=False`).
3. Smoke E2E #1 (juiz visual mockado, sem custo LLM; Wikimedia mockado vazio; Pixabay real "rio de janeiro"): 5 candidatas → heibe 1303951 **pulada por hash** ("imagem idêntica já publicada") → aceita foto diferente (12019) — MD5 ≠ da proibida.
4. Smoke E2E #2 (registry com `pixabay:1303951`): heibe **pulada por ID antes do download**; 2ª cópia da mesma foto sob OUTRO id Pixabay **pulada por hash** (prova de que as camadas se complementam); aceita 3ª (NakNakNak), retornando `['url', 'pixabay:3549788']` — id estável registrado para o futuro.
5. Controle negativo: foto diferente a Hamming 47 → não bloqueada.

## Rollback

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google/agentes_tematicos/v4"
cp publicador.py.bak_zcode_20260729_dedup_hash publicador.py
cp nucleo_visao_fallback.py.bak_zcode_20260729_dedup_hash nucleo_visao_fallback.py
python3 -m py_compile publicador.py nucleo_visao_fallback.py
rm -f "../../Projeto Cafezinho Agentes/agent_data/heroes_hash_usadas.json"
```
(`resgate_hero.py`/`retrofit_hero_mundotrilhos.py`: restaurar via git ou deixar — mudanças são aditivas.)

## Lições / regras novas

- **URL de CDN de banco de imagem NÃO é chave de dedup** — Pixabay assina/expira (`get/g<hash>`), Unsplash/Pexels podem variar por tamanho. Chave correta: **id da foto na fonte** + **hash de conteúdo** (MD5 exato + aHash perceptual p/ re-encodes/resizes).
- Dedup de imagem deve rodar **antes** do juiz visual: candidata repetida descartada sem gastar visão-LLM (regra anti-token).
- Registry compartilhado entre os sites evita também a mesma foto em portais diferentes da rede V4.
- Pendente (decisão Miguel): troca retroativa das 106 heroes duplicadas já publicadas (27 no Rio Carta) via `resgate_hero.py` — custa visão-LLM e toca posts indexados.

## Retrofit executado (29/07 17:20–18:15 BRT — Miguel autorizou "sim")

**Ferramenta nova:** `agentes_tematicos/v4/retrofit_hero_duplicadas.py` (compilada; dry-run validado). Lógica: grupos MD5 em `public/hero/*.jpg` → mapa hero→posts via `heroImage` no frontmatter → mantém o post MAIS ANTIGO do grupo (`pubDate`/prefixo do nome) → para os demais, `_buscar_hero` em **TEMP DIR** com `tentativa_atual=1` (só stock, sem IA/acervo) → aprovada pelo juiz real → `shutil.copyfile` sobre a hero viva → `_registrar_hero_usada` + `_atualizar_credito` → commit/push por site. TEMP DIR é a peça-chave de segurança: `_buscar_hero` remove o arquivo candidato em rejeição (juiz/hash) — se apontasse direto para a hero viva, uma rejeição deixaria o post SEM capa.

**Bug encontrado DURANTE a cura:** a 2ª troca do riocarta (campanha-coleta) baixou foto que, após `padronizar_hero` (blur-fill 1200×675), ficou byte-idêntica a `atividades-de-bem-estar...jpg` já publicada — o check pré-juíz usa hashes RAW e o reframe deslocou o aHash além do limiar 16. **Cura da cura (mesmo patch):** 2ª checagem `_hash_ja_usado` PÓS-padronização nas fases A e B do `publicador.py` + registro duplo (raw E padronizada) no registry. Validado: re-run trocou a duplicata residual com nova imagem aprovada (cachorro/Pexels para "bem-estar animal").

**Execução (sequencial — registry compartilhado, sem corrida):**

- `riocarta`: 17 trocas (commit `7824e55`) + 3 órfãs (`3377aba`) + 1 troca residual (`3afad48`) → 0 dups; CDN servindo hero nova (MD5 local == remoto ✅).
- `ceara`: 7/7 + 4 órfãs → 0 dups. `railpost`: 6/6 → 0. `discoverbrazil`: 5/5 → 0. `mundotrilhos`: 2/2 + 3 órfãs → 0. `aiatolah`: 3/3 → 0. `mapario`: 1/1 → 0.
- `globalsouth`: 0 trocas — as 6 duplicatas eram TODAS órfãs (35+ arquivos mortos do pipeline antigo smoke-brief, incl. 22 cópias da mesma imagem "alphabet"); 41 órfãs removidas → 0 dups.
- **Totais: 42 posts com imagens novas/únicas (100% aprovadas pelo juiz Gemini; 0 "SEM imagem"), 51 órfãs removidas, 8/8 sites com 0 grupos duplicados, tudo pushado.**
- Julgamentos ao vivo mostraram o dedup trabalhando: "cascata (pixabay): imagem idêntica já publicada, pulando", "hero já usada antes, pulando: File:2021-05-05 Reunião…", e rejeições corretas do juiz (foto SP para matéria RJ, genéricas off-topic).

**Lição registrada:** arquivos órfãos de hero (sem `heroImage` apontando) são comuns após renames de slug — o retrofit só troca o que tem referência viva; órfãs vão para limpeza separada com `git rm` após grep de referência em `src/` inteiro (cuidado: `src/data/destaques.json` também referencia heroes).
