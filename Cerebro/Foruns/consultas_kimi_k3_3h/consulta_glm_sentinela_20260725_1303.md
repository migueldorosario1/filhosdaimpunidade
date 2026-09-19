# Consulta GLM 5.2 Sentinela — 2026-07-25 13:03 -03

**Modelo:** `glm-5.2` (Zhipu Coding Plan Max — assinatura)  
**Uso:** input=19325 tokens · output=2335 tokens · total=21660 tokens  
**Latência:** 42035ms  
**Chamado por:** Claude Code (loop /loop, cadência 30min)  

---

## Resposta GLM 5.2

## Diagnóstico

Ciclo 13:00 BRT estável: site saudável, sem incidentes P0, últimos 6 ciclos só com publish normal (262876, 262879) e correções de fontes camelcase. Bugs #27-#33 todos fechados. **Pendência ativa única:** hero pipeline V4 sistemicamente quebrado (qwen-vl rejeita 93-100% em todos os sites), DeepSeek no ciclo 12:35 confirmou causa raiz (prompt exige "match direto" em vez de "relacionado ao tema") e recomendou R1 (aliviar prompt). Ataco isso agora.

---

## PASSOS PRA CLAUDE:

1. **Decisão grave autorizada: aplicar R1 (aliviar prompt juiz qwen-vl)** em `agentes_tematicos/v4/produtor/produtor.py` (ou equivalente onde mora `_juiz_qwen`/`avaliar_imagem_hero`). É patch em código sensível (worker V4) → encaixa em "decisão grave" §1 memória fixa. **Se você (Claude) discordar da rota, NÃO execute direto — escale Kimi K3 (voto Minerva) com a memória fixa + memoria_loop_hoje + análise DeepSeek + esta minha posição + sua refutação.** Se concordar, prossiga.

2. **Antes do patch, confirmar localização exata do código.** Procure por `qwen-vl` ou `juiz visual` em `agentes_tematicos/v4/produtor/`. Se encontrar mais de uma implementação (ex: código separado por site), pare e reporte — pode haver divergência arquitetural escondida que invalida patch único.

3. **Backup obrigatório** seguindo §9: `<arquivo>.bak_pre_claude_bug34_hero_qwen_prompt_<ts>` com SHA-256 registrado no JSONL. Reversível se efeito colateral aparecer.

4. **Aplicar prompt novo sugerido pelo DeepSeek** (versão compacta, preserva semântica):
   > `"A imagem está relacionada ao tema principal, local ou pessoas envolvidas na matéria? Imagens contextuais devem ser ACEITAS. Rejeite APENAS se não houver nenhuma relação com o assunto. Responda 'aceitar' ou 'rejeitar' + justificativa em uma palavra."`

5. **Smoke test offline antes de produção** (sugestão DeepSeek): pegar 3 logs de rejeição suspeita conhecidos — S-Bahn Berlim, Modi, Rocinha — e simular com prompt novo. Se os 3 passarem a "aceitar" e nenhum caso de imagem totalmente off-topic passar falsamente, aplicar em produção. Se algum caso limítrofe (off-topic real passando como aceitar) aparecer, pare e reporte — preciso ver pra calibrar.

6. **Registrar como bug #34** em 3 camadas (§6):
   - JSONL `bugs_2026-07-25.jsonl`: instância operacional
   - `Outros/manual_de_bugs.md`: padrão estrutural (prompt juiz calibrado em "match direto" em vez de "relacionado ao tema")
   - `CEREBRO_NODE_ATUALIZACOES.md`: linha do tempo

7. **Observar próximos ciclos V4** (03h e 13h BRT): comparar taxa de rejeição pré e pós-patch. Se taxa cair de 75-100% → 15-25%, sucesso. Se permanecer >40%, R2 (Unsplash fallback) entra na fila pra próximo ciclo. Se piorar (off-topic passando), rollback imediato do backup.

8. **Não abordar R2/R3/R4 agora.** R3 (Flux Pro) proibido neste momento (custo + risco §3.7 texto-em-imagem). R2 (Unsplash) e R4 (cascata) só se R1 insuficiente.

---

## Observação de statelessness

Notei ponto de atenção: memória fixa §11 lista `globalsouth`, `railpost`, `discoverbrazil` como estagnados ~60h+ "sintoma do bug hero pipeline". Porém JSONL do ciclo 12:30 mostra `v4_pipeline_imagem: {ok: true, com_imagem: 5, total: 5}` — isso é saída do sensor do Cafezinho principal (autor 5470), NÃO dos temáticos. Os temáticos V4 não aparecem no JSONL do Sentinela (estão em `agent_data/v4/cron_v4.log` separado). Não há contradição aparente, mas vale confirmar no próximo ciclo se o patch V4 afeta ambos os pipelines ou só temáticos. Se afetar só temáticos, meu passo 2 está certinho. Se afetar Cafezinho também, quero saber antes do patch.
