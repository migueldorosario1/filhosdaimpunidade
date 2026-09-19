# Memória — Espelho do ZCode do Miguel no computador Laura (log técnico)

**Data:** 2026-08-17 ~20:10 BRT · **Autor:** ZCode/DeepSeek · **Fórum:** `Foruns/forum_espelho_zcode_laura_20260817.md`

## Contexto

Miguel instalou o ZCode na Laura (Windows 11 ARM64) e pediu: (1) certificar que toda a memória está no pacote; (2) criar espelho do ZCode daqui para lá; (3) gerar arquivo com prompt + explicações + memórias + configurações para subir via pendrive.

## Levantamento feito (Dell/Ubuntu)

- Regras permanentes: `~/.zcode/AGENTS.md` (15.541 bytes).
- Memória auto do ZCode: `~/.zcode/cli/memories/projects/zcodeproject-1382c933b558c0cf/memory/` — 94 arquivos, 664 KB (outro projeto `ponte_smoke-*` = 16 KB de teste, EXCLUÍDO do pacote).
- Config: `~/.zcode/cli/config.json` (1.752 B; modelo `397f633c-73af-424a-a8fa-552e7818e123/deepseek-v4-pro`; hooks UserPromptSubmit/SessionStart; provider kimi openai-compatible) + `~/.zcode/hooks/fallback_config.json` (224 B).
- Hooks: `~/.zcode/hooks/credito_vigilia.py` (28.282 B) + `llm_fallback.py` (27.899 B). **Varredura de segredos (grep sk-/api_key/token/secret/password): LIMPO nos 4 arquivos** — scripts só leem env (`ZHIPU_CODING_API_KEY=`, `DEEPSEEK_API_KEY=`) de fora. Incluídos com segurança.
- Cérebro: `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/` = 173 MB.
- Pendrive: não montado no momento da geração (`lsblk` sem /dev/sd*; /media vazio).

## Pacote gerado

`/home/migueldorosario/ZCodeProject/espelho_zcode_laura/` (criado 17/08 20:07):

```
AGENTS.md                        15.541 B   (cp ~/.zcode/AGENTS.md)
LEIA_PRIMEIRO_ESPELHO_LAURA.md   (guia: Partes A-D + checklist + prompt de ativação)
memoria_zcode/                   94 arquivos, 664 KB (cp -r da pasta memory do projeto)
cerebro.zip                      47.786.515 B (~46 MB; zip -rq de Cerebro 173 MB)
config_zcode/config.json         1.752 B
config_zcode/fallback_config.json 224 B
hooks/credito_vigilia.py         28.282 B
hooks/llm_fallback.py            27.899 B
```

## Decisões registradas

1. **Não migram:** valores de segredos (Cofre de Chaves — o Cérebro que vai junto só aponta onde estão), automações/crons (por máquina; duplicar faria o Laura disparar os mesmos jobs), sessões/histórico (~/.zcode/v2), logs/estados da vigília (regeneráveis).
2. **AGENTS.md vai fiel, com replace de caminhos na Laura:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/` → `C:\Users\<SEU_USER>\Downloads\Antigravity Google\Cerebro\` (tabela no guia). Mantém a pasta "Antigravity Google" para os comandos das regras continuarem valendo.
3. **Config vai como referência** (não sobrescrever o do Laura).
4. **Sincronização contínua:** Cérebro já tem circuito GitHub (`cerebro-miguel`, Dell envia */30, Laura puxa); memória do ZCode sincroniza por Tema Duplo via Cérebro; regras sincronizam regenerando o pacote.

## Próximos passos

1. Miguel: copiar a pasta para o pendrive → Laura.
2. Laura: prompt de ativação (Parte B do guia) → instalar + checklist.
3. Comparar report da Laura com o estado daqui.

## ADENDO 17/08/2026 20:54 — espelhamento no Google Drive

Ordem do Miguel: subir o pacote ao Google Drive em `espelho-zcode/` na RAIZ. Feito via `rclone copy ~/ZCodeProject/espelho_zcode_laura drive:espelho-zcode` (remotes `drive:` e `gdrive:` apontam para a MESMA conta). Verificado: **101 objetos, 46,1 MiB**. O pacote agora existe em 2 lugares: Dell (`~/ZCodeProject/espelho_zcode_laura/`) e Drive (`espelho-zcode/`). Próximos passos inalterados: ativar na Laura (Parte B do guia).

## ADENDO 17/08/2026 22:06 — gravação no pendrive

Ordem do Miguel: gravar o pacote no pendrive recém-encaixado. Pendrive = `/dev/sda1` (exFAT, 58,6 GB) montado em `/media/migueldorosario/2079-8A26`. Copiado via `rsync -rlt --no-perms` para `espelho_zcode_laura/` na RAIZ do pendrive + `sync`. Verificado: **101 arquivos, 59 MB (cerebro.zip 46 MB)**. Pacote agora em 3 lugares: Dell, Drive (`espelho-zcode/`) e pendrive. Pronto para ativar na Laura (Parte B do guia).

## ADENDO 17/08/2026 22:20 — inventário das automações (pergunta do Miguel: "tem as memórias das tarefas agendadas?")

Resposta e ação: o pacote JÁ trazia as memórias DESCRITIVAS das tarefas (memoria_zcode/agendamento-vigilia-trindade-cafezinho.md, custos-reducao-automacoes-20260817.md, auditoria-backup-vigilia-20260813.md, cerebro-backup-locais.md, cadencia-boletim-baleia.md + fóruns/memórias do Cérebro), mas NÃO o banco vivo de automações (`tasks-index.sqlite` — não migra: é por máquina). Gerado `automatizacoes_inventario.md` (4 automações ativas do CronList: CCTV 8/8h, Caçadora 1/1h, Faxina 2h/4h madrugada, Vigília 4/4h-6/6h + crons de servidor + regra de failover só com ordem do Miguel) — adicionado ao pacote do Dell e ao Drive (`espelho-zcode/`, 102 objetos). **Pendrive: removido do PC antes da cópia desses 2 arquivos (inventário + guia atualizado) — ele leva a versão original completa (101 arquivos), que funciona igual; se for re-espetado, copiar os 2 arquivos.**
