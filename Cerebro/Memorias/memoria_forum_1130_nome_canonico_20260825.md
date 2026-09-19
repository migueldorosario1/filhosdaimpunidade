# 🔬 Memória técnica — Fórum 11:30: nome canônico + correção de posts + incidente slot-20min (25/08/2026)

**Par:** `Foruns/forum_forum_1130_nome_canonico_20260825.md` · **Sessão:** ZCode/GLM-5.3

## Comandos e evidências principais

### Fonte (verificação do nome)
```bash
# playlist oficial do programa no canal TV Fórum
curl -s "https://www.youtube.com/playlist?list=PL0M7rdgIk2iifjePO89emPPttp8cELtUg" | grep -oE 'og:title" content="[^"]+"'
# → FÓRUM ONZE E MEIA
# vídeo-fonte da matéria (oEmbed dá título+canal sem renderizar JS)
curl -s "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=_ipojHkU4fA&format=json"
# → "Flávio Bolsonaro:100 dias sem explicar milhões de Vorcaro para filme | Janja reage a ataque de Renan" / TV Fórum
```

### Correção no WordPress (servidor cafezinho-wp = 190.89.239.65:51439, /var/www/ocafezinho)
- Posts afetados: **267639** (3× corpo + 1× excerpt) e **267498** (1× corpo) — nenhum título.
- Fluxo: backup conteúdo+excerpt (`/root/backups_cafezinho/post_*_pre_forum1130_*.html|txt`) → replace `Fórum 11.6 → Fórum 11:30` via python+wp-cli → verificação por contagem → `rm -rf wp-content/cache/wp-rocket/*` (nota: `wp rocket clean` NÃO existe nesse WP — "not a registered wp command").
- Provas: origem 200 (248.772b, 7× "Fórum 11:30"); produção 200 (60.450b gzip, 7× "Fórum 11:30"); 267498 idem (1×).
- Forense de cache: `grep -rl "Fórum 11.6" /var/www/ocafezinho` = **zero arquivos** → página velha vinha do stale da cadeia NAT (190.89.239.31) / Cloudflare enquanto a origem 404ava; atualizou sozinha quando a origem voltou 200. cf-cache-status: DYNAMIC (CF não cacheia HTML do site).
- Cadeia de entrega: visitante → Cloudflare (DNS laranja) → NAT 190.89.239.31 → nginx 190.89.239.65 (`ocafezinho.com.conf`, PHP 8.3 pool :9083) → WP Rocket (cache `wp-content/cache/wp-rocket/www.ocafezinho.com/<permalink>/index-https.html{,_gzip}`) → MySQL localhost `ocafezinho`.

### 🔴 Incidente: edição virou `future` (cafezinho-slot-20min.php, Emenda 5)
- Mecânica: `wp_insert_post_data` filter; autor-agente (lista `5786,5742,5785,5470,…`) + status publish/future + conflito <20min com OUTRO post (por `post_date_gmt`) → empurra +20min até slot livre; se slot no futuro → `future`.
- Gatilho aqui: vizinho 267641 (Azul) publicado às 18:36:47 GMT, a 1.109s do original 18:18:18 → cascata de pushes → 20:58:18 GMT future → post FORA DO AR (origem 404) sem ninguém notar.
- Restauração (funcionou): `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 wp post update 267639 --post_status=publish --post_date="2026-08-25 15:15:18" --post_date_gmt="2026-08-25 18:15:18"` (≥20min de 17:48:21 e 18:36:47; slug e permalink intactos).
- **Regra para sessões futuras:** correção de post publicado de autor-agente ⇒ passar data E gmt em slot livre, conferir `post_status=publish` depois, provar no ar. (`wp option get _cafezinho_slot20_log` mostra os eventos.)

### Ensino do agente
- `agent_data/personagens_youtube.json` (248 personagens; backup `.bak_pre_forum1130_20260825`): entrada "Fórum 11:30" (aliases: Fórum Onze e Meia, Forum 11:30, Fórum 11 e Meia, **Fórum 11.6**); "Renato Rova" (stub duvidoso) promovido a alias de "Renato Rovai". Casamento por alias = exato casefold (`verifica_nomes.buscar_memoria`) — testado 3/3.
- `agentes_cafezinho/youtube_cafezinho.py` (backup `.bak_pre_forum1130_20260825`):
  - `PROGRAMAS_DIARIOS["11meia"]` → rótulo "Fórum 11:30"; match += ("fórum 11:30","forum 11:30","fórum 11.6","forum 11.6");
  - `_nota_nome_programa(video)` nova (dispara p/ canal/título TV Fórum ou termos do 11meia), injetada no fim do prompt de `analisar()` e no `sistema` de `redigir()`;
  - linha de ajuda interna atualizada ("11meia: Fórum 11:30 … playlist oficial 'Fórum Onze e Meia'");
  - `python3 -m py_compile` OK; teste unitário manual 3/3 (2 disparos TV Fórum, 1 não-disparo Mídia NINJA).

## O que falta
- Nada obrigatório. Opcional: Miguel validar acentuação ("Fórum 11:30" fixado).
- Ronda/CM: nas próximas matérias do programa, conferir que o texto saiu "Fórum 11:30" (o Tribunal Visual/nomes agora tem o banco + prompt).
