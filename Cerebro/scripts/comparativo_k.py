#!/usr/bin/env python3
"""Comparativo Legado vs Pos-Reforma — Comando K."""

from __future__ import annotations

import subprocess
import textwrap


SSH = [
    "ssh",
    "-o",
    "ConnectTimeout=10",
    "-o",
    "BatchMode=yes",
    "-i",
    "/home/migueldorosario/.ssh/id_rsa",
    "-p",
    "38422",
    "ubuntu@43.156.151.165",
]


REMOTE_SCRIPT = r"""
import html
import json
import re
import sqlite3
import subprocess
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

now = datetime.now().strftime("%Y-%m-%d %H:%M BRT")
inicio_brt = datetime.now().strftime("%Y-%m-%d")
after_utc = f"{inicio_brt}T03:00:00"

db_canario = Path("/root/cafezinho/portal_cafezinho/Dados/bancos/pipeline_editorial_local.db")
db_fallback = Path("/root/cafezinho/Dados/bancos/pipeline_editorial_local.db")
db_path = db_canario if db_canario.is_file() else db_fallback
log_path = Path("/root/cafezinho/Dados/logs/canario.log")
anti_path = Path("/root/cafezinho/Dados/logs/anti_repeticao.log")


def wp_get(params):
    url = "https://controle.ocafezinho.com/wp-json/wp/v2/posts?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def log_text(path):
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def tail_matches(text, pattern, limit=5, flags=re.I):
    rows = [line for line in text.splitlines() if re.search(pattern, line, flags)]
    return rows[-limit:]


def count_matches(text, pattern, flags=re.I):
    return len(re.findall(pattern, text, flags))


def sqlite_scalar(sql, default="0"):
    if not db_path.is_file():
        return default
    try:
        conn = sqlite3.connect(db_path)
        row = conn.execute(sql).fetchone()
        conn.close()
        return str(row[0] if row else default)
    except Exception:
        return default


def sqlite_rows(sql):
    if not db_path.is_file():
        return []
    try:
        conn = sqlite3.connect(db_path)
        rows = conn.execute(sql).fetchall()
        conn.close()
        return rows
    except Exception:
        return []


wp_posts_hoje = wp_get({
    "after": after_utc,
    "per_page": 100,
    "status": "publish",
    "_fields": "id",
})
wp_ultimos = wp_get({
    "per_page": 5,
    "status": "publish",
    "_fields": "id,date,title",
})

drafts_total = sqlite_scalar("SELECT COUNT(*) FROM noticias_prontas")
drafts_ultimos = sqlite_rows(
    "SELECT tema, titulo FROM noticias_prontas ORDER BY produzida_em DESC LIMIT 5"
)

log = log_text(log_path)
anti = log_text(anti_path)
erros = count_matches(log, r"ERROR|Traceback|CRITICAL|Falha|❌", flags=0)
duplicatas = count_matches(log + "\n" + anti, r"duplicata|DUPLICATA", flags=0)
imagens_aprovadas = count_matches(log, r"Tribunal Visual.*APROVADA|imagem.*aprovada|midia.*aprovada")

llms = tail_matches(log, r"provider_final", limit=5)
tokens = tail_matches(log, r"tokens", limit=5)
custo = tail_matches(log, r"custo", limit=5)
latencia = tail_matches(log, r"Conclu", limit=5)

cron = subprocess.run(
    "sudo crontab -l 2>/dev/null | grep maestro_grande || true",
    shell=True,
    capture_output=True,
    text=True,
    timeout=10,
).stdout.strip()

print(f"\n{'='*60}")
print(f"⚔️  COMPARATIVO LEGADO vs PÓS-REFORMA — {now}")
print(f"{'='*60}\n")
print(f"📰 LEGADO publishes hoje desde 00h BRT: {len(wp_posts_hoje)}")
print(f"🐤 CANARIO drafts total: {drafts_total}")
print(f"⚠️  Erros no canario: {erros}")

print("\n📊 METRICAS K:")
print("  LLMs usados:")
print("\n".join(f"    {line}" for line in llms) if llms else "    n/d")
print("  Tokens:")
print("\n".join(f"    {line}" for line in tokens) if tokens else "    n/d")
print("  Custo:")
print("\n".join(f"    {line}" for line in custo) if custo else "    n/d")
print("  Latencia/conclusoes recentes:")
print("\n".join(f"    {line}" for line in latencia) if latencia else "    n/d")
print(f"  Imagens aprovadas (grep): {imagens_aprovadas}")
print(f"  Duplicatas (grep): {duplicatas}")

print("\n📋 ULTIMOS 5 LEGADO:")
for post in wp_ultimos:
    title = html.unescape((post.get("title") or {}).get("rendered") or "")
    print(f"  {post.get('id')} | {str(post.get('date') or '')[:16]} | {title[:80]}")

print("\n📝 ULTIMOS 5 CANARIO:")
if drafts_ultimos:
    for tema, titulo in drafts_ultimos:
        print(f"  [{tema}] {str(titulo)[:80]}")
else:
    print("  (sem drafts)")

print("\n⏰ CRONTAB CANARIO:")
print(f"  {cron or '(sem cron maestro)'}")
print(f"\n{'='*60}")
print("📊 Fórum: Foruns/forum_comparativo_legado_vs_pos_reforma_20260614.md")
"""


def main() -> int:
    cmd = "python3 - <<'PY'\n" + REMOTE_SCRIPT.strip() + "\nPY"
    res = subprocess.run(SSH + [cmd], text=True)
    return res.returncode


if __name__ == "__main__":
    raise SystemExit(main())
