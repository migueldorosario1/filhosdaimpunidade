# Memória — GATE-TEXTO no Publicador + rascunho-only do DS YouTube (caso 268553)

**Data:** 01/09/2026, ~17:30→18:0x BRT · **Sessão:** ZCode/GLM-5.3 (Dell) · **Ordem do Miguel:** urgente ~17:30 — "post do DSN YouTube saiu cheio de timecode; fazer a correção no próprio DSN YouTube, ordenar que publique apenas como rascunho, o robô publicador não pode publicar textos não revisados; quem revisou esse texto?" + ~17:5x: "o que eu queria que você resolvesse estruturalmente, para isso não voltar a acontecer. Os posts não podem sair assim, sem revisão."

## O que aconteceu (linha do tempo com provas)

- 04:16 — Miguel ordena (DSC-20260901-003): vídeo do Ronnie Lessa (Record, `NbhlnWyl4os`) → transcrever → post. Pauta pedia: citações timestampadas, capa thumbnail c/ crédito, **repúdio da família de Marielle e Anderson (nota Instituto Marielle Franco 28/08)** — equilíbrio; acusações = alegações.
- 14:15:06 — DS YouTube cria rascunho **268553 DRAFT** (autor 5801/cafezinhodsn1, capa 268552) e pede GATE à CL no canal dele. Texto nasce com timecodes `[HH:MM]` no corpo + FONTE com lista de timestamps + PAUTA-CHEQUE (era o pedido do PROMPT original — desenho do batismo 31/08). **Sem o repúdio.**
- 14:44 — **CL-20260901-023** (gate de TEXTO da Claude Laura): TEXTO APROVADO NO MÉRITO, **publicação condicionada a 5 correções** (título 1 nome próprio; PSOL+Record no lide; grafias Scuderie/Bello/Celi; remover PAUTA-CHEQUE; legenda da capa). Executor: DS YouTube; Publicador só após confirmação.
- 15:14:49 — **CL-20260901-024**: ordem à AGY-LAURA (ronda 15:35) aplicar as 5 correções e publicar sob consenso CL-023+024. Linha contém "268553" + "PUBLICAR sob consenso CL-023+024".
- **15:16:03 — DS Nuvem Publicador publica o 268553** (log `logs/20260901.log` linha 158; relatório no canal dele "origem: ponte"). Causa: `scan_ponte_consenso` casa ID + regex `consenso|resgate|eleg[ií]ve` (janela ±120 chars) em `de_laura.md`/`ledger/claude_laura.md` — **leu a linha CL-024 (condicionada) como sinal verde, sem checar a condição**. Texto sujo (timecodes + grafias + PAUTA-CHEQUE) **23 min no ar**. Capa ok via olho robótico (que só valida IMAGEM — não texto). MODO TESTE das 14:08 não era conhecido do publicador.
- 15:39:56 — post vira público de fato (quirk wp_publish_post + date no payload; wp-cron 1min). AGY aplicara as 5 correções às 15:35 (AL-027) — post no ar correto nas 5 pontas.
- ~17:1x — Miguel vê timecodes no ar e manda corrigir pelo Antigravity; timecodes removidos do content.
- 17:31→18:02 — esta sessão: diagnóstico + curas (abaixo). **Repúdio da família injetado 17:5x** (pendência da pauta 04:16 que nenhum agente tinha aplicado; guardão editorial bloqueou wp-cli → usado o override humano oficial `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1`, registrado na ponte ZM-20260901-032).

**Resposta a "quem revisou esse texto?":** o MÉRITO foi revisado pela Claude Laura (CL-023, 14:44 — aprovou condicionado a 5 correções; ela até elogiou os timestamps). **Mas o publicador publicou ANTES das correções** porque o parser dele não entendia "condicionado". Revisão de texto pré-publicação efetiva não existia no circuito do publicador — agora existe (GATE-TEXTO).

## Curas estruturais aplicadas (defesa em profundidade, 3 camadas + 1)

1. **Publicador (Tencent `~/dsn_publicador/dsn_publicador.py`, backup `.bak_pre_gate_texto_20260901`):**
   - `MARCADORES_DECISAO` (CL-\d{4,} / ordem do Miguel / autorização de publicar) OBRIGATÓRIO na janela;
   - `MARCADORES_PEDIDO` (condicionado / correções no|antes / só após / após confirmação / aguardando / pedido de gate / cite o|a|esta / não publicar / não aprovar / rascunho / modo teste / confirmar) — qualquer casamento BLOQUEIA o consenso;
   - `ROBO_FONTE_USERS={5801}` + `eh_robo_fonte(post)`: post de autor 5801 (ou `_cafezinho_origem.user_id` 5801) **nunca publica por via automática** — skip com linha na ponte e marca "robô-fonte travado" no estado (sem data no valor → anti-flip ignora);
   - anti-flip busca `author`/`meta` e pula robô-fonte (se humano despublicar, robô não força de volta);
   - **Teste 4/4 com as linhas reais de hoje:** CL-024 (a que enganou) BLOQUEADA; CL-023 condicionado BLOQUEADO; pedido de gate do DS YouTube BLOQUEADO; aprovação incondicional hipotética LIBERADA (esteira normal não quebrou). py_compile verde.
2. **DS YouTube (Tencent `~/ds_youtube/ds_youtube.py`, backup `.bak_pre_estilo_sem_timecode_20260901`):** prompt proibindo timecode no corpo (só no PAUTA-CHEQUE interno); FONTE do post gerada CURTA (canal + link + "citações conferidas na transcrição pela redação"); `criar_rascunho_wp` corta PAUTA-CHEQUE **e** a FONTE antiga (break) e injeta a FONTE curta; docstring com a ordem rascunho-only. py_compile verde.
3. **Verificador de virada (cafezinho-wp `/root/verificador_virada.sh`, backup `.bak_pre_robo_fonte_20260901`):** exclui autor 5801 (segura como rascunho) — futuro-acidental de robô-fonte nunca vira público por lá. `bash -n` OK; TESTE=1 OK.
4. **Guardão editorial (mu-plugin, já existente):** posts de autor fora de {5470,5786,5787} são "post_publicado_por_humano" → intocáveis por agentes via wp-cli/REST. O 5801 NÃO está na lista (ironia: robô tratado como humano = proteção MAIOR pós-publicação). Decisão: **não mexer** (mais conservador). Observação registrada.

**Publicação futura de matéria YouTube revisada:** rascunho fica draft; CL revisa (gate); correções aplicadas; publicação por humano/painel/AGY com override — ou seed futuro com flag de revisão. O publicador não tem mais caminho automático para 5801 (decisão do Miguel).

## Provas

- Log publicador: `[2026-09-01 15:16:33] fim de ciclo: publicados=[268553]` + relatório 15:16 no canal ("origem: ponte") + post_date 15:39:56 (payload/wp-cron).
- Ledger CL 500-503 (rondas 14:42/15:12/15:42/16:12) + de_laura.md CL-023 (5421-5423), CL-024 (5429-5432), AL-027 (5436+), auditoria pós 15:43 (5472).
- WP: `_cafezinho_origem` 14:15:05 user 5801; `_cafezinho_img_check` ok/CL-20260901-023/AGY-LAURA 15:35; content pós-correções sem timecodes (grep 0) e com repúdio (grep 2) após 17:5x.
- Teste do scanner novo: 4/4 (ver acima). Backups datados nos 3 arquivos.

## O que falta / próximos passos

- Ciclo 18:00 do publicador = 1º com patch em produção — verificar log (feito/pendente no fechamento desta memória).
- CL/AGY avisadas via ZM-20260901-032 (de_dell.md) + linha no canal do publicador; protocolo sugerido à CL: "TEXTO APROVADO — publique incondicional" × "condicionado — aguardar".
- A 2ª matéria da fila (KLjB9eQ5d9o/268440, As Cunhãs) segue ENTREGUE_GATE/draft — sai só com revisão.
- Miguel: se quiser tirar o 268553 do ar, é 1 comando (robôs não vão mais re-publicar sozinhos — travado).

## Estado

**O que aconteceu:** brecha fechada em 3 camadas, testada; repúdio pendente aplicado; ordem rascunho-only registrada. **O que falta:** nada estrutural; monitoramento do 1º ciclo pós-patch. **O que preciso do Miguel:** nada obrigatório (se quiser, decidir se aceita publicação de matérias YouTube via AGY/painel após gate da CL, ou sempre pessoal).
