# FÓRUM — Agente YouTube ativado no Ceará Digital (05/08/2026)

**Data:** 2026-08-05 ~20:15 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel (chat, respondendo ao lembrete das 08:47): "os canais são as Cunhãs (vídeos longos, completos, e as lives, que são raras), o Ponto Poder do Diário do Nordeste (lives), Jogo Político do Jornal O Povo, e alguns outros" + 4 vídeos-exemplo.

## 1. Canais configurados (identificados a partir dos exemplos do Miguel)

| Canal | ID | Ref |
|---|---|---|
| **As Cunhãs** | `UCrEqVHi3Sj2WwDz0FrDZKSQ` | podcast (vídeos longos + lives raras) |
| **Diário do Nordeste** | `UCMf_wuiFqxdhZI1GVx02mmw` | casa do Ponto Poder (lives) |
| **O POVO** | `UCj-RTZE-V3Q6jleatRR9k2A` | casa do Jogo Político |
| **TV Otimista** | `UCWzt_BKiMfVoRLuXip7G84g` | sabatinas "O Otimista Eleições" (ex.: Ciro) |

Config `ceara.json` → `youtube.enabled: true` (estava `false` com nota "Miguel configura canais depois" desde 21/07). Backup `.bak_pre_youtube_20260805`. Regras: `min_duracao_minutos: 15` (só longos/completos), `max_por_rodada: 1`, `max_idade_horas: 168` (semanal — podcasts não são diários como o GSN que usa 3h), 8 entrevistados preferidos (Ciro, Elmano, Camilo, Luizianne, André Fernandes, Capitão Wagner, Evandro Leitão, Eduardo Girão), 7 queries (incl. "as cunhãs podcast", "ponto poder diário do nordeste", "jogo político o povo").

## 2. Estreia (primeira rodada, ~20:10 BRT)

- O agente escolheu logo **o episódio do As Cunhãs que o Miguel mandou de exemplo** (`_NeMI-K03aE` — "Indefinições, conchavos e machismo…").
- Transcrição veio com qualidade ruim (9,6 chars/min — episódio com muita música/blocos) → o agente seguiu com descrição (fallback projetado, não crítico).
- **Post no ar ✅:** `ceara.digital/blog/20260805-pre-campanha-no-ceara-indefinicoes-conchavos-e-machismo-marc/` — com **embed do YouTube + thumbnail oficial** como hero (regra do contrato: thumbnails YouTube permitidas para posts de vídeo).
- Na mesma leva o pipeline publicou mais 2 matérias locais (Luizianne ao Senado × Ciro — política cearense pura, o foco novo funcionando).

## 3. Operação

- O agente roda dentro do ciclo V4 do ceara (cron `0 */8`) — novos episódios dos 4 canais entram sozinhos, 1 por rodada, sem repostar (dedup `youtube_vistos.json`).
- Se a transcrição vier ruim de novo em episódios musicais, dá para subir `min_duracao` ou trocar o serviço de transcrição — observar próximas semanas.

## 4. REFINAMENTO (mesmo dia ~20:40 BRT) — prioridade = sabatinas dos candidatos; frescura 4h

**Ordem do Miguel:** "dá prioridade a Sabatinas dos candidatos (Ciro, Elmano, Cid Gomes, Luizianne Lins, Capitão Wagner, André Fernandes, Priscila Costa); quando não tiver nada novo desses nomes, bota debate do Ponto Poder/As Cunhãs (Cunhãs pode sempre); tem que ser nas últimas 4 horas, sempre bem fresquinho."

1. `entrevistados_preferidos` := os 7 nomes (candidatos). Queries trocadas para sabatina/entrevista/debate × nome + os 3 programas.
2. `max_idade_horas: 168 → 4` (regra da frescura).
3. `youtube.py`: score de prioridade virou **nome×2 + formato×1** (`prioridade_formatos` opt-in no config — demais sites inalterados).
4. **Cron dedicado `*/2 * * * *` `ceara_youtube.py`** (flock) — a janela de 4h exige checar mais que o ciclo de 8h; a regra de 1 vídeo/dia embutida evita inundação (testada: "já publicou vídeo hoje — pulando" ✅).
- Dúvida de transcrição pendente com o Miguel: "Chagas Freitas" (?) — fora da lista até ele confirmar o nome certo.

**Memória técnica:** `Memorias/memoria_youtube_ceara_ativado_20260805.md`
