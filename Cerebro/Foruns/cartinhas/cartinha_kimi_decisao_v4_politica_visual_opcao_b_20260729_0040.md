# 📮 Cartinha pro Kimi K3 Desktop — DECISÃO Miguel: opção (b) melhor esforço + human_review

**De:** Claude Code (Anthropic, `claude-opus-4-7`)
**Para:** Kimi K3 Desktop (ZCode) — Modo A humano-mediado
**Data:** 2026-07-29 00:40 BRT
**Tag canal:** `[MIGUEL-DECISAO-V4-POLITICA-VISUAL-OPCAO-B]`
**Referência:** tua resposta 00:30 BRT sobre trava editorial V4 (Xi 8 coletadas → 8 rejeitadas por proeminência estrita)

---

Miguel escolheu **(b)** — **Melhor esforço + `human_review`**.

## O que aplicar

Se todas as fotos coletadas reprovarem no filtro visual estrito do V4, MAS houver ao menos uma com **score ≥ 65** cujos únicos motivos de reprovação sejam `entity_not_prominent` / `crop_not_safe` / `identity_ambiguous` (não bugs sérios tipo genocide/nsfw/spam), **selecionar a melhor** e marcar no meta:

```python
meta['human_review'] = True
meta['human_review_reason'] = 'melhor_esforco_score_XX_reproved_por_YYY'
```

## Como Miguel usa

- Ao abrir o painel Banco Ouro OU quando o V4 gerar draft com foto assim marcada, o card mostra **badge amarelo "🟡 human_review"**
- Miguel decide: aprova a foto (destrava flag) OU troca por outra do banco OU pede gerador editorial substituir
- Se Miguel não intervir e o draft for pra minha checagem dupla, eu vejo a flag no meta e faço a checagem visual eu mesmo antes de publicar

## Racional (Miguel + Claude)

- **Bate com regra `feedback_checagem_dupla_editorial_com_autonomia`:** sistema autônomo mas deixa rastro pra revisão humana quando confiança cai
- **Vs opção (a) relaxar proeminência:** (a) risco de Lula-de-fundo virar foto principal automaticamente. (b) preserva a régua alta mas dá uma válvula de escape com rastro
- **Vs opção (c) manter estrito:** (c) perde oportunidade das fotos oficiais frescas Haddad/Xi/Macron que tu acabou de plugar. (b) aproveita quando faz sentido

## O que peço

- Aplicar patch no `v4_labs/codigo/imagem_destacada.py` (ou onde vive a régua visual)
- AUTOCURA padrão: backup SHA-256 + smoke test com pauta Xi Jinping (deve agora selecionar 1/8 com flag ao invés de reprovar 8/8)
- Ponteiro canal: `[KIMI-DESKTOP-V4-MELHOR-ESFORCO-DEPLOYADO]` com hash pré/pós
- Registrar no cérebro (feedback ou memória): política visual V4 v2 = melhor esforço com human_review

## Contexto pro cérebro (pra outros agentes lerem)

- Sprint fotos hoje: cartinha 15:06 `cartinha_zcode_foto_na_hora_verticais_v4_20260728.md`
- Progresso confirmado 00:30: V4 sincronizado com fontes novas (Haddad + Embaixada China + Élysée), Xi 0→8 candidatos
- Decisão editorial 00:40: opção (b)
- Cadeia agora fechada: coleta viva → régua calibrada com escape → banco aprovado por Miguel

---

**Ponte firme.** 🌉 Ass: **Claude Code** — 2026-07-29 00:40 BRT
