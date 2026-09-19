# PROMPT PARA COLAR NA SESSÃO DA RONDA — vigília das reformas de 10/09 (ZM-20260910-006/009/010/011/012)

Ronda: sua missão hoje é VIGIAR as reformas da obra e o pós-deploy das 17h, para nada quebrar em silêncio. Contexto completo: Cerebro/Foruns/forum_atualizacao_reforma_v3_20260908.md seções 12 a 16, e MONITORAMENTO_DE_TRABALHO.md (linhas ZM-20260910-006/009/010/011/012). Leia os dois antes de agir (regra 1 e 2 do AGENTS.md).

O QUE A SESSÃO ZM (GLM-5.3) FEZ HOJE — até 13:00, NADA tocou em produção:

(1) P1 emendas do gate Dois Checks (E5 sonda health-check 15min, E4-lite HMAC nas isenções de robôs/ordem-Miguel, E2 passaporte hash+TTL): designs completos e auditados no fórum §12. O Astra AUTORIZOU COM RESSALVAS (20, todas incorporadas ao design final §12.8; parecer integral no §12.7). O pedido de autorização à CL está na ponte (Foruns/ponte_laura_completa/de_dell.md, ref ZM-20260910-006-AUTORIZACAO) e AGUARDA resposta dela. Auditoria prévia feita ao vivo: 264 isentas vivas (258 CL-, 6 ordem já vencidas, zero AL/GM), 11 callbacks do hook wp_insert_post_data auditados com arquivo e linha. Implantação só às 17h e só com autorização da CL. Regra permanente do Miguel para testes: NADA público — testes só em rascunho/em memória (portal é do leitor, §131).

(2) P11 vigia de crédito DeepSeek sem LLM (fórum §13, ZM-20260910-009): lê o saldo na API oficial a cada 15min no Tencent, limiares US$ 2,00 (aviso) e US$ 0,50 (crítico), mensagem de texto FIXA no Telegram do Miguel pelo bot do Chefe, anti-spam de 1 aviso por limiar a cada 6h. Vai ao ar na janela das 17h primeiro (independente de autorizações; não mexe em chave nem recarrega).

(3) P2 botão de pause valendo de verdade (fórum §14, ZM-20260910-010): guards de 1 linha nos crons de agentes nos 3 hosts (tencent/nyc/dell) + espelho git cerebro/Foruns/CONTROLES no repo + prova de pause/play em cada host. Às 17h, depois das emendas.

(4) P4 PROMULGAÇÃO D8 (ZM-20260910-011): EXECUTADA e provada — controle total de custos em vigor (nenhum agente gasta/contrata sem farol ligado e registro no painel). Fórum §15, seed Onda 4 #1 ok, painel /v6/reforma em 43,0%. Encaminhamentos pendentes da casa: CM consolida o inventário; DS-N Chefe corrige o push do gateway (gh) com o PAT do cofre, sem expor valores.

(5) P5 (ZM-20260910-012): revisão do HMAC LITE para COMPLETA marcada para 07/11/2026; lembretes automáticos armados (01/11 D-6 e 07/11 DIA, 09:00 BRT, Tencent + agenda do maestro).

(6) Religões agendadas da sessão executora: 16h revisão e placar; 17h implantação (automation-2ef33890 — UMA automação cobre as duas fases; teto da plataforma). Se a religação das 17h ainda estiver rodando quando você passar: NÃO interfira; confira depois pelos registros no fórum.

ESTRATÉGIA DE ROLLBACK (blocos prontos; detalhe completo no fórum §12.5, §12.8, §13, §14):

- E5 (cafezinho-wp): no crontab do root, remover a linha com SONDA_GATE_E5 e apagar /root/sonda_gate_e5.py. Não toca no gate nem no WP.
- E4-lite e E2 (gate mu-plugin): sudo cp do .bak_pre_e4lite_20260910 (ou .bak_pre_e2_20260910) sobre /var/www/ocafezinho/wp-content/mu-plugins/cafezinho-gate-dois-checks.php + php -l + prova wp eval de barramento (receita no fórum). O backup do wp-config com o segredo está em /root/backups_gate/ (chmod 600, fora da raiz pública). CRITÉRIOS DE DISPARO: post future de robô atrasado mais de 20min; sonda vermelha do tipo GATE ABERTO (deixou passar) = rollback IMEDIATO na primeira detecção; gate mudo (barrou demais/travou) = investigar na segunda; PHP fatal no site; pedido da CL ou do Miguel. Pós-rollback: listar os posts que voltaram a draft e entregar à CL — republicação NUNCA automática.
- P11 (tencent, crontab ubuntu): remover a linha VIGIA_CREDITO_DS_P11 e apagar /home/ubuntu/ds_nuvem_chefe/vigia_credito_deepseek.py (estado e logs podem ficar).
- P2 (3 hosts): restaurar o crontab.bak_pre_p2_20260910 de cada usuário tocado (ubuntu e root no tencent, root no nyc, usuário no dell). As flags .pause do espelho podem ficar (inofensivas sem os guards). ATENÇÃO ESPECIAL: um .pause órfão significa AGENTE PARADO sem ninguém saber — se algum agente sumir do ar, checar /home/ubuntu/cafezinho/v6_data/controles/*.pause (tencent) e cerebro/Foruns/CONTROLES/*.pause (repo) ANTES de debugar qualquer outra coisa.
- P5 (tencent, crontab ubuntu): crontab.bak_pre_p5_20260910; script lembrete_hmac_completo.py (só remover se necessário).

CHECKLIST DA RONDA (na primeira passada após as 17h e depois a cada ciclo):

1. Site www.ocafezinho.com respondendo 200, sem PHP fatal, e o error_log do FPM sem rajada de [cafezinho-gate2c] BLOQUEADO (alguns bloqueios são o gate trabalhando; RAJADA é anomalia).
2. Esteira viva: posts de robô (autor 5470) publicando nos slots normais; nenhum future vencido — no cafezinho-wp: wp db query "SELECT ID, post_date FROM wp_posts WHERE post_status='future' AND post_author IN (5470,5786,5787,5801) AND post_date < NOW()" deve voltar vazio.
3. Sonda E5 verde: log /root/agent_data/sonda_gate_e5.log (cafezinho-wp) avançando a cada 15min SEM alerta; se ela gritar GATE ABERTO = rollback imediato do bloco E4/E2 acima.
4. Crons DSN rodando (logs frescos no tencent: dsn_revisor1/cron.log, dsn_revisor2/cron.log, dsn_financeiro/log/cron.log, ronda_dsn). Se algum parou, checar .pause antes de tudo (item P2 acima).
5. Vigia P11 comportado: no máximo as mensagens esperadas (1 aviso por limiar a cada 6h); se spammar o Telegram do Miguel, rollback P11.
6. Painéis 200 e coerentes: /v6/reforma, /v6/agentes, /v6/custos (a barra deve refletir o que as religações registrarem no seed).
7. Telegram do Miguel: só mensagens legítimas (nada em loop, nada de erro repetido).
8. Qualquer anomalia: executar o rollback do bloco correspondente + registrar na ponte (de_dell) + adendo no fórum da obra + linha no monitoramento. Se a CL pedir rollback do gate, executar sem discutir (critério dela é critério de disparo).
9. Aprovações: se a CL responder o pedido ZM-20260910-006-AUTORIZACAO depois das 17h com ressalvas novas, registrar na ponte e no fórum §12.7 — a sessão executora precisa achar.

— Prompt produzido pela sessão ZM/GLM-5.3 em 10/09/2026 13:0x BRT (fechamento da sessão da manhã).
