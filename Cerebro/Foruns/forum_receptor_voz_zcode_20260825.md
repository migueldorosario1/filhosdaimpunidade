---
name: forum-receptor-voz-zcode-20260825
description: Protótipo de receptor externo Whisper para ditado mãos-livres no ZCode
metadata:
  type: project
  date: 2026-08-25
---

# Receptor externo de voz do ZCode

## Decisão

O cliente nativo do ZCode não será adulterado. Como o código-fonte da interface não está disponível localmente, a solução sustentável é um receptor externo local, usando o Whisper já instalado e integração com clipboard/teclado X11.

## Comandos definidos pelo Miguel

- **“ZCode, ouvir”** inicia a mensagem.
- O silêncio não encerra a mensagem.
- **“ZCode, Enter”** encerra, remove o comando e envia.
- O receptor deve funcionar sem as mãos, desde que o ZCode esteja em primeiro plano.

## Implementação inicial

Criado `ZCodeProject/zcode_voice_receiver/receiver.py`, com:

- Whisper local;
- captura ALSA por `arecord` em blocos;
- estados aguardando/ouvindo;
- modo `dry-run` padrão;
- `--send` opcional;
- trava que impede envio se a janela ativa não tiver “ZCode” no título;
- clipboard via `xclip` e Enter via Python Xlib.

Criados também `README.md` e `test_receiver.py`.

## Estado

- Testes unitários: 3/3 passaram.
- Sintaxe Python: validada com `py_compile`.
- Whisper `large-v3-turbo`: já disponível no cache local.
- O receptor não foi iniciado no login e não está rodando em segundo plano.
- O envio real ainda não foi testado; isso deve ocorrer primeiro em uma janela de texto descartável e depois no ZCode.
- A primeira versão transcreve em blocos de quatro segundos; se a frase de ativação ou encerramento for dividida entre blocos, será necessário melhorar o buffer incremental.

## O que aconteceu / o que falta / o que preciso do Miguel

**O que aconteceu:** o protótipo externo foi criado e passou nos testes unitários, sem modificar o ZCode.

**O que falta:** teste manual com sua voz, confirmar o dispositivo ALSA e ajustar o tamanho dos blocos; depois testar clipboard/Enter e só então considerar inicialização automática.

**O que preciso do Miguel:** autorização explícita para fazer o primeiro teste com captura real e, depois, para ativar o modo `--send`; não ativar automaticamente antes dessa validação.
--- 25/08/2026 13:41 — protótipo iniciado em dry-run; rollback e INDEX criados; nenhum envio automático ---

## DESFECHO — 25/08/2026 14:20

O protótipo foi **reprovado e encerrado**. Embora a captura do microfone e a caixa visual tenham funcionado, a transcrição incremental local foi grotesca e alucinou repetições. O `tiny` foi rápido mas impreciso; o `base` melhorou parcialmente; o `large-v3-turbo` foi correto, porém levou ~21,5 segundos numa fala curta — inviável para tempo real. O comando Enter nunca alcançou confiabilidade suficiente.

Todos os processos `receiver.py`, `live_ui.py`, `live_worker.py`, `parec` foram desligados. Não há autostart. Rollbacks permanecem em `ZCodeProject/zcode_voice_receiver/rollback_*`. Miguel volta a usar o fluxo GNOME `Super+G`, cuja transcrição é comprovadamente superior.

**O que aconteceu:** tentativa técnica documentada e encerrada honestamente.

**O que falta:** nada nesta implementação; só retomar se houver acesso ao mecanismo de ditado que produz a transcrição perfeita usada pelo Miguel ou código-fonte oficial do ZCode.

**O que preciso do Miguel:** nenhuma ação; usar `Super+G` normalmente.

## DESFECHO FINAL — HÍBRIDO F8 (25/08/2026 15:13)

Miguel decidiu abandonar controle exclusivamente por voz e adotar o modo híbrido confiável. Implementado atalho global **F8 como alternador**:

- primeiro F8 aciona semanticamente `Record` no GNOME Sound Recorder por AT-SPI;
- segundo F8 aciona `Done`, espera o estado voltar a ocioso e restaura o foco ao ZCode;
- o pipeline original `transcritor.service` → Groq `whisper-large-v3-turbo` → clipboard permanece intacto;
- `Super+G` foi preservado;
- nenhum detector de voz/processo `parec`/autostart permanece ativo.

Arquivos: `ZCodeProject/zcode_voice_gnome_controller/atspi_recorder.py`, `f8_toggle.py`, `rollback_f8.sh`, `README.md`. Rollback dos atalhos: `backups/pre_f8_20260825_151118/`.

Prova ponta a ponta: primeiro acionamento → estado `gravando`; segundo → `ocioso`; foco ativo voltou para janela `ZCode`; Clip 2 fechado 15:12:53, Groq salvou transcrição 15:12:54 e arquivou áudio 15:12:55.

**O que aconteceu:** F8 híbrido entregue e testado.

**O que falta:** teste físico do Miguel pressionando F8 duas vezes; a transcrição fica no clipboard para `Ctrl+V`.

**O que preciso do Miguel:** pressionar F8, falar, pressionar F8 novamente e colar com Ctrl+V.
