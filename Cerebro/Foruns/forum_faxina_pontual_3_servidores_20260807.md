# 🧹 FAXINA PONTUAL AUTORIZADA — 3 SERVIDORES (07/08/2026)

**Status:** ✅ EXECUTADA E VERIFICADA (rio-ag + NYC concluídos; Tencent upload em curso)
**Autorização:** Miguel, por voz, 07/08 ~12h: *"Autorizo a faxina pontual imediata nos três servidores, desde que seja tudo indexado, e que você mantenha o Cérebro atualizado sobre isso... Pode seguir então. Pode aplicar o que eu já autorizei aí."*
**Executor:** ZCode (Kimi K3) — conversa Vigília/Varredura/Faxina
**Memória técnica completa:** [memoria_faxina_pontual_3_servidores_20260807.md](../Memorias/memoria_faxina_pontual_3_servidores_20260807.md)
**Manifestos de indexação (prova):** `Cerebro/Memorias/faxina_20260807/MANIFESTO_FAXINA_{rio-ag,nyc}.jsonl` (+ Tencent quando fechar)

## Regra de ouro aplicada (nada foi apagado sem prova)
**indexar → copiar p/ B2 → verificar (byte-size e/ou contagem de arquivos) → só então apagar local.** Caches regeneráveis (pip/npm/puppeteer) foram direto ao chão, mas indexados no manifesto.

## Decisões do Miguel aplicadas nesta faxina
| Decisão | Aplicação |
|---|---|
| Bucket `failover-cafezinho1` | ✅ destino único; convenção `faxina/<servidor>/<classe>/<aaaa-mm>/` |
| "desde que tudo indexado" | ✅ `MANIFESTO_FAXINA.jsonl` em cada servidor + espelho no Cérebro |
| Retenção aprovada | ✅ nada retocado na política (só limpeza pontual) |
| git gc aprovado | ✅ feito nos 3 repositórios do rio-ag (packs já eficientes — ganho de poucos MB; o grosso veio de npm/logs) |
| Zumbis | ⏸️ ficha pronta (ver abaixo), decisão do Miguel depois |

## Resultados
| Servidor | Antes | Depois | O que saiu |
|---|---|---|---|
| **rio-ag** (159.89.185.209) | 87% 🟠 | **83%** | npm cache −862MB; audit ceara 214MB→B2+truncate; git gc ×3 |
| **NYC** (198.199.121.136) | 79% | **61%** 🎉 | pip 4,4G + puppeteer 655M (caches); backups/ 1,6G→B2; logs ativos truncados (rotas_llm 167M + 4×robo_coleta); 815 `briefing used_*`→B2; `.bak`>7d→B2; `gsn_remote` morto 1,9G→B2 |
| **Tencent** (43.156.151.165) | 64% | (upload 9,2G em curso) | `/root/backups` jun/26 → `faxina/tencent/backups-locais/2026-08/`; apaga só após verificação |

## O que é "git gc" (Miguel perguntou)
Compacta o histórico interno do git (reagrupa os "packs" e remove objetos órfãos) **sem perder nada** do repositório — é manutenção de rotina. Nos 3 repositórios do rio-ag os packs já estavam eficientes, por isso o ganho foi pequeno.

## Ficha dos zumbis (ATUALIZADA 07/08 ~15:40 após questionamento do Miguel)
Nenhum dos dois é droplet em uso. Droplets em uso hoje (lista do painel colada pelo Miguel 07/08): `198.199.121.136` Cafezinho-failover-vigia, `159.89.185.209` Rio-Carta-Agentes, `142.93.48.252` gsn-youtube-nyc-01 (utilitário), `159.65.177.60` cafezinho-news-espelho.
| IP | Identidade | Estado real (07/08) | Ação |
|---|---|---|---|
| `174.138.36.31` | `riocarta-wordpress` (WP legado) | ✅ **JÁ DESTRUÍDO — fora da fatura.** O próprio print do painel do Miguel em 06/08 já confirmava "não consta mais na conta". Minha ficha original estava desatualizada neste ponto (errata). | nenhuma — resolvido |
| `159.89.237.100` | GSN WordPress | 👻 **VIVO E PAGANDO (~US$6/mês).** Print do painel de 06/08 o mostrava como o **5º droplet da conta ATUAL** (não está na conta legacy). Testes 07/08: ping 0% perda, porta SSH 22 ABERTA (estava fechada em 06/08), HTTP sem resposta, nenhuma chave nossa acessa. **Não aparece na lista de 4 do Miguel provavelmente por filtro de PROJETO no painel** — procurar em "All Projects"/buscar pelo IP. | Miguel: encontrar no painel (todos os projetos) e destruir — GSN hoje é Vercel + agente YouTube no droplet utilitário; este WP não faz nada |

Obs.: o `DIGITALOCEAN_TOKEN` do cofre local morreu (API responde Unauthorized) — por isso a confirmação foi via painel/testes de rede, não via API. Token morto descartado conforme Regra Nº 4/§117 (backup `.bak_pre_token_do_morto_20260807`); gerar token novo (read) quando quiser monitoramento de fatura por API.

**CHECKPOINT ~16:00 (crédito Kimi K3 esgotou — sessão segue no Qwen Token Plan após `continue`):** Miguel não encontra `159.89.237.100` em lugar nenhum do painel e suspeitou de confusão com o droplet GSN em uso — **não é confusão**: o em uso é `gsn-youtube-nyc-01` = `142.93.48.252` (IP diferente). Busca ampla nos cofres locais/espelhos: **nenhuma chave API DigitalOcean viva existe** (a única era o token morto já descartado c/ backup). Próximos passos: (a) Miguel gera token read-only no painel (API → Tokens/Keys) → listar droplets de TODOS os projetos via API e bater o martelo; ou (b) buscar "All Projects"/IP no painel. O IP segue respondendo ping+porta 22, então o droplet existe em algum lugar da conta (filtro de projeto continua sendo a hipótese mais provável).

## Pendências
1. Tencent: conferir fim do upload (nohup, log `/root/faxina_20260807/upload_b2.log`), verificar contagem/bytes, apagar local, manifesto.
2. `faxina_continua.py` (agente autônomo) — plano entregue no Tema Duplo `*_plano_faxina_continua_droplets_20260807`, construção ainda não autorizada.
3. Decisão do Miguel sobre os 2 zumbis acima.
