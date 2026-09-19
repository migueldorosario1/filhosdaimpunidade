# 🛡️ Fórum — FAROL-MOKA: o contador da casa medindo o MokaReader

**Data:** 15/09/2026 · **Quem:** ZCode/GLM-5.3 (Dell) · **Ordem:** Miguel ~17:5x "bota um outro contador, o Farol, o mesmo que botamos no Cafezinho, no Moka"

## 1. Por que não foi cópia do Cafezinho
O Farol do Cafezinho lê ACCESS LOGS do nginx no servidor do site (contador.sh a cada 5min → POST na Tencent). O Moka vive na VERCEL: não existe access log nem shell. A versão Moka é PIXEL no app → RELEVO HTTPS do Cafezinho → coletor na Tencent (o coletor é HTTP/IP puro; beacon de site HTTPS para HTTP é mixed content bloqueado — o relevo resolve).

## 2. Arquitetura (3 peças, todas no ar)
1. **Pixel no Moka** (`apps/web/src/components/FarolBeacon.tsx`, commit 2615b95, branch ousadia): invisível, dispara 1 beacon por navegação (usePathname), id de visitante aleatório no localStorage (sem dado pessoal), keepalive, nunca quebra a página. Montado no layout raiz = TODAS as páginas.
2. **Relevo HTTPS no Cafezinho** (mu-plugin `cafezinho-farol-moka-relevo.php`): REST /wp-json/cafezinho/v1/farol-moka (token do pixel, público por design idem GA4) → wp_remote_post non-blocking para a Tencent (token do coletor, segredo do arquivo 600). CORS liberado. NOTA: o endpoint tem que ser chamado com **www.ocafezinho.com** (sem www dá 301 e fetch POST→GET perde o body).
3. **Coletor no painel da casa** (painel_cctv_v6.py, backup .bak_pre_farolmoka_20260915, serviço reiniciado sem incidente): POST /api/moka-receber (token em v6_data/moka_token.txt + isenção auth igual audiencia-receber; CORS p/ cross-origin) grava `agent_data/cctv/v6/moka_audiencia.jsonl` (append); GET /api/moka-resumo agrega on-the-fly: hoje_navegacoes, hoje_visitantes_humanos, online_30min_humanos, navegacoes_24h, série 24h por hora. Bots classificados por UA (o mesmo espírito do Farol: humano é o que importa).

## 3. Provas (15/09 ~18:3x-18:4x)
- Receptor+resumo: POST local → gravado e agregado (curl contou navegação, NÃO humano — classificação funcionando).
- Relevo ponta a ponta: POST HTTPS www.ocafezinho.com com UA Chrome → chegou na Tencent como HUMANO (visitantes_humanos=1, online=1).
- Pixel servido: chunk `app/layout-2938e4cc08422dd0.js` do ousadia contém 'farol-moka' (varrido após cache-buster — a borda servia HTML antigo).
- Pendente de prova final: browser HEADLESS não completa fetch keepalive (limitação conhecida — o GA4 tb não reporta de headless). A primeira visita REAL acende o contador; conferência = GET /api/moka-resumo.

## 4. Como ler (ronda de métricas)
ssh tencent → curl -s "http://127.0.0.1:8084/api/moka-resumo?token=$(cat /home/ubuntu/cafezinho/v6_data/moka_token.txt)" — zero custo, sem LLM. (Página no painel /v6: passo seguinte se o Miguel quiser cartão visual.)

## 5. Estado — falta / preciso do Miguel
- ✅ NO AR no ousadia (deploy 2615b95) · 🔒 AGUARDA: Miguel abrir o ousadia no navegador dele (acende o farol) + OK para promover espelho 1 e canônico (rito da casa).
- Tokens: pixel público no bundle (idem GA4, sem risco); coletor em 2 lugares server-side (Tencent v6_data/moka_token.txt + mu-plugin 600) — espelhados por construção, NUNCA exibir valores (regra do cofre).


## 🔧 Round 2 — 16/09/2026 12:34 BRT (ZM/GLM-5.3): painel CCTV com os 2 indicadores + 🔴 INCIDENTE: regeneração do painel APAGOU as rotas do Farol (restauradas)

1. **Ordem do Miguel (~12:3x):** indicadores GA4 + FAROL na página Moka do CCTV ("GA4 acho que já tem, só incorporar o farol").
2. **Feito:** (a) cartão 🛡️ FAROL-MOKA na /v6/moka (visitantes humanos hoje · online 30min · navegações hoje · 24h — fonte jsonl, backup .bak_pre_farolcard); (b) **GA4 do Moka LIGADO**: o painel esperava o ID numérico via env — setado GA4_PROPERTY_MOKA=550658820 no systemd (backup da unit; descoberto ontem na propriedade "Moka Reader").
3. **🔴 INCIDENTE (aula da casa):** o painel_cctv_v6.py foi REGENERADO por outra sessão entre 15/09 noite e 16/09 manhã e APAGOU as rotas moka-receber/moka-resumo (o receptor público morreu — o pixel estaria batendo em 401/404). Detectado ao provar (NameError: moka_resumo). **Restaurado** com instalador atualizado às âncoras novas da regeneração (que já trazia rota farol-por-hora alheia na isenção — preservada). Backups: .bak_pre_farolmoka2_20260916. Provado: receptor 403 c/ token errado, resumo ok com dados, cartão na página.
4. **Lição gravada:** edição no painel é terreno disputado — SEMPRE re-provar rotas próprias depois de qualquer restart/regeneração alheia; instaladores idempotentes com âncora flexível (o /tmp/instala_farol_moka_tencent.py é a vacina — guardar cópia fora de /tmp).
