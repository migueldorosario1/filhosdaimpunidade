// ============================================================================
// Proxy serverless — Kimi 3 (Moonshot AI)
// ----------------------------------------------------------------------------
// Por quê existe: a api.moonshot.ai NÃO envia headers Access-Control-Allow-*
// (preflight OPTIONS retorna 204 vazio), então o navegador bloqueia a chamada
// direta feita pelo Estúdio Editorial. Este proxy same-origin (/api/kimi)
// recebe o POST do navegador e repassa à Moonshot no lado do servidor, onde
// CORS não se aplica.
//
// Segurança da chave (ordem de precedência):
//   1. process.env.MOONSHOT_API_KEY — definir no dashboard da Vercel
//      (recomendado: a chave nunca sai do servidor);
//   2. Header Authorization: Bearer <chave> enviado pelo cliente — usa a chave
//      salva no localStorage do próprio usuário (tráfego same-origin, sem
//      terceiros). NUNCA rotear via proxy CORS público.
//
// Auditoria QA Kimi 3 — 2026-07-29 (commit f2be4375 + esta entrega).
// ============================================================================

export const config = { maxDuration: 60 };

const ALLOWED_ORIGINS = [
  'https://filhosdaimpunidade.vercel.app',
  'http://localhost:3000',
  'http://127.0.0.1:3000',
  'http://localhost:8000',
  'http://127.0.0.1:8000'
];

export default async function handler(req, res) {
  const origin = req.headers.origin || '';
  if (ALLOWED_ORIGINS.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') {
    return res.status(405).json({ error: { message: 'Method not allowed — use POST.' } });
  }

  const clientAuth = req.headers.authorization || '';
  const apiKey = process.env.MOONSHOT_API_KEY
    || (clientAuth.startsWith('Bearer ') ? clientAuth.slice(7).trim() : '');

  if (!apiKey) {
    return res.status(401).json({
      error: {
        message: 'Chave Moonshot não configurada. Defina MOONSHOT_API_KEY na Vercel ou salve a chave no modal ⚙️ Configurações do Estúdio.'
      }
    });
  }

  try {
    const body = typeof req.body === 'string' ? req.body : JSON.stringify(req.body || {});
    const upstream = await fetch('https://api.moonshot.ai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body
    });

    const text = await upstream.text();
    res.status(upstream.status);
    res.setHeader('Content-Type', upstream.headers.get('content-type') || 'application/json');
    return res.send(text);
  } catch (err) {
    return res.status(502).json({
      error: { message: `Falha no proxy Kimi ao contatar a Moonshot: ${err.message || err}` }
    });
  }
}
