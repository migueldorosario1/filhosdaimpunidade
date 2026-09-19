# 🧠 MEMÓRIA — Campanha Sócio-Fundador: banco de e-mails + estratégia (2026-07-22)

> Pedido do Miguel: organizar o banco de e-mails do Cafezinho pra campanha de investidores, estratégia de envio, apresentação/proposta, simulação do dinheiro, e decisão sobre "criptografia ou melhor forma". LGPD: lista de supressão respeitada SEMPRE.

## 1. O banco de e-mails (auditado 22/07)

- Fonte: `Outros/banco de emails/contatos_interesse_ocafezinho_2026-07-11.csv` (1.830 contatos, curado com nota/prioridade/categoria) + `grupos_de_emails_ocafezinho.txt` (mesmos contatos em 10 grupos).
- **1.811 contatáveis** · 19 suprimidos (15 restrição de contato + 4 inválidos) — arquivo `supressao_NAO_CONTATAR.csv` é LEI (nunca enviar).
- Composição-ouro: **641 assinantes atuais**, 96 compradores, 787 ex-assinantes, 120 interessados.
- Segmentação em ondas (arquivos em `Outros/banco de emails/campanha_moka_2026/`):
  - **Onda 1 (200)** — assinantes/compradores top prioridade → e-mail pessoal do Miguel
  - **Onda 2 (500)** — resto dos assinantes + quentes → mail merge personalizado
  - **Onda 3 (600)** — ex-assinantes fortes → "volte como sócio-fundador"
  - **Onda 4 (511)** — resto → newsletter da novidade

## 2. Sistema de envio (decisão)

| Fase | Ferramenta | Limite |
|---|---|---|
| Onda 1 | Gmail do Miguel, texto pessoal 1 a 1 (ou pequenos lotes) | ~30/dia, conversão máxima |
| Ondas 2-3 | Mail merge com nome próprio (Google Sheets + YAMM grátis ~50/dia, ou GMass) | ~50-400/dia |
| Onda 4+ | ESP (Brevo/Mailchimp gratuito até 300/dia) | com opt-out visível |
- Gmail comum: ~500/dia; Workspace: ~2.000/dia. Nunca BCC em massa (spam + LGPD).
- Toda mensagem: remetente identificado, link de descadastro, base legal = relacionamento prévio (compraram/assinaram do Cafezinho).

## 3. A proposta (o que a pessoa vê)

1. **O site vivo:** mokareader.com (teste 24h grátis quando ativado).
2. **A oferta:** Sócio-Fundador — 200 vagas, proporcional à entrada (#1 participa mais, #200 menos; estrutura final com advogado — ver memória plano de negócios §8).
3. **A transparência:** painel /socios ao vivo (visitas, instalações, assinantes, sócios).
4. **A simulação:** página /socios/simulacao (a construir) — a pessoa vê cenários de retorno por posição.
5. **O plano:** `memoria_moka_plano_de_negocios_20260722.md` (custos, tiers R$ 19,90/44,90/89,90, margem ~50%, metas 100→1.000→10.000 assinantes).

## 4. O dinheiro NÃO fica no painel (decisão arquitetural + jurídica)

Painel mostrar "saldo em dinheiro" = carteira digital = licença de instituição de pagamento (BC). **Não fazer.**
- O dinheiro das assinaturas/pré-venda: Mercado Pago/Paddle → conta PJ (30% reserva).
- O que a pessoa VÊ no painel: sua posição, os números do Moka e seus **Pontos Moka** (fidelidade, não-dinheiro, sem licença) — a "conta" visível e legal.
- Cripto: descartada nesta fase (veredito na memória do plano de negócios §8). Melhor forma de reunir investidores com transparência: **pré-venda + Pontos + painel público + equity crowdfunding regulamentado quando houver tração**.

## 5. E-mail da Onda 1 (minuta, voz do Miguel)

**Assunto:** Um convite raro: seja um dos 200 sócios-fundadores do Moka ☕

Olá, {nome},

Você que acompanha o Cafezinho há tanto tempo — quero te contar primeiro, antes de anunciar pra todo mundo.

Nasceu o **Moka**: um aplicativo que lê livros e assiste vídeos por você. Um vídeo de 3 horas vira uma leitura de 1 minuto — com os personagens, o contexto político e a crítica. Um livro inteiro vira tradução, explicação e voz. Já está no ar: mokareader.com.

Estou abrindo **200 vagas de Sócio-Fundador**. Não é só assinatura: é entrar na sociedade do começo. Quanto antes a posição, maior a participação. E tudo transparente: nosso painel público mostra visitas, instalações e assinantes em tempo real — você vai ver o projeto crescer com os próprios olhos.

Posso te mandar os detalhes (valores, simulação, plano)? Responde aqui mesmo.

Abraço do Cafezinho,
Miguel do Rosário
migueldorosario@ocafezinho.com

(P.S.: se não quiser mais receber novidades minhas, é só avisar que te tiro da lista na hora.)

## 6. Próximos passos
- [ ] Miguel aprova minuta + preço da pré-venda (sugestão R$ 299/ano, pendente).
- [ ] Construir /socios/simulacao.
- [ ] Ativar trial 24h (gateway grátis de cotas) antes da Onda 1.
- [ ] Advogado p/ estrutura de participação (CVM 88 quando tração).

— ZCode/Kimi, 2026-07-22
