---
name: reference-servidor-wp-cafezinho-ssh
description: "Servidor WordPress do Cafezinho (us65.serverdo.in 190.89.239.65 porta 51439) — acesso SSH por chave configurado, alias cafezinho-wp local, ponteiros para credenciais e tutorial sem expor senha."
metadata: 
  node_type: memory
  type: reference
  originSessionId: c6c1efc3-9035-46e2-a05f-6b3f83fe0ea4
---

# Servidor WordPress do Cafezinho — SSH

**Configurado:** 2026-06-28 10:58 BRT

## Identificação

- **Hostname:** `us65.serverdo.in`
- **IP:** `190.89.239.65`
- **Porta:** `51439` (não-padrão; NUNCA usar 22)
- **User:** `root` (PermitRootLogin yes, ainda)
- **Stack:** OpenSSH 8.2p1 / Ubuntu 20.04 / Kernel 5.4

NÃO confundir com:
- `190.89.239.3:51439` — IP antigo do ticket (auth falhou, descartado 28/06).
- `43.156.151.165:38422` — Tencent (Cingapura), só agentes Python, NÃO tem WP.

## Acesso configurado

Acesso por chave instalado (Claude Code, 28/06):
- Chaves locais Miguel `~/.ssh/id_rsa.pub` + `~/.ssh/id_ed25519.pub` adicionadas em `/root/.ssh/authorized_keys` do servidor.
- Backup `authorized_keys.bak_pre_miguel_20260628_*` no `/root/.ssh/` antes de mexer.
- Alias `cafezinho-wp` em `~/.ssh/config` local.

Uso:
```bash
ssh cafezinho-wp
ssh -p 51439 root@190.89.239.65
ssh -o BatchMode=yes cafezinho-wp 'comando'   # script, sem prompt
```

## Onde estão as credenciais (NÃO repetir senha aqui)

- **Credenciais cruas com senha:** `Outros/chaves/ssh_servidor_wp_cafezinho.md` (gitignored, fora do repo público).
- **Tutorial / cartão de bolso compartilhável com outros agentes IA:** `Cerebro/CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md`.
- **Referência no CLAUDE.md:** §12, subseção "Servidor WordPress (us65.serverdo.in)".

## Pendências pra Miguel autorizar

1. Trocar senha root no painel ServerDo.in (compartilhada em chat com IA + suporte).
2. Hardening sshd: `PasswordAuthentication no` + `PermitRootLogin prohibit-password` após confirmar chave 100%.

## O que mora neste servidor

- WordPress de `https://www.ocafezinho.com` e `https://controle.ocafezinho.com`.
- Plugin **Code Snippets** com snippet **"Cafezinho Noindex Pruning 358 URLs (recovery SEO 2026-06-27)"** ativo desde 27/06 17:25 BRT (ver [[project-sprint-recuperacao-seo-27jun-pausa]]).
- Banco MySQL do WP (credencial em `wp-config.php` quando logar).

NÃO mora:
- Robôs Python do enxame (esses estão no Tencent `43.156.151.165:38422`).
- Banco mídia legado de 345k imagens (Tencent também).
- V3 de mídia (Tencent).
