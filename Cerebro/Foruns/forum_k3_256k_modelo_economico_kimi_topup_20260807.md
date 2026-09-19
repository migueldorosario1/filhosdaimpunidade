# Fórum — Modelo k3-256k como econômico do Kimi + top-up bridge de cota

**Data:** 2026-08-07 ~18:15 BRT
**Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan) — workspace ZCodeProject, chat direto
**Tema:** Gestão de crédito LLM / política de roteamento de modelo
**Status:** ✅ ENTREGUE — modelo `k3-256k` configurado no ZCode, testado ao vivo (HTTP 200), crédito extra do Miguel aplicado.

---

## Contexto (o que aconteceu)

1. **Kimi K3 (assinatura) esgotou** a cota semanal rápido demais. Assinatura vigente até 23/08, mas a **cota semanal** acabou.
2. Miguel precisa **aguentar ~5 dias** até a renovação semanal. Assinaturas novas estão em **fila de espera** (fechadas por enquanto).
3. Miguel consultou a doc do Kimi Code (colada no chat) e viu o modelo `k3-256k`.
4. Decisão do Miguel: **comprar crédito extra (top-up pay-as-you-go) e usar só o `k3-256k`** — mesma qualidade, metade do consumo.

## Decisão (Miguel + agente)

- **`k3-256k` é a escolha correta para trabalho de código/gestão do ecossistema.** A doc do Kimi é explícita: *"Within 256k context, it delivers the same results"* — é o mesmo K3, mesma inteligência, só com janela de contexto menor (256k vs 1M).
- **Consome ~metade da quota** do `k3` (1M) por chamada → dobra o tempo útil do mesmo crédito.
- Para o padrão de uso do Miguel (gerenciar Cérebro, agentes, projetos, editar código), 256k chega sobrando. O 1M só vale para ingerir codebases inteiras de uma vez (raro).
- **Crédito extra (top-up) + `k3-256k` = uso mais eficiente do dinheiro.** Miguel já colocou o crédito.

## O que foi feito (entrega)

### Configuração no ZCode (`~/.zcode/v2/config.json`)
- **Backup criado:** `config.json.bak_pre_k3-256k_20260807_1812` (arquivo original preservado — Regra "nenhum arquivo se perde").
- **Modelo `k3-256k` adicionado** ao provedor "Kimi 3" (`abc953f0-…`), logo após o `kimi-k3` (1M, que permanece):
  - `context: 262144` (256k), `output: 131072`
  - reasoning low/high/max, default `high`
  - modalidades: text in/out (sem vídeo — irrelevante para código)
- **JSON validado** (sintaxe correta, não quebrou o config).
- **Modelo `kimi-k3` (1M) NÃO foi removido** — continua disponível para quando o Miguel quiser voltar.

### Teste ao vivo
- `curl POST https://api.kimi.com/coding/v1/chat/completions` com `model: k3-256k` → **HTTP 200, resposta recebida**. Crédito extra do Miguel está funcionando.

## Como usar (passo a passo para o Miguel)

1. **Reiniciar o ZCode** (fechar o programa inteiro e abrir de novo — não só nova aba) para recarregar o `config.json`. Nova aba pode funcionar, mas o programa pode manter a config em cache no processo principal — reiniciar o programa é garantido.
2. No seletor de modelo: **Kimi 3 → `k3-256k`**.
3. Se vinha usando contexto >256k numa sessão, fazer `/compact` antes de trocar (preserva pontos-chave da tarefa).

### ⚠️ Reiniciar no CLI vs Desktop (ordem Miguel 07/08 ~18:16)
- **CLI:** reiniciar o processo pode encerrar a sessão atual. **Antes de fechar**, o estado já está no Cérebro (este fórum + memória). Se a sessão se perder, abrir conversa nova e dizer *"continuar a configuração do k3-256k"* — qualquer agente lê o fórum e retoma.
- **Desktop (Electron):** conversas ficam salvas; ao reabrir, a conversa está no ponto exato.
- **Recomendação:** o seguro é reiniciar o programa inteiro. Nova aba não é garantido.

## Como reverter (voltar ao kimi-k3 1M)

- **Rápido (seletor):** trocar no seletor de volta para `kimi-k3` (1M). Ele continua lá.
- **Remover totalmente o `k3-256k`:**
  ```bash
  cp ~/.zcode/v2/config.json.bak_pre_k3-256k_20260807_1812 ~/.zcode/v2/config.json
  ```

## Política de roteamento (ficar valendo)

> **Para trabalho de código / gestão do ecossistema: preferir `k3-256k` sobre `k3` (1M).**
> Mesma qualidade, metade do consumo de quota. Reservar `k3` (1M) apenas para ingerir codebases inteiras em uma única chamada (caso raro).
> Quando a assinatura semanal renovar, o `k3-256k` segue sendo o default econômico; o `k3` 1M fica para quando 256k não bastar.

## ⚠️ Cuidados da doc do Kimi (registrados para consulta)

- **Trocar de modelo invalida o cache de contexto** — recomenda iniciar sessão nova (ou `/compact`) pra não desperdiçar tokens.
- **K3/K2.7 com Thinking OFF cai pra K2.6** — manter thinking ligado para usar de fato o K3.
- **`kimi-for-coding-highspeed`** = ~6× mais rápido, 3× consumo de quota. Bom para tarefas curtas/repetitivas, péssimo para economia de crédito.
- IDs de modelo para o seletor/API: `k3`, `k3-256k`, `kimi-for-coding`, `kimi-for-coding-highspeed` (NÃO usar nomes como "Kimi K3" — dá erro).

## Estado da missão

- **O que aconteceu:** `k3-256k` configurado, testado, crédito extra funcionando. Política de roteamento definida.
- **O que falta:** Nada do lado do agente. Miguel precisa reiniciar o ZCode e selecionar `k3-256k` no seletor.
- **O que preciso de você (Miguel):** reiniciar o ZCode, escolher `k3-256k` no seletor e testar uma tarefa real. Se a qualidade atender, segue no 256k; se não, volta no 1M (um clique no seletor).

## Refs

- Doc do Kimi Code (Model Configuration) — colada na conversa.
- Backup: `~/.zcode/v2/config.json.bak_pre_k3-256k_20260807_1812`.
- Nodo: `CEREBRO_NODE_CHAVES_E_LLMS.md` (política de roteamento) + `CEREBRO_NODE_ATUALIZACOES.md` (linha do tempo).
- Memória irmã: `Memorias/memoria_k3_256k_modelo_economico_kimi_topup_20260807.md`.
