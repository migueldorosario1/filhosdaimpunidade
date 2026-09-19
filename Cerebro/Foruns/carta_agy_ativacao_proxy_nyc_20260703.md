# Ativação do proxy residencial IPRoyal com geolocalização em Nova York (NYC)

**Destinatário:** Chairman Miguel & Trindade  
**Remetente:** Antigravity (AGY-CLI)  
**Data:** 2026-07-03 00:12 BRT  

Registramos a ativação e configuração do proxy residencial pago da IPRoyal com geolocalização apontando para New York (NYC), conforme instrução do Chairman Miguel no chat operacional.

### 1. Testes de rota e formatação do provedor

Realizamos testes de conectividade na rota da IPRoyal (`geo.iproyal.com:12321`) com diferentes identificadores de estado americanos para mapear a sintaxe aceita:
* `new_york` -> 🔴 Rejeitado (HTTP 503 from proxy)
* `new-york` -> 🔴 Rejeitado (HTTP 503 from proxy)
* `ny` -> 🔴 Rejeitado (HTTP 503 from proxy)
* `newyork` -> 🟢 Aceito (HTTP 200 OK)

### 2. Validação técnica de IP residencial (Verizon Fios)

Efetuamos um request de teste utilizando o identificador `newyork` e uma nova session ID dinâmica (`KgtDBt25` para garantir que o pool residencial entregasse um IP limpo e dinâmico, sem cache de reputação anterior):
* **IP retornado:** `71.190.106.216`
* **Hostname:** `pool-71-190-106-216.nycmny.fios.verizon.net`
* **Cidade/Região:** Glen Cove, New York, EUA
* **Provedor (ISP):** AS701 Verizon Business (Conexão residencial de fibra Verizon Fios)
* **Timezone:** America/New_York

### 3. Configuração aplicada no sistema local

1. **Script de controle:** Atualizamos e salvamos o script local [toggle_proxy.sh](file:///home/migueldorosario/.gemini/antigravity-cli/brain/5b55ae63-0082-4c43-b1a5-a330b724fd30/scratch/toggle_proxy.sh) na pasta de scratch da sessão atual.
2. **Ajuste de schemas GNOME:** Removemos a tentativa de aplicar propriedades de autenticação no schema HTTPS (`org.gnome.system.proxy.https`), que no GNOME atual gera alertas por suportar apenas `host` e `port` (herdando a autenticação do HTTP).
3. **Ativação:** Executamos o script, atualizando as chaves do `gsettings` do sistema operacional. O tráfego do desktop GNOME agora passa pelo proxy residencial de Nova York com as credenciais corretas.

### 4. Diagnóstico de geolocalização (Texas vs. NYC)

Após a configuração, o Chairman relatou no chat que o IP ainda aparecia localizado no Texas. Realizamos a seguinte triagem:
1. **Verificação de rede local:** O comando `nmcli` e a tabela de rotas mostraram que nenhuma VPN do VPN Gate (como `vpngate_texas`) ou processo solto do OpenVPN está ativo na máquina. O IP direto do terminal sem proxy sai limpo pelo provedor brasileiro (Niterói, RJ).
2. **Checagem de schemas:** Re-consultamos o `gsettings` e confirmamos que a senha configurada no GNOME está apontando corretamente para `newyork` com a sessão `KgtDBt25`.
3. **Múltiplos bancos de dados:** Consultas de geolocalização para o IP alocado (`71.190.106.216`) no `ipinfo.io` e `ip-api.com` confirmam Glen Cove, New York.
4. **Hipóteses para o browser:**
   * **Cache de conexão TCP (Keep-Alive):** O browser pode estar retendo sessões TCP ativas abertas com o proxy apontando para a Flórida ou Texas. Fechar e abrir o browser (ou limpar cookies/cache) força o restabelecimento da sessão com o novo IP.
   * **Base de dados do site desatualizada:** Se o site de teste do IP (ex: meuip) estiver usando uma base geográfica desatualizada, ele pode mapear o IP residencial rotativo da Verizon como Texas.
   * **Configuração interna no browser:** Se o browser estiver com proxy manual estático configurado diretamente em suas preferências internas (em vez de usar o proxy do sistema), ele continuará saindo pela senha antiga do Texas.

### 5. Resolução de bloqueio no site governamental PACER (.gov)

O Chairman reportou que o site judicial `pacer.uscourts.gov` estava retornando `ERR_TUNNEL_CONNECTION_FAILED` no browser.
* **Diagnóstico:** Executamos testes via proxy e detectamos que o servidor de proxy da IPRoyal bloqueia ativamente conexões ao site `uscourts.gov` com **HTTP 403 Forbidden** (X-Response-Origin: proxy-server). Trata-se de uma política de segurança padrão do provedor comercial para evitar scraping de portais judiciais e governamentais.
* **Verificação sem proxy:** O teste direto de conexão ao PACER a partir do IP real brasileiro de Niterói obteve **HTTP 200 OK** instantâneo, provando que o site governamental aceita acessos do Brasil e o bloqueio era estritamente no proxy.
* **Ação corretiva aplicada (Bypass):**
  1. Atualizamos o script [toggle_proxy.sh](file:///home/migueldorosario/.gemini/antigravity-cli/brain/5b55ae63-0082-4c43-b1a5-a330b724fd30/scratch/toggle_proxy.sh) e injetamos o bypass de domínios governamentais no GNOME via gsettings.
  2. Adicionamos os padrões `.gov` e `.gov.br` na lista `ignore-hosts` do sistema.
  3. Com isso, a navegação para o PACER e outros portais públicos do governo ignora o proxy e conecta diretamente com a internet padrão (Niterói), resolvendo o erro de conexão, enquanto o restante da navegação de terceiros continua com o proxy de Nova York ativo.

### 6. Desativação do proxy residencial IPRoyal

Às 00:32 BRT, o Chairman solicitou o desligamento do proxy residencial da IPRoyal (mencionando o hash `recent:///8c08a642adba9e0bcf41f6d26a472d0d` referente a um recurso ou aba recente com erro de conexão).
* **Ação realizada:** Executamos o script `/home/migueldorosario/.gemini/antigravity-cli/brain/5b55ae63-0082-4c43-b1a5-a330b724fd30/scratch/toggle_proxy.sh off` e desativamos o proxy do GNOME globalmente (`gsettings set org.gnome.system.proxy mode 'none'`).
* **Status atual:** O tráfego do desktop GNOME voltou à rota padrão direta sem proxy (IP real Claro/Virtua Niterói, Brasil).

### 7. Bloqueio de ativação de pagamento no portal do PACER

O Chairman relatou falha contínua ao tentar ativar os privilégios de busca no PACER com cinco cartões diferentes:
1. Cartão MasterCard final `3982` (BIN `223786` - BR, expirando em 07/2034)
2. Cartão MasterCard final `0693` (BIN `223786` - BR, expirando em 06/2034)
3. Cartão Visa final `3572` (BIN `407838` - Neon BR, expirando em 07/2033)
4. Cartão Visa final `0029` (BIN `439701` - Wise BR, expirando em 07/2031)
5. Cartão Visa final `3076` (BIN `400180` - Nomad EUA, expirando em 04/2031)

Todas as tentativas falharam com o erro: *Instant Activation failed. Error validating payment data*.
* **Status de emissores e recursos:** O Chairman informou que não possui cartões de crédito pós-pagos tradicionais (apenas contas digitais/globais). O cartão Nomad com endereço de faturamento oficial (`8916 Jamaica Ave, Woodhaven, NY, 11421`) continuou falhando.
* **Causa do bloqueio contínuo:** A validação eletrônica de hold temporário falha se a conta Nomad estiver com saldo zerado (US$ 0.00). Caso o saldo esteja positivo e o gateway do PACER continue rejeitando cartões pré-pagos de débito por razões de política de assinatura recorrente trimestral, a ativação eletrônica direta fica inviabilizada.
* **Resolução proposta:**
  1. **Adicionar saldo à Nomad:** Inserir saldo mínimo de US$ 2.00 na conta corrente Nomad e tentar novamente a submissão com o faturamento do app (`8916 Jamaica Ave`).
  2. **Liberação por Invoice (Suporte do PACER):** Solicitar ao suporte do PACER (`pacer@psc.uscourts.gov`) a ativação manual da conta por fatura trimestral (*Invoice Billing*), que dispensa a garantia de cartão na ativação inicial.
  3. **Uso de alternativas agregadoras:** Apresentamos alternativas públicas e gratuitas para consulta de processos nos EUA que não exigem cartão de crédito para busca de dados e dockets básicos (como **CourtListener** e **Justia Dockets**).
  4. **Uso de plataformas comerciais privadas:** Sugerimos a utilização de plataformas privadas (como **Docket Alarm** e **PacerMonitor**) que servem de interface ao PACER via API, pois elas processam pagamentos através de gateways comerciais (Stripe/Paypal) que aceitam cartões pré-pagos e de débito sem as restrições do PACER.

— Antigravity (AGY-CLI)
