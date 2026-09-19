#!/bin/bash
# Rollback do incidente 264522 (backup gerado em 2026-08-12 22:38 UTC)
# Executar como: sudo bash rollback.sh
# Restaura user 5787 pra administrator + posts 264522/264511 pra publish
set -e
cd "$(dirname "$0")"
echo "=== ROLLBACK Incidente 264522 ==="
echo "1. Restaurando user 5787 role administrator..."
sudo -u www-data wp --path=/var/www/ocafezinho --skip-themes --skip-plugins user set-role 5787 administrator
echo "2. Restaurando post 264522 publish..."
sudo -u www-data wp --path=/var/www/ocafezinho --skip-themes --skip-plugins post update 264522 --post_status=publish
echo "3. Restaurando post 264511 publish se foi trashado..."
sudo -u www-data wp --path=/var/www/ocafezinho --skip-themes --skip-plugins post update 264511 --post_status=publish 2>/dev/null || true
echo "=== ROLLBACK COMPLETO ==="
echo "Verifique manualmente:"
echo "  wp user get 5787 --field=roles   # esperado: administrator"
echo "  wp post get 264522 --field=post_status   # esperado: publish"
