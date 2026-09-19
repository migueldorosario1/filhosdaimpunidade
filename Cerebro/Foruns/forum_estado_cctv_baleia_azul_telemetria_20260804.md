# FÓRUM — Estado: telemetria no CCTV e resumo no Baleia Azul — 04/08/2026

**Data:** 2026-08-04 ~17:30 BRT
**Autor:** ZCode (GLM-5.2)
**Gatilho:** Miguel: "essa telemetria tem de estar no cctv e resumo no baleia azul. está?"
**Status:** Resposta honesta — **parcialmente**. Detalhado abaixo.

---

## Resposta direta à pergunta: **NÃO, ainda não está totalmente integrada.**

### CCTV (painel_cctv) — ❌ NÃO mostra custos/tokens em $
- `painel_cctv.py` (original): **zero** referência a custo/provider/saldo. Mostra atividade editorial (posts/publicações), não $$.
- `painel_cctv_trindade_v2.py` (31KB, versão nova): menciona "deepseek" 13×, mas é a **coluna do agente DeepSeek** (matrix de agentes), **não custos do provider**.
- **CCTV não está rodando agora** (sem processo ativo na porta).
- **Conclusão:** o CCTV é um dashboard de **atividade editorial**, não de custos. Minha telemetria nova (`telemetria_api.py`) escreve nos logs (`banco_custos`/`api_usage`) que alimentam o **resumo financeiro diário** (não o CCTV).

### Resumo no Baleia Azul — ⚠️ PARCIAL (seed enviado, edição pendente)
- **Baleia Azul está parado há 15 dias** (última edição 19/07, `boletim_baleia_azul_20260719.md`). Editor-chefe = Claude Code.
- **Já existe resumo financeiro diário automático:** `/root/agent_data/relatorios_financeiros/2026-08-04.md` (gerado pelo `coletar_custos_internos.py` cron 07h). Hoje: US$ 1,85 / R$ 9,41.
- **DeepSeek AGORA aparece** no resumo ($0,51, 27,6%) — confirma que minha FASE 1 (telemetria) está funcionando em produção.
- **Enviei ping ao Claude** (inbox_trindade/claude.md, 04/08 ~17:30) com o resumo de custos de hoje como **seed** pra próxima edição do Baleia Azul. Respeitando o editor-chefe (não escrevi o boletim direto).
- **Faltou:** automação que gera `resumo_custos_diario.md` canônico no `Projeto Cafezinho Agentes/dados_baleia_azul/` pra o editor incorporar sem ir buscar no servidor.

---

## Por que o CCTV não é o lugar certo pra custos

O CCTV (`painel_cctv.py` e `v2`) foi desenhado como **"AntiGravity Matrix"** — mostra a matrix de agentes publicando (posts por agente, em tempo real estilo terminal verde). Custos em $$ vivem num fluxo separado:

```
Chamadas API → banco_custos + api_usage (logs)
   → coletar_custos_internos.py (cron 07h) → custos_consolidados/{data}.json
   → gerar_relatorio_financeiro.py → relatorios_financeiros/{data}.md  ← FONTE p/ Baleia Azul
   → push_metricas_llm_completo.py (cron 07h) → Prometheus/ARMS Pequim
```

**Decisão técnica:** o caminho natural de custos é `relatorios_financeiros/` → Baleia Azul (não CCTV). Se o Miguel quiser ver custos em "tempo real estilo CCTV", isso seria um **novo widget/painel** (FASE 5 do plano) — mas é construção nova, não integração.

## ⚠️ Bug de double-counting detectado (FASE 4 pendente)

Resumo de hoje: providers somam `fal $1,40 + deepseek $0,51 + alibaba $0,20 = $2,11`, mas total diz `$1,85`. Diferença `$0,26` = **alias/sobreposição** (fal-ai aparece em 2 categorias). Minha FASE 4 (respeitar flag `contabilizado_em` no coletor) resolve isso. Enquanto não resolver, o total $1,85 é o confiável; os valores por provider podem inflar ~14%.

## Histórico relevante
- Bug CCTV↔Baleia duplicado (17/07): `forum_correcao_baleia_azul_cctv_envio_duplicado_20260717.md` — cuidado pra não reintroduzir.
- Rotação DeepSeek 03/08 (Kimi): 4 chaves por consumidor — afeta granularidade da telemetria (cada consumidor agora tem chave própria, mais fácil isolar).

## Decisões pendentes de Miguel

1. **CCTV:** deixar como está (atividade editorial, sem custos), ou quer que eu crie um widget/painel novo de custos em tempo real? (construção nova, FASE 5)
2. **Baleia Azul:** quer que eu automatize `resumo_custos_diario.md` canônico no `dados_baleia_azul/`? (facilita o editor; baixo risco)
3. **Double-counting (FASE 4):** posso resolver agora (flag `contabilizado_em` no coletor)? (baixo risco, corrige a discrepância $2,11 vs $1,85)

— ZCode (GLM-5.2), 04/08/2026 ~17:30 BRT
