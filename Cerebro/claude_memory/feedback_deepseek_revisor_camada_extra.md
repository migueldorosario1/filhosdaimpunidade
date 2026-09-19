---
name: feedback-deepseek-revisor-camada-extra
description: "Camada extra de revisão editorial via DeepSeek V4 Flash antes de publish V4. Miguel 2026-08-03 13:56 BRT — objetivo é 2ª opinião automatizada, não substitui minha checagem."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9ff9d002-2c71-4670-87db-7c5f55616550
---

**Regra:** Em cada ciclo Vigília V5 (DIA e NOITE), ANTES de aplicar meus fixes e publish, chamar `deepseek_revisor.call_revisor(titulo, corpo, vertical)` pra receber JSON estruturado com bugs detectados.

**Motivação:** Miguel apontou (03/08 12:53 e 13:56 BRT) que estou passando bugs semânticos/editoriais recorrentes ("Lulinha porreta", "Irã alerta Israel" invertido, "Irã ataca Patriot" sem sentido, "Segundo o Folha" em 33 posts). Camada extra dobra a chance de pegar.

**Script:** `/home/migueldorosario/ferramentas/sentinela/deepseek_revisor.py`

**Modelo:** `deepseek-v4-flash` (endpoint `https://api.deepseek.com/v1/chat/completions`).

**Chave:** `DEEPSEEK_API_KEY` em `.env` do workspace (não colar literal em fórum/memória — regra `feedback_nunca_chave_literal_em_forum`).

**Custo real medido (03/08 smoke):** ~US$ 0.00054/call = ~R$ 0.003/post = **R$ 0.09/dia** pra 30 posts. R$ 2.70/mês. Desprezível.

**Formato de resposta (JSON):**
```json
{
  "titulo_ok": bool,
  "titulo_sugestao": str | null,
  "bugs_titulo": [str],
  "bugs_corpo": [str],
  "bugs_factuais_potenciais": [str],
  "gramatica_estilo": [str],
  "peso_editorial": "alto" | "medio" | "baixo",
  "risco_duplicata": bool,
  "recomendacao": "publicar" | "publicar_com_ajustes" | "pending" | "descartar",
  "resumo_curto": str,
  "_usage": {...},
  "_model": "deepseek-v4-flash"
}
```

**Como aplicar no ciclo:**
1. Puxar draft V4 (autor 5786, <2h) via `wp_get`.
2. Chamar `call_revisor(titulo, corpo, vertical)` — retorno em <10s tipicamente.
3. Consolidar bugs (DeepSeek + minha checagem própria).
4. Se `recomendacao == "pending"` OU eu detecto bug irrecuperável → `status=pending`.
5. Se `recomendacao == "descartar"` → `status=trash` (raro, exige justificativa).
6. Aplicar fixes recomendados (título/corpo).
7. Rodar WebSearch em `bugs_factuais_potenciais` pra confirmar antes de aceitar sugestão.
8. Backup SHA-256 + publish + log JSONL com o que o DeepSeek pegou vs o que eu peguei separadamente.

**Divisão de trabalho:**
- **DeepSeek:** semântica/regência/gênero fonte/CAPS/ponto-e-vírgula/nomes minúsculos/HTML/ruído template/entidades HTML/placeholders — coisas objetivas de padrão.
- **Eu (Claude):** WebSearch factual (autoridades cutoff, datas específicas, números), peso editorial contextual, decisão final (pending/publish), consolidação com regras vigentes do Cafezinho.

**Prompt do sistema** (guardado no script): revisor editorial Cafezinho, foco em bugs que Miguel pegaria (semântica de título, regência, gênero, siglas), listagem completa de fontes fem/masc + autoridades atuais + regras editoriais Cafezinho.

**Casos-teste de validação (03/08 13:56 BRT):**
- Bugado ("Milei ataca Lula de 'ladrão' de novo; ...") → DeepSeek detectou regência errada, `;` proibido, fonte CAPS, gênero fem, caps pós-vírgula, sugeriu título corrigido "Milei chama Lula de 'ladrão' de novo — Brasil convoca embaixador".
- OK ("Xi Jinping consolida poder no Exército Chinês") → DeepSeek marcou publicar, sinalizou risco_duplicata (cauteloso), peso alto.

**Limites conhecidos:**
- DeepSeek Flash tem knowledge cutoff — não confia em fatos recentes. Sempre WebSearch em cima quando ele aponta `bugs_factuais_potenciais`.
- Se DeepSeek falha (timeout/500), publish segue com apenas minha checagem — não bloqueia (script retorna `{"error": ...}` em vez de raise).
- Truncamento em 6000 chars de corpo pra economizar tokens (posts YT longos podem cortar contexto).

**Regras irmãs:** [[feedback-checagem-titulo-semantica-e-genero-fonte]], [[feedback-checagem-dupla-editorial-com-autonomia]], [[feedback-smoke-de-api-precisa-chamada-real-de-centavos]], [[feedback-nunca-chave-literal-em-forum]].
