# Memória — limpeza e recuperação do GNOME Transcritor

Data: 11/08/2026  
Autoridade: autorização direta de Miguel para apagar caches, áudios, transcrições e bancos locais do aplicativo

## Situação

O GNOME Sound Recorder estava praticamente inutilizável. A instância `165994` permanecia viva havia mais de nove horas e repetia erros JavaScript `MainWindow._record is undefined` ao tentar operar sobre o estado antigo.

O transcritor acumulava 117 áudios processados, 441 transcrições e `index.jsonl`, totalizando 559 arquivos e cerca de 54 MB. O cache Whisper ocupava aproximadamente 600 MB; a unidade systemd mantinha `MAX_ARQUIVO_AGE_DAYS=0` e `MAX_TRANSCRIPT_AGE_DAYS=0`, valores que desativavam a limpeza.

## Ação autorizada

O serviço foi parado e foram apagados todos os arquivos de `~/Recordings`, o estado e os logs de `~/.local/share/transcritor`, os caches dedicados `~/.cache/whisper` e `~/.cache/huggingface`, bytecode do transcritor, heartbeat, PID e preferências DConf do Sound Recorder. O índice Tracker foi limpo somente para `~/Recordings`, removendo referências a gravações inexistentes sem zerar a busca global dos outros arquivos.

Código, unidade systemd, chaves e configurações operacionais foram preservados.

Não foi produzido novo snapshot local porque Miguel autorizou o descarte integral e informou que os dados já possuem cobertura no Google Drive e, em grande parte, no Backblaze. A operação ficou estritamente limitada ao GNOME Sound Recorder e ao transcritor; nenhum banco ou cache de outro projeto entrou no corte.

## Prevenção

A unidade `~/.config/systemd/user/transcritor.service` passou a usar `MAX_AUDIO_AGE_HOURS=1`, `MAX_ARQUIVO_AGE_DAYS=1` e `MAX_TRANSCRIPT_AGE_DAYS=1`. Assim, gravações órfãs têm retenção de uma hora e áudios processados/transcrições ficam no máximo um dia.

## Resultado

O serviço voltou ativo com zero arquivos no fluxo e caches dedicados praticamente vazios. Um teste direto com áudio sintético respondeu pelo `whisper-large-v3-turbo` da Groq em 0,45 segundo.

A instância GNOME antiga não respondeu ao encerramento normal e foi eliminada pelo PID exato. Uma única instância nova foi aberta por unidade transitória independente, sem herdar o processo travado e sem novos erros no journal inicial.
