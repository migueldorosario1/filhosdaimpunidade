# Fórum — Espelho do ZCode do Miguel no computador Laura

**Data:** 2026-08-17 ~20:10 BRT · **Autor:** ZCode/DeepSeek (ordem do Miguel) · **Tema Duplo:** com `Memorias/memoria_espelho_zcode_laura_20260817.md`

## Decisão (ordem do Miguel)

Espelhar o ZCode do Dell (Miguel) no ZCode recém-instalado na Laura (Samsung Galaxy Book Go, Windows 11 ARM64) — **via pendrive/arquivo offline**: um pacote único com prompt (regras permanentes), explicações (guia), memórias do ZCode, configuração e o Cérebro completo, para o ZCode de lá "ficar exatamente igual".

## O que aconteceu (pronto)

- Pacote gerado em `~/ZCodeProject/espelho_zcode_laura/`:
  - `LEIA_PRIMEIRO_ESPELHO_LAURA.md` — guia completo (passo a passo Windows, prompt de ativação, checklist, sincronização contínua);
  - `AGENTS.md` — regras permanentes do Miguel (15,5 KB, caminhos Linux — o ZCode da Laura faz o replace p/ Windows);
  - `memoria_zcode/` — 94 memórias auto do ZCode (664 KB, `MEMORY.md` = índice);
  - `cerebro.zip` — Cérebro Imortal completo (173 MB → 48 MB compactados);
  - `config_zcode/` (config.json + fallback_config.json) e `hooks/` (credito_vigilia.py + llm_fallback.py) — **verificados sem segredos embutidos** (só leem variáveis de ambiente).
- Decisões de segurança: NÃO vão no pacote valores de chaves (Cofre), automações/crons (são por máquina), sessões/histórico, logs/estados da vigília.
- Tema Duplo catalogado no `CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md` + linha em `CEREBRO_NODE_ATUALIZACOES.md`.

## O que falta

1. Miguel copiar a pasta para o pendrive (pendrive não estava montado no Dell na hora da geração).
2. Na Laura: descompactar `cerebro.zip` em `Downloads\Antigravity Google\Cerebro\`, instalar `AGENTS.md` em `.zcode\`, pedir ao ZCode de lá para copiar/ler as memórias (prompt de ativação está no guia — Parte B).
3. Roda o checklist do guia e reportar.

## O que preciso de você (Miguel)

Espetar o pendrive (ou copiar a pasta) e colar o prompt da Parte B do guia no ZCode da Laura. Depois me conte o report dele que eu comparo com o estado daqui.

## ADENDO 17/08/2026 20:54 — espelhamento no Google Drive

Ordem do Miguel: subir o pacote ao Google Drive em `espelho-zcode/` na RAIZ. Feito via `rclone copy ~/ZCodeProject/espelho_zcode_laura drive:espelho-zcode` (remotes `drive:` e `gdrive:` apontam para a MESMA conta). Verificado: **101 objetos, 46,1 MiB**. O pacote agora existe em 2 lugares: Dell (`~/ZCodeProject/espelho_zcode_laura/`) e Drive (`espelho-zcode/`). Próximos passos inalterados: ativar na Laura (Parte B do guia).

## ADENDO 17/08/2026 22:06 — gravação no pendrive

Ordem do Miguel: gravar o pacote no pendrive recém-encaixado. Pendrive = `/dev/sda1` (exFAT, 58,6 GB) montado em `/media/migueldorosario/2079-8A26`. Copiado via `rsync -rlt --no-perms` para `espelho_zcode_laura/` na RAIZ do pendrive + `sync`. Verificado: **101 arquivos, 59 MB (cerebro.zip 46 MB)**. Pacote agora em 3 lugares: Dell, Drive (`espelho-zcode/`) e pendrive. Pronto para ativar na Laura (Parte B do guia).

## ADENDO 17/08/2026 22:20 — inventário das automações (pergunta do Miguel: "tem as memórias das tarefas agendadas?")

Resposta e ação: o pacote JÁ trazia as memórias DESCRITIVAS das tarefas (memoria_zcode/agendamento-vigilia-trindade-cafezinho.md, custos-reducao-automacoes-20260817.md, auditoria-backup-vigilia-20260813.md, cerebro-backup-locais.md, cadencia-boletim-baleia.md + fóruns/memórias do Cérebro), mas NÃO o banco vivo de automações (`tasks-index.sqlite` — não migra: é por máquina). Gerado `automatizacoes_inventario.md` (4 automações ativas do CronList: CCTV 8/8h, Caçadora 1/1h, Faxina 2h/4h madrugada, Vigília 4/4h-6/6h + crons de servidor + regra de failover só com ordem do Miguel) — adicionado ao pacote do Dell e ao Drive (`espelho-zcode/`, 102 objetos). **Pendrive: removido do PC antes da cópia desses 2 arquivos (inventário + guia atualizado) — ele leva a versão original completa (101 arquivos), que funciona igual; se for re-espetado, copiar os 2 arquivos.**

## ADENDO 17/08/2026 22:24 — pendrive re-espetado, pacote completado

Copiados os 2 arquivos que faltavam (`automatizacoes_inventario.md` + `LEIA_PRIMEIRO_ESPELHO_LAURA.md` atualizado) + `sync`. Pendrive agora com **102 arquivos, 59 MB** — idêntico ao pacote do Dell (diff do guia = IDENTICOS). Pendrive pronto e completo para a Laura.
