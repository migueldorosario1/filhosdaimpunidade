---
name: feedback-lab-visual-anotar-bugs-seguranca-port-canonico
description: Anotar TODO bug do espelho cafezinho.news em Cerebro/monitoramento_horario/lab_visual_bugs/bugs_YYYY-MM-DD.jsonl. Objetivo é port seguro pro canônico. Miguel 11/08 05:46 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

**Todo bug identificado no espelho `cafezinho.news` durante a reforma visual deve ser anotado** em `Cerebro/monitoramento_horario/lab_visual_bugs/bugs_YYYY-MM-DD.jsonl`. Objetivo declarado por Miguel: **fazer com muita segurança no espelho, sem ruídos, pra levar a mudança pro canônico ocafezinho.com quando decidir o momento**.

**Why:** Miguel 11/08 05:46 BRT: "sobre a reforma visual, eu quero que voce anote qq bug que aparecer, pq o objetivo é fazer com muita segurança no espelho, sem ruidos, para poder levar a mudança para o canonico quando decidirmos que é o momento."

**Estrutura do JSONL (schema):**

```json
{
  "ts": "ISO-8601 com timezone",
  "bug_id": "LV-YYYYMMDD-NNN",
  "escopo": "espelho_cafezinho.news | canonico_ocafezinho.com | ambos",
  "severidade": "baixa | media | alta | critica",
  "origem": "reforma_visual_20260811 | pre_existente | worker_v4 | plugin_wp | infra",
  "titulo": "resumo 1 linha",
  "descricao": "detalhado, o que acontece",
  "impacto": "como afeta usuário/editor",
  "hipotese_causa": "análise possível",
  "reproducao": "comando/URL exato",
  "correcao_proposta": "passos numerados",
  "prioridade_correcao": "baixa | media | alta | critica",
  "detectado_em_ciclo": "identificador",
  "arquivos_afetados": ["path1", "path2"],
  "corrigido": false,
  "corrigido_em": null,
  "correcao_aplicada": null
}
```

**Quando anotar:**

- **Detecção proativa** — auditoria de rotina (PHP lint, HTTP status, grep em logs) revela algo estranho
- **Detecção reativa** — Miguel aponta comportamento errado; ou algum ciclo Vigília notou (ex: post não renderiza)
- **Bug herdado do canônico** — sync trouxe algo do canônico que quebrou; anotar mesmo se não é da reforma visual (pra não portar bug de volta)

**Categorias de bug pra rastrear especialmente:**

1. **PHP fatal/warning/notice** — qualquer erro no lint ou log PHP-FPM
2. **HTTP 4xx/5xx** — erros de renderização em URLs canônicas (home, single, categoria, arquivo, tag, busca, autor, feed)
3. **CSS quebrado** — layout errado em algum breakpoint (mobile, iPad vertical, iPad horizontal, desktop)
4. **JS erros** — Uncaught, TypeError, undefined
5. **Cache/CDN** — mudança não aparece após deploy (bug de invalidação)
6. **Rewrite rules** — categoria/tag/arquivo retornando 404 ou 301 pra lugar errado
7. **Ads posicionamento** — slot renderiza mas visualmente quebra layout
8. **Regressão** — algo que funcionava parou de funcionar

**Auditoria mínima obrigatória após CADA mudança no lab visual:**

```bash
# 1. PHP lint em todos arquivos do tema e mu-plugins
for f in $THEME/*.php $THEME/includes/*.php $THEME/ad/*.php $MU/*.php; do
    php -l "$f"
done

# 2. HTTP status: home + 1 single + 1 categoria + 1 tag
curl -sI (com Basic Auth) — verificar 200

# 3. Grep em logs: nginx error + PHP-FPM error + WP debug (se existir)

# 4. Render structural: garantir que blocos essenciais aparecem no HTML
```

**Se auditoria acha bug NOVO** → registrar no JSONL do dia. Se bug PRÉ-EXISTENTE ao lab visual, marcar `origem: pre_existente` (não é falha da reforma, mas fica registrado pra não portar pro canônico).

**Como aplicar no port pro canônico (futuro):**

Antes de portar cada mudança do espelho pro canônico, consultar `lab_visual_bugs/*.jsonl` e:
- Verificar se algum bug relacionado ao arquivo/feature portado está aberto (`corrigido: false`)
- Se sim, ou corrigir no espelho primeiro OU documentar que canônico também vai receber (aceito)
- Nunca portar mudança que tem bug documentado sem plano explícito

**Primeiro bug registrado (11/08 05:47 BRT):** `LV-20260811-001` — URLs de categoria retornando 404 ou 301 pra posts com slug idêntico no espelho. Comportamento pré-existente (não é da reforma visual), mas registrado pra checar se canônico tem o mesmo antes de portar.

Regras irmãs: [[project-lab-visual-cafezinho-news-20260811]] · [[feedback-canonico-port-do-espelho-cirurgico]] · [[feedback-modo-enxuto-preservar-worker-v4]]
