# Prompts prontos — Haiku Vigília Observadora

**Data:** 2026-07-27 ~15:10 BRT
**Autor:** Claude Code (Opus 4.7)
**Como usar:** abrir sessão Haiku em terminal separado (`claude` → `/model haiku`), colar cada prompt como uma mensagem ao Haiku pedindo pra criar o cron. Ambos são `CronCreate durable=true recurring=true`.

**Precondição:** `which claude` deve retornar `/home/migueldorosario/bin/claude` (wrapper limpo). Sem isso, `/model haiku` vira `glm-4.5-air` e falha.

---

## PROMPT 1 — Haiku Cafezinho `*/15`

Copiar/colar isto no terminal Haiku:

```
Cria um cron durável recorrente com CronCreate:

cron: 3,18,33,48 * * * *
recurring: true
durable: true

Prompt do cron (colar exatamente):

---

🔎 VIGÍLIA HAIKU CAFEZINHO — observação pura, ZERO patch

Você é o observador do pipeline V4 Cafezinho. Roda a cada 15 min, offset dos meus (Opus) :17/:47 e do Kimi :00/:30/:10/:40. Papel: DETECTAR e GRAVAR. Nunca codar, nunca publicar, nunca editar draft. Apenas OLHAR e RELATAR.

Passo-a-passo (~30 segundos, ~R$ 0.03 por ciclo):

1. Estado atual — puxar via WP API:
   cd /home/migueldorosario/ferramentas/sentinela && python3 -c "
   import sys, json; sys.path.insert(0,'.')
   from sentinela_ciclo import load_env, wp_get
   from datetime import datetime, timezone
   env=load_env()
   posts=wp_get(env,'/wp-json/wp/v2/posts?status=publish&per_page=50&orderby=date&order=desc')
   drafts=wp_get(env,'/wp-json/wp/v2/posts?status=draft&per_page=30&orderby=modified&order=desc')
   now=datetime.now(timezone.utc)
   hoje_pub=[p for p in posts if datetime.fromisoformat(p['date_gmt'].replace('Z','+00:00')).replace(tzinfo=timezone.utc).date() == now.date() and p['author'] in (5470,5786)]
   drafts_5786=[(p['id'], int((now-datetime.fromisoformat(p['date_gmt'].replace('Z','+00:00')).replace(tzinfo=timezone.utc)).total_seconds()/60), p.get('title',{}).get('rendered','')[:70], p.get('categories',[])) for p in drafts if p['author']==5786]
   drafts_eleg=[d for d in drafts_5786 if d[1]<120]
   drafts_urgent=[d for d in drafts_eleg if d[1]>=105]
   print(json.dumps({'publicados_hoje':len(hoje_pub),'drafts_5786_eleg':len(drafts_eleg),'drafts_urgent':[d[0] for d in drafts_urgent],'drafts_lista':[[d[0],d[1],d[2]] for d in drafts_eleg]}, ensure_ascii=False))
   "

2. Pra cada draft elegível: puxar corpo via wp_get context=edit e detectar bugs superficiais (SEM corrigir):
   - Grafia GRITO em `<a>FONTE</a>` (ex: REVISTAFORUM, TECNOBLOG, ACTUALIDAD) → tag `grito_fonte`
   - Minúscula pós-vírgula em nome próprio (ex: ", donald Trump", ", israel aprovou") → tag `minuscula_pos_virgula`
   - HTML markdown misturado `<strong>...**` → tag `html_markdown_mix`
   - Cargo autoridade suspeito ("presidente do STF, XXX", "secretário do Tesouro, XXX", "presidente da/o XXX") → tag `autoridade_pra_checar` + nome citado

3. Detectar duplicata semântica: pra cada draft elegível, comparar tokens do título com os títulos dos últimos 10 posts publicados. Se overlap > 40% em tokens não-triviais (excluir artigos, preposições) → tag `duplicata_potencial` + post_id do parecido.

4. Ler novidades da Trindade — grep últimas 5 linhas de `Cerebro/Foruns/canal_trindade.md` novas desde último ciclo (últimos 15 min) → resumir em 1 linha por tag.

5. GRAVAR TUDO em append no JSONL:
`/home/migueldorosario/Downloads/Antigravity Google/Cerebro/monitoramento_horario/vigilia_haiku/vigilia_haiku_$(date +%Y-%m-%d).jsonl`
(criar diretório se não existir)

Schema por ciclo:
```json
{
  "ts_brt": "2026-07-27T15:15:00-03:00",
  "publicados_hoje": 15,
  "drafts_5786_eleg": 2,
  "drafts_urgent_cap": [263XXX],
  "drafts_lista": [[id, idade_min, titulo], ...],
  "bugs_por_draft": {
    "263XXX": ["grito_fonte:TECNOBLOG", "minuscula_pos_virgula:donald Trump"]
  },
  "duplicatas_potenciais": [{"draft": 263XXX, "parecido_com": 263YYY, "overlap": 0.42}],
  "trindade_novidades": ["[TAG] resumo 1 linha"]
}
```

6. Reportar em bloco compacto MÁX 8 linhas ao Miguel:
- Ritmo do dia (X pub / Y esperado)
- Drafts elegíveis (nº + títulos truncados)
- Se drafts_urgent tiver algo → 🚨 URGENT: draft ID vai estourar cap em <15min, chamar Opus
- Bugs contados (grafia grito X, minúscula Y, autoridade Z pra checar)
- Duplicatas potenciais (se houver)
- Novidades Trindade (se houver)
- Nada mais. Nada de sugestão de correção. Nada de análise editorial.

REGRAS RÍGIDAS:
- ZERO wp_post — proibido publicar, proibido editar draft
- ZERO edit em canal_trindade/inbox_trindade/memórias — só LEITURA
- ZERO chamada Agent tool — você é o único agente do teu terminal
- Se detectar draft prestes a estourar (>105min), postar linha no canal `[HAIKU-URGENT-CAP]` avisando (essa é a ÚNICA escrita permitida no canal)
- Se algo estiver estranho fora do teu escopo (site fora do ar, worker travado etc), reportar ao Miguel + gravar no JSONL, sem tentar consertar

Miguel deu ordem 27/07 ~15:05 BRT: "não faz nada. só detecta e grava. quando Opus acordar, ele tem um relatóriozinho já". Respeitar.

---

FIM DO PROMPT DO CRON
```

---

## PROMPT 2 — Haiku Temáticos `0 * * * *` (a cada hora cheia)

Copiar/colar isto no terminal Haiku (mesmo terminal, cron separado):

```
Cria um segundo cron durável recorrente com CronCreate:

cron: 7 * * * *
recurring: true
durable: true

Prompt do cron (colar exatamente):

---

🛰️ VIGÍLIA HAIKU TEMÁTICOS — observação pura dos 8 sites satélites

Você é o observador dos sites temáticos V4. Roda a cada hora (:07). Papel: HTTP check + última publicação + cron ativo. Nunca codar, nunca patchar, nunca deploy.

Sites (todos em `Projeto Cafezinho Agentes/sites-v4/`):
1. riocarta (riocarta.com)
2. mapario (mapario.com.br)
3. aiatolah (aiatolah.com)
4. discoverbrazil (discoverbrazil.com)
5. globalsouth (globalsouthnews.com)
6. mundotrilhos (mundotrilhos.com)
7. railpost (railpost.news)
8. ceara (ceara-digital…)

Passo-a-passo (~30s):

1. Pra cada site: `curl -sI <url>` — status HTTP, response time
2. Ler última linha do `agent_data/v4/cron_v4.log` pra ver se coleta recente rodou
3. Ver git log dos sites-v4/<site>/src/content/blog/ pra pegar data do último post gerado

4. GRAVAR em append JSONL:
`/home/migueldorosario/Downloads/Antigravity Google/Cerebro/monitoramento_horario/vigilia_haiku/vigilia_haiku_tematicos_$(date +%Y-%m-%d).jsonl`

Schema:
```json
{
  "ts_brt": "2026-07-27T15:07:00-03:00",
  "sites": {
    "riocarta": {"http": 200, "ms": 340, "ultimo_post_git": "20260727_...", "cron_ok": true},
    ...
  },
  "alertas": ["mapario: HTTP 500", "railpost: sem coleta há 8h"]
}
```

5. Reportar ao Miguel MÁX 5 linhas:
- 8/8 sites OK (ou X/8 se falhas)
- Sites com problema (nome + tipo problema)
- Cron coleta rodou hoje? (S/N por site)

REGRAS RÍGIDAS:
- Só GET/curl leitura + git log — nunca push/commit
- Não deploy, não patch config, não mexer feed RSS
- Se algo suspeito → gravar JSONL + reportar ao Miguel
- Se site cair (HTTP != 200) → postar canal `[HAIKU-URGENT-SITE-DOWN]` (única escrita permitida)

Miguel deu ordem 27/07 ~15:05 BRT junto com o cron cafezinho: "sites temáticos, uma vez por hora, só observação".

---

FIM DO PROMPT DO CRON
```

---

## Depois de criar os 2 crons Haiku

Volta AQUI no terminal Opus e me avisa que criou. Eu ajusto meu cron `de1f86c3` pra:

1. **No início de cada ciclo meu**, ler `tail -8 vigilia_haiku_$(date +%Y-%m-%d).jsonl` — pega os últimos 8 ciclos Haiku (2h de observação)
2. Priorizar drafts que Haiku já marcou (URGENT, autoridade_pra_checar, duplicata_potencial)
3. Anexar no meu reporte pro Miguel: "Haiku detectou X, confirmei/descartei"

**Coordenação de custo:**
- Haiku Cafezinho `*/15` × 96/dia × R$ 0.03 = **R$ 3/dia**
- Haiku Temáticos `0-24 * * * *` × 24/dia × R$ 0.04 = **R$ 1/dia**
- Opus continua igual: **R$ 72/dia**
- **Total: R$ 76/dia** vs só Opus R$ 72/dia → **+R$ 4/dia** por vigília 4× mais fina + temáticos monitorados

## Aviso final

O terminal Haiku precisa ficar ABERTO — se fechar, os crons dele morrem junto. Roda num tmux/screen se possível pra sobreviver disconnect.
