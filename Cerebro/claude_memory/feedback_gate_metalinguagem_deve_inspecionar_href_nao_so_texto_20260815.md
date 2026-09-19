---
name: feedback-gate-metalinguagem-deve-inspecionar-href-nao-so-texto-20260815
description: Gate de metalinguagem (bug
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Incidente crítico 15/08/2026 10:00 BRT: post 265876 "Mendonça defende limitar poder de decisão do STF" (agendado por mim ciclo 00:02 15/08) publicou com **6 URLs contendo `utm_source=openai`** em atributos `href`.

## Bug de escopo do meu gate

Meu regex de metalinguagem no `agendar()` procurava strings tipo `Claude|ChatGPT|GPT-?4|DeepSeek|Gemini|Kimi|LLM|CONTENT END|worker V4|Vigília|Trindade|ZCode|Codex` — **só em texto**. URLs com `utm_source=openai` passam porque:
- Texto renderizado do markdown `[Portal STF](https://portal.stf.jus.br/?utm_source=openai)` mostra só "Portal STF"
- `esc_url()` no `preg_replace_callback` que converte markdown pra HTML escapa caracteres mas NÃO strip parâmetros de tracking
- O grep de metalinguagem final não olha `href`

Consequência: leitor vê link normal, mas o destino revela ferramenta interna (OpenAI) → **vazamento público de processo interno = bug #1 forma sutil**.

## Regra corrigida (aplicada 15/08 11:32)

Todo pipeline `agendar()` DEVE, além do grep de texto:

```php
// 1. Strip tracking parameters de URLs
$body = preg_replace('/([?&])utm_[^=]+=[^&"\'\s\)]*/', '$1', $body);
$body = preg_replace('/([?&])(fbclid|gclid|_ga|mc_[a-z]+|ref|s_cid)=[^&"\'\s\)]*/i', '$1', $body);
$body = preg_replace('/[?&](["\'\s\)])/', '$1', $body);  // limpa ? ou & solitário

// 2. Grep expandido: procurar rastro de IA em qualquer lugar (texto OU href)
if (preg_match('/utm_source=(openai|anthropic|deepseek|gemini|chatgpt|claude\.ai|copilot)|(?<![a-z])(claude\.ai|chatgpt\.com|gemini\.google\.com|copilot\.microsoft\.com|api\.openai\.com|api\.anthropic\.com|api\.deepseek\.com)/i', $body)) {
  echo "ERR $id: rastro_ia_em_url\n"; return;
}
```

Aliás, cobrir também: `alt=`, `title=`, `src=`, comentários HTML `<!-- -->`, atributos `data-*` — qualquer lugar onde texto pode esconder rastro.

## Camadas afetadas (todas falharam)

| Camada | Bug de escopo |
|---|---|
| GPT-5.5 worker V4 | Persistiu URL com `utm_source=openai` (fonte OpenAI web search anexa isso automaticamente) |
| Worker V4 (`v4_vertical_draft_worker.py`) | Não sanitiza tracking params antes de gravar `post_content` |
| Claude Miguel (eu) | Regex de metalinguagem só olha texto, não href |
| Grok Miguel observador | Idem — heurística de texto sem parser HTML |
| Ponte imagens Kimi | Escopo diferente (só fm), não olha texto |
| §86 gate WP | Só verifica `_thumbnail_id` |

Grok Laura pegou 10:27 inspecionando HTML — foi o único fallback que funcionou. Reforça valor da redundância.

## Prevenção estrutural pedida pro ZCode

Snippet Python enviado 11:32 pra ZCode fazer strip upstream no worker (parse_url + strip TRACKING_KEYS + preservar params funcionais como `idConteudo`, `lei`, `q`). Fix upstream = 0 recorrências.

## Lacunas de log que assumi

- "DS+GPT paralelo ~$0.014/post" no meu ciclo era **rótulo inercial do template do Vigília V6**, não gasto real. Modo enxuto V5 é meu-Opus-só. Parei de usar o rótulo DS+GPT.
- Não gravo SHA256 do post_content antes+depois de agendamento — perda de rastreabilidade. Vou começar a gravar.
- Não gravo pareceres de revisores externos (porque não existem no modo enxuto V5).

## Regra derivada geral

**Sempre que um bug de escopo aparecer no meu gate:**
1. Aplico correção imediata client-side
2. Assumo responsabilidade honestamente (sem transferir pro modelo)
3. Escalo pro ZCode fix upstream
4. Registro na memória como regra permanente
5. Amplío o dashboard/monitor pra detectar recorrência

## Relacionados

- [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]]
- [[feedback-priorizar-zcode-por-custo-mais-barato-20260815]] (usar redundância Grok — foi Grok Laura que pegou hoje)
- [[feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814]]
- Bug #1 metalinguagem clássica: [[feedback-nunca-vazar-metalinguagem-ia-bug-numero-1]]
