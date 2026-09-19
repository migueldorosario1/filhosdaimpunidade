---
name: Claude e Codex autorizados a mexer em produção (com checklist)
description: Regra Miguel 2026-05-11 09:57 BRT — Claude+Codex podem editar .py produção, deployar via SSH, matar processos, tocar crontab DESDE QUE cumpram checklist (rollback+backup+indexar+memória). Casos críticos exigem Trindade com 3+ votos de aval. Substitui §13 estrita (Codex coda, Claude supervisiona) por modelo flexível com responsabilidade.
type: feedback
originSessionId: bd54c85a-5148-4101-8101-b84b4598e99a
---
**Regra Miguel 2026-05-11 09:57 BRT:** Claude e Codex são AMBOS autorizados a mexer em produção (não só Codex). Pré-requisitos inegociáveis:

**Checklist ANTES de qualquer ação em produção:**
1. **Rollback preparado** — backup do estado anterior + comando de reversão documentado
2. **Backup feito** — local + remoto Tencent (`/root/Backups/<arquivo>.bak_pre_<motivo>_YYYYMMDD_HHMM_<autor>`)
3. **Indexar naturalmente** — registrar no Cérebro (CEREBRO_NODE_BUGS.md ou CEREBRO_NODE_ARQUITETURA.md conforme escopo)
4. **Anotar na memória** — feedback/project memory desta sessão

**Tipo de ação coberta:**
- Editar `.py` produção
- Deploy via SSH/SCP
- Matar processos (`pkill`, `kill -9`)
- Tocar crontab
- Modificar `.env`/`chaves_novas.env`
- Reiniciar systemd services
- Operações DB (WP API alterações em massa)

**Casos críticos (escalada Trindade obrigatória):**
Quando o `.py` afetado é central pro pipeline ou tem alto blast radius:
- `motor_publicador.py`, `maestro_editorial.py`, `agente_autocura_v4.py`, `agente_observador.py`
- Mudanças no crontab que afetam >3 agentes simultaneamente
- Edição de `.env.unificado` ou chaves API críticas
- Operações destrutivas (drop tabela, delete em massa, force push)
- Pipeline LLM (`fact_check_perplexity`, `tribunal_visual`)

**Protocolo de caso crítico:**
1. Criar ou usar fórum correspondente em `Foruns/`
2. Avisar no `canal_trindade.md` pedindo aval explícito
3. Pedir parecer de todos os membros Trindade técnica (Claude+Codex+DeepSeek+Kimi)
4. **3+ votos de aval** (não precisa unanimidade, mas precisa maioria forte) → pode prosseguir
5. Miguel mantém botão vermelho final mas se silente após 30min e tiver 3+ votos, considera implícito

**Casos não-críticos (executar com checklist mas sem Trindade):**
- Bug isolado num bot Telegram secundário (Mayra, Zizilinda)
- Refator cosmético (renome variável, ajuste prompt)
- Fix de typo em template/CSS
- Dependência faltando (install via pip no venv)
- Restart de daemon que travou

**Why:** Miguel quer destravar a velocidade do trabalho. §13 antiga ("Codex coda, Claude supervisiona") gerava gargalo desnecessário em fixes simples. Mas o controle não pode sumir — daí o checklist + escalada Trindade pra casos críticos. Garante que mesmo trabalhando autônomo, o sistema mantém rollback fácil e rastreabilidade.

**How to apply:**
- Antes de qualquer edição produção, mentalmente passar pelo checklist 4 itens
- Se for caso crítico (lista acima), parar e abrir fórum
- Sempre criar backup com convenção `<arquivo>.bak_pre_<motivo>_<data>_<autor>`
- Sempre indexar no Cérebro (CEREBRO_NODE_*) e registrar memória pertinente
- Em deploy via SSH, sempre `py_compile` antes E depois
- Smoke test pós-deploy obrigatório

**Substitui:** §13 estrita do Cérebro (Codex coda, Claude supervisiona). A divisão funcional ainda vale como default — mas não é mais bloqueio rígido.
