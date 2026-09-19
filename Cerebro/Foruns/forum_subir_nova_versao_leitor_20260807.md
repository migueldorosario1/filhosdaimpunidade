# ⬆️ FÓRUM — SUBIR NOVA VERSÃO NO LEITOR (Filhos da Impunidade)

**Data:** 2026-08-07 · **Agente:** ZCode/Kimi K3 · **Commit:** `0ce3556` (AO VIVO em filhosdaimpunidade.vercel.app — HTTP 200, feature servida)
**Pedido do Miguel (07/08, por voz):** "sabe o que falta aqui no Filhos da Impunidade? Aqui na capa mesmo, um link, um botão para subir uma versão nova. A gente já tem como apagar as versões prontas, a gente tem como editar as versões prontas, mas a gente não tem como subir uma versão inteiramente nova de um capítulo que a gente está usando. Tem que criar essa liberdade aqui: subir uma versão inteiramente nova — continua com o mesmo nome, o capítulo continua no mesmo capítulo, só que uma versão nova."

## Decisões resumidas

1. **Onde fica:** botão **"⬆️ Subir Nova Versão"** na barra de versões do leitor (a "capa" — subheader `#leitor`, ao lado do dropdown 📜 Histórico de Versões e do botão 👑 Tornar Canônica) **+** mini-botão **"⬆️ Subir"** dentro do próprio menu de versões, ao lado do 🧹 Faxina — as duas portas de entrada levam ao mesmo modal.
2. **O que faz:** abre o modal `modal-upload-version` que aceita **arquivo do computador (.md/.txt/.pdf)** — texto lido na hora (PDF via pdf.js, já usado na Central de Fontes; até 200 págs / 400 mil chars) — **ou colar o texto** direto num textarea (contador de caracteres ao vivo). Rótulo opcional (ex.: "Sônia") entra no tag.
3. **Regra de ouro do pedido:** a versão enviada vira uma **revisão R# nova do MESMO capítulo** (`nextRevisionKey` = máximo+1, anti-colisão mesmo após faxina) — o nome do capítulo não muda, **nenhuma versão existente é tocada** e a **canônica 👑 NÃO muda** (verdade editorial preservada; se quiser, o editor torna canônica com o botão que já existe). Tag automática: `R# (upload)` ou `R# (upload: rótulo)`.
4. **Pós-gravação:** a versão nova vira a **ativa** na hora (leitor, métricas, URL `&ver=R#`, título do Estúdio atualizam juntos) e aparece no histórico/dropdown, no Duelo Lado a Lado e no compilado como qualquer outra revisão.
5. **Proteções:** texto vazio não grava; `full_book`/roteiro bloqueados; quota de armazenamento via `safeLocalSet` + `storageFullHelpMessage` (nada se perde em silêncio); teto de 400 mil chars com aviso de truncamento.
6. **Testes:** suíte Node DOM-stub nova (`scratch/teste_upload_versao.js`) — **14/14 OK** (abrir modal/anunciar próximo R#, gravar colado→R3, rótulo no tag, vazio não grava, full_book bloqueado, anti-colisão R4 após apagar R2, canônica inalterada, quota não grava, contador, rótulo no histórico, 4 checagens de fiação HTML). Regressão: suíte Central de Fontes 23/23 OK.

## Pendências / próximos passos

- [ ] Miguel testar ao vivo: subir 1 versão real (ex.: PDF ou .md de uma revisão nova) num capítulo e conferir o R# novo no histórico.
- [ ] Se quiser que a versão subida já vire canônica automaticamente, é 1 clique a mais no código — hoje fica de propósito como decisão editorial separada.

**Memória técnica:** `Memorias/memoria_subir_nova_versao_leitor_20260807.md`
