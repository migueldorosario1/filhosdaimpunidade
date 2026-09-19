# 🔍 PARECER — AUDITORIA CURA GEOPOLÍTICA/TECNOLOGIA (ZM-20260902-043, auditoria 2 pedida pelo Miguel ao DS-N Ideias)

> **Pendência:** MEMORIA_VIVA do DS-N Ideias (bloco ZM-043, ~15:3x) — ver `codigo/v41_ciclo.py` (marcas `V41_CURA_GEO_TEC_20260902`, `V41_TESE_FRONTIER`, `V41_FILA_SEM_CLOG`, `V41_MOTIVO_HONESTO`) + `dados/linha_editorial_viva.md`. **Perguntas centrais:** (1) a regra de pauta afirmativa (BRICS/SCO sem vilão) + a linha editorial podem gerar **viés de repetição ou paneleiro** (a mesma tese girando)? (2) o **fail-closed das âncoras** segue intacto?
> **Escopo deste parecer:** NÍVEL REPO (evidência documental) — `codigo/v41_ciclo.py` e `dados/linha_editorial_viva.md` NÃO estão neste workspace (vivem no runtime/NYC; execução é do ZM). O parecer responde com o que o repo prova e aponta o checklist de campo.

## 1. Evidência disponível no repo

Fonte: `forum_v41_ultra_luxo_cura_geo_20260902.md` (ZM-043) + `memoria_v41_ultra_luxo_cura_geo_20260902.md` + meus desenhos anteriores (005 §3.1 dedup de tese · 007 §4.2 anel de audiência · dossiê 008) + a prova 31/08 (Kast — banco geo cheio de Irã/China, critério premiava drama de personagem):

1. **Cura geo/tec (ZM-043):** a seca era tese+fila, não coleta → `V41_FILA_SEM_CLOG` (item sem post_id que falha só volta em 6h) + `V41_MOTIVO_HONESTO` (anti-repetição não sobrescreve o motivo do juiz) + coleta reforçada (+23 keywords geo/IA/BRICS, +3 queries Brave).
2. **Pauta afirmativa sem vilão:** "pauta afirmativa (BRICS/SCO/Sul Global) NÃO precisa mais de vilão — regra nova no system prompt da tese + linha editorial viva + manual injetados no contexto da tese ('a linha editorial prevalece sobre tudo'). Fail-closed intacto." Provado ao vivo: pauta SCO que falhava desde 12:01 UTC passou com vilão vazio; pauta de guerra passou com vilão nomeado.
3. **`_tese_frontier()`** lê o knob ultra-luxo (a tese é a etapa que usa frontier).
4. **Manual v2.1.0:** princípios/diretrizes (não regras ditatoriais); linha editorial = lente, não panfleto; criatividade dentro da linha é bem-vinda.

## 2. Resposta à pergunta 1 — viés de repetição/paneleiro? (nível repo)

**O risco é REAL e agora está INVERTIDO — e isso é a descoberta principal deste parecer.**

- Antes da cura (prova 31/08): o critério de tese premiava **vilão nomeado + drama** → o banco geo, cheio de Irã/China, escolhia crime/escândalo/personagem; a repetição era de TEMA com tese de guerra (a mesma pauta com ângulos diferentes entrava — China-IA 4×, bitcoin 3×).
- Depois da cura: pauta afirmativa SEM vilão destrava BRICS/SCO/Sul Global — mas cria o risco ESPELHO: **a mesma tese "Sul Global constrói / Ocidente hegemoniza" girando em loop diário**, porque a linha editorial viva ("prevalece sobre tudo") vira atrator: se o único critério de aceite é "afirmativa + linha", qualquer fato do dia cabe na MESMA tese-âncora.
- **Sintoma a vigiar (métrica):** 2+ análises na janela 7d com a MESMA tese-âncora (mesmo verbo/conflito/direção, mesmo par sujeito/objeto) = repetição de tese, mesmo com fatos diferentes. O dedup atual (L13) é de pauta; o `V41_MOTIVO_HONESTO` protege o motivo do juiz — **falta o dedup de TESE na captura** (meu 005 §3.1, desenho já entregue: comparar núcleo factual E tese-âncora com os últimos 50 do banco).

**Defesas no desenho (o que eu já propus e o que falta):**
1. Dedup de TESE na captura (005 §3.1) — não implementado (desenho).
2. Régua da pauta afirmativa: **exigir o DADO NOVO do dia** (o que mudou hoje — número, evento, decisão), senão a peça é opinião, não análise (mesma régua do V4.2 Investimento, arquivo irmão). Pauta afirmativa sem fato novo = paneleiro.
3. Métrica diária do funil com coluna tese/fonte/ângulo (006 §6.2 — sou dono; em execução pelo ZM quando autorizado).
4. Anel de audiência INFORMA-não-decide (007/dossiê) — a audiência mede o desdobramento, não elege a tese.

## 3. Resposta à pergunta 2 — fail-closed das âncoras? (nível repo)

**NÃO PROVÁVEL NESTE WORKSPACE — o código não está aqui.** O forum declara "fail-closed intacto" e a prova ao vivo (SCO passou, guerra passou) sugere que o caminho feliz E o caminho sem-vilão funcionam. Mas "fail-closed intacto" é a afirmação exatamente sobre o caminho DE FALHA (tese sem âncora válida → NÃO escreve), e isso só se prova lendo o código e forçando o caso. Checklist de campo (dono ZM):
1. Ler `codigo/v41_ciclo.py` nas marcas `V41_CURA_GEO_TEC_20260902` / `V41_TESE_FRONTIER` / `V41_MOTIVO_HONESTO` e confirmar: tese sem âncora/verbo/conflito → retorna `llm_sem_tese_valida` e NÃO gera rascunho (sem bypass).
2. Forçar 1 caso afirmativo sem âncora em espelho (pauta BRICS sem dado/verbo) → deve falhar fechado.
3. Confirmar que a linha editorial viva é INJETADA (contexto) e não REPLACE do fact-check (o FC continua independente da linha — senão a "linha prevalece sobre tudo" vira censura de veredito; a leitura correta é: prevalece no ENQUADRAMENTO da tese, nunca no veredito factual).
4. Registrar o resultado no fórum da cura geo (prova de leitura, padrão da casa).

## 4. Veredito (nível repo)

1. **Paneleiro:** risco real e agora invertido (repetição de TESE afirmativa, não de tema de guerra) — defesa de desenho pronta (dedup de tese + régua do dado novo do dia + métrica do funil); implementação é do ZM quando o Miguel autorizar.
2. **Fail-closed:** declaração no forum, prova de caminho feliz ao vivo, mas a prova do caminho de falha exige leitura de código (fora deste workspace) — checklist entregue ao ZM.
3. **Cruzamento com a constituição ideológica (minuta DSC-045, arquivo irmão):** a pauta afirmativa não pode virar "defender aliado sem crítica" — o Art. 10º (discordância honesta) e o Art. 17º (limite da posição declarada) são a régua que impede o paneleiro de virar propaganda.

Nada a alterar em produção por mim (Lei de Poderes — execução é do ZM; eu analiso e desenho).

— DS Nuvem Ideias (DS-N Ideias) · 20260902 15:49:29 BRT
