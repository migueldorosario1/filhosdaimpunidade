# Memória técnica — Livro ORIGENS: organização + capítulo 2

**Sessão:** ZCode/GLM-5.3 (Dell), 01/09/2026 14:12→14:3x BRT. Log completo do sprint.

## Atividades e comandos principais

- Varredura: `find ~ -maxdepth 4 -iname "*origens*" -o -iname "*democracia*"`; `ls ~/GDrive | grep -iE "origens|democra|capitulo|audio"`; `gh repo list migueldorosario1 --limit 100` (confirmou que NÃO havia repo do livro).
- Índices do Cérebro reutilizados: `Cerebro/Dados/GDRIVE/OBRAS_DO_MIGUEL_2026-08-30.md` (ficha nº 2 do Origens com mapa do Drive) — sessão de 30/08 já tinha mapeado tudo, economia enorme.
- Extração docx: python-docx no Dell exige cópia local antes (mount FUSE falha com "Package not found"). Extraídos: cap1 oficial (27.513 chars), cap2 versão existente (9.543), anotações (16.896), relatório (3.030) → `~/ZCodeProject/origens_work/`.
- Repo criado: `gh repo create origens --private --clone` → `~/ZCodeProject/origens`, branch **master** (default do gh), remote origin OK.
- Estrutura via script python (regex sobre o roteiro integral): parse dos blocos "## Capítulo N" → seção "### Rascunho" → gravação em pasta nova conforme remap. 19 rascunhos extraídos; 03_atomo e 19_principio_floresta sem rascunho (capítulos novos do índice aprovado).
- Remap antigo→novo (gravado no PROGRESSO.md): 2→02, 3→05_memetica, 4→04_celula_cerebro, 5→06_religioes, 6→07_renascimento, 7→08_revolucao_francesa, 8→09_americana, 9→10_pos_guerra, 10→11_chines, 11→12_america_latina, 12→13_big_techs, 13→14_redemocratizacao, 14→15_junho_2013, 15→16_lava_jato, 16→18_socialismo, 17→17_mercado_ou_povo, 18→19_principio_floresta(material base), 19→20_ia, 20→21_epilogo.
- Cap 2 escrito à mão (Write) e auditado por script: 0 ";" no corpo, 0 ":" no corpo, 0 "—" fora da epígrafe, 13.688 chars / 2.278 palavras. Typos corrigidos (Difícil, gênio, "Nada disso"), fatos ajustados: Melos 416 a.C. (16º ano da guerra), universidade de Robinson removida (blindagem), "Alexandria e Memphis" → "sacerdotes do Egito".
- Commit: bc69123 (estrutura + cap1 + dossiê/cap2 juntos, glob pegou tudo) → push origin master ✅. https://github.com/migueldorosario1/origens

## Provas

- `git log --oneline` = bc69123; `git push` OK ("[new branch] master -> master").
- Auditoria de estilo do cap 2 rodou com assert, saída limpa.
- 66 arquivos .md no repo (22 pastas × 3 arquivos - extras).

## Fontes lidas (para retomar sem reler tudo)

- Roteiro integral (82k) LIDO COMPLETO na sessão — sinopses, bibliografias e rascunhos dos 20 caps antigos.
- Arquivo completo (196k): Partes 1, 2, 3 e 5 lidas (mapa Drive, núcleo conceitual, índice, plano de trabalho, regras de estilo). Parte 6 = conversa (105k) só grepada.
- Cap 1 oficial lido integral (voz de referência: golpes curtos, cena factual + leitura moral + pergunta retórica, ironia atribuída, parágrafos curtos, epígrafe).
- Áudio transcrito do Miguel sobre o cap (Rascunhos/Capitulo_3_Mito_Milagre_Grego...) lido integral — imagens-chave: "vírus ideológico que nunca morreu", "pela solução de Sólon sabemos o problema", Aquiles/Agamemnon vs Xá, coalizão de endividados como 1º partido popular, classe média culta emancipando criatividade, sorteio como experiência "muito louca", corrupção (ricasso comprando cargo).
- "Comentarios Chat GPT cap 2.txt" = resposta do ChatGPT arquivada com o padrão de estilo do cap 1 (útil como checklist de voz).

## Pendências técnicas

- Espelho do repo para o Drive (pasta canônica do livro) — não feito nesta sessão (Miguel não pediu; fica como próximo passo opcional).
- Sync do cerebro-miguel (GitHub) fica por conta do cron/hook de 15 min.
