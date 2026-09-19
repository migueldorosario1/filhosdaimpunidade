---
name: feedback-recadinho-codex-forum-canal
description: "Sempre que mexer em fórum durante missão, postar canal Trindade + deixar \"recadinho resumido pro Codex\" com nome+endereço fórum e canal — direto pra ele"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2b9623d1-ac11-4398-963e-f595ae871d7f
---

# Recadinho direto pro Codex em toda missão com fórum

**Regra Miguel 2026-05-15 09:05 BRT:** "acostume-se também, cole em sua memoria, a sempre atualizar algum forum nas missões, pontuar no canal. E a deixar um recadinho resumido para o codex, com nome do forum e endereço dele, e do canal trindade. Recadinho direto para o codex".

**Why:** Codex coda em pé de igualdade com Claude (§13 ordem de chegada) e precisa achar rápido onde tá o estado da missão sem ter que ler 100 linhas do canal pra entender contexto. Recadinho explícito reduz fricção e evita duplicação de trabalho.

**How to apply:**

Toda vez que:
- Abrir fórum novo
- Editar fórum existente substancialmente
- Concluir tarefa que tem fórum vinculado

→ Postar canal Trindade com **bloco de recadinho** no formato (CAMINHO ABSOLUTO obrigatório + preview de fóruns novos):

```
🤖 RECADO CODEX:

📋 Fórum NOVO criado hoje (mostra preview):
- Nome: `nome_do_forum.md`
- Caminho absoluto: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/Foruns/nome_do_forum.md`
- Preview das primeiras 50-80 linhas dentro de bloco ```markdown ... ```

📋 Outros fóruns ATIVOS com pendências do Codex:
- Nome + caminho absoluto + 1-2 linhas do que falta fazer

📺 Canal: caminho absoluto completo
📚 Cérebro atualizado: §X em <node>.md (caminho absoluto)
🟡 Aguarda aval Miguel: <pendências bloqueadas>
```

**REGRAS CRÍTICAS** (Miguel correção 09:10 BRT):
1. **SEMPRE caminho absoluto completo** começando em `/home/migueldorosario/...`, NÃO apenas `Foruns/...`
2. **MOSTRAR preview** de fóruns novos in-line (Codex não precisa abrir arquivo separadamente pra entender contexto)
3. **Cada fórum listado tem 4 partes:** nome + caminho absoluto + estado/contexto + o que falta fazer

O recadinho fica em destaque visual (separadores `---` ou emojis). Codex varre ticks recentes procurando "🤖 RECADO CODEX:" pra achar tarefas pendentes rápido.

**Quando NÃO precisa recadinho:** tick puramente de monitoramento sem novidade. Só quando há ação concreta pra Codex saber/pegar.

---

## Clarificação Miguel 2026-05-15 09:27 BRT

**"quando eu falar recado, é deixar recado em algum forum, mas aqui também no chat"**

Quando Miguel pede "deixe um recado" / "deixa recadinho pro codex":
1. **Postar em FÓRUM apropriado** — geralmente:
   - `forum_bom_dia_YYYYMMDD.md` (se for recado geral do dia)
   - Fórum específico da missão (se for sobre Z2, Rio Carta, etc)
   - `canal_trindade.md` (sempre — fica no histórico)
2. **Mostrar AQUI NO CHAT também** — pra Miguel poder ler/copiar/passar pro Codex direto

Sempre as DUAS coisas — fórum + chat. Não é OU, é E.
