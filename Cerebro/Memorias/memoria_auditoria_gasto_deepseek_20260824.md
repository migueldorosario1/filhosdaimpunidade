# 🧠 Memória — Auditoria do gasto DeepSeek (24/08/2026, ZCode/GLM-5.3 sess_c3b1edeb)

Log técnico completo do fórum `Foruns/forum_auditoria_gasto_deepseek_chaves_moka_20260824.md`. Fatos verificáveis:

## Fontes provadas
- **Zip oficial da plataforma** (Downloads/Antigravity Google/Outros/Gastos IA/Deepseek/usage_data_2026-08-18_2026-08-24.zip) → CSVs `cost-*` e `amount-*` (por api_key_name). Total 18-24/08: **US$ 182,97**.
- **Banco do ZCode** (`~/.zcode/cli/db/db.sqlite`, tabela `model_usage`): 7 dias → DeepSeek 801,8M input (741,9M cache_read), 2,56M output; GLM 608M; Kimi 293M; Qwen 123M. Pico DeepSeek 18-19/08 (702+453 reqs) = época em que ronda Ponte Laura (automation-ed29f85f, cron `50 */6`, sess_a3d75442) rodava em deepseek-v4-pro. Depois do failover→GLM o ZCode caiu pra ≤9 reqs/dia.
- **Gateway Tencent** (`/home/ubuntu/moka/pontos_api/`): api.log = 6 POSTs /ia/completar desde 04/08; moka_pontos.db: 7 usuários (todos Miguel/teste), 10 débitos, último 04/08; rewrite Vercel `/api/pontos/:path*` → `https://43.156.151.165.sslip.io/:path*` (vercel.json).
- **Código Moka** (`~/ZCodeProject/moka-app`): BYOK — chave só no localStorage do navegador; /api/proxy só repassa (allowlist de hosts); gatewayProvider só quando não há BYOK.

## Mapa de chaves (máscara sk-prefixo***sufixo)
| Plataforma | ID | Onde vive |
|---|---|---|
| moka reader | sk-11f38***e13b | **SÓ navegador do Miguel** (BYOK, v4-pro). Maior gasto: US$ 101,44 |
| z code api | sk-d0101***b807 | app ZCode (provider uuid 397f633c) |
| sites temáticos | sk-e36d2***96ba | `DEEPSEEK_API_KEY` do `.env.unificado` (Dell 2 vias + Laura) + `.env` Antigravity Google |
| v4 cafezinho | sk-493c5***888f | **não está em env vivo do Dell** (só baks 07/08) — pipeline V4, localizar antes de girar |
| (sem nome no CSV) | sk-7cb691***e41d | Tencent pontos_api/.env + `DEEPSEEK_API_KEY_OUTROS` |
| (sem gasto no período) | sk-9335***de04 | droplet Rio-Carta-Agentes (chaves_{ceara,gsn,cicero}.env) |
| (sem gasto no período) | sk-ab79ae***412a | `DEEPSEEK_API_KEY_CLAUDE` .env.unificado |

## Auditoria de exposição no Moka: LIMPA
- Repos públicos: migueldorosario1/{moka, moka-espelho} (`private:false`).
- `git grep` em `git rev-list --all` (389 commits, main+espelho): zero matches de sk-{16+}, ghp_, AIza, xox, sk-proj, BEGIN PRIVATE KEY, eyJ{20+}, service_role.
- AAB `apps/web/public/moka-app.aab` (commit 4cd5f94, 1,5MB, baixável): unzip + strings → wrapper TWA com.mokareader.app v5.7.1, zero segredos.
- .env.example: explícito "chave NÃO fica em env"; sk- no código = função de máscara; Supabase só NEXT_PUBLIC_*.
- Gateway: /admin/metricas → 401 "chave admin inválida" sem chave ✓. Higiene futura: /painel/saldo manda senha na query string.

## Rio Carta
- Home www.riocarta.com: últimos posts 18/08 (confirmado ao vivo 24/08 08:2x).
- Droplet 159.89.185.209 (hostname "Rio-Carta-Agentes"): agentes Cícero/Ceará/GSN/turismo/trilhos; crontab ativo (cicero_cron_rotativo, remote_publish, indexador). Chave local sk-9335 não gastou na semana.
- Chave "sites temáticos" (Laura): output 1,63M tokens no período → produção existindo, publicação não. Caso Discover Brazil. Próximo: ronda Laura (ZL-035, gate/fila temáticos).

## Por página do Reader custa caro
~418k tokens input cacheado/req (média 1,29B cache_hit / 3.082 reqs). Tradução com contexto acumulado = livro inteiro reenviado a cada página. Mitigações: v4-flash na leitura comum (~25× mais barato), contexto por capítulo, ou página-a-página puro.
