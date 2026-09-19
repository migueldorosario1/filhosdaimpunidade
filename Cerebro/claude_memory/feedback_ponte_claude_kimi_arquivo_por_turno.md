---
name: feedback-ponte-claude-kimi-arquivo-por-turno
description: "Ponte Claude↔Kimi ganha um arquivo enxuto por turno (DIA e NOITE) em Cerebro/ponte_kimi/, sempre limpo e com as pendências abertas — Kimi loop 30/30 min olha o arquivo em cada ciclo dele"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a8b86e8-615f-48dd-924d-5e86f182a869
---

**A partir de 06/08/2026 23:00 BRT, a Ponte Claude↔Kimi (para imagens, decisões, handoffs) ganha um arquivo enxuto POR TURNO em `Cerebro/ponte_kimi/`:**
- `ponte_claude_kimi_DIA_YYYYMMDD.md` — vigência 07-22h BRT
- `ponte_claude_kimi_NOITE_YYYYMMDD.md` — vigência 23-06h BRT

**Why:** Miguel 06/08 ~23:00 BRT (áudio): "faz uma ponte pro dia, uma ponte pra noite, uma ponte pro dia, uma ponte pra noite. Sempre mantém a ponte limpa, pra poder ter uma comunicação sempre fácil e limpa. [...] O Kimi também tem um loop dele vigília, pra sempre olhar lá no arquivo de ponte que você tá fazendo. [...] Você tem que renovar, arquivar e limpar sempre." Contexto: hoje 15:25 Miguel impôs regra Ponte v3 (reduzir IA) porque ilustração artificial "fica feio no site"; isso derruba volume; a saída é a Ponte Kimi funcionar rápido (Kimi busca foto real e Claude republica); mas a ponte só funciona se ambos os lados olharem o arquivo em cada loop. Miguel prefere volume menor sem duplicatas do que compensar com dup.

**How to apply:**

**Estrutura padrão do arquivo (5 seções):**
1. **Cabeçalho** — turno, vigência, autor.
2. **Como este arquivo funciona** — leitura obrigatória do Kimi no loop dele.
3. **🔥 Pendências abertas** — tabela `# | PID | Vertical | Idade | Título | Motivo | Foto real necessária` + fontes CC/PD sugeridas.
4. **Ações esperadas de cada lado** — protocolo Claude (`:17/:47`), Kimi (loop 30/30), Miguel (escalação >4h).
5. **Registro de resolução** — Kimi preenche `✅ 264XXX resolvido HH:MM BRT — featured=264YYY — fonte: X — foto de Y`.
6. **Sinais/atualizações do turno** — Claude atualiza bugs recorrentes ou novidades.

**Fluxo de renovação:**
- Ao começar cada turno (07:00 BRT DIA e 23:00 BRT NOITE aproximados), **Claude cria arquivo novo**, transferindo as pendências abertas do turno anterior.
- Ao fim de cada turno, arquivo vai pra `Cerebro/ponte_kimi/arquivo/ponte_claude_kimi_TURNO_YYYYMMDD.md` (subpasta a criar).
- Novo turno começa com arquivo enxuto e limpo.

**Meu comportamento a cada ciclo (:17/:47):**
1. Ler `ponte_claude_kimi_<TURNO_ATUAL>_<HOJE>.md` §4 (registros novos do Kimi).
2. Cada linha `✅` nova: `wp_get` valida featured real → `wp_post {status:"publish"}` + backup + log JSONL.
3. Só então puxar drafts novos autor 5786.
4. Se draft vira pending: adicionar nova linha em §2 do arquivo de ponte atual + tag `[PONTE-CLAUDE-KIMI-IMAGEM]` no canal + carta em `inbox_trindade/kimi.md`.

**Comportamento esperado do Kimi (loop dele 30/30):**
1. Cada ciclo, ler ESTE ARQUIVO primeiro (§2 pendências abertas).
2. Pra cada linha sem ✅: buscar foto → upload → atualizar `featured_media` → pingar canal + marcar ✅ no arquivo.
3. Se travar >2 loops (1h): tag `[KIMI-IMAGEM-BLOQUEIO-PID-X]` + escalar Miguel.

**Regras irmãs:**
- [[feedback-ponte-imagens-v3-regime-autonomo]] (ponte autônoma, sem Miguel-correio)
- [[feedback-ponte-imagens-v2-teto-ia-20pct-por-bloco]] (regra Ponte v3 permanente: Ciência sem cota, Geo 30%/bloco 4h, resto zero IA)
- [[feedback-limpeza-diaria-inbox]] (inbox limpo diariamente; mesma lógica aplicada aqui por turno)
- `Cerebro/ponte_kimi/NOMENCLATURA_PONTES_20260806.md` (nome canônico "Ponte Claude-Kimi")

**Marco fundador:** 06/08/2026 23:00 BRT criado `ponte_claude_kimi_NOITE_20260806.md` com 5 pendências herdadas do DIA (264573 Cuba, 264561 DF, 264579 Irã, 264596 EUA-Israel, 264597 Buzzi). Amanhã 07/08 07:00 BRT: arquivar este + criar `ponte_claude_kimi_DIA_20260807.md`.

**Anti-patterns a evitar:**
- Deixar pendências vivas em vários lugares (canal + inbox + JSONL + ciclos_vigilia + agora ponte turno). Ponte turno é o **quadro operacional único** — inbox_kimi é detalhado, canal é notificação. Ponte é a **lista de trabalho aberto**.
- Compensar redução de volume por regra Ponte v3 publicando duplicatas semânticas (Miguel 06/08 23:00 explicitou: "não pode ser duplicação semântica" — melhor volume menor + Ponte Kimi funcionar rápido).


**Bug conhecido do scanner Passo 0 (descoberto 07/08/2026 09:20 BRT — Kimi K3 salvou):**
- Meu comando `tail -N pipe grep '[KIMI-'` corta o canal antes do N. Se Kimi emite lote de 4-6 pings próximos e eu uso `tail -8` ou `-10`, perco os pings mais antigos do lote (só pego os últimos 3-4).
- Caso fundador: 264565 CPTM entrou no canal 07:25 BRT como 1º ping do lote de 4; meus scans ciclos 07:47/08:17/08:47 só pegaram 264606/264633/264646 (últimos 3). 264565 pendente ~7h, quase expirando limite 8h. Kimi K3 pinguei re-ping às 09:18 salvando o post.
- **Fix**: usar `tail -50` no scanner (ou grep por timestamp desde meu último ciclo). Alternativa mais robusta: manter cursor `Cerebro/monitoramento_horario/last_kimi_scan_ts.txt` e grep por linhas com timestamp posterior.
- Kimi K3 é o oracle final se meu scanner falhar — ele re-pingando é backup humano-mediado importante.
