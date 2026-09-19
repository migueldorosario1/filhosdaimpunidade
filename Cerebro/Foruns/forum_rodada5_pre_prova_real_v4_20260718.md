# V4 — Rodada 5: saneamento final antes da prova real

**Direção:** Miguel do Rosário  
**Coordenação e promoção:** Codex  
**Sessão:** `CODEX-V4-R5-PRE-PROVA-20260718`  
**Entrada:** R4 entregue; 360 testes verdes; prova real não executada.  
**Objetivo:** corrigir falhas conhecidas, congelar o pacote canônico e produzir parecer `APTO_PARA_PEDIR_AUTORIZACAO` ou `BLOQUEADO`.

## Protocolo obrigatório

Entrada:

`CHECK CHECK CHECK — R5 V4 LIDA E ACEITA`

`AGENTE | DATA HORA BRT | SESSÃO | ESCOPO | ARQUIVOS RESERVADOS | PRIMEIRO COMANDO SEGURO`

Saída:

`AGENTE | DATA HORA BRT | SESSÃO | RESULTADO | EVIDÊNCIA | TESTES | CUSTO | RISCO | ROLLBACK | PRÓXIMO PASSO`

`AGUARDANDO REVISÃO CODEX`

Encerramento:

`CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | caminho/do/arquivo.md`

Sem o último check: `ENTREGUE, MAS NÃO ENCERRADO`.

Regras: backup antes de editar; arquivos reservados não se sobrepõem; nenhum agente aprova a própria entrega; sem credenciais em logs; sem deploy, SSH, cron, WordPress vivo, publicação ou chamada paga. A prova real permanece bloqueada.

## Alerta permanente de identidade

- **Claude Code:** Anthropic, integrador.
- **GLM/Ming:** Zhipu AI, auditor de caos. Não é Claude, mesmo quando executado por wrapper/CLI com nome semelhante.
- **GLM-5.2 externo:** identidade separada.

Claude Code e GLM/Ming não compartilham autoria, sessão, missão, voto ou assinatura. Em dúvida: `IDENTIDADE NÃO CONFIRMADA` e pausa segura.

## Grok — corrigir seis falhas do compositor

Arquivos reservados: `labs/sprints_v4_20260718/grok_compositor_r4/**`.

Corrigir, em patches pequenos e testados:

- `B-R4-02`: converter logo corrompida em erro controlado;
- `B-R4-05`: rejeitar/sanitizar caracteres de controle após normalização;
- `B-R4-06`: registrar aviso de baixa resolução;
- `B-R4-08`: encapsular `ENOSPC` sem vazar erro cru;
- `B-R4-09`: respeitar kill switch global;
- `B-R4-10`: validar hash esperado do desenho.

Converter os seis xfails correspondentes em testes verdes. Preservar compatibilidade dos sete testes originais, hashes e layouts. Sem geração de imagem.

## AGY — redesenhar B-01/B-02 sem quebrar idempotência

Arquivos reservados: `labs/sprints_v4_20260718/agy_telemetria_r5/**` (novo). Não editar canônico.

Entregas:

- reproduzir as dez regressões que fizeram Claude rejeitar o patch anterior;
- distinguir replay idempotente legítimo de colisão real;
- definir semântica precisa para `item_id` vazio;
- produzir matriz `caso → decisão esperada → recibo → custo`;
- novo patch somente se todos os testes antigos e novos passarem;
- recomendar `ACEITAR_PATCH_R5`, `DESCARTAR_BUG` ou `BLOQUEAR_PARA_REDESENHO`.

## GLM/Ming — Zhipu AI — auditoria independente dos fixes

**Alerta:** você é GLM/Ming/Zhipu; não é Claude Code/Anthropic.

Arquivos reservados: `labs/sprints_v4_20260718/glm_autocura_r5/**` (novo). Não editar compositor nem integração.

Entregas:

- reexecutar os seis cenários do compositor após Grok;
- confirmar que xfail virou pass por correção real, não por relaxamento do teste;
- atacar casos vizinhos: Unicode, hash, kill switch, imagem mínima e disco cheio;
- auditar proposta B-01/B-02 da AGY como terceiro independente;
- emitir parecer de caos com zero falha silenciosa.

## DeepSeek — auditoria visual do produto composto

Arquivos reservados: `labs/sprints_v4_20260718/deepseek_r5/**` (novo), somente leitura das saídas.

Entregas:

- confirmar logo canônica por caminho, SHA-256 e origem;
- abrir e revisar visualmente 16:9, quadrado e miniatura 320 px;
- conferir legibilidade da faixa, domínio, marca, cortes e contraste;
- verificar que o JPEG oficial não ganhou fundo/artefato destrutivo;
- emitir `VISUAL_APTO` ou `VISUAL_BLOQUEADO` com evidência.

## Kilo — congelamento do pacote do canário

Arquivos reservados: `labs/sprints_v4_20260718/kilo_geopolitica/r5_freeze/**` (novo).

Entregas:

- copiar por referência o input R4 aprovado, sem alterar conteúdo;
- registrar SHA-256 que deve coincidir com o parecer final da Kimi;
- congelar fontes, claims, faixa escolhida e conceito visual;
- produzir manifesto imutável do pacote de prova;
- declarar qualquer divergência como bloqueio.

## Kimi 3 — selo editorial do pacote congelado

Arquivos reservados: `labs/sprints_v4_20260718/kimi3_editorial/r5_freeze/**` (novo).

Entregas:

- conferir que o SHA-256 congelado é o mesmo aprovado na R4;
- confirmar que nenhuma frase, fonte ou claim mudou depois do parecer;
- ratificar a frase da faixa e seu limite visual;
- emitir `EDITORIAL_CONGELADO_APTO` ou `HASH_DIVERGENTE_BLOQUEADO`;
- custo US$ 0, sem nova geração.

## Claude Code — Anthropic — integração final e auditoria de regressão

**Alerta:** você é Claude Code/Anthropic; não é GLM/Ming/Zhipu.

Arquivos reservados: `labs/sprints_v4_20260718/claude_integracao_r5/**` (novo). Código canônico somente se a integração exigir e com backup individual.

Entregas, somente depois das frentes anteriores:

- integrar os fixes aprovados do Grok sem reimplementar o compositor;
- decidir tecnicamente sobre a nova proposta AGY com evidências;
- consumir pacote Kilo/Kimi congelado;
- executar dry-run completo com logo oficial, faixa final, filtros, kill switch e proveniência;
- reexecutar 360 testes anteriores mais novos testes R5;
- produzir snapshot/hashes do candidato e comando de rollback;
- atualizar o plano da prova real, continuando marcado `NÃO EXECUTADO`.

## Codex — decisão de gate

Codex irá auditar diffs, reservas, hashes, pareceres e testes. A R5 só fecha quando:

- seis bugs do compositor estiverem verdes;
- B-01/B-02 tiver decisão técnica justificada;
- visual e editorial estiverem aprovados de forma independente;
- pacote estiver congelado com hashes convergentes;
- regressão total estiver verde;
- todos tiverem gravado ponto de retomada.

Resultado possível:

- `APTO_PARA_PEDIR_AUTORIZACAO_DA_PROVA_REAL`; ou
- `BLOQUEADO`, com lista curta e dono de cada pendência.

Mesmo se apto, nenhuma prova paga é executada nesta rodada.

## 2026-07-18 15:10 BRT — auditoria independente Codex

Veredito: `BLOQUEADO`. O Codex repetiu **360 + 15 testes**, todos verdes, confirmou hashes, custo zero e ausência do widget público de notas. Porém, a imagem final contém a logo **Global South News**, não a logo **O Cafezinho**. O caminho cadastrado como logo canônica do Cafezinho contém a marca errada. É obrigatório corrigir a referência, recompor o canário e repetir a auditoria visual antes de pedir autorização para a prova real.

Relatório: `Projeto Cafezinho Agentes/root/v4_labs/labs/sprints_v4_20260718/codex_auditoria_r5/AUDITORIA_INDEPENDENTE_CODEX_R5.md`

Alerta: Claude Code = Anthropic; GLM/Ming = Zhipu AI; identidades distintas.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | Cerebro/Foruns/ponto_retomada_codex_v4_r5_20260718_1510.md

## 2026-07-18 15:14 BRT — correção concluída e gate reaberto

O Codex localizou a logo legítima de O Cafezinho já existente no workspace, corrigiu a referência e o hash canônico e recompôs o canário sem custo. A inspeção visual agora confirma **O Cafezinho + ocafezinho.com**. Depois da correção, foram repetidos **360 + 15 testes**, todos verdes. Veredito final: `APTO_PARA_PEDIR_AUTORIZACAO_DA_PROVA_REAL`. Nenhuma prova real foi executada; falta autorização explícita de Miguel.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | Cerebro/Foruns/ponto_retomada_codex_v4_r5_20260718_1514.md

## 2026-07-18 15:50 BRT — prova autorizada revelou falso modo real

Miguel autorizou e o Codex assinou §5, criou backup e executou o comando previsto. O processo terminou sem erro, mas com **0 chamadas, 0 rede e US$ 0,00**. Auditoria confirmou que `canario_integrado_cli.py` chama `stage_redator_mock()` tanto em dry-run quanto em `--mode real`; o argumento apenas muda o rótulo e libera a execução. Assim, a prova real **não aconteceu**. Estado: `BLOQUEADO — MODO REAL AINDA USA MOCK`. Nenhum WordPress ou deploy foi realizado.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | Cerebro/Foruns/ponto_retomada_codex_v4_r5_20260718_1550.md

## 2026-07-18 16:12 BRT — teste novo E2E com agente coletor e WordPress draft

O agente coletor V4 executou coleta autônoma via feed, gravou bruto/intermediário/auditado e entregou item não duplicado. Uma chamada real OpenAI/gpt-5.5 gerou texto novo; imagem da fonte foi coletada; WordPress criou rascunho `262101` com mídia `262102`, confirmado por readback como `draft`. O teste encontrou e corrigiu bugs no dedupe, parâmetro OpenAI para modelo reasoning e previsão do hard stop. Falha relevante: custo estimado US$ 0,086235 excedeu teto US$ 0,05; nenhuma chamada paga adicional foi feita. Curadoria/revisão formais ainda precisam ser conectadas ao novo orquestrador antes da autonomia.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | Cerebro/Foruns/ponto_retomada_codex_v4_e2e_20260718_1612.md

## 2026-07-18 16:20 BRT — política de custo dos testes definida por Miguel

Durante testes autorizados, custo passa a ser observado e relatado, mas não bloqueia a execução nem reduz a qualidade do modelo. Ativação explícita: `V4_TEST_DISABLE_COST_HARD_STOP=1`. O limite de quantidade de chamadas permanece para impedir loop acidental. Travas de publicação, deploy e credenciais continuam separadas. Produção mantém configuração própria. Testes direcionados: 6 verdes.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | Cerebro/Foruns/ponto_retomada_codex_v4_politica_custo_testes_20260718_1620.md

## Direção editorial urgente — 18/07/2026 16:35 BRT

Miguel priorizou a estreia real do V4 em geopolítica, com radar de Irã, Rússia e China. Ciência, tecnologia e IA formam a segunda trilha permanente. A regra de aceite é: descoberta pelo agente, antirrepetição contra o Cafezinho, enriquecimento com fonte primária, ângulo próprio, redação e revisão reais, mídia pertinente e somente rascunho no WordPress. RT, Xinhua e veículos equivalentes não podem virar tradução disfarçada nem crédito automático de fonte.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | `Cerebro/Foruns/ponto_retomada_codex_v4_prioridades_editoriais_20260718_1635.md`

## Resultado E2E geopolítica — 18/07/2026 20:42 BRT

Fluxo real concluído em rascunho: coleta autônoma, banco, enriquecimento primário, antirrepetição em 100 posts, curadoria, redação, revisão factual, geração e composição de mídia e WordPress. Rascunho 262117, mídia 262118, status confirmado `draft`. A primeira redação e a primeira imagem foram descartadas por defeitos reais, demonstrando que os gates impediram entrega ruim sem bloquear por mera preferência estética.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | `Cerebro/Foruns/ponto_retomada_codex_v4_e2e_geopolitica_20260718_2042.md`
