# 🖼️ Fórum — Mídia Ouro: nome identificado tem prioridade (ordem Miguel 07/08/2026 ~18:29)

> Tema Duplo de `Memorias/memoria_midia_ouro_prioridade_nome_identificado_20260807.md` (log técnico completo).
> Sessão: ZCode (`k3-256k` — 1ª missão real no modelo econômico do top-up), workspace ZCodeProject, chat direto.

## O pedido (voz, quase literal)

Miguel na página `/midia-ouro/revisao`: card com entidade **Hugo Motta** e foto do **Lula** ("uma ótima foto do Lula, nome identificado Lula"), e o card exibia **"Lula" e "Luiz Inácio Lula da Silva" juntos**. Ordens:
1. **Não pode ter as duas formas juntas** — "tem que botar um só" (fica só "Lula").
2. **O nome identificado tem prioridade** — "você muda a entidade, senão vai confundir o agente".
3. **Aprova direto** quando houver só 1 nome identificado ("se for só um nome identificado, for Lula, aprova agora").
4. **Corrige os arquivos que já estão lá** (retroativo) — "eu pedi já isso, pensei que você fosse corrigir automaticamente".

## Causas raiz (3)

1. **Painel** (`/root/painel_midia_ouro.py`): a lista de nomes exibida no card misturava `pessoas_identificadas_json` (já unificado 06/08) com `gemini.personalidade_principal` **cru** ("Luiz Inácio Lula da Silva") — sem `unificar_lista` na exibição. Por isso as duas formas apareciam juntas.
2. **Classificador** (`/root/V3/classificar_banco_ouro_midia.py`): nunca mexia na `entidade` — vinha sempre da fonte (página de origem), mesmo quando o gemini identificava outra pessoa como principal.
3. **Aprovação automática** exigia zero motivos; fotos de 1 pessoa identificada com motivos leves (título genérico, contextual, dimensão, ratio) caíam na fila humana.

## O que foi feito (ENTREGUE e verificado ao vivo, 07/08 ~18:50)

- **Painel:** `unificar_lista` na montagem das sugestões → card nunca mais mostra 2 formas da mesma pessoa. Prova ao vivo (API): card da cerimônia do Pacto contra o Feminicídio exibe `['Lula','Janja','Hugo Motta','Edson Fachin']` (antes traria "Luiz Inácio Lula da Silva" + "Lula").
- **Classificador — prioridade do nome identificado:** 1 nome identificado (pós-cânone) → entidade = esse nome; vários nomes → entidade = `personalidade_principal` (cânone). Retroativo: **11 entidades corrigidas** (incl. o card do Miguel: Hugo Motta → **Lula**).
- **Classificador — aprova direta:** 1 pessoa identificada + cena de 1 pessoa + sem bloqueio duro (licença/gemini/grupo incompleto/pessoa desfocada) + score ≥ 450 → `uso_automatico` direto (pula a fila), `tipo_uso=uso_automatico_nome_identificado`, motivo `regra_nome_identificado_prioritario_miguel_20260807`. 4 registros já classificados pela regra nova; 0 movimentos auto↔revisão indevidos (auditoria contra backup).
- **JSON armazenado:** 0 registros com forma longa ("Luiz Inácio…" / "Janja Lula da Silva") em `pessoas_identificadas_json`.
- Fila pendente: 397 → 397 (os 25 pendentes de 1 nome tinham bloqueio real: 13 grupo incompleto, 5 pessoa desfocada, 6 score < 450, 1 grupo de 5 pessoas).

## Estado da missão

- **Pronto:** as 3 ordens + retroativo, tudo ao vivo; backups `*.bak_pre_prioridade_nome_20260807` (2 arquivos) + tabelas `*_bak_priornome_20260807` (midia 739, fila 697); cron `:17/:47` mantém a regra daqui pra frente; painel reiniciado (porta 8091, página pública 200).
- **Não auto-aprova (by design, proteção editorial):** fotos de grupo com pessoas sem nome, pessoa desfocada/em segundo plano, score < 450 (fotos pequenas). O card original do Miguel (7 pessoas na cena, 4 identificadas) ficou com entidade **Lula** e segue na fila só para catalogar os demais.
- **O que preciso de você (Miguel):** (1) quer que **grupo com principal identificado também aprove direto** (ex.: a foto do pacto, principal=Lula)? (2) quer que a regra **ignore o score** para as 6 fotos pequenas (353–417)? Uma palavra e eu ajusto.

— ZCode (`k3-256k`), 07/08/2026 ~18:55 BRT

## ADENDO ~19:00 — checkpoint (crédito top-up esgotou)

- **Nova subtarefa aberta pelo Miguel (19:00):** "ver se o Lula aparece com destaque na cena" + **criar PROTOCOLO sobre o tamanho/prominência do presidente na foto**. Em andamento: URLs R2 das fotos do card (`8ec180fb…` e irmã `014c2648…`, Agência Brasil/EBC, 1024×683) já levantadas — próxima sessão: baixar e analisar visualmente + desenhar o protocolo (limiares de tamanho/posição do principal na cena → integrar ao classificador).
- **Crédito:** pacote top-up Kimi consumido $19,75 no mês, saldo $0,25 — Miguel: "definitivamente não vale a pena usar crédito extra". Sessão migra para Qwen Token Plan e retoma daqui.

## ADENDO ~19:25 — Protocolo de Prominência do Principal v0.1 (ordem Miguel)

> Miguel (~19:00): "tem que ver se o Lula aparece com algum destaque na cena" + "vamos criar um protocolo sobre o tamanho do presidente na foto".

**Olhei as 2 fotos do card** via a `descricao_visual` que o Gemini já grava na ingestão (a tool de visão MCP deu erro 400/parse; a leitura direta da análise estruturada é mais confiável). Confirmado: Lula tem destaque **totalmente diferente** nas duas:
- `8ec180fb`: Fachin **discursa no pódio**; Lula **sentado na primeira fila** → foto do *evento/Fachin*.
- `014c2648`: Lula **ao centro, segurando documento, posa** → retrato do *Lula*.

### Protocolo v0.1 — 4 tiers (decisão Miguel: "implementar como está")

| Tier | Critério | Decisão |
|---|---|---|
| **A** — protagonista visual | pódio/discursa/close próximo do principal | retrato da pessoa |
| **B** — protagonista em grupo | ao centro/segura/posa próximo do principal | retrato da pessoa |
| **C** — principal contextual | sentado/plateia/ouvinte/enquanto outro fala | **NÃO é retrato do principal** → entidade = quem discursa (`_quem_discursa`) ou tema do evento |
| **D** — secundário/fundo | desfocado/ao fundo/parcial (próximo do nome) | **bloqueia** como retrato do principal |

**Implementação:** `tier_prominencia(descricao, visiveis, principal)` + `_quem_discursa(descricao, pessoas)` em `classificar_banco_ouro_midia.py`. Lógica: varre **todas** as posições do nome do principal (lida com forma longa "luiz inácio **lula**"); sinais A/B (pódio/discursa/ao centro/segura/posa) **vencem** o contextual genérico quando a ≤60 chars do nome; "ao fundo/desfocado" só conta como D se próximo do nome (senão é cenário: "telão ao fundo"). Coluna nova `tier_prominencia` no banco.

### Resultado ao vivo (v4, rodado nos 739 registros)
- Card `8ec180fb`: entidade **Edson Fachin**, tier **C** (era Lula) ✅
- Irmã `014c2648`: entidade **Lula**, tier **B** ✅
- Distribuição: A=8, B=345, C=35, D=13 (338 sem descrição Gemini = neutro)
- **0 fotos saíram de `uso_automatico`** indevidamente (auditoria vs. backup `*_bak_priornome`).
- 54 entidades reajustadas vs. versão anterior.

### Bug travado no caminho (registrado p/ v0.2)
- `_quem_discursa` não acha o orador em todas as C → algumas viram entidade genérica ("politica", "geopolitica", "congresso") em vez de quem fala. Ex.: "Lula durante reunião com Trump" (D) mereceria revisão humana de qualquer forma. Refino p/ v0.2: fallback p/ orador por heurística de título, ou marcar como "evento_<tema>" em vez de tema cru.

### Pendência Miguel
- **v0.2** (quando quiser): melhorar o fallback do orador nas C sem `_quem_discursa` (hoje vira tema). Não afeta a decisão central (não atribuir foto contextual ao principal errado).
