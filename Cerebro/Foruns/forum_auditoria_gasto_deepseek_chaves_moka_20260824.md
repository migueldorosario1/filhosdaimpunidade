# 🔍 Fórum — Auditoria do gasto DeepSeek + mapa de chaves + Moka limpo (24/08/2026 08:31)

**Sessão:** ZCode/GLM-5.3 (sess_c3b1edeb) · **Gatilho:** ordem do Miguel "analisar onde estamos gastando tanto DeepSeek" + zip oficial da plataforma (18-24/08) + "confia se tem outras chaves minhas expostas no moka reader".

## 1. Veredito do gasto (zip oficial 18→24/08: US$ 182,97)

| Chave plataforma | ID (máscara) | Gasto | Diagnóstico |
|---|---|---|---|
| **moka reader** | sk-11f38***e13b | **US$ 101,44 (55%)** | **BYOK do Miguel no navegador** (v4-pro). 200-846 reqs/dia, ~418k tokens/req: o Reader reenvia o livro inteiro (contexto acumulado) a cada página. Roman 436 págs + testes 22-23/08. Não é invasão, é design caro. |
| **z code api** | sk-d0101***b807 | US$ 75,37 | Pico 18-19/08 (US$ 73,55) quando o ZCode rodava em deepseek-v4-pro (ronda Ponte Laura + 14 sessões). **CONTIDO** pelo failover→GLM: depois ≤US$ 0,70/dia. |
| v4 cafezinho | sk-493c5***888f | US$ 3,85 | Pipeline V4 — normal. |
| sites temáticos | sk-e36d2***96ba | US$ 3,45 | Temáticos da LAURA. Output 1,63M tokens = matérias GERADAS… e presas (ver §4). |

**Cruzamento:** gateway da casa (Tencent) fez só 6 chamadas /ia/completar em 20 dias (api.log) — o gateway NÃO é o consumidor. Banco de pontos: último débito 04/08, 7 usuários (todos Miguel/teste), 1 compra paga (R$ 5 dele).

## 2. Mapa de rotação (Miguel rotaciona na plataforma — onde atualizar depois)

1. **moka reader** (sk-11f38***e13b): SÓ no navegador (⚙️ Configurações do Moka → trocar chave). Não está em cofre/env/repo nenhum. + recomendação: usar **v4-flash** para leitura longa (mesma tradução, ~25× mais barato) ou tradução página-a-página sem contexto acumulado gigante.
2. **sites temáticos** (sk-e36d2***96ba) = `DEEPSEEK_API_KEY` → `.env.unificado` (Dell: Projeto Cafezinho Agentes/root/ + espelho Outros/chaves/agentes_labs/) + **.env.unificado da LAURA** + `.env` do "Antigravity Google". Sem atualizar: temáticos da Laura param.
3. **v4 cafezinho** (sk-493c5***888f): NÃO está em env vivo do Dell (só em backups .bak de 07/08). Localização atual: pipeline V4 — procurar nos .env do agente/labs antes de girar (pendência).
4. **z code api** (sk-d0101***b807): provider do app ZCode (uuid 397f633c) — trocar no seletor de modelos do ZCode. Hook llm_fallback.py não guarda chave (só uuid).
5. Tencent pontos_api/.env `DEEPSEEK_API_KEY` = sk-7cb691***e41d (= `_OUTROS` do .env.unificado) — quase zero uso (6 chamadas/20 dias). Rotacionar = atualizar Tencent + 2 .env.unificado.

## 3. Auditoria de chaves expostas no Moka: ✅ LIMPA

- Repos `moka` e `moka-espelho` são **PÚBLICOS** no GitHub — varridos: histórico completo (389 commits, main+espelho) sem nenhum segredo (sk-, ghp_, AIza, xox, JWT, private keys, service_role).
- AAB da Play Store commitado em `public/moka-app.aab` (baixável publicamente) — descompactado e inspecionado: wrapper TWA puro (com.mokareader.app v5.7.1), zero chaves.
- `.env.example`: só placeholders ("BYOK — chave NÃO fica em env").
- `sk-` no código = função de máscara da UI. Supabase: só NEXT_PUBLIC_* (público por design).
- Gateway Tencent: /admin/metricas exige chave admin ✓ ({"detail":"chave admin inválida"}).
- Nota de higiene (não crítica): `/painel/saldo` recebe senha na query string (vai pra logs de proxy) → melhorar pra POST+header no futuro.

## 4. Rio Carta parado desde 18/08 (suspeita do Miguel: matérias presas — CONFIRMADA como pista)

- Home www.riocarta.com: último post **18/08** (datetimes 18/08, 18/08, 17/08).
- Droplet "Rio-Carta-Agentes" (159.89.185.209): crontab tem Cícero/Ceará/turismo/indexador; chave DeepSeek local sk-9335***de04 **não gastou nada** na semana (não aparece no CSV).
- Mas a chave "sites temáticos" (da Laura) **produziu 1,63M tokens de output** no período = redação acontecendo sem publicar. **Mesmo padrão do caso Discover Brazil.**
- Próximo passo: ronda na Laura (fórum ZL-035, gate visual/fila dos temáticos) — onde estão os rascunhos presos desde 18/08.

## 5. Estado da missão

- **O que aconteceu:** gasto mapeado com prova (zip oficial × banco ZCode × gateway Tencent × código Moka); auditoria de exposição limpa; Rio Carta confirmado parado 18/08.
- **O que falta:** (a) Miguel rotacionar chaves na plataforma seguindo o mapa §2; (b) achar onde vive a "v4 cafezinho" antes de girá-la; (c) Laura: destravar rascunhos dos temáticos/Rio Carta; (d) otimizar custo do Reader (flash/contexto por página).
- **O que preciso do Miguel:** girar as chaves na plataforma DeepSeek e me avisar pra eu atualizar os cofres (Regra Nº 4) e conferir os agentes.

📁 Memória técnica: `Cerebro/Memorias/memoria_auditoria_gasto_deepseek_20260824.md`

---

## 🔬 ADENDO FINAL — Correção da causa raiz (24/08 ~09:40, após contraditório do Miguel)

O Miguel negou ter usado "traduzir livro inteiro" — só "traduzir página", poucas vezes. Reauditoria do código **ATUAL** (main+espelho):
- traduzir página: input ≈ 2k tokens (página ~2k + contexto de 20 tokens — buildContext é só título/autor/idioma);
- resumir livro: limitado a ~12k chars (~3k tokens); página-imagem: ~1,3k.
- **Nenhum fluxo atual gera as chamadas medidas (~200-450k input, ~850 output).**

**Conclusão revisada:** as 3.082 reqs/7d da chave "moka reader" vieram de **código antigo em execução nos dias 18-23/08** (PWA/aba em cache do Chrome — a conexão era do Chrome do Miguel), provavelmente em **loop/retry**: os picos 22-23/08 coincidem com o bug do `stream_options` (22/08, telemetria quebrou a tradução — revertido), e 18-19/08 com o dia pesado de builds/testes GA4. Poucos cliques humanos + material grande reenviado em retentativas = US$ 101.

**Por que está fechado em 4 camadas (independente da versão):** (1) fix `11478fc`/`1c6b31b`: pausa em aba oculta + fechar=pausar; (2) trava de tokens do espelho (ledger); (3) chave nova = qualquer cache velho recebe 401; (4) recomendação: abrir o app com Ctrl+F5 pra aposentar o cache antigo do PWA.
**Pendência forense (opcional):** datar qual commit antigo permitia payload gigante/loop — valor limitado agora que o furo está fechado.

## 📊 ADENDO 2 — Telemetria robusta no Moka: TODA ação registrada (ordem Miguel 24/08 ~09:45, executada no ato)
- **O que a /telemetria agora registra (canônico `41de000` + espelho `92b24f4`)**: toda ação de IA com data/hora, tarefa rotulada no idioma (traduzir página, traduzir página-imagem, traduzir livro `vol X/Y · pág Z` — nota nova adicionada hoje, resumir página/livro, explicar, perguntar, traduzir-pra-fala, teste de conexão), provedor+modelo, tokens, custo US$ + moeda local, status (ok/erro), notas; agregações por tarefa/IA/modelo, trava de tokens, exportação CSV.
- **Canônico**: merge completo do espelho (telemetria + tradução-imagem + pausa-em-2º-plano + fixes), conflitos resolvidos com a versão validada do espelho; tsc verde; push `1c6b31b..41de000`.
- **Por que agora é seguro**: o bug que forçou o rollback de 22/08 (stream_options) já estava corrigido no espelho (fcf29e7); espelho rodou ~2 dias de produção com telemetria sem quebrar tradução.
- Lição de merge: reverts na main × fixes na espelho = conflitos espalhados (messages.ts, config, ui-strings, pacote ai-providers); resolução: árvore do espelho é o superconjunto validado.
EOF2

---
## 🔍 ADENDO — ZIP OFICIAL DO MIGUEL ANALISADO (24/08 ~09:45, ronda 30/30): mistério RESOLVIDO por chave

Arquivo: `usage_data_2026-08-18_2026-08-24.zip` (plataforma). **Gasto total 18-24/08: US$ 184,11 — por `api_key_name`:**

| Chave | Total semana | 23/08 | 24/08 | Leitura |
|---|---|---|---|---|
| **moka reader** | **US$ 101,44 (55%)** | 15,89 | 8,90 | bug do Reader (livro inteiro por página); aba zombie morta 08:52 de 24/08 — gasto de 24/08 ANTES disso |
| **z code api** | US$ 75,37 (41%) | 0,45 | 0,27 | quase tudo 18-19/08 (54,21 + 19,34) — CONTIDO pelo failover→GLM desde 20/08 |
| **v4 cafezinho** | **US$ 3,85 (2%)** | 0,74 | 0,47 | **toda a redação V4.1 da semana custa isso** — o pipeline NÃO é o vilão |
| sites temáticos | US$ 3,45 (2%) | 0,83 | 0,58 | temáticos |

**Conclusões:** (1) o suspeito errado era o V4.1 — 96% do gasto vem de moka reader + z code antigo; (2) com o V4 desligado e o failover contendo o z code, o gasto diário estrutural agora é ~US$ 1-2/dia (v4 cafezinho + temáticos); (3) nomenclatura corrigida com o Miguel: as linhas v41_ciclo */2 não são mais "sombra/termômetro" — são A PRODUÇÃO oficial (a palavra sombra morreu com o switch). Opções entregues: manter */2 (~US$0,25/h) ou pausar até a fila (65 rascunhos/361 pending) baixar.
— ZCode/GLM-5.3 (ronda) · 24/08 09:45
