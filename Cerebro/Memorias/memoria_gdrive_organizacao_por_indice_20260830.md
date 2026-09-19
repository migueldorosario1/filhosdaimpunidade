# 🧠 MEMÓRIA — Organização do Google Drive por índice (log técnico completo)
**Sessão:** ZCode/GLM-5.3 (Dell) · **Data:** 30/08/2026 · **Fórum irmão:** `Foruns/forum_gdrive_organizacao_por_indice_20260830.md`

## Arquivos tocados (nada no Drive foi movido)
- `Outros/indices/GDRIVE_inventario_completo_2026-08-30.txt` — 675.247 linhas (novo; o de 28/08 mantido por histórico, TRUNCADO)
- `Outros/indices/busca_gdrive.py` — buscador (novo, executável)
- `Outros/indices/catalogar_biblioteca.py` — gerador do catálogo (novo)
- `Outros/indices/GDRIVE_biblioteca_catalogo_2026-08-30.csv` — 2.778 livros únicos (novo)
- `Outros/indices/biblioteca_fichas/*.md` — 62 fichas de categoria (novo)
- `Cerebro/Dados/GDRIVE/INDICE_GDRIVE_2026-08-30.md` — índice mestre (novo; anterior 28/08 mantido)
- `Cerebro/Dados/GDRIVE/OBRAS_DO_MIGUEL_2026-08-30.md` — ficha por obra (novo)
- `Cerebro/Foruns/forum_gdrive_organizacao_por_indice_20260830.md` + esta memória
- `Cerebro/MONITORAMENTO_DE_TRABALHO.md` — linha aberta/fechada da sessão
- Downloads de leitura (provas, sem edição): `pax siliica.docx`, pasta `Pax Silica`, 3 romances de `Singularidade`, `PONTE_MANUS_MIGUEL/*` — tudo em `/tmp/fc_probe/`

## Comandos-chave (receita)
```bash
# INVENTÁRIO ESTÁVEL (método pasta-a-pasta; NUNCA usar um --recursive único)
# worker: rclone lsf "gdrive:$CAM" --recursive --files-only --fast-list | sed "s:^:$CAM/:" > W_<md5>.txt
# orquestrador: joblist nível1+nível2 → filtro python (pai vira job só se não tem filhos) → xargs -P 6 → cat W_* | sort -u
# scripts da sessão: /tmp/gdrive_inv_worker.sh + /tmp/gdrive_inventario_paralelo.sh (recriar se /tmp limpo)

# verificação de sanidade
rclone size gdrive:            # total de objetos — comparar com inventário
rclone size gdrive:Backup_Total

# buscador
python3 "Outros/indices/busca_gdrive.py" fukuyama --livros

# catálogo/fichas da biblioteca
python3 "Outros/indices/catalogar_biblioteca.py"
```

## Bugs e pegadinhas da sessão (lições)
1. **`rclone lsf --recursive` único MENTE por omissão** no Drive grande: inv28 listou 101.682 com Backup_Total=2.888 (real ~60k); inv30-v1 325k ainda perdeu 12% de Backup_Total. Sem erro visível — só `rclone size` revela.
2. **rclone órfão sobrevive à morte do script pai** (script morto, rclone filho rodando horas) — matar por PID (lição já conhecida, aplicada).
3. **Órfãos + workers paralelos + `rclone copy` de OUTRA sessão** compartilham a MESMA quota da API Google → tudo engasga junto. Detectar com `ps aux | grep rclone` antes de culpar o método. Hoje: upload `~/legacy → Backup_Total/legacy` em curso durante toda a indexação.
4. **Bug do buscador:** contador `total` no mesmo loop do `break` do limite → contava só até o último achado. Fix: carregar linhas, contar, filtrar depois.
5. **Bug do catálogo:** `ext()` sem ponto vs `EXT_LIVRO` com ponto → 0 livros. Fix: set com ambas as formas.
6. **NFD + espaço final:** pasta "Singularidade " (espaço antes da barra) — `rclone copy` com caminho literal falha ("directory not found"); usar `--include "Singularidade*/**"` do pai.
7. **Joblist discovery vazia** para pasta grande sob throttle → pai vira job recursivo único (mais lento, mas correto).
8. `for f in $F` quebra com espaços em nomes — usar `find -exec`.

## Números (30/08, snapshot 10:45-11:30 BRT)
- Total inventário: **675.247** (Workspace_Vivo ainda listando; Backup_Total recebendo upload de outra sessão).
- Nível 1: Arquivos a organizar 297.466 · Dados_Frios 163.170 · Legacy 74.033 · Backup_Total 59.566+ · Workspace_Vivo 46.852+ · Cérebro Imortal 17.691 · raiz 7.584 · resto ~9k.
- Biblioteca: 2.778 únicos / 66.125 arquivos na cascata (Política 717, Historia 265, Literatura 258, Filosofia 212, Economia 201, Física 155, Direito 117).
- Obras: FdI (R1 23 caps canônico + R3 O Foragido 46 caps, última v7.0 Claude 17/08 11:30) · Origens (capítulos até 20; docs comerciais; "A Questão Democrática" título alternativo) · Curso v11 · FC = **"Singularidade"** (3 arquivos no Legacy).

## Estado ao fechar
- Workspace_Vivo: últimos jobs na fila do xargs; merge final do script roda sozinho (sobrescreve o TXT 30/08 com sort -u de tudo) — re-rodar `catalogar_biblioteca.py` depois se quiser o CSV final (biblioteca não muda).
- Pendências no Fórum (confirmar FC com Miguel; autorizar dedup; resgatar Singularidade).
