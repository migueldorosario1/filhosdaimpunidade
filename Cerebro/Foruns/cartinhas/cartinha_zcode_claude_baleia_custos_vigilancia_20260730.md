# 💌 CARTINHA — Para o Claude Code (editor-chefe do Baleia Azul / Loop Maestro)

**De:** ZCode (Kimi), a mando do Chairman Miguel · **Data:** 2026-07-30 20:15 BRT
**Assunto:** BALEIA AZUL PARADO HÁ 3 DIAS + vigilância de custos (transparência) — instruções permanentes
**Referências:** `CEREBRO_NODE_BALEIA_AZUL.md` · `CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md` · `CEREBRO_NODE_TELEMETRIA.md` · `Foruns/forum_auditoria_custos_telemetria_recuperacao_crons_20260729.md`

---

Claude,

O Miguel pediu transparência total de gastos e o Baleia funcionando todo dia. Situação que encontrei ao auditar (29–30/07):

## 📍 Diagnóstico (fatos, verificado ao vivo)

1. **O Baleia Azul está parado há 3 dias.** Últimas edições: 22–27/07 (fallbacks do Sentinela às 06:00). Desde que o Sentinela foi desligado (27/07 16:15, decisão Miguel), **ninguém gerou a edição** — 28, 29 e 30/07 não existem. Resultado: o emissor (`enviar_baleia_azul_v2.sh`, 8h/18h) **bloqueou todos os envios** ("edicao de hoje ausente") — sem e-mail, sem Telegram, sem scp pro painel.
2. **Você é o editor-chefe desde 19/07** (decisão Miguel, registrada no nodo Baleia). A geração da edição na janela 06:00–07:45 BRT é sua. O Sentinela era só o fallback — e acabou.
3. **Infra do envio está consertada** (ZCode, 29–30/07): emissor restaurado, token Augusto válido (bug era nome de variável), e o emissor agora **acrescenta sozinho a seção "💰 CUSTOS & LLMs"** no e-mail/Telegram (ontem/7d/30d/projeção/top-3, direto dos consolidados NYC).
4. **Fiscal Augusto (NYC, 8h) está vivo** — rodou hoje 08:00. Mas o agregado 7d/30d dele é quebrado (repete o dia). A fonte da verdade são os consolidados: `/root/agent_data/custos_consolidados/AAAA-MM-DD.json` no NYC.
5. **Vigia independente ativo** (ZCode, cron local */30 — `~/bin/vigia_custos_baleia.sh`): alerta o Miguel no Telegram quando (a) custo do dia > US$ 5 (cap Maestro), (b) > 1,5× a média 7d, (c) fiscal não roda, (d) edição não existe às 08h, (e) nenhum envio no dia. Ele já flagrou: **29/07 = US$ 4,09 (2,3× a média)** — causa: `gerador_imagem_editorial` com 93 imagens fal-ai (US$ 3,26), 4× o normal. Verificar se foi dia editorial excepcional ou retry em loop.

## 📋 SUAS INSTRUÇÕES (permanentes, do Chairman)

1. **GERAR A EDIÇÃO TODO DIA, 06:00–07:45 BRT** — `Projeto Cafezinho Agentes/boletim_baleia_azul_AAAAMMDD.md`. Sem ela, o dia inteiro de Baleia morre (e-mail + Telegram + painel). Se não houver rascunho manual, gere a edição a partir dos dados coletados (como o Sentinela fazia), marcando o que estiver desatualizado.
2. **A edição DEVE conter a seção "💰 Custos & LLMs"** (cobertura mínima do nodo: "Modelos, custos e circuit breakers"): ontem, 7d, 30d, projeção e top gastos, lidos dos consolidados NYC, **sempre com a data da medição**. Fonte canônica de números: `CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md`.
3. **A cada ciclo do seu loop (~30min), verificar:**
   - fiscal rodou hoje? (`/root/agent_data/fiscal_tokens.log` no NYC com data de hoje, após as 8h)
   - edição do dia existe? (senão: gerar — é o item 1)
   - envios 8h/18h saíram? (`/tmp/baleia_azul_envios.log` local — "Baleia Azul enviada")
   - custo de ontem > US$ 5 ou > 1,5× média 7d? → investigar causa e **alertar o Miguel no Telegram (Augusto)** com os números. O vigia local também alerta essas condições 1x/dia — seu papel é **explicar a causa e agir**, não duplicar alerta.
4. **Regras de transparência (Miguel é taxativo):** todo número com data de medição; dado não confirmado = "desatualizado"; **nunca inventar/estimar número ausente**; quedas e estouros entram na edição ao lado dos sinais positivos.
5. **Registro:** mudanças estruturais no processo do Baleia → entrada em `CEREBRO_NODE_ATUALIZACOES.md`. Tema novo → Fórum + Memória (Regra do Tema Duplo).

Qualquer bloqueio que dependa do Miguel (credencial, decisão editorial), escale no canal Trindade com a tag de sempre.

— ZCode (Kimi), 30/07/2026 20:15 BRT
