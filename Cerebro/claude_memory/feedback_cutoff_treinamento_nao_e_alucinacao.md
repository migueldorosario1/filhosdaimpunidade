---
name: feedback-cutoff-treinamento-nao-e-alucinacao
description: "Quando Claude não reconhece nome próprio (modelo IA, produto, empresa, pessoa), pode ser produto/evento posterior ao cutoff de treinamento — NÃO assumir alucinação. Perguntar ao Miguel antes de rebaixar matéria por \"nomes inventados\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

Erro caso fundador: 2026-06-13 13:45 BRT rebaixei #257974 "Governo dos EUA manda Anthropic bloquear estrangeiros" pra pending por suposta "alucinação factual grave" — cita "Fable 5" e "Mythos 5" como modelos da Anthropic e "GPT-5.5" da OpenAI. Argumentei: "Anthropic só tem Claude (Opus/Sonnet/Haiku 3.5-4.7), OpenAI tem GPT-4/4o/4.1/5 — esses nomes não existem".

Miguel corrigiu 21:18 BRT: **"fable e mythos são novos produtos da anthropic"** — lançados depois do meu cutoff de treinamento (janeiro 2026). A matéria É FACTUAL. Reverti um post legítimo. Mantive alerta errado horas seguidas insistindo no diagnóstico errado.

**Regra inegociável:**

Quando eu não reconheço uma entidade nomeada em matéria (modelo de IA, produto novo, empresa nova, pessoa, evento), **o sinal correto NÃO É "alucinação"**. O sinal correto é **"meu conhecimento está desatualizado"**.

**Como aplicar:**

Antes de classificar matéria como alucinação por "nomes inventados / entidades desconhecidas":

1. **Verificar se a estrutura interna do post bate** — se o post se refere à entidade desconhecida de forma consistente (datas, contexto, atribuições, fontes citadas), provavelmente é entidade REAL desconhecida pra mim.

2. **Marcar como SUSPEITA e perguntar ao Miguel** — não rebaixar. Pedir confirmação: "esse modelo/produto/pessoa existe? Se sim, mantenho publish."

3. **Reservar "alucinação factual grave" pra:**
   - Texto que se contradiz internamente
   - Datas impossíveis (200 d.C. com referência a iPhone)
   - Atribuições obviamente erradas (Lula presidente em 1990)
   - Recusa LLM vazada como matéria ("não posso responder isso")
   - Vazamento de prompt cru

4. **Nunca insistir em diagnóstico de alucinação** se Miguel ou outro engenheiro discorda — quem está no ano corrente sabe mais que meu cutoff.

**Memória relacionada:** [[feedback_revisor_ler_tudo_rebaixar_so_se_muito_estranho]] — limiar ALTO pra rebaixar. Esse caso passou esse limiar erroneamente porque eu não reconheci os nomes — mas "não reconhecer" não é critério.

**Tom da auto-cobrança:** sem catastrofismo, com humildade. Erro acontece. Importante é fixar a regra pra não repetir.
