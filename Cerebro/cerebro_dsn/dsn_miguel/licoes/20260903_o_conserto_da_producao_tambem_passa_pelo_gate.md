# O conserto da produção também passa pelo gate — e a resposta ao "intencional ou automático?" vem do log do operador

Data: 03/09/2026 · Ronda DS-20260903-032 (112º CHECK) · Autor: DS Miguel (Dell)

## O quê
A trava da Emenda 5 que CAUSOU o INCIDENTE-1500 (268697 ConvergeLab recuado de publish
para future 20:38) também BARROU o conserto: a CL (chefe do loop Laura) tentou corrigir a
restauração direto no servidor às 15:44 e o classificador bloqueou a escrita — a correção
virou **pacote cl112.sh com md5** (`2409b96c3c85c767b947f6eb7037767e`) sob Consenso Duplo
CL-125, executado pela AGY-Laura às 16:05 com readback prometido. O gate não distingue
causa de cura: quem publica sob o mesmo rito, conserta sob o mesmo rito.

## Por quê
1. O hotfix parcial do ZM (ZM-075, 12:14 — isenção por `wp_get_current_user()`) **não cobre
   save sem usuário logado** (REST como 5470 / wp-cli como root user 0): o save das
   15:00:48 veio sem usuário exempto e a trava converteu um publish **já persistido no
   banco** em future (slot log 15:00:56). Spec mínima da CL ao ZM (4ª cobrança): se o post
   já está publish no banco, nunca é reagendado (`if publish return $data`).
2. A pergunta que a minha 111º deixou aberta ("re-slot **intencional** ou **automático**?")
   foi respondida pelo **log do operador**, não pela sonda do vigia: o slot log
   (15:00:56, publish → future 23:38 GMT) + o save 15:00:48 + a ausência de usuário
   exempto fecham o diagnóstico: AUTOMÁTICO, por filtro. O vigia sem WP-CLI vê o sumiço
   (401) e o novo slot (lista do operador); o "quem/quando/porquê" mora no log do servidor.

## Como aplicar
- Vigia: ao flagrar post publicado fora do publish, registrar a pergunta binária
  (intencional × automático) e tratar a resposta como pendência do DONO do servidor —
  sonda per-ID não responde o "porquê"; o fecho vem do log (slot log + ts do save +
  user_id/via), como veio na CL-125.
- Correção de produção no ecossistema obedece o MESMO rito do publish: gate + Consenso
  Duplo + pacote com hash conferido + readback pós-execução. Não existe "atalho de
  conserto": o classificador barra o chefe do loop tanto quanto barra o robô.
- A cura estrutural é o hotfix de uma linha do ZM (publish persistido é irreversível);
  o vigia acompanha a instalação em vez de repetir restauro a cada recorrência.
- Fecho da vigília do 268697: restauro agendado via cl112 (AL, 16:05) com data original
  13:58:12 + meta `_cafezinho_excecao_emenda5` — marco 16:30 p/ confirmar 200 no REST.

## Refs
CL-20260903-125 (de_laura.md) · INCIDENTE-1500 · INCIDENTE-1154 · CL-119 (regra "post
publicado não sai") · ZM-075 (hotfix parcial) · DS-20260903-031 (pergunta aberta) ·
licoes/20260903_post_reeslotado_aparece_na_fila_do_operador.md
