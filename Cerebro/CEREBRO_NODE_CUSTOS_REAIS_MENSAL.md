# 💰 CEREBRO_NODE — CUSTOS REAIS MENSAL DO ECOSSISTEMA (DESTAQUE CHAIRMAN)

> **Criado:** 2026-07-29 12:20 BRT por ZCode (Kimi), ordem do Miguel: "guardar no cérebro com destaque no índex; cálculos realistas de quanto a gente está gastando".
> **Método:** telemetria real (`banco_custos` NYC) + specs reais dos servidores (lidas via SSH/metadata) + valores documentados no Cérebro + tabelas públicas de preço. Cada linha tem **nível de confiança**:
> ✅ CONFIRMADO (telemetria/documento) · 🟡 ESTIMATIVA FORTE (spec real + preço público de tabela) · 🔴 PENDENTE EXTRATO (sem registro; range honesto — Miguel vai confirmar com fatura).
> **Atualização:** revisar a cada mudança de plano/servidor e quando o extrato do cartão preencher os 🔴.

---

## A. LLMs / APIs variáveis (por mês, no ritmo pós-cortes de 19/07)

| Item | US$/mês | Confiança | Base |
|---|---|---|---|
| Produção NYC (todos os agentes V4, comentarista, imagens, SEO) | **~53–59** | ✅ | Média 7d US$ 1,77/dia × 30 (consolidados 22–28/07); projeção do Baleia 29/07: US$ 53,01 |
| Agentes LOCAIS temáticos (8 sites: ~68 artigos/dia deepseek-kimi + ~48 julgamentos visuais qwen-vl/gemini) | **8–12** | 🟡 | Volume medido por log (174 ciclos desde 21/07); SEM telemetria de custo — `nucleo_llm.py` descarta `usage` (fix pendente) |
| Cafezinho YouTube local (curador kimi-k3 + redação superluxo ocasional) | **2–4** | 🟡 | ~3 rodadas/dia; kimi-k3 $3/$15 por 1M; redação gpt-5.5 só quando publica |
| Transkriptor (transcrição, assinatura em minutos) | **~30** | ✅ | Documentado no plano Moka / regras vivas |
| Brave Search API (pós-upgrade 26/07) | **~5** | ✅ | Fórum 26/07 |
| Fal.ai/Ideogram extra fora da telemetria | 0 | ✅ | Já contado no item NYC (banco_custos) |
| **Subtotal A** | **~98–110** | | ≈ **R$ 500–560** |

## B. Assinaturas de IA (fixas mensais)

| Item | US$/mês | Confiança | Base |
|---|---|---|---|
| **GLM Coding Plan Max** | **144** | ✅ | `CEREBRO_NODE_CHAVES_E_LLMS.md`; renova **17/ago/2026** — revisar uso (622M tokens GLM-5.2) antes |
| Kimi "Allegretto" (plano atual do Miguel) | **31 anual / 39 mensal** | ✅ | Tabela oficial do painel Moonshot (colada pelo Miguel 25/08/2026): Moderato $15/$19 (1×) · **Allegretto $31/$39 (2×)** · Allegro $79/$99 (5×) · Vivace $159/$199 (10×) — formato anual/mensal. "Kimi Code" disponível já no Moderato; créditos escalam lineares com o preço (sem prêmio de escala); features superiores (Cluster, Goal, Claw) são do produto Moonshot, não do ZCode |
| Claude/Anthropic "Max" | **100–200** | 🔴 | Planos Max públicos: US$ 100 (5×) / US$ 200 (20×); qual dos dois? |
| Google AI Ultra / Drive 30 TB | **0–250** | 🔴 | Se ativo, é o **maior custo fixo do ecossistema** — confirmar urgente com extrato |
| Vercel Pro | **20** | ✅ | Plano Moka |
| Backblaze B2 | **~0,05–1** | ✅ | `CEREBRO_NODE_BACKUPS_BACKBLAZE.md` |
| Apple Developer | 8,25 (99/ano) | 🔴 | Só se/ quando app Moka iOS for publicado |
| **Subtotal B** | **294–523** | | |

## C. Servidores (mensal)

| Máquina | Spec real (lida 29/07) | US$/mês | Confiança |
|---|---|---|---|
| DigitalOcean NYC `Cafezinho-failover-vigia` (produção) | 1 vCPU / 1 GB | **6** | 🟡 (spec via metadata SSH; tabela DO Basic) |
| DigitalOcean `159.89.185.209` (Rio Carta Astro) | sem acesso | **6–12** | 🔴 |
| DigitalOcean `174.138.36.31` (Rio Carta WP) | sem acesso | **6–12** | 🔴 |
| DigitalOcean `159.65.177.60` (lab cafezinho.news) | sem acesso | **6–12** | 🔴 |
| Tencent Singapura (painéis V5/V6, espelho) | 2 vCPU / 8 GB / 118 GB | **15–25** | 🟡 (spec via SSH; faixa Lighthouse/CVM 2C8G) |
| Alibaba Beijing | **LEGACY 29/07** | **0** após desligar | 🔴 verificar se cobrança parou (se não: +10–20 que devem virar 0) |
| ServerDo.in (WordPress Cafezinho) | — | **10–30** | 🔴 (R$ 50–150) |
| **Subtotal C** | | **43–90** | |

## 🎯 TOTAL REALISTA MENSAL (A + B + C)

| Cenário | US$/mês | R$/mês (@5,10) | Premissas |
|---|---|---|---|
| **Mínimo provável** | **~435** | **~R$ 2.220** | Kimi $30, Claude $100, sem Google Ultra, servidores no piso |
| **Central (mais provável)** | **~520–560** | **~R$ 2.650–2.850** | Kimi ~$60, Claude $100–150, Tencent ~$20 |
| **Alto** | **~770–720** | **~R$ 3.700–3.900** | Com Google AI Ultra $250 e/ou Claude $200 |
| ⚠️ Pico histórico (julho c/ runaway) | ~900–1.100 | ~R$ 4.600–5.600 | APIs $443 + fixos — CENÁRIO JÁ EXTINTO (cortes 19/07) |

**Leitura honesta:** hoje o ecossistema custa **provavelmente R$ 2.200–2.850/mês**, dos quais só ~R$ 500 são APIs variáveis (sob controle pós-19/07). **O peso está nos fixos** — e os 3 maiores (Kimi Max, Claude Max, Google Ultra) estão sem valor documentado: são os 🔴 que o extrato do Miguel precisa preencher.

## 🔧 Qualidade das fontes (o que mente e o que fala verdade)

| Fonte | Estado | Nota |
|---|---|---|
| `banco_custos` → consolidados NYC | ✅ verdade | Base de todos os números ✅ deste nodo |
| Painel `/v6/custos` | ✅ verdade | Lê os consolidados; online |
| **Fiscal Augusto** (`augusto_fiscal_tokens.py`, NYC 8h) | ✅ verdade (desde 01/08) | **FIX APLICADO 01/08 (ZCode):** 7d/30d agora somam os consolidados diários (backup `...bak_pre_fix_7d30d_20260730`). Tabela interna de preços segue limitada (5 modelos) mas não afeta o relatório, que lê os consolidados |
| **Vigia 30min** (`~/bin/vigia_custos_baleia.sh`) | ✅ ativo desde 30/07 | cap US$ 5/dia · anomalia 1,5× 7d · fiscal vivo · edição/envio Baleia · **saldo DeepSeek < US$ 2**. Alertas Telegram Augusto 1×/dia |
| Agentes locais (temáticos) | ❌ cego | Sem registro de `usage` — valores 🟡 por volume |
| Conciliação com cartão | ❌ inexistente | Caso R$ 98 Gemini × US$ 2,68 interno; **NOVO 01/08: recarga DeepSeek afirmada não visível no saldo (US$ 1,15)** — extrato do Miguel é a única fonte da verdade final |

> **⚠️ Nota 01/08 — escalada de imagens em observação:** 28/07→01/08 o custo/dia subiu p/ US$ 4–9 (driver: `gerador_imagem_editorial` 48→397 imgs/dia, onda V4 Regional/heroes). Critério ativo (Codex+ZCode): **se 02/08 > 60 imgs ou > US$ 5 → cap reversível 60 imgs/dia**. Fallback pago Qwen-VL (chave Kimi velha) extinto 01/08 11:45. Se a onda não arrefecer, o item A.1 sobe de ~US$ 59 p/ **~US$ 200–270/mês**.

## 📉 Alavancas de economia (ordenadas por impacto)

1. **Confirmar Google AI Ultra** (se $250 ativo e subutilizado → maior alavanca única).
2. **Desligar Alibaba legacy** e confirmar fim da cobrança.
3. **Revisar GLM Max $144** antes de 17/ago (renovação) — usar quota ou downgrade.
4. **Consolidar droplets DO** (4 → 2): −$12–24/mês (Rio Carta Astro+WP num só).
5. **Instrumentar `usage` no `nucleo_llm.py` local** → transforma o 🟡 em ✅ e alimenta o painel.
6. **Fix do fiscal 7d/30d** (ou aposentá-lo: o Baleia Azul agora carrega a seção 💰 Custos & LLMs direto dos consolidados — implementado 29/07 no `enviar_baleia_azul_v2.sh`).
7. Alerta Telegram custo/dia > cap (roadmap telemetria) — evita o próximo runaway.

## 🔗 Documentos ligados

- Auditoria completa: `Foruns/forum_auditoria_custos_telemetria_recuperacao_crons_20260729.md` + `Memorias/memoria_auditoria_custos_telemetria_recuperacao_crons_20260729.md`
- Mapa das máquinas e pipeline: `CEREBRO_NODE_TELEMETRIA.md`
- Preços por modelo: `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` · Chaves/saldos: `CEREBRO_NODE_CHAVES_E_LLMS.md`
- Painel: `http://43.156.151.165/v6/custos`
- **01/09/2026 ~12:40 BRT · ZCode/GLM-5.3:** Miguel QUITOU assinaturas atrasadas: **DigitalOcean (NYC 198.199.121.136)** e **Tencent (43.156.151.165)**. Raio-X pós-pagamento (provas): DO `up 57 days` — nunca suspendeu, robôs rodaram o dia todo (capas 12:20, ciclo 12:37 BRT); Tencent `up 143 days`, cron/sshd active, DS-N com processos vivos; disco DO 🟡 80%. Conclusão: o atraso NÃO quebrou robôs (o que parecia quebrado era o daemon @dscelular_bot — não encontrado em servidor nenhum — + SSH us65→Tencent corrompido no paste, corrigido 12:35 + YouTube preso na porta do Dell). 🔴 Pendência financeira: DeepSeek pay-as-you-go US$ 2,47 (zera em horas na queima atual).
- **01/09/2026 ~12:4x BRT · ZCode/GLM-5.3:** ✅ Miguel RECARREGOU DeepSeek (US$ 20) — saldo oficial **US$ 22,44** (era US$ 2,47 🟠). Fim das pendências financeiras do dia (DO ✓ Tencent ✓ DeepSeek ✓). Restam apenas 🟡 de vigilância: Grok US$ 7,99 e disco DO 80%.
