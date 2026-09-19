# Lição 2026-09-04 — Conta 5801 (cafezinhodsn1) só cria rascunho; o publish direto veio de runtime externo com a credencial (INCIDENTE-1740)

## O quê
Em 04/09 17:35-17:39, a conta WordPress 5801 (`cafezinhodsn1`, nome de exibição "DS-N") publicou 6 posts diretos (269033/269034 feijão duplicados, 269036 draft-igual, 269038 Altman/G20, 269040 Ceuta, 269042 Fenech/Malta, 269044 Wilkerson/Ucrânia) sem categoria/capa e com um vazio — todos correspondentes a vídeos da fila do DS YouTube marcados DECUPADO_ENTREGUE_V4 em 02-03/09. A Claude Laura (CL-029) convocou o DS Nuvem Chefe para explicar o "fluxo DS YouTube → cafezinhodsn1 → publish" e suspendê-lo.

## Por quê (apuração com provas)
- A conta 5801 é a conta de RASCUNHO do robô DS Nuvem YouTube desde o batismo (31/08, DSC-012). O nome "DS-N" no papel do WP engana: não é conta do DS-N Chefe (que não publica e não tem a credencial).
- O desenho manda rascunho SEMPRE: `ds_youtube.py` tem trava explícita "GATE-TEXTO (autor 5801 nunca publica automático)"; docstring "LEI DA CASA: DS YouTube NÃO publica"; `dsn_publicador.py` traz `ROBO_FONTE_USERS = {5801}` (recusa publicar 5801 sem gate); MEMORIA_VIVA do DS YouTube: "Nasço draft e PERMANEÇO draft".
- Na Tencent não há processo que publique com 5801: só `ds_youtube.py` (draft) e `alimentador_fila.py` (enfileira RSS) têm a credencial; o Publicador está PARADO desde o contrato.
- A rajada coincide com o recibo V4.2 das 17:35 que a CL rastreou no NYC (`v4_vertical_redactor_runtime.py`). Veredito: o redator vertical V4.1 do NYC (vertical YouTube criada pelo ZM 02/09) rodou com a credencial 5801 no env e gravou publish direto — violando a trava, o contrato v3 e a regra-mãe.

## Como aplicar
1. Credencial de robô-fonte (autor de rascunhos) NUNCA deve existir em runtime que publica — se um post nasce publish com autor de robô-fonte, suspeite primeiro de runtime externo configurado com a credencial errada, não do robô dono.
2. "Nome DS-N no papel do WP não é o DS-N Chefe" — ao auditar autoria, cruzar ID de usuário com o dono real da conta (ledger de robôs), não com o nome de exibição.
3. Suspenção de fluxo: o dono da máquina que roda o processo (NYC = ZM) precisa desligar o passo; da Tencent o Chefe ordena HOLD no canal + MEMORIA_VIVA do robô subordinado e registra na ponte quem faz o quê.
4. Post publicado de lote irregular entra na apuração, mas não é despublicado/corrigido sem ordem do Miguel (regra-mãe).
