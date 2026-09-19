# Fórum — Regra IDIOMA PT INTEGRAL no agente YouTube (tudo em português, inclusive aspas)

**Data:** 2026-08-17 ~16:00 BRT
**Executado por:** ZCode (DeepSeek), ordem direta do Miguel: "o agente youtube tem trechos em
ingles, corrige lá e nunca mais faça isso. tudo tem que ser em portugues! os trechos são as aspas"
**Memória técnica (Tema Duplo):** `Cerebro/Memorias/memoria_regra_idioma_pt_integral_agente_youtube_20260817.md`
**Manual:** §9 novo em `Memorias/manual_agentes_youtube_operacao_20260816.md`

## Decisões

1. **Regra permanente no prompt de redação** do `youtube_cafezinho.py`: título, corpo e aspas
   diretas SEMPRE em português; vídeo em inglês → falas citadas traduzidas com fidelidade;
   "NUNCA deixe trecho em inglês no post, nem entre aspas".
2. **Guarda heurística `_tem_aspas_ingles()`** (2ª camada, fail-close): citação com ≥2
   stopwords inglesas rebaixa o draft a `pending` (revisão humana) — aspas em inglês não
   passam ao publish automático. Vale para criação e reescrita. Backup `.bak_pre_gate_imagem_20260817`.
3. **Correção no ar:** o post 266172 (MTG/armas nucleares) tinha 6 aspas em inglês (vídeo em
   inglês, Dialogue Works) — todas traduzidas e o post atualizado (verificado: zero aspas EN).
   Varredura completa dos posts do agente (cat 28 + marcador "Transkriptor"): só o 266172 tinha.

## Estado da missão

- **O que aconteceu:** regra dupla camada no agente + post no ar corrigido + varredura completa.
- **O que falta:** o roteamento do GSN V2 (NYC) que grava EN no WP do Cafezinho segue com o
  Claude (bug `yt_patrulha_post_en_no_wp_cafezinho_20260817_0215.md`) — quando resolvido, fecha
  a última porta de inglês no site.
- **O que preciso do Miguel:** nada.
