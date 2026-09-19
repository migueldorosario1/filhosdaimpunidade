# MANIFESTO — Reforma Visual Cafezinho · Deploy canônico PASSO 1 (Histórico)

**Autor:** ZCode · **Data:** 2026-07-27 ~09h00 BRT · **Autorizador:** Miguel
**Conforme:** Dez Mandamentos de Segurança para Agentes, §9 (manifesto próprio com arquivos, decisões, testes, riscos, backup e rollback)
**Fórum guarda-chuva:** `Foruns/forum_reforma_visual_cafezinho_20260727.md`
**Fórum do deploy:** `Foruns/forum_deploy_canonico_tablet_historico_20260727.md`
**Memória técnica:** `Memorias/memoria_deploy_canonico_tablet_historico_20260727.md`

## Escopo

Portar ao canônico `ocafezinho.com` a primeira de 4 mudanças homologadas no espelho: o link **"Histórico"** vermelho no fim do bloco Recentes da capa, abrindo painel com o arquivo do site por ano/mês. Passos 2–4 (Colunas, menu sanfona, resumo da manchete) **não** fazem parte deste manifesto e aguardam OK de Miguel.

## Arquivos

**Criados no canônico (us65.serverdo.in, `/var/www/ocafezinho/wp-content/mu-plugins/`) — nenhum arquivo existente foi tocado:**

| Arquivo | Bytes | Função |
|---|---:|---|
| `cafezinho-historico.php` | 3.588 | loader (enqueue só `is_front_page()`), painel no `wp_footer`, transient 1h + invalidação |
| `cafezinho-historico.css` | 2.271 | estilos `.cz-hist*` (var(--red) do tema) |
| `cafezinho-historico.js` | 2.621 | move painel pro fim da seção Recentes + toggles ano/mês |

**Criados no canônico (fora do webroot):**
- `/root/rollback_canonico_20260727/PLANO_E_ROLLBACK.md` — plano dos 4 passos + rollback + log
- `/root/rollback_canonico_20260727/baseline_capa_antes.html.gz` — capa pré-deploy (284.962 bytes)
- `/root/rollback_canonico_20260727/purge_rocket.php` — script de purge (rodar de /tmp)

**Criados/editados no Cérebro local:**
- `Foruns/forum_reforma_visual_cafezinho_20260727.md` (novo, guarda-chuva)
- `Foruns/forum_deploy_canonico_tablet_historico_20260727.md` (novo)
- `Foruns/MANIFESTO_REFORMA_VISUAL_CAFEZINHO_20260727.md` (este arquivo)
- `Memorias/memoria_deploy_canonico_tablet_historico_20260727.md` (novo)
- `Foruns/forum_lab_visual_cafezinho_news_20260720.md` (editado: changelog V1.3 + semente de posts)
- `Foruns/INDICE_FORUNS_SEMANAL.md`, `CEREBRO_NODE_SPRINTS_ATIVOS.md`, `CEREBRO_NODE_COFRE_CHAVES.md`, `CEREBRO_NODE_ATUALIZACOES.md` (indexação)

**Editados no espelho (trabalho prévio de homologação, 27/07):**
- `wp-content/mu-plugins/cafezinho-lab-visual.php/.css` (V1.3) + `.js` (novo); versões em `/root/lab_visual_versoes/`
- `wp option show_on_front = page` (correção de ambiente)
- 171 posts reais semeados (1/mês 2011–2025, IDs originais, zero colisão)

## Decisões

1. **100% aditivo** — tema e mu-plugins existentes intocados; rollback = apagar 3 arquivos + purge.
2. **Módulo independente** (`cafezinho-historico.*`) em vez de estender o lab-visual — o canônico não tem as V1.0–V1.2 do lab e cada feature vira um módulo com rollback próprio.
3. **Transient de 1h** no canônico (GROUP BY em ~70k posts não pode rodar por view); espelho ficou sem (escala pequena).
4. **Ordem dos passos definida por Miguel:** Histórico → Colunas → menu sanfona → resumo da manchete.
5. Purge de cache via `rocket_clean_domain()` (CLI `wp rocket` inexistente nesta instalação).

## Testes (todos executados, resultados reais)

| Teste | Resultado |
|---|---|
| `php -l` no mu-plugin | sem erros de sintaxe |
| Capa pós-deploy | HTTP 200; 284.962 → 318.145 bytes (+33KB do painel) |
| Painel | 16 anos (2011–2026), 179 links mensais, soma 2023 = 10.656 = valor do banco ✓ |
| Regressão | 21 cards colunistas, 37 anteriores, manchete — todos intactos |
| Smokes | CSS 200, JS 200, `/2019/05/` 200, post 200 |
| Cache | purge Rocket OK (87→2 entradas, regenera), object cache flushed |

## Riscos e mitigações

| Risco | Mitigação aplicada |
|---|---|
| HTML velho em cache esconder o painel | purge obrigatório + validação curl |
| Carga do GROUP BY na capa | transient 1h com invalidação em save_post |
| JS não localizar a seção Recentes | seletores confirmados no baseline + fallback; pior caso: painel no footer |
| Erro PHP derrubar o site | `php -l` prévio; mu-plugin sem dependências |
| www-data não ler script em /root | purge roda de /tmp (documentado no plano) |

## Backup

- Baseline da capa: `/root/rollback_canonico_20260727/baseline_capa_antes.html.gz`
- Como nenhum arquivo existente foi editado, não há outros backups neste passo. Backups versionados serão obrigatórios nos passos 3–4 (que editam o CSS criado no passo 2).
- UpdraftPlus ativo no canônico como rede adicional (não disparado — escopo cirúrgico coberto).

## Rollback (completo, testado mentalmente passo a passo)

```bash
ssh cafezinho-wp
rm /var/www/ocafezinho/wp-content/mu-plugins/cafezinho-historico.{php,css,js}
cp /root/rollback_canonico_20260727/purge_rocket.php /tmp/ && chmod 644 /tmp/purge_rocket.php
sudo -u www-data wp --path=/var/www/ocafezinho eval-file /tmp/purge_rocket.php
sudo -u www-data wp --path=/var/www/ocafezinho cache flush
# verificar: curl -s https://www.ocafezinho.com/ | grep -c cafezinho-historico  → deve dar 0
```

## Pendências

- OK visual de Miguel no canônico → libera PASSO 2 (Colunas só última no tablet).
- Dívida ativa registrada: rotação da senha root do ServerDo.in (desde 28/06).
- Dívida técnica nova: ruído `wp_bs_pagination` no stdout do wp-cli (os dois servidores) — investigar include do tema sem `<?php`.

— ZCode, 2026-07-27
