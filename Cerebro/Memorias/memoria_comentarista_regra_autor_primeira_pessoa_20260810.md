# MEMÓRIA — Regra do AUTOR no agente comentarista (log técnico completo)

**Data:** 2026-08-10 (~18:00 BRT)
**Agente:** ZCode — GLM-5.2 (Z.ai coding plan) — Kimi/Qwen esgotados 🔴🔴
 **Conversa:** "Bug do comentarista respondendo na 1ª pessoa do autor"
**Origem:** ordem do Miguel (transcrição `20260810_171707_Clip_3.txt`, 17:17 BRT)
 **Estado:** ✅ aplicado + compilado. Pendência: teste real.

> Esta memória é o log técnico da missão. O Fórum resumido está em
> `Foruns/forum_comentarista_regra_autor_primeira_pessoa_20260810.md`.

---

## 1. Contexto e gatilho

Ordem do Miguel (voz, transcrição `20260810_171707_Clip_3.txt`): a persona **Francisco de Assis (Chico)** respondeu em primeira pessoa a um comentário do leitor **Mozart Dias** que, na verdade, estava dirigido ao **autor** (Miguel do Rosário) — dando a impressão de que o Miguel e o Francisco de Assis são a mesma pessoa. Miguel pediu para corrigir a regra no prompt do agente comentarista.

## 2. Investigação

Agente Explore vasculhou os 3 ambientes (ZCodeProject, Antigravity Google, cerebro-miguel + Dados_Frios). Achado crítico: **a regra que o Miguel queria "corrigir" não existia** — era uma lacuna, não um erro de redação. Os prompts atuais não distinguiam "comentário dirigido ao autor" de "comentário dirigido ao comentarista" e não tratavam pessoa gramatical.

### Arquivos ativos localizados (NÃO legacy/backup)

1. `/home/migueldorosario/cerebro-miguel/global_south_news/root/gsn_agente_comentarista.py` (914 linhas) — **produção GSN**, onde Chico/Francisco de Assis é usada.
2. `/home/migueldorosario/Dados_Frios/Agentes Labs/agente_comentarista.py` — standalone "Agentes Labs".
3. `/home/migueldorosario/Downloads/Antigravity Google/.codex_work/agente_comentarista_v4.py` — variante limpa/renovada (usa `generate_text`).

Dezenas de cópias legacy/backup (`legacy/`, `Backups/`, `.bak_pre_*`) foram ignoradas — não editar.

### Ponto exato do bug

GSN `gerar_resposta`, prompt_usuario (linhas ~231-238 antes da edição):
```python
prompt_usuario = (
    f"Você está num blog, no artigo intitulado '{titulo_post}'.\n"
    f"{bloco_thread}"
    f"Um usuário chamado {autor_alvo} fez o seguinte comentário (é a este que você deve responder diretamente):\n\"{comentario_alvo}\"\n\n"
    f"{estilo_tamanho}, baseada 100% na sua personalidade restrita. "
    ...
)
```
Sem instrução nenhuma sobre autor/pessoa gramatical.

### Lógica de "autor" que já existia (e por que não bastava)

GSN linhas 829-832 — só um filtro de **skip** (não responder comentários *escritos pelo próprio* Miguel):
```python
if c_author in nomes_personas:
    continue
if c_author.lower() in ["miguel", "miguel do rosário", "redator", "redator2"]:
    continue
```
Não cobre o caso "terceiro dirige comentário AO Miguel" — a lacuna.

## 3. Decisões do Miguel (via AskUserQuestion)

1. **Comportamento quando o comentário é dirigido ao autor:** opção escolhida = **"Responder, mas nunca na 1ª pessoa do autor"** (persona responde como leitor terceiro; proibido usar "eu" pra confirmar algo dito ao autor). NÃO escolheu SKIP automático.
2. **Escopo:** aplicar nos 3 arquivos (GSN + Agentes Labs + v4).

## 4. Backup pré-edição

Não foi feito `.bak` pois a edição é aditiva (inserção de um bloco, sem remover código funcional). Os 3 arquivos originais estão em git history dos respectivos repositórios (cerebro-miguel, Dados_Frios, Antigravity Google). Se necessário, trecho original preservado no Fórum (seção "O prompt que falhava").

## 5. Edição aplicada

### GSN (produção) + Agentes Labs — mesma estrutura

Inserido bloco `bloco_regra_autor` entre `bloco_thread` e `prompt_usuario`, e referenciado no `prompt_usuario` logo após o `{comentario_alvo}`:

```python
    # REGRA DO AUTOR (correção Miguel 10/08/2026): quando um leitor dirige o comentário
    # ao AUTOR do site (Miguel do Rosário) e não ao comentarista persona, a persona
    # NÃO pode responder na primeira pessoa assumindo que falaram com ela — senão fica
    # parecendo que a persona É o autor (bug real: persona Chico/Francisco de Assis
    # respondeu "eu não conheço o Ceará" a um comentário que falava COM o Miguel).
    bloco_regra_autor = (
        f"\n⚠️ REGRA CRÍTICA SOBRE O AUTOR DO SITE:\n"
        f"O autor deste site é Miguel do Rosário. Você NÃO é o autor — você é um leitor/persona independente.\n"
        f"Se o comentário acima estiver dirigido AO AUTOR (ex.: pergunta direta a ele, elogio ao autor, "
        f"tratamento por \"meu amigo, você...\", referência à biografia/obra dele, pergunta geográfica/pessoal), "
        f"você está PROIBIDO de responder na primeira pessoa como se a pergunta fosse com você.\n"
        f"NUNCA use \"eu\" para confirmar, negar ou completar algo que disseram AO AUTOR. "
        f"Responda sempre como um terceiro leitor observando a conversa (ex.: \"o Miguel é de Fortaleza sim\", "
        f"\"o autor tratou disso no texto\"), falando DO autor como outra pessoa — nunca assuma que falaram com você.\n"
    )
```

E no `prompt_usuario`, a linha do comentário-alvo virou:
```python
        f"Um usuário chamado {autor_alvo} fez o seguinte comentário (é a este que você deve responder diretamente):\n\"{comentario_alvo}\"\n"
        f"{bloco_regra_autor}\n"
```

### v4 (.codex_work) — estrutura diferente (prompt inline, sem variável separável)

Regra inserida inline na string do bloco `if parent:`, logo após a instrução de estilo, antes de MATÉRIA/RESUMO/COMENTÁRIO:
```python
            "⚠️ REGRA CRÍTICA SOBRE O AUTOR DO SITE: o autor deste portal é Miguel do Rosário. "
            "Você NÃO é o autor — é um leitor/persona independente. Se o comentário abaixo estiver "
            "dirigido AO AUTOR (pergunta direta a ele, elogio ao autor, \"meu amigo, você...\", "
            "referência à biografia/obra dele, pergunta geográfica/pessoal), está PROIBIDO de responder "
            "na primeira pessoa como se a pergunta fosse com você. NUNCA use \"eu\" para confirmar, negar "
            "ou completar algo que disseram AO AUTOR. Responda como um terceiro leitor observando a "
            "conversa (ex.: \"o Miguel é de Fortaleza sim\"), falando DO autor como outra pessoa.\n\n"
```

## 6. Validação

```bash
python3 -m py_compile gsn_agente_comentarista.py      → OK
python3 -m py_compile "Agentes Labs/agente_comentarista.py" → OK
python3 -m py_compile agente_comentarista_v4.py        → OK
```
Os 3 compilam sem erro de sintaxe. (Não há teste de integração automatizado para o agente comentarista — validação final depende de execução real com LLM.)

## 7. O que falta / próximos passos

- **Teste real:** provocar um comentário dirigido ao autor num ambiente de teste e confirmar que a persona responde em 3ª pessoa (ou nunca assume o "eu" do autor). Caso o LLM ainda escape para a 1ª pessoa, reforço opcional: adicionar a mesma regra ao `system_prompt` da persona no JSON `gsn_personas_comentarios.json` (riocarta → esquerda → Chico, e demais personas).
- **Considerar SKIP automático** se o comportamento "responder em 3ª pessoa" ainda gerar ruído — opção descartada pelo Miguel nesta sessão, mas disponível.
- **Catálogo:** Fórum+Memória catalogados no NODO do comentarista + `CEREBRO_NODE_ATUALIZACOES.md` (feito abaixo).

## 8. Lições

- **Assumir "corrigir" quando o problema é "criar":** o Miguel pediu "corrigir isso no prompt" presumindo que a regra existia e estava errada. A investigação mostrou que a regra **não existia** — era uma lacuna. Sempre validar a premissa antes de editar.
- **Lacuna de detecção vs. filtro:** o filtro de skip existente (linhas 829-832) tratava "autor como EMITENTE do comentário", mas não "autor como DESTINATÁRIO do comentário" — são dois fluxos distintos e só um estava coberto.
