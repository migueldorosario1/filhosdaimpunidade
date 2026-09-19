# 📧 Fórum — Cura do e-mail da Priscila (fenixfilmes.com sem MX)

**Aberto:** 2026-09-01 ~14:35 BRT · **Por:** ZCode/GLM-5.3 (Dell)
**Pedido do Miguel (01/09 ~14:2x, por voz):** "resolve esse problema do email da priscila, minha mulher… ela falou que eu que estou no controle do DNS… manda as perguntas pra mim por Telegram que eu repasso pra ela."

---

## 1. O problema

Priscila (`priscila@fenixfilmes.com`) "não está conseguindo entrar no Gmail". Suporte do Google (via WhatsApp, print em `Outros/Negocios Priscila/bug_gmail/`) diagnosticou: **registros MX ausentes** no domínio — sem MX, o domínio não recebe e-mail.

## 2. Diagnóstico (fechado, com prova) — 01/09 14:32 BRT

| Consulta | Resultado | Leitura |
|---|---|---|
| `dig MX fenixfilmes.com +short` | **VAZIO** | confirma o Google: zero MX |
| `dig NS fenixfilmes.com +short` | `justin.ns.cloudflare.com` / `katelyn.ns.cloudflare.com` | DNS controlado na **Cloudflare** (conta do Miguel — a Priscila tá certa) |
| `dig TXT fenixfilmes.com +short` | **VAZIO** | sem SPF → e-mail enviado por ela tende a cair em spam |
| `dig TXT google._domainkey…` | vazio | DKIM nunca ativado (2º passo, opcional) |
| `dig A fenixfilmes.com` | 104.21.9.143 / 172.67.160.134 (proxy Cloudflare) | site no ar, domínio saudável |
| RDAP Verisign | registrar **eNom**; `last changed 2026-08-30T23:41:06Z` | **30/08 20:41 BRT** = mudança no domínio |

**Causa raiz (hipótese forte, datada):** o domínio foi mexido na noite de **dom 30/08 ~20:41 BRT** (migração de DNS pra Cloudflare e/ou setup do site atrás do proxy). A migração **não copiou os registros MX/SPF** → e-mail parou de chegar. Prova de que funcionava antes: **28/08 17:28 a Priscila respondeu nosso follow-up** ("nao entendi" — registrado no `forum_alianca_fenix_cafezinho_palestina_20260825.md` §19): ela só pode responder e-mail que CHEGOU.

## 3. A correção (5 min, no painel Cloudflare — só o Miguel, não há token de DNS no cofre)

1. `dash.cloudflare.com` → domínio **fenixfilmes.com** → **DNS → Records → Add record**
2. **MX:** Type `MX` · Name `@` · Mail server `smtp.google.com` · Priority `1` · TTL `Auto` → Save
3. **SPF:** Add de novo · Type `TXT` · Name `@` · Content `v=spf1 include:_spf.google.com ~all` · TTL `Auto` → Save
4. Avisar o ZM → verificação por `dig` daqui + teste real (mandar e-mail e ela confirmar chegada).
5. (Depois, opcional mas recomendado) **DKIM**: `admin.google.com` → Apps → Gmail → Authenticate email → gerar chave → add TXT `google._domainkey` no Cloudflare. E revalidar MX no assistente do Workspace.

⚠️ Segurança da mudança: MX hoje é VAZIO (ninguém recebe nada no domínio), então **adicionar MX do Google não pode quebrar e-mail que exista** — mudança puramente aditiva. Se existir OUTRO provedor de e-mail no domínio (não existe sinal disso), validar antes.

## 4. Perguntas pra Priscila (enviadas ao Telegram do Miguel 01/09 ~14:33)

1. Ela **consegue entrar** com login/senha (vê a caixa) ou o **login é recusado**? (MX não bloqueia login — se for o login, é outro bug: senha/2FA/conta, e aí o MX é só metade do problema.)
2. De que dia é o **último e-mail que ela lembra de ter recebido**? (esperado: até ~30/08)
3. Ela consegue **enviar** e-mail? Chega pro destinatário (mesmo no spam)?
4. **Quem mexeu no site/domínio domingo 30/08 à noite** — ela, o Miguel ou webmaster? (pra fechar a causa raiz e evitar repeat)

## 5. Estado da missão

- **O que aconteceu:** diagnóstico completo fechado em ~10 min, causa datada (30/08 20:41 BRT), plano de correção + perguntas entregues ao Miguel por Telegram.
- **O que falta:** Miguel aplicar os 2 registros no Cloudflare (item 3); ZM verificar por `dig`; DKIM depois; Priscila responder as perguntas (especialmente a 1 — login × recebimento).
- **O que preciso do Miguel:** aplicar os 2 registros (ou criar token de API Cloudflare c/ permissão Zone→DNS→Edit e guardar no cofre que o ZM aplica sozinho da próxima) + trazer as respostas da Priscila.

## 6. 🔄 ADENDO 2 — Reviravolta (01/09 ~14:4x, resposta do Miguel)

**Miguel:** "não tem nenhum domínio fenixfilmes.com no meu Cloudflare" + "ela não está conseguindo ENVIAR nem RECEBER e-mails".

**Mapa corrigido:**
- O DNS **NÃO está na conta Cloudflare do Miguel** — está na conta de **quem publicou o site**. Prova da publicação: header `last-modified: Sun, 30 Aug 2026 23:37:22 GMT` (= 30/08 **20:37 BRT**, 4 min antes do `last changed` 20:41 BRT do registro). Site = **WordPress 7.0.4 + Elementor 3.30.3** em servidor **CyberPanel-OLS/LiteSpeed** (VPS) atrás do Cloudflare.
- Logo: **webmaster/agência que lançou o site na noite de 30/08 migrou o DNS pro Cloudflare da conta dele e não copiou MX/SPF.** A Priscila assumiu que o DNS era do Miguel ("o cara de tecnologia da família").
- **"Não envia NEM recebe"** = sintoma mais largo que MX sozinho: receber = MX (fechado); enviar com ERRO na tela + login estranho pode ser **Workspace suspenso por billing** — verificar `admin.google.com → Billing`. Pendente resposta: o que aparece exatamente ao tentar enviar + se ela loga.

**Caminhos:**
- **A (rápido):** webmaster add os 2 registros — mensagem pronta em `Outros/Negocios Priscila/bug_gmail/MENSAGEM_PRA_WEBMASTER.txt`.
- **B (contingência, webmaster sumiu):** Miguel add o domínio na CONTA Cloudflare dele (o CF importa os registros atuais do site), add MX+SPF, e trocar os NS no registrador (eNom — acesso provavelmente também com quem comprou o domínio em 2016). Eu preparo a lista completa de registros a clonar na hora.
- **C:** se erro de envio/login → checar billing do Workspace antes de culpar só o DNS.

**Perguntas novas enviadas ao Telegram do Miguel (14:45):** (1) quem fez/publicou o site; (2) o que acontece ao tentar enviar (erro na tela × envia e não chega); (3) ela consegue logar no gmail.com.

## 7. 🕵️ ADENDO 3 — Investigação dono/hospedagem (01/09 ~15:0x, pedido do Miguel)

**Pergunta:** quem é o dono do site e onde está hospedado?

**Achados (tudo público, daqui do Dell):**
- **Registrante do domínio: OCULTO** (privacidade de WHOIS; RDAP só expõe registrador eNom + abuse@enom.com). Registrado 2016.
- **Hospedagem: VPS próprio com CyberPanel 2.5 + OpenLiteSpeed**, site WordPress 7.0.4 + Elementor 3.30.3 (`x-powered-by: CyberPanel-OLS/2.5.0`, 404 "Proudly powered by LiteSpeed").
- **Linha do tempo por certificados (certspotter):** Let's Encrypt p/ fenixfilmes.com+www em **07/06** e **07/08** (= servidor próprio servindo o site desde ~junho, ANTES da migração) → **30/08: 2 certificados de uma vez**: wildcard `*.fenixfilmes.com` por **Google Trust Services** (assinatura da entrada no Cloudflare) + Let's Encrypt novo na origem. Bate com last-modified 20:37 + RDAP 20:41.
- **Conclusão:** o site já rodava no VPS (do Leandro ou da produtora) desde junho com DNS apontando direto; em 30/08 o Leandro colocou o Cloudflare na frente → zona nova no CF → MX/SPF esquecidos → e-mail morto.
- **Contramedidas do webmaster (foi cuidadoso):** subdomínios comuns (cpanel/webmail/mail/ftp/direct/autodiscover…) NADA exposto (tudo proxy ou inexistente); `/wp-json/wp/v2/users` 404; feed sem autores; nenhum e-mail/crédito no site atual nem no arquivado (Wayback 03/2026: título "Fênix Filmes - Produtora e Distribuidora de Filmes", zero e-mails). IP real da origem: **não descobrível por fora**.
- **Rede social:** instagram.com/fenixfilmes1.
- **O que falta (contratação/faturas/senhas) só existe no Gmail da Priscila** — lista de 10 buscas enviada ao Telegram do Miguel (leandro · cloudflare · wordpress · cyberpanel · vps · hospedagem · enom · google domains · workspace · fatura). Se ela não conseguir LOGAR no Gmail → suspeita de suspensão Workspace sobe.

## 8. 🔄 ADENDO 4 — Sessão browser + admin + update do app (01/09 15:0x→15:2x, ZCode/GLM-5.3)

**O que aconteceu:**
- Miguel recebeu credenciais da Priscila pelo WhatsApp (⚠️ **senha NÃO gravada em lugar nenhum** — usada só no navegador, uma vez).
- **Login na conta Google da Priscila FUNCIONOU** (feito manualmente pelo Miguel no navegador dele, após o browser do ZCode ser bloqueado pelo anti-bot do Google no passo do e-mail) → **conta ATIVA e não suspensa** (fatura em dia) → o "não envia" era sintoma local (app/celular dela deslogado); o problema real documentado é o recebimento (MX).
- **Admin Workspace aberto** (Conta → Domínios → Gerenciar domínios → fenixfilmes.com → Status da configuração do e-mail): o PRÓPRIO GOOGLE CONFIRMA **MX "Incorreto" · SPF "Ausente" · DKIM "Incorreto"** — bate 100% com meu diagnóstico por `dig`. Não há "Configurações avançadas de DNS" no admin (domínio é standalone, ex-Google Domains → painel mora no **Squarespace**).
- **Assistente "Ativar o Gmail" aberto**: mostra MX `@ · smtp.google.com · pri 1 · TTL 3600` (idêntico à mensagem pro Leandro) + botão **"Abrir verificação"** (usar SÓ DEPOIS de add o registro). A tabela do assistente também listava o valor **DKIM** (`google._domainkey` com chave `p=MIIBIjAN...`) — usar na fase 2.
- **Bug de UI do ZCode à solta** (texto do agente sumindo): fichado como `BUG-20260901-ZCODE-UI-TEXTO-SUMINDO` no NODE_BUGS_ATIVOS (app 3.10.2, sem crash no log, hipótese scroll-jump em respostas longas; mitigação = respostas curtas + Telegram). **Miguel vai fechar o app p/ atualizar** (auto-update ligado) — se o texto sumir após update, o bug continua vivo.
- Gmail da Priscila acessível (11.7 mil mensagens) — buscas (`cloudflare`/`leandro`/`squarespace`/`wordpress`/`vps`) ainda NÃO executadas; ficam pra retomada se necessário.

**Estado:** diagnóstico 100% confirmado pelo Google; correção depende de: (a) Leandro add MX+SPF no Cloudflare dele (mensagem pronta), ou (b) Miguel assumir domínio no Squarespace (`account.squarespace.com` → Log in with Google da Priscila → DNS/Nameservers — zona antiga com MX dormindo deve estar lá), ou (c) ambos. Depois: "Abrir verificação" no assistente + fase 2 (DKIM + teste de envio).
**Falta:** o registro MX/SPF entrar no DNS; verificação Google; DKIM; teste real.
**Preciso do Miguel:** mandar a mensagem pro Leandro e/ou entrar no Squarespace; retomar a sessão após update do app.

## 9. 🔄 ADENDO 5 — Verificação do Google falhou (esperado); app atualizado (01/09 15:27)

- Miguel clicou no botão de verificação do assistente ("Abrir verificação") ANTES do registro existir → erro "Não foi possível concluir a verificação" + "preparando seu domínio". **Checado daqui 15:27: MX e SPF ainda vazios** — falha esperada, nada quebrou. Assistente também oferecia "Acessar o Cloudflare" (Google detectou NS=CF): inútil por ora — abre login da conta CF do **Leandro**.
- Ordem correta registrada: (1) add MX+SPF no DNS (Leandro ou Squarespace) → (2) "Abrir verificação" de novo.
- App ZCode atualizado pelo Miguel (~15:2x) — vigiar se o bug de texto sumir morreu (BUG-20260901-ZCODE-UI-TEXTO-SUMINDO).

## 10. 🏁 ADENDO 6 — eNom ACESSADO + mapa final (01/09 16:00→16:10, ao vivo com o Miguel)

**Conquistas da sessão ao vivo:**
- **Login Google da Priscila OK** (conta ativa/paga; suporte = Leandro do print = o próprio webmaster do WhatsApp).
- **Admin Workspace**: tela "Status da configuração do e-mail" confirma MX/SPF/DKIM errados; assistente "Ativar o Gmail" tem botão "Acessar o Cloudflare" (integração Google↔CF não aplicável: conta CF da Priscila estava VAZIA).
- **e-mail da renovação achado no Gmail dela**: domínio gerenciado pelo GOOGLE com registrador eNom, renovação automática (confirmada por RDAP: válido até 09/01/2027).
- **🔑 COFRE ABERTO**: Admin → Conta → Domínios → fenixfilmes.com (menu ⋮/detalhes) → "Configurações avançadas do DNS" revelou login do console eNom (login `fenixfilmes.com` + senha + PIN — ⚠️ **NÃO gravados aqui**; só na tela do Miguel) → **eNom Central acessado** (central.enom.com).
- **Zona NOVA no Cloudflare da Priscila**: domínio adicionado (plano free, status Pending, NS designados **lilyana** + **quinton**.ns.cloudflare.com); scan importou 4 A + 4 AAAA (todos IPs de PROXY da zona velha → **devem ser substituídos pelo IP REAL da origem antes de ativar, senão error 1000/site cai**) + 2 TXT _acme-challenge mortas; MX/SPF ainda não confirmados como adicionados.

**Página do domínio no eNom revelou:** modo **CUSTOM** (NS → CF velho justin/katelyn; "ERROR: Cannot get list of existing nameservers" = lentidão do painel, campos não carregados — NÃO estão vazios de verdade); **Host Records DESATIVADOS** ("use default DNS") = registros do site NÃO estão no eNom (estão na zona CF velha de alguém); expira 09/01/2027; Registrar Lock on.

**Estado do quebra-cabeça:** controle total do REGISTRADOR (eNom) ✅ + zona CF nova da Priscila ✅ + valores MX/SPF/DKIM ✅. **FALTA 1 PEÇA: o IP REAL do VPS do site** (CyberPanel) — fontes: (a) quem publicou o site em 30/08 (pergunta à Priscila — ela contratou), (b) headers de e-mails antigos do formulário do site (Received: from = IP do VPS), (c) dono da zona CF velha. **Plano de ativação:** 1) IP real na mão → 2) zona CF nova: A @/www → IP real (proxied), AAAA off, MX+SPF+DKIM TXT → 3) eNom: Custom NS → lilyana/quinton → 4) dig daqui confirma → 5) admin Google "Abrir verificação" → 6) teste de envio. Alternativa B: eNom DEFAULT + Host Records no próprio eNom (mesma dependência do IP real).

**⚠️ Segurança:** senha eNom/PIN ficaram na tela do Miguel — orientado a não compartilhar; não gravar em fórum/memória.

## 11. 🏆 ADENDO 7 — VITÓRIA: E-MAIL RESTAURADO (01/09 16:5x BRT)

**Como fechou (rota final):** modo Default do eNom falhava com `ERROR: Nameservers for fenixfilmes.com cannot be registered / Cannot get list of existing nameservers` → **rota alternativa venceu**: Miguel adicionou MX+SPF na zona CF nova → eNom Edit DNS Information → **Custom** com `lilyana.ns.cloudflare.com` + `quinton.ns.cloudflare.com` → **salvou e propagou em minutos**.

**Provas (16:55–16:58 BRT):**
- `dig @lilyana.ns.cloudflare.com MX fenixfilmes.com` → `1 smtp.google.com.` ✅ · TXT SPF ✅
- `dig @8.8.8.8 MX fenixfilmes.com` → `1 smtp.google.com.` ✅ · NS = lilyana/quinton ✅
- Relato do Miguel: **e-mails chegando na caixa dela + ela consegue enviar pra si mesma** (auto-envio = rota externa MX funcionando).

**Resíduos de propagação (explicados a ele):** primeiros testes do Gmail dele → provavelmente **bounced** (MX não existia na hora; procurar "Mail Delivery Subsystem" e reenviar); e-mails dela pra ele podem estar no **spam** (sem DKIM ainda).

**PENDÊNCIAS FASE 2 (site + acabamento):**
1. 🔴 **SITE FORA DO AR** (combinado "e-mail primeiro"): A/AAAA da zona CF nova = IPs proxy da zona velha → error 1000. **Cura:** achar o **IP real do VPS** (CyberPanel) — fontes: quem publicou o site em 30/08 (perguntar à Priscila/Leandro) ou headers `Received: from [IP]` de e-mails de formulário do site no Gmail dela → editar no CF novo: A @/www → IP real (proxied), apagar AAAA de proxy e TXTs `_acme-challenge` mortos.
2. **DKIM:** CF novo → DNS → Add TXT `google._domainkey` com o valor `v=DKIM1; k=rsa; p=MIIBIjAN...` (visível na tabela "Status da configuração do e-mail" do admin) → depois admin Google → "Autenticar e-mails". Reduz spam.
3. Zona CF **velha** (justin/katelyn, conta de alguém) → órfã, ignorar. Conta eNom: senha/PIN ficam com o casal (não gravados aqui).
4. Wizard "Ativar Gmail" no admin: concluir verificação (status → Concluída).

**Estado da missão:** ✅ **E-MAIL DA PRISCILA RESTAURADO** (~2h25 de sessão, 14:32→16:58). Faltam: site (IP real) + DKIM. **Preciso do Miguel:** resposta de quem publicou o site (IP do servidor) + OK pra fase 2.

## 12. 🏆 ADENDO 10 — VITÓRIA DUPLO-DEFINITIVA: E-MAIL + SITE (03/09 06:5x, com API)

**Contexto da retomada:** 02/09 11:44 o eNom **reverteu sozinho** os NS pra justin/katelyn (painel bugado — documentado no `runbook_fenixfilmes_email_site_20260902.md` do DSC, que também descobriu o **HostGator `162.241.3.30` com cópia viva do site** — revalidado 03/09 06:45, www 200).

**Execução 03/09 06:45→06:58 (ZM + Miguel, 13 min):**
- Miguel criou **API Token CF** (1º com escopo errado — 0 zonas; 2º correto: Edit Zone DNS) → **guardado nos 2 cofres como `CF_TOKEN_FENIXFILMES`** (backups `.bak_pre_fenix_token_20260903`, hash md5-8 `ad1d769e`, espelho conferido IGUAL; valor nunca em fórum/memória). Zone ID `cae31de3…` + Account ID anotados.
- **ZM aplicou via API** (`/zones/{id}/dns_records`): A `@` e `www` → **`162.241.3.30` proxied**; apagados 2 A duplicados + 4 AAAA + 2 TXT `_acme-challenge`; MX/SPF confirmados; **DKIM `google._domainkey` ADICIONADO** (chave da tabela do admin). Backup da zona pré-correção: `bug_gmail/zona_backup_pre_correcao_20260903.json`.
- **Miguel aplicou no eNom** (06:55, adiantou o Passo 2): Custom → lilyana/quinton.

**Provas finais (06:56–06:57):** NS lilyana/quinton propagando (oscilação de cache normal); **MX `1 smtp.google.com.` estável no 8.8.8.8**; SPF presente; **site HTTP 200 com título certo — ZERO downtime** (janela mista: zona velha servia VPS novo, nova serve HostGator, ambas 200).

**Pendências de acabamento:** (1) Miguel: teste real de e-mail + "Abrir verificação"/"Autenticar e-mails" no admin; (2) futura: IP do VPS novo (site definitivo — cópia HostGator defasa se editarem o novo); (3) monitorar se o eNom reverte o NS de novo → se sim, chamado no registrador (GoogleClients@enom.com) + re-aplicar (5 cliques ou ZM via... eNom não tem token na mão — manual).

## 13. 🔴 ADENDO 11 — E-MAIL CAIU DE NOVO: 3ª REVERSÃO AUTOMÁTICA DO NS (07/09 08:50→09:1x, ZCode/Qwen3.8-Max)

**Pedido do Miguel (07/09 ~08:5x):** "consertamos o e-mail + botamos o site no ar, mas o e-mail voltou a cair — verifica o que aconteceu, vamos consertar de novo."

**Diagnóstico (fechado, com prova):**
- `dig @8.8.8.8 / @1.1.1.1 NS fenixfilmes.com` → **justin/katelyn** (zona velha) = **3ª reversão** (30/08 original → 02/09 11:44 → **agora**).
- `dig @8.8.8.8 MX/TXT/DKIM` → **TUDO VAZIO** = e-mail morto (a zona velha não tem registros de e-mail — confirmado por `dig @justin.ns.cloudflare.com MX` autoritativo: vazio).
- **RDAP Verisign: `last changed 2026-09-04T05:28:55Z` = 04/09 02:28 BRT** ← data/hora da 3ª reversão (~22h DEPOIS da cura definitivo-dupla de 03/09 06:55). **E-mail morto desde então (~3 dias)** — o que chegou nesse período, bounceou.
- **API Cloudflare (CF_TOKEN_FENIXFILMES do cofre, sha8 3ed70dc5):** zona `cae31de3420e52edc6d88acd8d72e14b` (conta da Priscila) com **status `moved`** — activated_on 03/09 14:45 UTC, modified_on **04/09 14:45 UTC** (hora em que o CF detectou que o NS saiu).
- **Zona nova INTACTA (nada a refazer nela):** auditoria API lista exatamente 5 registros: A `@` e `www` → **162.241.3.30 proxied** (HostGator) + MX `smtp.google.com` + SPF + DKIM `google._domainkey`. Conferido também por `dig @lilyana.ns.cloudflare.com` (MX/SPF/DKIM respondendo).
- **Site NO AR (HTTP 200, título certo)** servido pela zona velha = **VPS CyberPanel** (x-powered-by CyberPanel-OLS/2.5.0) — ou seja, hoje o site serve a versão VIVA do Leandro, não a cópia HostGator.
- **Cópia HostGator revalidada 07/09:** apex responde **301 → https://www.fenixfilmes.com/** e o www no HostGator responde **200** → **virar o NS de volta NÃO derruba o site** (apenas troca a origem pra cópia, que pode defasar se editarem o VPS — trade-off já aceito no runbook).

**Cura (a peça que falta é SÓ do Miguel — credencial eNom nunca foi gravada, por segurança):**
1. **eNom → Edit DNS Information → Custom → `lilyana.ns.cloudflare.com` + `quinton.ns.cloudflare.com` → Save → RECARREGAR e conferir** (Passo 2 do `runbook_fenixfilmes_email_site_20260902.md`; o painel já reverteu sozinho antes — confirmar que salvou).
2. Avisar o ZM → verificação: `dig @8.8.8.8 NS/MX` + status da zona na API (`moved` → `active`; propagação em minutos, como em 01/09 e 03/09).
3. 🔴 **ABRIR CHAMADO NO eNom (GoogleClients@enom.com) AGORA** — 3ª reversão automática comprovada por RDAP (02/09 ~11:44 BRT e 04/09 02:28 BRT, ninguém mexeu). O runbook já previa isso desde a 2ª. Sem o chamado, é enxugar gelo.
4. **PLANO B (blindagem, independente do chamado):** `bug_gmail/MENSAGEM_PRA_WEBMASTER.txt` **ATUALIZADA (v2, 07/09)** — pedir ao Leandro que adicione **MX + SPF + DKIM na zona VELHA** (justin/katelyn). Com os registros nas DUAS zonas, qualquer reversão de NS deixa de derrubar o e-mail.
5. Acabamento (quando o NS estabilizar): admin Google → "Abrir verificação" + "Autenticar e-mails" (DKIM já está no DNS da zona nova desde 03/09); caçar o IP real do VPS p/ o site definitivo.

**Estado da missão:** diagnóstico 100% fechado (zona nova intacta, site no ar, e-mail morto desde 04/09 02:28 BRT pela 3ª reversão do eNom). **O que falta:** os 4 passos do Miguel acima (o 1 resolve em minutos; o 3 é a causa raiz; o 4 blinda). **Preciso do Miguel:** aplicar o NS no eNom + me avisar p/ verificar + decidir se manda a mensagem pro Leandro.

## 14. ✍️ NOTA DE RETIFICAÇÃO — WEBMASTER = MIGUEL; "LEANDRO" NÃO EXISTE MAIS (07/09 ~09:3x, ordem do Miguel)

**Fala do Miguel (07/09 ~09:3x):** "Esquece o Leandro. O webmaster sou eu. Eu que estou resolvendo isso. Não tem Leandro nenhum mais."

**Consequências (valem para TODAS as sessões/agentes):**
1. **CANCELADO o Plano B do Adendo 11** (mensagem ao "Leandro" pedindo MX/SPF/DKIM na zona velha) — `MENSAGEM_PRA_WEBMASTER.txt` v2 marcada CANCELADA. Nenhuma mensagem deve ser enviada a "Leandro"; nenhuma sessão deve aguardar resposta dele.
2. As menções anteriores a "Leandro" neste fórum/memória (Adendos 3, 6, 7, 10, 11) eram a hipótese da época (print do suporte WhatsApp 01/09) — ficam como registro histórico, **superadas por esta nota**.
3. **Blindagem nova (opcional):** SE o Miguel tiver acesso à conta Cloudflare da zona VELHA (justin/katelyn — a que serve o VPS), ELE MESMO pode adicionar lá MX + SPF + DKIM → qualquer reversão futura de NS deixa de derrubar o e-mail.
4. **Pendência antiga destravada:** o "IP real do VPS" (site definitivo, no lugar da cópia HostGator) agora se resolve direto com o Miguel (ele é o webmaster). Com o IP, o ZM atualiza os A da zona nova via API (token já no cofre).
5. O essencial NÃO muda: **eNom → Custom NS lilyana/quinton** (cura imediata) + **chamado no eNom** (causa raiz das 3 reversões automáticas).

## 15. ✅ ADENDO 12 — NS REAPLICADO PELO MIGUEL (07/09 09:41 BRT): PROPAGAÇÃO VERIFICADA, E-MAIL RESTAURADO + CHAMADO eNom PREPARADO (ZCode/Qwen3.8-Max, 07/09 ~09:5x)

**O Miguel aplicou o Custom NS no eNom Central** ("pronto. mudei.") e o ZM verificou na hora:

1. **RDAP Verisign:** `last changed 2026-09-07T12:41:03Z` (= **07/09 09:41:03 BRT**) · NS no registrador = `LILYANA.NS.CLOUDFLARE.COM` + `QUINTON.NS.CLOUDFLARE.COM` ✅ — timestamp oficial da 4ª aplicação (a 1ª desde 04/09).
2. **Resolver Google (8.8.8.8), 09:47 BRT:** NS = lilyana/quinton ✅ · **MX = `1 smtp.google.com.`** ✅ · SPF `v=spf1 include:_spf.google.com ~all` ✅ — **o e-mail da Priscila voltou a receber** (nível de resolução pública restaurado em ~6 min).
3. **NS autoritativo novo (lilyana), direto:** MX responde ✅ (ruído IPv6 no dig = benigno).
4. **1.1.1.1 ainda mostrava justin/katelyn às 09:47** — cache de resolver, esperado; vira em minutos/horas. Não afeta o Google (8.8.8.8 já ok).
5. **Site:** apex `https://fenixfilmes.com` **200** · www **200** ✅ — servido pela cópia HostGator (162.241.3.30) pela zona nova, como previsto no runbook; nada caiu.
6. **API Cloudflare (zona `cae31de3…`, conta da Priscila):** status ainda **"moved"** às 09:47 (a CF re-detecta a delegação em minutos→horas e volta pra "active" sozinha; é só contabilidade da CF — **não impede o e-mail**, que já resolve pelo 8.8.8.8).

**Chamado eNom (causa raiz):** rascunho em inglês **entregue ao Miguel no chat** para `GoogleClients@enom.com` — reporta as reversões automáticas de 02/09 e 04/09 (com timestamps RDAP), pede logs internos de quem/o quê alterou, correção da causa raiz (provável bug de auto-restore/sync da migração Google Domains→eNom) e confirmação de que o Custom NS atual persiste. Cópia de registro (SEM o PIN — regra do Cofre; PIN vai só no e-mail, para o fim que existe): `Outros/Negocios Priscila/bug_gmail/EMAIL_PARA_ENOM_20260907.txt`. Login de atendimento e PIN foram fornecidos pelo Miguel no chat de 07/09 — **não gravados aqui**.

**Falta agora:** (1) Miguel **enviar** o e-mail ao eNom; (2) acabamento no Google Admin ("Abrir verificação" + "Autenticar e-mails" — DKIM já está na zona); (3) blindagem opcional (Miguel add MX/SPF/DKIM na zona VELHA se tiver acesso à conta CF dela); (4) IP real do VPS (Miguel fornece → ZM atualiza os A via API); (5) **VIGILÂNCIA 4ª reversão:** se o RDAP `last changed` mudar de novo sem ação do Miguel = reverteu outra vez → reaplicar + cobrar o chamado; (6) pedir aos remetentes que tiveram bounce entre 04/09 e 07/09 que **reenviem**.

## 16. 📸 ADENDO 13 — PRINT DO PAINEL eNom PÓS-MUDANÇA (Miguel enviou 09:46; ZM conferiu 10:06, ZCode/Qwen3.8-Max)

1. **Print** (`access.enom.com/domainmain.aspx?edit=updateDNS#DNS`, 07/09 09:46, enviado pelo Miguel no chat): **Domain Name Server 1 = `lilyana.ns.cloudflare.com` · 2 = `quinton.ns.cloudflare.com`** — bate com o RDAP (`last changed 2026-09-07T12:41:03Z`). Expiração exibida no painel: 1/9/2027 (bate com RDAP 2027-01-09).
2. **Peculiaridade visual:** em modo de edição os rádios "Custom" (DNS Settings) e "Registrar Lock" aparecem SEM seleção marcada, embora os campos mostrem o NS custom — a verdade server-side é o RDAP (lilyana/quinton ativos e propagados). Orientação dada ao Miguel: F5 fora do modo de edição e conferir; se o rádio ainda aparecer vazio, re-clicar **Custom** + Edit/Save e recarregar; e deixar **Registrar Lock = Enable (recommended)** (protege contra transferência indevida; não afeta DNS).
3. **"Host Records: to enable host records, you need to use the default DNS settings"** — esperado e CORRETO: com Custom NS os registros próprios do eNom ficam inativos; todos os registros (MX/SPF/DKIM/A) vivem na Cloudflare. Nada a mexer ali.
4. **Rechecagem 10:06 BRT:** RDAP inalterado (12:41:03Z, lilyana/quinton) · 8.8.8.8 NS + MX `1 smtp.google.com` ok · site 200 — **sem 4ª reversão**. Vigilância mantida: qualquer `last changed` novo sem ação do Miguel = reversão → reaplicar + cobrar chamado.
5. Pendências inalteradas: Miguel **enviar** o chamado ao `GoogleClients@enom.com` (rascunho no chat 09:5x + cópia SEM PIN em `bug_gmail/EMAIL_PARA_ENOM_20260907.txt`); admin Google "Abrir verificação"/"Autenticar e-mails"; IP real do VPS; blindagem opcional na zona velha.

---
*Memória técnica completa: `Memorias/memoria_email_priscila_fenixfilmes_mx_20260901.md`
Tema relacionado: `Foruns/forum_alianca_fenix_cafezinho_palestina_20260825.md` (canal de e-mail c/ a Fênix)
