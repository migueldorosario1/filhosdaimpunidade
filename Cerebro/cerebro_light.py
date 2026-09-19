#!/usr/bin/env python3
"""
cerebro_light.py — F2 da Reforma do Cérebro (DS, 2026-05-24)
Gera .light.md para nodes >20KB: cabeçalho + últimas N entradas + ponteiros.
Zero LLM. Não toca os originais. Agentes usam .light.md ao despertar.

Uso:
  python3 cerebro_light.py              # gera para todos nodes >20KB
  python3 cerebro_light.py --force      # regenera todos, mesmo os <20KB
  python3 cerebro_light.py CEREBRO_NODE_GOVERNANCA.md  # um node específico
"""
import re
import sys
import time
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent
LIGHT_DIR = BASE / "cerebro_light"
LIGHT_DIR.mkdir(exist_ok=True)

THRESHOLD_KB = 20          # gera .light.md apenas para nodes acima disso
MAX_ENTRIES = 5            # quantas entradas recentes incluir no .light.md
HEADER_LINES = 60          # linhas do topo (navegação, sumário, regras críticas)
MIN_ENTRY_CHARS = 80       # ignora entradas muito curtas (linha de separação, etc.)


def kb(n: int) -> str:
    return f"{n / 1024:.0f}KB"


def extrair_entradas(content: str) -> list[tuple[str, str]]:
    """
    Divide o conteúdo em entradas por cabeçalho ## ou timestamp BRT.
    Retorna lista de (titulo, bloco).
    """
    # Parte por ## ou por marcador de data/timestamp
    pattern = re.compile(
        r'^(#{1,3} .+|## \[?\d{4}-\d{2}-\d{2})',
        re.MULTILINE
    )
    splits = list(pattern.finditer(content))
    if not splits:
        return [("(sem seções)", content[:2000])]

    entradas = []
    for i, m in enumerate(splits):
        titulo = m.group(0).strip()
        start = m.start()
        end = splits[i + 1].start() if i + 1 < len(splits) else len(content)
        bloco = content[start:end].strip()
        if len(bloco) >= MIN_ENTRY_CHARS:
            entradas.append((titulo, bloco))

    return entradas


def gerar_light(node: Path) -> Path:
    content = node.read_text(errors="ignore")
    lines = content.splitlines()

    # Cabeçalho: primeiras N linhas (sumário, links críticos, regras)
    header_block = "\n".join(lines[:HEADER_LINES])

    # Entradas recentes
    entradas = extrair_entradas(content)
    recentes = entradas[-MAX_ENTRIES:] if len(entradas) > MAX_ENTRIES else entradas

    size = node.stat().st_size
    total_entradas = len(entradas)
    omitidas = total_entradas - len(recentes)

    light_lines = [
        f"# {node.stem} — VERSÃO LIGHT",
        f"> Gerado automaticamente por `cerebro_light.py` em {datetime.now().strftime('%Y-%m-%d %H:%M BRT')}",
        f"> Original: `{node.name}` ({kb(size)}) — {total_entradas} entradas totais",
        f"> Este arquivo é READ-ONLY. Edite sempre o original.",
        "",
        "---",
        "",
        "## CABEÇALHO ORIGINAL (primeiras linhas)",
        "",
        header_block,
        "",
        "---",
        "",
    ]

    if omitidas > 0:
        light_lines += [
            f"## ⏩ {omitidas} entradas antigas omitidas",
            f"> Para ver o histórico completo, leia `{node.name}` diretamente.",
            f"> Busca rápida: `python3 cerebro.py --buscar <termo>`",
            "",
            "---",
            "",
        ]

    light_lines.append(f"## ÚLTIMAS {len(recentes)} ENTRADAS")
    light_lines.append("")

    for titulo, bloco in recentes:
        # Trunca blocos muito longos a 800 chars
        bloco_truncado = bloco if len(bloco) <= 800 else bloco[:800] + f"\n\n> *(... {len(bloco) - 800} chars omitidos — ler original)*"
        light_lines.append(bloco_truncado)
        light_lines.append("")
        light_lines.append("---")
        light_lines.append("")

    light_lines += [
        "## PONTEIROS",
        f"- Original completo: [`{node.name}`](./{node.name})",
        f"- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)",
        f"- Busca: `python3 cerebro.py --buscar <termo>`",
        f"- Validador: `python3 validar_cerebro.py`",
    ]

    out_path = LIGHT_DIR / f"{node.stem}.light.md"
    out_path.write_text("\n".join(light_lines), encoding="utf-8")
    return out_path


def main(args: list[str]):
    force = "--force" in args
    targets_arg = [a for a in args if not a.startswith("--")]

    if targets_arg:
        nodes = [BASE / t for t in targets_arg if (BASE / t).exists()]
        if not nodes:
            print(f"❌ Nenhum node encontrado: {targets_arg}")
            return
    else:
        nodes = sorted(BASE.glob("CEREBRO_*.md"))
        if not force:
            nodes = [n for n in nodes if n.stat().st_size > THRESHOLD_KB * 1024]

    print(f"\n🪶 GERADOR CÉREBRO LIGHT — {datetime.now().strftime('%Y-%m-%d %H:%M BRT')}")
    print(f"{'=' * 62}")
    print(f"Threshold: >{THRESHOLD_KB}KB | Entradas recentes: {MAX_ENTRIES} | Destino: cerebro_light/")
    print(f"{'-' * 62}")

    gerados = []
    for node in nodes:
        out = gerar_light(node)
        size_orig = node.stat().st_size
        size_light = out.stat().st_size
        reducao = (1 - size_light / size_orig) * 100
        print(f"  ✅ {node.name:<42} {kb(size_orig):>6} → {kb(size_light):>5} ({reducao:.0f}% menor)")
        gerados.append(out)

    print(f"\n✅ {len(gerados)} arquivo(s) .light.md gerados em: {LIGHT_DIR}")
    if not nodes:
        print("   (nenhum node acima do threshold — use --force para forçar)")


if __name__ == "__main__":
    main(sys.argv[1:])
