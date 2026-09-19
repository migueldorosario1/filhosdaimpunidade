# Relatório — rodada diária 02 — rio-ag

Data: 11/08/2026  
Host: `159.89.185.209` (`agente-clone-01`)  
Resultado: auditoria não destrutiva; candidato preservado

## Decisão

`/root/gsn_remote` não foi tratado como lixo. O último commit e a pausa operacional são de 07/08/2026, apenas quatro dias antes da auditoria.

Miguel definiu a regra canônica: somente após mais de 15 dias comprovadamente inativo um item pode virar candidato, e mesmo então qualquer ação depende de consulta explícita. Nenhum arquivo do candidato foi removido, movido, compactado ou substituído.

## Provas coletadas

O repositório está limpo, no branch `main`, com HEAD local e `origin/main` iguais a `36f86dfac0576201a82bf5dd906bec0dc57042e8`. Não há processo, serviço ou cron ativo usando `/root/gsn_remote`; os crons GSN estão comentados desde 07/08.

Isso prova pausa, não descarte. O disco permaneceu em 84%, e `/root/gsn_remote/gsn` continuou presente após a auditoria.

## Indexação integral

Foram indexadas 13.502 entradas: 12.036 arquivos, 1.445 diretórios e 21 links. O volume lógico dos arquivos catalogados foi 1.756.394.367 bytes.

O `.env.local` rastreado contém a variável `VERCEL_OIDC_TOKEN`. Por segurança, o índice registra caminho, tamanho, data, modo e classificação, mas não contém o valor nem o hash desse arquivo.

## Evidências e verificação

- Índice local: `INVENTARIO_GSN_RIO_AG_20260811_02.jsonl.gz`
- Resumo local: `RESUMO_AUDITORIA_GSN_RIO_AG_20260811_02.json`
- SHA-256 do índice: `6e800c08c56aeb41030f188858b8a4687179687f5d3aa3aec09196ee521b0662`
- SHA-256 do resumo: `f6f35a2459d9aaa60fce640468f7e26fa99025376c83773cb4a042963fdc9f17`
- B2: `b2:failover-cafezinho1/faxina/rio-ag/auditorias/2026-08/rodada_20260811_02/`

Os dois hashes foram recalculados por leitura remota via `rclone cat` e coincidiram. As cópias espelhadas no Cérebro também passaram em `sha256sum -c`.

## Pendências

O lote permanece em observação e não pode voltar à pauta antes de ultrapassar 15 dias contínuos de inatividade. Mesmo depois disso, é obrigatória nova prova de estado e consulta a Miguel.

O token Vercel rastreado precisa de decisão de rotação/revogação e eventual saneamento do histórico Git. Seu valor não foi copiado nem exposto nesta rodada.
