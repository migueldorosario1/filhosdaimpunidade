---
name: Sentinela V4 — arquivos canônicos no servidor
description: Nomes reais dos arquivos de estado do V4 no Tencent — o que MEMORY.md antigo dizia estava errado
type: reference
originSessionId: 64e4c471-3031-4a70-a7b1-a07c8b6e5a0d
---
## Arquivos canônicos do Sentinela V4 (Tencent SG, `/root/agent_data/`)

Verificado 2026-04-22 03:00 BRT durante baseline do monitoramento 24h.

| Memória dizia | Nome REAL no servidor | Status |
|---|---|---|
| `principios_aprendidos.json` | **NÃO EXISTE** com esse nome | — |
| `curas_realizadas.json` | **NÃO EXISTE** com esse nome | — |
| (não citado) | `autocura_acoes.json` (254KB, mtime hoje) | ✅ ATIVO |
| (não citado) | `autocura_v4.log` (587KB) | ✅ ATIVO |

**Why:** A memória antiga (`sistema_aprendizado_autocura.md`, `plano_sentinela_v4_autocura.md`)
citava nomes que nunca existiram no servidor. Ao tentar `ls principios_aprendidos*`
retorna vazio. Os nomes reais são `autocura_acoes.json` (registro de TODAS as
ações: cura_regex/cura_llm/rebaixar) e `autocura_v4.log`.

**How to apply:** Ao consultar estado do V4 ou auditar autoaprendizado, usar os
nomes REAIS. NÃO confiar nos nomes da memória antiga sem `ls` antes.

```bash
# Listar JSONs de estado do V4
ssh cingapura 'sudo ls -la /root/agent_data/autocura_*'
```

### Bonus achado: WordPress NÃO está no Tencent

Tencent SG é **só servidor de agentes** (publica via REST API). WP do Cafezinho
fica em `controle.ocafezinho.com` (host externo). Verificado: nenhum
nginx/apache/php-fpm rodando no Tencent, nenhum `wp-config.php` no filesystem.

Pra contar drafts/publicados, usar REST API direto (`/wp-json/wp/v2/posts?status=draft|publish`)
com auth basic do `WP_USER=Redator` (lido de `/root/.env`).
