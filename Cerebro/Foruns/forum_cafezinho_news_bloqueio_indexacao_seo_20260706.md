# Fórum — Bloqueio anti-indexação do espelho `cafezinho.news` (Opção B)

> **Criado:** 2026-07-06 ~11:50 BRT por **Claude Code** (`claude-opus-4-7`)
> **Pedido do Miguel:** "esse site espelho pode atrapalhar meu desempenho no Google? acha melhor deixar ele fechado por enquanto? ele está sendo indexado?"
> **Status:** ✅ **Aplicado — cafezinho.news bloqueado pra indexação sem quebrar acesso humano**
> **Complementa (não colide):** [`forum_bug_duplicate_content_www_vs_semwww_20260706.md`](forum_bug_duplicate_content_www_vs_semwww_20260706.md) do GLM (Ming), que trata do duplicate content sem-www vs com-www no **canônico** (`us65.serverdo.in`). Este fórum trata do **espelho** (`cafezinho.news` @ droplet DO NYC3 `159.65.177.60`). Problemas independentes.

---

## 1. TL;DR

O espelho diletante `cafezinho.news` (droplet DigitalOcean NYC3, `159.65.177.60`) **estava servindo 4.658 URLs indexáveis** pro Googlebot: sitemap XML ativo, canonical apontando pro próprio, sem `robots.txt`, sem `X-Robots-Tag`. Como o conteúdo é 100% cópia do canônico `ocafezinho.com`, seria canibalização SEO clássica se ficasse assim.

**Ação:** aplicada Opção B do audit — bloqueio de indexação preservando acesso humano.

- ✅ `robots.txt` com `User-agent: * / Disallow: /`
- ✅ Header HTTP `X-Robots-Tag: noindex, nofollow, noarchive` em toda resposta
- ✅ Todos os sitemaps (`sitemap_index.xml`, `post-sitemap*.xml`, `category-sitemap.xml`, `post_tag-sitemap.xml`, `page-sitemap.xml`) retornam **HTTP 404**
- ✅ Homepage e posts continuam **HTTP 200** pra humanos (Miguel continua acessando pelo browser)

---

## 2. Contexto — por que agora

- Espelho criado 29/06/2026 como **exercício diletante** (recorte 30 dias do Cafezinho canônico). Ver `forum_exercicio_copia_cafezinho_news_20260629.md` em `Projeto Cafezinho Agentes/Foruns/`.
- Sync horário `cafezinho.news ← ocafezinho.com` está ATIVO desde 03/07 (script `/root/sync_from_cafezinho.sh` no droplet, cron `17 * * * *`). Refletiu ~3.383 posts com URLs internas reescritas pra `cafezinho.news`. Ver `project_cafezinho_news_sync_horario_20260703.md` na auto-memória.
- **Nunca foi configurado bloqueio SEO** — o setup inicial focou em fazer o WordPress subir e o SSL funcionar.
- Miguel perguntou 06/07 se poderia atrapalhar o desempenho no Google → audit → **sim, canibalização em potencial**.

---

## 3. Diagnóstico técnico do estado ANTES

| Item | Estado ANTES | Risco |
|---|---|---|
| `robots.txt` | HTTP 404 (não existia) | 🔴 Googlebot livre |
| `<meta name="robots">` | AUSENTE (sem `noindex`) | 🔴 |
| Header `X-Robots-Tag` | AUSENTE | 🔴 |
| `<link rel="canonical">` | Apontava pro **próprio** `cafezinho.news` | 🔴 pior cenário (Google trata como original) |
| `<meta og:url>` | Apontava pro próprio `cafezinho.news` | 🔴 |
| `sitemap_index.xml` (Yoast) | HTTP 200 — ativo e atualizado hoje 14:13 UTC | 🔴 |
| Sub-sitemaps | 4.658 URLs total (3.383 posts + 268 categorias + 1000 tags + 7 páginas) | 🔴 |
| Tema ativo | `ocafezinho-portal` (mesmo do canônico, com plugin Yoast SEO) | (contexto) |

**Buscas `site:cafezinho.news` em Google/Bing/DuckDuckGo** retornaram vazio no parsing curl (User-Agents comuns) — sinal fraco, provavelmente ainda não indexado ou muito pouco (domínio tem ~1 semana). Sem confirmação 100% porque cafezinho.news não está no Google Search Console (mesmo service account `indexing-cafezinho@gen-lang-client-0200069757...` que já tem Owner de `sc-domain:ocafezinho.com` pode ser reaproveitado pra adicionar cafezinho.news como nova propriedade se Miguel quiser confirmação retroativa).

**Verificado que o problema é diferente do fórum do GLM sobre `www` vs sem-www no canônico:**
- GLM: duplicate content **dentro** do canônico (2 URLs mesma origem)
- Este: duplicate content **entre** o canônico e o espelho (2 domínios diferentes servindo mesmo conteúdo)

---

## 4. Ação aplicada — Opção B

### 4.1 Arquivos no droplet `159.65.177.60`

- **Backup do vhost:** `/etc/nginx/sites-available/cafezinho-news.bak_pre_noindex_20260706`
- **`/var/www/cafezinho-news/robots.txt`** (novo, owner `www-data:www-data`):
  ```
  # Este site é um espelho diletante do https://www.ocafezinho.com/
  # Não indexar em nenhum motor de busca.
  User-agent: *
  Disallow: /

  Sitemap:
  ```
- **`/etc/nginx/sites-available/cafezinho-news`** — patch dentro do bloco `server { listen 443 ssl }`, logo após `client_max_body_size 64M;`:
  ```nginx
  # 20260706 Claude/Miguel: bloqueio anti-indexação (Opção B do audit SEO)
  add_header X-Robots-Tag "noindex, nofollow, noarchive" always;

  # Bloquear sitemaps do Yoast — geram dinamicamente via WP rewrite, precisa location match antes do try_files
  location ~ ^/(sitemap[^/]*|.*-sitemap[0-9]*)\.xml$ {
      return 404;
      access_log off;
      log_not_found off;
  }
  ```
- **Reload:** `nginx -t` OK → `systemctl reload nginx` sem downtime.

### 4.2 Smoke test 100% verde

| Verificação | Resultado |
|---|---|
| `curl https://cafezinho.news/robots.txt` | `Disallow: /` |
| `curl -I https://cafezinho.news/` | `HTTP 200 + X-Robots-Tag: noindex, nofollow, noarchive` |
| `curl -I https://cafezinho.news/sitemap_index.xml` | HTTP 404 ✅ |
| `curl -I https://cafezinho.news/post-sitemap.xml` | HTTP 404 ✅ |
| `curl -I https://cafezinho.news/category-sitemap.xml` | HTTP 404 ✅ |
| Homepage pra humano | HTTP 200 em ~210ms ✅ |
| `nginx -t` | syntax OK ✅ |

---

## 5. Efeito esperado no Google

- **URLs ainda não indexadas** (majoritário): Googlebot lê `robots.txt` no próximo crawl (24-72h) e **nem começa** a indexar novas URLs.
- **URLs que porventura foram indexadas** (minoritário — domínio tem ~1 semana, provavelmente pouco ou nada): `X-Robots-Tag: noindex` faz Google **desindexar gradualmente** em 2-8 semanas conforme rerastrear cada URL.
- **`noarchive`** também instrui Google a não guardar snapshot cache das páginas.
- **`nofollow`** impede que autoridade seja passada por links internos do espelho — reforço extra.

---

## 6. Como reverter (rollback trivial)

```bash
ssh root@159.65.177.60 '\
  cp /etc/nginx/sites-available/cafezinho-news.bak_pre_noindex_20260706 /etc/nginx/sites-available/cafezinho-news && \
  rm /var/www/cafezinho-news/robots.txt && \
  nginx -t && systemctl reload nginx'
```

---

## 7. Opções que ficaram sobre a mesa (NÃO aplicadas)

| | O que faria | Por que NÃO |
|---|---|---|
| **A) Fechar TOTAL (nginx 503 pra tudo)** | Bloquearia Googlebot + humanos + IA | Miguel quer continuar acessando pra ver como está o espelho |
| **C) Fazer canonical apontar pro original via Yoast** | Configurar Yoast SEO no espelho pra reescrever `<link rel="canonical">` → `www.ocafezinho.com` | Mais elegante (Google entende que é cópia e credita o original) mas exige mexer no admin do WordPress e ter cuidado pra não afetar o próprio Yoast do canônico (mesmo tema, mesma config). Fica como upgrade futuro se Miguel quiser. |

---

## 8. Pendências / próximos passos opcionais

1. **[Opcional] Cadastrar `cafezinho.news` no Google Search Console** com o mesmo service account `indexing-cafezinho@gen-lang-client-0200069757...` (Owner atual de `sc-domain:ocafezinho.com` e outros) → permite acompanhar o "Excluído por noindex" ir subindo e confirmar retroativamente se havia URLs indexadas.

2. **[Opcional] Se um dia decidir "fechar total"** (Opção A do audit) — 1 linha no vhost:
   ```nginx
   return 503;
   ```

3. **[Não urgente] Se decidir manter o espelho e quiser fluxo canonical→original** (Opção C) — configurar Yoast SEO no admin do espelho pra sobrescrever canonical apontando pro `www.ocafezinho.com`. Ganho: passa autoridade acumulada de eventual indexação de volta pro original.

---

## 9. Relações com outras memórias / fóruns

- [`forum_bug_duplicate_content_www_vs_semwww_20260706.md`](forum_bug_duplicate_content_www_vs_semwww_20260706.md) — GLM/Ming trabalhando em paralelo no problema análogo dentro do canônico (não colide, escopos separados)
- `Projeto Cafezinho Agentes/Foruns/forum_exercicio_copia_cafezinho_news_20260629.md` — fórum canônico do exercício cafezinho.news (setup inicial, sync horário, patches)
- Auto-memória `project_cafezinho_news_sync_horario_20260703.md` — sync horário ativo desde 03/07
- Auto-memória `feedback_cafezinho_news_e_copia_nao_migracao.md` — regra semântica ("cópia diletante", nunca "migração")
- Auto-memória `project_seo_pruning_automatizado_20260701.md` — sistema SEO pruning do canônico (mu-plugin no ServerDo.in). Este bloqueio de indexação é conceitualmente similar (`noindex` via header) mas separado.

---

## 10. Estado atual — snapshot 2026-07-06 ~11:52 BRT

- **Cafezinho canônico (`www.ocafezinho.com` em `us65.serverdo.in`):** intocado, HTTP 200, publicação normal, servindo tráfego SEO real
- **Espelho (`cafezinho.news` em droplet DO NYC3 `159.65.177.60`):** HTTP 200 pra humano + `noindex` pra bot. Sync horário ativo (cutoff `2026-07-05 05:01:00` até próximo `17 * * * *` fechar o gap de ~26h que gerou por causa do desligamento do droplet 05-06/07).
- **Master de agentes NYC (`198.199.121.136`):** de volta ativo (foi religado 06/07 ~10:53 UTC após pagamento DO). 42 crons + bots Telegram Augusto/Mayra/Zizi rodando.

---

*Fórum aberto por Claude Code em 2026-07-06 ~11:52 BRT. Sinta-se livre pra registrar 2ª opinião, comentários ou próximos passos abaixo.*
