# 02 — Arquitetura do Sistema de Pontos

## Componentes (todos construídos e validados em 22/07)

### 1. Banco de dados (`moka_pontos.db`, SQLite→Postgres)
Schema: `Projeto Cafezinho Agentes/Foruns/moka_pontos_schema_v1.sql`

7 tabelas: `usuarios` · `convites` · `carteiras` · `creditos` · `consumo` · `compras` · `precos_acoes`
3 views: `v_saldos` (painel do usuário) · `v_margem_usuario` (receita×custo por usuário) · `v_custo_diario` (alarme de estouro)

Decisões-chave:
- **Preço das ações em tabela** (`precos_acoes`) — muda sem deploy
- **`custo_usd` por consumo** — margem histórica exata mesmo se API mudar de preço
- Senha: pbkdf2-sha256+sal (stdlib)

### 2. API (`Projeto Cafezinho Agentes/moka_pontos/app.py`, FastAPI :8420)

| Endpoint | O que faz | Proteções testadas |
|---|---|---|
| `POST /convite/resgatar` | cria conta + credita 200 pts do código | convite 1 uso, expiração, e-mail único, 409 reuso |
| `GET /painel/saldo` | saldo + últimas 20 ações (auth email+senha) | 401 credenciais |
| `POST /consumir` | debita pontos da ação | **402 anti-estouro**, preço do banco |
| `POST /compras/webhook` | confirma pagamento do gateway | **HMAC-SHA256**, idempotente |

### 3. Fluxos

**Convite (amostra):** Miguel gera lote → usuário resgata com email+senha → carteira 200 pts → consome por ação → 402 quando zera → compra pacote (webhook credita)

**Metering no app:** antes de cada ação, o app chama `/consumir`; só executa se debitar. LLM e custo real são registrados por linha (auditoria de margem).

## A construir (próximos passos)
- Gerador de lotes de convites (CLI)
- Tela do painel (HTML no `/painel/saldo`)
- Tabelas `assinantes` + `titulos_capital` (extensão do schema)
- Webhook real Mercado Pago
