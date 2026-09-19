#!/usr/bin/env python3
"""RESTAURA as rotas do FAROL-MOKA no painel_cctv_v6.py (apagadas pela
regeneração do painel de 16/09) — versão com âncoras pós-regeneração."""
from pathlib import Path
import secrets, shutil

P = Path("/home/ubuntu/cafezinho/v6/painel_cctv_v6.py")
bak = str(P) + ".bak_pre_farolmoka2_20260916"
shutil.copy2(P, bak)
txt = P.read_text(encoding="utf-8")

FUNCS = '''
# ============================================================================
# FAROL-MOKA (15/09/2026, ordem Miguel: "bota um outro contador, o Farol, no
# Moka") — o mesmo Farol da casa medindo o MokaReader. O site vive na Vercel
# (sem access log); o pixel do app posta via relevo HTTPS do Cafezinho
# (mu-plugin cafezinho-farol-moka-relevo.php) para POST /api/moka-receber.
# Historico em V6_CACHE/moka_audiencia.jsonl (append, nunca apaga).
# (Restaurado em 16/09 ~12:4x: rotas apagadas pela regeneração do painel.)
# ============================================================================

def _moka_jsonl() -> Path:
    return V6_CACHE / "moka_audiencia.jsonl"


def _moka_token() -> str:
    _t = os.environ.get("MOKA_FAROL_TOKEN", "")
    if not _t:
        _f = Path("/home/ubuntu/cafezinho/v6_data/moka_token.txt")
        _t = _f.read_text(encoding="utf-8").strip() if _f.exists() else ""
    return _t


def moka_receber(body: dict, ua: str, ip: str) -> dict:
    if not isinstance(body, dict) or not body.get("v"):
        return {"ok": False, "erro": "payload sem campo v"}, 400
    ponto = {
        "gerado": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "v": str(body.get("v"))[:64],
        "path": str(body.get("path") or "/")[:200],
        "host": str(body.get("host") or "")[:100],
        "ref": str(body.get("ref") or "")[:200],
        "ua": (ua or "")[:300],
        "ip": (ip or "")[:64],
    }
    arq = _moka_jsonl()
    arq.parent.mkdir(parents=True, exist_ok=True)
    with arq.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ponto, ensure_ascii=False) + "\\n")
    return {"ok": True}, 200


BOT_UA = re.compile(r"bot|crawl|spider|slurp|headless|curl|wget|python|monitor|uptime|lighthouse", re.I)


def moka_resumo() -> dict:
    import collections
    arq = _moka_jsonl()
    pontos = []
    if arq.exists():
        for ln in arq.read_text(encoding="utf-8").strip().splitlines()[-20000:]:
            try:
                pontos.append(json.loads(ln))
            except Exception:
                pass
    agora = datetime.now()
    hoje_ini = agora.replace(hour=0, minute=0, second=0, microsecond=0)
    lim30 = agora - timedelta(minutes=30)
    lim24 = agora - timedelta(hours=24)

    def _dt(p):
        try:
            return datetime.strptime(str(p.get("gerado"))[:19], "%Y-%m-%d %H:%M:%S")
        except Exception:
            return None

    nav_hoje = 0
    vis_hoje = set()
    on30 = set()
    nav24 = 0
    serie = collections.Counter()
    for p in pontos:
        d = _dt(p)
        if not d:
            continue
        v = p.get("v")
        bot = bool(BOT_UA.search(p.get("ua") or ""))
        if d >= hoje_ini:
            nav_hoje += 1
            if not bot:
                vis_hoje.add(v)
        if d >= lim30 and not bot:
            on30.add(v)
        if d >= lim24:
            nav24 += 1
            serie[d.strftime("%H")] += 1
    return {
        "ok": True, "site": "moka", "gerado": agora.strftime("%Y-%m-%d %H:%M"),
        "hoje_navegacoes": nav_hoje,
        "hoje_visitantes_humanos": len(vis_hoje),
        "online_30min_humanos": len(on30),
        "navegacoes_24h": nav24,
        "serie_24h_por_hora": dict(sorted(serie.items())),
        "pontos_totais": len(pontos),
    }

'''

ancora_funcs = "def farol_coleta() -> dict:"
assert txt.count(ancora_funcs) == 1
txt = txt.replace(ancora_funcs, FUNCS + ancora_funcs, 1)

ROTA_POST = '''        if path in ("/api/moka-receber", "/v6/api/moka-receber"):
            if self.command == "OPTIONS":
                self.send_response(204)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Token")
                self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
                self.end_headers()
                return
            _q = parse_qs(parsed.query)
            _tok_dado = (_q.get("token", [""])[0] or self.headers.get("X-Token") or "").strip()
            if not _moka_token() or _tok_dado != _moka_token():
                _r, _st = {"ok": False, "erro": "token invalido"}, 403
            else:
                _r, _st = moka_receber(self._ler_json_body(), self.headers.get("User-Agent", ""), self.headers.get("X-Real-IP") or self.client_address[0])
            _b = json.dumps(_r, ensure_ascii=False).encode("utf-8")
            self.send_response(_st)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(_b)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            try:
                self.wfile.write(_b)
            except BrokenPipeError:
                pass
            return
'''
ancora_post = '        if path == "/api/audiencia-receber":'
assert txt.count(ancora_post) == 1
txt = txt.replace(ancora_post, ROTA_POST + ancora_post, 1)

ROTA_GET = '''        if path in ("/api/moka-resumo", "/v6/api/moka-resumo"):
            _q = parse_qs(parsed.query)
            _tok_dado = (_q.get("token", [""])[0] or self.headers.get("X-Token") or "").strip()
            if not _moka_token() or _tok_dado != _moka_token():
                return self._send_json({"ok": False, "erro": "token invalido"}, 403)
            return self._send_json(moka_resumo())
'''
ancora_get = '        if path in ("/api/farol-coletar", "/api/farol-backfill"):'
assert txt.count(ancora_get) == 1
txt = txt.replace(ancora_get, ROTA_GET + ancora_get, 1)

ancora_isen = 'if path in ("/api/audiencia-receber", "/v6/api/audiencia-receber", "/api/farol-por-hora", "/v6/api/farol-por-hora"):'
assert txt.count(ancora_isen) == 1, txt.count(ancora_isen)
txt = txt.replace(
    ancora_isen,
    'if path in ("/api/audiencia-receber", "/v6/api/audiencia-receber", "/api/farol-por-hora", "/v6/api/farol-por-hora", "/api/moka-receber", "/v6/api/moka-receber", "/api/moka-resumo", "/v6/api/moka-resumo"):',
    1,
)

P.write_text(txt, encoding="utf-8")
print("rotas FAROL-MOKA restauradas; backup:", bak)
