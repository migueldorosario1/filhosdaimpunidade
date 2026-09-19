---
name: project-laura-escopo-ampliado-corrigir-sim-publicar-nao-20260818
description: "Miguel 18/08 ~00:04 expandiu escopo Laura: 'corrigir sim, publicar não'. UPDATE 09:34: Laura EXECUTA correções pós-publicação diretas via cafezinho-wp-write + laura_ed25519 (não mais só propor). Publish/agendamento/data/status/lixeira/deleção continuam com dono único (Claude Miguel). Outros agentes (Grok Miguel/Laura, Codex Laura, ZCode Laura) pedem autorização pela ponte (ordem Miguel 09:26) — Laura-Claude é exceção com autonomia direta."
metadata:
  node_type: memory
  type: project
  originSessionId: e8e1110d-efa6-4c4b-8e2b-d11b38f55da8
---

## UPDATE 18/08/2026 09:34 BRT — Miguel liberou EXECUÇÃO direta

Miguel textual 09:34: "ok, vamos liberar a claude laura para edições pós-publicação. vou dizer isso ao zcode que está preparando novo contrato".

**Antes**: Laura propunha pela ponte, eu executava. Latência = meu ciclo Vigília (até 20min).
**Agora**: Laura executa direto via `cafezinho-wp-write` + `laura_ed25519` (ZL-016 instalada, homologada). Latência = zero.

**Meu papel muda pra revisão amostral** — checar `auth.log` do servidor (rastro por comando), `ledger/claude_laura.md`, e `de_laura.md`. Se detectar padrão problemático, sinalizo pela ponte editorial pra ela.

**Regra pros OUTROS agentes** (ordem Miguel 09:26 BRT em resposta ao pedido do Grok Laura sobre correções de imagem): Grok Miguel, Grok Laura (LAURA-GROK), Codex Laura, ZCode Laura — quando encontrarem erro em post, escrevem pedido em `Cerebro/Foruns/ponte_claude_miguel_laura/mensagens/para_miguel/` com **problema+proposta+evidência**; eu analiso e autorizo (ou peço mudança, ou nego). Claude Laura é exceção — tem autonomia direta pelo escopo ampliado. Contexto: Grok Laura assumiu capas V4 pela Emenda 4 (08:42) e primeiro pedido dele deve chegar hoje.

**Aviso enviado à Laura-Claude**: `ponte_claude_miguel_laura/mensagens/para_laura/20260818_093500_claude_miguel_liberacao_edicoes_pos_publicacao.md`.
**Aviso Trindade em de_dell.md**: CM-20260818-024 (09:35 BRT, commit 784e1a12).
**Contrato formal**: ZCode Miguel está preparando — este update é operacional.


Miguel 18/08/2026 ~00:04 BRT (via chat direto na Laura, reportado por CL-20260818-002):

> "corrigir sim, publicar não"

## Escopo permitido à Laura

- ✅ Corrigir **texto** do post
- ✅ Corrigir **título**
- ✅ Corrigir **resumo/excerpt**
- ✅ Corrigir **taxonomia** (categorias, tags)
- ✅ Corrigir/trocar **imagem** (fm + caption)

## Escopo NÃO permitido (continua exclusivo Claude Miguel)

- ❌ `publish` — mudar `post_status` de draft/pending pra publish
- ❌ **agendamento** (`future` + `post_date`)
- ❌ **mudança de data** (`post_date`, `post_date_gmt`)
- ❌ **mudança de status** (`post_status`)
- ❌ **lixeira** (`trash`)
- ❌ **deleção** (`delete`, `wp post delete`)
- ❌ `wp eval`, `wp db`, `wp option`, `wp user`, `wp plugin`, `wp theme`, `wp cron` (comandos administrativos)

## Bloqueio técnico atual (18/08 00:04)

**Laura ainda não pode executar** porque:
- Canal SSH disponível na máquina LAURA é `cafezinho-wp-ro` (E1-RO — Executor 1 Read-Only)
- Servidor aceita apenas 6 comandos de leitura: `health`, `list`, `show`, `media`, `taxonomy`, `recent`
- **Nenhuma ordem muda isso do lado Laura** — restrição está no servidor

## Ação necessária (dono: Miguel + ZCode Miguel)

Criar **identidade SSH de escrita** própria da Laura, com:
- **Lista positiva de comandos**: `update-title`, `update-content`, `update-excerpt`, `update-taxonomy`, `set-media`, `set-img-check`
- **Lista negativa explícita**: `publish`, `status`, `date`, `delete`, `trash`, `eval`, `db`, `option`, `user`, `plugin`, `theme`, `cron`
- Chave instalada na máquina (nunca colar valor em mensagem)

## Requisitos de homologação (proposto por Laura)

Antes de ativar canal write Laura:

1. **Reserva por post antes de qualquer edição** — mesmo livro de reservas anti-atropelo já usado pra imagens. Sem reserva ≠ edita. Evita 2 agentes corrigindo mesmo título em sentidos opostos.
2. **Prova negativa na homologação** — canal só é homologado quando alguém TESTA que servidor **recusa** `publish` e `delete` (não apenas que aceita `update`). Foi assim que E1-RO foi homologado. Manter a régua.

## Enquanto identidade não existir

Laura **propõe correção pela ponte** — por impossibilidade física, não por escolha:
- Alertas via ponte editorial `Foruns/ponte_claude_miguel_laura/mensagens/para_miguel/` (protocolo §126 CLASSIFICACAO_SUGERIDA)
- Ou via ponte laura completa `de_laura.md` (ref `CL-YYYYMMDD-NNN`)

Claude Miguel (eu) recebe, aplica correção via SSH cafezinho-wp (Dell tem write), reporta de volta via ponte.

## Impacto sobre regras existentes

- **§126 (alertas Laura entrada obrigatória)**: continua válida. Laura ainda usa ponte pra alertar; eu ainda ACK+classificação+decisão+justificativa. Diferença: agora várias correções são executáveis por ela quando identidade write existir.
- **Contrato Geral §2 (Laura SHADOW_READ_ONLY no WP/infra)**: **ATUALIZADO** pela ordem Miguel — Laura passa de `SHADOW_READ_ONLY` a `SHADOW_EDITORIAL_WRITE` (nome tentativo) para os 6 comandos positivos, mantendo READ_ONLY para os administrativos. Precisa entrar em Emenda futura (candidata a Emenda 3 ou 4 do Contrato Geral).
- **Contrato Integridade Imagens §5**: `_cafezinho_img_check` continua obrigatório; Laura passará a poder gravar recibo `ok:true` diretamente via `set-img-check`. Publish continua exclusivo Claude Miguel.
- **Publish 100% Claude** — mantido intacto.

## Vantagens esperadas

- Round-trip correção mais rápido (Laura vê → Laura corrige direto)
- Reduz meu volume de correções operacionais (foco em publish/coordenação)
- Redundância real de correção editorial (Loop Laura como espelho de execução)
- Laura pode aplicar suas próprias sugestões (que hoje passam pela minha aprovação sempre)

## Riscos monitorados

- Colisão entre Claude Miguel + Claude Laura editando mesmo post — **mitigado pela reserva obrigatória**
- Perda de rastreabilidade — **mitigado por ledger próprio Laura + closes_ref**
- Escopo escapar do positivo — **mitigado por lista negativa no próprio SSH server**

Relacionado: [[feedback-laura-alertas-entrada-obrigatoria-20260817]] (§126 base, agora com execução dela), [[reference-ponte-laura-completa-20260817]] (canais).
