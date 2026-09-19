# 📘 RUNBOOK — Fênix Filmes: voltar E-MAIL + SITE de uma vez (só o Miguel)

**Criado:** 02/09/2026 ~17:1x BRT · **Por:** ZCode/GLM-5.3 (DSC)
**Contexto:** fórum `forum_email_priscila_fenixfilmes_mx_20260901.md` adendos 7–9 · **Execução:** Miguel em casa, ~5 min, sem depender de terceiros.
**Estado no momento da criação:** NS autoritativo = zona velha (justin/katelyn, revertida sozinha hoje 11:44 BRT) → site NO AR, e-mail SEM MX (quebrado de novo).

## O achado que destrava tudo

O servidor antigo **HostGator `162.241.3.30`** ainda roda uma **cópia viva do site** (probe 02/09: HTTPS 200, mesmo título, WordPress 7.0.4 + Elementor 3.30.3 — mesmas versões do site novo publicado 30/08). Logo, o site pode ser servido daí enquanto o IP do VPS novo não aparece.

## Passo 1 — Cloudflare da Priscila (zona nova, NS lilyana/quinton)

1. `dash.cloudflare.com` (login da Priscila — conta que o Miguel usou 01/09) → domínio **fenixfilmes.com**
2. **DNS → Records**:
   - Editar **A `@`** → conteúdo **`162.241.3.30`** → Save (manter proxy laranja)
   - Editar **A `www`** → conteúdo **`162.241.3.30`** → Save (manter proxy laranja)
   - Opcional (limpeza): APAGAR os registros **AAAA** (4, apontam pra proxy da zona velha) e os **TXT `_acme-challenge`** (2, mortos)
   - CONFERIR que existem: **MX `@` → `smtp.google.com` pri 1** e **TXT `@` → `v=spf1 include:_spf.google.com ~all`** (já estavam em 02/09)
3. Não mexer em mais nada.

## Passo 2 — eNom (mesmo caminho de 01/09)

1. Abrir o eNom Central (login aparece no Google Admin → Conta → Domínios → fenixfilmes.com → ⋮ → "Configurações avançadas de DNS"; credenciais na tela do Miguel, nunca gravadas)
2. **My Domains → fenixfilmes.com → DNS Server Settings (Edit DNS Information) → Custom**
3. NS 1: `lilyana.ns.cloudflare.com` · NS 2: `quinton.ns.cloudflare.com` → **Save**
4. ⚠️ **RECARREGAR A PÁGINA e conferir que os NS novos continuam salvos** — hoje 11:44 BRT o painel reverteu sozinho pra justin/katelyt (ninguém mexeu; painel estava bugado ontem). Se after reload estiver salvo, propagar leva minutos.

## Resultado esperado (ordem de chegada)

- **E-mail:** MX volta a responder → caixa da Priscila recebe em minutos (provado 01/09: ~minutos)
- **Site:** sobe na cópia do HostGator (mesma plataforma/conteúdo publicado; se o site do VPS for editado depois, essa cópia fica defasada — aceitável agora; caçar IP do VPS com calma: e-mails de hospedagem no Gmail dela)

## Verificação (agente, após o Miguel avisar)

```
dig @8.8.8.8 NS fenixfilmes.com +short        # esperar lilyana/quinton
dig @8.8.8.8 MX fenixfilmes.com +short        # esperar 1 smtp.google.com.
curl -s -o /dev/null -w '%{http_code}' https://fenixfilmes.com   # esperar 200
```

## Depois (acabamento, sem pressa)

1. **Trocar a senha do eNom** (segregação: só o casal) — mata a hipótese de 3º mexendo no domínio
2. **DKIM**: Cloudflare novo → TXT `google._domainkey` com valor `v=DKIM1; k=rsa; p=…` (visível no admin Google → Gmail → Autenticar e-mail) → depois "Autenticar e-mails"
3. Admin Google → assistente "Ativar o Gmail" → **"Abrir verificação"** → concluir (status Concluída)
4. Se o NS reverter SOZINHO de novo → é bug do painel eNom/Squarespace → abrir chamado no registrador (e re-aplicar enquanto isso)

## Riscos/rollback

- Mexida é toda na zona NOVA (inerte enquanto NS≠lilyana) → pode editar com calma ANTES do Passo 2, sem risco
- Se algo esquisito após o Passo 2: o estado anterior conhecido é NS→justin/katelyn (site ok, e-mail morto). Voltar = desfazer o Custom. Sem destruição em nenhum caminho.
- Bounces de teste durante a janela quebrada podem existir; e-mails dela→Miguel podem cair no spam até o DKIM.

— ZCode/GLM-5.3 · 02/09/2026
