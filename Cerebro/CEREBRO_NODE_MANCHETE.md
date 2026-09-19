# 📰 CEREBRO_NODE — Sistema de Manchete do Cafezinho

> Documentação técnica completa do sistema que define a manchete-hero da homepage.
> Criado 2026-07-15 por Claude Code após investigação com Miguel.

---

## 🎯 Como funciona (resumo executivo)

A manchete-hero da home do Cafezinho é definida por:

1. **Plugin regular `hello-highlight`** (`/var/www/ocafezinho/wp-content/plugins/hello-highlight/highlight.php`)
   - Autor: Leandro Guedes, versão 0.1 (plugin antigo, ainda funcional)
   - Cria tabela custom `wp_highlights` com colunas `id, post_id, name, created, modified`
   - Registro fixo instalado: `(name='Manchete')`
   - Interface admin: coluna "Destacar" na lista de posts (wp-admin/edit.php) — cada post tem um `<select>` pra marcar como manchete
   - Ação de marcar dispara AJAX `wp_ajax_highlight_process` → `UPDATE wp_highlights SET post_id = X WHERE name='Manchete'`
   - Tema lê via `get_highlight('Manchete')` e renderiza no topo da home

2. **NÃO É CATEGORIA.** A categoria `Destaques` (id=5087) existe mas alimenta widgets secundários, NÃO a manchete-hero. Confirmado por Miguel 15/07: *"manchete não tem nada a ver com categoria"*.

3. **Agente_manchete** (`/root/agente_manchete.py` no NYC) roda automático a cada 2h via cron (`0 */2 * * *`):
   - Consulta GA4 pra ranquear posts das últimas 24h por views
   - Score = `views_hoje + views_ontem * 0.3 + bonus_recencia`
   - Chama endpoint REST `POST /wp-json/cafezinho/v1/set-manchete` com o post_id do vencedor
   - Também adiciona categoria "Redação" (2403) ao post (compat do tema)

---

## 🔌 Endpoints REST (namespace `cafezinho/v1`)

Registrados por mu-plugins custom em `/var/www/ocafezinho/wp-content/mu-plugins/`:

| Endpoint | Método | Auth | Função | Definido em |
|---|---|---|---|---|
| `/cafezinho/v1/set-manchete` | POST | Redator App Password | Seta a manchete via UPDATE em `wp_highlights` | **Snippet WPCode ID 229816** (banco, não é arquivo — identificado 19/08/2026) |
| `/cafezinho/v1/manchete-status` | GET | Público | Retorna `{post_id, title, url, date}` da manchete atual | `cafezinho-purge-on-manchete.php` (novo 15/07) |
| `/cafezinho/v1/purge-cache` | POST | Autor+ | Purga WP Rocket + WP core cache | `cafezinho-purge-on-manchete.php` (novo 15/07) |
| `/cafezinho/v1/manchete-humana` | POST/GET/DELETE | POST/DELETE: Redator App Password · GET: público | **Trava humana 2–24h aberta p/ agentes** (ordem Miguel 19/08): POST `{post_id, horas}` trava + grava manchete + purga; GET lê estado `{trava, lock_until, horas, autor}`; DELETE solta | `cafezinho-manchete-humana-api.php` (novo 19/08/2026) |

**Auth padrão:** Basic Auth com `Redator` + App Password (do CLAUDE.md).

**Exemplos práticos:**

```bash
# Ver manchete atual (público)
curl https://controle.ocafezinho.com/wp-json/cafezinho/v1/manchete-status

# Setar manchete no post X (auth)
curl -X POST -u "Redator:APP_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{"post_id": 261750, "name": "manchete"}' \
  https://controle.ocafezinho.com/wp-json/cafezinho/v1/set-manchete

# Purgar cache (auth)
curl -X POST -u "Redator:APP_PASSWORD" \
  https://controle.ocafezinho.com/wp-json/cafezinho/v1/purge-cache
```

---

## 🚦 Lock manual da manchete (feature 15/07)

**Problema original:** Miguel marcava manchete manualmente pelo wp-admin, mas agente_manchete sobrescrevia em ≤2h automaticamente com sua escolha por GA4.

**Solução:** arquivo flag `/root/agent_data/manchete_lock` no NYC.

- Se o arquivo existe: agente_manchete pula execução no início e apenas loga `"⏸️ Lock manual ativo..."` sem tocar em nada
- Se não existe: agente opera normal (a cada 2h)

**Comandos:**

```bash
# TRAVAR (respeita manchete manual do Miguel)
ssh root@198.199.121.136 'touch /root/agent_data/manchete_lock'

# DESTRAVAR (agente volta a operar)
ssh root@198.199.121.136 'rm /root/agent_data/manchete_lock'

# STATUS
ssh root@198.199.121.136 'ls -la /root/agent_data/manchete_lock 2>/dev/null && echo TRAVADA || echo LIVRE'
```

**Implementado em:** `/root/agente_manchete.py` no NYC (patch Claude 2026-07-15).
**Backup pré-patch:** `/root/agente_manchete.py.bak_pre_lock_purge_20260715_171057`

---

## 🧹 Purga automática de cache WP Rocket (feature 15/07)

**Problema original:** ao trocar manchete (manual ou automática), o cache do **WP Rocket** continuava servindo home antiga por 10min-algumas horas. Miguel achava que "não funcionou" quando na verdade era só cache.

**Solução:** mu-plugin `cafezinho-purge-on-manchete.php` (deployado 15/07) faz 2 coisas:

1. **Hook AJAX** — intercepta `wp_ajax_highlight_process` (o AJAX do plugin hello-highlight quando Miguel marca manchete via wp-admin). Após o UPDATE original, o mu-plugin chama `rocket_clean_domain()` + `rocket_clean_home()` + `flush_rocket_htaccess()` + `wp_cache_flush()`.
2. **Endpoint REST** `/cafezinho/v1/purge-cache` — usado pelo agente_manchete no NYC após set-manchete bem-sucedido.

**Efeito:** manchete muda visualmente **imediato** (sem esperar TTL de cache).

**Localização:** `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-purge-on-manchete.php`
**Autor:** Claude Code (2026-07-15)

---

## 📊 Log e observabilidade

**Log do agente_manchete no NYC:**
- Arquivo interno: `/root/agent_data/agente_manchete.log` (via `f.write` interno, prefixo `[manchete]`)
- Cron redirect: `/root/agent_data/manchete.log` (via `>>`)
- **⚠️ Variante do bug log duplo:** dois arquivos diferentes com conteúdo similar. Não crítico. Ver `CEREBRO_NODE_OBSERVABILIDADE.md`.

**Log do mu-plugin purge:**
- PHP error_log padrão do WP (`/var/www/ocafezinho/wp-content/debug.log` se WP_DEBUG_LOG=on) — grep por `[cafezinho-purge]`

**Verificar manchete atual:**
```bash
curl -s https://controle.ocafezinho.com/wp-json/cafezinho/v1/manchete-status | python3 -m json.tool
```

---

## 🤔 Comportamento esperado (fluxos completos)

### Cenário A: Miguel marca manchete manual e trava

1. Miguel entra no wp-admin, coluna "Destacar" na lista de posts, seleciona "Manchete" no post X
2. AJAX `highlight_process` roda → UPDATE `wp_highlights SET post_id=X`
3. **Mu-plugin purge-on-manchete intercepta** → purga WP Rocket + WP cache
4. Manchete aparece **imediatamente** na home
5. Miguel roda `ssh root@198.199.121.136 'touch /root/agent_data/manchete_lock'`
6. Próxima execução do agente_manchete (2h depois): vê lock, loga "travada", sai sem tocar
7. Manchete manual **permanece** enquanto lock existir

### Cenário B: Agente_manchete roda automático (sem lock)

1. Cron dispara às `0 */2 * * *` (00:00, 02:00, 04:00, ..., 22:00 BRT)
2. Agente checa `/root/agent_data/manchete_lock` → não existe → prossegue
3. Consulta GA4, ranqueia posts últimas 24h
4. Chama `/wp-json/cafezinho/v1/set-manchete` com post_id vencedor
5. Sucesso → chama `/wp-json/cafezinho/v1/purge-cache`
6. Manchete atualiza + cache purgado + acionamento do agente_super_engajamento pra comentários

### Cenário C: Post é publicado (novo)

- Nada especial acontece com manchete
- Post entra no pool de candidatos do agente_manchete a partir da próxima execução (se estiver na janela de 24h)

---

## 🔗 Referências cruzadas

- `forum_sprint_v3_reforma_pipeline_fase_por_fase_20260623.md` §251 — decisão histórica: "Manchete usa plugin hello-highlight, NÃO cat 5087"
- `CEREBRO_NODE_AGENTES.md` — agente_manchete listado com role "Editor-Chefe (decide manchete via bypass REST)"
- `CLAUDE.md` §12 — mapa de credenciais Redator/App Password
- `CEREBRO_NODE_OBSERVABILIDADE.md` — bug log duplo do agente_manchete (variante não crítica)

---

## 👤 Redatores / Authors (mapa do agente_manchete)

Para a **curadoria inteligente** (priorizar redação humana, tirar repetidor estatal — ordem Miguel 12/08):

| author_id | Quem | Papel | Na manchete? |
|---|---|---|---|
| **2018** | **Miguel / `james2017`** (chairman) | ✅ redação humana — **PRIORIZAR** (já tem `bonus_james` +1M nas 1ªs 8h) | ✅ sim |
| **5780** | **Gabriel** | ✅ redação humana — **PRIORIZAR** (sem bônus ainda) | ✅ sim |
| 5470 | "Redação" (`REDACAO_AUTHOR_ID`) | automação genérica (agentes V4) — 29/100 posts | contextual |
| **5786** | **repetidor estatal** | republica conteúdo estatal — **52/100 posts recentes!** | ❌ **TIRAR** da manchete |

> **Mapeamento confirmado (12/08)** via ranking de posts: 5786 (repetidor, 52) > 5470 (Redação/agentes, 29) > 5780 (Gabriel, 16) > 2018 (Miguel, 3). O repetidor estatal domina o volume — por isso a manchete puramente determinística caía nele o tempo todo. **Curadoria inteligente = veto ao 5786 + bônus aos 2018/5780 + temperatura editorial via LLM.**
> **Gabriel identificado** pelo post https://www.ocafezinho.com/2026/08/12/idade-renda-e-a-fuga-do-eleitorado-lulista-o-que-explica-a-lideranca-de-ciro-no-ceara/ (author 5780). Miguel = `james2017` (2018), confirmado por ele.

## 🏆 Modelos de capa exemplares (referência/templates pro agente manchete)

Posts que servem de **modelo de boa manchete/capa** (nacional, com pegada, tese, redação humana) — o agente manchete inteligente deve usar como referência de qualidade:

- **Post 265125 — "Lula reconquista as capitais"** (`https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/`) — author **2018 (Miguel/James2017)**, cats [5088 Eleições, 2403 Redação, 28 Vídeos]. **Modelo de capa nacional/Lula** (performance de Lula = +pontos na tese). *Ordem Miguel 12-13/08: "deixa essa na capa, usa como modelo de capa pro agente manchete".* Enxame disparado nele.

## 📝 Histórico de mudanças neste node

- **2026-09-19 (ZCode/Kimi K3):** **JANELA DIURNA AFINADA** (ordem Miguel ~10:0x — "de dia só política nacional; eleição de preferência; tecnologia/geopolítica só à noite"): de 08h às 22h a manchete exige **Política (22) ou Eleições 2026 (5088), cat OU tag** — 'Nacional' (21141) puro NÃO basta mais de dia (caso Anne Frank/Bienal coroada de manhã); noite livre. Aplicado nos DOIS decisores: gate (`is_nacional_politica_eleicoes` + tax_query com `$incluir_nacional` p/ degrau anti-vazio — home nunca vazia) e agente NYC (filtro pré-ranking + rede final que nunca coroa sem capa). Curas da véspera completadas: widget renomeado p/ "canônico" e get-manchete aposentado (leitura pelo hero da home é melhor). Manchete resultante: 271987 (Lula×drones, capa real selada). Backups: `.bak_pre_janela_politica_20260919` (gate), `.bak_pre_rename_canonico_20260919` (widget), `.bak_pre_cura_manchete_20260918` (agente). Tema Duplo: `forum_/memoria_manchete_diagnostico_atlas_voltando_20260918` (adendo 2).
- **2026-09-18 (ZCode/Kimi K3, DIAGNÓSTICO — nada alterado):** bronca do Miguel ("Atlas ficou voltando / trava humana não funciona — bug?"). Confirmados **3 bugs**: (1) `/root/agent_data/manchete_lock_override` (23/08, esquecido) faz o agente IGNORAR a trava humana em toda rodada — às 03:00 BRT o agente derrubou a trava #271729 do Miguel (valia até 07:25) e recoroou o Atlas pela 4ª vez; (2) `get-manchete` = **404 desde sempre** (871 rodadas, 0 leituras pelo endpoint) — o agente lê a "manchete atual" pelo post mais novo da cat 5087 (fonte errada; ficou cego das 05:00 às 09:03 achando que a 271757 reinava quando a home tinha Atlas); (3) a rotação 24h funciona, mas a **rede de segurança recoroa o repetido** quando o pool elegível zera (Atlas tinha aud 5-8× o resto → 4 coroações em 12h). Estado: manchete #271757 (Datafolha 48%) NO AR desde 09:03 (trava até 12:03), provada no h1 ao vivo. Cura proposta (5 passos, AGUARDA "vai"): remover override · criar get-manchete de verdade (fonte=wp_highlights) · rede preferindo MANTER a atual · relógio único de rotação (meta WP) · renomear widget. Espelho cafezinho.news = redirect 301 p/ canônico (experimento encerrado). Tema Duplo: `Foruns/forum_manchete_diagnostico_atlas_voltando_20260918.md` + `Memorias/memoria_manchete_diagnostico_atlas_voltando_20260918.md`.
- **2026-08-19 (ZCode/DeepSeek, 2ª onda):** **PORTA ABERTA PARA AGENTES** (ordem Miguel "deixa aberto e dinâmico para o agente"): mu-plugin `cafezinho-manchete-humana-api.php` no canônico (REST manchete-humana POST/GET/DELETE, trava 2–24h com mínimo 2h) + `agente_manchete.py` (NYC) patcheado p/ respeitar trava com validade via API (mantém lock binário legado; backup `.bak_pre_manchete_humana_api_20260819_131701`) + mesmo contrato REST no experimento do espelho (com `/rodar`). Fluxo: agente marca N horas → post assume a manchete → ao expirar, o agente de manchete volta a escolher sozinho. Descoberta: `set-manchete` = snippet WPCode 229816 (nunca foi arquivo). Lição: hero se verifica no elemento exato (h1), não com grep na página inteira.
- **2026-08-19 (ZCode/Kimi K3):** (1) Manchete 266521 (Lula×Putin nuclear) setada no canônico 09:09 BRT via set-manchete+purge, com trava de 2h no agente (NYC, auto-release ~11:10). **Gotcha novo: POST no controle.ocafezinho.com exige User-Agent de navegador — sem ele Cloudflare 1010.** Credencial válida = par `WP_USER_CAFEZINHO`+`WP_APP_PASSWORD_CAFEZINHO` do cofre. (2) **EXPERIMENTO "MANCHETE HUMANA" NO ESPELHO** (ordem Miguel): mu-plugin `cafezinho-manchete-humana.php` no cafezinho.news = widget no wp-admin com botão 📌 É MANCHETE + barrinha 2–24h (mínimo 2h em código) + ❌ destrava + 🔁 Rodar; coluna Destacar também ganha trava automática de 2h; sync horário patcheado p/ PULAR wp_highlights com trava fresca (achado: sync fazia REPLACE toda hora :17 e sobrescrevia o espelho). Bateria 8/8 ✅ + prova real do sync. Tema Duplo `forum_/memoria_manchete_humana_espelho_20260819`. Port p/ canônico desenhado, aguarda OK do Miguel.
- **2026-08-12 (ZCode GLM-5.2):** FÓRUM+CARTA (sem código) — **retomada da frente de comentário da manchete + nova tese** (ordem Miguel). Quatro mudanças-editoriais que **elevam** a tese de 02/08 (cap dinâmico 40-120): (1) toda manchete **obrigatoriamente** comentada; (2) volume **80-130** comentários/manchete (antes 40-120); (3) **todo post da cat 22 (Nacional/Política) comentado** — não só a manchete; (4) **manchete SÓ nacional até o 2º turno eleitoral** (out/nov 2026) — `agente_manchete` passa a só eleger posts da cat 22. Estrutura proposta: **Agente Manchete** (decide QUAL) × **Agente Comentarista** (garante QUANTO/QUE). Documento-base: `Foruns/forum_manchete_comentario_soh_nacional_ate_2turno_20260812.md`. Carta à Trindade: `Foruns/cartinhas/cartinha_trindade_manchete_comentario_soh_nacional_20260812.md` (tag `[TRINDADE-MANCHETE-COMENTARIO-NACIONAL]`). **Não implementado** — fase de debate. Pendências: checar crontab V4 no NYC (estado ambíguo, pode estar OFF), confirmar data do 2º turno, decidir custo × kill switch `$5/dia`, decidir unificar V4+Enxame, edge case "sem post nacional recente".
- **2026-07-15 (Claude Code):** criado após investigação com Miguel + implementação de 2 fixes (lock file + purga automática)

*Editar via patch/Edit — nunca full rewrite.*

---

## 🇧🇷 REGRA DA JORNADA NACIONAL (15/09/2026 — ordem Miguel, ATIVA)

**Das 08h às 22h (Brasília), a manchete só pode ser post Nacional, Política ou Eleições 2026** (tag OU categoria; slugs: nacional, politica, politica-2, eleicoes-2026, eleicoes2026, eleicoes). Implantada no próprio gate de render (mu-plugin `cafezinho-real-image-gate.php` v1.1.0, funções `cafezinho_manchete_*`): manual fora da régua é rejeitado em silêncio de dia (volta a valer às 22h); fallback = nacional mais recente com capa verificada (degrau: capa qualquer se nenhum tiver selo; nunca fica vazio). 🔴 Bug de core documentado: `tax_query` + `category__not_in` juntos furam o filtro (mesclagem OR) — exclusão 20699 vive DENTRO da tax_query com relation AND. Detalhes: `Foruns/forum_regra_manchete_nacional_jornada_20260915.md` + `Memorias/memoria_regra_manchete_nacional_jornada_20260915.md`. Espelho cafezinho.news: aplicar quando reabrir.
