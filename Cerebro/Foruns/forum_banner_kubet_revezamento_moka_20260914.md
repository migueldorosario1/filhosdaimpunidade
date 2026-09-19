# Banner KUBET (thbku.bet) revezando com MOKA no Cafezinho — 14/09/2026

**Autor:** ZCode/GLM-5.3
**Data/hora:** 2026-09-14 18:5x BRT
**Autorização Miguel:** chat CLI 14/09 ~18:0x (áudio): investigar o melhor lugar vazio para o anúncio; em seguida ~18:1x: "você consegue botar no mesmo lugar do MOKA, mas revezando com ele?" — implementado na sequência.

## 1. Decisão

- **Onde:** exatamente no lugar do banner MOKA — o par 728×90 (desktop) / 300×250 (mobile) nos DOIS pontos de injeção existentes: home (`#moka-banner-home` no `front-page.php`, após a Linha do Tempo) e single (mu-plugin `cafezinho-moka-single.php`, depois do "Leia também", antes da newsletter).
- **Como:** revezamento 50/50 POR CARREGAMENTO, sorteado no NAVEGADOR (rotator HTML estático com `Math.random()` + `location.replace`). Imune ao cache de página (WP Rocket/CF) — cada pageview sorteia de novo.
- **Regra do Miguel preservada** (comentário no front-page.php): "1 anúncio por intervalo de conteúdo — nada empilhado". O revezamento nunca empilha: sempre 1 criativo por vez no mesmo slot.
- **Coerência com a Emenda 11** (gate `cafezinho-gate-apostas-emenda11.php`, ordem 26/08): aposta é parceria aceita; banner é arquivo estático, não passa por save_post — gate não interfere. Criativo deliberadamente sóbrio: só a logo, sem frase de funil/bônus, com selo discreto +18.

## 2. O que foi feito (resumo técnico)

- Pasta nova `wp-content/banners-cafezinho/` (www-data 755/644): `kubet-logo.png` (logo 351×141 do Miguel, fundo azul-marinho), `kubet-728x90.html`, `kubet-300x250.html` (fundo #051939 = cor média da borda da logo, emenda invisível; link thbku.bet com `rel="nofollow sponsored noopener"`), `rotator-728x90.html`, `rotator-300x250.html` (const `P_KUBET = 0.5` ajustável de 0 a 1; `<noscript>` cai pro MOKA).
- Backups datados: `front-page.php.bak_pre_kubet_revezamento_20260914` e `cafezinho-moka-single.php.bak_pre_kubet_revezamento_20260914`. Edição cirúrgica: `src` dos 4 iframes → rotators; `title` do iframe "Moka Reader" → "Publicidade". `php -l` OK nos dois.
- Cache WP Rocket limpo manualmente (`rm -rf cache/wp-rocket/*`; `wp rocket purge` não estava registrado no wp-cli).

## 3. Provas

- 5/5 arquivos novos: HTTP 200 no domínio público.
- HTML público: home e single servindo `rotator-728x90/300x250`.
- Browser real (in-app): ~24 sortes válidos na home → KUBET 13 × MOKA 11 (~50/50); screenshots do MESMO slot com KUBET (azul-marinho, logo dourada coroa+KUBET, +18) e com MOKA (laranja "Moka Reader") — revezamento visível e sem sobreposição.
- Single: 5 cargas → MOKA, KUBET, MOKA, MOKA, MOKA (alternando no mesmo slot).
- Nenhum outro anúncio afetado: o MOKA era o ÚNICO anúncio real do site (demais slots `.ad-space` do tema estão vazios/placeholder desde sempre — ver memória §2).

## 4. Estado / o que falta / o que preciso do Miguel

- **Pronto e no ar:** revezamento 50/50 funcionando em home + todas as matérias.
- **Falta:** nada técnico. Opcionais a pedido: ajustar proporção (`P_KUBET` num único arquivo), criativos novos da KUBET (a logo 351×141 fica pequena no 728×90 — criativo nativo de 728×90 renderia melhor), revezo também no AMP (hoje só non-AMP, onde os slots vivem).
- **Preciso do Miguel:** só se quiser mudar proporção/criativo. **Aviso regulatório (decisão dele):** thbku.bet é operador offshore não licenciado no Brasil — publicidade de bet não autorizada expõe o veículo à SPA/CONAR (Resolução SPA 1.315/2025); manter o selo +18 e evitar promessas de bônus (já é o padrão do criativo) reduz o risco, não zera.
- **Rollback total:** restaurar os 2 `.bak` (ou trocar `rotator-*.html` → `moka-*.html` nos 4 `src`) — 2 minutos.

## 5. Mapa de anúncios do site (contexto da investigação)

- Tema `ocafezinho-portal` 2.0 tem ~14 slots nomeados `.ad-space` (banner-top, after-manchete, middle, before/after-comments, after-related, bottom etc.) — TODOS vazios no HTML servido (placeholders). O par MOKA era o único anúncio real; agora reveza com KUBET.
- `banner-after-comments` (desktop+mobile) segue VAZIO — é o "embaixo dos comentários" que o Miguel citou; disponível para campanha futura sem esbarrar em nada (não usado nesta missão).

## 6. Adendo ~18:4x — PLANO DE DESLIGAMENTO PRONTO (ordem Miguel)

- Miguel pediu plano fácil de desligar/voltar só MOKA → gravado em `Outros/pautas editoriais o cafezinho/Dia a dia/bet/PLANO_DESLIGAR_ANUNCIO_KUBET.md` (3 caminhos: 1 = P_KUBET 0.5→0 via sed, 30s, religável/dosável · 2 = restaurar os 2 .bak + limpar cache rocket · 3 = rm -rf banners-cafezinho, SÓ depois do 2).
- Prints LIMPOS aprovados por visão na mesma pasta (print_LIMPO_kubet_728x90 / 300x250 / na_home_contexto) — os primeiros prints do single saíram duplicados por defeito do CAPTURADOR do IAB (não do site); sanidade do anúncio provada por DOM (iframe exato 728×90, criativo contido em 90px, zero overflow) + visão do recorte limpo.
- Prova DOM anti-estouro (para acalmar a suspeita "estourando a página"): iframe 728×90 attr+style, body interno 728×90, img 82px — nada vaza.

## 7. Adendo 15/09 ~18:0x — KUBET DESLIGADO (ordem Miguel "fica apenas o Moka")

- Executado o desligamento reversível: `P_KUBET 0.5→0` nos 2 rotators + **bump `?v=2`** nas URLs dos 2 templates (front-page.php + mu-plugin, c/ `.bak_pre_kubet_off_20260915`) + `wp eval opcache_reset` + rocket clean.
- Provas: arquivo público ?v=2 = `P_KUBET = 0`; home e single públicos servindo v2; browser real 4/4 cargas = MOKA.
- 🔴 APRENDIZADO 1 — camada de cache intermediária (header `x-cache-status`, entre CF e origem, caixa a identificar — suspeita plugin serverdoin-cdn) cacheia `wp-content/*.html` por **1 ano** (`cache-control: max-age=31536000`): toda mudança em rotator/criativo exige bump de versão na URL senão leitores antigos ficam no criativo velho até o TTL.
- 🔴 APRENDIZADO 2 — opcache do PHP segura o template compilado: após editar front-page/mu-plugin, rodar `wp eval 'opcache_reset();' --allow-root` (a home ficava velha mesmo com rocket limpo).
- RELIGAÇÃO (quando o Miguel pedir): comando único no `PLANO_DESLIGAR_ANUNCIO_KUBET.md` (pasta bet) = P_KUBET→0.5 + bump v2→v3 + opcache_reset + rocket clean. Pendência estrutural opcional: no-cache para os rotators na camada x-cache a identificar.

## 8. Adendo 15/09 ~18:1x — ANÁLISE DE RISCO DO ANUNCIANTE (ordem Miguel) — 🔴 VEREDITO: NÃO RELIGAR

Investigação do destino do anúncio (thbku.bet) + denúncias públicas:

1. **Funil com domínios camuflados rotativos:** thbku.bet → 301 → nissancompautos.com.mx (nome de autopeças) → e MINUTOS DEPOIS da 1ª análise já rotacionava para ciclocontinuoeditorial.com (nome editorial) → portal KUBET em TAILANDÊS (cassino/slots/futebol/loteria), 177 links empurrando o domínio de conversão kubet888.bz, login via ad310.bjh97.net (4º domínio), autor fictício "Wongsatorn Nilglad", depósitos SÓ por bancos tailandeses (KBank/BBL/SCB/Krungthai), zero PT/PIX, sem licença exibida, afirma-se "legal" num país onde jogo online é ilegal.
2. **Marca KUBET = histórico criminal (Vietnã):** polícia de Hưng Yên instaurou inquérito (24/8) por jogo ilegal + organização via KUBET/B52club (~131 mil contas); VnExpress/VietNamNet — rede de 500 BILHÕES de dong (~US$ 20 mi+) com centenas de contas bancárias/cripto p/ esconder fluxo; Thái Bình — lavagem de trilhões de dong, site "opera há anos com MUITOS domínios diferentes, servidores fora"; outra rede +1.000 bilhões usando IA p/ LAVAR DINHEIRO e MANIPULAR RESULTADOS (dono nomeado Phạm Hồng Chuyền); VTV — apostadores processados (1.000+ sessões, 3 bi dong).
3. **Família de domínios kubet*:** ScamAdviser/ScamDetector — kubet-88.bet «may be a scam», kubet9378.com «forte indicador de golpe», kubet88.company 10,6/100, kubet88z.me entre os piores da plataforma; kubet888.site 66/100 (misto). thbku.bet e kubet888.bz ESPECÍFICOS: zero denúncias indexadas (domínios novos/rotativos — em si sinal).
4. **PT-BR:** nada no Reclame Aqui contra Kubet.

**Classificação de risco (Miguel perguntou "pode ter sido golpe?"):**
- Para o SITE: NÃO houve golpe técnico — o banner era imagem+link escritos por nós (sem malware/tracker; rel nofollow sponsored). Nada foi injetado nos leitores.
- Para o LEITOR que clicou: ALTO risco — caiu em funil de afiliado de operação com histórico criminal comprovado (manipulação de resultados + lavagem), domínios camuflados, sem licença, sem PIX/PT. Se depositasse (cripto), risco real de perda (resultado manipulado/saque negado). Sem vítima BR documentada contra thbku.bet especificamente — mas o padrão é de operação fraudulenta, não de casa legítima.
- Exposição: ~24h no ar (14/09 18h→15/09 18h), 50/50 com MOKA.
- **Decisão registrada: manter desligado; NÃO religar com este domínio/anunciante. Se bet no futuro: SÓ operador licenciado SPA/BR.**
