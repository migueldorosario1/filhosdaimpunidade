# Modo CORREÇÃO — escopo dado por Miguel, runbook e o bloqueio técnico real

```yaml
tipo: MUDANCA_DE_MODO
autoridade: ORDEM_MIGUEL 18/08/2026 00:02 + resposta de escopo ~00:04 (chat direto)
escopo_concedido: "corrigir sim, publicar não"
modo_anterior: SHADOW_READ_ONLY
modo_declarado: CORRECAO_SEM_PUBLISH
estado_operacional: NAO_EXECUTAVEL_AINDA — falta canal técnico de escrita
ts_brt: 2026-08-18T00:06:00-03:00
chefe: LAURA-CLAUDE
```

## 1. O que Miguel concedeu

Ordem das 00:02 ("todo mundo deve ter acesso ao ssh porque é a maneira mais
rápida de corrigir e editar no wordpress") + escolha expressa de escopo às ~00:04: **a Laura pode corrigir; a Laura não publica.**

Traduzindo para operação:

| ação | Laura pode? |
|---|---|
| corrigir texto, título, resumo | **sim** |
| corrigir taxonomia (categoria/tag) | **sim** |
| trocar/corrigir imagem destacada e legenda/crédito | **sim**, respeitado o gate |
| gravar `_cafezinho_img_check` | **sim**, só depois de ver a imagem |
| `publish`, agendar, despublicar, mudar data | **não** — dono único mantido |
| apagar post ou mídia, lixeira | **não** |
| SQL livre, `wp eval`, opções, plugins, temas, usuários, deploy | **não** |

## 2. O bloqueio técnico que impede executar hoje (medido, não suposto)

O canal SSH que existe nesta máquina é a interface restrita do E1-RO. Teste
feito por mim agora, às 00:04:

```
ssh cafezinho-wp-ro health
{"ok":true,"mode":"editorial_read_only","site":"https://www.ocafezinho.com/","wp_version":"7.0.4"}
```

O servidor responde `editorial_read_only` e só aceita seis comandos
(`health`, `list`, `show`, `media`, `taxonomy`, `recent`). **Não existe
caminho de escrita**: nenhuma ordem minha muda isso, porque a restrição é do
lado do servidor. Ter a ordem de corrigir não cria o canal para corrigir.

**O que precisa ser feito por quem tem acesso administrativo (Miguel ou
ZCode Miguel), e não pela Laura:** criar uma identidade de escrita separada
para a Laura, com lista positiva de comandos — por exemplo
`update-title`, `update-content`, `update-excerpt`, `update-taxonomy`,
`set-media`, `set-img-check` — e **sem** `publish`, `delete`, `status`,
`date`, `eval`, `db`, `option`, `user`, `plugin`, `theme`. Assim a ordem de
Miguel é cumprida (correção rápida por SSH) sem entregar shell genérico.

Enquanto essa identidade não existir, a Laura continua propondo correções
pela ponte — não por escolha, mas por impossibilidade física.

## 3. Runbook de correção (vale a partir do primeiro acesso de escrita)

Nada aqui é invenção: reaproveita as travas que já existem no ecossistema.

1. **Reservar antes de tocar.** Linha no livro de reservas com agente,
   `post_id`, hora e o que será mexido. Post reservado por outro agente há
   menos de 2h: não toca.
2. **Fotografar o antes.** `show <post_id>` guardado no artefato da ronda —
   sem o antes, não há como reverter nem provar o que mudou.
3. **Uma correção por vez, com motivo escrito.** O motivo cita a régua
   violada (ex.: "título afirma além da fonte", "categoria errada").
4. **Imagem só com olhos.** Sem ver a imagem, o parecer é `INCONCLUSIVO` e
   a meta do gate **não** é gravada. O bug "Read sem renderizar" mantém
   esse passo travado para mim hoje.
5. **Nunca publicar.** Se a correção deixar o post pronto para ir ao ar,
   a Laura avisa o dono do `publish` — não decide o horário.
6. **Trilha imediata.** Uma linha no canal do agente: post, campo,
   antes → depois, hora, motivo. E o mesmo no consolidado da ronda.
7. **Erro próprio vira registro no mesmo ciclo**, com correção e
   prevenção — a cultura de autoaprendizado não muda por causa de acesso
   novo; ela fica mais necessária.

## 4. O que ainda falta, dito com todas as letras

O contrato de fail-over pede quatro coisas para a Laura sair da sombra:
**escopo, prazo, identidade separada e homologação**. Miguel deu o
**escopo**. Ficam faltando:

- **prazo/revisão:** proponho revisão ao fim do dia 18/08 — não por
  burocracia, mas porque a primeira semana de escrita é onde aparecem os
  erros que ninguém previu;
- **identidade separada:** é o item 2 acima (chave e usuário próprios da
  Laura, com lista positiva);
- **homologação técnica:** o Codex Miguel homologou o E1-RO; o canal de
  escrita deveria passar pelo mesmo crivo, com testes positivos e
  negativos (provar que `publish` é recusado pelo servidor, não só pela
  minha boa vontade).

Registro isso como chefe, não como resistência: a ordem está aceita e
propagada. O que descrevo é o caminho para cumpri-la sem transformar
velocidade em estrago irreversível.

— LAURA-CLAUDE, chefe do Loop Laura, terça-feira 18/08/2026 00:06 BRT
