# REST de borda mente por ~1-2 min pós-slot — o cache-buster `?cb=` e o WP-CLI como fonte (262ª DS-Dell, 07/09/2026 03:36)

## O quê
Na ronda 262ª (slot 03:30 do feriado), a peça 269305 (Schiller/App Store) disparou às 03:30:00 EM PONTO (41ª execução do colchão). A 1ª leitura REST canônica (`www.ocafezinho.com/wp-json/...`) SEM parâmetro extra, feita às 03:31 (~1 min depois do ar), devolveu:
- volume 3h = 3 (faltava o 269305, que estava na janela);
- per-ID `/posts/269305` → erro (resposta sem `id`), como se o post não existisse.

O WP-CLI no servidor às 03:33 provou: `post_status=publish`, `post_date=2026-09-07 03:30:00`. Refazendo a MESMA leitura REST com um cache-buster (`?cb=21044`), o REST devolveu 3h = 4 e per-ID 200 com `date 03:30:00`.

## Por quê
O REST canônico `www.ocafezinho.com` está atrás de borda/CDN (Cloudflare + cache de aplicação) que serve snapshot por alguns minutos após o disparo — a 1ª resposta pós-slot pode ser o estado anterior (sem o post que acabou de publicar). Não é o site atrasado nem o disparador falho: é a LEITURA pela borda que envelhece. A família de lições «o ar se prova na sonda» (251ª/255ª: status future ≠ evento ≠ ar) tratava de camadas internas (status × cron × REST); agora entrou uma camada NOVA no caminho: o cache da borda entre o REST e o observador.

## Como aplicar
1. Logo após um slot do colchão (minutos seguintes), não confiar na 1ª leitura REST sozinha:
   - se der 0/dígito menor que o esperado ou per-ID com erro, refazer com cache-buster `?cb=<aleatório>` (qualquer query param extra costuma furar o cache de borda);
   - a fonte da verdade do AR é o servidor (WP-CLI `wp post get <ID>` / `wp cron event list`) — quando houver divergência REST × WP-CLI, o WP-CLI decide.
2. Para contagem de volume perto de slot (3h/12h/24h), usar `?cb=` sempre que a leitura ocorrer ≤ ~5 min de um disparo previsto.
3. Registrar a divergência como NOTA DE MÉTODO (não como bug de esteira nem alarme) — o dígito baixo pós-slot com o servidor em publish é cache de borda, não esteira parada.

Arquivo novo da família (adendo às lições 251ª/255ª e ao caderno «agulha se fecha com a sonda»).
