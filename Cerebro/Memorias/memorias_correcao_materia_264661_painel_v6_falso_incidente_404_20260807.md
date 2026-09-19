# Memória — Correção matéria 264661 + Painel CCTV V6 (links/acentuação) + Falso incidente "site todo 404"

**Data:** 2026-08-07 (~11:30 → 16:00 BRT) · **Agente:** ZCode/Qwen 3.8 · **Fórum par:** `Foruns/forum_correcao_materia_264661_painel_v6_falso_incidente_404_20260807.md`
**Autorização Miguel:** mensagem 15 (voz, 07/08) — "tem que corrigir urgente" (título) + reclamação do painel CCTV ("link controle", "quebrando a acentuação").

---

## 1. Correção do título — WP post 264661 ✅

- Matéria das 11h: título gerado veio truncado ("Irã desdenha diplomacia de Trump teatro em loop rejeita ameaça").
- Correção via REST: `POST https://controle.ocafezinho.com/wp-json/wp/v2/posts/264661` (HTTP basic c/ application password; credenciais lidas do script `scratch/atualizar_materia_milei_wp.py` — **valores nunca copiados pra registro nenhum**).
- Resultado: HTTP 200; título novo **"Irã desdenha da diplomacia de Trump"**; slug mantido `ira-desdenha-diplomacia-de-trump-teatro-em-loop-e-rejeita-ameacas`; status publish.
- "Relida" pedida pelo Miguel: conteúdo íntegro — 4 parágrafos fechados (fonte Sputnik, falas de Ghalibaf), termina em "...crescente pressão em torno do Estreito de Ormuz." + marcador `<!-- CONTENT END 1 -->`. A impressão de truncamento vinha do título mal gerado + duplo-escape no painel (item 2).
- ⚠️ Erro de processo nesta sessão: um `grep` no script de credenciais imprimiu o valor da application password no transcript uma vez. Não há como des-imprimir; mitigação: nunca mais exibir, reutilizar só por parsing silencioso do arquivo.

## 2. Painel CCTV V6 — página "publicações" ✅ (deploy em produção, Tencent)

Dois bugs, um patch (função `wp_posts()`, `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`, serviço `cctv-v6` porta 8084, nginx `location /v6/`):

1. **"Acentuação quebrada"** = entidades HTML duplamente escapadas (`&amp;#8220;`): o painel aplicava `html.escape()` sobre strings REST `rendered` que ainda continham entidades. Fix: `html.unescape()` na ingestão (antes do escape de renderização). Truncamento do resumo (340 chars) movido para DEPOIS do unescape (não corta entidade no meio).
2. **"Link controle"** = WP devolve o campo `link` com o domínio da requisição; o painel consulta o endpoint `controle.ocafezinho.com` → links vinham `controle.*`. Fix: normalização `controle.ocafezinho.com → www.ocafezinho.com` em `link` e `thumb`.

Deploy: backup `painel_cctv_v6.py.bak_links_<ts>` no servidor → `py_compile` ok → `install -o ubuntu -g ubuntu -m 664` → cache `agent_data/cctv/v6/wp_posts.json` apagado → `systemctl restart cctv-v6` → **verificado ao vivo**: 0 entidades cruas, 0 hrefs controle, 20 hrefs www, card do Irã com título novo + link público + imagem pública.

## 3. Falso incidente "site todo 404" — NÃO EXISTIU ⚠️ (errata importante)

Ao verificar a correção, esta sessão (e a anterior, pré-resumo) concluiu erroneamente que TODOS os permalinks do www.ocafezinho.com davam 404. **Diagnóstico final: o site nunca caiu; os testes usavam URL em formato inexistente.**

### O que realmente aconteceu
- Formato real de permalink do site: `/%year%/%monthnum%/%day%/%postname%/` → `https://www.ocafezinho.com/2026-08-07/slug/` (confirmado byte a byte: estrutura no DB, link canônico REST, cache WP Rocket de 02/07 com hrefs `/2018-07-09/...`).
- Os testes desta sessão usaram repetidamente `.../2026-08-07/slug/` (data com hífens, um segmento só) — URL que não existe no site → WP cai na regra catch-all de página → 404 (comportamento correto).
- O erro nasceu na sessão anterior (URL malformada carregada no resumo de contexto) e se auto-reforçou: cada teste com formato errado "confirmava" o incidente.
- **Prova de que o site estava saudável o tempo todo:** access log com 22.852×200 em `/2026/...` hoje, incluindo a própria matéria do Irã com 200 às 13:13; `?p=264661` 200; homepage 200; artigo antigo (31/07) 200 na URL correta.

### O que foi verificado na investigação (estado real do WP — tudo íntegro)
- `permalink_structure` intacta (slashes); `rewrite_rules` 169.199 bytes, 1743 regras, **ordem correta** (regra de data pos 1719, antes da catch-all de página pos 1742 — verificado no DB E no contexto web via mu-plugin de debug temporário).
- Redis object cache (193k chaves, maxmemory 256MB, 2,78M evictions — cache sob pressão crônica, notar p/ futuro): `rewrite_rules` não estava em Redis (web lia do DB, correto).
- `wp rewrite flush` executado durante o falso incidente: regenerou regras IDÊNTICAS (mesmo tamanho) — sem dano. `redis-cli DEL wp:options:notoptions` + purge do cache WP Rocket: inócuos (reconstroem sozinhos).
- Plugins de nota: 43 ativos, incluindo AMPforWP (`ampforwp_rewrite_flush_option=true`), GTranslate, Yoast, EverMonitor; mu-plugins `cafezinho-*` (SEO pruning c/ token no wp-config, purge-on-manchete, force-rest-url-controle etc.) — nenhum mexe em rewrite_rules.
- Posts `admin-post.php` periódicos via loopback (UA `WordPress/7.0.3`) às 11:08/11:42/11:52/11:59/12:03 — não correlacionados a mudança de permalink (nenhum acesso a `options-permalink.php` ou REST settings hoje).

### Observações laterais (pré-existentes, sem ação)
- Arquivos de data de MÊS/DIA 404 (`/2026-08/`, `/2011-10/`) enquanto ANO 200 (`/2026/`, `/2011/`) — comportamento antigo do site (afeta 2011!), Yoast `disable-date=0`; provavelmente outro plugin/mu-plugin desativa. Não é defeito novo.
- 404s de ruído no log: probes `/amp/`, `mraid.js`, `robots.txt` sob post, `target=`, post com data futura `/2026-08-08/...`.
- wp-cli neste site cospe lixo de um snippet eval'd no bootstrap (função de paginação + notice HTTP_HOST) — filtrar sempre com `| tail -1` ou usar `wp db query`.

## 4. Lições (registrar no vivo do monitor)

1. **Antes de declarar incidente em URL, provar os bytes da URL testada** (`echo "$URL" | od -c`) e comparar com o link canônico real (REST `link` / cache antigo saudável).
2. Erro herdado de resumo de contexto NÃO é fato — re-verificar premissas-chave (a URL do "próximo passo" do resumo já veio errada).
3. "Funciona via `?p=` mas não via permalink" tem causas reais (ordem de regras, cache) — mas primeiro excluir o óbvio: a URL testada existe?
4. Mudança em produção durante diagnóstico (flush/purge) só porque era inócua e reversível; anotar cada uma.

## 5. Estado da missão

- **Aconteceu:** título 264661 corrigido e no ar (200, título certo); painel V6 corrigido e verificado ao vivo; falso incidente desfeito com provas; Cérebro atualizado.
- **Falta:** nada para este pedido do Miguel. (Arquivos de mês/dia 404 = observação, se ele quiser investigar um dia.)
- **Preciso do Miguel:** confirmação visual do título no ar + da página "publicações" do painel (link público, acentos ok).
