# Alerta editorial e de metalinguagem — post 266021

**Origem:** Codex Miguel, após rechecagem da ronda 078 de LAURA-GROK  
**Data:** 16/08/2026, 15:04 BRT  
**Destino:** Loop Miguel  
**Ação solicitada:** revisão editorial; nenhuma ação automática em produção

O post público **266021**, “Augusto Cury declara maior patrimônio entre
presidenciáveis”, apresenta dois pontos verificáveis:

1. **Recorte não explicado:** o texto afirma que Cury lidera entre os
   presidenciáveis que registraram candidatura. O G1 informa que Pablo Marçal
   registrou candidatura no TSE e declarou R$ 7,4 bilhões, embora esteja
   inelegível até 2032. Se o ranking pretende excluir candidaturas inelegíveis
   ou sem viabilidade jurídica, essa condição precisa estar explícita; do modo
   atual, título, lead e metadescrição podem induzir a uma conclusão ampla
   demais.
2. **Marcador interno no REST público:** o campo `content.rendered` de
   `https://www.ocafezinho.com/wp-json/wp/v2/posts/266021` expõe
   `<!-- CONTENT END 1 -->`. O comentário não aparece visualmente no HTML
   final, mas está publicamente acessível pela API.

Evidência consultada:

- REST público do próprio post, em 16/08/2026 às 15:04 BRT;
- G1 de 15/08/2026: Marçal registrou candidatura, declarou R$ 7,4 bilhões e
  está inelegível até 2032.

Solicitação ao Loop Miguel:

- revisar título, lead e metadescrição ou explicitar o critério de exclusão;
- remover o marcador interno usando o procedimento seguro habitual, se
  confirmado;
- registrar a decisão e a validação pós-correção.

Laura não deve editar, publicar, excluir nem alterar o post.
