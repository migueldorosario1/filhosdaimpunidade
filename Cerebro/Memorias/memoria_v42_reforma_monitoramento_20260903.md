# Memória — Reforma do V4.2 Estatística (NYC) + Monitoramento pelos Agentes

**Data:** 03/09/2026 ~01:45 BRT · **Sessão:** ZCode/GLM-5.3 (DSH us65) · **Ordem:** Miguel 02/09 ~20h ("melhorada no v4.2 estatística... vê se tá alucinando... reforma... tira a inteligência barata... DSN Ideias acompanha os posts").

## Fatos principais (o essencial em 6 linhas)

1. **Investigação:** 8 posts auditados; números 100% reais (Conferidos ComexStat/imprensa, FRED, BCB, Eurostat); 9 defeitos editoriais (título duplicado 400178=400265; 5 reciclagens do dado de julho; mensal→"acumulado 12m"; EUR→US$; GACC de fevereiro como "recorde"; etc.).
2. **Causa-raiz:** `escolher_tese()` devolvia sempre a primeira tese → mesma pauta todo dia.
3. **Reforma NYC (produção) 03/09 ~01h BRT:** 3 arquivos, backups em `backups_reforma_20260903/`; rodízio por frescor, gates de frescor/título, validador factual mecânico, regras 12–16 no prompt, cascata 6, legenda limpa, recibo com `gates_v42_reforma_20260903`. Código no repo: `Foruns/v42_monitor/nyc_codigo/`.
4. **Provas:** dry-run pegou "0,16%" inventado e recusou; rascunho 400299 (E2E draft) impecável; primeira publicação reformada 03/09 12:10 BRT.
5. **Vigia V4.2 no ar (us65 */15):** detecta post novo (cat 100005), audita mecânico+LLM, veredito no repo, pedido `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-<id>` pro DSN Ideias acompanhar, bloco na ponte de_ideias.md, Telegram pro Miguel. Retro-auditória dos 8 posts validou o motor (achou sozinho os 4 defeitos reais, zero falso positivo).
6. **DSC-052 cumprido para o vigia:** telemetria própria (`/root/agent_data/v42_monitor/telemetry.jsonl`), MEMORIA_VIVA, canal (Foruns/v42_monitor + ponte), memória própria (este arquivo + MEMORIA_VIVA).

## Lições técnicas transferíveis

- **Bug do "e" no regex:** unidade com classe negativa `[^e]` morre em "milhões" (tem "e"). Usar `.+?` até âncora (` em <data>`).
- **Escala > magnitude:** converter p/ bilhões pela palavra de escala ("milhões"→/1000), nunca pelo tamanho do número.
- **Sinal:** banco guarda déficit negativo; prosa cita magnitude ("déficit de 4,92") → candidatos também em valor absoluto.
- **Percentual de variação não é verificável a partir do post** (rodapé só traz o último valor) → validar na GERAÇÃO com pacote completo; no monitor, só absurdo >1000% + julgamento LLM.
- **Rodapé muda de formato** (virada 28/08): parser precisa dos dois padrões.
- **Telemetria/logging nunca derruba a operação** (try/except próprio em cada).
- **Cascata de LLM:** validador rígido + 1 provedor morto (gemini geo-bloqueado no NYC) esgota tentativas rápido → ciclar provedores até 6.
- **§131 PORTAL LIMPO:** prova de publish em produção = `--status-post draft` (invisível ao leitor, provável no WP admin).

## Onde está tudo

- Fórum completo: `Foruns/forum_v42_reforma_monitoramento_20260903.md`
- Vereditos retro: `Foruns/v42_monitor/vereditos/` · motor: `v42_checagens.py` · vigia: `v42_espelho_watcher.py`
- Ofício ao Ideias: `Foruns/v42_monitor/pedidos/2026-09-03_oficio_inicial_acompanhamento_v42.md`
- Rollback NYC: restaurar `backups_reforma_20260903/*.py` e py_compile.

## Pendências

- Ideias: processar ofício; adotar gates no V4.2 Investimento (DSC-051); revisar o motor.
- Miguel: apreciar rascunho 400299; assistir 1º ciclo reformado (12:10 BRT) + veredito do vigia.
- ZM: avaliar gate anti-eco de título para o V4.1 geral.
