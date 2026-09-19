#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v42_autocura.py — Serviço de AUTOCURA do V4.2 Estatística (us65)
================================================================
Ordem do Miguel (03/09/2026 ~05h BRT): "cria um serviço de autocura para
aproveitar isso... o monitor que registra e faz exame bem legal para consertar".

Como funciona (cron */15, logo após o vigia):
  1. LÊ os vereditos novos do Vigia V4.2 (Foruns/v42_monitor/vereditos/, últimos 35 min).
  2. EXAME: veredito ALUCINOU, ou problema mecânico grave (número sem origem /
     moeda trocada / eco de título) = SEVERO.
  3. FILosofia do Miguel (03/09 ~05:1x BRT): "espelho é laboratório, não precisa
     ficar nervoso com despublicar — o importante é ANOTAR para entender o que
     aconteceu". Então o conserto automático é REGISTRO, não pânico:
     a. FICHA DE AUTOCURA no repo (Foruns/v42_monitor/autocura/fichas/) com o
        diagnóstico completo — é o registro que alimenta a próxima reforma;
     b. AVISO CALMO no Telegram do Miguel (post, problema, link) — sem vermelho;
     c. QUARENTENA fica DESLIGADA por padrão (só liga com V42_AUTOCURA_QUARENTENA=1
        e credencial — para uso em produção no futuro).
  4. SAÚDE DO PIPELINE: se passou das 13:10 BRT e não há post novo da
     Estatística há mais de 26h, aviso (ciclo do NYC travado) — 1×/dia.
  5. Idempotente: trata cada post UMA vez (autocura_estado.json).

Telemetria própria (DSC-052): /root/agent_data/v42_monitor/telemetry_autocura.jsonl
Não publica, não edita posts (até ter credencial), não mexe em credencial.
"""
import json
import os
import re
import time
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VEREDITOS = AQUI / "vereditos"
FICHAS = AQUI / "autocura" / "fichas"
ESTADO = Path("/root/agent_data/v42_monitor/autocura_estado.json")
TELEMETRIA = Path("/root/agent_data/v42_monitor/telemetry_autocura.jsonl")
LOGF = Path("/root/agent_data/v42_monitor/autocura.log")
ESPELHO = "https://cafezinho.news"
ZONA_BRT = timezone(timedelta(hours=-3))

SEVERO_MEC = re.compile(r"sem origem|série em euros|série em dólares|título em eco",
                        re.IGNORECASE)


def log(msg: str) -> None:
    try:
        LOGF.parent.mkdir(parents=True, exist_ok=True)
        with LOGF.open("a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%F %T')}] {msg}\n")
    except Exception:
        pass


def telemetria(evento: str, dados: dict) -> None:
    try:
        TELEMETRIA.parent.mkdir(parents=True, exist_ok=True)
        with TELEMETRIA.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": datetime.now(ZONA_BRT).isoformat(),
                                "agente": "v42_autocura", "evento": evento, **dados},
                               ensure_ascii=False) + "\n")
    except Exception:
        pass


def carregar_estado() -> dict:
    try:
        return json.loads(ESTADO.read_text(encoding="utf-8"))
    except Exception:
        return {"tratados": {}, "alerta_stall": ""}


def salvar_estado(est: dict) -> None:
    try:
        ESTADO.parent.mkdir(parents=True, exist_ok=True)
        tmp = ESTADO.with_suffix(".tmp")
        tmp.write_text(json.dumps(est, ensure_ascii=False), encoding="utf-8")
        tmp.replace(ESTADO)
    except Exception as exc:
        log(f"salvar_estado falhou: {exc}")


def telegram(msg: str) -> None:
    env = {}
    try:
        for ln in Path("/root/.env.unificado").read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, v = ln.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
        token, chat = env.get("TELEGRAM_TOKEN_DSC_BOT", ""), env.get("DSC_BOT_CHAT_ID", "")
        if not token or not chat:
            return
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=json.dumps({"chat_id": chat, "text": msg[:3900]}).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        urllib.request.urlopen(req, timeout=20)
    except Exception as exc:
        log(f"telegram falhou: {exc}")


def _env_espelho() -> dict:
    env = {}
    try:
        for ln in Path("/root/.env.unificado").read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln.startswith("ESPELHO_WP") and "=" in ln:
                k, v = ln.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    except Exception:
        pass
    return env


def _quarentena(post_id: int) -> str:
    """Despublica (post → draft) se houver credencial do espelho no cofre us65."""
    env = _env_espelho()
    rest = env.get("ESPELHO_WP_REST") or (env.get("ESPELHO_WP_SITE", "") + "/wp-json/wp/v2")
    user, senha = env.get("ESPELHO_WP_USER", ""), env.get("ESPELHO_WP_PASS", "")
    if not (rest and user and senha):
        return "pendente_credencial"
    import base64
    tok = base64.b64encode(f"{user}:{senha}".encode()).decode()
    req = urllib.request.Request(
        f"{rest.rstrip('/')}/posts/{post_id}",
        data=json.dumps({"status": "draft"}).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Basic {tok}"},
        method="POST")
    try:
        urllib.request.urlopen(req, timeout=25)
        return "em_quarentena"
    except Exception as exc:
        log(f"quarentena falhou p/ {post_id}: {exc}")
        return "falhou"


def ficha(post_id: int, veredito: Path, conteudo: str, acao: str) -> Path:
    FICHAS.mkdir(parents=True, exist_ok=True)
    data = datetime.now(ZONA_BRT).strftime("%Y-%m-%d")
    caminho = FICHAS / f"{data}_post{post_id}.md"
    caminho.write_text(
        f"# AUTOCURA V4.2 — post {post_id} ({data} {datetime.now(ZONA_BRT).strftime('%H:%M')} BRT)\n\n"
        f"- Veredito de origem: `{veredito.name}`\n"
        f"- Ação executada: **{acao}**\n"
        f"- Diagnóstico (extrato do veredito):\n\n> "
        + "\n> ".join(conteudo.splitlines()[:14])
        + "\n\n— Autocura V4.2 (robô DSC us65)\n", encoding="utf-8")
    return caminho


def examinar_vereditos(est: dict) -> None:
    agora = time.time()
    for v in sorted(VEREDITOS.glob("*.md")):
        try:
            if agora - v.stat().st_mtime > 35 * 60:
                continue
        except OSError:
            continue
        m = re.search(r"post (\d+)", v.name) or re.search(r"— post (\d+)", v.read_text(encoding="utf-8")[:200])
        if not m:
            continue
        pid = int(m.group(1))
        if pid in est["tratados"]:
            continue
        conteudo = v.read_text(encoding="utf-8")
        grave_mec = SEVERO_MEC.search(conteudo)
        alucinou = re.search(r"Veredito LLM: ALUCINOU", conteudo)
        if not (grave_mec or alucinou):
            est["tratados"][pid] = "ok"
            salvar_estado(est)
            continue
        # SEVERO → regitra (filosofia: ANOTAR p/ entender; espelho é laboratório)
        quarentena_on = os.environ.get("V42_AUTOCURA_QUARENTENA") == "1"
        acao = _quarentena(pid) if quarentena_on else "anotado (lab: sem quarentena)"
        cam = ficha(pid, v, conteudo, acao)
        est["tratados"][pid] = f"severo:{acao}"
        salvar_estado(est)
        telemetria("severo", {"post": pid, "acao": acao, "ficha": cam.name})
        problema = grave_mec.group(0) if grave_mec else "veredito LLM ALUCINOU"
        telegram("AUTOCURA V4.2 - REGISTRO (lab, sem drama)\n"
                 f"Post {pid} com problema: {problema}\n"
                 f"Acao: {acao}\n"
                 f"Ficha: cerebro/Foruns/v42_monitor/autocura/fichas/{cam.name}\n"
                 f"Link: https://cafezinho.news/?p={pid}\n"
                 "- Autocura V4.2 (robô DSC us65)")
        log(f"post {pid}: SEVERO ({problema}) → {acao} / ficha {cam.name}")
        try:
            import subprocess
            subprocess.run(["git", "add", str(cam)], cwd="/root/Cerebro",
                           capture_output=True, timeout=60)
            subprocess.run(["git", "commit", "-m",
                            f"AUTOCURA V4.2: ficha post {pid} ({problema})"],
                           cwd="/root/Cerebro", capture_output=True, timeout=60)
            subprocess.run(["git", "push", "origin", "main"], cwd="/root/Cerebro",
                           capture_output=True, timeout=120)
        except Exception as exc:
            log(f"git da ficha falhou: {exc}")


def saude_pipeline(est: dict) -> None:
    """Ciclo diário às 12:10 BRT — se às 13:10 não há post novo há 26h+, alerta."""
    agora = datetime.now(ZONA_BRT)
    hoje = agora.strftime("%Y-%m-%d")
    if agora.hour < 13 or est.get("alerta_stall") == hoje:
        return
    try:
        req = urllib.request.Request(
            f"{ESPELHO}/wp-json/wp/v2/posts?categories=100005&per_page=1"
            "&_fields=id,date_gmt", headers={"User-Agent": "V42-Autocura/1.0"})
        with urllib.request.urlopen(req, timeout=25) as r:
            p = json.loads(r.read().decode("utf-8"))
        ultima = datetime.fromisoformat(p[0]["date_gmt"].replace("Z", "+00:00"))
        idade_h = (datetime.now(timezone.utc) - ultima).total_seconds() / 3600
        if idade_h > 26:
            est["alerta_stall"] = hoje
            salvar_estado(est)
            telemetria("stall", {"idade_h": round(idade_h, 1)})
            telegram(f"AUTOCURA V4.2 - ALERTA AMARELO\nSem post novo da Estatística há "
                     f"{idade_h:.0f}h (o ciclo diário é 12:10 BRT). Conferir o agente no NYC "
                     "(cron 15:10 UTC / receipts gerados/ciclos/).\n- Autocura V4.2 (robô DSC us65)")
            log(f"stall: {idade_h:.1f}h sem post")
    except Exception as exc:
        log(f"saude_pipeline falhou: {exc}")


def main() -> int:
    est = carregar_estado()
    examinar_vereditos(est)
    saude_pipeline(est)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
