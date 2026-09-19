# 16 — ESTUDO: Moka nas lojas (Google Play + Apple App Store)

> Estudo pedido pelo Miguel (28/07/2026): como transformar o Moka (PWA/Next.js) em aplicativo de verdade nas duas lojas. Ponto-chave do Miguel: **ele tem EMPRESA (CNPJ)** — e isso muda o jogo a favor dele.

---

## 1. O efeito EMPRESA (a memória do Miguel está correta)

### Google Play
- Conta **pessoal** criada depois de nov/2023: **obrigado a rodar um teste fechado com 20 testadores por 14 DIAS** antes de poder publicar em produção. Esse é o gargalo que trava todo mundo.
- Conta **organização (empresa)**: **PULA essa exigência** — publica direto. É o "entra mais rápido, quase automático" que o Miguel lembrou. Custa **US$ 25 (taxa única)**.
- Verificação de organização pede **número D-U-N-S** (grátis; ver §4) + dados do CNPJ + e-mail/telefone da empresa.

### Apple App Store
- Apple Developer **Organization**: **US$ 99/ano**. Publica com o NOME DA EMPRESA na loja ("Cafezinho Media Group" em vez do nome pessoal do Miguel — marca melhor), permite equipe (outros devs/testers), e exige **D-U-N-S** também.
- O tempo de REVISÃO da Apple (1–3 dias típico) é igual para pessoa/empresa — a vantagem da empresa é marca + equipe, não velocidade.

**Conclusão:** abrir as duas contas como **ORGANIZAÇÃO** com o CNPJ do Miguel.

---

## 2. O caminho técnico (decisão de arquitetura)

O Moka é um PWA (Next.js, client-rendered). Três rotas:

| Rota | O que é | Esforço | Veredito |
|---|---|---|---|
| **TWA (Bubblewrap)** — só Android | A loja lista um pacote que abre o PWA em tela cheia (o site É o app) | **baixíssimo** — dias | ✅ **ROTA DO ANDROID** — atualiza sozinho com o site, quase zero manutenção |
| **Capacitor** (Android + iOS) | Casca nativa embutindo o app (ou apontando pra URL viva) | médio | ✅ **ROTA DO iOS** (Apple não aceita TWA); manter para Android se quisermos recursos nativos depois |
| Reescrita nativa | Swift/Kotlin puro | altíssimo | ❌ fora de questão hoje |

**Decisão do estudo:** Android via **TWA** (rápido, segue o site), iOS via **Capacitor apontando para mokareader.com** (ou bundle estático — a app já é quase toda client-side; a rota `/api/proxy` do BYOK segue hospedada na Vercel e o app empacotado aponta pra ela).

**Detalhe Mac:** o Miguel roda Linux — build iOS precisa de macOS. Solução: **build em nuvem** (Codemagic, Expo EAS Build, ou runner macOS do GitHub Actions). Não precisa comprar um Mac.

---

## 3. Pré-requisitos por loja (checklists)

### Google Play (organização)
- [ ] Conta Play Console organização — US$ 25
- [ ] **D-U-N-S** da empresa (§4)
- [ ] `assetlinks.json` em `https://www.mokareader.com/.well-known/assetlinks.json` (prova de domínio pro TWA)
- [ ] Ícone 512×512 + feature graphic 1024×500 + 2+ screenshots (telefone e tablet/iPad)
- [ ] **Formulário Data Safety**: o app guarda dados localmente (IndexedDB), envia e-mail da compra pra nossa API, usa provedores de IA — declarar cada um
- [ ] Classificação de conteúdo (livre/everyone)
- [ ] Política de privacidade — JÁ TEMOS: mokareader.com/privacidade ✅

### Apple App Store (organização)
- [ ] Apple Developer Program Organization — US$ 99/ano
- [ ] **D-U-N-S** (o mesmo)
- [ ] Capacitor wrap + build em nuvem (Codemagic/EAS)
- [ ] Ícones + screenshots 6.7" e 6.5" e iPad 12.9"
- [ ] **App Privacy Details** (equivalente ao Data Safety)
- [ ] Notas de revisão + conta demo (para o revisor testar: usar a conta vitalícia do Miguel ou um cupom)

---

## 4. D-U-N-S — o gargalo real (começar JÁ)

- O que é: identificador internacional de empresas da Dun & Bradstreet, exigido por Google (org) e Apple (org).
- Como tirar no Brasil: **grátis** no site da D&B (ou via BvD — Boa Vista Dados, parceiro brasileiro). Prazo típico: **2–4 semanas** (às vezes dias). É o item mais lento de todo o plano — **abrir o pedido esta semana**.
- Dados necessários: CNPJ, razão social, endereço, telefone da empresa.

---

## 5. Cronograma proposto

| Semana | Ação |
|---|---|
| 1 | Pedir D-U-N-S · abrir Play Console (org, US$25) · gerar assetlinks.json · pacote TWA (Bubblewrap) |
| 2 | TWA em teste interno na Play · screenshots + textos da loja (PT/EN) · abrir Apple Developer (org) assim que o D-U-N-S sair |
| 3 | Produção no Google Play 🎉 · Capacitor iOS + build em nuvem · App Store Connect |
| 4 | Revisão Apple (1–3 dias) → Moka nas duas lojas |

**Android sai primeiro** (semana 2–3) porque org pula o teste dos 20; iOS depende do D-U-N-S + revisão.

---

## 6. Riscos e notas

1. **Apple e "app que é só um site"**: a regra 4.2 da Apple pode reclamar de apps "web wrapper sem valor nativo". Mitigação: recursos nativos via Capacitor (compartilhar, downloads locais, leitura offline — que já existem no PWA) + revisão bem escrita. O Moka tem valor real de app (biblioteca local, leitura offline, PWA instalável) — apresentar assim.
2. **Data Safety honesto**: declarar e-mail da compra e uso de IA — não esconder (reprovação por omissão é comum).
3. **Pagamentos**: vendemos por Pix/Mercado Pago FORA da loja. **Apple proíbe venda de bens digitais fora do IAP dentro do app iOS.** Mitigação: no iOS, a compra abre no navegador (Safari externo) — modelo aceito (reader apps), ou avaliar IAP depois. ⚠️ Ponto a tratar com cuidado na revisão.
4. **Versão**: alinhar o nome "Moka" e o ícone nas duas lojas; checar se "Moka" está livre nas lojas (há apps com nome parecido — avaliar "Moka Reader" se necessário).
