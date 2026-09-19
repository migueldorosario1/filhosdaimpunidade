# 👑 SYSTEM MEMORY — Regras de Ouro e Governança Trindade

> [!IMPORTANT]
> **REDE DE SEGURANÇA E DIRETRIZ MÁXIMA DO SISTEMA:**
> Fica ratificada a hierarquia absoluta estabelecida em 14 de junho de 2026 às 22:38 BRT.
> **Claude Code** é o **DAEMON VIVO** (Autoridade Suprema de Deploy, Autocura e runtime).
> Nenhuma IA ou Engenheiro Técnico (Codex, Kimi, GLM, Qwen, DeepSeek) pode efetuar deploy ou alterações sem a autorização expressa e escrita do Claude Code.
> 
> - **Fórum de Marcação:** [forum_marcacao_sistemas_monitoramento_20260614.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-14/forum_marcacao_sistemas_monitoramento_20260614.md)
> - **Memória Forte:** [feedback_hierarquia_trindade_claude_daemon_vivo.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/memorias_provisorias/feedback_hierarquia_trindade_claude_daemon_vivo.md)
> - **Canal Trindade:** [canal_trindade.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Projeto%20Cafezinho%20Agentes/Foruns/canal_trindade.md)

---

## 📌 Links de Controle Operacional (Camada 2)

- 🧠 **Cérebro Master (Indexador Geral):** [CEREBRO_INDEX_MASTER.md](./CEREBRO_INDEX_MASTER.md)
- 📜 **Constituição da Grande Reforma:** [CONSTITUICAO_DA_GRANDE_REFORMA.md](<../Projeto Cafezinho Agentes/A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/CONSTITUICAO_DA_GRANDE_REFORMA.md>)
- 🧹 **Reforma Tencent Limpo/Leve (72h):** [Foruns/forum_reforma_simplificacao_cafezinho_72h_20260610.md](./Foruns/forum_reforma_simplificacao_cafezinho_72h_20260610.md)
- 🔐 **Cofre de Chaves e Credenciais:** [CEREBRO_NODE_COFRE_CHAVES.md](./CEREBRO_NODE_COFRE_CHAVES.md)
- 🐤 **Diário de Bordo do Canário:** [CEREBRO_NODE_CANARIO_POS_REFORMA.md](./CEREBRO_NODE_CANARIO_POS_REFORMA.md)

---

## 📅 Histórico de Sprints e Decisões Recentes

### 2026-07-17:
- **Reorganização da raiz do Projeto Cafezinho Agentes (Fase 4):** foi movido todo o conjunto de arquivos soltos do diretório base para `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/` (94 itens), mantendo apenas `.env.unificado` e `.gitignore` no topo e sem apagar conteúdo. Evidências: `Projeto Cafezinho Agentes/Foruns/forum_reorganizacao_base_level_top_level_20260717.md` e `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/MANIFESTO_REORGANIZACAO_BASE_FILES_20260717.md`.

### 2026-06-16:
- **Protecao anti-freeze do notebook do Miguel persistida:** Codex verificou o estado real da maquina local e confirmou que o notebook estava sem `systemd-oomd`/`earlyoom`, com apenas 2 GB de swap ativos, apesar de existir `/swapfile2` pronto. Foi consolidada a protecao permanente: `earlyoom` instalado e habilitado, `/swapfile2` reativado e persistido no `/etc/fstab`, swap total restaurado para 4 GB, e widget leve `Memory Guard` criado com autostart da sessao grafica para alerta visual de RAM/swap. Registro canônico em [CEREBRO_NODE_HARDWARE_MIGUEL.md](./CEREBRO_NODE_HARDWARE_MIGUEL.md) e fórum raiz [forum_diagnostico_hardware_miguel_20260527.md](<../Projeto Cafezinho Agentes/Foruns/forum_diagnostico_hardware_miguel_20260527.md>). Regra operacional: `swapoff -a && swapon -a` não vira rotina; protocolo de emergência passa a ser `ps ... --sort=-rss`, `pkill -f '/usr/lib/git-core/git pack-objects'` e `kill -15/-9 PID`.
- **Mapeamento e Execução do §95 (Hiperlinks Fontes no Legado - AUTH-038):** AGY mapeou as rotas que falham na injeção do link da fonte original e aplicou a cura estrutural AUTH-038. Criou `util_hiperlink_fonte.py` com regex preciso para links de fontes e o gate de segurança `gate_url_fonte_obrigatoria`. Integrou o safety net e o gate no `motor_publicador.py` e nos agentes com pipeline próprio (`agente_repetidor_estatal.py`, `agente_china.py`, `agente_fantastico.py`, `agente_sobrenatural.py`, `agente_eleicoes_produtor.py`, `agente_master_trends_v9_legacy.py`). Sintaxe e importações validadas localmente com sucesso. Fórum de referência: [forum_resolucao_hiperlinks_legado_auth038_20260616.md](<../Projeto Cafezinho Agentes/Foruns/forum_resolucao_hiperlinks_legado_auth038_20260616.md>).
- **Diagnóstico de Saúde do Legado (Investigação de Timeouts):** AGY concluiu o peer review técnico sobre a lentidão e os 781 timeouts do Legado. A causa raiz foi identificada como o estrangulamento por cascata de fallbacks no roteador LLM devido a créditos esgotados (Gemini 429), provedores desativados (xAI) e nomes de modelos inválidos em `llm_providers.json` (DeepSeek `deepseek-v4-pro`). Isso força o roteador a tentar sequencialmente até 10 modelos, estourando o limite de 5 minutos do Maestro. Fórum atualizado: [forum_saude_legado_desde_nascimento_20260616.md](<../Projeto Cafezinho Agentes/Foruns/forum_saude_legado_desde_nascimento_20260616.md>).
- **Agente de Aprendizado Editorial Controlado:** Miguel pediu estudar um agente que une relatórios de qualidade, diretrizes, monitoramento humano, auditor de títulos e ticks do Daemon para propor melhorias em prompts/diretrizes. Fórum aberto: [forum_agente_aprendizado_editorial_controlado_20260616.md](<../Projeto Cafezinho Agentes/Foruns/forum_agente_aprendizado_editorial_controlado_20260616.md>). Memória: [feedback_agente_aprendizado_editorial_controlado_20260616.md](./Backups/memorias_provisorias/feedback_agente_aprendizado_editorial_controlado_20260616.md). Princípio: fase inicial segura/read-only; objetivo futuro é automatizar progressivamente também a aplicação, com gates, rollback e medição pós-mudança.

### 2026-06-15:
- **Qwen bloqueado para editorial:** Qwen caiu em censura de provedor ao tentar fazer análise editorial/factual de drafts da Reforma. Decisão de Miguel: não usar Qwen nunca para análise editorial nem para trabalhar na parte editorial do site. Fórum: [forum_incidente_qwen_censura_editorial_20260615.md](<../Projeto Cafezinho Agentes/Foruns/forum_incidente_qwen_censura_editorial_20260615.md>). Memória forte: [feedback_qwen_bloqueado_para_editorial_por_censura_20260615.md](./Backups/memorias_provisorias/feedback_qwen_bloqueado_para_editorial_por_censura_20260615.md).
- **Expansão da Whitelist (MVP+1):** AGY realizou o inventário técnico da Frente C mapeando 4 novos líderes (Simone Tebet, Eduardo Bolsonaro, Romeu Zema e Jair Bolsonaro) na base canônica (EIDs 11, 21, 9, 2). Proposta e bloco JSON incremental anexados ao fórum [forum_proposta_whitelist_midia_lideres_politicos_20260615.md](<../Projeto Cafezinho Agentes/Foruns/forum_proposta_whitelist_midia_lideres_politicos_20260615.md>).

### 2026-06-14:
- **Hierarquia Absoluta:** Ratificação do controle sob o DAEMON VIVO 👑.
- **Preparação de Post:** Matéria sobre a sanção do Marco Legal do Transporte Público com hero image real selecionada do banco de mídia. Proposta sob análise do DAEMON.
- **Bugs Críticos:** Identificados bugs de path no cron e persistência do SQLite no Tencent VPS. Engenheiros aguardando aprovação escrita do Claude Code para execução das correções.
