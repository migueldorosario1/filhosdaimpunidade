# Fórum — Manual de Estilo: página própria + Estúdio + Download íntegra

**Data:** 2026-08-08
**Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan) — conversa "FdI: página própria do Manual"
**Repo:** `filhosdaimpunidade` (`index.html` apenas)
**Commit:** `c4bd69d` — HEAD==origin ✅, deploy Vercel 200 ✅ (verificado ao vivo)
**Origem:** Ordem do Miguel por voz (transcrição no fim deste fórum)

---

## O que aconteceu (resumo executivo)

O Miguel observou que o Manual de Estilo do site **Filhos da Impunidade** era só um modal (janela pop-up) e que "a gente tem que dar mais importância" a ele. Ele pediu 3 transformações, todas entregues e no ar:

1. **Página própria do Manual** (tela cheia, não janela) — ganha destaque visual.
2. **Botão baixar íntegra** do manual (`.md`) — antes não existia.
3. **Estúdio do Manual** dedicado — editor full-screen "para quem quiser consertar qualquer coisa".

Os botões de baixar e estúdio ficam **na própria página** do manual (header sticky), como o Miguel pediu.

---

## Decisões de implementação

### Padrões reusados (nada inventado)
- **Página full-screen** → mesmo padrão do "Estúdio Editorial" (`modal-ai-audit`): `<div>` tela cheia que esconde `app-header`/`app-subheader`/`app-main` e mostra seu próprio conteúdo. Funções `openManualPage`/`closeManualPage` no molde de `openAiAuditModal`/`closeAiAuditModal`.
- **Download** → mesmo padrão do `downloadFullBook()` (Blob `.md` + `<a>` temporário), com `URL.revokeObjectURL` adicionado (boa prática que o original não tinha).
- **Estúdio (override no localStorage)** → mesmo padrão do "Editar Roteiro"/"Editar Livro Inteiro": texto editável persiste no navegador, banner âmbar quando há edição ativa, "Restaurar Original" com confirmação de 2 toques.
- **Render** → `marked.js` (já carregado no projeto) para Markdown → HTML.

### Conceito-chave: "texto ativo"
Toda a integração entre os 3 recursos gira em torno do **texto ativo** do manual:
- `getActiveManualMarkdown()` → retorna o **override** (se existir no localStorage) ou o **canônico + custom** (regras #35+ concatenadas).
- A página do manual, o estúdio e o download **todos usam essa mesma função** → uma edição no estúdio reflete imediatamente na página e no download.

### Compatibilidade
- `openManualModal()`/`closeManualModal()` viraram **aliases** de `openManualPage()`/`closeManualPage()` → nenhum botão antigo quebra.
- Os IDs internos do modal antigo (`manual-estilo-content`, `manual-custom-rules-container`, `manual-custom-rules-list`, `manual-proposal-*`) foram **preservados** na nova página → todas as funções JS existentes (`saveManualProposal`, `confirmManualProposal`, `deleteCustomManualRule`, `toggleVoiceManualProposal`, etc.) continuam funcionando sem alteração.
- O modal antigo `modal-manual` foi **removido** (conteúdo migrado, 0 refs órfãs verificadas).

---

## Estado da missão

### ✅ Pronto e no ar
- Página própria full-screen do Manual (`page-manual-estilo`, z-[9998]).
- Estúdio do Manual (`page-manual-estudio`, z-[9999]) com editor + preview + override.
- Download da íntegra (`downloadManualIntegra`, Blob `.md`).
- Commit `c4bd69d` pushado, HEAD==origin, Vercel 200, novas funções presentes no HTML ao vivo.
- Testes de regressão: **todos passaram** (api_drive 13/13, drive_sync 9/9, roteiro_livro_edit 24/24, upload_versao 14/14, renomear_versao 12/12, central_fontes ok).

### ⚠️ Não testado
- Verificação visual no navegador (Browser Use indisponível nesta sessão CLI — exige desktop/shared-host). A integridade estrutural e funcional foi validada por 73 testes automatizados + checks de IDs/funções. Recomenda-se o Miguel abrir o site e clicar nos botões para confirmação visual.

### O que falta / próximos passos
- **Confirmação visual do Miguel** (abrir `filhosdaimpunidade.vercel.app`, clicar em "Manual de Estilo", ver a página tela cheia, testar Estúdio + Download).
- (Opcional, só se pedir) Sincronização Drive/GitHub do override do Estúdio do Manual (hoje é local, como o Roteiro).

### O que preciso de você (Miguel)
- Abrir o site e confirmar visualmente que a página própria, o estúdio e o download estão funcionando como esperado. Se algo não servir, é só dizer.

---

## Transcrição do pedido (origem)

> "e olha só no site filhos da impunidade a gente montou né ele tem a parte que tem do manual tem um botão lá manual estilo logo na home mas tá faltando um botão para baixar a íntegra do manual Entendeu? Baixar íntegra Está faltando um botão para baixar tudo Falta dois botões Um botão para criar um estúdio Só para o manual de estilo Para quem quiser consertar qualquer coisa Um estúdio só para o manual de estilo Não só acrescentar Um estúdio e um botão para baixar que pode ficar aí na página do Manau Tilo inclusive o Manau Tilo cria uma página própria para ele não é uma janela que abre não a gente tem que dar mais importância, abre uma página própria e aí você tem o botão de criar o estúdio entrar no estúdio do Manau Tilo tem o botão de baixar a íntegra do Manau Tilo faz isso, vai ficar ótimo Tchau."

---

## Detalhes técnicos (ver Memória gêmea)

Arquivo, linhas, funções, diff, comandos de teste → `Memorias/memoria_manual_pagina_propria_estudio_download_20260808.md`.
