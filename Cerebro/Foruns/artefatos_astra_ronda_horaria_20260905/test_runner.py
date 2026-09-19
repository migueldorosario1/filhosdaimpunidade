"""Offline safety tests. No real model, network, scheduler or bot is invoked."""
from __future__ import annotations

from datetime import datetime, timedelta
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

try:
    from . import runner
except ImportError:
    import runner


def at(value="2026-09-05T08:00:00-03:00"):
    return datetime.fromisoformat(value)


def report(notification="Resultado novo para Miguel.", key="p01-conclusion-1", status="progress"):
    return {"title": "Análise concluída", "task_id": "P01", "status": status,
            "report_markdown": "Conferi somente as informações fornecidas, sem alterar sistemas.",
            "notification": notification, "notification_key": key}


class FakeDelivery:
    def __init__(self, config):
        self.config = config
        self.calls = {name: 0 for name in ("collect", "reserve", "finish", "notify")}
        self.finish_error = False
        self.notify_error = False
        self.incomplete = False
        self.no_task = False
        self.reserve_rejected = False

    def collect_sources(self, config):
        self.calls["collect"] += 1
        return {"all_current": not self.incomplete, "notices": [],
                "documents": [{"path": config["sources"][0]["path"], "content": "Regra: análise somente.",
                               "sha": "abc", "truncated": False}],
                "task": {"id": "NONE" if self.no_task else "P01", "title": "Análise", "fingerprint": "abc"}}

    def reserve(self, config, run_id, task):
        self.calls["reserve"] += 1
        return {"ok": not self.reserve_rejected, "task": task, "run_id": run_id}

    def finish(self, config, run_id, handle, result):
        self.calls["finish"] += 1
        if self.finish_error:
            raise RuntimeError("Simulated uncertain write; not provider output")
        return {"ok": True, "monitor_closed": True, "bridge_recorded": True}

    def notify(self, config, run_id, result):
        self.calls["notify"] += 1
        if self.notify_error:
            raise RuntimeError("Simulated uncertain delivery")
        return {"status": "sent", "message_id": 1}


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="astra-runner-test-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.prompt = self.base / "PROMPT.md"
        self.prompt.write_text("Responda JSON da tarefa reservada.", encoding="utf-8")
        self.source = self.base / "fonte.md"
        self.source.write_text("Análise permitida.", encoding="utf-8")
        self.config = {"version": 1, "enabled": True, "model": runner.MODEL,
                       "timezone": runner.TZ_NAME, "state_dir": str(self.base / "state"),
                       "prompt_file": str(self.prompt), "repository": runner.REPOSITORY,
                       "codex_binary": sys.executable,
                       "node_binary": sys.executable,
                       "sources": [{"kind": "local", "path": str(self.source)}],
                       "approvals": {who: {"approved": True, "reference": "fixture-offline"}
                                     for who in ("dsn", "zm")}}
        state_root = patch.object(runner, "STATE_ROOT", Path(self.config["state_dir"]))
        state_root.start()
        self.addCleanup(state_root.stop)
        self.delivery = FakeDelivery(self.config)
        self.inferences = 0
        self.answer = report()

    def inference(self, config, prompt, run_dir, task_id):
        self.inferences += 1
        self.assertEqual(task_id, "P01")
        return dict(self.answer), {"model": runner.MODEL, "tool_events": 0}

    def execute(self, current=None, **kwargs):
        return runner.execute(self.config, adapter=self.delivery, inference=self.inference,
                              clock=lambda: current or at(), **kwargs)

    def test_schedule_midnight_pause_and_resume(self):
        expectations = {
            "2026-09-05T00:00:00-03:00": True,
            "2026-09-05T00:02:59-03:00": True,
            "2026-09-05T00:03:00-03:00": False,
            "2026-09-05T01:00:00-03:00": False,
            "2026-09-05T07:59:59-03:00": False,
            "2026-09-05T08:00:00-03:00": True,
            "2026-09-05T23:00:00-03:00": True,
            "2026-09-06T03:00:00+00:00": True,
            "2026-09-06T04:00:00+00:00": False,
        }
        for value, expected in expectations.items():
            with self.subTest(time=value):
                self.assertEqual(runner.slot_for(at(value)) is not None, expected)
        self.assertEqual(runner.slot_for(at("2026-09-06T03:00:00+00:00")), "2026-09-06T00:00:00-03:00")

    def test_naive_timestamp_rejected(self):
        with self.assertRaisesRegex(runner.SafeError, "timezone_required"):
            runner.slot_for(datetime(2026, 9, 5, 8))

    def test_next_calendar_slot(self):
        self.assertEqual(runner.iso(runner.next_slot(at("2026-09-05T00:01:00-03:00"))), "2026-09-05T08:00:00-03:00")
        self.assertEqual(runner.iso(runner.next_slot(at("2026-09-05T23:59:00-03:00"))), "2026-09-06T00:00:00-03:00")
        self.assertEqual(runner.iso(runner.next_slot(at(), at("2026-09-05T14:01:00-03:00"))), "2026-09-05T15:00:00-03:00")

    def test_disabled_configuration_fails_closed(self):
        self.config["enabled"] = False
        self.assertEqual(self.execute()["reason"], "configuration_disabled")
        self.assertEqual(self.inferences, 0)
        self.assertEqual(self.delivery.calls["collect"], 0)

    def test_both_review_references_are_required(self):
        for who in ("dsn", "zm"):
            self.config["approvals"][who]["reference"] = ""
            self.assertEqual(self.execute()["reason"], "reviews_required")
            self.config["approvals"][who]["reference"] = "fixture-offline"
        self.config["approvals"]["dsn"]["approved"] = "true"
        self.assertEqual(self.execute()["reason"], "reviews_required")
        self.assertEqual(self.inferences, 0)

    def test_late_start_is_skipped_without_replay(self):
        result = self.execute(at("2026-09-05T08:03:00-03:00"))
        self.assertEqual(result["reason"], "outside_start_window")
        self.assertEqual(self.inferences, 0)

    def test_slot_is_durable_before_inference_and_deduplicated(self):
        def check_then_infer(config, prompt, run_dir, task_id):
            state = runner.read_state(Path(config["state_dir"]))
            self.assertEqual(state["slots"][runner.slot_for(at())]["status"], "started")
            return self.inference(config, prompt, run_dir, task_id)
        first = runner.execute(self.config, adapter=self.delivery, inference=check_then_infer, clock=at)
        second = self.execute()
        self.assertEqual(first["status"], "completed")
        self.assertEqual(second["reason"], "slot_already_attempted")
        self.assertEqual(self.inferences, 1)
        self.assertEqual(self.delivery.calls["reserve"], 1)

    def test_abandoned_started_slot_is_not_replayed(self):
        state = Path(self.config["state_dir"])
        runner.private_dir(state)
        data = runner.read_state(state)
        data["slots"][runner.slot_for(at())] = {"status": "started", "run_id": "abandoned"}
        runner.save_state(state, data)
        self.assertEqual(self.execute()["reason"], "slot_already_attempted")
        self.assertEqual(self.inferences, 0)

    def test_overlapping_process_is_skipped(self):
        state = Path(self.config["state_dir"])
        runner.private_dir(state)
        script = ("import fcntl, pathlib, sys; "
                  "p=pathlib.Path(sys.argv[1]); f=p.open('a'); "
                  "fcntl.flock(f, fcntl.LOCK_EX); print('locked', flush=True); sys.stdin.readline()")
        process = subprocess.Popen([sys.executable, "-c", script, str(state / "runner.lock")],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        try:
            self.assertEqual(process.stdout.readline().strip(), "locked")
            self.assertEqual(self.execute()["reason"], "previous_round_active")
        finally:
            process.communicate("release\n", timeout=5)
        self.assertEqual(self.inferences, 0)

    def test_test_live_is_isolated_and_does_not_authorize_recurring(self):
        self.config["enabled"] = False
        self.config["approvals"] = {}
        result = self.execute(test_live=True)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(self.inferences, 1)
        self.assertEqual(self.delivery.calls, {"collect": 1, "reserve": 0, "finish": 0, "notify": 0})
        self.assertEqual(runner.read_state(Path(self.config["state_dir"]))["slots"], {})
        self.assertFalse(self.config["enabled"])

    def test_no_task_does_not_call_model_or_register_fake_work(self):
        self.delivery.no_task = True
        self.assertEqual(self.execute()["status"], "no_task")
        self.assertEqual(self.inferences, 0)
        self.assertEqual(self.delivery.calls["reserve"], 0)

    def test_incomplete_snapshot_blocks_inference(self):
        self.delivery.incomplete = True
        result = self.execute()
        self.assertEqual(result["reason"], "snapshot_incomplete")
        self.assertEqual(self.inferences, 0)
        self.assertEqual(self.delivery.calls["reserve"], 0)

    def test_collision_blocks_model(self):
        self.delivery.reserve_rejected = True
        self.assertEqual(self.execute()["reason"], "task_reservation_rejected")
        self.assertEqual(self.inferences, 0)

    def test_snapshot_cannot_add_a_model_selected_source(self):
        snapshot = self.delivery.collect_sources(self.config)
        snapshot["documents"][0]["path"] = "https://example.invalid/unapproved"
        with self.assertRaisesRegex(runner.SafeError, "snapshot_source_not_allowed"):
            runner.build_prompt(self.config, snapshot)

    def test_source_allowlist_rejects_credentials_and_traversal(self):
        for source in ({"kind": "github", "path": "cerebro/../secret.md"},
                       {"kind": "local", "path": "/example/cofre/secret.json"},
                       {"kind": "github", "path": "other/README.md"}):
            self.config["sources"] = [source]
            with self.assertRaises(runner.SafeError):
                runner.validate_config(self.config)

    def test_environment_removes_api_keys_tokens_and_proxies(self):
        source = {"HOME": "/safe", "PATH": "/bin", "LANG": "pt_BR.UTF-8",
                  "OPENAI_API_KEY": "fixture", "ANTHROPIC_API_KEY": "fixture", "GH_TOKEN": "fixture",
                  "TELEGRAM_TOKEN_ASTRA": "fixture", "HTTPS_PROXY": "fixture", "CODEX_HOME": "fixture"}
        self.assertEqual(runner.child_environment(source), {"HOME": "/safe", "PATH": "/bin", "LANG": "pt_BR.UTF-8"})

    def test_command_fixes_model_subscription_and_disables_all_tools(self):
        command = runner.model_command(self.config, self.base)
        self.assertEqual(command[command.index("-m") + 1], "gpt-6-astra")
        self.assertIn("--strict-config", command)
        self.assertIn("--ignore-user-config", command)
        self.assertIn("--ephemeral", command)
        self.assertEqual(command[command.index("--sandbox") + 1], "read-only")
        settings = {command[i + 1].split("=", 1)[0]: json.loads(command[i + 1].split("=", 1)[1])
                    for i, value in enumerate(command[:-1]) if value == "-c"}
        self.assertEqual(settings["forced_login_method"], "chatgpt")
        self.assertEqual(settings["model_provider"], "openai")
        self.assertTrue(all(value is False for key, value in settings.items() if key.startswith("features.")))
        self.assertEqual(settings["web_search"], "disabled")
        self.assertEqual(command[-1], "-")

    def test_model_or_timezone_change_is_rejected(self):
        self.config["model"] = "some-other-model"
        with self.assertRaisesRegex(runner.SafeError, "model_or_timezone_mismatch"):
            runner.validate_config(self.config)

    def test_state_must_be_exact_private_directory_without_symlinks(self):
        for value in ("/", str(Path.home()), str(self.base), str(self.base / "different-state")):
            self.config["state_dir"] = value
            with self.assertRaisesRegex(runner.SafeError, "state_directory_not_allowed"):
                runner.validate_config(self.config)
        self.config["state_dir"] = str(self.base / "state")
        destination = self.base / "unrelated"
        destination.mkdir()
        Path(self.config["state_dir"]).symlink_to(destination, target_is_directory=True)
        with self.assertRaisesRegex(runner.SafeError, "state_symlink_not_allowed"):
            runner.validate_config(self.config)

    def test_explicit_node_launcher_does_not_depend_on_cron_path(self):
        with patch.dict(os.environ, {"PATH": "/usr/bin:/bin"}, clear=True):
            command = runner.model_command(self.config, self.base)
        self.assertEqual(command[:2], [sys.executable, sys.executable])

    def test_chatgpt_login_required_before_inference(self):
        fake = subprocess.CompletedProcess([], 0, "Logged in using an API key", "")
        with patch.object(runner.subprocess, "run", return_value=fake):
            with self.assertRaisesRegex(runner.SafeError, "chatgpt_login_not_confirmed"):
                runner.confirm_subscription(self.config)

    def test_report_parse_rejects_invalid_json_fields_and_task(self):
        for content, reason in (("plain text", "report_not_json"),
                                (json.dumps({**report(), "shell": "forbidden"}), "report_schema_invalid"),
                                (json.dumps({**report(), "task_id": "P99"}), "report_task_or_status_invalid"),
                                (json.dumps(report(status="no_change")), "notification_invalid")):
            with self.subTest(reason=reason), self.assertRaisesRegex(runner.SafeError, reason):
                runner.parse_report(content, "P01")

    def test_sensitive_input_and_output_are_blocked(self):
        fake_secret = "123456789:" + "a" * 35
        snapshot = self.delivery.collect_sources(self.config)
        snapshot["documents"][0]["content"] = fake_secret
        with self.assertRaisesRegex(runner.SafeError, "sensitive_input_blocked"):
            runner.build_prompt(self.config, snapshot)
        with self.assertRaisesRegex(runner.SafeError, "sensitive_output_blocked"):
            runner.parse_report(json.dumps({**report(), "notification": fake_secret}), "P01")

    def test_unexpected_tool_events_fail_closed(self):
        telemetry = {"tool_events": 0}
        runner.observe_event({"type": "item.started", "item": {"type": "command_execution"}}, telemetry, [""])
        with self.assertRaisesRegex(runner.SafeError, "unexpected_tool_event"):
            runner.classify_result(0, telemetry, "")

    def test_limit_and_failed_completion_classification(self):
        for returncode, telemetry, diagnostic, expected in (
            (1, {}, "Usage limit exceeded", "subscription_limit"),
            (0, {"turn_failed": True}, "capacity", "subscription_limit"),
            (1, {}, "other failure", "inference_failed"),
            (0, {}, "", "inference_completion_missing"),
        ):
            with self.subTest(expected=expected), self.assertRaisesRegex(runner.SafeError, expected):
                runner.classify_result(returncode, telemetry, diagnostic)

    def test_limit_records_six_hour_pause_without_retry(self):
        def limited(*args):
            self.inferences += 1
            raise runner.SafeError("subscription_limit")
        first = runner.execute(self.config, adapter=self.delivery, inference=limited, clock=at)
        second = self.execute(at("2026-09-05T09:00:00-03:00"))
        self.assertEqual(first["paused_until"], "2026-09-05T14:00:00-03:00")
        self.assertEqual(second["reason"], "subscription_pause")
        self.assertEqual(self.inferences, 1)
        self.assertEqual(self.delivery.calls["finish"], 1)

    def test_inference_failure_closes_task_and_never_repeats_slot(self):
        def failed(*args):
            self.inferences += 1
            raise runner.SafeError("report_not_json")
        first = runner.execute(self.config, adapter=self.delivery, inference=failed, clock=at)
        self.assertEqual(first["reason"], "report_not_json")
        self.assertEqual(self.delivery.calls["finish"], 1)
        self.assertEqual(self.execute()["reason"], "slot_already_attempted")
        self.assertEqual(self.delivery.calls["notify"], 0)

    def test_timeout_stops_only_the_readonly_child(self):
        run_dir = self.base / "timeout"
        runner.private_dir(run_dir)
        command = [sys.executable, "-c", "import time; time.sleep(60)"]
        with patch.object(runner, "confirm_subscription"), patch.object(runner, "model_command", return_value=command), \
                patch.object(runner, "MAX_INFERENCE_SECONDS", 0.15):
            with self.assertRaisesRegex(runner.SafeError, "inference_timeout"):
                runner.infer(self.config, "safe fixture", run_dir, "P01")
        telemetry = json.loads((run_dir / "model_telemetry.json").read_text())
        self.assertIsNotNone(telemetry["exit_code"])
        self.assertLess(telemetry["duration_seconds"], 10)

    def test_no_new_operation_at_fifty_minutes_or_next_hour(self):
        self.assertTrue(runner.before_new_operation(at(), at("2026-09-05T08:49:59-03:00")))
        self.assertFalse(runner.before_new_operation(at(), at("2026-09-05T08:50:00-03:00")))
        self.assertFalse(runner.before_new_operation(at(), at("2026-09-05T09:00:00-03:00")))
        self.assertFalse(runner.before_new_operation(at("2026-09-05T00:00:00-03:00"), at("2026-09-05T01:00:00-03:00")))
        self.assertTrue(runner.before_inference(at(), at("2026-09-05T08:25:59-03:00")))
        self.assertFalse(runner.before_inference(at(), at("2026-09-05T08:26:00-03:00")))
        self.assertFalse(runner.before_inference(at("2026-09-05T00:00:00-03:00"), at("2026-09-05T00:35:00-03:00")))

    def test_inherited_lock_survives_wrapper_death(self):
        child_path = self.base / "child.pid"
        script = """
import json, os, pathlib, sys
import runner
from test_runner import FakeDelivery, at
config = json.loads(sys.argv[1])
runner.STATE_ROOT = pathlib.Path(config['state_dir'])
runner.confirm_subscription = lambda config: None
child_script = 'import os,pathlib,sys,time; pathlib.Path(sys.argv[1]).write_text(str(os.getpid())); time.sleep(60)'
runner.model_command = lambda config, run_dir: [sys.executable, '-c', child_script, sys.argv[2]]
runner.execute(config, adapter=FakeDelivery(config), clock=at)
"""
        wrapper = subprocess.Popen([sys.executable, "-c", script, json.dumps(self.config), str(child_path)],
                                   cwd=runner.ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        child_pid = None
        try:
            deadline = time.monotonic() + 5
            while time.monotonic() < deadline and not child_path.exists():
                time.sleep(0.02)
            self.assertTrue(child_path.exists())
            child_pid = int(child_path.read_text())
            wrapper.kill()
            wrapper.wait(timeout=5)
            self.assertEqual(self.execute(at("2026-09-05T09:00:00-03:00"))["reason"], "previous_round_active")
        finally:
            if wrapper.poll() is None:
                wrapper.kill()
                wrapper.wait(timeout=5)
            if child_pid is not None:
                try:
                    os.kill(child_pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass

    def test_no_change_has_no_telegram_notification(self):
        self.answer = report("", "", "no_change")
        self.assertEqual(self.execute()["status"], "completed")
        self.assertEqual(self.delivery.calls["notify"], 0)

    def test_notification_deduplicates_key_and_normalized_text(self):
        self.execute()
        self.execute(at("2026-09-05T09:00:00-03:00"))
        self.answer["notification_key"] = "new-key-same-message"
        self.answer["notification"] = "  RESULTADO novo  para Miguel. "
        self.execute(at("2026-09-05T10:00:00-03:00"))
        self.assertEqual(self.inferences, 3)
        self.assertEqual(self.delivery.calls["notify"], 1)

    def test_ambiguous_notification_is_not_retried(self):
        self.delivery.notify_error = True
        self.assertEqual(self.execute()["status"], "failed")
        self.delivery.notify_error = False
        self.execute(at("2026-09-05T09:00:00-03:00"))
        self.assertEqual(self.delivery.calls["notify"], 1)

    def test_ambiguous_finish_is_not_retried(self):
        self.delivery.finish_error = True
        result = self.execute()
        self.assertEqual(result["status"], "failed")
        self.assertEqual(self.delivery.calls["finish"], 1)
        self.assertEqual(self.delivery.calls["notify"], 0)

    def test_private_logs_and_reports(self):
        result = self.execute()
        state = Path(self.config["state_dir"])
        self.assertEqual(state.stat().st_mode & 0o777, 0o700)
        path = state / "runs" / result["run_id"] / "report.json"
        self.assertEqual(path.stat().st_mode & 0o777, 0o600)
        self.assertEqual(path.parent.stat().st_mode & 0o777, 0o700)
        self.assertEqual((state / "runner_state.json").stat().st_mode & 0o777, 0o600)

    def test_status_does_not_claim_scheduler_or_readiness(self):
        self.config["enabled"] = False
        result = runner.status(self.config, at())
        self.assertFalse(result["recurring_allowed_by_config"])
        self.assertIsNone(result["next_eligible_slot"])
        self.assertEqual(result["scheduler_installed"], "not_checked")
        self.assertFalse(result["telegram_service_touched"])

    def test_integrated_delivery_progress_memory_and_no_change(self):
        try:
            from . import delivery
        except ImportError:
            import delivery
        brain = self.base / "Cerebro"
        brain.mkdir()
        source = brain / "FONTE.md"
        source.write_text("Fonte permitida e inalterada de análise.", encoding="utf-8")
        self.config["sources"] = [
            {"kind": "local", "path": str(source)},
            {"kind": "github", "path": delivery.MONITOR, "common": True},
            {"kind": "github", "path": delivery.BRIDGE, "common": True},
        ]
        self.config["tasks"] = [{"id": "P01", "title": "Análise independente", "sources": [str(source)],
                                 "ownership_terms": ["Análise independente"]}]
        database = {delivery.MONITOR: "| Agente | Data | Escopo | Estado |\n|---|---|---|---|\n",
                    delivery.BRIDGE: "# Canal de teste offline\n"}

        def remote(config, path, missing_ok=False):
            if path not in database:
                if missing_ok:
                    return None
                raise AssertionError("Fonte ausente na simulação")
            return {"content": database[path], "sha": "a" * 40}

        def put(config, path, content, sha=None):
            database[path] = content
            return "b" * 40

        prompts = []

        def inference(config, prompt, run_dir, task_id):
            prompts.append(prompt)
            return self.inference(config, prompt, run_dir, task_id)

        with patch.object(delivery, "ROOT", self.base), patch.object(delivery, "STATE_ROOT", self.base), \
                patch.object(delivery, "_remote", side_effect=remote), patch.object(delivery, "_put", side_effect=put), \
                patch.object(delivery, "_request", side_effect=AssertionError("Network prohibited in test")), \
                patch.object(delivery, "_telegram", side_effect=AssertionError("Telegram prohibited in test")), \
                patch.object(delivery, "notify", return_value={"status": "sent", "message_id": 1}) as notification:
            first = runner.execute(self.config, adapter=delivery, inference=inference, clock=at)
            second = runner.execute(self.config, adapter=delivery, inference=inference,
                                    clock=lambda: at("2026-09-05T09:00:00-03:00"))
            self.assertEqual(first["status"], "completed", first)
            self.assertEqual(second["status"], "completed", second)
            self.assertIn(runner.PREVIOUS_REPORT_ID, prompts[1])
            self.assertEqual(notification.call_count, 1)
            self.answer = report("", "", "no_change")
            third = runner.execute(self.config, adapter=delivery, inference=inference,
                                   clock=lambda: at("2026-09-05T10:00:00-03:00"))
            fourth = runner.execute(self.config, adapter=delivery, inference=inference,
                                    clock=lambda: at("2026-09-05T11:00:00-03:00"))
        self.assertEqual(third["status"], "completed", third)
        self.assertEqual(third["report_status"], "no_change")
        self.assertEqual(fourth["status"], "no_task", fourth)
        self.assertEqual(self.inferences, 3)
        self.assertNotIn("🔄 EM ANDAMENTO", database[delivery.MONITOR])
        self.assertEqual(database[delivery.BRIDGE].count("AST-RONDA-RESULTADO:"), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
