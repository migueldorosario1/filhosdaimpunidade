# Fórum — PLANO DE MIGRAÇÃO: espelho → canônico (hoje à noite, 12/08)

**Data:** 2026-08-12 ~17:00 BRT
**Sessão:** ZCode GLM-5.2
**Objetivo:** levar as 5 verticais V4 extras (cultura/economia/meio ambiente/esporte/saúde) + blocos + Mais Vistos do **espelho** pro **canônico** (ocafezinho.com).

> **Runbook de execução.** Cada etapa tem backup + rollback. O canônico é PRODUÇÃO (milhares de leitores) — máximo cuidado.

---

## Pré-requisitos (JÁ PRONTOS no canônico)
- ✅ Logo v10 (1550×280, 11KB) — JÁ no canônico (header trocado hoje).
- ✅ Mu-plugin `cafezinho-real-image-gate.php` — JÁ no canônico.
- ✅ Tema base (reforma V2.5: 🔥, CSS, header, footer) — JÁ no canônico.
- ✅ Cron das 5 verticais — JÁ ativo no NYC (mas publicando no espelho).
- ✅ Contratos v4_*_v1.md — JÁ no NYC (/root/v4_labs/contratos/).
- ✅ Categorias WP (79/43/582/1271/258) — JÁ existem no canônico.

## O que FALTA migrar (5 etapas)

### Etapa 1 — Front-page do canônico: adicionar 5 blocos + Mais Vistos + reorganização
O front-page do canônico tem a reforma V2.5 MAS não tem os 5 blocos novos nem o Mais Vistos.
1. Baixar front-page atual do canônico.
2. Aplicar a MESMA manipulação que fiz no espelho:
   - Inserir 5 blocos após `<!-- TECNOLOGIA -->` (Cultura → Economia → Meio Ambiente → Saúde → Esporte).
   - Substituir Linha do Tempo pelo bloco "Os 10 mais vistos" (gap g-3, sem views, link público).
   - Renomear Recentes → Outros Recentes.
3. Adicionar CSS customizado (append style.css): `hr.bar { display:none }` + `.coluna-editor-nome { color:#8B0000 }`.
4. Subir + `php -l` + testar home.
- **Backup:** `front-page.php.bak_pre_migracao_20260812` + `style.css.bak_pre_migracao_20260812`.

### Etapa 2 — top10_canonico.json no tema do canônico
1. Copiar `top10_canonico.json` pro `/img/` (ou raiz) do tema do canônico.
2. O script `atualizar_top10_espelho.py` (NYC) já gera o JSON. Mudar o destino: scp pro canônico também (ou só canônico). Linha: `ESP_PATH = "/var/www/ocafezinho/wp-content/themes/ocafezinho-portal/top10_canonico.json"` + host `cafezinho-wp`.
3. Ou: criar um script paralelo `atualizar_top10_canonico.py` (mesma lógica, destino canônico).
- **Nota:** o SSH NYC→canônico já funciona (alias `cafezinho-wp` no NYC? verificar). Se não, configurar.

### Etapa 3 — Worker: mudar creds das 5 verticais pro canônico
1. **REMOVER** o bloco `VERTICAIS_ESPELHO` do worker (linhas que sobrepõem `ESPELHO_WP_*`).
   - Com o bloco removido, as 5 verticais usam as creds padrão (`WP_SITE`/`WP_USER`/`WP_PASS` do `chaves.sh` = canônico).
2. py_compile + deploy NYC.
- **Rollback:** re-adicionar o bloco (as 5 voltam pro espelho).

### Etapa 4 — Confirmar cron + testar
1. O cron das 5 verticais já está ativo. Com a Etapa 3, elas passam a publicar DRAFT no canônico automaticamente.
2. Aguardar próximo disparo OU rodar manualmente: `v4_vertical_draft_worker.py economia` (sem FORCE_ESPELHO).
3. Verificar: draft criado no canônico (wp-admin ocafezinho.com, categoria Economia).
4. Confirmar: canônico home 200, blocos aparecem, Mais Vistos carrega.

### Etapa 5 — Pós-migração
1. **Religar Basic Auth do espelho** (1 linha + reload nginx): o espelho volta a ter senha.
2. Atualizar `MONITORAMENTO_DE_TRABALHO.md` (fase 0 → migrado pro canônico).
3. Atualizar Cérebro (checkpoint final).
4. Avisar Claude Code (a revisão agora é no canônico).

## Rollback GERAL (se algo quebrar)
- **Worker:** re-adicionar `VERTICAIS_ESPELHO` (5 verticais voltam pro espelho).
- **Front-page canônico:** restaurar `front-page.php.bak_pre_migracao_20260812`.
- **Cron:** comentar as 5 linhas (para as verticais).
- **Logo:** já é v10 nos dois (não precisa reverter).

## Riscos e cuidados
- **Canônico = PRODUÇÃO.** Erro no front-page = home derruba. Mitigação: `php -l` antes de subir, backup, testar.
- **8 verticais no canônico:** 3 ativas + 5 novas. O lock global cuida da concorrência.
- **O Mais Vistos:** no canônico, os links já apontam pra `ocafezinho.com` (não precisa mudar — já são do canônico).
- **Basic Auth do espelho:** religar depois (o espelho volta a ser lab protegido).

## Tempo estimado
- Etapa 1 (front-page + CSS): ~15 min.
- Etapa 2 (top10): ~5 min.
- Etapa 3 (worker): ~5 min.
- Etapa 4 (testar): ~10 min (ou esperar cron).
- Etapa 5 (pós): ~5 min.
- **Total: ~40 min.**
