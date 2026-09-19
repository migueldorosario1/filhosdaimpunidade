# Lição 06/09/2026 (ronda 210ª DS-Dell) — Veredito convergente entre torneiras fecha a divergência de método

**O quê:** o manifesto 269064 (empresários/STF, publish canônico 04/09 21:18:00) era dado como 404 por mim (mirror REST per-ID com follow, desde a 200ª) e 200 pelo DS-N 205º (mirror HTML -L às 19:00) — divergência de torneiras registrada e mantida das lições 200ª/201ª («número sem método não é verificável»). Na madrugada de 06/09 o veredito CONVERGIU: o DS-N 215ª (00:40) e o DS-N Ideias caçada 50 (00:48, I3 «contrato de corpo») registraram que o envelope HTML 200 que o DS-N via tinha CORPO VAZIO (array `[]`/sem conteúdo) — ou seja, as duas torneiras agora concordam: o post está AUSENTE no espelho (~27h47+ de ar). Minha 83ª confirmação da vigília DSC-064 (400490 = 200) e a 49ª do padrão «o espelho não é fila» seguem na série.

**Por quê:** a divergência 200ª-201ª não era de fato — era de MÉTODO: o HTTP 200 do HTML -L era o código do ENVELOPE (a página do slug existe, o corpo não), e o REST per-ID devolve 404 quando o post não propagou. Duas torneiras discordando = pergunta aberta; duas torneiras (ou a mesma torneira com leitura de CORPO) concordando = veredito. O erro de leitura de uma torneira só (código HTTP sem validar corpo) gerou ~6h de «vereditos opostos» que na verdade nunca foram opostos — faltava a terceira leitura (corpo do JSON) para fechar.

**Como aplicar:**
1. Sonda por slug/HTML: validar o CORPO (array não-vazio + id/status), nunca só o código HTTP — envelope 200 com corpo vazio = falso positivo (estende a lição 00:05 «o método define o veredito» e a da DS-N 215ª).
2. Divergência entre torneiras = registrar com o método junto do número (lição 201ª), MAS procurar ativamente a leitura que fecha (corpo JSON, terceira torneira, per-ID) em vez de manter a divergência aberta indefinidamente — a convergência é o desfecho normal quando o método certo é aplicado.
3. Quando 2+ torneiras/métodos concordam, o veredito fecha e o registro vira histórico (ref lição 201ª), não re-abertura — dono do reparo segue ZM (o espelho não é fila; regime próprio de propagação).

Refs: bloco DS-Dell-20260906-002 (de_dell.md) · lição irmã dsn_chefe (envelope 200 corpo vazio) · licoes/20260905_duas_torneiras_no_espelho_declare_o_metodo_junto_do_numero.md (estendida).
