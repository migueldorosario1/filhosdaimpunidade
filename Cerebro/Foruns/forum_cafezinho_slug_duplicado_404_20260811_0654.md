# Fórum — Post 404 por slug duplicado (O Cafezinho)

**Data:** 2026-08-11 ~06:15–06:55 BRT
**Agente:** ZCode (GLM-5.2 Z.ai)
**Sessão:** chat direto, workspace ZCodeProject
**Tema:** Bug de slug duplicado → post publicado retornando 404

## O que aconteceu / Estado final

### Problema
Post "Fãs da Liga dos Campeões e da Premier League na Tailândia: A Nova Era do Entretenimento Digital no Futebol" publicado em 10/08/2026 12:33 retornava **404** na URL sem sufixo; o post bom estava preso na URL `...no-futebol-2/`.

### Causa raiz (confirmada via wp-cli + SQL)
- O publicador criou **duas vezes** o mesmo post (intervalo de 1 minuto):
  - **265112** (12:32:09) → ocupou o slug limpo `...no-futebol`
  - **265113** (12:33:12) → recebeu `-2` (slug original já ocupado)
- Depois a 265112 foi para a **lixeira** (status `trash`, slug virou `...no-futebol__trashed`).
- O WordPress **não libera o slug automaticamente** quando o post vai pra lixeira → post bom ficou preso no `-2`.
- Conteúdo dos dois era quase idêntico (mesma imagem base `thailand-football-digital-era`, mesmo título; hashes diferentes por imagem `-1` vs sem sufixo e variações de formatação).

### Ação executada (ordem Miguel: "limpar o slug, renomear")
1. **Backup** do fantasma 265112 → `/tmp/backup_post_265112_fantasma_20260811_065146.txt` (8958 bytes) no servidor.
2. **Exclusão permanente** do fantasma 265112 (`wp post delete 265112 --force`).
3. **Renomeação do slug** do post bom 265113: `...no-futebol-2` → `...no-futebol` (limpo).
4. Meta `_backup_slug_com_traco_2` registrada no 265113 (histórico).
5. **Cache WP Rocket** limpo (`wp cache flush`).
6. Verificação Yoast: sem `noindex` (indexação normal) + canonical automático (agora aponta pra URL limpa).

### Prova (testes de mesa)
- URL limpa `...no-futebol/` → **HTTP 200** ✅ (título + conteúdo corretos)
- URL `-2` `...no-futebol-2/` → **HTTP 404** (Google descarta sozinho do índice)
- SQL confirma: só existe o 265113, `post_name` limpo, fantasma `COUNT=0`.

## O que falta / Próximos passos

- **Para o Miguel (opcional):** no Google Search Console do ocafezinho, pode-se solicitar "Inspecionar URL" → "Pedir indexação" para a URL limpa acelerar a indexação. A URL `-2` (se já tivesse sido indexada) sai sozinha pelo 404.
- **Monitorar:** confirmar em alguns dias que a URL limpa está indexada e a `-2` sumiu do índice.
- **Prevenção:** investigar no `motor_publicador.py` por que ele publicou duas vezes seguidas (possível duplo-click / retry mal configurado) — não feito nesta sessão.

## Decisões
- Miguel escolheu **limpar o slug** (opção recomendada) em vez de `noindex` ou manter `-2` + 301.
- `noindex` descartado: a URL quebrada dava 404, e o Google não indexa 404 (autocura).

## Acessos usados
- SSH alias `cafezinho-wp` (`us65.serverdo.in`), wp-cli em `/var/www/ocafezinho` (Cofre de Chaves).

---

## ADENDO — Redirecionamento 301 (~07:10)

**Motivo:** verificação de indexação revelou que a URL `-2` **estava indexada no Google** (publicador publicou 10/08, Google indexou rápido). Sem redirect, quem clicasse no resultado do Google da `-2` cairia em 404 por dias/semanas. Miguel autorizou o 301.

### Ação executada
1. **Backup** da config Nginx → `/etc/nginx/sites-enabled/ocafezinho.com.conf.bak_pre_redirect_20260811_070839` (no servidor).
2. **Inserida regra** no server block 443 (linha 153-156), antes do `location /`:
   ```nginx
   location = /fas-da-liga-dos-campeoes-e-da-premier-league-na-tailandia-a-nova-era-do-entretenimento-digital-no-futebol-2/ {
       return 301 https://$host/fas-da-liga-dos-campeoes-e-da-premier-league-na-tailandia-a-nova-era-do-entretenimento-digital-no-futebol/;
   }
   ```
   Usa `$host` (preserva www/não-www do visitante) em vez de `$server_name` (que resolvia só para `ocafezinho.com` sem www).
3. `nginx -t` → sintaxe OK. `systemctl reload nginx` → OK.
4. Site todo confirmado no ar (homepage 200).

### Prova
- `www.ocafezinho.com/...no-futebol-2/` → **HTTP 301** → redireciona para `www.ocafezinho.com/...no-futebol/` (HTTP 200) ✅
- Homepage e demais páginas intactas.

### Stack confirmada
- **Nginx puro 1.28.0** (sem Apache backend — `.htaccess` é ignorado, está ali só como padrão WP).
- PHP 8.3 via fastcgi pool `127.0.0.1:9083`.
- Config: `/etc/nginx/sites-enabled/ocafezinho.com.conf`.

## Estado final consolidado
- ✅ Post no ar na URL limpa (HTTP 200)
- ✅ URL `-2` redireciona 301 → URL limpa (quem vem do Google cai no lugar certo)
- ✅ Fantasma excluído, cache limpo, Yoast index normal
- **Falta (opcional, Miguel):** pedir indexação da URL limpa no Google Search Console pra acelerar. O Google vai consolidar o peso da `-2` na URL limpa via 301.
