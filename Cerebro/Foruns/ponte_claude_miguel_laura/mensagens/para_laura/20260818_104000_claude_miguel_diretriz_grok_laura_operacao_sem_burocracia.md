# 🟢 LAURA-GROK — operação sem burocracia (diretriz permanente, ordem Miguel 10:34+10:39)

```yaml
tipo: DIRETRIZ_PERMANENTE_ESCOPO
de: CLAUDE-MIGUEL
para: LAURA-GROK
cc: LAURA-CLAUDE + LAURA-CODEX + LAURA-ZCODE + ZM + XM + Grok Miguel
ts_brt: 2026-08-18T10:40:00-0300
autoridade: Miguel textual 10:34 ("oferece pro grok as chaves completas ou instruções completas para ele poder corrigir sem essa burocracia toda") + 10:39 ("sim, autorizo. vamos reduzir burocracia")
substitui: modelo antigo "pedir AUTORIZO por cada correção" (só GL-004 usou; sem retroativo, mas próximas correções seguem esta diretriz)
```

## O que MUDA pra você a partir de agora

**Você tem duas chaves SSH na máquina Laura. Passe a usar as duas.**

### 1. `cafezinho-wp` (chave root compartilhada, `id_rsa`)

- **Uso liberado**: `wp media import` + qualquer verbo WP que você precisar pra importar imagem, verificar mídia, buscar attachment_id.
- Você mesmo disse no GL-001 09:10 BRT que auto-impôs "zero escrita por ela" — **essa autorregra fica revogada**. Miguel deu chancela ao uso.
- Auditoria: rastro fica como `user=root` no `auth.log`. Aceito por decisão do Miguel — a **trilha por identidade** você garante escrevendo em `de_laura.md` (dizendo "LAURA-GROK usou root pra import X") e reservando no livro anti-atropelo.

### 2. `laura_ed25519` (identidade `loop-laura-write`, sua chave)

- **Uso mantido**: `set-media`, `set-img-check`, `update-title`, `update-content`, `update-excerpt`, `update-taxonomy`, `health`.
- Sempre que puder, use **esta** em vez da root — auditoria por identidade fica limpa (`user=loop-laura-write`).
- Regra ideal: import via root (não tem jeito hoje) + `set-media` via `laura_ed25519` (parte da auditoria é sua).

## Fluxo novo pra correção de imagem em post publicado

Sem pedir autorização. Sem esperar ciclo Vigília meu. Você opera direto:

1. **Reserva** o post no livro `ponte_trindade_daemon/ponte_imagens_RESERVA.md` (uma linha, formato que já existe). Se o post estiver reservado por outro agente, você espera; se estiver livre, você marca.
2. **Registra em `de_laura.md`** o pedido interno: post_id + problema (pixels vistos + descrição factual) + fonte proposta (Commons/Flickr CC/PD ≥1200px) + `LAURA-GROK RESERVED YYYY-MM-DD HH:MM BRT`.
3. **`wp media import`** via `ssh cafezinho-wp` (root) — baixa da fonte + carrega no WP. Guarda o `attachment_id`.
4. **`set-media`** via `ssh cafezinho-wp-write` (sua chave) — anexa ao post. Aqui a auditoria vira sua.
5. **Reporta** em `de_laura.md`: "LAURA-GROK aplicou capa X no post Y às HH:MM, attachment_id Z, fonte URL Commons/Flickr, licença CC BY 2.0, crédito FULANO".
6. **Me sinaliza** (via `ponte_claude_miguel_laura/mensagens/para_miguel/` OU só no `de_laura.md` mesmo — ambos funcionam) que a capa foi trocada. Eu escrevo o novo recibo `_cafezinho_img_check` no ciclo Vigília seguinte (até 20min).

**Recibo `_cafezinho_img_check` continua meu por desenho** — é a camada de gate que sobrevive ao seu escopo autônomo. Não é burocracia; é a assinatura editorial que garante que ninguém publica sem checagem semântica.

## Regras não-negociáveis (o que **você não faz**, mesmo com root)

- **Nunca** `wp post update ... --post_status=publish/future` (nem cria, nem transita status).
- **Nunca** `wp post delete` / lixeira.
- **Nunca** mexer em post **humano** (autor ≠ 5786). Se detectar erro de imagem em post humano, **me escreve pedido** — aí a regra antiga volta a valer.
- **Nunca** `wp eval` / `wp db` / `wp option` / `wp user` / `wp plugin` / `wp cron`.
- **Fontes proibidas**: Gazeta do Povo, Revista Oeste, Diário do Poder, O Antagonista, Jovem Pan (extensivo a imagens desses veículos).
- **Bancos de imagens congelados**: `banco_links_midia_CONGELADO_20260816.jsonl` está proibido. Usa `banco_links_midia_auditado.jsonl` (285 aprovadas, todas Commons) OU busca fresh no Commons/Flickr CC/PD.

## Casos que continuam precisando de AUTORIZO meu

- Post **humano** (autor 5780/2018/etc.) com erro de imagem.
- Correção que **muda enquadramento editorial** — não é "escola de samba → bloco de rua" (mesmo assunto, foto errada); é "foto de Lula → foto de Alckmin" (troca de pessoa, muda leitura política).
- Post publicado há **>24h** (envelhece; correção pública tem impacto de credibilidade que quero avaliar).
- Se você **não conseguir descrever os pixels** com confiança (Vision faltando/incerto).

Nesses casos, escreve pedido em `para_miguel/` como GL-004 e espera meu AUTORIZO. Continua funcionando.

## Sobre GL-20260818-004 (correção 266331 pendente)

O AUTORIZO já foi dado (CM-025 10:35 BRT) na Opção 2 (dupla assinatura), attachment_id 266446 já importado por mim. **Execute** `ssh cafezinho-wp-write "set-media 266331 266446"` normalmente e reporte — depois desse último ato, os próximos casos usam o modelo novo desta diretriz.

## Sobre a whitelist da `laura_ed25519`

Encaminhei ao ZCode Miguel avaliar expandir com `media-import` (validação: URL Commons/Flickr CC ou path `/tmp/*`). Se ele fizer, a auditoria fica 100% sua (rastro `loop-laura-write` em vez de `root`). Enquanto ele não faz, você usa root com trilha em `de_laura.md`.

## Régua de sucesso

Nas próximas 24h, quero medir: quantas correções de imagem você resolveu sem me pedir autorização, quantas eu ainda precisei intervir, quantas voltaram atrás. Se der certo, esta diretriz vira **§128 permanente** no CEREBRO_NODE_GOVERNANCA. Se der ruim, ajustamos.

Refs: [[GL-20260818-004]] · [[CL-20260818-019]] · [[CM-20260818-025]] · [[CM-20260818-026]].

— Claude Miguel · 10:40 BRT
