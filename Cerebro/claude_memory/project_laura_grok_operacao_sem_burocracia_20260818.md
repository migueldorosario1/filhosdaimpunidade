---
name: project-laura-grok-operacao-sem-burocracia-20260818
description: "LAURA-GROK autorizado 18/08 10:39 a operar correção de imagem em posts V4 (autor 5786) SEM pedir AUTORIZO caso a caso. Usa chave root cafezinho-wp compartilhada pra media-import + laura_ed25519 pra set-media. Trilha em de_laura.md + reserva. Recibo _cafezinho_img_check continua meu (Claude Miguel). Casos que ainda precisam AUTORIZO: post humano, mudança de enquadramento, publish >24h, sem confiança nos pixels. Whitelist expandida ao ZCode Miguel (longo prazo)."
metadata: 
  node_type: memory
  type: project
  originSessionId: 870114c6-7ee3-4080-8592-299996b3140e
---

## Contexto

Miguel 18/08/2026 09:26 BRT tinha estabelecido: agentes que acharem erro pedem autorização, Claude Miguel analisa e autoriza. Grok Laura (LAURA-GROK) fez o primeiro pedido dessa regra às 10:19 (GL-20260818-004, correção capa 266331 escola de samba → bloco de rua).

Miguel 10:34 mudou de opinião: **"oferece pro grok as chaves completas ou instruções completas para ele poder corrigir sem essa burocracia toda"**. Confirmação 10:39: **"sim, autorizo. vamos reduzir burocracia"**. E 10:41: **"sim, então fazer os dois"** (curto + longo prazo em paralelo).

Descoberta técnica que me fez propor: LAURA-GROK JÁ tinha as duas chaves na máquina Laura desde a instalação madrugada. O bloqueio era autorregra dele ("zero escrita pela chave root compartilhada" — GL-001 09:10 BRT). Não era gap técnico.

## Regra permanente (Curto prazo — vale HOJE)

**LAURA-GROK opera correção de imagem em post V4 (autor 5786) sem pedir AUTORIZO.** Fluxo:

1. Reserva no livro `Cerebro/Foruns/ponte_trindade_daemon/ponte_imagens_RESERVA.md`.
2. Registra em `de_laura.md`: post_id + problema (pixels descritos) + fonte proposta.
3. `wp media import` via `ssh cafezinho-wp` (id_rsa root — autorização Miguel revoga auto-regra dele).
4. `set-media` via `ssh cafezinho-wp-write` (laura_ed25519, sua identidade — auditoria dele).
5. Reporta em `de_laura.md` (attachment_id + fonte URL + licença + crédito).
6. Sinaliza ao Claude Miguel (ponte editorial OU de_laura.md).
7. Claude Miguel assina `_cafezinho_img_check` no próximo ciclo Vigília (≤20min) — recibo continua meu por desenho (camada de gate final).

**Auditoria**: passo 3 rastro fica como `user=root` (aceito por Miguel); passos 4-7 rastreados por identidade. Trilha por agente em `de_laura.md`.

## Casos que AINDA precisam de AUTORIZO Claude Miguel

- Post **humano** (autor ≠ 5786, ex.: 5780 Redação, 2018 Miguel).
- Correção que **muda enquadramento editorial** (não factual). Ex.: "escola de samba → bloco de rua" (mesmo assunto, foto errada) = SEM AUTORIZO; "foto de Lula → foto de Alckmin" (troca pessoa) = COM AUTORIZO.
- Post publicado há **>24h** (credibilidade impactada).
- Sem confiança nos pixels (Vision faltando/incerto).

## Regras não-negociáveis (mesmo com chave root)

- Nunca `publish` / `future` / `post_status` / `post_date`.
- Nunca `post delete` / lixeira.
- Nunca `wp eval` / `wp db` / `wp option` / `wp user` / `wp plugin` / `wp cron`.
- Nunca `set-img-check` (recibo é Claude Miguel — camada de gate).
- Fontes proibidas: Gazeta do Povo, Revista Oeste, Diário do Poder, O Antagonista, Jovem Pan.
- Banco `banco_links_midia_CONGELADO_20260816.jsonl` = proibido.

## Longo prazo (paralelo)

**ZCode Miguel formal pedido** (CM-20260818-026): expandir whitelist de `/usr/local/sbin/cafezinho-wp-write` incluindo `media-import` com validação (URL Commons/Flickr CC OU path `/tmp/laura-import/*.{jpg,jpeg,png,webp}`, ≤10MB, MIME válido, meta title+caption+credit obrigatória). Quando pronto, LAURA-GROK deixa de usar root e usa 100% `laura_ed25519` — auditoria limpa em todos os passos.

## Régua de sucesso

Nas próximas 24h (18/08 11:00 → 19/08 11:00 BRT), medir:
- Correções LAURA-GROK sem AUTORIZO (contador esperado)
- Correções que precisaram AUTORIZO (uso das exceções, aceitável)
- Correções que voltaram atrás (falha crítica — investigar)

Se contador saudável, vira **§128 permanente** no CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md.

## Aviso enviado

- Diretriz completa: `Cerebro/Foruns/ponte_claude_miguel_laura/mensagens/para_laura/20260818_104000_claude_miguel_diretriz_grok_laura_operacao_sem_burocracia.md`
- Aviso Trindade: CM-20260818-026 em `Cerebro/Foruns/ponte_laura_completa/de_dell.md`

Ligado a: [[project-laura-escopo-ampliado-corrigir-sim-publicar-nao-20260818]] · [[project-credenciais-em-cerebro-miguel-repo-privado-arquitetura-autorizada-20260818]] · [[feedback-contrato-integridade-imagens-v1-homologado-20260816]].
