# Fórum — Correção do domínio Ceará Digital no registry do Sentinela

**Data:** 2026-08-07 (~16:20 BRT)
**Quem:** Kimi K3/ZCode (conversa "Mapa Rio: página Quem Somos"), por ordem direta do Miguel
**Tema:** endereço do Ceará no `site_registry.json` estava errado

## Decisão

O endereço correto do site Ceará Digital é **`https://ceara.digital`** — NÃO `cearadigital.news`.

O registry do Sentinela (`Projeto Cafezinho Agentes/root/ferramentas/sentinela_tematicos/site_registry.json`) trazia `https://www.cearadigital.news`, domínio que **não tem DNS**. Como o sentinela lê o alvo exclusivamente do registry, todas as verificações que reportaram "cearadigital.news SEM DNS / fora do ar" (incl. a revisão temáticos da sessão Qwen 07/08 e a varredura de favicons desta conversa) foram **falso alarme causado pelo registro errado** — o site de verdade está no ar.

## Evidência (verificado ao vivo 07/08 ~16:15)

- `https://ceara.digital` → **200** (apex e `www`; `http://` redireciona p/ https)
- Favicons da marca: `/favicon.png`, `/favicon.svg`, `/favicon.ico` → **200**
- `<link rel="canonical" href="https://ceara.digital/">` na home
- Repo `sites-v4/ceara/astro.config.mjs`: `site: 'https://ceara.digital'` (repo já apontava pro domínio certo; só o registry estava errado)

## Mudança feita

- `site_registry.json` → entrada `ceara_digital.url`: `https://www.cearadigital.news` → **`https://ceara.digital`** (+ `atualizado_em: 2026-08-07`), conforme a regra do próprio registry ("Qualquer mudança de site/URL/repo exige edição aqui + nota no fórum").

## Pendência (decisão do Miguel) — ✅ RESOLVIDA

A entrada seguia `cadencia: "pre_lancamento"` / `status: "allowlist_sem_alerta"`, mas o site está claramente publicado e servindo conteúdo. **Miguel decide:** promover a `ativo` (diário/48h como os outros 7)? Se sim, é só dizer que eu altero.

### Resolução (2026-08-07 ~13:40 BRT — ZCode/Qwen 3.8, ordem direta do Miguel)

Miguel ordenou: **"Promover o Ceará ativo"** (confirmou ainda que o domínio sempre foi `ceara.digital` — por isso o estranhamento com o endereço velho). Entrada `ceara_digital` promovida no `site_registry.json`:

- `status`: `allowlist_sem_alerta` → **`ativo`**
- `cadencia`: `pre_lancamento` → **`diario`**
- `limiar_horas`: `null` → **`48`** (igual aos outros 7)
- `metrica_frescor`: mantida **`home_date`** — verificada com evidência: a home expõe `datetime` server-rendered com posts do próprio dia (200, 186KB, `datetime="2026-08-07"` na home).

Com isso o Sentinela passa a vigiar o Ceará Digital como os demais (alerta se home ficar >48h sem conteúdo novo).

## Ver também

- `Cerebro/Foruns/forum_vigilia_tematicos_3_sinais_falso_alarme_20260807.md` (falsos alarmes de vigília — mesma família de lição: conferir o alvo antes do veredito)
