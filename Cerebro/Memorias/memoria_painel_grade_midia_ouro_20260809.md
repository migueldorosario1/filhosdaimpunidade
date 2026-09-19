# Memória — Painel de Grade de Aprovação Humana do Banco Ouro (lote)

**Data:** 9 de agosto de 2026, ~18:00 BRT  
**Implementador:** GLM-5.2 (Z.ai coding plan) no ZCode  
**Fórum irmão:** `forum_painel_grade_midia_ouro_20260809.md`

## 1. Missão

Miguel (voz, 09/08 ~17:30): criar painel de aprovação humana de mídia muito mais funcional que o foto-a-foto atual — grade panorâmica com thumbnails leves, filtros por editoria/entidade, edição inline, aprovação em massa.

## 2. Arquitetura

- **Onde:** nova rota `/midia-ouro/grade` no app 8091 existente (`/root/painel_midia_ouro.py`, Tencent). Service `midia-ouro-panel.service`, porta 8091, nginx `/midia-ouro/`.
- **Por que não V6:** o V6 (`painel_cctv_v6.py`, porta 8084) só lê arquivos locais + HTTP, não acessa SQLite/R2. O app 8091 já tem SQLite master (mode=ro), R2 (boto3), transação `apply_review`, fila `fila_catalogacao_humana_ouro`. Reaproveitar = não duplicar.
- **Python stdlib + Pillow 12.1.1** (disponível no Tencent). Sem frameworks (igual ao app original).

## 3. Arquivos tocados

| Arquivo | Ação |
|---|---|
| `/root/painel_midia_ouro.py` (Tencent) | **Editado** — adicionadas funções `_thumb_para`, `grade_payload`, `decidir_lote`, constante `GRADE_HTML`, rotas em `do_GET`/`do_POST`/`do_HEAD`. 59.361 → 88.434 bytes (+29KB). |
| `/root/painel_midia_ouro.py.bak_pre_grade_20260809` (Tencent) | **Backup** (cópia pré-edit) |
| `ZCodeProject/painel_fix/painel_midia_ouro.py` | **Cópia de trabalho** (editada) |
| `ZCodeProject/painel_fix/painel_midia_ouro_ORIG_20260809.py` | **Preservação original** |

## 4. Funções novas (detalhe técnico)

### `_thumb_para(hash_sha) -> Path | None`
- Pillow `Image.open` do bytes do R2 → `thumbnail((400,400), LANCZOS)` → JPEG quality 75 optimize → `_thumbs_grade/<hash>.jpg`.
- Cache hit se arquivo existe e >1KB. Self-healing se vazio/corrompido (regera).
- Prefere `r2_portal_key` se existir (igual ao `/img/`), senão `r2_key`.

### `grade_payload(tema, entidade, status, ordem, offset, limit) -> dict`
- `SELECT ... FROM fila_catalogacao_humana_ouro f JOIN midia_ouro m WHERE f.resolvido_em IS NULL AND <filtros>`.
- Filtros: `tema` (lower), `entidade` (lower), `status` (pendentes|todos), `ordem` (recente/antigo/foto_nova/foto_velha/entidade/prioridade).
- Exclui instituições (`Senado Federal`, `Camara dos Deputados`, `STF`).
- Facetas: `temas_disponiveis` (10), `entidades_disponiveis` (top 60), `fila_total`.
- Enriquece cada item: `pessoas_sugeridas` (Gemini + entidade + canon), `thumb_url`, `img_url`.

### `decidir_lote(payload) -> dict`
- Valida todos (action, hash); rejeita inválidos antes da transação.
- `db_write(work)`: UM commit para todos os itens (atômico). Para cada item: mesma lógica do `apply_review` (3 UPDATEs: midia_ouro + propagação entidade para índice/FTS + fila resolvido_em).
- Mantém validação `catalogacao_incompleta` (approve c/ ≥2 pessoas visíveis e nomes insuficientes → rejeita aquele item, não aborta lote).
- `entidade_override`: se 1 nome identificado → vira entidade (regra Kimi K3 06/08); entidade explícita no edit tem prioridade.
- `revisado_por='painel_midia_ouro_grade_lote'` (distingue do foto-a-foto).
- Máx 200 itens/lote. Retorna `{ok, aplicados, rejeitados:[{hash,motivo}], fila_restante}`.

## 5. UI (`GRADE_HTML`, ~15KB inline)

- CSS: variáveis `--bg:#0d1117` etc (igual REVIEW_HTML). Grid `auto-fill minmax(150px,1fr)`. Cards com `.selected` (borda dourada) + `.expanded` (editor visível). Barra fixa bottom. Lightbox z-index 100.
- JS vanilla (sem framework): `state = {itens, selecionados:Set, edits:{}, offset, filtros}`.
  - `carregar()`: fetch API grade → render grade + filtros + paginação.
  - `toggleSel(hash)`: add/remove Set + toggle classes.
  - `coletarLote()`: mescla edits do `state.edits` nos selecionados.
  - `aplicarLote(action)`: POST decidir_lote com confirmação → recarrega.
  - Lightbox: click na imagem abre full-res.
- Responsivo: `@media (max-width:600px)` reduz cards para 120px.

## 6. Endpoints (registro em do_GET/do_POST/do_HEAD)

```python
# do_GET:
if path in {"/midia-ouro/grade", "/midia-ouro/grade/"}: → GRADE_HTML
if path in {"/api/midia-ouro/grade", "/midia-ouro/api/grade"}: → grade_payload(...)
if path.startswith("/api/midia-ouro/thumb/"): → _thumb_para + Cache-Control 24h
# do_POST:
if path in {"/api/midia-ouro/grade/decidir_lote", ...}: → decidir_lote(...)
```

## 7. Lições técnicas

1. **Heredoc bash com Python quebra aspas** — sempre usar arquivo de script `.py` separado para SQL complexo, nunca `ssh host 'python3 -c "..."'` com aspas duplas em literais SQL.
2. **`propagação entidade` em FTS** pode falhar silenciosamente — mantido `try/except` como no original.
3. **Cache-Control de thumb** = `public, max-age=86400` (24h) — diferente do `no-store` das páginas dinâmicas; correto porque o thumb é imutável por hash.
4. **`grade_payload` exclui instituições** igual ao `review_payload` (regra Miguel 04/08: "não quero Senado Federal, quero PESSOAS").

## 8. O que aconteceu / o que falta / o que preciso de você (Miguel)

**O que aconteceu:** painel de grade panorâmica construído, deployado e testado. 477 itens navegáveis em grade com thumbs de ~12KB, filtros (tema/entidade/status/ordem), seleção múltipla, edição inline e aprovação em lote atômica. Rotas antigas intactas.

**O que falta:** teste real do Miguel ao vivo. Ajustes de UX conforme feedback (tamanho de card, mais filtros, atalhos teclado, agrupamento visual).

**O que preciso de você (Miguel):** abrir `https://[dominio]/midia-ouro/grade`, testar filtros + seleção + aprovação em lote, e me dizer o que ajustar.

— GLM-5.2 (Z.ai coding plan) no ZCode, 09/08/2026 18:00 BRT
