"""Limited Cérebro receipts and Miguel notifications for the hourly Astra round.

No scheduler, model call, git checkout, shell evaluation or production operation.
GitHub writes use compare-and-swap, fixed destinations and read-back verification.
"""
from __future__ import annotations

import base64
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import time
from types import SimpleNamespace
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
STATE_ROOT = ROOT / "astra_operacoes/state"
REPOSITORY = "migueldorosario1/cerebro-miguel"
GH = "/home/migueldorosario/.local/bin/gh"
MONITOR = "cerebro/MONITORAMENTO_DE_TRABALHO.md"
BRIDGE = "cerebro/Foruns/ponte_laura_completa/de_astra.md"
REPORT_ROOT = "cerebro/Relatorios/astra/ronda_horaria/"
ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,100}\Z")
KEY_RE = re.compile(r"[A-Za-z0-9_.:-]{1,160}\Z")
MAX_FILE = 20 * 1024 * 1024
SECRET_RE = re.compile(r"(?:\b\d{7,12}:[A-Za-z0-9_-]{30,}\b|\b(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,})\b|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)")


class DeliveryError(Exception):
    """Controlled error text; never include command stderr or credential values."""


class Conflict(DeliveryError):
    pass


def _require(value, message):
    if not value:
        raise DeliveryError(message)


def _now():
    return datetime.now(timezone.utc).isoformat()


def _digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _run_id(run_id):
    _require(isinstance(run_id, str) and ID_RE.fullmatch(run_id), "Identificador de rodada inválido.")
    return run_id


def _safe_text(value):
    _require(isinstance(value, str) and not SECRET_RE.search(value), "Conteúdo recusado pela proteção de segredos.")
    return value


def _safe_source_path(path, remote=False):
    _require(isinstance(path, str) and path and "\\" not in path, "Caminho de fonte inválido.")
    parts = PurePosixPath(path).parts
    _require(".." not in parts and "\x00" not in path, "Travessia de diretórios recusada.")
    forbidden = {"state", "auth.json", ".env", ".ssh", ".config", ".codex", "cofre_intake", "credentials", "secrets"}
    _require(not any(p.lower() in forbidden or p.lower().startswith(".env.") for p in parts), "Fonte privada recusada.")
    if remote:
        _require(path.startswith("cerebro/") and not path.startswith("/"), "Fonte GitHub fora do Cérebro.")
    else:
        p = Path(path)
        _require(p.is_absolute(), "Fonte local exige caminho absoluto.")
        try:
            relative = p.relative_to(ROOT)
        except ValueError:
            raise DeliveryError("Fonte local fora do workspace.") from None
        _require(relative.parts and (relative.parts[0] == "Cerebro" or relative.as_posix() in {".agents/AGENTS.md", "AGENTS.md", "MEMORY.md"}), "Fonte local fora das instruções e do Cérebro.")
        current = ROOT
        for part in relative.parts:
            current = current / part
            _require(not current.is_symlink(), "Symlink de fonte recusado.")
    return path


def _sources(config):
    _require(config.get("repository") == REPOSITORY, "Repositório não autorizado.")
    sources = config.get("sources", [])
    _require(isinstance(sources, list) and sources, "Fontes não configuradas.")
    for source in sources:
        _require(source.get("kind") in {"local", "github"}, "Tipo de fonte inválido.")
        _safe_source_path(source.get("path"), source["kind"] == "github")
    return sources


def _state(config):
    p = Path(config["state_dir"])
    _require(p.is_absolute() and ".." not in p.parts, "Estado exige caminho absoluto seguro.")
    try:
        relative = p.relative_to(STATE_ROOT)
    except ValueError:
        raise DeliveryError("Estado fora do diretório privado Astra.") from None
    _require(relative.parts, "Estado exige subdiretório próprio.")
    current = STATE_ROOT
    _require(not current.is_symlink(), "Symlink de estado recusado.")
    for part in relative.parts:
        current = current / part
        _require(not current.is_symlink(), "Symlink de estado recusado.")
    p.mkdir(mode=0o700, parents=True, exist_ok=True)
    st = p.stat()
    _require(st.st_uid == os.getuid() and not (stat.S_IMODE(st.st_mode) & 0o077), "Estado deve ser privado (0700).")
    return p


def _private_subdir(config, name):
    p = _state(config) / name
    _require(not p.is_symlink(), "Symlink privado recusado.")
    p.mkdir(mode=0o700, exist_ok=True)
    _require(not (stat.S_IMODE(p.stat().st_mode) & 0o077), "Subdiretório deve ser privado.")
    return p


def _new_json(path, data):
    encoded = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(encoded)
        stream.flush()
        os.fsync(stream.fileno())


def _read_json(path):
    _require(not path.is_symlink() and path.is_file(), "Arquivo de estado inválido.")
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, "rb") as stream:
        data = stream.read(MAX_FILE + 1)
    _require(len(data) <= MAX_FILE, "Estado excede limite.")
    return json.loads(data)


def _gh(config, path, method="GET", payload=None):
    _require(config.get("repository") == REPOSITORY, "Repositório não autorizado.")
    _safe_source_path(path, remote=True)
    allowed_read = {s["path"] for s in _sources(config) if s["kind"] == "github"}
    is_report = path.startswith(REPORT_ROOT) and ID_RE.fullmatch(path[len(REPORT_ROOT):-3] or "") and path.endswith(".md")
    _require(path in allowed_read or path in {MONITOR, BRIDGE} or is_report, "Destino fora da lista permitida.")
    _require(method in {"GET", "PUT"}, "Método GitHub não autorizado.")
    if method == "PUT":
        _require(path in {MONITOR, BRIDGE} or is_report, "Escrita fora dos recibos autorizados.")
    endpoint = "repos/" + REPOSITORY + "/contents/" + quote(path, safe="/")
    if method == "GET":
        endpoint += "?ref=main"
    return _request(endpoint, method, payload)


def _request(endpoint, method="GET", payload=None):
    env = {k: os.environ[k] for k in ("HOME", "PATH", "DBUS_SESSION_BUS_ADDRESS", "XDG_RUNTIME_DIR", "LANG", "LC_ALL") if k in os.environ}
    env.update({"GH_PROMPT_DISABLED": "1", "GIT_TERMINAL_PROMPT": "0"})
    argv = [GH, "api", "--hostname", "github.com", "--method", method, endpoint]
    if payload is not None:
        argv += ["--input", "-"]
    try:
        result = subprocess.run(argv, input=None if payload is None else json.dumps(payload), text=True, capture_output=True, timeout=45, env=env, check=False)
    except (OSError, subprocess.TimeoutExpired):
        raise DeliveryError("GitHub indisponível; nenhuma entrega presumida.") from None
    if result.returncode:
        if "HTTP 409" in result.stderr or "HTTP 422" in result.stderr:
            raise Conflict("Conflito GitHub; releitura necessária.")
        if "HTTP 404" in result.stderr:
            return None
        raise DeliveryError("GitHub recusou a operação; detalhes privados omitidos.")
    _require(len(result.stdout) <= 3 * MAX_FILE, "Resposta GitHub excede limite.")
    try:
        return json.loads(result.stdout)
    except (ValueError, TypeError):
        raise DeliveryError("Resposta GitHub inválida.") from None


def _blob(config, path, sha):
    _require(config.get("repository") == REPOSITORY, "Repositório não autorizado.")
    _safe_source_path(path, remote=True)
    allowed = {s["path"] for s in _sources(config) if s["kind"] == "github"}
    _require(path in allowed or path in {MONITOR, BRIDGE}, "Blob fora das fontes permitidas.")
    _require(re.fullmatch(r"[0-9a-f]{40}", sha), "SHA de blob inválido.")
    return _request("repos/" + REPOSITORY + "/git/blobs/" + sha)


def _remote(config, path, missing_ok=False):
    obj = _gh(config, path)
    if obj is None:
        _require(missing_ok, "Documento GitHub ausente.")
        return None
    _require(obj.get("type") == "file" and obj.get("size", MAX_FILE+1) <= MAX_FILE, "Documento GitHub fora do formato permitido.")
    expected_sha = obj.get("sha", "")
    expected_size = obj["size"]
    if obj.get("encoding") == "none" or (not obj.get("content") and expected_size):
        obj = _blob(config, path, expected_sha)
        _require(isinstance(obj, dict) and obj.get("sha") == expected_sha and obj.get("size") == expected_size, "Blob GitHub não corresponde à fonte indexada.")
    _require(obj.get("encoding") == "base64", "GitHub não forneceu conteúdo integral.")
    try:
        raw = base64.b64decode(obj["content"], validate=False)
        content = raw.decode("utf-8")
    except (ValueError, UnicodeError, KeyError):
        raise DeliveryError("Documento GitHub não é texto válido.") from None
    _require(len(raw) <= MAX_FILE and re.fullmatch(r"[0-9a-f]{40,64}", obj.get("sha", "")), "Documento GitHub inválido.")
    _require(len(raw) == expected_size, "Conteúdo GitHub incompleto; rodada suspensa.")
    if "type" not in obj:
        git_sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        _require(git_sha == expected_sha, "Hash do blob GitHub não confere.")
    return {"content": _safe_text(content), "sha": obj["sha"]}


def _put(config, path, content, sha=None):
    _safe_text(content)
    payload = {"message": "AST: recibo da ronda horária", "branch": "main", "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    _gh(config, path, "PUT", payload)
    check = _remote(config, path)
    _require(check["content"] == content, "Entrega GitHub não confirmada por leitura.")
    return check["sha"]


def _append_once(config, path, marker, block):
    for attempt in range(3):
        old = _remote(config, path)
        if marker in old["content"]:
            return old["sha"]
        try:
            return _put(config, path, old["content"] + "\n\n" + block.rstrip() + "\n", old["sha"])
        except Conflict:
            if attempt == 2:
                raise DeliveryError("Três conflitos de registro; não forcei a ponte.") from None


def _collision(monitor, task, own_marker=None):
    terms = [str(t).casefold() for t in task.get("ownership_terms", []) if str(t).strip()]
    for line in monitor.splitlines():
        lower = line.casefold()
        if own_marker and own_marker in line:
            continue
        if ("em andamento" in lower or "🔄" in line) and any(term in lower for term in terms):
            # A completed row may retain historical words; its final status wins.
            last_cell = line.rstrip(" | ").split("|")[-1]
            if "✅" not in last_cell:
                return True
    return False


def _latest(config):
    folder = _private_subdir(config, "delivery_reports")
    latest = {}
    progress_counts = {}
    for path in sorted(folder.glob("*.json")):
        record = _read_json(path)
        report = record.get("report", {})
        task_id = report.get("task_id")
        operational_pause = (
            report.get("title") == "Rodada interrompida com segurança"
            and report.get("report_markdown", "").startswith(
                "O executor parou sem repetir a operação. Código para revisão técnica: "
            )
        )
        if task_id and report.get("status") == "progress" and not operational_pause:
            counter = progress_counts.setdefault(task_id, {})
            fingerprint = record.get("fingerprint")
            counter[fingerprint] = counter.get(fingerprint, 0) + 1
        if task_id and (task_id not in latest or record.get("finished_at", "") > latest[task_id].get("finished_at", "")):
            latest[task_id] = record
    for task_id, record in latest.items():
        record["_progress_counts"] = progress_counts.get(task_id, {})
    return latest


def _tutor_guidance(content):
    """Only canonical tutor-authored blocks; own receipts cannot reopen tasks.

    This digest detects new guidance, NEVER parses or grants authorization.
    """
    collected, active = [], False
    tutor_header = re.compile(r"^\[[^\n\]]{1,100}\]\s+(?:DS-N Chefe|DSN-Chefe|DS Nuvem Chefe)\b", re.IGNORECASE)
    any_header = re.compile(r"^(?:\[[^\n\]]{1,100}\]\s+|#{1,6}\s+|<!-- AST-RONDA)")
    for line in content.splitlines():
        if tutor_header.search(line):
            active = True
        elif any_header.search(line):
            active = False
        if active:
            collected.append(line)
    return "\n".join(collected).strip()


def collect_sources(config):
    documents, notices, all_current = [], [], True
    full = {}
    for source in _sources(config):
        path = source["path"]
        try:
            if source["kind"] == "github":
                item = _remote(config, path)
            else:
                p = Path(path)
                _require(p.stat().st_size <= MAX_FILE, "Documento local excede limite.")
                content = _safe_text(p.read_text(encoding="utf-8"))
                item = {"content": content, "sha": _digest(content)}
            content = item["content"]
            full[path] = content
            limit = source.get("max_chars", 30000)
            _require(isinstance(limit, int) and 100 <= limit <= MAX_FILE, "Limite de fonte inválido.")
            critical = source.get("must_complete", False) or source.get("full", False) or source.get("critical", False) or any(term in Path(path).name.upper() for term in ("CONTRATO_MINUTA", "CONSTITUTION", "CONSTITUICAO", "MEMORY", "AGENTS.MD"))
            truncated = len(content) > limit
            _require(not (critical and truncated), "Instrução obrigatória excede contexto; rodada suspensa.")
            visible = content
            if truncated and Path(path).name == "MONITORAMENTO_DE_TRABALHO.md":
                visible = "[INÍCIO PARCIAL; restante omitido; colisões avaliadas no documento integral]\n" + content[:limit]
            elif truncated:
                visible = "[CAUDA PARCIAL; início omitido; não é leitura integral]\n" + content[-limit:]
            documents.append({"path": path, "content": visible, "sha": item["sha"], "truncated": truncated, "full_chars": len(content), "collected_at": _now()})
        except (DeliveryError, OSError, UnicodeError):
            notices.append("Não foi possível ler integralmente uma fonte " + ("obrigatória." if source.get("required", True) else "opcional."))
            if source.get("required", True):
                all_current = False
    latest = _latest(config)
    selected = {"id": "NONE", "title": "Nenhuma tarefa liberada com novidade"}
    monitor = full.get(MONITOR, "")
    tutor_digest = _digest(_tutor_guidance(full.get(BRIDGE, "")))
    if MONITOR not in full:
        all_current = False
        notices.append("Monitor atual ausente; não iniciar trabalho.")
    if all_current:
        for configured in config.get("tasks", []):
            task = dict(configured)
            _require(ID_RE.fullmatch(task.get("id", "")) and isinstance(task.get("title"), str), "Tarefa configurada inválida.")
            if _collision(monitor, task):
                notices.append("Tarefa " + task["id"] + ": responsável já ativo; coordenar pela ponte antes de executar.")
                continue
            paths = task.get("sources") or [p for p in full if "MONITORAMENTO" not in p and "ponte_" not in p and "RETOMADA" not in p.upper() and "/Relatorios/" not in p]
            _require(all(p in full for p in paths), "Fonte de tarefa ausente do snapshot.")
            # Only subject documents count, never own monitor or bridge append.
            paths = [p for p in paths if p != MONITOR and "ponte_laura_completa/" not in p and "/Relatorios/astra/" not in p]
            fingerprint = _digest(json.dumps([(p, _digest(full[p])) for p in sorted(paths)] + [("TUTORIA_DSN", tutor_digest)], ensure_ascii=False))
            previous = latest.get(task["id"])
            if previous and previous.get("fingerprint") == fingerprint and previous.get("report", {}).get("status") in {"completed", "needs_review", "no_change"}:
                continue
            if previous and previous.get("_progress_counts", {}).get(fingerprint, 0) >= 3:
                notices.append("Tarefa " + task["id"] + ": três avanços sobre os mesmos dados; aguardo nova evidência ou orientação do tutor.")
                continue
            task.update({"fingerprint": fingerprint, "source_paths": paths, "_all_current": True, "_collected_at": time.time()})
            if previous:
                documents.append({"path": "MEMORIA_DA_ULTIMA_RODADA_DESTA_TAREFA", "content": _safe_text(json.dumps(previous["report"], ensure_ascii=False)), "sha": _digest(json.dumps(previous["report"], sort_keys=True)), "truncated": False, "collected_at": previous["finished_at"]})
            selected = task
            break
    if selected.get("sources"):
        selected_paths = set(selected["sources"])
        common_paths = {s["path"] for s in config["sources"] if s.get("common", False)}
        documents = [d for d in documents if d["path"] in selected_paths | common_paths or d["path"] == "MEMORIA_DA_ULTIMA_RODADA_DESTA_TAREFA"]
    return {"documents": documents, "task": selected, "notices": notices, "all_current": all_current}


def reserve(config, run_id, task):
    _run_id(run_id)
    _require(task.get("id") != "NONE" and task.get("_all_current") is True and 0 <= time.time() - task.get("_collected_at", 0) < 600, "Reserva exige snapshot completo e recente.")
    marker = "<!-- AST-RONDA:" + run_id + " -->"
    title = _safe_text(task["title"]).replace("|", "/").replace("\n", " ")[:180]
    row = "| Astra — " + title + " " + marker + " | " + _now() + " | Documentos próprios; análise autorizada | 🔄 EM ANDAMENTO |"
    for attempt in range(3):
        old = _remote(config, MONITOR)
        if marker in old["content"]:
            return {"ok": False, "reason": "Rodada já registrada; não iniciar processamento duplicado."}
        if _collision(old["content"], task):
            return {"ok": False, "reason": "Responsável iniciou a tarefa após a coleta; rodada pulada."}
        text = old["content"] + "\n\n" + row + "\n"
        try:
            _put(config, MONITOR, text, old["sha"])
            return {"ok": True, "task": task, "row_marker": marker, "reserved_at": _now()}
        except Conflict:
            if attempt == 2:
                raise DeliveryError("Reserva não confirmada após três conflitos.") from None


def finish(config, run_id, handle, report):
    _run_id(run_id)
    _require(handle.get("ok") and report.get("task_id") == handle["task"]["id"], "Relatório não corresponde à tarefa reservada.")
    _require(report.get("status") in {"progress", "needs_review", "completed", "no_change"}, "Estado de relatório inválido.")
    title = _safe_text(report.get("title", "Resultado da ronda")).replace("\n", " ")[:180]
    body = _safe_text(report.get("report_markdown", ""))
    _require(len(body) <= 16000, "Relatório excede limite.")
    path = REPORT_ROOT + run_id + ".md"
    content = "# " + title + "\n\nRodada: " + run_id + "\nTarefa: " + report["task_id"] + "\nEstado: " + report["status"] + "\n\n" + body.rstrip() + "\n"
    old = _remote(config, path, missing_ok=True)
    if old is not None:
        _require(old["content"] == content, "Rodada já possui relatório diferente; não sobrescrevi.")
        report_sha = old["sha"]
    else:
        report_sha = _put(config, path, content)
    marker = handle["row_marker"]
    monitor_closed = False
    for attempt in range(3):
        monitor = _remote(config, MONITOR)
        lines = monitor["content"].splitlines(keepends=True)
        matches = [i for i, line in enumerate(lines) if marker in line]
        _require(len(matches) == 1, "Linha própria ausente ou duplicada; monitor não alterado.")
        i = matches[0]
        if "✅" in lines[i]:
            monitor_closed = True
            break
        _require("🔄 EM ANDAMENTO" in lines[i], "Estado da reserva mudou; revisão necessária.")
        lines[i] = lines[i].replace("🔄 EM ANDAMENTO", "✅ RODADA ENCERRADA — " + report["status"] + "; [relatório](" + path + ")")
        try:
            _put(config, MONITOR, "".join(lines), monitor["sha"])
            monitor_closed = True
            break
        except Conflict:
            if attempt == 2:
                raise DeliveryError("Relatório entregue; fechamento do monitor pendente por conflito.") from None
    bridge_recorded = False
    if report["status"] != "no_change":
        bridge_marker = "<!-- AST-RONDA-RESULTADO:" + run_id + " -->"
        block = bridge_marker + "\n\nAstra · rodada " + run_id + " · " + title + "\n\nEstado: " + report["status"] + ". [Relatório da análise](https://github.com/" + REPOSITORY + "/blob/main/" + path + ").\nSem publicação, limpeza, gasto novo ou alteração em produção. Registro informativo; não dispara conversa automática."
        _append_once(config, BRIDGE, bridge_marker, block)
        bridge_recorded = True
    record = {"run_id": run_id, "finished_at": _now(), "fingerprint": handle["task"].get("fingerprint"), "report": report, "report_path": path, "report_sha": report_sha, "monitor_closed": monitor_closed, "bridge_recorded": bridge_recorded}
    local = _private_subdir(config, "delivery_reports") / (run_id + ".json")
    try:
        _new_json(local, record)
    except FileExistsError:
        _require(_read_json(local).get("report") == report, "Recibo local conflitante; não sobrescrevi.")
    return {"ok": True, "report_path": path, "report_sha": report_sha, "monitor_closed": monitor_closed, "bridge_recorded": bridge_recorded, "bridge_skipped": report["status"] == "no_change"}


def _telegram():
    # Direct runner.py invocation does not put the workspace root on sys.path.
    # Only this fixed, local repository is added; no path from model output.
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from ponte_astra.bridge import credentials
    return credentials(SimpleNamespace(env_file=[], chat_id=None, sender_id=None))[:2]


def notify(config, run_id, report):
    _run_id(run_id)
    message = report.get("notification", "")
    if not message or report.get("status") == "no_change":
        return {"status": "silent"}
    _safe_text(message)
    key = report.get("notification_key", "")
    _require(KEY_RE.fullmatch(key), "Chave de aviso inválida.")
    _require(len(message) <= 1800, "Aviso excede limite.")
    # Plain text: no Markdown parsing or untrusted recipient supplied by the model.
    message = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", message)
    message = message.replace("**", "").replace("`", "").strip()
    folder = _private_subdir(config, "delivery_notifications")
    key_digest = _digest(key)
    text_digest = _digest(" ".join(message.casefold().split()))
    paths = [folder / ("run_" + run_id + ".json"), folder / ("key_" + key_digest + ".json"), folder / ("text_" + text_digest + ".json")]
    if any(path.exists() for path in paths):
        return {"status": "duplicate"}
    claim = {"run_id": run_id, "claimed_at": _now(), "key_sha256": key_digest, "text_sha256": text_digest, "status": "send_unknown"}
    try:
        for path in paths:
            _new_json(path, claim)
    except FileExistsError:
        return {"status": "duplicate"}
    result = {"status": "send_unknown"}
    try:
        tg, chat = _telegram()
        _require(tg.call("getMe").get("username", "").casefold() == "astrarevolution_bot", "Identidade do bot divergente.")
        message_id = tg.send(chat, message + "\n\nAstra · " + run_id)
        result = {"status": "sent", "message_id": message_id}
    except Exception:
        # A timeout after send is ambiguous. Never retry automatically.
        pass
    _new_json(folder / ("receipt_" + run_id + ".json"), {"run_id": run_id, "at": _now(), **result})
    return result
