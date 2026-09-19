# FÓRUM — Regra do AUTOR no agente comentarista (proibido responder na 1ª pessoa do autor)

**Data:** 2026-08-10 (~18:00 BRT)
**Agente:** ZCode — GLM-5.2 (Z.ai coding plan) — Kimi/Qwen esgotados 🔴🔴
 **Conversa:** "Bug do comentarista respondendo na 1ª pessoa do autor"
**Origem:** ordem do Miguel (transcrição de áudio `20260810_171707_Clip_3.txt`, 17:17 BRT)
 **Estado:** ✅ CORREÇÃO APLICADA E COMPILADA nos 3 arquivos ativos. Pendência: teste real do Miguel.

---

## O problema (relato do Miguel, quase literal)

Um dos comentaristas, a persona **Francisco de Assis (Chico)**, respondeu a um comentário do leitor **Mozart Dias** — *"meu amigo, você é de Fortaleza?"* — com *"eu não conheço o Ceará"*. O problema: **o Mozart estava falando com o AUTOR (Miguel do Rosário), não com o Chico.** A persona respondeu na primeira pessoa, como se a pergunta fosse com ela — o que dá a qualquer leitor a impressão de que **o Miguel é o Francisco de Assis**.

> "Ele respondeu na primeira pessoa, como se o cara tivesse falado com ele. Ele falou com o autor, com o Miguel do Rosário, não com o Francisco Assis. Tem que corrigir isso no prompt. E quando o comentário for pra mim, pro autor, o comentarista não pode responder na primeira pessoa, senão fica parecendo que eu que sou o Francisco Assis."

## Diagnóstico raiz

**A regra simplesmente NÃO EXISTIA em nenhuma versão do prompt do agente comentarista.** Não era uma regra malfeita a corrigir — era uma lacuna a preencher.

A única lógica de "autor" que existia era um **filtro de skip** (não responder aos comentários escritos *pelo próprio* Miguel, `gsn_agente_comentarista.py:829-832`) — mas isso **não detecta** quando um *terceiro* (ex.: Mozart Dias) dirige o comentário *ao* Miguel. É exatamente essa lacuna que causou o bug.

O prompt que falhava (GSN, antes):
```python
f"Um usuário chamado {autor_alvo} fez o seguinte comentário (é a este que você deve responder diretamente):\n\"{comentario_alvo}\"\n\n"
```
Mandava a persona responder "diretamente", sem nenhum aviso de que o comentário podia estar dirigido ao autor. O LLM lia *"você é de Fortaleza?"* e respondia naturalmente na 1ª pessoa.

## A regra criada

Inserido um bloco `bloco_regra_autor` no prompt (logo depois do comentário-alvo, para o LLM ler imediatamente):

> ⚠️ REGRA CRÍTICA SOBRE O AUTOR DO SITE: O autor deste site é Miguel do Rosário. Você NÃO é o autor — você é um leitor/persona independente. Se o comentário acima estiver dirigido AO AUTOR (pergunta direta, elogio ao autor, "meu amigo, você...", referência à biografia/obra dele, pergunta geográfica/pessoal), você está PROIBIDO de responder na primeira pessoa como se a pergunta fosse com você. NUNCA use "eu" para confirmar, negar ou completar algo que disseram AO AUTOR. Responda como um terceiro leitor observando a conversa (ex.: "o Miguel é de Fortaleza sim"), falando DO autor como outra pessoa.

**Comportamento escolhido pelo Miguel:** a persona PODE responder, mas **nunca na 1ª pessoa do autor** — responde como leitor terceiro. (Não optou pelo SKIP automático.)

## Onde foi aplicado (3 arquivos ativos)

| # | Arquivo | Função | Status |
|---|---|---|---|
| 1 ⭐ | `cerebro-miguel/global_south_news/root/gsn_agente_comentarista.py` | `gerar_resposta` (linhas ~231-249) | ✅ `py_compile` OK |
| 2 | `Dados_Frios/Agentes Labs/agente_comentarista.py` | `gerar_resposta` | ✅ `py_compile` OK |
| 3 | `Downloads/Antigravity Google/.codex_work/agente_comentarista_v4.py` | `generate_text` (bloco `if parent:`) | ✅ `py_compile` OK |

⭐ = produção GSN, onde a persona Chico/Francisco de Assis é usada de fato.

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- ✅ **O que aconteceu:** regra criada e aplicada nos 3 arquivos; todos compilam sem erro.
- ⏳ **O que falta:** teste real — provocar um comentário dirigido ao autor e confirmar que a persona agora responde em 3ª pessoa (ou pelo menos nunca assume o "eu" do autor). Reforço opcional no `system_prompt` da persona no JSON `gsn_personas_comentarios.json`.
- 🙋 **O que preciso de você:** confirmar se o comportamento escolhido (responder em 3ª pessoa, não SKIP) está bom na prática, ou se prefere migrar pra SKIP automático quando o comentário for claramente dirigido ao autor.

## Decisões tomadas nesta sessão

1. **Comportamento:** responder em 3ª pessoa (proibido 1ª pessoa do autor) — **não** SKIP automático. (Escolha Miguel via AskUserQuestion.)
2. **Escopo:** aplicar nos 3 arquivos ativos (GSN + Agentes Labs + v4). (Escolha Miguel via AskUserQuestion.)

## Referências cruzadas

- Transcrição de origem: `/home/migueldorosario/Recordings/transcricoes/20260810_171707_Clip_3.txt`
- Memória técnica completa (log): `Memorias/memoria_comentarista_regra_autor_primeira_pessoa_20260810.md`
- Fóruns irmãos do comentarista: `forum_comentarista_v4_reativamento_30min_humanizado_20260802.md`, `forum_vazamento_deepseek_comentarista_v4flash_ativo_20260802.md`, `forum_comentarista_v4_20260719.md`, `forum_reforma_comentaristas_20260523.md`
