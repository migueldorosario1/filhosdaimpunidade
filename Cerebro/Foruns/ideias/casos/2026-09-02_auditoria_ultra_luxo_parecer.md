# 🔍 PARECER — AUDITORIA ULTRA-LUXO (ZM-20260902-043, auditoria 1 pedida pelo Miguel ao DS-N Ideias)

> **Pendência:** MEMORIA_VIVA do DS-N Ideias (bloco ZM-043, ~15:3x) — experimento frontier na redação (NYC `/root/v4_labs`): nacional=`claude-fable-5`, demais=`gpt-5.6-sol`. Ver: `contratos/v4_rotas_llm_limpas_v1.json` (contextos `v4_ultra_luxo_*`), `dados/ultra_luxo.json` (knob), `scripts/aplica_ultra_luxo.py`, ratings/pricing/providers (buscar `20260902`). **Pergunta central:** algo quebra a produção se o frontier falhar (a fila de fallback cobre? o `--desligar` restaura tudo? o teste de contrato cobre?).
> **Escopo deste parecer:** NÍVEL REPO (evidência documental em `cerebro-miguel`) — os arquivos de código NYC/Tencent runtime NÃO estão neste workspace (sandbox; e execução é ofício do ZM). O parecer diz o que o repo PROVA, o que FALTA provar e o checklist de campo. Natureza: análise, não execução.

## 1. Evidência disponível no repo (o que PROVA)

Fonte: `cerebro/Foruns/forum_v41_ultra_luxo_cura_geo_20260902.md` (ZM-043, 02/09) + `cerebro/Memorias/memoria_v41_ultra_luxo_cura_geo_20260902.md` + `MANUAL_DE_ESCRITA.md` v2.1.0 (mesmo pacote):

1. **Fila de fallback declarada íntegra:** "Fila inteira preservada (gpt-5.5 → opus → gemini → deepseek → moonshot): frontier falhou, produção segue." — a troca ultra-luxo é de CABEÇA de fila (frontier na frente), não de remoção do resto.
2. **Dispositivo de troca com backup datado:** `scripts/aplica_ultra_luxo.py --status | --geral X --nacional Y | --desligar` — valida no ratings, backup datado, reconstrói contextos; `--desligar` restaura rotas do `.bak.pre_ultra_luxo_20260902` (= contexto super luxo, o grau anterior).
3. **Backups e rollback indexados:** backups `.bak_*` em cada arquivo tocado + entradas `V41_ULTRA_LUXO_SOL` no `ROLLBACK_INDEX.md` (padrão da casa: backup → prova → registro → rollback escrito).
4. **Prova de fogo inicial:** dry-run do router 12/12 editorias (nacional→fable-5; demais→sol) + 1º post real **268674** (18:08 UTC, sol, $0,0228 esperado).
5. **Monitoramento 1/1h:** `scripts/monitor_ultra_luxo.py` (NYC) + ZCode :15 reportando no Telegram (read-only, nunca patcha).
6. **Promo:** sol $4/$20 até 21/11; fable-5 $10/$50.

## 2. Respostas às 3 perguntas do Miguel (nível repo)

| Pergunta | Resposta de nível repo | Lacuna de campo (provar com acesso NYC) |
|---|---|---|
| **A fila de fallback cobre?** | SIM, por desenho e por declaração: a fila (gpt-5.5→…→moonshot) segue atrás do frontier; o knob só reordena a cabeça. **Mas:** o próprio forum declara vulnerabilidade — a cadeia verificadora (GLM/DeepSeek/Moonshot) é FRACA em pauta afirmativa (retorna `llm_sem_tese_valida`): frontier caiu → produção NÃO para, mas a tese DEGRADA (qualidade, não quebra). | Log de um ciclo real com frontier fora (fila assumindo): registrar ok/degradação + tempo de fall-through. Dono: ZM (execução), eu (veredito). |
| **O `--desligar` restaura tudo?** | SIM, por desenho: `.bak.pre_ultra_luxo_20260902` = contexto super luxo; restaura rotas e reconstrói contextos; monitor 1/1h acompanha. | Rodar `--desligar` (ou `--status`) numa janela de baixo tráfego e conferir rotas/contextos pós-restauro + 1 post de prova. Dono: ZM. |
| **O teste de contrato cobre?** | **NÃO PROVADO no repo:** o forum documenta dry-run do router (12/12) e 1 post real, mas NÃO cita teste automatizado de contrato pós-troca (validação de campos/meta/contextos por editoria). | Verificar se existe teste de contrato no v4_labs p/ `v4_ultra_luxo_redacao*`; se não existe, criar (sugestão de desenho abaixo). Dono: ZM. |

## 3. Riscos e recomendações (desenho)

- **R1 — Degradação de tese na pauta afirmativa (o risco real de "quebrar"):** não é falha de entrega, é falha de QUALIDADE silenciosa — frontier cai, a cadeia fraca assume e devolve `llm_sem_tese_valida` ou tese fraca em pauta BRICS/SCO (o caso que a cura geo atacou). **Recomendação:** o monitor 1/1h ganha 1 linha: "se a tese do ciclo saiu da cadeia não-frontier em pauta afirmativa → avisar o Telegram (sinal, não alerta)" — a casa decide se aceita a degradação ou pausa a editoria.
- **R2 — Custo sem régua no repo:** o D8 (telemetria/custos) está PARADO por ordem do Miguel até a reforma dos verticais; só 1 post de custo documentado (268674 $0,0228). **Recomendação:** o Miguel mede (como o forum pede); sugiro régua: ultra-luxo vale enquanto o custo/dia da redação ficar ≤ teto D8 da época; o `--desligar` é o gatilho de volta (grau abaixo).
- **R3 — Falta o teste de contrato:** desenho de 1 teste (quando o ZM executar): após `--geral/--nacional/--desligar`, validar que os contextos `v4_ultra_luxo_*` existem/casam com as rotas do ratings p/ TODAS as editorias (parametrização do dry-run 12/12, agora como teste repetível pós-troca).

## 4. Checklist de campo (dono ZM — execução; eu não mexo em produção)

1. `aplica_ultra_luxo.py --status` (estado atual do knob e rotas).
2. Conferir entradas `V41_ULTRA_LUXO_SOL` no `ROLLBACK_INDEX.md` (02/09) + `.bak_*` existentes.
3. Procurar teste de contrato p/ `v4_ultra_luxo_*` (se ausente, criar com a régua do R3).
4. 1 janela de observação com frontier fora (ou simulação em espelho) p/ medir fall-through + degradação de tese.
5. Reportar custo acumulado do dia (o Miguel decide o retorno ao super luxo).

**Veredito (nível repo):** o desenho do ultra-luxo segue o protocolo da casa (backup → prova → registro → rollback escrito) e a fila cobre falha do frontier — **não há risco de quebra de produção documentado**; há risco de DEGRADAÇÃO silenciosa de tese em pauta afirmativa e lacuna de teste de contrato, ambos com dono ZM e veredito pendente de campo. Nada a alterar em produção por mim (Lei de Poderes).

— DS Nuvem Ideias (DS-N Ideias) · 20260902 15:49:29 BRT
