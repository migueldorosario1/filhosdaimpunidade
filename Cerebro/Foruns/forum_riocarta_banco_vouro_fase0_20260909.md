# Fórum — Rio Carta × Banco de Mídia V-Ouro: FASE 0 ressuscitada + carinho Couto + pesquisa obrigatória

Data: 09/09/2026 (sessão ZCode Qwen3.8-Max, Dell)
Origem: ordem do Miguel 09/09 ~07:5x — "vamos trabalhar melhor no rio carta… o ricardo merece a gente ter mais carinho por ele… tem que ter pelo menos uma por dia… se tem pesquisa nova sobre o rio de janeiro… O RioCarta tem acesso ao Banco de Mídia V-Ouro? A gente consegue adaptar para ele ter acesso? Como é que a gente melhora a questão da mídia, das fotos do RioCarta?"
Memória técnica irmã: `Memorias/memoria_riocarta_banco_vouro_fase0_20260909.md`

## Resposta direta à pergunta do Miguel

NÃO tinha acesso efetivo — agora TEM. A FASE 0 (busca no banco antes da cascata externa de capa) foi instalada em 05/08 no `publicador.py` dos V4 temáticos, mas o espelho local que ela lê (`agent_data/v4/banco_midia/index.json` + `img/`) só existia no Dell. O pipeline roda no NYC → `buscar_no_banco()` sempre retornava [] e caía no "banco de mídia indisponível — seguindo cascata externa". Pior: um tar.gz de export de 17/08 (2,7GB) ficou esquecido no /tmp do NYC sem nunca ser extraído. Cura: espelho regenerado HOJE no próprio NYC (1301 mídias, 3,1GB) + cron semanal local (seg 06:20) — sem tráfego entre máquinas, econômico.

## Decisões tomadas

1. Espelho local no NYC + `banco_sync_local_nyc.py` (dump Ouro+acervo → extract) no cron `20 6 * * 1`. Economia: 1x/semana, zero scp.
2. Coleta RJ no banco vivo: manifesto com 10 entidades (Couto prioridade 97 no topo) → +40 mídias aprovadas com visão: Couto ×12 (EBC/Fiocruz + álbum oficial GovRJ do evento França), Rodrigo Neves ×6, Benedita ×6, Portinho ×6, Garotinho ×6, Siri ×2, Jordy ×1, Castro ×1. QA visual humano-agente: Couto confirmado em 4 fotos baixadas e vistas.
3. PURGA Eduardo Paes ×6: as fotos do álbum "Reunião com prefeito Eduardo Paes" (Flickr GovRJ) NÃO condizem com a descrição (cena de evento de saúde, homem central não é Paes) — e foto junto com Castro é inapropriada p/ linha editorial. Removidas das 3 tabelas + 11 rejeições `curadoria_riocarta_20260909`.
4. GUARDA_CURADORIA no robô V3: ele NUNCA leu `rejeicoes_ouro` (dedup era só hash em `midia_ouro`) e re-aprovou as 5 fotos purgadas na mesma hora. Patch: URL com motivo `curadoria_*` em rejeicoes = pulada. Backup `.bak_pre_guarda_curadoria_20260909`.
5. Matcher: NÃO adicionar tokens soltos "couto"/"neves" aos `_TOKENS_FORTES` — "neves" casaria manchete de Aécio Neves com fotos de Rodrigo Neves (o bug original!) e "couto" com Mia Couto. A frase cheia da entidade ("ricardo couto", fronteira de palavra) já casa; guidelines exigem nome completo.
6. Editorial (riocarta.json + contrato riocarta.md): carinho Couto ("tratamento especialmente respeitoso e construtivo, sem bajulação, sem tratá-lo como extensão da era Castro — fiscalização pesada segue p/ Castro, Douglas Ruas e bolsonarismo"); NOVA pesquisa RJ (governo ou Senado) = matéria OBRIGATÓRIA do mesmo dia com números completos; +5 queries Brave de pesquisa + feed Google News `pesquisa eleitoral rio de janeiro when:2d`; foco_local += "ricardo couto", "pesquisa eleitoral".
7. Cadência: 1 matéria/dia confirmada (cron NYC `0 12 * * *` orquestrador --all; riocarta max_articles_per_run=1; as 2 corridas extras foram desligadas 08/09 pela ordem de economia).

## Achados de forense (reportar ao Miguel)

- O "loop de 30 min" que escrevia em `execucoes_ouro` (stats "tombadas", sem código no disco) era a ronda DeepSeek do Dell (`ronda_30min.sh` → agente headless via SSH heredoc no NYC). Morreu hoje ~03:00 BRT (exec 2389 sem fim). Últimos ciclos: 0 aprovações/dia (só duplicadas+tombadas) — não ressuscitar (economia); o robô V3 com manifesto cobre a necessidade.
- As aprovações RJ de 05/08 (Paes/Benedita/Neves/Castro) foram para um --db de TESTE, não para o banco vivo — por isso o banco parecia "sem RJ".

## Estado da missão

O que aconteceu: espelho vivo + FASE 0 testada (Couto→12 candidatas, Neves→6, Benedita→6, Garotinho→6, Aécio Neves→0 = caso negativo OK); editorial gravado; purga+guarda curadoria no ar.
O que falta: 1ª matéria do Rio Carta usando capa do banco (cron de hoje 12:00 UTC já pega o espelho); observação 1 semana do tribunal visual com as capas do banco.
O que preciso de você (Miguel): nada bloqueante. Se quiser, aprovar foto de Paes de outra fonte (atual banco tem 0 fotos dele por decisão de curadoria) e dizer se o carinho Couto vira também coluna fixa semanal.
