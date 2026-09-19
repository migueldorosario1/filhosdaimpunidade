# Fórum — Banco de Links de Mídia Jornalística (ordem Miguel 13/08 ~15:10)

**Agente:** ZCode (Kimi K3→GLM-5.2) · **Status:** 🔄 FASE 1 (coleta de links) em execução

## A ordem do Miguel (quase literal)

"Você está pegando aonde? Não é legal ficar pegando só retrato oficial. Faz um banco de links jornalísticos e vai juntando. Um sprint longo com as principais lideranças globais, sobretudo as mais importantes pro Cafezinho. Quando tiver dificuldade de encontrar o personagem, não procura só uma vez — procura vários, pra não repetir e usar em outras oportunidades. Primeiro o banco de links (mais rápido), depois baixamos as imagens, filtramos se são boas mesmo, e jogamos tudo pro banco de mídia V4 que a gente já tem."

## O que é (e o que NÃO é)

- **É:** um banco de **LINKS** de fotos **jornalísticas** licenciadas (1 linha por imagem-candidata), com várias opções por liderança (anti-repetição), prioridade **evento > retrato oficial**.
- **Não é (ainda):** o banco de mídia V4 (que guarda arquivos). Fase 2 futura: baixar tudo, **filtrar com olho humano/máquina** e injetar no banco V4 (`/root/agent_data/acervo_midia/` e/ou `banco_midia_ouro_v3` Tencent).

## Implementação (Fase 1)

- **Coletor:** `ZCodeProject/coletor_banco_links.py` — determinístico (sem LLM por foto): Wikimedia Commons API (≥1200px) + Flickr CC/PD (licenses 4,5,8,9,10), filtro de licença **sem NC/ND** (site tem anúncios), dedupe por URL, prioriza contexto de evento, **até 6 opções por líder**.
- **Lideranças (~75):** governo Lula (Haddad/Tebet/Dino/Padilha…), Congresso (Alcolumbre/Lira/Mota…), STF (Moraes/Barroso/Toffoli…), oposição e candidatos 2026 (Bolsonaro/Tarcísio/Ciro/Boulos/Marçal…), governadores, potências (Putin/Xi/Trump/Rubio/Macron/Modi/Kim/Erdoğan…), Oriente Médio (Netanyahu/Khamenei/Pezeshkian/Zelensky/Lavrov…), Américas (Maduro/Milei/Sheinbaum/Petro…) + encontros diplomáticos do Lula.
- **Saída:** `ZCodeProject/banco_links_midia.jsonl` + espelho no NYC `/root/agent_data/banco_links_midia/banco_links_midia.jsonl` (a ponte */30 passa a consultar ANTES de caçar na web).
- **Schema:** entidade · categoria · descricao · fonte · fonte_pagina · url_direta · licenca · autor · largura_px · contexto (evento/retrato) · coletado_em · usos (contador anti-repetição).

## Regras editoriais

- Licença verificada na fonte; sem agência paga, sem hotlink de notícia, sem IA.
- SEM NC (site tem anúncios) e SEM ND (legendamos).
- Várias opções por líder; contador `usos` para rotatividade.

## Estado / o que falta

- [x] Coletor escrito + executado (ver log do sprint)
- [ ] Consolidar JSONL + estatísticas por líder
- [ ] Espelhar no NYC + ponte */30 atualizada para consultar o banco primeiro
- [ ] Fase 2 (futura, ordem Miguel): baixar tudo → filtrar qualidade → injetar no banco de mídia V4

## ✅ FASE 1 CONCLUÍDA (13/08 ~15:35 BRT)

- **399 links · 73 lideranças** → `ZCodeProject/banco_links_midia.jsonl` (espelho NYC `/root/agent_data/banco_links_midia/` + coletor versionado lá).
- **396/399 contexto=evento** (foto jornalística; só 3 retratos) — ordem do Miguel atendida.
- Fontes: Commons 316 + Flickr 83. Licenças: CC BY 2.0/4.0, CC BY-SA, PD, CC0 (zero NC/ND — site tem anúncios e legendamos).
- Categorias: governo 85 · potências 72 · STF 36 · oposição 36 · candidatos 33 · américas 33 · congresso 32 · governadores 23 · oriente médio 49(+) · diplomacia Lula 6(+).
- Magros (≤2 opções, repor depois): Hugo Mota, Cláudio Castro, Pezeshkian, Salami.
- **Ponte */30 atualizada (CronUpdate):** novo PASSO 0 consulta o banco primeiro (menor `usos` primeiro, evento>retrato, incrementa usos); PASSO 3 passou a ALIMENTAR o banco com achados novos da web (cresce sozinho a cada rodada).
- **Próxima (Fase 2, ordem Miguel):** baixar tudo → filtrar qualidade (olho humano/juiz visual) → injetar no banco de mídia V4 (`acervo_midia`/`banco_midia_ouro_v3`). Não iniciada — aguarda "vai".

### Uso real (rodada 7 da ponte, 13/08 ~17:10)
- **1º e 2º usos do banco:** 265603 (nacional/Lula → almoço oficial Planalto jul/2024, Lula Oficial CC BY-SA 2.0) e 265604 (geo/Rússia → Putin fev/2024, Kremlin.ru CC BY 4.0). Contadores `usos` incrementados.
- **Lição 1 (backlog do coletor):** banco sem filtro de data escolheu foto de 2000 (posse do Putin) p/ notícia de hoje — troquei manualmente pela de 2024. Próxima versão do coletor: extrair `extmetadata.DateTimeOriginal` e preferir ≤3 anos (schema ganha `data_foto`).
- **Lição 2:** título de candidata em espanhol ≠ idioma do post (redator escreveu em PT) — confundiu na leitura da fila; sempre conferir o título no WP.
