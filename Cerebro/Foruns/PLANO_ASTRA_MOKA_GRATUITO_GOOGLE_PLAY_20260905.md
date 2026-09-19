# Plano Astra — Moka gratuito na Google Play e sustentabilidade

Data: 05/09/2026. Autor: Astra, apoio interno AST. Estado: PLANEJAMENTO PARA REVISÃO DO DS-N CHEFE E DO DONO DA OBRA (ZM); não é autorização de deploy, gasto ou publicação.

## 1. Entendimento e recomendação

Miguel quer levar o Moka/Mocha à Google Play, manter o aplicativo gratuito e encontrar receita para sustentá-lo. O nome do produto nos materiais é **Moka**. A ordem atual de gratuidade prevalece sobre planos comerciais antigos: não reativar pontos pagos, assinatura, licença, checkout ou captação do plano de julho.

**Recomendação: concluir e qualificar a TWA Android que já existe, mantendo o pacote `com.mokareader.app`; não criar outro aplicativo, pagar outra conta ou reescrever tudo.** O projeto já passou por submissão e teve problema de acesso para revisão. O próximo trabalho é reconciliar o estado atual do Console, comprovar a experiência gratuita e corrigir os requisitos concretos, não recomeçar o empacotamento.

O produto não é um simples atalho para notícias: reúne Reader de EPUB/PDF, Video, Memória, Harness e Writer. A proposta pública deve explicar usos reais: ler e organizar obras; compreender trechos/vídeos; guardar contexto; conversar com IAs escolhidas; escrever. O núcleo gratuito deve entregar utilidade mesmo sem conta e sem chave. IA BYOK pode ter cobrança do provedor escolhido pelo usuário; **Moka gratuito não significa inferência ilimitada gratuita**. Nenhuma chave da casa será ativada para subsidiar uso sem orçamento e autorização expressa.

## 2. O que foi efetivamente verificado

Repositório solicitado: `/home/migueldorosario/ZCodeProject/moka-app`, branch `obra/memoria`, HEAD `5159cca` de 03/09/2026 09:58:49 -03; worktree limpo nas consultas. Foram lidos AGENTS, README e ROADMAP antes da análise. Os três conservam referências antigas a “igot/scaffold”; não representam o estágio real do código. Não alterei o repositório, cofres, serviço ou conta externa.

| Evidência local | Achado e limite |
|---|---|
| `apps/web/package.json:14` | Next.js 14, React 18, TypeScript, Supabase; não é projeto Expo/React Native. |
| `apps/web/src/components/Capa.tsx:61` | Entradas Reader, Video, Memória, Harness e Writer. O fórum de marketing de 03/09 confirma os cinco módulos. |
| `apps/web/public/manifest.json:1` e `sw.js:19` | PWA com manifesto, ícones, modo standalone e service worker; cache inicial da home, demais recursos sob demanda. Offline completo é requisito de teste, não certificado por existência do SW. APIs de IA não são cacheadas. |
| `apps/web/src/lib/repository.ts:43` | Persistência local; com usuário autenticado envia livro parseado, notas e traduções ao Supabase. Não é correto dizer que nenhum conteúdo sai do dispositivo. |
| `apps/web/src/app/api/proxy/route.ts:8` e `:110` | Proxy recebe e encaminha credenciais/conteúdo ao provedor; comentário e implementação pretendem não persistir a chave. “Não persistida no servidor” não equivale a “nunca passa pelo servidor”. |
| `apps/twa/twa-manifest.json:2` | TWA Bubblewrap, host `www.mokareader.com`, package `com.mokareader.app`, versão 5.7.1/code 1, fallback Custom Tabs. Caminho de assinatura aponta para clone antigo; não abri o keystore. |
| `apps/twa/app/build.gradle:54` | `compileSdkVersion 36`, `targetSdkVersion 36`, min SDK 21; versão/code 5.7.1/1. Isso prova a fonte, não o conteúdo do artefato já enviado. |
| `apps/web/public/moka-app.aab` | AAB existente: 1.521.600 bytes, mtime 19/08/2026. Os APK/AAB dos caminhos antigos `apps/twa/` não aparecem neste clone. Não reconstruí nem assinei. |
| `apps/web/public/.well-known/assetlinks.json:6` | Declara o pacote e uma impressão pública de certificado. Ainda precisa comparação com **App signing certificate** do Play, não apenas com upload key. |
| Busca de arquivos fora de dependências/backups | TWA existente; não localizei configuração Capacitor nem Expo. A ausência neste recorte não exclui outros projetos do ecossistema. |

O domínio de produção, os espelhos Vercel e esta branch não foram tratados como equivalentes. Esta rodada não executou teste de aparelho, build, chamada de IA ou inspeção autenticada do Play Console. O estado de produção deve ser associado a commit/deploy e ao artefato correto antes de mudar qualquer coisa.

## 3. Histórico da Play: o que não repetir

Fonte: `Foruns/forum_moka_twa_android_play_store_20260807.md`, especialmente adendos de 13/08 e 27/08; `Foruns/forum_moka_sem_login_fix_play_paywall_20260819.md`.

- 07/08: projeto TWA e artefatos construídos, assetlinks publicado. A lista antiga “criar conta/pagar US$25” ficou superada pelo avanço posterior.
- 13/08: prints documentaram conta/app e submissão; declarações preenchidas. Não tomar “a bola está com o Google”, escrito naquela data, como situação atual.
- 19/08: rejeição por acesso/paywall percebido. O fórum documenta remoção do login obrigatório e posterior retirada de `/socios` da fase gratuita.
- 27/08: texto BYOK revisado; Console mostrou “Contestação enviada”, embora a resposta enviada por e-mail ao remetente no-reply não fosse um canal válido. São fatos distintos: o e-mail falhou; a tela registrou contestação.
- Último adendo lido, 01/09: consulta de e-mail falhou por autenticação. Isso **não prova ausência de resposta hoje**. Falta conferir a tela atual de Policy status, App access, Publishing overview e a versão efetivamente em análise.

O documento antigo `PLANO_NEGOCIOS_MOKA/documentos/16_lojas_play_store_app_store.md` é referência histórica, não checklist vigente: menciona 20 testadores e publicação quase automática por ser organização. O requisito pessoal hoje é 12/14; organização continua sujeita à revisão. O doc 18 contém uma boa ideia de catálogo opt-in, mas pontos, instalações de fórum e promessas amplas de direitos não serão retomados automaticamente. `07_proximos_passos.md` é backlog pago antigo, fora desta execução.

## 4. Requisitos atuais e sua aplicação

Fontes oficiais consultadas em 05/09/2026. A decisão final de aprovação é do Google; organização/TWA não garante aprovação nem prazo.

| Tema | Regra e ação proposta |
|---|---|
| Conta e taxa | A taxa de inscrição Play é US$25, uma vez por conta. Primeiro confirmar a conta já utilizada; não pagar novamente. Conta de organização exige verificação e D-U-N-S. Se realmente faltar uma conta válida, **AGUARDA VAI DO MIGUEL**, após explicar por que a existente não serve. [Cadastro Play](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en), [tipos de conta](https://support.google.com/googleplay/android-developer/answer/13634885?hl=en). |
| Teste pessoal | Para contas pessoais criadas após 13/11/2023: teste fechado com pelo menos 12 participantes inscritos continuamente por 14 dias, seguido de pedido de acesso à produção. Não atribuir essa obrigação à suposta conta organização sem confirmar o tipo; recomendar teste real em qualquer caso. [Requisito oficial](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en). |
| AAB e SDK | Novos apps são publicados em Android App Bundle. Desde 31/08/2026, novas submissões/atualizações Android móveis exigem target API 36. A fonte local já usa 36; verificar o AAB e o Console. Extensão não se presume concedida. Se houver novo upload, code deve superar o já usado. [AAB](https://developer.android.com/guide/app-bundle), [API alvo](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en). |
| TWA e domínio | TWA usa o navegador e Digital Asset Links; não é WebView genérica. Confirmar origem, associação com certificado de distribuição e fallback. Mudanças web refletem na TWA, mas o pacote Android também necessita manutenção; não afirmar “nunca mais atualiza na loja”. [TWA oficial](https://developer.chrome.com/docs/android/trusted-web-activity), [manutenção e qualidade](https://developer.chrome.com/docs/android/trusted-web-activity/whats-new). |
| Acesso do revisor | Fornecer instruções em inglês e acesso reutilizável a todas as funcionalidades, sem barreiras de localização/OTP. Login opcional não dispensa instruções para recursos de conta. Não declarar “tudo acessível” se IA/Harness exigirem configuração externa não fornecida. [Acesso para revisão](https://support.google.com/googleplay/android-developer/answer/15748846?hl=en). |
| Privacidade e conta | Política pública acessível no app/Console, coerente com processamento, retenção e terceiros. Se há criação de conta no app, deve existir solicitação de exclusão dentro dele e por recurso web externo, incluindo dados associados; logout não é exclusão. [User Data](https://support.google.com/googleplay/android-developer/answer/10144311). |
| Data Safety | Formulário deve refletir coleta/compartilhamento reais, inclusive bibliotecas/serviços terceiros; BYOK/local-first não justifica “nenhum dado coletado”. Fazer mapa por dado/destino/finalidade/retenção/consentimento. [Data Safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en). |
| IA generativa | Harness conversacional e Writer exigem análise além da exceção de um simples resumidor. Para recursos cobertos, implementar prevenção de conteúdo proibido e denúncia dentro do app. BYOK não elimina a responsabilidade do aplicativo. [Escopo](https://support.google.com/googleplay/android-developer/answer/14094294?hl=en), [política IA](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en-GB). |
| UGC | Biblioteca privada do usuário não demonstra por si uma comunidade pública. Se fórum, comentários ou compartilhamento entre usuários estiverem disponíveis, mapear termos, moderação, denúncia e bloqueio conforme o tipo de interação. Não instalar Discourse agora. [Moderação UGC](https://support.google.com/googleplay/android-developer/answer/12923286?hl=en). |
| Qualidade | Site próprio não é automaticamente proibido por estar empacotado. O problema é falta de permissão, spam, baixa utilidade ou experiência quebrada. Provar leitura, biblioteca, retomada, acessibilidade e comportamento offline/rede ruim. [Spam/WebViews](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en), [funcionalidade](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en). |

### Lacunas concretas para revisão antes de reenviar

1. **Política desatualizada/contraditória:** `privacidade/page.tsx:27` diz que livros ficam só no aparelho; `:40` e `:65` descrevem sync. `:78` afirma não usar rastreamento; `GoogleAnalytics.tsx:20` injeta GA4 no domínio canônico. Resolver com inventário real e consentimentos necessários, não só trocar frases. Data Safety antigo precisa ser revalidado.
2. **Exclusão de conta não demonstrada:** `privacidade/page.tsx:82` oferece remover livros/chaves e logout, não uma solicitação clara de exclusão da conta. Não localizei rota/fluxo explícito nas buscas desta rodada. Confirmar e propor recurso in-app + página externa; backend e descarte de dados só com autorização de implementação.
3. **Denúncia IA não demonstrada:** o feedback encontrado em `SiteFooter.tsx:52` é um `mailto:` genérico, que sai do app. Não prova o mecanismo exigido para sinalizar uma resposta ofensiva sem sair. Propor denúncia contextual e tratamento pelo operador, sem incluir livros/segredos indiscriminadamente no relato.
4. **Doações visíveis:** `SiteFooter.tsx:30` oferece PayPal e Pix. Não foi comprovado enquadramento de cada fluxo nem autorização da loja. Não esconder só do revisor ou trocar comportamento após aprovação. Avaliar uma política uniforme por distribuição/território e aprová-la antes de mudar.
5. **Revisão de IA sem gasto oculto:** a Biblioteca Livre local contém oito EPUBs (`apps/web/public/biblioteca-livre/`) e pode apoiar teste real do leitor sem conta/chave, após conferir licenças da edição. Isso não substitui acesso real às funções de IA. Não usar uma falsa resposta de demonstração como prova de IA funcionando. A estratégia para review de IA precisa ser confirmada com o tutor/Console; qualquer crédito, chave financiada ou infraestrutura nova fica **AGUARDA VAI DO MIGUEL** com teto e responsável.

## 5. Plano de execução por gates

| Gate | Entregável e critério para avançar | Quem/autoridade |
|---|---|---|
| G0 — estado verdadeiro | Evidência atual do Console: conta/tipo/verificação, package, política pendente, status da contestação, App access e AAB ativo. Vincular branch/commit ao deploy. Não reutilizar prints antigos como estado presente. | Miguel mostra/exporta tela; AST analisa; tutor prioriza; ZM confirma obra. |
| G1 — revisão do plano | DS-N Chefe valida esta rota e o dono da obra reserva arquivos. Lista precisa de mudanças separada de backlog de crescimento. | Nenhuma alteração no repo antes desta revisão e autorização cabível. |
| G2 — correções mínimas | Privacidade/Data Safety, exclusão de conta, denúncia IA, onboarding sem paywall, estratégia de review de recursos opcionais e doações. Preservar as cinco áreas úteis; não amputar funções apenas para enganar revisão. | Implementação futura pelo executor autorizado; backups/rollback e testes. |
| G3 — Android verificável | AAB existente inspecionado ou novo AAB construído somente se necessário; package/chave preservados, code correto, SDK 36 e Digital Asset Links conferidos com certificado Play. Sem chave nova. | ZM/engenharia autorizado; não há build nesta rodada. |
| G4 — teste de usuário | Matriz abaixo passada com provas e falhas abertas. Teste fechado 12/14 somente se aplicável; teste interno não equivale a aprovação. | Testadores convidados com consentimento; nada de comprar avaliações/testadores. |
| G5 — reenvio | Texto PT/EN, screenshots reais, permissões, idade/IARC/anúncios, privacy/Data Safety e acesso coerentes. Enviar pelo Console e guardar recibo. Não responder no-reply. | Miguel/operador autorizado, após revisão. Nenhuma data de aprovação prometida. |
| G6 — lançamento e acompanhamento | Só anunciar disponibilidade quando link público do pacote funcionar e instalação real estiver comprovada. Medir retenção e falhas; expansão de marketing exige vai próprio. | Miguel decide liberação; publicação editorial segue cadeia da casa. |

Matriz mínima de G4: instalação limpa pelo canal Play; primeira abertura sem login e sem chave; importar EPUB/PDF próprio e abrir amostra licenciada; navegar/selecionar/anotar/retomar livro; fechar/reabrir offline após carga; primeiro uso offline com aviso útil; login opcional, sync e exclusão; teclado, botão Voltar, orientação e fontes grandes; links externos com retorno; atualização do SW sem perder biblioteca; download/compartilhamento/permissões sem pedidos excessivos; IA com chave inválida/esgotada sem cobrança alternativa; teste de IA válido apenas com meio expressamente autorizado; vídeo indisponível/sem legenda com explicação honesta; denúncia de conteúdo e atendimento. Diferenciar teste da PWA, APK local e versão distribuída pela Play.

Não há estimativa honesta de data final antes de G0/G2. Diagnóstico e pacote de textos podem ser preparados já; correções, disponibilidade de testadores e revisão externa determinam o calendário.

## 6. Receita com núcleo gratuito — proposta, não execução

**Prioridade: patrocínio externo transparente da iniciativa e de conteúdos educativos**, negociado fora do aplicativo: uma marca/instituição pode apoiar uma série, oficina ou campanha de leitura no Cafezinho/canais próprios, sem comprar acesso à biblioteca particular e sem restringir funções do Moka. Separar editorial de publicidade; mostrar quem patrocina. Não contatar patrocinadores nem publicar campanha nesta rodada.

Reaproveitar o plano de marketing de 03/09: prints reais, banners, roteiros e pautas já existem. Piloto proposto de 30 dias: uma jornada “abrir primeiro livro em poucos passos”, público voluntário vindo dos canais próprios, demonstração da Biblioteca Livre com opt-in para adicionar itens, guia honesto de BYOK, feedback e retenção. A conta Google usada para sync **não é consentimento automático para e-mail/WhatsApp de marketing**. Lista só com adesão explícita, descadastro e supressão; nenhum disparo autorizado aqui.

Métricas propostas sem prometer faturamento: visitas qualificadas → primeiro livro aberto → retorno em sete dias; falhas de importação/leitura; entendimento do custo opcional da IA; interessados voluntários; propostas de patrocínio e receita efetivamente recebida. A coleta deve ser mínima e reconciliada com a política de privacidade. Não vender conteúdo de livros, chaves, histórico pessoal ou dados de usuários.

**Limite Play para monetização:** compra de funções/conteúdo digital no app normalmente requer Play Billing, salvo exceções/programas aplicáveis. Abrir navegador externo não cria uma exceção universal. Regras territoriais, inclusive EUA/EEE, exigem avaliação própria. Doação/contribuição sem vantagem digital pode ter tratamento específico; não assumir que qualquer Pix/PayPal é permitido. Nada de assinatura, pontos ou badge pago neste plano. [Política de pagamentos e exceções](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en).

Patrocínio dentro do app, anúncios/SDK de ads e remuneração que altere a experiência exigem proposta separada, revisão das declarações da Play e consentimentos; o registro histórico dizia “sem anúncios”. Crescimento de tráfego pode aumentar Vercel/Supabase/banda mesmo sem API da casa: monitorar antes de campanha. Hospedagem existente não significa custo incremental garantidamente zero.

| Item | Tratamento de custo e autorização |
|---|---|
| Este estudo e inventário de código | Sem compra, conta nova, build, deploy ou API de modelo contratada por esta tarefa. |
| Conta Play existente | Reusar se válida; sem repetir inscrição. Nova taxa US$25 só se necessidade comprovada: **AGUARDA VAI DO MIGUEL**. |
| Correções/build com ferramentas locais já disponíveis | Planejar dentro dos recursos existentes; nenhuma instalação/CI paga automática. Trabalho do executor e consumo de infraestrutura devem ser explicitados. |
| Crédito de IA/review, STT, imagens, hospedagem extra, e-mail em volume ou mídia paga | **AGUARDA VAI DO MIGUEL**, com provedor, teto incremental e condições. Sem cartão/top-up/fallback automático. |
| Apple, novo aplicativo, Discourse, planos premium e gateways antigos | Fora do escopo atual. Não contratar nem reativar. |

## 7. Entrega e próximo pedido ao tutor

**O que aconteceu:** produto e Android existentes foram identificados; histórico de rejeição reconciliado; requisitos Google atuais verificados em fontes primárias; plano gratuito e de receita externa preparado. Este arquivo é o único novo artefato desta subtarefa.

**O que falta:** evidência atual do Console/deploy; revisão do tutor e ZM; estratégia viável para o revisor testar recursos opcionais; correções/testes autorizados; decisão de reenvio. Não afirmar que falta pagar a conta, que o Google está mudo ou que o app já está pronto para aprovação.

**Pergunta proposta ao DS-N Chefe, via mediação escolhida por Miguel:** “Concorda em priorizar G0–G2 deste plano: retomar o pacote TWA existente, confirmar o estado atual da rejeição e fechar privacidade/exclusão/denúncia/acesso de revisão, mantendo núcleo gratuito e sem reativar assinatura/pontos? Quem executa as mudanças com o ZM, e qual forma sem gasto novo permite revisão real da IA?”

Do Miguel agora: acesso visual à tela atual do app no Play Console, sem compartilhar senha/token em chat; confirmação da prioridade do plano. **Nenhum pagamento é solicitado nesta etapa.**

Referências internas adicionais: `CEREBRO_INDEX_MOKA_MASTER.md`; `Foruns/forum_marketing_moka_20260903.md`; `Foruns/forum_moka_fase_gratuita_byok_doacao_20260804.md`; documentos 16 e 18 e `07_proximos_passos.md` do plano de negócios, usados como histórico com ressalvas, não como ordem vigente.


## AST-20260905-016 — prints recebidos e pesquisa atualizada

Miguel forneceu as capturas em 05/09 ~09:14 e confirmou que não recebeu outra resposta do Google. A tela mostra app rejeitado por acesso de revisão; as evidências são as instruções para obter chave e adicionar créditos de IA. O pacote está registrado; não há suspensão de conta demonstrada. O Console registra resposta à contestação, mas não comprova entrega do e-mail. Não manter como bloqueio 'aguardar primeira resposta/print'.

[Diagnóstico dos dez prints e próximo caminho](DIAGNOSTICO_ASTRA_PRINTS_PLAYSTORE_20260905.md): orientação oficial permite corrigir acesso e reenviar sem aguardar suporte, após testar e obter autorização. Preparada minuta em inglês para a Ajuda; nada enviado. Não basta remover login para provar acesso à IA. Custeio de teste não está autorizado e nenhuma solução integral sem gasto foi demonstrada. Privacidade/exclusão de conta e outras lacunas preventivas do plano acima não aparecem como novas acusações do Google nestes prints.
