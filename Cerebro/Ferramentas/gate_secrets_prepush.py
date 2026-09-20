#!/usr/bin/env python3
"""gate_secrets_prepush.py — GATE ANTI-SEGREDO (pre-push).

Ordem do Miguel ("vai", 20/09/2026 ~08:0x) após o incidente da chave Gemini
publicada no repo público filhosdaimpunidade (forum_incidente_chave_gemini_gcp_20260919).

Uso: hook pre-push do git. Lê stdin no formato "<local ref> <local sha> <remote ref> <remote sha>",
varre APENAS as linhas ADICIONADAS nos commits que estão sendo empurrados e bloqueia
(exit 1) se encontrar padrão de segredo. Nunca imprime valores — só arquivo + tipo de padrão.

Allowlist: linhas com REDACT/…/EXEMPLO/fake/fixture/dummy/PLACEHOLDER e caminhos em EXCLUDE_PATHS
(fixtures de teste conhecidos). O próprio gate se exclui (contém os padrões como regex).
"""
import re
import subprocess
import sys

PATTERNS = [
    (r'AIzaSy[A-Za-z0-9_-]{33}', 'Google API key (AIzaSy…)'),
    (r'AQ\.[A-Za-z0-9_-]{40,}', 'Google API key nova geração (AQ.…)'),
    (r'sk-ant-[A-Za-z0-9_-]{20,}', 'Anthropic (sk-ant-)'),
    (r'sk-or-v1-[a-f0-9]{20,}', 'OpenRouter (sk-or-v1-)'),
    (r'sk-[A-Za-z0-9]{20,}', 'OpenAI/DeepSeek-style (sk-)'),
    (r'ghp_[A-Za-z0-9]{30,}', 'GitHub PAT (ghp_)'),
    (r'github_pat_[A-Za-z0-9_]{20,}', 'GitHub fine-grained PAT'),
    (r'gho_[A-Za-z0-9]{30,}', 'GitHub OAuth token (gho_)'),
    (r'xai-[A-Za-z0-9]{20,}', 'xAI Grok (xai-)'),
    (r'AKIA[0-9A-Z]{16}', 'AWS access key (AKIA)'),
]
ALLOW = re.compile(r'REDACT|…|\.\.\.|EXEMPLO|exemplo|fake|FIXTURE|fixture|dummy|DUMMY|PLACEHOLDER|placeholder|xxxx', re.I)
EXCLUDE_PATHS = {
    'Cerebro/Foruns/gpt_5_6_sol/v4_qualidade_texto_curadoria_20260710/04_codigo_contexto/test_contracts.py',
    'Cerebro/Ferramentas/gate_secrets_prepush.py',
}
EMPTY_TREE = '4b825dc642cb6eb9a060e54bf8d69288fbee4904'


def run_git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True)


def base_para(local_sha, remote_sha):
    if remote_sha and set(remote_sha) != {'0'}:
        return remote_sha
    for cand in ('origin/main', 'origin/deploy-main', 'origin/HEAD'):
        mb = run_git('merge-base', local_sha, cand)
        if mb.returncode == 0 and mb.stdout.strip():
            return mb.stdout.strip()
    return EMPTY_TREE


def varrer_diff(base, local_sha):
    d = run_git('diff', '--unified=0', '--no-color', base, local_sha)
    if d.returncode != 0:
        return []
    achados = []
    arquivo = '?'
    for linha in d.stdout.split('\n'):
        if linha.startswith('+++ b/'):
            arquivo = linha[6:]
            continue
        if not linha.startswith('+') or linha.startswith('+++'):
            continue
        if arquivo in EXCLUDE_PATHS:
            continue
        corpo = linha[1:]
        if ALLOW.search(corpo):
            continue
        for pat, nome in PATTERNS:
            if re.search(pat, corpo):
                achados.append((arquivo, nome))
    return achados


def main():
    bloqueios = []
    for linha in sys.stdin.read().strip().split('\n'):
        if not linha.strip():
            continue
        partes = linha.split()
        if len(partes) < 4:
            continue
        local_ref, local_sha, remote_ref, remote_sha = partes[:4]
        if set(local_sha) == {'0'}:  # deleção de ref
            continue
        base = base_para(local_sha, remote_sha)
        for arquivo, nome in varrer_diff(base, local_sha):
            bloqueios.append((local_ref, arquivo, nome))
    if bloqueios:
        print('🚫 GATE ANTI-SEGREDO: push BLOQUEADO — padrão de segredo detectado nas linhas adicionadas:', file=sys.stderr)
        for ref, arq, nome in bloqueios[:20]:
            print(f'   • {ref}: {arq}  [{nome}]', file=sys.stderr)
        print('   Corrija (mova o valor para o Cofre e deixe só o ponteiro) e repita o push.', file=sys.stderr)
        print('   Ref: Cerebro/Foruns/forum_incidente_chave_gemini_gcp_20260919.md', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
