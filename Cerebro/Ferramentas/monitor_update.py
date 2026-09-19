#!/usr/bin/env python3
"""monitor_update.py — escrita SEGURA no MONITORAMENTO_DE_TRABALHO.md (§112, protocolo v2 — 15/09/2026).

Resolve os tropeços de agentes editando o mesmo arquivo ao mesmo tempo:
LOCK (flock exclusivo) + escrita ATÔMICA (tmp + rename). Ninguém perde edição.

USO (chamar SEMPRE por aqui — nunca editar o monitor na mão com outra sessão viva):
  monitor_update.py inicio <ID> "<quem/modelo>" "<o que está fazendo + arquivos>"
  monitor_update.py fim    <ID> "<resultado curto com ✅/⏳/🔴>"
  monitor_update.py nota   <ID> "<atualização curta da linha>"

REGRAS DO FORMATO v2:
  - Uma linha por sessão, identificada por <ID> curto único (ex: ZM-KUBET).
  - Linha ≤ 260 caracteres. Detalhe/comando/prova vai em FÓRUM PRÓPRIO e se
    linka na coluna do resultado. O quadro é um radar, não um relatório.
  - O script só toca a linha do próprio <ID>. Linha de outra sessão é sagrada.
  - ✅ sai do quadro na renovação 48h (vai pro morto); ⏳/🔴 ficam.
"""
from __future__ import annotations

import fcntl
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

MONITOR = Path(
    "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/MONITORAMENTO_DE_TRABALHO.md"
)
LOCK = Path("/tmp/monitor_update.lock")
TAM_MAX = 260
MARCADOR_TABELA = "## 📌 Em andamento AGORA"


def hora() -> str:
    return datetime.now().strftime("%d/%m %H:%M")


def main() -> int:
    if len(sys.argv) < 4 or sys.argv[1] not in ("inicio", "fim", "nota"):
        print(__doc__)
        return 2
    acao, sid, texto = sys.argv[1], sys.argv[2], " ".join(sys.argv[3:])
    if not re.fullmatch(r"[A-Z0-9][A-Za-z0-9._-]{1,30}", sid):
        print(f"ID inválido: {sid!r} (use curto tipo ZM-KUBET)")
        return 2

    LOCK.touch(exist_ok=True)
    with LOCK.open("r+") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)  # só uma escrita por vez no monitor
        linhas = MONITOR.read_text(encoding="utf-8").splitlines(keepends=False)
        padrao = re.compile(r"^\|\s*" + re.escape(sid) + r"\s*[|·]")
        idx = next((i for i, l in enumerate(linhas) if padrao.match(l)), None)

        if acao == "inicio":
            if idx is not None:
                print(f"linha {sid} já existe — use nota/fim")
                return 1
            nova = f"| {sid} · {texto} | {hora()} | ⏳ |"
            if len(nova) > TAM_MAX:
                print(f"linha muito longa ({len(nova)} > {TAM_MAX}) — resuma; detalhe vai em fórum")
                return 1
            try:
                pos = next(i for i, l in enumerate(linhas) if MARCADOR_TABELA in l) + 1
            except StopIteration:
                print(f"marcador '{MARCADOR_TABELA}' não achado no monitor")
                return 1
            linhas.insert(pos, nova)
        else:
            if idx is None:
                print(f"linha {sid} NÃO existe — chame inicio antes")
                return 1
            antiga = linhas[idx]
            estado = "✅" if acao == "fim" else "⏳"
            quem = antiga.split("|")[1].split("·")[0].strip() + " · " if "·" in antiga.split("|")[1] else ""
            corpo = antiga.split("|")[2].strip() if antiga.count("|") >= 3 else texto
            if acao == "nota":
                corpo = texto
            nova = f"| {quem.split(' · ')[0]} · {corpo} | {hora()} | {estado} |"
            if len(nova) > TAM_MAX:
                print(f"linha muito longa ({len(nova)} > {TAM_MAX}) — resuma")
                return 1
            linhas[idx] = nova

        # escrita atômica: tmp na mesma pasta + rename (nunca meio escrito)
        fd, tmp = tempfile.mkstemp(dir=str(MONITOR.parent), prefix=".monitor_", suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("\n".join(linhas) + "\n")
        os.replace(tmp, MONITOR)
    print(f"ok: {acao} {sid} registrado em {MONITOR.name} ({hora()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
