---
name: project-cafezinho-media-group-diretriz-18jun
description: "Cafezinho Media Group consolidado por Miguel 18/06 00:46 BRT. Rede com selos (GSN/Geopolítica, Mundo Trilhos/Ferrovias, Rio Carta/RJ, AIatolá/IA). Arquitetura v2 padrão em camadas (coletor→banco bruto, produtor→banco publicável, mídia/auditoria→banco auditado, publicador independente). Foco editorial: IA + Política/Geopolítica + Comércio Exterior + **Ciência** (séria, não pop/sobrenatural). SOBRENATURAL + FANTÁSTICO descontinuados definitivamente por dano SEO/identidade — mas pauta CIENTÍFICA permanece (Hubble, arqueologia, oceanografia, física). Linha futura: técnica, sóbria, científica."
metadata: 
  node_type: memory
  type: project
  originSessionId: 8151465d-76ab-4d1d-bfe5-285d266e7ca7
---

# Cafezinho Media Group — diretriz consolidada 18/06 00:46 BRT

Miguel transmitiu áudio + Codex consolidou em `Projeto Cafezinho Agentes/Foruns/forum_cafezinho_media_group_agentes_v2_20260618.md`. Esta diretriz molda os agentes v2 e a arquitetura da Grande Reforma daqui pra frente.

## 1. Rede de sites + selos comerciais

Site central: **Cafezinho Media Group** (portal comercial, agrega rede, vende publicidade integrada).

Selos editorias / parcerias:
- 🌍 **Geopolítica** = Cafezinho + Global South News
- 🚂 **Ferrovias / Logística** = Mundo Trilhos
- 🌆 **Rio de Janeiro** = Rio Carta
- 🤖 **Inteligência Artificial** = AIatolá

Cada braço deve ter presença própria em redes sociais.

## 2. Arquitetura padrão dos agentes v2

```
Coletador → banco bruto (notícias / diálogos / insumos)
Produtor → banco publicável + imagens julgadas
Mídia / Auditoria → banco auditado + fact-check formal
Publicador / Validador → ordem + horários + caps + CMS
```

**Regras absolutas:**
- Coletor NÃO publica
- Produtor NÃO publica
- Publicador NÃO produz notícia
- Publicador consome estoque pronto
- Cada etapa deixa rastro persistente e auditável (replay/auditoria por etapa)

## 3. Foco editorial nichos prioritários

1. **Inteligência Artificial**
2. **Política e Geopolítica**
3. **Comércio Exterior**
4. **Ciência** (séria, técnica — Hubble/astronomia, arqueologia, oceanografia, física fundamental). NÃO confundir com sobrenatural/fantástico descontinuados.

## 4. 🚨 DESCONTINUAÇÃO DEFINITIVA: Sobrenatural + Fantástico (mas NÃO Ciência séria)

Temas **sobrenaturais** (Bigfoot, Loch Ness, Champ, criptozoologia, OVNIs/UAPs, criaturas folclóricas) **descontinuados** por dano SEO/identidade. Linha futura: técnica, sóbria, científica.

**Distinção crítica**: agente_fantastico tem PAUTAS LEGÍTIMAS de ciência (Hubble, Stonehenge arqueologia, Fossa das Marianas oceanografia, relógio nuclear tório-229, Templo Poseidon) que DEVEM permanecer — essas saem com cat 735 Ciência. O que sai é o sub-eixo sobrenatural/criptozoologia, não a ciência séria.

**Como aplicar:**
- Continuar curando bug classificador em pautas científicas (cat=[19936]→[735, 20699]) — Ciência É nicho prioritário, vale o esforço
- Posts de criptozoologia/Bigfoot/Champ — não recurar agressivamente (descontinuação iminente)
- Sprint Codex+GLM dupla classificador foca: Ciência + Geopolítica/LATAM + política Brasil (#259157 Petro, #259175 Bolsonaro, #259177 Lula+Crime, #259190 Hubble)
- Quando descontinuação efetivada, agente_sobrenatural sai das crons; agente_fantastico pode permanecer reformulado pra ciência séria apenas

## 5. Qualidade como regra central

Prioridades:
- Densidade técnica
- Fact-checking rigoroso (etapa formal registrada no banco)
- Sobriedade
- Elegância textual
- Autoridade de nicho
- Consistência de SEO

## 6. Implicações técnicas pros próximos agentes

- Bancos intermediários REAIS (não JSONL transitório)
- Estoque publicável ANTES de qualquer chamada WP
- Produtor e publicador como processos executáveis INDEPENDENTES
- Fact-check formal registrado no banco
- Mídia tem ciclo próprio (seleção, auditoria, crédito)
- Publicador controla agenda, prioridade, caps, ordem
- Logs/eventos permitem replay por etapa

## 7. Estado atual sprints

- 🟦 **Codex YouTube v2**: 3 camadas (coletor diálogos, produtor notícias publicáveis, publicador final) — local PASS 18/06 00:00 BRT
- 🟦 **Codex Política v2**: revisão pendente pra garantir separação produtor↔publicador (carta pra Kilo 00:31 BRT)
- 🟦+🟨 **Codex+GLM classificador**: cura bug acumulado focada em pautas que SOBREVIVEM (não fantástico/sobrenatural)

**Vinculado a:** [[reference_reforma_arquitetura_produtor_unico_diretrizes_json]] (REFORMA tem produtor único + diretrizes JSON; nova arquitetura v2 adiciona camadas bancos persistentes) · [[feedback_lula_nunca_cat_crime_sempre_politica]] (regras editoriais coexistem com nova arquitetura).
