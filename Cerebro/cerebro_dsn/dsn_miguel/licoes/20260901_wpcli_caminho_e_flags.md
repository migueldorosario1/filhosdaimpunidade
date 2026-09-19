# Lição 2026-09-01 · WP-CLI: a ferramenta existe, o que faltava era o endereço

**Ronda:** DS-20260901-047 (23:30, 39º CHECK) · **Quem:** DS Miguel (Dell)

## O quê
O padrão "SSH cafezinho-wp sem DNS" relatado em rondas anteriores estava errado (ou era transitório): nesta ronda o SSH conectou normal (us65.serverdo.in) e o `wp` só funcionou com duas flags que nunca estavam no comando padrão:

- `--allow-root` (a sessão SSH cai em root e o wp-cli se recusa a rodar como root sem essa flag)
- `--path=/var/www/ocafezinho` (o wp-cli rodava de `/root/` e não achava a instalação do WordPress; há também `/var/www/rioocafezinho`)

Com elas: `wp --allow-root --path=/var/www/ocafezinho post list --post_status=future --format=count` → **0** (future) e `--post_status=pending,draft` → **2804** (colchão).

## Por quê
A lição de trás é a mesma da janela certa (licoes/20260901_janela_certa_para_a_pergunta_certa.md) aplicada à infra: antes de declarar um canal quebrado ("sem DNS", "não é WordPress"), conferir **caminho e flags**. O canal estava vivo o tempo todo — o comando é que não tinha o endereço. Diagnóstico errado de canal = ferramenta útil tratada como morta por semanas.

## Como aplicar
1. Ao sondar o servidor: `ssh cafezinho-wp "wp --allow-root --path=/var/www/ocafezinho post list --post_status=future --format=count"`.
2. Se o `wp` reclamar de caminho, procurar o `wp-config.php` (`find /var/www -maxdepth 2 -name wp-config.php` — há `ocafezinho` e `rioocafezinho`).
3. Atualizar a régua mental: "SSH sem DNS" não é mais o padrão a registrar — é exceção a provar; o padrão é SSH ok + wp com flags.
4. Registrar nos nodos/memória quando o canal "quebrado" voltar a funcionar — o retorno também é informação.
