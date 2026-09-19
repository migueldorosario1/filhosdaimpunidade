---
name: project-v4-destravado-ponte-imagens-20260813
description: "Sprint ZCode 13/08/2026 destravou V4 — draft nasce pending mesmo sem imagem, ponte de imagens */30 aplica foto real depois, regional ligado com 27 UFs, publish 100% do Claude"
metadata: 
  node_type: memory
  type: project
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## O que mudou 13/08/2026 ~14:00 BRT (sprint ZCode: Codex→ZCode handoff)

Cartinha em `Cerebro/Foruns/inbox_trindade/claude.md` tag `[ZCODE-SPRINT-V4-DESTRAVADO-PONTE-IMAGENS-20260813-1400-BRT]`. Docs completos: `Foruns/forum_auditoria_v4_todas_verticais_fase01_20260813.md` + `forum_auditoria_v4_matriz_plano_fase23_20260813.md` + `Memorias/memoria_auditoria_v4_todas_verticais_20260813.md`.

### Bug original diagnosticado

Um post sem imagem congelava a vertical inteira. Falha no reparo → `return 4` → vertical parava de selecionar pauta nova. Cultura tinha deadlock permanente (política "sem IA" absoluta bloqueava toda tentativa).

### Peças da solução em produção

| Peça | Comportamento novo |
|---|---|
| **Fila de imagem não bloqueante** | Falha de reparo NÃO trava mais. Só pausa a vertical se ≥3 posts sem imagem em aberto (válvula anti-fila da lição 27/07). |
| **`draft_sem_imagem`** | Se imagem falhar, rascunho nasce `pending` sem featured_media. Matéria não se perde. Post entra na fila da ponte, vertical segue produzindo. |
| **`reconcile_wp_created`** | Candidatas em `wp_created`/`wp_created_failed` reconciliam com WP real todo ciclo: post+imagem → confirmado / sem imagem → fila da ponte / 404 → reprocessa / falha transitória → retry 6h. |
| **Regional ligado top-27** | Motor escolhia SP toda hora, Centro-Oeste nem entrava no top-10. Agora: top-27 + prioridade UFs que nunca produziram + rotação 6h. NE/CO começam a produzir. |
| **Ponte de imagens `*/30`** | Cron novo. Caça imagens reais licenciadas (Wikimedia Commons CC/PD + Flickr CC/PD) pros `image_pending`. Aplica via wp-cli. **Nunca muda status de post.** Máx 3/rodada. Log em `Cerebro/Foruns/ponte_imagens_v4_LOG.md`. |
| **Bloco Regional na home** | Entre Esporte e Linha do Tempo. Consulta as 5 regiões. Menu reestruturado Regional▸Região▸Estado (27 estados, hover desktop, árvore hambúrguer). |

## O que NÃO mudou (e não vai)

**Nenhum V4 publica automaticamente.** Redator só cria draft; worker só move pra `pending`; nenhum caminho automático chega a `publish`. A decisão de subir matéria continua **100% minha**, com revisão editorial própria. Reafirmado por Miguel neste sprint.

## O que muda no meu fluxo Vigília Trindade V6

### 1. Ampliar filtro de fila: `draft` OR `pending`

Antes filtrava só `post_status=draft`. Agora novos rascunhos V4 nascem `pending`. Preciso incluir ambos em cada slot:

```php
$posts = get_posts([
  "category" => $cat,
  "post_status" => ["draft", "pending"],
  ...
]);
```

### 2. `pending` sem featured_media = NORMAL — deixa quieto

Antes tratava draft sem fm como bug. Agora:
- **Pending COM fm** → revisar + agendar/publicar
- **Pending SEM fm** → NÃO tocar. Ponte `*/30` está trabalhando. Se demorar >24h, escalar ZCode.

### 3. Regra cat 20699 (No home) ajustada

```php
if ($fm > 0 && in_array(20699, $cats)) {
  // remove 20699 — post pronto pra home
} else if ($fm === 0) {
  // MANTÉM 20699 — aguarda ponte trazer imagem
}
```

### 4. Após publish → banco reconcilia sozinho

`external_resolved` no `draft_events` do banco SQLite da vertical. Não preciso avisar ninguém.

### 5. Regional Slot A expandido

Regionais (cats 21058/21068/21055/21073/21064 = NE/N/SE/S/CO) começam a produzir de verdade. Meu Slot A já cobre essas cats. Manter.

### 6. Nova vertical Meio Ambiente ativa

Primeiro draft_confirmed da história: **265552** (Gafanhoto vira isca no São Francisco, agendado 16:20 BRT 13/08 por mim). Cat 582. Volume esperado: contínuo daqui pra frente.

## Estado do sprint (13/08 14:00 BRT)

- ✅ Fases 0–4 completas
- ✅ Regional no ar + menu Regional▸região▸estado + manchete sem excerpt
- ✅ Ponte de imagens `*/30` rodando (2 rodadas até 14:00; fila vazia porque os 2 eventos eram de posts já publicados pela manhã)
- 🔄 Fase 5 (homologação) começa sozinha nas próximas horas — cada vertical precisa 3 ciclos completos sem intervenção. ZCode acompanha logs.
- ⏳ Visual só de Miguel: hard refresh na home pra ver bloco Regional

## Referências

- Carta ZCode inbox tag `[ZCODE-SPRINT-V4-DESTRAVADO-PONTE-IMAGENS-20260813-1400-BRT]`
- `Cerebro/Foruns/ponte_imagens_v4_LOG.md` — log linha a linha da ponte
- `draft_events` por vertical em `/root/agent_data/v4_verticals/` no NYC
- 265552: primeiro draft_confirmed meio ambiente da história

Regras irmãs: [[project-v4-5-verticais-canonico-migradas-20260812]] · [[feedback-no-home-remover-se-tem-imagem-real]] · [[feedback-wp-update-post-edit-date-obrigatorio-para-agendamento]] · [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]].
