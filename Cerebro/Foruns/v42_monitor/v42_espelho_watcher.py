#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v42_espelho_watcher.py — Vigia do Agente V4.2 Estatística no espelho cafezinho.news
===================================================================================
Nasceu da ordem do Miguel (03/09/2026, sessão DSC us65): "manda o DSN Ideias analisar
o V4.2 estatística que tá rolando no cafezinho news... manda os posts para o cafezinho
ideias acompanhar e ver se ele tá fazendo alucinação ou está indo bem".

O que faz (a cada 15 min, cron com flock):
  1. Lê o REST público do espelho (categoria Estatística 100005) e detecta posts NOVOS.
  2. Para cada post novo roda AUDITORIA MECÂNICA:
     - todo número do texto precisa nascer do rodapé "Fontes primárias" (valor,
       variação %, ou soma/diferença de mesma moeda) — pega número inventado;
     - moeda trocada (US$ em cima de valor de série em euros);
     - título repetido/em eco com posts anteriores (Jaccard ≥ 0,6);
     - série defasada (>90 dias) tratada como dado corrente ("recorde" etc.).
  3. VEREDITO LLM (deepseek-chat, barato): ALUCINOU / ATENCAO / OK + problemas + nota.
  4. Registra no Cérebro (repo): veredito em Foruns/v42_monitor/vereditos/ e PEDIDO
     marcado IDEIA_PRO_DSNUVEM_IDEIAS em Foruns/v42_monitor/pedidos/ (o DSN Ideias,
     Tencent, caça esse marcador na ronda :13/:43 e acompanha) + 1 linha em
     Foruns/ponte_laura_completa/de_ideias.md.
  5. Avisa o Miguel pelo Telegram do DSC (texto limpo, sem asteriscos/# — ZM-058).
  6. Commit/push ESCOADO (só os caminhos próprios; nunca git add -A).

Telemetria própria (regra DSC-052): /root/agent_data/v42_monitor/telemetry.jsonl
Memória própria: /root/v42_monitor/MEMORIA_VIVA.md · Canal: Foruns/v42_monitor/ + ponte.
NÃO publica, NÃO edita posts, NÃO mexe em credenciais — só lê REST público e escreve
no repo. Chave DeepSeek só em memória, nunca impressa/gravada (§82).
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone, timedelta
from html import unescape
from pathlib import Path

BASE = Path(__file__).resolve().parent                      # /root/v42_monitor
REPO = Path("/root/Cerebro")
MON_DIR = REPO / "cerebro" / "Foruns" / "v42_monitor"
VEREDITOS = MON_DIR / "vereditos"
PEDIDOS = MON_DIR / "pedidos"
PONTE_IDEIAS = REPO / "cerebro" / "Foruns" / "ponte_laura_completa" / "de_ideias.md"
ESTADO = Path("/root/agent_data/v42_monitor/estado.json")
TELEMETRIA = Path("/root/agent_data/v42_monitor/telemetry.jsonl")
LOGF = Path("/root/agent_data/v42_monitor/watcher.log")

ESPELHO = "https://cafezinho.news"
CAT_ESTAT = 100005
ZONA_BRT = timezone(timedelta(hours=-3))

sys.path.insert(0, str(BASE))
from v42_checagens import (          # checker mecânico compartilhado
    extrair_texto, parse_fontes, checar_numeros, checar_titulo_eco,
    checar_defasados, candidatos_do_rodape,
)


def log(msg: str) -> None:
    try:
        LOGF.parent.mkdir(parents=True, exist_ok=True)
        with LOGF.open("a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")
    except Exception:
        pass


def agora_brt() -> str:
    return datetime.now(ZONA_BRT).strftime("%Y%m%d %H:%M:%S BRT")


def _get(url: str, timeout: int = 25):
    req = urllib.request.Request(url, headers={"User-Agent": "V42-Vigia-DSC/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def carregar_estado() -> dict:
    try:
        return json.loads(ESTADO.read_text(encoding="utf-8"))
    except Exception:
        return {"vistos": [], "instalado_em": datetime.now(ZONA_BRT).isoformat()}


def salvar_estado(est: dict) -> None:
    ESTADO.parent.mkdir(parents=True, exist_ok=True)
    tmp = ESTADO.with_suffix(".tmp")
    tmp.write_text(json.dumps(est, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, ESTADO)


def chave_deepseek() -> str:
    env = {}
    cam = Path.home() / ".dsh" / "deepseek_env"
    try:
        for ln in cam.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, v = ln.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    except Exception:
        pass
    return env.get("DEEPSEEK_API_KEY", "")


def veredito_llm(texto: str, checagens: list) -> dict:
    """Veredito de alucinação com deepseek-chat (barato). Falha → veredito
    conservador 'MECANICO' sem derrubar a ronda."""
    chave = chave_deepseek()
    if not chave:
        return {"veredito": "MECANICO", "nota": None, "problemas": [],
                "resumo": "sem chave LLM; só checagem mecânica", "modelo": ""}
    sistema = (
        "Você é auditor factual do jornal O Cafezinho (vertical Estatística, agente "
        "V4.2). Recebe o texto de uma matéria e as checagens mecânicas já feitas. "
        "Julgue APENAS: (a) algum número/afirmação não nasce das fontes do rodapé; "
        "(b) período/moeda/janela errados (ex.: valor mensal chamado de acumulado 12 "
        "meses, euros chamados de US$); (c) dado defasado apresentado como corrente; "
        "(d) afirmação oposta ao dado. NÃO julgue estilo, só fato. Responda SOMENTE "
        'JSON: {"veredito": "ALUCINOU|ATENCAO|OK", "nota": 0-10, "problemas": ["..."], '
        '"resumo": "1 frase em português"}'
    )
    usuario = f"CHECAGENS MECÂNICAS:\n{json.dumps(checagens, ensure_ascii=False)}\n\nMATÉRIA:\n{texto[:6000]}"
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "system", "content": sistema},
                     {"role": "user", "content": usuario}],
        "temperature": 0.2, "max_tokens": 600, "response_format": {"type": "json_object"},
    }
    req = urllib.request.Request(
        "https://api.deepseek.com/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {chave}"},
        method="POST")
    try:
        t0 = time.time()
        with urllib.request.urlopen(req, timeout=90) as r:
            dados = json.loads(r.read().decode("utf-8"))
        uso = dados.get("usage", {})
        try:  # telemetria NUNCA derruba o veredito
            TELEMETRIA.parent.mkdir(parents=True, exist_ok=True)
            with TELEMETRIA.open("a", encoding="utf-8") as f:
                f.write(json.dumps({
                    "ts": datetime.now(ZONA_BRT).isoformat(), "agente": "v42_espelho_watcher",
                    "modelo": "deepseek-chat", "prompt_tokens": uso.get("prompt_tokens"),
                    "completion_tokens": uso.get("completion_tokens"),
                    "latencia_s": round(time.time() - t0, 1),
                    "custo_usd_estimado": round(
                        (uso.get("prompt_tokens", 0) * 0.27 + uso.get("completion_tokens", 0) * 1.10) / 1e6, 6),
                }, ensure_ascii=False) + "\n")
        except Exception:
            pass
        bruto = dados.get("choices", [{}])[0].get("message", {}).get("content", "")
        obj = json.loads(bruto)
        obj.setdefault("veredito", "ATENCAO"); obj.setdefault("problemas", [])
        obj["modelo"] = "deepseek-chat"
        return obj
    except Exception as exc:
        log(f"veredito_llm falhou: {exc}")
        return {"veredito": "MECANICO", "nota": None, "problemas": [],
                "resumo": f"LLM indisponível ({type(exc).__name__}); checagem mecânica abaixo",
                "modelo": ""}


def telegram(msg: str) -> None:
    env = {}
    try:
        for ln in (Path("/root/.env.unificado")).read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, v = ln.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    except Exception:
        return
    token, chat = env.get("TELEGRAM_TOKEN_DSC_BOT", ""), env.get("DSC_BOT_CHAT_ID", "")
    if not token or not chat:
        return
    try:
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=json.dumps({"chat_id": chat, "text": msg[:3900]}).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        urllib.request.urlopen(req, timeout=20)
    except Exception as exc:
        log(f"telegram falhou: {exc}")


def auditar_post(post: dict, anteriores: list) -> dict:
    """Auditoria completa de um post novo. `anteriores`: [(id, titulo, texto)] mais
    recentes (excluindo o atual) para eco de título."""
    pid = post["id"]
    titulo = unescape(post.get("title", {}).get("rendered", ""))
    texto = extrair_texto(post.get("content", {}).get("rendered", ""))
    fontes = parse_fontes(texto)
    cand = candidatos_do_rodape(fontes)
    probs = []
    probs += checar_numeros(texto, cand)
    eco = checar_titulo_eco(titulo, anteriores)
    if eco:
        probs.append(eco)
    probs += checar_defasados(texto, fontes)
    return {"id": pid, "titulo": titulo, "texto": texto, "fontes": fontes,
            "problemas_mecanicos": probs, "eco_titulo": eco}


def gravar_veredito(aud: dict, llm: dict) -> Path:
    VEREDITOS.mkdir(parents=True, exist_ok=True)
    pid, data = aud["id"], datetime.now(ZONA_BRT).strftime("%Y-%m-%d")
    caminho = VEREDITOS / f"{data}_post{pid}.md"
    linhas = [
        f"# Veredito V4.2 — post {pid} ({data})",
        "",
        f"- Título: {aud['titulo']}",
        f"- Link: https://cafezinho.news/?p={pid}",
        f"- Veredito LLM: {llm.get('veredito')} · nota: {llm.get('nota')} · modelo: {llm.get('modelo','')}",
        f"- Resumo: {llm.get('resumo','')}",
        f"- Problemas mecânicos: {len(aud['problemas_mecanicos'])}"
        + ("" if not aud["problemas_mecanicos"] else " → " + "; ".join(aud["problemas_mecanicos"][:6])),
        f"- Problemas LLM: " + ("; ".join(llm.get("problemas", [])[:6]) or "—"),
        f"- Fontes do rodapé: " + ("; ".join(f"{f['serie']}={f['valor']} @{f['data']}" for f in aud['fontes']) or "—"),
        "",
        "## Texto integral",
        "",
        aud["texto"],
        "",
        f"— Vigia V4.2 (robô DSC us65) · {agora_brt()}",
        "",
    ]
    caminho.write_text("\n".join(linhas), encoding="utf-8")
    return caminho


def gravar_pedido_ideias(aud: dict, llm: dict) -> Path:
    """Pedido que o DSN Ideias caça (marcador IDEIA_PRO_DSNUVEM_IDEIAS)."""
    PEDIDOS.mkdir(parents=True, exist_ok=True)
    pid = aud["id"]
    data = datetime.now(ZONA_BRT).strftime("%Y-%m-%d")
    caminho = PEDIDOS / f"{data}_post{pid}_IDEIA_PRO.md"
    linhas = [
        f"# IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-{pid} — acompanhar post V4.2 (auditoria alucinação)",
        "",
        f"Post: {aud['titulo']} · https://cafezinho.news/?p={pid} · {data}",
        "Pedido do Miguel (03/09, sessão DSC): o DSN Ideias acompanha a vertical Estatística",
        "do espelho e diz se o agente V4.2 está alucinando ou indo bem.",
        "",
        "Veredito do vigia (mecânico + LLM):",
        f"- mecânico: {'nenhum problema' if not aud['problemas_mecanicos'] else '; '.join(aud['problemas_mecanicos'][:6])}",
        f"- LLM ({llm.get('modelo','')}): {llm.get('veredito')} · nota {llm.get('nota')} · {llm.get('resumo','')}",
        "",
        "O que se pede da ronda do Ideias: ler o texto abaixo com olhar de arquiteto —",
        "os números honram as fontes? há interpretação alucinada (janela, moeda, defasado)?",
        "a reforma de 03/09 (rodízio de teses, gates de frescor/título, validador factual)",
        "está segurando? Registrar veredito próprio em arquivo de ronda + síntese na ponte.",
        "",
        "## Texto do post",
        "",
        aud["texto"],
        "",
        "## Rodapé de fontes (valores citáveis)",
        "",
        *[f"- {f['serie']}: último {f['valor']} {f['unidade']} em {f['data']}" for f in aud["fontes"]],
        "",
        f"— Vigia V4.2 (robô DSC us65), em nome do Miguel · {agora_brt()}",
        "",
    ]
    caminho.write_text("\n".join(linhas), encoding="utf-8")
    return caminho


def ponte_ideias_linha(aud: dict, llm: dict, caminho_pedido: Path) -> None:
    bloco = (
        f"\n## [{datetime.now(ZONA_BRT).strftime('%Y-%m-%d %H:%M BRT')} · Vigia V4.2] "
        f"Post V4.2 novo no espelho: {aud['id']} — veredito {llm.get('veredito')} "
        f"(nota {llm.get('nota')}) — pedido IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-{aud['id']} em "
        f"Foruns/v42_monitor/pedidos/{caminho_pedido.name} — acompanhar e opnar se alucinou ou está indo bem. "
        f"— Vigia V4.2 (robô DSC us65) · {agora_brt()}\n"
    )
    try:
        with PONTE_IDEIAS.open("a", encoding="utf-8") as f:
            f.write(bloco)
    except Exception as exc:
        log(f"ponte_ideias falhou: {exc}")


def commit_repo(caminhos: list) -> bool:
    try:
        r = subprocess.run(["git", "pull", "--no-edit"], cwd=REPO,
                           capture_output=True, timeout=120)
        if r.returncode != 0:
            log(f"git pull falhou: {r.stderr.decode()[:200]}")
        subprocess.run(["git", "add", "--"] + [str(c) for c in caminhos],
                       cwd=REPO, capture_output=True, timeout=60)
        subprocess.run(["git", "commit", "-m",
                        f"V42MON: auditoria do vigia V4.2 ({datetime.now(ZONA_BRT).strftime('%d/%m %H:%M')} BRT)"],
                       cwd=REPO, capture_output=True, timeout=60)
        r = subprocess.run(["git", "push", "origin", "main"], cwd=REPO,
                           capture_output=True, timeout=120)
        ok = r.returncode == 0
        if not ok:
            subprocess.run(["git", "pull", "--no-edit"], cwd=REPO,
                           capture_output=True, timeout=120)
            r = subprocess.run(["git", "push", "origin", "main"], cwd=REPO,
                               capture_output=True, timeout=120)
            ok = r.returncode == 0
        return ok
    except Exception as exc:
        log(f"commit_repo falhou: {exc}")
        return False


def main() -> int:
    # ORDEM MIGUEL 03/09 ~02:20 BRT: rodar de hora em hora e PARAR hoje às
    # 10:30 BRT (ele quer entender o propósito antes de deixar continuar).
    EXPIRA_EM = datetime(2026, 9, 3, 10, 30, tzinfo=ZONA_BRT)
    if datetime.now(ZONA_BRT) >= EXPIRA_EM:
        log("expirado (ordem Miguel 03/09: parar às 10:30 BRT) — removendo o próprio cron.")
        subprocess.run("crontab -l 2>/dev/null | grep -v v42_espelho_watcher | crontab -",
                       shell=True, capture_output=True, timeout=60)
        telegram("Vigia V4.2 desligado (ordem: até 10:30). Ele so auditava post novo — "
                 "sem post novo, nao fazia nada (era so detector, nao produtor; o agente "
                 "escreve 1 post/dia as 12:10, isso nao mudou). O que ele ja achou nos 8 "
                 "posts antigos: Foruns/v42_monitor/vereditos/ (pega os 4 defeitos reais). "
                 "Religar depois de entender: 1 linha de cron. — ZCode/DSC us65")
        return 0
    est = carregar_estado()
    vistos = set(est.get("vistos", []))
    try:
        posts = _get(f"{ESPELHO}/wp-json/wp/v2/posts?categories={CAT_ESTAT}"
                     f"&per_page=20&_fields=id,date,title,content,link")
    except Exception as exc:
        log(f"REST espelho falhou: {exc}")
        return 0
    posts.sort(key=lambda p: p.get("date", ""))
    novos = [p for p in posts if p["id"] not in vistos]

    # primeira execução: apenas marca os existentes (sem retro-auditar tudo)
    if not vistos:
        for p in posts:
            vistos.add(p["id"])
        est["vistos"] = sorted(vistos)
        salvar_estado(est)
        log(f"primeira execução: {len(posts)} posts existentes marcados, sem auditoria retrô.")
        return 0

    anteriores = [(p["id"],
                   unescape(p.get("title", {}).get("rendered", "")),
                   extrair_texto(p.get("content", {}).get("rendered", "")))
                  for p in posts]

    for post in novos:
        try:
            aud = auditar_post(post, [a for a in anteriores if a[0] != post["id"]])
            llm = veredito_llm(aud["texto"], aud["problemas_mecanicos"])
            cam_v = gravar_veredito(aud, llm)
            cam_p = gravar_pedido_ideias(aud, llm)
            ponte_ideias_linha(aud, llm, cam_p)
            vistos.add(aud["id"])
            est["vistos"] = sorted(vistos)[-200:]
            salvar_estado(est)
            push_ok = commit_repo([cam_v, cam_p, PONTE_IDEIAS])
            nivel = llm.get("veredito", "?")
            msg = (f"Vigia V4.2 — post {aud['id']} no espelho: {nivel}"
                   + (f" (nota {llm.get('nota')})" if llm.get('nota') is not None else "")
                   + f"\n{aud['titulo']}"
                   + (f"\nProblemas: {'; '.join((aud['problemas_mecanicos'] + llm.get('problemas', []))[:4])}"
                      if (aud['problemas_mecanicos'] or llm.get('problemas')) else "\nSem sinais de alucinação.")
                   + f"\nPedido ao DSN Ideias no repo. Push: {'ok' if push_ok else 'PENDENTE'}.")
            telegram(msg)
            log(f"post {aud['id']}: veredito={nivel} problemas={len(aud['problemas_mecanicos'])} push={push_ok}")
        except Exception as exc:
            log(f"erro auditando post {post.get('id')}: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
