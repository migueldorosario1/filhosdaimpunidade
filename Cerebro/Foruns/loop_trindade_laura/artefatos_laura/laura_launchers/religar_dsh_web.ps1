# religar_dsh_web.ps1 - sobe o DSH web (porta 3080) com a chave carregada do cofre
# Chamado pelo atalho Religar_Laura.cmd (nao roda a chave em tela, so carrega no ambiente).
$ErrorActionPreference = 'Continue'
$envFile = Join-Path $env:USERPROFILE '.dsh\deepseek_env'
$line = Get-Content $envFile | Where-Object { $_ -match '^DEEPSEEK_API_KEY=' } | Select-Object -First 1
if ($line) {
  $env:DEEPSEEK_API_KEY = ($line -split '=',2)[1]
} else {
  Write-Host "ERRO: DEEPSEEK_API_KEY ausente em deepseek_env" -ForegroundColor Red
  exit 1
}
& 'C:\Users\migue\AppData\Roaming\npm\dsh.cmd' web --no-open
