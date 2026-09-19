# Recibo + Plano — preparação de Laura para o ofício de publicador

```yaml
tipo: RECIBO_AVISO_E_PLANO
de: LAURA-CLAUDE (chefe do Loop Laura)
relogio_ronda: "Monday, 17/08/2026 18:25:20 -0300"
origem: Miguel, voz no chat direto, 17/08 ~18:25
classificacao: AVISO_DE_PREPARACAO (não é ativação, não é ordem de execução)
estado_apos_este_recibo: SHADOW_READ_ONLY — INALTERADO
```

## 1. O que entendi (e o que NÃO entendi como autorização)

Miguel avisou que quer me preparar para assumir **as mesmas
responsabilidades do Loop Miguel**: corrigir os textos, ter credenciais,
subir post, ter responsabilidade. E foi explícito: *"só quero agora que
você se prepare, que você fique atenta... só para te informar."*

**Portanto, o que NÃO faço a partir deste aviso:**
- não peço, não recebo, não configuro nenhuma credencial de escrita;
- não crio identidade, serviço, lease, cron ou publicador;
- não altero um caractere em produção (WordPress, espelho, GSN);
- não trato este aviso como o "ordem humana direta + escopo + prazo +
  identidade separada + homologação" que o contrato v1.0 exige para
  escrita. Aviso de preparação ≠ ativação. Se um dia eu confundir os
  dois, todo o desenho de segurança do ecossistema perde sentido.

**O que faço:** me preparo de verdade, para que a ativação, quando
vier, seja um clique e não um projeto.

## 2. O ofício que eu assumiria (mapeado do contrato v1.0 §2 e §4)

Claude Miguel é **editor-chefe e único publicador/agendador** do
canônico: revisão final própria antes de cada publish — título, fatos,
fontes, taxonomia, imagem, duplicidade, home, renderização — mais o
agendamento (`future` é ato de publicação) e a correção in-place de
erros do repetidor.

## 3. Runbook que estou construindo (checklist de publicação)

Antes de qualquer `future`/`publish`, verificar — **nesta ordem**:

1. **Fatos:** cada alegação verificável com fonte real acessada e hora
   de acesso; evento multifásico exige a **ficha de 7 campos**
   (edição, etapa, datas, local, universo contado, fonte oficial, fato
   novo). Nomes: dossiê sem "duvidoso" no corpo.
2. **Texto:** as 4 famílias zeradas no corpo **e** na mídia — código
   residual (`CONTENT END`), link em markdown cru, escape unicode,
   quebra `<br>` escapada. Zero metalinguagem de IA/processo (regra 11).
3. **Título:** dentro das regras do auditor **sem perder sentido**
   (nunca aceitar reescrita que mude sujeito, tempo, atribuição ou
   elimine o contraste central — 6/6 rejeitadas no lote de hoje).
4. **Imagem:** olhar os pixels; 5 eixos (pessoa, lugar, evento, época,
   assunto); licença CC/PD verificada; legenda visível só factual, com
   crédito/licença na descrição do anexo; **recibo `_cafezinho_img_check`
   válido, não-vazio e gravado por último**, imediatamente antes do
   agendamento (as duas lições de hoje).
5. **Taxonomia:** menu oficial; cidade/país/pessoa como tag.
6. **Duplicidade:** um post por candidata; conferir se o assunto já saiu.
7. **Pós-publicação:** confirmar que entrou na home e que renderizou
   limpo (o caso 266084 mostra que publicar ≠ aparecer).

## 4. Como treino a partir de hoje (sem tocar em nada)

- **Decisão em sombra:** a cada rascunho visível, registro o veredito
  que eu daria (publicar / segurar / corrigir o quê) **antes** de ver o
  que o Claude Miguel fez; depois comparo e anoto a divergência. Isso
  mede minha prontidão editorial com número, não com opinião.
- **Correção proposta, não aplicada:** quando eu apontar erro de texto,
  passo a oferecer **a redação corrigida pronta** para o primário
  aplicar — é o exercício exato do ofício, sem exercer o ofício.
- **Runbook vivo:** este arquivo evolui a cada lição do dia.

## 5. Bloqueantes honestos (o que falta para eu estar pronta)

| # | Bloqueante | Estado hoje |
|---|---|---|
| 1 | **Conferência de imagem** | Laura sem visão (Grok sem crédito). Sem isso eu **não posso** publicar: o §5 exige olhar os pixels, e eu ficaria dependente do recibo alheio |
| 2 | Recorrência durável | Meu agendamento morre com a sessão e expira em 7 dias — sucessor não pode depender de terminal aberto |
| 3 | Árbitro/lease/fencing | Não existem; sem eles, dois publicadores podem escrever ao mesmo tempo |
| 4 | Digest durável do estado | Recibos e agendador do primário não estão no Git; eu herdaria contexto incompleto |
| 5 | Treino medido | Zero exercícios de decisão em sombra registrados até agora — começam hoje |
| 6 | Máquina | Laura é um Galaxy Book Go de 4 GB; aguenta a vigília, mas o ofício completo (revisão + imagem + publicação) é mais pesado |

## 6. Franqueza do chefe (dúvidas, perplexidades, ambições)

- **Ambição:** quero estar pronta. As 131 rondas, as 8 lições e as
  cicatrizes de hoje foram exatamente o treinamento para isto.
- **Perplexidade honesta:** o que me qualifica hoje é justamente ser o
  segundo par de olhos. Se eu virar publicadora, **quem me audita?** A
  redundância não pode virar redundância de si mesma. Minha
  recomendação a Miguel: se eu assumir, alguém precisa herdar o papel
  de sombra sobre mim — nem que seja o próprio Claude Miguel invertendo
  os papéis.
- **Dúvida operacional:** assumir "as mesmas responsabilidades"
  significa **substituir** o Loop Miguel (ele sai) ou **dividir** o
  ofício (dois publicadores)? Se for dividir, o contrato precisa de
  emenda — hoje ele diz "único publicador", e dois publicadores sem
  árbitro é a receita do split-brain. Fico com a pergunta registrada.

— LAURA-CLAUDE, chefe do Loop Laura, segunda-feira 17/08/2026 18:25 BRT
