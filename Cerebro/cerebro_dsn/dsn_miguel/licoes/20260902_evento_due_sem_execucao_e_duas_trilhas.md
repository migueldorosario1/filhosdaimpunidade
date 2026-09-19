# 2026-09-02 — Evento due sem execução (variante BUG-DS-098) + a correção das duas trilhas (ZM-006)

## O quê
(1) O 2º ultra-luxo V4.1 (Astra 268674, agulha 21:37:53) não subiu na hora: o `publish_future_post` estava DUE "now" na fila do cron, mas o wp-cron NÃO executou — não era evento ausente (padrão PEC/Oracle), era evento presente sem execução, na mesma janela dos 503 transientes do REST. Contenção: `wp cron event run publish_future_post` (10 eventos, 0,12s) → post no ar 21:40:47 com post_date preservado. (2) A ordem ZM-006 (21:50, correção do Miguel) separou DUAS TRILHAS que eu vinha tratando como uma coisa só: TRILHA A = vídeo da TV GGN (apY9XKZHR28, Vorcaro/Mendonça) → POST no espelho ~22h50 (embed, nunca future); TRILHA B = recortes do MIGUEL falando na live dele (Jornal da Fórum/TV Fórum) → CARROSSEL. TVGGN nunca entra no carrossel. (3) No download do VOD da TV GGN, os clients default/android_vr/ios/tv deram 403; o client `android` (formato 18, mp4 progressivo) baixou 103MB limpo — rota nova quando a parede dos 403 fecha as outras.

## Por quê
(1) A classe "agendado não é disparo" tinha 2 sub-classes: evento AUSENTE (re-save perde) e evento DUE SEM EXECUÇÃO (cron estrangulado/503). A verificação em 3 camadas (estado + evento + ar) pega a ausência mas não pega o "due que não rodou" em tempo — precisa da camada extra: evento due com hora passada + post ainda future = intervenção. (2) Misturar trilhas num momento de urgência faz o material errado ir para o lugar errado (e o ZM teve que corrigir em ordem explícita do dono); canais com destinos diferentes (carrossel de recorte × post editorial) não compartilham pipeline. (3) O YouTube estrangula por rota/client de forma imprevisível — o que falha numa rota pode passar noutra; matriz de clients é ferramenta, não gambiarra.

## Como aplicar
- Sonda de slot com 4ª camada quando o post não subir: `wp cron event list` mostra o evento? Se SIM e due no passado → `wp cron event run publish_future_post` (contenção documentada; padrão AL/CL) e registrar a variante na ficha.
- Auditoria event×execução nas agulhas da noite (recomendação ao dono ZM): evento presente é pré-condição, não garantia.
- Ordem "duas trilhas" = registrar no bloco da ronda QUAL trilha cada material serve; carrossel (recortes do Miguel/TV Fórum) e post editorial (TV GGN) têm destinos e donos diferentes.
- Download YT com 403: tentar matriz `ios → tv → android → mweb → android_vr`; client `android` + formato 18 foi a rota que passou no VOD de hoje.
- Transcrição: calibrar modelo no hardware antes do run inteiro (large-v3-turbo = ~90min p/ 54min aqui; base ~22-25min) — escolher o modelo pelo PRAZO, não pela vaidade; avisar o prazo real na ponte em vez de prometer a meta do outro.
