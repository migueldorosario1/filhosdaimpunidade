# Fórum — Painel de Grade de Aprovação Humana do Banco Ouro (lote)

**Abertura:** 9 de agosto de 2026, ~18:00 BRT  
**Solicitante:** Miguel do Rosário (voz)  
**Implementador:** GLM-5.2 (Z.ai coding plan) no ZCode  
**Estado:** ✅ ENTREGUE E NO AR  

## 1. Contexto e decisão

O Miguel (em voz) pediu um painel de aprovação humana **muito mais funcional** que o foto-a-foto atual: uma **grade panorâmica** com muitas imagens pequenas (thumbnails leves), filtros por editoria/entidade, edição inline de campos e **aprovação em massa** ("clicar, clicar, clicar, bota aprovar tudo"). A motivação: a fila de revisão humana tem 477 itens pendentes e o fluxo 1-por-vez é lento demais.

**Decisão arquitetural (após plano aprovado):** nova rota `/midia-ouro/grade` no **app 8091 existente** (`/root/painel_midia_ouro.py`, Tencent), que já tem acesso ao SQLite master, imagens no R2 (boto3), a transação `apply_review` e a fila `fila_catalogacao_humana_ouro`. **Não duplica nem quebra** o fluxo foto-a-foto (`/revisao`) nem a busca ativa (`/busca-ativa`) — é uma rota nova ao lado deles.

## 2. O que foi entregue

### 2.1 Componentes backend (novos, em `/root/painel_midia_ouro.py`)

| Função | Responsabilidade |
|---|---|
| `_thumb_para(hash)` | Gera thumbnail leve (~12-25KB, 400px máx) via Pillow 12.x a partir do original R2. Cache em disco `_thumbs_grade/<hash>.jpg`. Self-healing se corrompido. |
| `grade_payload(tema, entidade, status, ordem, offset, limit)` | SELECT read-only na fila `fila_catalogacao_humana_ouro` JOIN `midia_ouro` com filtros. Retorna itens + facetas (temas/entidades disponíveis) + contagem total. Exclui instituições (Senado/Câmara/STF), igual ao `review_payload`. |
| `decidir_lote(payload)` | Aprova/revisa/bloqueia múltiplos itens numa **única transação** (commit único = atômico). Reusa os mesmos 3 UPDATEs do `apply_review` (midia_ouro + propagação entidade + fila). Validação `catalogacao_incompleta` mantida. Máx 200 itens/lote. |

### 2.2 Endpoints novos (registrados em do_GET/do_POST/do_HEAD)

| Método | Rota | Função |
|---|---|---|
| GET | `/midia-ouro/grade` | Página HTML da grade (`GRADE_HTML`) |
| GET | `/api/midia-ouro/grade` | JSON com itens paginados + filtros |
| GET | `/api/midia-ouro/thumb/<hash>` | Thumbnail cacheado (Cache-Control 24h) |
| POST | `/api/midia-ouro/grade/decidir_lote` | Aprovação/revisão/bloqueio em lote |

Aliases `/midia-ouro/api/...` preservados (padrão do app).

### 2.3 UI da grade (`GRADE_HTML`)

- **Header sticky** com filtros: `<select>` tema (10 opções dinâmicas), `<select>` entidade (60 dinâmicas), `<select>` ordem (recente/antigo/foto nova/foto velha/entidade/prioridade), link "selecionar tudo visível".
- **Grade responsiva** (`grid-template-columns: repeat(auto-fill, minmax(150px, 1fr))`): cards com thumbnail 150px, checkbox de seleção (canto), overlay info (entidade + tema + data).
- **Editor inline expansível**: clique no card seleciona + expande campos (entidade, pessoas identificadas pré-preenchidas com sugestão Gemini, observação).
- **Lightbox**: clique na imagem abre original full-res (`/api/midia-ouro/img/<hash>`).
- **Barra de ação fixa no rodapé**: contador "N selecionados" + botões Aprovar (verde) / Revisar não-auto (azul) / Bloquear (vermelho) / Limpar seleção. Confirmação modal antes de aplicar.
- **Paginação**: anterior/próximo, 48/página.
- **Dark theme** GitHub `#0d1117` (igual às páginas existentes), mobile-first.

## 3. Smoke test (09/08 ~18:00 BRT)

| Teste | Resultado |
|---|---|
| Página `/midia-ouro/grade` | HTTP 200, 14.988 bytes |
| API `/api/midia-ouro/grade?limit=3` | `ok:True`, total 477, 3 itens, 10 temas, 60 entidades |
| Thumb (1º item) | HTTP 200, **12.026 bytes** (~12KB, vs ~2,8MB original) |
| Filtro tema=politica | 218 itens |
| Filtro entidade=Lula | 1 item |
| Público via nginx `/midia-ouro/grade` | HTTP 200 |
| Rotas antigas (`/`, `/revisao`, `/status`) | todas 200 (intactas) |
| Log | sem erros |

## 4. Disciplina Cérebro (cumprida)

- **Backup:** `/root/painel_midia_ouro.py.bak_pre_grade_20260809` (Tencent) + `ZCodeProject/painel_fix/painel_midia_ouro_ORIG_20260809.py` (local). Nenhum arquivo se perdeu.
- **Escrita só no master** Tencent (a transação `decidir_lote` faz commit único no master, igual ao `apply_review`). Réplica NYC intocada.
- **Rollback:** `sudo cp /root/painel_midia_ouro.py.bak_pre_grade_20260809 /root/painel_midia_ouro.py && sudo systemctl restart midia-ouro-panel.service`.
- **Deploy:** `sudo systemctl restart midia-ouro-panel.service` (service `enabled`/`active`).

## 5. O que aconteceu / o que falta / o que preciso de você (Miguel)

**O que aconteceu:** painel de grade panorâmica construído, deployado e testado no ar. 477 itens pendentes agora navegáveis em grade com thumbs leves, filtros e aprovação em lote.

**O que falta:** teste real do Miguel — abrir `/midia-ouro/grade`, filtrar por tema/entidade, selecionar vários, editar campos dos que precisar, aprovar em lote. Validar que a UX está fluida como imaginou. Ajustes possíveis: tamanho dos cards, mais filtros, atalhos de teclado, etc.

**O que preciso de você (Miguel):** teste ao vivo + feedback de UX. Se achar que falta algo (ex.: mais campos editáveis, ordenação diferente, agrupamento visual por entidade), me diga que ajusto.

— GLM-5.2 (Z.ai coding plan) no ZCode, 09/08/2026 18:00 BRT
