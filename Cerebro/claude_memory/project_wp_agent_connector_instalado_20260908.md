---
name: project-wp-agent-connector-instalado-20260908
description: "Plugin WP Agent Connector v0.9.13 (YLabs) instalado em ocafezinho.com 08/09 12:32 BRT, autorizado Miguel, testado, rollback SSH pronto. Conexão hoje = admin Miguel; próximo passo = migrar App Password para Editor dedicado"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1e65b525-4779-4da8-ad3d-793dcfe4565d
---

## Instalação WP Agent Connector v0.9.13 — 08/09/2026 12:32 BRT

**Autorização Miguel** chat CLI: "Pode instalar e testar o WP Agent Connector conforme o plano de rollback que você preparou". Ordem complementar 12:33: "não faça teste público, ou seja, nada que apareça para o público" — cumprido (só GETs e `wp eval` internas ao servidor, zero POST em `/wp/v2/posts`).

**Why:** Miguel queria testar a integração do WP Agent (serviço que já conecta ao site sem o plugin) com capacidades adicionais: SEO writing (Yoast/Rank Math/AIOSEO), Additional CSS, site overview, fallback de auth em hosts que strip `Authorization`.

**How to apply:**
- **Diretório:** `/var/www/ocafezinho/wp-content/plugins/wp-agent-connector/`
- **Slug:** `wp-agent-connector` (não confundir com nome interno "YLabs AI Assistant Connector" nem text-domain `ylabs-ai-assistant-connector`)
- **Namespace REST:** `wp-agent/v1`
- **Rollback ~2s via SSH:**
  ```bash
  ssh cafezinho-wp "wp plugin deactivate wp-agent-connector --path=/var/www/ocafezinho --allow-root"
  ```
  Se WP-CLI travar:
  ```bash
  ssh cafezinho-wp "mv /var/www/ocafezinho/wp-content/plugins/wp-agent-connector /var/www/ocafezinho/wp-content/plugins/wp-agent-connector.DISABLED"
  ```
- **Documento técnico completo (auditoria linha por linha, snapshot preflight, testes):** `~/cerebro-miguel/cerebro/Foruns/wp_agent_connector_instalacao_20260908.md`
- **Bloco anúncio Trindade:** `de_dell.md` CM-20260908-001

## Endpoints e capabilities confirmadas

| Endpoint | Cap | Editor default? |
|---|---|---|
| `GET /wp-agent/v1/site-state` | `manage_options` | ❌ 403 |
| `GET /wp-agent/v1/seo-status` | `edit_posts` | ✅ 200 |
| `GET,POST /wp-agent/v1/seo-meta/{id}` | `edit_post` | ✅ 200 |
| `GET,POST /wp-agent/v1/custom-css` | `edit_theme_options` | ❌ 403 |

**Confirmado via simulação `wp eval` com Editor `agy_laura` (usuário Editor real que já existe no site).** Editor default do WP cobre 100% do escopo desejado por Miguel; endpoints "poderosos" ficam bloqueados naturalmente sem qualquer edit de role/cap.

## Estado da App Password AGORA (ordem migração pendente)

- Conexão atual do WP Agent = admin **Miguel do Rosário** (confirmado `/wp/v2/users/me`)
- Miguel quer migrar para usuário Editor dedicado com escopo: posts/mídia/categorias/SEO Yoast; sem admin de plugins, tema, CSS ou options
- Objetivo: reduzir superfície de risco se App Password vazar

## Riscos residuais

- 🟡 **Ownership arquivos = `root`** (não `www-data`). Atrapalha auto-update via wp-admin. Correção sugerida `chown -R www-data:www-data <path>` **não executada — não foi autorizada**.
- 🟡 **Wordfence** pode marcar header custom `X-WPAgent-Authorization` como suspeito (não confirmado). Se plugin desligou App Passwords no Wordfence, o Connector religa (PHP_INT_MAX vence).
- 🟢 Yoast/Rocket/Redis/CDN/JWT/RSS: sem conflito real detectado.

## Ligações

- [[feedback-checagem-dupla-antes-publish-v41-20260829]] — checagem dupla se aplica a qualquer mudança sensível
- [[feedback-tensao-constante-autoaprendizado-memoria-bugs-20260826]] — TENSÃO: manter olho aberto em Wordfence live traffic e error_log PHP nas próximas 24h
