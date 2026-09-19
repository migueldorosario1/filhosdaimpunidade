"""Auditoria somente leitura de objetos Git; executar da raiz do repositorio."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

BASE = '4b20bd9c56098d34ae91e3206e7bf24b2d00e7c0'
CUT = 'a442bf126478c0bd7463a795157cab310c6cd92b'
LOCAL = '482b6b35fef834ff309d69a50c286f4ef5d76adb'
ROOT = 'cerebro/Foruns/ponte_laura_completa/'
PATH = ROOT + 'de_dell.md'
CHANNELS = [ROOT + name for name in ['de_dell.md', 'de_laura.md', 'de_ideias.md']]


def git(*args):
    return subprocess.check_output(['git'] + list(args))


def blob(ref, path):
    return git('show', ref + ':' + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


commits = git('rev-list', '--first-parent', '--reverse', BASE + '..' + CUT).decode().splitlines()
changes = []
for commit in commits:
    parent = git('rev-parse', commit + '^1').decode().strip()
    for path in CHANNELS:
        old, new = blob(parent, path), blob(commit, path)
        if old == new:
            continue
        row = git('diff', '--numstat', parent, commit, '--', path).decode().split('\t')
        changes.append({'commit': commit, 'parent': parent, 'path': path,
                        'added': int(row[0]), 'deleted': int(row[1]),
                        'parent_is_byte_prefix': new.startswith(old)})

# Recorte ja identificado na ronda anterior; nao restaura o arquivo vivo.
missing = b''.join(blob(BASE + '^1', PATH).splitlines(True)[2001:2026])
assert len(missing) == 9015
assert sha(missing) == '4299160ee2fd81bfd7332f061f110d3bb2c3685fbeaf06001255d40da0643b67'
header = re.compile(rb'^\[10/09/2026 [^\n]*\] (?:\*\*)?DS-N-20260910-011(?:\*\*)? [\xe2-]', re.M)
presence = []
for ref in ['b8514d0f7b42164b20aa8f3585c47e247e29ddda', BASE, LOCAL, CUT]:
    data = blob(ref, PATH)
    presence.append({'ref': ref, 'sha256': sha(data), 'exact_block_present': missing in data,
                     'dated_header_count': len(header.findall(data))})
canonical = Path('/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/ponte_laura_completa/de_dell.md')
data = canonical.read_bytes()
presence.append({'path': str(canonical), 'sha256': sha(data), 'exact_block_present': missing in data,
                 'dated_header_count': len(header.findall(data))})

manual_path = 'cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md'
review_path = 'cerebro/Foruns/revisao/canal_dsn_revisores.md'
manual = blob(CUT, manual_path).decode()
review_delta = git('diff', '--unified=0', BASE, CUT, '--', review_path).decode()
whitelist = next(line for line in manual.splitlines() if 'PODEM (texto e título)' in line)
rejection = next(line[1:] for line in review_delta.splitlines() if line.startswith('+') and 'R2 269693' in line)
print(json.dumps({'base': BASE, 'cut': CUT, 'local': LOCAL, 'first_parent_commit_count': len(commits),
                  'changes': changes,
                  'totals': {key: sum(row[key] for row in changes) for key in ['added', 'deleted']},
                  'all_channel_changes_append_only': all(row['parent_is_byte_prefix'] for row in changes),
                  'dsn011': {'bytes': len(missing), 'sha256': sha(missing), 'presence': presence,
                             'note': 'Ausencia herdada; nao e nova remocao nesta janela.'},
                  'r2_pf': {'manual_path': manual_path, 'manual_sha256': sha(blob(CUT, manual_path)),
                            'whitelist': whitelist, 'pf_in_whitelist': ' PF,' in whitelist,
                            'review_path': review_path, 'new_review_line': rejection,
                            'note': 'Conflito documental; nao revisa post nem altera o parecer R2.'},
                  'exit_note': 'RC 0 = auditoria concluida; nao significa guard aprovado ou ticket fechado.'},
                 ensure_ascii=False, indent=2))
