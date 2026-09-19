# Relance em ronda esbarra na física — e whisper parcial vale ZERO

**Data:** 2026-09-03 · **Ronda:** DS-20260903-004 (83º CHECK) · **Tema:** TRILHA A (transcrição TV GGN) + chegada de ordens do dono

## O quê
O whisper da TRILHA A (TV GGN, wav 16k 103MB, ~54 min de áudio) morreu pela 14ª vez. O relance da 82ª (01:06) parou em 3% (~01:09). Meu relance 01:31 com `setsid nohup` (o método que persistiu na 72ª para o DVR) **também morreu**: cada chamada de comando roda num namespace bwrap novo (`--die-with-parent` + `--unshare-pid`) e a teardown do fim da chamada leva os filhos junto — setsid não escapa do namespace. E o achado que muda a leitura: **o whisper só grava o .srt NO FIM da transcrição** → toda execução parcial produz ZERO output (13 logs de progresso, nenhum arquivo .srt). Relance cego em ronda = desperdício certo.

De brinde, a ordem do dono viajou em COMMIT: a DSC-060 (FALA do Miguel ~00:4x, V4.2 Investimento×Estatística separados no espelho, teste AGORA) só chegou ao origin às 01:23 (commit 780c3141 do ZM) — a minha 82ª grepou "sem FALA NOVA" às 01:05, 18 minutos antes do commit; o Ideias (01:18) e o Chefe (01:20) também não a viram. Eu fui o 1º bloco de ronda a registrá-la.

## Por quê
- **Física da sessão:** o harness não dá processo persistente entre chamadas; cada `bash` é um namespace novo que morre com a chamada. A persistência da 72ª (setsid nohup sobreviveu ao DVR) era de outra configuração — não replicar sem testar.
- **Granularidade do output:** ferramentas que só escrevem no fim (whisper, e provavelmente outras de transcrição/geração longa) transformam "progresso parcial" em "nada" — diferente de um download (arquivo .part cresce e serve).
- **Ordens viajam por commit:** o de_dell local/clone atrasa em relação ao origin; a FALA do Miguel pode existir no origin antes de qualquer ronda a ver. Quem só grepou o clone às 01:05 não viu a ordem que já estava no origin às 00:5x (commit 01:23).

## Como aplicar
1. **Tarefa longa que EU assumi:** na abertura da ronda, verificar pgrep + log + (crucial) se a ferramenta escreve incremental ou só no fim. Se só no fim → execução parcial = zero; não relancear às cegas.
2. **Ao bater o 14º insucesso do mesmo padrão:** parar e escalar a decisão estrutural (a: tencent com persistência real; b: sessão dedicada longa; c: fatias pequenas com modelo menor que convergem em rondas). Vigia honesto reporta o limite físico em vez de tentar a 15ª.
3. **Ordem do dono:** na abertura, pull --ff-only + grep DSC no origin (não no clone local atrasado). Número e "falas novas" saem do origin (DS-024, confirmado mais uma vez).
4. **Espelho ≠ portal:** teste autorizado no espelho não autoriza nada no portal principal — registrar a separação quando a ordem diz "publica no espelho".

Refs: DS-20260903-004 · lições irmãs 20260902_job_background_morre_com_a_sessao_relance_na_abertura.md · 20260902_canonico_local_atrasado_leia_pelo_origin.md · DSC-20260903-060 · ZM commit 780c3141.
