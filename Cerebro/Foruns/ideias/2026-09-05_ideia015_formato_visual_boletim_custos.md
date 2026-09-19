# 🧠 IDEIA_PRO_DSNUVEM_IDEIAS-015 — FORMATO VISUAL DO BOLETIM DE CUSTOS (o e-mail que o Miguel lê no celular, 2×/dia) — DESENHO DO ARQUITETO

> **Ronda:** 05/09/2026 09:43-09:5x BRT (DS-N Ideias, Tencent). Pull da abertura: ff-only OK na 1ª (09:43; HEAD == origin `1db661657` = DS-N Chefe ronda 186 + adendo 09:42).
> **Bloco:** ENCOMENDA do Maestro (DS-N Chefe 186º, `de_dell.md` 09:38) — ordem do Miguel por voz 09:25 (INBOX_MIGUEL.md, áudio transcrito): *"manda isso para o dsn ideias para ele ter uma ideia bem legal de formato e ele manda para você e aí você conserta"*. Fluxo do bloco, nas palavras do Maestro: **Ideias desenha a proposta (arquivo + aviso no meu bloco da ponte) → DS-N CHEFE aplica e fecha com o DSN-F** — papel dele é dar formato/linguagem, como na IDEIA-014.
> **CHECK de leitura (ordem do Miguel 09:27, MANUAL_DE_COMUNICACAO_INTERNA):** LI O MANUAL DE COMUNICAÇÃO INTERNA (cerebro/Estilo/MANUAL_DE_COMUNICACAO_INTERNA.md) — este desenho segue as regras 1-10 dele (texto limpo, emoji sem tracinho, espaço para respirar, assinatura completa, nome na 1ª menção, links completos, sem segredo).
> **Natureza:** DESENHO DE FORMATO + template pronto + plano de aplicação com backup/prova/registro/rollback — **NADA executado em produção** (Lei de Poderes; não tenho credenciais de e-mail nem do script do Dell).
> **Marcador:** `PRONTO_FORMATO_BOLETIM_CUSTOS_015`

---

## 0. Contexto verificado (o que existe — sem executar nada)

1. **A reclamação do Miguel (áudio 09:25, INBOX_MIGUEL.md):** o e-mail automático do boletim de custos chega "cru, sem assinatura, sem emoji, texto truncado/amassado — muito difícil de ler". Ele pediu: conferir QUEM escreve e POR QUE está sem assinatura, refazer AGORA num extra só para ele ver, e mandar ao DS Nuvem Ideias desenhar a ideia de formato — o Chefe conserta.

2. **Emissor identificado (Chefe 186º):** pipeline antigo `scratch/enviar_boletim_custos.sh` (cron 8h02/18h02, máquina do Dell), criado em 06/08 ANTES da régua de comunicação da casa (assinatura atual: "— Boletim de custos · automático do Cafezinho (só Miguel)" — não identifica robô/inteligência/data). O texto nasce cru (dump de números, sem emoji, sem bloco, sem quebra). Decisão editorial já tomada (memória `memoria_baleia_azul_humanizacao_custos_separados_20260806.md`): o boletim de custos é SEPARADO da Baleia Azul — só o Miguel recebe; a Baleia não fala mais de gastos. Esta separação NÃO muda — só o formato interno do e-mail.

3. **O que o Miguel recebe hoje (corpo cru, 09:15:26 no INBOX):** bloco "💰 CUSTOS & LLMs (fonte: banco_custos NYC; medido até ontem)" com números colados (ontem US$ 41.69 · 7d US$ 101.46 | media/dia · 30d · projecao), top gastos por nome técnico cru (`youtube_transcriber_autonomo`, `v4_1_ciclo`, `v4_1_redator`), LLMs com nomes técnicos (`claude-sonnet-4-6`, `gpt-5.6-sol`, `transkriptor_url_direto`), e um 2º bloco "📝 AUDITOR DE TÍTULOS" (5 posts auditados · 0 correções · 1 alerta · custo US$ 0.000297) com alerta truncado no meio da frase. Tudo em dump, sem espaçamento, sem R$ formatado, assinatura sem robô.

4. **O que o Chefe JÁ fez (09:37-09:38):** (a) EXTRA no formato novo enviado ao Miguel em `RESPOSTAS.md` (09:37) — 1ª aproximação boa: saudação, números em blocos com R$, "o que mais pesou" traduzido para linguagem clara, LLMs com nome amigável e chamadas, painel com link completo, auditoria em 1 linha, assinatura completa do Chefe; (b) ORDEM no canal DSN-F (09:38): confirmar se os números do extra batem com o banco_custos e preparar/apoiar a versão nova do corpo do script com assinatura completa + emoji + espaçamento + sem asterisco, e reenviar o e-mail de hoje no formato novo (extra).

5. **A régua da casa (MANUAL_DE_COMUNICACAO_INTERNA, ordem 09:27 — arquivo novo):** texto limpo sem * # (regra 1) · emoji sem tracinho (2) · espaço para respirar, frases curtas, nada de bloco técnico cru no canal do dono (3) · assinatura completa com robô + inteligência + AAAAMMDD HH:MM:SS BRT (4) · texto bem escrito e humanizado (5) · nome completo na 1ª menção (6) · palavra estranha = perguntar (7) · cadência e silêncio (8) · links completos (9) · segredo nunca (10). Vale para "e-mails automáticos (ex.: boletim de custos)".

6. **Dados disponíveis para o template (fonte: DSN-F, `canal_dsn_financeiro.md` + `relatorios/2026-09-04.md` + extra 09:37):** ontem US$ · R$ (câmbio ~5,10) · 7d total + média/dia · 30d · projeção 30d · top agentes (nome técnico → traduzir) · top LLMs ontem com chamadas · saldo DeepSeek · painel `/v6/custos` · bloco auditoria de títulos (posts, correções, alertas, custo). O relatório diário do DSN-F tem ainda decomposição por servidor e alertas — MAS o e-mail do Miguel deve ser CURTO: a régua é o extra 09:37 (~1.300 caracteres), não o relatório completo (que fica no Cérebro para quem quiser).

> ⚠️ Nota de honestidade (números): os valores usados no exemplo abaixo são os do EXTRA do Chefe (09:37) e os do INBOX (09:15) — a conferência com o banco_custos está em andamento pelo DSN-F (ordem do canal 09:38: "se algo mudou desde o envio das 08:02, me diga o valor certo"). O template é agnóstico: quem preenche é o DSN-F/script. Não é papel desta ideia arbitrar número.

---

## 1. A IDEIA — "Boletim do Cafezinho": um formato com CARA, não um dump

O problema não é o número — é que o e-mail parece saída de terminal. A ideia é dar ao boletim uma **identidade fixa + régua visual + 1 frase de leitura por dia**, para o Miguel ler em <40 segundos no celular, sempre no mesmo lugar (memória muscular de leitura: ele sabe onde está cada coisa sem procurar).

**Os 3 furos do desenho (o que o extra 09:37 ainda não tem):**

1. **Identidade e repetição**: nome fixo + edição numerada no assunto ("Boletim de custos do Cafezinho — edição 05/09 manhã"). Todo dia o MESMO esqueleto, só os números mudam. Leitor que repete não relê instrução.
2. **"A leitura em 1 frase"**: uma linha humanizada que TRAduz o número (ex.: "ontem foi o dia mais caro da semana — o transcritor respondeu por 86% do total"). Gerada por REGRA determinística (3 padrões: dia mais caro / mais barato / no meio da semana) — **custo zero de LLM**, sem robô invisível e sem gasto novo no boletim.
3. **Tradução de nomes técnicos**: mapa de nomes amigáveis no script (config separada) — `youtube_transcriber_autonomo` vira "Transcritor de vídeos do YouTube". Nome de agente cru no e-mail do dono é a cara do dump.

---

## 2. Arquitetura do formato (componentes, dados, fluxo, onde roda)

| Peça | O que é | Onde roda | Dono |
|---|---|---|---|
| **Template** (novo corpo do e-mail) | Texto fixo com campos `{{ }}` — plain text (e-mail não renderiza markdown) | Dentro do script `enviar_boletim_custos.sh` (função `render_boletim`) | Dell (script) — desenho: esta ideia |
| **Mapa de nomes** (config nova) | dict nome_técnico → nome amigável (agentes + LLMs) | Arquivo de config do script (ex.: `mapa_nomes_boletim.json` ao lado do .sh) | Dell — conteúdo: DSN-F (dono dos nomes) |
| **Regra da frase do dia** | 3 padrões determinísticos (max/min/meio da janela) | Dentro do script — sem LLM | Dell |
| **Números** | kit de campos (abaixo) | banco_custos NYC (fonte única) + relatório do auditor (NYC) | DSN-F |
| **Câmbio R$** | conversão com a taxa do dia | fonte única DSN-F (a mesma do extra) | DSN-F |
| **Assinatura** | rodapé fixo: robô + o quê gerou + data/hora real | Template | Dell (data via `date`) |

**Fluxo (2×/dia, inalterado):** cron 8h02/18h02 no Dell → script puxa números do banco (NYC) + relatório do auditor → preenche o template → envia só para o Miguel → registro do envio no canal DSN-F. Nada muda no banco, no cron, no destinatário, na Baleia Azul.

**Kit de campos que o script precisa receber do DSN-F (contrato do template):**

```
data_base (ex.: 04/09/2026)          total_ontem_usd + total_ontem_brl
total_7d_usd + total_7d_brl          media_dia_7d_usd
total_30d_usd + total_30d_brl        projecao_30d_usd + projecao_30d_brl
top_agentes: [{tecnico, usd}]        top_llms: [{tecnico, chamadas, usd}]
saldo_deepseek_usd (p/ alerta < 10)  painel_url (fixo)
auditoria: {posts, correcoes, alertas: [texto curto], custo_usd}
cambio_usd_brl
```

**Regras de ouro do formato (para constar no comentário do script):**
- Bloco por seção; 1 emoji por seção, SEM traço antes do emoji (regra 2 do manual).
- Linha em branco entre blocos; frases de 1-2 linhas; linha ≤ ~60 caracteres (não quebra feio no celular).
- "Rótulo: valor" empilhado — NUNCA tabela de colunas (quebra no celular).
- Número no padrão BR: `US$ 41,69 (R$ 212,62)`; milhar com ponto (`R$ 2.165,78`).
- Sem nome técnico cru (usa o mapa; fallback = nome cru se não mapeado).
- Silêncio por padrão: alertas/lacunas só aparecem quando existem; saldo DeepSeek só com 🟡 quando < US$ 10.
- Assinatura completa no rodapé (regra 4): quem gerou + o quê + AAAAMMDD HH:MM:SS BRT real.
- Sem markdown nenhum no corpo (e-mail plain text): nem *, nem #, nem _.

---

## 3. RASCUNHO — template do boletim (texto limpo, pronto para o script)

### 3.1 Template (com campos; o script substitui `{{ }}`)

```
💰 Boletim de custos do Cafezinho — {{dia_semana}}, {{data}}

{{saudacao}}, Miguel!

Segue o resumo dos gastos do ecossistema, medido até {{data_base}}.

📈 Os números
Ontem: US$ {{total_ontem_usd}} (R$ {{total_ontem_brl}})
Últimos 7 dias: US$ {{total_7d_usd}} (R$ {{total_7d_brl}}) — média de US$ {{media_dia_7d_usd}} por dia
Últimos 30 dias: US$ {{total_30d_usd}} (R$ {{total_30d_brl}})
Projeção para 30 dias no ritmo atual: US$ {{projecao_30d_usd}} (R$ {{projecao_30d_brl}})

💡 A leitura em 1 frase
{{frase_do_dia}}

🔍 O que mais pesou ontem
{{top_agentes_amigaveis}}  (ex.: Transcritor de vídeos do YouTube: US$ 36,00 — um por linha)

🤖 Inteligências mais usadas ontem
{{top_llms_amigaveis}}  (ex.: Claude Sonnet: 34 chamadas, US$ 3,08 — um por linha)
{{linha_saldo}}  (vazia se saldo ≥ US$ 10; senão: 🟡 Saldo DeepSeek: US$ {{saldo}} — abaixo de US$ 10)

🔗 Painel completo: http://43.156.151.165/v6/custos

📝 Auditor de títulos de hoje
{{auditoria_1linha}}  (ex.: 5 posts auditados · 0 correções · 1 alerta · custo US$ 0,0003)
{{auditoria_alertas}}  (até 2 alertas, 1 linha cada, texto curto; vazio se não houver)

Este boletim sai sempre assinado, de manhã e no fim da tarde. Quer ver algum número mais de perto? É só pedir.

— Boletim de custos do Cafezinho · emissor: DS Nuvem Finanças (DSN-F) · gerado por enviar_boletim_custos.sh (automático, sem LLM) · {{AAAAMMDD HH:MM:SS BRT}}
```

### 3.2 Exemplo preenchido (valores do extra 09:37 do Chefe — PROVISÓRIOS, conferência DSN-F em andamento)

```
💰 Boletim de custos do Cafezinho — sexta-feira, 05/09

Bom dia, Miguel!

Segue o resumo dos gastos do ecossistema, medido até ontem, 04/09.

📈 Os números
Ontem: US$ 41,69 (R$ 212,62)
Últimos 7 dias: US$ 101,46 (R$ 517,45) — média de US$ 14,49 por dia
Últimos 30 dias: US$ 424,66 (R$ 2.165,78)
Projeção para 30 dias no ritmo atual: US$ 434,83 (R$ 2.217,64)

💡 A leitura em 1 frase
Ontem foi o dia mais caro da semana: o transcritor de vídeos respondeu por US$ 36,00 dos US$ 41,69 (86% do total). Sem susto — foi a transcrição que você pediu.

🔍 O que mais pesou ontem
Transcritor de vídeos do YouTube: US$ 36,00
Ciclo de produção V4.1: US$ 4,28
Redator V4.1: US$ 1,10

🤖 Inteligências mais usadas ontem
Transcritor de URL direto: 6 chamadas, US$ 36,00
Claude Sonnet: 34 chamadas, US$ 3,08
GPT-5.6: 98 chamadas, US$ 2,27
DeepSeek de rotina: 88 chamadas, US$ 0,08

🔗 Painel completo: http://43.156.151.165/v6/custos

📝 Auditor de títulos de hoje
5 posts auditados · 0 correções · 1 alerta · custo US$ 0,0003
Alerta: o título do Luiz Gustavo diz que ele lidera o Athletico, mas o lide diz que ele pode receber a braçadeira.

Este boletim sai sempre assinado, de manhã e no fim da tarde. Quer ver algum número mais de perto? É só pedir.

— Boletim de custos do Cafezinho · emissor: DS Nuvem Finanças (DSN-F) · gerado por enviar_boletim_custos.sh (automático, sem LLM) · 20260905 08:02:05 BRT
```

### 3.3 Mapa de nomes (rascunho da config; DSN-F confere e completa)

```
agentes:
  youtube_transcriber_autonomo  → Transcritor de vídeos do YouTube
  v4_1_ciclo                    → Ciclo de produção V4.1
  v4_1_redator                  → Redator V4.1
  dsn_youtube                   → DS YouTube
  auditor_titulos_gpt           → Auditor de títulos
llms:
  transkriptor_url_direto       → Transcritor de URL direto
  claude-sonnet-4-6             → Claude Sonnet
  gpt-5.6-sol                   → GPT-5.6
  gpt-5.5                       → GPT-5.5
  gpt-4o                        → GPT-4o
  deepseek-chat                 → DeepSeek de rotina
  qwen3-vl-32b-thinking         → Qwen (visão)
fallback: nome técnico cru (sem invenção)
```

### 3.4 Regra da frase do dia (determinística, sem LLM — rascunho de lógica)

```
se total_ontem == max(7 dias) → "Ontem foi o dia mais caro da semana: {top1_amigavel} respondeu por US$ {top1_usd} dos US$ {total} ({pct}% do total). {contexto_opcional}"
se total_ontem == min(7 dias) → "Ontem foi o dia mais barato da semana: US$ {total} (R$ {brl}). Ritmo de economia."
senão → "Ontem ficou no meio da semana: US$ {total} (R$ {brl}), {delta}% acima/abaixo da média dos outros dias (US$ {media_sem_o_dia})."
```
O `contexto_opcional` (ex.: "foi a transcrição que você pediu") pode ser um campo manual raro do DSN-F quando houver causa conhecida — nunca obrigatório.

---

## 4. Plano de execução (protocolo da casa: backup → prova → registro → rollback escrito)

| Passo | Ação | Dono | Prova |
|---|---|---|---|
| **P0** | Chefe chancela o desenho + Miguel dá o ✓ no modelo (o extra 09:37 já é a amostra viva) | Chefe/Miguel | ✓ no canal |
| **P1** | Backup do script no Dell: `cp enviar_boletim_custos.sh enviar_boletim_custos.sh.bak_AAAAMMDD` (+ backup da config se existir) | DS-Dell/ZM | ls do .bak no canal |
| **P2** | Aplicar no script: função `render_boletim` com o template §3.1 + config `mapa_nomes_boletim` §3.3 + regra da frase §3.4; cron/destinatário/horário INTOCADOS | DS-Dell/ZM (com o DSN-F nos nomes) | diff do script no canal |
| **P3** | Prova: reenviar o e-mail de hoje no formato novo (extra) e conferir com o Miguel (ele pediu "manda agora um extra só para eu ver") | DS-Dell/ZM → Miguel | confirmação do Miguel no INBOX |
| **P4** | Registro no `canal_dsn_financeiro.md`: o que mudou, quando, por quem; número conferido com banco (ordem 09:38) | DSN-F | linha no canal |
| **P5** | Rollback (se algo quebrar): restaurar o .bak do P1 — alavanca única, < 5 min | DS-Dell/ZM | comando + resultado no canal |

**Riscos e mitigação:**
1. Números divergentes (extra 09:37 × banco) → conferência do DSN-F ANTES do P3 (ordem 09:38 já aberta); o template não inventa número.
2. Quebra de linha feia no cliente de e-mail → linhas ≤ 60 caracteres e sem tabela (regra do §2).
3. Emoji não renderizar em cliente antigo → emoji é só marcador de seção; o número nunca depende dele.
4. Nome técnico novo sem mapa → fallback = nome cru (nunca inventar tradução).
5. Mudança de câmbio → fonte única DSN-F no dia do envio.
6. Reversibilidade → P1 (backup) antes de P2; rollback P5 < 5 min; nada toca banco/cron/Baleia Azul.

---

## 5. O que preciso (para o fluxo fechar)

- **Chefe:** aplicar o desenho quando chancelar (P0-P5) e fechar com o DSN-F — papel dele no fluxo, como combinado no bloco.
- **Miguel:** ✓ no modelo (a amostra é o extra 09:37 + este desenho) e no "reenviar hoje" — o desenho não vale sem o ✓ dele.
- **DSN-F:** conferir os números do exemplo (ordem 09:38 em andamento) · manter/ampliar o mapa de nomes §3.3.
- **DS-Dell/ZM:** aplicar o template no script do Dell com backup e prova (P1-P3/P5).

Nada em produção (Lei de Poderes): este arquivo é desenho + rascunho; execução só com ✓ do Miguel e aplicação do Chefe.
