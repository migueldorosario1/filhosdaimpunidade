# Forum V4 - Fase 7 Multi-Item Lab - 2026-07-10

## Contexto

Fase aberta apos o veredito Fable `APROVADO_PARA_FASE7_LAB` da Fase 6.

Objetivo operacional: atacar o F6.2, isto e, provar generalizacao minima com casos novos e `curadoria_tese.py` congelado durante a rodada.

Esta fase nao promove para `root/v4`, nao chama WordPress real, nao publica externamente e nao executa promocao real.

Pacote-base imediatamente anterior:

`Projeto Cafezinho Agentes/root/v4_labs_fase6_ustr0331_pdf_followup_20260710.tar.gz`

SHA256:

`33d047800d5d2e8b53147fadd09c95236e82f552e1ac9720afa1094b94c284cc`

## Implementacao

Arquivos adicionados em `Projeto Cafezinho Agentes/root/v4_labs/`:

- `contratos/v4_multi_item_lab_v1.json`
- `codigo/multi_item.py`
- `codigo/multi_item_cli.py`

Arquivos ajustados:

- `codigo/test_contracts.py`: testes de lote multi-item e deteccao de curadoria alterada.
- `codigo/fluxo.py`: preserva `fontes` do fixture quando o contrato traz esse campo, sem preencher `fontes: null` em fixtures antigas.

O gerenciador multi-item:

- le contrato estavel de lote;
- mede hash dos arquivos congelados antes e depois;
- executa o fluxo completo por item;
- consolida relatorio por lote;
- falha se curadoria congelada mudar, se item falhar, ou se a rodada tiver diversidade minima insuficiente.

## Fontes Congeladas

Hashes registrados antes/depois da rodada:

- `codigo/curadoria_tese.py`
  - antes: `c1c5f3f592a537089030328fbd8906209de727ae5a8e4ae965eda3256c52a521`
  - depois: `c1c5f3f592a537089030328fbd8906209de727ae5a8e4ae965eda3256c52a521`
- `contratos/v4_curadoria_tese_v1.json`
  - antes: `c06885ce89cb4ef5f227c378f6257d67a57ce48155002afeb519beb9a9e8dc3f`
  - depois: `c06885ce89cb4ef5f227c378f6257d67a57ce48155002afeb519beb9a9e8dc3f`

Resultado: `curadoria_frozen=true`.

## Casos Rodados

Contrato de lote: `contratos/v4_multi_item_lab_v1.json`.

Itens:

- `v4_real_005` - `v4_internacional` - "Carta escrita e depoimento no USTR abrem nova frente sobre Flavio"
- `v4_real_006` - `v4_ciencia_tecnologia_ia` - "Data centers recolocam energia, IA e soberania no centro da politica industrial"
- `v4_real_007` - `v4_cultura` - "Audiovisual brasileiro disputa soberania cultural nas plataformas"

Resultado agregado:

- `status=multi_item_lab_ok`
- `total_items=3`
- `ok_items=3`
- `failed_items=0`
- `issues=[]`
- editorias: `v4_internacional`, `v4_ciencia_tecnologia_ia`, `v4_cultura`

Warnings:

- `imagem_destacada_pendente:sem_midia_auditada:Flavio Bolsonaro`
- `imagem_destacada_pendente:sem_midia_auditada:infraestrutura de IA no Brasil`
- `imagem_destacada_pendente:sem_midia_auditada:audiovisual brasileiro`

Leitura: warnings aceitaveis no dry-run, coerentes com a politica rascunho-primeiro. Continuam gate duro para publicacao real.

## Collection Request

Nos tres novos casos:

- `collection_request.status=none`
- `collection_request.required_before=none`
- `issues=[]`

Nao houve reabertura do F6.1. O follow-up do PDF USTR permanece registrado como `collection_followup`, nao como bloqueio de publicacao.

## Chamadas Externas

Houve roteamento/recibos LLM em laboratorio nas editorias novas, com `gemini-3.5-flash` registrado nos recibos.

O gate relevante para seguranca operacional permaneceu fechado:

- `external_publish=false`
- `wordpress_real=false`
- `promocao_real_executada=false`
- `root/v4` intocado

Nao declarar esta rodada como "sem LLM real"; declarar como laboratorio sem publicacao externa.

## Validacao

Validacao local em `Projeto Cafezinho Agentes/root/v4_labs/`:

- `PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts` -> `OK 90 contract tests`
- `PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.agentes_cli --strict` -> OK
- `PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.fluxo_cli --execute` -> OK
- `PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.promocao_cli --execute` -> `promocao_shadow_aprovada`, `issues=[]`
- sem `__pycache__` e sem `.pyc` no pacote

Validacao em extracao limpa:

Diretorio: `/tmp/v4_labs_fase7_multi_item_lab_check/v4_labs`

Resultado:

- `OK 90 contract tests`
- agentes strict OK
- fluxo dry-run OK
- promocao shadow aprovada
- `wordpress_real=false`
- `external_call=false` no preflight
- `promocao_real_executada=false`

## Pacote

Pacote Fase 7:

`Projeto Cafezinho Agentes/root/v4_labs_fase7_multi_item_lab_20260710.tar.gz`

SHA256:

`22e1e452c192a32a3bd55c7ec73d025066345c77ddbad2638a05aff475c2b2ef`

Tamanho: `1011K`.

## Veredito Codex

F6.2 recebeu evidencia mecanica suficiente para auditoria: os tres casos novos rodaram com `curadoria_tese.py` e o contrato de curadoria congelados, sem diff nos hashes antes/depois.

Isto nao e promocao para producao. O proximo passo correto e pedir auditoria Fable/GPT 5.5 do pacote Fase 7, com foco em:

1. confirmar que a prova de generalizacao da curadoria e aceitavel;
2. revisar se o gerenciador multi-item formal esta estreito o bastante;
3. confirmar que os warnings de imagem continuam aceitaveis no lab;
4. manter `wordpress_real=false` ate ordem humana explicita.

## Auditoria Fable - Fase 7 - 2026-07-10

Carta recebida:

`Cerebro/Foruns/carta_fable_auditoria_fase7_multi_item_20260710.md`

Veredito:

`APROVADO para continuidade em laboratório`.

Pontos confirmados pelo auditor:

- SHA256 `22e1e452c192a32a3bd55c7ec73d025066345c77ddbad2638a05aff475c2b2ef` confere.
- F6.2 mecanico fechado: curadoria congelada verificada contra copias auditadas da Fase 6, nao apenas contra hashes declarados.
- Batch multi-item reexecutado pelo auditor: `multi_item_lab_ok`, 3/3, tres editorias.
- `OK 90 contract tests`, agentes OK, fluxo OK, preflight `promocao_shadow_aprovada`, `issues=[]`.
- Guards mantidos: sem publicacao externa, sem WordPress real, sem promocao real.
- Reporte correto: houve roteamento/recibos LLM em laboratorio; nao declarar como rodada "sem LLM real".

Ressalvas:

- F6.1 foi marcado pelo auditor como fechado provisoriamente porque o arquivo de forum da Fase 6 nao estava no conjunto que ele abriu. Localmente, o forum existe e contem a decisao verbatim de Miguel, mas qualquer pacote futuro para auditor externo deve anexar esse forum ou um extrato verificavel.
- Follow-up USTR permanece aberto ate recibo/URL oficial direta do USTR. O auditor confirmou o PDF de 86 paginas e registrou anomalia de proveniencia: metadados internos indicam `Producer: LibreOffice 24.2`, criacao `2026-07-02`, sugerindo reexportacao por espelho.

## Achado F7.1 - Curadoria heuristica degradou fora das familias conhecidas

Severidade: media, editorial.

Leitura do auditor:

- `v4_real_005` ainda esta dentro da familia conhecida de keywords USTR/tarifa/Pix; portanto nao prova generalizacao editorial.
- `v4_real_006` e `v4_real_007` receberam teses do template industrial/IBGE mal aplicado.
- O caso de cultura/streaming saiu com linguagem de industria, valor agregado e politica economica, inclusive `quem_perde` sobre leitura que reduz industria a numero mensal.
- Nenhuma etapa do pipeline flagrou a incoerencia; o batch reportou `ok=true`.

Conclusao:

F6.2 esta mecanicamente fechado, mas o teto editorial da curadoria por keywords ficou demonstrado. Fora de politica/economia, a heuristica nao generaliza; ela encaixa a pauta no molde errado de forma silenciosa.

Decisao de Miguel registrada em 2026-07-10:

Miguel escolheu a politica interina e ratificou em sessao: "ok, ratifico".

Politica interina:

ate existir curadoria propria por editoria ou gate forte de coerencia, teses fora das familias conhecidas sao rascunho obrigatoriamente revisado por humano, sem promocao como `ok` editorial automatico.

Efeito:

F7.1 deixa de ser pendencia de decisao e vira diretriz de desenvolvimento em laboratorio. Continua proibida promocao para `root/v4` sem as demais condicoes e sem autorizacao humana explicita.

Recomendacao tecnica minima, qualquer que seja a decisao:

adicionar gate de coerencia tese x editoria/tema para que tese desalinhada vire issue ou warning auditavel no batch, nunca `ok=true` silencioso.

## Implementacao Lab F7.1 - Gate de Coerencia Editorial - 2026-07-10

Miguel autorizou a etapa tecnica apos ratificar a politica interina.

Escopo implementado em `Projeto Cafezinho Agentes/root/v4_labs/`:

- novo contrato `contratos/v4_editoria_coerencia_v1.json`;
- novo modulo `codigo/coerencia_editorial.py`;
- integracao do gate em `codigo/multi_item.py`;
- contrato de lote `contratos/v4_multi_item_lab_v1.json` agora aponta para `editorial_coherence_contract`;
- testes em `codigo/test_contracts.py`.

Decisao de arquitetura:

- `curadoria_tese.py` nao foi alterado;
- curadoria politica/economia nao foi mexida;
- o gate e parametrizado por editoria;
- cultura e IA/data centers sao as primeiras editorias com regra;
- a regra e warning-only em laboratorio, conforme politica interina;
- o gate olha o miolo da tese depois de `revela-se que`, para evitar falso positivo por entidade nominal.

Resultado do batch reexecutado:

- `status=multi_item_lab_ok`;
- `issues=[]`;
- `ok_items=3`;
- `curadoria_frozen=true`;
- `editorial_review_required_items=["v4_real_006","v4_real_007"]`.

Warnings novos:

- `v4_real_006`: `tese_ia_desalinhada_com_objeto`;
- `v4_real_007`: `tese_cultura_desalinhada_com_objeto`.

Leitura:

O problema F7.1 deixou de ser `ok=true` silencioso. O lote continua aprovado em laboratorio, mas os itens 006 e 007 exigem revisao humana editorial antes de qualquer promocao como tese `ok`.

Validacao local:

- `OK 92 contract tests`;
- agentes strict OK;
- fluxo OK;
- preflight `promocao_shadow_aprovada`, `issues=[]`;
- batch multi-item OK com warnings editoriais.

Pacote:

`Projeto Cafezinho Agentes/root/v4_labs_fase7_f71_editorial_coherence_gate_20260710.tar.gz`

SHA256:

`6a67d25e64483347aed443fb590833466d4e82c7c6c6295744752729edda549c`

Tamanho: `1015K`.

Validacao em extracao limpa:

- sem `__pycache__` e sem `.pyc`;
- `OK 92 contract tests`;
- agentes strict OK;
- fluxo OK;
- preflight `promocao_shadow_aprovada`, `issues=[]`;
- `multi_item_lab_ok`;
- `editorial_review_required_items=["v4_real_006","v4_real_007"]`.

Status:

F7.1 tem politica editorial ratificada e gate lab implementado. A curadoria cultural propria ainda nao existe; proxima etapa natural e criar contrato/rota de curadoria por editoria e re-rodar `v4_real_007` ate a tese sair com eixo cultural concreto sem disparar `tese_cultura_desalinhada_com_objeto`.

## Auditoria F7.1 E Ajuste F7.2 - 2026-07-10

Auditoria externa do gate F7.1 recebida e registrada.

Veredito:

implementacao verificada e aprovada para continuidade em laboratorio.

Pontos confirmados pelo auditor:

- SHA256 do pacote F7.1 `6a67d25e64483347aed443fb590833466d4e82c7c6c6295744752729edda549c` confere;
- curadoria permanece congelada contra Fase 6/7 auditadas;
- gate foi construido ao lado da curadoria, sem alterar `curadoria_tese.py`;
- `OK 92 contract tests`;
- batch reexecutado como `multi_item_lab_ok`;
- `editorial_review_required_items=["v4_real_006","v4_real_007"]`;
- warnings esperados: `tese_ia_desalinhada_com_objeto` e `tese_cultura_desalinhada_com_objeto`;
- vocabulario de reporte padronizado em `external_publish`.

Ratificacao de Miguel:

Miguel confirmou em 2026-07-10 a politica interina: teses fora das familias calibradas sao rascunho com revisao humana obrigatoria ate existir curadoria propria por editoria ou gate forte de coerencia.

Com isso, F7.1 esta completamente respondido em laboratorio: decisao editorial tomada, gate de primeira linha implementado, revisao humana sinalizada mecanicamente no batch, e `v4_real_007` mantido como regressao canonica.

Achado menor F7.2:

o auditor identificou edge warning-only: tese vazia ou `teses_candidatas` ausente fazia o gate devolver `status=ok`. Em laboratorio o risco era baixo, mas o rotulo era enganoso.

Correcao F7.2 implementada:

- contrato `contratos/v4_editoria_coerencia_v1.json` ganhou `missing_tese_warning_id: tese_ausente`;
- `codigo/coerencia_editorial.py` agora retorna `status=warning` quando a tese aplicavel esta ausente ou vazia;
- warning emitido: `tese_ausente`;
- `human_review_required=true` segue a politica da editoria;
- teste novo `test_editorial_coherence_gate_tese_ausente_vira_warning`.

Validacao local F7.2:

- `OK 93 contract tests`;
- agentes strict OK;
- fluxo OK;
- preflight `promocao_shadow_aprovada`, `issues=[]`;
- batch `multi_item_lab_ok`, `issues=[]`;
- `editorial_review_required_items=["v4_real_006","v4_real_007"]`;
- sem WordPress real, sem publicacao externa, sem promocao real.

Pacote F7.2:

`Projeto Cafezinho Agentes/root/v4_labs_fase7_f72_tese_ausente_gate_20260710.tar.gz`

SHA256:

`46254c849f3cd656f61bc1d8f8e429436820c0f255b5aaf46f9e979e06fcdb5c`

Tamanho: `1015K`.

Validacao em extracao limpa:

- sem `__pycache__` e sem `.pyc`;
- `OK 93 contract tests`;
- agentes strict OK;
- fluxo OK;
- preflight `promocao_shadow_aprovada`, `issues=[]`;
- `multi_item_lab_ok`;
- `editorial_review_required_items=["v4_real_006","v4_real_007"]`.

Status consolidado:

F7.1 fechado para laboratorio. F7.2 corrigido. A proxima fase de desenvolvimento continua sendo a curadoria propria por editoria, com prioridade para cultura e regressao `v4_real_007`.
