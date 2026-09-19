-- MOKA · Sistema de Pontos — Schema v1 (2026-07-22)
-- SQLite para desenvolvimento local; 100% compatível com Postgres (ajustar tipos marcados).

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ============================================================
-- 1. USUÁRIOS
-- ============================================================
CREATE TABLE usuarios (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,  -- BIGSERIAL no Postgres
    email           TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    senha_hash      TEXT NOT NULL,                      -- bcrypt/argon2 — NUNCA senha crua
    status          TEXT NOT NULL DEFAULT 'ativo',      -- ativo | bloqueado | excluido
    origem          TEXT NOT NULL DEFAULT 'convite',    -- convite | organico | admin
    device_fp       TEXT,                               -- fingerprint anti-farm (opcional)
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    last_login_at   TEXT
);
CREATE INDEX idx_usuarios_email ON usuarios(email);

-- ============================================================
-- 2. CONVITES (amostra grátis — 200 pts por código)
-- ============================================================
CREATE TABLE convites (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo          TEXT NOT NULL UNIQUE,               -- ex.: MOKA-7F3K2
    pontos          INTEGER NOT NULL DEFAULT 200,       -- pontos que o código concede
    lote            TEXT,                               -- ex.: 'funcionarios-2026-07' (rastreabilidade da campanha)
    max_usos        INTEGER NOT NULL DEFAULT 1,         -- 1 = código individual
    usos            INTEGER NOT NULL DEFAULT 0,
    expira_em       TEXT,                               -- NULL = sem expiração
    ativo           INTEGER NOT NULL DEFAULT 1,
    criado_por      TEXT NOT NULL DEFAULT 'admin',      -- quem gerou o lote
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    resgatado_por   INTEGER REFERENCES usuarios(id),
    resgatado_em    TEXT
);
CREATE INDEX idx_convites_codigo ON convites(codigo);

-- ============================================================
-- 3. CARTEIRA (saldo consolidado por usuário)
-- ============================================================
CREATE TABLE carteiras (
    usuario_id      INTEGER PRIMARY KEY REFERENCES usuarios(id),
    saldo_pontos    INTEGER NOT NULL DEFAULT 0,         -- cache do saldo (fonte rápida de leitura)
    total_creditado INTEGER NOT NULL DEFAULT 0,         -- soma histórica de créditos
    total_consumido INTEGER NOT NULL DEFAULT 0,         -- soma histórica de débitos
    updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ============================================================
-- 4. LEDGER DE CRÉDITOS (toda entrada de pontos)
-- ============================================================
CREATE TABLE creditos (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id      INTEGER NOT NULL REFERENCES usuarios(id),
    pontos          INTEGER NOT NULL,                   -- >0 crédito, <0 estorno
    tipo            TEXT NOT NULL,                      -- convite | compra | bonus | estorno | admin
    referencia_id   INTEGER,                            -- id do convite ou da compra
    descricao       TEXT NOT NULL,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX idx_creditos_usuario ON creditos(usuario_id);

-- ============================================================
-- 5. CONSUMO (toda saída de pontos, com custo real em USD p/ margem)
-- ============================================================
CREATE TABLE consumo (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id      INTEGER NOT NULL REFERENCES usuarios(id),
    acao            TEXT NOT NULL,                      -- resumo_video | resumo_livro | traducao_livro | tts | tts_premium
    recurso_ref     TEXT,                               -- url do vídeo / id do livro
    pontos          INTEGER NOT NULL,                   -- pontos debitados (ex.: 30)
    custo_usd       REAL NOT NULL DEFAULT 0,            -- custo REAL da API naquele momento (auditoria de margem)
    llm_usada       TEXT,                               -- ex.: 'deepseek-chat' (rastreio de rota)
    status          TEXT NOT NULL DEFAULT 'ok',         -- ok | falhou | estornado
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX idx_consumo_usuario ON consumo(usuario_id);
CREATE INDEX idx_consumo_acao ON consumo(acao, created_at);

-- ============================================================
-- 6. COMPRAS (pacotes pagos)
-- ============================================================
CREATE TABLE compras (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id      INTEGER NOT NULL REFERENCES usuarios(id),
    pacote          TEXT NOT NULL,                      -- starter | leitor | premium
    pontos          INTEGER NOT NULL,                   -- 500 | 1500 | 4000
    valor_brl       REAL NOT NULL,                      -- 19.90 | 49.90 | 99.90
    gateway         TEXT NOT NULL DEFAULT 'mercadopago',-- mercadopago | stripe | pix_manual
    gateway_ref     TEXT,                               -- id da transação no gateway
    status          TEXT NOT NULL DEFAULT 'pendente',   -- pendente | pago | cancelado | reembolsado
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    pago_em         TEXT
);
CREATE INDEX idx_compras_usuario ON compras(usuario_id);
CREATE INDEX idx_compras_status ON compras(status);

-- ============================================================
-- 7. TABELA DE PREÇOS DAS AÇÕES (configuração viva — nunca hardcode)
-- ============================================================
CREATE TABLE precos_acoes (
    acao            TEXT PRIMARY KEY,                   -- resumo_video | resumo_livro | traducao_livro | tts | tts_premium
    pontos          INTEGER NOT NULL,
    ativo           INTEGER NOT NULL DEFAULT 1,
    descricao       TEXT
);
INSERT INTO precos_acoes (acao, pontos, descricao) VALUES
    ('resumo_video',    30,  'Resumir vídeo de até 10 minutos'),
    ('resumo_livro',    40,  'Resumir 1 livro'),
    ('traducao_livro',  80,  'Traduzir livro inteiro (até ~500 páginas)'),
    ('tts',             20,  'Áudio de 10 min (voz padrão)'),
    ('tts_premium',    150,  'Áudio de 10 min (voz ElevenLabs)');

-- ============================================================
-- VIEWS PRONTAS PARA O PAINEL
-- ============================================================

-- Saldo por usuário (conferência ledger × carteira)
CREATE VIEW v_saldos AS
SELECT u.id, u.email, u.nome,
       w.saldo_pontos, w.total_creditado, w.total_consumido,
       (SELECT COUNT(*) FROM consumo c WHERE c.usuario_id = u.id) AS acoes_realizadas
FROM usuarios u
JOIN carteiras w ON w.usuario_id = u.id;

-- Margem por usuário (pontos vendidos × custo real)
CREATE VIEW v_margem_usuario AS
SELECT u.email,
       COALESCE(SUM(DISTINCT cp.valor_brl), 0)            AS receita_brl,
       COALESCE(SUM(c.custo_usd), 0)                      AS custo_usd,
       COALESCE(SUM(c.pontos), 0)                         AS pontos_consumidos
FROM usuarios u
LEFT JOIN compras cp ON cp.usuario_id = u.id AND cp.status = 'pago'
LEFT JOIN consumo c ON c.usuario_id = u.id AND c.status = 'ok'
GROUP BY u.id;

-- Custo do dia (para o alarme de estouro)
CREATE VIEW v_custo_diario AS
SELECT date(created_at) AS dia, COUNT(*) AS acoes,
       SUM(pontos) AS pontos, SUM(custo_usd) AS custo_usd
FROM consumo WHERE status = 'ok'
GROUP BY date(created_at);
