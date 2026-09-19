# Fórum — Faxina: `motor_publicador.py` → LEGACY

**Data:** 2026-08-12 ~11:00 BRT
**Autor:** ZCode (GLM-5.2, fallback final — Kimi/Qwen 🔴🔴)
**Origem:** ordem direta do Miguel — *"o motor_publicador é legacy, o V4 substituiu; ele estava me confundindo. Tira ele de Nova York e do local, bota no Legacy, indexa certinho, faz o rollback."*
**Status:** ✅ **CONCLUÍDO E VALIDADO** (produção segura).

---

## Decisão

O `motor_publicador.py` (o "mestre único publicador" de 10 estágios) foi **aposentado** e movido pra `legacy/`, seguindo o mesmo padrão datado da faxina anterior que já tinha aposentado o `agente_controlado.py` (cutover V4 de 09/08). O runtime canônico V4 (`codigo.v4_vertical_redactor_runtime`, chamado por `v4_vertical_draft_worker.py`) é o publicador ativo há dias.

O Miguel corretamente apontou que eu havia me **confundido**: cheguei a montar um plano de "conselheiro de títulos" supondo que o `motor_publicador.py` + `gate_titulo.py` (cerco 09/08) vigoravam no fluxo de publicação. **Não vigoram** — estavam órfãos do cron. Esta faxina remove a confusão da raiz.

## O que foi feito

| # | Ação | Resultado |
|---|------|-----------|
| FASE 0 | Portão de segurança read-only: cron + cadeia V4 não dependem do motor | ✅ confirmado |
| 1 | Backup tar (rollback) no NYC | ✅ `faxina_motor_publicador_20260812_135635.tar.gz` (sha256 `dddabe66…f5575d`) |
| 2 | Mover NYC: `/root/motor_publicador.py` + 3 `.bak` → `/root/legacy/motor_publicador_aposentado_20260812/` | ✅ |
| 3 | Mover espelho local idem | ✅ |
| 4 | `gate_titulo.py` mantido no `/root` (autossuficiente, órfão de caller) | ✅ |
| 5 | Smoke: `py_compile` 9/9, `gate_titulo` importável, `import motor_publicador`→`ModuleNotFoundError`, crontab 35 linhas sem ref. | ✅ tudo verde |
| 6 | Indexação no Cérebro (`CODIGO_MORTO_INDEXADO` + `ATUALIZACOES`) | ✅ |

## Estado / próximos passos

- **Pronto:** motor_publicador fora do `/root` ativo (NYC + local), em legacy datado, com rollback e smoke verde. Produção V4 intacta.
- **Falta (decisão Miguel — fora de escapo desta faxina):** 14 agentes-irmãos legacy ficaram com `import motor_publicador` quebrado (nenhum no cron, não afetam runtime): `agente_crime`, `agente_lula`, `agente_master_geopolitica`, `agente_master_nacional`, `agente_reciclador`, `agente_latam`, `agente_matriz_energetica`, `agente_sheinbaum`, `agente_militar`, `agente_soberania`, `agente_ia`, `publish_caiado`, `agente_master_lula_legacy`, `agente_master_trends_legacy` + cópias em `/root/cafezinho/portal_cafezinho/`. → **próxima faxina decide** (mover pra legacy ou descartar).
- **Preciso de você (Miguel):** confirmar se quer que eu faça a próxima faxina dos 14 órfãos, ou se deixar sinalizado por enquanto.
- **Relembro (em espera):** o plano do **conselheiro de títulos** (Gemini 3.1 Pro, 100% consultivo) não foi aprovado; fica aguardando seu sinal — agora já sem a confusão do motor_publicador.

## Referências

- Memória técnica completa: `Memorias/memoria_faxina_motor_publicador_legacy_20260812.md`
- Cutover V4 original: `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`
- Padrão de faxina diária (Codex 11/08): `Foruns/forum_missao_faxina_diaria_legacy_20260811.md`

---

## 🔄 ADENDO — RESGATE do motor_publicador (12/08 ~18:45)

**Origem:** ordem Miguel — *"resgata o motor publicador. eu pedi pra levar pro legacy, houve pesquisa sobre sua utilidade... e ninguem falou nada"* (ninguém flagou que ele era **gatilho do enxame de comentários**, linhas 2770-2776).

**Diagnóstico pós-faxina (importante):** a faxina NÃO errou ao dizer que o motor_publicador era legacy de **publicação** — confirmado: **20 agentes o importam, mas NENHUM está no cron ativo** (foram substituídos pelo V4 `v4_vertical_draft_worker` em ~09/08). O que escapou a TODOS (ZCode/Codex/Claude) foi a **2ª função**: o motor_publicador **disparava o enxame** ao publicar. Como estava órfão, o **enxame já estava sem gatilho desde o cutover V4 (~09/08)** — não foi a faxina de hoje que o matou.

**Ação:** `motor_publicador.py` **resgatado** → copiado de `/root/legacy/motor_publicador_aposentado_20260812/` de volta pra `/root/`. `py_compile` ✅, `import motor_publicador` ✅ (130 símbolos). `gate_titulo.py` já estava em `/root`. Os 20 importadores voltam a funcionar. **Rollback:** os arquivos seguem no `legacy/` + tar `dddabe66…`.

⚠️ **Resgatar sozinho NÃO religa o enxame** (ninguém no cron chama o motor_publicador pra publicar/disparar). Para "acionar enxames na manchete + nacionais" é preciso um **gatilho do enxame** (a ser decidido: cron disparador independente, ou patch no fluxo V4). — ZCode (GLM-5.2)
