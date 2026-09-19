# Fórum — Rotina de organização e limpeza do Antigravity Google (ZM × ASTRA, 10/09/2026)

**Ref:** ZM-20260910-002 · **Ator:** ZCode/GLM 5.3 + ASTRA (gpt-6-astra, direto via Codex, read-only) · **Estado: ROTINA FORMULADA — aguarda "vai" do Miguel por fase. Vazios já executados (ordem direta): 6 removidos com checagem de consumidor.**

## Ordem do Miguel (10/09 ~11:2x)

"Pede para ele te ajudar na formulação de uma rotina de organização e limpeza também do Antigravity. Tá com muito diretório lá nas bases. Preciso de menos diretórios nas bases e MAIS SUBDIRETÓRIOS. E REMOVER TUDO QUE ESTÁ VAZIO. Possivelmente tem muita coisa excessiva que podia estar APENAS no GDrive e Backblaze."

## O que aconteceu

1. Varredura ZM (adendo 2 do fórum da reorg ZCodeProject): 298 itens top-level (86 dirs + 211 arquivos + 1 symlink, ~62 GiB — Astra confirmou); 24/53 crons vivos apontam pro AG; .git 28G.
2. **ASTRA acionado direto** (11:3x→11:5x, rc=0, 16,3KB): parecer integral em `Foruns/PARECER_ASTRA_ROTINA_AG_20260910.md` — estrutura-alvo 10 guarda-chuvas + exceções, rotina 4/4h/diária/semanal/mensal, regra nuvem-first (6 critérios + rito), 11 candidatos por prioridade, auditoria específica do .git, política de vazios, mapa de produção, 4 fases.
3. **Vazios executados na hora** (ordem direta): 39 vazios achados → 6 REMOVIDOS com checagem de consumidor (dirs Google/.ds_r286 + Google/ vazia; 4 arq .ds_tmp/notas_*.txt) → LEDGER Lote 9; 33 MANTIDOS com motivo (locks agent_data ×2, ledgers publicadas_*.jsonl/gsn_inbox.db de robôs vivos, .git/branches ×7, node_modules/@emnapi/.astro ×5, Cerebro_FORBIDDEN + _organizacao (intocável), A_GRANDE_REFORMA (intocável), ds_ronda_385_pendente com pendente de HOJE, scratch/*.vtt ×3 (scratch intocável D3), vod_job_console.log (vai com a pasta grava_jornal na Frente A)).

## 🔴 CORREÇÃO importante (ZM leu errado, Astra corrigiu)

O .git de 28G NÃO está dormente: reflog mostra atividade até **07/09 06:35** (reset para origin/main; HEAD dc23697c commit de 05/09, autor "Refatoração V4") e o branch deploy-main **rastreia arquivos do Cérebro**. A leitura do ZM pelo mtime de .git/HEAD (29/07) estava ERRADA. Arquivá-lo agora seria prematuro — exige a auditoria de 7 pontos do Astra (branches/tags/stash/worktrees/untracked/hooks/alternates/LFS; comparar TODAS as refs vs repo vivo + GitHub; reflogs; mapear quem usa Git na raiz por descoberta ancestral; bundle não preserva tudo; restauração isolada antes da retirada).

## ROTINA CONSOLIDADA (ZM×Astra) — o essencial

**Estrutura-alvo:** 10 guarda-chuvas (Projetos/ Editorial-Produtos-CasaDaMoeda · Agentes/ · Editorial/ · Midia/ · Dados/ · Infra/ · Operacoes/ Rondas-Pontes-Artefatos-Organizacao · Laboratorio/ · Arquivo/ Quarentena-CatalogoNuvem · Outros/ preservado) + lista explícita de exceções (intocáveis D3 e caminhos com cron ficam onde estão; NELES, novas saídas nascem em subdiretórios internos: scratch/missoes/<id>/, zm_operacoes/artefatos/<id>/). Sem symlinks em massa. Dentro do Cérebro: nada.

**Cadência:** 4/4h leve (lock, inventário diff, vazios/temporários vencidos, só regras pré-aprovadas, ≤50 entradas ou 1GiB/ciclo, sem trabalho = sem mensagem) · diária (consolidação + identificar PRODUTOR de cada entrada indevida) · semanal (lotes de agrupamento + candidatos nuvem) · mensal (teste de restauração das 2 nuvens + revisão de exceções). Automação determinística, sem LLM.

**Nuvem-first (GDrive+B2)** — todos os 6: missão encerrada + ≥30d sem alteração relevante + zero cron/servição/importação dependente + fora da D3 + 2 cópias verificadas/restauráveis + catálogo local com hashes e rito de recuperação. Rito: inventário→manifesto SHA-256→upload duplo→lsf→readback integral ×2→teste de restauração→revalidação→remoção individualizada→LEDGER. Prioridade por tamanho (>500MiB primeiro). Candidatos numerados 1-11 no parecer (.git 28G = #1 BLOQUEADO até auditoria; novo livro 2,5G; mapa rio videos 2,2G; Aplicativos 1,8G; scratch_cerebro_miguel 1,4G; jornais históricos; .ds_ponte_clone+.ds_scratch 943M; cerebro_miguel_ponte 685M; grava_jornal 679M [8 dias — aguardar]; ds_ronda_386/387 662M; casadamoeda_backup 76M).

**Regra de entrada (o antídoto ao acúmulo):** toda missão nova recebe DONO + DESTINO + PRAZO antes de gerar arquivo; produtor escreve no destino certo (Projetos/<familia>/<nome>, Operacoes/Rondas/<agente>/<missao>, midia por assunto/data).

**Fases:** 1 Reconciliar e congelar (dupla varredura, tabela dono/leitor/escritor/cron/rollback por caminho, lotes concretos p/ aprovação — sem mutação) · 2 Reduzir a raiz (mídia/entregas/resíduos liberados + vazios elegíveis, método manifesto→mv→re-hash) · 3 Liberar espaço (offload duplo dos frios elegíveis; Git só após auditoria própria) · 4 Sustentar (rotina 4/4h + migrar exceções elegíveis gradualmente).

## O que falta / próximos passos

1. AGUARDA "vai" do Miguel: Fase 1 da reorg AG (reconciliar + congelar plano com lotes concretos).
2. Auditoria específica do .git 28G (7 pontos do Astra) — pode ser Fase 1B paralela.
3. Fase 3 da reorg ZCodeProject (agrupar o vivo em 6 pastas) — ainda pendente do "vai" anterior, independente.

## Provas

Parecer Astra: Foruns/PARECER_ASTRA_ROTINA_AG_20260910.md (16.329b, rc=0) · prompt /tmp/prompt_astra_rotina_ag.md · log /tmp/astra_rotina_ag_run.log · vazios: LEDGER Lote 9 + manifestos /tmp/vazios_removidos_*.tsv e ~/.local/share/buscador_local/.reorg_vazios_*.tsv · varredura AG: adendo 2 do fórum reorg ZCodeProject.
