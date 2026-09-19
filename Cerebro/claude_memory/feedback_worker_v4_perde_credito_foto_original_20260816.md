---
name: feedback-worker-v4-perde-credito-foto-original-20260816
description: "Bug estrutural worker V4: quando puxa capa de matéria original (cafezinho_image_generator=original_source, cafezinho_image_kind=real), achata caption pra 'Imagem da matéria original publicada por <dominio>' — perde autor real, licença explícita, URL matéria. Cai automaticamente em REPROVA_HOLD_PENDING pelo gate §5 v1. Casos confirmados 16/08: fm 266149 do post 266148 (Ari Versiani/PAC perdido); fm 266132 do post 266131 (padrão similar). Investigação código em curso — bug ainda não localizado no /root/v4_labs/ (grep pelo padrão vazio); pode estar em outro path/serviço. Meu papel: detectar via gate §5, escrever REPROVA_HOLD_PENDING, escalar Grok pra caso concreto + ZCode pra fix estrutural. NUNCA patchear worker V4 sem autorização Miguel (regra [[feedback-v4-producao-cautela-backup-rollback-20260816]])."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Descrição do bug

Quando o worker V4 puxa capa de matéria original (marca `cafezinho_image_generator: original_source` + `cafezinho_image_kind: real`), a metadata da fm fica genérica no formato:

- **post_title**: repete o título do post principal (nome real perdido)
- **post_excerpt** (caption): `"Imagem da matéria original publicada por <dominio>.com.br"`
- **post_content** (description): idem caption
- **nome do arquivo**: `v4-featured-<postid>.jpg` (genérico, sem descritor)

**O que se perde:**
1. Fotógrafo/autor real (ex.: "Ari Versiani/PAC")
2. Banco de imagem original quando republicado (ex.: PAC redistribuído via Agência Brasil)
3. Licença explícita (ex.: CC BY 3.0 Brasil da EBC)
4. URL da matéria original (não vai nem pra `post_meta` do post nem pra `post_content` da fm)

## Impacto no gate §5 v1 (homologado 20:41)

- §5 exige `fonte_licenca_legenda: OK` no recibo `_cafezinho_img_check` para aprovar
- Caption genérica = fonte insuficiente = veredito **REPROVA_HOLD_PENDING** (`ok: false`)
- Post fica em `pending` até correção manual da metadata

## Casos comprovados (16/08/2026)

- **fm 266149 do post 266148** (economia verde Nordeste): crédito real = "© Ari Versiani/PAC" via matéria [Agência Brasil 08/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/projeto-mapeia-caminhos-para-economia-verde-no-nordeste). Meu recibo REPROVA_HOLD_PENDING gravado 21:44.
- **fm 266132 do post 266131** (Lula lança campanha): flaggei no brainstorm de originalidade `CLAUDE-MIGUEL-CHAMADO-DOIS-LOOPS-ORIGINALIDADE-LANCAMENTO-CAMPANHAS-16AGO-20260816-2049`; Claude Laura confirmou no parecer preliminar 21:18.

**Suspeita:** existem mais casos — worker V4 tem provavelmente essa lacuna sempre que `original_source` é agregador (Agência Brasil, Brasil247, etc.). Precisa varredura.

## Solução para o loop (protocolo operacional)

### Detecção rápida durante gate visual

Sinais de alerta na metadata da fm:
- `post_excerpt` começa com "Imagem da matéria original publicada por"
- `post_excerpt == post_content` (redundância suspeita)
- Nome arquivo `v4-featured-*.jpg`
- `cafezinho_image_generator=original_source`

Se qualquer dos 4 casar, tratar como `fonte_licenca_legenda: INSUFICIENTE` e escrever `veredito_final: REPROVA_HOLD_PENDING` (`ok: false`).

### Ação corretiva (caso a caso)

1. **WebSearch** pela matéria original no domínio da caption (`site:<dominio> "<título do post>"`)
2. **WebFetch** da matéria original com prompt específico: "extraia URL da imagem de destaque, legenda literal, crédito/fotógrafo, licença declarada"
3. **Registrar achado no ledger** com bloco `[CLAUDE-MIGUEL-CREDITO-EXTRAIDO-FM-<fm_id>-<TS>]`
4. **Escalar Grok** (via `fila_para_grok.md`) para atualizar metadata da fm com crédito completo — Grok é dono da ponte imagens (nunca patchear worker upstream)
5. Após Grok atualizar: **reescrever meu recibo** com `ok: true` + veredito `APROVA` ou `APROVA_CONTEXTUAL` + novo hash sha256
6. **Agendar** o post normalmente

### Fix estrutural (upstream)

- **NÃO patchear worker V4 sem autorização Miguel** (regra [[feedback-v4-producao-cautela-backup-rollback-20260816]])
- Escalar ZCode via `fila_para_zcode.md` com bloco `[CLAUDE-MIGUEL-ESCALACAO-ZCODE-BUG-WORKER-V4-PERDE-CREDITO-FOTO-20260816-2148]` (já enviado 21:48)
- Fix proposto: quando `original_source`, worker deve varrer na página fonte:
  - `<meta property="og:image">` + `<meta property="og:image:credit">`
  - `<figure><figcaption>`
  - Classes `.credit`, `.foto-credito`, `.image-credit`, `.wp-caption-text`
  - Texto após imagem: padrões `Foto:`, `Crédito:`, `©`, `by`
  - `<a rel="license">` ou classe `.license` no rodapé (EBC = CC BY 3.0 Brasil implícito)
  - Salvar meta nova: `_v4_source_url`, `_v4_source_dominio`, `_v4_credito_extraido`
  - Fallback: caption vazia + `_cafezinho_img_credit_pendente=1` (cai automático em REPROVA_HOLD_PENDING pelo gate)

## Ler bugs em cada ciclo (NOVO — ordem Miguel 21:52)

Miguel pediu ao Loop Miguel + Loop Laura: ler memória de bugs em cada ciclo Vigília para não repetir. Meu compromisso a partir de agora:

- **Passo novo no ritual Slot A e B**: antes de qualquer wp_update_post, executar:
  ```bash
  tail -30 "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/monitoramento_horario/bugs_encontrados/bugs_$(date +%Y-%m-%d).jsonl" 2>/dev/null
  ```
- Grep memórias com tag `bug-`/`gate-`/`worker-` das últimas 48h no MEMORY.md
- Se um bug em curso afeta o post que vou processar, aplicar solução conhecida (não repetir descoberta)

## Origem histórica

- **16/08/2026 21:38**: worker V4 cria post 266148 com fm 266149 (caption genérica)
- **16/08/2026 21:42**: Vision aprova imagem mas metadata reprova por licença
- **16/08/2026 21:44**: escrevo recibo REPROVA_HOLD_PENDING no post 266148
- **16/08/2026 21:44**: escalo Grok via `[CLAUDE-MIGUEL-ESCALACAO-GROK-CREDITO-FM-266149-266148-20260816-2143]`
- **16/08/2026 21:45**: Miguel pergunta "qual crédito é insuficiente?"
- **16/08/2026 21:46**: Miguel pergunta "mas a fonte da foto qual é?"
- **16/08/2026 21:47**: identifico via WebFetch "Ari Versiani/PAC"; Miguel pede investigação estrutural + fix
- **16/08/2026 21:48**: escalo ZCode via `[CLAUDE-MIGUEL-ESCALACAO-ZCODE-BUG-WORKER-V4-PERDE-CREDITO-FOTO-20260816-2148]`
- **16/08/2026 21:52**: Miguel pede fórum de gestão de memórias (paralelo)
- **16/08/2026 21:53**: Miguel dá ordem de cautela V4 (produção não se brinca)

## Relacionados

- [[feedback-v4-producao-cautela-backup-rollback-20260816]] — regra de cautela p/ mexer no V4
- [[feedback-contrato-integridade-imagens-v1-homologado-20260816]] — gate §5 v1 que detecta o bug
- [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]] — regra geral para fix upstream
- [[feedback-nunca-vazar-metalinguagem-ia-bug-numero-1]] — atenção paralela (bugs de forma sutil)
- Fórum: `Cerebro/Foruns/forum_sistema_gestao_memorias_20260816.md` — pra evoluir a leitura de bugs

## Regra âncora

**"Se fm tem caption 'Imagem da matéria original publicada por' + nome 'v4-featured-*' + `cafezinho_image_generator=original_source`: gate §5 = REPROVA_HOLD_PENDING automático. Buscar crédito real na matéria fonte (WebFetch) → escalar Grok pra atualizar metadata → reescrever recibo com ok:true. NÃO patchear worker V4 sozinho (escalar ZCode com plano completo, esperar autorização Miguel)."** — Loop Miguel Vigília V6, 16/08/2026 21:55 BRT
