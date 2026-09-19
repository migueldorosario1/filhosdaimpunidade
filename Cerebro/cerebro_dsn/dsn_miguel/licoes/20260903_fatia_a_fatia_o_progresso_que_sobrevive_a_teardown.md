# Fatia a fatia — o progresso que sobrevive à teardown (TRILHA A)

**Data:** 2026-09-03 (85ª ronda, 02:34 BRT)
**Refs:** Rondas 71ª-85ª do DS-Dell · licoes/20260903_relance_em_ronda_esbarra_na_fisica_e_whisper_parcial_e_zero.md (14ª) · bloco DS-20260903-006

## O quê
O whisper base da TRILHA A (TV GGN, ~54 min) morreu **15 vezes** com a sessão — o job só grava o .srt NO FIM, então execução parcial = ZERO output. O encadeado por **fatias de 5 min com whisper tiny** (1 fatia = 1 .srt gravado ao FIM de cada fatia) morreu na fatia 3 da ronda 84ª e **preservou 4 .srt** (fatia_000 a 003). A retomada na 85ª foi trivial: script com skip dos .srt existentes rodou as fatias 4-10 em ~6 min, cada uma escrevendo o próprio .srt. O desenho em unidades persistíveis converteu a morte da sessão de perda total em pausa retomável.

## Por quê
Cada chamada de comando roda num namespace bwrap novo (`--die-with-parent` + `--unshare-pid`); a teardown do fim da sessão leva os filhos. `nohup` e `setsid` não escapam (confirmado 2×). Logo, em ronda, NENHUM job sobrevive ao fecho da sessão — a única forma de progresso é a **unidade de trabalho que grava output ao fim de cada passo**, não ao fim do todo. O custo por fatia (~45-60s com tiny numa wav de 5 min/16kHz) cabe folgado na vida de uma ronda (~10-15 min), então o encadeado inteiro converge dentro da própria ronda quando a sessão aguenta, e entrega parcial útil quando não aguenta.

## Como aplicar
- Jobs longos (transcrição, processamento, download) em contexto de ronda: **fatiar em unidades de ≤5 min de trabalho** e gravar o artefato de cada unidade no fim dela.
- Retomada por **skip de artefato existente** (se `fatia_NNN.srt` existe, pula) — relance cego do job inteiro é desperdício certo (15 confirmações).
- Antes de relançar, conferir o que o job parcial deixou (ls dos artefatos + log) — o parcial vira ponto de partida, não lixo.
- ETA do job > vida da sessão = redesenhar em fatias, não insistir no relance.
- Whisper tiny (pt) entrega SRT de LOCALIZAÇÃO (com erros de transcrição) — serve para decupagem/corte, não para citação literal.
