"""Offline delivery tests; every GitHub/Telegram operation is mocked."""
import base64
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch, Mock

from astra_operacoes.ronda_horaria import delivery as d


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="astra_delivery_test_")
        self.root = Path(self.temp.name)
        self.patches = [patch.object(d, "ROOT", self.root), patch.object(d, "STATE_ROOT", self.root / "astra_operacoes/state")]
        for p in self.patches:
            p.start()
        self.config = {
            "repository": d.REPOSITORY,
            "state_dir": str(self.root / "astra_operacoes/state/hourly"),
            "sources": [
                {"kind": "github", "path": d.MONITOR, "max_chars": 1000, "required": True, "common": True},
                {"kind": "github", "path": d.BRIDGE, "max_chars": 1000, "required": True, "common": True},
                {"kind": "github", "path": "cerebro/Dados/assunto.md", "max_chars": 1000, "required": True},
            ],
            "tasks": [{"id": "P01", "title": "Reconciliar evidências", "ownership_terms": ["reconciliação financeira"], "sources": ["cerebro/Dados/assunto.md"]}],
        }
        self.files = {d.MONITOR: "# Monitor\n\n| Outro agente | tarefa distinta | 🔄 EM ANDAMENTO |\n", d.BRIDGE: "# Ponte do Astra\n", "cerebro/Dados/assunto.md": "evidência A"}
        self.put_calls = []
        self.conflicts = 0
        self.fakegh = patch.object(d, "_gh", side_effect=self.gh)
        self.fakegh.start()

    def tearDown(self):
        self.fakegh.stop()
        for p in reversed(self.patches):
            p.stop()
        self.temp.cleanup()

    def sha(self, content):
        return hashlib.sha1(content.encode()).hexdigest()

    def gh(self, config, path, method="GET", payload=None):
        if method == "GET":
            if path not in self.files:
                return None
            content = self.files[path]
            return {"type": "file", "encoding": "base64", "size": len(content.encode()), "sha": self.sha(content), "content": base64.b64encode(content.encode()).decode()}
        self.put_calls.append((path, copy.deepcopy(payload)))
        if self.conflicts:
            self.conflicts -= 1
            self.files[path] += "\nMensagem simultânea do colega.\n"
            raise d.Conflict("conflito simulado")
        if path in self.files and payload.get("sha") != self.sha(self.files[path]):
            raise d.Conflict("SHA divergente")
        self.files[path] = base64.b64decode(payload["content"]).decode()
        return {"content": {"sha": self.sha(self.files[path])}}

    def report(self, status="completed"):
        return {"title": "Evidências conferidas", "task_id": "P01", "status": status, "report_markdown": "Análise feita; nenhum serviço alterado.", "notification": "Miguel, encontrei uma diferença para revisão.", "notification_key": "P01-evidencia-A"}

    def completed(self, status="completed", run="AST-20260905-1000"):
        snapshot = d.collect_sources(self.config)
        handle = d.reserve(self.config, run, snapshot["task"])
        result = d.finish(self.config, run, handle, self.report(status))
        return snapshot, handle, result

    def test_snapshot_and_truncated_tail(self):
        self.files[d.BRIDGE] += "x" * 1200
        result = d.collect_sources(self.config)
        self.assertTrue(result["all_current"])
        self.assertEqual(result["task"]["id"], "P01")
        bridge = next(x for x in result["documents"] if x["path"] == d.BRIDGE)
        self.assertTrue(bridge["truncated"])
        self.assertIn("CAUDA PARCIAL", bridge["content"])

    def test_large_github_blob_is_full_and_hash_verified(self):
        raw = b"x" * 1_100_000
        sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        metadata = {"type": "file", "encoding": "none", "content": "", "size": len(raw), "sha": sha}
        blob = {"encoding": "base64", "content": base64.b64encode(raw).decode(), "size": len(raw), "sha": sha}
        with patch.object(d, "_gh", return_value=metadata), patch.object(d, "_blob", return_value=blob) as getblob:
            result = d._remote(self.config, d.MONITOR)
            self.assertEqual(result["content"], raw.decode())
            getblob.assert_called_once_with(self.config, d.MONITOR, sha)
        blob["content"] = base64.b64encode(b"y" * len(raw)).decode()
        with patch.object(d, "_gh", return_value=metadata), patch.object(d, "_blob", return_value=blob), self.assertRaises(d.DeliveryError):
            d._remote(self.config, d.MONITOR)

    def test_context_only_common_and_selected_subject(self):
        self.config["sources"].append({"kind": "github", "path": "cerebro/Dados/outro.md", "max_chars": 1000})
        self.files["cerebro/Dados/outro.md"] = "tema distinto"
        paths = {x["path"] for x in d.collect_sources(self.config)["documents"]}
        self.assertNotIn("cerebro/Dados/outro.md", paths)
        self.assertIn(d.MONITOR, paths)

    def test_large_monitor_shows_current_head_but_collision_checks_full_text(self):
        self.files[d.MONITOR] = "# EM ANDAMENTO AGORA\n" + "histórico\n" * 1000
        result = d.collect_sources(self.config)
        monitor = next(x for x in result["documents"] if x["path"] == d.MONITOR)
        self.assertIn("INÍCIO PARCIAL", monitor["content"])
        self.assertIn("EM ANDAMENTO AGORA", monitor["content"])
        self.files[d.MONITOR] += "| ZM | reconciliação financeira | 🔄 EM ANDAMENTO |\n"
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "NONE")

    def test_missing_required_fails_closed(self):
        del self.files[d.BRIDGE]
        result = d.collect_sources(self.config)
        self.assertFalse(result["all_current"])
        self.assertEqual(result["task"]["id"], "NONE")

    def test_complete_instruction_cannot_be_truncated(self):
        self.config["sources"][2]["must_complete"] = True
        self.files["cerebro/Dados/assunto.md"] = "a" * 1100
        self.assertFalse(d.collect_sources(self.config)["all_current"])

    def test_active_owner_blocks_and_completed_owner_does_not(self):
        self.files[d.MONITOR] += "| ZM | reconciliação financeira | 🔄 EM ANDAMENTO |\n"
        result = d.collect_sources(self.config)
        self.assertEqual(result["task"]["id"], "NONE")
        self.assertTrue(result["notices"])
        self.files[d.MONITOR] = self.files[d.MONITOR].replace("reconciliação financeira | 🔄 EM ANDAMENTO", "reconciliação financeira antes EM ANDAMENTO | ✅ CONCLUÍDO")
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "P01")

    def test_owner_race_blocks_before_reservation(self):
        snapshot = d.collect_sources(self.config)
        self.files[d.MONITOR] += "| ZM | reconciliação financeira | 🔄 EM ANDAMENTO |\n"
        self.assertFalse(d.reserve(self.config, "AST-test", snapshot["task"])["ok"])
        self.assertEqual(self.put_calls, [])

    def test_reserve_retries_sha_preserves_colleague_and_is_idempotent(self):
        task = d.collect_sources(self.config)["task"]
        self.conflicts = 1
        result = d.reserve(self.config, "AST-test", task)
        self.assertTrue(result["ok"])
        self.assertIn("Mensagem simultânea do colega.", self.files[d.MONITOR])
        count = len(self.put_calls)
        self.assertFalse(d.reserve(self.config, "AST-test", task)["ok"])
        self.assertEqual(len(self.put_calls), count)
        self.assertEqual(self.files[d.MONITOR].count("<!-- AST-RONDA:AST-test -->"), 1)

    def test_three_conflicts_never_force(self):
        task = d.collect_sources(self.config)["task"]
        self.conflicts = 3
        with self.assertRaises(d.DeliveryError):
            d.reserve(self.config, "AST-test", task)
        self.assertEqual(len(self.put_calls), 3)

    def test_finish_closes_only_own_row_and_creates_receipts(self):
        old_line = self.files[d.MONITOR].splitlines()[2]
        snapshot, handle, result = self.completed()
        self.assertTrue(result["monitor_closed"])
        self.assertTrue(result["bridge_recorded"])
        self.assertIn(old_line, self.files[d.MONITOR])
        self.assertIn("✅ RODADA ENCERRADA", self.files[d.MONITOR])
        count = len(self.put_calls)
        d.finish(self.config, "AST-20260905-1000", handle, self.report())
        self.assertEqual(len(self.put_calls), count)

    def test_completed_and_needs_review_not_repeat_until_subject_changes(self):
        self.completed("needs_review")
        self.files[d.BRIDGE] += "\nAST: meu próprio registro novo.\n"
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "NONE")
        self.files["cerebro/Dados/assunto.md"] += "\nevidência B"
        result = d.collect_sources(self.config)
        self.assertEqual(result["task"]["id"], "P01")
        self.assertTrue(any(x["path"] == "MEMORIA_DA_ULTIMA_RODADA_DESTA_TAREFA" for x in result["documents"]))

    def test_new_tutor_guidance_reopens_but_own_receipt_does_not(self):
        self.files[d.BRIDGE] += "\n[05/09/2026 08:45 BRT] DS-N Chefe → Astra\nPriorize P01 sem produção.\n"
        self.completed("needs_review")
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "NONE")
        self.files[d.BRIDGE] += "\n<!-- AST-RONDA-RESULTADO:outro -->\nAstra: registro próprio novo.\n"
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "NONE")
        self.files[d.BRIDGE] += "\n[05/09/2026 11:45 BRT] DS-N Chefe → Astra\nConsidere a evidência complementar.\n"
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "P01")

    def test_append_preserves_existing_whitespace(self):
        old = "Histórico com espaços finais.   \n\n\n"
        self.files[d.BRIDGE] = old
        d._append_once(self.config, d.BRIDGE, "unique-marker", "unique-marker\ntexto")
        self.assertTrue(self.files[d.BRIDGE].startswith(old))

    def test_progress_receives_previous_report_and_can_advance(self):
        self.completed("progress")
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "P01")

    def test_three_progress_cap_excludes_operational_pause_and_new_inputs_reset(self):
        snapshot = d.collect_sources(self.config)
        handle = d.reserve(self.config, "AST-pause", snapshot["task"])
        paused = self.report("progress")
        paused.update({"title": "Rodada interrompida com segurança", "report_markdown": "O executor parou sem repetir a operação. Código para revisão técnica: rate_limit.", "notification": "", "notification_key": ""})
        d.finish(self.config, "AST-pause", handle, paused)
        for number in range(3):
            self.assertEqual(d.collect_sources(self.config)["task"]["id"], "P01")
            self.completed("progress", run="AST-progress-" + str(number))
        blocked = d.collect_sources(self.config)
        self.assertEqual(blocked["task"]["id"], "NONE")
        self.assertTrue(any("três avanços" in notice for notice in blocked["notices"]))
        self.files["cerebro/Dados/assunto.md"] += "\nNova evidência."
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "P01")
        self.files["cerebro/Dados/assunto.md"] = "evidência A"
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "NONE")
        self.files[d.BRIDGE] += "\n[05/09/2026 12:45 BRT] DS-N Chefe → Astra\nNova orientação de análise.\n"
        self.assertEqual(d.collect_sources(self.config)["task"]["id"], "P01")

    def test_no_change_records_report_but_no_bridge_message(self):
        _, _, result = self.completed("no_change")
        self.assertFalse(result["bridge_recorded"])
        self.assertEqual(self.files[d.BRIDGE], "# Ponte do Astra\n")

    def test_mismatched_report_refused(self):
        snapshot = d.collect_sources(self.config)
        handle = d.reserve(self.config, "AST-test", snapshot["task"])
        report = self.report()
        report["task_id"] = "P99"
        with self.assertRaises(d.DeliveryError):
            d.finish(self.config, "AST-test", handle, report)

    def test_auth_and_path_traversal_rejected(self):
        for path in ["cerebro/../auth.json", "cerebro/secrets/key.md", "cerebro/.env", "/etc/passwd", "cerebro/ponte_astra/state/inbox.json"]:
            with self.subTest(path=path), self.assertRaises(d.DeliveryError):
                d._safe_source_path(path, remote=True)
        with self.assertRaises(d.DeliveryError):
            d.reserve(self.config, "../../overwritten", {})
        self.config["repository"] = "someone/else"
        with self.assertRaises(d.DeliveryError):
            d.collect_sources(self.config)

    def test_local_symlink_and_state_escape_rejected(self):
        brain = self.root / "Cerebro"
        brain.mkdir()
        (brain / "linked.md").symlink_to("/etc/passwd")
        with self.assertRaises(d.DeliveryError):
            d._safe_source_path(str(brain / "linked.md"))
        self.config["state_dir"] = str(self.root / "outside")
        with self.assertRaises(d.DeliveryError):
            d.collect_sources(self.config)

    def test_secret_content_refused(self):
        self.files["cerebro/Dados/assunto.md"] = "token " + "123456789:" + "A" * 35
        self.assertFalse(d.collect_sources(self.config)["all_current"])

    def test_telegram_one_send_then_dedup(self):
        tg = Mock()
        tg.call.return_value = {"username": "astrarevolution_bot"}
        tg.send.return_value = 42
        with patch.object(d, "_telegram", return_value=(tg, 99)):
            self.assertEqual(d.notify(self.config, "AST-one", self.report()), {"status": "sent", "message_id": 42})
            self.assertEqual(d.notify(self.config, "AST-two", self.report())["status"], "duplicate")
        tg.send.assert_called_once()
        tg.call.assert_called_once_with("getMe")

    def test_telegram_ambiguous_does_not_retry(self):
        tg = Mock()
        tg.call.return_value = {"username": "astrarevolution_bot"}
        tg.send.side_effect = TimeoutError("simulated")
        with patch.object(d, "_telegram", return_value=(tg, 99)):
            self.assertEqual(d.notify(self.config, "AST-one", self.report())["status"], "send_unknown")
            self.assertEqual(d.notify(self.config, "AST-two", self.report())["status"], "duplicate")
        tg.send.assert_called_once()

    def test_wrong_bot_never_sends(self):
        tg = Mock()
        tg.call.return_value = {"username": "not_astra"}
        with patch.object(d, "_telegram", return_value=(tg, 99)):
            self.assertEqual(d.notify(self.config, "AST-one", self.report())["status"], "send_unknown")
        tg.send.assert_not_called()

    def test_gh_env_has_no_api_keys_and_write_scope_is_fixed(self):
        self.fakegh.stop()
        try:
            with patch.dict(os.environ, {"OPENAI_API_KEY": "fake", "GH_TOKEN": "fake", "HOME": str(self.root)}, clear=False), patch.object(subprocess, "run", return_value=SimpleResult()) as run:
                d._gh(self.config, d.MONITOR)
                env = run.call_args.kwargs["env"]
                self.assertNotIn("OPENAI_API_KEY", env)
                self.assertNotIn("GH_TOKEN", env)
                self.assertEqual(env["HOME"], str(self.root))
                with self.assertRaises(d.DeliveryError):
                    d._gh(self.config, "cerebro/Dados/assunto.md", "PUT", {})
        finally:
            self.fakegh.start()

    def test_direct_import_telegram_with_clean_environment_never_reads_credentials(self):
        actual_delivery = Path(d.__file__).resolve()
        script = '''import builtins, importlib.util, sys
spec = importlib.util.spec_from_file_location("delivery_standalone", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
original_import = builtins.__import__
def guarded_import(name, *args, **kwargs):
    imported = original_import(name, *args, **kwargs)
    if name == "ponte_astra.bridge":
        imported.credentials = lambda args: ("fake-telegram", 123, None)
    return imported
builtins.__import__ = guarded_import
assert module._telegram() == ("fake-telegram", 123)
print("offline import OK")
'''
        result = subprocess.run([sys.executable, "-I", "-c", script, str(actual_delivery)], cwd=self.root, env={"PATH": "/usr/bin:/bin", "HOME": str(self.root), "PYTHONNOUSERSITE": "1"}, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("offline import OK", result.stdout)


class SimpleResult:
    returncode = 0
    stdout = "{}"
    stderr = ""


if __name__ == "__main__":
    unittest.main()
