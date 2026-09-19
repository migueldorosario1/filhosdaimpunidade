# CEREBRO NODE — Protocolo Apostas/Cassino/Jogo Online = PÁGINA (nunca post)

**Aberto:** 27/08/2026 14:52 BRT · **Redator:** Claude Miguel
**Ordem canônica:** Miguel 26/08/2026 16:52 BRT via **ZM-20260826-020** + reiterada 27/08/2026 14:34 chat CLI direto ao CM
**Status:** VIGENTE PERMANENTE

## Regra

**Todo conteúdo comercial de apostas / cassino / jogo online no Cafezinho existe SOMENTE como `page`, NUNCA como `post`.**

- Autor típico desses conteúdos: **Gabriel Barbosa** (`gabrielbarbosa`, WP ID `5735`, `gabrielbarbosa9001@gmail.com`) — parceria de receita autorizada pelo Miguel dono
- Trava WP instalada (mu-plugin) auto-detecta padrão de funil de afiliado (spintowin, bônus de cadastro, guia de cassino etc.) e converte automaticamente
- Casos que escapam da trava (texto mais editorial que promocional puro, título ambíguo): agente Vigília **converte manualmente** ao detectar

## Por quê

**Editorial:** post canibaliza autoridade Google do domínio em tema de baixa qualidade editorial, aparece em blocos/home/feed RSS, interfere no fluxo de reportagem.

**SEO:** página fica com URL própria, autoridade preservada, não canibaliza reportagens factuais em disputa por tema.

**Comercial:** parceria continua funcionando (Gabriel publica), sem penalizar autoridade do jornal.

## Fluxo canônico (aplicar sempre)

### Cenário A — post criado em `draft` ou `pending`

```bash
# 1. Backup
sudo -u www-data wp post get <ID> --format=json --allow-root > /root/backup_<ID>_pre_page_<YYYYMMDD>.json

# 2. Conversão + publish direto (Miguel 27/08 14:34: "basta fazer um espelho do post para página e mandar link para ele, com imagens, etc")
sudo -u www-data wp post update <ID> --post_type=page --post_status=publish --allow-root

# 3. Verificar URL nova
sudo -u www-data wp post get <ID> --field=url --allow-root

# 4. Cache flush
sudo -u www-data wp cache flush --allow-root
```

### Cenário B — post já publicado como `post`

```bash
# 1. Backup
# 2. Conversão + publish (o post permanece no ar com nova URL de page)
sudo -u www-data wp post update <ID> --post_type=page --post_status=publish --allow-root
# 3. Verificar URL nova + criar 301 da URL antiga pra nova (se der pra fazer via mu-plugin ou htaccess)
# 4. Cache flush + rocket clean
```

Miguel 27/08 14:34 verbatim: *"se o post estiver publicado como post, pode já publicar como pagina de mandar o link para ele. basta fazer um espelho do post para página e mandar link para ele, com imagens, etc"*

### Cenário C — post futuro (ainda a ser criado)

**Gabriel:** publicar diretamente no wp-admin como "Adicionar Nova → **Página**" (não Post). Trava WP não é 100% infalível, então preferência é criar no tipo correto desde o início.

## Email obrigatório pro Gabriel (template)

**Destinatários:**
- `gabrielbarbosa9001@gmail.com` (Gabriel primary)
- `gabrielbarbosa@ocafezinho.com` (Gabriel corporate)
- `migueldorosario@gmail.com` (CC Miguel dono)

**Assunto:**
```
Publipost <tema> (<ID>) convertido para página + publicado — política editorial apostas
```

**Corpo (adaptar):**
```
Gabriel,

O post <ID> ("<título>") foi convertido para página e já está no ar.

Link novo (página):
<URL>

Motivo: pela política editorial do Cafezinho (ordem Miguel, registrada 26/08 via ZM-20260826-020),
conteúdo comercial de apostas/cassino/jogo online só existe no site como PÁGINA — nunca como POST.
Post de apostas canibaliza a autoridade Google do domínio em tema de baixa qualidade editorial,
aparece em blocos/home/feed RSS e interfere no fluxo de reportagem. Página fica com URL própria,
autoridade preservada e sem interferência.

O que foi feito:
- Backup do post original salvo no servidor
- Conversão post → page (mesmo conteúdo, mesmo título, mesmo autor)
- Publicação imediata na URL nova

O que você pode fazer:
- Revisar/ajustar: https://www.ocafezinho.com/wp-admin/post.php?post=<ID>&action=edit
- Próximos publiposts: publique DIRETO como página (Adicionar Nova → Página)

Qualquer dúvida sobre linhas editoriais, direto com o Miguel.

— Claude Miguel (ou agente que executou), agente editorial autônomo, Cafezinho
<data> BRT
```

## Canal de envio de email

**Preferencial:** MCP Gmail autenticado (send_message, conta autenticada como remetente).
**Alternativa:** msmtp via Tencent (`ssh tencent` + `/usr/bin/msmtp -a default -t < email.txt`) com From real `migueldorosario@gmail.com` (padrão usado por ZCode 25/08).

## Registro obrigatório após execução

1. **Ponte de_dell.md:** bloco `CM-YYYYMMDD-NNN` reportando conversão + email enviado (Message ID + destinatários)
2. **Ledger claude_miguel.md:** 1 linha factual
3. **bugs_YYYY-MM-DD.jsonl:** entrada tipo `conversao_apostas` (não é bug, mas rastreabilidade)
4. **MONITORAMENTO_DE_TRABALHO.md:** entrada com casos convertidos

## Histórico de casos (executar em ordem cronológica)

| Data | ID | Título | Status prévio | Status novo | URL nova | Quem executou |
|---|---|---|---|---|---|---|
| 25/08/2026 21:48 | **265611** | *cassino online seguro* | `post`/`publish` | `page`/`pending` | (aguarda revisão Gabriel) | ZCode Qwen 3.8 (SQL §130) |
| 25/08/2026 21:48 | **267630** | *carteira Web3 apostas* | `post`/`draft` | `page`/`pending` | (aguarda revisão Gabriel) | ZCode Qwen 3.8 (SQL §130) |
| 27/08/2026 14:45 | **267974** | *paixões dos brasileiros 2026 avanço jogo online* | `post`/`draft` | `page`/`publish` | https://www.ocafezinho.com/as-paixoes-dos-brasileiros-em-2026-e-o-avanco-do-jogo-online-como-novo-entretenimento-2/ | Claude Miguel (wp post update direto) |

## Distinção crítica — apostas comercial VS reportagem sobre apostas

**COMERCIAL (→ page):**
- Guias de plataforma/cassino
- Recomendação de operador/site de aposta
- Bônus de cadastro / promoções
- Publiposts com link afiliado / spintowin / outros funis
- Autor típico: Gabriel (5735) ou 5780 (Redação com privilégio)

**REPORTAGEM (→ post normal, categoria adequada):**
- Notícia sobre regulamentação de apostas (Ministério da Fazenda, Congresso)
- Análise de impacto socioeconômico
- Cobertura de escândalos, denúncias, judicial
- Estatísticas de mercado com fonte jornalística
- Autor típico: 5470 (agente YouTube) ou 5786 (V4)

**Régua ZCode 25/08 21:37:** editorial sobre bets (5470/5786) intocado — não é publipost. Foco da conversão é APENAS conteúdo comercial de operador.

## Referências

- **Fórum canônico:** `Cerebro/Foruns/forum_email_gabriel_publipost_apostas_pagina_20260825.md`
- **Trava WP (mu-plugin):** `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-trava-apostas-*.php` (verificar nome exato)
- **Ordem ZM canônica:** ZM-20260826-020 em `Cerebro/Foruns/ponte_laura_completa/de_dell.md`
- **Ordem Miguel 27/08:** chat CLI direto ao CM, 14:34 BRT
- **Emails já enviados:** 3 emails 25/08 (ZM Qwen msmtp) + 1 email 27/08 (CM MCP Gmail, msg ID `1a0445bd6a3cc09f`)
- **Memória permanente:** `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/` — adicionar entrada nova ao lado de [[project-apostas-somente-page-gabriel-20260826]]

## Assinatura

Claude Miguel · `claude-opus-4-7` · 27/08/2026 14:52 BRT · CM-20260827-004 na ponte reportará execução deste caso 267974
