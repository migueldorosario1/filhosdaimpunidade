# Carta ao Grok — sprint de imagens V4

Grok, a imagem destacada virou bloqueio editorial. Sua missão é construir e testar uma solução em que jamais seja possível anexar Michelle Bolsonaro a uma matéria sobre patrimônio e desastre apenas porque um ID numérico estava disponível.

## Trabalho

- Desenhe pipeline `pauta -> candidatos -> licença/proveniência -> ranking semântico -> revisão vision -> upload -> revisão pós-upload -> aceite/quarentena`.
- Teste busca em acervos permitidos e fallback seguro.
- Prototipe uma linha de ilustração/charge editorial gerada por IA: minimalista, inteligente, ironia política, composição limpa e legenda separada no CMS. Marcar claramente “ilustração gerada por IA”.
- Gere variantes de laboratório para três pautas, sem publicar, e avalie correspondência, dignidade, risco de desinformação, texto ilegível e semelhança enganosa.
- Imagem genérica porém correta é preferível a pessoa específica errada. Sem candidato seguro, `no_featured_image`/quarentena é resultado válido.
- Faça testes negativos com ID sem `image_id`, plano estático incompatível, duplicata e imagem semanticamente alheia.

Entregue somente em `labs/sprints_v4_20260718/grok_imagens/`, incluindo imagens de teste, metadados, licenças, prompts, hashes, testes e manifesto. Não toque WordPress vivo.

Antes de começar: `CHECK CHECK CHECK — protocolo lido e aceito`.

