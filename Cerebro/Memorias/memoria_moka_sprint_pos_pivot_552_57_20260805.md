# MEMÓRIA — Moka sprint pós-pivô 5.5.2 → 5.7 (sessão ZCode Kimi K3, 05/08/2026 ~18h→22h30 BRT)

> **Tema Duplo:** Fórum par = `Cerebro/Foruns/forum_moka_sprint_pos_pivot_552_57_20260805.md`
> **Sessão:** ZCode (Kimi K3), conversa Moka contínua (continuação direta da sessão que fez 5.5.1)
> **Repo:** `Outros/Aplicativos/Moka/Moka-Lab` (github.com/migueldorosario1/moka, branch main → Vercel auto-deploy ~2 min)

## O que foi entregue (6 commits, todos em produção)

### 1. Moka 5.5.2 — `b69a3a8` (18:11) — login modal virava FAIXA CORTADA ("probleminha meio grave")
- **Relato:** Miguel (print): clicar em Entrar abria uma faixa fina no topo, só título+✕, página sem escurecer.
- **Causa:** `position:fixed` do AuthModal inline quebrado por ancestral com containing block (transform/filter/contain) — overlay cobria só uma tira.
- **Cura:** `createPortal(document.body)` + guarda `mounted` (SSR) + centrado à prova de corte (`align-items:flex-start` + `margin:6vh auto`; NUNCA `margin:auto` com overflow-y — bug clássico do topo clipado).
- **Bug registrado:** `BUG-20260805-MOKA-LOGIN-MODAL-FAIXA-CORTADA` (CEREBRO_NODE_BUGS_RESOLVIDOS). Padrão-irmão do BUG-20260801-MOKA-MENU-SUPERIOR-SOME: **modal/overlay full-screen nunca inline na árvore**.

### 2. Moka 5.5.3 — `136eca8` (18:18) — "Configurações avançadas" → "Configurações" ×12
- Pedido direto: "não bota configurações avançadas, bota configurações só".
- `nav_advanced` renomeado nos 12 idiomas; quicknav perdeu 2 links MORTOS (#ajuda/#quem-somos — as seções saíram na 5.5.1, os atalhos ficaram). Ajuda = banner "❓ Tutorial completo" → /ajuda; Quem somos = rodapé global.

### 3. Moka 5.6 — `48bcd60` (18:32) — marketing GRATUITO sem "nesta fase" + tutorial "O que é API?"
- Pedido: "tira essa coisa de esta fase — bota: o Moka é grátis, é gratuito, você só tem que colocar a sua API. E tem que ter um bom tutorial sobre o que é API."
- `free_title` ×12: "Moka é gratuito ☕" (era "...nesta fase"). Varredura: zero "fase/phase/étape/этап/阶段/段階/단계/مرحلة/चरण" user-facing (restou só comentário interno — a memória do pivô fica no Cérebro, não no marketing).
- **/tutorial** abre com cartão novo **"🔑 O que é essa tal de API?"** ×12 (`tut_api_t`/`tut_api_d`): API = ponte entre o Moka e a IA que VOCÊ escolhe; chave = senha criada de graça no provedor; quem cobra é o provedor (centavos); o Moka é gratuito.
- /ajuda FAQ: 4 respostas reescritas sem "fase".
- **Incidente evitado:** quase subi sílaba coreana errada (물 em vez de 무 — U+BB3E×U+BB34) — conferência codepoint-a-codepoint antes do push. Lição: em string i18n não-latina, verificar por `unicodedata`, nunca no olho.

### 4. Moka 5.6.1 — `803007b` (19:25) — botão Entrar em TODAS as páginas
- Pedido: "na Moka Livros não tem o botão de entrar, mesma coisa na Moka Vídeo — tem que estar em tudo".
- `AuthGate` (Google + e-mail) adicionado ao topo de: /estante, /video, /biblioteca, /ajuda, /tutorial, /sobre — sempre antes da bandeirinha de idiomas (posição da capa). Já existia em: capa (page.tsx) e Reader.

### 5. Moka 5.7 — `ba918da` (22:30) — Entrar neutro + página "✅ E-mail confirmado"
- Miguel TESTOU o cadastro (tvcafezinho@gmail.com) e reportou 2 bugs:
  - **(a)** botão do topo tinha logo do Google → "a pessoa pode entrar com e-mail normal; bota só Entrar; o Google fica DENTRO da janela". Cura: `AuthButton` deslogado perdeu o SVG do Google (o G continua na AuthModal).
  - **(b)** clicar "Confirmar acesso" no e-mail caía numa "página estranha com interrogação" → era a HOME recebendo sem aviso. Cura: `signUpWithPassword` manda `emailRedirectTo: callback?next=/auth/confirmado`; nova página `/auth/confirmado` ×12 ("✅ E-mail confirmado! Sua conta está ativa — a biblioteca fica guardada na nuvem" + botão "Entrar no Moka →"; chega LOGADA); callback detecta falha do `exchangeCodeForSession` e manda `?erro=1` com explicação amiga.
- Chaves i18n novas: `auth_confirmed_title/sub/cta/error` ×12 (inseridas antes de `auth_reset_sent`).

## Respostas dadas ao Miguel (fatos verificados no código)
- **Login Google grava a biblioteca? SIM.** EPUB sobe completo (texto parseado incluso — abre em outro aparelho sem o arquivo); PDF sobe metadados/progresso/notas/traduções (reanexa o arquivo no aparelho novo); videoteca é local-only. Cadastro Google OU e-mail caem em auth.users = base da newsletter.

## ⚠️ ADENDO 07/08 ~13h BRT (descoberto na consolidação — o ecossistema andou enquanto esta conversa dormia)

- **SMTP info@mokareader.com = ✅ RESOLVIDO 06/08 ~14:35 BRT** pela sessão Kimi K3 "Ceará/Banco" (outra conversa): Miguel entregou a senha no chat → cofre `.env.unificado` (`SMTP_MOKA_USER/HOST=smtpout.secureserver.net/PORT=465/PASSWORD`, backup `…bak_pre_smtp_moka_20260806`); login testado :465 SSL e :587 TLS ✅ (`smtp.office365.com` ❌ — não é M365); e-mail real enviado ao Gmail do Miguel ✅. ⚠️ A senha trafegou no chat → recomendado **trocar no GoDaddy** por precaução. Detalhes: CEREBRO_NODE_ATUALIZACOES 06/08 ~14:35. **Resta saber:** se os envs do Supabase Dashboard foram ligados (verificar remetente real dos e-mails de auth — pendência levada pela sessão de lojas).
- **Sessão irmã ativa 07/08 ~12:00:** "Moka Reader: estágio + deploy nas lojas" — preparando TWA/Play Store + iOS (retomou a Fase 3!). Sem conflito de arquivos com esta consolidação (só Cérebro). Pendências que ela carrega: `assetlinks.json`, screenshots, contas das lojas (US$25 Google + US$99/ano Apple — pagamento Miguel), ~~PIX_KEY~~ (✅ resolvido por ESTA sessão na 5.7.1 `a85007d`), FOUC styled-jsx.
- **Monitor renovado:** ciclo 1 arquivado em `MONITORAMENTO_DE_TRABALHO_2026_08_07_1128.md` (nossa linha de sessão preservada lá, com o SMTP riscado como resolvido); ciclo 2 vivo.
- **Moka 5.5 (`68063f5`) autoria confirmada:** sessão FdI/Moka Writer (sess_c766156b) — e ela já fez rebase SOBRE nosso 5.7 (`5dd26b2` topbar Quem somos).

## ⚠️ ADENDO 07/08 ~12h — Moka 5.7.1 (`a85007d`): chave Pix definida

- Miguel respondeu à pendência do Pix: chave nova = **info@mokareader.com** (substitui `migueldorosario2@gmail.com` que estava hardcoded no SettingsForm desde a sessão anterior).
- Implementado em 4 arquivos: `lib/donate.ts` (PIX_KEY + PIX_HOLDER), `components/SettingsForm.tsx` (importa as constantes — fim do hardcoded), `components/SiteFooter.tsx` (botão agora com alerta de cópia; antes copiava em silêncio), `app/ajuda/page.tsx` (FAQ sem "Pix em breve").
- Repo tinha andado: `git pull` trouxe `5dd26b2` (sessão FdI/Moka Writer — "Quem somos" na topbar da capa) SOBRE o nosso 5.7; fast-forward limpo, zero conflito com os 4 arquivos do Pix.
- Versão: 5.7 → **5.7.1**. Deploy Vercel ~2 min; botão 🟢 PIX visível na home ao vivo.

## PENDÊNCIAS aguardando Miguel (na ordem de prioridade)
1. ~~SMTP info@mokareader.com~~ → **RESOLVIDO 06/08** (ver ADENDO acima). Resta apenas confirmar se o Supabase Dashboard está usando o SMTP custom nos e-mails de auth (teste de cadastro real).
2. ~~**Chave Pix da doação**~~ → **RESOLVIDO 07/08 ~12h (`a85007d`, Moka 5.7.1).** Miguel: "não, eu mudei o pix para info@mokareader.com". Cura: `PIX_KEY = "info@mokareader.com"` + `PIX_HOLDER = "Miguel Gomes Barbosa do Rosário"` em `lib/donate.ts` (fonte única); SettingsForm parou de hardcodar (importa do donate); rodapé global agora MOSTRA o botão 🟢 PIX (antes escondido) com alerta de confirmação de cópia; /ajuda sem "Pix em breve". Build limpo + verificado AO VIVO (botão presente na home, HTTP 200). A linha "Banco: Nubank" saiu do alerta (banco da chave nova não confirmado — Miguel não citou; se ele disser, re-adiciona).
3. **Re-teste do modal de login** no desktop — tentativa GUI em 07/08 ~12h30 (browser-use/IAB): botão Entrar renderiza neutro ✅, handler React onClick anexado ✅ (fibra+props inspecionados), mas NENHUM caminho de clique abre o modal (locator, coordenada CUA, nó DOM, Enter) — e o teste de controle provou que o defeito é do ambiente: clique locator falha até em example.com. Conclusão: automação de clique indisponível nesta sessão; fix estrutural mantido; prova final = clique físico do Miguel. SMTP: tentativa de disparar /auth/v1/recover via API parou na extração da anon key do bundle (não está nos 17 chunks iniciais da home) — Miguel encerrou ("terminado"); segue valendo o caminho simples: cadastro/reset real e olhar o remetente, ou colar SMTP_MOKA_* no Supabase Dashboard.

## PENDÊNCIAS técnicas (não urgentes)
- Fase 2: reintroduzir premium gradualmente (backup/tag `pre-pivot-pago-v4.3` preservados) quando o gratuito estiver sólido ("pouca reclamação").
- Fase 3: TWA/Bubblewrap AAB pra Play Store (DUNS 943494728 já no Cofre) — pausado pelo Miguel.
- systemd pro uvicorn na Tencent (hoje nohup — não sobrevive reboot).
- styled-jsx restante → globals.css (mesma classe de FOUC da biblioteca: estante/video/sobre/ajuda/settings).
- X/Twitter & Instagram video (motorzinho yt-dlp→S3→Transkriptor).
- Moka-Producao snapshot sync (stale).
- LGPD: linha de consentimento pra newsletter (em /privacidade ou 1º login).

## Verificação de cobertura Cérebro (esta sessão)
- Bugs: `BUG-20260805-MOKA-LOGIN-MODAL-FAIXA-CORTADA` ✅ no nodo de resolvidos.
- INDEX_MOKA: entradas (9)(10)(11)(12)(13) de 05/08 ✅.
- MONITORAMENTO_DE_TRABALHO: linha da sessão atualizada a cada entrega ✅.
- Sprint: bloco Moka no CEREBRO_NODE_SPRINTS_ATIVOS ✅ (esta consolidação).
- Despertar: INDICE_DESPERTAR_LEVE aponta pra cá ✅ (esta consolidação).
