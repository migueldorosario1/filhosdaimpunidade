---
name: ceticismo-pesquisa-ficticia-worker-v4
description: "Antes de publicar draft V4 que fala de pesquisa de opinião, checar se worker marcou como \"fictícia/hipotética/não verificável\" no título ou corpo — bug sistêmico do template que precisa ser verificado ceticamente com WebSearch."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3300515f-8122-40eb-b750-07b8ef13881e
---

Ao processar draft V4 (autor 5786) vertical geopolítica ou nacional cujo tema central é **pesquisa de opinião** (Marquette, Pew, Datafolha, Ibope, Ipec, AtlasIntel, Quaest, YouGov, Reuters/Ipsos, Marist, etc.): **sempre rodar WebSearch cético antes de aceitar a estrutura do texto**. Se worker marcou a pesquisa como `fictícia`, `hipotética`, `não verificável`, `suposta` no título/corpo — ou se corpo inteiro está em verbos condicionais (`teria`, `seria`, `confirmaria`, `indicaria`, `sugeriria`) —, provavelmente é bug do template, não pesquisa falsa. Rewrite completo em afirmativo baseado em WebSearch.

**Why:** Caso fundador PID 264708 (07/08/2026 19:47 BRT): título original = *"Pesquisa fictícia sugere que americanos desaprovam conflito com Irã"*, corpo todo em condicional com expressões `não verificável`/`suposto`/`hipotético`. WebSearch com 8 fontes independentes (The Hill, Marquette Law School, OSV, ABC News, Pew, Marist, Reuters, Opera Mundi) confirmou: Marquette Law School Poll REAL, 22-29/jul/2026, 1.076 adultos, MOE 3,2, 88% dos americanos dizem EUA não atingiram objetivos na guerra contra o Irã (subiu de 81% jun). Publicar sem rewrite teria sido desastre editorial — Cafezinho anunciando "pesquisa fictícia" quando pesquisa é totalmente factual. Bug parece sistêmico (não confundir com o caso 264581 mesmo dia, que trouxe AtlasIntel/Bloomberg sem esse padrão) — provável interação entre prompt "seja cauteloso com dados" + tema politicamente sensível (Trump/Israel/Irã).

**How to apply:**
- **Detecção rápida:** ao puxar draft V4, grep em título + corpo por: `fictíci`, `hipotétic`, `suposto`, `não verific`, `teria` (múltiplas ocorrências), `seria` (múltiplas), `confirmaria`, `indicaria`, `sugeriria`. Se 2+ dessas ocorrem no mesmo texto, ligar alerta.
- **Verificação:** WebSearch em `<instituto> poll <tema> <número> <ano>` (ex: "Marquette poll Iran 88% 2026"). Buscar 3-5 fontes independentes. Se pesquisa existir → rewrite completo em afirmativo, adicionar dados reais (data, N amostra, MOE, evolução temporal). Se pesquisa NÃO existir → pending + motivo=`alucinacao_pesquisa_worker_v4_confirmada` + escalar ZCode via `inbox_trindade/zcode.md`.
- **Escalação ZCode:** já foi feita cartinha `[CLAUDE-BUG-WORKER-V4-PESQUISA-FICTICIA-20260807-2005-BRT]` pedindo revisão do prompt do worker V4 na vertical geopolítica. Aguardando diagnóstico. Se ZCode reportar patch aplicado, esta memória pode ser aposentada; até lá, ceticismo obrigatório.
- **Não confundir:** pesquisa `AtlasIntel/Bloomberg Lula 48%` (264581, mesmo dia, mesma vertical) NÃO teve o bug — logo, padrão afeta subset (talvez temas Trump/Israel/EUA-Irã, ou fontes menos conhecidas). Manter olho aberto, não presumir.

Ver [[feedback-nomenclatura-zcode-ambiente-nao-kimi]] pra escalação; [[feedback-checagem-titulo-semantica-e-genero-fonte]] pra outros bugs recorrentes worker V4; [[feedback-autoaprendizado-governado-ativo]] pra registro JSONL (campo `editorial_alert_CRITICO`).
