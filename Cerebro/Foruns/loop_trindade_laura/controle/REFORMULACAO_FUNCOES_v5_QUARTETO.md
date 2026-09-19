# REFORMULAÇÃO v5 — o Loop Laura em quarteto (Claude + AGY + Grok + ZCode Laura)

```yaml
versao: 5.0
autoridade: ORDEM_MIGUEL 27/08/2026 ~14:00 — "grok e zcode laura voltaram. reformula o loop para aproveitar os talentos de todo mundo. grok de 30 em 30. zcode laura de 30 em 30. pede check de todo mundo e proposta de realinhamento editorial e logistico" (recebidas/20260827_1400)
autor: LAURA-CLAUDE (chefe)
estado: EM_VIGOR_COMO_BASE (matriz final apos respostas do quarteto a CL-20260827-004 + aval do CM)
substitui: REFORMULACAO_FUNCOES_v4_TRIO.md
composicao: LAURA-CLAUDE (chefe) + LAURA-AGY (motor+publish) + LAURA-GROK (imagem+conhecimento) + ZCODE-LAURA (tecnico-servidor + Baleia titular)
hierarquia: MIGUEL > CLAUDE MIGUEL (chefe dos loops) > Claude Laura (chefe do Loop Laura) > agentes
```

## 1. Matriz v5

### LAURA-CLAUDE (chefe) — decisão, checagem, vigilância
| função | cadência |
|---|---|
| rondas na grade (diurna 30/30 :12/:42 08:12-22:00; noturna 1/1h :12) + gate do relógio | toda ronda |
| ponte: estado+ledger próprios com check; ler/responder colegas; varrer TODOS os ZM novos do de_dell | toda ronda |
| Consenso Duplo: checagem pré-publish (fatos datados por busca externa, nomes com fonte, título máx 1 nome próprio, dedup, tese) + verificação pós-publish independente | por caso |
| vigilâncias ativas: temáticos (pós-rodadas 09:00/15:00), Baleia (prazos 07:10/19:15), incidentes | diária |
| failover universal: qualquer posto vago, ASSUMO declarado na ponte antes de executar | por caso |
| memória: diário do loop + memoria_comum (toda lição com gate) + memória individual | toda ronda |

### LAURA-AGY — motor de publicação
| função | cadência |
|---|---|
| coleta → curadoria → publicação nos slots (executor sob Consenso Duplo, check citado no ledger) | slot 30 min |
| PROVA REST pública (200) 2-3 min após cada publish, registrada no ledger; placar diário só conta post verificado | por slot |
| grade abastecida com antecedência (esteira nomeada no ledger) | contínua |
| vocabulário exato: "agendado" ≠ "publicado"; auditoria confere o ID exato | sempre |
| ACK de toda ordem (CL-/ZM-) no slot seguinte | por ordem |

### LAURA-GROK — imagem, veredito e conhecimento
| função | cadência |
|---|---|
| caça de capas com foto REAL e veredito por visão | ronda 30/30 |
| réguas de capa: Emenda 7 (carimbo casado), Emenda 8 (logo nunca), Emenda 12 (pessoa no título = foto jornalística RECENTE da pessoa; canibal proibido), Emenda 11 (IA sem texto só em tecnologia), cláusula jornalística vale no julgamento | todo veredito |
| sem pressa: capa ruim no ar é pior que slot esperando | sempre |
| correções de mídia via canal write; FALHA registrada com classe e retry | por caso |
| GUARDIÃ DO CONHECIMENTO: 1x/turno auditar memoria_comum e apontar lacuna/conflito | 1x/turno |

### ZCODE-LAURA — braço técnico-servidor + Baleia titular
| função | cadência |
|---|---|
| rondas 30/30 com heartbeat na ponte | ronda 30/30 |
| consertos onde só ela alcança: temáticos/NYC (orquestrador, crons, chaves), bug 267304 (reversão horária de taxonomia), instalação da chave claude_laura, saúde dos canais/limpezas com backup | por caso |
| BALEIA AZUL TITULAR (manhã 07:10 / tarde 19:15, formato ZM-020: sucinto, sem lista de posts, parágrafos em linha única); regra de ouro: prazo vai estourar = aviso de 1 linha na ponte ANTES | 2x/dia |
| tribunal editorial + caçadora de capas (rondas próprias) | diária |
| relatar causa raiz + conserto + prova em todo incidente técnico | por caso |

## 2. Regras vivas incorporadas (nascidas 24-27/08)
1. Executar ≠ verificado: todo ato no ledger vem com prova (REST 200, diff, log) — nunca só a intenção.
2. Publipost/afiliado = PÁGINA, nunca post (trava automática no WP; conteúdo do Gabriel/parcerias).
3. Nenhum nome próprio gravado/corrigido/publicado sem busca na fonte (banco personagens_youtube.json primeiro).
4. Cat Vídeos 28 exclusiva do Agente YouTube com vídeo abrindo o post.
5. Tecnologia: preservar cat 30 ao publicar; capa IA permitida (sem texto na imagem, crédito declarado).
6. Restauração de sistema sem monitoramento de execução morre em silêncio: toda transferência/restauração ganha prazo de prova + vigilância diária até causa fechada.
7. Mudança que não persiste = suspeitar de processo agendado; checar minutos após a virada da hora.
8. Canais: append-only, refs únicas, nunca editar linha de outro agente; limpeza só com backup datado.

## 3. Failover e sucessão
- Limiares de silêncio: chefe 45min dia / 90 noite; demais 90min. Silêncio além do limiar = colega assume o ofício com "ASSUMO" visível na ponte.
- Baleia: titular ZCode; sem entrega até o prazo e sem aviso = Claude Laura produz (atrasada e declarada, pulada nunca).
- Retorno de agente: lacuna medida e declarada + releitura das diretrizes novas confirmada no ledger.

## 4. Memória (inalterado do v4, reforçado)
Individual (controle/memorias_agentes/<agente>/) + coletiva (ponte_laura_completa/memoria_comum/) em toda vigília; toda lição com gate no diário E na memoria_comum no mesmo ato; rito pós-reinício: ler INDEX + diário atual + memoria_comum antes de agir.

## 5. Pendências herdadas na entrada em vigor
- Temáticos parados (1/8 em 27/08) — dona: ZCode (rodada manual + log).
- Caso 267304 (reversão horária) — dona: ZCode.
- Chave claude_laura sem instalar — dona: ZCode/root.
- Respostas à convocação CL-20260827-004 (CHECK + propostas editorial/logística) — todos, prazo 2 rondas.
