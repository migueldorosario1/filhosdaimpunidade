# 📣 VAGA: DS RELAÇÕES PÚBLICAS + PROJETO MAPA RIO — rascunho para ✓ do Miguel

> **Origem:** pedido do Miguel por voz ao DSH/us65 em 01/09/2026 ~02:0x BRT (transcrição literal — nomes próprios marcados ⚠️ para confirmar). Frases-chave: *"a gente tem que ter muita maturidade porque publicidade é relações públicas"* · *"quero criar também um DSN de relações públicas para estudar os diferentes níveis de empresas e governos com os quais a gente deveria se relacionar e mandar relatório"* · *"rastreamento de todos os vereadores do Brasil, suplentes, quantos eleitores tiveram… pesquisa científica, banco de dados total"* · *"mapa Rio… sessão Mapa Rio aqui na nossa inteligência… usar para investir em tecnologia e pesquisa"* · *"é o projeto lá do Remo, foi uma relação de confiança política comigo"* · *"não quero dinheiro, quero debater como a gente distribui bem os recursos"* · *"manda o resumo pelo Telegram"*.
> **Nascimento:** ✓ do Miguel → prompt da §7 numa sessão dedicada (padrão DS-N Pub / DS-N Redes).
> **Regra-mãe:** dados de pessoas públicas a partir de FONTES PÚBLICAS OFICIAIS (TSE/Câmaras/ALERJ/Assembleias/Congresso), nada de dado pessoal sensível, nada de compra secreta de dados, nada se publica sem ✓. Este documento registra uma INTENÇÃO de projeto — nada foi contratado nem construído ainda.

## 1. As duas frentes (uma sessão, dois ofícios gêmeos)

**A) DS-N RP (Relações Públicas)** — o "diplomata" da casa:
1. Mapear **com quem a casa DEVERIA se relacionar**, por nível: prefeituras, câmaras municipais, ALERJ e assembleias, deputados estaduais e federais, senadores, órgãos públicos, empresas (patrocínio, publicidade direta, publipost), institutos e fundações.
2. Estudar cada nível (como funciona, quem decide, qual a porta de entrada) e manter **memória viva de relacionamento** (quem já falou com quem, o que pendeu).
3. **Relatórios periódicos** ao Miguel (Telegram + Cérebro), com recomendações de aproximação — sempre maduro: institucional primeiro, transacional depois.
4. Sinergia declarada com o **DS-N Pub** (publicidade): anunciante direto é relatório público de audiência + relacionamento; o RP abre a porta, o Pub entrega o número.

**B) PROJETO MAPA RIO** — banco de dados político-científico da casa:
1. **Escopo final (decidido pelo Miguel):** todos os **vereadores do Brasil + suplentes** (com votação recebida), **deputados estaduais** e **deputados federais** — e o universo eleitoral de cada um (eleitores do município/estado).
2. **Piloto:** banco TOTAL do **Rio de Janeiro** primeiro (capital + 92 municípios: 51 vereadores da Capital + câmaras do estado, ALERJ 70 deputados, RJ na Câmara Federal e Senado) — daí escalar para o Brasil (≈5.570 municípios, ≈51 mil vereadores titulares + suplentes).
3. **Uso declarado:** pesquisa científica, tecnologia e inteligência editorial (o Cafezinho cobre política — o banco alimenta cobertura, gráficos e séries históricas).
4. É a "sessão Mapa Rio" na inteligência da casa — pasta própria, relatórios próprios.

## 2. O que a casa JÁ tem (herança aproveitável)

| Ativo | Estado | Uso no Mapa Rio |
|---|---|---|
| Banco Ouro de mídia (743+ fotos de políticos, fontes oficiais) | ✅ vivo | Foto oficial de cada mapeado ( Matcher já liga manchete→pessoa) |
| V4 regional (cobertura por estado) | ✅ vivo | Canal editorial p/ publicizar o que o banco descobrir |
| Café/audiência (contador + GA4) | ✅ vivo | Número de audiência para apresentação institucional |
| Infra DS (Tencent/us65, Git ponte, Telegram) | ✅ vivo | Onde o robô e o banco moram |
| **Dados eleitorais estruturados** | ❌ NÃO existe — é a lacuna que o Mapa Rio preenche | — |

## 3. Fontes de dados (verdade primeira: o dado público é GRÁTIS)

- **TSE — Dados Abertos** (base oficial, gratuita, baixável): *Consulta de Candidatos* (titulares **e suplentes** com situação), *Votação por candidato* (município/zona), *Perfil do Eleitorado* (eleitores por município), resultados consolidados 2024. É 90% do Mapa Rio sem gastar 1 real.
- **Câmara Municipal do Rio (DataLR)**, **ALERJ** (dados abertos de deputados), **Câmara dos Deputados API** (deputados federais: id, partidos, comissões), **Senado API** — todos públicos.
- **Banco de dados pago anual** (transcrição ⚠️ "Cláudio"?) — a contratar SÓ como complemento (atualização/cruzamento), nunca como fonte única; custo/nome a confirmar com o Miguel antes de qualquer assinatura.

## 4. Fases propostas

- **F0 (feito neste documento):** registro da intenção + contexto.
- **F1 — Piloto Rio (1ª entrega):** carregar TSE 2024 → RJ completo: 51 vereadores da Capital (titular+suplente+votos+coligação), câmaras dos 92 municípios, 70 deputados ALERJ, bancada federal RJ; entregar em `Relatorios/mapa_rio/` com método declarado.
- **F2 — Escala Brasil:** todos os municípios; sanity checks (soma de votos, lacunas de suplência).
- **F3 — DS-N RP em ronda:** relatório quinzenal de "com quem relacionar" por nível + dossiê de 1 página por instituição-alvo; memória de contatos.
- **F4 — Debate de recursos (Miguel + Rogério ⚠️ + Maíra ⚠️):** mesa sobre a verba do projeto (do Remo ⚠️ — confiança política): assinatura GLM anual dividida em 3 ("uma IA de primeira… ela vai segurar a gente"), banco pago anual, e o que mais o Miguel puser. **O Miguel foi explícito: não quer dinheiro para si; quer debater a MELHOR distribuição.** A casa prepara o dossiê de custos; a decisão é deles.

## 5. Regras inegociáveis (herdadas + específicas)

1. Fontes públicas oficiais apenas; dado de pessoa pública no contexto de função pública; **nada de dado pessoal de eleitor** (nunca existe no TSE aberto, e nunca será procurado).
2. Nomes de pessoas da conversa (Remo ⚠️, Rogério Dutra ⚠️, Maíra ⚠️) ficam como o Miguel falou, marcados para confirmar — nunca presumir vínculo nem inventar autoria (padrão `COMENTARIOS_ROGERIO.md`).
3. Nada se contrata/assina sem ✓ do Miguel; verba é debateda em F4, não executada por robô.
4. Regras da casa: pt-BR; hora real; UTF-8 sem BOM; sem segredos (§82); commit seletivo; assinatura `— DS <nome> · carimbo`; MONITORAMENTO sempre.

## 6. Interação Miguel ↔ robô (pedido explícito dele)

Padrão inaugurado nesta conversa: **Miguel fala (aqui ou no Telegram) → robô responde aqui → resumo curto vai ao Telegram dele ("DFC" ⚠️ a confirmar qual chat) na mesma interação, 1 ou 2 mensagens, sem demora.**

## 7. 📋 PROMPT — colar na sessão dedicada (após ✓)

> 🤖 PROMPT — SESSÃO DEDICADA "DS RELAÇÕES PÚBLICAS + MAPA RIO"
>
> MISSÃO: (A) ser o diplomata da casa — mapear níveis de empresas/governos para relacionar e relatar; (B) construir o MAPA RIO, o banco político-científico da casa (vereadores+suplentes+votos do RJ → Brasil; depois deputados estaduais/federais).
>
> 1) LEIA PRIMEIRO: `Foruns/VAGA_DS_RELACOES_PUBLICAS_MAPARIO_20260901.md` (teu contrato) · `Foruns/forum_banco_ouro_candidatos_qwen_20260805.md` (banco de fotos ligável) · `Foruns/VAGA_DS_PUBLICIDADE_20260901.md` (irmão Pub — sinergia).
> 2) F1 PILOTO RIO: baixar TSE Dados Abertos 2024 (Candidatos c/ suplentes; Votação por candidato; Perfil do Eleitorado) → montar `Relatorios/mapa_2026.../mapa_rio/` com: (a) os 51 vereadores da Capital (nome, partido, coligação, votos, suplente, situação); (b) tabela dos 92 municípios (vereadores eleitos, quociente eleitoral, eleitores); (c) 70 deputados ALERJ; (d) bancada RJ federal. Método e data de corte declarados no relatório.
> 3) DS-N RP: relatório quinzenal "COM QUEM RELACIONAR" (1 nível por vez: prefeituras → câmaras → ALERJ → federal → empresas), dossiê de 1 página por alvo (o que faz, quem decide, porta de entrada, o que a casa oferece).
> 4) INTERAÇÃO: resumo curto ao Telegram do Miguel a cada entrega (padrão §6 da vaga).
> 5) REGRAS: só fonte pública oficial; sem dado pessoal de eleitor; nomes ⚠️ confirmar antes de usar; nada se assina sem ✓; regras da casa (hora real, §82, commit seletivo, assinatura DS, MONITORAMENTO).
>
> Comece lendo a vaga, entregue o piloto RJ e reporte como **DS-RP-001**.

## 8. Pendências para o ✓ do Miguel

1. Confirmar nomes (transcrição de voz): **Remo** · **Rogério Dutra** · **Maíra** — e quem entra no debate de recursos (F4).
2. **Banco de dados pago anual**: qual serviço (transcrição "Cláudio" ⚠️)? custo? — antes de qualquer assinatura.
3. **Assinatura GLM 1 ano ÷ 3** (Miguel/Rogério/Maíra): confirmar plano/valor — a casa prepara comparativo na F4.
4. Telegram do resumo: mandar no chat **"DFC"** ⚠️ (qual chat exato? hoje usei o canal DSC existente no vault).
5. Ordem das frentes: RP e Mapa Rio nascem juntos (uma sessão) ou o Mapa Rio primeiro (dado é o alicerce)?

— Registrado por **DS us65 (DSH)** · 20260901 02:05:00 BRT · transcrição de voz do Miguel anotada com ⚠️ nos nomes a confirmar
