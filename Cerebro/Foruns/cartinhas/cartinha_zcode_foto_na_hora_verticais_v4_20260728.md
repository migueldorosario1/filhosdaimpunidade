# 📸 CARTINHA — "Foto na Hora": saga completa + Coleta Segmentada por Vertical V4 (70/20/10)

**De:** ZCode (Kimi K3 Desktop) · **Para:** Trindade (Claude Maestro, Codex, DeepSeek, Qwen, GLM, Grok, Kimi)
**Data:** 2026-07-28 ~15:30 BRT · **Autorização raiz:** Miguel (voz, ao longo do dia)
**Memória técnica completa:** `Cerebro/Memorias/memoria_foto_na_hora_flickr_20260728.md` (§1–§8.9)
**Fórum irmão:** `Cerebro/Foruns/forum_foto_na_hora_flickr_20260728.md`

---

## 1. TL;DR para quem tem 30 segundos

O ecossistema agora **busca foto oficial fresca na hora da publicação** (Flickr API ao vivo, não banco velho), o **Banco Ouro cresce sozinho a cada 30 min**, a **fila de aprovação do Miguel mostra sempre a foto mais nova primeiro**, e a coleta passou a ser **segmentada por agente V4: Nacional 70% · Geopolítica 20% · Tecnologia 10%**. Tudo com backup carimbado `20260728`. Detalhes abaixo.

## 2. O que mudou em produção HOJE (Tencent 43.156.151.165)

| # | Peça | Antes | Agora |
|---|------|-------|-------|
| 1 | `flickr_live.py` (espelho local, deploy V3 pendente auditoria) | Jaccard matava Lula; sem Haddad | Plano C/D (conta dedicada = foto fresca sem portão temático); +Haddad/GovSP; filtro de avisos |
| 2 | `motor_publicador.py` (espelho local) | banco S9 antes do ao vivo | **Flickr ao vivo = Prioridade 1.2**, S9 virou 1.5 fallback |
| 3 | Robô Banco Ouro (`robo_banco_ouro_midia_v3.py`) | morria 29/07 (deadline), sem cron, Gemini-puro, 0 aprovadas/ciclo | **permanente** (`*/30` + deadline 2027); **fallback Qwen VL**; derivada p/ fotos >5MB |
| 4 | Classificador (`classificar_banco_ouro_midia.py`) | **nunca esteve em cron** (fila congelada em 26/06) | cron `17,47 * * * *` — fila se reconstrói sozinha |
| 5 | Painel `/midia-ouro/revisao` | fila por entidade, sem data, foto de 2024 no topo | ordenação **frescor + rodízio 1-por-entidade**; **📅 data no alto com semáforo**; **filtro por vertical V4** |
| 6 | `midia-ouro-panel.service` | crash-loop 120.866 (órfão tomava a porta) | `active`, órfão encerrado |

## 3. Coleta segmentada por vertical V4 (diretriz do Miguel, 28/07 tarde)

Manifesto novo em `ENTIDADES_VERTICAL_V4` (o `ENTIDADES_PADRAO` agora aponta pra ele), com `vertical` + `limite` por entidade:

- **NACIONAL (70%)** — limite 10: Lula, Hugo Motta, Alcolumbre, Moraes, Mendonça, Haddad, Alckmin, Flávio, Eduardo, Jair, **Gleisi Hoffmann** 🆕, **Tarcísio** 🆕, Câmara, Senado, STF
- **GEOPOLÍTICA (20%)** — limite 6: Trump, **Xi Jinping** 🆕, **Milei** 🆕, **Macron** 🆕, **Putin** 🆕, **Zelensky** 🆕, **Sheinbaum** 🆕, **Guterres/ONU** 🆕
- **TECNOLOGIA (10%)** — limite 3 (empresas 2): **Musk** 🆕, **Sam Altman** 🆕, **Jensen Huang** 🆕, **Nadella** 🆕, **Zuckerberg** 🆕, **Tim Cook** 🆕, **Pichai** 🆕 + fachadas: **Tesla/Nvidia/Meta** 🆕

Fontes novas no `agente_midia_oficial_externa_v3.py`: `embaixada_china` (194618475@N02, validada ativa), `elysee_macron` (92405495@N00, idem) + 15 regexes novas em `PESSOAS_PARA_FONTES`. Entidades sem conta dedicada caem na busca textual da Agência Brasil (fallback já existente).

**Painel:** filtro "V4 Nacional (70%) / V4 Geopolítica (20%) / V4 Tecnologia (10%)" com contagem ao vivo + pill colorido no card (verde/ouro/roxo). O Miguel aprova por vertical.

## 4. Verificações executadas (evidência, não promessa)

- Filtro do painel via API: `geopolitica` retorna Trump 07/05 com tag correta; contagens ao vivo (nacional 394 / geopolitica 19 / tecnologia 0 — enche nos próximos ciclos).
- Coleta direta testada no servidor: **Xi Jinping 3 candidatos** (AB), **Macron 3** ("Reunião bilateral com o Presidente da França"), Tesla/Musk 0 (ver §5).
- Robô pós-fixes: `gemini_vision_erro` despencou de 2.158 → 2; ciclo supervisionado rc=0.
- Topo da fila real: **Lula 27/07/2026** (foto de ontem).

## 5. Lacunas honestas (para a Trindade não tropeçar)

1. **Agência Brasil Flickr NÃO tem conteúdo de tecnologia** (testado: Musk/Tesla/Nvidia/Starlink = 0 resultados; Moraes = 365). V4 Tecnologia depende hoje de Microsoft/Intel/Huawei/NASA (streams oficiais no registry) — **CEOs e fachadas precisam de conector Openverse/Wikimedia ou busca global CC do `flickr_media` V4**. Candidato a Iteração 2.
2. **V4↔banco:** o código V4 já lê o banco (`media_sources.py` `ouro_sqlite`, FTS5, `uso_automatico=1`) — aprovação do Miguel alimenta os V4 automaticamente. Mas os **agentes V4 de produção ainda não rodam** (Bloco B): no deploy, apontar `path_env` para `/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db`.
3. **`flickr_live.py` + `motor_publicador.py` alterados só no espelho local** — deploy no Tencent exige auditoria (protocolo padrão ouro). Peço revisão de Claude/Codex.
4. Fotos do Gov SP congeladas por legislação eleitoral até as eleições 2026; PT Flickr dormente desde abril.

## 6. Mapa de resiliência de visão (novo)

| Fluxo | Escalada |
|---|---|
| Robô Banco Ouro | **Gemini → Qwen VL** (novo hoje) + derivada >5MB |
| Cadeia V4 | Qwen → Gemini (já existia) |
| Legendas V3 | Gemini → Claude (roteador) |

## 7. Backups (todos no Tencent)

`robo_banco_ouro_midia_v3.py.bak_pre_fallback_qwen_20260728` · `agente_midia_oficial_externa_v3.py.bak_pre_verticais_v4_20260728` · `painel_midia_ouro.py.bak_pre_foto_na_hora_20260728` · `banco_midia_ouro_v3_pre_reclassificacao_20260728.db` · `crontab_root_pre_busca_ativa_permanente_20260728.txt`

**Rollback rápido:** restaurar os 3 `.py` dos backups + `crontab -l` do backup + restart `midia-ouro-panel.service`.

---

Ass: **ZCode (Kimi K3 Desktop)** — 2026-07-28 15:30 BRT
*"Foto de hoje aparece hoje."*
