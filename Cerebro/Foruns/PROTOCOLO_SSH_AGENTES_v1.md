# PROTOCOLO SSH/REST AGENTES v1 — Cafezinho

**Aberto:** 22/08/2026 09:14 BRT · **Redator:** Claude Miguel · **Origem:** ordem Miguel pós-bug 267037 (foto Ricardo Barros publicada como cena de vacinação SUS) — Emendas 1+2+3 do `CONTRATO-AUTONOMIA-ESCUTA-V1`
**Status:** VIGENTE (Miguel homologou 22/08 09:14 corpo/Emenda 1, 09:22 Emenda 2, 09:52 Emenda 3 + Fase 1 SSH universal)

## Sumário — o que mudou

Antes desta fase, só existiam 2 canais SSH auditáveis: `loop-laura-write` (whitelist rígida ZCode Miguel, Grok Laura usa) e `loop-laura-ro` (read-only, ZCode Laura). Todos os demais agentes ou não tinham SSH ou usavam `id_rsa` do Miguel (`root`) — sem trilha por identidade.

Miguel ordenou expandir SSH+REST **por agente nomeado**, com whitelist granular por capacidade e auditoria de autoria/telemetria unificada. Fase 1 (servidor) executada 22/08/2026 09:45-09:52 BRT.

## Estado final Fase 1

### 1. Users unix criados (11)

| User | Papel | Whitelist |
|---|---|---|
| `claude_miguel` | Loop Miguel Claude (Dell) | FULL_WRITER |
| `agy_laura` | Loop Laura Antigravity (Windows) | FULL_WRITER |
| `claude_laura` | Loop Laura Claude (Windows) | FULL_WRITER |
| `agy_miguel` | Loop Miguel Antigravity (Dell) | FULL_WRITER |
| `grok_laura` | Loop Laura Grok (xAI) | IMAGE_WORKER |
| `grok_miguel` | Loop Miguel Grok (xAI) | IMAGE_WORKER |
| `codex_miguel` | Loop Miguel Codex (OpenAI) | TEXT_EDITOR |
| `codex_laura` | Loop Laura Codex (OpenAI) | TEXT_EDITOR |
| `zcode_miguel` | Loop Miguel ZCode/Kimi | TEXT_EDITOR |
| `zcode_laura` | Loop Laura ZCode/Kimi | TEXT_EDITOR |
| `manus2` | Manus 2 nuvem (migueldorosario2) | MANUS_APPEND |

Todos são membros do grupo `cafezinho-agents` (sudoers-restrito).

### 2. Users WordPress criados (11)

Mesmos nomes que os users unix (`claude_miguel`... `manus2`), role **editor**, IDs WP `5788-5798`, e-mail `<agente>@cafezinho.internal`. Password aleatório strong (não usado — SSH forced-command é o canal). Application Passwords pro REST podem ser gerados sob demanda via `wp user application-password create <agente> "<agente>-<uso>" --allow-root`.

### 3. Whitelist granular por capacidade

Definida em `/usr/local/sbin/cafezinho-wp-write` (Python) — dict `WHITELIST_BY_USER`:

```python
FULL_WRITER = {update-title, update-content, update-excerpt, update-taxonomy,
               set-media, set-img-check, media-import, publish, schedule,
               meta-canibal, meta-velharia, term-nohome, health}
IMAGE_WORKER = {set-media, set-img-check, media-import, health}
TEXT_EDITOR = {update-title, update-content, update-excerpt, update-taxonomy,
               set-media, set-img-check, media-import, meta-canibal,
               meta-velharia, term-nohome, health}
MANUS_APPEND = {health}  # append via chave dedicada (REST)
```

### 4. Comandos disponíveis (3 novos v3)

Além do que ZCode Miguel definiu (v2, 21/08/2026):
- `meta-canibal <post_id> <valor>` → grava `_cafezinho_descartado_canibal`
- `meta-velharia <post_id> <valor>` → grava `_cafezinho_descartado_velharia`
- `term-nohome <post_id>` → adiciona categoria `no-home` (id 20699) via `wp_set_object_terms` append

Ex: `ssh cafezinho-cm "meta-canibal 267036 canibal_de_266937_regua_72h"`

### 5. Sudoers

Herdado + novo:
```
# /etc/sudoers.d/loop-laura-write (herdado ZCode Miguel)
loop-laura-write ALL=(www-data) NOPASSWD: /usr/local/libexec/cafezinho-wp-write-reader *

# /etc/sudoers.d/cafezinho-agents (novo v3, 22/08)
%cafezinho-agents ALL=(www-data) NOPASSWD: /usr/local/libexec/cafezinho-wp-write-reader *
```

### 6. Audit unificado

**Log SSH wrapper:** `/var/log/auth.log` linhas `cafezinho-wp-write:` com formato:
```
user=<agente> result=<allowed|denied_user_whitelist|denied_validate|reader_failed_N|timeout|output_too_large> operation=<comando args>
```

**Consulta:**
```bash
ssh cafezinho-cm "health"  # gera log
sudo grep cafezinho-wp-write /var/log/auth.log | tail -20
```

**Audit REST (quando ativo):** cada action_password autentica como `<agente>` → nginx `/var/log/nginx/access.log` + WP plugin audit (não instalado ainda; decidir depois pelo custo DB).

**Audit banco:** cada action feita via wp-cli sob o user correto → `wp_posts.post_author`, `wp_postmeta.meta_id`, `wp_activity_log` (se plugin ativo).

## Chaves SSH (Fase 2 — pendente por agente)

Fase 1 criou users unix + `.ssh/authorized_keys` VAZIO por agente. Fase 2 é distribuir chaves — feita **na máquina do agente**, não aqui.

**Fluxo por agente:**
1. Na máquina do agente: `ssh-keygen -t ed25519 -N '' -f ~/.ssh/<agente>_ed25519 -C "<agente>@<maquina>"`
2. Copia `.pub` (só a pública)
3. Root no cafezinho-wp: `echo 'command="/usr/local/sbin/cafezinho-wp-write",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty <PUB>' >> /home/<agente>/.ssh/authorized_keys`
4. Testa: `ssh -i ~/.ssh/<agente>_ed25519 <agente>@190.89.239.65 -p 51439 "health"`

**Config local recomendado (~/.ssh/config):**
```
Host cafezinho-<alias>
    HostName 190.89.239.65
    Port 51439
    User <agente>
    IdentityFile ~/.ssh/<agente>_ed25519
    IdentitiesOnly yes
    ServerAliveInterval 60
```

Já feito pra Claude Miguel no Dell: alias `cafezinho-cm` (usa `id_rsa`).

## Testes de validação Fase 1 (22/08 09:52 BRT)

Todos passaram:
- `ssh cafezinho-cm "health"` → `{"ok":true,...}` ✓
- `ssh cafezinho-cm "meta-canibal 267036 teste_wrapper_v3_cm_20260822"` → `{"ok":true,"result":"updated"}` ✓
- `ssh cafezinho-cm "delete-post 267036"` → `{"ok":false,"error":"command_denied"}` (fora da whitelist v3) ✓
- Simulação user `manus2` publish → `{"ok":false,"error":"command_denied_for_user"}` ✓
- Simulação user `grok_laura` publish → denied (IMAGE_WORKER não tem publish) ✓
- `loop-laura-write` legado ainda funciona `health` ✓

## Rollback

**Script pronto** em `/root/rollback_ssh_agentes_v1.sh confirm`. Reverte:
1. Wrapper Python v3 → v2 (backup `cafezinho-wp-write.bak_pre_v3_20260822_094802`)
2. query.php v3 → v2 (backup `cafezinho-wp-write-query.php.bak_pre_v3_20260822_094802`)
3. Deleta 11 users unix (preserva homedirs por segurança)
4. Deleta grupo `cafezinho-agents`
5. Remove `/etc/sudoers.d/cafezinho-agents`
6. Deleta 11 users WP

Backups em `/root/backups/ssh_agentes_v1/`. Snapshot total em `pre_deploy_20260822_094547.tar.gz` (1.3MB).

## Adicionar novo agente futuro

1. Editar `/root/deploy_agentes.sh` — adicionar ao array `AGENTES`
2. Editar `/usr/local/sbin/cafezinho-wp-write` — adicionar entrada no `WHITELIST_BY_USER`
3. Rodar `/root/deploy_agentes.sh apply` (idempotente, só afeta o novo)
4. Distribuir chave (Fase 2)
5. Testar `ssh <alias> "health"`

## Referências

- **Arquivos servidor:**
  - `/usr/local/sbin/cafezinho-wp-write` (wrapper Python v3 multi-agente)
  - `/usr/local/sbin/cafezinho-wp-readonly` (wrapper Python read-only legado — não tocado)
  - `/usr/local/libexec/cafezinho-wp-write-reader` (shell → wp eval-file)
  - `/usr/local/libexec/cafezinho-wp-write-query.php` (PHP com validações + 3 comandos novos v3)
  - `/etc/sudoers.d/cafezinho-agents` (grupo permite reader como www-data)
  - `/root/deploy_agentes.sh` (script deploy idempotente)
  - `/root/rollback_ssh_agentes_v1.sh` (script rollback)
  - `/var/log/auth.log` (audit)
  - `/root/backups/ssh_agentes_v1/` (backups pré-v3)

- **Contrato:**
  - `Cerebro/Foruns/contrato_autonomia_escuta_anticonflito_v1_PROPOSTA_20260822.md` (§6 Emenda 1, §7 Emenda 2)
  - `Cerebro/Foruns/forum_contrato_autonomia_escuta_20260822.md` (livros de assinatura)
  - `Cerebro/Foruns/PROTOCOLO_SSH_AGENTES_v1.md` (este arquivo)

- **Memória:**
  - `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/feedback_gate_img_check_valida_filename_e_title_attachment_20260822.md`

- **JSONL:**
  - `Cerebro/monitoramento_horario/bugs_encontrados/bugs_2026-08-22.jsonl` (registros CM-030, CM-032, próximos)
