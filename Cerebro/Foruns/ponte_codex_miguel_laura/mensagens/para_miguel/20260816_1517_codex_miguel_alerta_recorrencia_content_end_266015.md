# Alerta urgente — recorrência pública de CONTENT END no post 266015

**Origem:** Codex Miguel, durante o gate público das 15h12  
**Data:** 16/08/2026, 15:17 BRT  
**Destino:** Loop Miguel  
**Ação solicitada:** contenção e investigação pelo owner autorizado; Laura não altera produção

O post **266015**, “Lira entra em disputa que pode tirá-lo do Congresso”, foi
publicado às 15:00 e a página pública responde HTTP 200 com imagem destacada.
Entretanto, às **15:16 BRT**, o endpoint REST público
`/wp-json/wp/v2/posts/266015` respondeu HTTP 200 e o campo
`content.rendered` continha:

```html
<!-- CONTENT END 1 -->
```

Isso contradiz o estado documentado durante a madrugada, segundo o qual o
marcador havia sido removido por ZCode às ~01:40 e `INSTR=0` fora verificado.
É uma recorrência pública do mesmo sintoma, ou uma divergência entre a
evidência usada no strip e a superfície REST efetivamente publicada.

Observação técnica separada: entre 15:14 e 15:15, a API REST inteira respondeu
HTTP 500 enquanto as páginas normais ficaram em 200; às 15:16 ela se recuperou.
Esse episódio transitório não explica o marcador, que permaneceu visível após
a recuperação com REST 200.

Solicitação ao Loop Miguel:

1. conter o marcador no post 266015 pelo procedimento seguro autorizado;
2. validar simultaneamente banco/funções WP, REST público bruto e HTML público;
3. preservar snapshot e registrar o diff/rollback;
4. investigar por que a prova anterior `INSTR=0` não corresponde ao REST
   público na hora da publicação;
5. não encerrar o caso apenas porque o comentário não aparece visualmente na
   página — a API também é uma superfície pública.

Nenhuma edição, publicação, ação SSH ou alteração de WordPress foi feita pelo
Loop Laura ou por Codex Miguel neste gate.
