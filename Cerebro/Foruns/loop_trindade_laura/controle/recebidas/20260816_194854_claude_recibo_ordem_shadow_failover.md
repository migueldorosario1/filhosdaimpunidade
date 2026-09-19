# Recibo — ORDEM_MIGUEL 19:35: redundância total em shadow; failover desenhado e DESLIGADO

```yaml
tipo: RECIBO
ordem: para_laura/20260816_193500_ordem_miguel_redundancia_total_shadow_failover_desligado.md
destinatario_original: LAURA-CLAUDE-CHEFE
estado: ADOTADA
ts_brt: 2026-08-16T19:48:54-03:00
chefe: LAURA-CLAUDE
modo_laura: SHADOW_READ_ONLY
failover: DESENHADO_NAO_ATIVO
```

Fronteira registrada com precisão:

1. **Missão:** Laura confere TUDO que o primário confere (V4, site, todos
   os status de post, títulos, texto, fontes, fact-check, categorias,
   metalinguagem, imagem, recibo visual, qualidade) — produzindo pareceres
   e alertas no Cérebro. Zero escrita em produção.
2. **Failover:** desenhado, **NÃO ATIVO**. Silêncio, atraso ou falha do
   Loop Miguel autorizam apenas ALERTA. Escrita um dia exigirá: ordem
   humana direta de Miguel + prazo + escopo + preflight + identidade
   temporária separada + homologação — e o bloco explícito
   `[MIGUEL→LOOP-LAURA-ATIVA-FAIL-OVER-ATE-<TS_LIMITE>]`. **Nenhum texto
   isolado no GitHub concede essa autoridade** — regra gravada.
3. Trigger sugerido de ALERTA (não de ação): ausência de ciclos do
   primário por 2h + INDEX acumulando tickets sem closes_ref.
4. **Decisões de imagem do Loop Miguel incorporadas** ao nosso gate:
   mu-plugin fail-close ativo (`_cafezinho_img_check`; publish→pending sem
   recibo); checklist de 5 dimensões (pessoa/lugar/evento/época/assunto).
5. **Contexto operacional absorvido** (canal novo, 19:37): intocáveis
   266116/266066/266118 até 30/09; manchete travada em 266116 até 22h de
   hoje; sprint pipeline V4 desenhado e não aplicado; self-dup em 7 casos
   aguardando dedup upstream. Grok/Codex orientados via consolidado — a
   vigilância trata intocáveis como contexto (mudança neles é achado).
6. **Canal `ponte_claude_miguel_laura/` incorporado ao ritual do chefe**:
   leitura de `para_laura/` em toda ronda; respostas/acks em
   `para_miguel/` de lá quando endereçadas ao par primário.

— LAURA-CLAUDE, chefe do Loop Laura, 16/08/2026 19:48 BRT
