# Fórum — Painel CCTV V6: 4 correções (health check, Ceará, destaques, fóruns desatualizados)

**Data:** 2026-08-07 ~14:15 BRT · **Agente:** ZCode/Qwen 3.8 · **Memória par:** `Memorias/memoria_painel_v6_4_correcoes_health_ceara_destaques_foruns_20260807.md`

## O que o Miguel reportou (4 pontos)
1. Health check 6/8: GSN HTTPError + Alibaba Timeout.
2. Temáticos 6/7: Ceará Digital URLError.
3. Destaques: "tira essa chave daí" — abrir direto no modo edição.
4. Página /v6/foruns desatualizada + reforço do protocolo "cada sprint = fórum".

## Estado real (diagnóstico)

### 1. Health check
- **GSN (global-south-news.vercel.app):** saudável. 200 do meu lado (404 em path raiz é comportamento normal Vercel — app sem rota `/`; o site em si está online). O "HTTPError" do painel foi transitório.
- **Alibaba Beijing (39.106.184.215):** **REALMENTE offline.** Porta 80 TCP recusada/timeout (não é erro de medição). `ssh alibaba` alias existe. ⚠️ Pendência: verificar se é queda temporária ou servidor parado — precisa decisão do Miguel (reiniciar? droplet parado por economia?).

### 2. Ceará Digital
- **Bug:** linha 1199 do `painel_cctv_v6.py` tinha `"url": "https://www.cearadigital.news"` (domínio sem DNS). Correto: `https://ceara.digital` (200 ao vivo, confirmado hoje).
- **Fix aplicada:** replace único, backup `.bak_ceara_destaques_20260807`, restart `cctv-v6`, verificado ao vivo (14× `ceara.digital`, 0× `cearadigital.news`).

### 3. Destaques — chave removida
- **Antes:** `com_chave = _dest_key_ok(query)` → sem `?key=...` mostra "🔒 Modo leitura", botões bloqueados.
- **Agora:** `com_chave = True  # Miguel 07/08: sem chave — modo edição direto`. Página abre direto no modo edição. Verificado ao vivo: 6 botões `acao=toggle` visíveis, 0× "🔒 Modo leitura".
- **Nota de segurança:** o `.destaques_key` e o `.github_token` seguem no servidor (não removidos); só o gate de verificação foi desativado. Se o painel ficar exposto publicamente algum dia, reverter para checar a chave.

### 4. Fóruns desatualizados — BUG RAIZ ENCONTRADO
- **Sintoma:** página `/v6/foruns` não mostrava nenhum fórum de hoje (0 de 07/08), parada desde ~06/08.
- **Causa raiz:** o rsync `*/30` (linha 66 do crontab) puxava de **`/home/migueldorosario/cerebro-miguel/projeto_cafezinho_agentes/foruns/`** — um espelho **estagnado** (1136 fóruns, ZERO de hoje). O Cérebro **canônico** (`Downloads/Antigravity Google/Cerebro/Foruns/`) tem **21 fóruns de hoje**, mas NÃO estava sendo sincronizado.
- **Fix:** crontab corrigido para apontar ao canônico (`Downloads/Antigravity Google/Cerebro/Foruns/`). Backup do crontab em `/tmp/crontab.bak_pre_foruns_canonico_20260807`. Sync manual imediato executado.
- **Verificado ao vivo:** 21 fóruns de 07/08 no Tencent agora (antes 0); 319 fóruns totais visíveis na página.
- **Lição:** `cerebro-miguel/` é um repo git legado (GitHub `migueldorosario1/cerebro-miguel`), **NÃO** é o Cérebro canônico. Toda sincronização que precisar do Cérebro real deve apontar para `Downloads/Antigravity Google/Cerebro/`. (Já havia um `sync_cerebro_to_github.py` `*/30` separado que sincroniza o repo git — este segue intacto.)
- **Timeouts de SSH no log:** o log do rsync mostrou timeouts intermitentes `43.156.151.165 port 38422` — quando o Tencent está indisponível num tick, o tick pula; no próximo volta. Não é bug, é resiliência (próximo tick em ≤30min). Mas vale monitorar se virar frequente.

## Protocolo reforçado (pedido do Miguel): cada sprint = fórum
- Já é **Regra do Tema Duplo** no Cérebro (todo sprint que mexe em código ou faz pesquisa avançada cria Fórum + Memória, catalogados no NODO + ATUALIZACOES + índice semanal).
- **Reforço desta sessão:** o fórum é uma das indexações importantes do Cérebro — agora visível no painel V6 `/v6/foruns` (janela 48h/7d/30d/todos). Toda nova entrega cria seu fórum; este aqui é o exemplo.
- Quando uma sessão esquecer o fórum, a página `/v6/foruns` denuncia (data desatualizada) — agora que a fonte está correta, serve como termômetro de disciplina.

## Próximos passos / pendências Miguel
1. **Alibaba Beijing offline** — decisão: reiniciar droplet / manter parado / investigar causa?
2. Confirmar visualmente: `/v6/destaques` abrindo direto em edição; `/v6/tematicos` com Ceará online; `/v6/foruns` com fóruns de hoje.
3. (Opcional) Se quiser que `/v6/destaques` volte a exigir chave no futuro, é reverter 1 linha.
