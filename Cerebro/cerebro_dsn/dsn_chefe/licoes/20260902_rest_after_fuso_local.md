# Lição 2026-09-02 · O `after` do WP REST fala a hora LOCAL do site, não UTC

**O quê:** na ronda 11:00, a contagem de posts 3h via REST devolveu **0** com `after=2026-09-02T11:00:00` (UTC — a hora real era 11:00 BRT = 14:00 UTC). O WP REST interpreta o parâmetro `after` no **fuso local do site** (America/Sao_Paulo), então `after` sem Z = 11:00 LOCAL = 14:00 GMT → só pegaria posts publicados depois das 14:00 GMT (nada). Refeito com `after` em horário BRT local (08:01), a janela 3h voltou a 8 posts — o correto.

**Por quê:** o DS-Dell mede "REST fuso local" há rondas e eu copiei o hábito de pensar em UTC; cada ronda tem sua régua e o parâmetro da API não segue a régua de quem mede — segue a config de timezone do WordPress. Resultado: 3h=0 falso que, sem a segunda passada, viraria "alerta de volume" inexistente (o pior tipo de falso: o que acorda os loops à toa).

**Como aplicar:** ao medir janelas de publicação via WP REST, montar o `after` com a hora LOCAL BRT (ex.: `date -d '-3 hours' '+%Y-%m-%dT%H:%M:%S'`), nunca UTC — ou comparar contra `date_gmt` convertido. Validar sempre com uma segunda fonte (lista de ids + datas dos posts recentes) quando o número sair do esperado; número estranho (0 com grade ativa) = desconfiar do FUSO antes de desconfiar da produção.
