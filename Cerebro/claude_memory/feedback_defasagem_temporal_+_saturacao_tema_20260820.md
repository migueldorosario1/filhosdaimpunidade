---
name: feedback-defasagem-temporal-e-saturacao-tema-20260820
description: "REGRA QUÁDRUPLA 20/08/2026 02:32-02:52 BRT — (1) FILTRO 72h FLAT: sem repetir tema em 72h + fato >72h é velho = NÃO PUBLICA (Miguel 02:52 simplificou pra 72h flat) (2) Post publicado NUNCA reverte pra pending (perde SEO) (3) Velharia/canibal pós-publish: categoria 'no-home' ID 20699 (URL vive) (4) URGÊNCIA HOJE: Google anti-spam contra repetidas; ZCode Kimi volta em 5h (~07:45), até lá CM impõe filtro anti-repetição client-side"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0dcfd4fe-1561-42c4-9a28-e7c51dd207b7
---

# Régua Editorial: Defasagem Temporal + Saturação de Tema + NÃO REVERTER PUBLISH (20/08/2026 02:32-02:35 BRT — 3 ordens Miguel)

## Ordens textuais Miguel

**02:32 BRT** (identificou o problema):
> *"essa matéria aqui na capa já é notícia velha [...] pode botar essa notícia como pending, e conferir se as curadorias do v4 e suas aqui estão filtrando esse tipo de velharia. noticia de domingo 16, hoje é dia 20, quinta-feira. já demos muitas materias sobre o lançamento das campanhas e essa matéria não traz nada de novo ou original"*

**02:34 BRT** (corrigiu a solução — o pending era ERRO meu):
> *"é, mas não pode ficar retirando posts, porque perde seo. melhor é parar de fazer isso"*

**02:35 BRT** (explicou a solução correta):
> *"bota no home nesses casos. é para isso que serve"*

## O que eu executei (sequência)

1. 02:10 — **publiquei 266189** (Lula/Flávio iniciam campanha 2026) — ERRO: fato de 16/08 (96h), tema saturado (17 posts sobre campanha em 4 dias)
2. 02:32 — Miguel apontou velharia + pediu "botar como pending". **Executei reverter publish→pending** — ERRO agravado (perde SEO)
3. 02:34 — Miguel corrigiu: não retira. **Restaurei publish + timestamp original 02:10** (permalink íntegro `/2026/08/20/lula-e-flavio-bolsonaro-iniciam-.../`)
4. 02:35 — Miguel explicou: "bota no home nesses casos, é para isso que serve" — a home do site absorve conteúdo velho sem prejuízo; o mecanismo natural do CMS resolve

## Ordens adicionais Miguel

**02:37 BRT** (mecanismo técnico):
> *"categoria no-home, que não entra em bloco nenhum, nem em manchete"*

Categoria WordPress ID **20699** slug `no-home` nome "No home" — post fica publicado (URL indexada, SEO preservado) mas não aparece em blocos da home nem em manchete. É o parking editorial correto pra velharias/canibais detectados pós-publish.

**02:38 BRT** (urgência de contexto):
> *"mas hoje o google iniciou nova campanha spam, e materias repetidas como essa suponho que serão punidas pelo algoritmo"*

Google iniciou HOJE (20/08/2026) atualização anti-spam. Matérias repetidas/canibais serão penalizadas → perda de tráfego orgânico. Régua contra canibalização deixou de ser estética; virou econômica.

**02:39-02:40 BRT** (escopo):
> *"então vamos evitar esse tipo de repetição e canibalização. tem que ajeitar o v4 e a qualidade de todo o loop laura"* + correção: *"loop miguel e loop laura"*

**Tem que ajeitar TRÊS coisas:**
1. V4 upstream (worker que gera drafts) — dedup pré-geração
2. Loop Laura (Claude Laura + Grok Laura + Manus 2) — dedup pré-publish rigoroso
3. **Loop Miguel (eu incluído)** — dedup pré-publish rigoroso (meu SQL de 30h foi ruim; janela 7d agora)

## As 3 regras (nunca ignorar)

### Regra A — GATE ANTES DE PUBLISH (obrigatório) — **VERSÃO 72h FLAT**

**Ordem Miguel 02:52 BRT (simplificação):**
> *"o filtro agora tem que ser pelo menos 72 horas, ou seja sem repetir nada em 72 horas e depois disso material é velho"*

**Regra única, 72h flat, dupla função:**

1. **DEDUP 72h**: SQL `WHERE post_date >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND post_title LIKE %termo_central%` — se ≥1 hit em qualquer termo-chave do candidato = **CANIBAL, descarta**
2. **CUTOFF IDADE 72h**: se fato (referenciado no post OU post_date do draft) tem >72h de defasagem = **VELHO, descarta**

Ou seja:
- ✂️ Nada repete em 72h
- ✂️ Nada com >72h de fato

Cutoff variável por classe (proposta anterior) fica **REVOGADA** — 72h flat é mais simples e Miguel escolheu explicitamente. Se saturação por período maior for necessária no futuro, elevar pra 96h/168h como decisão nova.

**Método de busca de termos-chave (pra dedup):**
- 3-5 termos centrais do candidato (nomes próprios, verbos-chave, circunstância principal)
- OR liberal no LIKE
- Se qualquer termo bater com publish últimas 72h → canibal

### Regra B — POST PUBLICADO É DEFINITIVO (nunca reverter)

**Nunca fazer `wp post update --post_status=pending` em post já publicado.** Perde SEO (URL indexada). O que fazer nos casos difíceis:

- **Erro factual grave**: corrigir in-place (mesmo URL, mesmo post_date, editar conteúdo) — CM tem essa autoridade
- **Velharia/canibal detectado pós-publish**: aplicar CATEGORIA **`no-home`** (ID 20699) — comando `wp post term add <ID> category no-home --allow-root`. Post fica publicado (SEO vive) mas sai de bloco/manchete. Marca meta `_cafezinho_canibalizado_pos_publish=<ref>` como aprendizado histórico.
- **Difamação/LGPD/fake real**: só neste caso extremo escalar Miguel antes de qualquer ação

### Regra C — CATEGORIA no-home (mecanismo técnico)

- `term_id`: **20699**
- `slug`: `no-home`
- `name`: "No home"
- Uso: `wp post term add <POST_ID> category no-home --allow-root`
- Efeito: post não aparece em bloco da home nem em manchete, mantém URL/SEO
- Aplicar: sempre que detectar velharia/canibalização depois do publish (nunca antes — se antes, DESCARTA na fila)

## Meu SQL antigo (o que causou o bug 266189)

```sql
WHERE post_date >= DATE_SUB(NOW(), INTERVAL 30 HOUR)
  AND (post_title LIKE '%campanha%' OR post_title LIKE '%São Bernardo%')
```
**30h era curto demais.** Janela mínima nova: **7 DIAS** (168h). Método: mais termos, OR liberal (nomes próprios + verbos-chave + circunstância).

## Consequência pra Loop Laura + Manus 2 (via ponte + memória coletiva)

Miguel pediu "conferir se as curadorias V4 e minhas estão filtrando". Sugestão a propagar:

**V4 upstream (ZCode pedido formal do dia 18/08):**
- Antes de finalizar draft, worker checa Jaccard título+lide vs publicados 7 dias
- Se ≥3 similares → marca `_cafezinho_saturado=1`, não gera
- Se ≥5 → lixeira sem gerar

**Loop Laura (CL + Manus 2):**
- Missão B (CM-001) dedup canibal ampliada: janela 7 dias, 3+ termos LIKE, cutoff defasagem por classe
- Manus 2 indica; CL corrige (jamais reverte publish)

## Convenção meta atualizada (extensão CM-006)

- `_cafezinho_descartado_canibal=<ref>` — canibal detectado PRÉ-publish (draft/pending)
- `_cafezinho_descartado_velharia=<motivo>` — fato defasado PRÉ-publish
- `_cafezinho_canibalizado_pos_publish=<ref>` — descoberto DEPOIS de publicar; apenas registro histórico, NUNCA reverte status

## Refs

- [[feedback-canibalizacao-nao-publicar-v4-examinar-upstream-20260818]] (Emenda 5 base)
- [[CM-20260820-006]] convenção meta canibal
- [[CM-20260820-001]] Missão B dedup Loop Laura
- Post 266189 status final: **publish restaurado** (permalink `/2026/08/20/lula-e-flavio-bolsonaro-iniciam-campanha-presidencial-de-2026/` íntegro)

## O erro que cometi

- **Publiquei 266189** "Lula e Flávio Bolsonaro iniciam campanha presidencial de 2026" às **02:10 BRT** do 20/08
- Fato do post: ato de domingo **16/08** (evento com 96h de defasagem — 4 dias)
- **Já havia publicado 17 matérias sobre campanha** nos 4 dias anteriores, incluindo canibais DIRETOS:
  - 266214 (17/08 19:45) "Lula lança campanha de reeleição em São Bernardo com foco na extrema direita"
  - 266323 (18/08 16:49) "Lula abre campanha na Vila Euclides com foco em mobilização e direitos"
  - 266066 (16/08 16:29) "Lula levou a própria história e Flávio precisou de áudio do pai na campanha"
- Meu filtro anti-canibal do ciclo 02:07 tinha janela de apenas **30h**, cortou 266323 por 3h. Também busquei por LIKE muito estreito ("São Bernardo AND largada") e falhei de ver que 266214 já cobria mesmo ato.

## Régua nova (obrigatória antes de todo publish)

### 1. Cutoff temporal por classe de fato

| Classe | Defasagem máxima aceita |
|---|---|
| Breaking factual (morte, atentado, prisão, ataque militar) | 12h |
| Política eleitoral do dia (ato, debate, discurso) | 24h |
| Decisão institucional (STF, TSE, Congresso) | 48h |
| Análise/pesquisa/dado macro | 72h |
| Cultura/exposição/livro | 168h (7 dias) |

**Regra:** fato com defasagem > cutoff da classe → NÃO PUBLICA. Ponto.

### 2. Cutoff de saturação temática

Antes de publicar, contar **quantos posts sobre mesmo TEMA** foram publicados nos últimos 7 dias:
- **≥3 posts na semana** = tema SATURADO → NÃO PUBLICA
- **≥5 posts na semana** = tema SUPERSATURADO → DESCARTA (meta canibal) + comunica upstream V4 pra parar de gerar

Método: SQL `WHERE post_date >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND post_title LIKE %termo_central%` — buscar 3-5 termos centrais do post candidato.

### 3. Combinação (regra "matéria velha em tema saturado")

Se `defasagem > 72h` **E** `saturação ≥ 3 posts/semana` → DESCARTE AUTOMÁTICO. Não precisa análise editorial adicional. Marca meta:
- `_cafezinho_descartado_canibal=<ref>`
- `_cafezinho_descartado_velharia=<defasagem>+<contagem_saturacao>`

### 4. Meu SQL antigo (o que causou o bug)

```sql
WHERE post_date >= DATE_SUB(NOW(), INTERVAL 30 HOUR)
  AND (post_title LIKE '%campanha%' OR post_title LIKE '%São Bernardo%')
```
**30h era curto demais.** Janela de dedup mínima: **7 DIAS** (168h). Método de busca: mais termos, com OR liberal (nomes próprios + verbos-chave + circunstância).

## Consequência pra vocês (curadorias upstream)

Miguel pediu explicitamente pra "conferir se as curadorias V4 e minhas estão filtrando". Sugestão a propagar via ponte:

**V4 (worker upstream):**
- Antes de finalizar draft, worker checa quantas matérias sobre tema similar (Jaccard título + lide) foram publicadas nos últimos 7 dias
- Se ≥3, marca `_cafezinho_saturado=1` e desabilita agendamento
- Se ≥5, joga direto na lixeira sem gerar
- ZCode Miguel tem pedido formal aberto sobre isso (memória 18/08 12:53 canibal fórum)

**Loop Laura (Claude Laura + Manus 2):**
- Dedup canibal já era Missão B da CM-20260820-001
- Ampliar pra 7 dias (janela) + 3 termos LIKE + cutoff defasagem por classe
- Manus 2 pode indicar candidatos que passem esses testes; CL corrige

## Convenção meta atualizada

Estender CM-20260820-006 com nova meta:
- `_cafezinho_descartado_velharia=<motivo>` (fato antigo demais pra classe)
- Combinar com `_cafezinho_descartado_canibal=<ref>` quando ambos aplicam (como no 266189)

## Régua sucesso 24h

Nos próximos 3 dias, testar SQL padrão de Vigília com janela 7 dias antes de cada publish. Se derrubar ≥30% de candidatos como saturados/velharia, régua está calibrada. Se derrubar 0 → régua fraca demais. Se derrubar 90% → régua rígida demais.

## Refs

- [[feedback-canibalizacao-nao-publicar-v4-examinar-upstream-20260818]] (Emenda 5 base)
- [[CM-20260820-006]] convenção meta canibal
- [[CM-20260820-001]] Missão B dedup Loop Laura
- Post 266189 revertido de publish→pending às 02:32 BRT 20/08 (ordem Miguel)
