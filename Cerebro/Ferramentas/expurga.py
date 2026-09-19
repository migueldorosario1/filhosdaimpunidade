#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
expurga.py — Varredura e expurgo de conteúdo sensível que entrou no Cérebro
 Ferramenta do PROTOCOLO_EXPURGO_SENSIVEL.md (17/09/2026, ordem do Miguel)

Uso:
  python3 expurga.py "termo"                      # só varre e reporta
  python3 expurga.py "termo" --expurgar-arquivos  # remove linhas com o termo dos .md vivos (backup fora do repo)
  python3 expurga.py "termo" --remotos            # inclui tencent/nyc na varredura (ssh)
  python3 expurga.py "termo" --git-historico      # verifica histórico git e gera /tmp/expurgo_git.txt pronto p/ filter-repo

Regra de ouro: o termo sensível NÃO é gravado em nenhum log/backup dentro do repo.
Backups de expurgo vão para ~/backups_expurgo/ (FORA do repo e do Cérebro).
"""
import os
import re
import subprocess
import sys
import datetime
import shutil

CEREBRO = "/home/migueldorosario/Downloads/Antigravity Google/Cerebro"
REPO = os.path.expanduser("~/cerebro-miguel")
MEMORIAS_ZCODE = os.path.expanduser("~/.zcode/cli/memories")
EXEC_ZCODE = os.path.expanduser("~/.zcode/cli/exec")
BACKUP_DIR = os.path.expanduser("~/backups_expurgo")

# 1) arquivos vivos do Cérebro (fóruns, memórias, nodos, índices, ponte, monitor e mortos)
LOCAIS_VIVOS = [
    CEREBRO,
    os.path.expanduser("~/Downloads/Antigravity Google/Projeto Cafezinho Agentes/Foruns"),
]
PADRAO_ARQ = (".md", ".txt", ".json")


def sh(cmd, timeout=40):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip(), r.returncode
    except subprocess.TimeoutExpired:
        return "(timeout)", 124


def varrer_dir(base, termo):
    achados = []
    rx = re.compile(re.escape(termo), re.IGNORECASE)
    for raiz, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__")]
        for fn in files:
            if not fn.endswith(PADRAO_ARQ):
                continue
            p = os.path.join(raiz, fn)
            try:
                texto = open(p, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            n = len(rx.findall(texto))
            if n:
                achados.append((p, n))
    return achados


def varrer_git(termo):
    out = []
    for repo, nome in [(REPO, "cerebro-miguel (clone Dell)")]:
        if not os.path.isdir(repo):
            continue
        o, rc = sh(f"cd {repo} && git log --all --oneline -S {shlex_termo(termo)} | head -10")
        if o and o != "(timeout)":
            out.append((nome + " — HISTÓRICO git", o))
        o2, _ = sh(f"cd {repo} && git stash list | head -3")
        if termo.lower() in o2.lower():
            out.append((nome + " — STASH", o2))
    return out


def shlex_termo(t):
    return "'" + t.replace("'", "'\\''") + "'"


def varrer_remotos(termo):
    out = []
    t = shlex_termo(termo)
    o, _ = sh(f"timeout 60 ssh tencent 'grep -rl --include=*.md --include=*.json --include=*.log {t} "
              f"/home/ubuntu/cafezinho/v6_data/foruns /home/ubuntu/cafezinho/v6_data/entregas 2>/dev/null | head -10'", timeout=70)
    if o:
        out.append(("tencent v6_data (fóruns/entregas espelhados + logs)", o))
    o, _ = sh(f"timeout 60 ssh tencent 'grep -rl {t} /home/ubuntu/cafezinho/redes 2>/dev/null | head -5'", timeout=70)
    if o:
        out.append(("tencent esteira redes", o))
    o, _ = sh(f"timeout 60 ssh nyc 'cd /home/ubuntu/cerebro-miguel-mirror.git && git log --all --oneline -S {t} | head -5'", timeout=70)
    if o and o != "(timeout)":
        out.append(("nyc mirror — HISTÓRICO git", o))
    return out


def expurgar_arquivos(termo, achados):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    rx = re.compile(re.escape(termo), re.IGNORECASE)
    print("\n== EXPURGO DE ARQUIVOS VIVOS (linhas com o termo saem; backup em %s) ==" % BACKUP_DIR)
    for p, n in achados:
        bak = os.path.join(BACKUP_DIR, stamp + "__" + p.replace("/", "_")[-160:])
        shutil.copy2(p, bak)
        linhas = open(p, encoding="utf-8", errors="ignore").read().split("\n")
        novas = [l for l in linhas if not rx.search(l)]
        removidas = len(linhas) - len(novas)
        if removidas:
            open(p, "w", encoding="utf-8").write("\n".join(novas))
            print("  limpo: %s (-%d linhas)" % (p.replace(os.path.expanduser("~"), "~"), removidas))
    print("  (refaça a varredura para confirmar zero; histórico git exige passo próprio — ver protocolo)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    termo = sys.argv[1]
    expurgar = "--expurgar-arquivos" in sys.argv
    remotos = "--remotos" in sys.argv
    git_hist = "--git-historico" in sys.argv

    print("== VARREDURA: termo procurado (não é gravado em log) ==")
    total = 0
    for base in LOCAIS_VIVOS:
        for p, n in varrer_dir(base, termo):
            print("  %dx  %s" % (n, p.replace(os.path.expanduser("~"), "~")))
            total += n

    # memórias de agentes ZCode (todos os projetos)
    if os.path.isdir(MEMORIAS_ZCODE):
        for p, n in varrer_dir(MEMORIAS_ZCODE, termo):
            print("  %dx  %s" % (n, p.replace(os.path.expanduser("~"), "~")))
            total += n

    # transcripts/exec de sessões ZCode (outputs de bash já rodados)
    if os.path.isdir(EXEC_ZCODE):
        for p, n in varrer_dir(EXEC_ZCODE, termo):
            print("  %dx  %s" % (n, p.replace(os.path.expanduser("~"), "~")))
            total += n

    for nome, o in varrer_git(termo):
        print("  [GIT] %s:\n%s" % (nome, "    " + o.replace("\n", "\n    ")))
        total += 1

    if remotos:
        for nome, o in varrer_remotos(termo):
            print("  [REMOTO] %s:\n%s" % (nome, "    " + o.replace("\n", "\n    ")))
            total += 1

    if git_hist:
        print("\n== HISTÓRICO GIT — arquivo pronto para filter-repo ==")
        replace = os.path.join("/tmp", "expurgo_git.txt")
        with open(replace, "w") as f:
            f.write("%s\n==>\n" % termo)
        print("  cat /tmp/expurgo_git.txt  # confira (termo => vazio)")
        print("  cd ~/cerebro-miguel && python3 -m git_filter_repo --replace-text /tmp/expurgo_git.txt --force")
        print("  git remote add origin git@github.com:migueldorosario1/cerebro-miguel.git  # filter-repo remove remotes")
        print("  git push --force origin main ; git push --force nyc main")
        print("  ssh nyc 'cd /home/ubuntu/cerebro-miguel-mirror.git && git gc --prune=now'")

    if expurgar and total:
        expurgar_arquivos(termo, [(p, n) for base in LOCAIS_VIVOS for p, n in varrer_dir(base, termo)] +
                          (varrer_dir(MEMORIAS_ZCODE, termo) if os.path.isdir(MEMORIAS_ZCODE) else []))
    print("\nTOTAL de ocorrências em lugares varríveis: %d" % total)
    print("Lugares NÃO varríveis automaticamente (ver protocolo): histórico do app ZCode (manual do dono), "
          "commits antigos do GitHub por SHA direto (janela até GC deles), espelhos B2/GDrive (re-copy resolve).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
