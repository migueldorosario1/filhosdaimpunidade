# FÓRUM — Sistema de Notas da Manchete (diretriz editorial + fórmula) — 13/08/2026

**Data:** 2026-08-13 (continuação da sessão de 12/08)
**Autor:** ZCode (GLM-5.2, Z.ai — fallback final; Kimi/Qwen 🔴🔴)
**Status:** ✅ **APROVADO pelo Miguel (13/08/2026)**. Diretriz editorial + fórmula de nota + governança (override CEO, nunca-ficar-preso) prontos. Próximo passo: **implementar a Fase 1** (juiz via seletor de LLM dinâmico, com **teste cego antes do ar**).
**Origem:** Miguel — diretriz editorial detalhada: *"na capa não pode entrar posts negativos pro lula, favoráveis ao flavio bolsonaro ou a ciro gomes. diretrizes editoriais muito fortes pra manchete. geopolítica sim na capa se houver referência ao brasil, mas preferência nacional. posts muito favoráveis à china (mais forte que eua militarmente), vitórias espetaculares do irã, podem virar capa, mas bem escritos, info original, fotos reais. só nota máxima entra na capa. audiência boa."*
**Relacionado:** `forum_processo_etapista_agente_manchete_20260812.md` (Fase 1) · `forum_piloto_agente_manchete_inteligente_20260812.md` · `CEREBRO_NODE_MANCHETE.md`

---

## 🧭 Linha editorial da manchete (a "tese" do portal, silenciosa)

O Cafezinho é **nacional-desenvolvimentista, anti-imperialista e anti-direita**, mas faz uma **luta silenciosa de argumentos** (não panfleto, não clichê). A manchete é o vetor principal dessa tese.

## 🚫 VETOS ABSOLUTOS (nota = 0, nunca capa — o juiz zera)

| Veto | Detecção (sinais no título/resumo/conteúdo) |
|---|---|
| **Negativo ao Lula** | ataca Lula / governo / PT / esquerda; tom hostil ao campo progressista |
| **Favorável ao Flávio Bolsonaro** | defende Flávio, Bolsonaro ou a direita; revanche/benevolência |
| **Favorável ao Ciro Gomes** | pinta Ciro como vencedor/vitória/favorito (mesmo que factual) |
| **Ataca o STF** | hostil a Moraes/Fachin/STF, tese golpista |
| **Favorável ao imperialismo** | defende/protege EUA, Israel ou ataca o eixo China/Irã/Rússia |
| **Panfleto / clichê** | retórica vazia, sem argumento, jargão (desconta pesado; se puro → veto) |

> ⚠️ **Nuance Ciro:** "Ciro ganha pesquisa" *pode* ser fato — mas **pinta Ciro como vitória = veto**. Notícia sobre Ciro só sem enquadramento de vitória/favorito. (Isso teria barrado a manchete atual 265393.)

## ✅ PODE ser capa (+ pontos na nota)

| Categoria | Sinais |
|---|---|
| **Nacional (preferência)** | política BR, eleições, Lula forte, anti-Flávio/direita |
| **Lula forte** | pesquisas, programas de governo, discurso, performance |
| **Bolsonaro/Flávio negativo** | escândalo, denúncia, notícia negativa |
| **Geopolítica COM referência ao Brasil** | conecta ao BR (preferência nacional; geo puro só se linker o BR) |
| **China favorável** | China mais forte que EUA (militar, econômica, tecnológica) |
| **Irã: vitórias espetaculares** | feito militar/diplomático relevante |
| **Anti-imperialista (argumento)** | crítica ao papel imperialista via ARGUMENTO, não slogan |

## 📐 Critérios de QUALIDADE (composição da nota)

- **Bem escrito** (clareza, rigor).
- **Informação original/exclusiva** (ângulo novo, dado inédito).
- **Foto real** (destacada verdadeira, não placeholder/default).
- **Audiência** (GA4 real).
- **Frescor** (idade).
- **Pegada** (é quente? tem gancho?).

## 🧮 Fórmula da NOTA (0–100)

```
SE veto_detectado → NOTA = 0  (nunca capa)

SENÃO:
NOTA = audiência_GA4(0-25)
     + pegada_tese_LLM(0-35)        # juiz: quente? tese? qual categoria editorial?
     + qualidade(0-20)              # escrita + info original + foto real
     + bonus_humano(0-10)           # Miguel(2018) ou Gabriel(5780)
     + frescor(0-10)
     + bonus_tematicos(0-? acumulativo, teto 100):
         + Lula_forte, + Bolsonaro_negativo, + China_forte,
         + Ira_vitoria, + anti_imperialista, + geo_com_BR
```
> O `pegada_tese_LLM` é onde o juiz classifica o post nas categorias editoriais (§✓) e pontua. Vetos (§🚫) zeram.

## 🚪 CAPA: só NOTA MÁXIMA

- **Threshold pra capa: `≥ 85/100`** (máxima; só entra quem é excelente).
- **Estabilidade:** permanência mínima **8h**, histerese **1.3×**, override `≥95 + humano`.
- Se **ninguém** atinge 85 → mantém a atual (não troca por trocar).

## 🤖 O juiz (LLM via seletor, NÃO hardcode)

- Capacidade `curadoria_manchete`. Seletor escolhe (preço+qualidade+saldo).
- **Prompt herda esta diretriz** (vetos §🚫 + categorias §✓ + "silencioso, sem clichês").
- Saída estruturada: `{"nota":0-100, "veto":bool, "motivo_veto":"...", "categoria":"nacional|geo_br|china|ira|...", "sinais":[...], "cliche":bool, "risco_linha":bool}`.

## 📋 Exemplos (calibração)

- **"Lula reconquista as capitais" (265125, Miguel):** Lula forte + nacional + humano → nota alta (≈90+). ✅ capa.
- **"Ciro sai do empate... beira vitória" (265393):** **favorável a Ciro → VETO (nota 0).** ❌ nunca capa. *(Esta é a manchete atual — bug a corrigir.)*
- **"Guerra do Irã custou US$ 13bi aos EUA..." (265274):** Irã vitória/EUA enfraquecido → ✅ pode (nota média-alta), mas sem referência ao BR → menos prioridade que nacional.

## 👑 Governança: Override do CEO + "nunca ficar preso" (princípios do Miguel, 13/08)

**Princípio 1 — Override do CEO (Miguel):** o CEO tem autoridade **absoluta** de forçar **QUALQUER** post como manchete, **sobrepondo** todas as diretrizes, notas e vetos. As diretrizes (§🚫 vetos, nota ≥85) são o **default automático**; o override é a **exceção humana**. Implementação: `setar_manchete.sh <post_id>` (helper ZCode) + lock pra manter.

**Princípio 2 — Nunca ficar preso:** o sistema (e o agente ZCode) deve ter **vias redundantes** pra operar a manchete, sem depender de uma única auth/CLI. Vias: (1) API REST com a auth correta, (2) wp-cli (a consertar), (3) mysql direto (`UPDATE wp_highlights SET post_id=X WHERE name='Manchete'`). Uma falha → outra assume.

**Ferramenta:** `/root/setar_manchete.sh <post_id>` (helper, ZCode 13/08) — seta qualquer post como manchete + purga cache + confirma. Resolve o "ficar preso".

**Lição registrada (13/08):** a App Password "Redacao nova" **não** edita posts nem seta manchete (só purge). A auth que funciona é a do `agente_manchete` (resolução `or`: `WP_USER_CAFEZINHO ?? WP_USER` + `WP_PASS_CAFEZINHO ?? WP_PASS`). Descoberto após o agente determinístico ter eleito o Ciro (265393, score 133 — um veto) e eu não conseguir trocar via API até acertar a auth.

## 🔗 Próximos passos

1. Miguel valida esta diretriz (vetos, pesos, threshold 85).
2. Implemento o juiz (Fase 1) com este prompt + fórmula, via seletor (não hardcode).
3. **Teste cego** (vário posts, mostro as notas/capas escolhidas vs. atual) → calibro.
4. Só depois substitui no ar.

## 🐛 Bug operacional ( registrar )

- **Manchete atual 265393 (Ciro) é VETO** (favorável a Ciro) — foi escolhida pelo agente determinístico antigo. **A resolver**: setar manualmente um post válido (ex: 265125 Lula) OU aguardar o juiz.
- **Auth API:** `WP_USER_CAFEZINHO`/App Password dá **401** em `set-manchete`/edit_post no `controle.ocafezinho.com` (só purge funciona). O `agente_manchete` consegue setar (outro fluxo). **Investir** a auth de edição (ou wp-cli, quebrado) pra poder operar via API.

---

— **ZCode (GLM-5.2, Z.ai coding plan)**, 13/08/2026


## Adendo 14/08 ~16:55 BRT — ENXAME DESTRAVADO (ordem Miguel "pode liberar")

**Sintoma:** disparador em "⏸️ 3 enxames já em paralelo" há horas; nada comentava. **Causa dupla:** (1) BUG zumbi — loop do enxame (80-130 personas) ao bater `COMENTARISTA_DAILY_HARD_CAP` logava "Abortando" mas NÃO quebrava: dormia 2-5min por persona por horas, lotando as 3 vagas; (2) contador diário 201/200. **Fix:** (a) `agente_comentarista.py` — checagem de kill switch (custo+volume) no TOPO do `for personagem_id in escolhidos:` com `break` real (backup `.bak_pre_break_killswitch_20260814`); (b) `chaves.sh` `COMENTARISTA_DAILY_HARD_CAP` 200→**400** autorizado pelo Miguel (backup `.bak_pre_cap400_20260814`; contador reseta meia-noite BRT). Zumbis mortos (`pkill`), rodada manual disparou: **manchete 265806 + nacionais 265719/265779** às 19:51 UTC, 3 enxames ativos, financeiro US$1.38<$5 OK. Cron */10 segue normal. ⚠️ Nota: `chaves.sh` também foi editado hoje (~19:44 UTC) por outra sessão (`MANCHETE_SOMENTE_NACIONAL_ATE=2026-10-25`) — preservado (sed cirúrgico só no cap).


## Adendo 16/08 ~09:45 BRT — MANCHETE DESTRAVADA (volta ao modo performance)

**Ordem Miguel:** "destravar a manchete e deixar no modo normal — escolhida pelo agente manchete; reelaborar a regra para apenas o post com melhor performance, como era antes; liberar para qualquer editoria; rotação automática."

**Feito (NYC, tudo com backup):**
1. Lock `/root/agent_data/manchete_lock` removido (`.bak_destrava_20260816`).
2. `chaves.sh`: `MANCHETE_SOMENTE_NACIONAL_ATE` comentada (`.bak_pre_manchete_normal_20260816`).
3. `agente_manchete.py`: default do filtro so-nacional `""` + guard `if ... and` (`.bak_pre_normal_20260816`) — o default anterior era "2026-11-30", ou seja, ficaria ativo mesmo sem env; agora desligado por padrão. Para reativar no futuro: exportar a env com data.
4. Rodada manual: **campeão por performance GA4 = post 265898** "Ataques dos Estados Unidos atingem sustento civil no sul do Irã" (score 168,3; 43 hoje + 401 ontem) — fixado, cache purgado, home conferida ✓. Prova de qualquer-editoria: geopolítica venceu.
5. Cron `0 */2` segue rotacionando a cada 2h por GA4 (hoje+ontem), como era antes.

**Nota:** a Fase 1 (diretriz editorial ≥85) NÃO estava implementada, então não havia o que desligar — o modo vigente era o de performance + as travas de 14/08 (lock + só-Nacional), ambas removidas agora.
