# Memória técnica — Perfil leve da Laura (Windows 11 ARM)

**Data:** 2026-08-14 BRT  
**Executor:** Grok Build (grok-4.6)  
**Pedido:** Miguel, sessão Grok na Laura  
**Fórum:** `Foruns/forum_laura_perfil_leve_windows_20260814.md`  
**Rollback:** `CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md`  
**Status:** canônico para esta alteração

---

## 1. Máquina (não confundir)

| Campo | Valor |
|---|---|
| Nome | **Laura** |
| Equipamento | Samsung Galaxy Book Go (Wi‑Fi), `NP340XLA-K06BR` |
| Hostname | `WIN-S8A8I33BC7U` |
| CPU | Snapdragon 7c Gen 2 @ 2,55 GHz, 8 núcleos, ARM64 |
| RAM visível | 3,68 GB |
| Disco C: | 107,6 GB (~51 GB livres no diagnóstico) |
| OS | Windows 11 Home Single Language 10.0.26100 |
| Identidade completa | `Memorias/memoria_identidade_computador_laura_20260814.md` |

O nodo `CEREBRO_NODE_HARDWARE_MIGUEL.md` descreve o **Dell/Ubuntu de 16 GB**. Esta memória é só da Laura.

---

## 2. Diagnóstico inicial (antes de mexer)

Primeiro snapshot da sessão (3 CLIs ociosos: Claude, Codex, Grok):

| Métrica | Valor |
|---|---|
| RAM usada | 2,96 / 3,68 GB (80,5%) · livre 0,72 GB |
| Depois, pré-lighten | 3,07 / 3,68 GB (83,6%) · livre 0,60 GB |
| CPU | 7% |
| Pagefile | 0,53 / 6,5 GB |
| Uptime | ~17 h |

Maiores blocos (pré-lighten): `svchost` 420 MB · Edge 258 MB · `MsMpEng` 221 MB · WebView2 137 MB · 6 PowerShells 103 MB · compressão 94 MB. Os 3 CLIs juntos ~160 MB.

Decisão: não dual-boot Linux (SoC sem suporte decente). WSL2 sem virtualização útil e comeria 1–2 GB. Caminho: Windows leve.

---

## 3. O que foi aplicado

### 3.1 Serviços — Disabled (não sobem no boot)

`WSearch`, `SysMain`, `PhoneSvc`, `InventorySvc`, `WSAIFabricSvc`, `MapsBroker`, `lfsvc`, `DiagTrack`, `dmwappushservice`, `XblAuthManager`, `XblGameSave`, `XboxGipSvc`, `XboxNetApiSvc`, `WMPNetworkSvc`, `RetailDemo`, `wisvc`, `WalletService`, `SharedAccess`, `MessagingService`

Estado **antes** (os que importam):

| Serviço | Antes |
|---|---|
| WSearch | Running / Automatic |
| SysMain | Running / Automatic |
| PhoneSvc | Running / Manual |
| InventorySvc | Running / Automatic |
| WSAIFabricSvc | Running / Automatic |
| MapsBroker | Stopped / Automatic |
| lfsvc | Running / Manual |
| DiagTrack | StartPending / Automatic |
| dmwappushservice | Stopped / Manual |
| Xbox* / extras | Stopped / Manual |

`DiagTrack` ficou Disabled mas o processo ficou StartPending (não-stoppable) até o próximo reboot.

### 3.2 Serviços — Manual (só sobem se um app pedir)

`ClickToRunSvc` (Office), `PcaSvc`, `DusmSvc`, `edgeupdate`, `DoSvc` (Start=3 no registro; `sc config` deu acesso negado), `SSDPSRV`, `InstallService`

**Antes:** ClickToRun, Pca, Dusm, DoSvc, edgeupdate = Automatic (DoSvc delayed).

### 3.3 Não mexidos de propósito

`WinDefend`, `MDCoreSvc`, `wscsvc`, WLAN/DHCP/DNS/RPC/áudio, `XtaCache`, todos os serviços Samsung de firmware/rádio/painel (`Galaxy Book Service`, `SafiService`, `PanelManagerSvc`, `RCD`, `MdmLdrSvc`, `Samsung System Service`, `SamsungOSDService`, `Grip sensor Reset service`, `SecUTSSvc`). `SamsungAccountService` também não foi desligado.

### 3.4 Arranque e políticas

- Removido `HKCU\...\Run\MicrosoftEdgeAutoLaunch_*`
- Removido `HKLM\...\Run\SecurityHealth`
- Políticas Edge (`HKLM\SOFTWARE\Policies\Microsoft\Edge`): `StartupBoostEnabled=0`, `BackgroundModeEnabled=0`, `HideFirstRunExperience=1`, `SmartScreenEnabled=0`, `SmartScreenPuaEnabled=0`
- SmartScreen Windows: `EnableSmartScreen=0`, `ShellSmartScreenLevel=Off`, Explorer `SmartScreenEnabled=Off`, AppHost `EnableWebContentEvaluation=0`
- Prefetch: `EnableSuperfetch=0`, `EnablePrefetcher=0`
- Game DVR policy `AllowGameDVR=0`
- Content Delivery Manager (sugestões) desligado no HKCU
- `TaskbarDa=0` (widgets) **falhou** — acesso negado

### 3.5 Defender

Pedido do Miguel: desligar. Tamper Protection bloqueou CLI até ele desligar no UI.

Estado gravado no fim da sessão:

| Chave | Valor |
|---|---|
| Tamper (UI / `IsTamperProtected`) | False (utilizador desligou; registo `Features\TamperProtection=4`, source=2) |
| Real-time | False (`DisableRealtimeMonitoring=True` + GPO=1) |
| Behavior / IOAV / script / BAF | desligados via `Set-MpPreference` + GPO |
| NIS / NisSrv | False; `WDNisSvc` Stopped/Manual (não deu para pôr Disabled) |
| `WinDefend` | **ainda Running/Automatic** — `sc stop/config` acesso negado mesmo com Tamper off |
| `MsMpEng` | processo residente ~208–278 MB, **sem varrer** |
| Exclusões path | `%USERPROFILE%\.claude`, `.grok`, `.codex`, `.local\bin`, `.local\share\claude`, `%LOCALAPPDATA%\Programs\OpenAI` |
| Exclusões process | `claude.exe`, `grok.exe`, `codex.exe` e paths completos |

GPO persistente:

```
HKLM\SOFTWARE\Policies\Microsoft\Windows Defender
  DisableAntiSpyware=1
  DisableAntiVirus=1
HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection
  DisableRealtimeMonitoring=1
  DisableBehaviorMonitoring=1
  DisableOnAccessProtection=1
  DisableScanOnRealtimeEnable=1
  DisableIOAVProtection=1
HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet
  SpynetReporting=0
  SubmitSamplesConsent=2
```

O Windows **apagou** `DisableAntiSpyware` uma vez durante a sessão; a tarefa de persistência volta a escrever.

### 3.6 Tarefas agendadas desativadas

Compatibility Appraiser Exp, StartupAppTask, MareBackup, PcaPatchDbTask, Consolidator, UsbCeip, MapsToastTask, MicrosoftEdgeUpdateTaskMachineUA, XblGameSaveTask, Office Automatic/Feature Updates (3), Windows Defender Scheduled Scan + Cache Maintenance + Cleanup + Verification.

### 3.7 Processos mortos na sessão (não “desinstalados”)

Edge (~261 MB), PhoneExperienceHost, Widgets, SmartScreen, SearchIndexer. Phone Link (`Microsoft.YourPhone`) **não foi desinstalado**; voltou a abrir sozinho uma vez — a persistência mata `PhoneExperienceHost` no boot.

### 3.8 Persistência

| Artefacto | Caminho |
|---|---|
| Script que reaplica o perfil | `%LOCALAPPDATA%\Laura\persist-lite.ps1` |
| Script de rollback | `%LOCALAPPDATA%\Laura\rollback-lite.ps1` |
| Tarefa | `LauraLitePersist` (SYSTEM, Highest, AtStartup + AtLogOn delay 45 s) |
| Log pontual da 1ª passagem | `%TEMP%\laura-lighten-log.txt` |

Se o Tamper for religado no UI, `Set-MpPreference` deixa de pegar e o Defender volta a varrer.

---

## 4. Comparação (sessão suja vs perfil)

| | Pré-lighten | Fim da sessão | Após reboot limpo (esperado) |
|---|---|---|---|
| RAM usada | 3,07 GB (83,6%) | 3,18 GB (86,5%) — Codex/Explorador/7 PowerShells/Definições incháram | ~70–75% se não abrir Edge/Definições |
| Livre | 0,60 GB | 0,50 GB | ~1,0–1,3 GB |
| Edge auto | sim, 258 MB | off | off |
| Search / SysMain | on | off | off |
| Defender a varrer | sim | não | não (se Tamper off) |
| `MsMpEng` residente | 221 MB | ~208 MB | deve voltar (~150–220 MB) |

---

## 5. Rollback (resumo)

Receita completa no nodo `CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md`.

Na Laura, admin:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\Laura\rollback-lite.ps1"
```

Depois: Segurança do Windows → Tamper ON + tempo real ON → reboot.

---

## 6. Regra operacional

Qualquer agente que altere sistema na Laura (serviço, GPO, Defender, arranque, tarefa, script em `%LOCALAPPDATA%\Laura`) deve, **no mesmo turno**:

1. Atualizar esta memória **ou** abrir Tema Duplo novo se for outro tema.
2. Atualizar `CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md` (aplicar + reverter).
3. Anotar em `CEREBRO_NODE_ATUALIZACOES.md`.
4. Não republicar números de série / UUID da Laura em material aberto.
