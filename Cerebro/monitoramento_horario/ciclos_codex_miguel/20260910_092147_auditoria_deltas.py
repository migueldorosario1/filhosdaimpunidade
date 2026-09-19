#!/usr/bin/env python3
"""Auditoria somente leitura de objetos Git; não usa rede nem executa o runtime."""
import hashlib
import json
import re
import subprocess
import sys


def git(*args):
    return subprocess.check_output(['git', *args])


def audit(base, head):
    git('merge-base', '--is-ancestor', base, head)
    paths = [p for p in git('diff', '--name-only', base, head).decode().splitlines()
             if p.startswith('cerebro/Foruns/ponte_laura_completa/')
             and (re.search(r'/de_[^/]+\.md$', p) or '/ledger/' in p
                  or p.endswith('/telegram_dsc/RESPOSTAS.md'))]
    commits = git('rev-list', '--reverse', '--first-parent', base + '..' + head).decode().splitlines()
    checks = []
    for commit in commits:
        parent = git('rev-parse', commit + '^1').decode().strip()
        changed = git('diff', '--name-only', parent, commit, '--', *paths).decode().splitlines()
        for path in changed:
            before = git('show', parent + ':' + path)
            after = git('show', commit + ':' + path)
            diff = git('diff', '--no-ext-diff', '--unified=0', parent, commit, '--', path).decode()
            removed = [s[1:] for s in diff.splitlines() if s.startswith('-') and not s.startswith('---')]
            added = [s[1:] for s in diff.splitlines() if s.startswith('+') and not s.startswith('+++')]
            checks.append(dict(commit=commit, parent=parent, path=path,
                               before_sha256=hashlib.sha256(before).hexdigest(),
                               after_sha256=hashlib.sha256(after).hexdigest(),
                               exact_prefix=after.startswith(before),
                               prefix_ignoring_final_lf=after.startswith(before.rstrip(b'\n')),
                               added_lines=len(added), removed_lines=len(removed),
                               nonblank_removed_lines=sum(bool(s.strip()) for s in removed)))
    response_path = 'cerebro/Foruns/ponte_laura_completa/telegram_dsc/RESPOSTAS.md'
    before = git('show', base + ':' + response_path)
    after = git('show', head + ':' + response_path)
    assert after.startswith(before), 'RESPOSTAS deixou de ser append-only'
    delta = after[len(before):].decode()
    response_headers = re.findall(r'^## \[([^\n]+)\] RESPOSTA_PRO_MIGUEL.*$', delta, re.M)
    erratum = git('show', '3086683d9a166198fdc38680899831584a16e04b', '--',
                  'cerebro/cerebro_dsn/dsn_chefe/MEMORIA_VIVA.md').decode()
    result = dict(base=base, head=head, commits=len(commits), checks=checks,
                  total_added_lines=sum(c['added_lines'] for c in checks),
                  total_removed_lines=sum(c['removed_lines'] for c in checks),
                  nonblank_removed_lines=sum(c['nonblank_removed_lines'] for c in checks),
                  literal_prefix_exceptions=[{'commit': c['commit'], 'path': c['path'],
                                             'only_final_lf': c['prefix_ignoring_final_lf']}
                                            for c in checks if not c['exact_prefix']],
                  response_audit=dict(path=response_path, append_only=True,
                                      new_headers=response_headers,
                                      delta_sha256=hashlib.sha256(delta.encode()).hexdigest(),
                                      dedupe_prompt_present='Corrija a classificação de lista_publicados_indisponivel' in delta,
                                      codex_reference_present='XM-20260910-018' in delta,
                                      timestamp_erratum_commit='3086683d9a166198fdc38680899831584a16e04b',
                                      erratum_present='CARIMBO ARREDONDADO PARA FRENTE' in erratum,
                                      telegram_delivery_verified=False,
                                      limitation='Arquivo de resposta e protocolo não comprovam entrega Telegram; faltam recibos do daemon/message_id.'))
    return result


if __name__ == '__main__':
    result = audit(sys.argv[1], sys.argv[2])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(1 if result['nonblank_removed_lines'] else 0)
