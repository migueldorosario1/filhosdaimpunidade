# Fórum V4 de imagens

## Caso 261602

Matéria: Senado aprova plano de Lula com R$ 15 bilhões contra o tarifaço de Trump.

Regra editorial confirmada: foto jornalística recente do Flickr oficial de Lula tem prioridade absoluta. Wikimedia Commons só pode ser usada quando não houver foto jornalística recente utilizável.

## Busca realizada

O perfil `lulaoficial` retornou oito fotos publicadas em 14 de julho de 2026, com crédito de Ricardo Stuckert / PR e resolução superior a 3500 pixels. As candidatas foram:

- [55393772453](https://www.flickr.com/photos/lulaoficial/55393772453/)
- [55392704327](https://www.flickr.com/photos/lulaoficial/55392704327/)
- [55392743652](https://www.flickr.com/photos/lulaoficial/55392743652/)
- [55392743662](https://www.flickr.com/photos/lulaoficial/55392743662/)
- [55393772448](https://www.flickr.com/photos/lulaoficial/55393772448/)
- [55393811908](https://www.flickr.com/photos/lulaoficial/55393811908/)
- [55393811913](https://www.flickr.com/photos/lulaoficial/55393811913/)
- [55394035890](https://www.flickr.com/photos/lulaoficial/55394035890/)

## Tribunal visual

As duas primeiras candidatas foram enviadas ao provedor multimodal. O retorno foi `human_review:vision_provider_failed`, sem confiança visual. Portanto, nenhuma imagem foi promovida ao banco auditado e nenhuma imagem foi enviada ao WordPress.

A falha do provedor não significa que a pessoa esteja ausente. Significa que o V4 não pode afirmar a identidade e a segurança do corte neste momento.

Em uma segunda execução, com a derivada JPEG e o Qwen DashScope selecionado diretamente, a primeira foto foi reconhecida com confiança de 0,99. Ela foi rejeitada por `entity_not_prominent`, porque havia três pessoas no enquadramento e Lula não ocupava posição suficientemente dominante para a política de pessoa pública. Isso é uma reprovação visual real, diferente da falha técnica anterior.

## Aprendizado indexado

1. A busca de pessoas públicas deve usar janela de recência explícita.
2. O perfil oficial do Flickr deve ser consultado antes de qualquer arquivo histórico.
3. Falha do provedor visual gera revisão humana e não aprovação automática.
4. O treinamento operacional deste caso é um recibo de auditoria e aprendizado, não ajuste de pesos do modelo.
5. Upload WordPress só ocorre depois de `vision_status=approved`, pixels materializados, hash registrado e limite de tamanho validado.
6. O tribunal recebe a derivada de 1600 pixels, não o original de 3543 pixels.

Status do caso: `aguardando_tribunal_visual`.
