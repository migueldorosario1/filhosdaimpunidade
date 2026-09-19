---
name: reference-gsc-property-sc-domain-cafezinho
description: Site URL correto para GSC API do ocafezinho.com é sc-domain:ocafezinho.com (NÃO https://www.ocafezinho.com/ — service account sem acesso a essa property específica)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 595de6c5-a613-4f51-b42d-e3bc009de9ef
---

Para queries Google Search Console API do `ocafezinho.com` via service account `indexing-cafezinho@gen-lang-client-0200069757.iam.gserviceaccount.com`, usar `siteUrl="sc-domain:ocafezinho.com"`. 

**Why:** Confirmado empiricamente 28/06 via `service.sites().list().execute()` — service account é `siteOwner` em `sc-domain:ocafezinho.com`, `https://ocafezinho.com/` (sem www), `sc-domain:globalsouth.news`, `https://www.riocarta.com/`. **NÃO é Owner de `https://www.ocafezinho.com/`** (com www). Tentar essa URL retorna HTTP 403 "User does not have sufficient permission". Property `sc-domain:` é a mais abrangente (cobre www, sem www, http, https, subdomínios).

**How to apply:** Em qualquer script Python que use `googleapiclient build("searchconsole", "v1")` para o Cafezinho, hardcode `SITE_URL = "sc-domain:ocafezinho.com"`. Ver `/root/util_cron_gsc_diario.py` (deployado 28/06 20:15 BRT). Para descobrir properties acessíveis em outros domínios do projeto: `service.sites().list().execute()` retorna `siteEntry[]` com `permissionLevel`. Note também `mundotrilhos.com` consta como `siteUnverifiedUser` (precisa verificação) — NÃO usar GSC API nele até resolver.

Relaciona com [[project-seo-monitoramento-fase0-20260628]].
