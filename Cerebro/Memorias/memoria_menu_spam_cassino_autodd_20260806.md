# Memória — Link spam de cassino no menu do Cafezinho + trava de auto-add (2026-08-06)

> **Tema Duplo:** fórum de decisões em `Foruns/forum_menu_spam_cassino_autodd_20260806.md`.
> **Guia operacional permanente (como editar/corrigir o menu):** `Cerebro/cartoes_bolso/CARTAO_BOLSO_MENU_WP_CAFEZINHO.md`.
> Executor: ZCode (Kimi K3), chat direto PC, workspace ZCodeProject. Ordem do Miguel 06/08: "tira esse link do menu, e aproveita e deixa de um jeito que nenhuma página nova possa entrar assim no menu".

## 1. Sintoma

Menu do topo e do rodapé do ocafezinho.com (é o MESMO menu, term_id 21062, slug `menu`, locations `menu, amp-menu, amp-footer-menu, amp-alternative-menu`) exibia um 11º item estranho:
**"O jogo do balão no Brasil: como funciona este popular jogo de cassino"**.

## 2. Diagnóstico (wp-cli, servidor cafezinho-wp / us65.serverdo.in / 190.89.239.65:51439)

| Fato | Valor |
|---|---|
| Página spam | ID **264513**, slug `o-jogo-do-balao-no-brasil-como-funciona-este-popular-jogo-de-cassino`, status `publish`, criada **2026-08-06 11:28:19** |
| Autor | user ID **5749** = `rhyandemeira` (rhyandemeiracontato@gmail.com), role **editor**, registrado 2023-04-20 |
| Item no menu visível | `nav_menu_item` **264519** no menu 21062 (`Menu`) |
| Item no menu legado | `nav_menu_item` **264518** no menu 1279 (`apptha`, 626 itens, sem location — não renderiza) |
| Causa-raiz da entrada no menu | `wp option nav_menu_options = {"0":false,"auto_add":[1279,21062]}` → **auto-add de páginas novas LIGADO** nos dois menus |
| Evidência ao vivo (antes) | homepage com 3 links para a página (grep `balão` = 3) |

**Por que entrou no menu:** todo `page` novo de nível superior era auto-adicionado pelo `auto_add`. A página em si foi criada por uma conta editor com credencial válida — NÃO há sinal técnico de injeção/hack (nada de post fantasma, autor é humano conhecido do WP).

**Padrão da conta 5749 (publis periódicos):** 264513 (cassino, 06/08), 261667 ("Revisão do MostBet Plataforma de Jogos", 14/07), 258664, 256652, 251680, 249571, 234514, 229985… Contas 5470 e 2018 também publicam páginas de publi (TEMU afiliados, Keeta). Lista completa na seção 5.

## 3. Execução (06/08, ~12:00 BRT)

Backup ANTES de mexer (servidor, `/root/backup_menu_fix_20260806/`):
- `nav_menu_options.bak.json` — valor original da opção
- `menu_21062_items.bak.txt` — itens do menu
- `fix_menu.php` — script usado (idempotente)

```bash
# 1) remover os 2 itens de menu que apontavam pra página spam
sudo -u www-data wp --path=/var/www/ocafezinho menu item delete 264518 264519
# → Success: Deleted 2 of 2 menu items.

# 2) travar auto-add em TODOS os menus + purgar cache (via wp eval-file /tmp/fix_menu.php)
#    $o=get_option('nav_menu_options'); $o['auto_add']=array(); update_option(...);
#    rocket_clean_domain(); wp_cache_flush();
# → AUTO_ADD_OK / ROCKET_CLEANED / CACHE_FLUSHED
```

## 4. Verificação (depois)

- `wp menu item list 21062` → 10 itens, sem o spam (Quem somos?, Editorias, Regional>Ceará/RJ, Política, Economia, Geopolítica, Tecnologia, Ciência e Tecnologia).
- `wp option get nav_menu_options` → `{"0":false,"auto_add":[]}` ✅
- `curl https://www.ocafezinho.com/` → `grep balão` = **0**, `grep -i cassino` = **0**; menu renderiza só os 10 itens legítimos (topo e rodapé).

## 5. PENDÊNCIAS (aguardando decisão do Miguel)

1. **Página 264513 segue PUBLICADA** — acessível pela URL direta e indexável. Só perdeu o link do menu. Opções: lixeira / manter / noindex.
2. **Conta rhyandemeira (editor)** e padrão de publis — autorizado ou não? Auditar 5470/2018 também?
3. Páginas-publi antigas (MostBet 261667 etc.) — destino?

### Páginas recentes por autor (levantamento 06/08)

| ID | Título | Data | Autor |
|---|---|---|---|
| 264513 | O jogo do balão no Brasil: … jogo de cassino | 2026-08-06 | 5749 |
| 263412 | 4 Melhores Ferramentas de Conversão… | 2026-07-29 | 2018 |
| 261667 | Revisão do MostBet Plataforma de Jogos | 2026-07-14 | 5749 |
| 261269 | Como verificar o status de direitos autorais… | 2026-07-02 | 5470 |
| 261003 | Keeta Delivery e Keeta São Paulo… | 2026-06-29 | 5470 |
| 258664 | Como a inovação tecnológica está ajudando famílias… | 2026-06-15 | 5749 |
| 256652 | Como Limpar Alto-Falante de Celular… | 2026-06-06 | 5749 |
| 246677 | Programa de Afiliados TEMU… | 2026-05-13 | 2018 |

## 6. Rollback (se um dia precisar)

- Re-adicionar item ao menu: `wp menu item add-post 21062 <page_id>` (ou wp-admin → Aparência → Menus).
- Re-ligar auto-add: restaurar `nav_menu_options` de `/root/backup_menu_fix_20260806/nav_menu_options.bak.json`.

## 7. Lições

- `nav_menu_options.auto_add` é a "porta dos fundos" que joga qualquer página nova no menu — em site com múltiplos editores/publis, **sempre desligado**.
- O menu do topo e do rodapé do Cafezinho são o MESMO objeto (term 21062) — mexer num mexe nos dois (+ AMP).
- wp-cli nesse servidor cospe um PHP Notice + dump de `wp_bs_pagination` (bootstrap do tema faz eval sem HTTP_HOST) — ruído cosmético, usar `2>/dev/null | tail`.

— ZCode (Kimi K3), 2026-08-06
