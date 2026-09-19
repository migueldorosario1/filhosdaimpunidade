---
name: feedback-cron-como-codigo-producao
description: "Cron é infraestrutura de produção, não bloco de texto auxiliar. Toda linha exige manifesto positivo, dono, pipeline, produtor+consumidor, custo, backup, diff revisado. Failover jamais restaura crontab inteiro sem revisão linha por linha."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-19 10:27 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra

**Cron deve ser tratado como código de produção. Toda linha exige:**

1. manifesto positivo (lista explícita do que está autorizado a rodar)
2. dono identificado
3. pipeline associado
4. produtor + consumidor pareados (produtor sem consumidor é incidente)
5. custo esperado documentado
6. estado autorizado registrado
7. diff revisado antes de aplicar
8. backup do estado anterior com hash
9. recibo de implantação

**Failover NUNCA deve significar "ligar tudo". Deve significar "ativar somente o conjunto atualmente autorizado".**

**Why:** Caso fundador em 2026-07-01. Miguel promoveu NYC (`198.199.121.136`) a servidor primário via script `/root/failover_armar_completo.sh`, que instalou o template `/root/crontab_failover_primary_complete.txt`. Esse template era um retrato antigo do cron completo de Cingapura — reativou 11 coletores legados (`robo_coleta_soberania`, `_militar`, `_latam`, `_sheinbaum`, `_ia`, `_matriz_energetica`, `_flavio_bolsonaro`, `_fantastico`, `_turismo`, `_sobrenatural`, `coletor_eleicoes`) que haviam sido pausados posteriormente em outros pontos do sistema.

Consequências (18 dias, até 19/07 pausa emergencial):
- produtores V3 ligados;
- consumidores correspondentes pausados no `maestro_distribuicao.py`;
- filas JSON crescendo sem consumo (IA 8.052 itens, matriz 988, soberania 406);
- 141.779 chamadas LLM em julho pelo `motor_coletor.py`;
- identidade perdida — biblioteca compartilhada gravava tudo como `motor_coletor:curadoria`;
- custo interno estimado US$ 380,42 (89,8% do total de julho US$ 423,73);
- R$ 98 no Gemini em 18/07 sem que Miguel soubesse a origem;
- ninguém deliberadamente ligou — foi automação ampla + template desatualizado + falta de autoria detalhada.

Miguel: "Automação ampla é mais perigosa que patch pequeno." (§19.3 da carta de passagem)

**How to apply:**

1. **Antes de instalar nova linha cron:**
   - Escrever manifesto positivo em `Cerebro/Foruns/manifesto_cron_YYYYMMDD.md` com dono/pipeline/produtor/consumidor/custo
   - Verificar produtor E consumidor ativos
   - Definir hard-stop financeiro
   - Corrigir telemetria (identidade real, não biblioteca)
   - Obter autorização Miguel explícita
   - Backup do cron atual com hash (`sha256sum`)
   - Aplicar diff mínimo (uma linha por vez preferencialmente)
   - Confirmar não afetou outras linhas
   - Registrar rollback seletivo (`sed` específico da linha, não `cp` do backup inteiro)

2. **Antes de restaurar crontab de backup:**
   - JAMAIS `crontab backup.txt` inteiro
   - Revisar linha por linha
   - Checar quais produtores/consumidores ainda existem
   - Aplicar apenas o subconjunto autorizado hoje

3. **Auditoria de cron (protocolo §14 da carta):**
   - Auditoria só-leitura primeiro em: cron root NYC, cron dos demais usuários, `/etc/cron.d`, timers systemd, serviços permanentes, processos sem cron, templates de failover, cron+serviços Tencent
   - Classificar cada linha: V4 / legado(V3) / Repetidor Estatal / site temático / infraestrutura / observabilidade / qualidade editorial / SEO+indexação / redes sociais / backup / desconhecido
   - Ação por linha: manter / reduzir frequência / pausar / duplicada / investigar
   - Apresentar matriz a Miguel antes de substituir cron

4. **Convenções de backup:**
   - Nome padrão: `/root/crontab_backup_pre_<motivo>_YYYYMMDD_HHMMSS.txt`
   - Sempre computar SHA-256 e registrar no ponto de retomada
   - Backup fica em `~/legacy/` também (redundância) quando material

5. **Sentinelas de identificação:**
   - Toda linha ativada por Claude Code deve ter comentário `# PAUSADO/ATIVADO_CLAUDE_MIGUEL_YYYYMMDD_<motivo>`
   - Segue padrão Codex `PAUSADO_CODEX_MIGUEL_20260719_LEGADO_SEM_CONSUMIDOR`

## Casos históricos aplicáveis

- **2026-07-01 → 2026-07-19:** failover NYC restaurou cron completo antigo, reativou coletores → incidente `motor_coletor:curadoria`
- **2026-07-19 09:09 BRT:** Codex pausou 11 coletores emergencialmente após auditoria dos R$ 98 Gemini
- **2026-06-28:** cron bulk meta description Gemini Flash instalado corretamente (linha única, custo esperado documentado, sentinela `CRON_SEO_META_RETROATIVO_GLM_20260628`)

## Relacionadas

- [[claude-engenheiro-chefe-ecossistema-20260719]]
- [[feedback-manifesto-antes-de-acao-grande]]
- [[feedback-biblioteca-nao-sobrescreve-identidade-agente]]
- Carta canônica §4-5, §14, §19.3 em `Cerebro/Foruns/carta_passagem_autoridade_codex_claude_20260719.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-19 10:27 BRT.
