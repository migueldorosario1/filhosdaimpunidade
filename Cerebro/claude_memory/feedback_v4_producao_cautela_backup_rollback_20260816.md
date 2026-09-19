---
name: feedback-v4-producao-cautela-backup-rollback-20260816
description: "Regra Miguel 16/08/2026 21:53: ao mexer no worker V4 (produção), pesquisar bem antes, indexar, backup e rollback preparados. 'Produção não se brinca'. Antes de qualquer patch no worker V4 (código NYC, mu-plugins, crons), escrever plano no ledger com backup + rollback + testes + esperar autorização Miguel explícita. Investigação read-only não precisa autorização, mas patch sim."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Regra vigente (a partir de 16/08/2026 21:53 BRT)

Toda intervenção no worker V4 em produção (código NYC `/root/v4_labs/`, mu-plugins do cafezinho-wp, crons, pipeline de imagens, publicador) exige protocolo de segurança **antes** de qualquer patch:

**Miguel textual (chat direto 21:53):**
> "ao mexer no v4 cuidado hein. pesquisa bem antes, indexa, faz rollback, backup. produção não se brinca."

## Protocolo obrigatório antes de patch

1. **PESQUISA** (read-only, sem autorização): grep amplo, ler código fonte, mapear função-alvo, identificar callers/dependentes, reproduzir bug com evidência concreta (ID de post + antes/depois esperado)
2. **INDEXAÇÃO**: documentar no ledger com bloco `[CLAUDE-MIGUEL-INVESTIGACAO-V4-<tema>-<TS>]`: arquivo/linha/função + entrada/saída atual vs esperada + evidência
3. **PLANO DE PATCH escrito**: bloco `[CLAUDE-MIGUEL-PROPOSTA-PATCH-V4-<tema>-<TS>]` com:
   - Diff exato (linhas removidas / adicionadas)
   - Backup do arquivo original (`cp -a <file> <file>.bak_pre_claude_<TS>`)
   - Rollback: comando exato para reverter (`cp <file>.bak_pre_claude_<TS> <file>`)
   - Testes: como validar antes de deploy (dry-run, teste unitário, canary post ID)
   - Impacto: quais posts/pipelines afetados
4. **AUTORIZAÇÃO EXPLÍCITA MIGUEL** antes de aplicar patch — nunca aplicar sob assunção
5. **APLICAÇÃO** só com Miguel de olho ou autorização escrita clara
6. **VALIDAÇÃO PÓS-DEPLOY**: reprocessar 1-3 posts amostra + confirmar comportamento novo + gravar no ledger `[CLAUDE-MIGUEL-DEPLOY-V4-<tema>-<TS>]`
7. **ROLLBACK IMEDIATO** ao primeiro sinal de regressão + notificar Miguel

## O que NÃO exige autorização Miguel

- **Grep read-only** (`grep`, `find`, `ls`, `cat`) para investigação
- **Leitura de logs** (`tail`, `wc -l`)
- **Consulta ao banco WP** (`get_post`, `get_post_meta` sem escrita)
- **Meus recibos `_cafezinho_img_check`** (é minha função no §5, não é patch em código)
- **Escrever memória/ledger/fórum** (documentação nunca precisa autorização)

## O que SEMPRE exige autorização

- Editar `.py` no `/root/v4_labs/`
- Editar `.php` em `wp-content/mu-plugins/` ou `plugins/`
- Alterar cron (`crontab -e`, `systemctl`)
- Deletar/mover código em produção
- Executar scripts de reprocessamento em lote (>3 posts)
- Redeploy/restart de serviço

## Casos borderline (perguntar Miguel)

- Fix de 1 linha claramente inócuo (typo, string constante): perguntar mesmo assim — "produção não se brinca"
- Patch já testado em dev/staging mas nunca em prod: perguntar
- Correção urgente com Miguel offline: escalar Codex primeiro; se Codex também offline, esperar Miguel

## Meta-lição

- Meu histórico como Loop Miguel Vigília: paliativos client-side (regex, patch cirúrgico via `wp_update_post`) eu faço sem autorização porque estão no meu escopo editorial. Mas **mexer no worker V4 é escopo ZCode/infra** — mesmo que eu ache o bug primeiro.
- Regra: "achei o bug" ≠ "aplico o patch". Investigação minha vira **contribuição de leitura** entregue ao ZCode via ledger; aplicação é decisão de fábrica + Miguel.
- Se eu identificar solução clara e ZCode estiver demorando, escalar Miguel (não pisar no worker sozinho).

## Origem histórica

- **16/08/2026 21:52**: Miguel pediu correção do bug worker V4 achata crédito de foto (ver [[feedback-worker-v4-perde-credito-foto-original-20260816]]).
- **16/08/2026 21:53**: Miguel deu ordem de cautela ("produção não se brinca") logo em seguida.
- Meu erro potencial (evitado a tempo): já ia começar a patchear o `featured_image_pipeline.py` sem escrever plano/backup. Miguel me travou preventivamente. Bom timing.

## Relacionados

- [[feedback-worker-v4-perde-credito-foto-original-20260816]] — bug alvo da regra
- [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]] — quando ir estrutural (upstream)
- [[feedback-priorizar-zcode-por-custo-mais-barato-20260815]] — ZCode primeiro em tarefas mecânicas de fábrica
- [[feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814]] — anti-colisão entre daemons

## Regra âncora

**"Produção não se brinca. Antes de qualquer patch no V4: pesquisa read-only → plano escrito com backup + rollback → autorização Miguel explícita → aplicação supervisionada → validação. Achar o bug não é autorização pra patchear."** — Miguel, 16/08/2026 21:53 BRT
