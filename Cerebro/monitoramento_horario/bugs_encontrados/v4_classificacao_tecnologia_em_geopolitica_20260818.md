# V4-CLASSIFICACAO-2 — Tecnologia entrando no bloco GEOPOLÍTICA (aviso Miguel 18/08)

**Tag:** V4-CLASSIFICACAO
**Achado por:** Miguel ("esse aqui é tecnologia. quem fez isso e porque errou?") — post 266468.
**Status:** 🟢 RESOLVIDO estruturalmente 18/08 ~13:50 (post recategorizado + 2 patches + gates) — ver `Foruns/forum_v4_gate_tema_geopolitica_tecnologia_20260818.md`.

## Sintoma
Post 266468 "Demanda por inteligência artificial dispara preço do fosfeto de índio" (pauta de tecnologia) publicado como Geopolítica (cat 5003) — imagem-espelho do bug 0315 (geo no bloco Tecnologia).

## Causa
1. `config_editorial.py`: feed **News GERAL do SCMP** (rss/91) cadastrado na seção geopolitica — trazia tech/negócios/esporte.
2. `v4_vertical_intake.py`: seção geopolitica SEM gate de tema (diferente da tecnologia, que tem nexus ≥4).

## Correção (18/08, backups .bak_pre_*)
1. Post 266468 → cat `30 Tecnologia` (única) + primary 30.
2. Feeds: geopolitica rss/91→rss/4 (China); tecnologia rss/4 removido.
3. Intake: gate tech `title_tech>0` (fecha pendência do bug 0315) + veto `off_theme_title_veto` na geopolitica (fail-open; v1 de exigência de nexo SOBREREJEITOU 77 legítimas — revertida; lição registrada).
4. Backlog geopolitica: 6 vetadas, 234 legítimas preservadas.
