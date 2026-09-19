---
name: feedback-check-cm-ponte-laura-a-cada-loop-20260822
description: "Miguel 22/08/2026 11:18 BRT ordem direta — CM tem que dar sinal de vida (CHECK) na ponte Laura Completa (de_dell.md) a CADA loop Vigília V6, sem exceção, mesmo em ciclo vazio útil"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 72dcfc6b-0e41-4a3a-a509-8308aa9cfb28
---

**Ordem Miguel 22/08/2026 11:18 BRT (chat CLI direto após ciclo vazio 11:16):** "dá um sinal de vida na ponte laura completa. não esquece nunca de dar seu check lá a cada loop."

**Contexto do disparo:** ciclo Vigília V6 Slot A 11:16 rodou vazio útil (9 drafts todos com meta canibal), reportei ao Miguel no CLI mas NÃO tinha registrado nada na ponte (`Foruns/ponte_laura_completa/de_dell.md`). Havia CHECK formal do ZM-004 pendente resposta minha desde 10:40. Miguel percebeu ausência.

**Why:** ponte Laura Completa é o registro auditável transversal aos 6 agentes (CM+GM+AGY Dell / CL+GL+ZL Windows) — silêncio meu na ponte parece agente OFF pra Trindade, gera dúvida sobre estado do Loop Miguel. CHECK a cada ciclo mata dupla dúvida: (1) estou vivo, (2) o que rodou. Vale mesmo em ciclo sem publish, porque "vazio útil" é resultado válido — omitir da ponte é pior que reportar zero.

**How to apply:** ao FIM de cada ciclo Vigília V6 (Slot A ou B, DIURNO 20min ou NOTURNO 1h), obrigatoriamente:

1. Anexar em `Cerebro/Foruns/ponte_laura_completa/de_dell.md` bloco curto com prefixo `CM-YYYYMMDD-NNN`:
   ```
   [DD/MM/YYYY HH:MM BRT] CM-YYYYMMDD-NNN — Claude Miguel → TODOS (CHECK ciclo Vigília)
   CHECK CM slot=A|B HH:MM estado=vivo publish=N correcoes=N descartes=N proximo=HH:MM
   [1-3 linhas de detalhe se houver algo transversal — canibal notável, HOLD, alerta Laura, sinal factual]
   ```

2. Se ciclo vazio útil: reportar assim mesmo. Silêncio ≠ ausência. Formato: `estado=vivo publish=0 correcoes=0 descartes=0 fila_util=0 custo_llm=zero`.

3. Se houver pedido/CHECK transversal pendente (ex: ZM-004 tipo "aguardo CHECKs: ZL·CL·AGY·CM·XM·XL·GM"), aproveitar o CHECK do ciclo para responder inline — não deixar acumular por >1 ciclo.

4. Nunca pular o CHECK esperando "próximo ciclo terá mais coisa". Se a próxima janela é 20min à frente, o silêncio de 20min já é sinal ruim pra Trindade.

**Consequência prática:** ledger próprio (`ledger/claude_miguel.md`) e heartbeat (`estado/claude_miguel.md`) continuam obrigatórios como antes, mas ambos são LEITURA passiva pros outros — CHECK em `de_dell.md` é anúncio ATIVO que aparece no tail dos que abrem a ponte. Manter ambos os mundos.

Relacionadas: [[reference-ponte-laura-completa-20260817]] (canal), [[feedback-comunicacao-miguel-agentes-hibrida-20260820]] (coordenação = ponte, urgência = chat direto).
