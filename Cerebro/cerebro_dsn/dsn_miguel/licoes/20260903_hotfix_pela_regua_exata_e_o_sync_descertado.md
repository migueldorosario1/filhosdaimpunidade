# Lição DS — 03/09/2026 · O conserto veio pela régua exata — e o sync-bug ganhou mecanismo

**Ronda:** DS 115ª (17:30) · **Estado:** INCIDENTE-1154 curado no código (ZM-079, 17:18) · sync-bug com mecanismo descertado

## O quê

1. O hotfix da Emenda 5 (a trava que rebaixava post publicado a future) foi aplicado pelo ZM às 17:18 — depois de 7 cobranças da CL e 6 do Chefe ao longo do dia. A guarda é UMA linha, exatamente como a CL especificou: `if (!empty($postarr['ID']) && get_post_status($postarr['ID']) === 'publish') return $data;` no topo do `cafezinho_slot20_garantir`. Protocolo cumprido: backup `.bak_pre_ronda_emenda5_20260903_1715` + `php -l` OK + diff de 1 linha + **prova da cura** (save simulado de robô sobre o 268697 devolveu `$data` intocado). Rollback = 1 comando (cp do .bak).
2. O ZM descartou o MECANISMO do sync-bug (que come escritas canônicas desde o dia 01/09, 30+ recorrências): o trilho de PULL :00/:15/:30/:45 copia o repo por cima do CANÔNICO e come escritas canônicas feitas na janela — prova: de_dell canônico mtime 17:15:02 terminando no CHECK 16:35 do repo; o próprio ZM-079 de 17:14 sumiu. **Defesa: escrever DIRETO no repo + commit imediato** (fluxo DS-Laura/Ideias); escrita canônica solta = perdida.

## Por quê

- A CL especificou a guarda com o código EXATO e a condição certa (checar `$postarr['ID']` + `get_post_status` ANTES da lógica de slot). Sem a régua exata, o ZM teria que adivinhar o ponto de inserção — e o pedido genérico ("conserta a trava") não destrava nada. Régua exata + protocolo (backup/lint/diff/prova) = conserto verificável.
- O sync-bug parecia "restauro vira alvo do sync" (lições 02/09 e 03/09 manhã) — um mistério de comida de arquivo. Agora tem causa provada: não é um agente malicioso nem o GitHub, é o PRÓPRIO trilho de pull do canônico que sobrescreve o working tree. Mecanismo conhecido muda a defesa: de "restaurar no pós" (respiro) para "escrever no repo e commitar antes do próximo trilho" (prevenção).

## Como aplicar (régua da casa)

- **Pedido de conserto = spec mínima:** dizer a função, a linha, a condição e o comportamento esperado (prova). A 7ª cobrança da CL só resolveu porque a 1ª já tinha a linha exata — a persistência foi na régua, não no volume.
- **Fecho de incidente exige prova da cura**, não só o commit: o ZM simulou o save do robô sobre um post publish e viu o `$data` intocado. Registrar "aplicado" sem prova = anúncio de grade sem prova de ar (lição 02/09).
- **Escrita na casa:** canônico é leitura; escrita vai DIRETO no repo (ou no clone-scratch do workspace, física DS-032) + commit imediato + push. Escrita solta no canônico morre no próximo trilho :00/:15/:30/:45.
- **Vigia:** ao ver commit de hotfix, conferir no origin + registrar fecho no nodo de bugs com ref — mas a vigília do INCIDENTE-1154 só fecha de vez com a observação de que nenhum post publicado recua a future nas próximas horas (prova em produção, não só em simulação).

**Refs:** ZM-079 (de_dell 17:18) · CL-128/CL-127 (cobranças) · licoes/20260903_post_publicado_nao_sai_e_a_excecao_registrada_e_o_caminho.md · licoes/20260903_restauro_vira_alvo_do_sync_ate_o_kill_switch.md · INCIDENTE-1154 · DSC-049 (kill-switch, aguarda ✓ do Miguel)
