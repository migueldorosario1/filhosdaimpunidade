# Memória — Painel V6: separação YouTube × Temáticos (18/08/2026)

**Sessão:** ZCode/DeepSeek — "PAINEL V6: YOUTUBE × TEMÁTICOS" (ZCodeProject) · 21:10–21:30 BRT

## Arquivos
- Servidor (produção): `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (Tencent, porta 8084, unit `cctv-v6`, usuário ubuntu).
- Cópia de trabalho local: `ZCodeProject/painel_v6_reforma/painel_cctv_v6_SERVIDOR_20260818_2110.py` (baixada ANTES de editar; md5 do vivo na hora do deploy = `025c098e…` = idêntico ao baixado → sem colisão com outra sessão).

## Mudanças no código
1. Nova função `_posts_video_yt_tematico(cfg, limite=8)` (após `_posts_tematico`): varre `sitemap-0.xml`, filtra `<loc>` com `/youtube-` que casa `post_re` do temático; título real via `<title>` da página do post (regex limpa sufixo `| Site`); fallback = slug. Cache `tem_videos_yt_<host>.json` 30min.
2. `pagina_tematicos()`: card novo "📰 Publicações nas últimas 24h" ANTES do grid — `hoje_s`/`ontem_s` em BRT (UTC−3) + loop `TEMATICOS` com `_posts_tematico(cfg,12)` filtrado por data (código movido da página YouTube).
3. `pagina_youtube()`: card antigo "Publicados nas últimas 24h" REMOVIDO. Novo "🎬 Últimos posts dos agentes YouTube": Cafezinho = REST `WP_API/posts?status=publish&categories=28&per_page=10&orderby=date&order=desc` (cache novo `yt_ult_caf.json` 600s — o `yt_pub24_caf.json` antigo ficou órfão); temáticos = loop fixo ("gsn","aiatolah","mapario") com `_posts_video_yt_tematico()` + notas fixas `_NOTAS_YT` (gsn=draft NYC; mapario=desativado 03/08).

## Deploy (comandos)
- `scp` edição → `/tmp/painel_test_yt_tem.py`; `PYTHONPYCACHEPREFIX=/tmp/pycache_ubuntu python3 -m py_compile` (o `__pycache__` de /tmp é de outro user — SEM o prefixo dá Permission denied; gotcha já conhecido); teste funcional por import (guarda `if __name__ == "__main__"` na linha ~4169) com asserts nas duas funções.
- Backup `cp -p painel_cctv_v6.py painel_cctv_v6.py.bak_pre_yt_tematicos_20260818` → `cp` da versão testada → `py_compile` → `sudo -n systemctl restart cctv-v6` → `is-active` = active.
- Provas: `/youtube` contém "Últimos posts dos agentes YouTube" e NÃO contém "Publicados nas últimas 24h"; `/tematicos` contém "Publicações nas últimas 24h"; nginx público HTTP 200 nas duas (36.870 e 26.473 bytes).

## Gotchas novos/confirmados
- Painel usa **Python 3.12** no servidor (f-string aninhado PEP 701 ~linha 3474) — `py_compile` LOCAL com 3.10 FALHA; validar SEMPRE no servidor.
- `_posts_tematico` depende de data no slug `YYYYMMDD`; posts sem data caem no fim da lista (não afeta o card da Central, que filtra por data).

Tema Duplo: `Foruns/forum_painel_v6_youtube_x_tematicos_pub_20260818.md` + esta memória.
