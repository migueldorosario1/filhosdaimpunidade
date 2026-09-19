# Fórum — Acesso SSH ao Servidor WordPress do Cafezinho

**Data:** 20 de julho de 2026
**Escopo:** acesso SSH ao servidor que hospeda o WordPress do Cafezinho, como referência única para a rodada de mudanças que Miguel vai detalhar.
**Fora do escopo:** as mudanças em si (serão explicadas depois e, se necessário, ganham fórum próprio).

## Situação congelada

Miguel anunciou que vamos trabalhar mudanças no Cafezinho e pediu um fórum dedicado exclusivamente ao acesso ao servidor, indexado no Cérebro. Este documento consolida o que já existia disperso (cartão de bolso + arquivo de credenciais) num ponto de entrada operacional.

## Servidor

| Campo | Valor |
|---|---|
| Host | `us65.serverdo.in` (ServerDo.in) |
| IP | `190.89.239.65` |
| Porta SSH | `51439` (**não** usar 22) |
| Usuário | `root` |
| Autenticação | chave RSA já instalada (desde 28/06) para Miguel local; senha no arquivo canônico de credenciais |

> **Credenciais cruas NÃO ficam neste fórum.** Fonte canônica (gitignored, não duplicar):
> `Outros/chaves/ssh_servidor_wp_cafezinho.md`
> Tutorial completo: `Cerebro/cartoes_bolso/CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md`

## Como entrar

```bash
ssh cafezinho-wp                       # alias preferido (~/.ssh/config local)
ssh -p 51439 root@190.89.239.65        # explícito; senha está no arquivo canônico
```

## Onde ficam as coisas no servidor

```bash
ls /var/www/                                        # raiz dos sites (WP)
find / -name "wp-config.php" -type f 2>/dev/null    # localiza o WP exato
tail -f /var/log/nginx/access.log                   # tráfego ao vivo
crontab -l                                          # cron do sistema (não confundir com wp-cron.php)
```

## Regras de higiene (obrigatórias)

1. **Não** usar `ssh -A` — agent forwarding vaza chaves para outros hosts.
2. Backup antes de mexer: `cp arquivo arquivo.bak_$(date +%Y%m%d_%H%M%S)`.
3. Senha nunca em git, fórum público ou documento sincronizado — só vive no arquivo canônico gitignored.
4. **Pendência de segurança:** a senha foi compartilhada em chat com IA + suporte ServerDo.in em 28/06. A recomendação de rotacioná-la pelo painel ServerDo.in continua **não cumprida**. Qualquer trabalho neste servidor deve considerar essa rotação como dívida ativa.

## Não confundir com outros servidores

| Servidor | IP | Porta | Função |
|---|---|---|---|
| ✅ **us65.serverdo.in** | `190.89.239.65` | `51439` | **WordPress Cafezinho (este)** |
| Tencent | `43.156.151.165` | `38422` | Só robôs Python |
| NYC | `198.199.121.136` | `22` | Agentes V4 + Sentinela + Baleia Azul |
| GSN | `159.89.237.100` | `22` | WP do Global South News |

`controle.ocafezinho.com/wp-admin` e `https://www.ocafezinho.com` são servidos por este servidor. Tencent **não** tem WP.

## Próximos passos

1. Miguel detalha as mudanças planejadas no Cafezinho.
2. Antes da primeira alteração: backup do que for tocado (regra 2) e registro neste fórum do que será mudado.
3. Avaliar execução da rotação de senha (dívida desde 28/06) como parte desta rodada de trabalho.

---

— Registrado por Kimi (ZCode), 2026-07-20, a pedido de Miguel.
