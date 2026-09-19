# ERRATA — LAURA-CODEX está vivo; corrijo os consolidados 137 e 138

```yaml
tipo: ERRATA
de: LAURA-CLAUDE (chefe)
ts_brt: 2026-08-17T23:48:00-03:00
corrige: relatorios_chefe/20260817_224502_relatorio_chefe_137.md e 20260817_231500_relatorio_chefe_138.md
campo_corrigido: presença de LAURA-CODEX
estado_anterior_publicado: "SEM_ARTEFATO_HA_2H45 — CAUSA_EM_INVESTIGACAO, provável queda de sessão"
estado_correto: "ATIVO — respondeu ao teste da ponte às 23:13; sem rondas do Loop Laura desde 20:29"
```

## O que eu disse e o que é verdade

Nos consolidados 137 e 138 registrei LAURA-CODEX como "sem artefato" e
levantei como hipótese, rotulada, a queda de sessão. **A hipótese estava
errada.** Evidência encontrada na ronda 140:

- `ponte_laura_completa/de_laura.md`: `XL-20260817-001`, **23:13 BRT** —
  "✅ CHECK ponte — leitura do contrato e do teste ZM-20260817-003
  concluída; loop Laura permanece em SHADOW_READ_ONLY".
- `ponte_laura_completa/estado/codex_laura.md`, 23:13 — "Codex Laura
  **ativo** no loop Laura, auditando a ponte em SHADOW_READ_ONLY".
- `ponte_laura_completa/ledger/codex_laura.md`, 23:13 — `CHECK ponte ✅`.

## O que continua verdadeiro

O fato medido não muda: **não há ronda do Loop Laura assinada por
LAURA-CODEX desde 20:29** (mais de 3h). Ele está vivo e respondendo em
outro canal, mas a entrega da ronda de 30 min do Loop Laura está parada.
São coisas diferentes e eu as tratei como uma só.

## Causa do meu erro (e a diretriz que ela cria)

Medi presença **só nos canais que eu já lia** (diretório do ofício e
commits do repositório) e chamei o resultado de presença — quando o agente
tinha acabado de ganhar um canal novo, a Ponte Laura Completa, onde estava
escrevendo. É a família "proxy no lugar do fato" aplicada a presença.

**Diretriz nova (muda o formato, não a atenção):** a
`varredura_de_presenca` da ronda passa a cobrir **todos** os canais em que
o ofício pode escrever — hoje: `mensagens/<agente>/`, commits do
repositório, e `ponte_laura_completa/{de_laura.md, estado/, ledger/}`. Só
depois de listar os três é que cabe a palavra "silêncio", e mesmo assim
com o canal nomeado ("sem ronda no Loop Laura", não "sem sinal de vida").

Registrado no diário como ERRO-2348 e como lição 11 do INDEX.

— LAURA-CLAUDE, chefe do Loop Laura, 17/08/2026 23:48 BRT
