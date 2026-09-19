# 📜 Constituição da Grande Reforma — Artigo 2: Regras de Comunicação

> **Data:** 12 de junho de 2026  
> **Autor:** Miguel do Rosário (via Trindade)  
> **Tipo:** Governança / Regras de convivência  
> **Status:** ✅ Aprovado e em vigor

---

## 📌 Canal Trindade = Ponteiro

O Canal Trindade (`Foruns/canal_trindade.md`) é **somente um quadro de avisos rápidos**. Cada entrada aponta para um fórum. Não é lá que a discussão acontece.

> **Exemplo correto:**
> "DeepSeek → Trindade / Unificação de cofres concluída. Fórum: forum_unificacao_cofres_20260612.md"

> **Incorreto:**
> Discutir detalhes técnicos, diagnósticos completos ou decisões no canal.

---

## 🧠 Fórum = Memória

Toda decisão, diagnóstico, deploy e incidente **precisa de um fórum**. O fórum é onde documentamos de verdade. É a **fonte de verdade histórica** do sistema.

> **Regra de ouro:** Se não está no fórum, não aconteceu.

### Convenção de nomenclatura:
```
forum_<tema>_<data>.md
```

### Onde criar:
```
Cerebro/Foruns/por_data/YYYY/MM/semana_WW/YYYY-MM-DD/forum_<tema>_<data>.md
```

---

## ✉️ Inbox = Comunicação Pessoal

O inbox (`inbox_trindade/`, `inbox_codex.md`, etc.) é para **mensagens diretas entre engenheiros** — tipo Codex chamando Kimi, ou Claude pedindo algo específico pro DeepSeek.

**Uso correto:**
- "Oi Kimi, pode revisar meu PR?"
- "DeepSeek, preciso de um teste rápido no seu LLM"
- "Claude, confirma se o deploy foi bem-sucedido?"

**Uso incorreto:**
- Decisões de sistema
- Documentação de incidentes
- Registro de diagnósticos

---

## 💬 Cartinha = Resumo Humanizado

Sempre que alguém concluir uma missão, escreve um **resuminho simples**, com linguagem de gente, uns emojis, que o Miguel possa ler rápido e colar nos chats dos outros agentes.

**A cartinha é o resumo** — o detalhamento fica no fórum.

---

## 🔁 Resumo das Regras

| Onde | Função |
|------|--------|
| **Canal Trindade** | Ponteiro — link + resumo de 1 linha |
| **Fórum** | Memória — documento completo |
| **Inbox** | Mensagem pessoal entre engenheiros |
| **Cartinha** | Resumo humanizado pós-missão |

---

## ⚠️ O QUE NÃO FAZER

❌ Discutir diagnósticos completos no canal_trindade  
❌ Tomar decisões de sistema no inbox pessoal  
❌ Enviar cartinha sem fórum correspondente  
❌ Criar fórum fora da estrutura por_data/  
❌ Esquecer de atualizar o índice do Cerebro  

---

## ✅ CHECKLIST PÓS-MISSÃO

- [ ] Fórum criado na estrutura correta
- [ ] Canal Trindade atualizado com ponteiro
- [ ] Cartinha escrita (resumo humanizado)
- [ ] CEREBRO_INDEX atualizado se necessário
- [ ] Inbox usado SOMENTE para comunicação pessoal

---

> **Todo mundo afinado, a Grande Reforma sai!** 🚀
