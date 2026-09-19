# MEMÓRIA — Agente YouTube ativado no Ceará Digital (05/08/2026)

**Data:** 2026-08-05 ~20:15 BRT · **Agente:** ZCode/Kimi K3
**Fórum irmão:** `Foruns/forum_youtube_ceara_ativado_20260805.md`

## 1. Configuração

- `agent_data/configs/ceara.json` → seção `youtube` (backup `.bak_pre_youtube_20260805`):
  - `enabled: true` (estava `false` — nota de 21/07 "Miguel configura canais depois").
  - `canais`: As Cunhãs `UCrEqVHi3Sj2WwDz0FrDZKSQ` · Diário do Nordeste `UCMf_wuiFqxdhZI1GVx02mmw` · O POVO `UCj-RTZE-V3Q6jleatRR9k2A` · TV Otimista `UCWzt_BKiMfVoRLuXip7G84g` (IDs extraídos dos 4 vídeos-exemplo do Miguel: `QwXPT1uaj28` TV Otimista sabatina Ciro · `_NeMI-K03aE` As Cunhãs · `NCz0ld9xiFA` Diário/Ponto Poder · `P-HYLx1veoQ` O POVO/Jogo Político).
  - `queries` (7): política ceará, elmano, eleições ce 2026, ciro gomes, as cunhãs podcast, ponto poder diário do nordeste, jogo político o povo.
  - `entrevistados_preferidos` (8): Ciro, Elmano, Camilo, Luizianne, André Fernandes, Capitão Wagner, Evandro Leitão, Eduardo Girão.
  - `min_duracao_minutos: 15` ("vídeos longos, completos e lives" — ordem Miguel); `max_por_rodada: 1`; `max_idade_horas: 168` (podcasts semanais; o GSN usa 3h porque geopolítica é diária).

## 2. Estreia validada

- `ceara_youtube.py` standalone: RSS dos 4 canais (feedparser `feeds/videos.xml`) → escolheu o episódio As Cunhãs `_NeMI-K03aE` (prioridade por entrevistado/tema? — o vídeo era o mais fresco dentro de 168h).
- Transcrição (YouTubeTranscriber): 755 chars/45 segmentos, 9,6 chars/min < 100 → rejeitada como ruído pela própria ferramenta (custo $0,47 registrado pela API mesmo assim); agente seguiu com descrição (fallback by design).
- Thumbnail `youtube-_NeMI-K03aE.jpg` → hero (regra do contrato: thumbnails YouTube permitidas em posts de vídeo).
- `ceara_publicador.py` ×3 rodadas: desafogou a fila (Decon/água SAAE, Luizianne Senado) e publicou o vídeo: **`20260805-pre-campanha-no-ceara-indefinicoes-conchavos-e-machismo-marc`** — 200 ✅ com embed `youtube.com/embed/_NeMI-K03aE`.
- Cron `0 */8` (`orquestrador --site ceara`) inclui a etapa YouTube no ciclo — dedup em `agent_data/v4/ceara/youtube_vistos.json`.

## 3. Observações operacionais

- Episódios musicais/podcast com blocos podem sempre falhar na transcrição — o artigo sai com base na descrição do vídeo; se a qualidade editorial ficar fraca, opções: aumentar `min_duracao`, trocar o provedor de transcrição, ou veto de post sem transcrição (decisão do Miguel se virar padrão).
- `max_idade_horas: 168` revisita vídeos de até 1 semana; com 1 post/rodada ×3 rodadas/dia, a fila não inunda.
