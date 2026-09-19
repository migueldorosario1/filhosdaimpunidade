---
name: feedback-crontab-substitui-tudo-nao-merge
description: "NUNCA usar `sudo crontab <arquivo>` sem ler o conteúdo do arquivo primeiro. O comando SUBSTITUI o crontab inteiro pelo arquivo (não faz merge). Caso fundador 08/06/2026 DeepSeek+Antigravity."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

🚨 **`sudo crontab <arquivo>` SUBSTITUI O CRONTAB INTEIRO pelo arquivo — não faz merge.**

**Why:** Em 08/06/2026 ~07:53 BRT o **Antigravity** + ~09:03 BRT o **DeepSeek** independentemente fizeram a mesma operação destrutiva: usaram `sudo crontab /root/crontab_tencent.txt` pra "limpar linhas ferroviárias" — mas `crontab <arquivo>` é destrutivo, sobrescreve TUDO. E o arquivo `crontab_tencent.txt` era um snapshot PRÉ-Maestro v2.1 (de abril/maio 2026), então a operação **reverteu o sistema várias semanas** (perdeu maestro_distribuicao, auditor §95 Kimi, robô liberador, Instagram, coletor social, marcadores PAUSADO).

Custo: 2 caos consecutivos em 14h, perda de produtividade da Trindade inteira pra reconstruir do zero linha por linha. Kimi documentou o segundo incidente em `forum_reconstrucao_crontab_pos_caos_antigravity_20260608.md` e criou 5 backups CANONICO em locais distintos.

**How to apply (antes de tocar crontab):**

1. **NUNCA fazer `crontab <arquivo>` sem antes verificar o conteúdo:**
   ```bash
   diff <(crontab -l) /caminho/arquivo  # comparar
   wc -l /caminho/arquivo                # ver tamanho
   head -5 /caminho/arquivo              # ver topo
   ```
2. **Pra remover linhas específicas, NÃO usar arquivo antigo. Usar:**
   - `crontab -e` (editor interativo seguro)
   - OU `sed` ou `python` sobre o ATUAL: `crontab -l | sed '/padrão/d' | crontab -`
3. **Sempre backup ANTES de mexer:**
   ```bash
   sudo crontab -l > /root/crontab.PRE_<MOTIVO>_$(date +%Y%m%d_%H%M%S).bak
   ```
4. **Arquivos `crontab_*.txt` espalhados em `/root` são MUITAS VEZES desatualizados** — não confiar como fonte de verdade. Pode haver `crontab_tencent.txt`, `crontab_backup_*.txt`, etc. de versões antigas.
5. **Arquivos canônicos a confiar (pós-08/06/2026 09:30 BRT):**
   - `/root/crontab_CANONICO_20260608_0930.txt` (primário)
   - `/root/backups/crontab_SEGURO_20260608_0930.bak`
   - `/home/ubuntu/crontab_SEGURO_20260608_0930.bak`
   - `/tmp/crontab_SEGURO_20260608_0930.bak`

**Scripts perigosos renomeados `.DEPRECATED_FORENSE_20260608` (NÃO restaurar):**
- `/root/religar_site_ordenado.sh` — removia tudo exceto Maestro+Gate
- `/root/generate_crontab.py` — gerava crontab a partir de fonte antiga
- `/root/deploy_crontab_2026_04_09.sh` — aplicava sem verificar
- `/root/crontab_add.sh` — adicionava sem controle
- `/root/crontab_tencent.txt` (em todas suas variantes `.bak`, etc) — fonte antiga

**Cadeia editorial inegociável (Kimi 08/06/2026 09:30 BRT, lição validada):**
> "crontab <arquivo> substitui TUDO. Nunca usar sem verificar o conteúdo do arquivo primeiro. Se precisar editar, usar crontab -e (editor seguro) ou sed -i no spool. Nunca crontab <arquivo_antigo>."

Relacionado: [[feedback_deploy_gate_92]] §92, [[feedback_protocolo_backup_rollback_index_inegociavel]] (backup+rollback+índice), [[project_claude_maestro_definitivo_22mai]] (NUNCA tocar .env/crontab/motor sem aval Miguel).
