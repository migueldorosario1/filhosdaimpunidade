# 🛡️ PLANO DE SEGURANÇA DE IMPLEMENTAÇÃO — Constituição/Contrato v3 + V4.2 (análise de risco + ondas)

> **Encomendador:** Miguel, direto ao DSC, 02/09/2026 ~00:3x BRT ("plano de segurança pra implementar esse contrato sem criar instabilidade — ele tem que OFERECER estabilidade e segurança ao sistema").
> **Objeto:** promulgação e ativação do Contrato v3 (Constituição) + V4.2 + capítulos D8-D11, conforme dossiê da noite e consulta pública (9 pareceres, 0 rejeições até 00:30).
> **Princípio-mãe:** o contrato é PAPEL (risco zero). O risco mora na IMPLEMENTAÇÃO — e é controlado por sequência, raio de blast pequeno, régua e rollback.

## 1. MAPA DE RISCO (o que pode dar errado e a trava de cada um)

| # | Risco | Gravidade | Trava |
|---|---|---|---|
| R1 | **Lei morta no dia 1** — promulgar regra que o sistema ainda não cumpre (caso real: D8 telemetria congelada desde 22/08) | Média | **Vigência escalonada**: Art. 1-7 + E1-E5 vigor imediato; capítulos novos entram em vigor por onda, com nota "em reparo" quando for o caso (proposta CM) |
| R2 | **Mudança simultânea** — V4.2 + coletores + Banco Ouro + gates + anel ao mesmo tempo; se quebrar, ninguém sabe quem quebrou | **Alta** | **1 mudança por vez por vertical**; janelas separadas; cada onda tem dono único |
| R3 | **Esteira parar** (o pior cenário — 29/08: 11h sem publicar) | **Alta** | Hard news segue no **modo QUENTE** durante TODAS as ondas; health-check 15min (E5); monitor de fila (posts/h); **V4.1 congelado como fallback** com downgrade documentado |
| R4 | **Custo crescer** (self-review +5-8% · modo VALOR 3-5 fontes) | Média | QUENTE nunca quebra (custo igual); VALOR com régua de custo por pauta; **D8 consertado PRIMEIRO** — sem painel vivo, mudança é às cegas |
| R5 | **Ponte/git em corrida** (appends conflitantes — 2 hoje) | Baixa | Append-only por dono; commit só dos próprios arquivos; retry com rebase |
| R6 | **Agente cair na transição** (Grok crédito, sessão CL, relógio torto) | Média | Cargos com suplentes (a própria Constituição); escada FERRAMENTA_FORA; CM↔CL cobertura ≤24h |
| R7 | **Qualidade em público** (canário errar título/caption ao vivo) | Média | Espelho primeiro; A/B por pares; régua ≥3 vitórias + 0 erro título + FC 100% |

## 2. AS ONDAS (sequência segura)

**ONDA 0 — HOJE (papel + farol; risco ~zero)**
1. **Mini-inventário D8** (30-45 min; proposta CM): DS-N Chefe + AGY Miguel inventariam pushers/Prometheus/Grafana → religam o que morreu → snapshot ao vivo → registram na ponte. *Farol primeiro: sem telemetria viva, nenhuma onda seguinte é mensurável.*
2. ZM fecha a redação final (ressalvas absorvidas + E1-E5 + cláusula de transição de cargos).
3. Miguel lapida e **PROMULGA com vigência escalonada** (§R1).
4. CM assina na sequência (já declarado: "ASSINO quando promulgar").

**ONDA 1 — SOMBRA (48-72h; risco zero — nada publica)**
- Coletores ×3 + curador em espelho · Banco Ouro camada 1 em modo log · V4.2 em espelho (5 posts/dia `_v42_*`, não publicados) · anel de audiência em canário (2 pautas/dia).
- Saída: régua real de cada peça (acerto/erro/custo medidos).

**ONDA 2 — CANÁRIO (vertical geo, onde nasceu o Kast)**
- V4.2 publica SÓ na geo, A/B por pares; gate mídia 3 vias como lei; TEXTO_APROVADO em produção.
- Monitor ativo: 0 erro de título · 0 caption default · FC 100% · fila andando · custo no painel VIVO · quórum ≥2 loops de 30/30.

**ONDA 3 — PROMOÇÃO POR RÉGUA**
- V4.2: ≥3 vitórias seguidas no A/B · Banco Ouro: ≥80% N≥20/24h · Coletores: item válido ≥95% + dedup ≥95%.
- Rollback sempre pronto: 1 arquivo/cron · backup datado · registro no ROLLBACK_INDEX (ZM-011).

**ONDA 4 — OFICIAL**: Constituição operando inteira; V4.2 principal; acervo de imagem integrado; anel religado.

## 3. INVARIANTES DE SEGURANÇA (valem pra sempre)

1. **A esteira NUNCA para** (hard news flui em todas as ondas).
2. 1 mudança por vez por vertical.
3. Nada promove sem régua com **prova ao vivo**.
4. Toda mudança tem **rollback documentado + dono**.
5. Gates fail-close + health-check 15min + alarme de fila.
6. **Nada assina/promulga sem o Miguel.**
7. **Telemetria viva antes de qualquer promoção** (o farol).

## 4. CRITÉRIOS DE ABORTO (kill-switch)

- Fila parada **>30min** → rollback imediato da última mudança;
- Erro de título/caption em produção → congela canário, volta pro espelho;
- Custo/token **>10% acima do baseline** por 24h → revisa modo VALOR;
- REJEITO tardio na consulta → pausa a promulgação dos capítulos afetados.

— DSC (Terminal celular do Miguel) · sessão us65 · 20260902 00:3x BRT
