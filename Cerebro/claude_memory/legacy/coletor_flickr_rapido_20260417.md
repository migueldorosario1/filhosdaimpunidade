---
name: Coletor Flickr institucional rápido (2026-04-17)
description: Novo coletor dedicado que roda a cada 10 min só puxando Flickr (Lula/Planalto/Senado/Itamaraty/STF etc) — garante banco sempre fresco pra pautas de política BR, sem pagar o custo do Wikimedia.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 Miguel pediu que o banco de mídia tivesse fotos RECENTES do Lula e política nacional disponíveis na hora da publicação — não esperando o ciclo de 30min do `robo_coleta_imagens.py`.

## Solução (Opção B — coletor dedicado, não busca on-demand)

Criado `/root/robo_coleta_flickr_rapido.py` que reusa a função `coletar_flickr_institucional()` do `robo_coleta_imagens.py` mas PULA o scan Wikimedia (que é lento, ~358 queries por rodada). Roda a cada 10 min via cron.

**Crontab:** `*/10 * * * * cd /root && /root/venv/bin/python3 robo_coleta_flickr_rapido.py >> /root/agent_data/robo_coleta_flickr_rapido.log 2>&1`

Total de perfis varridos (reusa a constante `FLICKR_PERFIS_NSID` do robo_coleta_imagens): @lula, @planalto, @senado, @mre, @pt, @stf, @casa_branca, @elysee_macron, @flavio_bolsonaro, @embaixada_china (10 contas). Cada rodada traz até 20 fotos por perfil = até 200 fotos/ciclo.

**Performance:** ~6s por execução. Primeira rodada manual pós-deploy: +200 fotos, banco 19772→19972.

## Pegadinha: FLICKR_API_KEY no .env.unificado

`carregar_chaves.py` carrega apenas `/root/chaves_novas.env`, `/root/.env`, e variantes locais — **NÃO lê `.env.unificado`**. Mas a `FLICKR_API_KEY` vive só no `.env.unificado`. Por isso o script tem bloco extra:

```python
import carregar_chaves  # noqa: F401
try:
    from dotenv import load_dotenv
    for _env in ("/root/.env.unificado", ...):
        if os.path.exists(_env):
            load_dotenv(_env, override=False)
except ImportError:
    pass
```

**Lição:** qualquer script novo que precise de chave que esteja no `.env.unificado` (ex: FLICKR, FB_PAGE_ACCESS_TOKEN pra alguns agentes) precisa deste load_dotenv complementar. Ou: evoluir `carregar_chaves.py` pra incluir `.env.unificado` no rol de candidatos.

## Como isso integra com o bônus de recência

Pipeline pra pauta de política BR:
1. `*/10` flickr_rapido enche o banco com fotos do dia
2. Matéria do Maestro chega ao `motor_publicador`
3. Prioridade 1 tenta imagem da fonte (`og:image` de ocafezinho.com/outras) — Tribunal Visual julga
4. Prioridade 2: `buscar_imagem_banco_local` — agora com bônus forte pra fotos <= 30 dias (+60 de score)
5. Fotos frescas do Lula/Planalto postadas há 5-30 min **sobem pro topo** e passam pro Tribunal primeiro
6. Tribunal valida recência e aprova

## Backup e como reverter

Se o robô começar a sobrecarregar Flickr API (rate limit), trocar cadência no crontab: `*/10` → `*/15` ou `*/20`. Ou desativar a linha específica do cron — o `robo_coleta_imagens` (15,45) continua garantindo cobertura Wikimedia + Flickr a cada 30 min como antes.

## How to apply

- **Adicionar perfil novo:** editar `FLICKR_PERFIS_NSID` em `robo_coleta_imagens.py` — o coletor rápido herda automaticamente.
- **Aumentar fotos por perfil:** no `robo_coleta_imagens.py` em `coletar_flickr_institucional`, `per_page=20` → aumentar. Cuidado com rate limit Flickr.
- **Monitorar:** `tail -f /root/agent_data/robo_coleta_flickr_rapido.log` — log deve mostrar "+X novas fotografias" a cada 10min.
