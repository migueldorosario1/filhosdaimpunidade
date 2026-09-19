# 🧊 Fórum — Emagrecimento do Workspace + Migração Nuvem-First (2026-07-22)

> **Tema:** Redução do workspace `Antigravity Google` de 153G → 23G e backup escalonado do `Dados_Frios` (131G) para o Google Drive em ~7 madrugadas.
> **Executante:** ZCode/Kimi (terminal local, fora da IDE) a pedido do Miguel.
> **Memória técnica completa:** `../MEMORIA/memoria_emagrecimento_workspace_nuvem_first_20260722.md`

## Contexto

- Antigravity (IDE) não conseguia mais abrir: workspace com 153G.
- Descoberta de segurança vital: ~75G críticos (`doc lawfare oab` 61G + `pautas editoriais` 14G) existiam **só no disco local**, sem espelho no Drive.
- Google Drive: 30TB totais, apenas ~472G usados — espaço soberano disponível.

## Decisões (martelo batido)

1. **Estratégia em 2 tempos:** primeiro tirar o peso de dentro do workspace (move local, instantâneo, nada apagado) → IDE volta a abrir; depois upload com calma.
2. **`~/Dados_Frios/`** criado como área de espera fora da IDE (131G). Nada foi deletado do disco.
3. **Workspace final: 23G** — só código vivo, Cérebro, scripts de cron e o projeto ativo do livro (`Outros/novo livro`, sprint Vol. 1 — **permanece no workspace**, foi movido por engano e devolvido no mesmo dia).
4. **Backup escalonado:** script `~/bin/backup_semana_gdrive.sh`, cron **03:00 toda madrugada**, cota ~17 GiB/noite, fila priorizada (crítico sem backup primeiro), idempotente — `rclone copy` pula o que já é idêntico no Drive (nada repete; orlando diniz e Jornais do dia já tinham partes lá).
5. **Dedup por destino canônico:** `orlando diniz` → `gdrive:orlando diniz`; `Jornais do dia` → `gdrive:Jornais do dia`; demais → `gdrive:Dados_Frios/<pasta>`.
6. **Cron quebrado desativado:** Painel CCTV v5 (`@reboot`) e `watchdog_painel.sh` (1/min) apontavam para `Legacy20260610`, que saiu do workspace em 17/07. Painel estava morto desde então. Entradas comentadas no crontab com tag `DESATIVADO 2026-07-22`. Decisão do Miguel: desativar (não reapontar).
7. **Só apagar `Dados_Frios` local depois** de `rclone check` 100% em toda a fila (verificação final ao fim das 7 noites).

## Estado ao fim do dia 22/07

- Workspace: **23G** ✅ | Dados_Frios: **131G** (fila de upload) | Disco: ~258G usados
- Primeira noite de upload: **madrugada 22→23/07, 03:00**
- Log: `~/log/backup_semana_gdrive.log` | Estado da fila: `~/log/backup_semana_estado.txt`

## Pendências

- [ ] Ao fim da fila: `rclone check` completo → só então apagar `~/Dados_Frios` (libera ~131G no disco).
- [ ] Opcional: `rclone mount gdrive: ~/Drive --vfs-cache-mode full` para acesso sob demanda aos dados frios sem baixar.
- [ ] Regra da casa: dado novo nasce em pasta sincronizada; local nunca mais é cópia única.
