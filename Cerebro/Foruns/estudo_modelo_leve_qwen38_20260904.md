# 📉 Estudo — Quem usa o Qwen 3.8 ("coin") e onde trocar por modelo mais leve (04/09/2026)

**Encomenda:** Miguel, por voz, manhã de 04/09 (~07:1x BRT): *"acho que o coin 3.8 esgotou… acho até que o 3.8 era grande demais, podia botar um mais fraquinho, mais leve, gastaria menos — não evidentemente para as funções mais importantes."*
**Executor:** sessão DSH-us65 (GLM-5.3). **Base:** registros do Cérebro + telemetria DSN-F de hoje.

---

## 1. Estado das chaves HOJE (04/09 manhã) — resposta à suspeita "esgotou"

| Chave/plano | Estado | Prova |
|---|---|---|
| **DeepSeek (API paga)** | ✅ **VIVA, sem esgotamento** — saldo **US$ 28,70** (07:30), caindo com consumo normal: 33,18 (04:45) → 28,70 (07:30) ≈ US$ 1,5/h durante a madrugada da esteira | série `dsn_financeiro/estado_us65.json` (pontos a cada 15 min) |
| **Qwen 3.8 Token Plan (Alibaba, "o coin")** | ⚠️ **ESGOTOU ontem** (HTTP 429 no smoke D4 do V4.2, 03/09 ~04:1x) **→ renovou hoje 03:15 BRT** (04/09 06:15 UTC). Confirmar no ciclo V4.2 das 14:00 | `Memorias/memoria_v42_investimento_teste_20260903.md` § smoke D4 |
| Fallback da casa | ✅ provado ontem: qwen 429 → `glm-5-turbo` assumiu por exceção (ciclo das 14:00 não para) | idem |

**Conclusão da suspeita:** o que esgotou foi o **Token Plan do Qwen no ZCode** (agente ZM/Dell), não a chave DeepSeek. A esteira em si nunca parou por chave.

## 2. Reclamação da Laura × coletores — NÃO é chave

Diagnóstico da CL (CL-20260904-006/007/008, madrugada): fila future vazia 03:48→06:48 porque o **coletor nacional repetiu pautas** — `todas_pautas_ja_rascunhadas_24h` nos ciclos 05:25/05:35/05:55/06:55, e o item "London Tube" travou o ciclo de ciência 3×. **A fábrica estava viva** (cron conferido no NYC; 43 matérias ontem; 14 hoje até 07:00 — série limpa de 33+ disparos pontuais). Dono do coletor: **ZM** (pendência aberta pela CL: limpar London Tube + pauta manual/Gonet). Ou seja: coletores OK de infra e de chave — falta **pauta nova** (fonte/dedupe), não crédito.

## 3. Mapa: quem usa Qwen 3.8 hoje e quanto custa

| Uso | Modelo | Custo observado | Função é "importante"? |
|---|---|---|---|
| **Agente ZM no ZCode (Dell)** | qwen3.8-max via **Token Plan** | plano fixo (foi o que ESGOTOU ontem) | Mista: sessões de código/ops do ZM |
| **R1/R2 revisores (Tencent)** | escada: GLM+web → **qwen3.8-max** (Token Plan) → brave+deepseek → deepseek estático | 2ª perna da escada | Média: revisão mecânica de posts |
| **V4.2 Investimento (Tencent)** | **qwen3.8-flash** na validação + **qwen-vl-max** na imagem; reserva glm-5-turbo | flash: fração de centavo/ciclo (1 ciclo/dia) | Baixa: validação de rascunho draft-only |
| **Materializador YouTube (NYC)** | escada: sol → **qwen3.8-max** → kimi-k2.5 | só cai no qwen quando o Sol falha | Média |
| **V4.1 redação (NYC)** | **NÃO usa Qwen**: glm-5-turbo (110×/$0,37) · deepseek-v4-pro (48×/$0,29) · gpt-5.6-sol ultra-luxo (8×/$0,18) · claude-fable-5 nacional | dia 02/09 = $2,58 total | Alta (redação) — sem Qwen |

## 4. Proposta — "mais fraquinho" onde dá, forte onde importa

**Princípio do Miguel preservado:** funções mais importantes continuam com os fortes.

1. **Triagem mecânica → flash já é suficiente (trocar max→flash):**
   - R1/R2: 2ª perna da escada qwen3.8-**max** → qwen3.8-**flash** (revisão é mecânica: conferir número, nome, link — o flash acerta; o max só entra em desempate, se necessário manter como 4ª perna).
   - Materializador YouTube: idem (max → flash; kimi-k2.5 segue atrás).
   - Estimativa: o consumo de max nesses pontos era intermitente; economia direta no Token Plan (o gargalo que esgota) e ~10-30× menor no preço por token quando exceder plano.
2. **Validações V4.2 → manter flash (já está certo):** o desenho de ontem já usa qwen3.8-flash + reserva glm-5-turbo — provado no 429. Não mexer.
3. **Visão (imagem) → qwen-vl-max só quando o caso é difícil:** validação comum de imagem pode rodar `deepseek-v4-flash-vision` (~US$ 0,0003/análise, já o olho primário das capas) e escalar p/ qwen-vl-max apenas em reprovação/empate.
4. **Agente ZM (ZCode):** disciplina de uso — tarefas mecânicas (grep, formatação, scripts pequenos) com modelo leve do próprio ZCode; qwen3.8-max reservado a código complexo/análise. É o MAIOR consumidor do Token Plan e o único ponto que já derrubou a cota.
5. **NÃO trocar (funções importantes):** redação ultra-luxo (gpt-5.6-sol / claude-fable-5), tese/frontier, fact-check cascata, DeepSeek Vision primário de capas. Custo total ontem da esteira: ~US$ 2,58/dia — saudável e auditado (`scripts/relatorio_llms_v41.py`).
6. **Blindagem sempre:** toda perna que usa Qwen mantém fallback (glm-5-turbo/deepseek) — o desenho da casa já exige (regra do Miguel 02/09: telemetria total, sem robô invisível).

## 5. Checklist de execução (dono ZM, ~30 min no NYC/Tencent)

- [ ] R1/R2: escada max→flash (`~/r1/r2` Tencent, backup + py_compile)
- [ ] Materializador YouTube: idem (`/root/agents_labs/youtube_v2/` NYC)
- [ ] Visão V4.2: deepseek-vision primeiro, qwen-vl-max no empate (tencent `v42_investimento_teste`)
- [ ] Confirmar no ciclo das 14:00 que o Token Plan renovado responde (200)
- [ ] Telemetria DSN-F continua discriminando por LLM (regra vigente)

---
*Relacionados: `Memorias/memoria_v42_investimento_teste_20260903.md` (429/fallback) · `forum_v41_ultra_luxo_cura_geo_20260902.md` §telemetria · CL-20260904-006/007/008 (fila/coletor).*
