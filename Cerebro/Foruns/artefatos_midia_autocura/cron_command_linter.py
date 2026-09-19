#!/usr/bin/env python3
"""Lint read-only de entradas cron usadas pelo V4.

Detecta comentário que corta comando, executável/script ausente e ausência de
flock/timeout. Não altera crontab, arquivos ou processos. Opcionalmente emite
um recibo v0.1.1 atômico para a inbox do media_ledger.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Callable, Iterable


AUTHORIZATION_REF = "chat_miguel_20260807_TRINDADE-F2-CONSTRUCAO-AUTOCURA-V4-MIDIA"
SHELL_BUILTINS = {"cd", "echo", "exec", "printf", "test", "true", "false"}
WRAPPERS = {"flock", "timeout", "nice", "ionice", "nohup", "setsid"}


def _now() -> datetime:
    return datetime.now().astimezone()


def _find_shell_comment(command: str) -> int | None:
    """Return the index of an unquoted # that starts a shell word."""
    single = double = escaped = False
    for index, char in enumerate(command):
        if escaped:
            escaped = False
            continue
        if char == "\\" and not single:
            escaped = True
            continue
        if char == "'" and not double:
            single = not single
            continue
        if char == '"' and not single:
            double = not double
            continue
        if char == "#" and not single and not double:
            if index == 0 or command[index - 1].isspace():
                return index
    return None


def _comment_likely_truncates_command(suffix: str) -> bool:
    """Avoid treating a harmless trailing annotation as a cut command.

    A cut is actionable when the discarded part still contains shell operators,
    an absolute operational path or a recognizable command/script token.
    """
    discarded = suffix.lstrip("# ")
    return bool(
        re.search(r"(?:&&|\|\||>>|2>&1|[;|])", discarded)
        or re.search(r"/(?:bin|usr|root|opt|home|var|tmp)/[^\s]+", discarded)
        or re.search(r"(?:^|\s)(?:flock|timeout|python[0-9.]*|bash|sh)(?:\s|$)", discarded)
        or re.search(r"\.(?:py|sh)(?:\s|$)", discarded)
    )


def _is_env_assignment(token: str) -> bool:
    return bool(re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", token))


def _command_from_line(line: str, source_format: str) -> str | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]*\s*=", stripped):
        return None

    if stripped.startswith("@"):
        parts = stripped.split(None, 2 if source_format == "system" else 1)
        expected = 3 if source_format == "system" else 2
        return parts[-1] if len(parts) == expected else ""

    parts = stripped.split(None, 5)
    if len(parts) < 6:
        return ""
    rest = parts[5]
    if source_format == "system":
        user_and_command = rest.split(None, 1)
        return user_and_command[1] if len(user_and_command) == 2 else ""
    return rest


def _auto_format(path: str) -> str:
    normalized = os.path.abspath(path)
    return "system" if normalized == "/etc/crontab" or "/cron.d/" in normalized else "user"


def _tokenize(command: str) -> list[str]:
    try:
        return shlex.split(command, comments=False, posix=True)
    except ValueError:
        return []


def _command_candidates(tokens: list[str]) -> list[str]:
    """Return executables/scripts worth checking, including wrapped command."""
    candidates: list[str] = []
    index = 0
    command_start = True
    while index < len(tokens):
        token = tokens[index]
        if token in {"&&", "||", ";", "|"}:
            command_start = True
            index += 1
            continue
        if token.startswith(">") or token.startswith("<") or token in {"2>&1", "&"}:
            index += 1
            continue
        if not command_start:
            index += 1
            continue
        while index < len(tokens) and _is_env_assignment(tokens[index]):
            index += 1
        if index >= len(tokens):
            break
        token = tokens[index]
        base = os.path.basename(token)
        candidates.append(token)
        command_start = False

        if base == "env":
            index += 1
            while index < len(tokens) and (tokens[index].startswith("-") or _is_env_assignment(tokens[index])):
                index += 1
            command_start = True
            continue
        if base == "flock":
            index += 1
            while index < len(tokens) and tokens[index].startswith("-"):
                index += 1
            if index < len(tokens):
                index += 1  # lock file/fd
            command_start = True
            continue
        if base == "timeout":
            index += 1
            while index < len(tokens) and tokens[index].startswith("-"):
                index += 1
            if index < len(tokens):
                index += 1  # duration
            command_start = True
            continue
        if base in WRAPPERS:
            index += 1
            while index < len(tokens) and tokens[index].startswith("-"):
                index += 1
            command_start = True
            continue

        if re.match(r"^(python[0-9.]*)$", base) and index + 1 < len(tokens):
            script = tokens[index + 1]
            if script.endswith(".py"):
                candidates.append(script)
        index += 1
    return candidates


def _exists(candidate: str) -> bool:
    if candidate in SHELL_BUILTINS:
        return True
    if "/" in candidate:
        return os.path.isfile(candidate) and (candidate.endswith(".py") or os.access(candidate, os.X_OK))
    return shutil.which(candidate) is not None


def lint_text(
    text: str,
    *,
    source: str = "<stdin>",
    source_format: str = "user",
    exists: Callable[[str], bool] = _exists,
    read_text: Callable[[str], str] | None = None,
) -> list[dict]:
    if read_text is None:
        read_text = lambda path: Path(path).read_text(encoding="utf-8")
    findings: list[dict] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        command = _command_from_line(line, source_format)
        if command is None:
            continue
        if not command:
            findings.append({
                "source": source, "line": line_number, "severity": "error",
                "code": "CRON_ENTRY_MALFORMED", "reason_code": None,
                "detail": "entrada cron sem comando analisável",
            })
            continue

        comment_at = _find_shell_comment(command)
        executable_command = command
        if comment_at is not None and _comment_likely_truncates_command(command[comment_at:]):
            executable_command = command[:comment_at].rstrip()
            findings.append({
                "source": source, "line": line_number, "severity": "error",
                "code": "COMMAND_TRUNCATED_BY_COMMENT",
                "reason_code": "COMMAND_TRUNCATED_BY_COMMENT",
                "detail": "comentário shell não citado pode cortar o comando",
                "command_before_comment": executable_command,
                "discarded_suffix": command[comment_at:],
            })

        tokens = _tokenize(executable_command)
        guard_tokens = list(tokens)
        for candidate in _command_candidates(tokens):
            if candidate.endswith(".sh") and exists(candidate):
                try:
                    wrapper_text = read_text(candidate)
                except (OSError, UnicodeError):
                    continue
                for wrapper_line in wrapper_text.splitlines():
                    stripped_wrapper = wrapper_line.strip()
                    if stripped_wrapper and not stripped_wrapper.startswith("#"):
                        guard_tokens.extend(_tokenize(stripped_wrapper))
        basenames = {os.path.basename(token) for token in guard_tokens}
        if "flock" not in basenames:
            findings.append({
                "source": source, "line": line_number, "severity": "warning",
                "code": "LOCK_WRAPPER_MISSING", "reason_code": None,
                "detail": "comando não usa flock; sobreposição de ciclos não está bloqueada",
            })
        if "timeout" not in basenames:
            findings.append({
                "source": source, "line": line_number, "severity": "warning",
                "code": "TIMEOUT_WRAPPER_MISSING", "reason_code": None,
                "detail": "comando não usa timeout; duração máxima não está explícita",
            })

        for candidate in dict.fromkeys(_command_candidates(tokens)):
            if not exists(candidate):
                findings.append({
                    "source": source, "line": line_number, "severity": "error",
                    "code": "EXECUTABLE_MISSING", "reason_code": "EXECUTABLE_MISSING",
                    "detail": f"executável ou script não encontrado: {candidate}",
                    "candidate": candidate,
                })
    return findings


def lint_paths(paths: Iterable[str], source_format: str) -> tuple[list[dict], list[str]]:
    findings: list[dict] = []
    scanned: list[str] = []
    for raw_path in paths:
        path = Path(raw_path)
        targets = sorted(p for p in path.iterdir() if p.is_file()) if path.is_dir() else [path]
        for target in targets:
            scanned.append(str(target))
            fmt = _auto_format(str(target)) if source_format == "auto" else source_format
            try:
                findings.extend(lint_text(target.read_text(encoding="utf-8"), source=str(target), source_format=fmt))
            except (OSError, UnicodeError) as exc:
                findings.append({
                    "source": str(target), "line": None, "severity": "error",
                    "code": "SOURCE_UNREADABLE", "reason_code": None, "detail": str(exc),
                })
    return findings, scanned


def make_receipt(findings: list[dict], scanned: list[str], timestamp: datetime | None = None) -> dict:
    timestamp = timestamp or _now()
    canonical = next((item["reason_code"] for item in findings if item.get("reason_code")), None)
    stamp = timestamp.strftime("%Y%m%d_%H%M%S")
    return {
        "sinal": f"cron lint shadow: {len(findings)} achado(s) em {len(scanned)} fonte(s)",
        "causa_raiz": "configuracao_cron_insegura" if findings else "none_observed",
        "correcao": "none — read-only shadow",
        "prova": {
            "before": {"sources": scanned},
            "after": {"findings": findings},
            "checks": ["parser cron executado", "nenhum arquivo cron alterado"],
            "artifacts": ["cron_command_linter.py"],
        },
        "rollback": "n/a — read-only",
        "regra_derivada": "cron inseguro → alertar; nunca corrigir automaticamente em shadow",
        "alcance": "v4",
        "risco_promocao": "L0",
        "policy_version": "midia-v0.1",
        "origem": "machine_autocure",
        "system_state": {"seletor": "n/a", "cotas": "n/a", "fontes_ativas": scanned,
                         "prompt_juiz": "n/a", "schema_versions": {"receipt": "v0.1.1"}},
        "role": "shadow",
        "gold_source": None,
        "reason_code": canonical,
        "metadata": {
            "schema_version": "receipt-v0.1.1",
            "receipt_id": f"rcpt_{stamp}_antigravity_cron_lint",
            "ref": None,
            "vertice": "antigravity",
            "ts": timestamp.isoformat(timespec="seconds"),
            "generalizabilidade": "medium",
            "causa_suspeita": "cron_configuration" if findings else None,
            "actor_roles": {"proposer": ["antigravity"], "technical_reviewer": [],
                            "authorizer": ["miguel"], "executor": ["codex"], "verifier": []},
            "decision_state": "executed",
            "authorization_ref": AUTHORIZATION_REF,
            "delivery_state": "delivered",
            "model_identity": {"model": "codex-gpt-5", "environment": "codex",
                               "session_ref": "antigravity-f2-20260807"},
        },
    }


def write_jsonl_atomic(path: str, receipts: list[dict]) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            for receipt in receipts:
                handle.write(json.dumps(receipt, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="arquivo(s) ou diretório(s) de cron")
    parser.add_argument("--format", choices=("auto", "user", "system"), default="auto")
    parser.add_argument("--json", action="store_true", help="imprime relatório JSON")
    parser.add_argument("--receipt-out", help="drop-file JSONL v0.1.1 (escrita atômica)")
    args = parser.parse_args(argv)

    findings, scanned = lint_paths(args.paths, args.format)
    report = {"mode": "shadow-read-only", "sources": scanned, "findings": findings,
              "summary": {"errors": sum(x["severity"] == "error" for x in findings),
                          "warnings": sum(x["severity"] == "warning" for x in findings)}}
    if args.receipt_out:
        write_jsonl_atomic(args.receipt_out, [make_receipt(findings, scanned)])
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        for item in findings:
            print(f"{item['severity'].upper()} {item['source']}:{item['line']} {item['code']} — {item['detail']}")
        print(f"{report['summary']['errors']} erro(s), {report['summary']['warnings']} aviso(s); read-only")
    return 2 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
