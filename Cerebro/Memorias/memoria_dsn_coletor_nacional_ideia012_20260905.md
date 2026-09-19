# Memória — DSN Coletor Nacional fase 1 (IDEIA-012, 05/09/2026)

**Autor:** ZM (ZCode/GLM-5.3) · **Fórum-irmão:** `Foruns/forum_dsn_coletor_nacional_ideia012_20260905.md`

## Executado (ordem Miguel ~07:2x, autorização da IDEIA-012 + parecer DS-N-137A)

1. **Adapter NYC** `/root/v4_labs/scripts/dsn_adapter_v41.py` (cron */15 flock): scp do tencent (`-P 38422 ubuntu@43.156.151.165:/home/ubuntu/dsn_coletores/entregas/`) → validação fail-closed (item_key=sha1(url)[:16] · published_at ISO-UTC obrigatório · título ≤140 · corpo ≥800) → INSERT OR IGNORE em `/root/agent_data/v4_verticals/nacional.sqlite3` tabela candidates status='new' · entregas.log · estado idempotente (último arquivo + chave).
2. **Produtor Tencent** `/home/ubuntu/dsn_coletores/dsn_coletor_nacional.py` (cron 15 6,7,8 + 45 23, flock): RSS Senado rss.xml ATIVO; Câmara/TCU/Planalto/STF/TSE/DOU marcadas pendentes (WAF/endpoint — sondagem 05/09); trafilatura p/ corpo; vistos.json (dedupe produtor); máx 25/entrega, 5/feed; --dry-run → staging; real → entregas/ + commit no repo (carimbo) + telemetria entregas_produtor.log.
3. **E2E provada** (5 itens reais do Senado na fila, commit eb6aea150) + idempotência 2 camadas. Rollback 1 alavanca no ROLLBACK_INDEX do NYC.

## Armadilhas (para futuras sessões)

- **"RSS" de órgão público costuma ser HTML ou WAF para datacenter** — sondar content-type + conteúdo real antes de listar como fonte (curl 200 ≠ RSS).
- **Senado: permalink no `<guid>`, sem `<link>`** no item.
- **urllib NÃO descomprime gzip** — curl --compressed sim.
- NYC sem credencial git (helper aponta p/ gh inexistente; repo privado) → transporte físico via scp tencent→nyc (as 2 direções funcionam).
- Adapter: contar inserções com cursor.rowcount, não por execução.
- Itens de teste na fila: limpar no mesmo ato (DELETE) — re-processamento forçado re-insere (o banco não lembra do DELETE).

## Estado

No ar. 1ª corrida automática: 06/09 06:15 BRT (hoje 05/09 as corridas da manhã já passaram; a sonda 23:45 de hoje é a 1ª). Observar a manhã de 06/09. Fase 1.5 (fontes via proxy/endpoints reais) aguarda Miguel.
