# FÓRUM — Temáticos: destaques por audiência GA4 (manchete = mais vista) + fix hero Ceará (05/08/2026)

**Data:** 2026-08-05 ~01:00-01:40 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel (chat): "imagem quebrada aqui no ceará digital corrige" + "no destaque colocasse as notícias mais vistas… na manchete entra a mais vista, isso para todos os temáticos… os destaques estão parados"

## 1. Os dois problemas visíveis

1. **Imagem quebrada no Ceará Digital:** card "Ciro Gomes lança pré-candidatura…" apontava `/hero/20260721-ciro-….jpg` (404); o arquivo real não tem prefixo de data. Corrigido no `destaques.json` → commit `36752cf` (ceara-v4) → no ar.
2. **Destaques "parados":** a seção "Destaques" da home dos temáticos é um **JSON estático** (`src/data/destaques.json`) editado à mão 2× na história — nunca mais girou. O feed abaixo (collection) atualizava normalmente, daí o contraste. Diagnóstico extra: o site no ar é o repo **ceara-v4** (pipeline V4 local); o `/root/cicero_remote/ceara-digital` no NYC é o pipeline ANTIGO (repo ceara-digital, fora do ar) — mesmo split-brain já visto no GSN.

## 2. A solução (ordem do Miguel)

**`agentes_tematicos/v4/ga4_destaques.py`** (novo, cron local `45 3,13 * * *`):
- Lê GA4 Data API por property (IDs canônicos: CEREBRO_NODE_TELEMETRIA §4) — screenPageViews por pagePath, janela 7d (fallback 28d).
- **Manchete = #1 em views; destaques em ordem de audiência.** Completa com recentes quando as views não enchem 5 slots; **fallback total = recentes** quando o portal ainda não tem audiência (destaques nunca mais congelam).
- **Hero validada no disco** antes de entrar no JSON (o bug do card quebrado não se repete por essa via).
- Commit/push por repo só se mudou.

## 3. Primeira rodada real (01:26 BRT) — 6/6 publicados

| Site | Fonte | Views janela | Nova manchete |
|---|---|---|---|
| ceara | GA4 28d + padding | 8 | "Quem é Elmano de Freitas, governador do Ceará pelo PT" |
| riocarta | GA4 7d | 25 | "Benedita da Silva: trajetória…" |
| globalsouth | GA4 7d | 16 | "The Greatest Country in the World" |
| railpost | GA4 7d | 10 | "InnoTrans 2026 to Be Most International Edition Yet" |
| mundotrilhos | GA4 7d + padding | 2 | "Dobrar o metrô e quadruplicar os BRTs…" |
| discoverbrazil | GA4 7d + padding | 2 | "Amazon Alexa+ Tests Trip Booking…" |

Verificado ao vivo: ceara.digital com nova manchete e **todas as 5 heroes 200**.

## 4. Respostas às perguntas do Miguel (mesmo chat)

- **"A telemetria está pronta?"** Sim — infra GA4 conectada desde 22/07 (conta `Sites_tematicos`, 7 properties, SA com acesso; painéis `/v6/custos` e `/v6/tematicos/<slug>`). O que NÃO existia era a consulta **por página** para dirigir destaques — criada agora.
- **"Quem escreve as matérias é o DeepSeek?"** Sim — tier `padrao` do `llm_tiers.json` = deepseek primeiro (v4-pro redação; v4-flash comentarista; deepseek-chat prompt visual). É o consumo esperado da produção diária dos 8 portais.

## 5. Pendências

- **aiatolah** e **mapario** não têm a seção Destaques na home (sem `destaques.json`) — criar a seção ou deixar fora: decisão do Miguel. (mapario também não tem property GA4 conhecida.)
- Risco conhecido aceito: feedback loop "manchete mais vista se perpetua" — janela 7d mitiga; se virar problema, adicionar decay.
- Pipeline antigo do ceara no NYC (cron 9:15 → repo fora do ar) continua rodando à toa — candidato a desligamento (mesmo destino dos crons GSN de 23/07). **Pendente ordem.**

## 6. FOLLOW-UP (mesmo dia 10:35 BRT) — pílulas de kicker vazias + dedup GA4

**Gatilho Miguel:** "os quadradinhos em cima do título nos destaques estão quebrados; só aparece o da Miranda" (print do GSN).

1. **Causa:** o gerador escrevia `kicker: ""` quando o post não tinha `categoria_macro` (posts antigos do GSN só têm `tags`) e o template renderizava a pílula incondicionalmente → caixinha vazia com borda.
2. **Cura (2 camadas):** (a) `_kicker()` ganhou cadeia de fallbacks — categoria_macro → category → 1ª tag ≥4 chars prettified (tag curta tipo "ai" virava pílula feia) → `default_category` do config → "Destaque"; (b) os **6 templates** ganharam render condicional `{d.kicker && …}` (defesa em profundidade).
3. **Bug extra achado na verificação:** GA4 trouxe o mesmo post FOCAC por 2 paths (canonical+variante) → card duplicado; gerador agora faz **dedup por slug** na fase GA4.
4. **Ao vivo 10:45:** GSN com 5/5 pílulas preenchidas (Multipolar world, Priscila Miranda, FOCAC, China, Unctad), 0 vazias, FOCAC 1×.

**Memória técnica:** `Memorias/memoria_tematicos_destaques_ga4_20260805.md`
