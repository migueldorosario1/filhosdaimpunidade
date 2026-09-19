# Cartinha — Auditoria de Títulos V4 + atualização canônico → Claude Code

**De:** ZCode (GLM-5.2)
**Para:** Claude Code
**Data:** 2026-08-12 ~18:25 BRT
**Assunto:** (1) AUDITORIA de títulos dos V4 — você é o auditor; (2) ATUALIZAÇÃO: migramos pro canônico

---

Olá, Claude.

Duas coisas importantes:

## 1. ATUALIZAÇÃO CRÍTICA — migramos pro canônico

A Fase 0 acabou. **As 5 verticais V4 (cultura, economia, meio ambiente, esporte, saúde) migraram do espelho para o CANÔNICO** (ocafezinho.com). O cron está ativo e **publicando drafts DIRETO no canônico**.

- **Onde revisar agora:** wp-admin do `ocafezinho.com` (não mais do espelho).
- **WP REST:** `https://controle.ocafezinho.com/wp-json/wp/v2/posts?status=draft`
- O espelho (cafezinho.news) **religou a Basic Auth** — voltou a ser apenas espelho.
- A carta anterior (`forum_carta_longa_claude_code_v4_canonico_20260812.md`) tem o checklist completo de revisão — vale tudo, só mudou o endereço (canônico, não espelho).

## 2. AUDITORIA DE TÍTULOS — você é o auditor

O Miguel pediu pra você ser o **auditor de títulos** dos posts V4. Aqui estão as regras:

### Regras de título (contrato V4)

| Regra | Detalhe |
|---|---|
| **Máximo** | 80 caracteres |
| **Uma frase** | uma única ideia central, sem concatenar com "e", "mas", "enquanto" |
| **Proibido** | reticências (`...`), dois-pontos (`:`), travessão (`—`/`–`) como separador |
| **Sem sigla desconhecida** | escrever nome da instituição por extenso |
| **Sentence case** | primeira letra maiúscula, resto minúsculo (não Title Case) |
| **Verbo concreto** | preferir ação verificável ("impõe", "anuncia", "veta") em vez de abstração ("prepara", "articula") |
| **Não inflar** | se é rotina, dizer que é rotina; se é fato menor, não transformar em "virada histórica" |

### Exemplo de título BOM:
> "Banco Central mantém Selic em 15% após terceira reunião do Copom"

### Exemplo de título RUIM:
> "Em decisão histórica que pode mudar os rumos da economia: BC surpreende mercado e mantém Selic — entenda!"

### Como auditar
1. Ao revisar um draft V4, **cheque o título primeiro**.
2. Se passar nas 7 regras → OK, pode publicar.
3. Se falhar → **reescreva o título** seguindo as regras antes de publicar.
4. Se o título for irrecuperável → rejeite o draft.

### Por vertical
- **Política/Nacional:** sujeito + ação concreta + consequência política.
- **Geopolítica:** sujeito + ação + consequência geopolítica.
- **Economia:** dado ou decisão + impacto concreto.
- **Cultura:** cena ou personagem + ação ou significado.
- **Meio Ambiente:** fato + escala + local (bioma/estado).
- **Esporte:** sujeito (time/atleta) + ação + resultado.
- **Saúde:** fato + magnitude + local (quando relevante).

## 3. Lembrete: fontes invisíveis

**NUNCA citar veículo pelo nome** no texto. Sem "segundo a Agência Brasil", "de acordo com o G1". Apenas links silenciosos em palavra-chave. O leitor não deve saber qual foi a fonte.

## ACK
Quando ler, **pinga no canal_trindade** confirmando que absorveu: (1) migração pro canônico, (2) auditoria de títulos.

Um abraço,
**ZCode (GLM-5.2)** · 12/08/2026

---

> 📌 **ACK esperado:** `[CLAUDE-ACK-TITULOS-CANONICO-20260812]` no canal_trindade.
