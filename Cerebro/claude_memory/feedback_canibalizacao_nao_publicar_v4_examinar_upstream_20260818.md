---
name: feedback-canibalizacao-nao-publicar-v4-examinar-upstream-20260818
description: "Miguel 18/08 12:51+12:53+12:55+12:56 BRT — canibalização proibida. Post humano tem preferência (V4 recua sempre). V4 vs V4 = bug do worker, corrigir upstream em 2 lugares (coleta + bancos de conteúdo). Fórum aberto + pedido formal ZCode Miguel resolver com cuidado E audácia. Emenda 5 ao Contrato."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 870114c6-7ee3-4080-8592-299996b3140e
---

## Regra Master

Canibalização editorial (dois posts com ângulo idêntico ou muito próximo) é PROIBIDA. Regras hierárquicas:

### 1. Post humano vs Post V4 → V4 RECUA sempre

Se detectar pending V4 (autor 5786) canibalizando post publicado por autor humano (não-5786, ex.: 5470 Redação, 2018 Miguel, etc.) nas últimas 24-48h da mesma categoria/tema:
- **Descartar o V4 imediato** (`wp post update --post_status=draft` ou lixeira).
- Sem discussão, sem reaproveitamento.
- Log JSONL: `acao=descarte_canibalizacao_humano_preferencia`.

Miguel textual 12:56 BRT: **"Posts humanos tem preferencia. Ai nao tem jeito. O post v4 recua."**

### 2. Post V4 vs Post V4 → BUG do worker, escalação upstream

Se detectar dois pending V4 (ou pending V4 + publicado V4) com ângulo idêntico:
- **Descartar** o mais recente (mesmo tratamento, `--post_status=draft`).
- **Escalar como bug do worker V4** — o próprio V4 está produzindo variações redundantes do mesmo tema. É defeito de fonte/coleta OU do banco de conteúdo semântico.
- Log JSONL: `acao=descarte_canibalizacao_v4_vs_v4_BUG_UPSTREAM`.
- Alimentar estudo dedup do ZCode Miguel.

Miguel textual 12:56 BRT: **"Mas se a gente está tendo posts repetidos do próprio v4 aí é um problema"**.

## Problema upstream — pedido de estudo ao ZCode Miguel

Miguel 12:55 BRT (autorização + orientação técnica dupla):

> "Faça o fórum sozinho, contate o zcode, e peça para ele resolver isso com muito cuidado, mas também com audacia. Isso pode ser corrigido nos v4 em dois lugares, na coleta e nos bancos de conteúdo."

Dois pontos de correção técnica no V4:

### (a) COLETA — antes do worker gerar

Pipeline de fontes/scraping do V4. Dedup entre fatos brutos coletados:
- Se dois fatos coletados apontam pro mesmo evento (ex.: "Sea Legend inaugura rota Ártico 15/08" e "Rota do Ártico substitui Suez"), deduplicar antes de virar dois posts.
- Threshold: similaridade semântica entre lides ≥ X% (definir com estudo).
- Comparação em janela de 24-48h.

### (b) BANCO DE CONTEÚDO — antes do worker aprovar/finalizar

Repositório dos posts já gerados (V4 mantém). Dedup semântico ao aprovar/finalizar:
- Antes de mover post V4 de rascunho pra pending, comparar título+lide com posts já publicados nas últimas 24-48h da mesma categoria.
- Se similaridade > threshold, marcar como duplicata e não finalizar (fica em rascunho ou é descartado).
- Alternativa: marcar como "atualização candidata" pra futuro update in-place de post original — mas isso é DECISÃO EDITORIAL, não automática.

### Diretriz para o ZCode

> "muito cuidado, mas também com audácia" — Miguel.

- **Cuidado**: mudança em worker V4 é produção — pesquisa read-only, plano escrito, backup, rollback ANTES de patchear (regra §125 pré-existente).
- **Audácia**: pode fazer alteração estrutural (nova etapa no pipeline, novo campo de metadata, novo índice de similaridade) se justificar. Não é só remendo pontual.

## Emenda 5 ao Contrato

Miguel: "vamos colocar isso no contrato". Formalização pendente. Proposta: **Emenda 5 ao Contrato Ponte Completa** — "Canibalização editorial é proibida. Post humano prevalece sobre V4. V4 deve dedup upstream (coleta + banco de conteúdo). Vigília jusante descarta canibais sem reaproveitar."

## Meu papel no Vigília jusante

1. Ao processar pending Slot A/B, comparar título+lide com últimos posts publicados nas últimas 24-48h da mesma categoria/tema.
2. Se autor do publicado = **humano**: descartar V4 canibal automaticamente (regra 1).
3. Se autor do publicado = **V4**: descartar canibal + registrar como bug upstream (regra 2), alimenta estudo ZCode.
4. Sinalizar Trindade Laura pela ponte pra dados alimentarem estudo dedup V4.
5. **Meta**: zero canibalização detectada no Vigília após implementação (30 dias).

## Exemplos históricos hoje

- **266388** (V4) vs **266364** (V4 publicado 07:45) — Trump/Omã: descarta 266388 (V4 vs V4 bug).
- **266398** (V4) vs **266330** (V4 publicado 03:15) — Prazo Irã: descarta 266398.
- **266440** (V4) vs pilha Trump/Irã: descarta ou consolida.
- **266461** (V4 pending 12:33) vs **266327** (V4 publicado ontem 20:00) — China Ártico: **descarta 266461**. Ambos V4 → bug upstream, entra no estudo.

## Fórum aberto

`Cerebro/Foruns/forum_dedup_v4_upstream_canibalizacao_20260818.md` — meu convite ao ZCode Miguel + registro dos casos históricos + espaço pra desenho técnico dele.

## Ligação com outras regras

- Complementa [[feedback-regra-eventos-etapas-v4-20260817]]: eventos em etapas aceitam publicação separada; canibalização não.
- Sobrescreve minha proposta anterior de "HOLD com sugestão de aproveitamento in-place" — Miguel corrigiu 12:53 BRT.
- Alertas Laura §126 continuam precedendo minha decisão de descarte se sinalizar primeiro.
