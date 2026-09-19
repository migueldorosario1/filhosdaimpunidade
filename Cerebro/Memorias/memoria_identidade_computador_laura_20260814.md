# Memória — Identidade do computador Laura

**Data do registro:** 2026-08-14 BRT

**Responsável pelo registro:** Codex

**Origem:** consulta local de firmware e hardware autorizada por Miguel

**Status:** canônico

## Decisão de identidade

Miguel atribuiu o nome **Laura** ao computador Windows usado nesta sessão. Esse nome humano deve ser associado aos identificadores físicos abaixo, mesmo que o hostname do Windows permaneça diferente.

## Identificadores confirmados

| Campo | Valor |
|---|---|
| Nome atribuído | **Laura** |
| Hostname do Windows no momento da consulta | `WIN-S8A8I33BC7U` |
| Fabricante | Samsung Electronics Co., Ltd. |
| Modelo comercial | Galaxy Book Go (Wi-Fi) |
| Produto da placa-base | `NP340XLA-K06BR` |
| Número de série do BIOS | `0AEQ9QEX206271R` |
| Número de série da placa-mãe | `123490EN400015` |
| UUID do sistema | `CE181DE5-2312-E27C-0E49-08287E00C66D` |
| Número de série do chassi | não informado pelo firmware (`None`) |

## Método de verificação

Os dados foram lidos no Windows por meio das classes WMI/CIM `Win32_BIOS`, `Win32_ComputerSystemProduct`, `Win32_ComputerSystem`, `Win32_BaseBoard` e `Win32_SystemEnclosure`.

## Regra operacional

- A menção **Laura** identifica este Samsung Galaxy Book Go.
- Para confirmação física forte, usar primeiro o número de série do BIOS e, em seguida, o UUID do sistema.
- Não confundir Laura com o notebook Dell/Ubuntu registrado anteriormente no nodo de hardware.
- Tratar os números de série e o UUID como dados sensíveis: podem circular no repositório privado, mas não devem ser publicados em páginas, relatórios ou repositórios abertos.

## Indexação

- Nodo temático: [`CEREBRO_NODE_HARDWARE_MIGUEL.md`](../CEREBRO_NODE_HARDWARE_MIGUEL.md) (secção 7)
- Ficha das duas máquinas: [`Foruns/computadores_miguel_e_laura_20260814.md`](../Foruns/computadores_miguel_e_laura_20260814.md)
- Perfil leve Windows 14/08/2026 (Tema Duplo): [`Foruns/forum_laura_perfil_leve_windows_20260814.md`](../Foruns/forum_laura_perfil_leve_windows_20260814.md) + [`memoria_laura_perfil_leve_windows_20260814.md`](./memoria_laura_perfil_leve_windows_20260814.md)
- Rollback: [`CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md`](../CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md)

**Regra:** mudança de sistema na Laura → indexar no mesmo turno (Tema Duplo + nodo de rollback).
