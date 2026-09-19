# 🧪 Fórum: Smoke Tests por Coletor — Sprint de Migração

> **Data:** 13 de junho de 2026, ~16:15 BRT  
> **Autor:** Kimi (Maestro Diagnóstico)  
> **Tipo:** Framework de validação local  
> **Regra:** Nada executado. Tudo documentado para aprovação antes de rodar.

---

## 1. Contexto

O Codex identificou que o pós-reforma tem **apenas 3 coletores** operacionais, enquanto o legado tem **27 coletores + bancos brutos** acumulados. Este fórum propõe um **framework de smoke tests** para validar cada coletor migrado antes de ele entrar no pipeline.

---

## 2. Arquitetura do Pipeline Pós-Reforma (Contrato)

```
coletor temático → noticias_brutas → produtor → noticias_prontas → mídia → auditoria → noticias_auditadas → publicador único
```

### Tabelas do Pipeline (SQLite local)

| Tabela | Função |
|--------|--------|
| `noticias_brutas` | Pautas coletadas (fonte, título, URL, hash dedup) |
| `noticias_prontas` | Matérias produzidas (corpo, categorias, tags) |
| `midias` | Imagens selecionadas |
| `auditorias_midia` | Verificação de qualidade de imagem |
| `escolhas_midia` | Decisão final de imagem |
| `noticias_auditadas` | Matérias aprovadas para publicação |
| `eventos_pipeline` | Log de todo o fluxo |

### Smoke Test Existente (Base)

Já existe: `A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/scripts/smoke_pipeline_editorial_local.py`

- Faz dry-run completo do pipeline
- Não publica, não chama LLM, não acessa WP
- Usa dados sintéticos (notícia fake de ônibus elétrico)
- Limpa run anterior antes de inserir

---

## 3. Framework de Smoke Tests por Coletor

### 3.1 Objetivo de Cada Smoke Test

Validar que um coletor migrado:
1. ✅ **Coleta** corretamente (fontes acessíveis, parsing OK)
2. ✅ **Dedup funciona** (não insere duplicatas)
3. ✅ **Latência é aceitável** (< 30s por fonte, < 5min total)
4. ✅ **Schema é respeitado** (campos obrigatórios preenchidos)
5. ✅ **Eventos são registrados** no pipeline
6. ✅ **Não quebra** o banco nem o pipeline

### 3.2 Estrutura do Smoke Test por Coletor

```python
#!/usr/bin/env python3
"""
Smoke Test: Coletor <TEMA>
===========================
Valida o coletor_<tema>.py migrado do legado.
NÃO publica, NÃO chama LLM, NÃO acessa WordPress.
"""

import sqlite3
import json
import hashlib
import time
from datetime import datetime, timezone
from pathlib import Path

# --- CONFIGURAÇÃO -----------------------------------------------------------
DB_PATH = "A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/Dados/bancos/pipeline_editorial_local.db"
TEMA = "<tema>"  # ex: trends, nacional, geopolitica
COLETOR_PATH = f"A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/Sistema/agentes/{TEMA}/coletor_{TEMA}.py"
RUN_ID = f"smoke_{TEMA}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"

# --- MÉTRICAS ---------------------------------------------------------------
metricas = {
    "tema": TEMA,
    "run_id": RUN_ID,
    "inicio": time.time(),
    "itens_coletados": 0,
    "itens_inseridos": 0,
    "duplicatas_detectadas": 0,
    "erros": [],
    "latencia_total_s": 0,
    "latencia_por_fonte_s": {},
}

# --- FUNÇÕES ----------------------------------------------------------------

def conectar_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def limpar_run_anterior(conn):
    """Remove registros de smoke tests anteriores deste tema."""
    conn.execute("DELETE FROM noticias_brutas WHERE agente_coletor LIKE ?", (f"%smoke_{TEMA}%",))
    conn.execute("DELETE FROM eventos_pipeline WHERE agente LIKE ?", (f"%smoke_{TEMA}%",))
    conn.commit()

def verificar_schema(conn):
    """Verifica se a tabela noticias_brutas tem as colunas esperadas."""
    cur = conn.execute("PRAGMA table_info(noticias_brutas)")
    colunas = {row[1] for row in cur.fetchall()}
    obrigatorias = {
        "noticia_bruta_id", "agente_coletor", "tema", "titulo_original",
        "url_fonte", "fonte_nome", "data_publicacao_fonte", "hash_dedup",
        "score_relevancia", "status"
    }
    faltando = obrigatorias - colunas
    if faltando:
        metricas["erros"].append(f"Colunas faltando: {faltando}")
        return False
    return True

def rodar_coletor():
    """
    Executa o coletor em modo dry-run ou limitado.
    Retorna lista de itens coletados.
    """
    # TODO: adaptar para cada coletor específico
    # Opção A: importar e chamar função principal do coletor
    # Opção B: rodar como subprocess com --dry-run
    # Opção C: mock de dados baseado no legado
    pass

def verificar_dedup(conn, hash_dedup):
    """Verifica se o hash já existe no banco."""
    cur = conn.execute("SELECT 1 FROM noticias_brutas WHERE hash_dedup = ?", (hash_dedup,))
    return cur.fetchone() is not None

def inserir_bruta(conn, item):
    """Insere uma notícia bruta no pipeline."""
    conn.execute("""
        INSERT INTO noticias_brutas
        (noticia_bruta_id, agente_coletor, tema, titulo_original, url_fonte,
         fonte_nome, data_publicacao_fonte, texto_extraido, resumo_coletor,
         keywords_json, score_relevancia, hash_dedup, idioma_detectado, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item["id"], f"coletor_{TEMA}_smoke", TEMA, item["titulo"],
        item["url"], item["fonte"], item["data"], item.get("texto", ""),
        item.get("resumo", ""), json.dumps(item.get("keywords", [])),
        item.get("score", 0.5), item["hash_dedup"], "pt-BR", "nova"
    ))
    metricas["itens_inseridos"] += 1

def registrar_evento(conn, entidade_id, status):
    """Registra evento no pipeline."""
    conn.execute("""
        INSERT INTO eventos_pipeline
        (entidade_tipo, entidade_id, etapa, agente, status, criado_em)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("noticia_bruta", entidade_id, "coleta", f"coletor_{TEMA}_smoke", status, datetime.now(timezone.utc).isoformat()))

def gerar_relatorio():
    """Gera relatório final do smoke test."""
    metricas["latencia_total_s"] = round(time.time() - metricas["inicio"], 2)
    
    print("=" * 60)
    print(f"🧪 SMOKE TEST: Coletor {TEMA.upper()}")
    print(f"   Run ID: {RUN_ID}")
    print("=" * 60)
    print(f"   Itens coletados:     {metricas['itens_coletados']}")
    print(f"   Itens inseridos:     {metricas['itens_inseridos']}")
    print(f"   Duplicatas:          {metricas['duplicatas_detectadas']}")
    print(f"   Latência total:      {metricas['latencia_total_s']}s")
    print(f"   Erros:               {len(metricas['erros'])}")
    if metricas["erros"]:
        for e in metricas["erros"]:
            print(f"      ❌ {e}")
    print("=" * 60)
    
    # Salvar relatório JSON
    relatorio_path = Path(f"A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/Dados/relatorios/smoke_{TEMA}_{RUN_ID}.json")
    relatorio_path.parent.mkdir(parents=True, exist_ok=True)
    with open(relatorio_path, "w", encoding="utf-8") as f:
        json.dump(metricas, f, ensure_ascii=False, indent=2)
    print(f"📄 Relatório salvo: {relatorio_path}")

# --- MAIN -------------------------------------------------------------------

def main():
    print(f"🚀 Iniciando smoke test: {TEMA}")
    conn = conectar_db()
    
    # 1. Verificar schema
    if not verificar_schema(conn):
        print("❌ Schema inválido. Abortando.")
        return 1
    
    # 2. Limpar run anterior
    limpar_run_anterior(conn)
    
    # 3. Rodar coletor (dry-run ou limitado)
    itens = rodar_coletor()
    metricas["itens_coletados"] = len(itens)
    
    # 4. Inserir e verificar dedup
    for item in itens:
        if verificar_dedup(conn, item["hash_dedup"]):
            metricas["duplicatas_detectadas"] += 1
            continue
        inserir_bruta(conn, item)
        registrar_evento(conn, item["id"], "nova")
    
    conn.commit()
    
    # 5. Relatório
    gerar_relatorio()
    
    # 6. Verdict
    if metricas["erros"]:
        print("\n🔴 FALHA — Smoke test com erros")
        return 1
    if metricas["itens_inseridos"] == 0 and metricas["itens_coletados"] > 0:
        print("\n🟡 ATENÇÃO — Todos os itens eram duplicatas")
    else:
        print(f"\n🟢 SUCESSO — {metricas['itens_inseridos']} itens inseridos")
    return 0

if __name__ == "__main__":
    exit(main())
```

### 3.3 Thresholds de Aprovação

| Métrica | Mínimo | Ideal | Crítico |
|---------|--------|-------|---------|
| Itens coletados | ≥ 1 | ≥ 5 | 0 = falha |
| Itens inseridos | ≥ 1 | ≥ 5 | 0 = atenção |
| Duplicatas | < 50% | < 20% | > 80% = problema |
| Latência total | < 300s | < 120s | > 600s = falha |
| Latência por fonte | < 30s | < 10s | > 60s = lento |
| Erros | 0 | 0 | > 0 = falha |
| Schema OK | ✅ | ✅ | ❌ = bloqueante |
| Eventos registrados | ✅ | ✅ | ❌ = bloqueante |

---

## 4. Ordem de Smoke Tests por Prioridade

Seguindo a ordem do Codex:

| # | Coletor | Banco Legado | Prioridade | Status Smoke |
|---|---------|-------------|------------|--------------|
| 1 | `trends` | 188 itens | 🔴 Alta | ⏳ Pendente |
| 2 | `nacional` | 70 itens | 🔴 Alta | ⏳ Pendente |
| 3 | `geopolitica` | 70 itens | 🔴 Alta | ⏳ Pendente |
| 4 | `soberania` | 28 itens | 🟡 Média | ⏳ Pendente |
| 5 | `crime` | 17 itens | 🟡 Média | ⏳ Pendente |
| 6 | `lula` | 10 itens | 🟡 Média | ⏳ Pendente |
| 7 | `ia` | 1 item | 🟢 Baixa | ⏳ Pendente |
| 8 | `matriz_energetica` | 1 item | 🟢 Baixa | ⏳ Pendente |
| 9 | `latam` | 0 itens | 🟢 Baixa | ⏳ Pendente |
| 10 | `sheinbaum` | 0 itens | 🟢 Baixa | ⏳ Pendente |

---

## 5. Checklist Antes de Executar Cada Smoke Test

- [ ] Coletor migrado está em `Sistema/agentes/<tema>/coletor_<tema>.py`
- [ ] Diretriz `diretriz_<tema>.json` existe e é válida
- [ ] Fontes foram migradas e testadas
- [ ] Banco local `pipeline_editorial_local.db` está acessível
- [ ] Nenhum outro processo está escrevendo no banco
- [ ] Modo é dry-run ou limitado (máx 10 itens)
- [ ] Logs serão salvos em `Dados/relatorios/`

---

## 6. Status deste Framework

**🟡 NÃO EXECUTADO — AGUARDANDO APROVAÇÃO**

Este fórum é uma **proposta de framework**. Nenhum smoke test foi rodado ainda. A execução só deve acontecer após:
1. Aprovação do Miguel
2. Migração do primeiro coletor (`trends`) pelo Codex
3. Confirmação de que o banco local está pronto

---

> **Regra:** Nada de deploy, nada de Tencent, nada de cron, nada de WordPress. Este sprint é local e arquitetural-operacional.

— Kimi (Maestro Diagnóstico), 13/06/2026
