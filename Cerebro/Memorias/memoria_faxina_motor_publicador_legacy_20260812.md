# Memória — Faxina: `motor_publicador.py` → LEGACY (log técnico)

**Data:** 2026-08-12 ~11:00 BRT
**Autor:** ZCode (GLM-5.2, fallback final — Kimi/Qwen 🔴🔴)
**Servidor alvo:** NYC (`nyc` = `root@198.199.121.136`)
**Par:** `Foruns/forum_faxina_motor_publicador_legacy_20260812.md`

---

## 1. Contexto e motivação

Diagnóstico do agente auditor de títulos (mesma sessão) revelou que o `motor_publicador.py` e o `gate_titulo.py` (cerco de títulos longos, 09/08) estavam **órfãos do cron** — eu montei um plano de "conselheiro de títulos" partindo da premissa errada de que vigoravam no fluxo de publicação. O Miguel corrigiu: *"motor_publicador é legacy, V4 substituiu, me confundiu — tira de Nova York e do local, bota no Legacy, indexa, faz o rollback"*. Esta faxina executa a ordem.

O cutover V4 (09/08, ver `memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`) já tinha aposentado o `agente_controlado.py` (movido a `/root/legacy/agente_controlado_aposentado_20260809/`). Esta faxina segue o mesmo padrão datado para o `motor_publicador.py`.

## 2. FASE 0 — portão de segurança (read-only, antes de mover)

### 2.1 Crontab ativo NYC — referências ao motor/agentes-irmãos

```bash
ssh nyc 'crontab -l | grep -v "^#" | grep -v "^$" | \
  grep -iE "motor_publicador|agente_china|agente_lula|agente_master_geopolitica|\
agente_master_nacional|publicador_tematicos|publish_caiado|iniciar_publicacao|\
escudar_modulo|agente_controlado"'
# → VAZIO. Ninguém no cron ativo chama o motor_publicador ou seus agentes.
```

Cadeia V4 ativa no cron (confirmada, a cada 30min por vertical):
```
0,30  *  geopolitica: coletor.py geo   → v4_vertical_intake.py geopolitica  → v4_vertical_draft_worker.py geopolitica
10,40 *  ciencia:     coletor.py tec   → v4_vertical_intake.py tecnologia   → v4_vertical_draft_worker.py ciencia
20,50 *  nacional:    coletor.py pol   → v4_vertical_intake.py politica      → v4_vertical_draft_worker.py nacional
```
+ auditor de títulos (`*/10` + `:58`), auditor indexação (`14 6`), repetidor estatal.

### 2.2 Cadeia V4 não importa o motor nem irmãos

```bash
ssh nyc 'for alvo in motor_publicador gerenciador_imagens util_detectar_recusa \
  publicador_tematicos revisor_titulo_luxo verificador_indexing_retroativo \
  agente_crime agente_latam; do
  for core in v4_vertical_draft_worker.py v4_labs/codigo/v4_vertical_redactor_runtime.py \
    v4_vertical_intake.py coletor.py; do
    grep -nE "import $alvo|from $alvo" /root/$core 2>/dev/null
  done
done'
# → VAZIO. A cadeia V4 ativa não puxa nenhum desses. Mover é seguro.
```

### 2.3 Imports reais (`import`/`from`) de motor_publicador

Apareceram **apenas em agentes-irmãos legacy** (fora do cron): `agente_crime`, `agente_latam`, `agente_matriz_energetica`, `agente_sheinbaum`, `agente_militar`, `agente_soberania`, `agente_ia`, `agente_lula`, `agente_reciclador`, `agente_master_geopolitica`, `agente_master_nacional`, `publish_caiado` + cópias em `/root/cafezinho/portal_cafezinho/` (`publish_china_draft`, `update_china_draft`, `scratch/publica_artigo`, `agente_master_lula_legacy`, `agente_master_trends_legacy`).

### 2.4 `gate_titulo.py` é autossuficiente

O `gate_titulo.py` **não** importa `motor_publicador` (o contrário: era importado por ele). Confirmado: ficou intacto e importável no `/root` após o movimento.

**Veredito FASE 0:** ✅ seguro para mover — runtime V4 intacto.

## 3. Execução (backup + mover)

### 3.1 NYC
```bash
ssh nyc 'set -e
TS=$(date +%Y%m%d_%H%M%S); DATA=$(date +%Y%m%d)
BK=/root/Backups; DEST=/root/legacy/motor_publicador_aposentado_${DATA}
mkdir -p $BK $DEST
cd /root
tar -czf $BK/faxina_motor_publicador_${TS}.tar.gz \
  motor_publicador.py \
  motor_publicador.py.bak_pre_cerco_titulos_20260809 \
  motor_publicador.py.bak_pre_safety_net_95_20260609_2330_claude \
  motor_publicador.py.bak_sprint_cat_20260610
# sha256: dddabe6653577fd45fe73c49dd332759d6eb9a3c6da51ce35fb5ac5f54f5575d
mv motor_publicador.py $DEST/
mv motor_publicador.py.bak_pre_cerco_titulos_20260809 $DEST/
mv motor_publicador.py.bak_pre_safety_net_95_20260609_2330_claude $DEST/
mv motor_publicador.py.bak_sprint_cat_20260610 $DEST/'
```

**Resultado NYC:**
- Backup: `/root/Backups/faxina_motor_publicador_20260812_135635.tar.gz`
- Destino: `/root/legacy/motor_publicador_aposentado_20260812/` (4 arquivos: motor 148885 B + 3 `.bak`)
- `/root/motor_publicador.py` → não existe mais
- `/root/gate_titulo.py` (7060 B) → intacto

**Rollback:** `tar -xzf /root/Backups/faxina_motor_publicador_20260812_135635.tar.gz -C /root`

### 3.2 Espelho local
```bash
cd "Projeto Cafezinho Agentes/root"
DEST=legacy/motor_publicador_aposentado_20260812
mkdir -p $DEST
mv motor_publicador.py $DEST/
mv motor_publicador.py.bak* $DEST/   # local tinha 1 .bak: .bak_pre_foto_na_hora_20260728
```
**Resultado local:** `Projeto Cafezinho Agentes/root/legacy/motor_publicador_aposentado_20260812/` (motor 145697 B + 1 `.bak` 145338 B).

## 4. Smoke pós-movimento (tudo verde)

```bash
ssh nyc 'cd /root
# SMOKE 1: py_compile
/root/venv/bin/python3 -m py_compile legacy/motor_publicador_aposentado_20260812/motor_publicador.py  # OK
/root/venv/bin/python3 -m py_compile gate_titulo.py                                                    # OK
/root/venv/bin/python3 -m py_compile v4_vertical_draft_worker.py v4_vertical_intake.py coletor.py \
  agente_repetidor_estatal.py agente_auditor_titulos_gpt.py auditor_indexacao_posts.py                # 5/5 OK
/root/venv/bin/python3 -m py_compile v4_labs/codigo/v4_vertical_redactor_runtime.py                    # OK
# → 9/9 OK

# SMOKE 2: gate_titulo autossuficiente
/root/venv/bin/python3 -c "import gate_titulo; print(hasattr(gate_titulo,\"aplicar_gate_titulo\"))"
# → True

# SMOKE 3: motor_publicador não mais importável do /root
/root/venv/bin/python3 -c "import motor_publicador"
# → ModuleNotFoundError: No module named "motor_publicador"  (esperado)

# SMOKE 4: crontab íntegro
crontab -l | grep -v "^#" | grep -v "^$" | wc -l   # → 35 linhas ativas
crontab -l | grep -v "^#" | grep -v "^$" | grep -i motor_publicador   # → vazio'
```

## 5. Indexação no Cérebro

- `CEREBRO_NODE_CODIGO_MORTO_INDEXADO.md` → nova seção "🆕 Aposentados posteriores à faxina 2026-06-23" (motor_publicador + tabela + sinalização dos 14 órfãos).
- `CEREBRO_NODE_ATUALIZACOES.md` → entrada cronológica no topo.

## 6. Sinalização — órfãos pendurados (fora de escopo)

14 agentes-irmãos legacy ficaram com `import motor_publicador` quebrado (ImportError se rodados manualmente). **Nenhum no cron** → não afetam runtime automático. Próxima faxina decide:

`agente_crime`, `agente_lula`, `agente_master_geopolitica`, `agente_master_nacional`, `agente_reciclador`, `agente_latam`, `agente_matriz_energetica`, `agente_sheinbaum`, `agente_militar`, `agente_soberania`, `agente_ia`, `publish_caiado`, `agente_master_lula_legacy`, `agente_master_trends_legacy` + cópias em `/root/cafezinho/portal_cafezinho/` (`publish_china_draft`, `update_china_draft`, `scratch/publica_artigo`).

## 7. Pendência Miguel

- (a) Autorizar próxima faxina dos 14 órfãos? Ou deixar sinalizado por enquanto?
- (b) Conselheiro de títulos (Gemini 3.1 Pro, consultivo) — retomar o plano agora sem a confusão do motor_publicador?
