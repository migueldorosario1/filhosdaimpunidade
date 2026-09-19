#!/usr/bin/env python3
"""indice_local.py — constrói/atualiza o ÍNDICE LOCAL de arquivos por metadados.

Missão Faxina Dell + Buscador (ordem do Miguel 08/09/2026 ~15:0x:
"tudo indexado no Cérebro, computador levinho, poucos diretórios").

O índice é um SQLite em ~/.local/share/buscador_local/indice.sqlite
(FORA do Cérebro para mantê-lo leve; o Cérebro guarda os scripts, o
LEDGER_APAGADOS.md e os relatórios legíveis).

Registra arquivos e diretórios com: caminho, nome, extensão, tamanho, mtime,
e rollup de tamanho/quantidade por diretório. Prune de lixo regenerável
(.git interno, node_modules, caches, toolchains) — o diretório podado é
gravado como linha 'excl' para constar no mapa sem pesar o índice.

Uso:
  python3 indice_local.py            # rebuild completo (padrão)
  python3 indice_local.py --budget 300   # limita a 300s (roda parcial e marca)
  python3 indice_local.py --raiz /caminho  # raiz extra além do $HOME
"""
import argparse
import os
import sqlite3
import sys
import time

HOME = os.path.expanduser("~")
DB_DIR = os.path.join(HOME, ".local", "share", "buscador_local")
DB = os.path.join(DB_DIR, "indice.sqlite")

# Nomes de diretório podados em QUALQUER profundidade (nunca entrar).
PODA_NOME = {".git", "node_modules", "__pycache__", ".venv", "venv",
             ".tox", ".mypy_cache", ".pytest_cache", "dist-info"}

# Prefixos relativos à raiz podados (registra a pasta, não entra).
PODA_PREFIXO = (
    ".cache/", ".npm/", ".nvm/", ".pyenv/", ".rustup/", ".gradle/",
    ".local/lib/", ".local/share/Trash/", "snap/", ".android/",
    "Android/Sdk/", ".deepseek/snapshots/", ".gemini/antigravity-browser-profile/",
    ".gemini/antigravity/", ".config/google-chrome/", ".config/Code/CachedData/",
    ".config/Code/Cache/", ".vscode/extensions/", ".unsloth/",
    ".mozilla/firefox/", ".grok/marketplace-cache/", ".codex/.tmp/",
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS files(
  path TEXT PRIMARY KEY, name TEXT, ext TEXT,
  size INTEGER, mtime REAL
);
CREATE TABLE IF NOT EXISTS dirs(
  path TEXT PRIMARY KEY, name TEXT,
  size INTEGER, nfiles INTEGER, mtime REAL, excl INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT);
CREATE INDEX IF NOT EXISTS idx_files_name ON files(name);
CREATE INDEX IF NOT EXISTS idx_files_size ON files(size);
CREATE INDEX IF NOT EXISTS idx_files_mtime ON files(mtime);
CREATE INDEX IF NOT EXISTS idx_dirs_size ON dirs(size);
"""


def escanear(raizes, budget_s):
    files, dirs = [], []
    dir_size, dir_nfiles = {}, {}
    t0 = time.time()
    parcial = False
    for raiz in raizes:
        raiz = os.path.abspath(raiz)
        # mounts de outro dispositivo (~/GDrive = rclone FUSE do Google Drive,
        # gvfs, etc.) NUNCA são atravessados — índice é LOCAL (armadilha 08/09:
        # 1ª passada queimou o budget varrendo 119G de nuvem pela rede).
        try:
            raiz_dev = os.stat(raiz).st_dev
        except OSError:
            continue
        pilha = [raiz]
        dir_size.setdefault(raiz, 0)
        dir_nfiles.setdefault(raiz, 0)
        while pilha:
            if time.time() - t0 > budget_s:
                parcial = True
                pilha = []
                break
            atual = pilha.pop()
            try:
                entries = list(os.scandir(atual))
            except (PermissionError, FileNotFoundError, OSError):
                continue
            nome_base = os.path.basename(atual)
            mtime_dir = 0.0
            try:
                mtime_dir = os.stat(atual).st_mtime
            except OSError:
                pass
            dirs.append((atual, nome_base, dir_size.get(atual, 0),
                         dir_nfiles.get(atual, 0), mtime_dir, 0))
            for e in entries:
                try:
                    if e.is_dir(follow_symlinks=False):
                        st_d = e.stat(follow_symlinks=False)
                        if st_d.st_dev != raiz_dev:
                            # mount de nuvem/rede: registra como excl, não entra
                            dirs.append((e.path, e.name, -1, -1, st_d.st_mtime, 1))
                            continue
                        rel = os.path.relpath(e.path, raiz)
                        if e.name in PODA_NOME or any(
                                rel.startswith(p) or ("/" + p) in ("/" + rel + "/")
                                for p in PODA_PREFIXO if p.endswith("/") and rel == p.rstrip("/")) \
                                or any(rel.startswith(p) for p in PODA_PREFIXO):
                            # pasta podada: registra como excl, não entra
                            try:
                                st = e.stat(follow_symlinks=False)
                                dirs.append((e.path, e.name, -1, -1, st.st_mtime, 1))
                            except OSError:
                                dirs.append((e.path, e.name, -1, -1, 0.0, 1))
                            continue
                        dir_size.setdefault(e.path, 0)
                        dir_nfiles.setdefault(e.path, 0)
                        pilha.append(e.path)
                    elif e.is_file(follow_symlinks=False):
                        st = e.stat(follow_symlinks=False)
                        ext = os.path.splitext(e.name)[1].lower()
                        files.append((e.path, e.name, ext, st.st_size, st.st_mtime))
                        # rollup para todos os ancestrais até a raiz
                        d = atual
                        while True:
                            dir_size[d] = dir_size.get(d, 0) + st.st_size
                            dir_nfiles[d] = dir_nfiles.get(d, 0) + 1
                            if d == raiz or len(d) <= len(raiz):
                                break
                            pai = os.path.dirname(d)
                            if pai == d:
                                break
                            d = pai
                except (PermissionError, FileNotFoundError, OSError):
                    continue
    # rollup final: dirs gravadas antes dos filhos serem somados → recalcula
    dirs_final = [(p, n, dir_size.get(p, s), dir_nfiles.get(p, f), m, x)
                  for (p, n, s, f, m, x) in dirs]
    return files, dirs_final, parcial, time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=int, default=900, help="segundos máximos")
    ap.add_argument("--raiz", action="append", default=[], help="raiz extra")
    args = ap.parse_args()

    raizes = [HOME] + args.raiz
    os.makedirs(DB_DIR, exist_ok=True)
    con = sqlite3.connect(DB)
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript(SCHEMA)

    t0 = time.time()
    files, dirs, parcial, dur = escanear(raizes, args.budget)

    con.execute("BEGIN")
    if not parcial:
        con.execute("DELETE FROM files")
        con.execute("DELETE FROM dirs")
    con.executemany("INSERT OR REPLACE INTO files VALUES(?,?,?,?,?)", files)
    con.executemany("INSERT OR REPLACE INTO dirs VALUES(?,?,?,?,?,?)", dirs)
    con.execute("INSERT OR REPLACE INTO meta VALUES('ultimo_scan',?)",
                (time.strftime("%Y-%m-%d %H:%M:%S"),))
    con.execute("INSERT OR REPLACE INTO meta VALUES('parcial',?)", ("1" if parcial else "0",))
    con.execute("INSERT OR REPLACE INTO meta VALUES('duracao_s',?)", (f"{dur:.0f}",))
    con.execute("INSERT OR REPLACE INTO meta VALUES('n_files',?)", (str(len(files)),))
    con.execute("INSERT OR REPLACE INTO meta VALUES('n_dirs',?)", (str(len(dirs)),))
    con.commit()
    con.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    con.close()
    print(f"índice {DB}: {len(files)} arquivos, {len(dirs)} dirs em {time.time()-t0:.0f}s"
          + (" (PARCIAL — budget estourou)" if parcial else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
