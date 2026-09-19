---
name: memoria-receptor-voz-zcode-20260825
description: Log técnico do protótipo Whisper externo para comandos de voz no ZCode
metadata:
  type: project
  date: 2026-08-25
---

## Contexto

Miguel quer operar o ZCode sem as mãos: dizer “ZCode, ouvir”, falar o pedido e dizer “ZCode, Enter”. O cliente ZCode instalado é Electron empacotado sem código-fonte local; não há extensão suportada para inserir microfone na UI.

## Descobertas

- Whisper disponível em `~/.local/bin/whisper`.
- Modelo `large-v3-turbo` encontrado no cache local.
- `arecord`, `xclip`, Python Xlib e sessão X11 disponíveis.
- `sounddevice` está instalado, mas falha por ausência de PortAudio; a implementação usa `arecord` diretamente.
- O GNOME Sound Recorder já teve travamentos documentados; não foi usado como intermediário.

## Arquivos criados

- `/home/migueldorosario/ZCodeProject/zcode_voice_receiver/receiver.py`
- `/home/migueldorosario/ZCodeProject/zcode_voice_receiver/test_receiver.py`
- `/home/migueldorosario/ZCodeProject/zcode_voice_receiver/README.md`

## Comportamento

O modo padrão é dry-run. `--send` habilita clipboard + Enter somente quando `xprop` identifica janela ativa contendo “ZCode”. A transcrição ocorre em blocos de quatro segundos. O modelo é carregado uma vez no início, não a cada bloco. Comandos de ativação e término são removidos do texto.

## Verificação

`python3 -m unittest -v`: 3 testes OK.
`python3 -m py_compile receiver.py`: OK.
Nenhum processo foi iniciado automaticamente; nenhuma configuração de login foi alterada.

## Estado de continuidade

O próximo passo é teste manual autorizado com áudio real, primeiro sem envio. Depois validar colagem/Enter em janela descartável e no ZCode. Só após esses testes avaliar inicialização automática. O protótipo pode precisar de buffer incremental para comandos divididos entre blocos.

## O que aconteceu / o que falta / o que preciso do Miguel

A primeira implementação e testes locais foram concluídos. Falta validar captura no microfone real, desempenho do `large-v3-turbo` e envio seguro. Preciso que Miguel autorize o teste manual com microfone e indique se quer testar com `large-v3-turbo` ou modelo mais leve.

## Desfecho técnico — 25/08/2026 14:20

Foram tentadas três arquiteturas: blocos `arecord` + Whisper; UI Tkinter monolítica + `parec`; UI/worker isolados + medidor de nível. O microfone foi provado (RMS ~2842, peak 32767), mas a qualidade/latência inviabilizou o produto. Benchmark em gravação real Clip 7: `tiny` 1,11s com texto ruim; `base` 1,87s com erros relevantes; `large-v3-turbo` 21,54s com texto perfeito. O modelo rápido alucinou frases e repetições; o modelo preciso não foi ao vivo. Enter por voz não ficou confiável.

Todos os processos foram desligados e nenhum autostart foi criado. Código e rollbacks foram mantidos apenas como histórico em `ZCodeProject/zcode_voice_receiver/`. Estado final: **REPROVADO/ENCERRADO**, usar GNOME `Super+G`.

**O que aconteceu:** protótipo falhou na exigência central de transcrição visível, precisa e imediata.

**O que falta:** nada; não insistir nesta implementação.

**O que preciso do Miguel:** nenhuma ação.

## Implementação final híbrida F8 — 25/08/2026 15:13

Controle mãos-livres abandonado. Novo componente isolado `ZCodeProject/zcode_voice_gnome_controller/`:

- `atspi_recorder.py` roda em `/usr/bin/python3` (pyatspi) e identifica Record/Done por role, nome, estados SHOWING/VISIBLE/ENABLED/SENSITIVE e action click;
- `f8_toggle.py` roda no Python pyenv (Python Xlib), usa lock `/tmp/zcode_voice_f8.lock`, alterna start/stop e ativa o ZCode por EWMH;
- custom keybinding GNOME `custom2`: F8 → f8_toggle.py;
- custom1 Super+G inalterado;
- rollback `rollback_f8.sh` e snapshot `backups/pre_f8_20260825_151118/`.

Teste ponta a ponta: start 15:12:48 (`gravando`); stop 15:12:53 (`ocioso`, foco_zcode=True); transcritor processou Clip 2 e Groq salvou `.txt` 15:12:54; áudio arquivado 15:12:55. Nenhum processo de voz contínuo ativo. Nenhum autostart novo.

**O que aconteceu:** híbrido F8 funciona e reaproveita a transcrição perfeita existente.

**O que falta:** validação tátil do Miguel e uso de Ctrl+V após a notificação da transcrição.

**O que preciso do Miguel:** teste físico F8→fala→F8→Ctrl+V.
