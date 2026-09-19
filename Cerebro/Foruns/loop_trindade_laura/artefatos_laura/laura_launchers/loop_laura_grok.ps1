# Loop LAURA-GROK — transporte do Task Scheduler (marca :51).
# Pula se o heartbeat do /loop Grok estiver fresco (<40 min).
$ErrorActionPreference = "Continue"
$Root = "C:\Users\migue\cerebro-miguel"
$Grok = "C:\Users\migue\.grok\bin\grok.exe"
$Prompt = Join-Path $Root "cerebro\Foruns\loop_trindade_laura\controle\loop_laura_grok_PROMPT.md"
$Hb = Join-Path $Root "cerebro\Foruns\ponte_laura_completa\protocolo_anticonflito\heartbeats\grok_laura.md"
$LogDir = Join-Path $Root "laura_launchers\logs"
$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$Log = Join-Path $LogDir "loop_laura_grok_$Stamp.log"

function Write-Log($m) {
  $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $m"
  Add-Content -Path $Log -Value $line
  Write-Output $line
}

if (-not (Test-Path $Grok)) { Write-Log "FAIL: grok.exe ausente"; exit 1 }
if (-not (Test-Path $Prompt)) { Write-Log "FAIL: prompt ausente"; exit 1 }

if (Test-Path $Hb) {
  $raw = Get-Content $Hb -Raw
  if ($raw -match "hora_brt:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2})") {
    try {
      $hbTime = [datetime]::ParseExact($Matches[1], "yyyy-MM-dd HH:mm", $null)
      $ageMin = [int]((Get-Date) - $hbTime).TotalMinutes
      if ($ageMin -ge 0 -and $ageMin -lt 40) {
        Write-Log "SKIP: heartbeat fresco (${ageMin} min) — /loop Grok ja rodou"
        exit 0
      }
    } catch {
      Write-Log "WARN: nao parseou heartbeat; sigo"
    }
  }
}

Set-Location $Root
Write-Log "START ronda LAURA-GROK"
$p = Start-Process -FilePath $Grok -ArgumentList @(
  "-p", "--prompt-file", $Prompt,
  "--cwd", $Root,
  "--yolo",
  "--output-format", "text"
) -Wait -PassThru -NoNewWindow -RedirectStandardOutput (Join-Path $LogDir "stdout_$Stamp.txt") -RedirectStandardError (Join-Path $LogDir "stderr_$Stamp.txt")
Write-Log "END exit=$($p.ExitCode)"
exit $p.ExitCode
