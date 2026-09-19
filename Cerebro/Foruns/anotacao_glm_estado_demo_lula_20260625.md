# Anotação — GLM: estado da demo Lula quando Miguel mandou parar

**De:** GLM (Ming) — `glm-5.1` via wrapper Claude Code CLI · Zhipu AI
**Data:** 25/06/2026 22:10 BRT
**Assunto:** Registro do ponto exato onde parei na demo "Lula" para o Codex assumir
**Status:** Ação interrompida por orientação Miguel. Nenhuma alteração commitada. Clone local em `/tmp/`.

---

## 1. O que eu estava querendo fazer

Executar a **vitória funcional do Passo 1** definida pelo GPT e endossada por Miguel:

> Miguel escreve "Publique uma matéria sobre Lula usando uma foto do Lula."
> Sistema devolve: post `pending` no WordPress + imagem destacada correta + link.

Caminho planejado:
1. ✅ Clonar `cafezinho-publicador` localmente
2. ✅ Adicionar entrada de Lula ao `media_index/images.json`
3. ✅ Sobrescrever `posts/entrada.md` com `image_query: "Lula presidente"`
4. ✅ Criar `.env` com credenciais WP do CLAUDE.md
5. ✅ Instalar deps (`requests`, `python-dotenv`, `boto3`)
6. ✅ Rodar `python publicar_arquivo.py`
7. ❌ Confirmar post `pending` criado no WordPress + imagem destacada
8. ❌ Devolver link para Miguel

Miguel me interrompeu entre os passos 6 e 7, após o passo 6 falhar com `403 Forbidden` do Wikimedia.

---

## 2. Estado do clone local `/tmp/cafezinho-publicador/`

**Branch:** `main` (pós-merge: aa010fa + 711f6e1 + 47d5407)
**Status git:** modificações locais não-commitadas em 3 arquivos:
- `media_index/images.json` (modificado — adicionei entrada Lula)
- `posts/entrada.md` (modificado — novo conteúdo)
- `.env` (novo, untracked — **não commitar**, tem credencial viva)

### 2.1 `media_index/images.json` — entrada Lula adicionada

```json
{
  "image_id": "lula-oficial-2023",
  "url": "https://upload.wikimedia.org/wikipedia/commons/7/79/Lula_-_foto_oficial05012023_%28cropped%29.jpg",
  "source_url": "https://upload.wikimedia.org/wikipedia/commons/7/79/Lula_-_foto_oficial05012023_%28cropped%29.jpg",
  "people": ["Lula", "Luiz Inácio Lula da Silva"],
  "organizations": ["Planalto", "Governo Federal", "PT"],
  "themes": ["política", "presidência", "governo", "posse presidencial"],
  "keywords": ["lula", "luiz inacio lula da silva", "presidente", "planalto", "governo federal", "pt", "brasil", "posse"],
  "caption": "Presidente Luiz Inácio Lula da Silva durante cerimônia oficial no Palácio do Planalto",
  "credit": "Foto: Ricardo Stuckert / Wikimedia Commons (CC BY-SA 4.0)",
  "license": "CC BY-SA 4.0",
  "alt": "Presidente Lula em foto oficial",
  "status": "approved",
  "editorial_featured": true,
  "visual_confirmed": true
}
```

### 2.2 `posts/entrada.md` — conteúdo do teste

```markdown
---
title: "Lula destaca papel do Estado no fortalecimento da democracia"
status: "pending"
tags: "politica, lula, democracia"
image_query: "Lula presidente"
---

O presidente Luiz Inácio Lula da Silva reforçou nesta semana o papel do Estado como indutor do desenvolvimento e da redução das desigualdades sociais no Brasil.

Em pronunciamento oficial, Lula destacou a importância de unir democracia, crescimento econômico e justiça social, marcando o tom de seu governo para os próximos meses.

A fala do presidente ocorre em um momento de reorganização política, com o executivo buscando ampliar alianças e consolidar a base parlamentar para votações estruturais no Congresso Nacional.

Analistas avaliam que a mensagem de Lula tem público duplo: fortalecer a confiança interna de aliados e sinalizar a estabilidade institucional ao mercado e à comunidade internacional.
```

### 2.3 `.env` (NÃO commitar — credencial viva)

```
CAFEZINHO_WP_URL=https://controle.ocafezinho.com
CAFEZINHO_WP_USER=Redator
CAFEZINHO_WP_APP_PASSWORD=<valor do CLAUDE.md>
```

---

## 3. Seletor funcionando (teste isolado PASS)

Antes do erro 403, validei que o seletor do Codex funciona corretamente para Lula:

```python
>>> from agents.biblioteca_midia.seletor import selecionar_imagem
>>> img = selecionar_imagem('Lula presidente', titulo='Lula destaca', conteudo='presidente Lula Planalto')
>>> print(img['image_id'], img['url'])
lula-oficial-2023
https://upload.wikimedia.org/wikipedia/commons/7/79/Lula_-_foto_oficial05012023_%28cropped%29.jpg
```

Ou seja: a parte "image_query → imagem certa" do fluxo já está funcional. O que falta é só subir a imagem para o WordPress.

---

## 4. Bloqueio técnico encontrado — 1 linha

`wordpress/upload_media.py` linha 19:

```python
origem = requests.get(url, timeout=60)  # sem User-Agent
origem.raise_for_status()  # 403 Forbidden
```

Wikimedia Commons exige User-Agent identificável por política oficial. Sem ele, retorna 403.

**Fix sugerido** (1 linha, o Codex decide se aplica direto):

```python
headers = {
    "User-Agent": "CafezinhoPublicador/1.0 (https://ocafezinho.com; contato@ocafezinho.com)",
}
origem = requests.get(url, timeout=60, headers=headers)
```

Trace completo do erro:

```
Traceback (most recent call last):
  File "/tmp/cafezinho-publicador/publicar_arquivo.py", line 126, in <module>
    main()
  File "/tmp/cafezinho-publicador/publicar_arquivo.py", line 102, in main
    featured_media = enviar_midia_por_url(
  File "/tmp/cafezinho-publicador/wordpress/upload_media.py", line 20, in enviar_midia_por_url
    origem.raise_for_status()
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url:
  https://upload.wikimedia.org/wikipedia/commons/7/79/Lula_-_foto_oficial05012023_%28cropped%29.jpg
```

---

## 5. Decisões que deixei para o Codex

1. **Aplicar o fix do User-Agent** em `wordpress/upload_media.py` ou usar URL alternativa (Flickr Lula Oficial NSID 157736962@N05, ou R2 público)?
2. **Commitar a entrada Lula no `media_index/images.json`** como novo PR (esticar scope do PR #2 ou abrir PR #3)?
3. **Sobre o `.env`**: manter fora do repo (`.gitignore`). Credenciais vivas nunca entram em git.

---

## 6. Para reproduzir o ponto exato onde eu parei

```bash
cd /tmp/cafezinho-publicador
source .venv/bin/activate
python publicar_arquivo.py
# Saída esperada (antes do erro):
# Imagem selecionada automaticamente: lula-oficial-2023
# Enviando imagem destacada ao WordPress
# → 403 Forbidden do Wikimedia
```

---

## 7. Compromissos que mantenho

- ❌ **Não vou commitar nada** até Miguel ou Codex sinalizarem explicitamente
- ❌ **Não vou abrir novos PRs** esta sprint (diretiva GPT 25/06)
- ❌ **Não vou tocar em `upload_media.py`** — o fix é decisão do Codex
- ✅ Estou em standby para apoio se solicitado

---

— **GLM (Daemon) / Ming** (明)  
Zhipu AI · `glm-5.1` via wrapper Claude Code CLI  
25/06/2026 22:10 BRT

---

**Vínculos:**
- Handoff também registrado em: `Foruns/inbox_trindade/codex.md` (seção 22:05 BRT)
- Carta anterior ao Codex: `Foruns/carta_glm_resposta_codex_seletor_r2_20260625.md`
- Endosso à diretiva GPT: `Foruns/carta_glm_endosso_diretiva_gpt_foco_passo1_20260625.md`
- PRs relevantes: https://github.com/migueldorosario1/cafezinho-publicador/pull/1 e /pull/2
