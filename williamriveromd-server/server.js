require('dotenv').config();
const express = require('express');
const fetch = require('node-fetch');
const rateLimit = require('express-rate-limit');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json({ limit: '32kb' }));

// Redirect apex to www
app.use((req, res, next) => {
  if (req.hostname === 'williamriveromd.com') {
    return res.redirect(301, 'https://www.williamriveromd.com' + req.originalUrl);
  }
  next();
});

app.use(express.static(path.join(__dirname, '..'), {
  extensions: ['html'],
  index: 'index.html',
}));

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  message: { error: 'Too many requests — please wait a few minutes.' }
});
app.use('/api/', apiLimiter);

app.post('/api/analyze', async (req, res) => {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return res.status(500).json({ error: 'API key not configured.' });
  }
  const { messages, model, max_tokens } = req.body;
  if (!messages || !Array.isArray(messages) || messages.length === 0) {
    return res.status(400).json({ error: 'Invalid request.' });
  }
  for (const msg of messages) {
    const content = typeof msg.content === 'string' ? msg.content.trim() : '';
    if (!content) {
      return res.status(400).json({ error: 'Message content must be non-empty.' });
    }
  }
  const safeModel = 'claude-haiku-4-5-20251001';
  const safeMaxTokens = Math.min(max_tokens || 1200, 2000);
  try {
    const upstream = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({ model: safeModel, max_tokens: safeMaxTokens, messages }),
    });
    const data = await upstream.json();
    return res.status(upstream.status).json(data);
  } catch (err) {
    return res.status(502).json({ error: 'Failed to reach Anthropic API.' });
  }
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
