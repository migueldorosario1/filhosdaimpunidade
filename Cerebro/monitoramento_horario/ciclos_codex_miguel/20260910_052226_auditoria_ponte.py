"""Auditoria somente leitura; executar da raiz do repositorio. Nao instala guard."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

BASE = 'a442bf126478c0bd7463a795157cab310c6cd92b'
CUT = '47d39bbeae595364e7ffa2c656bdf940d5e4c5cb'
LOCAL = 'efd9366b79ec10e573907c745e79f16a80199a09'
BIRTH = 'b8514d0f7b42164b20aa8f3585c47e247e29ddda'
REMOVAL = '4b20bd9c56098d34ae91e3206e7bf24b2d00e7c0'
ROOT = 'cerebro/Foruns/ponte_laura_completa/'
PATH = ROOT + 'de_dell.md'
CANONICAL = '/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/ponte_laura_completa/de_dell.md'


def git(*args):
    return subprocess.check_output(['git', *args])


def blob(ref, path=PATH):
    return git('show', ref + ':' + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def header_count(data, token):
    # Adendos entre a ref e o travessao contam; -RESTAURO e citacoes nao contam.
    pattern = rb'^\[[^\n]+\] (?:\*\*)?' + re.escape(token.encode()) + rb'(?=\s|\*\*)'
    return len(re.findall(pattern, data, re.M))


commits = git('rev-list', '--first-parent', '--reverse', BASE + '..' + CUT).decode().splitlines()
changes = []
for commit in commits:
    parent = git('rev-parse', commit + '^1').decode().strip()
    for name in ['de_dell.md', 'de_laura.md', 'de_ideias.md']:
        path = ROOT + name
        before, after = blob(parent, path), blob(commit, path)
        if before == after:
            continue
        stat = git('diff', '--numstat', parent, commit, '--', path).decode().split('\t')
        changes.append({'commit': commit, 'parent': parent, 'path': path,
                        'added': int(stat[0]), 'deleted': int(stat[1]),
                        'parent_is_byte_prefix': after.startswith(before)})

birth = blob(BIRTH)
start = birth.index(b'[10/09/2026 04:03 BRT] DS-N-20260910-011 ')
end = birth.find(b'\n[', start + 1)
original = birth[start:] if end == -1 else birth[start:end]
body = original.rstrip(b'\n')
assert len(original) == 9015
assert sha(original) == '4299160ee2fd81bfd7332f061f110d3bb2c3685fbeaf06001255d40da0643b67'
assert sha(body) == '9f77c13e5fa9812798368351905c9ab9ff56c108a2227112f7e0f29b23de1860'
presence = []
for ref in [BIRTH, BASE, CUT, LOCAL]:
    data = blob(ref)
    presence.append({'ref': ref, 'sha256': sha(data),
                     'full_original_count': data.count(original),
                     'dated_header_count': header_count(data, 'DS-N-20260910-011')})
canonical = Path(CANONICAL).read_bytes()
presence.append({'path': CANONICAL, 'sha256': sha(canonical),
                 'full_original_count': canonical.count(original),
                 'dated_header_count': header_count(canonical, 'DS-N-20260910-011')})
assert presence[2]['full_original_count'] == 1

before, after = blob(REMOVAL + '^1'), blob(REMOVAL)
removal_diff = git('diff', '--unified=0', REMOVAL + '^1', REMOVAL, '--', PATH).decode()
deleted_lines = [line[1:] for line in removal_diff.splitlines() if line.startswith('-') and not line.startswith('---')]
deleted_bytes = ('\n'.join(deleted_lines) + '\n').encode()
assert deleted_bytes == original
tokens = ['DS-N-20260910-001', 'DS-N-20260910-010', 'DS-N-20260910-011', 'CL-20260910-002']
counts = {token: {'before': header_count(before, token), 'after': header_count(after, token)} for token in tokens}
assert counts['DS-N-20260910-001'] == {'before': 1, 'after': 1}
assert counts['DS-N-20260910-010'] == {'before': 1, 'after': 1}
assert counts['DS-N-20260910-011'] == {'before': 1, 'after': 0}

print(json.dumps({
    'base': BASE, 'cut': CUT, 'local': LOCAL,
    'first_parent_commit_count': len(commits), 'changes': changes,
    'totals': {key: sum(row[key] for row in changes) for key in ['added', 'deleted']},
    'all_channel_changes_append_only': all(row['parent_is_byte_prefix'] for row in changes),
    'dsn011': {'birth': BIRTH, 'raw_bytes': len(original), 'raw_characters': len(original.decode()),
               'raw_sha256': sha(original), 'body_without_final_lf_bytes': len(body),
               'body_without_final_lf_sha256': sha(body), 'presence': presence,
               'conclusion': 'Restauro integral confirmado no remoto. 8646 sao caracteres, 9015 sao bytes UTF-8 com LF final. Hash declarado pelo DS-N corresponde ao corpo de 9014 bytes sem LF final.'},
    'removal_attribution': {'commit': REMOVAL, 'path': PATH, 'deleted_lines': len(deleted_lines),
                            'deleted_bytes': len(deleted_bytes), 'deleted_sha256': sha(deleted_bytes),
                            'all_deleted_bytes_are_dsn011': deleted_bytes == original,
                            'dated_header_counts': counts,
                            'conclusion': '4b20bd9c5 removeu somente DS-N-011 neste arquivo. DS-N-001/010 permanecem. Ausencia do resumo CL-002 antecede esse commit.'},
    'exit_note': 'RC 0 = auditoria documental concluida; nao fecha BUG-178/185 nem aprova guard.'
}, ensure_ascii=False, indent=2))
