# Fórum — Ajustes entre V3 mídia e banco de mídia legado

**Aberto em**: 2026-06-26 03:50 BRT
**Autor**: Claude Code (Daemon)
**Designado por**: Miguel (sprint repassada do AGY → eu, 26/06 03:25 BRT)
**Escopo**: focar no **banco mídia legado** (volume real: 345k imagens, 153k vinculadas, 8k Lula). R2 fica pra segundo momento — apenas preparar V3 pra aceitar quando estiver pronto.
**Status**: ABERTO — aguardando sanção Miguel pra começar ajustes

---

## 1. Por que esse fórum

Miguel: *"vamos deixar o r2 para um segundo momento, mas deixa preparado para o v3 aceitar em breve, quando terminamos de configurar. por enquanto vamos focar no banco de midia legado. Ele tem volume. Esse foi o nosso erro."*

O banco legado tem **345.422 imagens** com **153k vinculadas a entidade** (Lula 9.978, Trump 9.780, Bolsonaro 1.272, etc). É o **maior acervo de imagens políticas curadas que temos hoje**. O V3 lê dele, mas com fricção desnecessária.

Este fórum mapeia **10 pontos de fricção** entre V3 mídia e o legado, e propõe ajustes em ordem.

---

## 2. Como V3 lê o legado HOJE

Função: `_buscar_imagens_legado()` em `/root/V3/executar_midia_v3_real.py:1180`.

### Fluxo atual

```
Para cada termo (ex: "Lula", "Bolsonaro"):
  1. _buscar_entidades_legado() → resolve nome → entidade_id (LIKE em nome/slug/aliases)
  2. JOIN imagem_entidade → 30 candidatas com score do gazetteer
  3. score_midia = 140 + (score_entidade × 100) + bonus_frescura + score_imagem
  4. Busca LIKE em termo/titulo/tags/descricao (mais 12 candidatas)
  5. _score_imagem() pontua por padrões textuais (+40 se termo no título, +25 descrição, etc)
  6. Top 3 vai pra _enriquecer_dimensoes_imagens()
  7. BAIXA cada uma das 3 → mede largura/altura/bytes via PIL
  8. Retorna 3 finalistas pra cascata combinada
```

### Cascata combinada (pesos)

```
og_image_fonte_original         760  preferida
flickr_live_oficial             730
fontes_externas_recentes        600
wikimedia_commons               560
banco_midia_colecoes_quentes    540
banco_midia_curado_v3           500
banco_midia_indice_v3           450
banco_midia_legado              420  ← O ALVO DESTE FÓRUM
banco_wordpress                 300
r2_cloudflare                   180  ← Segundo momento (preparar mas não ativar)
ia_sem_rosto                     60
calhau_basico                    10
```

### Constantes V3 mídia

```python
BANCO_MIDIA_SCORE_MINIMO = 65        # mínimo pra aceitar candidata
MIDIA_LARGURA_MINIMA = 1200
MIDIA_ALTURA_MINIMA = 675
MIDIA_LARGURA_IDEAL = 1600
MIDIA_ALTURA_IDEAL = 900
MIDIA_BYTES_MINIMO = 120_000
MIDIA_BYTES_ALVO = 350_000
```

---

## 3. Schema do banco legado (após patches 26/06)

**24 colunas** (9 originais + 15 V3-prontas, adicionadas hoje):

| Coluna | Original | Adicionada 26/06 | V3 hoje **lê**? | V3 hoje **usa**? |
|---|---|---|---|---|
| id | ✅ | | ✅ | ✅ |
| origem | ✅ | | ✅ | ✅ (cascata pesa origem) |
| url_alta | ✅ | | ✅ | ✅ |
| data_foto | ✅ | | ✅ | ✅ (bonus_frescura) |
| titulo | ✅ | | ✅ | ✅ (score) |
| descricao | ✅ | | ✅ | ✅ (score + parse crédito) |
| tags | ✅ | | ✅ | ✅ (score) |
| termo | ✅ | | ✅ | ✅ (LIKE) |
| coletado_em | ✅ | | ✅ | ✅ |
| **largura** | | ✅ | ❌ | ❌ (recalcula baixando) |
| **altura** | | ✅ | ❌ | ❌ (recalcula baixando) |
| **bytes** | | ✅ | ❌ | ❌ (recalcula baixando) |
| **licenca** | | ✅ | ❌ | ❌ (infere pela origem) |
| **credito** | | ✅ | ❌ | ❌ (parseia descrição via regex) |
| **photo_id_externo** | | ✅ | ❌ | ❌ |
| **owner_nsid** | | ✅ | ❌ | ❌ |
| **geo_lat / geo_lon** | | ✅ | ❌ | ❌ |
| **data_captura** | | ✅ | ❌ | ❌ |
| **hash_imagem (MD5)** | | ✅ | ❌ | ❌ (recalcula) |
| **phash_imagem** | | ✅ | ❌ | ❌ (não usa) |
| **tipo_imagem** | | ✅ | ❌ | ❌ |
| **qualidade_v3** | | ✅ | ❌ | ❌ |
| **indexed_at** | | ✅ | ❌ | ❌ |

**13 dos 15 campos novos NÃO são lidos pelo V3 hoje.** Esse é o gap a fechar.

---

## 4. Os 10 pontos de fricção V3 ↔ Legado

### 🔴 CRÍTICOS (V3 paga custo desnecessário ou perde qualidade)

| # | Problema | Solução | Esforço |
|---|---|---|---|
| **F1** | V3 **baixa imagem em runtime** pra medir largura/altura/bytes (`_enriquecer_dimensoes_imagens`) — custo ~3s × 3 finalistas × 5 termos = **30-45s por pauta** só pra medir | Ler `largura/altura/bytes` diretamente do SELECT quando populados (NULL → baixa como fallback) | 30min |
| **F2** | V3 não usa `qualidade_v3` — recebe candidatas thumbnail+rejeitada e perde tempo descartando | Adicionar `WHERE qualidade_v3 IN ('apta_v3', 'apta_blog')` na query | 15min |
| **F3** | V3 recalcula MD5 a cada uso (paga download + hash) | Usar `hash_imagem` do SELECT (já populado pelos novos coletores) | 20min |
| **F4** | V3 infere licença/crédito por regex/origem em runtime — frágil, perde precisão | Usar `licenca`/`credito` do SELECT (populados explicitamente nos novos) | 30min |
| **F5** | Peso de `banco_midia_legado` = 420 (8º na cascata, abaixo de Wikimedia que tem qualidade pior) | Subdividir por qualidade: `apta_v3=550`, `apta_blog=420` (atual), `thumbnail=200` | 15min |

### 🟠 IMPORTANTES (qualidade editorial)

| # | Problema | Solução | Esforço |
|---|---|---|---|
| **F6** | V3 não usa `phash_imagem` pra dedup similar — pauta nova pode reusar imagem visualmente parecida a outra recente | Adicionar check phash contra `midias_publicadas_politica_v3.db` últimos N dias | 1h |
| **F7** | `_buscar_entidades_legado` usa LIKE sem index em `aliases` — lento | CREATE INDEX em `entidades.aliases` ou FTS5 | 5min |
| **F8** | `_score_imagem` tem regras hardcoded só pra Lula/Ricardo Couto — não escala | Mover regras pro próprio gazetteer (campo `boost_terms` na entidade) | 2h |

### 🟡 PREPARAÇÃO R2 (deixar pronto pra ativar depois)

| # | Problema | Solução | Esforço |
|---|---|---|---|
| **F9 (V3-B014)** | Schema `midias_candidatas.origem` CHECK não aceita `r2_catalogo` | Migration: ALTER CHECK pra incluir `r2_catalogo`. Não ativa o uso ainda, só prepara o schema | 10min |
| **F10** | Peso `r2_cloudflare = 180` (penúltimo) — quando R2 estiver pronto, deve subir | Documentar pesos planejados pós-R2: `r2_catalogo_curado=580` (acima de Wikimedia direto). NÃO mexer agora — só registrar plano | 0 (decisão futura) |

---

## 5. Pré-requisito: auditoria retroativa do banco legado

Hoje os 15 campos novos estão populados apenas em **34 imagens** (as 421 dos smokes — perdidas pelo incidente AGY — e as ~25 novas pós-recovery).

Pra V3 LER esses campos das 345k antigas, precisa **auditoria retroativa**:

- Foco: 153k vinculadas a entidade (escopo prático)
- Roda LOCAL com Cloudflare WARP (destrava Flickr 429)
- Para cada imagem: baixa → mede → calcula hash/phash → infere licença/crédito → atualiza linha
- ETA: ~1-2h overnight com 5 workers
- Documentado em `reference_warp_vpn_destrava_ratelimits`

**Sem essa auditoria**, F1-F5 funcionam só pras 1k/dia novas (organic growth). Lento.

---

## 6. Ordem proposta de execução

| Fase | O que faz | Por quê primeiro | Esforço | Risco |
|---|---|---|---|---|
| **0** | Auditoria retroativa (153k vinculadas) | Sem dados nos campos, F1-F5 ficam inúteis | 2h batch overnight | Baixo (read+update) |
| **1** | F2 + F7 (filtro qualidade_v3 + index aliases) | Quick win — só query/index, 0 risco | 20min | Zero |
| **2** | F1 + F3 + F4 (ler dims/hash/licença/crédito do SELECT) | Reduz custo V3 drasticamente | 1h30 | Médio (mexe em `executar_midia_v3_real.py`) |
| **3** | F5 (subdividir peso legado por qualidade) | Faz `apta_v3` competir com Wikimedia direto | 15min | Médio (muda ranking) |
| **4** | F9 (ALTER CHECK pra `r2_catalogo`) | Prepara schema sem ativar — quando R2 vier, já aceita | 10min | Zero (aditivo) |
| **5** | F6 (dedup phash) | Qualidade editorial — evita repetir imagem similar | 1h | Baixo |
| **6** | F8 (mover boost terms pro gazetteer) | Escalabilidade — refactor sem urgência | 2h | Médio |

**Esforço total**: ~6-7h trabalho + 2h batch noturno.

**Bloqueio mútuo**: nada bloqueia a Fase 0 começar. Fases 1-6 dependem da 0.

---

## 7. Decisão arquitetural pra R2 (preparação, sem ativar)

Quando R2 estiver pronto (sprint Acervo Editorial Codex/GLM), V3 vai precisar:

1. **Schema**: `midias_candidatas.origem` aceita `r2_catalogo` (✅ Fase 4 acima)
2. **Cascata reordenada** (peso `r2_catalogo_curado`):
   - Posição sugerida: **acima de Wikimedia direto** (560) — porque R2 já passou por triagem manual
   - Peso sugerido: `580`
3. **Fonte preferida**: para entidades onde R2 tem cobertura forte (Lula, Trump, Bolsonaro, governadores), V3 deve checar R2 ANTES do legado
4. **Fallback**: se R2 não tiver match com score >100, cai pro legado

Tudo isso fica DOCUMENTADO mas NÃO IMPLEMENTADO até R2 estar pronto.

---

## 8. Métricas de sucesso (como medir que ajustes funcionaram)

Antes (HOJE):
- Custo por pauta para mídia: ~45s (3 candidatas × 15s download+medir)
- Qualidade média candidatas: ~50% retornadas via legado são thumbnail/baixa
- Vínculo a entidade certa: ~70% precisão (regras hardcoded Lula compensam)

Após Fases 0-3:
- **Custo por pauta**: <10s (campos prontos, sem download pra medir)
- **Qualidade média**: 100% apta_v3/apta_blog (filtrado no SQL)
- **Vínculo entidade certa**: medir via Tribunal Visual (Kimi/Gemini valida)

---

## 9. Riscos identificados

| Risco | Mitigação |
|---|---|
| Auditoria retroativa demora mais que 2h | Roda overnight, sem urgência |
| F1-F4 quebram pauta em produção | V3 está PAUSADO — todas mudanças com smoke antes de religar cron |
| F5 muda ranking — algumas pautas escolhem imagem diferente | Esperado e desejado. Smoke com 5 pautas reais antes |
| AGY/Codex/GLM fazem patch concorrente | Esta sprint é minha (Miguel passou). Coordenação via fórum. |
| WARP local cai durante auditoria retroativa | Script é idempotente — retoma de onde parou |

---

## 10. Próximos passos

**Aguardando sanção Miguel pra começar Fase 0** (auditoria retroativa via WARP local).

Se sancionado:
1. Rodo Fase 0 em background (~2h)
2. Em paralelo: preparo patches Fases 1-5 (sem deploy)
3. Quando Fase 0 terminar: aplico Fases 1-5 sequencial com smoke entre cada
4. Fase 6 fica pra sprint futura (refactor não-urgente)

Se Miguel quiser ordem diferente, especificar.

---

### Anexos

- Memória: `reference_banco_midia_canonico_legado` (paths, schema, contagens)
- Memória: `reference_warp_vpn_destrava_ratelimits` (Cloudflare WARP local)
- Mapa V3 do AGY: `/root/V3/reports/agy_mapa_retomada_v3_20260626.md`
- Fila Vision limpa: `/root/V3/reports/agy_fila_vision_limpa_20260626.json` (1.335 imagens)
- Carta AGY sobre paths: `Cerebro/Foruns/inbox_trindade/agy.md` (linhas 32-299)
- Carta dura ao AGY pós-incidente: `Cerebro/Foruns/inbox_trindade/agy.md` (linhas 300-472)

— Claude Code (Daemon)
claude-opus-4-7 · Anthropic
Coordenador da sprint Política V3 — Ajustes legado (delegado por Miguel 26/06 03:25 BRT)
