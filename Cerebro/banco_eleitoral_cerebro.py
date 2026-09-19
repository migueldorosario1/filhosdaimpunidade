#!/usr/bin/env python3
"""
Banco Eleitoral do Cérebro — Ingestor e Consolidador Unificado
Consolida dados eleitorais do TSE (Vereadores, Prefeitos, Deputados Estaduais, Deputados Federais, Senadores e Governadores)
em uma base SQLite unificada para o Cérebro do Antigravity.
"""

from __future__ import annotations
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
DB_PATH = BASE_DIR / "banco_eleitoral.db"

RIOCARTA_DATA = PROJECT_ROOT / "Projeto Cafezinho Agentes" / "sites-v4" / "riocarta" / "src" / "data"
CEARA_DATA = PROJECT_ROOT / "Projeto Cafezinho Agentes" / "sites-v4" / "ceara" / "src" / "data"

def init_db(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidatos_eleicao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ano INTEGER NOT NULL,
        uf TEXT NOT NULL,
        municipio TEXT,
        municipio_slug TEXT,
        cargo TEXT NOT NULL,
        sq_candidato TEXT,
        nome TEXT NOT NULL,
        nome_urna TEXT NOT NULL,
        slug TEXT NOT NULL,
        partido TEXT NOT NULL,
        numero TEXT,
        situacao TEXT,
        turno INTEGER DEFAULT 1,
        votos_validos INTEGER NOT NULL,
        total_votos_validos_local INTEGER NOT NULL,
        pct_votos_validos REAL NOT NULL,
        eleitores_aptos INTEGER DEFAULT 0,
        pct_sobre_eleitorado REAL DEFAULT 0.0,
        criterio_percentual TEXT NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS municipios_eleitorado (
        uf TEXT NOT NULL,
        municipio TEXT NOT NULL,
        municipio_slug TEXT NOT NULL,
        ano INTEGER NOT NULL,
        eleitores_aptos INTEGER,
        comparecimento INTEGER,
        PRIMARY KEY (uf, municipio_slug, ano)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estatisticas_resumo (
        chave TEXT PRIMARY KEY,
        valor TEXT,
        atualizado_em TEXT
    );
    """)
    conn.commit()

def Ingest_rio_elections(conn: sqlite3.Connection):
    cursor = conn.cursor()
    criterio_padrao = "Votos nominais válidos do candidato divididos pelo total de votos válidos apurados na eleição local (1º turno)."

    # 1. Eleitores RJ 2024
    eleitores_file = RIOCARTA_DATA / "eleitores_rj_2024.json"
    eleitorado_map = {}
    if eleitores_file.exists():
        data = json.loads(eleitores_file.read_text(encoding="utf-8"))
        for slug, info in data.get("eleitorado", {}).items():
            eleitorado_map[slug] = info.get("eleitores", 0)
            cursor.execute("""
                INSERT OR REPLACE INTO municipios_eleitorado (uf, municipio, municipio_slug, ano, eleitores_aptos, comparecimento)
                VALUES (?, ?, ?, ?, ?, ?)
            """, ("RJ", slug.replace("-", " ").title(), slug, 2024, info.get("eleitores", 0), info.get("comparecimento", 0)))

    # 2. Vereadores RJ 2024
    ver_file = RIOCARTA_DATA / "vereadores_rj.json"
    if ver_file.exists():
        data = json.loads(ver_file.read_text(encoding="utf-8"))
        for cid in data.get("cidades", []):
            cid_nome = cid["cidade"]
            cid_slug = cid["cidadeSlug"]
            total_votos_mun = cid.get("totalVotosNominaisMunicipio") or sum(v["votosNominaisValidos"] for v in cid["vereadores"])
            total_eleitores = eleitorado_map.get(cid_slug, 0)

            for v in cid["vereadores"]:
                votos = v["votosNominaisValidos"]
                pct = (votos / total_votos_mun * 100) if total_votos_mun else v.get("percentualMunicipio", 0.0)
                pct_eleit = (votos / total_eleitores * 100) if total_eleitores else 0.0

                cursor.execute("""
                    INSERT INTO candidatos_eleicao 
                    (ano, uf, municipio, municipio_slug, cargo, sq_candidato, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, eleitores_aptos, pct_sobre_eleitorado, criterio_percentual)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (2024, "RJ", cid_nome, cid_slug, "Vereador", v.get("numero"), v["nome"], v["nome"], v["slug"], v["partido"], v.get("numero"), v.get("situacao", "ELEITO"), 1, votos, total_votos_mun, round(pct, 4), total_eleitores, round(pct_eleit, 4), criterio_padrao))

    # 3. Prefeitos RJ 2024
    pref_file = RIOCARTA_DATA / "prefeitos_eleitos_rj_2024.json"
    if pref_file.exists():
        data = json.loads(pref_file.read_text(encoding="utf-8"))
        for p in data.get("prefeitos", []):
            votos = p.get("votos", 0)
            total_votos = p.get("totalVotosMunicipio", 0)
            pct = (votos / total_votos * 100) if total_votos else p.get("percentualMunicipio", 0.0)
            cursor.execute("""
                INSERT INTO candidatos_eleicao 
                (ano, uf, municipio, municipio_slug, cargo, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, criterio_percentual)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (2024, "RJ", p["municipio"], p["municipioSlug"], "Prefeito", p["nome"], p.get("nomeUrna", p["nome"]), p["slug"], p["partido"], p.get("numero"), p.get("situacao", "ELEITO"), p.get("turno", 1), votos, total_votos, round(pct, 4), criterio_padrao))

    # 4. Deputados Estaduais RJ 2022
    dep_est_file = RIOCARTA_DATA / "deputados_estaduais_eleitos_rj_2022.json"
    if dep_est_file.exists():
        data = json.loads(dep_est_file.read_text(encoding="utf-8"))
        for d in data.get("deputados", []):
            votos = d.get("votos", 0)
            total_votos = d.get("totalVotosEstado", 0)
            pct = (votos / total_votos * 100) if total_votos else d.get("percentualEstado", 0.0)
            cursor.execute("""
                INSERT INTO candidatos_eleicao 
                (ano, uf, municipio, municipio_slug, cargo, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, criterio_percentual)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (2022, "RJ", "Estado do Rio de Janeiro", "rio-de-janeiro-estado", "Deputado Estadual", d["nome"], d.get("deputado", d["nome"]), d["slug"], d["partido"], d.get("numero"), d.get("situacao", "ELEITO POR QP"), 1, votos, total_votos, round(pct, 4), criterio_padrao))

    # 5. Deputados Federais RJ 2022
    dep_fed_file = RIOCARTA_DATA / "deputados_federais_eleitos_rj_2022.json"
    if dep_fed_file.exists():
        data = json.loads(dep_fed_file.read_text(encoding="utf-8"))
        for d in data.get("deputadosFederais", []):
            votos = d.get("votos", 0)
            total_votos = d.get("totalVotosEstado", 0)
            pct = (votos / total_votos * 100) if total_votos else d.get("percentualEstado", 0.0)
            cursor.execute("""
                INSERT INTO candidatos_eleicao 
                (ano, uf, municipio, municipio_slug, cargo, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, criterio_percentual)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (2022, "RJ", "Estado do Rio de Janeiro", "rio-de-janeiro-estado", "Deputado Federal", d["nome"], d.get("deputado_federal", d["nome"]), d["slug"], d["partido"], d.get("numero"), d.get("situacao", "ELEITO POR QP"), 1, votos, total_votos, round(pct, 4), criterio_padrao))

    conn.commit()

def ingest_ceara_elections(conn: sqlite3.Connection):
    cursor = conn.cursor()
    criterio_padrao = "Votos nominais válidos do candidato divididos pelo total de votos válidos apurados na eleição local (1º turno)."

    # 1. Vereadores CE 2024
    ver_file = CEARA_DATA / "vereadores_ce.json"
    if ver_file.exists():
        data = json.loads(ver_file.read_text(encoding="utf-8"))
        for cid in data.get("cidades", []):
            cid_nome = cid["cidade"]
            cid_slug = cid["cidadeSlug"]
            total_votos_mun = cid.get("totalVotosNominaisMunicipio") or sum(v["votosNominaisValidos"] for v in cid["vereadores"])

            for v in cid["vereadores"]:
                votos = v["votosNominaisValidos"]
                pct = (votos / total_votos_mun * 100) if total_votos_mun else v.get("percentualMunicipio", 0.0)

                cursor.execute("""
                    INSERT INTO candidatos_eleicao 
                    (ano, uf, municipio, municipio_slug, cargo, sq_candidato, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, criterio_percentual)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (2024, "CE", cid_nome, cid_slug, "Vereador", v.get("numero"), v["nome"], v["nome"], v["slug"], v["partido"], v.get("numero"), v.get("situacao", "ELEITO"), 1, votos, total_votos_mun, round(pct, 4), criterio_padrao))

    # 2. Prefeitos CE 2024
    pref_file = CEARA_DATA / "prefeitos_eleitos_ce_2024.json"
    if pref_file.exists():
        data = json.loads(pref_file.read_text(encoding="utf-8"))
        for p in data.get("prefeitos", []):
            votos = p.get("votos", 0)
            total_votos = p.get("totalVotosMunicipio", 0)
            pct = (votos / total_votos * 100) if total_votos else p.get("percentualMunicipio", 0.0)
            cursor.execute("""
                INSERT INTO candidatos_eleicao 
                (ano, uf, municipio, municipio_slug, cargo, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, criterio_percentual)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (2024, "CE", p["municipio"], p["municipioSlug"], "Prefeito", p["nome"], p.get("nomeUrna", p["nome"]), p["slug"], p["partido"], p.get("numero"), p.get("situacao", "ELEITO"), p.get("turno", 1), votos, total_votos, round(pct, 4), criterio_padrao))

    # 3. Deputados Estaduais CE 2022
    dep_est_file = CEARA_DATA / "deputados_estaduais_eleitos_ce_2022.json"
    if dep_est_file.exists():
        data = json.loads(dep_est_file.read_text(encoding="utf-8"))
        for d in data.get("deputados", []):
            votos = d.get("votos", 0)
            total_votos = d.get("totalVotosEstado", 0)
            pct = (votos / total_votos * 100) if total_votos else d.get("percentualEstado", 0.0)
            cursor.execute("""
                INSERT INTO candidatos_eleicao 
                (ano, uf, municipio, municipio_slug, cargo, nome, nome_urna, slug, partido, numero, situacao, turno, votos_validos, total_votos_validos_local, pct_votos_validos, criterio_percentual)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (2022, "CE", "Estado do Ceará", "ceara-estado", "Deputado Estadual", d["nome"], d.get("deputado", d["nome"]), d["slug"], d["partido"], d.get("numero"), d.get("situacao", "ELEITO POR QP"), 1, votos, total_votos, round(pct, 4), criterio_padrao))

    conn.commit()

def build_summary(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM candidatos_eleicao")
    total_cand = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT municipio_slug) FROM candidatos_eleicao")
    total_muns = cursor.fetchone()[0]

    now_iso = datetime.now(timezone.utc).isoformat()
    cursor.execute("INSERT OR REPLACE INTO estatisticas_resumo (chave, valor, atualizado_em) VALUES (?, ?, ?)", ("total_candidatos", str(total_cand), now_iso))
    cursor.execute("INSERT OR REPLACE INTO estatisticas_resumo (chave, valor, atualizado_em) VALUES (?, ?, ?)", ("total_municipios", str(total_muns), now_iso))
    conn.commit()

def main():
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    Ingest_rio_elections(conn)
    ingest_ceara_elections(conn)
    build_summary(conn)
    
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM candidatos_eleicao")
    c_cnt = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT uf) FROM candidatos_eleicao")
    uf_cnt = cursor.fetchone()[0]
    print(f"✅ Banco Eleitoral do Cérebro criado em {DB_PATH}")
    print(f"   Total de Registros de Candidatos: {c_cnt} em {uf_cnt} UFs")
    conn.close()

if __name__ == "__main__":
    main()
