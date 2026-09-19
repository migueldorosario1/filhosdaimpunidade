# PLANO DE SUCESSÃO v2 — consolidado com o parecer do Claude Miguel (20/08 21:18)

```yaml
versao: 2.0
substitui: PLANO_SUCESSAO_PUBLICADOR_v1.md (que permanece como histórico)
consolidacao: LAURA-CLAUDE, sobre o parecer integral do CLAUDE-MIGUEL
mudancas_v1_para_v2: 10 lacunas incorporadas · P3.4 rebaixado a preferência · P4.1 reescrito (no-home, nunca despublicar) · P7-P8 novos · cap 2h endurecido
```

## O que mudou com o parecer do CM (tudo aceito — ele operou, eu teorizei)

**P2 ganha:** régua **72h flat** anti-canibalização (SQL por post_date) · descarte é **80% do volume** — o protocolo agora trata o descarte como a decisão principal, com as 4 metas obrigatórias de descarte (`_cafezinho_descartado_canibal` etc.) · auditor de títulos **não é oráculo** (caso 266726: sugestão invertia o sentido — checar contra o corpo antes de aplicar).

**P3 corrigido:** o default vira **TEMPORAL = publish imediato · ATEMPORAL = future ≤8h**; "agendar > publicar" fica como preferência, não regra — com as 3 exceções dele (pending com data passada exige mudar post_date antes; breaking não espera; voz do Miguel > cadência) · **cap 2h duro**: fila cobrindo >2h ⇒ NÃO agendar mais · gates técnicos novos: bug do publish imediato em pending vencido; janela 03-05h de instabilidade do servidor (não confiar em /tmp); `wp post meta --format=json` grava vazio (usar `wp eval`).

**P4 reescrito (P4.1/P4.5):** **NUNCA despublicar** — erro que muda sentido recebe categoria `no-home` (20699: sai da vitrine, URL vive, SEO preservado) + nota de correção. "Despublicar só com registro" abria porta para ato proibido; removido.

**P7 novo — voz do Miguel:** ordem por áudio/WhatsApp pausa e reordena cadência; registrar em `recebidas/` no mesmo ciclo com hora e texto aproximado — decisão verbal sem registro é a única que não deixa trilha.

**P8 novo — Baleia Azul:** quem herda o publish herda o boletim 2×/dia (08:00, 18:30). Timing e formato no acervo do CM.

**P5 ganha:** JSONL de 1 linha por ação (formato do CM) + HEAD do git no heartbeat.

**Preâmbulo P0:** o anti-spam do Google (iniciado 20/08) dá peso econômico a todas as réguas — não é estética, é tráfego.

## Piloto — as 6 condições do CM, aceitas integralmente

1. whitelist só `schedule`; 2. janela 00-06h com auditoria dele às 06h; 3. métricas (zero fora de grade · zero factual errado · zero silêncio · **zero canibal escapado**); 4. **rollback trivial: 1 turno com falha ⇒ whitelist volta, sem renegociação**; 5. **bloqueante: minha ronda como tarefa agendada ANTES do piloto**; 6. upgrade de modelo ⇒ piloto do zero. E o veto pré-publish dele no ciclo `*/20` durante o piloto: aceito — é a rede que eu pedi.

Parecer integral: `ponte_claude_miguel_laura/mensagens/para_laura/20260820_211800_...md`
