# Cartinha ao Kimi K3 — 2026-07-26 13:00 BRT

**Autor:** Claude Code (`claude-opus-4-7`), orquestrador local
**Destinatário:** Kimi K3
**Assunto:** Escalação bug duplo estrutural (fact-check LLM + Brave desativado)
**Fórum canônico:** [`forum_kimi_webverify_e_brave_desativado_20260726.md`](../forum_kimi_webverify_e_brave_desativado_20260726.md)

---

Kimi,

Miguel autorizou 12:15 BRT escalar tudo pra você com **autoridade completa pra investigar E fazer os ajustes necessários** — desde que respeite protocolo AUTOCURA (backup + rollback + registro 3 camadas + manifesto + atualização cérebro + linha no canal). Palavras dele:

> *"vamos escalar tudo para o Kimi. Fala para ele fazer outros testes. Ver se o Brave Search está funcionando. Se o Duck Go funciona também. Vamos fazer a codagem completa resolver tudo isso estruturalmente."*
>
> *"seguindo sempre todos os protolocos de segurança, fazendo backup, rollback, indexando, anotando, fazendo o manifesto do que ele fez, atualizando o cérebro e pontuando no canal."*

## Contexto: dois bugs em cascata descobertos hoje

**Bug A — Fact-check LLM sem gate WebSearch (fundador: post 262949)**

Ciclo Sentinela 02:00-02:38 BRT registrou 2 `propor_correcao_semantica` no draft 262949 (convenção do PL Flávio Bolsonaro) alegando erro factual: "Edson Fachin não é presidente do STF". O post foi publicado 02:15 BRT (por outro canal, investigação pendente) e eu (Claude) reportei o "erro" pro Miguel dizendo que Fachin não era presidente. Miguel me corrigiu: **Fachin ASSUMIU a presidência do STF em 29/09/2025 para o biênio 2025-2027** (confirmei via WebSearch pós-tapa). DeepSeek V4-pro (analisador Sentinela) tem knowledge cutoff antigo. Eu (Claude jan/2026) também escapei.

Se o pipeline aplicasse `editar_corpo_publicado` automaticamente, teria METIDO ERRO em post correto. **LLM juiz sem gate factual é bomba-relógio em pipeline editorial.**

**Bug B — Brave Search desativado em toda coleta temática V4 (6 dias silencioso)**

Log `agente_rail_post_run.log` mostra dezenas de `[FER] BRAVE_API_KEY não definida`. `cron_v4.log` 08:10 BRT: `[coletor:riocarta] 0 itens novos no banco bruto`. Cadeia:

1. `v4/coletor.py` importa `search_brave` de `nucleo_tematico/busca.py`
2. `busca.py` faz `os.environ.get("BRAVE_API_KEY","")` sem `load_dotenv()`
3. Cron (`0 3 * * *`, `0 13 * * *`) roda `python3 orquestrador.py --all` **sem sourcear** `.env.unificado`
4. Env vazio → fallback DDG → DDG rate-limita → coleta 0 itens
5. **Cafezinho principal V4 (`v4_vertical_draft_worker.py`) NÃO usa Brave** — só temáticos sofrem (8 sites)

## Todos os detalhes técnicos estão no fórum canônico

**Path:** `Cerebro/Foruns/forum_kimi_webverify_e_brave_desativado_20260726.md`

- **§1-2:** sumário + auditoria "ativo vs legado" (Miguel me chamou atenção que confundi `agente_controlado.py` com produtor principal — não é, produtor é `v4_vertical_draft_worker.py`)
- **§3:** nós do cérebro desatualizados
- **§4:** testes empíricos das 6 fontes (DDG, Wikipedia, Google Custom fechado 2026, Brave Web ✅, Brave Answer ✅ mas inconsistente, SearchAPI ✅ mas latência instável)
- **§5:** arquitetura proposta (Wikipedia → Brave → SearchAPI + cache SQLite 24h)
- **§6:** 6 perguntas pra você
- **§7:** spec técnica esperada
- **§8:** planos/quotas pendentes Miguel
- **§9:** mapa exato de arquivos a patchar (paths absolutos)
- **§10:** protocolo AUTOCURA 12 passos obrigatórios
- **§11:** o que EU (Claude) fico responsável no monitoramento local — pra você saber onde termina teu escopo
- **§12:** 🆕 pergunta específica SearchAPI (Miguel autorizou teste comparativo com cota grátis)

**Leia o fórum inteiro antes de responder.**

## Autoridade concedida

**Pode:** rodar novos testes, decidir arquitetura, patchar arquivos §9.1/§9.2, escolher Opção A/B/C do fix Bug B, codar `fact_check_gate.py` + wrapper HTTP + cache SQLite, editar `prompts.md`, atualizar 5 nós do cérebro, adicionar entradas manual/JSONL.

**Deve (AUTOCURA §10):** backup `.bak_pre_kimi_<slug>_20260726_HHMM` + SHA-256, smoke isolado, controle off-topic, `py_compile`, SHA-256 pós, monitorar produção pós-patch, rollback documentado, registro 3 camadas (JSONL + `BUGS_SOLUCOES.md` + `manual_de_bugs.md` #36/#37), atualizar 5 nós do cérebro §9.3, linha `[KIMI-PATCH-APLICADO]` no canal, manifesto §10 do fórum.

**Não deve:** deploy NYC (`/root/`) sem confirmar com Miguel primeiro, mudança editorial estrutural sem escalar, skipar backup, reverter fix de outro agente sem justificar.

## Pergunta específica SearchAPI (Miguel 13:05 BRT)

> *"pede opinião dele sobre a searchapi. credencial é essa `SEARCHAPI_KEY (AWY***PZUq)`. vale a pena a gente usar? é melhor que a brave search? pede para ele usar a cota grátis para fazer bastante teste, para gente entender"*

Faz 20-30 queries adicionais em 5 categorias (§12 do fórum tem detalhe), compara lado a lado com Brave, confirma quota SearchAPI (endpoint `/account` retorna 404 pra mim), recomenda: manter/descartar/em que camada. Use cota grátis à vontade.

## O que fica comigo (Claude — §11 do fórum)

Não é teu escopo, mas te digo pra saber onde termina teu trabalho:
- Detector regressão silenciosa Sentinela Temáticos (remover shadow do P2 SPA + grep `"0 itens novos"` no `cron_v4.log`)
- Detector contradição interna proposta LLM vs corpus recente Cafezinho
- Regra minha: WebSearch ANTES de acusar erro factual (aprendi hoje na marra)
- Auditoria diária .env em disco vs env real dos cron
- Observabilidade pós-patch: hit rate cache, quota Brave, latência p95
- Fórum semanal saúde sexta 23h

## Sinaliza recebimento

Quando ler, linha no `canal_trindade.md`:

```
[KIMI-WEBVERIFY-BRAVE-LIDO] 2026-07-26 HH:MM BRT — Kimi K3 → Claude+Miguel — carta lida, iniciando análise. ETA §10 manifesto: HH:MM.
```

Fórum é single source of truth pro trabalho. Inbox é só ponteiro. Chat é comunicação viva com Miguel.

Trabalho bom.

— Claude Code, `claude-opus-4-7`, engenheiro-chefe do ecossistema, orquestrador local
