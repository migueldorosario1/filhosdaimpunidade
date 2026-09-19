# Memória — Painel CCTV V6: 4 correções (health check, Ceará, destaques, fóruns)

**Data:** 2026-08-07 ~14:15 BRT · **Agente:** ZCode/Qwen 3.8 · **Fórum par:** `Foruns/forum_painel_v6_4_correcoes_health_ceara_destaques_foruns_20260807.md`

## Ambiente / arquivos tocados

- **Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`** (serviço `cctv-v6`, porta 8084, nginx `location /v6/`):
  - Backup criado: `painel_cctv_v6.py.bak_ceara_destaques_20260807`.
  - Patch 1 (linha 1199): `"url": "https://www.cearadigital.news"` → `"url": "https://ceara.digital"`.
  - Patch 2 (linha 1544): `com_chave = _dest_key_ok(query)` → `com_chave = True  # Miguel 07/08: sem chave — modo edição direto`.
  - `python3 -m py_compile` OK; `sudo systemctl restart cctv-v6` → active.
- **Crontab local do Miguel:** linha do sync de fóruns corrigida:
  - Antes: `7,37 * * * * rsync -a --delete -e ssh /home/migueldorosario/cerebro-miguel/projeto_cafezinho_agentes/foruns/ tencent:/home/ubuntu/cafezinho/v6_data/foruns/`
  - Depois: `7,37 * * * * rsync -a --delete -e ssh "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/" tencent:/home/ubuntu/cafezinho/v6_data/foruns/`
  - Backup do crontab: `/tmp/crontab.bak_pre_foruns_canonico_20260807`.
  - `FORUNS_DIR` no código (linha 34) = `CCTV_V6_FORUNS` env ou `/home/ubuntu/cafezinho/v6_data/foruns` (intacto — só a fonte do rsync mudou).
- **Sync manual executado:** `rsync -a --delete -e ssh ".../Cerebro/Foruns/" tencent:.../v6_data/foruns/` → exit 0.

## Comandos / provas

```text
# Ceará URL (antes vs depois)
grep -c '"url": "https://www.cearadigital.news"' → 1 (única)
replace aplicado → 0

# Destaques
grep -c 'com_chave = _dest_key_ok(query)' → 1 (única)
replace aplicado → 0

# Verificação ao vivo (curl ao painel)
/v6/tematicos/ceara-digital → 14× "ceara.digital", 0× "cearadigital.news"
/v6/destaques              → 6× "acao=toggle", 0× "🔒 Modo leitura"
/v6/foruns?f=todos         → 42× "20260807", "319 fóruns ·"
/v6/servidores             → 8 online, 2 falha

# Fóruns no Tencent (antes/depois do sync)
antes: ls *20260807* | wc -l → 0
depois: 21  (total 332, era 1136 do espelho estagnado)

# Health independente
GSN  https://global-south-news.vercel.app/ → 200 (404 em path raiz = normal Vercel sem rota /)
Alibaba 39.106.184.215:80 → TCP timeout/recusada (REAL offline)
```

## Decisões técnicas

1. **Ceará:** replace direto (URL única, confirmada). Não mexer no `site_registry.json` do Sentinela aqui — sessão Mapa Rio já corrigiu hoje (`https://ceara.digital`).
2. **Destaques:** preferi `com_chave = True` (1 linha) em vez de remover toda a lógica de `_dest_key_ok` / `.destaques_key` — mínimo, reversível, mantém a chave no servidor para um futuro re-gate. Ação fica: sempre que o painel V6 ficar publicamente exposto, reverter.
3. **Fóruns:** corrigir a **fonte** do rsync era o certo (não contornar no código). O `cerebro-miguel/` é repo git legado, não fonte de verdade. Agora `--delete` reflete fielmente o canônico (fóruns removidos do canônico somem do painel — comportamento desejado).
4. **GSN:** não mexer (saudável). **Alibaba:** não reiniciar sem ordem do Miguel.

## Lições

1. Quando uma página "desatualizada" serve dados por sincronização, **primeiro verificar de onde vem o sync** — pode ser fonte errada, não falha de refresh.
2. `cerebro-miguel/` ≠ Cérebro canônico. Mapa mental importante: canônico = `Downloads/Antigravity Google/Cerebro/`; `cerebro-miguel/` = espelho git histórico (ainda sincronizado ao GitHub por outro cron, segue no ar, intacto).
3. "Falha" no health check pode ser 3 coisas diferentes: (a) site real offline (Alibaba — agir), (b) transitório (GSN — ignorar/retentar), (c) config errada no próprio painel (Ceará — corrigir fonte). Diagnosticar antes de agir.

## Estado da missão
- **Aconteceu:** 4 pontos endereçados (Ceará URL ✓, destaques sem chave ✓, fóruns sincronizando do canônico com 21 de hoje ✓, GSN/Alibaba diagnosticados).
- **Falta:** decisão do Miguel sobre o Alibaba Beijing offline.
- **Preciso do Miguel:** (1) Alibaba — reiniciar ou deixar? (2) confirmar visualmente as 3 páginas.
