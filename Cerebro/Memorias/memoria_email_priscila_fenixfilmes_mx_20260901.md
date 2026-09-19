# 📝 Memória técnica — E-mail Priscila fenixfilmes.com sem MX (01/09/2026)

**Sessão:** ZCode/GLM-5.3 (Dell) · **Janela:** 14:32→14:4x BRT · **Fórum:** `Foruns/forum_email_priscila_fenixfilmes_mx_20260901.md`

## Log do que foi feito (comandos e provas)

1. **Print do WhatsApp** (`Outros/Negocios Priscila/bug_gmail/WhatsApp Image 2026-09-01 at 14.26.39.jpeg`): print do notebook da Priscila (WhatsApp Web) com o suporte (Leandro) — mensagem é a citada pelo Miguel (MX ausente, instrução de add MX `@` → `SMTP.GOOGLE.COM` pri 1, artigo support.google.com/a/answer/174125).
2. **Diagnóstico DNS público (Bash, sem credencial):**
   - `dig MX fenixfilmes.com +short` → **vazio** (zero registros MX)
   - `dig NS fenixfilmes.com +short` → `justin.ns.cloudflare.com.` `katelyn.ns.cloudflare.com.`
   - `dig TXT fenixfilmes.com +short` → **vazio** (sem SPF)
   - `dig TXT google._domainkey.fenixfilmes.com +short` → vazio (sem DKIM)
   - `dig A fenixfilmes.com +short` → `104.21.9.143` `172.67.160.134` (IPs de proxy Cloudflare — site no ar)
   - `whois` local falhou (sem saída); usado **RDAP Verisign** (`curl https://rdap.verisign.com/com/v1/domain/fenixfilmes.com`):
     - registro 2016-01-09 · expira 2027-01-09 · registrar **eNom, LLC**
     - `last changed 2026-08-30T23:41:06Z` = **30/08 20:41 BRT** ← data da mudança que matou o e-mail
3. **Prova de e-mail funcionando antes:** fórum aliança Fênix (`forum_alianca_fenix_cafezinho_palestina_20260825.md`): 28/08 17:28 Priscila respondeu follow-up enviado 17:01 (`250 OK` no msmtp.log) → recebimento funcionava em 28/08.
4. **Cofre checado (Regra Nº 1/4):** `CEREBRO_NODE_COFRE_CHAVES.md` + `.env.unificado` — só existe credencial **R2 Cloudflare** (storage, escopo Object Read&Write) — **NÃO existe token de DNS** → correção no painel é manual do Miguel (ou criar token Zone→DNS→Edit e cofrar pra autonomia futura).
5. **Telegram ao Miguel** (`ponte_cafezinho.py --send`, exit 0, 14:33): diagnóstico resumido + passos Cloudflare + 4 perguntas pra repassar à Priscila.
6. **Monitoramento:** linha adicionada em `MONITORAMENTO_DE_TRABALHO.md` (Regra Nº 2).

## Conclusão técnica

MX e SPF ausentes desde a mudança de 30/08 20:41 BRT (migração pra Cloudflare sem copiar registros de e-mail). Correção aditiva e segura: `@ MX smtp.google.com pri 1` + `@ TXT "v=spf1 include:_spf.google.com ~all"` no dashboard Cloudflare. DKIM fica pendente (gerar no admin.google.com depois).

## Estado

- FEITO: diagnóstico datado + provas, plano entregue, perguntas enviadas, Tema Duplo gravado.
- PENDENTE: Miguel aplicar os 2 registros; verificação `dig`; teste real de recebimento; respostas da Priscila (login × recebimento); DKIM opcional.
- Próxima sessão retoma por: este arquivo + fórum + linha no monitoramento.

## Lições

- Migração de DNS pra Cloudflare (ou qualquer troca de NS) **precisa de checklist de exportação**: comparar `dig MX/TXT/CNAME/AAAA/A` do velho ANTES de desligar o NS antigo — e-mail morre silenciosamente dias depois, quando alguém nota.
- "Não consigo entrar no Gmail" (fala do usuário) ≠ diagnóstico técnico (MX = recebimento). Sempre separar LOGIN de RECEBIMENTO antes de mexer.


## Adendo técnico 07/09/2026 — 3ª reversão de NS (ZCode/Qwen3.8-Max)

**Sintoma:** e-mail caiu de novo (relato do Miguel 07/09 ~08:5x); site segue no ar.

**Provas coletadas (07/09 08:50→09:1x BRT):**
- `dig @8.8.8.8 NS fenixfilmes.com +short` → `justin.ns.cloudflare.com.` / `katelyn.ns.cloudflare.com.` (idem 1.1.1.1) — NS na zona velha.
- `dig @8.8.8.8 MX/TXT/google._domainkey +short` → vazios; `dig @justin.ns.cloudflare.com MX +short` → vazio (autoritativo da zona velha SEM e-mail).
- RDAP Verisign: `last changed 2026-09-04T05:28:55Z` (**04/09 02:28 BRT**) — 3ª reversão, ~22h após a cura de 03/09 06:55 BRT. Registro 2016, expira 2027-01-09, registrar eNom.
- API CF (`GET /zones?name=fenixfilmes.com`, token `CF_TOKEN_FENIXFILMES` — sha8 `3ed70dc5`, 53 chars, presente nos 2 `.env.unificado`): zone id `cae31de3420e52edc6d88acd8d72e14b`, conta "Priscila@fenixfilmes.com's Account", **status `moved`**, name_servers lilyana/quinton, activated_on `2026-09-03T14:45:26Z`, modified_on `2026-09-04T14:45:28Z` (detecção CF da saída do NS).
- API CF (`GET /zones/{id}/dns_records`): **5 registros, zona intacta** — A `@`→162.241.3.30 proxied · A `www`→162.241.3.30 proxied · MX `@`→smtp.google.com · TXT SPF · TXT DKIM `google._domainkey` (chave idêntica à publicada em 03/09).
- `dig @lilyana.ns.cloudflare.com` MX/TXT/DKIM/A → tudo responde certo (zona nova viva, só não está delegada).
- Site: `curl https://fenixfilmes.com` → **HTTP 200**, título "Fênix Filmes - Produtora e Distribuidora de Filmes", headers `server: cloudflare` + `x-powered-by: CyberPanel-OLS/2.5.0` (zona velha → **VPS vivo**).
- HostGator direto (`--resolve fenixfilmes.com:443:162.241.3.30`): apex **301 → https://www.fenixfilmes.com/**; seguindo com www também resolvido p/ 162.241.3.30: **final 200** → virar o NS não derruba o site.

**Ação tomada (agente):** linha no monitor + Adendo 11 no fórum + `MENSAGEM_PRA_WEBMASTER.txt` v2 (plano B: MX+SPF+DKIM na zona velha pelo Leandro — DKIM é público por natureza, valor copiado do dig da zona nova).

**Cura pendente (só Miguel):** (1) eNom Custom NS lilyana/quinton + reload-conferência; (2) chamado eNom GoogleClients@enom.com citando as 2 reversões datadas por RDAP (02/09 11:44 BRT, 04/09 02:28 BRT); (3) opcional blindagem: o próprio Miguel add MX/SPF/DKIM na zona velha (✍️ webmaster = MIGUEL; "Leandro" cancelado — nota 14 do fórum); (4) pós-NS: admin Google "Abrir verificação"/"Autenticar e-mails". Verificação ZM pós-aplicação: `dig @8.8.8.8 NS/MX` + API status `moved`→`active`.

**Padrão confirmado:** eNom reverte NS custom SOZINHO (3ª vez) — enquanto não houver chamado/transferência, a cura é reaplicar (5 cliques) e/ou tornar as duas zonas equivalentes em registros de e-mail (plano B).

## Adendo técnico 07/09/2026 ~09:5x — NS REAPLICADO pelo Miguel: propagação verificada

- Miguel aplicou Custom NS no eNom Central **07/09 ~09:41 BRT** ("pronto. mudei.").
- **RDAP Verisign 09:4x:** `last changed 2026-09-07T12:41:03Z` · nameservers = `LILYANA.NS.CLOUDFLARE.COM`, `QUINTON.NS.CLOUDFLARE.COM` (timestamp oficial da reaplicação).
- **dig @8.8.8.8 09:47 BRT:** NS `quinton/lilyana.ns.cloudflare.com` · MX `1 smtp.google.com.` · TXT `"v=spf1 include:_spf.google.com ~all"` — e-mail restaurado em resolução pública ~6 min após a mudança.
- **dig @1.1.1.1 09:47:** ainda `justin/katelyn` (cache de resolver — esperado, vira em minutos/horas).
- **dig @lilyana.ns.cloudflare.com MX:** `1 smtp.google.com.` (autoritativo novo ok; "communications error" IPv6 no dig = benigno, respostas IPv4 chegaram).
- **curl 09:47:** `https://fenixfilmes.com` **200** · `https://www.fenixfilmes.com` **200** (site servido pela cópia HostGator via zona nova).
- **API CF zona `cae31de3420e52edc6d88acd8d72e14b` 09:47:** status ainda `"moved"` · `activated_on 2026-09-03T14:45:26Z` · `modified_on 2026-09-04T14:45:28Z` — reativação automática pendente (contabilidade CF; não impede MX).
- **Chamado eNom:** rascunho EN entregue ao Miguel no chat (To: `GoogleClients@enom.com`); cópia de registro SEM PIN em `Outros/Negocios Priscila/bug_gmail/EMAIL_PARA_ENOM_20260907.txt`. Login de atendimento + PIN fornecidos pelo Miguel no chat 07/09 — **valores NÃO gravados** (regra do Cofre). O rascunho cita: reversões sem ação do titular em 02/09 ~14:44 UTC (observação) e **04/09 05:28:55 UTC** (RDAP), reaplicações 01/09 e 03/09, nova aplicação 07/09 12:41:03 UTC; pede logs internos, correção da causa raiz (hipótese: auto-restore/sync da migração Google Domains→eNom) e garantia de persistência.
- **Vigilância:** novo `last changed` no RDAP sem ação do Miguel = 4ª reversão → reaplicar (runbook Passo 2) + cobrar chamado.
**Cura pendente (só Miguel):** (1) eNom Custom NS lilyana/quinton + reload-conferência; (2) chamado eNom GoogleClients@enom.com citando as 2 reversões datadas por RDAP (02/09 11:44 BRT, 04/09 02:28 BRT); (3) opcional blindagem: mensagem v2 pro Leandro; (4) pós-NS: admin Google "Abrir verificação"/"Autenticar e-mails". Verificação ZM pós-aplicação: `dig @8.8.8.8 NS/MX` + API status `moved`→`active`.
- **Print do painel eNom (Miguel, 09:46):** NS 1/2 = lilyana/quinton salvos (confere RDAP 12:41:03Z); rádios "Custom"/"Registrar Lock" aparecem sem marca em modo de edição (peculiaridade visual do access.enom.com — verdade server-side = RDAP); orientação: F5-conferência + Registrar Lock = Enable; Host Records inativos com Custom NS = esperado. Rechecagem 10:06: sem 4ª reversão (RDAP inalterado, MX/site ok). Fórum seção 16 (Adendo 13).
