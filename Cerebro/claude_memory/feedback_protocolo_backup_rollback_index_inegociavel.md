---
name: feedback-protocolo-backup-rollback-index-inegociavel
description: "Toda mudança em produção (Cafezinho/Rio Carta/GSN) DEVE ter: (1) backup arquivo com timestamp+autor, (2) rollback testado e documentado no fórum, (3) entrada no índice de mudanças. Inegociável (Miguel 24/05 10:55 BRT)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 42789f13-00c9-4e70-9b8c-f37d93570ab6
---

# Protocolo backup + rollback + índice — INEGOCIÁVEL (Miguel 24/05 10:55 BRT)

> "não esquece de fazer rollback, backups e indexar toda e qq mudança, para a gente saber o que fazer em caso de erro"

## 3 elementos obrigatórios em TODA mudança em produção

### 1. Backup com timestamp + autor

Formato canonical:
```bash
sudo cp /root/<arquivo>.py /root/<arquivo>.py.bak_pre_<motivo>_$(date +%Y%m%d_%H%M)_<autor>
```

Exemplos válidos hoje:
- `motor_publicador.py.bak_pre_anti_meta_250605_20260524_021809_codex`
- `motor_publicador.py.bak_pre_russia_20260524_022722_codex`
- `fact_check_perplexity.py.bak_pre_patch_6B2_20260523_2229_claude`
- `diretrizes_editoriais.py.bak_pre_russia_20260524_022722_codex`

**Onde:** mesmo diretório do arquivo (Tencent `/root/`). Backups B2 (Backblaze) já cobrem incremental geral; backups locais cobrem rollback rápido.

### 2. Rollback testado e documentado no fórum da sprint

Documentar comando exato no §rollback do fórum:
```bash
sudo cp /root/<arquivo>.py.bak_pre_<motivo>_<timestamp>_<autor> /root/<arquivo>.py
sudo python3 -c "import ast; ast.parse(open('/root/<arquivo>.py').read()); print('rollback syntax OK')"
```

Critério de gatilho de rollback (escolher 1):
- Smoke pós-deploy falha
- Taxa de rejeição sobe >2× baseline em 30min
- HTTP 500 em produção
- 3+ tracebacks em 10min relacionados ao patch

### 3. Índice de mudanças no Cérebro

Toda mudança vai em **`CEREBRO_NODE_BUGS.md`** (ou criar `CEREBRO_NODE_MUDANCAS.md` se preferir frente separada) com:
- Timestamp deploy
- Arquivo(s) afetado(s)
- Autor (Codex, Claude, Kimi Code)
- Sprint vinculada
- Path do backup
- Comando de rollback
- Smoke pós-deploy: PASS/FAIL
- Link pro fórum da sprint

**Exemplo de entrada:**
```markdown
### [2026-05-23 22:33 BRT] Sprint A — Patch fact_check_perplexity SYSTEM_PROMPT
- **Arquivo:** /root/fact_check_perplexity.py (+939 bytes)
- **Autor:** Claude
- **Backup:** /root/fact_check_perplexity.py.bak_pre_patch_6B2_20260523_2229_claude
- **Rollback:** `sudo cp <backup> /root/fact_check_perplexity.py`
- **Smoke:** 4/4 PASS (Datafolha TRUE, Gaza FALSE, IBGE TRUE, Macron FALSE)
- **Fórum:** Foruns/forum_sprint_A_perplexity_patch_20260523.md
- **Status:** ativo em produção
```

## Quando não aplica (exceção rara)

- Criação de arquivo NOVO sem efeito em produção (ex: helper isolado) — não tem o que "backupar". Mas ENTRADA NO ÍNDICE é obrigatória.
- Edição em fórum/canal/Cérebro (texto, não código) — git já cobre, mas anote no commit message.

## Auto-verificação ao deployar

Antes de marcar sprint como ✅ deployada, conferir:
- [ ] Backup criado com timestamp + autor no nome
- [ ] Rollback documentado no fórum
- [ ] Entrada no índice do Cérebro (CEREBRO_NODE_BUGS.md ou MUDANCAS)
- [ ] Smoke pós-deploy reportado (PASS ou FAIL)
- [ ] Canal Trindade avisado

Se faltar 1 dos 5 → deploy não está "completo".

## Relacionado
- [[feedback_validacao_pos_deploy_http_e_plugin]] — §12 Cérebro validação pós-deploy
- [[feedback_credito_explicito_detector_decisor]] — §nomear autor

— Inscrito por Claude Maestro 2026-05-24 10:55 BRT (regra suprema Miguel)
