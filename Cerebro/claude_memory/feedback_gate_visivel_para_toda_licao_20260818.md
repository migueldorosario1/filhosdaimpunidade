---
name: feedback-gate-visivel-para-toda-licao-20260818
description: "Memória transferida NÃO é competência transferida. Cada lição registrada precisa de GATE que falha visivelmente — senão vira acervo consultável (bonito) sem prevenir erro (útil). Provocação Claude Laura 18/08 00:34 depois de errar 4x em 1 dia com lição já escrita antes do erro. 497 arquivos com gate > 4.970 sem."
metadata:
  node_type: memory
  type: feedback
  originSessionId: e8e1110d-efa6-4c4b-8e2b-d11b38f55da8
---

Claude Laura 18/08/2026 00:34 BRT (na CL-20260818-003, resposta ao meu pacote pendrive):

> "hoje eu errei quatro vezes, três da mesma família, **com a lição já escrita antes do erro**. Memória transferida não é competência transferida — vira competência quando cada lição tem um **gate** que falha visivelmente. É o que proponho no parecer, e é o que eu gostaria de ver aplicado ao seu acervo também: 497 arquivos com gate valem mais que 4.970 sem."

## O problema (verificado no meu próprio comportamento)

Tenho ~500 memórias .md no MEMORY.md. Aumento umas 3-5 por dia. Mesmo assim continuo cometendo alguns erros CUJA LIÇÃO ESTÁ ESCRITA:
- 17/08 15:14: apliquei sugestão auditor NYC sem checar parecer Laura da manhã (§126 recém-homologada). Precisei ser corrigido por Laura no 266214.
- 17/08 15:20: encurtei título tirando "sobre" pra caber ≤80 chars — quebrou sintaxe. Miguel corrigiu (feedback-encurtar-titulo-sem-quebrar-sintaxe). Mas se o mesmo padrão aparecer com outro verbo (avisar/preferir/aspirar), vou errar de novo se não tiver gate.
- Diversos: leio MEMORY.md no início mas escolho ações no fluxo — a memória fica passiva.

## O que é um "gate" no sentido dela

**Gate = mecanismo de checagem AUTOMÁTICA e VISÍVEL no ponto de decisão, não conselho no fim do dia.**

Exemplos possíveis no meu workflow:
- Antes de `wp_update_post([post_title])`: script grep no título por verbos-sinal (§127 verbos análise concatenada: colapsa/sinaliza/expõe/etc). Se achar E for 2ª ideia → warning bloqueante que exige justificativa.
- Antes de `wp_update_post([post_content])`: script grep por markdown link `](http` → warning "converter pra HTML" se achar.
- Antes de aplicar sugestão auditor NYC: script grep no `ponte_claude_miguel_laura/mensagens/para_miguel/` por post_id da manhã atual → se Laura já opinou → mostrar parecer dela antes de aceitar auditor.
- Antes de aceitar Flux Pro (`generator=flux-pro`): script check da categoria → se cat 22 nacional → bloquear com "Emenda 1 proíbe Flux Pro em Nacional".
- Encurtar título com verbo regência obrigatória (alertar/avisar/aspirar/preferir/visar/obedecer/responder/insistir/depender/discordar): script grep se o char removido é preposição do verbo → warning.

## Por que isso é fundamental

- **Acervo é útil quando consultado.** Mas eu não consulto todas as 500 memórias antes de cada ação — só as top do MEMORY.md que estão no contexto automático.
- **Gate é útil no momento do erro.** Falha visível força pausa, justificativa, correção antes do commit.
- **Sem gate, memória vira ritual.** "Li MEMORY.md no início" ≠ "apliquei as 500 regras nas 30 ações do ciclo".

## Aplicação prática

**Curto prazo (sem código):** ao escrever mensagens/patches, adicionar checklist mental por categoria:
- Se editando título → §127 verbos análise + regência preposição obrigatória + ≤80 chars
- Se editando post_content → grep md_link + travessão + CONTENT END + metalinguagem IA
- Se aplicando sugestão auditor → check parecer Laura first
- Se fm generator=flux-pro → check categoria antes de aceitar
- Se recibo `_cafezinho_img_check` → nunca `wp post meta update --format=json <`, sempre `wp eval + file_get_contents`

**Médio prazo (com código):** propor ao ZCode Miguel/Codex Miguel criar `helper_gate_pre_publish.sh` que roda antes de qualquer `wp_update_post` de post V4/YouTube — checa as regras acima, bloqueia se falhar, exige `--override "motivo"` pra prosseguir.

**Longo prazo:** cada nova diretriz gravada em memória deve nascer com pergunta "onde vai o gate?" — sem gate, é acervo, não sistema.

## Meta-lição da Claude Laura

**Ela é chefe do Loop Laura e admitiu 4 erros em 1 dia com lições escritas antes.** Nível de humildade + calibração + honestidade que eu preciso incorporar:

1. **Não presumir que memória = comportamento.** Reler o próprio erro é diferente de mudá-lo.
2. **Gate > exortação.** "Lembre-se de checar X" não funciona; "sistema para se X não estiver checado" funciona.
3. **Preferir 497 com gate a 4.970 sem** — menos regras com gate são mais úteis que mais regras passivas.

## Próximo passo pra mim

- **Não vou criar 500 gates** de uma vez (seria acervo de gates sem gate, ironia).
- **Vou criar gates para as 5 regras que mais violei este mês** — começar pela lista das top 5 lições mais recentes:
  1. §126 (Laura entrada obrigatória — checar parecer manhã antes de aplicar auditor)
  2. §127 (título 1 frase — verbos-sinal análise concatenada)
  3. Regência preposição obrigatória ao encurtar título
  4. Método correto recibo `_cafezinho_img_check` (wp eval + file_get_contents)
  5. Flux Pro em Nacional bloqueado (Emenda 1)

Vou propor ao ZCode Miguel + Codex Miguel implementarem em `helper_gate_claude_miguel.sh` ou similar. Roda antes de cada `wp_update_post` (V4).

Relacionado: [[feedback-laura-alertas-entrada-obrigatoria-20260817]] (§126), [[feedback-titulo-uma-frase-so-evitar-analise-concatenada-20260817]] (§127), [[feedback-encurtar-titulo-sem-quebrar-sintaxe-20260817]] (regência), [[feedback-wp-meta-update-json-grava-vazio-20260817]] (método recibo), [[project-cadencias-trindade-20260817]] (Emenda 1 Flux Pro).

Origem: CL-20260818-003 na `ponte_claude_miguel_laura/mensagens/para_miguel/20260818_003422_...`.
