# 🧠 Memória técnica — Página /v6/pagamentos (PIs) no Painel CCTV V6

**Ref:** ZM-20260910-014 · **Data:** 10/09/2026 ~15:2x BRT · **Autor:** ZM (GLM-5.3) · Fórum par: `Foruns/forum_painel_v6_pagamentos_pis_20260910.md`

## 1. Fonte dos dados

- Pasta dos PDFs: `/home/migueldorosario/Downloads/Antigravity Google/Outros/Pagamentos/Pis/` (4 arquivos, ~130-147KB cada).
- Extração: `pdftotext -layout` → `/tmp/pis_txt/*.txt`; leitura manual dos campos. Textos extraídos não persistidos (regeneráveis com 1 comando).
- Dados finais embutidos na constante `PAGAMENTOS_PIS` do `painel_cctv_v6.py` (Tencent) com estrutura documentada no cabeçalho do bloco. Campo `pago_em` (AAAA-MM-DD) vira pill ✅ PAGO quando preenchido.

## 2. Números conferidos (provêm dos PDFs; aritmética revalidada)

| PI | Bruto formatos | Abatimentos | Negociado | Desc. padrão (20%) | FATURADO | Impressões | Estimativa |
|----|---------------|-------------|-----------|--------------------|----------|------------|------------|
| 053459 | 2.093,69 | 703,84 | 1.389,85 | 277,97 | 1.111,88 | 66.998 | 04/05/26 |
| 054223 | 9.489,60 | 2.529,25 | 6.960,35 | 1.392,07 | 5.568,28 | 379.584 | 22/06/26 |
| 054247 | 2.172,48 | 229,69 | 1.942,79 | 388,56 | 1.554,23 | 65.333 | 21/07/26 |
| 023878 | 616,76 | 0,00 | 616,76 | 123,35 | 493,41 | 16.447 | 24/07/26 |

- Estimativas: 15 dias úteis após o fim da veiculação (feriados nacionais 2026 descontados: carnaval 16-17/02, Paixão 03/04, Tiradentes, Trabalho, Corpus Christi 04/06, 07/09, 12/10, 02/11, 15/11, 20/11, Natal); PI CLX = contra apresentação → emissão (03/07) + 15 úteis = 24/07.
- GA4 (propriedade 374552425, plataforma web, screenPageViews): 53459=233.502 · 54223=758.216 · 54247=199.505 · 23878=91.506.

## 3. Arquivos tocados

- **Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`** (vivo, servido pelo systemd `cctv-v6`, porta 8084; nginx :80 faz strip de `/v6/`): +função `ga4_views_periodo()` (antes de `ga4_posts_datados`), +bloco `PAGAMENTOS_PIS`/helpers `_pgt_*`/`pagina_pagamentos()` (antes de `ROUTES`), +rota `"/pagamentos"`, +item NAV `("/v6/pagamentos", "💵 Pagamentos", "pagamentos")`, +card home no grupo 📊 Números.
- Backup rollback: `painel_cctv_v6.py.bak_pagamentos_20260910` (no mesmo dir) → rollback = `cp .bak sobre o vivo && sudo systemctl restart cctv-v6`.
- Staging local: `/home/migueldorosario/ZCodeProject/pagamentos_painel/painel_cctv_v6_VIVO.py` (md5 = deploy deffcf86cf74159bfb0c84532b9cd643).
- Cérebro: este arquivo + fórum + linha em CEREBRO_NODE_AGENTES.md + linha em CEREBRO_NODE_ATUALIZACOES.md + monitoramento ✅.

## 4. Armadilhas anotadas (para próximas páginas/painéis)

1. **Oficina desatualizada**: NÃO editar `.tencent_v6_oficina/painel_cctv_v6.py` e subir — ela está ATRÁS do vivo (divergência desde ~03/09); subir por cima reverteria páginas recentes. Fluxo seguro: `scp tencent:vivo → editar → .bak no servidor → scp → restart cctv-v6`.
2. **py_compile local NÃO valida** este arquivo (código pré-existente usa PEP 701, exige 3.12): validar com `python3 -c "compile(open(f).read(), f, 'exec')"` NO servidor (e sem `-m py_compile`, que morre tentando gravar `__pycache__` em dir sem permissão).
3. **Porta do nginx é a 80** para `/v6/*` (proxy com strip); a :8080 NÃO serve o painel (502 em tudo — não é bug).
4. GA4: cliente e credenciais (`root/ga4.json`) já embutidos no painel — reusar `_ga4_client()` + `os.environ.get("GA4_PROPERTY_ID", "374552425")`; sempre `platform=web` filter e cache (`_cache_get/_cache_set`), período histórico = TTL 12h.
5. Reinício do cctv-v6 é rápido (~2s) e não derruba nada mais; conferir `systemctl is-active` + curl 200 no `/` e numa segunda rota antiga antes de dar tarefa por feita.

## 5. Como atualizar quando chegarem PIs novos

1. `pdftotext -layout "<PDF>" /tmp/pi.txt` e ler os campos (agência/cabeçalho, DATA EMISSÃO, PERÍODO(S), FORMATO, CPM-IMPACTOS, custo unitário, % neg, abatimentos, VALOR NEGOCIADO/DESCONTO PADRÃO/VALOR FATURADO, TOT de impressões).
2. Editar `PAGAMENTOS_PIS` no arquivo VIVO do Tencent (ou staging → deploy igual §3), calcular estimativa (15 dias úteis pós-veiculação; C/APRES. → emissão + 15úteis), restart, curl 200.
3. Pagamento confirmado pelo Miguel → preencher `pago_em`.

## 6. Adendo (10/09 ~16:1x) — página PÚBLICA independente (ZM-20260910-015)

- Arquivo novo: `/home/ubuntu/cafezinho/pagamentos_publico/pagamentos_publico.py` (staging local `ZCodeProject/pagamentos_painel/pagamentos_publico.py`) — servidor único stdlib + cliente GA4, porta 8085 loopback, serviço `pagamentos-publico.service`, nginx `location /pagamentos` (:80). Público: `http://43.156.151.165/pagamentos`.
- Render é função `render()` única; handler só aceita `/` e `/pagamentos` (resto 404); nunca retorna 500 cru (página de indisponibilidade). Cache GA4 em arquivo próprio 12h.
- **Armadilhas novas:** (a) systemd `Environment=` com valor contendo ESPAÇOS exige aspas duplas (`Environment="K=Caminho Com Espaços"`) — sem aspas o systemd ignora a atribuição em silêncio (journalctl mostra "Invalid environment assignment"); (b) reload do nginx tem janela de workers antigos — 404 imediatamente após `nginx -s reload` pode ser corrida, retestar antes de debugar; (c) atualizar PI = DOIS arquivos agora (interno `PAGAMENTOS_PIS` no painel + público `PIS_PUBLICOS` aqui).
- Backups/rollbacks: nginx `painel.conf.bak_pagamentos_publico_20260910`; serviço `systemctl disable --now pagamentos-publico`; interno intocado.

## 7. Adendo (10/09 ~16:5x) — incidente "não consigo entrar" + HTTPS sslip.io (ZM-20260910-016)

- Evidência: access.log do nginx NÃO tem nenhuma requisição da agência — o pedido morreu na rede deles (HTTP em IP cru bloqueado por proxy corporativo, ou browser auto-upgrade p/ HTTPS sem cert no IP). Página sempre 200.
- Solução em produção: **https://43.156.151.165.sslip.io/pagamentos** — `location /pagamentos` adicionada ao server 443 (`server_name 43.156.151.165.sslip.io`) do `/etc/nginx/sites-available/moka-pontos`, que já tinha certificado Let's Encrypt (válido até 21/10/2026; renovar = certbot renova sozinho, conferir depois). Backup: `/etc/nginx/backups_pre_edit/moka-pontos.bak_pagamentos_publico_20260910`.
- **Armadilha do .bak:** NÃO deixar backup dentro de `/etc/nginx/sites-enabled/` (nem conf.d) — o include é glob `*` e carrega o .bak como server block duplicado (warning "conflicting server name", e o servidor ignora o segundo). Backups de nginx vivem em `/etc/nginx/backups_pre_edit/`.
- Provas finais: HTTPS externo 200 (1,9s Dell) · http IP 200 · redirect 301 http→https no sslip · Moka no mesmo 443 intocado (200).
