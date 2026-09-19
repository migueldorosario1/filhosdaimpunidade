# 00_INICIAR_AGY_LAURA.ps1 - relanca o AGY-Laura (Antigravity CLI) com o oficio completo
# Uso: powershell -ExecutionPolicy Bypass -File C:\Users\migue\cerebro-miguel\laura_launchers\00_INICIAR_AGY_LAURA.ps1
# Conserto do "timer magro": mata a sessao presa e relanca com o oficio (le AGENTS.md).
$ErrorActionPreference = 'Continue'
$agy = 'C:\Users\migue\AppData\Local\agy\bin\agy.exe'
$repo = 'C:\Users\migue\cerebro-miguel'

# 1. Mata a sessao presa (PID vivo porem em template de presenca)
Get-Process -Name agy -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 2

# 2. Prompt inicial (ASCII-only) - le o AGENTS.md e reestabelece o loop 30/30 com o oficio
$prompt = "Voce e o AGY-LAURA (Motor de Publicacao + Curadoria + Visual). Leia AGENTS.md na raiz do repo e siga a secao 'Oficio AGY-LAURA'. Configure teu loop de 30 em 30 minutos (marcas :05 e :35) para executar ESSE oficio a cada ronda: git pull; ler de_laura.md e de_dell.md procurando TODOS os blocos novos enderecados a AGY-LAURA/AL; executar cada ordem (montar post, aplicar capa com _cafezinho_img_check, publicar sob Consenso Duplo + prova REST); responder na ponte com PROVA; atualizar ledger/estado; commit so dos teus arquivos sob o lock .ponte-laura-git.lock; push. NUNCA repetir o template de presenca de 3 itens. Comece agora: git pull, leia a ponte, e se ainda houver ordem de reteste (capa 267542) execute-a com prova."

# 3. Relanca interativo, na pasta do repo, com o repo adicionado ao workspace
Start-Process -FilePath $agy -ArgumentList @('--prompt-interactive', $prompt, '--add-dir', $repo) -WorkingDirectory $repo

Write-Output "AGY-LAURA relancado: sessoes antigas encerradas, nova sessao aberta com o oficio (le AGENTS.md)."
