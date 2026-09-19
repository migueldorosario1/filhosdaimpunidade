# 📰 Fórum — Correção do título 268482 (Villatoro) + EMENDA EMU-2 (títulos simples, sem sigla, cargo em vez de sobrenome)

**Data:** 2026-09-01 ~17:36 BRT · **Sessão:** ZCode/GLM-5.3 (Dell) · **Origem:** queixa do Miguel no chat ("Já falei para você não usar a sigla no título? … vamos fazer títulos mais simples. Uma frase só. E sem sigla no título. E quem é Vila Toro? tem que falar ministro")

## O que aconteceu

- Post **268482** (publicado 01/09 12:39, esteira `v41_nacional`, job `9b39f2cf2c57`, autor REST 5470 "Redação") nasceu com o título **"Villatoro defende exceção de Bukele e restringe imagens do Cecot"** — violando **2 regras canônicas de título que JÁ existiam** no Manual de Estilo Unificado (regra 2: uma ideia, zero "e" concatenando; regra 4/EMU-1: sigla não consagrada — "Cecot") e o ponto novo: **sobrenome de pessoa que o leitor não conhece**.
- Gustavo Villatoro = **ministro da Justiça e Segurança Pública de El Salvador** (o próprio fact-check `_v41_fc` do post confirmava o cargo).

## Correção aplicada (17:36, in place, URL/slug preservado)

- `wp post update 268482 --post_title='Ministro de Bukele defende regime de exceção do país'` (sugestão literal do Miguel) via SSH `cafezinho-wp` + wp-cli.
- **Cache:** o purge documentado (`/root/rollback_canonico_20260727/purge_rocket.php` rodado de /tmp) **não funciona mais** — script standalone não carrega o WordPress, funções `rocket_clean_*` não existem, saída vazia. Cura: `sudo -u www-data wp eval 'rocket_clean_domain(); rocket_clean_minify();'` → "domain OK minify OK". Depois disso a página ainda ficou ~5 min com HTML velho por cache de URL exata; resolveu sozinho ao expirar (query string `?v=2` provou origem limpa na hora).
- **Provas públicas finais:** `<title>` = "Ministro de Bukele defende regime de exceção do país - O Cafezinho" · og:title novo · h1 novo · zero ocorrências do título velho · home já exibindo o novo · cf-cache-status DYNAMIC (Cloudflare não cacheia HTML).

## EMU-2 gravada no Manual (`Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md`)

1. Regras de título: "as 7" → **"as 8 regras canônicas"** — nova regra 8: **pessoa pouco conhecida entra pelo CARGO/qualificação, nunca pelo sobrenome solto** ("Villatoro" → "Ministro de Bukele"; sobrenome cru só para fama nacional).
2. Checklist C3 item 9 ganhou "sem sigla não consagrada, cargo p/ pessoa pouco conhecida".
3. Apêndice I: **EMU-2 (01/09/2026)** com o caso-escola 268482 completo.

## Estado / o que falta / o que preciso de você (Miguel)

- **Pronto:** post corrigido e provado; manual emendado; monitor ✅; NODE_ESTILO e NODE_ATUALIZACOES catalogados; memória irmã gravada.
- **Falta (pendente de sessão com frente NYC):** as regras 2 e 4 JÁ CONSTAVAM do manual e o **auditor de títulos do v41_ciclo deixou passar** — precisa de enforcement no gerador/auditor (NYC `/root/v4_labs`) + atualizar a cópia do manual em `nyc:/root/v4_labs/dados/`. Não foi feito nesta sessão para não colidir com a sessão urgente que patcheava o `dsn_publicador` na Tencent no mesmo horário.
- **Do Miguel:** nada obrigatório — se quiser, validar o título novo no ar (link do post segue o mesmo slug antigo).

---

## Adendo — caso-irmão 268457 (Kast) — ZCode/GLM-5.3 01/09 18:0x

2º título degenerado do mesmo dia flagrado pelo Miguel: **268457** «Cocaína em transferência expõe falha em prisão vitrine de Kast» (v41_geopolitica, 14:31) — tradução literal de "cárcel vitrina". Corrigido in place 17:52 → «Preso é flagrado com cocaína antes de ir para cadeia de segurança máxima de Kast» (80c). Investigação de autoria completa + mapa da checagem dupla (auditor advisor cobre só autor 5786; V4.1 publica pelo 5470 e passa batido): `forum_titulo_kast_investigacao_autoria_20260901.md` + ponte ZM-20260901-031. Enforcement EMU-2 no v41_ciclo segue pendente e agora tem 2 casos-escola.
