---
name: feedback-ler-cerebro-boletim-news-ao-acordar
description: "Ao despertar, LER Cérebro/Boletim News PRIMEIRO antes de qualquer ação. Boletim é Camada 2 destacada no INDEX_MASTER e contém últimas atividades Miguel + frentes vivas + cronológico."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6bc43130-4d88-4938-bd25-084d519ee690
---

**Regra:** Toda sessão Claude lê `Projeto Cafezinho Agentes/CEREBRO_NODE_BOLETIM_NEWS.md` PRIMEIRO ao despertar — antes de tarefas, fóruns, canal Trindade ou qualquer outra coisa.

**Why:** Em 2026-05-15 13:00 BRT acordei lendo só o `estado_fim_sessao_20260514_1759.md` (ontem) e reportei como atual. Miguel me corrigiu duramente ("ih ta atrasado. perdeu memoria"). Quando pediu pra reler canal Trindade, eu li só últimas 200 linhas de 1.8MB e propus ação numa frente cuja decisão estava em outro ponto que eu não vi. Miguel cortou: "perai. o que voce está fazendo? voce está pegando materias antigas?". Ele então mandou "antes de qq coisa, faça um forum memorias de hoje". Depois ordenou criar o Boletim News no Cérebro pra que TODA IA acorde já orientada. Sua frase central: "é para isso que estamos construindo o cérebro".

**How to apply:**
1. **Passo 0 (NOVO):** Ler `Projeto Cafezinho Agentes/CEREBRO_NODE_BOLETIM_NEWS.md` — destaque "Últimas Atividades do Diretor Miguel" por iniciativa (Cafezinho/Rio Carta/Origens/GSN) + TOP frentes vivas hierarquizadas + cronológico hoje+7d.
2. **Passo 1:** `CEREBRO_INDEX_MASTER.md` (mapa Camada 1)
3. **Passo 2:** Node pertinente ao escopo do tick (GOVERNANCA/BUGS/ARQUITETURA/COMUNICACAO/CHAVES/RIOCARTA)
4. **Passo 3:** `Tarefasdeagora.md` — slot ativo
5. **Passo 4:** Canal Trindade `Foruns/canal_trindade.md` (últimas mensagens — mas Boletim já dá o panorama, então pode ser leitura focada)
6. **Passo 5:** Fórum/memória da frente ativa

**Diferenças importantes vs ritual antigo:**
- Antes: começava pelo INDEX_MASTER (mapa do Cérebro). Agora: começa pelo Boletim News (estado real).
- Boletim News tem ponteiros — não substitui leitura dos fóruns, mas evita "pegar matérias antigas" como aconteceu hoje.
- Boletim auto-atualiza a cada decisão Miguel / deploy crítico / § Cérebro novo. Toda IA pode/deve atualizar quando fechar algo importante.

**Tamanho/peso:**
- Alvo Boletim: <500 linhas / <25KB. Se passar, auto-poda agressiva movendo linhas >7d pra `Memorias/boletim_arquivo_<periodo>.md`.
- Filosofia: só ponteiros, conteúdo nos fóruns/memórias.

Relacionado: [[reference-sistema-resumo]] [[feedback-trigger-retomar]]
