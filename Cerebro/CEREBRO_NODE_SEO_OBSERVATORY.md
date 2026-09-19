# CEREBRO_NODE_SEO_OBSERVATORY

**Função:** Registro canônico da arquitetura SEO autônoma do Cafezinho — Observador, Analisador e Otimizador. Rastreia indexação, Core Web Vitals, Search Analytics, Discover e ações corretivas automatizadas.

**Governança:** Ações destrutivas (compressão de imagem, reindexação) requerem §92. Modo dry-run é default; `--live` ativa execução real.

**Owner:** Kimi Code CLI (engenheiro executor) / Claude Maestro (supervisor §92)

> **📊 BASELINE GSC DA TAXONOMIA (15/08/2026):** `Foruns/forum_plano_seo_organizacao_categorias_tags_20260815.md` + `Memorias/memoria_baseline_gsc_taxonomia_20260815.md` — 90d via API: **só 4/298 categorias** (`/politica-2/` 951 cliques · `/politica-internacional/` 108 · `/economia/` 41 · `/pt/` 20) e **5/18.477 tags** (`/tag/brasil/` 53 c/ 20.742 impressões · `/tag/ira/` 44 · +3 residuais) têm tráfego orgânico = **9 URLs patrimônio intocável**; 294 categorias = 0 cliques. Plano de faxina de taxonomia com **pipeline prudente** `noindex→14d→merge≤500→redirect 301 antes→excluir→medir 7d` + monitoramento (baseline mensal dia 15 via `/tmp/gsc_baseline2.py`; alerta queda >15% semana pós-onda).

---

## 1. Arquitetura de 3 Agentes

| Agente | Arquivo | Cron | Função | Status |
|--------|---------|------|--------|--------|
| **Observador (Crawler)** | `cron_seo_crawler.py` | `0 3 * * *` | Ingestão: URL Inspection, PageSpeed, CrUX, Search Analytics | ✅ Operacional |
| **Analisador** | `seo_analyzer.py` | `15 3 * * *` | Detecção: desindexação, LCP, CLS, PSI, Discover | ✅ Operacional |
| **Otimizador** | `agente_optimizador_seo.py` | `30 3 * * * --live` | Ação: reindexação, compressão de imagem, relatórios | ✅ §92 ativado 2026-06-05 |
| **Diário Técnico** | `agente_diario_tecnico.py` | `0 8 * * *` | Boletim diário: SEO + Claude Monitor + Bugs + Auditoria Financeira, Telegram + cobrança | ✅ Ativo 2026-06-05 |
| **Auditoria Financeira** | `auditoria_financeira.py` | Importado pelo Diário | Módulo desconfiado: lê banco_custos, detecta anomalias, pede ground truth do cartão | ✅ Ativo 2026-06-05 |

**Servidor:** Tencent Cingapura (`43.156.151.165:38422`)
**Banco:** `/root/agent_data/seo_performance.db` (SQLite, 4 tabelas)
**Log de ações:** `/root/agent_data/seo_actions.json`
**Log de aprendizado:** `/root/agent_data/seo_learning.db`

---

## 2. Schema do Banco (`setup_db_seo.py`)

```sql
urls_monitoramento(id, url UNIQUE, categoria, data_criacao, status_ativo)
historico_indexacao(id, url, data_verificacao, indexada, ultimo_rastreio, erros_indexacao)
historico_performance(id, url, data_verificacao, lcp_val, inp_val, cls_val, crux_status, pagespeed_score, diagnosticos_json)
performance_palavras_chave(id, url, data_registro, query, cliques, impressoes, ctr, posicao, UNIQUE(url, data_registro, query))
```

**Alteração 2026-06-05:** `UNIQUE(url, data_registro, query)` adicionado para evitar duplicatas no Search Analytics.

---

## 3. Ingestão de Search Analytics — Correção 2026-06-05

**Problema:** Crawler registrava 0 palavras-chave.

**Causa raiz (3 fatores):**
1. `hours_back=72` no WordPress → banco só monitorava posts de ~3 dias
2. Search Analytics tem delay de 2–3 dias → API retornava dados de posts mais antigos
3. Filtro `if page_url in monitored_urls` → zero interseção temporal

**Correções aplicadas:**
- `hours_back=72` → `168` (7 dias)
- **Removido filtro `monitored_urls`** — agora registra todas as queries do site
- `UNIQUE` constraint no schema
- Deduplicadas 20.000 → 10.000 linhas limpas

**Resultado:** 10.000 keywords/dia inseridas; re-execução retorna 0 duplicatas.

---

## 4. Otimizador SEO v1.1 — Deploy 2026-06-05

### Bugs corrigidos

| Bug | Correção |
|---|---|
| `url=url` (tupla SQLite) | `url=row[0]` |
| `check_featured_image(self: int)` | `check_featured_image(self, post_id: int)` |
| `ensure_max_image_preview(self: int)` | `ensure_max_image_preview(self, post_id: int)` |
| `_handle_alert` passava URL direto | Resolve `post_id` via `_url_to_post_id()` |
| `action_outcomes` coluna `data_verificacao` | Alinhado para `timestamp` |
| Default sem flag = execução real | **Default = DRY-RUN**; `--live` obrigatório |

### Compressão de imagem (Pillow ativado)

**Lógica:**
- JPEG/PNG → WebP q=85% + redimensiona se >1920px
- WebP < 100KB → pula
- WebP > 100KB → recompressão WebP q=70%
- Redução < 5% → aborta

**Teste real:**
```
Post: lula-lanca-plataforma-tela-brasil...
Original: 1200x669 | 121KB | WebP
→ Comprimido: 121KB → 92KB (WebP q=70)
→ Nova media_id: 256489 | Post 256475 atualizado
```

### Meta tag `max-image-preview:large`

**Solução:** Code Snippets no WP admin
```php
add_action('wp_head', function() {
    if (is_singular('post') || is_singular('page')) {
        echo '<meta name="robots" content="max-image-preview:large">' . "\n";
    }
}, 1);
```

**Status:** ✅ Ativo no Cafezinho. Otimizador verifica HTML real e confirma presença.

---

## 5. Limiares e Alertas

| Métrica | Limiar | Severidade | Ação |
|---------|--------|------------|------|
| LCP | > 2.5s | CRITICAL (>5s) / WARNING | Verifica imagem + comprime |
| CLS | > 0.1 | WARNING | Reporta (theme/JS) |
| PSI | < 50 | WARNING | Reporta (theme/JS) |
| Desindexado | indexada=0 | CRITICAL | Reindexa via Google Indexing API |
| Discover queda | > 50% | CRITICAL | Alerta editorial |

**Max ações por execução:** 10 (proteção contra loop)

---

## 6. Google APIs — Configuração

| API | Método | Chave |
|-----|--------|-------|
| URL Inspection | Service Account | `agent_data/indexing_key.json` |
| Search Analytics | Service Account | `agent_data/indexing_key.json` |
| PageSpeed Insights | API Key | `GOOGLE_DEVELOPER_API_KEY` (env) |
| CrUX | API Key | `GOOGLE_DEVELOPER_API_KEY` (env) |
| Indexing API | Service Account | `indexador_google.py` |

**Service Account:** `indexing-cafezinho@gen-lang-client-0200069757.iam.gserviceaccount.com`
**Propriedade Search Console:** `sc-domain:ocafezinho.com`

---

## 7. Arquivos Sincronizados (Local ↔ Tencent)

```
Projeto Cafezinho Agentes/root/
├── agente_optimizador_seo.py   ← v1.1 (compressão real, verificação HTML)
├── cron_seo_crawler.py         ← sem filtro monitored_urls, 7 dias
├── seo_analyzer.py             ← detector de regressões
├── google_api_client.py        ← cliente compartilhado
├── setup_db_seo.py             ← schema com UNIQUE
├── adaptador_discover.py       ← helper Discover
└── crontab_tencent.txt         ← --live na linha do otimizador
```

**Espelho remoto (Tencent):** `/root/agente_optimizador_seo.py`, `/root/cron_seo_crawler.py`, `/root/seo_analyzer.py`, `/root/google_api_client.py`, `/root/setup_db_seo.py`

---

## 8. Rollback

### Otimizador para DRY-RUN
```bash
ssh -p 38422 ubuntu@43.156.151.165 'sudo crontab -l | sed "s/--live//g" | sudo crontab -'
```

### Remover meta tag
Desativar snippet `SEO Discover — max-image-preview:large` no Code Snippets do WP.

### Banco (schema antigo)
Restaurar `setup_db_seo.py` sem `UNIQUE` e recriar banco (perde dados).

---

## 9. Auditoria Financeira (Modo Desconfiado)

**Arquivo:** `auditoria_financeira.py`
**Integrado em:** `agente_diario_tecnico.py` §Financeiro
**Filosofia:** *"Os dados internos são hipótese. O cartão de crédito é prova."*

### O que faz
1. Lê `banco_custos_YYYY-MM.jsonl` (fonte canônica de custos LLM)
2. Calcula gastos últimas 24h, média 7 dias
3. Detecta anomalias:
   - Chamada individual > $0.10
   - Custo zero com tokens > 0 (erro de registro)
   - Custo real > 2x o esperado pela tabela de preços
   - Agente gastando > $5/dia
   - Dia atual > 2x média de 7 dias
4. Compara com **ground truth do cartão de crédito** (`ground_truth_cartao.json`)
5. Se discrepância > 15%, emite 🚨 e pede print da fatura

### Fontes de dados
| Fonte | Path | Formato | Função |
|-------|------|---------|--------|
| Banco de custos | `agent_data/banco_custos_YYYY-MM.jsonl` | JSONL append-only | Custo real por chamada LLM |
| Tabela de preços | `agent_data/precos_modelos.json` | JSON | Preços USD/1M tokens por modelo |
| API usage | `agent_data/governanca_financeira_api_usage.jsonl` | JSONL | Log detalhado por provider |
| Ground truth | `diario_tecnico/ground_truth_cartao.json` | JSON | Valor confirmado pelo usuário |

### Como registrar ground truth
O usuário deve enviar o valor real da fatura do cartão. O agente pede isso no Telegram:
```
👉 Miguel, envie o valor real da fatura (ex: /ground_truth 12.34)
```

Ou registrar manualmente:
```python
from auditoria_financeira import registrar_ground_truth
registrar_ground_truth(valor_usd=12.34, fonte="Print fatura Nubank 05/06", observacao="Valor confirmado pelo usuário")
```

### Limiares configuráveis
```python
LIMIAR_CUSTO_DIARIO_USD = 15.0    # Alerta se gasto diário > $15
LIMIAR_CUSTO_CHAMADA_USD = 0.10   # Alerta se 1 chamada > $0.10
LIMIAR_VARIACAO_DIA = 2.0         # Alerta se hoje for 2x média 7d
LIMIAR_AGENTE_DIARIO = 5.0        # Alerta se 1 agente gastar > $5/dia
```

---

## 10. Diário Técnico Cafezinho

**Arquivo:** `agente_diario_tecnico.py`
**Cron:** `0 8 * * *`
**Canais:**
  1. Telegram — mensagem com botão "✅ Li o Diário Técnico"
  2. Markdown — `/root/agent_data/diario_tecnico/boletim_diario_tecnico.md`
  3. Banco SQLite — rastreia confirmações de leitura

**Conteúdo:**
- SEO Observatory (ações, keywords, cliques)
- Relatório Claude Monitor (alertas, métricas)
- Bugs ativos (🔴 / 🟡)
- Dica do dia (quando não tem inovação)
- Cobrança: se não confirmar leitura em 3 dias, registra "não lido"

**Zero custo LLM:** Determinístico, frases predefinidas.

---

## 11. Pendências e Limitações

| # | Item | Status | Nota |
|---|------|--------|------|
| 1 | Compressão de imagem real | ✅ Funcionando | Pillow 12.1.1 instalado |
| 2 | Meta tag Discover | ✅ Ativa | Code Snippets |
| 3 | CrUX dados individuais | ⚠️ Sem dados | Normal para URLs novas |
| 4 | CLS alto / PSI baixo | ⚠️ Reporta apenas | Requer otimização de theme/JS |
| 5 | URLs `/amp/` no Search Analytics | ⚠️ Monitorar | Podem fragmentar métricas |
| 6 | Yoast/SEOPress API | ⏳ Pendente | Para injetar meta tag via API |

---

## 12. Tema novo — Cafezinho Multilíngue (versão EN, EM ESTUDO 27/07)

Ideia de Miguel: traduzir matérias (geopolítica, ciência, política BR) para inglês em `/en/` e abrir mercado internacional. Estudo completo (hreflang, geo-redirect = NÃO fazer, Indexing API é cega a idioma, spam policy mar/2024, casos El País/HuffPost/Le Monde, custos, matriz de riscos):

- **Fórum:** `Foruns/forum_cafezinho_site_multilingue_20260727.md`
- **Memória:** `Memorias/memoria_cafezinho_site_multilingue_20260727.md`

**Status:** pesquisa concluída, aguardando decisão de Miguel (piloto 60–90 dias). Se aprovado, o SEO Observatory ganha segmento `en` em `urls_monitoramento` — Search Analytics já ingere sem filtro (§3), Search Console `sc-domain` já cobre subdiretório.

---

## 13. Auditoria GA4+GSC+Vitals 30d (14/08/2026 — ZCode GLM-5.3)

Análise completa de audiência/performance Google: comparativos 7d×7d e 30d×30d até 13/08, padrões de conteúdo que geram audiência, CWV desktop/mobile e diagnóstico de bots. **Síntese:** web +27,6% cliques/30d com posição 4,55→3,35; Discover +755% (concentrado em 3 virais); CWV desktop 100% "Bom"; bots da China inflam GA4 em ~19% dos "usuários" (real ≈ +34%). Fórmula de audiência: título com verbo de ação (9× mais resultado) + 55–75 chars + 450–800 palavras; Economia = melhor score/post, Geopolítica = volume.

- **Fórum:** `Foruns/forum_cafezinho_analise_ga4_gsc_20260814.md`
- **Memória:** `Memorias/memoria_cafezinho_analise_ga4_gsc_20260814.md`
- **Relatório + dados brutos:** `Outros/google search/google search/analise_cafezinho_20260814/`

**Pendências para o Observador/Otimizador:** filtro GA4 anti-bot China (P1), cadência posts formato Discover (P2), otimização CTR queries broad "bolsa família"/"pix"/"dolar" (P3), TTFB ~1s (P4), CLS mobile 5.836 URLs (P5), redirects 404 (P6).

---

## 14. Análise profunda de posts — 3 semanas (15/08/2026 — ZCode GLM-5.3)

1.125 posts (25/07–15/08) ranqueados por audiência/leitura/cliques. **Lições:** título verbo+nome próprio = 9× chance de decolagem; sábado e horários 06h/09h/10h são os slots de ouro; Eleições (104–119 clk/post) e Regional/Ceará (50/post, 134s de leitura) são as eficiências; Ciência+IA+Tecnologia = 23% da produção p/ 7,6% dos cliques; tamanho de texto não gera alcance (r=0,06) e sim leitura (r=0,49); AMP = 64% das views; mediana de views/post = 25. Fórum+memória `*_cafezinho_analise_posts_3semanas_20260815`; relatório+JSONs em `Outros/google search/google search/analise_posts_3semanas_20260815/`.

**Node criado por:** Kimi Code CLI
**Data de criação:** 2026-06-05 03:20 BRT
**Última atualização:** 2026-08-14 23:50 BRT (seção 13 — auditoria GA4/GSC)
**Próxima revisão:** após 7 dias de operação LIVE ou quando houver mudança de schema
