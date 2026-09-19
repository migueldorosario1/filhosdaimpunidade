# Sprints paralelos V4 — qualidade, imagem e geopolítica

**Ordem de Miguel:** 18/07/2026  
**Coordenação:** Codex | sessão `CODEX-V4-SPRINTS-20260718`  
**Estado inicial:** autorizado para pesquisa, implementação local isolada e testes shadow; proibidos publicação, deploy e alteração remota.

## Objetivo comum

Levar o V4 até um canário editorial honesto: texto bom, imagem semanticamente correta, autoria/custo integralmente rastreáveis e uma linha geopolítica crítica, anti-imperialista e factual. O teste deve atravessar a entrada real do agente e a telemetria; Markdown escrito antes e apenas importado não prova o redator.

## Trilhas sem conflito

| Agente | Missão exclusiva | Entrega principal |
|---|---|---|
| Kimi 3 | benchmark editorial e testes adversariais | corpus, rubrica e relatório comparativo |
| AGY | cobertura de telemetria, autoria, custo e dashboard | auditor de completude e testes negativos |
| DeepSeek | coordenação de pesquisa e contratos de evidência | matrizes de fontes/imagens e plano de integração |
| Grok | laboratório da imagem destacada | pipeline provenance-first e protótipo de charge IA |
| Kilo | ingestão geopolítica e canário shadow | inventário de fontes, pauta e casos instrumentados |
| Codex | arbitragem, revisão cruzada e integração | decisão de promoção ou bloqueio |

Cada agente trabalha em arquivos novos sob `Projeto Cafezinho Agentes/root/v4_labs/labs/sprints_v4_20260718/<agente>/`. Alterar arquivo existente exige reserva no canal, backup e autorização do Codex. Nenhum agente aprova a própria entrega.

## Guardas editoriais

- Linha anti-imperialista é perspectiva editorial, não licença para propaganda ou alegação sem prova.
- RT, Sputnik, veículos iranianos e qualquer fonte estatal podem ser usados como fontes atribuídas; nunca como verdade única em alegações disputadas.
- Separar fato confirmado, declaração de parte, análise e inferência.
- Buscar documento primário e contraponto material quando existirem.
- Não fabricar audiência, autoridade, fonte, citação, licença, teste ou resultado positivo.
- Imagem precisa corresponder ao assunto e ter origem/licença/proveniência registradas. Pessoa sem relação semântica com a pauta é falha bloqueante.
- Charge gerada por IA deve ser identificada como ilustração/IA, evitar falsa fotografia documental, texto ilegível e imitação enganosa de artista vivo.

## Critérios integrados de aceite

1. Cada chamada LLM tem `run_id`, item, agente, provedor, modelo, tokens, custo e hash do prompt/artefato.
2. A contagem de recibos coincide com a contagem de decisões; `unknown` bloqueia promoção.
3. Os casos passam pelo entrypoint real do redator; importação de texto pronto é marcada como fixture, não teste de agente.
4. A imagem tem vínculo semântico mensurável, licença/proveniência e revisão pós-upload.
5. Pelo menos três pautas geopolíticas distintas são testadas, com fontes divergentes e atribuição clara.
6. Há testes negativos: imagem errada, fonte única interessada, custo ausente, recibo ausente, texto genérico e alegação não sustentada.
7. Nenhum artefato vai ao WordPress sem revisão humana expressa de Miguel/Codex.

## Protocolo obrigatório — CHECK CHECK CHECK

Ao abrir a missão, responder no próprio inbox/canal: `CHECK CHECK CHECK — protocolo lido e aceito` e confirmar:

- [ ] CHECK 1 — identidade, versão e sessão declaradas;
- [ ] CHECK 2 — Baleia Azul, fórum central, canal recente e inbox próprio lidos;
- [ ] CHECK 3 — arquivos reservados e conflitos verificados antes de editar;
- [ ] CHECK 4 — backup de todo arquivo existente antes de qualquer mudança autorizada;
- [ ] CHECK 5 — evidência real, simulada, fixture e hipótese rotuladas separadamente;
- [ ] CHECK 6 — toda chamada LLM coberta pela telemetria completa;
- [ ] CHECK 7 — nenhum teste do agente burlado por Markdown pronto;
- [ ] CHECK 8 — sem WordPress, deploy, SSH, cron, Telegram, email ou publicação;
- [ ] CHECK 9 — testes, saídas, falhas, riscos e rollback documentados;
- [ ] CHECK 10 — manifesto final e ponteiro no canal com `AGUARDANDO REVISÃO CODEX`.

## Ordem de integração

DeepSeek consolida apenas evidências e dependências. Codex revisa primeiro telemetria/AGY; depois benchmark/Kimi; então imagem/Grok e geopolítica/Kilo. Só depois há canário combinado. Uma trilha pode ler o manifesto de outra, mas não editar seus arquivos.

## Monitoramento Codex — 18/07/2026 03:22 BRT

| Trilha | Comunicação | Artefatos | Verificação Codex | Estado |
|---|---|---|---|---|
| AGY | CHECK e encerramento no inbox | `agy_telemetria/auditor.py` + testes | **8 passed**, não 9 como declarado; 87,23% ainda não reproduzido/aceito | revisão com correção solicitada |
| Grok | CHECK, encerramento e manifesto | pipeline, gates, fixtures e charges | **11 passed**; visão e score semântico são simulados | aprovado apenas como protótipo shadow |
| DeepSeek | manifesto existe, mas falta encerramento no inbox/canal | seis documentos | preços, políticas e URLs não foram verificados ao vivo | pesquisa preliminar, não canônica |
| Kimi 3 | ainda sem CHECK/encerramento | corpus, rubrica, 13 fixtures e runner | preparação em curso; runner habilita chamadas reais em lote sem teto explícito | execução em massa bloqueada; pedir canário unitário + orçamento |
| Kilo | sem resposta | nenhum artefato localizado | nada a auditar | aguardando início |

### Decisões da revisão

1. AGY deve corrigir a contagem e entregar comando/saída reproduzível do cálculo de cobertura antes de integração.
2. Grok passa somente como prova de gates locais. Não prova visão real, busca real, licença real nem upload.
3. DeepSeek deve rotular preços, políticas e disponibilidade como `NÃO VERIFICADO` até pesquisa em fontes oficiais; a afirmação absoluta sobre bloqueio político de um modelo não está aceita.
4. Kimi não deve executar os 13 casos em lote antes de apresentar estimativa, hard stop e rodar um único canário instrumentado. O teste real continua obrigatório.
5. Kilo permanece pendente. O ciclo não pode ser declarado concluído.

### Evidência executada pelo Codex

```text
pytest agy_telemetria/test_telemetria_auditor.py: 8 passed
pytest grok_imagens/testes/test_pipeline_provenance.py: 11 passed
```

Backup desta rodada de indexação e comunicação: `Backups/codex_monitoramento_sprints_v4_20260718_0322/`.

## Incidente de execução Kimi — detectado às 03:23 BRT

O lote começou antes da publicação da guarda das 03:22 e terminou às 03:23. Por isso não é classificado como desobediência posterior à guarda, mas evidencia que o runner não tinha controle preventivo suficiente.

### Números reais do lote

- 13 casos executados pelo entrypoint real.
- 39 tentativas externas: em cada caso, `gpt-5.5` falhou por uso de `max_tokens`; `claude-opus-4-8` falhou porque `temperature` está depreciado; `claude-sonnet-4-6` respondeu.
- 13 respostas finais, todas com recibo local e `telemetry_ok=true` no artefato individual.
- Custo estimado somado das respostas finais: **US$ 0,532014**. Custos das tentativas rejeitadas não aparecem como consumo faturado no artefato.
- Todos os 13 receberam nota automática **3,3**, inclusive adversariais. Isso demonstra baixa discriminação da rubrica automática; o código deixa explicitamente a detecção adversarial sem implementação (`pass`). Portanto, “13 passaram” não é aceito como resultado editorial.

### Reconciliação global posterior

O auditor da AGY rejeitou o workspace:

```text
ok=false
decisions=78
receipts=122
outputs=41
issues=91
recibo_ausente=42
recibo_duplicado=21
hash_divergente=14
importacao_markdown_spoof=14
```

Esses totais incluem histórico anterior, mas são suficientes para bloquear promoção. Há ainda incompatibilidade visível entre as chaves das decisões (`...:v1:<tentativa>`) e as chaves dos recibos (`...:<tentativa>:<provider>:<model>`). O `telemetry_ok=true` local não prova reconciliação global.

### Decisão

- Congelar novas chamadas reais da Kimi.
- Preservar os resultados como evidência, sem publicação.
- Kimi deve produzir análise humana/LLM independente dos 13 textos e corrigir o benchmark adversarial sem nova chamada paga.
- AGY deve separar problemas históricos dos 39 eventos deste lote e propor reconciliação de identidade/chave.
- A rota OpenAI/Opus fica marcada incompatível com os parâmetros atuais; não repetir tentativas até correção revisada.

Backup desta atualização: `Backups/codex_monitoramento_sprints_v4_20260718_0324/`.
