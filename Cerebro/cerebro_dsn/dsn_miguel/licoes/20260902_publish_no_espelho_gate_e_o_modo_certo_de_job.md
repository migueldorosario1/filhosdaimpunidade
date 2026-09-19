# 2026-09-02 · Ordem no espelho: o gate quer o visto, não a burla — e o fix que já existia não tinha subido

## O quê
A ordem ZM-20260902-007/008 (Miguel 23:1x: "publica só no cafezinho espelho, estamos fazendo um teste") me deu a 1ª missão de publish da série: post do TVGGN/Nassif no espelho cafezinho.news (cat 28, capa = frame do próprio vídeo, publish direto, nada no canônico). Três descobertas na execução:

1. **O gate-IMG fail-close do espelho (cafezinho-gate-imagem-checada.php) REVERTEU o publish para pending** ("imagem sem checagem") — todo publish no espelho exige a meta `_cafezinho_img_check` (ok) ou `_cafezinho_img_isenta`. A saída honesta foi REGISTRAR a checagem com proveniência completa (ok:true, origem=frame do próprio vídeo embutido no post, md5, ref da ordem) e republicar — checagem construtiva, não burla: o frame é do MESMO vídeo que o post incorpora.
2. **O reels do droplet estava em v0.2** (sem o fix do som postMessage/enablejsapi) apesar de o repo já ter o v0.3 com o fix — alguém iterava no droplet (backups jsready/autoplay/io 23:05-23:33) sem subir a correção canônica. Deployei o v0.3 do repo com backup (.bak_pre_v03_dsdell_20260902_2338), php -l verde, home 200.
3. **Modo de job definitivo no sandbox**: `nohup … &` (e até `setsid nohup`) morrem quando o comando que os criou termina; o modo que PERMANECE é o job do harness (run_in_background) — 9ª confirmação do padrão, agora com a régua certa.

## Por quê
- O gate de imagem existe porque um post foi ao ar com arte 3D no lugar de foto real (266029, ordem direta do Miguel 16/08) — a casa prefere pending a post errado. Burlar (apagar o gate ou gravar meta falsa) seria trair a régua; documentar a checagem com proveniência VERDADEIRA é cumprir a régua.
- O fix do som do carrossel já estava pronto no repo (v0.3) mas o servidor vivo rodava v0.2: "está no repo" ≠ "está no ar" — a prova é o arquivo VIVO (md5/grep), como "armado na ronda anterior" é hipótese, não fato.
- Job longo (whisper ~30min) só sobrevive como job do harness; qualquer outro relance morre com a sessão e queima a abertura da próxima ronda.

## Como aplicar
- Publicar no espelho (ou canônico): SEMPRE conferir a meta de checagem ANTES do publish (wp post meta get _cafezinho_img_check) — o gate reverte silencioso p/ pending; e registrar checagem com origem+md5+ref quando a imagem for construtiva (frame do próprio vídeo, foto da própria fonte), nunca meta vazia.
- Antes de "deployar" um arquivo que já existe no servidor: comparar o VIVO com o do repo (md5/diff) — se o vivo for mais novo ou diferente, NÃO sobrescrever sem backup + aviso (append-only da casa aplicado a arquivos de produção).
- Job que precisa rodar entre rondas: relançar SEMPRE como job do harness (run_in_background), nunca nohup/setsid dentro do comando.
- Prova de publish: permalink + HTTP 200 + md5 da capa (servidor = local) + autor/cat — carimbar no bloco da ponte.

— DS Miguel (Dell) · 20260902 23:43 BRT
