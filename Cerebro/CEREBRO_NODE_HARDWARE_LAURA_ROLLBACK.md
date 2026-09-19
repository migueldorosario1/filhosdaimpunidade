# CEREBRO NODE — Rollback do perfil leve da Laura

**Criado:** 2026-08-14 BRT  
**Autor:** Grok Build  
**Máquina:** **Laura** (Samsung Galaxy Book Go, Windows 11 ARM64)  
**Não usar este nodo no Dell/Ubuntu (Miguel).** Esse rollback está em `CEREBRO_NODE_HARDWARE_MIGUEL_ROLLBACK.md`.

**Fonte da alteração:** Tema Duplo  
`Foruns/forum_laura_perfil_leve_windows_20260814.md` +  
`Memorias/memoria_laura_perfil_leve_windows_20260814.md`

**Regra:** toda mudança de sistema na Laura atualiza **este arquivo** com o par aplicar/reverter.

---

## Atalho (preferido)

Na Laura, PowerShell **administrador**:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\Laura\rollback-lite.ps1"
```

Depois, à mão:

1. Segurança do Windows → **Proteção contra adulteração = Ativado**
2. **Proteção em tempo real = Ativado**
3. Reiniciar

O script remove a tarefa `LauraLitePersist`, restaura serviços/tarefas/políticas e tira as exclusões do Defender. **Não desinstala nada.** Edge e Phone Link voltam a poder abrir; o auto-start do Edge não é recriado (ligar de novo em Edge → Definições → ao iniciar, se quiseres).

Se o ficheiro local sumir, executar as secções abaixo à mão.

---

## 1. Tirar a persistência

```powershell
Unregister-ScheduledTask -TaskName 'LauraLitePersist' -Confirm:$false
```

Ficheiros (opcional apagar):

- `%LOCALAPPDATA%\Laura\persist-lite.ps1`
- `%LOCALAPPDATA%\Laura\rollback-lite.ps1`

---

## 2. Serviços — voltar ao estado de 14/08/2026 *antes* do perfil

| Serviço | Restaurar para |
|---|---|
| WSearch | Automatic (depois `Start-Service WSearch`) |
| SysMain | Automatic |
| DoSvc | Automatic delayed (`Start=2` em `HKLM\SYSTEM\CurrentControlSet\Services\DoSvc`) |
| MapsBroker | Automatic |
| DiagTrack | Automatic |
| dmwappushservice | Manual |
| InventorySvc | Automatic |
| PcaSvc | Automatic |
| DusmSvc | Automatic |
| WSAIFabricSvc | Automatic |
| ClickToRunSvc | Automatic |
| SSDPSRV | Manual |
| lfsvc | Manual |
| PhoneSvc | Manual |
| InstallService | Manual |
| edgeupdate | Automatic |
| MicrosoftEdgeElevationService | Manual |
| Xbox* / WMPNetworkSvc / RetailDemo / wisvc / WalletService / SharedAccess / MessagingService | Manual |

```powershell
Set-Service WSearch -StartupType Automatic; Start-Service WSearch
Set-Service SysMain -StartupType Automatic
Set-Service ClickToRunSvc -StartupType Automatic
# ... demais linhas da tabela
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Services\DoSvc' -Name Start -Value 2
```

**Não mexer no rollback:** serviços Samsung de firmware/rádio/painel, `XtaCache`, WLAN, áudio, RPC, `WinDefend` (nunca saiu de Automatic).

---

## 3. Políticas e registo a apagar

```powershell
Remove-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender' -Name DisableAntiSpyware -ErrorAction SilentlyContinue
Remove-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender' -Name DisableAntiVirus -ErrorAction SilentlyContinue
Remove-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection' -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet' -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen' -Recurse -Force -ErrorAction SilentlyContinue
Remove-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\System' -Name EnableSmartScreen,ShellSmartScreenLevel -ErrorAction SilentlyContinue
Remove-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer' -Name SmartScreenEnabled -ErrorAction SilentlyContinue
Remove-ItemProperty 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppHost' -Name EnableWebContentEvaluation -ErrorAction SilentlyContinue
Remove-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Edge' -Name StartupBoostEnabled,BackgroundModeEnabled,HideFirstRunExperience,SmartScreenEnabled,SmartScreenPuaEnabled -ErrorAction SilentlyContinue
Remove-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\GameDVR' -Name AllowGameDVR -ErrorAction SilentlyContinue
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters' -Name EnableSuperfetch -Value 3
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters' -Name EnablePrefetcher -Value 3
New-ItemProperty 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Run' -Name SecurityHealth -PropertyType String -Value '%windir%\system32\SecurityHealthSystray.exe' -Force
```

---

## 4. Defender (prefs + exclusões)

Só funciona com **Tamper ainda OFF**. Depois religar Tamper e tempo real no UI.

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -DisableBehaviorMonitoring $false
Set-MpPreference -DisableIOAVProtection $false
Set-MpPreference -DisableScriptScanning $false
Set-MpPreference -DisableBlockAtFirstSeen $false
Set-MpPreference -DisableIntrusionPreventionSystem $false
Set-MpPreference -EnableNetworkProtection Enabled
Set-MpPreference -PUAProtection Enabled
Set-MpPreference -MAPSReporting 1
Set-MpPreference -SubmitSamplesConsent 1

Remove-MpPreference -ExclusionPath "$env:USERPROFILE\.claude"
Remove-MpPreference -ExclusionPath "$env:USERPROFILE\.grok"
Remove-MpPreference -ExclusionPath "$env:USERPROFILE\.codex"
Remove-MpPreference -ExclusionPath "$env:USERPROFILE\.local\bin"
Remove-MpPreference -ExclusionPath "$env:USERPROFILE\.local\share\claude"
Remove-MpPreference -ExclusionPath "$env:LOCALAPPDATA\Programs\OpenAI"
Remove-MpPreference -ExclusionProcess 'claude.exe'
Remove-MpPreference -ExclusionProcess 'grok.exe'
Remove-MpPreference -ExclusionProcess 'codex.exe'
```

---

## 5. Tarefas agendadas a reativar

```
\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser Exp
\Microsoft\Windows\Application Experience\StartupAppTask
\Microsoft\Windows\Application Experience\MareBackup
\Microsoft\Windows\Application Experience\PcaPatchDbTask
\Microsoft\Windows\Customer Experience Improvement Program\Consolidator
\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip
\Microsoft\Windows\Maps\MapsToastTask
\MicrosoftEdgeUpdateTaskMachineUA
\Microsoft\XblGameSave\XblGameSaveTask
\Microsoft\Office\Office Automatic Updates 2.0
\Microsoft\Office\Office Feature Updates
\Microsoft\Office\Office Feature Updates Logon
\Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan
\Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance
\Microsoft\Windows\Windows Defender\Windows Defender Cleanup
\Microsoft\Windows\Windows Defender\Windows Defender Verification
```

```powershell
Enable-ScheduledTask -TaskName 'Windows Defender Scheduled Scan' -TaskPath '\Microsoft\Windows\Windows Defender\'
# repetir para a lista
```

---

## 6. O que o rollback NÃO desfaz (porque não foi alterado)

- Windows instalado / partições  
- Serviços Samsung de firmware  
- `WinDefend` start type (já era Automatic)  
- Apps instaladas (Edge, Office, Phone Link, CLIs)  
- BitLocker (já estava off) / Secure Boot (já estava off)

---

## 7. Histórico de alterações neste nodo

| Data | O quê | Rollback |
|---|---|---|
| 2026-08-14 | Perfil leve + persistência `LauraLitePersist` + Defender/Nis/SmartScreen off | este documento + `rollback-lite.ps1` |

---

## Espelho do ZCode na Laura (17/08/2026)

Tema Duplo: `Foruns/forum_espelho_zcode_laura_20260817.md` + `Memorias/memoria_espelho_zcode_laura_20260817.md`.
Pacote de espelho (AGENTS.md + 94 memórias do ZCode + Cérebro zip 48 MB + config/hooks sem segredos) em `~/ZCodeProject/espelho_zcode_laura/` no Dell. Ativação na Laura segue o guia `LEIA_PRIMEIRO_ESPELHO_LAURA.md` do pacote.
