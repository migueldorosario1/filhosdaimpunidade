---
name: Cross-linking "Leia também" LIVE — 2026-04-20
description: Cross-linking redesenhado como bloco "Leia também" ao final do post (fio hr + link do título). Sem LLM gerando frase. Afeta Trindade + Historiador + temáticos que passam pelo motor_publicador.
type: project
originSessionId: 12b56cc4-8603-4cea-8db1-6cd7358800e3
---

**Redesign 2026-04-20 ~11:50 UTC.** Miguel reportou que as frases retóricas geradas pelo LLM estavam mecânicas e repetitivas — 30+ inserções quase todas começando com "Como já destacamos/analisado/discutido em §LINK§...". Trocamos pelo formato de bloco separado.

## Novo formato (ao FINAL do corpo, antes da caixa_newsletter)

```html
<hr class="cafezinho-leia-tambem-fio" />
<p class="cafezinho-leia-tambem"><strong>Leia também:</strong> <a href="URL">Título do artigo relacionado</a></p>
<hr class="cafezinho-leia-tambem-fio" />
```

## Mudanças no `interlink_interno.py`

- LLM agora só escolhe: retorna `{"escolhido": int|null}`. Não redige mais frase. `max_tokens=60`, `temperature=0.2`.
- Removidas funções: `_validar_frase`, `_montar_anchor_html` (ajuste gramatical feminino), `_inserir_apos_segundo_p`, constante `PLACEHOLDER`.
- Adicionadas: `_montar_bloco_leia_tambem(url, titulo)` + `_anexar_bloco(html, url, titulo)` (checa se URL já está no html).
- `_limpar_titulo` faz `html.unescape` antes de usar (resolve `&#8220;` etc. em títulos brutos do WP).
- Circuit breaker (3 nulls consecutivos do LLM → pausa) mantido.
- Cache 6h, filtro canibalização (>1 ano + Jaccard>0.7), filtro slug idêntico, filtro "recém-publicado <30min" — todos preservados.

## Quem usa

- `motor_publicador.py` linha 1127 — cobre Trindade (Geopolítica/Nacional/Trends) + temáticos + turismo + qualquer agente que chame `publicar_postagem`.
- `agente_historiador.py` linha ~281 — chamada direta própria.
- Ambos chamam ANTES de `html += CAIXA_NEWSLETTER_AJAX`, então bloco "Leia também" fica sanduichado entre o corpo e a caixa newsletter.

## Fix duplicação hr 2026-04-20 12:00 UTC

Miguel notou que a caixa_newsletter (`CAIXA_NEWSLETTER_AJAX` no motor_publicador) já começa com `<hr style="margin: 30px 0;">`. Nosso bloco original fechava com outro `<hr class="cafezinho-leia-tambem-fio" />`, gerando 2 hrs visuais colados. Removido o hr final do `_montar_bloco_leia_tambem` — agora só tem 1 hr antes do "Leia também" (o hr depois vem da própria caixa).

## Validação empírica — monitoramento 8 ciclos (2026-04-20 11:51 → 16:03 UTC, 4h12min)

- 24 entries novos no `/root/agent_data/interlink_dry_run.log`
- **15 `ok` (publish com bloco) = 63%**
- 7 `sem_candidato` (5 busca_vazia, 2 llm_null) = 29%
- 2 `ok_dryrun` (drafts legítimos — agentes que publicam em draft pulam bloco) = 8%
- 0 erros, 0 circuit breakers disparados, 0 `ja_tem_link`, 0 entities vazadas
- 9 posts publish amostrados via API WP (237119, 237125, 237135, 237144, 237155, 237175, 237190, 237199, 237214) — **100% com exatamente 1 `cafezinho-leia-tambem-fio`**, bloco sanduichado entre último `<p>` do corpo e `<hr style="margin: 30px 0;">` da caixa newsletter. Sem duplicação.
- Cross-linking temático bom: Belém→MPF Belém, Pezeshkian→Pezeshkian, Rosatom→Rosatom, Kremlin→Kremlin.

## Arquivos

- `root/interlink_interno.py` (local + Tencent `/root/`) — reescrito 2026-04-20, sintaxe validada, deploy via rsync seguro sem `-a`.
- `root/agente_historiador.py` e `root/motor_publicador.py` **inalterados** — continuam chamando `injetar_link` com a mesma assinatura.
- Log: `/root/agent_data/interlink_dry_run.log` (JSONL, 1 linha por execução; agora sem campo `frase_inserida`).

## Histórico anterior

Antes deste redesign, o módulo gerava frase via LLM com placeholder `§LINK§` e inseria após o 2º `<p>`. Fix de 2026-04-20 03:24 UTC tinha corrigido tema-longo + concordância feminina, mas o problema da repetição retórica continuou. Por isso virou bloco estático.
