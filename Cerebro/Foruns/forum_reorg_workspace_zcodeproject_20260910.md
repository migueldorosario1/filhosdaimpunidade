# Fórum — Reorganização radical do workspace ~/ZCodeProject (ZM × ASTRA, 10/09/2026)

**Ref:** ZM-20260910-001 · **Ator:** ZCode/GLM 5.3 + ASTRA (GPT-6 via Codex CLI, consultor-chefe) · **Estado: FASES 1+2 EXECUTADAS 10/09 ~03:3x-03:5x (ordem "vai" do Miguel ~03:1x) — 40 itens/520 arq/641MB no frio, 520/520 íntegros. Fases 3-4 (agrupamento do VIVO) aguardam próximo "vai".**

## Ordem do Miguel (voz, 10/09 ~02:35)

Sessão constante de faxina/limpeza (ele "rataciona" criando conversa nova de vez em quando, sempre com esse objetivo). Pedições: (1) responder se workspace grande atrapalha o ZCode; (2) varredura + PLANO de reorganização radical com POUCOS diretórios de frente, agrupando por afinidade — "não sai mudando, indexa tudo primeiro"; aprovação PRÉVIA obrigatória ("todas as vezes que organizei com IA ficou mais bagunçado"); (3) parceria com o ASTRA — varredura conjunta, prompt direto a ele pela ponte, ele oferece solução.

## O que aconteceu

1. §112 consultado (02:40) — sem colisão (sessões ativas em LOGIS/Rio Carta, fora do alvo).
2. Varredura ZM: 87 itens top-level (40 dirs + 47 soltos), 2,8 GiB, ~34.813 arquivos. Comando do Codex confirmado em `ponte_astra/codex_reply.py` (modelo gpt-6-astra, sandbox read-only, --ephemeral).
3. **ASTRA acionado direto** via `codex exec --sandbox read-only -m gpt-6-astra -C ~/ZCodeProject` (02:47→02:51, rc=0): prompt completo em `/tmp/prompt_astra_reorg.md`, resposta integral 13,5KB gravada em `Cerebro/Foruns/PARECER_ASTRA_REORG_ZCODEPROJECT_20260910.md` (com anexo da varredura).
4. Dependências mapeadas: 2 crons VIVOS em `~/ZCodeProject/scripts/` (auditor entrega 8h10 + watchdog */5, ambos com flock) — caminho NÃO pode mudar sem atualizar crontab na mesma janela.

## Decisão proposta (árvore-alvo, 6 de frente + scripts preservado)

```
~/ZCodeProject/
├── projetos/     (aplicativos: moka-app, igot · sites: cafezinhomediagroup, filhosdaimpunidade · origens, origens_work)
├── operacao/     (paineis: painel_fix, painel_v6_reforma, farol_v6 · midia: media_ledger, publicador, banco auditado · regional: regional_v4, v4_archiver, v4_novos_staging · voz: zcode_voice_gnome_controller, zcode_voice_receiver · laura: credenciais_laura)
├── pesquisas/    (eleicoes_2026: xlsx/csv/txt/gerar_tabela · pesquisa-cmb · editorial: ceara-digital, rio-carta)
├── referencias/ (base_conhecimento, modelos)
├── bancada/      (social_simulacoes, scratch, scratch_patches, pending_delegados, manutencao_editorial/scripts avulsos vivos)
├── scripts/      [PRESERVADO — 2 crons dependem do caminho absoluto]
└── INDICE.md     (a criar na Fase 1: destino/finalidade/situação de cada unidade)
```

Frio sai do workspace inteiro → `~/Dados_Frios/ZCodeProject/missoes/` agrupado POR MISSÃO (comércio-exterior 07/26: dados_carnes, dados_corrente, tarifao_p3... · matérias 07/26: publicar_*.py, lula_*.jpg... · video-kakay: cacai_teste · midia-v4 08/26: mutirao_midia_v4, auditoria_v4_20260813, bloco_regional_20260813, handoff_gsn...), + `evidencias/` (provas_botnews) + `recuperacao/` (espelho_zcode_laura, MAPA_BACKUPS_20260805.md). Código+insumos+resultados juntos, missão reproduzível. Lista de descarte CANDIDATA (só com OK do Miguel): 3 arquivos vazios de nomes corrompidos (`re`, `{n[status]}`, `{x[destino]}`), caches pytest/__pycache__, jpgs intermediários de cacai_teste.

### Achados críticos da dupla varredura (governam a migração)

- **5 repositórios git aninhados** (filhosdaimpunidade, igot, moka-app, origens, cafezinhomediagroup) — cada repo viaja INTEIRO, nunca desmontado.
- **filhosdaimpunidade/index.html modificado sem commit** — preservar como está (sem reset/commit automático).
- Caminhos absolutos entre irmãos: análises→dados_carnes/dados_corrente; publicar_cafezinho.py→lula_destaque.jpg; gerador de cards→social_simulacoes; F8 (voz)→pasta atual (consumidor GNOME externo — verificar lançadores antes de mover).
- `coletor_banco_links.py` recriaria `banco_links_midia.jsonl` no topo se reexecutado (re-sujeira automática).
- Estados ocultos com consumidores desconhecidos: `.vigilia_claude_state.json`, `.demo_acorda_state.json` — ficam até localizar consumidores.
- Dados_Frios e workspace no MESMO dispositivo → `mv` atômico reversível (reconfirmar `df` na execução).

### Migração em 4 fases (só após aprovação)

1. **Inventário fechado** — manifesto completo 87 itens (origem→destino, permissões, links, git status/HEAD de cada repo, crontab e consumidores); INDICE.md; backup dos insubstituíveis; **Miguel aprova o mapa antes do primeiro mv**.
2. **Retirada do frio** — famílias de missões encerradas, um lote por vez; recontagem+hash antes/depois; rollback = rename inverso.
3. **Agrupamento do trabalho** — referencias/pesquisas/projetos, um repo por vez; validar imports/caminhos em ambiente isolado.
4. **Pontas operacionais** — painéis/mídia/regional/voz/laura com dependências verificadas; `scripts/` fica; homologação por observação dos ciclos reais (NUNCA rodar os crons manualmente como teste).

Regras de execução: sem sobrescrever destinos, sem fundir homônimos, sem cp+rm em árvore viva sem backup, sem exclusões na mesma leva da migração, rollback por rename em ordem inversa bloqueando escritas na janela.

### Performance (resposta à pergunta do Miguel)

Workspace enxuto: SIM vale — buscas do agente varrem o cwd; ganho real vem de (a) tirar material inativo do workspace e (b) dirigir buscas à subpasta da tarefa. Agrupar em 6 pastas melhora navegação mas não reduz varredura recursiva sozinho; ripgrep já ignora ocultos/binários (node_modules ~1,24 GiB pesa pouco na busca). Instalação do ZCode (/opt) e tamanho do diretório ONDE está instalado não interferem.

## O que falta / próximos passos

1. **AGUARDA "vai" do Miguel** sobre a árvore-alvo (e destinos do frio).
2. Após aprovação: Fase 1 (inventário+manifesto+INDICE.md) → nova rodada de aprovação → Fases 2-4.
3. Pendência Miguel na fase de descarte: lista de candidatos (acima).

## Provas

- Parecer Astra integral + varredura: `Foruns/PARECER_ASTRA_REORG_ZCODEPROJECT_20260910.md` (255 linhas, gerado 02:51, rc=0).
- Prompt enviado: `/tmp/prompt_astra_reorg.md`; log da corrida: `/tmp/astra_reorg_run.log`; resposta crua: `/tmp/astra_reorg_resposta.md`.
- Varredura bruta: `/tmp/varredura_zcodeproject.txt` (75 linhas).
- Crons vivos: `crontab -l | grep ZCodeProject` → 2 linhas (auditor 8h10, watchdog */5, ambos flock).


---

## ADENDO — EXECUÇÃO FASES 1+2 (10/09 ~03:3x–03:5x, ZM, ordem Miguel "vai" com condições: indexação completa + cuidado com produção)

### Checagens de produção (todas LIMPAS antes do primeiro mv)

Existência 34 itens ✅ · 0 repos .git dentro do frio ✅ · crontab COMPLETO (única linha que casa = comentário # V4-DESATIVADO 20/07 do aiatolah, fora do workspace) ✅ · systemd user ✅ · ~/.bashrc/.profile ✅ · grep em scripts/ + Cerebro/Ferramentas + ponte_cafezinho ✅ · lsof +D nas 10 pastas (0 processos) ✅ · mesmo filesystem (df 1 device → mv atômico) ✅.

### Indexação completa (condição do Miguel)

- `.reorg/manifesto_fase2_20260910_033551.tsv`: sha256+bytes+mtime dos 514 arq (640,7MB) + `.reorg/manifesto_fase2b_*.tsv` (6 complementares). Espelhos: /tmp/manifesto_fase2_backup.tsv + commit no repo.
- `.reorg/rollback_fase2.sh`: mv inversos completos (45 linhas), executável.
- INDICE.md no workspace (mapa vivo/frio/planejado) · README.md no Dados_Frios/ZCodeProject (estrutura, rollback, alertas).
- Buscador local reindexado pós-movimento: 277.958 arq / 48.152 dirs (33s).

### Movimento executado (Fase 2 — 40 itens, frio)

6 lotes → ~/Dados_Frios/ZCodeProject/: missoes/2026-07-comercio-exterior (dados_carnes, dados_corrente, tarifao_p3 + 6 coletores + 5 análises + gráfico) · missoes/2026-07-materias (4 publicar/trocar/metadata .py + 4 jpg) · missoes/2026-07-video-kakay (cacai_teste) · missoes/2026-08-midia-v4 (mutirao_midia_v4, auditoria_v4, bloco_regional, handoff_gsn, 3 faxinas/varredura .py, coletor_banco_links.py, 3× banco_links históricos) · evidencias (provas_botnews, crime-v4.jpg) · recuperacao (espelho_zcode_laura, MAPA_BACKUPS_20260805.md). Log: /tmp/reorg_fase2_033630.log (34 mv OK) + 6 do complemento.

### Verificação pós-mv

Re-hash sha256+bytes de TODOS no destino vs manifesto: **520/520 conferem, 0 divergências**. Workspace: 87→48 itens, 2,8G→2,2G. scripts/ intocado (crons vivos). NADA apagado; descartes (3 vazios re/{n[status]}/{x[destino]}, scratch_teste_*) AGUARDAM OK explícito.

### O que falta / próximos passos

Fase 3 (agrupar o vivo em projetos/operacao/pesquisas/referencias/bancada — 5 repos git inteiros, F8/voz, credenciais_laura) e Fase 4 (pontas operacionais) após novo "vai" do Miguel, com mapa item-a-item do INDICE.md já aprovável.


## ADENDO 2 — DIAGNÓSTICO INICIAL DO ANTIGRAVITY GOOGLE (10/09 ~11:2x, ZM, pergunta do Miguel "consegue organizar o antigravity também?" — SÓ LEITURA, nada movido)

Top-level: 298 itens. Pesos: .git 28G (repo-armadilha, origin filhosdaimpunidade, HEAD/reflog DORMENTE desde 29/07) · Outros 11G · Projeto Cafezinho Agentes 5,2G · agent_data 2G · zm_operacoes 1,9G · scratch_cerebro_miguel 1,4G · .ds_ponte_clone_308 1,4G + _309 1,2G (faxina mantém) · scratch 1,3G · cerebro-miguel 1,1G (repo publicação — INTOCÁVEL) · astra_operacoes 1,1G · Cicero Agentes 902M · grava_jornal_20260902 679M · cerebro_miguel_ponte 649M · moka 616M · Cerebro 483M (SAGRADO, caminho canônico) · clones resíduo de ronda: .ds_ponte_clone 477M + .ds_scratch 424M + ds_ronda_386/387_ponte 620M · aiatolah 232M · GSN 230M · Rio Carta Agentes 227M · casadamoeda 3× (171+171+75M) · logis 160M · Revista Maquiavel 148M · dezenas de jpgs/vtt/tmp soltos (sb_frame_* de storyboard, elmano_*, transcrições, index.html+bak).

Dependência viva: 24 dos 53 crons do Dell apontam pro AG (quase metade da produção robótica). Conclusão: reorg do AG = método da reorg ZCodeProject + trava extra (crons mapeados por pasta; nada com cron se move sem atualização síncrona; Cérebro/Outros intocáveis D3 não entram).

Proposta a aprovar (3 frentes por ganho/risco): A) resíduos de ronda/clones velhos/caches/jpgs soltos → quarentena c/ manifesto (~1,5-2G, risco baixo); B) .git 28G armadilha → arquivar p/ Dados_Frios após provar que branches locais não têm unpushed e repo vivo do filhos (agora em ~/ZCodeProject) cobre (ganho enorme); C) agrupamento top-level só do que NÃO tem cron (risco alto, por último). Detalhamento e execução: mesma dupla ZM×ASTRA, fases, manifesto sha256+rollback. AGUARDA "vai" por frente.
