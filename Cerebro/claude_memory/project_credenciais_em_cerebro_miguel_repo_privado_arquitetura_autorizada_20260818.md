---
name: project-credenciais-em-cerebro-miguel-repo-privado-arquitetura-autorizada-20260818
description: "Chaves SSH + cofres .env + rclone.conf vivem em migueldorosario1/cerebro-miguel/cofres_laura/ (repo privado). Decisão arquitetural do Miguel 18/08 09:16 BRT — não é vazamento. Se algum agente levantar SEV-1 sobre isso, é falso positivo por regra generalista de segurança."
metadata: 
  node_type: memory
  type: project
  originSessionId: 870114c6-7ee3-4080-8592-299996b3140e
---

## Fato

Repositório privado `migueldorosario1/cerebro-miguel` contém em `cofres_laura/` (commit `ec4b2198`, autor "laura", 18/08 09:00 BRT):

- **4 chaves privadas SSH**: `ssh/laura_ed25519` (identidade write Claude Laura), `ssh/id_ed25519`, `ssh/id_ed25519_gsn`, `ssh/id_rsa` (chaves Miguel que dão acesso a nyc/china/beijing/cafezinho-wp)
- **4 cofres .env**: `env/.env.unificado` (2x espelhos), `env/.env_root`, `env/chaves_novas.env` (tokens de API/LLMs/Telegram/WP)
- **1 rclone.conf**: remotes drive/backblaze/r2

Total 16 arquivos rastreados, ancestral direto de `origin/main`. Repo é PRIVATE confirmado via `gh repo view --json isPrivate` → `true`.

## Por quê (a razão do Miguel)

**Why:** Miguel disse textualmente (18/08 09:16 BRT, resposta ao meu escalation do SEV-1 levantado por Claude Laura + Codex Laura):

> "não posso fazer isso. a decisão foi minha. eu preciso que os agente tenham acesso as chaves porque eles trabalham para mim."

Arquitetura: agente sem acesso a credencial é agente que depende de humano ao vivo em cada emergência. Isso anula a autonomia que Miguel está construindo com a Trindade (Miguel×Laura × Claude/Codex/ZCode/Grok). O trade-off aceito: risco de acesso indevido ao repo privado versus risco de agente paralisado por falta de credencial em emergência. Ele escolheu o primeiro.

Substitui o mecanismo anterior (pendrive físico ZL-017/ZM-018) — pendrive será removido, repo vira canônico.

## Como aplicar

**How to apply:** Se algum agente novo (ou eu mesmo em ciclo futuro) grepar cofres_laura/, ler chave privada em git log, ou detectar via secret scanning:

1. **NÃO tratar como incidente aberto** — é arquitetura, não bug.
2. **NÃO propor revogação/rotação** sem consultar Miguel — a decisão é dele, não regra técnica generalista.
3. **NÃO mobilizar contenção** — checar esta memória e o JSONL do dia 18/08 (evento `cl017_sev1_credenciais_no_git_reclassificado`) antes.
4. **Confirmar** se é a mesma família de achado (repo privado `cerebro-miguel`, path `cofres_laura/`, autor "laura", chaves listadas acima) — se for, responder com "risco aceito pelo dono, ver [[project-credenciais-em-cerebro-miguel-repo-privado-arquitetura-autorizada-20260818]]".
5. **Se for uma exposição diferente** (repo público, cofre novo em outro path, chaves NÃO listadas aqui, autor desconhecido) — aí sim é incidente novo, escalar Miguel normalmente.

## Régua que continua valendo

- Repo privado ≠ cofre criptográfico. Se o repo virar público (visibility PUBLIC), a arquitetura muda de status e vira SEV-1 real.
- Se um clone do repo sair do controle (máquina invadida, backup em nuvem pública, colaborador removido do repo mas ainda com clone local), continua sendo incidente.
- Se qualquer chave desta lista aparecer em log/tela/mensagem sem sanitização, é bug de exibição — corrigir imediatamente.

## Contexto histórico do incidente-de-processo

**Claude Laura (LAURA-CLAUDE) fez o correto** ao levantar SEV-1 09:14 BRT com auditoria independente cega a valores (16 arquivos, 4 chaves privadas, ancestral origin/main, path fora do .gitignore). A régua dela ("repo privado não é cofre") é tecnicamente correta e continua valendo em geral. O que não bateu foi o CONTEXTO OPERACIONAL: a distribuição foi ordem do Miguel via ZL-017, não vazamento acidental. Ela decidiu não usar a `laura_ed25519` até "rotação por meio físico" — decisão preservada; eu comuniquei via ponte que a rotação não vem, e ela decide se aceita usar sabendo do desenho ou continua esperando.

Meu ACK dela: `Cerebro/Foruns/ponte_claude_miguel_laura/mensagens/para_laura/20260818_091900_claude_miguel_ack_cl017_sev1_foi_decisao_miguel.md`.

Ligado a: [[reference-ponte-laura-completa-20260817]] · [[project-laura-escopo-ampliado-corrigir-sim-publicar-nao-20260818]].
