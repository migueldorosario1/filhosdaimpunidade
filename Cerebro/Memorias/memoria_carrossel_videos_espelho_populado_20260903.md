# Memória técnica — Carrossel de vídeos do espelho (cafezinho.news) populado + reprodução curada + merge v0.3

**Data:** 03/09/2026 ~02:5x BRT · **Autor:** ZCode/Qwen 3.8 (Dell) · **Fórum companion:** `Foruns/forum_carrossel_videos_miguel_captacao_automatica_20260902.md` §7 · **IDEIAs:** 009/011 (`Foruns/ideias/`)

## Contexto

Ordem do Miguel (voz 02/09 ~22:4x): carrossel do espelho "foi feito sem vídeo" — botar vídeos de verdade (mín. 6), testar com quaisquer videos, escolher a melhor forma de segurar o leitor no site. O módulo `cafezinho-video-reels.php` (v0.2, sessão ZM/GLM-5.3 = DS-Dell) existia mas renderizava VAZIO no espelho (nenhum post cat 28 com `_cafezinho_recorte_mp4`).

## Execução (dados)

- 7 posts de teste cat 28 no espelho: IDs **400282, 400284, 400286, 400288, 400290, 400292, 400294** (autor 5795, publish, slugs `carrossel-video-teste-1..7.htm`).
- Metas de cada post: `_cafezinho_recorte_mp4` (URL pública do MP4), `_cafezinho_reels_teste=1` (marcador de limpeza), `_cafezinho_img_check` = `{"ok":true,"metodo":"thumbnail_oficial_video",...,"lei":"ZM-042..."}`, `_thumbnail_id` = attachment do pôster (IDs ímpares 400281–400293).
- Pôsteres 720×1280 gerados NA DELL (espelho sem ffmpeg): `ffmpeg -ss 1.5 -vf "crop=trunc(ih*9/16/2)*2:trunc(ih/2)*2,scale=720:1280" -frames:v 1 -q:v 3`; importados com `wp media import`.
- MP4s (já nos uploads do espelho, zero download): `tse-urna-segura-1786281741.mp4`, `kakay-moraes-prudente-20260723.mp4`, `corte-elmano-seguranca-ponto-poder.mp4`, `corte-elmano-pastor-gcmais.mp4`, `corte-ciro-mossad-legendado.mp4`, `corte-ciro-mossad-gcmais.mp4`, `china-ormuz-legendado-vertical.mp4`.
- Sync horário `:17` (`/root/sync_from_cafezinho.sh`, REPLACE INTO por ID) é seguro p/ faixa 400k (canônico máx ~268700). Kill-switch `/root/SYNC_PAUSED`.

## Fixes de reprodução no mu-plugin (3, provados)

1. **DOMContentLoaded:** o `<script>` inline saía ANTES da `<section data-cafezinho-reels>` → `querySelector` null → IIFE morria. Init embrulhado: `if(document.readyState==='loading'){addEventListener('DOMContentLoaded',init)}else{init()}`.
2. **Tag video:** `muted autoplay loop playsinline preload="metadata"` (antes `preload="none"` sem autoplay).
3. **IntersectionObserver media-aware:** ao entrar na tela → `play()` timer + `m.play()` no vídeo ativo; ao sair → `parar()` + `m.pause()` (economiza banda; antes o IO só gerenciava o timer e o carrossel nasce abaixo da dobra).

## Clobber + merge (coordenação com a sessão paralela)

- 02:39 (03/09) a sessão DS-Dell deployou **v0.3** (som via postMessage `enablejsapi` p/ iframes YT + CSS da página do post cat 28 — melhorias reais) e **sobrescreveu meus 3 fixes** (carrossel congelou: JS morria de novo no load).
- Merge cirúrgico: reapliquei os 3 fixes SOBRE o v0.3 preservando as melhorias deles (python com assert count==1 por fix; `php -l` limpo).
- Backups no espelho (`/var/www/cafezinho-news/wp-content/mu-plugins/`): `.bak_pre_jsready_20260903` (sha a966fc67b857be5e) · `.bak_pre_autoplay_20260903` (027edf558152b7bf) · `.bak_pre_io_20260903` (57901d4ddbf5553c) · `.bak_pre_v03_dsdell_20260902_2338` (da outra sessão) · `.bak_pre_merge_qwen_20260903` (6e32f122add1ae01 = v0.3 puro pré-merge).
- Metas `_cafezinho_recorte_mp4` de 400288/400292 tinham sumido (restauradas com `wp post meta update`).

## Rollback

- Dados: `wp post delete --force 400282 400284 400286 400288 400290 400292 400294` + attachments 400281–400293 (ou listar por `--meta_key=_cafezinho_reels_teste`).
- Módulo: v0.3 puro = `cp .bak_pre_v03_dsdell... ` (ou `.bak_pre_merge_qwen_20260903`, idêntico); v0.2+fixes = `.bak_pre_io_20260903`.

## Provas

- Servidor: `curl -sk https://127.0.0.1/ -H 'Host: cafezinho.news'` = 6 `data-slide` + seção presente; HTTP 200 externo.
- Navegador (IAB ZCode): vídeo tocando (currentTime 4.5→6.5s; 15.5s no ciclo seguinte), auto-avanço 8s troca de slide e pausa o anterior, screenshot do carrossel com vídeo do Kakay tocando + frame t=15.5s do China/Ormuz (legenda amarela assada visível).
- **Artefato do ambiente de teste (não é bug do site):** o webview embutido do ZCode (IAB) bloqueia autoplay de nós criados durante o load inicial da página (sem foco OS; `hasFocus=false` permanente; `window.focus()`/cliques não destravam). Nós criados pós-load tocam normal. Provas no IAB feitas recriando o nó (cloneNode+replace). Navegadores reais: autoplay mudo = permitido sem gesto (padrão web).

## Estado / próximos passos

- Cortes REAIS da Trilha B (cat 28 + `_cafezinho_recorte_mp4`, mais novos) entram no topo do carrossel automaticamente; post 400296 da sessão paralela já apareceu (fallback embed quando <6 MP4s… agora com 7 MP4s o limite 6 corta o mais antigo).
- Limpeza futura dos testes: 1 comando pela meta `_cafezinho_reels_teste`.
- Lição p/ casa: duas sessões no mesmo mu-plugin = clobber certo; registrar linha no MONITORAMENTO antes de tocar arquivo quente e conferir mtime+grep antes de assumir que o próprio código ainda está no ar (padrão da memória `cerebro-clobber-escrita-paralela-copia-velha`).

---

## Adendo v0.4 + matérias (03/09 ~08:4x, Qwen 3.8)

**Bug do som (v0.3):** botão ♪ renderizado POR SLIDE no loop PHP, mas listener só no primeiro + `ativar()` resetava `som_on=false` a cada troca → clique morto na maioria do tempo e som que não persistia. **v0.4:** botão global único (irmão das setas), `setSom(som_on)` re-aplicado em `ativar()`, clique no vídeo liga som (toggle pause/play depois), ícone 🔇 pulsante/🔊, 2,7rem. Backup no espelho: `cafezinho-video-reels.php.bak_pre_v04_somglobal_20260903`. Provas: muted=false após clique no botão; muted=false mantido através de auto-avanços (slides 2→4); clique no vídeo 🔇→🔊; screenshot com 🔊 confirmado por visão.

**Armadilha wp_emoji:** `button.textContent` vazio nos evaluates porque o WP converte emoji do markup em `<img class="emoji" alt="🔇">` — usar `img.emoji.alt` para ler o estado visual.

**Matérias:** transcrições whisper large-v3-turbo (CPU, ~2min/vídeo; `--language pt` não impede saída em inglês quando o áudio é inglês — China/Ormuz saiu EN). 7 matérias com citações literais publicadas via `wp post update <id> arquivo.html --post_title --post_excerpt` (ARMAZILHA: `wp post update` com caminho de arquivo exige o arquivo NA MÁQUINA do wp-cli — scp antes, e mkdir do diretório destino ANTES do scp, senão scp falha silencioso com 2>/dev/null). Nome de arquivo ≠ conteúdo: o "corte-ciro-mossad" fala de segurança pública com IA no Ceará; conferir transcrição antes de escrever título.

**Estados v0.4:** slides usam classe `is-active` (v0.2 usava `ativo`); clique físico (CUA) no IAB não dispara handlers de seta de forma confiável — clique sintético `el.click()` via evaluate sim (artefato do IAB, não do site).

**Salto NTP de ~8h no meio da sessão (03/09):** relógio local marcava ~00:4x quando o real era ~08:4x BRT; NTP corrigiu durante o trabalho (ls/git 08:2x+). Carimbos "~00:4x" foram corrigidos para "~08:4x" por sed nos registros. Lição: rodar `date` fresco NO MOMENTO de cada carimbo, não confiar no último valor visto (reforça a memória rodape-brt-virada-utc-date-real).
