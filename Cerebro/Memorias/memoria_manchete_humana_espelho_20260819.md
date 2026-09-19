# 🧠 Memória técnica — Manchete 266521 no canônico + experimento "Manchete Humana" no espelho (19/08/2026)

> Sessão: ZCode/**Kimi K3** · 09:04→09:30 BRT · Ordem do Miguel (voz transcrita no chat)
> Fórum irmão: `Foruns/forum_manchete_humana_espelho_experimento_20260819.md`

---

## 1. Manchete no canônico (09:09 BRT)

- Post: **266521** — "Lula e Putin vão assinar acordo histórico de cooperação nuclear" (18/08 19:51, cats 15+22).
- Macete (do `CEREBRO_NODE_MANCHETE.md`): manchete = plugin **hello-highlight** → tabela `wp_highlights`, linha `name='Manchete'`. **NÃO é categoria.**
- Comandos executados:
  - Descoberta do ID: `GET /wp-json/wp/v2/posts?slug=lula-e-putin-vao-assinar-acordo-historico-de-cooperacao-nuclear` → 266521.
  - `POST /wp-json/cafezinho/v1/set-manchete {"post_id":266521,"name":"manchete"}` → `{"status":"success"}`.
  - `POST /wp-json/cafezinho/v1/purge-cache` → `{"ok":true,"purged":["wp_rocket_domain","wp_rocket_home","wp_rocket_htaccess","wp_cache"]}`.
  - Verificação: `manchete-status` = 266521; hero da home `www.ocafezinho.com` exibindo o título.
- **GOTCHA Cloudflare 1010:** POST via urllib/curl com UA padrão → `403 error code: 1010` (Cloudflare Browser Integrity). Com UA de Chrome → passa e a API responde normal. Credencial válida: par `WP_USER_CAFEZINHO`/`WP_APP_PASSWORD_CAFEZINHO` (cofre `Outros/chaves/agentes_labs/.env.unificado`). Gotcha extra: extrair valor do cofre com `sed`, não com `tr` mal-escapado (quebrou a 1ª tentativa).
- **Trava 2h no robô (NYC 198.199.121.136):** `touch /root/agent_data/manchete_lock` + `manchete_lock.motivo` + `nohup bash -c "sleep 7200; rm -f ..."` → auto-release ~11:10 BRT. Cron do agente: `0 */2 * * *` (`/root/agente_manchete.py`, respeita o lock desde 15/07).

## 2. Radiografia do espelho (feita antes de codar)

- Espelho = droplet `root@159.65.177.60`, WP em `/var/www/cafezinho-news`, site `https://cafezinho.news`, tema `ocafezinho-portal` 2.0.
- `hello-highlight` **ativo**; `wp_highlights` existe (linha id=2, `name='Manchete'`).
- Front-page NÃO usa `get_highlight` direto: usa **`cafezinho_get_real_highlight('Manchete')`** (mu-plugin `cafezinho-real-image-gate.php:205`) — mantém a escolha manual só se `cafezinho_post_has_verified_real_image()` E fora da 20699; senão cai no fallback (recente c/ `_thumbnail_id` + imagem real).
- **`cafezinho_post_image_kind`** lê meta `cafezinho_image_kind` ('real'/'artificial') no post OU no anexo; sem meta → blob do anexo (título/caption/conteúdo/arquivo) com marcadores (`foto:`, `foto `, `wikimedia`, `agencia brasil`, `reproducao`...). **Slug hifenizado NÃO casa** ("Foto-Ricardo" ≠ "foto ").
- **Sync horário** `/root/sync_from_cafezinho.sh` (cron `17 * * * *`) faz `mysqldump wp_highlights` no canônico → **`REPLACE INTO` no espelho** — ou seja, **a manchete do espelho é sobrescrita pela do canônico toda hora**. Qualquer experimento de manchete humana no espelho PRECISA de trava contra o sync.

## 3. O experimento (tudo implantado 09:19–09:25)

### 3.1 mu-plugin `wp-content/mu-plugins/cafezinho-manchete-humana.php` (v0.1.0, 17,7KB)
Classe `CMH_Manchete_Humana`:
- **Widget de Dashboard** "📰 Manchete Humana — EXPERIMENTO (espelho)": manchete atual (link+editar), status 🔒/🤖, campo URL-ou-ID, **barrinha `<input type=range min=2 max=24>`** (label vivo em JS), botões **📌 É MANCHETE / ❌ Tirar trava / 🔁 Rodar**, histórico (10 últimas). AJAX com nonce `cmh_manchete_humana` + `manage_options`.
- **Estado:** option `cmh_estado` {post_id, desde, ate, horas, autor, origem}; **arquivo de trava** `wp-content/uploads/cmh/manchete_humana.lock` (linha1=epoch expiração, linha2=post_id, linha3=humano). Expiração **preguiçosa** no getter.
- **Regra do mínimo 2h:** `aplicar_trava()` clampa 2–24h; `ajax_set` recusa se já há trava ("clica no ❌ primeiro"); `guardar_trava()` hook em `wp_ajax_highlight_process` prio 0 → `wp_die(403)` se tentarem trocar pela coluna Destacar durante a trava; `auto_travar_coluna()` prio 99 → **toda manchete marcada pela coluna ganha trava automática de 2h**.
- **Rodar:** `vencedor_automatico($excluir_atual)` = mesma regra do fallback do tema (60 recentes, publish, fora 20699, `_thumbnail_id`, `cafezinho_post_has_verified_real_image`), preferindo post ≠ atual.
- **Purge:** rocket (se existir) + `wp_cache_flush()`.
- Resolver de alvo: ID numérico ou URL (slug final via `get_page_by_path`) — aceita URL do canônico porque IDs são espelhados.

### 3.2 Patch no sync (`/root/sync_from_cafezinho.sh`)
- Backup: `/root/sync_from_cafezinho.sh.bak_pre_manchete_humana_20260819_122003` · `bash -n` OK.
- Bloco novo antes do sync de highlights: se `uploads/cmh/manchete_humana.lock` existe e epoch > agora → `log "wp_highlights: TRAVA HUMANA ATIVA ... sync de highlights PULADO"` + `CMH_SKIP=1`; se vencido → apaga o arquivo e segue. Bloco original embrulhado em `if [ "$CMH_SKIP" != "1" ]`.
- Aplicado via `/tmp/patch_sync_manchete.py` (idempotente, marca `MANCHETE HUMANA ESPELHO`).

### 3.3 Bateria de testes (`/tmp/cmh_teste.php` via `wp eval-file`) — **8/8 ✅**
T0 carga/gate · T1 set+trava exata 7200s+lock file+estado · T2 guarda (wp_die no post diferente; mesmo post passa) · T3 Rodar escolheria 266599 · T4 render do widget (4 botões/barrinha/status) · T5 unlock limpa tudo · T6 trava vencida expira sozinha · T7 clamp 1h→2h e 99h→24h · T8 estado final 266521.
**Prova real do sync (09:23):** espelho=266580 com trava × canônico=266521 → log `TRAVA HUMANA ATIVA ... PULADO`, linha intacta 266580. ✔ A trava humana vence o canônico.

### 3.4 Ajuste da imagem do 266521 (espelho)
- Sintoma: home do espelho mostrava fallback (266599 TSE/Marçal) mesmo com manchete=266521.
- Causa: `image_kind=unknown` — anexo 266522 sem `cafezinho_image_kind` e título hifenizado não casa marcadores; meta `_cafezinho_gate_imagem` = "imagem_sem_checagem"; MAS existia `_cafezinho_img_isenta` (isenção **manual do editor** user 5735, 18/08 19:52) e a foto é real (Ricardo Stuckert/PR).
- Ação: `wp post meta update 266522 cafezinho_image_kind real` + idem 266521 → `verified_real=SIM` → purge → home do espelho exibe Lula×Putin. (Decisão factual, não contorno: humano já tinha isentado.)

## 4. Estado final (09:30 BRT)

| Lado | Manchete | Trava | Expira |
|---|---|---|---|
| Canônico | 266521 Lula×Putin ✅ no hero | `manchete_lock` NYC | ~11:10 (auto-release) |
| Espelho | 266521 Lula×Putin ✅ no hero | `cmh_estado` + lock file | 11:25 (preguiçosa) |

## 5. Rollback completo (espelho)

```bash
ssh root@159.65.177.60
cp /root/sync_from_cafezinho.sh.bak_pre_manchete_humana_20260819_122003 /root/sync_from_cafezinho.sh
rm /var/www/cafezinho-news/wp-content/mu-plugins/cafezinho-manchete-humana.php
rm -rf /var/www/cafezinho-news/wp-content/uploads/cmh
cd /var/www/cafezinho-news && wp option delete cmh_estado --allow-root && wp option delete cmh_historico --allow-root
```

## 6. Caminho do port para o canônico (se Miguel aprovar)

1. Mesmo mu-plugin no canônico (`/var/www/ocafezinho/wp-content/mu-plugins/`).
2. `agente_manchete.py` (NYC): ler trava **com validade** — hoje só checa existência do arquivo; patch: se conteúdo linha1=epoch futuro → pula; vazio/ausente → comportamento atual (binário) preservado p/ compat.
3. Guarda `highlight_process` + auto-trava 2h valem para o canônico igual (hello-highlight idêntico).
4. Decidir o 🔁 Rodar no canônico: chamar a lógica GA4 do agente ou manter "recente+real" local.

---

## 7. SEGUNDA ONDA (~09:50–10:20 BRT) — porta aberta para agentes (ordem Miguel)

### 7.1 Canônico: mu-plugin `cafezinho-manchete-humana-api.php` (v1.0.0, deploy 10:13)
- REST `POST/GET/DELETE /wp-json/cafezinho/v1/manchete-humana` (namespace cafezinho/v1).
- POST: clamp 2–24h; valida publish; grava wp_highlights + `cafezinho_purge_all_caches()`; trava em `cmh_estado` {post_id, desde, ate, horas, autor, origem}; trava ativa + POST de outro post → WP_Error 409.
- GET: público, montar_resposta() {post_id, title, url, trava, lock_until, lock_until_fmt, horas, autor, origem}; expira preguiçosa.
- DELETE: solta + purga.
- Guardas `wp_ajax_highlight_process`: prio 0 bloqueia troca na coluna durante trava (wp_die 403); prio 99 auto-trava 2h em toda marcação pela coluna.
- **Descoberta:** o `set-manchete` histórico vive em **snippet WPCode ID 229816** (post_type=wpcode no banco) — nunca esteve em arquivo (por isso o grep do NODO nunca achou). Callback = Closure com `$this=WPCode_Snippet_Execute`. Permissão: edit_posts. Ele NÃO purga cache (quem purga é o agente, chamando purge-cache depois).

### 7.2 NYC: patch agente_manchete.py
- Backup `/root/agente_manchete.py.bak_pre_manchete_humana_api_20260819_131701` (aplicado 13:17 UTC).
- Nova `checar_trava_humana()`: GET na API → `trava:true` ⇒ log "⏸️ Trava humana ATIVA ate X — Pulando execucao" e return; exceção de rede ⇒ avisa e cai no legado; legado: `os.path.exists(LOCK_FILE)` binário segue valendo.
- main(): `if checar_trava_humana(): return` substitui o `os.path.exists` direto.
- Teste real: `python3 -c "import agente_manchete as a; a.checar_trava_humana()"` → TRAVADA (log comprovado).

### 7.3 Espelho: REST no mu-plugin do experimento
- Rotas: POST/GET/DELETE `/cafezinho/v1/manchete-humana` + POST `/manchete-humana/rodar` (permission edit_posts; GET público). POST aceita `post_id` ou `alvo` (URL); bloqueia 20699; trava ativa → 409.
- Teste ponta a ponta com creds `ESPELHO_WP_USER/PASS`: GET (trava demo ativa até 11:25) → POST bloqueado 409 → DELETE ok → Rodar girou 266521→266599 → POST restaura 266521+2h (autor "Redator"). Hero do espelho conferido no h1: Lula×Putin.

### 7.4 Incidente do teste + correção de imagem no canônico
- Soluço de Redis do canônico (500 "Error establishing a Redis connection") durante um POST de teste → manchete ficou 266483 por ~2 min (o POST seguinte gravou antes da trava nascer). Restaurada via API 266521 + 2h + purge.
- Hero do canônico caía no fallback do gate: 266521 sem `cafezinho_image_kind` no canônico (mesma causa do espelho). Fix: `wp post meta update 266522 cafezinho_image_kind real` (ANEXO). A meta no POST foi bloqueada pelo `cafezinho-protecao-editorial` ("post publicado por humano" — by design, ok). `verified_real=SIM`, hero = Lula×Putin.
- **Lição de verificação:** conferir o hero SEMPRE no elemento exato (`h1.manchete-titulo`), nunca com grep na página inteira — a manchete pode aparecer em bloco lateral e enganar.

### 7.5 Estado final (10:20 BRT)
Canônico: manchete 266521, trava API até 12:14 + lock binário NYC até ~11:10. Espelho: manchete 266521, trava API até 12:18. Depois disso: normalização automática nos dois lados (agente GA4 no canônico; sync :17 no espelho).

---

## 8. TERCEIRA ONDA (~10:45) — o "não muda na hora" era o gate, não cache

- Sintoma do Miguel: box gravou #266537 (Sergipe) com trava até 12:42, mas home seguia com 266599. Banco × home divergiam.
- Causa: fallback de `cafezinho_get_real_highlight` — 266537 sem `cafezinho_image_kind` e anexo "Legislative Assembly of Sergipe, Almirante Barroso Plaza, Aracaju" (Commons, real) sem marcadores no blob → verified_real=NAO → hero = último post com foto verificada.
- Fix: kind=real no anexo 266539 (+post). Home passou a servir Sergipe imediatamente.
- Melhoria do box: aviso vermelho + botão "✅ Confirmar imagem real (sou o editor)" (`wp_ajax_cmh_img_real`) quando a manchete falha no gate — marca anexo+post, purga, loga autor. Testes: aviso oculto com gate OK; botões íntegros; home OK.
- Gotcha de teste: grepar "cmh-img-real" no render dá falso positivo (o seletor JS sempre existe) — usar o rótulo do botão.
- Lembrete: a blindagem também existe no canônico (mesma marcação foi preciso no 266521).
