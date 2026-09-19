---
name: WordPress Cafezinho está hospedado em ServerDo.in (não Tencent/NYC)
description: Descoberta crítica 28/04 — controle.ocafezinho.com vive em us65.serverdo.in. Sem SSH direto. Para deploy de código PHP usar plugin WPCode Lite que já está ativo.
type: project
originSessionId: 2c8ca443-cdc4-4211-8398-01df9ce389b7
---
**Fato:** O WordPress de `controle.ocafezinho.com` NÃO está no Tencent (`43.156.151.165`) nem no NYC (`45.55.50.249`). Está em **`us65.serverdo.in`** (IP `190.89.239.65`), provedor **ServerDo.in** (plugin "CDN ServerDo.in" confirma).

**Why:** Em 28/04, durante deploy de MU-plugin anti-duplicate UUID, gastei tempo procurando WP no Tencent. Tencent só tem agentes Python; nenhum nginx/apache rodando. Tarefa ficou bloqueada até descobrir o host real via `nslookup` + reverse DNS.

**How to apply:**
- Quando precisar editar arquivos do WordPress (themes, plugins, wp-content), **não tente SSH no Tencent** — não tem nada lá.
- Para qualquer deploy de código PHP custom no WP do Cafezinho: usar **WPCode Lite** (plugin `insert-headers-and-footers/ihaf`, já ativo). É equivalente a MU-plugin via UI admin.
- Para arquivos de mídia/posts: REST API (`/wp-json/wp/v2/`) com user `Redator` (App Password em CLAUDE.md §12). User é admin completo (`install_plugins: true`).
- Endpoints úteis:
  - `/wp-json/wp/v2/plugins` lista todos plugins (instala via slug WP.org só)
  - `/wp-json/wp/v2/users/me?context=edit` confirma capabilities
  - `/wp-json/wp/v2/types` lista CPTs (WPCode snippets não expostos via REST)
- Credenciais SFTP/cPanel próprios do ServerDo.in: **NÃO** estão no `.env.unificado`. `CPANEL_MIGUEL_PASS`/`CPANEL_COMERCIAL_PASS` são senhas IMAP de email do domínio `ocafezinho.com`, não acesso SSH/SFTP do servidor WP.
- Se precisar SFTP, perguntar a Miguel — ele tem o painel ServerDo.in.

**Plugins relevantes ativos no WP (snapshot 28/04):**
- WPCode Lite — injetar PHP/JS/CSS snippets globais
- UpdraftPlus — backup
- WPeMatico — RSS importer
- Yoast SEO Premium, WP Rocket, Really Simple Security
- Wordfence — **inativo** (não bloqueia deploys)
- Temporary Login Without Password — inativo, mas disponível pra gerar acesso temporário se precisar

**Snippets PHP custom ativos no WPCode Lite (snapshot 28/04 11:29 BRT):**
- "Indent UUID Protection (anti-duplicate)" — rejeita POST com `_indent_uuid` duplicado via HTTP 409. Hook `rest_pre_insert_post`. Lê UUID de `$request->get_param()` (cobre JSON + form-encoded). Salva UUID como post_meta `_indent_uuid`. Arquivo de referência local: `Projeto Cafezinho Agentes/root/wp_indent_protection.php` (versão original tinha bug de $_POST com JSON; versão deployada foi corrigida via consultoria GPT auditada).

**Lição operacional 28/04:** snippet PHP que lê body do REST request DEVE usar `$request->get_param()`, NÃO `$_POST`. WordPress só popula `$_POST` quando body é form-encoded. Em JSON (caso default de `requests.post(url, json=payload)`), `$_POST` fica vazio.
