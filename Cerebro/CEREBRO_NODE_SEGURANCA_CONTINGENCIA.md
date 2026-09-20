# 🛡️ NODO — SEGURANÇA & CONTINGÊNCIA DO ECOSSISTEMA

> Nodo Camada 2 do tema **Plano Total de Segurança & Contingência** (aberto por ordem do Miguel em 23/08/2026). Cobra TODO o ecossistema: Cafezinho, Cérebro, GitHub, Vercel, GoDaddy, GDrive, servidores, chaves LLM/API, Telegram/WhatsApp/Gmail, redes sociais.

## Documento-mestre (vivo)

- **Fórum:** `Foruns/forum_plano_seguranca_contingencia_20260823.md` — inventário da superfície, riscos, 8 pilares, **agenda 48h S1–S10** e estado da missão. É por aqui que se retoma o plano.
- **Memória (log técnico da abertura):** `Memorias/memoria_plano_seguranca_contingencia_20260823.md`

## Cadência

- Automação ZCode dispara **a cada 48h às 10:00** → prepara a próxima sessão, grava adendo no fórum (seção Histórico, append-only) e avisa o Miguel no Telegram.
- Sessão atrasada **desliza** a agenda; bloco só fecha com entregável gravado.
- Após S10 (fechamento da fase intensiva 12/09): manutenção **trimestral** (a definir na S10).

## Pilares do plano

P1 Identidade & Recuperação · P2 Segredos & Cofres · P3 Backups & Restore provado · P4 Domínios/DNS/E-mail · P5 Servidores · P6 Sites/WP/Vercel/Supabase · P7 Redes sociais & Canais · P8 Runbooks + Kit de Emergência físico + Simulado

## Nodos irmãos (peças de segurança já existentes)

- `CEREBRO_NODE_COFRE_CHAVES.md` — onde vivem as credenciais (P2)
- `CEREBRO_NODE_BACKUPS_BACKBLAZE.md` — espelho B2 do Cérebro (P3)
- `CEREBRO_NODE_CHAVES_E_LLMS.md` + `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` — mapa de LLMs/chaves
- `CEREBRO_NODE_BUGS_ATIVOS.md` — inclui SEV-1 chaves no git (rotação pendente) e git contaminado Antigravity→FdI público
- `CEREBRO_NODE_HARDWARE_MIGUEL.md` / `CEREBRO_NODE_HARDWARE_LAURA_ROLLBACK.md` — máquinas

## Regras fixas do tema

1. **NUNCA** valores de segredos em fórum/memória/chat — só caminhos, nomes e hash (Regra do Cofre).
2. Backup só vale com **restauração provada** na prática.
3. Kit de Emergência final é **impresso/físico**; senhas mestras ficam no cofre físico, nunca no digital.
4. Toda rodada registra adendo datado no fórum-mestre (Histórico append-only) + estado "o que aconteceu / o que falta / o que preciso de você".

## Peças já em execução (antecipações do plano)

- **FAILOVER NYC × TENCENT (fim de semana 29–30/08/2026):** `Foruns/forum_failover_nyc_tencent_plano_fim_de_semana_20260826.md` + `Memorias/memoria_failover_nyc_tencent_inventario_20260826.md` — mapa vivo dos dois servidores (inventário SSH 26/08), princípios de troca segura (detecção automática + flip manual + escritor único) e plano por fases (backup/snapshot → auditoria/drift → redundância mútua → simulado domingo 06–10h). Antecipa parte do P5; mecanismo de failover da era do enxarme (26/07 fórum dualidade) auditado como desarmado/desatualizado.

## Histórico do nodo

- **23/08/2026 ~01:05 BRT — ZCode/GLM-5.3:** nodo criado na abertura do plano (S0). Fonte: ordem do Miguel ~00:55.
- **26/08/2026 ~11:50 BRT — ZCode/Kimi K3:** registrado o plano de failover NYC×Tencent do fim de semana (ordem do Miguel ~11:30).
- **14/09/2026 ~19:4x BRT — ZCode/GLM-5.3 (ZM-20260914-013):** emendas de segurança do gate do Cafezinho E5/E4-lite/E2 AUDITADAS VIVAS no servidor (implantadas 10/09 §12.11 + regime consultivo 11/09); card P1 da /v6/reforma é dívida fantasma (risco de reimplantação); plano de fechamento F0-F4 + riscos R1-R7 entregues ao Miguel aguardando "vai". Fórum: `Foruns/forum_atualizacao_reforma_v3_20260908.md` §22 · Memória: `Foruns/memoria_plano_emendas_gate_20260914.md`.

- **17/09 ~16:3x — PROTOCOLO DE EXPURGO DE CONTEÚDO SENSÍVEL + ferramenta expurga.py (ordem do Miguel, nascido de caso real do dia):** quando algo que não deveria entrar no Cérebro entra (avaliação de pessoa, segredo, ordem que o dono quer inexistente), o protocolo manda: varrer com `Ferramentas/expurga.py "TERMO" --remotos` (mapeia 10 camadas: fóruns/memórias/nodos/monitor+mortos, fóruns irmãos, memórias de agentes, git história/stash, remotes GitHub+NYC, espelho de fóruns no tencent, servidores, B2/GDrive, artefatos de sessão ZCode, V6), expurgar arquivos (backup FORA do repo em ~/backups_expurgo), reescrever história git (filter-repo + force push + gc no mirror), avisar clones por ponte com mensagem NEUTRA, e re-varrer até zero. Regras de ouro: o protocolo nunca registra o conteúdo; apagar arquivo não basta (o sync commitou); limites honestos documentados (histórico do app = manual do dono; GitHub por SHA = janela até GC). Documento: [PROTOCOLO_EXPURGO_SENSIVEL.md](../PROTOCOLO_EXPURGO_SENSIVEL.md).

- 19/09 17:1x BRT (ZCode/GLM-5.3) — INCIDENTE chave Gemini no repo público (ZM-GCP-CHAVE-20260919): sub-cérebro com valor de chave subiu no deploy-main às 16:19; Google deletou a chave em ~7 min e avisou. Cura + scan completo de segredos na árvore publicada (nenhum vivo além da deletada; PAT de fóruns morto redigido). REGRA REFORÇADA: valor de chave JAMAIS em .md do Cérebro — só cofre + ponteiro. Pendência de gate: scan de padrões (AIzaSy/AQ./sk-/ghp_/github_pat_/xai-) antes de push no repo público, aguarda "vai". Fórum: forum_incidente_chave_gemini_gcp_20260919.md

- 20/09 12:5x BRT (ZCode/Kimi K3) — PLANO ECONOMICO A (contingência do tribunal visual sem Gemini): IMPLEMENTADO e testado em produção (foto real aprovada via DeepSeek vision; fail-close do gate final preservado). Peças: cascata Kimi/DeepSeek no nucleo_visao NYC, rota deepseek_vision no contrato V4, escada econômica no roteador do portal (NYC+Dell), flag reversível (env + arquivo .pause). Rollback: apagar flag + restaurar 6 backups .bak_pre_plano_a_20260920. Detalhes no Tema Duplo plano_economico_a_tribunal_visual_20260920.
