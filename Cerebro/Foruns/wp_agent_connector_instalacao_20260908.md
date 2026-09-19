# WP Agent Connector — Instalação e Auditoria — 08/09/2026

**Autor:** Claude Miguel (`claude-opus-4-7`)
**Data/hora:** 2026-09-08 12:32 BRT
**Autorização Miguel:** chat CLI 12:1x ("Pode instalar e testar o WP Agent Connector conforme o plano de rollback que você preparou")
**Ordem complementar Miguel:** 12:33 "não faça teste público, ou seja, nada que apareça para o público" — cumprido (só GETs e simulações `wp eval` internas ao servidor).

## 1. Identidade do plugin

| Campo | Valor |
|---|---|
| Nome interno | YLabs AI Assistant Connector |
| Diretório real | `wp-agent-connector` |
| Slug/text-domain | `ylabs-ai-assistant-connector` |
| Arquivo principal | `wp-agent-connector.php` |
| Versão instalada | 0.9.13 |
| Autor | YLabs / getwpagent.com |
| Requires | WP ≥5.6, PHP ≥7.4 |
| Tamanho | 3 arquivos (~650 linhas PHP) |
| Hash ZIP oficial | SHA256 `8161c849dd23a3a5dfbc856f22868c0fbb87b7cd828c07fb2e73153f75987bd0` |
| Fonte ZIP | `https://mcp.getwpagent.com/downloads/wp-agent-connector.zip` (Miguel confirmou hash local = oficial) |

## 2. Comportamento do plugin (auditado linha por linha)

### 2.1 Endpoints REST criados (namespace `wp-agent/v1`)

| Método | Rota | Capability | Cobertura Editor |
|---|---|---|---|
| GET | `/site-state` | `manage_options` | ❌ 403 (desejado) |
| GET | `/seo-status` | `edit_posts` | ✅ 200 |
| GET | `/seo-meta/{id}` | `edit_post` no post | ✅ 200 |
| POST | `/seo-meta/{id}` | `edit_post` no post | ✅ 200 |
| GET | `/custom-css` | `edit_theme_options` | ❌ 403 (desejado) |
| POST | `/custom-css` | `edit_theme_options` | ❌ 403 (desejado) |

**Todos os endpoints têm `permission_callback`. Nenhum é anônimo.** Testado sem auth: `/site-state` e `/seo-status` retornam 401 corretamente.

### 2.2 Filters adicionados

1. **`wp_is_application_passwords_available`** (prioridade `PHP_INT_MAX`): força App Passwords ligadas se Wordfence/host tinha desativado globalmente. Só ativa se WordPress core suportaria (HTTPS ou local). Não sobrescreve gate nativo do core.
2. **`determine_current_user`** (prioridade 20): aceita App Password em header custom `X-WPAgent-Authorization` como fallback quando `Authorization` é stripped. Escopo restrito a URIs contendo `/wp-json/` ou `rest_route=`. Valida via função nativa `wp_authenticate_application_password`. Não implementa auth próprio.
3. **`init`** (prioridade 20): expõe meta Yoast/Rank Math no core REST via `register_post_meta` com `auth_callback = current_user_can('edit_post', $post_id)`.

### 2.3 Escrita em banco

- Toda escrita via APIs nativas WordPress (`update_post_meta`, `wp_update_custom_css_post`, AIOSEO model save).
- Zero SQL cru.
- Zero manipulação de `wp_options` durante uso normal.

### 2.4 Uninstall

Apaga apenas `wp_agent_image_key_openai` e `wp_agent_image_key_gemini` (legado da versão 0.9.x, opção removida em 0.9.10). Muito limpo.

## 3. Preflight do site (antes da instalação)

- **Path WP:** `/var/www/ocafezinho`
- **WordPress:** 7.1
- **PHP:** 7.4.33 (atende requisito)
- **Tema ativo:** `ocafezinho-portal` v2.0
- **App Passwords:** já ativadas (`using_application_passwords=1`)
- **Redis:** conectado (phpredis v6.3.0)
- **WP Rocket:** active
- **Yoast SEO + Premium + News + Local:** todos active
- **Plugins ativos:** 45
- **REST `/wp-json/`:** HTTP 200 (0.4s)
- **Snapshot salvo:** `/tmp/wp-agent-snapshot-pre.txt` (Dell local)

## 4. Instalação

Executado 12:32 BRT via SSH `cafezinho-wp`:

```bash
scp /tmp/wp-agent-inspect/wp-agent-connector.zip cafezinho-wp:/tmp/
ssh cafezinho-wp "cd /var/www/ocafezinho && wp plugin install /tmp/wp-agent-connector.zip --activate --allow-root"
```

Output:
```
Descompactando o pacote...
Instalando o plugin...
Plugin instalado com sucesso.
Activating 'wp-agent-connector'...
Plugin 'wp-agent-connector' activated.
Success: Installed 1 of 1 plugins.
```

## 5. Testes pós-instalação

### 5.1 HTTP externos (só GETs)

| URL | Código |
|---|---|
| `https://www.ocafezinho.com/` | 200 |
| `https://www.ocafezinho.com/wp-json/` | 200 |
| `https://www.ocafezinho.com/wp-json/wp/v2/posts?per_page=1` | 200 |
| `https://controle.ocafezinho.com/wp-login.php` | 200 |
| `https://www.ocafezinho.com/wp-json/wp-agent/v1/site-state` (sem auth) | 401 ✅ |
| `https://www.ocafezinho.com/wp-json/wp-agent/v1/seo-status` (sem auth) | 401 ✅ |

### 5.2 Simulação internas via `wp eval` (sem HTTP externo, sem publicação)

**Editor `agy_laura` (usuário Editor real já existente no site):**
- `GET /wp-agent/v1/site-state` → **403** ✅ bloqueado (esperado — exige `manage_options`)
- `GET /wp-agent/v1/seo-status` → **200** ✅ funciona
- `GET /wp-agent/v1/custom-css` → **403** ✅ bloqueado (esperado — exige `edit_theme_options`)

### 5.3 Vitalidade de outros componentes

- Yoast SEO: active
- Yoast SEO Premium: active
- Plugins ativos: 45 → 46 (só o Connector)
- PHP-FPM error_log: só reciclagem cron 03:30 — **zero fatal/warning do plugin**
- Redis: conectado, phpredis v6.3.0 (inalterado)
- WP Rocket: active (inalterado)

## 6. Migração planejada para usuário Editor dedicado

**Ordem Miguel (12:1x):** conexão atual do WP Agent está como admin `Miguel do Rosário`; após confirmar funcionamento, criar usuário Editor dedicado e migrar App Password.

**Objetivo da configuração final:**
- ✅ criar/editar/publicar posts
- ✅ upload de mídia
- ✅ categorias e tags
- ✅ editar SEO/Yoast dos posts
- ❌ administrar plugins
- ❌ editar tema / Additional CSS
- ❌ alterar opções globais

**Confirmação técnica:** role Editor **default do WordPress** cobre 100% dos objetivos. As caps que Editor tem por padrão (`edit_posts`, `edit_others_posts`, `publish_posts`, `upload_files`, `manage_categories`, `edit_post` em posts de outros) satisfazem todos os endpoints SEO do Connector. As caps que Editor **não** tem por padrão (`manage_options`, `edit_theme_options`, `activate_plugins`) bloqueiam naturalmente `/site-state` e `/custom-css`. **Nenhum ajuste de role/cap é necessário.**

## 7. Rollback preparado

**Comando 1 — desativar limpo (preferido):**
```bash
ssh cafezinho-wp "wp plugin deactivate wp-agent-connector --path=/var/www/ocafezinho --allow-root"
```

**Comando 2 — emergência (se WP-CLI/wp-admin travarem):**
```bash
ssh cafezinho-wp "mv /var/www/ocafezinho/wp-content/plugins/wp-agent-connector /var/www/ocafezinho/wp-content/plugins/wp-agent-connector.DISABLED"
```

**Comando 3 — purge completo (deleta + roda `uninstall.php`):**
```bash
ssh cafezinho-wp "wp plugin uninstall wp-agent-connector --path=/var/www/ocafezinho --allow-root"
```

## 8. Riscos residuais e observações

| Componente | Risco | Ação |
|---|---|---|
| Wordfence | 🟡 Média | Se Wordfence tinha App Passwords desativadas, plugin religa (PHP_INT_MAX). Monitorar se Wordfence WAF marca header `X-WPAgent-Authorization` como suspeito |
| Really Simple Security | 🟢 Baixa | Não afeta REST autenticado |
| JWT Auth REST API | 🟢 Baixa | Ambos rodam em `determine_current_user` como fallback complementar; sem loop nem conflito |
| Yoast | 🟢 Baixa | `register_post_meta` duplo pode gerar warning silencioso (Yoast já registra os mesmos meta) — cosmético |
| WP Rocket / Redis / CDN | 🟢 Nulo | Não toca cache |
| **Superfície externa (admin)** | 🟡 **Operacional** | Enquanto App Password admin: WP Agent pode editar Additional CSS + listar todos os 46 plugins. **Mitigação:** migrar pra Editor dedicado (aprovado por Miguel) |
| Maturidade 0.9.13 | 🟢 Baixa | Código pequeno, defensivo, com try/catch em pontos frágeis (AIOSEO v4) |
| **Ownership arquivos = `root`** | 🟡 Baixa | Arquivos criados como `root:root` (não `www-data`). Não afeta operação hoje, mas atrapalha auto-update do plugin via wp-admin. Correção sugerida: `chown -R www-data:www-data /var/www/ocafezinho/wp-content/plugins/wp-agent-connector` (não executado — não foi autorizado explicitamente) |

## 9. Recomendação final

**MANTER ATIVO.** Código auditado, testes passaram, rollback em ~2s via SSH garantido. Aguardar Miguel confirmar migração para Editor dedicado.

## 10. Estado da conexão WP Agent (informação do Miguel)

Confirmado via `/wp/v2/users/me`:
- usuário: **Miguel do Rosário**
- role: **administrator**
- caps: `manage_options`, `edit_theme_options`, `activate_plugins`, `install_plugins`, etc.

Miguel considera isto **temporário** — próximo passo é criar usuário Editor dedicado e migrar App Password.

## Assinatura

Claude Miguel (`claude-opus-4-7`) · 2026-09-08 12:32 BRT
