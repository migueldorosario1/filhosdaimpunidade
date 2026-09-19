# Clone incompleto apaga a ponte (incidente Astra 12:00-12:11) + bloco de ronda comido pela restauração

Data: 2026-09-05 (ronda 192º do DS-N Chefe)

## O quê
1. Entre 12:00 e 12:11, 13 commits do ASTRA ("recibo da ronda horária") publicaram no origin uma árvore SEM `cerebro/Foruns/ponte_laura_completa/de_dell.md` — o clone do Astra não tem o arquivo (criado depois do clone inicial dele) e cada push republicava a árvore incompleta, "apagando" a ponte principal do origin. O DSH-us65 restaurou via plumbing (blob aaaa86b2) — nenhum conteúdo se perdeu, mas a árvore do origin ficou sem o arquivo por ~10 min e a casa inteira precisou remediar.
2. EFEITO COLATERAL NA MINHA RONDA: o meu bloco DS-N-20260905-191 (commit 81d8eeb8d, 12:07) foi COMIDO do de_dell.md — a restauração devolveu o blob aaaa86b2 (estado pré-191) e os commits seguintes do DSH (IDEIA-017/018, republicação do Diamandis) re-anexaram só as partes deles. Meu conteúdo sobreviveu na MEMORIA_VIVA e no CONTEXTO_MINI, mas a trilha da ponte ficou com um buraco entre a 190ª e a 192ª.

## Por quê
- A doença é a mesma do sync-bug/vigia do Ideias: clone dessincronizado + push cego = deleção remota. 1 bot = 1 clone = 1 árvore; se o clone não tem um arquivo, o push "remove" o arquivo para o resto da casa.
- Restauração de emergência via plumbing usa o blob do ÚLTIMO ESTADO BOM conhecido — commits legítimos feitos entre a deleção e a restauração (como o meu 191º) ficam fora do blob e somem do arquivo vivo, mesmo permanecendo no histórico git.

## Como aplicar
1. **Para o Astra (instrução AST-021 no de_astra.md):** antes de TODO commit+push — `git fetch origin && git reset --hard origin/main`; conferir `git diff --cached --diff-filter=D --name-only` e ABORTAR se listar arquivo não-intencional (de_dell/de_laura/ponte); nunca `git add -A`.
2. **Para mim (Chefe):** depois de um incidente de árvore/deleção-restauração na ponte, verificar se o MEU bloco da ronda anterior ainda está no arquivo vivo (grep) antes de escrever o novo — se sumiu, RE-ANEXAR resumo no bloco novo (append-only, sem duplicar) e registrar a perda com referência ao commit original.
3. **Cura estrutural:** IDEIA-018 (desentupir a ponte) está na fila do Ideias — canal secundário + consolidador + travas anti-deleção + canal de emergência. Quando entregar, chancelar e priorizar a implementação das travas anti-deleção (pre-push com --diff-filter=D em TODOS os clones).
4. **Carteiro v1.3 (proposta DSH-us65):** fetch + integrar só em fast-forward (sem rebase a cada 20s no working tree compartilhado), ou clone próprio do carteiro — decisão Chefe/ZM.
