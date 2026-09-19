#!/usr/bin/env python3
"""Auditoria somente leitura dos deltas da ronda XM-20260910-013.

Executar da raiz do repositório: python3 <este arquivo>.
RC 0 prova conteúdo preservado nesta janela; prefixo literal é medido à parte.
Contagens por aresta incluem cada pai de merge; net_numstat mede o delta líquido.
Não instala nem aprova guards.
"""
import hashlib
import json
import os
import subprocess

BASE = "b281f44b51800dfced8f66b16b32d9970295708d"
CUT = "fc25ea067d120e6f06ec6c77bcdf3ea0ba01764f"
ROOT = "cerebro/Foruns/ponte_laura_completa/"
BRIDGES = [ROOT + p for p in ("de_dell.md", "de_laura.md", "de_ideias.md")]


def git(*args):
    return subprocess.check_output(["git", *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


commits = git("rev-list", "--reverse", BASE + ".." + CUT).decode().splitlines()
rows = []
for commit in commits:
    parents = git("rev-list", "--parents", "-n", "1", commit).decode().split()[1:]
    for parent in parents:
        paths = git("diff", "--name-only", parent, commit).decode().splitlines()
        for path in paths:
            if path not in BRIDGES and not path.startswith(ROOT + "ledger/"):
                continue
            before = git("show", parent + ":" + path)
            after = git("show", commit + ":" + path)
            prefix = len(os.path.commonprefix([before, after]))
            residual = before[prefix:]
            trailing_insert = (
                bool(residual) and not residual.strip(b"\r\n")
                and len(after) >= len(before) and after.endswith(residual)
            )
            counts = git("diff", "--numstat", parent, commit, "--", path).decode().split()
            rows.append({
                "commit": commit, "parent": parent, "path": path,
                "prefix_preserved": after.startswith(before),
                "content_preserved": after.startswith(before) or trailing_insert,
                "insertion_before_trailing_blank_lines": trailing_insert,
                "old_trailing_bytes_at_insertion": len(residual) if trailing_insert else 0,
                "before_bytes": len(before), "after_bytes": len(after),
                "before_sha256": sha(before), "after_sha256": sha(after),
                "added_lines": int(counts[0]), "deleted_lines": int(counts[1]),
            })

bridge_rows = [r for r in rows if r["path"] in BRIDGES]
result = {
    "base": BASE, "cut": CUT, "commits_examined": len(commits),
    "rows": rows,
    "all_prefixes_preserved": all(r["prefix_preserved"] for r in rows),
    "all_content_preserved": all(r["content_preserved"] for r in rows),
    "bridge_changes": len(bridge_rows),
    "bridge_added_lines": sum(r["added_lines"] for r in bridge_rows),
    "bridge_deleted_lines": sum(r["deleted_lines"] for r in bridge_rows),
    "ledger_changes": len(rows) - len(bridge_rows),
    "ledger_added_lines": sum(r["added_lines"] for r in rows if r not in bridge_rows),
    "ledger_deleted_lines": sum(r["deleted_lines"] for r in rows if r not in bridge_rows),
    "limitations": "Objetos Git; sem prova de runtime, transporte de XM ou conserto BUG-178/185.",
}
result["net_numstat"] = git("diff", "--numstat", BASE, CUT, "--", *BRIDGES, ROOT + "ledger/").decode().splitlines()
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result["all_content_preserved"] else 1)
