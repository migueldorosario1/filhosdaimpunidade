# 🎬 IDEIA_PRO_DSNUVEM_IDEIAS-009 — MÓDULO DE VÍDEO VERTICAL ROLANDO (estilo reels do 247) NO ESPELHO `cafezinho.news`

> **Bloco:** DSC 01/09/2026 23:5x BRT (ref DSC-20260901-027, ledger ds_celular.md) — ordem do Miguel via prints do site 247.
> **Arquiteto:** DS Nuvem Ideias (DS-N Ideias) · ronda 00:13-00:1x de 02/09/2026 (Tencent, 30/30).
> **Ambiente:** SOMENTE espelho `cafezinho.news` (O ESPELHO, criado 22/08). NUNCA no canônico `ocafezinho.com` — nada de produção.
> **Marcador de conclusão (quando visível):** `PRONTO_VIDEO_ESPELHO_TELEGRAM` em linha própria + link — o vigia do DSC manda no Telegram do Miguel.

---

## 1. A ideia (o que o Miguel viu no 247 e pediu)

Carrossel de **vídeo vertical curto** (reels) **ancorado sob a manchete**: comentarista falando · setas ‹ › · **mudo por padrão** · expandir tela cheia · badge de áudio ♪ · título + CTA de apoio · anúncio embaixo. "NÃO é pro contrato — é experiência no espelho, pra valer."

O que o DSC pede (5 itens): (1) procurar no Cérebro o que já existe; (2) avaliar com honestidade se TENHO CONDIÇÃO de montar (ordem do Miguel: "vê se o DSN Ideias tem condição") — se faltar runtime do ZM ou cooperação do DSN YouTube, DIZER o que falta e propor a dupla; (3) montar o módulo no espelho; (4) botar UM vídeo de teste (vertical, curto, da casa/YouTube DSN, nada sensível); (5) avisar quando visível com o marcador + link.

---

## 2. Pesquisa no Cérebro — o que JÁ EXISTE (tudo verificado nesta ronda)

### 2.1 Trabalho anterior DIRETO no espelho — bloco de vídeos (12/08)
`forum_bloco_videos_espelho_cafezinho_20260812.md`:
- Categoria **Vídeos (ID 28, term_taxonomy_id 29)** — JÁ EXISTE e é a categoria canônica de vídeo desde 12/08 (cat Youtube 20751 unificada na 28; hoje cat 28 ≈ **767 posts** no canônico).
- **Bloco "Vídeos" no `front-page.php` do tema `ocafezinho-portal`** (espelho): 1 hero + 5 na lista, `category__in => array(28)`, inserido após Tecnologia/antes de Cultura (12/08); **portado ao canônico 12/08 ~18:25** (bloco + menu + 106 posts).
- **mu-plugin `cafezinho-auto-cat-videos.php`** (canônico): todo post com embed YouTube (youtube.com/embed, youtu.be, watch?v=, wp-block-embed-youtube, youtube-nocookie) entra na cat 28 sozinho — cobre TODA fonte (repetidor, V4, agente YouTube, futuro).
- **Sync espelho** (`/root/sync_from_cafezinho.sh`, cron `:17`/hora): copia **posts + uploads** do canônico (delta por post_modified); **não copia tema** → bloco/mu-plugin no tema do espelho PERSISTE. Posts da cat 28 chegam ao espelho pelo sync.
- Menu do espelho/canônico: "Vídeos" no dropdown Editorias (canônico 12/08; pendência antiga: replicar item de menu no espelho — verificar com ZM se ainda falta).

### 2.2 Parente técnico mais próximo — o CARROSSEL Top 10 Tendências (19/08)
`forum_top10_tendencias_espelho_arquiteturas_v4_20260819.md` + `forum_algoritmo_velocidade_top10_espelho_20260820.md`:
- **Implementado como mu-plugin `cafezinho-top-tendencias.php` v2.0** (espelho E canônico): carrossel com **scroll-snap horizontal + clone-loop infinito em JS vanilla**, setas só ≥768px, badge "Top N", trava da manchete, anti-repetição via `$excludes` por referência entre blocos.
- **Padrão da casa validado**: mu-plugin no tema + hook no front-page + JS/CSS vanilla (sem dependência externa de lib) + backup `.bak_pre_*` antes + prova HTTP + push duplo NYC (espelho + canônico).
- Lição do 19/08: o Miguel aprova carrossel com deslize no celular e setas no desktop — o reels segue o MESMO padrão de UX, agora vertical.

### 2.3 Infra de vídeo — DSN YouTube (31/08-01/09)
`forum_ds_youtube_20260831.md` + `canal_ds_youtube.md`:
- **Cérebro na Tencent** (`~/ds_youtube/ds_youtube.py`, cron :07/:22/:37/:52, flock): fila → transcrição → flash matéria → **rascunho WP** (conta cafezinhodsn1, ID 5801) → canal + PEDIDO DE GATE. **RASCUNHO-ONLY PERMANENTE** (ordem Miguel ~17:30 de 01/09): o robô não publica; gate CL + palavra do Miguel; Publicador com GATE-TEXTO (post de autor 5801 nunca sai automático).
- **Porta no Dell** (`~/ds_youtube_fetcher/`, cron */5, flock): yt-dlp baixa legendas pt + info.json + **thumbnail**; YouTube bloqueia IP de datacenter → **o Dell (IP residencial) é a única porta que passa**; live → AGUARDANDO_VOD; sem legenda → áudio p/ Whisper.
- **Vídeos já baixados na fila**: 2 (Sabatinas das Cunhãs — VOD 68min horizontal; Ronnie Lessa/Record — entrevista longa). **NENHUM vertical curto ainda** — o teste do reels precisará de um Short.
- **Meta `_cafezinho_img_check`**: posts da cat 28 chegam com `ok:true, metodo=thumbnail_oficial_video` (gate de imagem satisfeito na origem — capa é a thumb oficial do vídeo; regra ZM-042: **Vídeos(28) com thumbnail_oficial_video NUNCA entram na caçada de capa**).

### 2.4 Outros achados
- **Regra "espelho é IGUAL ao canônico EM TUDO"** (ordem Miguel 23/08 ~20:20, forum_moka_espelho_experimentos adendo 9) — era do MOKA Reader; a ordem EXPLÍCITA de 01/09 ("montar JÁ no espelho", "experiência no espelho, pra valer") prevalece para este módulo. Registrar no canal quando executar.
- **Rito da casa para obras novas** (ZM-012, 30/08): "Ousadia (experiências) → Espelho 1 (confirmado) → Canônico (certinho)" — o espelho cafezinho.news é o **Espelho 1 (confirmado)** do portal de notícias; o reels é experiência confirmada por ordem do Miguel.
- **noindex**: espelho mantém fechado/noindex para o Google (preocupação do Miguel de 22/08) — o módulo não deve mexer nisso.
- **CTA de apoio**: NÃO encontrei URL de apoio/doação/assinatura da casa no repo (grep apoie/apoia/contribua/assine) — o CTA do módulo precisa de destino: item a definir com o Miguel (página `/apoie`? link externo?).
- **Espelho = DigitalOcean droplet NYC `159.65.177.60`**; WP `cafezinho-news`; App Password user Redator (ID 5470) no cofre NYC; Basic Auth foi desativada 12/08 (religar ao fim do teste — verificar estado atual com ZM).

---

## 3. Avaliação HONESTA de condição (pergunta do DSC item 2)

**Resposta direta: o DS-N Ideias NÃO tem condição de montar SOZINHO — e por lei, não deve.** Motivos (Lei de Poderes, inegociáveis):
1. **Não tenho credenciais de WordPress e não devo procurá-las** — montar o módulo exige aplicar mu-plugin/front-page no WP do espelho.
2. **Não executo em produção** — o espelho é ambiente de teste da casa, mas é infra WordPress viva (tema, mu-plugins, servidor); qualquer aplicação é execução de código em site, fora do meu ofício (pesquisa → arquitetura → plano → rascunhos).

**O que eu TENHO condição e entrego NESTA ronda:** pesquisa completa (§2), arquitetura (§4), plano de execução com backup/prova/rollback (§5) e **código pronto para aplicar** (§6). Ou seja: o módulo fica **engatilhado** — quem tem runtime aplica em minutos.

**Dupla proposta (o que falta e quem cobre):**
| Papel | Quem | O que faz |
|---|---|---|
| Arquiteto + código pronto | **DS-N Ideias** (eu) | este arquivo + rascunhos §6 |
| **Executor no espelho** (runtime WP + SSH) | **ZM** (ZCode/GLM-5.3, Dell — histórico de execução no espelho: 12/08 bloco vídeos, 19/08 carrossel, 25/08 MOKA) | backup → aplica mu-plugin/hook → php -l → prova HTTP/print → registro → rollback escrito |
| **Vídeo de teste** | **DSN YouTube** (cérebro Tencent + porta Dell) | fase 1: usar Short JÁ espelhado na cat 28 (zero dependência nova); fase 2: baixar 1 vertical curto exclusivo via porta Dell |
| Validação visual final | **Miguel** | vê no celular via marcador + link (vigia DSC) |

**Falta para executar:** ✓ do Miguel ao ZM para aplicar no espelho (a ordem DSC "montar já" é explícita e cobre o espelho — se o ZM ler assim, pode executar direto com o protocolo da casa: backup → prova → registro → rollback; confirmar com CL se houver dúvida de escopo).

---

## 4. Arquitetura da solução

### 4.1 Componentes
1. **Renderer (PHP)** — mu-plugin `cafezinho-video-reels.php` no tema `ocafezinho-portal` do **espelho** (padrão do `cafezinho-top-tendencias.php`): consulta posts da **cat 28** (Vídeos) dos últimos 30 dias com embed YouTube; extrai video_id; renderiza o módulo com `$excludes` (anti-repetição com os blocos abaixo, padrão 19/08).
2. **Player (HTML/JS/CSS vanilla)** — carrossel vertical 9:16:
   - **iframe youtube-nocookie** por slide, `autoplay=1&mute=1&playsinline=1&controls=0&loop=1&playlist=VIDEOID&rel=0&enablejsapi=1`;
   - **auto-avance 6-10s** (JS, pausa em hover/focus/toque);
   - **mudo por padrão** (pedido do Miguel) + **badge ♪** para ligar/desligar som (postMessage IFrame API: unMute/mute);
   - **setas ‹ ›** (desktop ≥768px) + **swipe** no celular (touchstart/touchend);
   - **expandir tela cheia** (Fullscreen API no container);
   - **título + CTA de apoio** sobrepostos na base (CTA: link a definir — §2.4);
   - **slot de anúncio embaixo** (placeholder vazio com data attribute — anúncio é decisão futura do Miguel);
   - **progresso** (barra fina por slide / pontos).
3. **Dados** — posts da cat 28 do próprio espelho (já sincronizados do canônico); nenhuma fonte nova. Se não houver posts com embed → módulo some (graceful, zero quebra).
4. **Onde roda** — espelho `cafezinho.news` (droplet NYC 159.65.177.60, tema `ocafezinho-portal`). Nada no canônico.

### 4.2 Fluxo (o que acontece quando abre a home do espelho)
```
home cafezinho.news
  → bloco MANCHETE (inalterado)
  → [NOVO] MÓDULO REELS (sob a manchete — posição A; alternativa B após Top 10, §4.3)
      slide ativo: iframe yt-nocookie mute=1 autoplay (9:16, max-h 70vh)
      badge ♪ · setas ‹ › (≥768px) · swipe (mobile) · expandir ⛶ · título+CTA · barra progresso
      auto-avance 6-10s → próximo post da cat 28 (loop)
  → carrossel Top 10 Tendências (inalterado, com $excludes do reels)
  → blocos editoriais (Nacional/Geo/… com $excludes do reels)
  → slot de anúncio embaixo do módulo (placeholder)
```

### 4.3 Posição — 2 opções (decisão do ZM/Miguel no deploy)
- **A (default, fiel à ordem):** imediatamente após a manchete, antes do Top 10 Tendências ("ancorado sob a manchete" = como no 247).
- **B:** após o carrossel Top 10 (se o Miguel achar que o reels "rouba" o espaço do trending).
- Implementação idêntica nas 2; mudar = mover 1 hook no front-page.

### 4.4 Vídeo de teste (2 fases)
- **Fase 1 (mais rápida, zero dependência):** o módulo estreia com **Shorts/verticais que JÁ ESTÃO espelhados na cat 28** (posts embed de YouTube curtos vindos do canônico). Testa o módulo inteiro (auto-avance, mudo, setas, expandir) sem baixar nada.
- **Fase 2 (se o Miguel quiser vídeo exclusivo da casa):** DSN YouTube baixa **1 vídeo vertical curto** (ex.: corte de 15-60s de um vídeo já licenciado dos canais da casa patrulhados — Opera Mundi/Fórum/247/ICL/DCM — ou Short enviado pelo Miguel) via porta Dell (única porta que passa no bloqueio do YouTube), sobe como mídia WP no espelho e o slide usa `<video poster=thumb>` nativo ou embed. Crédito do canal no canto (regra da casa).
- Nada sensível; vídeo de teste assinado com a ref do módulo.

---

## 5. Plano de execução (para o EXECUTOR ZM — numerado, com riscos e reversibilidade)

**Protocolo da casa: backup → prova → registro → rollback escrito.**

1. **Backup do espelho** (antes de qualquer alteração): copiar `front-page.php` + `functions.php` + diretório `mu-plugins/` + nginx conf → `/root/backup_video_reels_espelho_20260902/` (SHA256 de cada arquivo; padrão 12/08).
2. **Criar mu-plugin** `cafezinho-video-reels.php` (rascunho §6.1) no espelho + **CSS/JS** (ou assets no tema, §6.2).
3. **Hook no `front-page.php`** do espelho: inserir `cafezinho_reels_render()` após o bloco da manchete (posição A; B se o Miguel pedir), com `$excludes` por referência.
4. **Lint + prova estática:** `php -l` nos 2 arquivos; `curl -sI https://cafezinho.news/` → HTTP 200; HTML contém `.cafezinho-reels`; cache WP Rocket do espelho purgado (se houver); hard refresh.
5. **Vídeo de teste:** fase 1 — conferir que há posts da cat 28 com embed nos últimos 30 dias no espelho (se vazio, subir 1 post de teste draft/publish no espelho com embed de um Short); fase 2 (opcional) — DSN YouTube baixa vertical curto e entrega no espelho.
6. **Prova visual:** screenshot/print da home (desktop + mobile) e do módulo; link `https://cafezinho.news/` → postar bloco no `de_ideias.md` (ou canal do ZM) com **`PRONTO_VIDEO_ESPELHO_TELEGRAM` em linha própria + link** — vigia DSC manda no Telegram do Miguel.
7. **Registro:** fórum/canal com refs (backup SHA, HTTP 200, prints, posição escolhida, decisões) — padrão da casa.
8. **Rollback escrito (1 comando cada):** restaurar `front-page.php` do backup + remover/desativar mu-plugin; módulo some sem tocar em posts. Testado antes de dar por concluído.

### Riscos e mitigação
| Risco | Mitigação |
|---|---|
| YouTube bloqueia autoplay com som | mudo por padrão É o pedido; iframe `mute=1` é permitido; badge ♪ desmutado via postMessage |
| Vários iframes autoplay simultâneos (peso) | só o slide ativo carrega src (JS seta src ao ativar; demais = poster/thumb) |
| 9:16 ocupa espaço no desktop | max-height 70vh + layout compacto (módulo colapsa verticalmente); desktop vê setas; mobile vê swipe |
| Fase 2 depende da porta Dell (YouTube bloqueia datacenter) | fase 1 não depende de nada novo; porta Dell é a única via e JÁ funciona (2 vídeos baixados) |
| Sync do espelho não copia tema | módulo no tema PERSISTE (padrão 12/08 comprovado) |
| noindex do espelho | não tocar em robots/indexação |
| Vazio de posts cat 28 com embed | renderer some (graceful) — nunca quebra a home |
| Conflito com regra "espelho = canônico em tudo" (23/08) | ordem explícita de 01/09 prevalece; registrar no canal |

---

## 6. Rascunhos de código (dentro do arquivo da ideia — NUNCA em produção)

### 6.1 `cafezinho-video-reels.php` (mu-plugin, espelho) — esqueleto renderer

```php
<?php
/**
 * Plugin Name: Cafezinho Video Reels (espelho)
 * Description: IDEIA-009 — carrossel de video vertical curto (reels) sob a manchete.
 *              SOMENTE espelho cafezinho.news. Nada no canonico.
 * Version: 0.1 (rascunho DS-N Ideias 20260902 — validar com php -l antes de ativar)
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

function cafezinho_reels_extrair_video_id( $html ) {
    // mesma familia de deteccao do mu-plugin cafezinho-auto-cat-videos
    $padroes = array(
        '~youtube(?:-nocookie)?\.com/embed/([A-Za-z0-9_-]{6,20})~',
        '~youtube\.com/watch\?v=([A-Za-z0-9_-]{6,20})~',
        '~youtu\.be/([A-Za-z0-9_-]{6,20})~',
        '~youtube\.com/shorts/([A-Za-z0-9_-]{6,20})~',
    );
    foreach ( $padroes as $re ) {
        if ( preg_match( $re, $html, $m ) ) { return $m[1]; }
    }
    return false;
}

function cafezinho_reels_posts( $excluir = array(), $limite = 5 ) {
    // posts da cat 28 (Videos), 30 dias, com embed youtube no conteudo
    $q = new WP_Query( array(
        'cat'              => 28,
        'posts_per_page'   => $limite,
        'post_status'      => 'publish',
        'date_query'       => array( array( 'after' => '30 days ago' ) ),
        'post__not_in'     => (array) $excluir,
        'no_found_rows'    => true,
        'ignore_sticky'    => true,
    ) );
    $videos = array();
    foreach ( $q->posts as $p ) {
        $id = cafezinho_reels_extrair_video_id( $p->post_content );
        if ( ! $id ) { continue; }
        $videos[] = array(
            'video_id' => $id,
            'titulo'   => get_the_title( $p ),
            'link'     => get_permalink( $p ),
            'thumb'    => get_the_post_thumbnail_url( $p, 'medium_large' ),
        );
        if ( count( $videos ) >= $limite ) { break; }
    }
    return $videos;
}

function cafezinho_reels_render() {
    $videos = cafezinho_reels_posts();
    if ( empty( $videos ) ) { return ''; } // graceful: sem videos, sem modulo
    // nota: ids usados no modulo devem entrar em $excludes dos blocos abaixo (padrao 19/08)
    ob_start(); ?>
    <section class="cafezinho-reels" data-cafezinho-reels>
      <div class="cafezinho-reels__viewport">
        <?php foreach ( $videos as $i => $v ) :
          $src = 'https://www.youtube-nocookie.com/embed/' . $v['video_id']
               . '?autoplay=1&mute=1&playsinline=1&controls=0&loop=1'
               . '&playlist=' . $v['video_id'] . '&rel=0&enablejsapi=1';
          $ativo = ( 0 === $i ) ? ' is-active' : ''; ?>
          <article class="cafezinho-reels__slide<?php echo $ativo; ?>" data-slide="<?php echo (int) $i; ?>">
            <div class="cafezinho-reels__player" data-player>
              <iframe data-src="<?php echo esc_url( $src ); ?>" title="<?php echo esc_attr( $v['titulo'] ); ?>"
                allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>
            </div>
            <button class="cafezinho-reels__som" data-mute aria-label="Ligar/desligar som">♪</button>
            <button class="cafezinho-reels__expand" data-expand aria-label="Tela cheia">⛶</button>
            <div class="cafezinho-reels__meta">
              <h3 class="cafezinho-reels__titulo"><a href="<?php echo esc_url( $v['link'] ); ?>"><?php echo esc_html( $v['titulo'] ); ?></a></h3>
              <a class="cafezinho-reels__cta" href="<?php echo esc_url( $v['link'] ); ?>">Leia no Cafezinho →</a>
            </div>
            <span class="cafezinho-reels__badge">Top <?php echo (int) $i + 1; ?></span>
          </article>
        <?php endforeach; ?>
      </div>
      <button class="cafezinho-reels__seta cafezinho-reels__seta--prev" data-prev aria-label="Anterior">‹</button>
      <button class="cafezinho-reels__seta cafezinho-reels__seta--next" data-next aria-label="Próximo">›</button>
      <div class="cafezinho-reels__progresso" data-progresso></div>
      <!-- slot de anuncio (decisao futura do Miguel) -->
      <div class="cafezinho-reels__anuncio" data-anuncio></div>
    </section>
    <?php return ob_get_clean();
}
```

### 6.2 JS/CSS (inline no mu-plugin via `wp_add_inline_script`/`wp_add_inline_style`, ou assets no tema)

```js
// auto-avance 6-10s, pausa hover/focus/toque; setas >=768px; swipe mobile; expandir (Fullscreen API); som (postMessage IFrame API)
(function () {
  var root = document.querySelector('[data-cafezinho-reels]');
  if (!root) return;
  var slides = Array.prototype.slice.call(root.querySelectorAll('[data-slide]'));
  var atual = 0, timer = null, INTERVALO = 8000;
  function ativar(n) {
    slides[atual] && slides[atual].classList.remove('is-active');
    atual = (n + slides.length) % slides.length;
    slides[atual].classList.add('is-active');
    var f = slides[atual].querySelector('iframe');
    if (f && !f.src) { f.src = f.getAttribute('data-src'); f.play && f.play(); } // lazy: so o ativo carrega
    // demais slides: remove src p/ nao tocar varios ao mesmo tempo
    slides.forEach(function (s, i) { if (i !== atual) { var x = s.querySelector('iframe'); if (x && x.src) { x.removeAttribute('src'); } } });
  }
  function play() { parar(); timer = setInterval(function () { ativar(atual + 1); }, INTERVALO); }
  function parar() { timer && clearInterval(timer); }
  root.addEventListener('mouseenter', parar); root.addEventListener('mouseleave', play);
  root.addEventListener('touchstart', parar, { passive: true }); root.addEventListener('touchend', play);
  // setas
  root.querySelector('[data-prev]').addEventListener('click', function () { ativar(atual - 1); });
  root.querySelector('[data-next]').addEventListener('click', function () { ativar(atual + 1); });
  // swipe
  var x0 = null;
  root.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  root.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null; if (Math.abs(dx) > 40) { ativar(atual + (dx < 0 ? 1 : -1)); } }, { passive: true });
  // som (badge ♪) via IFrame API do YouTube
  root.querySelector('[data-mute]').addEventListener('click', function () {
    var f = slides[atual].querySelector('iframe');
    if (!f) return;
    this.classList.toggle('is-mudo');
    var mudo = this.classList.contains('is-mudo');
    f.contentWindow.postMessage(JSON.stringify({ event: 'command', func: mudo ? 'mute' : 'unMute', args: [] }), '*');
  });
  // expandir
  root.querySelector('[data-expand]').addEventListener('click', function () {
    var p = root.querySelector('.cafezinho-reels__player');
    if (document.fullscreenElement) { document.exitFullscreen(); } else { p.requestFullscreen && p.requestFullscreen(); }
  });
  play();
})();
```

```css
/* espelho: modulo reels 9:16 sob a manchete */
.cafezinho-reels{position:relative;max-width:420px;margin:1rem auto}
.cafezinho-reels__viewport{position:relative;aspect-ratio:9/16;max-height:70vh;overflow:hidden;background:#000;border-radius:12px}
.cafezinho-reels__slide{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .3s}
.cafezinho-reels__slide.is-active{opacity:1;visibility:visible}
.cafezinho-reels__player,.cafezinho-reels__player iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.cafezinho-reels__som,.cafezinho-reels__expand{position:absolute;z-index:3;background:rgba(0,0,0,.55);color:#fff;border:0;border-radius:50%;width:34px;height:34px;cursor:pointer}
.cafezinho-reels__som{top:12px;right:12px}
.cafezinho-reels__expand{top:52px;right:12px}
.cafezinho-reels__meta{position:absolute;left:0;right:0;bottom:0;z-index:3;padding:2rem .75rem .6rem;background:linear-gradient(transparent,rgba(0,0,0,.85));color:#fff}
.cafezinho-reels__titulo{font-size:.95rem;margin:0 0 .3rem}
.cafezinho-reels__titulo a{color:#fff;text-decoration:none}
.cafezinho-reels__cta{display:inline-block;font-size:.8rem;font-weight:700;color:#ffd700}
.cafezinho-reels__seta{position:absolute;top:50%;transform:translateY(-50%);z-index:4;background:rgba(0,0,0,.55);color:#fff;border:0;border-radius:50%;width:36px;height:36px;font-size:1.4rem;cursor:pointer}
.cafezinho-reels__seta--prev{left:6px}.cafezinho-reels__seta--next{right:6px}
.cafezinho-reels__anuncio{min-height:90px;margin-top:.75rem;border:1px dashed #ccc;display:flex;align-items:center;justify-content:center;color:#888;font-size:.75rem}
@media(max-width:767px){.cafezinho-reels__seta{display:none}} /* mobile = swipe */
```

> **Nota do rascunho:** código é PROPOSTA de arquitetura — o executor (ZM) valida (php -l, lint JS), ajusta ao tema real (nomes de hooks do `ocafezinho-portal`) e aplica com backup. Nada disso toca produção por mim.

---

## 7. O que precisa do Miguel / da casa

1. **✓ ao ZM para executar no espelho** (backup → prova → registro → rollback) — ou o ZM lê a ordem DSC 23:5x como cobertura suficiente e executa com o protocolo da casa.
2. **Posição do módulo:** A (sob a manchete, default) ou B (após Top 10).
3. **Destino do CTA de apoio** (não existe URL de apoio/assinatura na casa — §2.4): página `/apoie` no espelho? link externo? só o link do post?
4. **Vídeo de teste:** fase 1 (Short já espelhado na cat 28) OK? ou quer fase 2 (DSN YouTube baixa vertical curto exclusivo via porta Dell)?
5. **Slot de anúncio:** placeholder por ora, ou já tem anunciante/página?
6. **Validação visual no celular** (via marcador + link quando o módulo estiver no ar).
7. Depois de homologado no espelho, **portar ao canônico é decisão separada do Miguel** (fora do escopo desta ideia — espelho só).

---

*Pesquisa, arquitetura, plano e rascunhos desenvolvidos SOZINHO pelo DS Nuvem Ideias (ronda 00:13-00:1x de 02/09/2026). Fonte de verdade da ronda: repo `cerebro-miguel` (ff-only OK, b5433194c..8e06d6a55).*
— DS Nuvem Ideias (DS-N Ideias) · 20260902 00:15:44 BRT
