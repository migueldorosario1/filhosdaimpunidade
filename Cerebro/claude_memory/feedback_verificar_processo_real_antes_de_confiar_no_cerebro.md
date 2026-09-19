---
name: feedback-verificar-processo-real-antes-de-confiar-no-cerebro
description: "Antes de auditar/recomendar deploy baseado em 'cérebro diz que script X está ativo', VERIFICAR cron/processo real do servidor. Cérebro pode ter defasagem silenciosa — caso fundador 28/07/2026 16:45 BRT motor_publicador"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Antes de auditar código para deploy OU recomendar restart/rollback baseado em "cérebro diz que script X está ativo em cron", **verificar o processo/cron REAL do servidor** (SSH + `crontab -l`, `systemctl status`, `ps aux | grep`, mtime dos arquivos). Cérebro pode ter defasagem silenciosa de dias/semanas — script pode ter sido desativado sem atualizar ATUALIZACOES.md.

**Como aplicar:**
1. Se auditoria/deploy vai afetar script mencionado no cérebro como "ativo", ANTES de emitir parecer: rodar checagem em NYC/Tencent — `ssh <servidor> "crontab -l | grep -i <script>; ls -la /root/<script>.py; ps aux | grep <script>"`.
2. Se defasagem detectada: corrigir cérebro (adicionar ⚠️ CORREÇÃO com timestamp) + reportar no fórum + memória.
3. Se defasagem NÃO detectada: prosseguir com deploy normal + registrar verificação no rastro do fórum.

**Why:** Caso fundador 28/07 15:30-16:45 BRT: ZCode pediu auditoria pra deploy `motor_publicador.py` + `flickr_live.py` (V3 Foto na Hora). Fiz auditoria técnica score 9/10 baseado em premissa que motor_publicador estava ativo (`CEREBRO_NODE_ATUALIZACOES.md` linha 156 de 26/07 dizia "agentes que usam util_fonte — motor_publicador, etc. — rodam via cron"). Miguel 15:47 questionou: *"motor publicador é... acho que ele está desautorizado"*. Investigação ZCode confirmou: **arquivos INTACTOS desde 21-23/06 nos 2 servidores (NYC+Tencent), zero cron, zero processo, zero log — MORTOS**. Auditoria técnica seguiu válida em qualidade mas mirou script morto. Deploy real ZCode foi em `painel_midia_ouro.py` (Tencent, código vivo). Cérebro corrigido linha 156 pós-descoberta.

**Lição meta:** memória do humano (Miguel: "está desativado") bateu cérebro escrito. Cérebro que descreve "quem roda o quê" tem shelf-life curta em ecossistema com refactor ativo — treatit as **snapshot in time**, não fonte de verdade atemporal. Verificação de processo real é o único ground truth.

**Casos de aplicação:**
- Auditoria de código pré-deploy → verificar se script alvo tem cron/processo ativo antes de aprovar
- Recomendação de rollback → verificar se o script problemático está mesmo rodando (pode já estar morto e problema é fantasma)
- Diagnóstico de bug em produção → não assumir que scripts do cérebro estão ativos; grep processo primeiro
- Refactor em massa → após terminar, atualizar cérebro linha por linha do que ficou vivo vs morto

**Anti-pattern:** basear parecer em `git log` + `ATUALIZACOES.md` + memória de reuniões sem SSH verificado.

**Regras irmãs:**
- [[feedback-sempre-pesquisar-web-em-duvida]] — mesma família: verificar realidade antes de afirmar
- [[feedback-autocura-protocolo-registro-com-solucao-e-rollback]] — protocolo padrão ouro exige testes reais, não só teóricos
- [[feedback-checagem-dupla-editorial-com-autonomia]] — autonomia com verificação, não com confiança cega em snapshots
