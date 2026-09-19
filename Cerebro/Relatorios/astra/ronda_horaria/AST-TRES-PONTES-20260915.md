# AST-TRES-PONTES-20260915 — decisões, estado e configuração

Corte inicial 15/09/2026 19:17–19:18 BRT. Pesquisa dos fóruns e inspeção read-only de crons, scripts, GitHub, rclone e NYC. Não executei sincronizadores de escrita nem alterei infraestrutura.

## Decisão vigente

A = GitHub `git@github.com:migueldorosario1/cerebro-miguel.git`, branch main, pasta `cerebro/Foruns/ponte_laura_completa/`.
B = GDrive `drive:espelho-zcode/ponte_zcode/`, snapshot existente a cada 30 min (:05/:35).
C = NYC `nyc:/home/ubuntu/cerebro-miguel-mirror.git`, branch main. Tencent é cópia adicional; Telegram é canal humano.

ZM-20260914-009 (14/09 17:49, de_dell linha 8179): Miguel autorizou reativar NYC; push duplo adicionado ao sync Dell, cron NYC corrigido. ZM-20260914-018 (22:33, linha 8512): automação de manutenção criada, ID automation-7bfdd5e5-67d7-4504-8dc8-a59d1af91262, slots 08/12/16/20 BRT. Não criar outra.
ZM-20260915-008-PONTE-RONDA (16:02, linha 8917): sync bloqueado por ledger porta_voz escrito diretamente no repo. ZM-20260915-010 (18:16, linha 8979): corrigido LEDGER_DIR para a árvore fonte e provado ciclo com repo limpo. Situação antiga de NYC órfão já foi superada.

## Estado observado

GitHub acessível, main 69904b7b02b8f2aaccee639662e054484eea4f18 no primeiro corte; clone Dell a7fd93e767aff4c600721dfd0cd1b2489de1fe09 (19:12), worktree limpo. Vários escritores: igualdade instantânea não é requisito entre ciclos.
NYC acessível, main d4e3285fecd8a4e28cb535f8c69e1c07780f03e2 (18:52). Cron */5 presente, log 19:15 BRT informa GitHub adiante; último log do sync Dell informa sucesso NYC. O atraso precisa ser reavaliado após o próximo ciclo, não confundido com parada de 12 dias.
Drive acessível via rclone, de_dell.md 2.574.602 bytes, ModTime 18:45:07 BRT, SHA256 16895b455fdf6602c28c70839bf8f3c04d87614b378cb1b4a91565c166af40da. Mtime representa alteração do conteúdo, não heartbeat de execução. Log tem quota temporária às 10h e tentativa posterior bem-sucedida. Não usar o mount antigo como indicador da saúde de todo o Drive.

## Lacunas concretas no código vigente

1. `scripts/sync_cerebro_from_github.sh` só faz fetch origin. Não há leitura automática por NYC/Drive. Na falha, reflete a cópia local.
2. `scripts/sync_cerebro_to_github.py`: sync_locked chama integrate_remote; fetch origin pode lançar exceção antes de chegar ao fallback de push_with_retry. Portanto o fallback de escrita não cobre toda indisponibilidade do GitHub.
3. `push_mirror_nyc` força HEAD sobre main NYC. Enquanto NYC for só espelho isso corresponde ao desenho documentado; se passar a receber mensagens independentes, esse force pode perder commits. Não abrir escrita de contingência em main sem preservação de divergências/refs por emissor.
4. `scripts/ponte_push.sh` ainda usa `gdrive:ponte_laura_completa`, diferente do estepe comprovado `drive:espelho-zcode/ponte_zcode`; também não inclui de_astra.md na lista de cópia. Não foi executado nesta inspeção.
5. O mesmo script só retorna falha quando TODAS as vias falham: uma só via bem-sucedida devolve exit 0. Isso não implementa a exigência de pelo menos duas entregas independentes.
6. Drive é snapshot sobrescrito por cópia periódica, sem entrada/ACK próprios. Escrever mensagens diretamente nesse snapshot arrisca sobreposição no próximo ciclo. O cron NYC trata divergência como rotina; não demonstra reconciliação de duas pontas com commits exclusivos.

## Preparação entregue nesta sessão

Leitor local `astra_operacoes/bridge_tools/read_three.py`: consulta GitHub, Drive e NYC independentemente, em clones privados/snapshots, sem tocar no índice do clone canônico. Emite resultado, hash, HEAD quando houver e recibo por rota; não faz push, não envia mensagens e não prova ACK de outro agente.
Uso a partir do workspace: `python3 astra_operacoes/bridge_tools/read_three.py --channel de_dell.md` (também de_laura.md e de_astra.md).

## Próxima configuração a concluir nos componentes existentes

Padronizar os consumidores no caminho Drive comprovado; adicionar leitura de contingência; corrigir o fetch inicial que impede o fallback; exigir duas entregas com readback; preservar mensagens independentes no NYC/Drive em caixas por emissor com IDs únicos e ACK, em vez de disputar snapshot/main descartável. Ensaiar falha de GitHub em fixtures/ambiente isolado e obter resposta real de outro agente por B e C. Depois incorporar aos leitores das rondas e validar acesso no Windows e servidores. Mantêm-se os crons existentes e a manutenção ZM; não criar quarto circuito.

Não há prova de duas vias de TROCA independentes durante pane; há três destinos existentes e acessíveis. Nenhuma alteração WordPress, cron, gate ou fila nesta missão. Chefia CL e palavra final Miguel preservadas.

## Teste integral e recibos

GitHub leu 2.576.223 bytes, SHA256 ec9c94def9116fc48a389278e1ac7fa1e7dd71c9b328f0520ba87e5aff724aaa; NYC leu 2.574.602 bytes, hash igual ao Drive. GitHub inclui CL-20260915-039 19:12, posterior ao corte das cópias. Drive falhou no primeiro teste conjunto, mas leitura integral repetida por rclone retornou exit 0 e SHA256 16895b455fdf6602c28c70839bf8f3c04d87614b378cb1b4a91565c166af40da. Não esconder a primeira falha nem atribuir causa sem prova. Recibos: /home/migueldorosario/Downloads/Antigravity Google/astra_operacoes/state/bridge_reads/20260915T221801387611Z/receipt.json e drive_retry.json. Não houve ensaio de escrita ou ACK.
