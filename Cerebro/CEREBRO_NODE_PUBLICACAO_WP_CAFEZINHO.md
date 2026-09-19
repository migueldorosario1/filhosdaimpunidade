- **🌊 MATÉRIA HUTIS × BAB EL-MANDEB (14/09, ZM — ordem Miguel urgente ~17:0x):** `Foruns/forum_bab_el_mandeb_houthis_20260914.md` + `Memorias/memoria_bab_el_mandeb_houthis_20260914.md` — rascunho **270884** «Hutis apertam o gargalo por onde passava 9% do petróleo» (Redação 5470, cats 2403+5003+5052, capa 270885 = foto ISS da NASA c/ Perim ao centro PD, img_check+carimbo §86+§136 ok, verificador 0 infrações) aguardando **ponte revisar E publicar** (autorizado pelo Miguel; bloc ZM-20260914-008; slot 20:01 sugerido) · fatos 11/09: costa iemenita inteira + Perim/Hanish/Mokha/Dhubab (Reuters/CNN/AJ/BBC); 9 mi b/d ≈9% (EIA); Brent US$ 110 intradia, hoje +4,9% 109,74 (Folha); dólar R$ 5,16 (UOL)
- **📸 MANUAL DA CAPA DO CAFEZINHO (14/09, ZM — ordem Miguel):** `Estilo/MANUAL_DA_CAPA_CAFEZINHO.md` — instruções completas p/ capadores: 4 rotas de imagem (banco de mídia V4 NYC via featured_image_runtime_cli; Flickr oficial/Commons/receita staticflickr+UA+SHA1; biblioteca do WP c/ wp media list; IA flux-pro p/ tecnologia Emenda 11), licenças (CC BY/BY-SA/PD ok; NC/ND/all-rights NUNCA; crédito SÓ na legenda), regras editoriais (Emenda 12 pessoa=foto real; blacklist datadas; dedup 72h), passo-a-passo de aplicação (img_check ANTES thumb; carimbo §86; _publicado_por; Rocket index-https), escalação do alerta v1.6 · par: memoria_auditoria_pipeline_capa_20260914 §8 + forum_auditoria_pipeline_capa_parado §10.1
# Cérebro Node — Publicação WordPress O Cafezinho (todos os LLMs)

**Atualizado:** 2026-09-01 (rascunho editorial 268576 fim da 6x1)  
**Última pauta editorial manual (01/09):** fórum `Foruns/forum_pauta_6x1_lula_politica_20260901.md` — reescrita da Agência Senado c/ pegada política; **draft 268576** (autor 5795 zcode_miguel, cats Política+Eleições 2026, thumb 268575, olho no excerpt); aguarda revisão do Miguel.
**Escopo:** Grok Desktop, Grok Cursor, ChatGPT, Claude Code, Codex, Kimi, DeepSeek, Qwen, GLM, Antigravity — qualquer agente com acesso ao workspace local ou cofre Tencent.  
**Tutorial expandido:** `Projeto Cafezinho Agentes/Foruns/forum_tutorial_publicar_wordpress_cafezinho_todos_llms_20260620.md`  
**Script canônico (PC):** `scratch/publicar_cafezinho_wp.py`  
**Chatbots celular/desktop:** `Outros/chaves/wp_cafezinho_chatbots.md` + `Cerebro/cartoes_bolso/CARTAO_BOLSO_WP_CAFEZINHO_SYNC_CHATBOTS.md`
**Menu do site (editar/corrigir/travar):** `Cerebro/cartoes_bolso/CARTAO_BOLSO_MENU_WP_CAFEZINHO.md` — menu canônico = term **21062** (topo+rodapé+AMP são o MESMO); regra de ouro (06/08/2026): `auto_add` SEMPRE desligado — publi autorizado não pode entrar no menu (caso-escola `BUG-20260806-MENU-SPAM-CASSINO-AUTOADD`).
**Publipost (apostas/afiliação) = PÁGINA, nunca post (regra 11/06, executada 25/08 com sanção do dono):** 3 emails ao Gabriel (21:38/21:40/21:48, msmtp 250 OK) + **intervenção do Miguel (dono/SEO, "eu autorizo")**: 265611 e 267630 convertidos post→**page** via SQL (mu-plugin `cafezinho-protecao-editorial` bloqueou wp-cli — §130; bypass SQL SÓ com ordem expressa do dono) e ambos em **pending** fora do ar (provas: URL antiga 404, feed e home limpos; backup `/root/backup_265611_267630_pre_page_20260825.tsv`). Motivo registrado: post de apostas = perda de autoridade Google em momento delicado. Aguarda Gabriel revisar/publicar as pages; ao republicar 265611, criar 301 da URL com data. Fórum: `Foruns/forum_email_gabriel_publipost_apostas_pagina_20260825.md` · regra-mãe: `claude_memory/feedback_publipost_so_como_page_nao_post.md`.
**Taxonomia (categorias + tags) — GRANDE LIMPEZA em planejamento:** `Cerebro/Foruns/forum_grande_limpeza_taxonomia_cafezinho_20260812.md` — plano em 7 etapas. Diagnóstico (12/08): **296 categorias** + **19.460 tags** (969 órfãs, 12.845 singletons, 59 com `#`); ~45 categorias são nomes de colunistas (virar tag); modelo-alvo **~15 editoriais** + eixo geografia **Regional▸5regiões▸27estados** com **cidade = tag**. Redirects 301 obrigatórios quando categoria some (SEO — ver `CEREBRO_NODE_SEO_OBSERVATORY.md`). **✅ WHITELIST APROVADA (12/08 23:10).** **Política canônica = `Cerebro/cartoes_bolso/CARTAO_BOLSO_POLITICA_CATEGORIAS.md`** (referência rápida — ONDE publicar, 1 página) + `Foruns/forum_politica_categorias_cafezinho_20260812.md` (detalhe). Princípio: **tudo fora da whitelist vira TAG, nunca categoria nova**; categorias antigas = arquivo morto. Faxina do histórico pausada.

---

## ⚠️ DIRETRIZ PRINCIPAL — CORRIGIR POSTS EXISTENTES (13/08/2026)

> **Para corrigir post já existente no WordPress canônico, o caminho preferencial é SSH direto no `cafezinho-wp` + WP-CLI.**
>
> Isso vale para Claude, Codex, Kimi, GLM, DeepSeek, Qwen, ZCode e qualquer agente CLI com acesso à chave. A API REST é alternativa quando o agente não tem SSH ou quando o fluxo externo realmente exige API.

```bash
ssh cafezinho-wp
# WordPress canônico: /var/www/ocafezinho
# Executar WP-CLI como www-data:
cd /var/www/ocafezinho
sudo -u www-data wp ...
```

### Método correto

- Para título, texto, status, categoria, metadados e imagem destacada, usar WP-CLI ou um PHP temporário executado com `wp eval-file`.
- Dentro do PHP, usar funções oficiais: `wp_update_post()`, `wp_set_post_categories()`, `update_post_meta()` e `set_post_thumbnail()`.
- **Não fazer `UPDATE` cru diretamente nas tabelas MySQL** para corrigir posts. Isso pode deixar revisions, hooks, cache Redis, taxonomia e plugins inconsistentes.
- Para lotes com **5 posts ou mais**, gerar antes snapshot JSON com título, conteúdo, status, categorias, imagem destacada e metadados essenciais.
- Para exclusão, sempre gerar backup JSON explícito e preferir lixeira recuperável.
- Depois da mudança, confirmar no WP-CLI e, quando afetar renderização ou publicação, verificar também a URL pública `www.ocafezinho.com`.

### Quando usar REST

- Agente sem acesso SSH funcional ao canônico.
- Integração externa ou automação já desenhada para a API.
- Criação remota de rascunho quando executar no servidor não trouxer vantagem.

**Resumo:** correção em lote = SSH + WP-CLI; correção isolada = preferencialmente SSH + WP-CLI; REST = fallback; MySQL cru = evitar.

**Fórum de alinhamento da Trindade:** `Cerebro/Foruns/forum_diretriz_correcao_posts_ssh_wpcli_trindade_20260813.md`

---

## 0. Dois modos — escolha pelo ambiente

| Modo | Ambiente | Credenciais | Como publicar |
|------|----------|-------------|---------------|
| **A — Workspace** | Cursor, Claude Code, terminal PC | Cofre `.env.unificado` | `python3 scratch/publicar_cafezinho_wp.py criar ...` |
| **B — Chatbot** | ChatGPT, Grok, Claude **app** (celular/desktop) | Cartão `Outros/chaves/wp_cafezinho_chatbots.md` | curl / fetch do cartão; imagem **anexada no chat** |

**Setup chatbot (Miguel, uma vez):** copiar `wp_cafezinho_chatbots.md` → Google Docs no celular + Project Knowledge do ChatGPT/Claude. Ver `CARTAO_BOLSO_WP_CAFEZINHO_SYNC_CHATBOTS.md`.

Regenerar cartão após trocar senha: `python3 Cerebro/scripts/gerar_cartao_wp_chatbots.py`

---

## 1. Resumo em 60 segundos

| Item | Valor |
|------|--------|
| Site público | https://www.ocafezinho.com |
| API REST (painel) | https://controle.ocafezinho.com/wp-json/wp/v2/ |
| Autenticação | HTTP Basic Auth — usuário WP + **Application Password** |
| Status padrão do agente | `draft` — **nunca** `publish` sem ordem de Miguel ou Claude Daemon |
| Regra §86 | Todo post precisa de `featured_media` > 0 (imagem destacada) |
| Fluxo | upload imagem → `media_id` → POST/PATCH post com `featured_media` |

---

## 2. Credenciais (cofre — valores NÃO vão neste node)

**Regra Art. 1:** senhas e Application Passwords ficam **somente** no cofre local. Agentes **leem do arquivo**; nunca copiam valor para chat, fórum, memória markdown ou Git.

### Cofre canônico (Miguel / máquina local)

```text
/home/migueldorosario/Downloads/Antigravity Google/Outros/chaves/agentes_labs/.env.unificado
```

Espelhos úteis:

```text
Projeto Cafezinho Agentes/root/.env.unificado
```

### Variáveis (ordem de fallback no script)

| Variável | Uso |
|----------|-----|
| `WP_SITE` | Base da API. Default: `https://controle.ocafezinho.com` |
| `WP_USER_CAFEZINHO` | Usuário REST atual: `Redacao nova` (slug WP `redacao-nova`) |
| `WP_PASS_CAFEZINHO` | Application Password do Cafezinho |
| `WP_USER` | Fallback se `WP_USER_CAFEZINHO` ausente |
| `WP_APP_PASSWORD` / `WP_PASS` | Fallback se `WP_PASS_CAFEZINHO` ausente |

### Carregar no terminal (bash)

```bash
COFRE="/home/migueldorosario/Downloads/Antigravity Google/Outros/chaves/agentes_labs/.env.unificado"
set -a && source "$COFRE" && set +a
# Teste sem vazar senha:
curl -s -o /dev/null -w "%{http_code}" -u "$WP_USER_CAFEZINHO:$WP_PASS_CAFEZINHO" \
  "$WP_SITE/wp-json/wp/v2/users/me"
# Esperado: 200
```

### Carregar em Python

```python
from pathlib import Path

COFRE = Path("/home/migueldorosario/Downloads/Antigravity Google/Outros/chaves/agentes_labs/.env.unificado")
for line in COFRE.read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
```

### Cofre no servidor Tencent (agentes em produção)

```text
/root/chaves.sh          # exporta variáveis no cron
/root/.env               # ou espelho em /root/cafezinho/portal_cafezinho/
```

Agentes no servidor usam o mesmo par `WP_USER_CAFEZINHO` / `WP_PASS_CAFEZINHO` quando publicam via `motor_publicador.py`.

**Rotação 2026-07-27:** nova Application Password do usuário `redacao-nova` validada no endpoint `/wp-json/wp/v2/users/me?context=edit` (HTTP 200; perfil administrador). O valor existe somente no cofre `.env.unificado`; documentação e scripts não devem conter a senha em texto claro.

### Verificar presença sem expor valor

```bash
grep -E '^WP_(SITE|USER|PASS)' "$COFRE" | sed 's/=.*/=<no cofre>/'
```

---

## 3. Endpoints REST usados

| Ação | Método | URL |
|------|--------|-----|
| Upload imagem | `POST` | `{WP_SITE}/wp-json/wp/v2/media` |
| Criar post | `POST` | `{WP_SITE}/wp-json/wp/v2/posts` |
| Atualizar post | `POST` | `{WP_SITE}/wp-json/wp/v2/posts/{id}` |
| Ler post (edição) | `GET` | `{WP_SITE}/wp-json/wp/v2/posts/{id}?context=edit` |
| Listar categorias | `GET` | `{WP_SITE}/wp-json/wp/v2/categories?per_page=100` |

**Headers upload:** `Content-Disposition: attachment; filename="..."`, `Content-Type: image/jpeg` (ou mime correto), `User-Agent: CafezinhoAgent/1.0`.

---

## 4. Payload mínimo (criar rascunho)

```json
{
  "title": "Título editorial",
  "content": "<p>HTML do corpo...</p>",
  "status": "draft",
  "featured_media": 259949,
  "categories": [22]
}
```

**Atualizar só o corpo:**

```json
{ "content": "<p>...</p>" }
```

**Publicar (só com AUTH explícita):**

```json
{ "status": "publish" }
```

---

## 5. Script canônico (qualquer LLM com shell)

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google"

# Criar rascunho novo
python3 scratch/publicar_cafezinho_wp.py criar \
  "Título da matéria" \
  scratch/attachments/imagem.jpg \
  scratch/attachments/corpo.html \
  22

# Atualizar post existente (só HTML)
python3 scratch/publicar_cafezinho_wp.py atualizar 259950 scratch/attachments/corpo.html

# Atualizar título + corpo
python3 scratch/publicar_cafezinho_wp.py atualizar 259950 scratch/attachments/corpo.html --titulo "Novo título"
```

---

## 6. Categorias frequentes

Fonte local: `Outros/Agentes Labs/taxonomia_wordpress.json`  
Fonte servidor: `/root/taxonomia_wordpress.json`

| ID | Nome |
|----|------|
| 22 | Política |
| 19936 | Ciência e Tecnologia |
| 5008 | Inteligência Artificial |

**Nunca** enviar `categories: []` em publish — motor rebaixa para draft.

---

## 7. Dicas operacionais (erros comuns)

1. **Imagem não existe no ambiente do agente** — Grok Desktop usa `/home/workdir/attachments/`; Cursor usa `scratch/attachments/`. Copiar arquivo antes de publicar.
2. **Título ≠ primeira linha do texto** — título vai no campo `title`, não no `content`.
3. **401 rest_forbidden** — Application Password errada ou expirada; gerar nova no WP Admin → Usuários → Application Passwords.
4. **featured_media: 0** — upload falhou ou PATCH esquecido; post inválido para §86.
5. **Conteúdo duplicado** — usar PATCH em post existente, não criar segundo post.
6. **Preview draft** — https://controle.ocafezinho.com/wp-admin/post.php?post={id}&action=edit (requer login WP).

---

## 8. Governança

| Regra | Fonte |
|-------|--------|
| Padrão `draft` | Trindade / Miguel |
| §86 imagem obrigatória | `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` |
| Não expor cofre em chat | Art. 1 Constituição |
| `publish` só com AUTH | Claude Daemon ou ordem Miguel |
| User-Agent identificado | Evita bloqueio CDN/WP |

---

## 10. Credenciais Antigravity e Regra de Links Públicos (2026-07-28)

| Item | Valor / Regra |
|------|--------------|
| **Usuário Exclusivo Antigravity** | `James2017` (Application Password no cofre `.env.unificado`) |
| **Finalidade** | Operação headless e publicações diretas efetuadas pelo Antigravity Desktop |
| **Domínio Backend (API REST)** | `https://controle.ocafezinho.com` (Uso exclusivo de sistema; **NUNCA** divulgar) |
| **Domínio Público Oficial (Mandamento #8)** | `https://www.ocafezinho.com` (Todas as URLs finais entregues ao usuário ou divulgadas publicamente **DEVEM** usar o domínio público oficial) |

---

## 11. Links de retorno rápido

- Cofre índice: `CEREBRO_NODE_COFRE_CHAVES.md` § WordPress Cafezinho
- Memória Grok (sessão WP): `memorias_provisorias/memoria_grok_viva.md`
- Exemplo real: post_id **259950**, media_id **259949** (rascunho socialismo/democratas, 2026-06-20)
- Exemplo Antigravity: post_id **263282**, media_id **263281** (Cármen Lúcia na FLIP, 2026-07-28)
- Upload legado com metadados: `Projeto Cafezinho Agentes/Legacy20260610/root/upload_imagem_wp.py`

---

## 12. Conhecimento estrutural do canônico (base de aprendizado viva)

> **Índice mestre:** `Memorias/INDICE_APRENDIZADO_CANONICO_OCAFEZINHO.md` (criado 11/08/2026 por ZCode GLM-5.2, ordem do Miguel)
>
> **Filosofia:** cada descoberta sobre o canônico (ads, categorias, plugins, DB, estrutura) vira entrada indexada nesse documento vivo, pra qualquer agente (Claude/ZCode/Codex) aprender mais rápido. Cresce a cada iteração do sprint visual.

### Aprendizados consolidados (11/08/2026)

- **Publisher GAM real:** `/21715141650,22670554696/ocafezinho.com/...` (NÃO `21622511100` — ID errado que aparecia em docs anteriores, retratado)
- **Ad-inserter:** 19 `used_blocks`, 18 com code; quase todo AMP (16 slots GAM + 1 mgid só em `/amp/`)
- **Non-AMP ads:** só Teads (bloco 17) + 360yield header (option `wpc_inner_header_wide_ad`, ⚠️ mixed content HTTP)
- **Plugins de ads ativos (3):** `ad-inserter`, `ads-txt`, `insert-headers-and-footers` (legacy inerte). **Quick AdSense e Colabs NÃO existem.**
- **Estrutura home:** canônico tem 2 blocos (Manchete + Coluna Editor); espelho reformado tem 7 (+Nacional, Geopolítica, Ciência, Linha do Tempo, Recentes) + 5 V4 (Cultura, Economia, Meio Ambiente, Saúde, Esporte) + **Vídeos (12/08)** = 11 blocos `section.pb-5`
- **Categorias dos blocos temáticos:** Nacional=[22,43], Geopolítica=[5003], Tecnologia=[30], Cultura=[79], Economia=[43], Meio Ambiente=[582], Saúde=[258], Esporte=[1271], **Vídeos=[28]**, Linha do Tempo=sem filtro, Recentes=`post__not_in=$excludes`
- **Bloco Vídeos (12/08, espelho):** `category__in=array(28)`; cat 28 (tt_id 29) populada com 107 posts embed-YouTube (publish, ≥2026-06-12) — count real 4→111. Modelo = bloco Cultura. **Pendente:** portar ao canônico após homologação. Detalhes: `Foruns/forum_bloco_videos_espelho_cafezinho_20260812.md`. ⚠️ count declarado da cat 28 era 655 (fantasma); sempre cruzar com `COUNT(*)` real em `wp_term_relationships`.
- **Autor Miguel = ID 2018** (Coluna do Editor)
- **ads.txt:** 1822 vendors (richaudience, rubicon 17210, appnexus 10264, pubmatic 156383, criteo B-060278, smartadserver 1743, etc.)

### Documentos filhos

- Mapa ads (decisões): `Foruns/forum_mapa_ads_canonico_ocafezinho_20260811.md`
- Mapa ads (log técnico): `Memorias/memoria_mapa_ads_canonico_ocafezinho_20260811.md`
- Sprint visual transferência: `Foruns/forum_transfer_sprint_visual_cafezinho_zcode_20260811.md`

---
## § AUDITORIA INTEGRAL V4 (13/08/2026, ZCode Kimi K3)
- Sprint handoff Codex/Miguel: `Foruns/forum_handoff_zcode_auditoria_todos_v4_padrao_ouro_20260813.md`
- **Fase 0+1:** `Foruns/forum_auditoria_v4_todas_verticais_fase01_20260813.md` + `Memorias/memoria_auditoria_v4_todas_verticais_20260813.md` (evidências `ZCodeProject/auditoria_v4_20260813/fase0/`)
- Achados-chave: 5 novas redigem OK (gargalo = imagem+fila); cultura deadlock permanente SEM_IA; Nordeste/Centro-Oeste sem draft_events; nenhum caminho automático a publish.

---
## § POLÍTICA DE LEGENDA DE FOTO (16/08/2026, ordem Miguel — ZCode Kimi K3)
- **Regra:** legenda visível = SÓ descrição factual; crédito/licença/fonte no campo DESCRIÇÃO do anexo (+ALT); legenda só no single post (home não mostra — tema V2.9); UTF-8 limpo (proibido `\uXXXX` literal).
- Tema Duplo: `Foruns/forum_politica_legenda_foto_cafezinho_20260816.md` + `Memorias/memoria_politica_legenda_foto_cafezinho_20260816.md`
- Aplicado em: prompt da Caçadora (automação e1b2d648), diretriz canal Trindade + inboxes Claude/Grok, passivo de 116 anexos migrado.

---
## §gate-imagem-checada (16/08/2026 — fail-close, ordem Miguel)

Nenhuma transição p/ `publish` de post passa sem `_cafezinho_img_check` (ok) ou `_cafezinho_img_isenta` (isenção editorial humana via checkbox no editor). Mu-plugin `cafezinho-gate-imagem-checada.php` (espelho+canônico): REST 400 / revert→pending fora do REST (inclui future→publish do wp-cron). Complementa o §86 (imagem obrigatória). Checagem = Tribunal Visual (`/root/checar_imagem_vision.py` no NYC, exit 0/1/2) com fallback de checagem visual do agente quando o Vision está sem crédito. A caçadora (e1b2d648) grava a meta no PASSO 4.1 e varre imagens sem checagem no 4.5. **Banco de links: CONGELADO/PROIBIDO como fonte (auditoria 16/08: 407 entradas → 285 APROVADAS Commons + 122 REPROVADAS, sendo 100% do Flickr contaminado); versão depurada `banco_links_midia_auditado.jsonl` (285) só volta como candidata após ordem do Miguel.** Regras p/ todos os agentes no topo do fórum: `Foruns/forum_gate_imagem_checada_fail_close_20260816.md` · memória: `Memorias/memoria_gate_imagem_checada_fail_close_20260816.md`.

---
## §banners-moka-reader (16/08 estudo → 17/08 APLICADO home+single não-AMP; AMP e temáticos pendentes)

Banners animados do Moka Reader (4 HTML autossuficientes PT/EN, iframe tamanho exato, link mokareader.com): plano de publicação SEM tocar nos slots GAM/Taboola/Teads/MGID existentes (Ad Inserter desligado na home desde 14/08; AMP 64% das views fica sem banner na fase 1). Inserção = slot novo no tema (front-page.php), arquivos em `wp-content/moka-banners/` nos 2 servidores (sync não copia wp-content). Temáticos = `public/banners/` + `MokaBanner.astro` (AdSense auto ads, sem conflito de slot). Fórum: `Foruns/forum_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md` · memória: `Memorias/memoria_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md`.

- 17/08 ~01:30: **cross-promotion da rede CMG** — conceito, matriz por idioma, zonas vazias (sidebar sticky/after-recents) e 12 prompts p/ Claude Design em `Foruns/forum_banners_cross_promo_rede_cafezinho_media_group_20260817.md` (aguarda artes + "vai" da implementação).

---
## §mapa-sinais-autoria (21–22/08/2026) — QUEM FEZ O QUÊ em cada post

> **Documento vivo:** `Foruns/MAPA_SINAIS_AUTORIA_CAFEZINHO.md` — tabela-mestre de sinais + árvore de decisão. USE este mapa antes de perguntar "de quem é este post".

- **Sinal permanente (22/08):** meta `_cafezinho_origem` (via rest/wp-cli/cron/admin + User-Agent) gravada AUTOMATICAMENTE em todo post novo pelo mu-plugin `cafezinho-origem-post.php` (classificador: função `cafezinho_classificar_autoria()` — nova regra de fluxo edita ali).
- **API:** `GET /wp-json/cafezinho/v1/autoria?horas=&limite=&fmt=json|md` (auth app password "Integracoes-Autoria", cofres `AUTORIA_*`; fonte ÚNICA de classificação — não reimplementar).
- **Autorias:** 2018=Miguel (James2017) · 5780/5735=Gabriel Barbosa · 5786=agentes (V4/YouTube/V5) E ferramentas do Miguel via Antigravity/Manus (UA `Antigravity/1.0`, podem assinar author=2018) · 5470=repetidor estatal · 5742/5785=pool técnico Motor V5 · **5788-5798=identidades do PROTOCOLO_SSH_AGENTES_v1** (rótulo automático "Agente <nome> (SSH v1)").
- **Bug GMT correlato:** drafts via wp-cli nascem `post_date_gmt=0000-00-00` (invisíveis a date_query por GMT) — filtrar com tolerância (fix aplicado na API).
- Sprint: `Foruns/forum_mapa_sinais_integracoes_baleia_cctv_20260822.md` (+Adendos views/coordenação ponte) · raio-X inicial: `Foruns/forum_mapa_autoria_posts_v4_v5_humanos_20260821.md` · memória: `Memorias/memoria_mapa_sinais_integracoes_baleia_cctv_20260822.md`.

## 23/08/2026 — Pauta editorial: 4 artigos do ato de Lula em Bangu (22/08)
- `Foruns/forum_4_artigos_bangu_lula_20260823.md` + `Memorias/memoria_4_artigos_bangu_lula_20260823.md` — produção humana (ZCode/GLM-5.3) a partir da transcrição do Moça Bonita; diretórios em `Outros/pautas editoriais o cafezinho/2026 Ago 23/lula no rio/` (Paes ✓ · Lula, Benedita+Pedro Paulo, Cavaliere pendentes). Fact-check independente previsto depois (pendências nas notas de cada artigo).

## 26/08/2026 — Troca de capa em post publicado (caso-escola do procedimento completo)
- `Foruns/forum_troca_capa_marina_quaest_senado_sp_20260826.md` + `Memorias/memoria_troca_capa_marina_quaest_senado_sp_20260826.md` — post 267686 (Quaest Senado SP): fachada do Senado → Marina na COP30 (Commons CC BY-SA 4.0, mídia 267739), ordem direta do Miguel.
- **Procedimento que funcionou (reusar):** (1) inspeção visual de TODAS as candidatas antes de escolher; (2) `ImageOps.exif_transpose` antes de crop; (3) upload REST com caption/alt/crédito; (4) **carimbo `_cafezinho_img_check` ANTES de `_thumbnail_id`** (gate visão-capa rejeita media_id sem carimbo casado — REST devolve 200 mas ignora); (5) `wp eval wp_update_post` p/ reindexar Yoast (og:image/JSON-LD ficam presos no indexable); (6) rm cache Rocket da home + prova ao vivo com screenshot.

## 🖼️ EMENDA 11 (26/08/2026 — ordem Miguel) — tecnologia pode ter capa IA
- [Fórum EMENDA 11 — capa IA em tecnologia + caso LNCC 267719](Foruns/forum_emenda11_capa_ia_tecnologia_lncc_20260826.md) — regra viva: tecnologia (esp. IA/supercomputadores) PODE ter capa IA sem texto interno; banco real reprovado → gerador editorial é caminho legítimo; caso 267719 = Flux Pro (mídia 267763).
- [Memória técnica emenda11](Memorias/memoria_emenda11_capa_ia_tecnologia_lncc_20260826.md) — log completo + gotcha: Rocket grava `index-https.html`/`index-mobile-https.html` (find -name index.html não acha).

- **26/08 — BLOCOS SAÚDE/ESPORTE/MEIO AMBIENTE RELIGADOS NO V4.1 (2-3x/dia, ordem Miguel):** as 3 verticais estavam órfãs desde a ordem "só V4.1" de 24/08 (coletavam mas ninguém redigia). v41_ciclo.py passa a aceitar as 3 verticais (pauta = `new` frescas 48h; patch de categorias no nascimento [258/1271/582, 2403]); coletas 1x→3x/dia; 3 ciclos v41 novos 3x/dia (`V41_3VERTICAIS_20260826`). Prova: rascunho 267820 (saude) draft com cats certas; publicação segue com CM/AGY. Detalhes: `Foruns/forum_blocos_saude_esporte_ambiente_v41_20260826.md` + `Memorias/memoria_blocos_saude_esporte_ambiente_v41_20260826.md`. Lateral registrada: repetidor estatal bloqueado no gate de imagem desde 16/08 (199 falhas — incidente separado).

- **26/08 — BLOCO DIGITAL na home + vertical V4.1 nova (ordem Miguel ~19:35):** categoria `Digital` term_id **21189**; vertical completa do zero (coletor seção `dig` c/ 5 feeds cultura digital, intake, v41_ciclo, runtime `v4_digital` + diretriz própria); crons 3x/dia (`V41_DIGITAL_20260826`); semente 5 posts on-theme; bloco no front-page.php após Esporte (padrão 1+5); home ao vivo com o bloco populado (cache Rocket limpo). 1º ciclo reprovou pauta B2B por sem-tese (fail-closed OK). Receita completa de criar vertical V4.1 em 7 pontos: `Foruns/forum_bloco_digital_home_vertical_v41_20260826.md` + `Memorias/memoria_bloco_digital_home_vertical_v41_20260826.md`.

- [Fórum DS-N Publicador + DS-N Ideias — 2 robôs NO AR + batismo 5/5](Foruns/forum_ds_nuvem_publicador_ideias_20260831.md) — Publicador 15/15 (Tencent): publica só consenso CL citado/resgate DSC-004, sem capa não publica, freio 3/dia, respeita GATE-IMG; Ideias 30/30: arquiteto de brainstorms, nunca executa. Batismo 31/08: 5/5 elegíveis no ar (268374/373/372/380/386) com capas crédito+licença e Tribunal Visual. Quirk REST future→wp_publish_post.
- [Memória técnica do batismo](Memorias/memoria_ds_nuvem_publicador_ideias_20260831.md) — decisões (scan janela ±120 `consenso|resgate|elegível`; capa aprovada ≠ consenso publicação), comandos, bugs curados.

- **04/09 — POST MANUAL COM VÍDEO "Ciro não está comigo" (ordem Miguel ~22:2x, ZM-20260904-085):** post 269085 publicado 22:41 (autor 5795) com vídeo nativo `<video>`, capa Ricardo Stuckert do Flickr do dia, 4 links internos p/ pesquisas de hoje; transcrição faster-whisper local; cats 22/4984/4968/5088 + 5 tags. Armadilhas novas: slot-20min empurra publish p/ future via wp-cli (cura = --user=<admin ≠ autor> + post_date < current_time do WP) e protecao-editorial trava meta pós-publish humano (thumbnail ANTES de publicar). [Fórum](Foruns/forum_lula_juazeiro_ciro_nao_esta_comigo_20260904.md) + [Memória](Memorias/memoria_lula_juazeiro_post_manual_20260904.md).

- **07/09/2026 (tarde)** — [Fórum CULTURA DE QUALIDADE CAFEZINHO](./Foruns/forum_cultura_qualidade_cafezinho_20260907.md) — debate convocado pelo Miguel: curadoria ANTES da coleta (precisar menos de juiz), qualidade+segurança na Constituição, forma divertida × conteúdo sério, toda matéria ensina; retrospectiva de erros dos meses.
- **07/09/2026 (tarde)** — [Fórum NOVO AGENTE DE COMENTÁRIOS SEGURO](./Foruns/forum_agente_comentarios_seguro_discussao_20260907.md) — ⚠️ SÓ DISCUSSÃO (trava do Miguel: NÃO ATIVAR); arqueologia das 3 gerações mortas + elenco de ~63 personas + 5 pilares (seguro/moderado/bem colocado/humanizado/biografias).

- **14/09 — BANNER KUBET (thbku.bet) REVEZANDO 50/50 COM O MOKA (ordem Miguel ~18:1x):** rotator client-side (`Math.random()`+`location.replace`, imune a cache de página) nos 2 pontos do MOKA — home (`#moka-banner-home`, front-page.php) e single (mu-plugin `cafezinho-moka-single.php`); criativos em `wp-content/banners-cafezinho/` (logo 351×141 do Miguel, fundo #051939, +18, rel sponsored); regra "1 anúncio por intervalo" preservada (nunca empilha); provas: 200×5, ~24 sortes ≈50/50, screenshots KUBET×MOKA no mesmo slot, single alternando 5/5; `banner-after-comments` segue VAZIO para campanha futura. Aviso regulatório dado (bet offshore × SPA 1.315/2025 — decisão editorial do Miguel). [Fórum](Foruns/forum_banner_kubet_revezamento_moka_20260914.md) + [Memória](Memorias/memoria_banner_kubet_revezamento_moka_20260914.md).

- **15/09 — PORTA DE REVISÃO EDITORIAL PARA O CLAUDE + GATE v1.2.5 (ordem Miguel ~19:35, "liberar o claude para alterar"):** Claude travava no 423 `post_publicado_por_humano` ao corrigir posts publicados via REST; solução = porta de revisor já existente (ZM_REVISOR_AST): option `cafezinho_revisores_editoriais` `["AST"]`→`["AST","CLAUDE","ZM"]` + patch do mu-plugin `cafezinho-protecao-editorial.php` v1.2.0→v1.2.5 (exceções do revisor nos hooks WP-CLI de taxonomia — reafirmação idêntica passa, mudança real segue bloqueada — e de meta — blacklist editorial: `_cafezinho_*` exceto trilha de auditoria, `_publicado_por`, `_agente_*`, `_thumbnail_id` seguem travadas). Receitas: REST header `X-Cafezinho-Revisor: CLAUDE` · wp-cli `CAFEZINHO_EDITORIAL_REVISOR=ZM wp post update <id> arquivo`. Provas E2E: wp-cli Success + REST no-op HTTP 200 revisor=claude + auditoria sha igual + site 200 limpo. Post 270762 (pesquisa BTG × crise STF) corrigido: 10 travessões→0. ⚠️ Incidente de processo: 4 min de 500 por patch sem lint prévio (19:45-19:48, restaurado; lição: php -l em /tmp ANTES do mu-plugins). [Fórum](Foruns/forum_revisao_editorial_porta_claude_20260915.md) + [Memória](Memorias/memoria_revisao_editorial_porta_claude_20260915.md).

- **15/09 23:0x — LIBERAÇÃO GERAL DA REVISÃO (V2, ordem Miguel ~22:5x «destrava geral, registra e faz backup»):** gate protecao-editorial v1.3.1 — qualquer agente (wp-cli/REST, sem header/env) pode UPDATE de título/corpo/excerpt/slug em post humano publicado; sistema registra (log REVISAO LIBERADA) + BACKUP AUTOMÁTICO do estado anterior (meta `_cafezinho_backups_conteudo` base64 cap 20). Seguem travados: delete/trash, metas da casa, capa, mudança de taxonomia, ordens explícitas (30/09). Post 271172 (Dino vista 4-3) aplicado sob a nova regra: título 75 chars + 15§ + 5 h3 + slug novo (antigo 301), 0 travessões. 🔴 Lição WP: meta via wp-cli perde backslashes → JSON em meta = base64. [Fórum](Foruns/forum_revisao_editorial_porta_claude_20260915.md#v2) + [Memória](Memorias/memoria_revisao_editorial_porta_claude_20260915.md).

- **17/09 10:5x — FIO DE DIVULGAÇÃO NO X (@ocafezinho) — seção nova p/ fios de 2 tweets:** tweet 1 = emoji temático + título caixa alta + abertura da matéria (~1,2k chars, Long Post Premium) + capa og:image da matéria anexada; tweet 2 = reply com chamada + link (o card do X puxa a capa sozinho). Credenciais no cofre unificado (`Outros/chaves/agentes_labs/.env.unificado`: X_API_KEY/X_API_KEY_SECRET/X_ACCESS_TOKEN/X_ACCESS_TOKEN_SECRET; token OAuth1 só ESCRITA — get_users_tweets 401, create_tweet OK). Molde: `scratch/post_x_gilmar_mendonca.py` (família post_x_*/publish_twitter_*). Confirmação pública: oembed c/ `curl -sL`. 1º do formato: matéria Gilmar Mendes x Mendonça [Fórum](Foruns/forum_publicacao_fio_x_gilmar_mendonca_20260917.md).

- **17/09 11:3x — ESTEIRA DE FIOS 10x/DIA NO AR (X + Facebook):** tencent `/home/ubuntu/cafezinho/redes/fios_diarios.py` — 10 slots/dia (08:00/09:30/10:30/11:30 · 13:30/15:00/16:30/18:00 · 20:00/21:30, tag # FIOS_REDES, fuso BRT): análise editorial automática (categoria+frescor+views FAROL 6h+diversidade, corte 60, capa obrigatória, sem repetir slug por 48h) → fio X de 2 tweets (texto maior+capa, reply c/ link) + post FB c/ link no 1º comentário. Batismo 17/11:35 AtlasIntel nas 2 redes. Pausar: `touch redes/PAUSA`. [Fórum](Foruns/forum_esteira_fios_redes_10xdia_20260917.md) + [Memória](Memorias/memoria_esteira_fios_redes_10xdia_20260917.md).

## 📮 Substack — publicação via API (pesquisa 17/09/2026)

- **Veredito:** API oficial NÃO publica (só leitura de perfis; ToS jan/2026). Publicação programática possível via API interna não documentada + lib não-oficial `python-substack` (ma2za, PyPI, MIT, 175★, ativa 11/09/2026): rascunho de Markdown → `drafts schedule --at` → `drafts publish [--no-send]`.
- **Auth:** NÃO existe "senha de aplicação" (conceito WP). Usar e-mail+senha da conta OU cookie de sessão `substack.sid` (`.env` COOKIES_PATH/COOKIES_STRING; mais confiável c/ captcha/magic-link; expira → renovar).
- **Estado:** pesquisa concluída, 0 implementado, aguarda "vai" + segredo no cofre. Fórum: `Foruns/forum_substack_api_pesquisa_20260917.md` · Memória: `Memorias/memoria_substack_api_pesquisa_20260917.md`.
