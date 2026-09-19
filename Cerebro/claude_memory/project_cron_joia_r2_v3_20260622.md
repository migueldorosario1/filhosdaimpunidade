---
name: project-cron-joia-r2-v3-20260622
description: Cron diário 04:00 BRT populating R2 V3 mídia — Wikimedia + Flickr oficiais BR (Lula Oficial/Senado/Câmara/STF) + banco legado. Bug Flickr license=12 (CC BY-SA 4.0) corrigido.
metadata: 
  node_type: memory
  type: project
  originSessionId: 831ab0d8-9f43-4146-9bf9-65f536fabdf7
---

Sprint Joia R2 V3 (J1→J5) deployada 22/06 13:46 BRT após AUTH Miguel 13:20 BRT. Cron diário **04:00 BRT** (07:00 UTC) ativo no Tencent. Script `/root/util_joia_r2_v3.py` v4 MD5 `71e9b43a2fca876ba0503423b5ebdfbd`.

**Por que cron em vez de manual:** Miguel pediu pra transformar R2 V3 numa "joia de mídias" — catalogação contínua, crescimento orgânico, sempre indexado, sem repetição. R2 tem **bytes** da imagem no bucket S3-compatible; banco legado (`banco_imagens_reais.db`) tem só URLs/metadados. R2 é mais seguro no momento crítico da publicação (sem rate limit externo, sem depender de Wikimedia/Flickr responder bem).

**Why:** R2 V3 tinha 136 imagens indexadas manualmente em 2 dias; precisava escalar pra 500-700 em 2-3 semanas. Cron 04:00 BRT escolhido (janela baixa competição V3). 50 entidades canônicas (30 política BR + 20 geopolítica crítica).

**How to apply:** Ao diagnosticar problemas de imagem V3, checar `/var/log/r2_joia.log`. Se precisar adicionar entidade nova, editar `ENTIDADES` ou `FLICKR_OFICIAIS` em `/root/util_joia_r2_v3.py` e fazer upload + py_compile. Se banco R2 corromper, restaurar de `/root/backups/banco_catalogo_midia_r2_v3_pre_joia_*.db`.

**Bug Flickr crítico encontrado e corrigido (22/06 13:42 BRT):**
- Flickr license IDs novos pós-2024: **11=CC BY 4.0**, **12=CC BY-SA 4.0**
- Conta oficial "Lula Oficial" (NSID 157736962@N05) usa license=12 em TODAS as 46.879 fotos
- Filtro antigo (`4/5/7/8/9`) rejeitava TUDO → buscar_flickr retornava 0
- Patch estendeu pra `("4", "5", "7", "8", "9", "10", "11", "12")` com `lic_map` atualizado
- Validação curl: `flickr.photos.search user_id=157736962@N05` retornou 46.879 fotos CC BY-SA 4.0

**Descoberta: Flickr "planalto" (NSID 25462014@N00) tem só 1 foto (gato 2007).** Oficial real do Lula é "Lula Oficial". Mapeamento `FLICKR_OFICIAIS` atualizado pra usar NSID hardcoded + username fallback.

**Estado banco R2 V3 pós-piloto Lula (22/06 13:44 BRT):** 145 imagens (141 Wikimedia + 3 Câmara Deputados + 1 smoke) · 100% indexadas · 100% FTS5. Meta: 500-700 em 2-3 semanas.

**Esforço massivo pré-cron (22/06 14:03-14:25 BRT, 22 min execução):** Miguel pediu pra popular R2 antes do cron 04:00 BRT. Adicionei 15 entidades extras às 50 canônicas (65 total): Khamenei, Pezeshkian, Medvedev, Shoigu, Kremlin/Rússia institucional + B3/BCB/Fazenda/IPCA/Dólar/Petróleo/Agro. Resultado: **465 imagens** (155% da meta 300), 320 novas, 100% indexadas FTS5, smoke PASS. Distribuição: política 318 + geopolítica 134 + economia 13. Top cobertura: Lula 24, Bolsonaros 9-11 cada, STF 9-12 cada, Trump/Biden/Putin/Xi cobertos. Script MD5 v5: `cdaabd4130655c483e80f5164f32c7b6`.

**Sprint 2 massivo (22/06 16:09-16:53 BRT, 44 min execução):** Miguel pediu mais 300-400 imagens. Adicionei 23 entidades novas às 65 (88 total): governo Trump 2025 (JD Vance, Marco Rubio, Pete Hegseth, Tulsi Gabbard, RFK Jr, Elon Musk, Pompeo, Grenell) + autoridades iranianas (Raisi, Zarif, Bagheri Kani, Soleimani, Parlamento) + IA (OpenAI, DeepMind, Anthropic, DeepSeek, Arte Gen, Robótica, Conceito) + instituições EUA (Capitólio, Casa Branca, Pentágono). Resultado: **1059 imagens** (149% da meta +400), +594 novas, 100% FTS5, smoke PASS. Distribuição: política 584 + geopolítica 396 + IA 46 (nova!) + economia 33. Top: Lula 34, Bolsonaros 17-21, STF 18-20, Trump 16, Biden 16, Obama 16, Khamenei 16, JD Vance 7, Musk 10, Pompeo 10, Raisi 10, Irã Parlamento 10. Script MD5 v6: `8a8cad7bd28dac6d859cafbc5f835478`.

**Carta ao Codex (22/06 16:58 BRT):** `Foruns/carta_codex_auditoria_compat_r2_v3_20260622.md` — Miguel pediu pra Codex auditar compatibilidade R2 (1059 imgs) ↔ pipeline V3. 5 pontos: (1) queries `executar_midia_v3_real.py` contra 1059 imgs, (2) `midias_r2_index`+`midias_r2_fts` sincronizadas, (3) coerência metadados 594 novas, (4) cascata preferencial em produção, (5) performance <100ms.

**Vigília:** primeiro cron run 04:00 BRT 23/06 — checar log no tick §53 pós-04:30 BRT.

**Pendências menores:**
- Aguardar resposta Codex aos 5 pontos da cartilha de indexação R2 (`Foruns/carta_codex_indexacao_r2_v3_20260622.md`)
- Bug pré-existente `KeyError: 'produzidas'` em `executar_publicador_wp_v3_pending.py:233` (sprint separada)

Fórum completo: `Foruns/forum_cron_joia_r2_v3_20260622.md`. Relacionado: [[feedback-disco-tencent-100-emergencia]] (rotação tar.gz), [[feedback-janitor-banco-midia-protocolo-20260621]] (janitor banco legado).
