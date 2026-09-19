# 💌 CARTINHA — Kimi K3/ZCode → Claude Code

**Data:** 2026-08-05 14:40 BRT
**Assunto:** 🤝 HANDOFF FORMAL — você é o EXECUTOR do BACKUP TOTAL (resto = seu, no seu loop). Eu viro só fiscal.
**Tag canal:** `[KIMI-HANDOFF-BACKUP-TOTAL-EXECUTOR-CLAUDE]`
**Substitui/complementa:** `cartinha_kimi_claude_backup_total_100_drive_20260805_1255.md`

---

Claude,

O Miguel leu o andamento e foi explícito: **o restante do backup é para VOCÊ fazer, no SEU loop — "cada loop ele faz um pouco"**. Eu (Kimi) saí do papel de executor: meu cron agora é só fiscal (vigia o ESTADO, te re-pinga se travar, alerta o Miguel se passar de 24h parado). Já fechei o **C01** (pautas ✔ verificado) e deixei o **C02** parcial (rclone retoma de onde parou).

## Seu protocolo de loop — 5 passos por acordada

1. Abra `Cerebro/backup_total_2026/ESTADO.md` → pegue o **1º chunk `PENDENTE`** (ou `EM_ANDAMENTO` parado >75 min = travado).
2. Marque `EM_ANDAMENTO | claude | <ts BRT>` na linha do chunk.
3. Rode o comando do chunk conforme `PLANO_BACKUP_TOTAL_100.md` §4, template §3: `timeout 1500 rclone copy …` (excludes de `node_modules`/`__pycache__`/`*.pyc`/`.Trash`; log em `logs/<ID>.log`). **Uma janela ≤25 min.** Se sua sessão tiver tempo, repita com o próximo chunk — cada janela é independente e o rclone retoma sozinho quando cortado.
4. Fim da janela: exit 0 → `CONCLUÍDO` + nota de verificação (linha `Total size` do log ou `rclone size` origem×destino); timeout/erro → volta a `PENDENTE` com nota. **Em ambos os casos: +1 linha na tabela de `Cerebro/Memorias/memoria_backup_total_2026.md`.**
5. Se deu a hora de fechar sua sessão: deixe o ESTADO coerente (nada de EM_ANDAMENTO órfão com processo morto sem nota).

## Limites (não negociáveis)

- **NÃO** subir `cofre_intake/` nem `gcloud_indexing_keys/` (segredos — rito do Cofre).
- **NÃO** re-upar `orlando diniz` nem `Jornais do dia` do Dados_Frios (já espelhados na raiz do Drive — ver mapa `Cerebro/backup_total_2026/MAPA_GERAL_ARQUIVOS_E_BACKUPS_20260805.md`).
- **FASE 2 (Backblaze B2) 🔒 DESATIVADA** — só o Miguel liga.
- Erro de cota/rate-limit do Drive: marca PENDENTE, avisa no canal, não insiste.

## Fechamento (sua missão final)

C01–C15 `CONCLUÍDO` → rode **C16** (verificação `rclone check`/`size` por destino) → tudo limpo → poste **`[BACKUP-TOTAL-100-FASE1-DRIVE-CONCLUIDA]`** no canal_trindade. O Miguel só limpa o disco depois dessa tag. Referência do que é cada pasta: o MAPA canônico acima.

ACK esperado no canal: `[CLAUDE-BACKUP-TOTAL-100-ENTRANDO-NO-LOOP]` quando você assumir.

Abs,
Kimi K3 (ZCode) — agora só na arquibancada fiscalizando 🫡
