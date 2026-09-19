# 🗂️ ÍNDICE DO GOOGLE DRIVE DO MIGUEL (gdrive: — 30 TB)
> Gerado por ZCode/GLM-5.3 em 30/08/2026 (sprint "organizar o GDrive por índice", ordem do Miguel).
> **PRINCÍPIO DE OURO desta organização: POR ÍNDICE, NUNCA POR MOVIMENTAÇÃO.** Nenhum arquivo/pasta foi movido, renomeado ou apagado — tentativas antigas de "arrumar arrastando" é que criaram as duplicações em cascata. Organizar = mapear + indexar + buscar; mudança física só com plano aprovado pelo Miguel.

## ⚠️ Correção importante sobre o índice de 28/08
O `GDRIVE_inventario_completo_2026-08-28.txt` (101.682 arquivos) estava **TRUNCADO** — a listagem recursiva única (`rclone lsf --recursive`) perde páginas silenciosamente em árvores grandes (Drive+rate limit). Exemplo real: `Backup_Total` listava 2.888; o real era ~60k. **Não confiar nos números de 28/08.**

## ✅ Inventário definitivo (30/08)
- **Método estável:** pasta-a-pasta (nível 1/2) com `--fast-list`, 6 workers paralelos, merge com `sort -u`. Receita em `Outros/indices/` (scripts `/tmp/gdrive_inv*` documentados no Fórum desta sprint).
- **Arquivo:** `Outros/indices/GDRIVE_inventario_completo_2026-08-30.txt` — **675.247 arquivos** (fora do sync GitHub: nomes pessoais não sobem).
- **Snapshot:** gerado ~10:45-11:30 BRT; **Backup_Total estava RECEBENDO upload de outra sessão** (`~/legacy` → `Backup_Total/legacy`) durante a indexação — números dessa pasta crescem depois.
- Nomes no Drive vêm em Unicode **NFD** — caminho literal com acento falha no rclone; usar glob (`--include "*padrão*"`).

## Mapa nível 1 (arquivos reais, 30/08)
| Pasta | Arquivos | O que é |
|---|---|---|
| `Arquivos a organizar` | **297.466** | Acervo pessoal: Livros (cascata!), backups, viagens, gravador, curso, dossiês |
| `Dados_Frios` | **163.170** | Arquivo frio do ecossistema (Agentes Labs 100k, Rio Carta 31k, GSN 15k, livros baixados) |
| `Legacy_2026_08_06` | 74.033 | Legado cafezinho pré-julho |
| `Backup_Total` | 59.566+ | Backup geral de máquinas (**crescendo**: upload legacy em curso) |
| `Workspace_Vivo` | 46.852+ | Espelho vivo do workspace Dell (Cerebro, Cafezinho, moka, agent_data) |
| `Cérebro Imortal da Trindade` | 17.691 | Cópia antiga do Cérebro |
| *(raiz, soltos)* | 7.584 | Documentos pessoais, versões de capítulos, chaves ⚠️ |
| `pautas editoriais o cafezinho` | 3.552 | Pautas com imagens por data |
| `Cerebro_Backups` | 1.382 | Tarballs do Cérebro |
| `novo livro` | 1.367 | **Filhos da Impunidade** (ver ficha de obras) |
| `Jornais do dia` | 1.175 | Capas de jornais do mundo |
| `filhosdaimpunidade` | 461 | Repo/site do projeto FdI |
| `orlando diniz` | 424 | Dossiê Orlando Diniz |
| `espelho-zcode` | 257 | Espelho de sessões ZCode |
| `notebook galaxy laura` | 168 | Cinema/família |
| `Projeto Casa da Moeda` | 48 | Origem do LOGIS/ILS |
| `ReadEra` | 17 | Livros do leitor |
| Outras pequenas | ~35 | `Cofres`, `PONTE_DRIVE_LAURA` (4), `PONTE_MANUS_MIGUEL` (3: ponte c/ agente Manus p/ capas), `pesquisas_eleitorais`, `Notas do Google Play Livros`, `Subcérebro AGY`, `Manus Data Recovery` ×2, `Ponte_Spark_Kimi`, `Foruns — O Foragido (Trindade)`, `Artigos Casa da Moeda` |
| `Arquivos organizados` | 0 | Pasta vazia (criada, nunca usada) |

## 📚 Biblioteca (catálogo + fichas)
- **2.778 livros únicos** catalogados (66.125 arquivos na árvore — a cascata multiplica ~24× cada livro).
- Catálogo completo: `Outros/indices/GDRIVE_biblioteca_catalogo_2026-08-30.csv` (título, autor, categoria, formato, cópias, caminho).
- Fichas por categoria (62): `Outros/indices/biblioteca_fichas/*.md`.
- Top categorias: Política 717 · Historia 265 · Literatura 258 · Filosofia 212 · Economia 201 · livros baixados novos 195 · Física 155 · Direito 117 · Biologia 87 · Antropologia 78.
- Regenerar: `python3 "Outros/indices/catalogar_biblioteca.py"`.

## 📖 Obras do Miguel
Ficha por obra (FdI/R1+R3, Origens da Democracia, Curso de Análise Política v11, ficção científica ⏳, menções): **`Cerebro/Dados/GDRIVE/OBRAS_DO_MIGUEL_2026-08-30.md`**.

## 🔍 Buscador
`python3 "Outros/indices/busca_gdrive.py" <termo> [-e pdf] [-p pasta] [--livros] [-n N]` — acento/case-insensitive, aponta o inventário mais recente. Dica de download: `rclone copy "gdrive:<pasta>" /tmp/ --include "*<padrão>*"`.

## 🧯 Patologias mapeadas (NÃO corrigir por conta própria!)
1. **Cascata `Livros/Livros/Livros/...`** até 10 níveis (cada nível duplica a árvore — 66k arquivos p/ 2.778 livros). Causa provável: sincronização/arrastar pasta pra dentro de si. O catálogo já colapsa isso no `caminho_canonico`.
2. **7.584 arquivos soltos na raiz** — inclui versões de capítulos do Origens (v2/v3/v4) e chaves/senhas ⚠️ (`login- migueldorosario@gmail.docx`, `Senhas nova 6 abril 2026.docx`) — candidatos a cofre/limpeza futura COM o Miguel.
3. **Espelhos sobrepostos**: Workspace_Vivo ↔ Backup_Total/ZCodeProject ↔ espelho-zcode ↔ Legacy (mesmo conteúdo em 3-4 lugares).
4. **Nomes com caractere de newline** (ex.: `Projeto do Livro: "A História do Café"␊.docx`) — quebram scripts ingênuos.
5. **Uploads simultâneos de outras sessões** mudam o Drive durante a indexação (Backup_Total/legacy hoje).

## 🔁 Manutenção
Reindexar (método estável): rodar `/tmp/gdrive_inventario_paralelo.sh` (recriar se /tmp limpo — receita no Fórum da sprint) e `python3 Outros/indices/catalogar_biblioteca.py`. Verificação de sanidade: comparar total com `rclone size gdrive:`.

## Histórico
- 28/08/2026 — 1º índice (inventário truncado; números desatualizados, manter só por histórico).
- 30/08/2026 — inventário definitivo 675k, buscador, catálogo+fichas da biblioteca, ficha de obras, patologias.
