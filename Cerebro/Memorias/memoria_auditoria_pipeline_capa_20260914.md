# Memória Técnica — Auditoria causa raiz: pipeline de capa parado (12-14/09/2026)

**Autor:** ZM · ZCode/GLM-5.3 · 14/09/2026 ~14:0x BRT
**Ref:** ZM-20260914-003 · Fórum: `Foruns/forum_auditoria_pipeline_capa_parado_20260914.md` (seções 4, 9, 10.1)
**Encomenda:** CM-20260914-002 (prompt §8 do fórum). Prazo sugerido 07:45; prompt chegou ao ZM ~13:30, entregue ~14:10.

## 1. Conclusão em uma linha

O passo "capa" do V4.1 (`_thumbnail_id` + `_cafezinho_img_check` + agendamento) **nunca foi robô cronizado — era agente no loop via wp-cli/SSH (uploads autor user_id 0, ferramenta = scripts `/root/cl2NN.sh` do CL no servidor WP)**. A parada = **perda de operador** (CL silente 12/09 15:17; claudionor sem lotes após a série RJ 13/09 13:15-13:27), **não pane de infra** — gerador, REST, wp-cron, crons e gates todos sãos e comprovadamente vivos.

## 2. Fronteira corrigida (importante para o fórum)

- Primeiro draft V4.1 SEM capa: **270419, criado 12/09 22:57** (não 270603/13/09 16:57 como na abertura do fórum).
- Último attachment wp-cli autor-0 (o canal das capas): **270563, 13/09 13:27:39** (capa do 270557, série RJ).
- Último publish: 270557 13/09 15:44 (future da série RJ; série manual, não esteira).
- Última ferramenta do CL no servidor: `cl277_body.sh` 11/09 18:07, `cl_funcs.sh` 12/09 02:14, `backups_cl/` 12/09 05:36. CL state file: última escrita 12/09 15:17 (CL-20260912-011); voltou 14/09 13:11 "modo sombra" (CL-20260914-001/002).

## 3. Provas por hipótese

| Hipótese | Veredito | Prova principal |
|---|---|---|
| H1 gerador sem crédito/key | ❌ REFUTADA | Fluxo IA `cafezinho-<hash>` (REST, autor 5470, 2h/2h, ~:07) VIVO até 270805/270806 de 14/09 13:07; **órfão de `_thumbnail_id` em toda amostra 08/09→hoje** = nunca foi o canal das capas V4.1. Gap único 13/09 05:07→15:07, recuperou sozinho. GL (`estado/grok_laura.md`) parado desde 28/08 — anterior ao período funcional. |
| H2 cron/daemon morto | ❌ REFUTADA | WP-CRON 1MIN no ar (root crontab us65); sonda gate E5 gera 2 posts de teste/trash a cada 15min até 14/09 16:37 UTC; esteira cria drafts às :56/:57 de 2h/2h via REST (270711 em 14/09 04:27). Não existe cron de capa — nunca existiu. |
| H3 AL regressão | ❌ REFUTADA | AL (AGY-LAURA) viva: heartbeats 30/30 ininterruptos AL-958 (13/09 14:05)→AL-1008 (14/09 13:05); state file 14/09 13:30. CHECK de 13/09 já registrava `fila_v41_drafts..._publish0_aguardando_decisao_miguel` — ela sabia e aguardava ordem (ofício ≠ publicar solo). |
| H4 claudionor/CL parou | ✅ CAUSA RAIZ | Evidências da seção 2 + cadeia abaixo. |
| H5 App Password expirou | ❌ REFUTADA | REST autenticado operante (drafts criados até 14/09; AGY-M publicando com capa 14/09 13:37). `debug.log` = 22 GB **inerte desde 14/07** (WP_DEBUG off) — nada de 401/403 a analisar. |

Hack 13/09 (espelho DO): irrelevante — só o espelho; canônico auditado intacto; parada de capas já existia desde 12/09 à noite.

## 4. Comandos que geraram as provas (receita)

```bash
# who criou cada post (origem plugin casa)
wp db query "SELECT p.ID,p.post_date,p.post_status,p.post_author,SUBSTRING(IFNULL(m.meta_value,'-'),1,130)
 FROM wp_posts p LEFT JOIN wp_postmeta m ON m.post_id=p.ID AND m.meta_key='_cafezinho_origem'
 WHERE p.post_type='post' AND p.post_date_gmt >= '...'" --skip-column-names --allow-root
# attachments por autor/título (padrões: cafezinho-<hash>=REST 5470; autor 0=wp-cli/SSH do CL; 5786=vídeo; 5735=Android)
wp db query "SELECT p.ID,p.post_date,p.post_author,SUBSTRING(p.post_title,1,55) FROM wp_posts
 WHERE p.post_type='attachment' AND p.post_date >= '...'" --allow-root
# vínculo de capa (quem usa o attachment)
SELECT ... (SELECT GROUP_CONCAT(pm.post_id) FROM wp_postmeta pm WHERE pm.meta_key='_thumbnail_id' AND pm.meta_value=p.ID)
# scripts do CL no servidor
ls -lat /root/*.sh | head    # cl2NN.sh param em 11-12/09
# access REST da esteira: vhost CONTROLE (não www!), atrás de Cloudflare, fuso -0300
grep -a '13/Sep/2026:16:57' /var/log/nginx/access.controle.ocafezinho.com.log.1 | grep wp-json
```

## 5. Armadilhas encontradas (poupam a próxima auditoria)

1. **wp-cli em loop no servidor exige `--allow-root`** — sem ele falha em silêncio (variável vazia ≠ meta vazia).
2. `wp db query` via SSH: usar `ssh host 'bash -s' <<'EOF'` com aspas simples no SQL; aspas duplas escapadas quebram sintaxe MySQL (Erro 1064).
3. Access log do canônico: API REST da esteira chega pelo vhost **controle.ocafezinho.com** (www não registra) e o IP de origem é Cloudflare (162.158/172.70/104.23) — identificar caller só por padrão de tempo/UA.
4. **wp-cli NÃO gera access log** (roda direto no servidor) — a via do CL é invisível no nginx; visível em `/root/*.sh` + `auth.log` (rajadas SSH da chave id_rsa do Dell, IPs dinâmicos Vivo).
5. `debug.log` do WP: 22 GB e sem escrita desde 14/07 — inútil para auditoria recente.
6. Drafts V4.1 têm `post_date_gmt = 0000-00-00` — filtrar por GMT os exclui; usar `post_date` (fuso site -03) ou meta `_cafezinho_origem.ts`.
7. Posts da série RJ (270550-57) são fluxo MANUAL — não misturar com a esteira V4.1 na hora de datar fronteiras.
8. Pares de posts trash 8/hora no banco = sonda gate E5 (teste robô 5470 + humano 2018 a cada 15min) — normal, não é ataque nem bug.

## 6. Estado na entrega (14/09 ~14:05 BRT)

- Destravamento AGY-M Lote 1 verificado ao vivo: 270532 publish 13:37 com capa 270809 + imgcheck ok; 270603 future 14:00 e 270582 future 14:22 com capas 270823/270824 + imgcheck ok; descartes 269021/270646/270711 ok.
- Fix de máquina: NENHUM aplicado — corretamente (nada quebrou).
- Pendência estrutural (Miguel decide): (a) cronizar capa consumindo os `cafezinho-*` 2h/2h hoje 100% órfãos (ativo pago desperdiçado); (b) rodízio formal do posto capador; (c) status quo manual. ➕ alerta de fila: draft V4.1 >6h sem thumb → ping na ponte.

## 7. O que falta / próximos passos

- Miguel: escolher a opção estrutural (a/b/c) do §6.
- CM/CL: definir quem segura o posto capador até a decisão (hoje = AGY-M manual por lotes com CHECK CM).
- Futuro: se cronizar (a), especificar revisão de visão automatizada (img_check sem agente) — mexe em gate §86/Emenda 7, exige fórum próprio.

## 8. Pé de resposta à opção (b) — ALERTA DE FILA V4.1 IMPLEMENTADO (14/09 15:2x, ZM-20260914-004)

Autorização Miguel 14/09 14:2x (via CM-20260914-006). No ar no cafezinho-wp:

- **Script** `/root/alerta_capa_v41.py` v1.3 + **cron root `*/30`** com `flock -n /tmp/alerta_capa_v41.lock`, log `/var/log/alerta_capa_v41.log`. Modos `--dry-run` e `--self-test`.
- **Detecção** (SQL wp db query): draft + `_v4_versao=4.1` + `_thumbnail_id` vazio/0/NULL + post_date <=72h + autor≠2018 + NOT EXISTS hold/descartado_velharia/reprovado/canibalizado + série ordem>1 fora. Idade calculada em BRT (-03) contra `post_date` (fuso do site).
- **Níveis:** 1 (>=6h) bloc `ALERTA-CAPA-V41-YYYYMMDD-HHMM` na ponte; 2 (>=12h OU fila>=5) + Telegram `@pontecafezinhobot` (creds por NOME em `/root/.env.unificado`: `TELEGRAM_TOKEN_PONTE`/`PONTE_CHAT_ID`).
- **Rate-limit:** 3h/draft (ledger `/root/agent_data/alerta_capa_v41/ledger.jsonl`, persiste reboot diário 03:31 UTC); teto 4/dia nível-1; nível-2 sem teto; auto-silêncio ao ganhar capa/ser descartado/trash.
- **Publicação git:** worktree dedicado `/root/cerebro_alerta_wt` (detached origin/main, push HEAD:main) — não toca no clone principal do DSH; ciclos fetch→reset→regen→commit→push ×3 (30s/60s); falha final → diferidos persistentes + Telegram; sentinela cron >2h → meta-alerta; WP caído = silêncio.
- **Ledger de auditoria:** `cerebro/monitoramento_horario/alertas_capa_v41/YYYY-MM-DD.jsonl` (pushado junto).
- **Validação:** dry-run fila real → self-test push OK → **1º alerta legítimo 15:22:41 nível-2** (bloc + Telegram + ledger push_git_ok=true) → 2º ciclo silenciado pelo cooldown ✓.
- **Armadilhas novas (v1.0→v1.3):** reset --hard descarta commits locais do worktree E remove dirs que só existiam neles (regens recriam dir com makedirs); push rejeitado quando DS YouTube pusha entre fetch e push (tratado refetchando por ciclo); credential store git compartilhado com carteiro → lock ~1s transitório, retry resolve.
- **Achado de passagem:** main LOCAL do clone `/root/Cerebro` (carteiro DSH) preso em 06/09, ahead 2 (AVISO ANTI-COLISÃO/RESPOSTA DSC nunca pushados) — reportado, não mexido.
- **Fila real 14/09 15:22 = 9 drafts** (não 5): inclui 270268/270389/270401 de 12/09 anteriores à janela 22:57 dos «11». Tabela completa no bloc ALERTA-CAPA-V41-20260914-1522.
