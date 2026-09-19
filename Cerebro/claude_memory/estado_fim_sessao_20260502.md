---
name: Estado fim de sessão 2026-05-02
description: Snapshot completo do que foi deployado hoje + pendências em aberto pra próxima sessão pegar do zero. Dia foi sprint Modelos Dinâmicos (LLM tier system + governança custos).
type: project
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
# Estado fim sessão 2026-05-02 20:19 BRT

## ✅ Concluído hoje (deployado e validado)

### Sprint principal: LLM Tier System + Governança de Custos
1. **3 tiers dinâmicos** (`/root/config/tarefas_tier.json` MD5 `bf74460a41da3431301d2fa4d998a286`)
2. **Blocklist dinâmica** (`/root/config/modelos_blocklist.json`) com `auto_detected` flag — preenchida via smoke test diário
3. **Wrapper governado** `gerar_texto_governado(tarefa, sys_prompt, prompt, ...)` em `agente_roteador_llm.py` (MD5 `f22c2396f95e4370ad666990c9f4a644`)
4. **agente_validador_modelos.py** roda smoke test diário (cron `0 3 * * *`)
5. **Ondas A+B+C migradas** (15 agentes ao todo): publicador_tematicos, agente_china, motor_coletor, agente_crime, agente_news_trend, agente_diario_direita, agente_historiador, robo_coleta_bruta, urgencia_ira, bot_mapa_rio_telegram

### Bug de produção corrigido
- **Recusa LLM vazada como matéria publicada** (post 241982). Fix: `detectar_recusa_llm()` em `motor_publicador.py:444` (MD5 `5b7322a78cf5b58beaa11f2e43c2ac1b`). Memo: `bug_critico_vazamento_recusa_llm_20260502.md`

### Painel HTML de Despesas
- `/root/config/cambio.json` (USD→BRL fixo 5.10, MD5 `7a75d481c04a0706e95ac538e247e2c9`)
- `/root/gerador_painel_despesas.py` (MD5 `17e4096e6746023b06c1a2cea6deb472`) — cron `*/15 * * * *`
- Rota `/despesas` em `painel_cctv.py` — HTTP 200, 16.6KB
- **URL:** `http://43.156.151.165/despesas` · auto-refresh 60s
- Mostra: total mês/dia/semana (USD+BRL) · tier-via-tarefa · tier-via-modelo · top 30 agentes (com tokens) · top tarefas/modelos/contextos · timeline 30 dias

### Painel CCTV expandido
- `painel_cctv.py` (MD5 `f2fb5d49b6edd529c04724ddf0f744a2`) — lista expandida 11→**31 agentes** (6 coletores + 4 masters + 4 controle + 11 temáticos premium + 3 redes + 2 bots Telegram + 1 analytics)
- Match exato JS↔Python (auto-discovery via array sincronizado)
- **URL:** `http://43.156.151.165/`
- PID atual: 915256 · Backup: `/root/painel_cctv.py.bkp_pre_lista_expandida_20260502_2011`

### Migrações finais Onda
- `agente_curador_midia.py` (MD5 `1504efcb59c35a4e70b2013aafe6a2e3`) — registro de gasto Gemini 1.5 Flash (visão multimodal). Não migrou pro roteador (texto-only) mas custo agora rastreado. Backup `bkp_pre_governance_20260502_2008`

### Sistema dinâmico em fila redes
- `/root/config/prioridade_categorias.json` (MD5 `c0f9194c0ee5a2f285d691ceb969ca99`) — 17 P1 + 15 P2
- `gerenciador_fila_redes.py` (MD5 `e132bf8290225199ecb8ea0285789ae9`) — `calcular_prioridade()` lê config dinâmica com mini-cache mtime · failsafe pros hardcodes preservado · backup `bkp_pre_prio_dyn_20260502_1936`

### Cloud agent agendado
- Routine `trig_0136z8XfTVzA69JjMKMEdskm` (`0 12 * * 1` = segunda 09:00 BRT)
- Tarefa: BCB PTAX → comparar com 5.10 → propor JSON pronto se diff ≥1%
- Próximo run: **2026-05-04 09:06 BRT**

### Diagnósticos confirmados
- **BRAPI_TOKEN funcional** (Ibovespa 187.317,64 hoje 20:19 BRT)
- **Maestro timeout=300 estável** desde pelo menos 01/05 18:54 (não é regressão; backups confirmam)
- **0 NameErrors HOJE** dos 3 bugs de 01/05 (strip_html, gerenciador_tokens, hashlib) — fix solid

### Higiene editorial
- `forum_modelos_dinamicos_governanca_20260502.md` renumerado §1–§20 (eram §11/§12/§13 duplicados — Antigravity criou conflito de naming antes das seções individuais existirem)

## 🟡 Pendência ATIVA pra continuar amanhã

### Auto-detect runtime no roteador (Codex Q5) — INICIADO mas NÃO DEPLOYADO
**Estado atual:** roteador `agente_roteador_llm.py` lido. Plano de implementação completo abaixo. **Não tocou no arquivo Tencent ainda — local sincronizado com Tencent (MD5 `f22c2396f95e4370ad666990c9f4a644`).**

**Plano de implementação:**
1. Adicionar função `_auto_blocklistar_modelo(modelo, motivo, agente_nome)` antes do `def carregar_modelos_vivos()` (~linha 100)
2. Hook no outer except do `_gerar_texto_interno` (linha 555–556) — converge todas as falhas do for loop por modelo
3. Hook idêntico no `_gerar_texto_provider_hard_interno` (~linha 821+)

**Padrões PERMANENTES (auto-blocklistar):**
- "not a chat model" / "is not a chat model"
- "max_completion_tokens" + "is not supported"
- "only supported in v1/responses"
- "use max_completion_tokens instead"

**Padrões TRANSIENTES (NÃO blocklistar):**
- "API_KEY_INVALID", "Sem Chave", "401", "429"
- "500", "502", "503", "504"
- "timeout", "TimeoutError", "Connection"

**Estrutura proposta da função:**
```python
def _auto_blocklistar_modelo(modelo, motivo, agente_nome):
    PADROES_PERMANENTES = ("not a chat model", "max_completion_tokens",
                            "only supported in v1/responses", "use max_completion_tokens")
    PADROES_TRANSIENTES = ("API_KEY_INVALID", "Sem Chave", "401", "429",
                            "500", "502", "503", "504", "timeout",
                            "TimeoutError", "Connection")
    motivo_lower = motivo.lower()
    if any(p.lower() in motivo_lower for p in PADROES_TRANSIENTES):
        return False
    if not any(p.lower() in motivo_lower for p in PADROES_PERMANENTES):
        return False
    try:
        from datetime import datetime
        blockfile = "/root/config/modelos_blocklist.json"
        with open(blockfile, "r", encoding="utf-8") as f:
            data = json.load(f)
        bloqueados = data.setdefault("modelos_bloqueados", {})
        if modelo not in bloqueados:
            bloqueados[modelo] = {
                "motivo": motivo[:300],
                "detectado_em": datetime.now().isoformat(),
                "agente_origem": agente_nome,
                "auto_detected": True,
            }
            data["_atualizado"] = datetime.now().isoformat()
            tmp = blockfile + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            os.replace(tmp, blockfile)
            log(f"🚫 AUTO-BLOCKLIST: {modelo} adicionado por '{motivo[:80]}' (agente={agente_nome})")
            return True
    except Exception as e:
        log(f"⚠️ Falha ao auto-blocklistar {modelo}: {e}")
    return False
```

**Hook no except (linha 555):**
```python
except Exception as e:
    err_str = str(e)
    log(f"⚠️ Falha no modelo {modelo}: {err_str[:200]}. Subindo o próximo da fila...")
    try:
        _auto_blocklistar_modelo(modelo, err_str, agente_nome)
    except Exception:
        pass
```

**Próximos passos:** sincronizar local com Tencent (MD5 sanity), aplicar 2 Edits, deployar via SCP, smoke test runtime.

## 🔵 Outras pendências (sem urgência)
- **`claude_em_nyc.md`** — decisão estratégica indecisa (rodar Claude Code no servidor remoto)
- **`master_lula` anacronismo** — investigação aberta (parqueado)
- **Temáticos sem retry** — implementação de mecanismo de re-tentativa em falhas isoladas
- **Migrar `google.generativeai` → `google.genai`** — pacote deprecated, aviso oficial. Vários agentes afetados (agente_curador_midia, agente_crime, agente_news_trend, publicador_tematicos, agente_diario_direita)
- **`agente_curador_midia` migração total pro roteador** — exige sprint "vision tier" (suporte multimodal no roteador)
- **Painel CCTV auto-discovery dinâmico** — atualmente lista hardcoded no JS+Python; sprint futura: discovery via /var/log + crontab

## 📊 Métricas rápidas pra contexto
- 32k registros JSONL no `banco_custos_2026-05.jsonl` no momento do build do painel
- Total acumulado mês corrente: $110.58 USD
- 31 agentes ativos no CCTV (todos emitindo)
- 14 linhas temáticas no crontab + 3 autocura + sentinelas OK
- Crontab: 253 linhas (1 SHELL, 14 temáticos, 3 autocura, 1 sync_nyc_leve, 1 painel_despesas)
