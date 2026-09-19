# Conserto não é aceleração — cadência é decisão do dono (grade única)

**Data:** 02/09/2026 · **Ronda:** DS-20260902-019 (58º CHECK) · **Ref.:** DSC-20260902-038 (11:42) + DSC-20260902-039 (12:00) + CL-20260902-068 (11:50)

## O quê

O Miguel deu DUAS ordens sobre os revisores em ~30 minutos:
1. **~11:3x** (DSC-038): "vê se conserta então os revisores... conserta para mim esses revisores, que ontem a gente meio que desligou eles... ainda ia esperar o contrato" + "no contrato, quando é que os revisores entram em ação? já me responde e conserta eles".
2. **~12:0x** (DSC-039): "volta os revisores [pra cadência calma]... bota a ronda deles de uma hora... tem que ter uma grade de controle única no cérebro de todos os agentes — qual é a ronda de cada um; qualquer mudança tem que avisar na roda de controle e mudar na grade; atualizada a cada ronda do DSN Chefe".

O DSC executou as duas em sequência: (038) consertou a escada R1 com sonda ao vivo ANTES de mexer (prova perna a perna), patch com fail-through (perna que não busca cai pra próxima — antes a 1ª resposta não-vazia truncava a escada, o bug do dia todo), perna nova brave+deepseek com busca REAL, chave DeepSeek sincronizada, grok-4 fora da escala, cadência reativada 15min com freios mantidos (hardstop US$3/dia); (039) depois da ordem das ~12:0x, criou a **grade de controle única** (`cerebro/Foruns/GRADE_DE_CONTROLE_AGENTES.md`), pôs os revisores em **1x/hora** (R1 :05 · R2 :20) e nomeou o **DS-N Chefe como GESTOR da grade**.

## Por quê

A manhã revelou uma régua do dono que eu não tinha nomeado: **consertar ≠ acelerar**. O Miguel primeiro quis a escada FUNCIONANDO (conserta, capaz que ficou sem crédito, ontem desligamos) e depois, com o conserto feito, pediu CADÊNCIA CALMA (bota de uma hora — "tudo a gente não pode fazer bagunça"). Ou seja: o valor não é rodar rápido, é rodar certo com prova, e a cadência é uma DECISÃO de governança do dono, não um parâmetro técnico que o executor escolhe sozinho. A "bagunça" que o Miguel teme não é o código — é cada agente mudando o próprio ritmo sem registro comum: por isso a ordem cria uma grade única com regra-de-ouro (mudança de cadência exige anúncio na ponte COM ref + atualização da grade NO MESMO commit; sem isso = violação de protocolo D9).

## Como aplicar

1. **Separar "funcionar" de "acelerar":** quando um serviço cai, a primeira ordem do dono é consertar com prova (sonda antes de mexer, freios mantidos, fail-close preservado); a cadência é ajuste POSTERIOR e só o dono decide — nunca assumir que consertado = religar rápido.
2. **Cadência de agente = registro, não costume:** antes de mudar (ou quando notar mudança de) cadência/agenda de qualquer agente: anunciar na ponte com ref + atualizar a grade no mesmo commit. A grade é fonte única; cron espalhado é consequência, não verdade oficial.
3. **Grade tem gestor:** DS-N Chefe confere a grade contra o real (cron/processos/canal) a cada ronda B e reporta resumo; qualquer DSN silencioso 2+ rondas = alerta. DS-Dell (eu): minha linha na grade estava defasada ("56º CHECK 11:05" quando eu já estava no 58º) — o gestor atualiza na ronda dele; eu registro sem editar arquivo alheio.
4. **Fail-close vira régua de transição:** o DSC manteve o CL como cobertura humana até a escada provar estabilidade — redundância de papel durante a prova é o desenho, não desperdício (mesma lição de 01/09: "a medição tem redundância").

**Reconfirmação irmã (mesma ronda):** 3ª confirmação do escalonador Emenda 5 — Pix 10:42→10:57 · Bayern 11:05→11:27:56 · Dia de Sorte 11:35→11:57:59. Publish em modo grade vira agendado do slot (gap ≥20min); 3 confirmações = padrão da casa, não bug (ref. licoes/20260902_o_future_que_mexe_e_a_mao_do_dono_no_volume.md).
