# FÓRUM — Moka sprint pós-pivô 5.5.2 → 5.7 (05/08/2026)

> **Tema Duplo:** Memória técnica completa = `Cerebro/Memorias/memoria_moka_sprint_pos_pivot_552_57_20260805.md`
> **Participantes:** Miguel do Rosário (product owner, testador real) + ZCode Kimi K3 (execução)
> **Resultado:** 6 commits em produção (`b69a3a8`→`ba918da`), Moka 5.5.2 → 5.7

## Decisões tomadas (todas do Miguel, executadas no dia)

1. **Modal/overlay full-screen: sempre portal pro `<body>`** — o login virou faixa cortada por causa de ancestral com containing block. Padrão permanente: nada de overlay inline na árvore (irmão do fix do menu superior).
2. **Marketing = "gratuito", ponto.** Nada de "nesta fase" em lugar nenhum (12 idiomas). A versão paga existe só na memória do Cérebro (tag `pre-pivot-pago-v4.3`) — não no site.
3. **O tutorial do usuário começa explicando O QUE É API** — antes de qualquer passo. Linguagem de gente: API = ponte; chave = senha gratuita no provedor; quem cobra é o provedor; o Moka é gratuito.
4. **Botão do topo = "Entrar" neutro.** Sem logo do Google (entra por e-mail também). O Google aparece DENTRO da janela de login.
5. **"Entrar" em TODAS as páginas** (estante, video, biblioteca, ajuda, tutorial, sobre — além de capa e Reader).
6. **Confirmação de e-mail merece página própria** — `/auth/confirmado` ("✅ E-mail confirmado! …Entrar no Moka →"), nunca cair na home sem aviso. Link expirado = explicação amiga.

## Fatos confirmados ao Miguel
- **Google login grava SIM a biblioteca** (EPUB completo; PDF metadados; videoteca local). Google OU e-mail alimentam a newsletter (auth.users).

## Aguardando Miguel (bloqueadores) — atualizado 07/08
1. ~~**Senha do e-mail info@mokareader.com (GoDaddy)**~~ → **RESOLVIDO 06/08 ~14:35** pela sessão "Ceará/Banco" (senha no cofre `SMTP_MOKA_*`, login testado :465 SSL, e-mail real enviado ✅). Resta: confirmar que o Supabase Dashboard usa o SMTP custom nos e-mails de auth. **↳ TESTE DISPARADO 07/08 ~12h50** (POST /auth/v1/recover p/ tvcafezinho@gmail.com via chave publishable pública do bundle, HTTP 200): aguarda Miguel olhar a caixa do tvcafezinho e dizer o REMETENTE — info@mokareader.com = dashboard já usa SMTP ✅; noreply@mail.app.supabase.io = falta colar SMTP_MOKA_* no Dashboard. ⚠️ Senha passou pelo chat → trocar no GoDaddy por precaução.
2. ~~**Confirmar chave Pix**~~ → **RESOLVIDO 07/08 ~12h:** Miguel MUDOU a chave para **`info@mokareader.com`** (a antiga `migueldorosario2@gmail.com` NÃO vale mais). Unificada como fonte única em `lib/donate.ts` (`PIX_KEY` + `PIX_HOLDER`), usada no rodapé global E nas Configurações; alerta de cópia mostra chave + titular. Commit `a85007d` (Moka 5.7.1), no ar ✅. Nota: a chave é pública (é pra doação), não vai no Cofre.
3. **Re-testar o modal de login** no desktop. **SEGUE ABERTO p/ teste físico do Miguel.** Tentativa de teste GUI por automação em 07/08 ~12h30: BLOQUEADA — o navegador embutido da sessão não despacha cliques pra página (falhou até em example.com; só foco funciona). Verificação estrutural segue válida (portal no body + flex-start + margem 6vh = padrão anti-corte; Miguel clicou no fluxo de cadastro inteiro num navegador real em 05/08, pós-fix).
4. **Deploy nas lojas:** sessão irmã ativa 07/08 ~12:00 preparando TWA/Play + iOS — aguarda contas das lojas (US$25 + US$99/ano) e assets.

## Lições da sessão
- String i18n não-latina: verificar codepoints (quase subiu 물 por 무 no coreano).
- i18n: depois de REMOVER uma seção, varrer os ÂNCORAS/atalhos que apontavam pra ela (quicknav ficou com 2 links mortos na 5.5.1, descobertos na 5.5.3).
- Miguel testa de verdade e acha bug real: o teste dele com tvcafezinho@gmail.com gerou 2 fixes (botão Google + página de confirmação).
