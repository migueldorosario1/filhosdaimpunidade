---
name: Fix branch deepseek faltante no agente_roteador_llm 2026-04-25
description: `_gerar_texto_interno` não tinha branch para provider="deepseek". Cadeia do comentarista listava deepseek primary mas caía silenciosamente em Gemini. Adicionado branch espelhando padrão openai. Smoke test OK. Economia esperada -57% no comentarista (~US$ 2/dia).
type: project
originSessionId: 3fe330c3-19fc-40ae-a8cb-5d6a13d594a3
---
## Bug

Em `agente_roteador_llm.py:29-92`, a função `decidir_ordem_ias("comentario_site")` retornava cadeia:
```
[deepseek-chat, gemini-flash-latest, gpt-4o-mini]
```

Mas o for loop em `_gerar_texto_interno` (linhas 145-291) só tinha branches pra `openai`, `gemini`, `xai`, `anthropic`, `mistral` — **sem `deepseek`**. Resultado: ao tentar `deepseek-chat` o for não fazia nada, caía no `except` silenciosamente, e seguia pro `gemini-flash-latest`.

Confirmação no log do comentarista:
```
🔄 Acionando Modelo >>> [DEEPSEEK - deepseek-chat]   ← não tem branch, pula
🔄 Acionando Modelo >>> [GEMINI - gemini-flash-latest] ← respondia tudo
```

100% das chamadas do comentarista hoje passaram pelo Gemini. Segundo gerenciador_tokens, isso vinha do dia 20-21/04 pelo menos.

## Fix

Adicionado branch `elif provider == "deepseek":` antes do `except` em `_gerar_texto_interno`. Espelha padrão da openai (mesmo SDK, base_url DeepSeek).

```python
elif provider == "deepseek":
    import openai
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key: raise Exception("Sem Chave DeepSeek")
    cli = openai.OpenAI(api_key=key, base_url="https://api.deepseek.com")
    kwargs = {
        "model": modelo,
        "messages": [{"role":"system","content":sys_prompt}, {"role":"user","content":prompt}],
        "temperature": temperature,
    }
    if max_tokens: kwargs["max_tokens"] = max_tokens
    resp = cli.chat.completions.create(**kwargs, timeout=60)
    if gerenciador_tokens and hasattr(resp, 'usage') and resp.usage:
        gerenciador_tokens.registrar_gasto(agente_nome, modelo, resp.usage.prompt_tokens, resp.usage.completion_tokens, contexto=contexto)
    txt = resp.choices[0].message.content
    if txt:
        log(f"✅ Texto entregue com maestria por {modelo} (DeepSeek)!")
        return txt, modelo
```

## Smoke test

```
Sequência de Ataque Definida: ['deepseek-chat', 'gemini-flash-latest', 'gpt-4o-mini-2024-07-18']
🔄 Acionando Modelo >>> [DEEPSEEK - deepseek-chat]
✅ Texto entregue com maestria por deepseek-chat (DeepSeek)!
TEXTO: "Porque é nesse bloco que o Brasil encontra aliados para reformar a ordem global..."
```

DeepSeek respondeu direto. Sem fallback.

## Deploy

- **Local canônico:** `Projeto Cafezinho Agentes/root/agente_roteador_llm.py`
- **Backup local:** `agente_roteador_llm.py.bkp-pre-deepseek-fix-20260425_0841`
- **Backup Tencent:** `/root/agente_roteador_llm.py.bkp-pre-deepseek-fix-20260425_0841`
- **MD5 deployado (idêntico em 3 lugares):** `b0b3972a25c34f1e7a044307157cb4ee`
- **MD5 antes do fix:** `6924d909c9853248806692d812f7a0a0`

## Impacto esperado

Tabela de preços `gerenciador_tokens.py:59-72`:
| Modelo | Input/1M | Output/1M | Custo médio comentário (1248 in + 109 out) |
|---|---|---|---|
| gemini-flash-latest (antes) | — | — | $0.000990 (medido real) |
| **deepseek-chat (agora)** | **$0.27** | **$1.10** | **$0.000457** (-54%) |

**Custo do comentarista:** US$ 3.86/dia → **~US$ 1.66/dia** (economia ~US$ 2.20/dia, -57%).

Beneficia também `comentario_site_resposta` (mesma cadeia) e qualquer outro caller futuro que use contextos com deepseek primary.

## Rollback (se necessário)

```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  'sudo cp /root/agente_roteador_llm.py.bkp-pre-deepseek-fix-20260425_0841 /root/agente_roteador_llm.py'
cp "Projeto Cafezinho Agentes/root/agente_roteador_llm.py.bkp-pre-deepseek-fix-20260425_0841" \
   "Projeto Cafezinho Agentes/root/agente_roteador_llm.py"
```
