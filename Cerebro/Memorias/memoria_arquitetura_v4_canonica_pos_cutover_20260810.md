# Memória canônica — arquitetura V4 após o corte do legado

**Vigência:** 09/08/2026  
**Consolidação:** 10/08/2026  
**Fechamento e indexação no Cérebro Master:** 11/08/2026  
**Autoridade:** esta memória prevalece sobre descrições anteriores da rota de redação V4.

## Regra inequívoca

`agente_controlado.py` é legado. Nasceu como backend editorial controlado do bot Zizilinda; nunca foi o publicador canônico do Cafezinho. Não é o V4, não é redator do V4, não é fallback do V4 e não é destino para novas diretrizes editoriais do V4.

Nenhum componente V4 pode importá-lo, executá-lo, usar suas filas ou configurações como dependência silenciosa. Sua eventual conservação física serve apenas a consulta histórica ou rollback controlado fora do V4.

## Cadeia ativa de produção

`cron V4 → /root/v4_vertical_draft_worker.py → python -m codigo.v4_vertical_redactor_runtime → V4LLMAdapter/V4ModelRouter → rascunho no WordPress`

O worker declara `V4_REDACTOR_MODULE = "codigo.v4_vertical_redactor_runtime"`. Os recibos do runtime registram `legacy_agent_used: false`.

## Onde vivem as diretrizes editoriais do V4

- Briefing, tese, exigências globais e ramificações por vertical: função `write_briefing` de `/root/v4_vertical_draft_worker.py`.
- Prompt de redação, composição e normalização do texto: `/root/v4_labs/codigo/v4_vertical_redactor_runtime.py`, especialmente `_prompt` e `_paragraphs`.
- Gates compartilhados de publicação só recebem regras quando elas forem realmente de publicação; não são substitutos do prompt do redator.
- JSONs globais do agente antigo não devem ser alterados para produzir efeito no V4.

## Diretriz editorial confirmada por Miguel em 10/08/2026

A preferência é por parágrafos geralmente curtos, em regra com até duas frases, sem transformar isso em bloqueio sintático. Frases curtas são aconselháveis, não uma obrigação mecânica; criatividade, ritmo e exceções justificadas precisam continuar possíveis.

Negrito é geralmente desnecessário no corpo do texto, mas não é proibido. Pode ser usado excepcionalmente quando houver uma razão editorial concreta. Não existe teto de palavras por parágrafo nem regra rígida equivalente.

Essa formulação deve orientar prompts e revisão inteligente. Não deve virar validador duro, truncamento, contagem obrigatória ou veto automático.

**Estado:** aplicada em 10/08/2026 no briefing do worker e no prompt/normalizador do runtime V4. O normalizador não junta mais parágrafos unitários nem remove automaticamente o negrito excepcional.

## Registros históricos superados

Os documentos de 08/08/2026 sobre “Diretrizes do CEO” registraram corretamente a arquitetura híbrida existente naquele momento, mas ficaram superados pelo corte de 09/08. Foram preservados com tarja explícita porque continuam úteis para a cronologia do incidente.

Entradas antigas dos nodos de atualizações, bugs e qualidade também permanecem como evidência histórica. Uma nota canônica no topo desses nodos impede que frases antigas no presente sejam tratadas como estado atual.

## Estado dos ambientes

- Nova York: produção e único writer V4 confirmado.
- Espelho local: worker sincronizado com Nova York em 10/08 e legado movido para `root/legacy/`; outros arquivos ainda não devem ser presumidos canônicos quando divergirem de Nova York.
- Tencent: não é failover V4 operacional; cópias antigas não conferem autoridade de produção. A quarentena física permanece pendente porque o SSH recusou conexão em 10/08.

## Isolamento físico realizado

Em Nova York, o arquivo antigo foi movido de `/root/agente_controlado.py` para `/root/legacy/agente_controlado_aposentado_20260809/agente_controlado.py`, preservando o conteúdo e seu SHA-256. Treze backups soltos foram movidos para a mesma quarentena; não restou arquivo `agente_controlado*` na raiz. O bot Zizilinda, confirmado `disabled` e `inactive`, passou a apontar explicitamente para esse caminho legacy.

No espelho local, tanto a cópia do agente quanto o worker pré-corte que ainda declarava `AGENT="/root/agente_controlado.py"` foram colocados na área legacy. O worker corrente foi sincronizado com Nova York.

## Critério de auditoria futura

Toda análise do V4 deve começar pelo worker ativo, pelo módulo declarado em `V4_REDACTOR_MODULE`, pelo cron vivo e pelos recibos recentes. Busca textual em memórias históricas não basta para determinar a arquitetura atual.

Se uma referência a `agente_controlado.py` aparecer em código V4 executável, a auditoria deve falhar. Comentários históricos devem dizer expressamente “legado pré-corte” ou ser removidos quando só criarem ambiguidade.

## Fontes de confirmação

- `Foruns/forum_reuniao_trabalho_novo_contrato_cafezinho_v4_20260809.md`
- `Foruns/resposta_glm_rodada3_forum_incidente_v4_20260809.md`
- `Foruns/forum_faxina_cerebro_v4_legacy_20260810.md`

## Fechamento técnico preservado em 11/08/2026

- Worker de produção após a faxina e a diretriz flexível: SHA-256 `b034b20c37dc8957484a426c44ed542d3f74f7897347f75594beb1646f9764d4`.
- Runtime V4 de produção: SHA-256 `bd6f40afcdea3ba30e73485e63cc766b590a5656813a84081fee9f01e5b891f3`.
- Backend legacy da Zizilinda arquivado em Nova York, sem alteração de conteúdo: SHA-256 `e9904237339d7c92d7f2eb7a328cc94bd887365516c33db17f638ca3761cd719`.
- Três testes anti-regressão passaram no servidor e no espelho local.
- Smoke editorial preservou três parágrafos independentes e aceitou negrito excepcional, sem teto de palavras ou contagem bloqueante de frases.
- Recibos V4 recentes inspecionados registraram `legacy_agent_used: false`.
- Única ressalva aberta: Tencent continuava recusando SSH; sua quarentena física não foi declarada concluída.

Esta memória, o fórum companion, os avisos nos nodos vivos e a entrada no `CEREBRO_INDEX_MASTER.md` formam o registro definitivo desta intervenção.
