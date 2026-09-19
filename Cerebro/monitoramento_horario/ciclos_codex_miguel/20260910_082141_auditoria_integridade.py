#!/usr/bin/env python3
"""Auditoria Git somente leitura: reconciliação externa observada em 10/09/2026."""
import hashlib
import json
import subprocess

OLD_LOCAL = '7fbbd37931844e8be5778e2a3a77ab1f833952af'
OLD_REMOTE = '65e29b18f9c5cb7ad5da1967aa285c81b1b5bc54'
PREVIOUS_REMOTE = '4c039b07704a784dd197d384baa890f204b6e5b1'
CUT = 'ca004992f5f33376700a4ecb6ef28c7bf218de3a'
BRIDGE = 'cerebro/Foruns/ponte_laura_completa/'
RECEIPTS = 'cerebro/monitoramento_horario/ciclos_codex_miguel/'

def git(*args):
    return subprocess.check_output(['git', *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

def subsequence(old, new):
    """Preserva ordem e multiplicidade de todas as linhas não vazias."""
    a = [l for l in old.splitlines() if l.strip()]
    b = iter(l for l in new.splitlines() if l.strip())
    matched = 0
    for line in a:
        if not any(other == line for other in b):
            return False, matched, len(a)
        matched += 1
    return True, matched, len(a)

def main():
    result = {'old_local': OLD_LOCAL, 'old_remote': git('rev-parse', OLD_REMOTE).decode().strip(), 'previous_remote': PREVIOUS_REMOTE, 'cut': CUT, 'reconciliation': [], 'receipts': [], 'new_bridge_commits': []}
    for ref in (OLD_LOCAL, OLD_REMOTE):
        for p in ('de_dell.md', 'de_laura.md', 'ledger/codex_miguel.md', 'estado/codex_miguel.md'):
            before = git('show', ref+':'+BRIDGE+p)
            after = git('show', CUT+':'+BRIDGE+p)
            preserved, matched, total = subsequence(before, after)
            result['reconciliation'].append({'source_commit': ref, 'path': BRIDGE+p, 'old_sha256': sha(before), 'new_sha256': sha(after), 'old_nonblank_lines': total, 'matched_in_order': matched, 'all_nonblank_lines_preserved_in_order': preserved, 'byte_prefix': after.startswith(before)})
    files = git('ls-tree', '-r', '--name-only', OLD_LOCAL, '--', RECEIPTS).decode().splitlines()
    for p in files:
        if '20260910_' not in p: continue
        a = git('show', OLD_LOCAL+':'+p); b = git('show', CUT+':'+p)
        result['receipts'].append({'path':p, 'sha256':sha(a), 'byte_identical': a==b})
    commits = git('rev-list', '--reverse', '--first-parent', PREVIOUS_REMOTE+'..'+CUT).decode().splitlines()
    for c in commits:
        parent = git('rev-parse', c+'^').decode().strip()
        rows = git('diff', '--numstat', parent, c, '--', BRIDGE+'de_dell.md', BRIDGE+'de_laura.md', BRIDGE+'ledger/').decode().splitlines()
        for row in rows:
            added, deleted, path = row.split('\t', 2)
            a = git('show', parent+':'+path); b=git('show', c+':'+path)
            ok, matched, total = subsequence(a,b)
            result['new_bridge_commits'].append({'commit': c, 'parent': parent, 'path':path, 'added':int(added), 'deleted':int(deleted), 'all_nonblank_lines_preserved_in_order':ok})
    result['first_parent_commits'] = len(commits)
    data=git('show',CUT+':'+BRIDGE+'de_dell.md')
    result['conflict_marker_lines'] = sum(line.startswith((b'<<<<<<< ', b'=======', b'>>>>>>> ')) for line in data.splitlines())
    result['passed'] = all(x['all_nonblank_lines_preserved_in_order'] for x in result['reconciliation']+result['new_bridge_commits']) and all(x['byte_identical'] for x in result['receipts']) and result['conflict_marker_lines']==0
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
