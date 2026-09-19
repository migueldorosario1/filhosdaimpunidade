# Relatório — Faxina diária 11/08/2026 — NYC rodada 01

**Missão:** `memoria_missao_faxina_diaria_legacy_20260811.md`  
**Ambiente:** Nova York (`198.199.121.136`)  
**Resultado:** concluído e verificado

## Censo inicial

- Local: 72% de disco usado.
- NYC: 68%.
- rio-ag: 84%, prioridade alta da próxima rodada.
- Tencent: SSH recusado novamente; permanece pendente e não saneado.

## Lote canário

Oito arquivos de código explicitamente marcados como legacy ou desativados foram selecionados na raiz `/root`:

1. `agente_master_trends_legacy.py`
2. `fix_bot.py.legacy`
3. `agente_master_lula_legacy.py`
4. `bot_augusto.py.legacy`
5. `maestro_editorial_legacy.py`
6. `agente_turismo_embratur.py.legacy`
7. `MT_agente_ferroviario.py.LEGACY_DISABLED_20260609_0353_claude`
8. `agente_master_trends_v9_legacy.py`

Tamanho original total: 226.117 bytes.

Arquivos que continham `chaves` ou `.env` foram excluídos deliberadamente desta rodada. Segredos não podem entrar em pacote comum de faxina.

## Prova de inatividade

Para todos os oito candidatos:

- processos: zero;
- crons: zero;
- serviços systemd: zero;
- symlinks: zero;
- imports ou referências executáveis por caminho em AST dos arquivos ativos `/root/*.py`: zero.

## Arquivo e verificação B2

Destino:

`b2:failover-cafezinho1/faxina/nyc/legacy-code/2026-08/rodada_20260811_01/`

Objetos:

- `legacy_code_20260811_01.tar.gz` — 67.507 bytes — SHA-256 `8da37f2f9108ef13de6ac14fa3e5e3a31cfb7e5317cc31daba7f2617d874ffe0`;
- `MANIFESTO_FAXINA.jsonl` — 6.096 bytes — SHA-256 `49baa3905daf455e14b0bacd8e523b7998e215546fe1e038f520787bbe4886f1`;
- `SHA256SUMS`.

O hash dos dois objetos principais foi recalculado com `rclone cat` diretamente do Backblaze e coincidiu com o original. Depois da retirada dos arquivos quentes, o pacote foi lido novamente do B2 e manteve o mesmo hash.

## Retirada e smoke

- oito originais removidos explicitamente da raiz, sem glob;
- arquivo tar de staging removido do servidor após verificação;
- manifesto e checksums pequenos mantidos em `/root/faxina_diaria/20260811_01/`;
- `augusto-cafezinho.service`: ativo;
- `mayra-cafezinho.service`: ativo;
- teste anti-legacy V4: 3/3 verde;
- `py_compile` do worker, runtime e bot Zizilinda: verde;
- disco NYC permaneceu em 68% — ganho pequeno, pois o lote foi escolhido pela segurança, não pelo volume.

## Espelho do manifesto no Cérebro

- `MANIFESTO_FAXINA_NYC_01.jsonl`
- `SHA256SUMS_NYC_01`

## Próximas prioridades

1. rio-ag em 84%: encontrar volume legacy relevante e provar inatividade antes de arquivar.
2. Tencent: repetir conexão; quando responder, localizar o backend antigo da Zizilinda e demais legacy soltos.
3. NYC: tratar backups antigos da raiz por classes, preservando rollbacks recentes e isolando cofres.
4. Local: revisar espelhos divergentes e arquivos históricos fora de `legacy`/Dados Frios.
