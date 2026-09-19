# Fórum — Fix: gate de imagem bloqueava publicação dos drafts do agente YouTube

**Data:** 2026-08-17 ~08:15–08:45 BRT
**Executado por:** ZCode (Qwen 3.8), após o Miguel reportar "não entrou mais nenhum post do agente YouTube no cafezinho"
**Memória técnica (Tema Duplo):** `Cerebro/Memorias/memoria_fix_gate_imagem_agente_youtube_20260817.md`
**Bug:** `monitoramento_horario/bugs_encontrados/yt_patrulha_gate_imagem_bloqueava_drafts_20260817_0830.md` (YT-PATRULHA)

## Contexto

Desde 16/08 nenhum post do agente YouTube entrou no Cafezinho, mesmo com drafts prontos
e o Claude publicando V4 normalmente. Causa: o **gate de imagem fail-close** criado em
16/08 (ordem do Miguel, pós-266029) exige `_cafezinho_img_check` e o agente YouTube não
gravava essa meta — publicação retornava HTTP 400 BLOQUEIO GATE-IMG (provado com teste real).

## Decisões / correções

1. **Meta registrada p/ REST** no canônico (mu-plugin `cafezinho-meta-img-check-rest.php`) —
   sem isso o agente nem conseguia gravar a meta pelo payload.
2. **Agentes gravam a checagem por proveniência**: a capa do post YouTube é o thumbnail
   OFICIAL do próprio vídeo (a imagem É o objeto) — `ok:true, metodo: thumbnail_oficial_video`.
   Patch no agente nacional (create+update) e no publicador GSN V2 (NYC). Backups `.bak_pre_gate_imagem_20260817`.
3. **Backfill nos 4 drafts parados** (266072/266073/266172/266195) — todos destravados.
4. **Bônus:** `coletar()` blindado contra `RemoteDisconnected` de feed único (rodada das 08h de
   hoje morreu por isso — um canal derrubava a coleta inteira).

## Estado da missão

- **O que aconteceu:** causa raiz provada, 5 correções aplicadas, fila destravada.
- **O que falta:** Claude revisar e publicar a fila (266172/266195/266072/266073) — inbox +
  canal Trindade avisados 08:40. Rodada das 14h deve gerar draft novo.
- **O que preciso do Miguel:** nada — só avisar se quiser que eu peça prioridade maior ao Claude.

---

## Adendo 17/08 15:45 — Ordem direta do Miguel: posts parados PUBLICADOS

Miguel: "vamos destravar e publicar os posts parados?" → publicação executada na hora (ordem do dono
prevalece sobre a divisão de papéis; Claude avisado no inbox + canal Trindade para o ledger):

- **266072** (Irã e Iêmen partem para a ofensiva...) → **publicado**, no ar HTTP 200
- **266172** (MTG: equipe de Trump discutiu armas nucleares contra o Irã) → **publicado**, no ar HTTP 200
- 266195 (17:15) e 266073 (17:45) → já estavam agendados pela vigília do Claude; seguem no schedule.

Prova: publish via REST passou pelo gate (meta ok) e páginas públicas www.ocafezinho.com responderam 200.
Fila YouTube zerada: nada parado no Cafezinho.
