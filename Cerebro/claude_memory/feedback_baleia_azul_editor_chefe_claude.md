---
name: feedback-baleia-azul-editor-chefe-claude
description: "Claude é editor-chefe do Baleia Azul desde 19/07/2026. Gera edição todo dia 06:00-07:45 BRT em `Projeto Cafezinho Agentes/boletim_baleia_azul_AAAAMMDD.md` + verificações extras por ciclo Vigília V5. Cartinha permanente ZCode 30/07 20:15 BRT."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b2a244d9-f9b6-46dc-8edb-3f4744e84e11
---

**Regra:** A partir de 19/07/2026 (decisão Miguel registrada no nodo Baleia), Claude é editor-chefe do **Baleia Azul** (newsletter do Cafezinho). O Sentinela foi desligado 27/07 16:15 e não gera mais fallback — se eu não gerar, o dia inteiro morre (e-mail + Telegram + painel).

**Why:** O Baleia é o produto editorial diário do Miguel — se não sai, não há e-mail para leitores, não há push no Telegram, não há atualização do painel. O emissor `enviar_baleia_azul_v2.sh` (8h/18h BRT) bloqueia envio se não achar `boletim_baleia_azul_YYYYMMDD.md` do dia. Cartinha fundadora: `cartinha_zcode_claude_baleia_custos_vigilancia_20260730.md`. Contexto: Baleia parou 28/07 → 01/08 (5-6 dias sem edição) porque ninguém assumiu o vazio deixado pelo Sentinela.

**How to apply (janela diária):**

**06:00-07:45 BRT — gerar edição:**
1. Criar `Projeto Cafezinho Agentes/boletim_baleia_azul_YYYYMMDD.md` do dia
2. Se houver rascunho manual do Miguel, incorporar; senão gerar dos dados coletados (como o Sentinela fazia)
3. Marcar como "desatualizado" qualquer dado não confirmado; **nunca inventar/estimar número ausente**
4. **Incluir seção obrigatória "💰 Custos & LLMs"** com: ontem, 7d, 30d, projeção mensal, top-3 gastos — TODOS com data da medição, lidos dos consolidados NYC (`/root/agent_data/custos_consolidados/AAAA-MM-DD.json`). Fonte canônica: `CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md`
5. Quedas/estouros de custo entram ao lado dos sinais positivos (transparência total — Miguel taxativo)

**A cada ciclo Vigília V5 (~30min) checar 4 itens ADICIONAIS:**
1. Fiscal rodou hoje? (`/root/agent_data/fiscal_tokens.log` NYC com data de hoje, após 8h)
2. Edição do dia existe? Se não → gerar agora
3. Envios 8h/18h saíram? (`/tmp/baleia_azul_envios.log` local, procurar "Baleia Azul enviada")
4. Custo de ontem > US$ 5 OU > 1,5× média 7d? → investigar causa e **alertar Miguel no Telegram Augusto** com números
   - O vigia local do ZCode (`~/bin/vigia_custos_baleia.sh`, cron */30) já alerta essas condições 1×/dia
   - Meu papel é **explicar a causa e agir**, NÃO duplicar alerta

**Regras de transparência (Miguel é taxativo):**
- Todo número com data de medição
- Dado não confirmado = "desatualizado"
- Nunca inventar/estimar número ausente
- Quedas e estouros na edição ao lado dos positivos

**Registro:**
- Mudanças estruturais no processo do Baleia → `CEREBRO_NODE_ATUALIZACOES.md`
- Tema novo → Fórum + Memória (Regra do Tema Duplo)

**Escalação:** Bloqueios que dependam do Miguel (credencial, decisão editorial) → canal Trindade com tag `[CLAUDE-BALEIA-BLOQUEIO-...]`.

**Integração com loop Vigília V5:** A janela 06:00-07:45 cai dentro do ciclo NOITE 06:17. A partir de 02/08/2026 esse ciclo passa a ter DUAS missões: (a) processar drafts V4 elegíveis, (b) gerar edição Baleia do dia. Ciclos 07:17+ verificam se envio 8h saiu (`baleia_azul_envios.log`) e se custo do dia anterior disparou alerta.

Regras irmãs: [[feedback-loop-vigilia-opus-v5]], [[feedback-gatilho-zizi-retomada-sessao-31-07]].

**Contexto operacional 01/08/2026 10:52 BRT (ZCode retomada):**
- Fiscal 7d/30d fix aplicado hoje 08h (primeira vez com números reais: ontem US$ 6,40 · 7d US$ 26,58 · 30d US$ 455,50)
- Chave Kimi vision NYC sincronizada (era 401 → agora 200) — juiz visual volta pra quota flat
- Escalada custos: 48 → 93 → 397 → 180 → 161 imgs/dia (V4 Regional 27 UFs + heroes sem texto regenerando)
- Baleia ausente há 5-6 dias — recomeço 02/08 06:00 BRT

**PRIORIDADE ATUAL do Miguel (01/08 11:20 BRT — correção explícita):** transparência + precisão dos gastos reais, NÃO barreira de custo. Miguel: "não tem nada de barreira de custo menor de 5 dólares. isso fica pra depois. no momento o que eu preciso é de transparência, e precisão, o que só vai acontecer quando o nosso agente estiver alinhado com os gastos reais pagos por mim com cada llm."
- **Regra:** editor do Baleia = fiscal fiel do gasto real, SEM cap arbitrário. Trabalho #1 = fazer o fiscal bater com o que Miguel paga em cada dashboard (Anthropic, Moonshot/Kimi, DeepSeek, Google, fal-ai, OpenAI, Groq, Qwen, etc)
- Só depois de bater os números reais, discutir volume/limite
- Anti-pattern: propor "gate US$ 7,50" ou "cap 60 imgs/dia" antes de garantir precisão do fiscal — foi erro meu 01/08 10:52 corrigido por Miguel imediatamente
- Ordem correta: (1) inventariar todos os LLMs pagos + fonte de verdade de cada dashboard, (2) comparar fiscal atual × dashboards, (3) corrigir divergências, (4) SÓ ENTÃO conversar sobre limites


---

## ⚠️ SUPERSEDED 07/08/2026 10:05 BRT — Baleia Azul passa a ser editado integralmente pelo Kimi (ZCode)

**Ordem Miguel 07/08 ~10:05 BRT** (via chat, comunicada por Kimi 10:25 em `inbox_trindade/claude.md`): "deixa o Claude mais livre na missão de monitorar os sites". Kimi assume:
- Fechamento da edição das 06:00-07:45 BRT (a partir de 08/08).
- Escrita da coluna, revisão, envio.
- Manutenção do emissor (Kimi já corrigiu bug da saudação por faixa horária).

**Estado 07/08**: edição das 08:00 atrasou por eu não ter gerado o `boletim_baleia_azul_20260807.md` a tempo (fui pego pelo cruzamento de vigília temáticos + drenagem Ponte v3 + dev gate_pre_publish). Kimi gerou às 10:20 com números reais (56 posts ontem = recorde retomada, 14 hoje até 10h).

**Regra atual pra mim (Claude)**:
- ❌ Não gero mais boletim Baleia Azul.
- ❌ Não faço mais fechamento diário do Baleia.
- ✅ Se coletor de custos falhar OU Kimi pedir ajuda via ponte, respondo como parceiro (não como editor).
- ✅ Meu foco: Vigília V4 + vigília temáticos 3×/dia + drenagem Ponte v3 + dev gate_pre_publish.

**Kimi manteve o que eu construí**: linguagem de carta, datas nas duas pontas, manchetes completas, pendência só com resposta. Assina embaixo dessas regras.

**Regra irmã nova**: [[feedback-vigilia-sites-tematicos-3x-dia]] — minha missão liberada.


---

## Regra completa do novo editor Kimi (Miguel 07/08 ~11:00 BRT)

**Miguel especificou pra mim (chat 07/08 ~11:00) — passei pro Kimi via ponte:**

1. **2 edições por dia**: **08:00 BRT** (manhã) + **18:00 BRT** (tarde/noite). Antes eu fazia só 06:00-07:45; agora Kimi manda 2×.
2. **Destinatários**: **Miguel + Gabriel** por email.
3. **REGRA CRÍTICA (verbatim)**: *"não tem importância chegar atrasado. Se tiver qualquer problema e atrasar, não tem importância. NÃO É PRA PULAR a edição, não. Faz na próxima, faz atrasado, mas pode fazer."*
   - **Atraso está OK** — não há SLA rígido.
   - **Pular edição = zero. Nunca zero.** Se travar 08h, manda 10h/12h/14h. Se travar 18h, manda 20h/22h. Se 22h ainda tá travado, manda 08h junto com a próxima. Sempre entregar.
4. **Miguel 07/08 11:00 reclamou**: não recebeu edição da 08h (Kimi enviou 10:20). Pode ser bounce/spam do lado do email; Kimi ZCode deve verificar log emissor + entregar 18h sem falta.

**Meu papel a partir de 07/08 10:05 BRT (Claude):**
- ❌ Não gero mais boletim.
- ❌ Não envio mais email.
- ✅ Se Kimi pedir ajuda via ponte (coletor caiu, dado ausente), respondo como parceiro.
- ✅ Se Miguel reclamar comigo (como agora), passo recado ao Kimi via `inbox_trindade/kimi.md` + `canal_trindade.md` + emito recibo preventivo.

**Boas práticas gerais desta transição (aprendizado):**
- Quando missão passa entre agentes, quem sai deve documentar as regras completas em carta pro que entra — evita perda de contexto.
- Miguel pode dar regra a mim mesmo depois da transição (por hábito) — meu papel é traduzir e repassar sem interpretar.
