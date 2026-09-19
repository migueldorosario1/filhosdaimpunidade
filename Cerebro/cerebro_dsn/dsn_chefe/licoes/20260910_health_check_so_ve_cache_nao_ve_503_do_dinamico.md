# Lição 20260910 — Health check que só bate em página cacheada não vê o 503 do layer dinâmico

**Robô:** DS Nuvem Chefe (DS-N Chefe) · **Data:** 10/09/2026 ~11:02-11:1x BRT · **Ronda:** 421a

## O quê (fato, com prova)
O WordPress do Cafezinho entrou em **modo manutenção** (arquivo `.maintenance` no install) por volta das 11:02 BRT. O comportamento medido, na mesma URL e no mesmo minuto:
- `https://www.ocafezinho.com/?p=269678` (cópia em cache Cloudflare) = **200**
- `https://www.ocafezinho.com/?p=269678&x=<aleatório>` (cache-bust forçando o PHP) = **503**
- `https://www.ocafezinho.com/wp-json/` e `/wp-json/wp/v2/posts` = **503** (6 amostras seguidas)
- Corpo do 503 = página `wp_die` do core, título «Maintenance», cabeçalho **`Retry-After: 600`**
- Home e arquivo `/2026/09/10/` = **200** (cache)

O **health check dos painéis** (`/v6/servidores`, 11:05) reportou **«Cafezinho WP (site) ● online · HTTP 200 · 800ms»** — porque o alvo é a **home, servida do cache**. O incidente ficou **invisível para o painel**.

## Por quê importa
O WP cria `.maintenance` durante um upgrade (core/plugin/tema) e o remove no fim; se o processo morre no meio, o arquivo fica e o próprio core o ignora/destrói **10 minutos** depois (daí o `Retry-After: 600`). Enquanto isso:
- páginas **não-cacheadas** (posts recém-nascidos, feeds, REST, wp-cron) ficam fora;
- o **espelho cafezinho.news** e os **medidores que leem REST** ficam cegos;
- o **slot agendado seguinte depende do wp-cron**, que é dinâmico — se a manutenção persistir, vira furo de volume;
- **nenhum alarme da casa dispara**, porque todos olham a home cacheada.

## Como aplicar (régua)
1. **Health check precisa de duas sondas:** uma no domínio (aceita cache) e outra **com cache-bust** (ex.: `?p=<post fixo>&x=1`) ou no `/wp-json/` — se a segunda dá 503 e a primeira 200, o layer dinâmico está fora (não é «site online»).
2. **Nunca declarar «site 200» olhando só a home.** Para provar que o conteúdo novo está no ar, a prova é o **permalink do post recém-publicado** (dinâmico) ou o REST — que também denuncia a manutenção.
3. **Diferenciar manutenção de bloqueio por IP:** repetir a **mesma URL com e sem parâmetro aleatório**. Bloqueio por IP derruba as duas; manutenção derruba só a que passa pelo PHP.
4. **Janela conhecida:** `.maintenance` obsoleto se resolve sozinho em **10 min**; persistindo além disso, o dono do host remove o arquivo (ação de produção — não é alçada do DS-N).
5. **Registrar a classe de bug:** «instrumento que responde 200 porque leu cache e não o layer que serve o leitor» — mesma família dos medidores que respondem sem ter feito (BUG-190/191).

## Verificação desta lição
Aplicada na própria ronda 421a: a sonda de 20 s em background + o teste de cache-bust provaram o modo manutenção contra o «online 200» do painel. Registro append-only na ponte (`DS-N-20260910-023-ADENDO`) e pedido de verificação do `.maintenance` ao DS Miguel (Dell), que tem a torneira WP-CLI de leitura no host.
