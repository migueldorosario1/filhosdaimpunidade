---
name: feedback-travessao-denuncia-ia-nunca-usar
description: Travessão (—) denuncia texto de IA no Cafezinho — regra crítica bug
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel 13/08/2026 ~14:00 BRT: *"cuidado com travessão. Não fique usando travessão não. Travessão é muita. Fica aparecendo. Todo mundo vê que é texto de inteligência artificial. Não usa travessão não."*

## Regra

**Nunca usar travessão (—) em texto público** — título, corpo, excerpt, caption de mídia. É sintoma clássico de LLM/IA e denuncia autoria automática ao leitor. Faz parte do BUG #1 do ecossistema ([[feedback-nunca-vazar-metalinguagem-ia-bug-numero-1]]).

Também evitar meia-risca (–) pelo mesmo motivo.

## Substituição por contexto

**Travessão como separador de cláusula (` — ` ou ` – `):**
- → `,` na maioria dos casos: *"O agro é forte — inclusive na exportação"* → *"O agro é forte, inclusive na exportação"*
- → `.` quando são duas ideias independentes: *"A safra bateu recorde — o Brasil consolida liderança"* → *"A safra bateu recorde. O Brasil consolida liderança"*
- → `(...)` quando é aposto/parêntese: *"O texto — sancionado ontem — vale a partir de janeiro"* → *"O texto (sancionado ontem) vale a partir de janeiro"*

**Travessão de fala direta (`— frase`, no início de parágrafo):**
- → aspas: *"— Vou vetar, disse Lula"* → *`"Vou vetar", disse Lula`*
- ou parágrafo comum sem marca: *"O ministro afirmou que vai vetar"*

**Travessão em título:** já era proibido pela regra auditor 7 regras ([[feedback-auditor-titulos-v4-7-regras-canonico]]); esta regra reforça.

## Também evitar (por sintoma IA)

- **Ponto e vírgula excessivo** (`;`) — regra memória antiga [[feedback-modo-enxuto-preservar-worker-v4]]
- **"—" (meia-risca em faixas de números)**: substituir por "a" ou "-" hífen simples. Ex: *"2027—2031"* → *"de 2027 a 2031"* ou *"2027 a 2031"*
- **Frases muito longas com múltiplas subordinadas** — quebrar em 2-3 frases curtas
- **"É importante notar que..."** / **"Vale destacar..."** / **"Cabe ressaltar..."** — remover, entrar direto no fato
- **Adjetivo genérico duplicado**: "belo e impactante", "importante e relevante"

## Detector automático (grep antes de todo patch)

Antes de qualquer `wp_update_post` que toque `post_content` ou `post_title`, checar:
```bash
grep -c "—\|–\|;.*;\|Vale destacar\|Cabe ressaltar\|É importante notar" <arquivo>
```
Se > 0 no material que EU escrevi, revisar antes de aplicar.

## Auditoria retroativa 13/08 ~14:00 BRT

19 posts revisados nesta sessão → **12 com travessão** (263 no total). Vou corrigir em batch:
- 265322 (2) · 265318 (2) · 265353 (1) · 265339 (1) · 265329 (2) · 265196 (1) · 265370 (2) — worker V4 5786 ontem
- 265452 (3) · 265459 (5) · 265381 (1) · 265492 (5) · 265391 (10) — repetidor

Snapshot JSON pré-batch (regra [[feedback-backup-json-pre-batch-wp]]) + patch mecânico com substituição por vírgula (padrão maioria dos casos) + auditoria manual de casos ambíguos.

## Aplicação prática daqui pra frente

**Ao escrever qualquer texto novo** (correção in-place, patch, cartinha em fórum, comentário em canal_trindade que possa virar público): grep mental `—` `–` `;` antes de gravar. Se aparecer, reformular.

**Ao revisar draft do worker/repetidor**: primeira coisa é grep travessão. Se tem, corrigir junto com dedup/título — nunca deixar passar.

**Cartinhas internas em `inbox_trindade/*.md`** são OK usar travessão (ambiente interno) — mas se algum dia migrar pra público, corrigir.

Regras irmãs: [[feedback-nunca-vazar-metalinguagem-ia-bug-numero-1]] · [[feedback-auditor-titulos-v4-7-regras-canonico]] · [[feedback-modo-enxuto-preservar-worker-v4]].
