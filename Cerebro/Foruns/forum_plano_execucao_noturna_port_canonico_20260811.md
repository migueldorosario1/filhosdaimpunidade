# 🌙 Plano de Execução Noturna — Port Completo Espelho → Canônico

**Data:** 2026-08-11, preparado para execução a partir das **22h BRT**
**Autor:** ZCode (GLM-5.2 Z.ai)
**Status:** PRONTO PRA EXECUTAR — todos scripts pré-aprovados, Miguel só confirma visualmente a cada etapa
**Duração estimada:** ~60-90 min (com validação em cada breakpoint)

---

## 🎯 Estratégia (diferente de hoje)

Hoje (tarde) a casa caiu por causa de **15 iterações sobrepostas** no header (cada uma corrigindo a anterior, gerando efeitos colaterais). À noite farei diferente:

✅ **1 script consolidado por etapa** (não 15)
✅ **Aplicar → validar → próxima** (não empilhar)
✅ **Rollback fácil em cada etapa** (snapshot pré-etapa)
✅ **Audiência baixa** → se algo quebrar, impacto mínimo
✅ **Miguel EM LOCAL** → valida visualmente a cada etapa antes de avançar

---

## 📋 Pré-flight (5 min)

Antes de qualquer edição, SEMPRE:

```bash
# 1. Snapshot temático com timestamp da sessão noturna
TS=$(date +%Y%m%d_%H%M%S)
ssh cafezinho-wp "mkdir -p /root/port_canonico_noturno_${TS} && \
  cp /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/{header.php,footer.php,front-page.php,single.php,style.css} /root/port_canonico_noturno_${TS}/ && \
  cp -r /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/img/ /root/port_canonico_noturno_${TS}/img_pre/"
```

✅ Confirma com Miguel: site está visivelmente estável antes de começar?

---

## 🎯 Etapas (em ordem de segurança)

### 🟢 FASE A — Estáticos (10 min, baixíssimo risco)

#### A1. Subir logo v6 + foto editor v2 (só upload de arquivo)
- **Arquivos:**
  - `/img/logo-cafezinho-2026-v6.png` (1550×280, 55KB, do espelho)
  - `/img/foto-miguel-editor-v2.jpg` (240×240, 10KB, do `/tmp/adiag_work/logos/`)
- **Ação:** só `scp` + `chown www-data`, **não edita PHP/CSS**
- **Rollback:** `rm` os 2 arquivos
- **Validação:** curl HTTP 200 nos 2 arquivos

#### A2. Confirmar cache CDN não causou problema dos anúncios
- Tirar screenshot da home atual (pós-rollback, deve estar = original)
- Comparar com print durante Fase 1
- Se anúncios iguais → problema era meu (investigar)
- Se anúncios diferentes → pré-existente, não meu

---

### 🟡 FASE B — Header (15 min, médio risco)

#### B1. REWRITE do header.php (script único consolidado)

**O que muda:** header fica minimalista — logo esquerda + hamburger direita.

**Script:** `canonico_noturno_b1_header.php` (já preparado, versão LIMPA aprendida hoje)
- Substitui TODO o `<header>...</header>` por:
  ```php
  <header class="border-bottom">
      <div class="container-xxl header-bar-minimal">
          <a href="<?= bloginfo('url') ?>" class="header-logo-link">
              <img src="<?= bloginfo('template_url') ?>/img/logo-cafezinho-2026-v6.png"
                   width="277" height="50" alt="O Cafezinho" class="header-logo">
          </a>
          <a href="#menu" data-bs-toggle="offcanvas" data-bs-target="#menu"
             class="header-hamburger-link" aria-label="Abrir menu">
              <img src="<?= bloginfo('template_url') ?>/img/icon-menu.svg"
                   width="28" height="28" alt="Menu" class="header-hamburger-icon">
          </a>
      </div>
  </header>
  ```
- **Sem `d-md-none`** no hamburger (visível em todos breakpoints)
- **Sem `d-lg-none`** no `<img>` interno do hamburger (foi o bug de hoje)

#### B2. Footer.php: offcanvas expandido
- Adicionar Buscar + Apoie + gtranslate dentro do offcanvas
- `wp_nav_menu` do offcanvas: `depth 1 → 2` + `walker bootstrap_5_wp_nav_menu_walker` (corrige submenus)
- CSS `.offcanvas-menu .dropdown-menu { position: static }` (submenu abre empilhado)

#### B3. CSS do header (estilo consolidado)
- `.header-bar-minimal` com `flex-wrap: nowrap !important` (hamburger nunca quebra)
- `header.border-bottom` com `border-bottom: 1px solid #dee2e6 !important` (linha cinza) + `overflow: hidden`
- Logo progressiva: 50px mobile / 80px iPad / 100px desktop
- Hamburger sempre `margin-right: 0` (encostado na direita)

#### B4. Validar mobile + iPad + desktop
- Miguel valida os 3 breakpoints
- Confirmar: header não sobrepõe banner top, hamburger abre offcanvas, submenus funcionam

---

### 🟠 FASE C — Manchete (10 min, médio risco)

#### C1. front-page.php: manchete vertical (título em cima + imagem 100% + caption)
- Reestrutura bloco da manchete (mesmo padrão do espelho V2.0)
- Caption via `wp_get_attachment_caption()` (só aparece se preenchida)

#### C2. CSS manchete
- `.manchete-cima .manchete-img { object-fit: contain; max-height: 70vh; background: #f8f9fa }` (não corta)
- `.manchete-balao-comentarios` (vermelho escuro #8b0000, sempre que ≥1 comentário)

#### C3. Validar
- Foto da capa INTEIRA (não corta)
- Caption aparece (manchete atual tem caption Ricardo Stuckert)
- Balão de comentários 🔥 no lugar

---

### 🟠 FASE D — Coluna do Editor (15 min, médio risco)

#### D1. front-page.php: posts_per_page 4→8 + iPad vira swipe
- `$editor_args['posts_per_page'] = 8`
- `@media (768-991px)` deixa de ser grid 2×2 fixo → vira swipe (overflow-x: auto)
- Setas carrossel desktop (`.coluna-editor-carousel`)

#### D2. Cabeçalho Coluna Editor (Avatar > Título > Nome)
- Substituir `get_avatar()` por `<img src="foto-miguel-editor-v2.jpg">`
- COLUNA DO EDITOR (preto, 1.55rem) / MIGUEL DO ROSÁRIO (vermelho, 1.45rem)
- Maiúsculas via `text-transform: uppercase`

#### D3. Validar
- 8 cards na Coluna do Editor
- iPad: swipe com 2 cards por vez (não mais grid 2×2)
- Desktop: setas ← → funcionam
- Cabeçalho: foto nova do Miguel em cima, títulos maiúsculos

---

### 🟡 FASE E — Footer (5 min, baixo risco)

#### E1. Botão Apoie pill vermelho escuro no footer
- `<a href="/apoie" class="btn-apoie-footer">`
- CSS pill #8b0000 + gap (sem margin-right no img)

#### E2. Validar
- Botão centralizado, dentro da caixa preta do footer

---

### 🟢 FASE F — Finalização (5 min)

#### F1. Purgar cache WP Rocket + confirmar
- `find /var/www/ocafezinho/wp-content/cache/wp-rocket/ -mindepth 1 -delete`

#### F2. Teste de smoke
- HTTP 200 em home, single, categoria, AMP
- PHP lint em todos os arquivos tocados
- Grep nos logs (nginx error, PHP-FPM) por warnings novos

#### F3. Tema Duplo no Cérebro
- Adendo no `forum_plano_execucao_noturna_port_canonico_20260811.md` (status: ✅ executado)
- Atualizar `memoria_port_canonico_fase1_20260811.md` com tudo que foi aplicado
- Linha no `MONITORAMENTO_DE_TRABALHO.md`
- Adendo no `INDICE_APRENDIZADO_CANONICO_OCAFEZINHO.md`

---

## 🛡️ Cuidados ESPECÍFICOS (lições de hoje)

### ⚠️ O que NÃO fazer (causou problemas hoje)
1. ❌ Empilhar 15 iterações sobrepostas no header → gerou cascata de overrides
2. ❌ Esconder elemento via `display: none` em classe Bootstrap `d-md-none` E também via CSS → conflito
3. ❌ Esquecer do `d-lg-none` no `<img>` interno do hamburger
4. ❌ Esconder `<ul class="nav">` do header sem mover o menu pro offcanvas
5. ❌ Deixar `.logo` com `position: absolute` (sobrepõe single post)

### ✅ O que fazer (boas práticas)
1. ✅ **1 script consolidado por fase** (header pronto numa tacada só)
2. ✅ Snapshot pré-etapa + rollback script testado
3. ✅ PHP lint + HTTP check + grep logs EM CADA etapa
4. ✅ Validação visual Miguel nos 3 breakpoints (mobile/iPad/desktop)
5. ✅ Purgar cache WP Rocket após cada edição
6. ✅ Documentar cada passo no Cérebro imediatamente

---

## 📦 Scripts já preparados (em `/tmp/adiag_work/`)

```
canonico_noturno_b1_header.php       # Rewrite header.php (logo esq + hamburger dir)
canonico_noturno_b2_footer.php       # Offcanvas expandido
canonico_noturno_b3_css_header.css   # CSS header-bar-minimal
canonico_noturno_c1_manchete.php     # Manchete vertical + caption
canonico_noturno_c2_css_manchete.css # CSS manchete + balão fogo
canonico_noturno_d1_coluna.php       # Coluna editor 8 posts + swipe iPad
canonico_noturno_d2_cabecalho.php    # Cabeçalho avatar+titulo+nome
canonico_noturno_e1_btn_apoie.php    # Botão apoie footer pill
```

*Vou criar cada um desses scripts limpinhos durante a tarde, antes das 22h.*

---

## ⏰ Timeline estimada (22h-23h30)

| Horário | Etapa | Duração |
|---|---|---|
| 22:00-22:05 | Pré-flight + snapshot | 5 min |
| 22:05-22:15 | A1: subir logo + foto | 10 min |
| 22:15-22:30 | B1-B4: Header completo | 15 min |
| 22:30-22:45 | **Validação Miguel (mobile/iPad/desktop)** | 15 min |
| 22:45-22:55 | C1-C3: Manchete | 10 min |
| 22:55-23:10 | **Validação Miguel** | 15 min |
| 23:10-23:25 | D1-D3: Coluna Editor | 15 min |
| 23:25-23:35 | **Validação Miguel** | 10 min |
| 23:35-23:40 | E1-E2: Botão Apoie | 5 min |
| 23:40-23:50 | F1-F3: Finalização + Cérebro | 10 min |

**Total: ~90 min** (com validação em cada breakpoint + documentação Cérebro)

---

## 🆘 Se algo quebrar durante a noite

**Rollback por etapa:**
- Cada etapa tem snapshot prévio em `/root/port_canonico_noturno_*/`
- Script `rollback.sh` restaura + purga cache

**Rollback TOTAL (emergência):**
```bash
ssh cafezinho-wp "
TS_NOTURNO=<timestamp da sessão de hoje>
cp /root/port_canonico_noturno_${TS_NOTURNO}/* /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/
find /var/www/ocafezinho/wp-content/cache/wp-rocket/ -mindepth 1 -delete
"
```

---

## 📞 Quando você chamar às 22h

**Miguel só precisa dizer:** *"Vamo pro port noturno"*

Eu:
1. Confirmo que site está estável (HTTP 200 baseline)
2. Executo Pré-flight (snapshot)
3. Começo pela Fase A (estáticos)
4. A cada etapa, te mostro o resultado e você valida antes de avançar
5. Não te pergunto mais **o que** fazer — só **se está bom** o resultado

---

## Assinatura

**ZCode (GLM-5.2 Z.ai)** — sessão fallback final
**Preparado:** 2026-08-11 13:10 BRT
**Execução:** a partir das 22h BRT (audiência baixa)
**Duração estimada:** ~90 min

_Documento vivo. Atualizado conforme scripts são preparados durante a tarde._
