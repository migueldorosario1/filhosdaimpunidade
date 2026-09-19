#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gera_seed_faxina.py — alimenta a página /v6/faxina do painel CCTV v6 (Tencent)
==============================================================================
Ideia do Miguel (08/09/2026): "cria uma página no painel cctv v6 com uma BARRA DE
PERCENTUAL mostrando a evolução da faxina e um MAPA dos diretórios."

Transporte (padrão us65 da /v6/reforma):
  Dell: este gerador escreve  ~/cerebro-miguel/.tencent_v6_oficina/faxina_dell_status_SEED.json
        e (--push) commita+empurra pro origin/main.
  Tencent: cron */7 sync_faxina_status.py faz git fetch + show origin/main:<seed>
        e instala /home/ubuntu/cafezinho/v6_data/faxina_dell_status.json
  Página: painel_cctv_v6_faxina.py lê o JSON (tolera ausente/velho — STALE 13h).

Fontes de dados (tudo local, sem rede):
  1. df /home                     → barra do disco
  2. LEDGER_APAGADOS.md (fila N*) → barra da missão (lotes concluídos/total)
  3. índice SQLite do buscador    → tamanhos do MAPA (dirs.path/size)
  4. faxina_mapa_curadoria.json   → status/obs/overrides do mapa + início + nuvem
  5. seed anterior (se existir)   → série histórica (append de ponto novo)

ÍNDICE DUPLO (ordem do Miguel 08/09: "o index de preferência é duplo"):
  6. espelho diário do DB        → gdrive:Backup_Total/dell_faxina/indice/ E b2:.../faxina/indice/
  7. CATALOGO_NUVEM.md legível   → lista o que há nas nuvens; commitado junto com a seed
                                   (o Cérebro já é espelhado = catálogo nasce triplo).

Uso:  python3 gera_seed_faxina.py [--push] [--quiet] [--sem-nuvem]
  --push = commit seletivo (seed + catálogo) + pull --rebase --autostash + push + prova no origin.
  --sem-nuvem = pula espelho do índice e catálogo (teste local rápido, sem rede).
Fail-soft: qualquer fonte que falhe vira campo ausente/None — a seed sempre nasce.
"""
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
LEDGER = AQUI / "LEDGER_APAGADOS.md"
CURADORIA = AQUI / "faxina_mapa_curadoria.json"
DB = Path.home() / ".local/share/buscador_local/indice.sqlite"
REPO = Path.home() / "cerebro-miguel"
SEED_REL = ".tencent_v6_oficina/faxina_dell_status_SEED.json"
SEED = REPO / SEED_REL
CATALOGO = AQUI / "CATALOGO_NUVEM.md"
CATALOGO_REL = "cerebro/Ferramentas/buscador_local/CATALOGO_NUVEM.md"  # no repo
ESPELHO_DESTINOS = ["gdrive:Backup_Total/dell_faxina/indice/",
                    "b2:failover-cafezinho1/faxina/indice/"]
HOME = str(Path.home())


def log(msg):
    print(f"[gera_seed_faxina {time.strftime('%H:%M:%S')}] {msg}")


# ---------------------------------------------------------------- disco (df)
def disco():
    try:
        out = subprocess.run(["df", "-BG", HOME], capture_output=True, text=True,
                             timeout=30).stdout.strip().splitlines()[-1].split()
        g = lambda s: int(s.rstrip("G"))
        return {"total_gb": g(out[1]), "usado_gb": g(out[2]), "livre_gb": g(out[3]),
                "pct": int(out[4].rstrip("%"))}
    except Exception as e:
        log(f"df falhou: {e}")
        return {"total_gb": None, "usado_gb": None, "livre_gb": None, "pct": None}


# ------------------------------------------------------- fila (LEDGER parse)
def fila_ledger(overrides=None):
    """Lê a seção '## Fila' do LEDGER: itens N pendentes e N riscados (~~..~~ ✅ FEITO)."""
    lotes = []
    overrides = overrides or {}
    try:
        txt = LEDGER.read_text(encoding="utf-8")
    except Exception as e:
        log(f"LEDGER ilegível: {e}")
        return lotes
    m = re.search(r"^## Fila.*?$(.*?)(?=^## |\Z)", txt, re.M | re.S)
    bloco = m.group(1) if m else txt
    limpa = lambda s: re.sub(r"\s+", " ", s.replace("`", "").replace("*", "")).strip()
    for linha in bloco.splitlines():
        linha = linha.rstrip()
        # concluído: - ~~**N3** Jornais do dia~~ ✅ **FEITO 08/09 15:3x** (...)
        md = re.match(r"^- ~~\*\*(N[\w]+)\*\*\s*(.*?)~~\s*(.*)$", linha)
        if md:
            nid, desc, resto = md.groups()
            feito = re.search(r"FEITO\s+([^\(·—*]+)", resto)
            lotes.append({"id": nid, "t": limpa(desc), "ok": True,
                          "quando": limpa(feito.group(1)) if feito else "",
                          "gb": overrides.get(nid, _gb(resto) or _gb(desc))})
            continue
        # pendente: - **N1** descrição → rito...
        mp = re.match(r"^- \*\*(N[\w]+)\*\*\s*(.*)$", linha)
        if mp:
            nid, resto = mp.groups()
            segs = resto.split("→")
            desc = segs[0]
            i = 1
            # não corta dentro de parêntese: "(209 itens → D5 ...)" continua
            while desc.count("(") > desc.count(")") and i < len(segs) and len(desc) < 150:
                desc += " → " + segs[i]
                i += 1
            gb = overrides.get(nid, _gb(desc) or _gb(resto))
            if re.search(r"OK (explícito )?do Miguel|só com OK", resto, re.I):
                eta = "⚠️ aguarda OK do Miguel"
            elif "decisão" in resto and "Miguel" in resto:
                eta = "decisão do Miguel"
            else:
                eta = "madrugada (03:15)"
            lotes.append({"id": nid, "t": limpa(desc)[:150], "ok": False, "eta": eta, "gb": gb})
    return lotes


def _gb(s):
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*G\b", s or "")
    return float(m.group(1).replace(",", ".")) if m else None


# ------------------------------------------------------------- mapa (índice)
def tamanho(path, con):
    """GB do diretório no índice: linha exata; senão soma dos filhos diretos."""
    if not path:
        return None
    cur = con.cursor()
    r = cur.execute("SELECT size FROM dirs WHERE path=?", (path,)).fetchone()
    if r and r[0] and r[0] > 0:
        return round(r[0] / 1073741824.0, 2)
    like = path.rstrip("/") + "/%"
    deeper = path.rstrip("/") + "/%/%"
    # soma dos filhos diretos (nível 1) — netos já estão contados neles
    r = cur.execute("SELECT COALESCE(SUM(size),0) FROM dirs WHERE path LIKE ? AND path NOT LIKE ?",
                    (like, deeper)).fetchone()
    v = (r[0] or 0) / 1073741824.0
    return round(v, 2) if v > 0.01 else None


def mapa(curadoria):
    linhas = []
    con = None
    try:
        con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    except Exception as e:
        log(f"índice indisponível (mapa só com curadoria): {e}")
    for row in curadoria.get("mapa", []):
        gb = row.get("gb")
        if gb is None and con is not None:
            gb = tamanho(row.get("path"), con)
        linhas.append({"p": row.get("label"), "nivel": row.get("nivel", 0),
                       "gb": gb, "st": row.get("st", ""), "obs": row.get("obs", ""),
                       "destino": row.get("destino", "")})
    if con is not None:
        con.close()
    return linhas


# ------------------------------------------------- índice duplo (nuvem)
def espelhar_indice():
    """Cópia diária do indice.sqlite p/ GDrive + B2 (ordem: índice DUPLO).
    Verificação fail-soft: rclone copy rc=0 + lsf com tamanho igual ao local.
    Retorna dict de estado p/ a seed; nunca levanta exceção."""
    estado = {"destinos": ESPELHO_DESTINOS, "ultimo": None, "ok": None, "nota": ""}
    marker = DB.parent / ".ultimo_espelho"
    hoje = time.strftime("%Y-%m-%d")
    if not DB.exists():
        estado["nota"] = "DB local ausente — nada a espelhar"
        return estado
    if marker.exists() and marker.read_text().strip() == hoje:
        estado["ultimo"] = hoje
        estado["ok"] = True
        estado["nota"] = "já espelhado hoje"
        return estado
    tamanho_local = DB.stat().st_size
    falhas = []
    for dest in ESPELHO_DESTINOS:
        try:
            r = subprocess.run(["rclone", "copy", str(DB), dest, "--timeout", "300s"],
                               capture_output=True, text=True, timeout=1200)
            if r.returncode != 0:
                falhas.append(f"{dest}: {r.stderr.strip()[:120]}")
                continue
            v = subprocess.run(["rclone", "lsf", dest, "--format", "sp", "--timeout", "120s"],
                               capture_output=True, text=True, timeout=300)
            confere = any(DB.name in ln and str(tamanho_local) in ln
                          for ln in v.stdout.splitlines())
            if not confere:
                falhas.append(f"{dest}: copy rc=0 mas lsf não confirma tamanho")
        except Exception as e:
            falhas.append(f"{dest}: {e}")
    if falhas:
        estado["nota"] = "🔴 falha(s): " + " | ".join(falhas)
        log(estado["nota"])
        return estado
    marker.write_text(hoje)
    estado.update(ultimo=hoje, ok=True, nota=f"cópia verificada ({tamanho_local/1048576:.0f}MB) nos 2 destinos")
    log(f"índice espelhado p/ GDrive+B2 ({estado['nota']})")
    return estado


def catalogo_nuvem(espelho):
    """CATALOGO_NUVEM.md — índice LEGÍVEL do que está nas nuvens (listagens rclone)."""
    ts = time.strftime("%Y-%m-%d %H:%M")
    L = ["# ☁️ CATÁLOGO_NUVEM — o que a faxina do Dell guarda nas nuvens",
         "",
         f"> Gerado automaticamente por `gera_seed_faxina.py` em {ts} (roda a cada passada da automação leve).",
         "> Nada sai do disco sem backup VERIFICADO — quem retirou o quê, quando e onde está: `LEDGER_APAGADOS.md`.",
         f"> Índice DUPLO: DB local `~/.local/share/buscador_local/indice.sqlite` + cópias em GDrive e B2 ({espelho.get('nota','?')}).",
         "> O Cérebro (este catálogo inclusive) já é espelhado: repo GitHub + B2 + GDrive = catálogo triplo.",
         ""]
    alvos = [
        ("Backblaze B2 — b2:failover-cafezinho1/faxina/", "b2:failover-cafezinho1/faxina/", "lsf"),
        ("Google Drive — gdrive:Backup_Total/dell_faxina/", "gdrive:Backup_Total/dell_faxina/", "lsf"),
        ("Google Drive — Jornais do dia (1216+ PDFs; origem dos jornais varridos)", "gdrive:Jornais do dia/", "size"),
    ]
    for titulo, remoto, modo in alvos:
        L.append(f"## {titulo}")
        try:
            cmd = (["rclone", "size", remoto, "--json"] if modo == "size"
                   else ["rclone", "lsf", remoto, "--max-depth", "2", "--format", "sp"])
            r = subprocess.run(cmd + ["--timeout", "300s"], capture_output=True, text=True, timeout=600)
            if r.returncode != 0:
                L.append(f"- 🔴 listagem falhou: {r.stderr.strip()[:150]}")
            elif modo == "size":
                s = json.loads(r.stdout or "{}")
                L.append(f"- {s.get('count','?')} arquivos · {s.get('bytes',0)/1073741824:.1f} GB")
            else:
                linhas = r.stdout.strip().splitlines()[:300]
                L += ["```"] + (linhas or ["(vazio)"]) + ["```"]
                if len(r.stdout.strip().splitlines()) > 300:
                    L.append("- (truncado em 300 linhas)")
        except Exception as e:
            L.append(f"- 🔴 erro: {e}")
        L.append("")
    tmp = CATALOGO.with_suffix(".tmp")
    tmp.write_text("\n".join(L), encoding="utf-8")
    os.replace(tmp, CATALOGO)
    log(f"catálogo de nuvem gravado: {CATALOGO}")
    return CATALOGO


# ------------------------------------------------------------------- seed
def resolver_faxinas(curadoria):
    """Botões numerados das faxinas regulares (ordem Miguel 08/09 ~19h: «Faxina 1 (data), etc»).
    Data da última execução resolvida de MARCADORES quando houver (scripts gravam ao rodar:
    .marcadores/purga_zcode, .marcadores/db_snapshot, .ultimo_espelho, cabeçalho do de_dell);
    senão vale a data curada em faxina_mapa_curadoria.json. Exibição: DD/MM/AAAA (+ HH:MM)."""
    import re as _re
    cere = AQUI.parents[1]  # .../Cerebro
    saida = []
    for f in curadoria.get("faxinas_regulares", []):
        item = dict(f)
        marc = str(f.get("marcador") or "")
        ultima = str(f.get("ultima") or "")
        try:
            if marc == "auto:cabecalho_de_dell":
                t = (cere / "Foruns" / "ponte_laura_completa" / "de_dell.md").read_text(encoding="utf-8")[:800]
                m = _re.search(r"ROTACIONADO em (\d{2}/\d{2}/\d{4} \d{2}:\d{2})", t)
                if m:
                    item["ultima_fmt"] = m.group(1)
                    item["ultima_iso"] = ""
                    saida.append(item)
                    continue
            elif marc:
                pm = Path(marc).expanduser()
                if pm.exists():
                    txt = pm.read_text(encoding="utf-8").strip().splitlines()[0]
                    if _re.match(r"^\d{4}-\d{2}-\d{2}", txt):
                        ultima = txt
        except Exception:
            pass
        m = _re.match(r"^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{2}:\d{2}))?", ultima)
        if m:
            item["ultima_fmt"] = f"{m.group(3)}/{m.group(2)}/{m.group(1)}" + (f" {m.group(4)}" if m.group(4) else "")
        else:
            item["ultima_fmt"] = ultima or "—"
        item["ultima_iso"] = ultima
        saida.append(item)
    return saida


def main():
    push = "--push" in sys.argv
    quiet = "--quiet" in sys.argv
    sem_nuvem = "--sem-nuvem" in sys.argv
    now = time.localtime()
    curadoria = json.loads(CURADORIA.read_text(encoding="utf-8"))

    d = disco()
    espelho = {"nota": "pulada (--sem-nuvem)"} if sem_nuvem else espelhar_indice()
    ini = curadoria.get("inicio", {})
    liberado = None
    if d["usado_gb"] is not None and ini.get("usado_gb"):
        liberado = max(0, ini["usado_gb"] - d["usado_gb"])

    # fila = lotes de abertura (curadoria) + N do LEDGER (gb por lote = override curado)
    n_lotes = fila_ledger(curadoria.get("fila_gb_override", {}))
    lotes = list(curadoria.get("lotes_abertura", [])) + n_lotes
    ok = sum(1 for l in lotes if l.get("ok"))
    total = len(lotes) or 1
    pct_missao = round(100.0 * ok / total, 1)

    # série histórica: seed anterior + ponto novo (se mudou); 1ª seed nasce com o ponto inicial
    serie = []
    try:
        antiga = json.loads(SEED.read_text(encoding="utf-8"))
        serie = antiga.get("serie", [])
    except Exception:
        pass
    if not serie:
        serie = list(curadoria.get("serie_semente", []))
    ponto = {"d": time.strftime("%d/%m %H:%M", now), "pct": d["pct"],
             "livre_gb": d["livre_gb"], "lib_acum_gb": liberado}
    if not serie or serie[-1].get("pct") != ponto["pct"] or serie[-1].get("d", "")[:5] != ponto["d"][:5]:
        serie.append(ponto)
    serie = serie[-40:]

    nota = (f"Disco {d['pct']}% (era {ini.get('pct_disco','?')}% em {ini.get('data','?')}) · "
            f"{liberado if liberado is not None else '?'}G liberados · "
            f"fila {ok}/{total} lotes · meta {ini.get('meta_pct','?')}%")

    seed = {
        "atualizado": time.strftime("%Y-%m-%d %H:%M", now),
        "autor": "ZCode ZM · gera_seed_faxina.py (Dell)",
        "nota": nota,
        "disco": {**d,
                  "pct_inicio": ini.get("pct_disco"),
                  "usado_inicio_gb": ini.get("usado_gb"),
                  "liberado_gb": liberado,
                  "meta_pct": ini.get("meta_pct"),
                  "data_inicio": ini.get("data"),
                  "nota_inicio": ini.get("nota")},
        "serie": serie,
        "fila": {"pct": pct_missao, "ok": ok, "total": total, "lotes": lotes},
        "mapa": {"linhas": mapa(curadoria),
                 "legenda": curadoria.get("_legenda_status", {})},
        "nuvem": {**curadoria.get("nuvem", {}),
                  "espelho_indice": f"último: {espelho.get('ultimo','—')} · {espelho.get('nota','')}"},
        "faxinas": resolver_faxinas(curadoria),
        "docs": {"ledger": "Cerebro/Ferramentas/buscador_local/LEDGER_APAGADOS.md",
                 "catalogo": "Cerebro/Ferramentas/buscador_local/CATALOGO_NUVEM.md",
                 "forum": "Cerebro/Foruns/forum_faxina_dell_buscador_20260908.md",
                 "nodo": "Cerebro/CEREBRO_NODE_INDICE_LOCAL.md"},
    }

    SEED.parent.mkdir(parents=True, exist_ok=True)
    tmp = SEED.with_suffix(".tmp")
    tmp.write_text(json.dumps(seed, ensure_ascii=False, indent=2), encoding="utf-8")
    json.loads(tmp.read_text(encoding="utf-8"))  # valida
    os.replace(tmp, SEED)
    if not quiet:
        log(f"seed escrita: {SEED} · missão {pct_missao}% ({ok}/{total}) · disco {d['pct']}% · mapa {len(seed['mapa']['linhas'])} linhas")

    if not sem_nuvem:
        try:
            catalogo_nuvem(espelho)
        except Exception as e:
            log(f"catálogo falhou (seed segue válida): {e}")

    if not push:
        return 0

    # push: commit SELETIVO (seed + catálogo) + rebase autostash + prova no origin
    import shutil
    cat_repo = REPO / CATALOGO_REL
    if CATALOGO.exists():
        cat_repo.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(CATALOGO, cat_repo)
    git = lambda *a: subprocess.run(["git", "-C", str(REPO)] + list(a),
                                    capture_output=True, text=True, timeout=180)
    alvos = [SEED_REL] + ([CATALOGO_REL] if CATALOGO.exists() else [])
    r = git("add", "--", *alvos)
    if r.returncode != 0:
        log(f"git add falhou: {r.stderr.strip()[:200]}"); return 1
    st = git("status", "--porcelain", "--", *alvos).stdout.strip()
    if not st:
        log("seed/catálogo sem mudança (nada a commitar) — origin já está atualizado"); return 0
    r = git("commit", "-m", f"🧹 seed /v6/faxina {seed['atualizado']} — missão {pct_missao}% · disco {d['pct']}%")
    if r.returncode != 0:
        log(f"commit falhou: {(r.stderr or r.stdout).strip()[:200]}"); return 1
    git("fetch", "-q", "origin", "main")
    r = git("pull", "--rebase", "--autostash", "origin", "main")
    if r.returncode != 0:
        git("rebase", "--abort")
        log(f"rebase falhou (colisão c/ ronda?) — abortei; resolver manual: {r.stderr.strip()[:200]}")
        return 1
    r = git("push", "origin", "HEAD:main")
    if r.returncode != 0:
        log(f"push falhou: {r.stderr.strip()[:200]}"); return 1
    prova = subprocess.run(["git", "-C", str(REPO), "show", f"origin/main:{SEED_REL}"],
                           capture_output=True, text=True, timeout=60)
    ok_prova = prova.returncode == 0 and seed["atualizado"] in prova.stdout
    log(f"push OK · prova no origin/main: {'✅ atualizado confere' if ok_prova else '🔴 NÃO conferido — investigar'}")
    return 0 if ok_prova else 1


if __name__ == "__main__":
    sys.exit(main())
