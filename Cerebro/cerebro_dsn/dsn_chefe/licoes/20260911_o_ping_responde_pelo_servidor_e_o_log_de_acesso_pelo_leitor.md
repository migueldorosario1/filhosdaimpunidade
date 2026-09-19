# LIÇÃO — 2026-09-11: o `ping` responde pelo servidor, o log de acesso responde pelo leitor — e 404 não é 500 (ronda 447ª, adendo ao BUG-208)

## O quê
O BUG-20260911-DS-208 (DS-Dell, 02:15) provou que o object cache do us65 **falha fechado**
e entrega `wp_die()` ao leitor. Duas armadilhas de leitura apareceram juntas na mesma
madrugada e valem régua própria:

1. **`redis-cli ping = PONG` não é prova de saúde.** O Dell colheu `ping` em 0,00 s cinco
   vezes **enquanto** o `MGET` do PHP morria na mesma máquina. O `ping` responde **pelo
   servidor**; o dano mora no **caminho do cliente** (conexão sob carga, fork/COW sob swap).
2. **404 e 500 se parecem numa lista e são diagnósticos opostos.** Na minha sonda externa
   das 02:36-02:42, o único não-200 foi `/tag/japan/feed` = **404** — **feed de tag que eu
   mesmo montei e que não existe** (`/tag/` dá 404 neste site). A **mesma URL** aparece na
   lista de "URLs derrubadas" do bloco do Dell, onde os erros eram **500/503 de cache
   morto**. Se eu tivesse somado as duas coisas, teria "confirmado" 136 erros que não medi.

## Por quê
- Saúde de dependência compartilhada se mede **no mesmo caminho em que o cliente falha**,
  não no canal de controle: o canal de controle pode estar saudável enquanto o dado não passa.
- Log de aplicação conta **metade** da história; a outra metade está no **log de acesso de
  quem foi derrubado** (foi o `grep` que faltava desde 31/08, quando o caso foi arquivado
  como "ruído transitório do WP-CLI").
- Código HTTP não é "erro" genérico: **404 = o objeto não existe; 500/503 = o objeto
  existe e o servidor não conseguiu entregá-lo**. Somar os dois infla o laudo e aponta o
  dono errado.

## Como aplicar
1. Antes de declarar dependência saudável, medir pelo caminho do cliente (uma escrita/leitura
   real) **e** pelo canal de controle — e declarar qual dos dois falhou.
2. Ao herdar lista de URLs "com erro", **separar por classe de status** antes de contar:
   4xx é conteúdo/rota, 5xx é infraestrutura. Contar junto é falso positivo com cara de prova.
3. URL da lista de outro agente **se reexecuta** (curl próprio, mesmo minuto) antes de
   entrar no meu laudo: às vezes o "erro" é o slug.
4. Medir o que a física alcança **e escrever o não-medido**: do meu lado não há nginx de
   us65 — a sonda externa prova que a janela fechou **de fora**, não prova ausência do defeito.

## Verificação
Ronda 447ª: 26 requisições (25 × 200, 1 × 404 de slug inexistente, 0 × 5xx) + `/wp-json/` e
`/wp-json/wp/v2/posts` = 200 + 269758 no ar às 02:30:00 (X-WP 79110 → 79111). Registro no
adendo ao BUG-208 (`CEREBRO_NODE_BUGS_ATIVOS.md`) e no bloco DS-N-20260911-006. Lição irmã,
do dono da prova: `cerebro/cerebro_dsn/dsn_miguel/licoes/20260911_o_ruido_era_o_incidente.md`.
