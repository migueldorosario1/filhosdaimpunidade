# Ponto de Retomada — Claude Code — R4 Integração final

## 1. Identidade

- **Agente:** Claude Code (agente oficial da **Anthropic**, modelo `claude-opus-4-7`)
- **NÃO É:** GLM/Ming (agente da Zhipu AI, wrapper `~/bin/glm`). Identidades separadas. Wrapper/CLI não transfere autoria, sessão, missão ou assinatura.
- **Wrapper de execução:** superfície "Claude Code CLI" (`~/bin/claude`), Anthropic direto.
- **Data:** 2026-07-18
- **Hora:** 13:45 BRT (BRT = UTC-3, America/Sao_Paulo)
- **Sessão:** `CLAUDE-V4-INTEGRACAO-R4-20260718-1255`
- **Sessão anterior (R3):** `CLAUDE-V4-INTEGRACAO-R3-20260718-1030` — ponto de retomada gravado em `ponto_retomada_claude_v4_r3_20260718_1202.md`

## 2. Missão recebida

Do fórum `forum_rodada4_cartum_canario_ativacao_v4_20260718.md` § "Claude Code — Anthropic — integração e dry-run completo":

1. corrigir o bloqueio MIME/PDF com testes;
2. integrar o compositor aprovado à interface do pipeline, sem WordPress;
3. preservar desenho original e produzir derivado composto rastreável;
4. consumir o input aprovado por Kimi, telemetria AGY e contrato visual;
5. executar dry-run completo e local: input → redator simulado/fixture → revisão → mídia → faixa → fila simulada;
6. produzir comando único, matriz de entrada/saída, backup e rollback;
7. preparar plano da futura prova real com teto de custo, sem executá-la.

Restrições: sem WordPress vivo, sem chamada paga, sem deploy, sem SSH, sem cron, sem publicação, sem editar arquivo reservado por outro agente, sem aprovar própria entrega, sem sistema de notas 1–5.

## 3. Resultado alcançado

- **Regressão consolidada:** 360 passed, 0 failed em 104.33s.
  - 323 canônicos preservados (baseline R2)
  - 12 negativos R3 (hard stop + pré-gate mídia + telemetria + WP indisponível)
  - **17 MIME R4 novos** (magic bytes, PDF disfarçado, symlink, HTML/SVG)
  - **8 compositor R4 novos** (proveniência separada, logo canônica, determinismo, PDF bloqueado antes de compor)
- **Filtro MIME:** implementado em `mime_filter.py`, integrado ao `composer_integration.py`. Bloqueia PDF/SVG/HTML/executáveis mesmo com extensão `.png`. Cobre CAOS-07 do GLM.
- **Interface do compositor Grok:** implementada em `composer_integration.py`. Consome compositor R4 do Grok via import isolado; aplica filtro MIME antes; resolve logo canônica DeepSeek automaticamente (SHA-256 auditado); expõe 4 hashes distintos (desenho original, composto, logo, texto da faixa).
- **Canário R4 dry-run:** estendido com nova etapa `stage_faixa`. Executado com fixture patrimônio Grok + desenho placeholder + logo canônica DeepSeek → `faixa_outcome=composed, faixa_logo_canonicidade=canonical, cost=0, network=false, wordpress=false`. Também executado sem drawing_path → `no_composition:sem_desenho` (fail-closed honesto).
- **Plano da futura prova real:** documentado em `PLANO_PROVA_REAL_R4.md` com pré-condições, comando exato, teto de custo (US$ 0.05 / 10 chamadas), autorização escrita exigida — **não executado**.
- **Patch AGY B-01/B-02 auditado:** **rejeitado após causar 10 regressões** (quebra idempotência de replay legítimo). Rollback imediato via `codigo/telemetry.py.bak_pre_claude_r4_20260718_133205`. Pendência reportada para AGY revisar spec.
- **7 falhas GLM/Ming:** classificadas. B-R4-07 (PDF disfarçado) **resolvido** pelo filtro MIME. Outros 6 (B-R4-02/05/06/08/09/10) são internos ao `compositor.py` do Grok — encaminhados via manifesto.

## 4. Arquivos e evidências

### Novos artefatos no lab `labs/sprints_v4_20260718/claude_integracao/`

- `MANIFESTO_R4.md` (assinatura formato R4 + `AGUARDANDO REVISÃO CODEX`)
- `MATRIZ_R4.md` (matriz entrada/saída/rollback R4 estendendo R3)
- `PLANO_PROVA_REAL_R4.md` (plano da futura prova real, não executado)
- `mime_filter.py` (filtro magic-bytes; 17 testes)
- `test_mime_filter.py`
- `composer_integration.py` (interface compositor Grok + logo canônica + MIME; 8 testes)
- `test_composer_integration.py`
- `canario_integrado_cli.py` (**editado** — adiciona `stage_faixa` + args `--drawing`/`--strip-text`)
- `canario_integrado_cli.py.bak_pre_claude_r4_20260718_133855` (backup pré-edição)
- `_outputs_r4/`, `_outputs_r4_full/`, `_outputs_r4_canonica/` (execuções do canário R4)

### Backups R4 em `codigo/`

- `codigo/telemetry.py.bak_pre_claude_r4_20260718_133205` — usado para rollback do patch AGY rejeitado (o `codigo/telemetry.py` atual é o baseline R3, íntegro)

### Registros em fóruns

- `Cerebro/Foruns/inbox_trindade/claude.md` — CHECK R4 completo (formato exato exigido) com escopo, arquivos reservados, primeiro comando seguro, estratégia em ondas, dependências.
- `Cerebro/Foruns/canal_trindade.md` — 2 ponteiros meus na R4: CHECK inicial (12:55 BRT) + este ponto de retomada.
- `Cerebro/Foruns/ponto_retomada_claude_v4_r4_20260718_1345.md` — este arquivo.

## 5. Testes executados

### Suíte consolidada R4

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
python3 -m pytest \
  codigo/test_contracts.py codigo/test_casos_editoriais.py \
  codigo/test_wordpress_media.py codigo/test_last_mile_reconcile.py \
  codigo/test_redator_telemetria_end_to_end.py \
  labs/sprints_v4_20260718/claude_integracao/test_integracao_negativos.py \
  labs/sprints_v4_20260718/claude_integracao/test_mime_filter.py \
  labs/sprints_v4_20260718/claude_integracao/test_composer_integration.py \
  -q --tb=no
```
Última execução: **360 passed, 0 failed em 104.33s**

### Testes MIME R4 (novos, cobrem CAOS-07)

- 17 testes passando isoladamente em 0.03s
- `test_pdf_disfarcado_rejeitado`, `test_pdf_com_extensao_png_rejeitado`
- `test_svg_rejeitado`, `test_html_rejeitado`
- `test_symlink_rejeitado`
- `test_arquivo_vazio_rejeitado`, `test_bytes_desconhecidos_rejeitados`
- `test_png/jpeg/webp/gif_valido_aceito`
- `test_candidate_bytes_pdf_rejeitado`, `test_candidate_local_path_png_aceito`, `test_candidate_sem_bytes_nem_path_rejeitado`

### Testes compositor R4 (novos, proveniência separada)

- 8 testes passando em 0.65s
- `test_resolve_canonical_logo_no_workspace_real` — logo canônica DeepSeek confirmada por SHA-256
- `test_compose_com_logo_placeholder_e_desenho_valido` — 4 hashes distintos gerados
- `test_desenho_com_pdf_rejeitado_antes_de_compor` — CAOS-07 do GLM coberto
- `test_determinismo_composed_image_sha256` — mesmas entradas ⇒ mesmo hash
- `test_logo_ausente_e_sem_placeholder_bloqueia` — fail-closed sem logo
- `test_desenho_ausente_bloqueia` — fail-closed sem desenho
- `test_import_nao_abre_socket` — sem side-effects de rede no import

### Canário R4 dry-run

```bash
python3 labs/sprints_v4_20260718/claude_integracao/canario_integrado_cli.py \
  --input labs/sprints_v4_20260718/grok_midia_integracao/fixtures/gate_b/01_patrimonio_desastre.json \
  --drawing labs/sprints_v4_20260718/grok_compositor_r4/fixtures/desenhos/desenho_a.png \
  --strip-text "Museu histórico arde: prevenção sem verba." \
  --output-dir labs/sprints_v4_20260718/claude_integracao/_outputs_r4_canonica
```
Última saída: `cost=0.0, faturavel_calls=0, faixa_outcome=composed, faixa_logo_canonicidade=canonical, network_call_performed=false, wordpress_delivered=false, faixa_original_drawing_sha256=18dbd7..., faixa_composed_image_sha256=d9601c...` ✅

## 6. Custo

- **Chamadas pagas:** US$ 0.00 (zero)
- **Tokens externos:** 0
- **Tráfego externo:** 0 bytes
- **WordPress:** não invocado
- **SSH/deploy/cron:** não executados
- **Uso novo de disco:** ~40 KB no lab (docs + módulos + testes + saídas canário)

## 7. Decisões tomadas

1. **Rejeitar patch AGY B-01/B-02** após auditoria: 10 regressões canônicas por causa que o remédio proposto captura idempotência legítima como colisão. Rollback imediato; pendência reportada para AGY revisar spec.
2. **Aplicar filtro MIME em duas camadas:** módulo `mime_filter.py` para uso genérico + hook em `composer_integration.compose_with_provenance()` que roda o filtro **antes** de invocar o compositor Grok. Cobre CAOS-07 do GLM.
3. **Consumir compositor Grok via import isolado** (`_load_grok_compositor()` com `importlib.util.spec_from_file_location`) para evitar side-effects globais. Sem editar código Grok.
4. **Resolver logo canônica DeepSeek automaticamente** — se `logo_path` vazio, `composer_integration` tenta path canônico com SHA-256 auditado; se não bater, retorna erro auditável.
5. **Preservar proveniência separada com 4 hashes distintos** — desenho original, composto, logo, texto da faixa — nunca misturar. Determinismo garantido pelo compositor Grok.
6. **NÃO consumir input Kilo R4** — Kimi 3 ainda não emitiu parecer definitivo sobre o arquivo novo (`input_canario_geo_002_R4.json` de 13:00 BRT). Canário roda com fixture Grok como declarado no MANIFESTO_R4.md §1.
7. **NÃO tocar código Grok** para corrigir B-R4-02/05/06/08/09/10 — código reservado; encaminhado ao Grok.
8. **NÃO executar prova real** — apenas plano em `PLANO_PROVA_REAL_R4.md` com autorização escrita exigida.

## 8. Problemas e riscos encontrados

### Resolvidos nesta sessão

- **Patch AGY B-01/B-02 quebra idempotência de replay legítimo:** detectado por regressão (10 falhas), rollback imediato, spec reportado para revisão AGY. Sem sequela técnica.
- **Compose retornava `original_drawing_sha256=""`:** correção — os hashes ficam em `receipt["hashes"]`, não no root do dict. Ajustado no `composer_integration.py`.
- **`workspace_root` estava calculado 1 nível abaixo do correto:** ajustado para `_V4_LABS_ROOT.parents[2]` = `Antigravity Google/`.

### Reconhecidos, não resolvíveis nesta rodada

- **Input Kilo R4 pendente de Kimi 3:** integração está pronta pra receber assim que Kimi liberar.
- **6 bugs do compositor Grok (B-R4-02/05/06/08/09/10):** fora do meu escopo; encaminhados.
- **Logo canônica é JPEG sem transparência:** DeepSeek já sinalizou; compositor Grok trata; sem impacto.
- **Prova real não executada:** aguarda autorização escrita Codex + Miguel via §5 do `PLANO_PROVA_REAL_R4.md`.

## 9. Pendências

### Para Codex
- Reexecutar regressão 360 passed e auditar 5 novos artefatos + 1 edição
- Aprovar minha rejeição do patch AGY B-01/B-02
- Decidir se autoriza Gate B canário real com input Kilo aprovado

### Para AGY
- Revisar spec do patch B-01/B-02 (quebra idempotência de replay legítimo)

### Para Grok
- Aplicar B-R4-02, B-R4-05, B-R4-06, B-R4-08, B-R4-09, B-R4-10 no compositor

### Para Kimi 3
- Reavaliar `labs/.../kilo_geopolitica/input_canario_geo_002_R4.json` (novo arquivo Kilo às 13:00 BRT)

### Para mim (Claude) no próximo ciclo, se autorizado
- Integrar input Kilo após parecer Kimi
- Estender canário para consumir texto de faixa aprovado por Kimi
- Executar `PLANO_PROVA_REAL_R4.md` apenas com §5 preenchida e assinada

## 10. Rollback

Documentado em `MATRIZ_R4.md` §7. Executável em <2 min.

Rollback total dos novos artefatos R4 (sem tocar canônico):

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
rm labs/sprints_v4_20260718/claude_integracao/mime_filter.py
rm labs/sprints_v4_20260718/claude_integracao/test_mime_filter.py
rm labs/sprints_v4_20260718/claude_integracao/composer_integration.py
rm labs/sprints_v4_20260718/claude_integracao/test_composer_integration.py
rm labs/sprints_v4_20260718/claude_integracao/MANIFESTO_R4.md
rm labs/sprints_v4_20260718/claude_integracao/MATRIZ_R4.md
rm labs/sprints_v4_20260718/claude_integracao/PLANO_PROVA_REAL_R4.md
# reverter canário para versão R3:
bak=$(ls -1 labs/sprints_v4_20260718/claude_integracao/canario_integrado_cli.py.bak_pre_claude_r4_* | tail -1)
cp "$bak" labs/sprints_v4_20260718/claude_integracao/canario_integrado_cli.py
rm -rf labs/sprints_v4_20260718/claude_integracao/_outputs_r4*
python3 -m pytest codigo/test_contracts.py codigo/test_casos_editoriais.py \
  codigo/test_wordpress_media.py codigo/test_last_mile_reconcile.py \
  codigo/test_redator_telemetria_end_to_end.py -q --tb=no
# esperado: 323 passed
```

O patch AGY B-01/B-02 já está em rollback (baseline R3 restaurado). Sem `git reset`. Sem `--force`. Sem delete de recibo histórico.

## 11. Primeiro comando seguro para continuar

Antes de qualquer ação futura na trilha "integração final Claude R4":

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_labs"

# 1. Confirmar 360 passed:
python3 -m pytest \
  codigo/test_contracts.py codigo/test_casos_editoriais.py \
  codigo/test_wordpress_media.py codigo/test_last_mile_reconcile.py \
  codigo/test_redator_telemetria_end_to_end.py \
  labs/sprints_v4_20260718/claude_integracao/test_integracao_negativos.py \
  labs/sprints_v4_20260718/claude_integracao/test_mime_filter.py \
  labs/sprints_v4_20260718/claude_integracao/test_composer_integration.py \
  -q --tb=no

# 2. Confirmar canário R4 dry-run funcional:
python3 labs/sprints_v4_20260718/claude_integracao/canario_integrado_cli.py \
  --input labs/sprints_v4_20260718/grok_midia_integracao/fixtures/gate_b/01_patrimonio_desastre.json \
  --drawing labs/sprints_v4_20260718/grok_compositor_r4/fixtures/desenhos/desenho_a.png \
  --strip-text "smoke check R4" \
  --output-dir labs/sprints_v4_20260718/claude_integracao/_outputs_r4_smoke_$(date +%s)

# 3. Confirmar SHA-256 da logo canônica não mudou:
python3 -c "
import hashlib
p='../../../sites-tematicos/cafezinho/src/assets/logo.png'
h=hashlib.sha256(open(p,'rb').read()).hexdigest()
print('canonical' if h=='f03c8f68c9f3b5e3ed8798bbbc33378e7b7c8fc281772f0f7b9a32595cf8eb84' else 'DIVERGENTE:'+h)
"
```

Todos os três são idempotentes, locais, sem rede, sem WordPress, sem chamada paga.

## 12. Estado final desta entrega

- Regressão: **360 passed, 0 failed** (323 canônicos + 12 negativos R3 + 17 MIME R4 + 8 compositor R4)
- Custo: **US$ 0.00**
- Efeitos externos: **nenhum**
- Publicação: **nenhuma**
- Manifesto R4 assinado com formato R4 completo em `MANIFESTO_R4.md`
- Plano da prova real em `PLANO_PROVA_REAL_R4.md` — **NÃO EXECUTADO**

**AGUARDANDO REVISÃO CODEX** para: (a) validar os 5 novos artefatos R4 + 1 edição, (b) aprovar rejeição do patch AGY B-01/B-02, (c) decidir se autoriza um Gate B canário real com fixture aprovada + input Kilo aprovado + teto de chamadas explícito.

---

*Ponto de retomada assinado por Claude Code (`claude-opus-4-7`), agente da Anthropic, sessão `CLAUDE-V4-INTEGRACAO-R4-20260718-1255`, em 2026-07-18 13:45 BRT.*
*Este agente é distinto de GLM/Ming (Zhipu AI, wrapper `~/bin/glm`). Nenhuma autoria, sessão, voto, missão ou assinatura pode ser compartilhada entre os dois.*
