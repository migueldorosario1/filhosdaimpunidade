#!/usr/bin/env python3
# patch_sol_painel.py — insere a página ☀️ SOL no painel_cctv_v6.py (Tencent)
# Protocolo: âncoras únicas ou ABORTA ruidosamente; backup .bak_sol_20260901 antes.
# Ordem do Miguel 01/09/2026: "página no CCTV, como tenho GA4, FAROL, etc."
import pathlib, shutil, sys

ARQ = pathlib.Path("/home/ubuntu/cafezinho/v6/painel_cctv_v6.py")
src = ARQ.read_text(encoding="utf-8")

NAV_ANCORA = '    ("/v6/lumina", "🌙 LUMINA", "lumina"),\n'
NAV_NOVO   = NAV_ANCORA + '    ("/v6/sol", "☀️ SOL", "sol"),\n'

ROT_ANCORA = '    "/lumina": pagina_lumina,\n'
ROT_NOVO   = ROT_ANCORA + '    "/sol": pagina_sol,\n'

BLOCO = '''# ============================================================================
# ☀️ SOL — 4º contador do Cafezinho (WP Statistics no us65) — ordem do Miguel
# 01/09/2026: "página no CCTV, como tenho GA4, FAROL, etc." · coordenação:
# Foruns/forum_sol_painel_cctv_20260901.md (commit 5bbdd153d) · batizado SOL:
# constelação GA4 · FAROL · LUMINA · SOL (Umami cancelado — repetia a Lumina).
# Fonte: endpoint privado controle.ocafezinho.com/sol_cctv.php (token: sol_token).
# ============================================================================
def sol_dados() -> dict:
    c = _cache_get("sol_serie", 300)
    if c:
        return c
    try:
        tok = Path("/home/ubuntu/cafezinho/v6/sol_token").read_text().strip()
        j = _fetch_json(f"https://controle.ocafezinho.com/sol_cctv.php?k={tok}&fmt=json", timeout=15)
        d = {"online": int(j.get("online", 0)), "hoje": int(j.get("hoje", 0)),
             "total": int(j.get("total", 0)), "pico30": int(j.get("pico30", 0)),
             "media30": j.get("media30", 0),
             "dias30": [{"data": p.get("data", ""), "views": int(p.get("views", 0))} for p in j.get("dias30", [])],
             "meses12": [{"data": m.get("data", ""), "views": int(m.get("views", 0))} for m in j.get("meses12", [])]}
        _cache_set("sol_serie", d)
        return d
    except Exception as e:
        s = _cache_get_stale("sol_serie")
        if s:
            return s
        return {"online": 0, "hoje": 0, "total": 0, "pico30": 0, "media30": 0,
                "dias30": [], "meses12": [], "erro": str(e)}

def pagina_sol() -> str:
    d = sol_dados()
    linhas = "".join(
        f'<tr><td>{html.escape(p["data"])}</td><td style="text-align:right">{p["views"]}</td></tr>'
        for p in sorted(d["dias30"], key=lambda p: p["data"], reverse=True)[:14])
    meses = "".join(
        f'<tr><td>{html.escape(m["data"])}</td><td style="text-align:right">{m["views"]}</td></tr>'
        for m in d["meses12"][::-1])
    aviso = ""
    if d.get("erro"):
        aviso = f'<div class="alerta">⚠️ Fonte SOL indisponível agora: {html.escape(d["erro"])}</div>'
    elif len(d["dias30"]) < 8:
        aviso = ('<div class="alerta alerta-warn">📊 SOL nasceu em 01/09/2026 — os gráficos ligam sozinhos '
                 'ao acumular 5–8 dias de dados; os números e o histórico abaixo já estão ao vivo.</div>')
    conteudo = f"""
  <div class="stats">
    <div class="stat"><div class="v">{_fmt_int(d["online"])}</div><div class="l">Online agora</div></div>
    <div class="stat"><div class="v">{_fmt_int(d["hoje"])}</div><div class="l">Visitas hoje</div></div>
    <div class="stat"><div class="v">{_fmt_int(d["total"])}</div><div class="l">Visitantes total</div></div>
    <div class="stat"><div class="v">{_fmt_int(d["pico30"])}</div><div class="l">Pico diário 30d</div></div>
    <div class="stat"><div class="v">{d["media30"]}</div><div class="l">Média diária 30d</div></div>
  </div>
  {aviso}
  <div class="card"><h2>☀️ Visitas por dia — últimos 30 dias</h2>{svg_linha(d["dias30"])}</div>
  <div class="card"><h2>Visitas por dia (barras)</h2>{svg_barras(d["dias30"], 30)}</div>
  <div class="card"><h2>Histórico — últimos 14 dias</h2>
    <table class="tbl"><tr><th>Dia</th><th style="text-align:right">Visitas</th></tr>{linhas}</table></div>
  <div class="card"><h2>Visitas por mês — últimos 12 meses</h2>
    <table class="tbl"><tr><th>Mês</th><th style="text-align:right">Visitas</th></tr>{meses}</table></div>
  <div class="alerta">☀️ SOL = WP Statistics (us65) · contando desde 01/09/2026 · Constelação: GA4 · FAROL · LUMINA · SOL · invisível no site público (ordem do Miguel)</div>"""
    return chrome("☀️ SOL — Contador do Cafezinho", "sol", conteudo)

'''

ROT_DEF_ANCORA = "ROUTES = {\n"

# — Validações: âncoras únicas, senão aborta sem tocar em nada —
for nome, a in (("NAV", NAV_ANCORA), ("ROUTES-linha", ROT_ANCORA), ("ROUTES-dict", ROT_DEF_ANCORA)):
    n = src.count(a)
    if n != 1:
        sys.exit(f"ABORTADO: âncora {nome} aparece {n}x (esperado 1) — arquivo mudou, reavaliar.")

if '"/sol"' in src or "pagina_sol" in src:
    sys.exit("ABORTADO: SOL já parece presente no arquivo — nada a fazer.")

shutil.copy2(ARQ, ARQ.with_name("painel_cctv_v6.py.bak_sol_20260901"))
novo = src.replace(NAV_ANCORA, NAV_NOVO, 1)
novo = novo.replace(ROT_DEF_ANCORA, BLOCO + ROT_DEF_ANCORA, 1)
novo = novo.replace(ROT_ANCORA, ROT_NOVO, 1)
ARQ.write_text(novo, encoding="utf-8")
print("PATCH OK: NAV + ROUTES + bloco sol_dados/pagina_sol inseridos (backup .bak_sol_20260901)")
