@echo off
title Religar Laura (pos-reboot)
echo Religando a Laura: Claude Laura + DSH web (porta 3080)...

start "LAURA-CLAUDE" cmd /k "C:\Users\migue\cerebro-miguel\laura_launchers\laura_claude.cmd"
timeout /t 5 /nobreak >nul

start "DSH-Web" powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\migue\cerebro-miguel\laura_launchers\religar_dsh_web.ps1"
timeout /t 12 /nobreak >nul

start "" http://127.0.0.1:3080
echo.
echo Pronto. Claude Laura aberta e DSH web no ar. Se o navegador nao abriu, abra http://127.0.0.1:3080 no Edge.
timeout /t 6 /nobreak >nul
