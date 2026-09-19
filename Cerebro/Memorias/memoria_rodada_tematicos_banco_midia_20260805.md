# MEMÓRIA — Rodada temáticos: destaques mini, about pages, trava turismo, pautas GSN, Banco Mídia V4 (05/08/2026)

**Data:** 2026-08-05 11:20→12:30 BRT · **Agente:** ZCode/Kimi K3
**Fórum irmão:** `Foruns/forum_rodada_tematicos_banco_midia_20260805.md`

## 1. Destaques mini (`fv-mini`)

6 templates (`sites-v4/*/src/pages/index.astro`): h2 ganhou classe `fv-mini` (0.78rem/800/0.14em/uppercase/`var(--accent)` + barra 6×14 accent antes) inserida antes do primeiro `</style>`; textos encurtados ("Destaques"/"Featured"). Cores por `--accent` de cada site: trilhos #d35400 (laranja), railpost #c0392b, GSN #9e2f50, demais #2337ff. GSN usava `.section-title` compartilhado com "Latest Dispatches" — por isso a classe nova (não editei a regra global).

## 2. About pages

- Rio: `riocarta/src/pages/quem-somos.astro` + `public/hero/quem-somos-rio.jpg` (Wikimedia `File:Rio-panorama-Botafogo-Sugarloaf.jpg` 1920px, CC BY 4.0 Acediscovery). Causa da "imagem quebrada": `BlogPost.astro` renderiza `div.hero-image` (fundo #f0f3f7) mesmo sem hero → caixa cinza no topo.
- DB: `discoverbrazil/src/pages/about.astro` reescrito (era lorem ipsum do starter + section Editor fora do `<Layout>`) + `public/hero/about-discover-brazil.jpg` (`File:Iguazu Falls (144902383).jpeg` 1920px, CC BY 3.0 Mayra Vazquez). Domínio canônico DB = www.discoverbrazil.news (apex 307→www; conferir sempre com -L).

## 3. Trava turismo DB + pautas GSN

- `discoverbrazil.json`: `editorial.foco_local` (reuso do gate de localidade do `produtor.py` como gate TEMÁTICO — 48 termos: tourism/travel/destinos BR; veto sem LLM; `feeds_locais: []` pois nenhum feed DB é tematicamente confiável por origem). Backup `.bak_pre_foco_turismo_20260805`.
- `globalsouth.json`: +6 brave_queries (Irã/Hormuz, Trump polls, Lula polls, vistos EUA-BR, BR×Argentina, Lula diplomacia). Backup `.bak_pre_pautas_20260805`.
- Contratos (Regra-mãe): `globalsouth.md` DIRETRIZ 2026-08-05 (Irã pró-Irã, queda Trump, Brasil em EN toda semana pró-Brasil/anti-Milei/anti-Trump, sempre pauta Lula) · `discoverbrazil.md` DIRETRIZ 2026-08-05 (SOMENTE turismo no Brasil).

## 4. Banco de Mídia V4 → temáticos

**Arqueologia (importante p/ futuros agentes):**
- `acervo_midia/acervo.db` (NYC): 81 approved, mas 55 com `storage_key` apontando p/ `canonico/…` que **NÃO existe** no bucket `cafezinho` (0/8 head test) e 26 sem chave; 52 storage_url = endpoint S3 (morto p/ GET anônimo); 3 com pub-7c53…r2.dev também 404; **26 com URL pública viva** (wikimedia/flickr) — só essas aproveitáveis.
- **Banco Ouro** (`agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db`, NYC): 661 mídias de lideranças com `r2_key ouro/…` que **EXISTEM** (10/10). Lula ×99, Alckmin ×95, Haddad ×88, Alcolumbre ×67, Jair ×62, Motta ×45, Moraes ×41… Licença `licenca_confirmada`, CC BY-SA 4.0 / uso editorial.

**Implementação local (`agentes_tematicos/v4/`):**
- `banco_midia_dump_nyc.py` (sobe p/ NYC): lê os 2 DBs, baixa ouro via boto3 **paralelo 24 workers** (serial estourava 10 min) + acervo público via HTTP → tar.gz.
- `banco_midia_sync.py` (local; cron `20 6 * * 1`): scp dump → tar → extrai p/ `agent_data/v4/banco_midia/` (index.json + img/). Estreia: **666 mídias, 1,8 GB, 0 faltantes**.
- `nucleo_banco_midia.py`: match por entidade/tag normalizada (sem acento); frase ≥5 chars contida no título OU token forte whitelist (`_TOKENS_FORTES`: lula, milei, trump, putin, alckmin, haddad, alcolumbre…). Cache por mtime.
- `publicador.py` `_buscar_hero` **FASE 0** (antes de Wikimedia): copia do espelho local → dedup conteúdo → `julgar_imagem` → `padronizar_hero` → registra hash; chave anti-reuso `banco:<id>`. Falha/ausência do banco → cascata externa normal (try/except total).
- Testes matcher 7/7: "Lula leads…" → 99 cand; "Lulau Festival" → 0 (tokenização por palavra); sem entidade → 0.

## 5. Pendências

- Acervo morto (52 S3 + 3 r2.dev quebrados): re-subir binários ou aposentar linhas — o Ouro cobre lideranças; decisão não urgente.
- Próxima rodada GSN (13:45 destaques / 16:00 pipeline): observar se pautas Lula/Irã entram e se a hero sai do banco (log "hero do BANCO DE MÍDIA V4").
- Sync semanal pega fotos novas do Ouro automaticamente.
