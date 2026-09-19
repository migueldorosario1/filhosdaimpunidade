# Cartão de Bolso — SSH ao Servidor WordPress do Cafezinho

**Atualizado:** 2026-08-14
**Para quem:** Grok, Codex, Claude Code, GLM, qualquer agente CLI que precise acessar o servidor onde roda o WP do Cafezinho.

> **Fonte canônica das credenciais (gitignored, NÃO duplicar):**
> `Outros/chaves/ssh_servidor_wp_cafezinho.md`
>
> Este cartão é o **tutorial** — credenciais cruas estão lá.

> **REGRA OPERACIONAL (13/08, playbook expandido 14/08/2026):** para conferir ou corrigir posts no canônico, preferir este SSH + WP-CLI em `/var/www/ocafezinho` como `www-data`. Receitas (listar, inspecionar, backup, No Home, imagem, publicar, validar): `Cerebro/cartoes_bolso/CARTAO_BOLSO_WP_CAFEZINHO_CONFERENCIA_CORRECAO.md`. Node-mãe: `Cerebro/CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md`.
>
> **Relatórios:** use só o alias `cafezinho-wp`. Não cole IP, porta, chave ou senha em chat, fórum ou Git.

---

## TL;DR

```bash
ssh cafezinho-wp                       # alias preferido
ssh -p 51439 root@190.89.239.65        # explícito
```

Acesso por chave já instalado para Miguel local. Outros agentes precisam (1) ter sua chave pública adicionada ao `authorized_keys` do root, ou (2) usar a senha consultando o arquivo de credenciais.

---

## Topologia (não confundir servidores)

| Servidor | IP | Porta | Função |
|---|---|---|---|
| **us65.serverdo.in** | `190.89.239.65` | `51439` | **WordPress do Cafezinho** |
| Tencent | `43.156.151.165` | `38422` | Agentes Python do enxame |
| NYC failover | `198.199.121.136` | `22` | Réplica dormente |
| GSN | `159.89.237.100` | `22` | WordPress do Global South News |

`controle.ocafezinho.com/wp-admin` aponta pro servidor ServerDo.in.
`https://www.ocafezinho.com` também é servido por este servidor.
Tencent **NÃO** tem WP — só roda os robôs.

---

## Acesso passo-a-passo

### 1) Tenha uma chave SSH local

Se você (agente/máquina) ainda não tem:

```bash
ssh-keygen -t ed25519 -C "<seu-identificador>" -f ~/.ssh/id_ed25519_cafezinho
# Aperta Enter pra passphrase vazia (se quiser SSH sem prompt)
```

Mostra a pública pra instalar no servidor:

```bash
cat ~/.ssh/id_ed25519_cafezinho.pub
```

### 2) Instalar a chave pública no servidor (uma vez só)

**Opção A — se você tem a senha** (lê do arquivo `Outros/chaves/ssh_servidor_wp_cafezinho.md`):

```bash
ssh-copy-id -i ~/.ssh/id_ed25519_cafezinho.pub -p 51439 root@190.89.239.65
# Vai pedir a senha do root uma vez
```

**Opção B — via Python+paramiko** (útil quando `sshpass`/`ssh-copy-id` não existe):

```python
import paramiko, os
pub = open(os.path.expanduser('~/.ssh/id_ed25519_cafezinho.pub')).read().strip()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('190.89.239.65', port=51439, username='root',
            password='SENHA_DO_ARQUIVO_DE_CHAVES',
            look_for_keys=False, allow_agent=False, timeout=15)
for c in [
    'mkdir -p ~/.ssh && chmod 700 ~/.ssh',
    'touch ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys',
    'cp ~/.ssh/authorized_keys ~/.ssh/authorized_keys.bak_$(date +%Y%m%d_%H%M%S)',
    f'grep -qxF "{pub}" ~/.ssh/authorized_keys || echo "{pub}" >> ~/.ssh/authorized_keys',
]:
    ssh.exec_command(c)
ssh.close()
```

**Opção C — pedir ao Miguel** que rode os passos acima da máquina local dele.

### 3) Criar alias no `~/.ssh/config` local (opcional, recomendado)

```
Host cafezinho-wp
    HostName 190.89.239.65
    Port 51439
    User root
    IdentityFile ~/.ssh/id_ed25519_cafezinho
    ServerAliveInterval 60
```

### 4) Testar sem senha

```bash
ssh -o BatchMode=yes cafezinho-wp 'whoami && hostname'
# Espera: root \n us65.serverdo.in
```

`BatchMode=yes` bloqueia prompt — se rodou, foi por chave.

---

## Coisas que você vai querer fazer no servidor

### Conferir e corrigir posts (playbook)

Receitas completas — listar 20 recentes (draft/pending/future/publish), inspecionar metas V4/Repetidor, snapshot, No Home `20699`, thumbnail, publicar, validar:

`Cerebro/cartoes_bolso/CARTAO_BOLSO_WP_CAFEZINHO_CONFERENCIA_CORRECAO.md`

```bash
# Teste somente leitura
ssh -o BatchMode=yes cafezinho-wp \
  'sudo -u www-data wp --path=/var/www/ocafezinho post get <ID> --fields=ID,post_status,post_title'

# Para patches controlados, envie um PHP temporário e use funções oficiais do WP:
scp /tmp/patch.php cafezinho-wp:/tmp/patch.php
ssh cafezinho-wp \
  'cd /var/www/ocafezinho && sudo -u www-data wp eval-file /tmp/patch.php'
```

No `patch.php`, preferir `wp_update_post()`, `wp_set_post_categories()`, `wp_remove_object_terms()`, `update_post_meta()` e `set_post_thumbnail()`. Não usar `UPDATE wp_posts ...` como atalho.

Antes de batch com 5+ posts, salvar JSON contendo estado anterior completo. Após o patch, validar status, título, categorias, `_thumbnail_id` e permalink. O tema pode emitir `PHP Notice: HTTP_HOST` no stderr — ignore.

### Localizar o WordPress

```bash
ssh cafezinho-wp
ls /var/www/                              # raiz dos sites
ls /var/www/<dominio>/wp-content/themes/  # tema ativo
ls /var/www/<dominio>/wp-content/plugins/ # plugins (Code Snippets, Yoast etc.)
ls /var/www/<dominio>/wp-content/mu-plugins/  # mu-plugins (se houver)
```

> Path canônico confirmado: `/var/www/ocafezinho`.

### Achar o snippet noindex da Sprint SEO 27/jun

O snippet está cadastrado no plugin **Code Snippets** do wp-admin, não em mu-plugin. Listar pelo banco:

```bash
mysql -u root -p<senha> -e "USE <db_wp>; SELECT id, name, active FROM wp_snippets WHERE name LIKE '%Cafezinho%' OR name LIKE '%noindex%';"
```

Credencial MySQL precisa ser consultada em `/var/www/<dominio>/wp-config.php` ou no painel ServerDo.in.

### Ver logs e tráfego

```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
# ou apache, dependendo do stack:
tail -f /var/log/apache2/access.log
```

### Cron do WP / sistema

```bash
crontab -l
# WP usa wp-cron.php interno (HTTP) — não confundir com crontab Unix.
# Plugin "WP Crontrol" (se instalado) mostra os jobs WP.
```

---

## Hardening sugerido (aguarda AUTH Miguel)

Após confirmar que múltiplos acessos por chave funcionam:

```bash
# Backup
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak_$(date +%Y%m%d_%H%M%S)

# Edit
sed -i 's/^#*PasswordAuthentication .*/PasswordAuthentication no/' /etc/ssh/sshd_config
sed -i 's/^#*PermitRootLogin .*/PermitRootLogin prohibit-password/' /etc/ssh/sshd_config

# Validar config sintaxe
sshd -t && echo OK || echo ERRO

# Reload (sessão atual não cai)
systemctl reload sshd
```

**Antes de aplicar:** abrir 2ª sessão SSH em paralelo e mantê-la aberta como rede de segurança. Se hardening lockar, dá pra reverter da 2ª sessão.

---

## Regras de higiene (todos os agentes)

1. **Nunca** colar senha em `git`-trackeado, em snapshot público, em fórum aberto. Senha mora SÓ em `Outros/chaves/ssh_servidor_wp_cafezinho.md` (gitignored).
2. **Nunca** rodar `ssh -A` (agent forwarding) num servidor que pode ter outras sessões — vaza acesso a outros servidores.
3. **Sempre** fazer backup do `authorized_keys` antes de mexer (`cp .ssh/authorized_keys .ssh/authorized_keys.bak_$(date +%Y%m%d_%H%M%S)`).
4. **Sempre** testar `BatchMode=yes` antes de remover senha — confirma que chave de fato funciona.
5. **Sessão paralela** durante hardening do sshd. Sem rede.
6. Em caso de dúvida com blast radius alto (mexer em sshd, firewall, fail2ban): seguir REGRA #6 do `CLAUDE.md` → abrir `forum<topico>hoje.md` e esperar Miguel.

---

## Quando este cartão fica desatualizado

- Se a porta mudar (improvável).
- Se o IP mudar (servidor migrado).
- Se hardening for aplicado (atualizar "Estado atual do sshd" em `Outros/chaves/ssh_servidor_wp_cafezinho.md`).
- Se Miguel mudar a senha do root (atualizar em `Outros/chaves/ssh_servidor_wp_cafezinho.md`).

Quem detectar a divergência primeiro, atualiza.
