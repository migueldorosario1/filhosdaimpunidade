@echo off
rem Abre a Trindade LAURA completa: Claude (chefe), Codex e Grok,
rem cada um na sua janela, retomando a ultima sessao e iniciando "loop laura".
start "LAURA-CLAUDE" cmd /k "%~dp0laura_claude.cmd"
timeout /t 5 /nobreak >nul
start "LAURA-CODEX" cmd /k "%~dp0laura_codex.cmd"
timeout /t 5 /nobreak >nul
start "LAURA-GROK" cmd /k "%~dp0laura_grok.cmd"
