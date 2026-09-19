---
name: Backup só em Backblaze B2 — não acumular em Tencent local
description: Miguel 17:58 BRT 09/05 — backup é apenas Backblaze, não fazer backup em Tencent. Disco Tencent é pra produção viva, não armazenamento de histórico.
type: feedback
originSessionId: 508809f1-d779-44e6-85dc-eeff08788235
---
**Regra (Miguel 2026-05-09 17:58 BRT):** *"backup é apenas o backblaze, não faça backup em tencent"*.

**Tradução:**
- Tarballs diários para B2 já estão configurados (cron `0 6 * * * auto_backblaze_cleanup.sh` instalado 09/05)
- Backups `.py.bak_pre_X` em `/root/` no Tencent **NÃO devem acumular**
- Pra mudanças críticas individuais: criar backup específico em B2 antes do deploy
- Disco Tencent é pra **produção viva**, não armazenamento de histórico

**Why:** memória `feedback §17 Cérebro 14:05 BRT 05/05` registrou disco Tencent em 98% por acúmulo. B2 cleanup diário resolveu (50% agora). Mas a tendência de criar `.bak` localmente vai voltar a encher. Padrão correto: backup vai pra B2, local fica limpo.

**How to apply:**
- Codex (e qualquer agente que patche): após fazer backup local pré-deploy + validar, **mover backup pra B2 OU deletar local após 24h**
- Pra patches incrementais (low risk): pode confiar no tarball diário B2 (`:06:00`)
- Pra patches críticos: criar backup nomeado em B2 antes do deploy
- Comando padrão: `rclone copy /root/agente_X.py.bak_pre_Y_TS b2:cafezinho-backups/criticos/`
- NÃO mais fazer `cp /root/agente_X.py /root/agente_X.py.bak_TS` sem mover pra B2 depois

**Aplicabilidade:** Codex (mais afetado — ele cria a maioria dos `.bak` no Tencent). Claude (menos, mas pode acontecer). Antigravity (raro).

**Caso fundador:** sangria de disco 05/05 14:05 BRT — Tencent foi a 98%, comentarista entrou em loop. B2 cleanup configurado 09/05 14:43 BRT. Regra 17:58 BRT formaliza pra evitar repetir.
