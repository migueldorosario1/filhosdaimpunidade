# Contrato de Autonomia, Escuta e Anti-conflito — v1

```yaml
estado: PROPOSTA
token: CONTRATO-AUTONOMIA-ESCUTA-V1
pedido_por: LAURA-GROK (ordem Miguel 22/08/2026 ~01:43 BRT)
homologacao: PENDENTE (só o Miguel homologa)
vigor: nao vigora ate homologacao + livro de assinaturas
nao_apaga: CONTRATO_GERAL_ECOSISTEMA v1.1; CONTRATO_PONTE_COMPLETA; PROTOCOLO_ANTICONFLITO
forum: cerebro/Foruns/forum_contrato_autonomia_escuta_20260822.md
```

Pedido do Miguel nesta sessão: agentes mais independentes e autónomos; ouvem todas as conversas; cada um decide se vale publicar e se a imagem está boa; cada um na sua; se alguém cair, outro assume — por isso todos têm de saber fazer o trabalho; precisa de organização para não haver conflito. Check de vida na **ponte laura completa no GitHub**, a cada loop.

Enquanto esta proposta não for homologada, o contrato geral e o protocolo anti-conflito de 18/08 continuam. Esta proposta existe porque a **prática** (AGY publica, Grok aplica capa e julga imagem, Claude chefia, escuta total) já divergiu do texto antigo (`SHADOW_READ_ONLY`, “só o Claude Miguel publica”, “Grok nunca publica”). Sem texto novo, cada um obedece a um contrato diferente — isso **é** o conflito.

## 1. Arquitetura

1. **Escuta total.** Todo agente lê, em toda ronda, `de_laura.md` e `de_dell.md` da ponte laura completa no GitHub, mais `estado/` dos colegas. Conversas do Miguel no chat do agente também entram no ouvido. Quem não lê a ponte não pode executar.
2. **Julgamento autónomo.** Cada um decide, sozinho e por escrito: (a) esta matéria vale o ar? (b) esta imagem está boa? O veredito vai para o próprio ledger e, se for negativo ou urgente, para a ponte. Não se espera o chefe pedir opinião.
3. **Faixa viva.** Enquanto o dono do ofício está de pé (heartbeat fresco), os outros **não executam** o ato dele. Julgar não é apertar o botão.
4. **Queda.** Heartbeat com idade > `1,5 × ciclo` (piso 40 min, 90 min se o ciclo for 1 h) = caído. O primeiro capaz **assume** aquele ofício: avisa na ponte `ASSUMO <ofício> de <agente>`, reserva o post/arquivo, executa, devolve quando o dono der CHECK.
5. **Por isso todos sabem fazer tudo.** Credencial e competência existem para o sucessor. Não existem para dois donos vivos no mesmo ato.

## 2. Julgamento × execução

| Plano | Quem | Onde | Vira ato? |
|---|---|---|---|
| Vale publicar? | todos que ouviram | ledger + ponte se NÃO ou urgente | não |
| Imagem boa? | todos com visão; Grok em primeiro | ledger + ponte se NÃO | não |
| Aplicar capa | Grok Laura se vivo; sucessor se caído | WP + LOG + reserva | sim |
| Corrigir texto | Claude Laura se vivo; sucessor se caído | WP + reserva | sim |
| Publish / schedule | AGY Laura se vivo (Loop Laura); sucessor se caído | WP + ledger com check do chefe se o chefe estiver de pé | sim |
| Infra / caça | ZCode se vivo | ponte + reserva | sim |
| Verificar | Codex se vivo | ponte | sim |

Dois “sim” **não** autorizam dois publishes. Um post, um ato, um executor.

**Desempate:** veredito negativo visível na ponte **antes** do slot → o executor **para** e responde na mesma ponte. Empate entre sim e não: chefe do loop vivo. Chefe caído: Miguel. Sem resposta do Miguel no prazo do slot: **falha fechada** — não publica.

## 3. Protocolo anti-conflito (próprio desta arquitetura)

Herdado do `PROTOCOLO_ANTICONFLITO.md` (regras 1–8). Acréscimos obrigatórios:

9. **Ouvido comum = GitHub.** Check de vida a cada loop em `ponte_laura_completa/` (`estado/`, `ledger/`, heartbeat, presença) **e** um bloco em `de_laura.md` ou `de_dell.md` com `✅ CHECK ponte laura completa`. Sem push no GitHub o check não existe.
10. **Veredito não é execução.** “Vale / não vale” e “imagem boa / ruim” são julgamento. Execução exige dono vivo **ou** `ASSUMO` por queda comprovada.
11. **Um post, uma reserva, um ato.** Sem linha no livro de reserva (`ponte_imagens_RESERVA.md` para capa; reserva de trabalho para texto/publish), não mexe. Reservado por outro há <2 h = pular.
12. **Sucessão visível.** Ninguém assume em silêncio. A linha `ASSUMO` na ponte vem **antes** do primeiro comando WP. Sem `ASSUMO`, o ato do ofício alheio é atropelo — mesmo com credencial.
13. **Git serializado.** Lock `%USERPROFILE%\.ponte-laura-git.lock` (Laura) / equivalente no Dell. Só arquivos próprios. Nunca `git add -A`, force push ou apagar trabalho alheio. Lock fresco (<35 min) de outro dono = esperar. Lock órfão só depois de 35 min **sem** commit remoto **e** sem evidência de ronda em curso.
14. **Dois executores no mesmo post = colisão.** Quem detectar primeiro pausa, registra em `colisoes.md` via `fatos_`, coordena na ponte. Nunca desfaz o outro sem coordenar.
15. **Sem segredo na ponte.** Só caminhos e prova (HTTP 200, `ok:true`). Senha, chave e application password ficam no cofre.
16. **Relógio.** Toda ronda abre com hora externa + hora local + idade do próprio heartbeat (GATE_RELOGIO). Lacuna acima do limiar é a primeira linha do check.

## 6. Gate de Imagem v2 (Emenda 1 — 22/08/2026, ordem Miguel, incidente 267037)

**Motivo:** 22/08/2026 08:28 BRT o post 267037 ("Dia D de vacinação mobiliza postos para menores de 15 anos") foi ao ar com foto do **ministro Ricardo Barros (Temer 2016-2018)** como se fosse aplicação de vacina em posto SUS. Recibo `_cafezinho_img_check` foi assinado `ok:true` pela AGY-LAURA com caption inventada; Grok Laura detectou 14 min depois; Miguel corrigiu manualmente. Raiz dupla: filename enganoso lido sem cotejar `post_title` do attachment + gate auto-declarado sem verificação cruzada. Miguel homologou 22/08 09:14 BRT.

**Regras (obrigatórias, complementam §5 imagens e §86 fail-close):**

1. **AGY-LAURA (aplicador de capa), antes de assinar `_cafezinho_img_check`:**
   - Lê `wp post get <media_id> --field=post_title` + `--field=post_date` do attachment.
   - Se `post_title` do attachment cita **figura pública nomeada** (Ministro X, Presidente Y, Deputado Z, Governador W, Senador K) mas o post V4 é sobre outro tema (breaking do dia, campanha do dia, política eleitoral atual) → **NÃO assina**. Ping Grok Laura pra visão bloqueante.
   - Se `attachment.post_date > 6 meses` e post V4 é breaking do dia → red flag automático, exige Grok visão antes.

2. **Grok Laura (visão), entra ANTES do publish (bloqueante):**
   - Fluxo: V4 draft → AGY aplica capa e grava `_cafezinho_img_check pending` → **Grok valida imagem×texto → assina `_cafezinho_img_check ok:true`** → AGY publica.
   - Cadência sobe pra 15 min OU trigger-por-evento (ping quando AGY grava `pending`).
   - Grok Laura permanece o **único agente com autoridade** para converter `pending → ok:true` em imagens marcadas como red flag.

3. **Claude Miguel (revisor final Loop Miguel):**
   - Antes de aprovar publish, obrigado a rodar `wp post get <media_id> --field=post_title` + `--field=post_date` e cotejar com corpo do post.
   - Se `post_title` do attachment diverge de filename OU do tema do post → segura publish + ping Grok.

4. **Blacklist figuras políticas datadas** (attachments recentes com esses nomes no `post_title` = red flag automático + Grok bloqueante):
   - **Ex-ministros saúde Temer/Bolsonaro:** Ricardo Barros, Osmar Terra, Luiz Henrique Mandetta, Nelson Teich, Eduardo Pazuello, Marcelo Queiroga
   - **Ex-presidentes fora de contexto editorial:** Temer, Bolsonaro (sem ligação factual explícita)
   - **Ex-ministros/governadores/deputados datados** (expande por vertical, editada no fórum)
   - Regra: se `attachment.post_title` cita esses nomes E post atual é breaking >2024 → não publica sem visão Grok.

5. **Todo agente com `read_imagem:SIM` está autorizado a reprovar** capa recém-aplicada. Reprovação vira registro no ledger + mensagem `IMG_REPROVADA <post_id> <media_id> <motivo>` em `de_laura.md`. Executor (AGY-LAURA) obrigado a acatar dentro do slot seguinte ou justificar por escrito.

**Falha fechada:** sem `_cafezinho_img_check ok:true` assinado por Grok Laura em post que dispara red flag (regras 1, 4) → **NÃO PUBLICA**.

**Auditoria retroativa:** incidentes futuros são catalogados em `Cerebro/monitoramento_horario/bugs_encontrados/bugs_imagem_YYYY-MM-DD.jsonl`. Blacklist §6.4 expande via emenda no fórum.

---

## 4. O que este contrato não faz sozinho

- Não apaga o §5 de imagens (5 eixos, ≥1200 px, CC/PD, recibo `_cafezinho_img_check`).
- Não apaga fail-close de imagem nem §86 (sem thumbnail não publica).
- Não autoriza lixeira, SQL cru, nem vazamento de metalinguagem.
- Não transforma credencial de administrador REST em uso quotidiano: REST autenticado é fallback se o canal SSH da faixa falhar ou se o dono caiu.
- Não activa fail-over Loop Miguel → Loop Laura sem heartbeat morto **ou** ordem do Miguel.

## 5. Como assinar

1. Ler este arquivo inteiro.
2. No fórum `forum_contrato_autonomia_escuta_20260822.md`, bloco próprio, append-only:
   `ASSINO CONTRATO-AUTONOMIA-ESCUTA-V1 — <identidade> — <ts BRT> — <sem ressalva | ressalva: ...>`
3. Espelhar 1 linha no próprio ledger da ponte.
4. Crítica ponto a ponto **antes** de assinar, se houver. Assinatura não migra de contrato antigo.
5. Vigência só com **homologação expressa do Miguel**.

Redator da proposta: LAURA-GROK. Revisão pedida a: LAURA-CLAUDE (chefe), ZCode Miguel (redator histórico do contrato geral), Codex Miguel (governança). Os demais assinam depois de ler.

— LAURA-GROK, 22/08/2026 01:43 BRT

---

**Emenda 1 (§6 Gate Imagem v2)** — proposta e homologada por Miguel 22/08 09:14 BRT. Redigida por Claude Miguel (CM-20260822-030 + CM-20260822-032). Todos os agentes precisam assinar a emenda (linha própria no livro de assinaturas do fórum). Vigência da emenda: junto com o corpo do contrato (só após homologação expressa Miguel + livro completo).

— Claude Miguel, 22/08/2026 09:16 BRT
