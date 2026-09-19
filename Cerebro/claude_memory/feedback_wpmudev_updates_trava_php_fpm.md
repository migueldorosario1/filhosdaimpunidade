---
name: feedback-wpmudev-updates-trava-php-fpm
description: "Plugin wpmudev-updates do WPMU DEV trava PHP-FPM do WP Cafezinho ao ser instalado via wp-admin — renomear pasta NÃO basta, precisa remover do active_plugins no banco e restartar PHP-FPM. Aplicável a qualquer plugin pesado."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e29ff28c-6410-49eb-9d07-9c7aa88707ce
---

**Não instalar plugins WPMU DEV (ou qualquer plugin que faça boot pesado: HTTP externo, scan filesystem) no WP Cafezinho via wp-admin sem janela de manutenção. Se site travar pós-install, renomear pasta do plugin NÃO basta — sempre remover do `active_plugins` no banco + restart PHP-FPM.**

**Why:** Caso fundador 28/06/2026 22:34 BRT — Miguel instalou `wpmudev-updates` via wp-admin do `controle.ocafezinho.com`. Plugin começou a fazer operações pesadas no boot (provavelmente verificar updates remotos / scan / autoinstall). Cada request PHP demorou 60-160s, `child exited on signal 15 SIGTERM`, pool `www74` esgotou, site WP foi pra HTTP 500 generalizado. Claude tentou primeiro renomear pasta `mv wpmudev-updates → wpmudev-updates.DISABLED_*` mas NÃO destravou — o `wp_options.active_plugins` (PHP serialized array, 41 entries) ainda referenciava `s:40:"wpmudev-updates/update-notifications.php"`. WP entrava em loop fatal tentando `include` arquivo inexistente, segurando worker indefinidamente. Cura definitiva (~5min total): backup do active_plugins → reconstruir array via PHP CLI (`unserialize → array_filter → serialize`) sem a entrada problemática → `UPDATE wp_options` → `systemctl restart php7.4-fpm`. Smoke 5/5 PASS pós-restart, homepage voltou em 70ms.

**How to apply:**

1. **Antes de instalar plugin WPMU DEV** (ou similar pesado: Hummingbird, Defender, Smush variantes, Hustle, Forminator, Snapshot, Shipper, Branda) — usar SFTP + ativar via `wp-cli` em vez de wp-admin. Idealmente em janela de manutenção (madrugada BRT).

2. **Se site travar pós-install de qualquer plugin** (sintomas: HTTP 500, latência PHP >10s, `child exited on signal 15`, `upstream timed out`), o protocolo é:
   - Renomear pasta do plugin para `.DISABLED_TIMESTAMP/` (rápido pra confirmar suspeito)
   - **OBRIGATÓRIO:** remover entrada do plugin no `wp_options.active_plugins`:
     ```bash
     # backup do array atual
     mysql -uocafezinho -p"..." ocafezinho -sN -e "SELECT option_value FROM wp_options WHERE option_name='active_plugins'" > /tmp/active_plugins_backup_$(date +%s).txt
     # reconstruir sem plugin problemático via PHP CLI
     php -r 'unserialize → array_filter → serialize'
     # update no banco
     mysql ... -e "UPDATE wp_options SET option_value = NEW_SERIALIZED WHERE option_name = 'active_plugins'"
     ```
   - **OBRIGATÓRIO:** `systemctl restart php7.4-fpm` (mata workers travados + limpa OPcache)
   - Smoke test homepage + admin + REST API + 1 post + 1 imagem antes de declarar resolvido

3. **Regra genérica do padrão:** qualquer plugin removido do disco SEM remover do `active_plugins` causa loop fatal porque WP tenta `include` arquivo inexistente em cada request. Vale para qualquer plugin, não só WPMU.

4. **wp-cli `plugin deactivate <nome>`** vai FALHAR se a pasta já foi renomeada (erro `"plugin could not be found"`) — neste caso só SQL direto resolve. Por isso o protocolo é desativar PRIMEIRO via wp-cli (com pasta intacta), depois remover pasta. Mas se o site já está em 500, wp-cli também pode hangar; pular pra SQL direto.

5. **Healthcheck preventivo sugerido (B-022 patch §92 futuro):** cron 1min checando `pgrep php-fpm | wc -l` + p95 latência PHP — alerta se workers ativos >2min OU se p95 >10s. Detectaria esse incidente em <2min.

Veja também [[reference-servidor-wp-cafezinho-ssh]] (como conectar) e bug [[B-022]] na MEMORIA_BUGS_ATUAL.md.
