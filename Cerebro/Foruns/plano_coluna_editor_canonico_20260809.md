# Plano — Portar "Coluna do Editor" do espelho para o canônico

**Data:** 09/08/2026 17:20 BRT
**Autor:** Claude Code (`claude-opus-4-7`)
**Autorização Miguel:** "Pode fazer isso, então, pro Cafezinho Canônico. Mas faz com cuidado, pelo amor de Deus. Cafezinho canônico tem que fazer com muito cuidado."
**Origem:** espelho `cafezinho.news` V1.5 (feito ~14:30 BRT hoje, aprovado por Miguel: "ficou perfeito")
**Alvo:** canônico `ocafezinho.com` (host `us65.serverdo.in`)
**Escopo mínimo:** só o bloco "Colunas" da home vira "Coluna do Editor" (4 posts do autor 2018 lado a lado desktop/iPad, 1 no mobile) + filter de avatar OpenID pra usar a foto real do Miguel no lugar do mystery man do Gravatar.

---

## 0. Diferenças espelho ↔ canônico que exigem cuidado adicional

| Item | Espelho | Canônico | Implicação |
|---|---|---|---|
| Autores no bloco Colunas | 2 (Miguel + Rhyan) | **21 colunistas** | Vou eliminar 20 pra deixar só o Miguel — grande mudança visual |
| Basic Auth | `cafezinho`/`000` | público, sem auth | Verificação HTTP direto |
| V1.4 reorder ("Colunas antes de Recentes") | JÁ aplicado (27/07) | **NÃO sei se está aplicado** | Precisa Fase 0 confirmar ordem atual do `front-page.php` |
| Mu-plugin `cafezinho-lab-visual.php` | JÁ existe | **NÃO existe** ou pode ter outro nome | Vou criar SÓ um mu-plugin novo isolado (`cafezinho-avatar-openid.php`), sem trazer o CSS/JS todo do lab |
| Sync horário | puxa DO canônico | é a fonte | **Nenhum risco de sync sobrescrever** — sync `:17 * * * *` toca só posts/uploads/`wp_highlights`, não tema/mu-plugins (confirmado no fórum lab visual) |
| Tema ativo | `ocafezinho-portal` | provavelmente idêntico | Fase 0 confirma |
| Cache CDN | não sei | pode ter Cloudflare | Vou verificar; se tiver, avisar Miguel pra purge |

---

## 1. Estratégia — cirúrgica, não portar o lab inteiro

**Duas mudanças mínimas:**

### Mudança A — bloco Colunas no `front-page.php`
Substituir SÓ o `<?php if( !empty( $columnists ) ): ?> ... <?php endif; ?>` por uma versão que:
- Query `WP_Query` com `author=2018 posts_per_page=4`
- Cabeçalho: xicrinha (`img/cafezinho.svg`) + `get_avatar(2018, 48)` + "Coluna do Editor" + nome "Miguel do Rosário"
- Grid Bootstrap `row-cols-1 row-cols-md-4` (1 mobile, 4 md+)
- Cards 2, 3 e 4 recebem `d-none d-md-block` (só desktop/iPad mostram)
- Cada card: thumbnail + título + data (sem os 2 "small extras" que existiam no espelho e canônico originais)
- Preserva `array_push( $excludes, get_the_ID() )` pra não duplicar nos Recentes
- Se V1.4 reorder NÃO estiver no canônico, mantém o bloco na posição original (sem `ob_start`)

### Mudança B — mu-plugin novo, isolado
Arquivo: `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-avatar-openid.php` (uns 40 linhas)
- Só o filter `get_avatar_url` que substitui mystery man por `moopenid_user_avatar` quando o usuário tem essa meta
- **Não traz** o painel Histórico, tipografia fluida, menu pills, footer redesenhado etc. do lab do espelho
- Nome propositalmente diferente do `cafezinho-lab-visual.php` — deixa claro que é feature aditiva mínima
- Pré-condição: pasta `mu-plugins/` já existe (Fase 0 verifica; senão cria)

**O que NÃO vou fazer:**
- Não vou instalar o `cafezinho-lab-visual.{php,css,js}` completo do espelho (bloco escopo).
- Não vou alterar tema além do bloco Colunas específico.
- Não vou reorganizar seção da home (Manchete/Notícias/Colunas/Recentes) — se V1.4 reorder não estiver no canônico, o bloco Colunas fica na posição que já tem hoje.
- Não vou tocar outros arquivos do tema.
- Não vou publicar/deletar/mover posts.
- Não vou mexer em plugins ativos ou config PHP.
- Não vou purgar cache CDN sem confirmar com Miguel (pode ter estratégia própria).

---

## 2. Fases de execução

### Fase 0 — Descoberta read-only (5 min, zero risco)

Checar sequencialmente:
0.1. `ssh root@us65.serverdo.in` funciona?
0.2. `wp core version --path=/var/www/ocafezinho` — versão WP
0.3. `wp theme list --status=active --path=/var/www/ocafezinho` — qual tema ativo (esperado: `ocafezinho-portal`)
0.4. `ls /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php` — existe?
0.5. Baixar front-page.php canônico pra `/tmp/cafezinho_canonico_20260809/front-page.php.original`
0.6. `grep -n 'columnists\|Colunas' front-page.php` — localizar bloco e comparar com espelho
0.7. Verificar se `ob_start`/`ob_get_clean` estão presentes (indica V1.4 já aplicada)
0.8. `ls img/cafezinho.svg` — xicrinha existe?
0.9. `wp user get 2018 --field=display_name` — confirmar "Miguel do Rosário"
0.10. `wp user meta get 2018 moopenid_user_avatar` — foto Google Photos existe?
0.11. `ls wp-content/mu-plugins/` — listar mu-plugins existentes (evitar colisão de nome)
0.12. `wp cache flush --path=/var/www/ocafezinho` disponível? (pra saber se depois preciso rodar)
0.13. `curl -sI https://ocafezinho.com/` — checar headers (Cloudflare? Cache-Control?)

**Critério de parada Fase 0:**
- Se qualquer 0.1-0.10 falhar → PARAR, reportar ao Miguel, não seguir.
- Se `moopenid_user_avatar` não existir no canônico → adaptar Mudança B (pode ser plugin OpenID diferente com meta diferente).
- Se tema for diferente de `ocafezinho-portal` → PARAR, replanejar.

### Fase 1 — Backup preventivo triplo (2 min)

1.1. **Backup no droplet, ao lado do original:**
```bash
sudo -u www-data cp /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php \
                    /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php.bak_pre_coluna_editor_20260809_HHMMSS
```
1.2. **Cópia versionada em /root** (mesmo padrão do lab):
```bash
mkdir -p /root/coluna_editor_canonico_versoes/
cp /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php \
   /root/coluna_editor_canonico_versoes/front-page_pre_coluna_editor_20260809_HHMMSS.php
```
1.3. **Download local (na minha máquina)** — 3ª cópia offline:
```bash
scp root@us65.serverdo.in:/var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php \
    /tmp/cafezinho_canonico_20260809/front-page.php.bak_TRIPLE
```
1.4. Computar SHA-256 dos 3 backups e garantir que os 3 são idênticos.

### Fase 2 — Edição do bloco Colunas (5 min)

2.1. Editar cópia local `/tmp/cafezinho_canonico_20260809/front-page.php` — substituir apenas o bloco Colunas.
2.2. Preservar TUDO ao redor (Manchete, Notícias, ordem, Recentes, includes de ads, tags, comentários PHP).
2.3. Se V1.4 reorder JÁ estiver aplicado no canônico → uso mesma abordagem `ob_start`/`ob_get_clean` do espelho.
2.4. Se V1.4 reorder NÃO estiver → deixo o bloco Colunas na posição original, SEM buffer.
2.5. `php -l` local antes de subir.
2.6. Upload:
```bash
scp /tmp/cafezinho_canonico_20260809/front-page.php root@us65.serverdo.in:/tmp/front-page.php.new
ssh root@us65.serverdo.in "install -o www-data -g www-data -m 664 /tmp/front-page.php.new \
    /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php && \
    php -l /var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php"
```
2.7. Cópia da versão nova em `/root/coluna_editor_canonico_versoes/front-page_coluna_editor_v1.0_canonico_20260809_HHMMSS.php`.

### Fase 3 — mu-plugin avatar OpenID (2 min)

3.1. Verificar se `moopenid_user_avatar` existe no canônico pro user 2018 (Fase 0.10).
3.2. Se SIM: criar `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-avatar-openid.php` (~40 linhas — só o filter).
3.3. Se NÃO: adaptar o filter pra outra meta ou usar avatar padrão do WP; reportar ao Miguel.
3.4. `php -l` local + upload + `install -o www-data`.
3.5. Cópia versionada em `/root/coluna_editor_canonico_versoes/`.

### Fase 4 — Verificação HTTP + visual (5 min)

4.1. `curl -s https://ocafezinho.com/ -o home_after.html -w "HTTP %{http_code} · size %{size_download}\n"` — HTTP 200 obrigatório.
4.2. `grep -c "Coluna do Editor" home_after.html` — deve ser ≥ 1.
4.3. `grep -c "coluna-editor-item" home_after.html` — deve ser 4.
4.4. `grep -oE "src=['\"][^'\"]*avatar[^'\"]*['\"]" home_after.html | head -1` — verificar se avatar é googleusercontent (não `d=mm`).
4.5. Screenshots headless Chrome: desktop 1440 · iPad 1024 · mobile 390 → crops da seção Coluna do Editor.
4.6. Comparar visualmente com o espelho — se diferir muito, reportar.
4.7. Cache: se Cloudflare, avisar Miguel; se cache WP interno, `wp cache flush`.

**Critério de PARADA + ROLLBACK IMEDIATO se:**
- HTTP ≠ 200
- 500/502/504 em qualquer página da home
- Erro fatal PHP visível
- Cards não renderizam (grep coluna-editor-item < 4)
- Home visualmente quebrada (ex: layout descolado, resto da página sumindo)

### Fase 5 — Script de rollback (pré-instalado, pronto pra rodar)

Script `/root/coluna_editor_canonico_versoes/rollback_coluna_editor_canonico.sh` já pronto ANTES da Fase 2:

```bash
#!/bin/bash
set -e
STAMP="20260809_HHMMSS"
THEME=/var/www/ocafezinho/wp-content/themes/ocafezinho-portal
MU=/var/www/ocafezinho/wp-content/mu-plugins

# 1. Restaura front-page.php
cp "${THEME}/front-page.php.bak_pre_coluna_editor_${STAMP}" "${THEME}/front-page.php"
chown www-data:www-data "${THEME}/front-page.php"

# 2. Remove mu-plugin novo
rm -f "${MU}/cafezinho-avatar-openid.php"

# 3. PHP lint + curl teste
php -l "${THEME}/front-page.php"
curl -sI https://ocafezinho.com/ | head -3

echo "ROLLBACK OK"
```

Doc `rollback_MANUAL.md` com passo-a-passo caso script falhe:
1. SSH `root@us65.serverdo.in`
2. `cp` do backup pra front-page.php
3. `rm` do mu-plugin
4. Verificar `curl -sI https://ocafezinho.com/` = 200
5. Se cache CDN, purgar (via painel Cloudflare ou API)
6. Se ainda quebrar: contatar Miguel

### Fase 6 — Registro (5 min)

6.1. Anotar em `Cerebro/Foruns/forum_lab_visual_cafezinho_news_20260720.md` uma seção nova "**Port ao canônico V2.0**" com timestamps, backups, resultado.
6.2. Ping no `canal_trindade.md` avisando ZCode/GLM/outros que a mudança foi ao ar.
6.3. Se aprovado por Miguel após 24h no ar, salvar memória `feedback_lab_visual_canonico_como_portar_do_espelho.md`.

---

## 3. Rollback rápido — cenários

| Cenário | Ação |
|---|---|
| PHP fatal error visível na home | `cp` do `.bak_pre_coluna_editor_*` sobrescreve front-page.php → home volta em segundos |
| Home renderiza mas Coluna do Editor não aparece | mesmo rollback (talvez `moopenid_user_avatar` era diferente ou ACF `columnists` field bloqueou) |
| Home renderiza mas quebra layout | rollback + reportar visual antes/depois |
| Cache CDN preso mostrando versão antiga por muito tempo | avisar Miguel para purge; NÃO fazer eu mesmo sem autorização |
| Erro só no mobile ou só no desktop | rollback + investigar CSS media query |
| Sync horário sobrescreve? | Verificado no fórum lab visual: sync não toca tema/mu-plugins. Risco = 0. |
| Outro dev/agente tocou o mesmo arquivo depois | verificar `.bak` == estado atual antes de restaurar; se não bater, PARAR e reportar |

---

## 4. Perguntas em aberto antes de executar

1. **Cache CDN:** o canônico tem Cloudflare? Se sim, preciso purge? Ou você faz?
2. **Janela de execução:** Vou executar agora ou você prefere um horário específico (fora do pico)?
3. **Aprovação pós-Fase 4:** Antes de eu marcar como "concluído", quer ver os screenshots? Ou confia direto?
4. **21 colunistas atuais:** Alguém no fórum vai reclamar de "sumir" com os outros colunistas na home? Isso é decisão editorial sua — só confirmando.

---

## 5. Timing estimado

- Fase 0: 5 min (read-only)
- Fase 1: 2 min (backup)
- Fase 2: 5 min (edit + upload + lint)
- Fase 3: 2 min (mu-plugin)
- Fase 4: 5 min (verify + screenshots)
- Fase 5: 2 min (rollback script + doc, mas já pré-preparado antes)
- Fase 6: 5 min (registro)

**Total: ~25 min** com pausas pra você aprovar entre fases se quiser.

---

## 6. Assinatura

Claude Code (`claude-opus-4-7`) · 09/08/2026 17:20 BRT · plano gravado antes de qualquer touch · autorização Miguel: "Pode fazer, mas com muito cuidado" · nenhuma ação executada até aqui.
