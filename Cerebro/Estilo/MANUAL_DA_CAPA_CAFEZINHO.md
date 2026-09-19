# 📸 MANUAL DA CAPA DO CAFEZINHO — onde encontrar foto, como escolher, como aplicar

**Criado:** 14/09/2026 ~16:1x BRT · **Autor:** ZM (ZCode/GLM-5.3), ordem Miguel 14/09 ~16:0x («coloca no cérebro instruções completas para o agente já saber onde encontrar a foto»).
**Para quem é:** os capadores de plantão — **AGY-Miguel (Antigravity CLI), AGY-LAURA/AL, Claude Laura (CL), Claude Miguel (CM)** — e qualquer agente que o alerta escalar. Todos os quatro já sabem fazer capa; este manual entrega o mapa completo de fontes e o método para fazer RÁPIDO e SEM ERRO.
**Gatilho de uso:** você recebeu bloc `ALERTA-CAPA-V41-*` ou `ESCALACAO-CAPA-V41-*` na ponte → draft V4.1 esperando capa. Protocolo de turno/handoff: `Foruns/RUNBOOK_RODIZIO_CAPADOR_V41.md` (CM). Ao ser escalado, você tem 30min para agir ou postar ACK com motivo (senão o secundário assume).

---

## 1. As 4 rotas para conseguir a imagem (ordem de preferência)

### ROTA 1 — Banco de mídia V4 (NYC) — já tem curadoria e gates de visão
O pipeline de imagem da casa (`/root/v4_labs/codigo/`, NYC `ssh nyc`) já busca, valida identidade por visão dupla (DeepSeek × Qwen) e pontua candidatas. É o caminho mais seguro para pessoa nomeada.
```
ssh nyc
cd /root && set -a; . chaves_novas.env; . chaves.sh; set +a    # ORDEM importa
python3 -m codigo.featured_image_runtime_cli /tmp/pedido.json --allow-network --execute --root /root/v4_labs
```
- `pedido.json` mínimo: `{"item_id": "<PID>", "title": "<título>", "primary_entity": "<pessoa/ente principal>", "editoria": "<vertical>", "requires_person": true|false}`.
- `--execute` persiste a decisão em `agent_data/v4/media/pipeline_decisions/` (NUNCA sobe ao WP sozinho — a aplicação é sua, passo §5).
- Gates que ele já aplica (confie no veredito): mínimo **1200x675px**; sem animadas; sem screenshot/logo/montagem; pessoa nomeada exige **conta oficial Flickr OU metadata confirmada** (Commons/Openverse sozinhos NÃO valem para pessoa); score final mínimo 70.
- Lotes aprovados ficam no acervo auditado; a promoção mecânica roda no NYC (`v4_media_mechanical_promoter.py`, cron 6/6h).

### ROTA 2 — Busca direta em fontes abertas (a mais usada na prática)
**Flickr oficial (sempre CC BY — a melhor fonte para político brasileiro):**
- Agência Senado: `https://www.flickr.com/photos/agenciasenado/`
- Câmara dos Deputados: `https://www.flickr.com/photos/camaradosdeputados/`
- Palácio do Planalto / Ricardo Stuckert: `https://www.flickr.com/photos/palaciodoplanalto/` (CC BY / CC BY-SA)
- Governo do CE, MEC, Alece, PT: ver `Memorias/BANCO_LINKS_FOTOS_CEARA_E_LIDERANCAS.md` (modelo de banco por estado — replicável para outros estados).
- 🔴 **Nunca usar:** contas `pl22`, `politico…` e similares com licença "All rights reserved" (já auditadas e descartadas pela casa, 10/09).

**URL direta do Flickr (receita da casa):** a página não entrega a imagem no HTML rasteiro — `curl -s <página-da-foto> | grep -o 'live.staticflickr.com/[^"]*'` (2 níveis de path) e sufixo do arquivo `_b` = 1024px. Confirmar dims ≥1200 de largura (se `_b` não bastar, subir o tamanho).

**Wikimedia Commons:** busca `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=<ENTIDADE>&iiurlwidth=1920…` — **UA obrigatório `Cafezinho-V4-MediaScout/1.0`** (sem UA dá 403) e `iiurlwidth` máximo 1920 (2400 devolve 400). Desempate de identidade canônico: hash **SHA1 da imagem → `list=allimages&aisha1=`** no Commons devolve o nome canônico do arquivo.

**Outras fontes já usadas e aprovadas pela casa:** Agência Brasil/EBC e Fotos Públicas (política nacional), STF oficial (= Public Domain Mark), Kremlin.ru (CC BY 4.0), GODL-India (BRICS/Índia), NASA/U.S. Navy/USCG (domínio público), TV ALERJ (CC BY 3.0), Panoramio→Wikimedia. Para temas novos: preferir fonte governamental/agência com licença explícita na página.

### ROTA 3 — O próprio WordPress do Cafezinho (biblioteca de mídia)
```
cd /var/www/ocafezinho && wp media list --search="<termo>" --fields=ID,post_title,post_date,guid --allow-root | head
```
- Ótimo para tema recorrente (STF, Lula, eleições, prédios, urnas) — a biblioteca tem milhares de fotos já licitadas.
- 🔴 **MD5 único (§86/Emenda 6):** NÃO reaproveitar imagem que já é capa de outro post publicado — o gate devolve HTTP 400 se o MD5 do carimbo bater. Checar a quem a imagem pertence antes.

### ROTA 4 — Capa IA gerada (TECNOLOGIA/IA/abstrato — Emenda 11)
- Para editoria tecnologia, imagem IA é PADRÃO: «capa IA gerada OK, crédito **Ilustração: Cafezinho / <gerador>** na legenda» (Emenda 11, 26/08). SEM texto escrito dentro da imagem.
- Gerador da casa (NYC): `cd /root && . chaves.sh && python3 -c "from <modulo_gerador> import generate_editorial_image; generate_editorial_image({'titulo':…, 'resumo':…, 'secao':'tecnologia'}, caminho_download='/tmp/capa_<PID>.jpg')"` — tenta banco real antes; para forçar IA: `forcar_ia_cartoon=True`. Fallback histórico: **flux-pro** (fal.media).
- Os attachments `cafezinho-<hash>` (autor 5470, 2h/2h) na biblioteca são ILUSTRAÇÕES IA já geradas e quase sempre órfãs — inspecione e reutilize quando servir (crédito "Ilustração: Cafezinho").

## 2. Licenças — pode e não pode

| PODE | NÃO PODE |
|---|---|
| CC BY 2.0/3.0/4.0, CC BY-SA | CC **NC** (não comercial) e **ND** (sem derivativos) |
| Domínio público / PD / PDM (STF, NASA, US Navy, Kremlin.ru é CC BY 4.0) | "All rights reserved" (contas Flickr pessoais/pl22) |
| Fotos oficiais de governo/agência pública com atribuição | Print de tela, logo, montagem de terceiros, foto de rede social alheia |
| Montagem da casa = 2+ fotos livres c/ créditos individuais (padrão consagrado) | Foto de agência paga (Reuters/EFE/AFP) baixada sem licença |

**Atribuição vai SÓ na legenda (caption) do attachment — NUNCA "Foto: …" no corpo do post** (ordem Miguel 11/09: `grep -i 'foto:' post_content` deve dar 0 antes de publicar).

## 3. Regras editoriais (o que a casa já pagou para aprender)

1. **Pessoa nomeada / geopolítica / eleição = FOTO JORNALÍSTICA REAL E RECENTE** da pessoa (Emenda 12). Validar QUEM está na foto (erro clássico: homônimos, assessor parecido). Se houver dúvida de identidade e não houver metadata confiável: trocar a foto ou marcar p/ revisão — o pipeline usa visão dupla justamente por isso.
2. **Legenda descreve os pixels** ("Eduardo Paes discursa na campanha de 2026"), não o que a matéria opina. `alt_text` = descrição acessível da cena.
3. **Blacklist de fotos datadas** para figuras que envelheceram mal visualmente (caso Ricardo Barros 267037, 22/08): antes de usar attachment antigo de político, conferir se a aparência bate com o presente.
4. **Canibalização visual:** capa já usada em post recente do mesmo tema = confusão para o leitor; imagem nova ou ângulo novo.
5. **Dedup 72h** (gate 5): antes de publicar, `wp db query "SELECT ID,post_title FROM wp_posts WHERE post_status='publish' AND post_title LIKE '%<termo>%' AND post_date >= NOW() - INTERVAL 72 HOUR" --allow-root`.
6. Crédito sempre completo na legenda: `… (Foto: <FOTÓGRAFO> / <INSTITUIÇÃO> — <LICENÇA>)` ou `(Ilustração: Cafezinho / <gerador> — gerada por IA)`.

## 4. Dimensões e qualidade

- Mínimo **1200x675** (16:9 horizontal); ideal 1600-1920 de largura.
- Sem marca d'água, sem borda, sem texto queimado na imagem.
- Pessoas: rosto legível, enquadramento que sobre viva ao crop 16:9 do tema (`crop_safe`).

## 5. Aplicação da capa (passo-a-passo wp-cli — a ordem importa!)

```bash
ssh cafezinho-wp
cd /var/www/ocafezinho
# 1) upload (crédito SÓ aqui — caption/legenda; alt acessível; título descritivo)
wp media import "<URL_ou_arquivo>" --post_id=<PID> --featured_image \
  --title="<descrição curta>" --caption="<legenda + (Foto: …)" --alt="<descrição acessível>" \
  --porcelain --allow-root        # devolve o attachment ID
# 2) img_check ANTES do thumbnail (gate de visão exige media_id casado — Emenda 11 lição 26/08)
MD5=$(md5sum wp-content/uploads/2026/09/<arquivo> | cut -d' ' -f1)
wp post meta update <PID> _cafezinho_img_check '{"ok":true,"ts":"<agora BRT>","via":"<seu-slug>","image_kind":"real|ia_gerada","media_id":<ATT_ID>}' --allow-root
wp post meta update <PID> _cafezinho_featured_carimbo '<MD5>' --allow-root
# 3) thumbnail
wp post meta update <PID> _thumbnail_id <ATT_ID> --allow-root
# 4) autoria (§136) + metas do rodízio (RUNBOOK §4.1)
wp post meta update <PID> _publicado_por <seu-slug> --allow-root
wp post meta update <PID> _cafezinho_capa_operador <seu-slug> --allow-root
wp post meta update <PID> _cafezinho_capa_fonte "<url ou ilustracao-IA-<gerador>>" --allow-root
# 5) publicar (ou agendar future em slot de 20min — café-slot-20min)
wp post update <PID> --post_status=publish --allow-root     # se direto
# 6) reindex + cache
wp eval 'wp_update_post(["ID"=><PID>]);' --allow-root
wp cache flush --allow-root
# GOTCHA Rocket: páginas cacheiam sob controle.ocafezinho.com/.../index-https.html — se a URL servir velho:
grep -rl "<trecho-do-título>" wp-content/cache/ | xargs rm -f
```
- Via REST também funciona: `featured_media` direto no payload (provado no 270826, 14/09).
- Publicou? Provar: `curl -s https://www.ocafezinho.com/?p=<PID>` → 200 + capa no body.

## 6. Os 6 gates V4.1 (regra 29/08 — nada publica sem os 6)

1. `_v4_versao = 4.1` · 2. `post_date < 72h` no publish · 3. `_thumbnail_id` preenchido · 4. `_cafezinho_img_check` APROVADA · 5. dedup 72h de título · 6. Regional só pesquisa/bastidor. + GATE §86 carimbo↔featured casado.

## 7. Escalação automática (como o alerta te chama)

O script `/root/alerta_capa_v41.py` (cron 30/30min no cafezinho-wp) escala SOZINHO, sem passar pelo Miguel:
- **Nível 1 (≥6h sem capa):** bloc `ALERTA-CAPA-V41-*` na ponte → capador da faixa age.
- **Nível 2 (≥12h OU fila ≥5):** bloc `ESCALACAO-CAPA-V41-*` chamando TODOS os aptos (AGY-Miguel, AGY-LAURA, CL, CM) — quem pegar primeiro aplica; ACK na ponte em 30min ou o próximo assume (emergência §6 do RUNBOOK).
- **Nível 3 (≥24h):** ÚNICO momento em que o Miguel é incomodado no Telegram (escalação esgotada — 1 aviso/6h). Não deixe chegar aqui.

## 8. Fontes de consulta rápida

- `Foruns/RUNBOOK_RODIZIO_CAPADOR_V41.md` — turnos, handoff, metas de operador, emergência.
- `Memorias/memoria_capas_v41_pipeline_deepseek_20260829.md` — o pipeline técnico completo (gates de visão, schema do pedido, bugs já corrigidos).
- `Memorias/memoria_emenda11_capa_ia_tecnologia_lncc_20260826.md` — capa IA passo-a-passo (generate → upload → img_check ANTES thumb → cache).
- `Memorias/BANCO_LINKS_FOTOS_CEARA_E_LIDERANCAS.md` — banco de links por instituição/liderança (modelo p/ outros estados).
- `Foruns/forum_auditoria_pipeline_capa_parado_20260914.md` — por que o passo capa é de agente (causa raiz H4) e o nascimento do alerta.
- `Memorias/memoria_flickr_capas_*` (10/09) — auditoria de contas Flickr: `agenciasenado` OK; `pl22/politico*` proibidas.

— ZM · ZCode/GLM-5.3 · 14/09/2026 ~16:1x BRT
