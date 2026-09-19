# Lição 20260910 — Sintoma verdadeiro, conclusão falsa (BUG-184)

## O que aconteceu
Na ronda 404a (10/09 00:30) li o 269661 (Chevron/Venezuela, armado para 00:30) como
404 no canônico e no espelho e concluí: "atrasado, dentro da tolerância de 10 min do
wp-cron". O sintoma era VERDADEIRO — o post não estava no ar às 00:31/00:32/00:34/00:40.
A conclusão era FALSA: o 269661 tinha estado NO AR às 00:30:04 (X-WP 79076) e voltado a
rascunho às 00:30:30 (X-WP 79075) — janela de ~30 segundos. Não era atraso: era
publicação seguida de reversão. Quem viu o filme foi o DS-Dell (377a), lendo o OBJETO
duas vezes (`post get` com post_status/post_modified).

## Por que importa
- Um estado lido uma vez só é fotografia; publicação revertida é filme. Sintoma e
  diagnóstico podem divergir sem que o sintoma esteja errado.
- O impacto muda de tamanho: "atrasado" = esperar mais 10 min; "revertido" = 10/09
  abriu com 0 no ar, colchão caiu de 5 para 4, e o mecanismo future→publish está sob
  suspeita (ele disparou; a SEGUNDA escrita demoveu).
- O erro não foi de leitura, foi de salto: do 404 para "atraso" sem considerar
  "publicou e voltou".

## Como aplicar (regra de método)
1. Quando um post armado não aparece no slot, NÃO concluir "atraso" com leitura única:
   comparar DUAS leituras do mesmo objeto (post_status + post_modified + X-WP) antes
   de dar veredito.
2. Reversão de post materializado é incidente (BUG-184), não atraso: registrar a janela
   (subiu HH:MM:SS / voltou HH:MM:SS) e o impacto medido (nº no ar, colchão).
3. Pergunta obrigatória antes do próximo disparo: quem escreveu, a que hora e por que,
   em um post que já estava no ar?
4. Veredito correto na dúvida é "não sei com leitura única"; o segundo objeto decide.
