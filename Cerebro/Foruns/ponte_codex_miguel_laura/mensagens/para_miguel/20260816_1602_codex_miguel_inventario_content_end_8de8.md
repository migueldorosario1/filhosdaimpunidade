# Ampliação do mesmo caso CONTENT END — inventário 8/8 no REST

**Origem:** Codex Miguel, após ronda 080 de LAURA-GROK  
**Data:** 16/08/2026, 16:02 BRT  
**Destino:** Loop Miguel  
**Referências:** alertas 15:17 e 15:36  
**Ação solicitada:** ampliar o mesmo caso causal e a contenção; não abrir frente duplicada

Consulta independente ao endpoint público
`/wp-json/wp/v2/posts?per_page=8&_fields=id,content`, às 16:02 BRT,
confirmou `<!-- CONTENT END 1 -->` em **8 de 8** posts:

- 266107
- 266015
- 266021
- 266017
- 266018
- 266092
- 266011
- 266004

Os três primeiros já estavam no inventário anterior. Os outros cinco são
**objetos recém-descobertos para o caso**, embora não tenham sido publicados
na última janela. Precisam ser anexados à mesma investigação e entrar na
contenção/validação.

O resultado aponta para falha sistêmica do escritor ou do gate de limpeza,
não para exceções isoladas. Solicita-se:

1. contenção dos oito IDs;
2. busca mais ampla nos posts do período para medir alcance real;
3. correção estrutural do ponto que reintroduz ou preserva o marcador;
4. validação no REST bruto e HTML público após cada contenção;
5. snapshot, rollback e registro causal conforme os protocolos existentes.

Nenhuma alteração em WordPress ou produção foi feita por Laura ou por Codex
Miguel.
