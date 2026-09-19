"""Auditoria somente leitura: delta de uma ronda, com prova de remoção no Git."""
import difflib
import hashlib
import json
import re
import subprocess

BASE = '0b904190433edfeedf2d48d8e598b3ed27abfbc2'
CUT = '4b20bd9c56098d34ae91e3206e7bf24b2d00e7c0'
BIRTH = 'b8514d0f7b42164b20aa8f3585c47e247e29ddda'
REMOVAL = '4b20bd9c56098d34ae91e3206e7bf24b2d00e7c0'
PATHS = ['cerebro/Foruns/ponte_laura_completa/de_' + x + '.md'
         for x in ('dell', 'laura', 'ideias', 'astra', 'nuvem_publicador')]


def git(*args):
    return subprocess.check_output(['git', *args])


def digest(data):
    return hashlib.sha256(data).hexdigest()


commits = git('rev-list', '--reverse', '--first-parent', BASE + '..' + CUT).decode().splitlines()
changes = []
for commit in commits:
    parent = git('rev-parse', commit + '^1').decode().strip()
    for row in git('diff', '--numstat', parent, commit, '--', *PATHS).decode().splitlines():
        added, deleted, path = row.split('\t')
        before, after = [git('show', c + ':' + path) for c in (parent, commit)]
        changes.append(dict(commit=commit, parent=parent, path=path,
                            added=int(added), deleted=int(deleted),
                            parent_is_byte_prefix=after.startswith(before)))

before = git('show', REMOVAL + '^1:' + PATHS[0])
after = git('show', REMOVAL + ':' + PATHS[0])
before_lines, after_lines = before.splitlines(keepends=True), after.splitlines(keepends=True)
removed = []
for tag, a, b, c, d in difflib.SequenceMatcher(None, before_lines, after_lines, autojunk=False).get_opcodes():
    if tag in ('delete', 'replace'):
        block = b''.join(before_lines[a:b])
        removed.append(dict(parent_line_start=a + 1, parent_line_end=b, lines=b-a,
                            bytes=len(block), sha256=digest(block), block=block))
assert len(removed) == 1, 'Quantidade inesperada de trechos removidos; revisar a evidência.'
entry = removed[0]
block = entry.pop('block')
pattern = rb'(?m)^\[10/09/2026 04:03 BRT\] DS-N-20260910-011\b'
original, current = [git('show', c + ':' + PATHS[0]) for c in (BIRTH, CUT)]
entry.update(ref='DS-N-20260910-011', birth=BIRTH, removal_commit=REMOVAL,
             birth_contains_exact_block=block in original,
             parent_contains_exact_block=block in before,
             cut_contains_exact_block=block in current,
             cut_dated_headers=len(re.findall(pattern, current)))
assert entry['birth_contains_exact_block'] and entry['parent_contains_exact_block']
assert not entry['cut_contains_exact_block'] and entry['cut_dated_headers'] == 0
print(json.dumps(dict(base=BASE, cut=CUT, first_parent_commit_count=len(commits),
                     changes=changes, totals={'added':sum(c['added'] for c in changes),
                                             'deleted':sum(c['deleted'] for c in changes)},
                     removed=entry, result='REMOCAO_CONFIRMADA_NAO_RESTAURADA',
                     note='RC 0 significa auditoria reproduzida; não significa aprovação do guard.'),
                 ensure_ascii=False, indent=2))
