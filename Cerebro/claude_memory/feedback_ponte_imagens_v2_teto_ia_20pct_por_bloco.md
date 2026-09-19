---
name: feedback-ponte-imagens-v2-teto-ia-20pct-por-bloco
description: "Ponte Claude-Kimi de imagens v3 (Miguel 06/08/2026 15:25 BRT direto chat) — Ciência sem cota (IA à vontade); Geopolítica cota 30% por bloco 4h; nacional/regional/temáticos = zero IA; hierarquia foto real jornalística > arquivo > retrato oficial > IA; fluxo falta imagem via tag [PONTE-CLAUDE-KIMI-IMAGEM] no canal."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cf4e142a-050c-46de-b793-bee2464fc7f7
---

## ⚠️ Mudança v2 → v3 (06/08 15:25 BRT — Miguel direto no chat)

Miguel refinou a Ponte de Imagens v2 (que era 20% Geo+Ciência ambas):
- **Ciência: IA à vontade** — sem cota. Se não achar no banco de mídia, usa IA sem restrição. "Vamos procurar uma solução para isso depois com mais calma."
- **Geopolítica: cota 30%/bloco 4h** (era 20% na v2). No máximo 30% dos publish Geo do bloco podem ter hero IA.
- Restante (nacional/regional/temáticos/YT/opinião) — segue **zero IA** como na v2.
- Hierarquia foto real → arquivo → retrato oficial → IA segue igual.
- Fluxo falta imagem (tag `[PONTE-CLAUDE-KIMI-IMAGEM]` + fila Kimi 30/30) segue igual.
- Linha vermelha "post nunca sobe com imagem errada" segue igual.
- Kimi K3 avisado no canal_trindade.md 06/08 15:30 BRT (Miguel pediu: "avise ao kimi que eu mudei a orientação").

**Motivação da mudança:** matéria de Ciência tem maior escassez natural de foto real jornalística contextual (temas abstratos, papers, instituições sem foto pública). Impedir IA em Ciência bloqueava vertical inteiro — não vale a pena o custo editorial. Já Geo tem foto real de agência quase sempre disponível (guerra, política internacional, líderes), então cota 30% (mais generosa que os 20% originais mas mantendo teto) equilibra.

---

**🖼️ Regra permanente de imagens editoriais V4 — v2 (ordem Miguel 06/08/2026 ~14:30 BRT via Kimi K3 no canal) — texto original v2 preservado abaixo pra referência histórica.**

## As 5 partes

1. **Teto de IA: 20% por bloco de 4 horas.** Dia dividido em 6 blocos BRT (00-04, 04-08, 08-12, 12-16, 16-20, 20-24). Em cada bloco, **no máximo 1 em cada 5 posts** com imagem gerada por IA. Se o bloco tiver 3 publish, IA só se ainda não teve nenhuma; se tiver 5 publish, IA só uma vez; se tiver 10, IA no máximo 2. Contagem por bloco, não acumula pro seguinte.

2. **IA só em Geopolítica e Ciência.** Nacional, regional, temáticos, YT-Cafezinho, opinião — todos = foto real ou rascunho, **zero IA**. Se draft nacional/regional chegar com imagem IA, tratar como falta de imagem (voltar pro fluxo §4).

3. **Preferência de imagem (hierarquia irrestrita):**
   - **Foto real jornalística** (agência, evento coberto — 1ª escolha)
   - **Foto real de arquivo** (mesmo evento/pessoa/local, data anterior — 2ª)
   - **Retrato oficial** (governo, empresa, entidade — 3ª, última analógica)
   - **IA** (só Geo/Ciência, dentro da cota do bloco — 4ª e última)

4. **Fluxo quando falta imagem:**
   - (a) Claude tenta primeiro com seus instrumentos (Banco Ouro, cache local, WebSearch de imagens quando aplicável, `hero_tentativas` do worker se disponível).
   - (b) Se não resolver → **manter rascunho** (não publish) + o post entra automático na fila do Kimi (faltas NYC + hero_tentativas). NUNCA publish com imagem errada.
   - (c) Priorizar caso urgente via tag `[PONTE-CLAUDE-KIMI-IMAGEM]` no `canal_trindade.md` (formato: PID + título + vertical + motivo da falta).
   - (d) Kimi (loop 30/30 min) faz busca ativa, ingere no Banco Ouro, e o pipeline Claude publica na rodada seguinte quando a imagem aparecer.
   - (e) Travou dos dois lados → Miguel recebe Telegram + e-mail (via Kimi) com o título; Kimi segue caçando.
   - **Post nunca sobe com imagem errada.** Esta é a linha vermelha.

5. **FYI Agente Ciência:** ativo hoje 06/08 com 5 posts, mas tudo sai `no_home=true`. Regra aberta pra revisitar com Miguel — se Geo/Ciência merecem vitrine home ou seguem no-home padrão. **Não decidir sozinho**; se Miguel pedir avaliação, escalar com contexto (peso editorial do post + tráfego histórico da editoria + concorrência no bloco).

## Como aplicar no meu loop Vigília DIA/NOITE

- **Cheque vertical do draft antes de publish:** se Nacional/Regional/YT-Cafezinho/temático com imagem gerada por IA → tratar como falta de imagem (mesmo se o worker já anexou hero IA).
- **Cheque cota de IA no bloco:** antes de publish Geo/Ciência que use hero IA, calcular quantos publish já saíram no bloco atual (BRT) e quantos com IA — se cota estourada, voltar pro fluxo §4.
- **Registro no log JSONL** (bugs_YYYY-MM-DD.jsonl): adicionar campo `imagem_tipo` (`foto_real_jornalistica` | `foto_real_arquivo` | `retrato_oficial` | `ia` | `sem_imagem_pending`) + `imagem_bloco_4h` (rótulo do bloco) + `imagem_cota_bloco_status` (dentro/estourada).
- **Ao mandar pro Kimi via tag `[PONTE-CLAUDE-KIMI-IMAGEM]`:** formato canônico `[PONTE-CLAUDE-KIMI-IMAGEM] PID X — vertical — título — motivo (sem hero / hero IA em vertical proibido / hero IA em bloco lotado)`.

## Por quê

**Why:** matérias com foto IA sofrem redução de credibilidade e engajamento; leitor do Cafezinho valoriza foto real jornalística; IA foi virando muleta em nacional/regional onde não cabe editorialmente. Cota de 20%/bloco impede saturação visual de IA num período curto (o pior é 4-5 IA seguidas na home). Ponte com Kimi (loop 30/30) permite escalar sem barrar publicação eternamente — post pode esperar 30-60min por imagem real, mas não publica errado.

**How to apply:** aplicar em CADA publish do Vigília V5 DIA (07-22:17/47) e NOITE (23-06:17). Sem exceção. Se dúvida, prefere segurar rascunho e escalar ao Kimi (barato) do que publish com imagem inadequada (custoso reverter na home).

## Casos-teste (a validar nos próximos ciclos)

- (a) Draft Geo com hero IA em bloco 12-16 BRT já com 2 IA nesse bloco (2/10 = 20% — cota estourada se próximo) → hold pro bloco seguinte OU trocar por foto real.
- (b) Draft Regional MG com hero IA → tratar como falta de imagem (regional = zero IA), pending + tag Kimi.
- (c) Draft Ciência com hero IA em bloco 16-20 com apenas 1 publish anterior sem IA → publish OK (dentro cota).

## Refs

- Regra irmã de [[feedback-loop-vigilia-opus-v5]] (protocolo publish V5).
- Regra irmã de [[feedback-gravacao-datada-por-ciclo-e-ponte-kimi-regular]] (ping consolidado 1×/h no canal).
- Substitui qualquer regra anterior sobre imagens IA sem cota/vertical restrita.
- Cartinha fundadora: mensagem Kimi no canal_trindade.md 06/08/2026 ~14:30 BRT (a arquivar como cartinha canônica se pedido).
