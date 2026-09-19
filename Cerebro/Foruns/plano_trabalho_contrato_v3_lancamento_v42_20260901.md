# 📋 PLANO DE TRABALHO — Contrato da Casa v3 COMPLETO + lançamento suave do Redator V4.2

> **Pedido:** Miguel, via DSC celular, 01/09/2026 ~20:0x BRT ("refaz todo um plano de trabalho para mim com essas coisas todas para a gente fechar o contrato depois das 22:00 — um contrato completo abrangendo várias coisas do sistema").
> **Sessão de fechamento:** hoje, depois das 22:00 BRT.
> **Princípio da noite:** PRIMEIRO A LEI, DEPOIS OS CIDADÃOS — o contrato sai completo; o Publicador novo e o Redator V4.2 nascem JÁ conforme ele.

---

## 1. O CONTRATO v3 COMPLETO — o que entra hoje

### 1.1 Núcleo já aprovado na ouvidoria (unanimidade — NÃO se mexe)

2 checks independentes (R1 fact-check + R2 título/categoria) + autorização assinada (CL/CM/Miguel) + Publicador-carteiro + gate-cartório em todas as vias + fail-close + §131 portal limpo + Art. 6 (grade Laura preservada) + emendas **E1** (emergência blindada), **E2** (hash SHA-256 + TTL), **E3** (mini-cérebros — já no ar) e **E5** (health-check do gate 15min).

Emendas convergentes dos 10 pareceres: tirar `GM-` das refs que autorizam publish; `AL-` só por delegação expressa CL; gate cobre mídia (legenda+crédito+alt+img_check); canário de regressão 3 casos (268440/268553/268511) + teste só em draft/private; TTL 30min; alerta de fila 10min; readback ≤5min; isenção expressa para post de autor humano; ref `ordem-Miguel` só vale registrada em bloco datado na ponte.

### 1.2 Capítulo NOVO — Manual de Estilo VIVO (atualização constante)

1. O Manual de Estilo Unificado é **documento vivo, versionado e datado** — existe UM, no repo, com changelog.
2. O revisor/producer sempre lê **a versão do dia** (nunca cópia velha na memória) — entra no Kit do Revisor (Art. 5) por link, não por cópia.
3. **Lição vira regra em ≤24h**: erro fichado com data → emenda no manual com data → vale do próximo ciclo em diante (não retroativo).
4. Dono editorial: **CL** propõe/mantém; **regra nova só o Miguel promulga**.
5. Hoje o manual está no MEU v1.1.0 (EMU-1…EMU-5) — a lição nova de hoje (cargo no título, nome completo no lide — CL-030) já entra.

### 1.3 Capítulo NOVO — COLETA (a entrada finalmente ganha lei)

1. **Hierarquia de fontes** declarada (a mesma régua do V4.2 de imagens, aplicada a texto).
2. **Dedup de pauta/tese JÁ NA CAPTURA** — a lista dos últimos títulos é consultada ANTES de produzir o rascunho (hoje só o revisor vê).
3. **Licença e crédito capturados na ORIGEM** — item de mídia entra na fila JÁ com legenda/crédito/alt preparados (a causa do caption "default" do 268511 nasce aqui).
4. Fila priorizada: pessoa-central e frescor de pauta primeiro.
5. **Métrica diária**: pautas colhidas → rascunhos → publicadas; mortas e por quê (dono: DS Nuvem Ideias no relatório do dia).

### 1.4 Capítulo NOVO — IMAGENS (o coração do V4.2): de "certa" para "BONITA e JORNALÍSTICA"

**A evolução que o Miguel pediu** — hoje o sistema pergunta "a imagem está certa?"; o contrato passa a exigir 3 níveis, em ordem:

| Nível | Pergunta | Régua |
|---|---|---|
| 1. CORRETA | É da pessoa/tese certa? | visão dupla (pertinência — mantém; lição do 268380: aprovada ≠ pertinente) |
| 2. JORNALÍSTICA | Conta a notícia? | frescor (foto RECENTE), contexto do fato, **proibida institucional genérica antiga** (fachada de palácio, foto de arquivo desatualizada) |
| 3. BONITA | Vale a capa? | nitidez, resolução mínima, enquadramento, expressão/momento — foto do Lula CERTA existe aos montes; foto do Lula BOA é outra coisa |

Regras duras do capítulo:
- **Cascata multi-Vision como LEI**: PsicVision → QwenVision → GoogleVision → GeminiVision → KimiVision → DeepSeekVision (fallback um do outro; fail-close, nunca fail-open).
- **Nome no título → prioridade máxima é foto jornalística RECENTE da pessoa** (Emenda 12); tese dinâmica do redator como âncora da curadoria.
- **Hierarquia de fontes**: Flickr allowlist oficial (senado, lula, planalto, agência_brasil, câmara, stf, tse, governos, prefeituras) > **Banco Ouro da casa** > Wikimedia (só datada e relevante ao fato) > IA generativa (última, sempre com crédito).
- Legenda pt-BR + crédito + alt + `img_check` como **parte do item coletado, não retoque posterior**.
- Nenhuma capa pelada no ar (Lei v2 mantida); Tribunal Visual segue como instância de decisão.

---

## 2. RECUPERAÇÃO DO BANCO OURO V3 (a casa já tem 1.214 fotos aprovadas)

- **Estado real**: master na Tencent (`/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db`), 1.214 fotos aprovadas/R2 — e **NÃO é consultado pelo runtime** (diagnóstico Ideia-003 P3; endossado CL-041 §12). É ouro parado.
- **Sombra já medindo**: hit/miss desde 02:20 de hoje (ZM ADENDO 8). Régua de promoção proposta pelo DS-N Ideias: **hit-rate ≥80% com N≥20/24h** (2 níveis: pessoa-central ≥75%); bloco de decisão consolidado pro Miguel.
- **Cura (ordem de execução)**: (1) Banco Ouro como **camada 1 da cascata em sombra+flag** `OURO_CAMADA1`; (2) canário na vertical pessoa-central; (3) promoção gradual com a régua acima; (4) rollback sempre de 1 arquivo; (5) **banco por tese** (`tipo_entidade` + campo tese) + rank por frescor + homônimos via nomes canônicos; (6) **mapa de fontes canônicas por entidade** (P4 — a madrugada deixa de esperar a manhã: coluna `fonte prevista` na fila de capas).
- **Dono:** ZM (runtime) + DS Nuvem Imagem (relatório diário com taxa de acerto e NOTA DE QUALIDADE nova — níveis 1/2/3 do capítulo de imagens).

## 3. PESQUISA ABRANGENTE — todas as fontes de imagem do Brasil (seed inicial do DSC)

Levantamento começado agora (DSC); tabela viva a completar em 24h no fórum V4.2 com todos os agentes:

| Fonte | Licença | API | Frescor | Risco/nota |
|---|---|---|---|---|
| **Material fotojornalístico oficial do gov.br** (serviço "acessar material fotojornalístico gratuitamente") | uso público permitido | a verificar | alto | [gov.br](https://www.gov.br/pt-br/servicos/acessar-material-fotojornalistico-gratuitamente) — prioridade máxima |
| **Agência Brasil** (acervo também espelhado no Commons) | CC-like institucional | API a mapear | alto | [Commons: Agência Brasil](https://commons.wikimedia.org/wiki/Category:Photographs_by_Agencia_Brasil) |
| **Agência Senado / Câmara / Planalto / STF / TSE** | uso público permitido | Flickr oficial de cada uma | alto | já na allowlist — **mapear contas faltantes** |
| **Flickr allowlist** (governos, prefeituras, políticos) | CC BY variando | Flickr API | alto | núcleo atual do sistema |
| **Fotos Públicas** (coletivo fotojornalístico livre, de volta em parceria c/ Brasil de Fato) | CC | a verificar | alto | [notícia do retorno](https://nucleopiratininga.org.br/fotos-publicas-volta-ao-ar-nesta-segunda-feira-em-parceria-com-o-brasil-de-fato/) — candidato NOVO |
| Wikimedia Commons | CC/domínio público | API madura | baixo p/ política | SÓ datada e relevante (regra da casa) |
| IA generativa (cascata) | crédito obrigatório | interna | n/a | última opção, sempre com crédito |

Faltam mapear (24h): prefeituras capitals, assembleias, bancos de esporte (confederações), cultura/lazer, economia (B3, bancos), internazionale. **Saída: tabela viva no repo + coluna `fonte prevista` por entidade.**

## 4. TRANSIÇÃO SUAVE V4.1 → V4.2 (o baile sem sustos)

### 4.A A EVOLUÇÃO Nº 1 DO V4.2: ESCREVER MELHOR (ordem Miguel ~20:0x)

**O grande desafio do V4.2 é ser o redator mais talentoso da casa — na MESMA faixa de custo de tokens do V4.1, porém mais moderno.** Eixos apontados pelo Miguel:

1. **TÍTULO MELHOR** — "os títulos não estão ficando bons" (palavra dele): acabar com tradução literal (caso "prisão vitrine", OBS-033); título nasce JÁ na régua da casa (EMU/MEU v1.1.0), não conferido depois.
2. **TESE MELHOR** — aprofundar o ângulo próprio (a `tese_dinamica` é a âncora; não o fato cru).
3. **FRESCOR MELHOR** — critério de ESCOLHA da pauta, não só do post.
4. **NOTAS/ESTRUTURA MELHORES** — lide direto ao fato, zero metalinguagem, fecho com a pergunta que importa.
5. **COLETA E CURADORIA MAIS INTELIGENTES** — dedup de tese na captura, priorização melhor, menos repetição chegando ao redator.
6. **CUSTO IGUAL** — mesmo orçamento de tokens; a evolução é de MÉTODO (prompts em camadas, exemplos calibrados, self-review antes de entregar), não de gasto.

**Encaminhado ao DS-N IDEIAS** (encomenda `IDEIA_PRO_DSNUVEM_IDEIAS-005` no canal `de_ideias.md`, postada pelo DSC): estudar o V4 INTEIRO — não um pedaço — e desenhar o V4.2 que escreve melhor (síntese até 21:45 para a sessão das 22:00). **DS-Miguel segue líder da implementação** (carta 29/08).

O V4.2 **é o V4.1 modernizado, não uma troca de motor**: mesmo fluxo de redação, mesmo carimbo de rascunho — o que muda é **ELE ESCREVER MELHOR (nº 1)** + o **sistema de busca de imagem** (cascata multi-Vision + Banco Ouro + régua de qualidade 3 níveis) e a limpeza das sujeiras (caption "default", Wikimedia velha, dependência externa de capa).

| Fase | O quê | Risco | Saída |
|---|---|---|---|
| **0 (hoje)** | Integrar o que JÁ EXISTS pronto e nunca foi ligado: `featured_image_runtime.py` + `media_vision_providers.py` (NYC) no ciclo do V4.1 — mata a dependência externa que derrubou 11h de esteira em 29/08 | zero (código pronto) | V4.1 autossuficiente em capa |
| **1 (24h)** | Banco Ouro como camada 1 em **sombra+flag** (não publica; só mede) | zero | hit-rate real medido |
| **2 (48h)** | Cascata multi-Vision no **espelho** (Miguel: "testar V4.2 no espelho") | zero (espelho) | régua 3 níveis calibrada |
| **3 (≥72h)** | Canário pessoa-central na produção; promoção gradual por vertical com métrica | contido | rollback = 1 arquivo |
| **4** | V4.2 assume verticais; V4.1 permanece como fallback congelado | — | V4.2 oficial |

**Regra de ouro da transição: a esteira NUNCA para.** V4.1 publica enquanto V4.2 prova. Nada entra em produção sem bater a régua (hit ≥80% / qualidade 3 níveis); nada fica sem rollback de 1 arquivo.

## 5. DIVISÃO DA NOITE (22:00) + LINHA DO TEMPO

- **20:00–21:50** — DSC entrega este plano + rascunhos dos capítulos no repo; ZM traz spec do Publicador-carteiro; DS-Miguel traz estado/plano V4.2 (líder pela carta de 29/08); CL/CM preparam grade de assinaturas.
- **21:05** — placar da ouvidoria (ZM).
- **22:00** — sessão com o Miguel: lapidação do contrato COMPLETO (núcleo + 1.2 + 1.3 + 1.4 + plano de transição como anexo executivo).
- **Depois** — Miguel promulga ("vai") → tabela do Art. 7 roda os ACKs de todos → **Fase 0 dispara na hora** ( integração do runtime de imagem no V4.1).

## 6. CHECKLIST DE DECISÃO DO MIGUEL NA LAPIDAÇÃO (1 minuto cada)

1. ☐ Promulga v3 com os 3 capítulos novos (Manual Vivo + Coleta + Imagens)? 
2. ☐ Régua de qualidade 3 níveis (correta → jornalística → bonita) vira lei?
3. ☐ Banco Ouro: autoriza Fase 1 (sombra) com a régua de promoção ≥80%?
4. ☐ Fotos Públicas entra na pesquisa/fontes (novo candidato)?
5. ☐ Números: TTL 30min / alerta 10min / readback 5min / health-check 15min?
6. ☐ Isenção de autor humano + refs finais do gate (CL-/CM-/ordem-Miguel; AL- delegação; GM- fora)?
7. ☐ Transição V4.2: aprova o plano de fases 0→4 com a esteira nunca parando?

---
*Elaborado pelo DS Celular (DSC) sob pedido direto do Miguel · 01/09/2026 ~20:10 BRT · sessão us65. Fontes da pesquisa: gov.br, Wikimedia Commons, Núcleo Piratininga (Fotos Públicas).*
