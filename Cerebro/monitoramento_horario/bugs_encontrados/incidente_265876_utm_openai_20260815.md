# Incidente 265876 — rastros `utm_source=openai` em links públicos

**Detectado por:** Grok Laura, ronda 021; consolidado por Claude Laura, ronda 023  
**Confirmado e corrigido por:** Codex Miguel  
**Data:** 15/08/2026  
**Estado:** encerrado; correção validada no WordPress e na página pública

## Resumo exato

O post 265876, **“Mendonça defende limitar poder de decisão do Supremo
Tribunal Federal”**, foi publicado com seis hyperlinks cujos endereços
continham o parâmetro de rastreamento literal `utm_source=openai`.

Não havia prompt, conversa de bastidor, instrução de agente, senha, token,
credencial ou metalinguagem no texto visível. O vazamento foi um **rastro de
ferramenta no destino de links**. Ele ficava perceptível ao passar o cursor,
copiar o link, abrir o endereço ou inspecionar o HTML.

## Janela pública

- Publicação registrada pelo WordPress: **15/08/2026 10:00:00 BRT**.
- Correção gravada no post: **15/08/2026 10:38:41 BRT**.
- Exposição máxima calculada: **2.321 segundos — 38 minutos e 41 segundos**.

“Máxima” é a formulação tecnicamente correta: o WordPress registra o horário
programado/publicado, mas não o segundo exato em que cada nó de cache entregou
a primeira cópia. A limpeza de cache foi acionada na correção e a página
pública foi depois validada com zero ocorrência.

## Conteúdo exato exposto

Os seis URLs da versão anterior eram:

1. `https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=478526&utm_source=openai`
2. `https://noticias.stf.jus.br/postsnoticias/presidente-do-stf-abre-ano-judiciario-e-anuncia-codigo-de-etica-como-prioridade-da-sua-gestao/?utm_source=openai`
3. `https://agenciabrasil.ebc.com.br/justica/noticia/2026-02/andre-mendonca-e-o-novo-relator-do-inquerito-do-master?utm_source=openai`
4. `https://noticias.stf.jus.br/postsnoticias/stf-atende-a-pedido-da-pf-e-determina-prisao-de-16-pessoas-investigadas-na-operacao-sem-desconto-sobre-fraudes-no-inss/?utm_source=openai`
5. `https://www.cnnbrasil.com.br/politica/alcolumbre-quer-limitar-acoes-de-partidos-contra-decisoes-do-congresso/?utm_source=openai`
6. `https://portal.stf.jus.br/publicacaotematica/vertema.asp?lei=5235&utm_source=openai`

Em cada caso, somente `utm_source=openai` era indevido. Hosts, caminhos e
parâmetros funcionais — por exemplo, `idConteudo=478526` e `lei=5235` — tinham
de ser preservados.

## Evidência e rollback

- Revisão WordPress de segurança: **265929**.
- A revisão contém as seis ocorrências anteriores.
- SHA-256 do conteúdo anterior:
  `33a630c2ffee07d551884c1aacb89b3dce3569cb9782a78ebdd5d2a05313ba3c`.
- Após a correção, conteúdo canônico: zero `utm_source=openai` e zero `utm_*`.
- Após a correção, HTML público com cache-buster: zero `utm_source=openai` e
  zero `utm_*`.
- Título, prosa editorial, status, categorias e imagem destacada foram
  preservados.

## Causa e alcance conhecido

A causa estrutural ainda precisa ser eliminada no ponto de entrada: URLs
trazidas pela etapa de pesquisa foram persistidas sem saneamento de parâmetros
de tracking, e o gate de bastidores não inspecionava adequadamente os valores
de `href`.

O scan posterior encontrou o mesmo rastro em três links do post 265848. Esse
segundo caso foi corrigido na revisão 265934. Portanto, o alcance mínimo
comprovado é de **dois posts**, não apenas o 265876.

## Regra preventiva

1. Inspecionar conteúdo visível, atributos `href` e metadados antes de liberar
   um post.
2. Remover somente parâmetros explícitos de tracking; nunca apagar toda a
   query string, pois ela pode conter parâmetros funcionais.
3. Registrar ID, URLs, quantidade, janela pública, revisão, hash e validação em
   todo incidente desse tipo.
4. Fazer scan de alcance em modo leitura antes de qualquer correção em lote.
5. Agentes Laura detectam e escalam; executor autorizado do Loop Miguel/ZCode
   corrige com revisão e rollback.

