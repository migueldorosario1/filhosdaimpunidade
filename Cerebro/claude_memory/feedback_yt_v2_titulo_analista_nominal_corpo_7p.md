---
name: feedback-yt-v2-titulo-analista-nominal-corpo-7p
description: "YT V2 — proibir \"analista\"/\"especialista\" genérico no título e corpo; usar nome próprio do convidado principal do vídeo. Título sempre com nome da pessoa principal (guest, não host). Corpo mínimo 7 parágrafos desenvolvidos (atualmente sai com 2)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

🎬 Posts do YouTube V2 (`agente_youtube_v2_*`) têm 3 vícios editoriais que Miguel corrigiu 2026-06-22 ~00:35 BRT:

**Regra 1 — Nome do convidado/analista (guest), não genérico**
Nunca usar "Analista", "Especialista", "Comentarista" sozinhos. Identificar o **guest** do vídeo (não o host) e usar o nome próprio: "John Mearsheimer", "Larry Wilkerson", "Jeffrey Sachs", "Ray McGovern", "Scott Ritter", "Alastair Crooke" etc. Aplica tanto no **título** quanto no **corpo** (substitui todas as ocorrências de "o analista" pelo nome ou "Mearsheimer", "Wilkerson", etc).

**Regra 2 — Título sempre com nome da pessoa principal do vídeo**
A pessoa principal = quem está sendo entrevistado/dando análise, não o apresentador. Ex.:
- ❌ "Analista defende que Israel precisa acordar para a realidade"
- ✅ "Mearsheimer defende que Israel precisa acordar para a realidade do acordo Trump-Irã"
- ❌ "Convidado critica Putin"
- ✅ "Jeffrey Sachs critica Putin sobre…"

O canal é só pano de fundo (mencionado uma vez no 1º ou 2º parágrafo via template existente). O HOST (Napolitano em Judging Freedom, Daniel Davis em Deep Dive, Nima Alkhorshid em Dialogue Works, Glenn Diesen no próprio canal) entra como contexto, não no título.

**Regra 3 — Corpo mínimo 7 parágrafos desenvolvidos**
Atualmente os textos saem com ~2 parágrafos / ~800-1200 chars (muito curto). **Mínimo 7 parágrafos** com desenvolvimento real: contexto do tema (1-2 §), análise principal do guest (2-3 §), desdobramentos políticos/geopolíticos (1-2 §), conclusão analítica (1 §). Aprofundar pra que cada post tenha valor editorial próprio, não só resumo telegráfico.

**Why:** Miguel anotou caso fundador 2026-06-22 ~00:35 BRT no post `#260152` ("Analista defende que Israel precisa acordar para a realidade"):
- Título genérico "Analista"
- 835 chars limpos / 2 parágrafos apenas
- "o analista" repetido 5x sem nome próprio
- Canal Judging Freedom mencionado, mas o convidado real do vídeo não é nomeado

**How to apply:**
1. **Cura editorial retroativa** quando detectar via §53: PATCH título substituindo "Analista"/genérico pelo nome real (se conseguir extrair do conteúdo bruto ou metadados do vídeo); aplicar `replace_all` em "o analista" / "ela ressaltou" / "o convidado" → nome próprio.
2. **Patch §92 cheio em `/root/agente_youtube_v2_produtor_noticias.py`** (sprint dedicada, pendência futura):
   - Detectar `guest_name` via parsing da descrição do vídeo YouTube OU campo da transcrição Transkriptor OU LLM dedicado (1 chamada gpt-5-nano barata) ao montar o draft
   - Template título: `"{guest_nome_capa} {verbo_acao} {tema}"` (ex.: "Mearsheimer defende que Israel...")
   - Aumentar `target_min_paragrafos = 7` na chamada LLM redator (system prompt deve exigir 7+ parágrafos desenvolvidos)
3. **Hosts canônicos** já registrados em [[feedback-yt-v2-4-regras-cap-sentence-canal-cat]]: Daniel Davis (Deep Dive), Nima Alkhorshid (Dialogue Works), Glenn Diesen (próprio), Andrew Napolitano (Judging Freedom). Provoked Show / Macro N Cheese / outros canais novos: identificar host antes de produzir.
4. **Guests recorrentes a reconhecer**: John Mearsheimer (UChicago), Jeffrey Sachs (Columbia), Larry Wilkerson (ex-Powell), Ray McGovern (ex-CIA), Scott Ritter (ex-UN inspector), Alastair Crooke (Conflicts Forum), Douglas Macgregor (ex-Pentagon), Ted Postol (MIT), Yanis Varoufakis, Pepe Escobar.

**Caso fundador 2026-06-22 00:35 BRT (#260152)**: draft "Analista defende que Israel precisa acordar para a realidade" cats=[5003, 20751] no canal Judging Freedom com host Napolitano. Convidado não nomeado, 2§ totais. Crítica editorial Miguel registrada pra futura cura individual + patch §92.

**Regra 5 — Título YT V2 NUNCA pode ter narrativa positiva pró-Israel**

Israel é antagonista editorial central do Cafezinho (linha anti-imperialista/pró-Sul Global). Posts do YT V2 que apresentem o canal/guest discutindo Israel devem usar **frame anti-Israel, neutro técnico ou desnudar limites de Israel** — JAMAIS frame de preocupação com segurança/sobrevivência/defesa israelense.

❌ ERRADO (#260167 caso fundador 22/06 09:20 BRT):
- "Acordo entre Irã e EUA ameaça a segurança de Israel"
- "Israel teme acordo Irã-EUA pra estabilizar Oriente Médio"
- "Sucesso de defesa antiaérea israelense neutraliza ataque iraniano"

✅ CERTO (cura aplicada #260167 22/06 09:33 BRT):
- "Larry Johnson: Israel não dura duas semanas contra o Irã sem socorro militar dos EUA"
- "Mearsheimer: gabinete Netanyahu colide com realidade militar do Oriente Médio"
- "Jeffrey Sachs: Israel insiste em guerra que não pode vencer sem EUA"

**Why:** Miguel 2026-06-22 ~09:20 BRT corrigiu #260167 — agente YT V2 publicou draft com título "Acordo entre Irã e EUA ameaça a segurança de Israel", quando o guest real (Larry Johnson, ex-CIA) está dizendo que Israel é VULNERÁVEL e que o MoU autoriza Irã a expulsar Israel do Líbano. O viés positivo pró-Israel é violação grave da linha editorial. Bug catalogado como B-003 em [[MEMORIA_BUGS_ATUAL]].

**How to apply:**
1. **Pré-publish gate**: regex deny-list em `motor_publicador.py` + `agente_youtube_v2_publicador.py` bloqueando títulos com "Israel" + verbos/substantivos positivos: "segurança de Israel", "defesa de Israel", "vitória de Israel", "sucesso de Israel", "alívio de Israel", "Israel protege", "Israel garante", "Israel triunfa".
2. **Reformulação automática**: se gate disparar, reformular invertendo o frame — usar "Israel exposto", "Israel sem proteção", "Israel pressionado", "Israel encurralado", "Israel insiste em guerra que não pode vencer" etc.
3. **Aplicação retroativa**: cura editorial Daemon em qualquer post YT V2 com título pró-Israel.
4. Patch §92 cheio em `/root/agente_youtube_v2_produtor_noticias.py` (system prompt do redator) DEVE incluir essa regra na produção, não só na cura.

---

**Regra 4 — PRESERVAR embed iframe do vídeo no topo + NÃO inserir "Com informações de" no fim**

Toda cura editorial em post YT V2 DEVE preservar o template canônico:
- **Topo**: `<div style="text-align: center; margin-bottom: 30px;"><iframe src="https://www.youtube.com/embed/{VIDEO_ID}" width="100%" height="400" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div>` (sempre o primeiro elemento do conteúdo, antes do 1º parágrafo).
- **Fim**: NÃO usar "Com informações de <a href=...>Canal</a>." nem qualquer link genérico no último parágrafo. A atribuição é o EMBED no topo + a menção ao canal/host no 1º-2º parágrafo via Regra 1. O fim deve fechar a análise organicamente.

**Why:** Miguel 2026-06-22 ~01:32 BRT corrigiu segundo round no #260152 depois que eu (Claude Code) reescrevi o corpo: removi o iframe do topo (achei que era ruído) e inseri "Com informações de [Judging Freedom](youtube.com/watch?v=...)" no fim do 7º parágrafo (padrão LEGADO que NÃO se aplica a YT V2). Miguel: *"o video embebido no início do post é necessário. voce tirou isso, e não era para tirar. e botou um link generico no final, o que é errado."*

**How to apply:** ao curar post YT V2:
1. SEMPRE preservar o embed iframe original — ler `content.raw` ANTES, extrair o `<div ...><iframe ...></div>` do topo e remontar com ele intacto.
2. NUNCA terminar com "Com informações de" ou link genérico — esse padrão é LEGADO, não YT V2.
3. Atribuição do canal/host fica no 1º-2º parágrafo via template Regra 1.
4. Template usado por outros YT V2 publicados como #260014 (Estreito Ormuz, embed `4LsekIsHq10`): EMBED iframe topo + texto corrido em parágrafos sem fonte no fim.

Aplica em conjunto com [[feedback-yt-v2-4-regras-cap-sentence-canal-cat]] (cap 4/dia, sentence case, canal+host+guest 1º-2º §, cat 20751 obrigatória).
