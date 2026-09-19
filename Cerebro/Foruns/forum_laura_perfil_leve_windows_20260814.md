# Fórum — Perfil leve da Laura (Windows) e obrigação de indexar mudanças

**Data:** 2026-08-14 BRT  
**Máquina:** **Laura** (Samsung Galaxy Book Go, Windows 11 ARM64) — não confundir com **Miguel** (Dell/Ubuntu 16 GB)  
**Autor da sessão:** Grok Build (grok-4.6), a pedido do Miguel  
**Status:** aplicado + persistido + indexado  
**Tema Duplo:** este fórum (decisões) + [`Memorias/memoria_laura_perfil_leve_windows_20260814.md`](../Memorias/memoria_laura_perfil_leve_windows_20260814.md) (log técnico)  
**Rollback canônico:** [`CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md`](../CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md)

---

## Decisões

1. **Não instalar Linux nativo na Laura.** Snapdragon 7c Gen 2 (Windows on ARM antigo) tem suporte Linux incompleto (Wi‑Fi, teclado, GPU, áudio). Desinstalar o Windows é perigoso. WSL2 nesta máquina piora a RAM (4 GB).
2. **Não desligar serviços Samsung de firmware/rádio/painel, nem `XtaCache`, nem rede/áudio.**
3. **Aplicar perfil leve reversível** para caber CLIs (Claude, Codex, Grok) nos 4 GB: Search, SysMain, Edge auto-start, Phone Link, telemetria, Xbox, Office C2R em Manual, exclusões do Defender nos CLIs.
4. **Defender em tempo real, NisSrv e SmartScreen desligados** a pedido explícito do Miguel. O motor `MsMpEng` (~200 MB) **continua residente** — o Windows 11 não deixa parar o serviço `WinDefend` mesmo com Tamper off.
5. **Persistência no reboot:** tarefa agendada `LauraLitePersist` (SYSTEM, arranque + 45 s após login) reaplica o perfil. Condição: **Tamper Protection permanece OFF** na Segurança do Windows.
6. **Regra viva (a partir de 14/08/2026):** qualquer mudança de sistema na Laura (serviço, política, Defender, arranque, tarefa, script em `%LOCALAPPDATA%\Laura`) **tem de ser indexada no Cérebro no mesmo turno**, em Tema Duplo + atualização do nodo de rollback, para dar para reverter.

## O que NÃO se fez

- Dual-boot / wipe do Windows  
- Desligar `WinDefend` (acesso negado; processo protegido)  
- Desligar widgets da barra (registo bloqueado)  
- Instalar WSL  

## Como reverter

Ver o nodo de rollback. Atalho na própria Laura (PowerShell **admin**):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\Laura\rollback-lite.ps1"
```

Depois, na Segurança do Windows: religar **Proteção contra adulteração** e **Proteção em tempo real**. Reiniciar.

## Ligação

- Identidade física: [`Memorias/memoria_identidade_computador_laura_20260814.md`](../Memorias/memoria_identidade_computador_laura_20260814.md)
- Ficha das duas máquinas: [`Foruns/computadores_miguel_e_laura_20260814.md`](./computadores_miguel_e_laura_20260814.md)
- Nodo hardware (Dell + ponte Laura): [`CEREBRO_NODE_HARDWARE_MIGUEL.md`](../CEREBRO_NODE_HARDWARE_MIGUEL.md)
