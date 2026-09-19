# Memória Técnica — Port Canônico Fase 1 (Header) — ROLLBACK APLICADO

**Data:** 2026-08-11, 12:50 BRT (rollback definitivo)
**Autor:** ZCode (GLM-5.2 Z.ai)
**Missão pai:** Sprint Visual Cafezinho → port espelho→canônico
**Fórum-irmão:** `Foruns/forum_plano_port_canonico_20260811.md`
**Status:** ⏸️ PAUSADO pelo Miguel — site canônico em ROLLBACK COMPLETO ao estado pré-port (estável)

---

## 1. O que aconteceu (resumo executivo)

Miguel decidiu iniciar o port da reforma visual do espelho (`cafezinho.news`) pro canônico (`ocafezinho.com` — produção). Escolheu começar pela **Fase 1: Header** (cabeçalho). Após ~15 iterações no header (logo v6, hamburger sempre visível, offcanvas expandido com Buscar+Apoie+gtranslate+submenus), o resultado era **bom no mobile e iPad**, mas Miguel reportou **2 problemas no final**:

1. **Bug do dropdown/submenu do offcanvas**: Editorias não abria submenus (Política, Economia, etc). Foi corrigido trocando `wp_nav_menu depth 1→2` + adicionando walker Bootstrap.
2. **Anúncios da parte de baixo do site "colados na esquerda"** no iPad e mobile. Miguel perguntou se eu mexi.

Sobre o item 2: **investigação honesta mostra que NÃO toquei em CSS global**. Meu diff do style.css (original 705 linhas vs atual) só ADICIONOU regras no final (linhas 706+) usando seletores específicos do header (`.header-bar-minimal`, `.header-logo`, `.header-hamburger-link`, `.offcanvas-menu`, etc). Nenhuma regra minha afeta `body`, `footer`, `.container-xxl`, `.ad-space`, ou `#banner-*`.

Miguel decidiu: "prefiro fazer a noite, com o site com menos audiência". **ROLLBACK COMPLETO foi aplicado** pra ele ter site 100% estável durante a tarde.

---

## 2. Decisão: ROLLBACK COMPLETO

**Por que rollback completo:**
- Miguel quer pausar até a noite
- Reportou problema nos anúncios (origem incerta — pode ser meu, pré-existente, ou cache CDN)
- Site está em PRODUÇÃO com milhares de leitores
- Melhor ter site 100% original e estável do que com mudanças não-validadas

**Como:**
- Restaurei `header.php`, `footer.php`, `style.css` do snapshot PRÉ-Fase 0 (11:17 BRT): `/root/port_canonico_backup_20260811_111704/snapshot_arquivos_alvo/`
- Removi `logo-cafezinho-2026-v6.png` (preservada `logo-ocafezinho-outline.png` original)
- Purguei cache WP Rocket
- **SHAs confirmam integridade total** (header.php atual = `0aba7d76...` = original)

**Validação pós-rollback:**
- ✅ PHP lint verde
- ✅ HTTP 200 em home/single/categoria/AMP
- ✅ Logo original de volta no HTML renderizado

---

## 3. Estado que deixo pronto (não se perdeu nada)

### Backup completo do tema (intacto)
`/root/port_canonico_backup_20260811_111704/`
- `tema_ocafezinho_portal_pre_port_20260811_111704.tar.gz` (1.7 MB, SHA `6a12b421...`)
- `snapshot_arquivos_alvo/` — 8 PHP/CSS + 24 imgs da pasta img/
- `http_baseline.log`

### Rollbacks por sub-etapa da Fase 1 (10 snapshots, todos intactos)
Em `/root/port_canonico_fase1_*/`:
- `port_canonico_fase1_header` — primeira edição (logo v6 + header-bar)
- `port_canonico_fase1_right_group` — wrapper menu+gtranslate+search
- `port_canonico_fase1_minimal` — tudo do header some, fica só logo+hamburger
- `port_canonico_fase1_hamburger_fix` — tirar d-lg-none do `<img>` hamburger
- `port_canonico_fase1_linha_logo` — restaurar border-bottom + overflow hidden
- `port_canonico_fase1_espaco_header` — min-height 140px + flex-wrap nowrap
- `port_canonico_fase1_ipad` — logo 60px iPad específico
- `port_canonico_fase1_mobile_hamburger` — respiro mobile
- `port_canonico_fase1_header_definitivo` — 3 breakpoints limpos
- `port_canonico_fase1_ajuste_desktop` — menu+gtranslate+search à direita
- `port_canonico_fase1_dropdown_offcanvas` — depth 2 + walker Bootstrap
- `port_canonico_fase1_tamanho_single` — position static logo + tamanhos
- `port_canonico_fase1_rewrite_header` — header.php rewrite minimalista

### Logo v6 (não perdida)
- Ainda existe em `/tmp/adiag_work/logos/logo-cafezinho-2026-v6.png` (local) — pode ser re-subida quando retomar
- Também já está no espelho `cafezinho.news` em uso

### Aprendizados da Fase 1 (pra próxima sessão)

1. **Header do tema é flex + position absolute**: a logo original tem `position: absolute; top: 4px` no desktop, o que causa sobreposição com o conteúdo abaixo (single post). Necessário `position: static !important` em qualquer redesign.

2. **wp_nav_menu do offcanvas estava com `depth=1`**: submenus não apareciam. Solução: `depth=2` + `'walker' => new bootstrap_5_wp_nav_menu_walker()`.

3. **Hamburger com `d-md-none` no `<a>` E `d-lg-none` na `<img>`**: o `<a>` some ≥768px, mas o `<img>` interno também some ≥992px. Pra hamburger sempre visível, remover AMBOS.

4. **`align-items: baseline` NÃO funciona** quando os elementos têm alturas muito diferentes (img 25px vs img 50px vs svg 24px). Usar `align-items: flex-end` + `padding-bottom` fino.

5. **`justify-content: space-between`** é mais robusto que tentar inverter ordem via CSS `order`. Logo primeiro no HTML, hamburger segundo — naturalmente ficam em lados opostos.

6. **`flex-wrap: nowrap !important`** é essencial pra hamburger não quebrar de linha em telas pequenas.

7. **CDN (serverdoin) pode ter cache próprio** além do WP Rocket. Pra mudanças aparecerem rápido, pode ser preciso purgar os dois. (A confirmar — pode ter sido esse o problema dos anúncios.)

8. **Logo v6 (1550×280, proporção 5.54:1)** é a "definitiva" aprovada no espelho. Mas no canônico, sua largura grande (554px no desktop) demanda header-bar com `min-height: 140px` pra não sobrepor banner top.

9. **Miguel prefere estrutura minimalista** (só logo + hamburger no header, tudo no offcanvas). Reduz complexidade de alinhamento e mantém consistência mobile/iPad/desktop.

10. **Investigação problema anúncios**: não encontrei regra minha que afete globalmente. Pode ser (a) pré-existente e Miguel só notou agora, (b) cache CDN, ou (c) algum efeito colateral que não identifiquei. **À noite, investigar com calma**: comparar screenshot pré-port vs pós-rollback nos anúncios da parte debaixo.

---

## 4. Próxima sessão (à noite) — checklist

### Antes de retomar
- [ ] Confirmar com Miguel que site está visualmente estável (problema dos anúncios sumiu?)
- [ ] Se problema persistir pós-rollback: é pré-existente, não meu
- [ ] Se problema sumiu pós-rollback: eu causei em algum lugar que não encontrei — investigar diff mais a fundo

### Quando retomar a Fase 1
- [ ] Re-aplicar mudanças uma por UMA (não todas de vez), validar a cada
- [ ] Sequência sugerida:
  1. Subir só a logo v6 (item A1 isolado)
  2. Testar 30 min com audiência real
  3. Se OK, aplicar reorganização header (header-bar-minimal)
  4. Testar mais 30 min
  5. Aplicar offcanvas expandido (Buscar + Apoie + gtranslate + submenus)
  6. Validar mobile/iPad/desktop antes de declarar Fase 1 completa
- [ ] Em CADA passo: backup + rollback + PHP lint + HTTP check + validar visualmente

### Pergunta em aberto
- O problema dos anúncios "colados na esquerda" era meu? Tem que investigar com printscreen antes/depois do rollback.

---

## 5. Referências

- **Snapshot original:** `/root/port_canonico_backup_20260811_111704/` (canônico)
- **Fórum do plano:** `Cerebro/Foruns/forum_plano_port_canonico_20260811.md`
- **Esta memória:** `Cerebro/Memorias/memoria_port_canonico_fase1_20260811.md`
- **Índice de aprendizado canônico:** `Cerebro/Memorias/INDICE_APRENDIZADO_CANONICO_OCAFEZINHO.md`
- **Bugs do lab visual (espelho):** `Cerebro/monitoramento_horario/lab_visual_bugs/bugs_2026-08-11.jsonl`

---

## Assinatura

**ZCode (GLM-5.2 Z.ai)** — sessão fallback final
Timestamp: 2026-08-11 12:50 BRT

_Pausa solicitada pelo Miguel. Site em produção estável. Tudo documentado, nada perdido. Retomada à noite com menos audiência._
