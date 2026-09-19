# 🧭 MAPA DE SINAIS — Autoria dos posts do Cafezinho (quem fez o quê)

> **Documento vivo** (sprint 22/08/2026 — ordem do Miguel: "mapa de sinais para a gente sempre saber identificar quem fez o quê").
> Alimentado por: `wp_posts`/`wp_postmeta` + meta `_cafezinho_origem` (mu-plugin `cafezinho-origem-post.php`, desde 22/08/2026) + endpoint **`GET /wp-json/cafezinho/v1/autoria`** (canônico, auth por app password "Integracoes-Autoria").
> Consumidores: **Painel CCTV → /v6/autoria** · **Baleia Azul → seção "🧭 Quem fez o quê"** anexada a cada envio (08:00 e 19:30).

## 1) Tabela-mestre de sinais

| Fluxo | Conta WP (author_id) | Meta de pipeline | Origem técnica (`_cafezinho_origem`) | Sinais extras |
|---|---|---|---|---|
| **V4 — agentes temáticos** | 5786 "Redação" (Redacao nova, cafezinhov4@gmail.com) | `zizi_job_id` = `v4d_<vertical>_<hash>` | wp-cli/cron (interno, sem access log) | Espelho usa conta 5470 (posts 400xxx); draft V4 pode ser PUBLICADO depois por outro fluxo (REST) — a meta v4d_ raiz prevalece |
| **Agente YouTube** | 5786 | `cafezinho_nomes_check` (JSON com `video_id`) | REST/wp-cli | embed de YouTube no conteúdo |
| **Motor V5 / esteira LAURA-AGY** | pool: **5786** (sem zizi, sem nomes_check) · **5742** migueldorosario · **5785** miguelpublicador · **5470** | — (não grava meta própria) | wp-cli/cron interno | slots de 30 min (:00/:30); confirmação no ledger `ponte_laura_completa/ledger/agy_laura.md`; **não confundir 5742/5785 com o Miguel humano** |
| **Miguel — via Antigravity CLI / Manus** | **5786** ou **2018** (quando o payload assina `author=2018`) | — | `via=rest` + **UA `…Antigravity/1.0`** (Windows) | IP 190.89.239.244/.31 = front-proxy do provedor (TODAS as conexões externas chegam por eles — **IP não identifica**) |
| **Miguel — manual (wp-admin)** | 2018 James2017 (migueldorosario@gmail.com) | — | `via=admin` | conta histórica com 10 mil+ posts |
| **Gabriel Barbosa** | **5780** redator2 (migueldorosario5@gmail.com — principal, colunas analíticas) · **5735** gabrielbarbosa9001 (notas curtas) · 5774/5784 ociosas | — | `via=admin` (quando manual) | ⚠️ 4942 (ydb9111999) NÃO é Gabriel (erro de fórum antigo) |
| **Repetidor estatal** | 5470 "Redator" (editordocafezinho@gmail.com) | — | wp-cli/interno | notícias gerais curtas; 5470 também serve ao pool V5 e ao espelho |
| **Claude nuvem (Miguel)** | a confirmar | — | `via=rest`, UA ≠ Antigravity (registrado a partir de agora) | ver `sinais` na API/rodapé do painel |

## 2) Árvore de decisão (a ordem importa)

1. `zizi_job_id` começa com `v4d_` → **V4** (mesmo que outro fluxo tenha publicado).
2. Existe `cafezinho_nomes_check` → **Agente YouTube**.
3. `_cafezinho_origem.via=rest`:
   - UA contém `Antigravity` → **Miguel via Antigravity CLI/Manus** (se author=2018: "assinado como Miguel").
   - UA `Mozilla/5.0` puro etc. → publicação REST da casa (loop/motor) — ver sinais.
4. `_cafezinho_origem.via=admin` → humano manual: 2018=Miguel · 5780/5735=Gabriel · outros=autor externo.
5. `_cafezinho_origem.via=wp-cli|cron` interno → **Motor V5/esteira** (autores do pool) ou worker V4 (já peguei no passo 1).
6. **Sem `_cafezinho_origem` (posts anteriores a 22/08/2026)** → mapa histórico: Gabriel (5780/5735) · Miguel (2018, confirmar ferramenta no access log) · pool V5 (5742/5785) · repetidor (5470) · 5786 pós-20/08 sem zizi = Motor V5 (confirmar ledger).

## 3) Como consultar

- **Painel**: `https://<cctv>/v6/autoria` (janelas 6h–168h; cards por classificação + tabela com sinais).
- **Baleia Azul**: seção "🧭 Quem fez o quê" no fim de cada boletim (e-mail 08:00 + Telegram 19:30).
- **API**: `curl -u "Redacao nova:<app password Integracoes-Autoria>" "https://www.ocafezinho.com/wp-json/cafezinho/v1/autoria?horas=24&limite=100"` (`&fmt=md` → campo `md` com tabela pronta). Credenciais nos cofres (`AUTORIA_*`): `.env.unificado` (Dell ×2) + `.wp_creds` (Tencent).
- **Na mão (SQL)**: ver queries no fórum `forum_mapa_autoria_posts_v4_v5_humanos_20260821.md`.

## 4) Lacunas e recomendações

1. **Pré-22/08 é forense, pós-22/08 é sinal gravado** — a meta `_cafezinho_origem` só existe daqui pra frente (posts antigos seguem pelo mapa histórico).
2. **Manus e Antigravity CLI compartilham o UA** `Antigravity/1.0` (o Manus atua por dentro do Antigravity) — se o Miguel quiser distinguir por ferramenta, criar app passwords separadas por ferramenta e/ou usar contas autorais distintas (aí o sinal passa a ser o usuário autenticado).
3. **Motor V5 não grava meta própria** — recomendação pendente: publicador da esteira gravar `motor=v5` no post (tornaria o passo 5 da árvore inequívoco sem depender da conta).
4. IPs do access log **não identificam cliente** (front-proxy do provedor concentra tudo em 190.89.239.244/.31) — o sinal é UA + usuário autenticado.

## 4.5) ✏️ Correção manual (Miguel, 22/08)

- **Onde:** subpáginas do CCTV (`/v6/autoria/<grupo>`) — coluna "✏️ corrigir" em cada linha (select: Miguel/Gabriel/V4/Motor V5/YouTube/Repetidor/Humano/Outro/auto).
- **Como gravado:** meta `_cafezinho_autoria_manual` (+`_audit` quem/quando) no post — **sobrepõe a classificação automática**; "auto" limpa e volta o automático.
- **API:** `POST/DELETE /wp-json/cafezinho/v1/autoria/<id>` com body {rotulo} (auth app password Integracoes-Autoria).
- Rótulo corrigido aparece como "X (corrigido manual)" e entra no grupo normal da subpágina.

## 5) Manutenção

- Mu-plugin: `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-origem-post.php` (classificação em `cafezinho_classificar_autoria()` — nova regra de fluxo = editar ali).
- Painel: `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (`pagina_autoria()`; backup `.bak_pre_autoria_20260822`).
- Baleia: `/home/migueldorosario/bin/enviar_baleia_azul_ponte.sh` passo 3.5 (backup `.bak_pre_autoria_20260822`).
- Sprint de origem: fórum `forum_mapa_sinais_integracoes_baleia_cctv_20260822.md` + memória técnica idem (22/08/2026).
