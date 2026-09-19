#!/usr/bin/env python3
"""buscador.py — busca arquivos/diretórios do Dell pelo ÍNDICE de metadados.

Índice: ~/.local/share/buscador_local/indice.sqlite (gerado por indice_local.py).
Missão Faxina Dell + Buscador (ordem do Miguel 08/09/2026).

Exemplos:
  python3 buscador.py --nome vorcaro
  python3 buscador.py --ext pdf --min 50M --antes 2026-07-01 --ordem tamanho
  python3 buscador.py --pesados 30                 # 30 maiores arquivos
  python3 buscador.py --pastas 30                  # 30 dirs mais pesados (rollup)
  python3 buscador.py --velhos 90 --min 100M       # velhos+pesados = candidato a nuvem
  python3 buscador.py --dir --nome jornais         # só diretórios
  python3 buscador.py --caminho "Dados_Frios" --ordem tamanho
  python3 buscador.py --duplicatas --min 50M       # mesmo tamanho >1x (investigar)
"""
import argparse
import os
import sqlite3
import sys
import time

DB = os.path.join(os.path.expanduser("~"), ".local", "share", "buscador_local", "indice.sqlite")


def human(n):
    if n is None or n < 0:
        return "?"
    for u in ("B", "K", "M", "G", "T"):
        if n < 1024:
            return f"{n:.0f}{u}" if u == "B" else f"{n:.1f}{u}"
        n /= 1024
    return f"{n:.1f}P"


def parse_size(s):
    s = s.strip().upper()
    mult = 1
    if s and s[-1] in "KMGT":
        mult = {"K": 1024, "M": 1024**2, "G": 1024**3, "T": 1024**4}[s[-1]]
        s = s[:-1]
    return int(float(s) * mult)


def parse_data(s):
    return time.mktime(time.strptime(s, "%Y-%m-%d"))


def conecta():
    if not os.path.exists(DB):
        print("índice não existe — rode antes: python3 indice_local.py", file=sys.stderr)
        sys.exit(2)
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def where(args):
    w, p = [], []
    if args.nome:
        w.append("name LIKE ? COLLATE NOCASE"); p.append(f"%{args.nome}%")
    if args.caminho:
        w.append("path LIKE ? COLLATE NOCASE"); p.append(f"%{args.caminho}%")
    if args.ext:
        exts = [e.strip().lower() if e.strip().startswith(".") else "." + e.strip().lower()
                for e in args.ext.split(",") if e.strip()]
        w.append(f"ext IN ({','.join('?' * len(exts))})"); p += exts
    if args.min:
        w.append("size >= ?"); p.append(parse_size(args.min))
    if args.max:
        w.append("size <= ?"); p.append(parse_size(args.max))
    if args.antes:
        w.append("mtime < ?"); p.append(parse_data(args.antes))
    if args.depois:
        w.append("mtime > ?"); p.append(parse_data(args.depois))
    return (" WHERE " + " AND ".join(w) if w else ""), p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nome"); ap.add_argument("--caminho"); ap.add_argument("--ext")
    ap.add_argument("--min"); ap.add_argument("--max")
    ap.add_argument("--antes"); ap.add_argument("--depois")
    ap.add_argument("--dir", action="store_true", help="só diretórios")
    ap.add_argument("--arq", action="store_true", help="só arquivos")
    ap.add_argument("--ordem", choices=["nome", "tamanho", "data"], default="tamanho")
    ap.add_argument("--limit", type=int, default=60)
    ap.add_argument("--pesados", type=int, help="top N maiores arquivos")
    ap.add_argument("--pastas", type=int, help="top N dirs mais pesados")
    ap.add_argument("--velhos", type=int, help="arquivos com mtime > N dias")
    ap.add_argument("--duplicatas", action="store_true")
    ap.add_argument("--resumo", action="store_true", help="estado do índice")
    args = ap.parse_args()
    con = conecta()

    if args.resumo:
        for r in con.execute("SELECT k,v FROM meta ORDER BY k"):
            print(f"{r['k']}: {r['v']}")
        tot = con.execute("SELECT SUM(size) s, COUNT(*) c FROM files").fetchone()
        print(f"total indexado: {tot['c']} arquivos, {human(tot['s'] or 0)}")
        return

    if args.pesados:
        print("== MAIORES ARQUIVOS ==")
        for r in con.execute("SELECT path,size,mtime FROM files ORDER BY size DESC LIMIT ?",
                             (args.pesados,)):
            print(f"{human(r['size']):>8}  {time.strftime('%Y-%m-%d', time.localtime(r['mtime']))}  {r['path']}")
        return

    if args.pastas:
        print("== DIRETÓRIOS MAIS PESADOS (rollup) ==")
        for r in con.execute("SELECT path,size,nfiles FROM dirs WHERE excl=0 AND size>=0 "
                             "ORDER BY size DESC LIMIT ?", (args.pastas,)):
            print(f"{human(r['size']):>8}  {r['nfiles']:>7} arq  {r['path']}")
        return

    if args.duplicatas:
        w, p = where(args)
        sql = (f"SELECT size, COUNT(*) c, GROUP_CONCAT(path, ' ||| ') paths FROM files{w} "
               f"GROUP BY size HAVING c > 1 ORDER BY size*(c-1) DESC LIMIT ?")
        p.append(args.limit)
        n = 0
        for r in con.execute(sql, p):
            n += 1
            print(f"\n[{human(r['size'])} × {r['c']}]")
            for pth in r["paths"].split(" ||| ")[:6]:
                print(f"   {pth}")
        print(f"\n{n} grupos de possíveis duplicatas")
        return

    if args.velhos:
        cutoff = time.time() - args.velhos * 86400
        w, p = where(args)
        w = (w + " AND " if w else " WHERE ") + "mtime < ?"
        p.append(cutoff)
        sql = f"SELECT path,size,mtime FROM files{w} ORDER BY size DESC LIMIT ?"
        p.append(args.limit)
        print(f"== ARQUIVOS > {args.velhos} DIAS (por tamanho) ==")
        tot = 0
        for r in con.execute(sql, p):
            tot += r["size"]
            print(f"{human(r['size']):>8}  {time.strftime('%Y-%m-%d', time.localtime(r['mtime']))}  {r['path']}")
        print(f"-- top {args.limit}: {human(tot)}")
        return

    tabela = "dirs" if args.dir else ("files" if args.arq else "files")
    if args.dir:
        w, p = where(args)
        w = (w + " AND " if w else " WHERE ") + "excl=0 AND size>=0"
        ordem = {"nome": "name", "tamanho": "size", "data": "mtime"}[args.ordem]
        sql = f"SELECT path,name,size,nfiles,mtime FROM dirs{w} ORDER BY {ordem} DESC LIMIT ?"
        p.append(args.limit)
        for r in con.execute(sql, p):
            print(f"{human(r['size']):>8}  {r['nfiles']:>6} arq  {r['path']}")
        return

    w, p = where(args)
    ordem = {"nome": "name", "tamanho": "size", "data": "mtime"}[args.ordem]
    sql = f"SELECT path,size,mtime FROM files{w} ORDER BY {ordem} DESC LIMIT ?"
    p.append(args.limit)
    tot = 0
    for r in con.execute(sql, p):
        tot += r["size"]
        print(f"{human(r['size']):>8}  {time.strftime('%Y-%m-%d', time.localtime(r['mtime']))}  {r['path']}")
    print(f"-- {args.limit} resultados, {human(tot)} somados")


if __name__ == "__main__":
    main()
