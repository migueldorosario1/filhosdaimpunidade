# FÓRUM — Selo "Cafezinho Media Group" em toda a rede + seção Aplicativos no site do grupo (05/08/2026)

**Data:** 2026-08-05 ~10:50-11:20 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel (chat): "tem que colocar em todos os sites temáticos, Cafézinho Média Grupo com link. Embaixo, pequenininho. Cuidado para não quebrar a formatação" + "coloca primeiro no cafezinho.news para eu ver" + "no canônico só deixa o plano pronto e me lembra" + "no Moka Reader também" + "no site do grupo acrescenta aplicativos com o Moka Reader bem bonitinho"

## 1. O que foi feito (tudo no ar)

| Propriedade | Mudança | Verificado |
|---|---|---|
| 8 temáticos V4 (ceara, riocarta, mundotrilhos, mapario, globalsouth, discoverbrazil, railpost, aiatolah) | Linha pequena no rodapé: "Um portal do / Part of the **Cafezinho Media Group**" (PT/EN conforme o site; aiatolah bilíngue) | 8/8 ao vivo ✅ |
| **cafezinho.news (espelho)** | mu-plugin `cafezinho-media-group-selo.php` (100% aditivo, hook `wp_footer` pri 99) — **primeiro da família Cafezinho, p/ Miguel ver** | ao vivo ✅ |
| **Moka Reader** (mokareader.com) | selo no `SiteFooter.tsx` + chave i18n `footer_group` nos **12 idiomas** (padrão da casa) | ao vivo ✅ |
| **cafezinhomediagroup.vercel.app** | nova seção **"Aplicativos do Grupo"** com card-vitrine do Moka Reader (mesma linguagem visual dos cards de portais: hover, badge, ícone livro) | ao vivo ✅ |

## 2. Cuidados tomados ("não quebrar a formatação")

- Footers V4: inserção idempotente via script (1 `</footer>` por arquivo, CSS scoped `.group-tag`, font-size 0.72em, borda pontilhada no link) — **build local validado em ceara (astro build OK) e aiatolah (313 páginas OK)** antes do push.
- aiatolah não tem `Footer.astro` — footer vive no `layouts/Layout.astro` (edição separada, bilíngue `isPt`).
- Moka: repo ativo por outro agente — rebase limpo sobre `moka/main` (commit Moka 5.4.2 dele preservado), push nos 2 remotes (moka + origin/igot); `tsc --noEmit` 0 erros + `npm run build` OK.
- Media Group: seção nova **fora** do grid filtrável (`.portal-card` é varrido pelo JS de filtros — usei `.app-card` com CSS espelhado para não acoplar).
- Espelho WP: nada de edição de tema — mu-plugin novo, rollback = apagar arquivo.

## 3. Canônico ocafezinho.com — PLANO PRONTO (aguardando "vai")

Acesso confirmado (SSH `cafezinho-wp` = us65.serverdo.in; WP Super Cache ATIVO). Plano registrado em `CEREBRO_NODE_AGENDA_LEMBRETES.md` (lembrete datado 05/08 tarde):
1. Copiar o mesmo mu-plugin do espelho para `/var/www/ocafezinho/wp-content/mu-plugins/`.
2. `wp super-cache flush --path=/var/www/ocafezinho --allow-root`.
3. Verificar `curl -s https://www.ocafezinho.com/ | grep cmg-selo`.
4. Rollback = apagar arquivo + flush.

## 4. Pendências

- **Miguel homologar o espelho** (cafezinho.news) → depois executar o port ao canônico.
- Backup local do mu-plugin: `/tmp/cafezinho-media-group-selo.php` (também recuperável do espelho).

**Memória técnica:** `Memorias/memoria_selo_cafezinho_media_group_20260805.md`
