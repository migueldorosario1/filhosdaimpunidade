# Memória — E-mail do domínio mokareader.com (GoDaddy)

- **Data de abertura:** 2026-07-22
- **Agente:** ZCode/Kimi, com Miguel
- **Status:** 🟡 EM ANDAMENTO — DNS verificado ✅, criação da caixa de correio pendente (ação do Miguel no painel GoDaddy)

---

## 1. Contexto

Miguel pediu tutorial para configurar o e-mail do domínio `mokareader.com` (registrado na GoDaddy). Tema novo — não havia registro prévio no Cérebro. Pedido do Miguel: ir anotando aqui conforme a resolução avança.

## 2. Diagnóstico DNS (verificado via `dig` em 2026-07-22 ~22:45)

| Registro | Valor | Estado |
|----------|-------|--------|
| MX (prio 0) | `smtp.secureserver.net.` | ✅ propagado |
| MX (prio 10) | `mailstore1.secureserver.net.` | ✅ propagado |
| SPF (TXT) | `v=spf1 include:spf.em.secureserver.net ?all` | ✅ propagado |
| DKIM CNAME | `secureserver1._domainkey` → `s1.dkim.mokareader_com.593.onsecureserver.net.` | ✅ propagado |
| DKIM CNAME | `secureserver2._domainkey` → `s2.dkim.mokareader_com.593.onsecureserver.net.` | ✅ propagado |

**Conclusão:** o lado DNS está 100% pronto. Os registros são do **E-mail Profissional GoDaddy** (infra `secureserver.net` — não é Microsoft 365, que usaria `*.mail.protection.outlook.com`). Também há um TXT de verificação de titularidade (`"T8435342"`).

## 3. O que falta (passos ensinados ao Miguel)

1. **Criar a caixa de correio** no painel GoDaddy: `Meus Produtos` → seção **E-mail** → `Gerenciar` → criar usuário/endereço (ex.: `contato@mokareader.com`) + senha.
2. **Webmail:** `email.godaddy.com` (login com o e-mail completo + senha criada).
3. **Cliente de e-mail** (Thunderbird/Outlook/app): IMAP `imap.secureserver.net:993` (SSL) / SMTP `smtpout.secureserver.net:465` (SSL) ou 587, usuário = e-mail completo.
4. **Teste:** enviar e-mail de fora (Gmail) para a caixa nova e responder; confirmar ida para Caixa de Entrada (não spam) — valida MX + SPF + DKIM na prática.

⚠️ **Atenção:** se não houver plano de e-mail pago ativo na conta, a GoDaddy cobra por caixa. Alternativas gratuitas (Zoho Mail etc.) exigiriam **trocar os registros MX** — decisão a registrar aqui se ocorrer.

## 4. Observações do DNS atual (não quebrar)

- Domínio também serve o site: registro `A @ → 216.198.79.1` e CNAMEs `www`/`video` para Vercel (`vercel-dns-016/017.com`). Qualquer mudança de nameserver (ex.: migrar para Cloudflare) precisa preservar esses registros.

## 5. Log de resolução

- **2026-07-22 ~22:45** — Diagnóstico DNS concluído (tabela §2). Tutorial entregue ao Miguel. Aguardando ele criar a caixa no painel e reportar resultado do teste de envio/recebimento.
- **2026-07-22 ~23:00** — **Bloqueio encontrado:** painel GoDaddy recusa envio com aviso "registro SPF incorreto". **Causa raiz:** o SPF do domínio era `v=spf1 include:spf.em.secureserver.net ?all` — esse include é do **Microsoft 365**, mas o produto ativo é o **E-mail Profissional** (MX/DKIM `secureserver.net`). Ou seja, SPF configurado para o produto errado (provável preenchimento automático da GoDaddy). **Correção orientada:** editar o TXT `@` existente (nunca criar segundo SPF) para `v=spf1 include:secureserver.net -all`.
- **2026-07-22 ~23:10** — **Registro travado:** Miguel localizou o TXT SPF (página 2 da tabela DNS, registros 11-13), mas **Editar e Excluir estão bloqueados** — registro gerenciado pela GoDaddy, não editável manualmente. Página de ajuda oficial ("Editar um registro SPF") confirma o valor-alvo mas não cobre o caso travado. **Descoberta importante:** a caixa **`info@mokareader.com` já existe** (visível em Meus Produtos → E-mail → Visão geral, usuário "Miguel do Rosario"). Dashboard tem abas Visão geral / Encaminhamentos / Aliases. Domínio também tem DMARC ativo (`_dmarc`, p=quarantine, rua=dmarc_rua@onsecureserver.net). **Próximo passo:** botão de correção automática no aviso do painel; se não houver, suporte GoDaddy (chat "Fale conosco") para destravar/corrigir o registro gerenciado.
