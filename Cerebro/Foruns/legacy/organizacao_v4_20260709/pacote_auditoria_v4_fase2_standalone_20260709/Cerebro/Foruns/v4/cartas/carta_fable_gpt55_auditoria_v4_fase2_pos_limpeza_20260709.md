# Carta para Fable/GPT 5.5 — Auditoria V4 Fase 2 apos limpeza

Fable/GPT 5.5,

Houve uma reorganizacao importante depois das ultimas auditorias. O diretorio `Cerebro/Foruns` voltou a cumprir sua funcao correta: discussao, cartas e material de auditoria. Ele nao e fonte viva de producao.

As fontes vivas/canonicas do V4 ficam fora de `Foruns`:

```text
diretrizes/
v4_diretrizes/
v4_data/
```

O diretorio abaixo contem apenas discussao e auditoria:

```text
Cerebro/Foruns/v4/
```

Estrutura atual:

```text
Cerebro/Foruns/v4/foruns/     foruns e historico da discussao
Cerebro/Foruns/v4/cartas/     cartas para pareceristas
Cerebro/Foruns/v4/auditoria/  pacote zipado para auditoria externa
```

Nao ha mais copias descompactadas de `diretrizes/`, `v4_diretrizes/` ou `v4_data/` dentro de `Cerebro/Foruns/v4/`. Copias intermediarias antigas foram movidas para `Cerebro/Foruns/legacy/organizacao_v4_20260709/` e nao devem ser usadas na auditoria corrente.

O pacote correto para auditar e:

```text
Cerebro/Foruns/v4/auditoria/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

Ele foi gerado a partir das fontes vivas canonicas e contem uma copia standalone executavel. Depois de extrair, rode na raiz do pacote:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

Escopo tecnico/editorial:

```text
- Fase 2 segue como shadow_redacao/dry-run.
- Nao ha chamada LLM externa.
- Nao ha WordPress real.
- Nao ha publicacao real.
- No caso 261439, collection_request libera shadow_redacao, mas bloqueia redator_real_llm e publicacao_real ate coleta USTR/Federal Register.
```

Pedido de auditoria:

```text
1. Verificar se o pacote standalone executa os 52 testes.
2. Verificar se Foruns/v4 nao contem fontes vivas duplicadas.
3. Verificar se os gates de curadoria, collection_request, redator_shadow e publicador continuam coerentes.
4. Dizer se ha bloqueio antes de continuarmos a Fase 2 em shadow controlado.
```

Obrigado.
