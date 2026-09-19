---
name: project-cafezinho-news-sync-horario-20260703
description: Sync horário cafezinho.news ← Cafezinho canônico ATIVO 03/jul 12:57 BRT — cron 17 * * * * no droplet 159.65.177.60
metadata: 
  node_type: memory
  type: project
  originSessionId: 3b16bc8e-faad-4476-b629-4bf5b27bdd35
---

Sync horário do espelho `cafezinho.news` a partir do Cafezinho canônico (`us65.serverdo.in`) **ATIVO** desde 2026-07-03 12:57 BRT.

**Why:** Miguel pediu 03/jul ~09:30 BRT: "quero ver o cafezinho.news espelhar o cafezinho". Decisões: 1h de frequência, NOVOS+EDITADOS (INSERT→REPLACE via `post_modified`), retenção crescente, roda no droplet (não no canônico), chave SSH dedicada com `from=` restriction, kill-switch, log+logrotate.

**How to apply:**

Arquivos operacionais (droplet `159.65.177.60`):
- `/root/sync_from_cafezinho.sh` — script principal (6764 B, chmod +x)
- `/root/.ssh/id_ed25519_sync_from_prod` — chave dedicada droplet→canônico (fingerprint `SHA256:4+xZ5Eq17HO2/H//MLu6GJe+LMX5fXy15Oah93F/i3o`)
- `/var/lib/cafezinho_sync/last_sync.txt` — state (cutoff atual)
- `/var/log/cafezinho_sync.log` — log com timestamp
- `/etc/logrotate.d/cafezinho_sync` — rotação weekly x8
- Cron root: `17 * * * * /root/sync_from_cafezinho.sh` (sentinela `SENTINELA_CAFEZINHO_NEWS_SYNC_CLAUDE_20260703`)
- Kill-switch: `touch /root/SYNC_PAUSED` no droplet → sync exit 0
- Lock: `flock` em `/var/run/cafezinho_sync.lock` (singleton)

No canônico (`us65.serverdo.in`):
- Chave pública appended em `/root/.ssh/authorized_keys` com `from="159.65.177.60"` restriction
- Backup: `/root/.ssh/authorized_keys.bak_pre_cafezinho_news_sync_20260703_095343`

Como monitorar:
```bash
ssh root@159.65.177.60 'tail -f /var/log/cafezinho_sync.log'
ssh root@159.65.177.60 'cat /var/lib/cafezinho_sync/last_sync.txt'
```

Como pausar/parar:
```bash
ssh root@159.65.177.60 'touch /root/SYNC_PAUSED'      # pausar (mantém cron)
ssh root@159.65.177.60 'crontab -e'                    # apagar linha SENTINELA_CAFEZINHO_NEWS_SYNC (parar de vez)
```

Sync inicial (12:50-12:56 BRT): 2231 posts modificados + 1694 uploads (169 MB) em 6 min. Espelho: 2357 → 3359 posts_publish. Muitas edições vieram porque agentes editoriais do canônico (autocura, observador) tocam posts constantemente.

Comportamento normal do sync horário: **~5-30 modificados/hora**, uploads leves (<10 MB), duração <30s.

Riscos vigentes (mitigados, mas conhecidos):
- `wp_postmeta.meta_value` com URLs `controle.ocafezinho.com` preservadas — search-replace SÓ toca colunas não-serialized (`post_content`, `guid`, `post_excerpt`) por segurança. Impacto real baixo (meta values raramente renderizados no frontend)
- Featured images de posts pré-30d editados podem quebrar (attachment antigo não veio no sync inicial) — fixável com sync full de uploads manual
- wp-cli no droplet corrompido pelo tema (imprime `<? function wp_bs_pagination` antes do output) — não afeta site, mas impede uso do `wp` como ferramenta
- Tabelas custom NÃO sincronizadas (podem causar desatualização visual): `wp_top_ten`, `wp_top_ten_daily`, `wp_wp_rp_tags`, `wp_responsive_menu`, `wp_useful_banner_manager_banners`. Baixo impacto — plugins fazem rebuild via cache. Se Miguel notar sidebar/related atrasados, avaliar caso a caso.

**Patch 04/07/2026 12:40 BRT:** adicionado sync SEMPRE de `wp_highlights` (tabela do tema `ocafezinho-portal` que define manchete `<h1>` da home). Antes ficava engessada porque script só rodava dumps se houvesse delta em `wp_posts`. Agora `wp_highlights` sincroniza como bloco separado no início (+2s por ciclo). Miguel reportou site desatualizado 12:33 BRT — na verdade só a manchete estava (posts recentes batiam). Fix imediato + fix permanente aplicados 12:36-12:39 BRT.

Relacionado: [[feedback-cafezinho-news-e-copia-nao-migracao]] (nomenclatura correta — é cópia diletante, não migração).

Fórum canônico completo: `Projeto Cafezinho Agentes/Foruns/forum_exercicio_copia_cafezinho_news_20260629.md` (seção "SYNC HORÁRIO ATIVO" ao final).
Snapshot Claude Code: `Projeto Cafezinho Agentes/Ponto de Retomada/Claude Code/20260703_125700_sessao.md`.
