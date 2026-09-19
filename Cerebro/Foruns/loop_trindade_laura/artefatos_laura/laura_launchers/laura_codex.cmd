@echo off
title LAURA-CODEX (auditor tecnico)
cd /d C:\Users\migue\cerebro-miguel
codex resume --last "loop laura"
if errorlevel 1 codex "loop laura"
