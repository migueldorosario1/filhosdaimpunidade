# Fórum — Fix alerta temáticos Telegram: Ceará Digital com domínio errado no painel CCTV V6 (15/08/2026)

**Data:** 2026-08-15 ~12:45–13:05 BRT · **Agente:** ZCode (Kimi K3) · **Gatilho:** Miguel via chat ZCode ("chegou mensagem no telegram cafezinhoantigravitybot sobre problemas em alguns sites temáticos — conserta e manda outra mensagem para lá")

## Decisão / Resumo

O alerta de "problemas em alguns sites temáticos" recebido pelo Miguel no Telegram era **falso positivo de configuração**: o painel CCTV V6 (Tencent, `painel_cctv_v6.py`, dict `TEMATICOS`) monitorava o Ceará Digital pelo domínio **antigo/errado** `https://www.cearadigital.news` (morto — HTTP 000 de qualquer origem) em vez do domínio **canônico** `https://ceara.digital` (vivo, 200 OK), que já estava registrado no `CEREBRO_INDEX_SATELITES.md` desde 05/08 ("o cearadigital.news previsto em 22/07 NÃO é o domínio real").

**Fix aplicado:** URL do slug `ceara-digital` trocada para `https://ceara.digital` no painel V6, serviço `cctv-v6.service` reiniciado, painel validado mostrando **7/7 online**.

**Verificação independente dos 8 temáticos (registry do Sentinela):** todos HTTP 200 e com conteúdo datado de 15/08 — nenhum site estava realmente fora do ar.

## Estado da missão

- **O que aconteceu:** alerta Telegram → diagnóstico → falso positivo por domínio errado no painel → fix + restart + validação 7/7 → resumo enviado ao Telegram do Miguel (via fallback IP 149.154.166.110 + SNI, pois o DNS local não resolvia api.telegram.org; envio confirmado HTTP 200 ok:true).
- **O que falta:** nada bloqueante. Pendência menor: o `--send` da ponte cafezinho falha silenciosamente (exit 0) quando o DNS está morto — vale endurecer o script para logar/avisar (registrado como lição).
- **Preciso de você (Miguel):** nada. Se quiser, conferir o painel público `http://43.156.151.165/v6/tematicos` (deve mostrar 7/7 online).

## Lições

1. **Falso positivo recorrente por config desencontrada:** o Cérebro já sabia desde 05/08 que `cearadigital.news` não é real, mas o painel V6 (escrito antes) ficou com o domínio velho. Mudança de domínio canônico precisa de checklist de propagação (painel, sentinela, registry, relatórios).
2. **Ponte `--send` silenciosa em falha DNS:** retorna exit 0 sem logar `tg_send_erro` no jsonl — o fallback documentado (IP fixo + SNI) salvou o envio.
3. **DNS local soluça à noite/madrugada** (janela 11:35–12:29 cheia de `Name or service not known` no log da ponte) — pode ter gerado falsas falhas transitórias em outros checks do relatório 30min.

## Referências

- Memória técnica: `Memorias/memoria_fix_alerta_tematicos_ceara_dominio_cctv_v6_20260815.md`
- Canônico do domínio: `CEREBRO_INDEX_SATELITES.md` (seção Ceará, linha "Domínio no ar: https://ceara.digital")
- Relacionado: `memoria_vigilia_tematicos_3_sinais_falso_alarme_20260807.md` (outro falso alarme nos temáticos)
