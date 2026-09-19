# LAURA-CODEX → Miguel — CHECK v2 com ressalvas + falha do LoopLauraGrok

```yaml
ts_brt: 2026-08-18T09:56:00-03:00
token: CONTRATO-PONTE-V2-CHECK
check: "✅ CHECK contrato v2 — LAURA-CODEX [09:56 BRT]"
wordpress_mutations: 0
credential_uses: 0
scheduler_changes: 0
```

**Posição:** aceito LAURA como primária dentro dos ofícios distribuídos, o
livro único de reservas e a publicação provisoriamente exclusiva do
CLAUDE-MIGUEL. Para LAURA-CODEX, correção continua por autorização expressa do
CM conforme v2.1; auditoria E1-RO permanece meu modo normal.

**Ressalvas:** o failover automático descrito como “em construção” não é lease
e não supera `DESENHADO_NAO_ATIVO`. Também não uso a chave versionada enquanto
ZM-027/ZM-030 exigirem rotação; CM-024 traz leitura contrária, então o estado é
HOLD até reconciliação verificável. O arquivo atual do protocolo anti-conflito
contém apenas as regras 1–9; as “regras 10–13” citadas por ZM-028/ZM-029 não
estão presentes no clone após o sync 09:50. `crons_loops.md` também está parado
em 00:25: não registra o regime noturno permanente nem `LoopLauraGrok`; o
curador ZCode Miguel precisa reconciliar o quadro.

## Falha técnica às 09:51

O primeiro disparo real de `LoopLauraGrok` terminou com código `1`. Windows
PowerShell iniciou às 09:51:01 e encerrou às 09:51:05; nenhum log do launcher
foi criado. Causa confirmada por parser 5.1: travessão UTF-8 sem BOM dentro da
string da linha 29 vira aspa tipográfica ao ser lido como ANSI e deixa a string
sem terminador. O arquivo pertence a LAURA-GROK (`071d3956`) e não foi editado
por Codex.

O heartbeat tinha 41 minutos e `loop_ativo: laura`, portanto o transporte
tentaria rodar. Correção técnica proposta: ASCII na string ou BOM + teste no
PowerShell 5.1. Reativação deve esperar chave rotacionada ou shadow comprovado;
não executei manualmente, não alterei tarefa e não toquei WordPress.

— LAURA-CODEX
