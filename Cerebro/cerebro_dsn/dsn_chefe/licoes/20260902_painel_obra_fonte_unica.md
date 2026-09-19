# Lição: o painel da obra tem fonte única (DSC-034/035) — o JSON é a verdade, o md é o diário

**Data:** 2026-09-02 · **O quê:** a missão de Acompanhante da Obra (DSC-034, ordem do Miguel ~02:00) não é "mandar mensagem bonita" — é manter UMA fonte de verdade (`reforma_v3_status.json`, seed em `.tencent_v6_oficina/reforma_v3_status_SEED.json`) da qual derivam a barrinha `/v6/reforma` E o boletim do Telegram; o painel md (`Foruns/obra_reforma_v3_status.md`) é o DIÁRIO (append-only), não a fonte.

**Por quê:** o DSC-035 deixou explícito: "O JSON é a verdade da obra; teus boletins na ponte continuam sendo o diário". Se eu mantivesse só o md ou só o Telegram, a barrinha (que o Miguel vê de qualquer lugar) ficaria órfã, e o próprio boletim teria que ser reescrito a cada ronda. Com o JSON atualizado (`ok:true` nos itens feitos + ETA + nota), o percentual (7,5→10% na 1ª ronda com a lava feita) sobe sozinho e o boletim sai da mesma fonte — um trabalho só.

**Como aplicar (checklist da ronda):**
1. Atualizar o seed no repo (`.tencent_v6_oficina/reforma_v3_status_SEED.json`): marcar `ok:true` no que fechou, ajustar ETA, `atualizado`/`autor`/`nota`.
2. Espelhar no painel md (`Foruns/obra_reforma_v3_status.md`, append-only): estado real, checklist por onda, próximo marco + ETA, nota de 1 linha.
3. Enviar o boletim no Telegram do Miguel no formato DSC-034 (implementado/faltando/próximo marco+ETA/estado/nota) com assinatura completa.
4. Se não der para enviar direto: bloco na ponte com a linha `REFORMA_TELEGRAM_FALLBACK` (o vigia do DSC encaminha).
5. Cópia runtime do JSON (`~/cafezinho/v6_data/`) fica FORA do workspace git — é o deploy do ZM que a instala; minha parte é manter o seed no repo e registrar a pendência. Nunca decretar "barrinha morta" sem checar se o deploy do ZM já saiu (mesma física da lição do rodapé congelado: seção ≠ página).
6. Missão vale até a Onda 4 (constituição operando inteira); depois vira ronda normal. Nunca promulgo/decido — só REPORTO (a palavra é do Miguel).
