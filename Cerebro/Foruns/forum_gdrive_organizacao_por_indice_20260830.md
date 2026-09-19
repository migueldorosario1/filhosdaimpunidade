# 📌 FÓRUM — Organização do Google Drive por ÍNDICE (buscador + biblioteca com fichas + ficha de obras)
**Sessão:** ZCode/GLM-5.3 (Dell) · **Data:** 30/08/2026 ~10:30-12:00 BRT · **Ordem do Miguel:** organizar o GDrive, mas "qualquer organização tem que vir antes com mapeamento e indexação... não pode perder a estrutura de diretórios... a maneira de organizar é por index... tem que ter um índice e desenvolver um buscador... biblioteca ótima com índice e uma ficha de cada livro, para os meus trabalhos de escrever."

## ⚖️ Decisão central (irreversível nesta fase)
**Organização POR ÍNDICE — ZERO movimentação de arquivos.** As tentativas antigas de arrastar pastas é que criaram a cascata `Livros/Livros/Livros...` (até 10 níveis). Nada foi movido/renomeado/apagado. Mudança física futura só com plano aprovado pelo Miguel.

## O que foi entregue (pronto ✅)
1. **Inventário definitivo 30/08** — `Outros/indices/GDRIVE_inventario_completo_2026-08-30.txt`, **675.247 arquivos** (Workspace_Vivo ainda fechando; snapshot ~10:45-11:30). ⚠️ O inventário de 28/08 (101.682) estava TRUNCADO (listagem recursiva única perde páginas: Backup_Total listava 2.888 de ~60k).
2. **Buscador** — `Outros/indices/busca_gdrive.py` (acentos ignorados, filtros `-e ext`, `-p pasta`, `--livros`, `-n limite`).
3. **Catálogo da biblioteca** — `Outros/indices/GDRIVE_biblioteca_catalogo_2026-08-30.csv`: **2.778 livros únicos** (66.125 arquivos na cascata ≈ 24 cópias/livro) + **fichas por categoria** em `Outros/indices/biblioteca_fichas/` (62 categorias; top: Política 717, Historia 265, Literatura 258, Filosofia 212, Economia 201). Regenerável: `catalogar_biblioteca.py`.
4. **Ficha das obras do Miguel** — `Cerebro/Dados/GDRIVE/OBRAS_DO_MIGUEL_2026-08-30.md`: FdI (R1 canônico + R3 O Foragido v7.0 Claude 17/08), **Origens da Democracia** (tese do algoritmo; docs comerciais prontos; título alternativo "A Questão Democrática"), **Curso Análise Política** (v11 = última), e ✅ **ficção científica LOCALIZADA: romance "Singularidade"** ("Singularidade Tropical" — ucrônica: sem golpe de 64, Brasil potência em 2030; + versão nova c/ cérebro artificial) em `Legacy_2026_08_06/backup 20260717/Outros/Singularidade /`.
5. **Índice mestre** — `Cerebro/Dados/GDRIVE/INDICE_GDRIVE_2026-08-30.md` (mapa nível 1 com números reais, patologias, receitas).
6. **Patologias mapeadas** (ver índice): cascata ×10, 7.584 soltos na raiz (⚠️ inclui docs de SENHA/logins — candidatos a cofre), espelhos sobrepostos ×3-4, nomes com newline, uploads concorrentes de outra sessão (Backup_Total/legacy subindo HOJE).

## O que falta
- Fechar Workspace_Vivo no inventário (número final ~+10-20k) e bater total vs `rclone size gdrive:`.
- Dedup REAL da cascata Livros (economiza ~60k arquivos e confusão) — **exige plano + "vai" do Miguel** (mudança física).
- Resgatar "Singularidade" do Legacy para pasta própria de projeto (hoje mora num backup) — aguarda Miguel.
- Conferir com o Miguel: "Singularidade" é mesmo a FC? "New novel.docx"/"Short Story in English.docx" são da mesma obra?
- Fichas ricas (com resumo/temas) dos livros-chave de cada projeto de escrita — próxima rodada.

## O que preciso de você, Miguel
1. Confirmar que "Singularidade" (Singularidade Tropical) é a FC certa.
2. Decidir se autoriza, NUMA PRÓXIMA SPRINT, a dedup da cascata (com backup e lista de conferência antes).
3. Dizer se quer a FC resgatada do Legacy para pasta viva (eu moveria CÓPIAS, origens intactas).

## Adendo 1 (30/08 ~11:45) — Curso de Análise Política: mapa de cópias completo (pedido do Miguel)
Confirmado: o curso está **no local** (`~/Dados_Frios/Outros_docs/analise politica curso/` — 293 arqs, v11, última edição 09/06 c/ transcrições de vídeos p/ aulas) **e em backup no Drive** (`Dados_Frios/Outros_docs/...` = o "backup do cérebro" que o Miguel lembrava; + pasta viva `Arquivos a organizar/...` c/ v1→v11; + 3 backups históricos: pasta 1fqTj, backup 7 abril 2026, Legacy 17/07). Na raiz do Drive (vista via mount `~/GDrive`): docs de apoio soltos ("Eleições de 2026", "Proposta Notebook KLM 22 fev 2026", Mapa geral, Roteiro Aula 1 v2, teleprompters 1-3, comentários polarização/ideologia, trechos entrevista Zucco/UOL). Os espelhos do Cérebro em si NÃO têm o curso. Ficha do curso atualizada em `OBRAS_DO_MIGUEL_2026-08-30.md`. Nada movido.

## Nota de convergência (30/08 ~12:10)
A sessão do Manual de Estilo Unificado (~11:40, ver NODE_ATUALIZACOES) chegou à **Singularidade** por via independente (capítulos publicados no site 22/07, posts 400111/400114; perfil B5 SINGULARIDADE no manual; estado em `tencent:v6_data/ficcao/estado.json`). Esta sprint localizou os **arquivos-fonte dos romances** no Drive (Legacy) — as duas frentes se complementam: ela trabalha a continuação (cap. 3+), este fórum garante o achado/acervo no Drive.

## Regras vivas desta sprint (propostas)
- **§119 (proposta): organização de acervos = por índice; movimentação física só com plano aprovado.**
- Inventário de Drive gigante: **NUNCA** `rclone lsf --recursive` único; usar pasta-a-pasta `--fast-list` + paralelo + `sort -u`; conferir com `rclone size`.
