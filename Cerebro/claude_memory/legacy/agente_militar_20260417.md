---
name: Agente Militar — Tecnologia bélica Sul Global (criado 2026-04-17)
description: Novo agente especializado em tecnologia militar e indústria de defesa com lente do Sul Global. Coletor a cada 30min, publicador 3x/dia. Herda motor_publicador, Trindade de fact-check, Tribunal Visual Gemini.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Criado em 2026-04-17 a pedido do Miguel. Não existia agente com foco em tecnologia bélica — soberania tocava tangencialmente mas cobria Defesa+BRICS+Infra juntos.

## Arquivos

- **`robo_coleta_militar.py`** — coletor via `motor_coletor.iniciar_coleta_especializada`. Feeds: Bulgarian Military, Naval News, TASS, Sputnik, Global Times, CGTN, Press TV, Tasnim, IRNA, RT, Defesa.net, TeleSUR, Al Jazeera, Army Recognition. Banco: `agent_data/banco_artigos_brutos_militar.json`. Fontes: `agent_data/fontes_militar.json`.
- **`agente_militar.py`** — publicador enxuto que chama `motor_publicador.iniciar_publicacao_especializada` com `exige_imagem_real=True`, `nota_corte_imagem=50`. Herda curadoria Trindade, fact-check Perplexity+Claude, banco de mídia real com Tribunal Visual Gemini + legenda jornalística.

## Linha editorial (em CRITERIOS_SCORE e REGRAS_APROVACAO)

**Aprova:** tecnologia militar concreta (caças, mísseis, submarinos, drones, antiaéreos, hipersônicos, IA em guerra, ciberdefesa), indústria do Sul Global (Embraer, Avibras, Rosoboronexport, NORINCO, HAL, Bayraktar/ASELSAN, KAI, DRDO, DEFA), cooperação BRICS de defesa, exercícios navais multi-país.

**Reprova:** propaganda enfraquecendo Rússia/China/Irã, glorificação de operações OTAN/EUA/Israel como "cirúrgicas", "regime" contra Sul Global, comparações exaltando supremacia ocidental sem contrapor fracassos.

## Crontab (atual: 39 linhas ativas)

```
8,38 * * * * /root/venv/bin/python3 robo_coleta_militar.py >> /root/agent_data/robo_coleta_militar.log
0 9,14,20 * * * /root/venv/bin/python3 agente_militar.py >> /root/agent_data/militar.log
```

Coletor 2x/hora (8,38 — sem conflito com outros coletores: nacional 0,30 / soberania 5,35 / geopolitica 10,40 / imagens 15,45 / trends 20,50). Publicador 3x/dia (9h, 14h, 20h — intercalado com soberania 7/13/19).

## Validação inicial

Rodado manualmente no dia da criação: 63 matérias salvas de primeira, com destaques tipo "Kalashnikov Skat-350M drone" (score 8.5) e "Russia's defense spacecraft placed in target orbit" (6.5).

## Why

Completar a prateleira editorial: o Cafezinho tinha cobertura política, econômica, cultural, esportiva — mas faltava jornalismo **técnico** de defesa. Com as tensões Irã/Gaza/Ucrânia/Ormuz, é nicho quente e sem concorrente progressista em português.

## How to apply

- **Adicionar fontes:** editar `DEFAULT_FEEDS` em `robo_coleta_militar.py` OU diretamente no `agent_data/fontes_militar.json` com `ativo_agora: true`.
- **Ajustar cadência:** editar `crontab_server.txt` (espelho canônico) e reaplicar.
- **Teste draft:** `sudo /root/venv/bin/python3 agente_militar.py --rascunho`.
