---
name: Toda mensagem dos 3 agentes (Claude, Codex, Antigravity) inclui bloco copy-paste com paths absolutos
description: Regra de comunicação ampliada 2026-05-02 11:00 BRT. Todos os 3 agentes terminam suas mensagens técnicas com bloco que Miguel pode copiar inteiro pra repassar pros outros agentes.
type: feedback
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
Toda mensagem técnica de **qualquer um dos 3 agentes** (Claude, Codex, Antigravity) que envolva coordenação multi-agente deve terminar com uma seção:

```
## 📋 Pra colar pro [outros agentes]
> [conteúdo da mensagem em 2ª pessoa, paths absolutos, ações esperadas]
> — [autor]
```

**Why:** Miguel pediu 2026-05-02 10:54 BRT (regra inicial só pra Claude) e ampliou 2026-05-02 11:00 BRT (universal pros 3 agentes). Razão: Antigravity já violou 3x esta semana postando em path errado por confiar em referência relativa cacheada. Solução: cada agente fornece o path absoluto explícito pra Miguel poder repassar sem ambiguidade.

**How to apply:**

### Claude Code (eu)
- Sempre que minha resposta envolver coordenação com Antigravity/Codex: incluir bloco no fim.
- Endereçar "Antigravity, Codex,..."
- Path absoluto SEMPRE (canal, fórum, memória).
- Path negativo (subpasta zumbi) explícito quando relevante.

### Codex
- Sempre que postar parecer técnico no fórum/canal: incluir bloco copiável apontando pra fórum/memória + ação esperada.
- Endereçar "Claude, Antigravity, Miguel,..."

### Antigravity
- Sempre que postar parecer/diagnóstico no fórum/canal: incluir bloco copiável apontando pra fórum/memória + ação esperada.
- Endereçar "Claude, Codex, Miguel,..."

### Template canônico

```markdown
## 📋 Pra colar pro [Antigravity / Codex / outros]

> [Endereçar agentes específicos],
>
> [Resumo curto do que foi feito/proposto/perguntado]
>
> 📁 Canal canônico: `/home/migueldorosario/Downloads/Antigravity Google/Foruns/canal_claude_antigravity.md`
> 📁 Fórum vivo: `/home/migueldorosario/Downloads/Antigravity Google/Foruns/<nome>.md`
> 📁 Memória [(Claude|Antigravity|Codex)]: <path absoluto>
>
> ❌ NÃO usar `Projeto Cafezinho Agentes/Foruns/` — subpasta zumbi apagada 01/05 12:36.
>
> [Pergunta concreta ou ação esperada]
>
> — [Autor REAL da mensagem — quem realmente escreveu: Claude Code, Codex ou Antigravity. NUNCA "Miguel" — ele só intermedia/cola, não é o autor do conteúdo técnico.]
```

⚠️ **Erro corrigido 2026-05-02 11:08 BRT:** anteriormente eu estava assinando os blocos copy-paste como "— Miguel" (porque o bloco é pro Miguel colar). Miguel corrigiu: a assinatura deve ser do **autor real** (eu, Claude Code), pois o bloco é uma mensagem MINHA que o Miguel só repassa. Mesma regra vale pra Codex e Antigravity quando eles usam o template — assinam o nome deles, não Miguel.

⚠️ **Papéis dentro do bloco — CRÍTICO (2026-05-02 11:46 BRT):**

Cada agente endereçado dentro do bloco copy-paste deve receber instrução compatível com seu papel real, **pra não sugerir indevidamente que vão codar**:

- **Pra Antigravity, SEMPRE:** "diagnostica, propõe, atualiza trindade — **NÃO coda**". Antigravity nunca toca código de produção (precedente CLAUDE.md `/root/.env` 21/04, CLAUDE.md HEREDOC 22/04). Mesmo se ele se oferecer pra codar, devo redirecionar a tarefa pro código pra mim ou pro Codex via Miguel — nunca pedir/permitir Antigravity executar.

- **Pra Codex:** depende do contexto. Codex pode codar (já fez deploys reais — ex: hardening B/C/D em motor_publicador.py + agente_roteador_llm.py 02/05). MAS quando Antigravity já delegou explicitamente a codagem pra mim (como em "Codex/Claude vão fazer X — vai!"), **devo pedir só investigação/parecer/atualização de trindade ao Codex** pra evitar duplicação de deploy. Não há sentido dois agentes deployarem o mesmo arquivo.

- **Pra mim (Claude Code):** sou líder técnico e codo por padrão. Quando Codex já codou, eu audito (precedência: auditoria do hardening §12 02/05).

**Como aplicar:** ao escrever cada parágrafo do bloco endereçado a outro agente, fechar com a ação esperada compatível com o papel:
  - Pro Antigravity: "...querias opinar sobre X?" / "...alguma proposta editorial?" / "...registra no fórum se vir algo." Nunca: "...podes deployar..."
  - Pro Codex (quando eu coda): "...audita o resultado quando deployar?" / "...registra parecer no fórum §X?"
  - Pro Codex (quando ele coda): "...podes deployar o fix?"

**Memórias relacionadas:**
- `feedback_foruns_diretorio_unico.md` — regra do path canônico
- `feedback_trindade_papeis.md` — papéis canal/fórum/memória
- `feedback_botar_na_linha_sem_desanimar.md` — tom firme mas construtivo
- `feedback_hierarquia_antigravity.md` — Antigravity é consultor premium, não opera infra
- `feedback_audit_antigravity_tudo.md` — auditar tudo que vem do Antigravity
