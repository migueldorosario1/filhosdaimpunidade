# Memória técnica — Esteira de fios X+FB 10x/dia (17/09/2026, ZCode/GLM-5.3)

Log completo de implementação. Fórum de decisões: `Foruns/forum_esteira_fios_redes_10xdia_20260917.md`.

## Ambiente

- Servidor: tencent (ubuntu via ssh; sudo disponível — `sudo -n true` OK). Fuso America/Sao_Paulo → cron em hora BRT direto.
- tweepy 4.16.0 já presente no python3 do servidor. FB via urllib puro (Graph API v21.0).

## Arquivos criados/modificados

- `tencent:/home/ubuntu/cafezinho/redes/fios_diarios.py` — motor completo (~340 linhas): coleta WP REST (`/wp-json/wp/v2/posts?per_page=30&_embed=1`), FAROL (`v6_data/farol_por_hora.json`, formato {slug: {"AAAA-MM-DD HH": views}}), score editorial, estado, publicação X (tweepy v1 media_upload + v2 create_tweet/reply) e FB (`/{page}/photos` + `/{post_id}/comments`).
- `tencent:/home/ubuntu/cafezinho/redes/.env_redes` — 7 chaves (X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET, X_BEARER_TOKEN, FB_PAGE_ACCESS_TOKEN, FB_PAGE_ID), 600 ubuntu. Extraído com sudo de /root/.env.unificado (sem transitar valores pela rede).
- Crontab ubuntu do tencent: +10 linhas tag `# FIOS_REDES` (08:00/09:30/10:30/11:30/13:30/15:00/16:30/18:00/20:00/21:30), backup prévio em /tmp/cron_backup_20260917.txt (tencent).
- Cofres (5) com token FB novo + backups `.bak_pre_fb_engagement_20260917`.
- Local: `scratch/post_x_gilmar_mendonca.py` (fio manual do Gilmar).

## Comandos-chave (para operar)

```bash
# dry-run (mostra ranking + texto do escolhido, não publica)
ssh tencent "cd /home/ubuntu/cafezinho/redes && python3 fios_diarios.py --dry-run"
# pausar a esteira
ssh tencent "touch /home/ubuntu/cafezinho/redes/PAUSA"
# religar
ssh tencent "rm /home/ubuntu/cafezinho/redes/PAUSA"
# auditoria do dia (textos + links publicados)
ssh tencent "cat /home/ubuntu/cafezinho/redes/fios_textos_\$(date +%F).json"
# ver cron
ssh tencent "crontab -l | grep FIOS_REDES"
```

## Erros e curas (para não repetir)

1. `dateGmt` não existe no REST do WP → campo é `date_gmt` (fallback `date` tratando BRT=UTC−3).
2. `urllib.request.urlretrieve` sem UA toma **403 da borda do ocafezinho** (Cloudflare bloqueia Python-urllib) → sempre Request com User-Agent de navegador (função baixar_capa). FB não sofre porque o Graph baixa a URL da capa por conta própria.
3. Comentário como página exige `pages_manage_engagement` no page token (erro 403 #200 sem ela). Publicar foto exige só pages_manage_posts.
4. Verificar validade de token FB sem app secret: `GET graph.facebook.com/oauth/access_token_info?access_token=TOKEN` → campo expires_at (0 = nunca expira).
5. Editor de texto do Miguel salva com BOM UTF-8 → ler com `encoding="utf-8-sig"` ao receber tokens colados por ele.
6. crontab: comentário `#` no MEIO da linha engole o resto (incluindo redirecionamento de log) — marca de manutenção vai no FIM da linha, após o redirect.
7. oembed público para provar tweet no ar: `curl -sL` (sem -L fica no 301).
8. tencent root_copy pertence a root → atualizar com sudo; /root/.env e /root/.env.unificado também existem e FORAM atualizados (incidente de abril/2026 não se repete).

## Estado no fim da sessão

- Esteira no ar; batismo completo (AtlasIntel nas 2 redes: X 2100594844918034492 · FB 1601824175316876).
- Gilmar (fio manual do turno) semeados no estado.json → não repete por 48h.
- Próximo slot 13:30 escolheria OpenAI (106) no dry-run.
