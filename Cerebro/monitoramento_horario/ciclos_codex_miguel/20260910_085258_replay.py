"""Reproduz só as duas funções puras capturadas por leitura; não importa runtime."""
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

def main(primary_path):
    primary = json.loads(Path(primary_path).read_text())
    functions = primary['runtime']['functions']
    namespace = {'html': html, 're': re, 'Any': Any}
    for function in functions:
        exec(compile(function['source'], function['name'], 'exec'), namespace)
    paragraph = 'conteúdo fictício usado somente neste diagnóstico local ' * 9
    raw = '\n\n'.join(f'<p>{paragraph}</p>' for _ in range(3))
    cases = {
        'texto_simples': '\n\n'.join([paragraph] * 3),
        'html_p_separados': raw,
        'html_escapado_uma_vez': html.escape(raw, quote=False),
        'html_escapado_duas_vezes': html.escape(html.escape(raw, quote=False), quote=False),
        'html_p_adjacentes_sem_escape': raw.replace('\n\n', ''),
    }
    results = []
    for name, value in cases.items():
        try:
            output = namespace['_paragraphs'](value)
            results.append({'case': name, 'outcome': 'returned', 'paragraphs': output.count('<p>')})
        except RuntimeError as error:
            results.append({'case': name, 'outcome': 'RuntimeError', 'message': str(error)})
    expected = ['returned', 'returned', 'returned', 'RuntimeError', 'RuntimeError']
    assert [r['outcome'] for r in results] == expected, results
    print(json.dumps({'runtime_sha256': primary['runtime']['sha256'], 'synthetic_inputs': True,
                      'production_imported': False, 'production_written': False,
                      'results': results}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main(sys.argv[1])
