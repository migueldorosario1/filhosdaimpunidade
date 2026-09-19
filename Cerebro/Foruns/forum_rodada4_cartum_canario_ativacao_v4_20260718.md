# V4 — Rodada 4: cartum composto e canário pronto para prova real

**Direção:** Miguel do Rosário  
**Coordenação e auditoria:** Codex  
**Sessão:** `CODEX-V4-R4-CARTUM-CANARIO-20260718`  
**Base:** estimativa de 74% concluído; 26% ainda falta; regressão de entrada com 348 testes verdes.  
**Objetivo:** fechar o cartum como produto visual composto, corrigir os bloqueios do canário e deixar pronta — mas não executar sem autorização — uma prova real controlada.

## Protocolo obrigatório

Resposta inicial:

`CHECK CHECK CHECK — R4 V4 LIDA E ACEITA`

Depois:

`AGENTE | DATA HORA BRT | SESSÃO | ESCOPO | ARQUIVOS RESERVADOS | PRIMEIRO COMANDO SEGURO`

Regras:

1. Ler este fórum, o fórum central, o painel vigente, o Canal Trindade e o próprio inbox.
2. Publicar no Canal somente ponteiro curto; detalhes e evidências ficam no manifesto/fórum.
3. Não assumir missão, identidade, voto, sessão ou arquivos de outro agente.
4. Backup antes de editar; diff pequeno; rollback explícito; não alterar teste para fazê-lo passar.
5. Não revelar nem imprimir credenciais. Somente nomes de variáveis são permitidos.
6. Sem deploy, SSH, cron/systemd, WordPress vivo, publicação, mensagem externa ou chamada paga sem autorização nova e explícita.
7. Não aprovar a própria entrega. Toda entrega termina `AGUARDANDO REVISÃO CODEX`.
8. Trabalho importante só encerra depois de gravar ponto de retomada e publicar no Canal:

`CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | caminho/do/arquivo.md`

Sem o último check: `ENTREGUE, MAS NÃO ENCERRADO`.

## Alerta permanente — Claude Code ≠ GLM/Ming

- **Claude Code:** agente Anthropic, integrador desta rodada.
- **GLM/Ming:** agente Zhipu AI, executado por wrapper próprio. O nome da superfície/CLI não o transforma em Claude.
- **GLM-5.2 externo:** terceira identidade separada.

Claude Code e GLM/Ming não compartilham autoria, sessão, missão, assinatura, voto ou autorização. Em dúvida: `IDENTIDADE NÃO CONFIRMADA` e pausa segura.

## Grok — compositor determinístico do cartum

Missão: implementar em lab isolado o compositor que recebe desenho limpo + texto aprovado + logo canônica + domínio e produz uma imagem final única.

Entregas:

- compositor local, sem rede, com entrada explícita do arquivo de logo;
- faixa inferior colada ao desenho, não legenda WordPress;
- uma ou duas frases, máximo de duas linhas visuais;
- `ocafezinho.com` e logo oficial obrigatórios;
- layouts 16:9 e compartilhamento social, com safe areas;
- tratamento de texto longo, acentos, contraste e miniatura de 320 px;
- fixtures usando logo-placeholder claramente marcada até DeepSeek validar o ativo oficial;
- testes determinísticos, hashes de saída e rollback.

Não gerar cartum pago nem escolher uma logo por semelhança.

## DeepSeek — ativo oficial, MIME, licença e visão

Missão: fechar a cadeia de confiança visual.

Entregas:

- localizar candidatos a logo do Cafezinho e provar qual é canônico; se não houver prova, declarar `LOGO_CANONICA_NAO_CONFIRMADA`;
- registrar arquivo, formato, dimensões, transparência, SHA-256 e origem;
- especificar filtro MIME/magic-bytes que rejeite PDF ou arquivo disfarçado de imagem;
- revisar semântica dos candidatos de mídia e separar pessoa, patrimônio, infraestrutura e conceito;
- atualizar shortlist de visão real com payload, custo estimado e limites, sem executar chamada paga;
- parecer independente sobre o compositor do Grok.

Pesquisa externa somente read-only, com links e datas.

## Kilo — canário geopolítico final e imutável

Missão: transformar `input_canario_geo_002_R3.json` no input exato aceito pelo redator real.

Entregas:

- validar contra o schema/código real, não contra lista presumida;
- completar ou mapear `estado_editorial`, `collection_request`, promessa, briefing e validações;
- preservar 10/10 claims com fonte, data, locator e triangulação;
- marcar contrapontos pendentes sem inventar fatos;
- fornecer uma ou duas frases candidatas para a faixa do cartum;
- produzir pacote final imutável e SHA-256.

Não escrever a matéria, não gerar imagem e não chamar modelo.

## Kimi 3 — tribunal do input correto e texto da faixa

Missão: reavaliar o arquivo R4 produzido pelo Kilo, não o arquivo FINAL antigo.

Entregas:

- registrar caminho e SHA-256 do input efetivamente avaliado;
- emitir `APTO_PARA_REDATOR` ou `BLOQUEADO` com razões reproduzíveis;
- avaliar novidade, tese, fluidez potencial, risco de texto artificial e coerência geopolítica;
- escolher ou editar levemente uma faixa contextual de uma ou duas frases;
- garantir que a faixa não repita título, não explique a piada e não invente fato;
- custo desta reavaliação: US$ 0, usando apenas artefatos existentes.

Não produzir nova matéria nem realizar outra bateria paga.

## AGY — auditoria pós-integração e recibo do cartum

Missão: auditar a integração real da R4 sem editar arquivos canônicos reservados.

Entregas:

- reconciliar decisão, tentativa, recibo, output, custo e mídia sob uma identidade canônica;
- incluir proveniência do desenho e da composição final como etapas distintas;
- verificar hashes do desenho, logo, texto da faixa e bitmap final;
- testar duplicata, colisão, retry, custo excedido e ausência de campos;
- resolver ou encaminhar com teste mínimo os bugs B-01/B-02;
- parecer independente sobre a cobertura da rodada nova.

Meta: 100% da R4 reconciliada, zero `unknown`, sem misturar histórico.

## Claude Code — Anthropic — integração e dry-run completo

**Alerta:** você é Claude Code/Anthropic; não é GLM/Ming/Zhipu.

Missão: integrar somente depois das entregas isoladas e revisáveis.

Entregas:

- corrigir o bloqueio MIME/PDF com testes;
- integrar o compositor aprovado à interface do pipeline, sem WordPress;
- preservar desenho original e produzir derivado composto rastreável;
- consumir o input aprovado por Kimi, telemetria AGY e contrato visual;
- executar dry-run completo e local: input → redator simulado/fixture → revisão → mídia → faixa → fila simulada;
- produzir comando único, matriz de entrada/saída, backup e rollback;
- preparar plano da futura prova real com teto de custo, sem executá-la.

Gate C, WordPress e chamada paga continuam bloqueados.

## GLM/Ming — Zhipu AI — caos controlado e autocura

**Alerta:** você é GLM/Ming/Zhipu; não é Claude Code/Anthropic, mesmo usando wrapper/CLI com nome semelhante.

Missão: atacar o compositor e a cadeia integrada com falhas simuladas, sem editar a integração de Claude.

Entregas:

- testes para logo ausente/corrompida, fonte ausente, texto longo, caractere inválido, imagem pequena, PDF disfarçado, hash divergente e disco sem espaço;
- confirmar que falha de faixa termina em `PAUSA_SEGURA` ou fallback explícito, nunca publicação silenciosa;
- testar kill switch, orçamento e idempotência do derivado final;
- registrar recomendações de autocura mecânica e reversível;
- auditar que nenhum sistema de notas 1–5 foi implementado antes do lançamento.

Não assumir nem executar a missão de integração do Claude Code.

## Codex — promoção e próximo gate

Codex irá:

1. conferir checks, reservas e colisões;
2. auditar logo, compositor, input, tribunal, telemetria e testes de caos;
3. reexecutar a regressão integrada;
4. atualizar percentual concluído/faltante;
5. decidir se há evidência para pedir a Miguel autorização de **uma** geração real com teto explícito;
6. manter WordPress e publicação bloqueados nesta rodada.

## Critério de encerramento da R4

- logo canônica confirmada ou bloqueio honesto documentado;
- compositor determinístico verde com fixtures;
- PDF rejeitado por conteúdo real, não apenas extensão;
- input correto aprovado pelo tribunal;
- telemetria e hashes reconciliados;
- dry-run completo reproduzível;
- zero efeito externo e custo US$ 0;
- todos os pontos de retomada gravados e publicados no Canal.

