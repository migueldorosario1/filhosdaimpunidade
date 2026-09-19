---
name: Agente Latam+Sheinbaum — DEPLOYADO, 2 drafts rodados, cron DESATIVADO aguardando decisão categoria
description: Todos os 12 arquivos no Tencent. Coleta+DRY_RUN funcionaram. 2 drafts pendem inspeção editorial. Bloqueio pro cron: decidir A/B/C sobre categoria "Pátria Grande".
type: project
originSessionId: 5463c220-6a29-496f-875a-64c9d5fac390
---
**Sessão 2026-04-20 (retomar daqui ao religar o computador).**

Conceito vivo em `Projeto Cafezinho Agentes/root/CONCEITO_AGENTE_LATAM.md` (Seção 7 tem nota do Antigravity).

## ✅ Deploy concluído no Tencent

- **Código:** `agente_latam.py`, `agente_sheinbaum.py`, `robo_coleta_latam.py`, `robo_coleta_sheinbaum.py` em `/root/`
- **Dados:** `diretriz_latam.json`, `diretriz_sheinbaum.json` (chave `diretriz_especifica` — padrão do projeto), + 6 bancos JSON vazios em `/root/agent_data/`
- **Whitelist Sentinela:** `/root/Outros/regras_vivas_auditoria.md` atualizado com bullet de 5 itens (imperialismo/lawfare/doutrina Monroe/etc) + entrada histórico 2026-04-20
- **Crontab:** merged localmente (4 linhas Pátria Grande inseridas antes do Sentinela V4) **MAS NÃO APLICADO NO SERVIDOR**. `/root/crontab_server.txt` no Tencent está atualizado (137 linhas), mas `sudo crontab -l` ainda tem a versão antiga sem Latam/Sheinbaum.
- **MD5 local ↔ servidor idêntico** pros 12 arquivos.

## ✅ Pipeline validada

- **Coleta Latam:** 23 matérias (scores 2.0→9.0). 15/15 feeds ativos (Confidencial, TN8, El Faro, Prensa Comunitária, Plaza Pública, Criterio HN, Semanario CR, TeleSUR, RT Español, Nodal, Resumen Latinoamericano, Tiempo Argentino, Alba Ciudad, Últimas Notícias VE, Wayka).
- **Coleta Sheinbaum:** 18 matérias (scores 2.0→8.5). 5/5 feeds ativos (La Jornada Política + Economia, Regeneración MX, Contralínea, Desinformémonos).
- **Heurística CA:** determinística via `agent_data/controle_ciclo_ca.txt` alternando 0↔1. Fallback pro Geral se CA vazio.

## 📝 2 drafts de teste no WP (AGUARDAM INSPEÇÃO EDITORIAL)

- **#237160 Latam** — "Cortes de Milei provocam colapso no sistema ferroviário argentino" (media 237158 de resumenlatinoamericano.org)
- **#237164 Sheinbaum** — "Justiça mexicana derruba centenas de ações contra obras de infraestrutura e reformas constitucionais" (media 237161 de jornada.com.mx)

Ambos passaram **todas as 14 camadas** (idênticas à Trindade): curadoria anti-ads → produção gpt-5 → audit Claude → swarm Grok-4.20 → audit final Claude → fact-check cascata → Tribunal Visual Gemini → upload mídia com caption → figcaption → interlink "Leia também" → Yoast OG/Twitter → sanitizador markdown → enxame comentarista.

## 🛑 Bloqueio do cron: categoria "Pátria Grande"

`motor_publicador.iniciar_publicacao_especializada()` NÃO tem parâmetro `categoria_forcada`. O LLM categorizador escolhe entre categorias WP existentes baseado no conteúdo. Resultado dos drafts:
- Latam → **argentina** (ID 5012) — queria "Pátria Grande"
- Sheinbaum → **internacional** (ID 15) — queria "Pátria Grande"

### 3 opções propostas aguardando decisão Miguel:

- **(A)** Criar categoria "Pátria Grande" no WP via API REST + atualizar `taxonomia_wordpress.json` + hint nas diretrizes JSON dizendo "esta matéria DEVE ser categorizada como Pátria Grande". Risco: LLM pode ignorar o hint e preferir categoria mais específica (argentina).
- **(B)** Adicionar parâmetro `categoria_forcada` em `motor_publicador.iniciar_publicacao_especializada()` — mexe em coração de código de produção (~5 linhas). Garante categoria fixa sempre. Miguel resistiu à Opção C análoga antes ("abrir caixa de Pandora").
- **(C)** Abandonar categoria única: LLM escolhe por país (argentina/venezuela/internacional). Tags identificam país. Perde a unidade visual que Miguel queria.

Recomendação Claude: (A) + (B) — criar a categoria pra ter onde cair e adicionar o parâmetro pra garantir determinismo. Mas aguardar aval.

## 🎯 Próximos passos ao retomar

1. Miguel inspeciona drafts 237160 + 237164 no painel WP (https://controle.ocafezinho.com/wp-admin/)
2. Decide A/B/C sobre categoria "Pátria Grande"
3. Opcional: rodar mais DRY_RUNs (`sudo python3 agente_latam.py --rascunho` e idem sheinbaum) pra gerar mais amostras. Cada teste leva ~3min e cria 1 draft.
4. Aplicar as 4 linhas do crontab quando Miguel autorizar:
   ```bash
   ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
     "cat /root/crontab_server.txt | sudo crontab -"
   ```
5. Cleanup dos drafts de teste (237160, 237164) e mídias (237158, 237161) após validação.

## ⚠️ Lições desta sessão

- **Antigravity entregou 10 arquivos com 5/5 feeds Sheinbaum QUEBRADOS + 4/12 Latam quebrados.** Claude validou tudo com feedparser+UA custom e substituiu.
- **SEMPRE `feedparser.parse(url, agent=UA)` antes de commitar lista de feeds** — é regra de ouro pra qualquer agente novo.
- **Antigravity sugeriu `DRY_RUN=1` env var — NÃO EXISTE no motor_publicador.** O único modo teste é `--rascunho` que publica draft real no WP.
- **Hook do harness bloqueou --rascunho inicialmente.** Correto (é side-effect real). Miguel autorizou explicitamente depois.
- **Diretrizes JSON:** chave padrão do projeto é `"diretriz_especifica"` (motor lê arquivo como string crua, linha 834). Antigravity usou `"diretriz"` + `"nome_modulo"` que poluiria prompt.

## Comando de retomada rápida

```bash
# Ver drafts no WP
curl -u "Redator:$WP_PASS_CAFEZINHO" "https://controle.ocafezinho.com/wp-json/wp/v2/posts/237160" | jq '.title, .status, .categories'
curl -u "Redator:$WP_PASS_CAFEZINHO" "https://controle.ocafezinho.com/wp-json/wp/v2/posts/237164" | jq '.title, .status, .categories'

# Rodar DRY_RUN de novo
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  "sudo bash -c 'source /root/chaves.sh; /usr/bin/python3 /root/agente_latam.py --rascunho'"
```
