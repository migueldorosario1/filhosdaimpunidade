---
name: Footer de custo no fim de cada mensagem
description: Toda resposta do Claude termina com footer de modelo + tokens da msg + R$ da msg + R$ acumulado da sessão. Rodar scripts/cost_session.py antes de fechar.
type: feedback
originSessionId: 194b7409-a046-4f3f-8022-79c63cec32c0
---
**Regra:** TODA mensagem do Claude para Miguel termina com o footer abaixo (ou variante equivalente):

```
🤖 <Modelo> | 🪙 <Xk tokens> (essa msg) | 💵 R$ <Y> (essa msg) | 💰 R$ <Z> sessão
```

**Why:** Miguel quer visibilidade contínua de gastos por mensagem e por sessão. Sem isso, ele só descobre o consumo no fim do dia ou quando algo dispara alerta — tarde demais pra ajustar comportamento.

**How to apply:**

1. **Antes de fechar resposta:** rodar `python3 scripts/cost_session.py` (na raiz do projeto). O script lê o JSONL da sessão CC ativa, agrupa por turnos, e imprime o footer pronto pra colar.

2. **Limitação conhecida:** o JSONL só registra usage de cada chamada DEPOIS que ela termina. O **output da resposta final** (o texto que o usuário lê depois do footer) não está contabilizado quando o footer é gerado. Por isso o footer subestima ligeiramente o custo da própria mensagem — corrige no próximo turno.

3. **Acumulado da sessão = soma de todos os turnos do JSONL desta sessão CC.** Não é o total do dia (esse vem do `monitor_gastos_claude.py`).

4. **Quando NÃO incluir o footer:** mensagens triviais (1 linha) ou quando Miguel pediu explicitamente pra omitir.

5. **Atualização da cotação:** o script lê a cotação do dia em `Financas/Claude_Financas/Claude_Financas.md` (seção "Cotação USD→BRL do dia"). Se o dia atual não estiver lá, fallback é R$ 5,00/USD — nesse caso, atualizar a cotação primeiro (ver memória `feedback_orcamento_antes_e_real_depois.md`).

6. **Formato do footer:** usar emojis 🤖 🪙 💵 💰 nesta ordem. Pipes ` | ` separam os 4 campos. Tokens em formato curto (12.4k, 1.2M).

7. **Quando o script falhar:** reportar o erro e usar valores aproximados manuais. Não silenciar.
