# Memória — Mapa de Sinais de autoria: implementação técnica (22/08/2026)

**Sprint:** ordem Miguel "mapa de sinais para sempre identificar quem fez o quê + Baleia Azul + Painel CCTV". Fórum: `Foruns/forum_mapa_sinais_integracoes_baleia_cctv_20260822.md`. Documento vivo: `Foruns/MAPA_SINAIS_AUTORIA_CAFEZINHO.md`.

## Arquivos tocados (todos com backup)

| Arquivo | Mudança | Backup |
|---|---|---|
| canônico `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-origem-post.php` | NOVO — hook `wp_insert_post` grava `_cafezinho_origem` (via+ua+user+ts, só na criação, só posts); `cafezinho_classificar_autoria()` regras; rota REST `cafezinho/v1/autoria` (permission `edit_posts`, cache transient 60s, `fmt=md` devolve `{"md":...}`) | arquivo novo (rollback = remover) |
| Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` | NAV + `autoria_dados()` (basic auth lendo `AUTORIA_*` do `.wp_creds`, cache 300s, stale-soft) + `pagina_autoria()` (cards/tabela/filtros 6-168h) + rota `/autoria` no dispatcher | `painel_cctv_v6.py.bak_pre_autoria_20260822` |
| Dell `~/bin/enviar_baleia_azul_ponte.sh` | passo 3.5: curl API `fmt=md` → extrai `.md` via python → appenda ao boletim (fail-soft) | `.bak_pre_autoria_20260822` |
| Cofres `.env.unificado` (Dell ×2) + `.wp_creds` (Tencent) | `AUTORIA_API_URL/AUTORIA_WP_USER/AUTORIA_WP_PASS` | `.bak_pre_autoria_20260822` em cada |
| canônico `/root/.autoria_apppass` | app password "Integracoes-Autoria" (600) | — |

## Comandos/provas

- Endpoint: sem auth → 401; com app password → 200 (`n=8` classificados corretamente). `wp transient delete --search=autoria_api_` após o fix do fmt=md.
- Meta origem: teste wp-cli → `{"via":"wp-cli","ua":"","user_id":0}`; teste REST UA custom → `{"via":"rest","ua":"Antigravity/1.0 TESTE","user_id":5786}`; posts de teste deletados (267046/267047).
- CCTV: `systemctl restart cctv-v6` → active; `/autoria?horas=24` → 200; janela 48h mostrou V4/Motor V5/Gabriel/Miguel classificados.
- Baleia: `bash -n` OK; curl Dell→API→`json.load().md` → tabela markdown limpa.
- Gotchas: (1) Python 3.10 do Dell não compila o painel (sintaxe 3.12) → validar no Tencent com `compile()`; (2) `py_compile` no /tmp do Tencent dá EACCES em `__pycache__` → usar `python3 -c "compile(...)"`; (3) WP REST envelopa string em JSON — nunca retornar markdown cru como data; (4) `wp user application-password` não tem `revoke`, é `delete`; `--porcelain` imprime a senha no stdout → SEMPRE redirecionar direto para arquivo; a 1ª senha vazou no terminal e foi revogada/recriada.

## Forense access log (fatos)

- Log certo: `/var/log/nginx/access.ocafezinho.com.log` (não `access.log`, não o do vhost controle).
- Fronts do provedor concentram TODO tráfego externo em 190.89.239.244/.31 → IP inútil p/ identificar; UA + basic user são o sinal.
- 267017 (dívida externa, "meu de verdade"): 02:57 22/08, REST UA `Antigravity/1.0`, `author=2018` no payload — Miguel via Manus.
- 266991 (Datafolha): criado 22:43 21/08 SEM access log = interno wp-cli (mesma via do motor V5); edição 03:25 também interna.
- 142 ações POST/PUT do Antigravity/1.0 em 48h (1ª vista no log atual: 22/08 00:27).
