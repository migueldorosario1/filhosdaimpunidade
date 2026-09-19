# Memória — Manual de Estilo: página própria + Estúdio + Download íntegra

**Data:** 2026-08-08
**Sessão:** ZCode (GLM-5.2) — conversa "FdI: página própria do Manual"
**Repo:** `/home/migueldorosario/ZCodeProject/filhosdaimpunidade`
**Arquivo modificado:** `index.html` (único; +312/-68 linhas)
**Commit:** `c4bd69d` — HEAD==origin ✅ — deploy Vercel HTTP 200 ✅
**Fórum gêmeo:** `Foruns/forum_manual_pagina_propria_estudio_download_20260808.md`

---

## 1. Contexto técnico

O `index.html` é um SPA (aplicação de página única, ~7700 linhas) com roteamento por hash (`#leitor`, `#estudio`). Antes desta missão, o Manual de Estilo era o **modal** `modal-manual` (linhas ~970-1047): uma janela pop-up aberta por `openManualModal()`. O conteúdo canônico vivia na string JS `manualEstiloMarkdown` (linha ~2017, 34 regras em Markdown) e as regras customizadas (#35+) no `localStorage` chave `miguel_manual_de_estilo_custom_rules`.

---

## 2. O que foi feito (3 partes)

### PARTE 1 — Página própria do Manual (`page-manual-estilo`)
- **Substituiu** o modal `modal-manual` por `<div id="page-manual-estilo" class="fixed inset-0 z-[9998] ...">` (tela cheia, padrão do Estúdio Editorial `modal-ai-audit`).
- **Header sticky** com título + badge de edição ativa (`manual-override-badge`) + 3 botões: `📥 Baixar Íntegra` / `🎬 Estúdio do Manual` / `Voltar`.
- **Migrou TODO o conteúdo interno** do modal antigo (IDs preservados: `manual-estilo-content`, `manual-custom-rules-container`, `manual-custom-rules-list`, `manual-proposal-input`, `manual-proposal-confirm`, `manual-proposal-processed`, `manual-proposal-next-number`, `btn-voice-manual`, `voice-manual-btn-text`).
- **Funções:** `openManualPage()` / `closeManualPage()` — toggle `.hidden` em `app-header`/`app-subheader`/`app-main` + `window.scrollTo(0,0)` + `refreshManualOverrideBadge()` + `renderCanonicalManual()` + `renderCustomManualRules()` + `lucide.createIcons()`.
- **Aliases:** `openManualModal()`/`closeManualModal()` viram wrappers → não quebra botões antigos.

### PARTE 2 — Download da íntegra (`downloadManualIntegra`)
- Blob `.md` do **texto ativo** (`getActiveManualMarkdown()`).
- Nome: `Manual_de_Estilo_Filhos_da_Impunidade_<YYYY_MM_DD>[_editado].md` (sufixo `_editado` se houver override).
- Padrão `downloadFullBook()`, com `URL.revokeObjectURL(url)` após click (correção de vazamento que o original tem).

### PARTE 3 — Estúdio do Manual (`page-manual-estudio`)
- `<div id="page-manual-estudio" class="fixed inset-0 z-[9999] ...">` — editor full-screen.
- **Layout:** textarea editável (`manual-estudio-textarea`, `oninput` → `refreshManualEstudioPreview()`) + preview (`manual-estudio-preview`, renderizado por `marked.parse`).
- **Override no localStorage** chave `miguel_manual_de_estilo_override` (const `MANUAL_OVERRIDE_KEY`).
- **Botões:** `💾 Salvar Edição` / `↩️ Restaurar Original` (2 toques, padrão do app) / `📥 Baixar` / `Voltar ao Manual`.
- **Banner âmbar** (`manual-estudio-banner`) quando há override ativo.
- **Funções:** `openManualEstudio` / `closeManualEstudio` (re-renderiza página ao fechar) / `refreshManualEstudioPreview` / `refreshManualEstudioBanner` / `saveManualEstudioEdit` / `restoreManualEstudioOriginal` (dataset.confirming para 2 toques).

### Integração unificadora
- `getCanonicalManualWithCustom()` → `manualEstiloMarkdown` + regras custom (#35+) formatadas como bloco Markdown.
- `getActiveManualMarkdown()` → override (se existir) senão canônico+custom. **Esta é a fonte única de verdade** para página, estúdio e download.
- `hasManualOverride()` + `refreshManualOverrideBadge()` → mostram o badge âmbar na página.
- `renderCanonicalManual()` atualizado para chamar `getActiveManualMarkdown()` em vez de `manualEstiloMarkdown` direto.

---

## 3. Arquivos e linhas (referência pós-commit)

- **HTML página do manual:** `page-manual-estilo` (~linha 972-1058).
- **HTML estúdio do manual:** `page-manual-estudio` (~linha 1060-1130).
- **Funções JS manual/estúdio/download/override:** após `renderCanonicalManual` (~linha 2108-2230) e wrappers `openManualPage`/`closeManualPage` (~linha 4524-4555).
- **Botão da toolbar:** linha ~359 (mantém `onclick="openManualModal()"` que agora é alias de `openManualPage`).

---

## 4. Comandos de teste (todos passaram)

```bash
cd /home/migueldorosario/ZCodeProject/filhosdaimpunidade
node scratch/teste_api_drive.js          # 13/13 ✅
node scratch/teste_drive_sync.js         # 9/9 ✅
node scratch/teste_roteiro_livro_edit.js # 24/24 ✅
node scratch/teste_upload_versao.js      # 14/14 ✅
node scratch/teste_renomear_versao.js    # 12/12 ✅
node scratch/teste_central_fontes.js     # ok ✅
```

Checks de integridade:
- 8 funções novas presentes (grep -c = 8).
- 6 IDs HTML novos presentes (1 cada).
- 0 referências órfãs a `modal-manual` (antigo removido sem resíduo).

---

## 5. Deploy

- `git pull --rebase origin main` (sem conflito — só 2 commits de sync automático de custom_rules/revisions que outra sessão/app subiu).
- `git push origin main` → `4a0ba27..c4bd69d`.
- HEAD==origin ✅ (commit-guard).
- Vercel HTTP 200 em `/` e `/index.html`.
- Novas funções presentes no HTML ao vivo (curl confirmou: `page-manual-estilo`, `page-manual-estudio`, `downloadManualIntegra`, `openManualEstudio`).

---

## 6. O que não foi feito / limitações

- **Verificação visual no navegador não executada:** Browser Use exige desktop/shared-host session (indisponível nesta CLI). Integridade validada por 73 testes automatizados + checks estruturais. Recomendação: Miguel abrir o site e clicar.
- **Sincronização Drive/GitHub do override:** não implementada (override é local, como o Roteiro). Se o Miguel quiser sync do estúdio, é tarefa separada.
- **Conteúdo das regras canônicas:** não foi alterado — só a "casa" visual e a editabilidade.

---

## 7. Reversão (se necessário)

O commit `c4bd69d` é isolado (1 arquivo, +312/-68). Para reverter:
```bash
cd /home/migueldorosario/ZCodeProject/filhosdaimpunidade
git revert c4bd69d
```
O modal antigo volta exatamente como estava.
