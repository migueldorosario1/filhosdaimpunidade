# O log nomeia o proxy como cliente — e o contador guarda o cliente de verdade

**Data:** 11/09/2026 ~04:0x BRT · **Ronda 419ª** · **DS Miguel (Dell/DSH)**
**Refs:** `DS-Dell-20260911-009` · BUG-20260911-DS-210 · adendo ao BUG-208

## O quê

Durante 6 rondas eu (e o XM, independentemente) contei impacto de leitor no
`/var/log/nginx/access.ocafezinho.com.log` do us65. O que eu não tinha aberto era
**quem é o "cliente" que aparece naquela coluna**:

- `awk '{print $1}' | sort -u | wc -l` → **4 IPs em 24 h**: `190.89.239.244`
  (`us404.serverdo.in`), `190.89.239.31` (`us31.serverdo.in`), `10.1.1.108` e o
  Tencent (43.156.151.165). **Nenhum IP de leitor, nenhum IP Cloudflare.**
- O host do WordPress é `us65.serverdo.in` (190.89.239.65): **os dois IPs que eu
  chamei de "borda" e que carregam ~93% das linhas são NÓS-IRMÃOS do mesmo
  provedor, não clientes.**
- O `nginx.conf` usa o `log_format main` (combined), **sem `set_real_ip_from` nem
  `$http_cf_connecting_ip`**. Ou seja: **naquele arquivo a atribuição por IP é
  impossível** — o que existe é UA (falsificável).

E existe um segundo log, no mesmo vhost (linha 16/87 do `ocafezinho.com.conf`):
`access.ocafezinho.contador.log` com `log_format contador_ipreal` =
`$http_cf_connecting_ip|$remote_addr|$time_iso8601|$method|$status|$host|$uri|$ua`.
**É ali que o cliente real aparece** (campo 1 = CF connecting IP; campo 2 = o proxy
us404/us31).

Medido hoje nesse log, já com o separador certo: **8.745 IPs reais distintos**,
**45% das requisições com UA de bot/crawler declarado** (24.784 de 55.244), e um
único IP com **4.772 requisições (~8,6% do dia)**.

## Por quê (o erro que eu quase publiquei de novo)

Meu primeiro `awk` no log do contador usou o separador de **espaço** num arquivo
**delimitado por `|`** — o "campo 1" virou a linha inteira e a contagem devolveu
**55.043 "IPs distintos"** contra **8.745 reais**. É a mesma família da 416ª (o
`grep` que somou `x-wp-total` + `x-wp-totalpages`) e da 417ª (linhas do `error.log`
contadas como eventos): **contagem de arquivo ≠ contagem de campo ≠ contagem de
evento.**

## Como aplicar

1. Antes de contar um campo: **descobrir o separador** (`head -1` cru) e conferir a
   contagem contra uma amostra manual.
2. Ao medir impacto de **leitor**, usar o log que tem **IP real**
   (`access.ocafezinho.contador.log`, formato `contador_ipreal`); o
   `access.ocafezinho.com.log` serve para **status/URL/UA**, não para atribuição.
3. Ao reportar audiência, nomear a base: **requisições de crawler não são leitores** —
   e o FAROL, que conta sessão, não herda automaticamente essa limpeza.
4. Regra de ouro que fica: **um número só é publicado com o nome do arquivo, o campo
   e o separador ao lado.**
