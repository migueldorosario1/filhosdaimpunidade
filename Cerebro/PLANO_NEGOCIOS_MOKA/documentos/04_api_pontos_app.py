#!/usr/bin/env python3
"""MOKA · API de Pontos (v1) — FastAPI mínima.

Endpoints:
  POST /convite/resgatar   — cria conta via código de convite (+200 pts)
  GET  /painel/saldo       — saldo e histórico do usuário (auth email+senha)
  POST /consumir           — debita pontos de uma ação (com custo real USD)
  POST /compras/webhook    — confirmação de pagamento do gateway (idempotente)

Roda local:  uvicorn app:app --port 8420
Banco:       moka_pontos.db (SQLite, schema v1 ao lado)
Sem deps externas além de fastapi/uvicorn (hash = pbkdf2 stdlib).
"""
import hashlib
import hmac
import os
import secrets
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, EmailStr

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, "moka_pontos.db")
SCHEMA = os.path.join(BASE_DIR, "..", "Foruns", "moka_pontos_schema_v1.sql")
WEBHOOK_SECRET = os.environ.get("MOKA_WEBHOOK_SECRET", "troque-em-producao")

app = FastAPI(title="Moka Pontos API", version="1.0")


# ---------- infra ----------

@contextmanager
def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    try:
        yield con
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


@app.on_event("startup")
def init_db():
    if not os.path.exists(DB):
        with db() as con:
            con.executescript(open(SCHEMA, encoding="utf-8").read())


def _hash_senha(senha: str, sal: str = None) -> str:
    sal = sal or secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", senha.encode(), sal.encode(), 120_000).hex()
    return f"{sal}${h}"


def _verifica_senha(senha: str, gravado: str) -> bool:
    sal, _ = gravado.split("$", 1)
    return hmac.compare_digest(_hash_senha(senha, sal), gravado)


def _agora() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def _auth(con, email: str, senha: str) -> sqlite3.Row:
    u = con.execute("SELECT * FROM usuarios WHERE email = ? AND status = 'ativo'",
                    (email,)).fetchone()
    if not u or not _verifica_senha(senha, u["senha_hash"]):
        raise HTTPException(401, "credenciais inválidas")
    return u


# ---------- modelos ----------

class ResgatarIn(BaseModel):
    codigo: str
    email: EmailStr
    nome: str
    senha: str

class ConsumirIn(BaseModel):
    email: EmailStr
    senha: str
    acao: str                       # resumo_video | resumo_livro | traducao_livro | tts | tts_premium
    recurso_ref: str = ""
    custo_usd: float = 0.0
    llm_usada: str = ""

class WebhookIn(BaseModel):
    compra_id: int
    gateway_ref: str
    status: str                     # pago | cancelado | reembolsado


# ---------- 1. resgatar convite ----------

@app.post("/convite/resgatar")
def resgatar(d: ResgatarIn):
    with db() as con:
        c = con.execute("SELECT * FROM convites WHERE codigo = ? AND ativo = 1",
                        (d.codigo.strip().upper(),)).fetchone()
        if not c:
            raise HTTPException(404, "convite inválido ou inativo")
        if c["usos"] >= c["max_usos"]:
            raise HTTPException(409, "convite já utilizado")
        if c["expira_em"] and c["expira_em"] < _agora():
            raise HTTPException(410, "convite expirado")
        if con.execute("SELECT 1 FROM usuarios WHERE email = ?", (d.email,)).fetchone():
            raise HTTPException(409, "e-mail já cadastrado")

        cur = con.execute(
            "INSERT INTO usuarios (email, nome, senha_hash, origem, last_login_at)"
            " VALUES (?, ?, ?, 'convite', ?)",
            (d.email, d.nome, _hash_senha(d.senha), _agora()))
        uid = cur.lastrowid
        con.execute("INSERT INTO carteiras (usuario_id, saldo_pontos) VALUES (?, 0)", (uid,))
        con.execute(
            "INSERT INTO creditos (usuario_id, pontos, tipo, referencia_id, descricao)"
            " VALUES (?, ?, 'convite', ?, ?)",
            (uid, c["pontos"], c["id"], f"Amostra grátis — convite {c['codigo']}"))
        con.execute(
            "UPDATE carteiras SET saldo_pontos = saldo_pontos + ?,"
            " total_creditado = total_creditado + ?, updated_at = ? WHERE usuario_id = ?",
            (c["pontos"], c["pontos"], _agora(), uid))
        con.execute("UPDATE convites SET usos = usos + 1, resgatado_por = ?,"
                    " resgatado_em = ? WHERE id = ?",
                    (uid, _agora(), c["id"]))
        return {"ok": True, "usuario_id": uid, "pontos": c["pontos"]}


# ---------- 2. painel/saldo ----------

@app.get("/painel/saldo")
def saldo(email: str, senha: str):
    with db() as con:
        u = _auth(con, email, senha)
        w = con.execute("SELECT * FROM carteiras WHERE usuario_id = ?", (u["id"],)).fetchone()
        hist = con.execute(
            "SELECT acao, pontos, created_at FROM consumo"
            " WHERE usuario_id = ? ORDER BY id DESC LIMIT 20", (u["id"],)).fetchall()
        con.execute("UPDATE usuarios SET last_login_at = ? WHERE id = ?", (_agora(), u["id"]))
        return {
            "nome": u["nome"], "email": u["email"],
            "saldo_pontos": w["saldo_pontos"],
            "total_creditado": w["total_creditado"],
            "total_consumido": w["total_consumido"],
            "ultimas_acoes": [dict(h) for h in hist],
        }


# ---------- 3. consumir ----------

@app.post("/consumir")
def consumir(d: ConsumirIn):
    with db() as con:
        u = _auth(con, d.email, d.senha)
        preco = con.execute("SELECT pontos FROM precos_acoes WHERE acao = ? AND ativo = 1",
                            (d.acao,)).fetchone()
        if not preco:
            raise HTTPException(400, f"ação desconhecida: {d.acao}")
        w = con.execute("SELECT saldo_pontos FROM carteiras WHERE usuario_id = ?",
                        (u["id"],)).fetchone()
        if w["saldo_pontos"] < preco["pontos"]:
            raise HTTPException(402, f"saldo insuficiente ({w['saldo_pontos']} pts)")
        con.execute(
            "INSERT INTO consumo (usuario_id, acao, recurso_ref, pontos, custo_usd, llm_usada)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (u["id"], d.acao, d.recurso_ref, preco["pontos"], d.custo_usd, d.llm_usada))
        con.execute(
            "UPDATE carteiras SET saldo_pontos = saldo_pontos - ?,"
            " total_consumido = total_consumido + ?, updated_at = ? WHERE usuario_id = ?",
            (preco["pontos"], preco["pontos"], _agora(), u["id"]))
        novo = con.execute("SELECT saldo_pontos FROM carteiras WHERE usuario_id = ?",
                           (u["id"],)).fetchone()
        return {"ok": True, "debitado": preco["pontos"], "saldo_pontos": novo["saldo_pontos"]}


# ---------- 4. webhook de compra (idempotente) ----------

@app.post("/compras/webhook")
def webhook(d: WebhookIn, x_moka_signature: str = Header(default="")):
    esperado = hmac.new(WEBHOOK_SECRET.encode(),
                        f"{d.compra_id}:{d.gateway_ref}".encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(x_moka_signature, esperado):
        raise HTTPException(401, "assinatura inválida")
    with db() as con:
        cp = con.execute("SELECT * FROM compras WHERE id = ?", (d.compra_id,)).fetchone()
        if not cp:
            raise HTTPException(404, "compra não encontrada")
        if cp["status"] == "pago" and d.status == "pago":
            return {"ok": True, "idempotente": True}
        con.execute("UPDATE compras SET status = ?, gateway_ref = ?, pago_em = ? WHERE id = ?",
                    (d.status, d.gateway_ref, _agora() if d.status == "pago" else None,
                     d.compra_id))
        if d.status == "pago":
            con.execute(
                "INSERT INTO creditos (usuario_id, pontos, tipo, referencia_id, descricao)"
                " VALUES (?, ?, 'compra', ?, ?)",
                (cp["usuario_id"], cp["pontos"], cp["id"],
                 f"Pacote {cp['pacote']} ({cp['pontos']} pts)"))
            con.execute(
                "UPDATE carteiras SET saldo_pontos = saldo_pontos + ?,"
                " total_creditado = total_creditado + ?, updated_at = ? WHERE usuario_id = ?",
                (cp["pontos"], cp["pontos"], _agora(), cp["usuario_id"]))
        return {"ok": True, "status": d.status}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8420)
