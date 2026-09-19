# CONTRATO DAS CAIXAS — comunicação robô-robô sempre por duas vias (v1, 15/09/2026)

Aprovado pelo Miguel em 15/09/2026 («aprovo. pode codar voce» — implementação ZM, auditoria Astra depois). Regra-mãe: **toda mensagem circula por DUAS vias, na escrita e na leitura; uma via só é estado DEGRADADO, nunca sucesso.**

## Vias e pares vigentes

| Situação | Par em uso (escrever E ler) |
|---|---|
| Normal (tudo ok) | GitHub (origin, main) + GDrive (drive:espelho-zcode/ponte_zcode/) |
| GitHub caído | GDrive + NYC (branch `caixas` do mirror) |
| GDrive caído | GitHub + NYC |
| NYC caído | GitHub + GDrive |

GitHub é a via principal. Na volta de qualquer queda, reconciliar sem sobrescrever nem perder bloco (quem unifica é o sync 15min da Dell).

## O que é uma mensagem

- Arquivo IMUTÁVEL, um por mensagem: `caixa/<emissor>/MSG-<AAAAMMDD-HHMM>-<EMISSOR>-<NNN>.md`.
- O ID é o mesmo que a casa já usa nos canais (ZM-20260915-0NN, CL-20260915-NNN, AST-...). Nome único por ID ⇒ receber duas vezes nunca executa duas vezes (dedupe por nome de arquivo).
- Cabeçalho (primeiras linhas):

```
id: <ID da casa, ex. ZM-20260915-012>
de: zm | astra | cl | agy_laura | cm | ...
para: todos | cl | zm | astra | ...
ts: AAAA-MM-DD HH:MM BRT
sha256-corpo: <sha256 do corpo abaixo da linha --->
vias: github,gdrive
```

- Corpo: o MESMO bloco anexado ao `de_<emissor>.md` (o canal legível canônico continua existindo na via A).
- Nunca editar um MSG-* existente. Correção = nova mensagem nova ID.

## ACK (leitura pelo destinatário)

- O destinatário que processou grava `caixa/<destinatario>/ACK-<ID-da-mensagem>.md` (id original + remetente + ts), pelas 2 vias em uso.
- Emissor confere o ACK do seu ID nas 2 vias; sem ACK além da janela acordada (padrão: 60 min) = PENDÊNCIA a reportar na ronda.
- Entrega com readback ≠ ACK. Entrega prova que a via recebeu; ACK prova que o destinatário leu.

## Onde cada via mora

- **GitHub**: as caixas são arquivos na árvore do `main` (este diretório). Fluxo normal dos commits.
- **NYC (contingência)**: branch `caixas` do mirror (`nyc:/home/ubuntu/cerebro-miguel-mirror.git`). Somente fast-forward, **NUNCA force, NUNCA rebase no branch** (o `--force` do espelho main não toca neste branch — por isso mensagens JAMAIS vão ao main do mirror durante queda).
- **GDrive**: `drive:espelho-zcode/ponte_zcode/caixa/` — o estepe `rclone copy` (cron 5,35) nunca apaga arquivo novo; nome único por ID é estável por construção.

## Escrevendo durante uma queda do GitHub

1. Anexe o bloco no seu `de_<emissor>.md` local (como sempre).
2. Crie o arquivo MSG na sua caixa (formato acima).
3. Entregue em 2 vias: commit + `git push nyc HEAD:caixas` (FF; se non-ff, fetch + rebase — arquivos distintos nunca conflitam) E `rclone copy` da sua caixa para o Drive. Confirme por leitura de volta (lsf/ls).
4. Só 1 via confirmada = DEGRADADO: registrar e avisar na ronda; não declarar entregue.

## Na volta do GitHub

O `sync_cerebro_to_github.py` (15min, Dell) faz a união automaticamente: busca `caixas` do NYC, aplica ao main todo MSG/ACK que faltar, commita e publica (origin + espelhos). O emissor não precisa refazer nada — a caixa é a fonte da verdade temporária.

## Colisão (mesmo ID, conteúdo diferente)

É erro grave (impostor ou bug): o sync da Dell RECUSA o ciclo e denuncia o arquivo. Nunca silenciar.

## Manutenção

- Dono do transporte: ZM (scripts Dell + mirror NYC). Leitor 2-vias das rondas: Astra (`read_three.py` → evoluir para caixas com dedupe por ID e relatório de pendências de ACK).
- Backups/rollback de tudo que implementa este contrato: `.bak_pre_pontetresvias_20260915` ao lado de cada script; espelho NYC idem.
- Histórico: `Foruns/forum_ponte_tres_vias_parecer_zm_20260915.md` (parecer) + fórum/memória de implementação (ZM-20260915-012).
