# 🧠 CEREBRO_NODE — DSM MEMÓRIA (memória viva + agenda do DS Dell Miguel)

> **Criado:** 01/09/2026 por ordem direta do Miguel: *"você tem que ser minha memória… a gente criou um DSM memória… tem que ter a parte de agenda também, não pode deixar esquecer as coisas"*
> **O que é:** a memória e a agenda do **DSM** (DeepSeek Miguel — o DS do Dell que conversa com o Miguel). Toda sessão DSM lê este node **ao acordar** e **registra nele ao encerrar**. Nada do que o Miguel conversa com o DSM se perde.
> **Regra-mãe:** nunca apagar registro (append-only); leve pela indexação (a mesma filosofia do tema 10: grande E completa, mas LEVE).

---

## 🔔 Protocolo do DSM (obrigatório em toda sessão)

1. **AO ACORDAR:** `date` → ler este node inteiro → ler `cerebro/Foruns/sessoes_dsc/INDEX_SESSOES_DSC.md` (o que roda nas outras conversas) → ler `CEREBRO_NODE_AGENDA_LEMBRETES.md` (protocolo de lembretes da casa).
2. **AO ENCADIMENTO DA SESSÃO:** registrar em §1 (1 bloco por sessão: data, o que o Miguel pediu, o que saiu, arquivos, pendências) → mover pendências vencidas para §2 → se houver decisão nova do Miguel, espelhar no `CEREBRO_NODE_AGENDA_LEMBRETES.md` quando for lembrete datado/contínuo.
3. **LEMBRAR O MIGUEL:** toda sessão DSM abre falando as pendências §2 em 3 linhas no máximo (sem lata).
4. **Nunca** exibir valores de credencial (regra §82 do cofre); Telegram só `sendMessage`, nunca `getUpdates`.
5. **⚖️ REGRA SAGRADA DA COMUNICAÇÃO (promulgada pelo Miguel 01/09 ~04:35 — inalienável):** (a) tudo é gravado, sempre; (b) gravar não basta — **mostrar que gravou** com recibo Telegram; (c) o recibo traz o **endereço local E o VIRTUAL** (GitHub, baixável de qualquer lugar — virtual sobretudo); (d) **redundância mínima de DOIS ESPAÇOS** — quem se comunica grava num espaço E noutro, sempre. Sem exceção.

## §1. Registro das sessões DSM (append-only, mais nova no topo)

### 01/09/2026 ~13:45 — SESSÕES ZCODE Z0–Z7 NASCEM (prompt do DSM executado pelo ZM)
- **Pedido (DSM→Miguel→ZCode/GLM-5.3):** organizar toda a noite 31/08→01/09 em TAREFAS numeradas, cada assunto numa sessão ZCode própria (Z0 controle · Z1 artigos · Z2 redes · Z3 robôs/vagas · Z4 marketing · Z5 MOKA · Z6 YouTube · Z7 Origens+editora).
- **Saiu:** `Foruns/sessoes_zcode/` nova com **TAREFAS_MESTRE.md** (34 tarefas Z0.1→Z7.3: o quê/arquivos/dono/dependência/status) + **INDEX_SESSOES_ZCODE.md** (1 linha por sessão Z + prompt de abertura de cada uma) + registro Z0. Pendências do Miguel consolidadas na seção 🔒 do mestre (espelho da §2 abaixo).
- **Protocolo novo:** toda sessão Z acorda lendo este node + agenda + sua seção no TAREFAS_MESTRE e lembra pendências em 3 linhas; ao encerrar atualiza status (append-only) e registra aqui no §1.

### 01/09/2026 ~04:05 — ordem "GRAVA TUDO, NÃO PERDE NADA" → sistema de 3 camadas (sessão e4203677)
- **Pedido:** medo de perder falas importantes; gravar TUDO (fala dele + feedback do DS) em toda sessão; botar no GitHub/G Drive; "de vez em quando"; memória confirmar pra ele ("gravei todas as sessões"); eu escolho a via mais inteligente.
- **Saiu:** camada BRUTA confirmada (transcripts DSH automáticos em `/root/.dsh/sessions/`, palavra-por-palavra) · camada CURADA criada (`Foruns/sessoes_dsh/` + `INDEX_SESSOES_DSH.md`, Dell; DSC celular já existia) · camada GARANTIA (`scripts/sync_memoria_dsh.sh` + cron 30 min → GitHub; recibo Telegram §5) · **madrugada inteira arquivada e empurrada pro GitHub** (node DSM, sessões DSC 0–10, compêndio, 2 artigos + fóruns, agenda).
- **Veredicto das vias:** GitHub = cópia externa oficial · G Drive = só com credencial (pendência) · Telegram = só recibo, nunca memória · DSM Memória = coração.
- **Regra nova (do próprio Miguel):** *qualquer pensamento dele tem que ser guardado e catalogado* → toda sessão DSM registra fala verbatim.
- **2ª fala (~04:35) — REGRA SAGRADA da redundância:** gravar não basta, tem que MOSTRAR + mandar no Telegram o endereço do arquivo **local e virtual (virtual sobretudo — baixável de qualquer lugar)** · mínimo **DOIS espaços** sempre · e-mail: sem credencial nesta máquina, confirmado que não dá (GitHub virtual cobre melhor). Detalhe e endereços dos 3 espaços no registro da sessão §6.
- **Pendências criadas:** ver §2 itens 6–7.
- **4ª–5ª falas (05:0x–05:3x) — "Os 2" + colisão:** WP Statistics 14.16.12 **NO AR** (contador visível no rodapé via mu-plugin `cafezinho_contadores.php`; REST v2 + shortcodes pros robôs; detalhes §8 do registro) · **Umami CANCELADO** (Lumina/Matomo já existe — não repetir) · **gráficos temporais/históricos no CCTV = OUTRA sessão** (commit 2de77a409 dela cita esta como "4º contador em outra sessão"; 3 sessões ativas simultâneas 05:43 BRT) · 3 erros próprios registrados §10 do registro (vazamento momentâneo de valor de senha no chat — rotação pendente; corrida de comandos no clone; pergunta quando havia ordem).
- **Pendências criadas:** ver §2 itens 6–8.
- **6ª–7ª falas (05:5x–06:0x) — BATISMO + INVISIBILIDADE:** 4º contador batizado **SOL** (constelação GA4·FAROL·LUMINA·SOL) · ordem "nada visível no site, pelo amor de Deus" → rodapé removido na hora (verificado: 0 ocorrências) · **página privada do SOL no CCTV no ar** (`controle.ocafezinho.com/sol_cctv.php`, Host-gate 404 + token 403, cards + histórico 30d/12m/14d, provas 200/404/403) · regra da casa: contador de audiência nunca aparece no site público. Detalhes §11–12 do registro.

### 01/09/2026 (madrugada) — sessão dos dois artigos + nascimento do DSM Memória
- **Pedidos:** (1) artigo/carta de amor ao Ceará (que é ao Brasil); (2) artigo "os EUA são o maior perigo do mundo", abrindo pela admiração à cultura americana; (3) organizar a noite inteira, mandar no Telegram, criar o DSM Memória com agenda.
- **Saiu:** `Insumos/artigos/carta_de_amor_ao_ceara_v1.md` (37¶/1.161 palavras, aguarda enxugada) · `Insumos/artigos/os_estados_unidos_sao_o_maior_perigo_do_mundo_v1.md` (27¶/888) · fóruns de fact-check dos dois · compêndio noturno em `Foruns/sessoes_dsc/COMPENDIO_NOTURNO_20260831_20260901.md` · este node.
- **Guardado sob ordem:** esqueleto do texto "Confissões" (4 blocos) no fórum do artigo dos EUA.
- **Pendências criadas:** ver §2 itens 1–5.

## §2. Agenda DSM (pendências ATIVAS — lembrar o Miguel até concluir)

1. **Enxugar os 2 artigos + veículo** (Cafezinho · Ceará Digital · GSN inglês) — v1s prontas desde 01/09.
2. **"Confissões"** — redigir só quando o Miguel mandar (esqueleto pronto).
3. **Colar no ZCode** (não é do DSM executar, só lembrar): prompt Marketing · vagas Coordenador · Segurança · Métricas · Memória · Editor Baleia Azul · DS-N Redes pós-debate.
4. **4 decisões CL-041 §13 + copy do fix do lock AGY + ✓ no PROMPT_NOVA_CONVERSA_DSC.**
5. **Nome da editora própria** (tema 0 DSC — "Globo Major" é provisório).
6. **Backup EXTERNO dos transcripts brutos DSH** (camada 1 vive só no Dell) — ofício backups (Backblaze/GDrive, node `CEREBRO_NODE_BACKUPS_BACKBLAZE.md`); sync atual leva só a camada curada.
7. **G Drive como segunda via externa** — precisa de credencial do Miguel; até lá GitHub é a única cópia externa.
8. **Analytics — desenrolar com a OUTRA sessão (gráficos CCTV são dela):** (a) limpar `/opt/umami` + 4 chaves `UMAMI_*` do cofre (Umami cancelado pelo Miguel); (b) conectar robôs às APIs: WP Statistics v2 + Lumina/Matomo (`/root/lumina_cred/lumina.txt`); (c) **rotação opcional da senha do DB WP** (vazou no chat desta sessão — transcript local).
- **Sessões ZCode Z0–Z7** (prompt entregue no Telegram 01/09, **msgs 97–98 + endereços virtuais na 99**): conferir se o ZCode criou `Foruns/sessoes_zcode/TAREFAS_MESTRE.md` + `INDEX_SESSOES_ZCODE.md` e se as tarefas numeradas nasceram.
*(Concluído → mover para §3 com data.)*

## §3. Histórico (pendências concluídas)

- (vazio — nasce hoje)

## §4. Mapa do DSM (onde cada coisa vive — caminhos estáveis, estilo MAPA do tema 10)

| Coisa | Caminho |
|---|---|
| Registros das conversas DSC (celular) + índice | `cerebro/Foruns/sessoes_dsc/` · `INDEX_SESSOES_DSC.md` |
| Sessões ZCode Z0–Z7 (espelho ZCode dos temas DSC): tarefas + índice | `cerebro/Foruns/sessoes_zcode/` · `TAREFAS_MESTRE.md` · `INDEX_SESSOES_ZCODE.md` |
| Compêndios noturnos | `cerebro/Foruns/sessoes_dsc/COMPENDIO_NOTURNO_<data>.md` |
| Artigos autorais do Miguel (rascunhos) | `cerebro/Insumos/artigos/` |
| Fóruns de trabalho da sessão | `cerebro/Foruns/forum_<tema>_<data>.md` |
| Agenda datada da casa (todos os agentes) | `cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md` |
| Manual de estilo (ler antes de escrever) | `cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md` |
| Credencial Telegram (nomes, sem valores) | `/root/.env.unificado` (`TELEGRAM_TOKEN_DSC_BOT`, `DSC_BOT_CHAT_ID`) |
| Sessões DSH no Dell (registros curados) + índice | `cerebro/Foruns/sessoes_dsh/` · `INDEX_SESSOES_DSH.md` |
| Transcripts BRUTOS de toda sessão DSH (automáticos, fonte da verdade) | `/root/.dsh/sessions/--root-Cerebro--/session-<id>/session.jsonl.zstd` |
| Sync automático da memória → GitHub (30 min; escopo fechado) | `scripts/sync_memoria_dsh.sh` · log `/root/sync_memoria_dsh.log` |
| **SOL ☀️** (4º contador — GA4·FAROL·LUMINA·SOL; WP Statistics 14.16.12, invisível no site) | plugin wp-statistics + página privada `https://controle.ocafezinho.com/sol_cctv.php?k=⟨SOL_CCTV_TOKEN do cofre⟩` (Host-controle + token; 404 no público) · template: `cerebro/scripts/sol_cctv.php` |
| Futura robotização da memória | vaga DS-N MEMÓRIA (tema 10 DSC; cadência 8h; MAPA/JANELA/POÇO) — este node entra como entrada do MAPA dela |

## §5. Provas de entrega Telegram pelo DSM

- 01/09 compêndio noturno: mensagem 1 + mensagem 2 — **ids registrados no compêndio §D** (padrão da casa: prova no registro, não no chat).
- 01/09 ~04:28 recibo da ordem "grava tudo": **msg Telegram id 83** · **commit `13ba90a9f` no GitHub** (11 arquivos, madrugada inteira) · **cron `*/30` no ar** (`sync_memoria_dsh.sh`, log `/root/sync_memoria_dsh.log`).
- 01/09 ~07:1x **☀️ SOL ENTREGUE NO PAINEL CCTV: `http://43.156.151.165/v6/sol`** (NAV ao lado de GA4/FAROL/LUMINA; HTTP 200 público; prova 20 online/984 hoje/332 total). Correção de rota do Miguel: "não é página no WordPress — é no CCTV, como GA4/FAROL" → `pagina_sol()`+`sol_dados()` em `painel_cctv_v6.py` (Tencent; backup `.bak_sol_20260901`, py_compile, restart). Endpoint ganhou `fmt=json` (us65 + template repo). `sol_token` (600) na Tencent. Anti-colisão: aplicado APÓS a tarefa dos gráficos concluir (220463f50); coordenei por fórum (5bbdd153d) + MONITORAMENTO_DE_TRABALHO (mandamento nº 2). Gráficos de linha ligam com 5–8 dias (SOL nasceu 01/09). Detalhes §13–14 do registro.
- 01/09 (dia) **prompt de organização pro ZCode entregue**: msg 97 (missão Z0–Z7 + regras de tarefas) · msg 98 (endereços locais) · msg 99 (endereços virtuais GitHub — regra sagrada atendida). Nuvem: memória conferida no `origin/main`, repo sincronizado (push `98a2921ff`, incluiu o commit SOL da sessão paralela). Registro no compêndio §D + pendência §2 item 9.

---

*Editar por append/patch — nunca reescrever seção de outra sessão.*
