# 💵 Fórum — Página /v6/pagamentos no Painel CCTV V6 (PIs de publicidade oficial)

**Ref:** ZM-20260910-014 · **Data:** 10/09/2026 ~15:2x BRT · **Autor:** ZM (GLM-5.3) · **Ordem do Miguel:** prompt de 10/09 ~15h ("faz uma nova página no painel cctv, chamado Pagamentos… lista os PIs (ler cada um dos pdfs)… valor, agência, estimativa da data de pagamento… impressões vendidas por tipo de anúncio… pesquisa no GA4 quantas visualizações tivemos no período específico do contrato")

## 1. O que foi feito

Nova página **/v6/pagamentos** ("💵 Pagamentos") no painel CCTV V6 (Tencent, `painel_cctv_v6.py`, serviço `cctv-v6`, porta interna 8084, pública `http://43.156.151.165/v6/pagamentos`). Os 4 PDFs de PIs da pasta `Downloads/Antigravity Google/Outros/Pagamentos/Pis/` foram lidos um a um (pdftotext -layout) e os dados entram como constante `PAGAMENTOS_PIS` no próprio painel (fonte de verdade seguem sendo os PDFs). Views por período vêm AO VIVO do GA4 (função nova `ga4_views_periodo`, intervalo fixo de datas, cache 12h).

Adições ao painel: função GA4 por período + bloco PAGAMENTOS_PIS + `pagina_pagamentos()` + rota `/pagamentos` + item no NAV + card na home (grupo "📊 Números"). Backup do arquivo vivo: `.bak_pagamentos_20260910` no servidor (rollback = cp de volta + restart).

## 2. Os 4 PIs (valores conferidos contra os PDFs)

| PI | Anunciante | Agência | Campanha | Veiculação | Faturado | Estimativa de pgto |
|----|-----------|---------|----------|------------|----------|--------------------|
| 053459 | Ministério da Saúde | DeBrito Brasil | Always On — Tuberculose | 01–09/04/2026 | R$ 1.111,88 | 04/05/2026 |
| 054223 | Ministério da Saúde | DeBrito Brasil | Always On — SUS | 05–31/05/2026 | R$ 5.568,28 | 22/06/2026 |
| 054247 | Ministério da Saúde | DeBrito Brasil | Always On — SUS | 04–30/06/2026 | R$ 1.554,23 | 21/07/2026 |
| 023878 | MIDR | CLX Comunicação | PNAE | 15–30/06/2026 | R$ 493,41 | 24/07/2026 (C/APRES.) |

**Totais:** negociado R$ 10.909,75 · faturado R$ 8.727,80 · 528.362 impressões · CPM líquido médio R$ 16,52.

Fluxo do dinheiro (checado PI a PI): bruto (CPM tabela − 75% negociação) → − abatimentos (brand safety/viewability) = negociado → − 20% desconto padrão = **faturado**.

**Impressões por tipo:** Super Banner 300x250/320x100 = 377.990 (R$ 9.449,76) · Super Banner Footer Fixo = 150.372 (R$ 4.922,77).

**GA4 (views no período exato do contrato, propriedade 374552425):** 53459 = 233.502 · 54223 = 758.216 · 54247 = 199.505 · 23878 = 91.506.

## 3. Achados que o Miguel precisa saber

1. **Todas as 4 previsões de pagamento estão VENCIDAS** (regra contratual: 15 dias úteis após fim da veiculação; a página mostra "previsão vencida há Nd — cobrar"): 129d (53459), 80d (54223), 51d (54247), 48d (23878). Se algo já caiu na conta, preencher `pago_em` na constante que a linha vira ✅ PAGO.
2. PI 054247 tem **data de emissão 16/03/2026 impressa no PDF** — anterior à própria campanha (junho); provável artefato do sistema da agência. Página exibe com asterisco e nota de rodapé.
3. Abatimentos pesados no 54223: viewability 51,2% (−R$ 2.163,95) + brand safety (−R$ 365,30) — cortaram 26,6% do bruto.
4. O período de maio (54223) teve **758.216 views para 379.584 impressões vendidas** — audiência entregou folga 2:1 (bom argumento comercial para renovação).
5. `.tencent_v6_oficina/painel_cctv_v6.py` (oficina local) estava DESATUALIZADA em relação ao servidor ANTES desta missão (md5 divergente desde ~03/09). O arquivo vivo no Tencent é o canônico; staging desta missão salvo em `ZCodeProject/pagamentos_painel/painel_cctv_v6_VIVO.py`.

## 4. Estado / o que falta / o que preciso de você (Miguel)

- ✅ Pronto: página no ar, 4 PIs lidos, GA4 ao vivo, menu+home, backup com rollback de 1 comando, provas 200 interno/público + screenshot QA.
- Falta: confirmar na conta quais PIs já foram pagos e me dizer as datas (preencho `pago_em` → ✅).
- Falta (futuro): novos PIs que chegarem na pasta Pis = acrescentar objeto na lista `PAGAMENTOS_PIS` (estrutura documentada no cabeçalho do bloco).

## 5. Provas

- curl interno `127.0.0.1:8084/pagamentos` → 200 (18.369 bytes) · público `127.0.0.1/v6/pagamentos` (nginx :80) → 200; `/`, `/servidores`, `/audiencia` → 200 (painel sadio).
- Sintaxe: `compile()` no Python 3.12 do servidor = OK (warning linha 7620 pré-existente).
- GA4 testado direto na API com as credenciais do servidor (4 períodos retornaram dados).
- md5 deploy: deffcf86cf74159bfb0c84532b9cd643 (servidor = staging).

## 6. Adendo (10/09 ~16:1x) — PÁGINA PÚBLICA INDEPENDENTE /pagamentos (ZM-20260910-015)

Ordem do Miguel ~15:4x: mesma tabela, mas num endereço ABERTO e INDEPENDENTE para enviar à agência — SEM menu (o nav do painel interno tem links não-divulgáveis). A interna /v6/pagamentos permanece intacta.

- **Endereço público:** `http://43.156.151.165/pagamentos`
- **Arquitetura:** servidor próprio `pagamentos_publico.py` (arquivo único ~300 linhas, `/home/ubuntu/cafezinho/pagamentos_publico/`), serviço systemd `pagamentos-publico.service` na porta 8085 (loopback), nginx `location /pagamentos` → 8085 (conf com backup `.bak_pagamentos_publico_20260910`). Independente do cctv-v6: um cair, o outro segue.
- **Segurança:** SEM nav/menu e zero links internos; meta robots noindex/nofollow; auditoria grep no HTML renderizado = 0 ocorrências de nav, href=/v6, href=/v5, "cobrar", pago_em, caminhos internos e ID da propriedade GA4. Tons internos trocados: "previsão vencida — cobrar" → "prazo vencido há N dias" (factual, sem tom interno); notas operacionais fora.
- **Conteúdo:** mesmos 4 PIs + resumo + impressões por tipo (total bruto R$ 14.372,53) + GA4 ao vivo por período (cache arquivo próprio 12h `ga4_cache_publico.json`).
- **Bugs curados no caminho:** (1) systemd `Environment=` com caminho contendo espaços ("Projeto Cafezinho Agentes") exige ASPAS → credencial GA4 não carregava; (2) o código não aplicava GA4_CREDS no env (agora `os.environ.setdefault`); (3) 404 pós-reload do nginx era só corrida de workers antigos (persistiu sozinho).
- **⚠️ MANUTENÇÃO (2 lugares):** PI novo ou pagamento confirmado → atualizar `PIS_PUBLICOS` AQUI e `PAGAMENTOS_PIS` no painel_cctv_v6.py (interno). Documentado nos cabeçalhos dos dois arquivos.
- Rollbacks: nginx `cp .bak_pagamentos_publico_20260910 && nginx -s reload`; serviço `systemctl disable --now pagamentos-publico`; página interna intocada.
- Provas: 200 interno (8085) e público (:80/pagamentos); GA4 com os 4 números reais na tela; screenshot QA 6/6 (sem menu, cards, tabelas, sem quebra).

## 7. Adendo (10/09 ~16:5x) — RECLAMAÇÃO "NÃO CONSIGO ENTRAR" da agência + URL HTTPS (ZM-20260910-016)

- **Diagnóstico pelos logs:** NENHUMA requisição da agência chegou ao nginx (access.log só tem os testes nossos: 177.27.x Dell, 189.94.x, curl 16:43). Página estava 200 o tempo todo, interna e externa. Causa provável: rede corporativa deles bloquejando HTTP em IP cru (sem domínio) e/ou navegador auto-subindo p/ HTTPS num IP que não tem certificado → erro de conexão/certificado.
- **Cura:** a página agora também é servida com HTTPS e certificado válido Let's Encrypt no hostname que já existia no servidor: **`https://43.156.151.165.sslip.io/pagamentos`** (sslip.io = DNS coringa gratuito que aponta o próprio IP; cert LE do bloco do Moka, válido até 21/10/2026). Patch: `location /pagamentos` no server 443 do `sites-available/moka-pontos` (backup em `/etc/nginx/backups_pre_edit/` — ⚠️ backup JAMAIS dentro de sites-enabled, o nginx carrega tudo que está lá e nasce server-name duplicado, warning na tela).
- **URLs válidas agora (as duas):** `https://43.156.151.165.sslip.io/pagamentos` (mandar ESSA para a agência) · `http://43.156.151.165/pagamentos` (continua 200). Redirect 301 http→https no sslip OK · Moka no mesmo bloco 443 intocado (200).
- **Se a agência continuar sem entrar:** pedir o print do erro; plano B = exportar a página em PDF e mandar por e-mail (serviço já gera HTML estático, conversão trivial).
