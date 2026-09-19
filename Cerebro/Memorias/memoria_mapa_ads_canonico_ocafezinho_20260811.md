# Memória Técnica — Mapa Ads Canônico ocafezinho.com (auditoria read-only)

**Data:** 2026-08-11 07:25 BRT
**Autor:** ZCode (GLM-5.2 Z.ai)
**Missão pai:** Sprint Visual Cafezinho (transferência do Claude 11/08 07:12 BRT)
**Sub-etapa:** "Decodificar ads do canônico" (investigação pendente §9.1 do fórum de transferência)
**Fórum-irmão:** `Cerebro/Foruns/forum_mapa_ads_canonico_ocafezinho_20260811.md`
**Tipo:** READ-ONLY — nenhuma escrita em produção, nenhuma edição de plugin/DB

---

## 1. Estado da missão

- **O que aconteceu:** aceitei a transferência do sprint do Claude (cartinha `[CLAUDE-TRANSFER-SPRINT-VISUAL-CAFEZINHO-ZCODE-20260811-0815]`), li o fórum completo + monitoramento, fiz verificação de sanidade do espelho (acesso SSH ✅, 14 rollbacks ✅, mu-plugin calhau v1.1 ✅), e executei a primeira sub-etapa pendente: decodificar e mapear todos os ads do canônico.
- **Resultado:** mapa completo entregue (fórum-irmão) + 4 retratações factuais ao fórum do Claude (publisher ID errado, contagem de blocos errada, Quick AdSense e Colabs não existem).
- **O que falta:** decisão do Miguel sobre próximo passo — (a) port incremental Coluna Editor → blocos → single, (b) validar slots `.ad-space` vazios via browser headless primeiro, (c) continuar iterando espelho.
- **O que preciso do Miguel:** escolher a direção (pergunta já formulada via AskUserQuestion — resposta: "Decodificar ads do canônico", **concluída**).

---

## 2. Arquivos tocados

### Criados (Cérebro)
- `Cerebro/Foruns/forum_mapa_ads_canonico_ocafezinho_20260811.md` — fórum com mapa + retratações (decisões resumidas)
- `Cerebro/Memorias/memoria_mapa_ads_canonico_ocafezinho_20260811.md` — ESTA memória (log técnico)
- `Cerebro/Foruns/inbox_trindade/claude.md` — adendo com aceite da transferência (tag `[ZCODE-ACEITE-SPRINT-VISUAL-CAFEZINHO-GLM52-20260811]`)
- `Cerebro/MONITORAMENTO_DE_TRABALHO.md` — linha "SPRINT VISUAL CAFEZINHO" adicionada ao quadro "Em andamento AGORA"

### Criados (local /tmp, evidência)
- `/tmp/adiag_decode_ads_v1.php` — script PHP decodificador
- `/tmp/adiag_work/adiag_ads_full.json` — dump JSON completo decodificado (46KB)
- `/tmp/adiag_work/adiag_mapa_final.json` — mapa estruturado (19 blocos + globais)
- `/tmp/adiag_work/adiag_mapa.tsv` — TSV tabular de todos 85 blocos
- `/tmp/adiag_work/analyze.py`, `analyze2.py` — scripts de análise
- `/tmp/adiag_work/wpcode_raw.txt` — raw wpcode_snippets (49KB, latin-1)
- `/tmp/adiag_work/wpcode_decode.php`, `wpcode_decode2.php`, `ihaf_check.php`, `list_plugins.php` — scripts auxiliares

### Copiados pro canônico (temporários, /tmp — podem ser limpos depois)
- `cafezinho-wp:/tmp/adiag_decode_ads_v1.php`
- `cafezinho-wp:/tmp/adiag_ads_full.json`
- `cafezinho-wp:/tmp/list_plugins.php`, `/tmp/ihaf.php`, `/tmp/ihaf_check.php`, `/tmp/wpcode_decode.php`, `/tmp/wpcode_decode2.php`, `/tmp/wpcode_raw.txt`

### NÃO modificados (read-only garantido)
- `wp_options.ad_inserter` — só SELECT, nunca UPDATE/DELETE
- `wp_options.wpcode_snippets` — só SELECT
- `wp_options.wpc_inner_header_wide_ad` — só SELECT
- `wp_options.active_plugins` — só SELECT
- Qualquer arquivo do tema/mu-plugins do canônico — intocado
- Qualquer arquivo do espelho — intocado nesta etapa

---

## 3. Comandos executados (log reproduzível)

### 3.1 Acessos SSH confirmados
```bash
ssh root@159.65.177.60 'hostname'        # → cafezinho-news-espelho (espelho)
ssh cafezinho-wp 'hostname'              # → us65.serverdo.in (canônico)
```

### 3.2 Decodificação ad_inserter
```bash
# Script PHP local → scp → executa no canônico
scp /tmp/adiag_decode_ads_v1.php cafezinho-wp:/tmp/
ssh cafezinho-wp 'php /tmp/adiag_decode_ads_v1.php'
# Saída: TOTAL_BLOCKS=90, FIRST_BLOCK_ID=1, FIRST_BLOCK_TOP_KEYS=[code,disable_insertion,...]
# Arquivo gerado: /tmp/adiag_ads_full.json (46KB)

# Copiar pra local pra analisar
scp cafezinho-wp:/tmp/adiag_ads_full.json /tmp/adiag_work/

# Análise local
python3 /tmp/adiag_work/analyze2.py
# Saída-chave: used_blocks=[14,15,17,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
#              (19 blocos, mas bloco 14 code_len=0 = placeholder vazio)
```

### 3.3 Validação publisher ID real (AMP)
```bash
curl -sL "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/amp/" \
  | grep -oE 'data-slot="[^"]*"' | sort -u
# 15 ad-units únicos, TODOS com prefixo /21715141650,22670554696/
# ZERO ocorrências de 21622511100
```

### 3.4 Validação non-AMP (sem GAM)
```bash
curl -sL "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/" \
  | grep -oE "(googletag|adsbygoogle|gpt\.js|ca-pub-|/21622511100/|/21715141650)"
# → só "googletag" 1x (GTM data layer, não ad call)
# → sem gpt.js, sem adsbygoogle, sem publisher IDs

curl -sL "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/" \
  | grep -c "ad-space"
# → 18 slots .ad-space vazios

curl -sL "https://www.ocafezinho.com/2026/08/10/lula-reconquista-as-capitais/" \
  | grep -c "teads"
# → 1 (bloco 17, Teads page 86345)
```

### 3.5 Plugins ativos (43 total)
```bash
scp /tmp/adiag_work/list_plugins.php cafezinho-wp:/tmp/
ssh cafezinho-wp 'php /tmp/list_plugins.php'
# Ads-related ativos: ad-inserter, ads-txt, insert-headers-and-footers
# (NÃO há quick-adsense, NÃO há colabs, NÃO há adsense nenhum)
# AMP: accelerated-mobile-pages/accelerated-moblie-pages.php
```

### 3.6 wpc_inner_header_wide_ad (360yield legado)
```bash
ssh cafezinho-wp 'php /tmp/ihaf_check.php'
# OPTION wpc_inner_header_wide_ad (772 bytes):
#   document.write('<script src="http://ad.360yield.com/adj?p=739943&w=728&h=90">')
# ⚠️ HTTP não-HTTPS = mixed content (LV-005)
```

### 3.7 wpcode_snippets (não contém ads)
```bash
scp /tmp/adiag_work/wpcode_decode2.php cafezinho-wp:/tmp/
ssh cafezinho-wp 'php /tmp/wpcode_decode2.php'
# Raw 50.344 bytes; unserialize falha (encoding); fallback grep
scp cafezinho-wp:/tmp/wpcode_raw.txt /tmp/adiag_work/

python3 -c "
raw = open('/tmp/adiag_work/wpcode_raw.txt', encoding='latin-1').read()
for pat in ['21622511100','googletag','adsbygoogle','teads','360yield','doubleclick']:
    c = raw.count(pat)
    if c: print(f'{pat}: {c}')
# → nenhum pattern de ad encontrado
"
# wpcode_snippets = 17 snippets funcionais (noindex pruning, Denakop, trava anti-repetição, etc.)
```

### 3.8 ads.txt
```bash
curl -sL "https://www.ocafezinho.com/ads.txt" | grep -cE "^[a-z]"
# → 1822 linhas de vendors (richaudience, rubicon, appnexus, pubmatic, criteo,
#   smartadserver, indexexchange, onetag, triplelift, amxrtb, contextweb, etc.)
```

---

## 4. Hashes de evidência (integridade)

```bash
sha256sum /tmp/adiag_work/adiag_ads_full.json
# (rodar quando gravar backup definitivo)

sha256sum /tmp/adiag_work/adiag_mapa_final.json
# (idem)
```

**Não houve commit** (workspace `/home/migueldorosario/ZCodeProject` não é git repo do Cérebro; Cérebro é espelhado separadamente por backup total — automação `*/30` id `automation-647b2f13`).

---

## 5. Testes feitos

| Teste | Resultado |
|---|---|
| Acesso SSH canônico (`cafezinho-wp`) | ✅ `us65.serverdo.in` |
| Acesso SSH espelho (`root@159.65.177.60`) | ✅ `cafezinho-news-espelho` |
| Decodificação `ad_inserter` (PHP unserialize) | ✅ 90 entradas, 19 used_blocks |
| Publisher ID real no AMP ao vivo | ✅ `/21715141650,22670554696/` (não 21622511100) |
| 21622511100 aparece no ad_inserter? | ✅ 0 ocorrências (confirma fórum Claude errado) |
| gpt.js/adsbygoogle no non-AMP? | ✅ 0 (só GTM googletag 1x) |
| Slots `.ad-space` non-AMP | ✅ 18 vazios |
| Teads no non-AMP | ✅ 1 (bloco 17) |
| Quick AdSense plugin existe? | ✅ NÃO (nem instalado) |
| Colabs AdSense plugin existe? | ✅ NÃO (nem instalado) |
| wpcode_snippets contém ads? | ✅ NÃO (17 snippets funcionais) |
| ihaf_insert_header vazio? | ✅ sim (legacy inerte) |

---

## 6. Decisões tomadas

1. **Aceitar a transferência do sprint** do Claude sem reservas bloqueantes (sanidade do espelho confirmada).
2. **Escolher "Decodificar ads do canônico"** como primeira sub-etapa (pergunta via AskUserQuestion, resposta do Miguel) — trabalho 100% read-only, alinha com a pendência §9.1 do fórum do Claude.
3. **Não tocar no canônico** além de SELECT/leitura — toda escrita requer plano MD aprovado (6 fases cirúrgicas).
4. **Registrar retratações ao Claude** em vez de corrigir silenciosamente o fórum dele — proveniência e auditabilidade são regras do ecossistema.

---

## 7. Próximos passos sugeridos (ordem de prioridade)

1. **Browser headless nos slots `.ad-space` vazios** — confirmar se ficam realmente vazios ou se JS deferred os preenche. Skill disponível: `browser-use:web-gui-tester`. Resolve a hipótese §3 do fórum.
2. **Plano MD de port incremental** — se Miguel aprovar, começar pela Coluna do Editor (etapa mais isolada).
3. **Limpar /tmp do canônico** — os scripts PHP temporários (`adiag_*`, `list_plugins`, `wpcode_*`, `ihaf*`) podem ser removidos depois da auditoria.

---

## 8. Referências cruzadas

- **Fórum de transferência (Claude):** `Cerebro/Foruns/forum_transfer_sprint_visual_cafezinho_zcode_20260811.md`
- **Fórum-irmão desta memória:** `Cerebro/Foruns/forum_mapa_ads_canonico_ocafezinho_20260811.md`
- **Bugs lab visual JSONL:** `Cerebro/monitoramento_horario/lab_visual_bugs/bugs_2026-08-11.jsonl` (adicionar LV-005/006/007)
- **Monitoramento:** `Cerebro/MONITORAMENTO_DE_TRABALHO.md` (linha "SPRINT VISUAL CAFEZINHO")
- **Contrato port cirúrgico:** memory `feedback-canonico-port-do-espelho-cirurgico` (6 fases)
- **Inbox Claude:** `Cerebro/Foruns/inbox_trindade/claude.md` (tag aceite + retratações pendentes de ping)

---

## Assinatura

**ZCode (GLM-5.2 Z.ai)** — sessão fallback final
Workspace: `ZCodeProject`
Timestamp: 2026-08-11 07:25 BRT
