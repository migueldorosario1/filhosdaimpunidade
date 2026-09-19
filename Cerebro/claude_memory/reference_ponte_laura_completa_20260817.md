---
name: reference-ponte-laura-completa-20260817
description: "Ponte Laura Completa (17/08/2026 23h) — 6 agentes (Claude/Codex/ZCode Miguel + Claude/Codex/ZCode Laura) via GitHub. Trilho 15min. Leitura ENCAIXADA no loop */20 do Claude Miguel, sem cron novo. Meu prefixo CM-, ledger próprio, estado próprio, append-only."
metadata:
  node_type: memory
  type: reference
  originSessionId: e8e1110d-efa6-4c4b-8e2b-d11b38f55da8
---

Ponte Laura Completa criada 17/08/2026 ~23:00 BRT por ordem Miguel (autor: ZCode Miguel).

## Estrutura

`Cerebro/Foruns/ponte_laura_completa/`:
- `CONTRATO_PONTE_COMPLETA.md` — regras completas
- `de_dell.md` — agentes do Dell escrevem AQUI (Claude Miguel, Codex Miguel, ZCode Miguel)
- `de_laura.md` — agentes da Laura escrevem AQUI (Claude Laura, Codex Laura, ZCode Laura); eu LEIO
- `estado/<agente>.md` — 6 arquivos de estado (só dono escreve)
- `ledger/<agente>.md` — 6 ledgers append-only (só dono escreve; registrar ACK aqui)

**Arquivos disjuntos por máquina = zero conflito git** (2 arquivos de mensagem, 1 por lado).

## Minhas responsabilidades (Claude Miguel = CM-)

- **Prefixo ref:** `CM-YYYYMMDD-NNN` (sequencial por dia)
- **Escrevo em:** `de_dell.md` (append-only, formato `[DD/MM/AAAA HH:MM BRT] CM-... — Claude Miguel → <PARA>: <assunto>\n<texto>`)
- **Meu ledger:** `ledger/claude_miguel.md` (append-only; formato `ACK <REF> [ts] <1 linha>` quando leio; `<MEU-REF> emitida — <descrição>` quando envio)
- **Meu estado:** `estado/claude_miguel.md` (1-3 linhas do que estou fazendo agora — reescrevo a cada mudança)
- **Nunca** editar linha de outro agente. Correção = linha nova.
- **Nunca** valores de segredos — só caminhos e como testar.

## Como encaixar no loop Vigília V6 (regra Miguel: SEM cron novo)

**Preflight de cada Slot A/B do meu loop `*/20`** (adicionar ao ritual existente):

1. `tail -20 Foruns/ponte_laura_completa/de_laura.md` (mensagens novas dos agentes Laura)
2. `grep "ACK CM-" Foruns/ponte_laura_completa/ledger/*.md` (ver quem já reconheceu minhas emissões)
3. Se houver mensagem endereçada a mim (Claude Miguel) OU relevante ao meu papel (coordenação/editorial/CCTV):
   - Registrar ACK no `ledger/claude_miguel.md`
   - Se pede ação: responder em `de_dell.md` com `CM-YYYYMMDD-NNN`
   - Atualizar `estado/claude_miguel.md` se meu foco mudou

**Latência esperada:** ~30min (trilho GitHub 15min Dell push :07/:22/:37/:52 + pull :00/:15/:30/:45 Windows Laura). Mensagem escrita agora chega em ~15-30min.

## Ref sequencial

Numeração diária começa em 001. Reset todo dia. Nunca reusar. Ex.: `CM-20260817-001`, `CM-20260817-002`.

## Escopo — o que vai na ponte vs onde vai o resto

- **Ponte** = mensagens OPERACIONAIS entre agentes das duas máquinas
- **Cérebro** (fora da ponte, mas mesmo repo) = conhecimento perene, memórias, contratos, nodes
- **Ledger Trindade** (`Foruns/inbox_trindade/*` + `canal_trindade.md`) = coordenação intra-Miguel (Claude+ZCode+Codex+Laura via ponte antiga)
- **Ponte Claude Miguel/Laura** (`ponte_claude_miguel_laura/mensagens/`) = alertas editoriais LAURA-CLAUDE (§126)

**Não duplicar.** Se mensagem já foi via inbox_trindade ou ponte editorial, não repetir na ponte laura completa.

## Missão imediata (Miguel)

Configurar na Laura o **sistema de monitoramento do ecossistema** (painel CCTV V6, vigília, patrulhas). Vou ser CHAMADO por esta ponte quando o CCTV Laura precisar de coordenação editorial. Aguardar.

Relacionado: [[project-cadencias-trindade-20260817]] (cadências Trindade), [[feedback-laura-alertas-entrada-obrigatoria-20260817]] (§126 tratamento de alertas Laura vale também para mensagens de agentes Laura pela ponte completa).
