@echo off
title LAURA-GROK (capas V4 + observador)
cd /d C:\Users\migue\cerebro-miguel
rem Sessao interativa. O loop 1h :51 e a tarefa LoopLauraGrok + /loop Grok.
rem Runbook: cerebro\Foruns\loop_trindade_laura\controle\loop_laura_grok_RUNBOOK.md
grok --continue "ronda loop laura grok — leia o RUNBOOK de capas e execute uma ronda"
if errorlevel 1 grok "ronda loop laura grok — leia o RUNBOOK de capas e execute uma ronda"
