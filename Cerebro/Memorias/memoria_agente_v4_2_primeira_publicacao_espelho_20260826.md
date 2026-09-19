---
tema: Agente V4.2 Economia/Estatística — desenvolvimento Módulos C/D/E + 1ª publicação no espelho cafezinho.news
data: 2026-08-26
agente: ZCode/Qwen 3.8
forum_irmao: Foruns/forum_agente_v4_2_economia_estatistica_20260825.md
---

# Memória — V4.2: primeira publicação no espelho cafezinho.news (26/08/2026)

## Missão (ordem do Miguel 26/08 ~12h)
Desenvolver Módulos C e D do V4.2, produzir imediatamente para o espelho cafezinho.news com bloco novo "Estatística" na home (igual ao Economia), categoria slug `estat`, selo de teste V4.2, desenho de comércio exterior (Beijing/China, Eurostat, FRED, Argentina/mundo), bancos no padrão V4.1, primeira postagem publicada e aviso no Telegram.

## Arquivos novos (todos em `Projeto Cafezinho Agentes/root/v4_labs/codigo/agente_economia/`)
- `env_loader.py` — carrega `.env.unificado` do cofre canônico sem sobrescrever e sem imprimir valores.
- `config_comercio_exterior.json` — países bilaterais ComexStat (China código **160** validado), séries INDEC vazias (código Argentina pendente), notas de unidade (metricFOB ÷1e6).
- `coletor_comercio_exterior_v4.py` — coletas isoladas try/except (Zero-Break): ComexStat (backoff progressivo `20s×tentativa`, máx 5, pausa 11s entre consultas), Eurostat (teiet010/110/210), FRED (USTRADE), GACC legado (CSV Beijing 50 meses), INDEC esqueleto. Envelopes → `raw/incoming`.
- `banco_producao_v4.py` — `BancoProducaoV42`, SQLite `banco_producao_v42.sqlite3`; tabelas materias / graficos_publicacao / fontes_usadas; idempotência por sha256 do JSON canônico {titulo, paragrafos}.
- `redator_economia_v4.py` — Módulo D completo: ConstrutorFactual (só números do banco, filtra datas futuras), TESES (comercio_sul_sul / politica_monetaria_comparada / inflacao_primaria), cascata DeepSeek→OpenAI(gpt-4o-mini)→Gemini, SYSTEM_PROMPT anti-alucinação, validadores `validar_texto_musica`/`validar_titulo` + reparos determinísticos, asserts fail-closed pós-reparo.
- `publicador_economia_v4.py` — Módulo E: REST espelho (ESPELHO_WP_*), garantir_categoria/tag, upload_midia, montar_html (lead + parágrafos + figuras após 2º § + selo + fontes), publicar/carimbar_checagem/alterar_status/readback.
- `ciclo_v42.py` — orquestrador CLI: [--coletar] redação → gráficos → auditoria → registro/publicação; recibo JSON em `gerados/ciclos/`; EN em `gerados/gsn/`.

## Descobertas técnicas importantes
1. **ComexStat metricFOB retorna US$ brutos** (não milhões) — conversão ÷1e6. Rate limit 429 agressivo; backoff 20s progressivo resolveu.
2. **Beijing (Tencent 82.156.167.218) segue OFFLINE** desde ~07/2026; CSV legado local (`Outros/beijing/dados_gacc/china_trade_monthly_complete.csv`, 2022-01→2026-02) ingerido com metadados `origem=beijing_legacy_csv`.
3. **gate-imagem fail-close do espelho** (mu-plugin `cafezinho-gate-imagem-checada.php`): `rest_pre_insert_post` valida meta JÁ PERSISTIDA — publish direto de post novo é impossível. Solução: 3 passos (draft → POST meta `_cafezinho_img_check` com ok+media_id casado → POST status=publish).
4. **meta não registrada é rejeitada no REST**: criado mu-plugin `cafezinho-v42-meta.php` no espelho registrando `v42_texto_sha256` (show_in_rest). Sync horário canônico→espelho é DB-only (não toca mu-plugins/tema) — edições persistem.
5. **Import do provider visual**: `media_vision_providers.py` usa import relativo (`from .vision_media`) → precisa ser importado como pacote: sys.path += `v4_labs/` e `from codigo.media_vision_providers import create_media_vision_provider`.
6. **AUTO_INCREMENT do espelho já está em 400000+** (posts/mídia) e termos em 100000+ — sem colisão com IDs do canônico (~267xxx) no sync REPLACE INTO.
7. Contrato Texto Música: "etc." NÃO pode estar na lista de abreviações protegidas do separador de frases (quebra a contagem).

## Provas da 1ª publicação (post 400137)
- Link: https://cafezinho.news/2026/08/26/v42-20260826-comercio_sul_sul/ (HTTP 200, título correto, 3 gráficos, selo, fontes)
- Readback REST context=edit: status=publish, categories=[100005], tags=[100006], featured_media=400134, `v42_texto_sha256` presente, `_cafezinho_img_check` com ok=true media_id=400134 audit=approved.
- Auditoria visual: 3/3 approved (COMEXSTAT/COMEX_EXPORT_CHINA line, GACC/GACC_CHINA_BALANCE bar, FRED/USTRADE line).
- Home: bloco Estatística entre Economia e Coluna do Editor com exatamente 1 matéria (prova por seção `<section>` + wp-cli `post list --category_name=estat` → só 400137).
- Mídias: 400134/400135/400136. Banco estatístico: 389 observações. Banco produção: matéria PT publicada + EN registrada.
- Telegram enviado ao Miguel ~12:38 via ponte_cafezinho (exit 0).
- Backup tema: `/var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/front-page.php.bak_pre_bloco_estatistica_20260826`.

## Comandos úteis
```bash
cd "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_labs/codigo/agente_economia"
python3 coletor_comercio_exterior_v4.py              # coleta comércio exterior
python3 coletor_economia_v4.py                       # coleta base (BCB/IBGE/FRED)
python3 ciclo_v42.py --tema comercio --publicar      # ciclo completo com publicação
python3 ciclo_v42.py --tema auto                     # dry-run local (sem publicar)
```

## Pendências
- Crons (§5 do fórum) ainda não instalados — aguardando decisão do Miguel.
- Código SISCOMES da Argentina para bilateral (150/639/0639 não funcionaram).
- Cesta Premium (interlinks + newsletter) não implementada no HTML — fase 2.
- Publicação EN no GSN (arquivo pronto em `gerados/gsn/`).
- Reativação do Beijing para GACC atual (dados param em 02/2026).

## 🐛 Incidente do "dezembro" (26/08 ~14h→15h) — log técnico

**Detecção:** reclamação do Miguel (~14h) — matéria citava "exportações para a China em dezembro" sem ano; número estava defasado (banco já tinha jul/2026).

**Diagnóstico:** `resumo_serie()` (redator_economia_v4.py) chamava `obter_serie_historica(fonte, serie_id, limite=24)`; essa função ordena `data_referencia ASC LIMIT N` → devolve os 24 mais ANTIGOS. Séries longas (COMEX 2024-08→2026-07, GACC CSV 50 meses) davam "último" = dez/2025 e dez/2023 respectivamente. Gráficos ileso (`load_series` ordena DESC).

**Fix:**
```python
serie = self.db.obter_serie_historica(fonte, serie_id, limite=1000)
serie = [s for s in serie if s["data_referencia"] <= hoje_utc]
serie.sort(key=lambda s: s["data_referencia"])
serie = serie[-limite:]   # janela recente de verdade
```
+ regra 7 no SYSTEM_PROMPT: período completo COM ano sempre; mês solto PROIBIDO.

**Provas (regressão):** COMEX_EXPORT_CHINA último=2026-07-01 valor=10673.11 · GACC_CHINA_BALANCE último=2026-02-01 valor=90.98 · USTRADE último=2026-07-01.

**Correção da matéria (in place, §119):**
- `publicador.alterar_status` NÃO usado — update direto via PUT em `posts/400137` com novo title/content (mesma URL/slug, status publish mantido).
- Redação: tentativa 1 DeepSeek REPROVOU (parágrafo com 1 frase — contrato Texto Música); tentativa 2 OpenAI gpt-4o-mini APROVADA.
- Banco produção: matéria PT id=4 (metadados `correcao_26_08`), EN id=5, `fontes_usadas` substituídas.
- GSN: `gerados/gsn/gsn_comercio_sul_sul_<ts>_CORRIGIDA.json` novo; 2 defasados → `gerados/gsn/descartados/`.
- Readback final: publish | menções a mês SEM ano: nenhuma | trecho inicial: "As exportações brasileiras para a China atingiram US$ 10.673 milhões em julho de 2026."

**Arquivos tocados:** `redator_economia_v4.py` (fix+regra 7) · post 400137 no espelho · `banco_producao_v42.sqlite3` · `gerados/gsn/`.
