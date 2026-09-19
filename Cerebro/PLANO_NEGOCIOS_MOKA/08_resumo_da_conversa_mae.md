# 08 — Resumo da Conversa-Mãe (20–22/07/2026, ZCode/Kimi + Miguel)

Linha do tempo do que foi feito nesta conversa, para qualquer IA (ou humano) retomar sem perder contexto.

## Fase 0–1 · Refatoração V4 (20/07)
- Levantamento: 8 sites temáticos, configs desatualizados, riocarta duplicado, mapario órfão sem repo
- **Backup total verificado** (git bundles + checksums) em `Backups/refatoracao_v4_tematicos_20260720_171637/`
- 8 repos novos `*-v4` criados, 4.257 posts migrados, Vercel reconectada via API, 8 domínios validados
- Incidente git 2.25 (`init -b`) → repo-pai contaminado → rollback limpo documentado
- GSN: projeto `gsnews` renomeado p/ `global-south-news`, staging deletado, zero downtime

## Fase 2 · Motor V4 (20–21/07)
- 3 agentes + YouTube (coletor → produtor → publicador), 2 bancos JSONL, dedup fuzzy, auditoria LLM
- Roteador LLM: DeepSeek→Kimi→GLM→Qwen→GPT(0,2); **DeepSeek fixado a 0,2** depois
- 40 wrappers nomeados por site, cron 3h/13h + YouTube 2:30/12:30
- 12 posts na 1ª rodada; feeds mortos substituídos; Brave key corrigida (havia 3, 2 mortas)

## Um por um (21/07)
- **AIatolah**: bilíngue PT/EN, ranking com Kimi K3 (2 lugares: JSON + sidebar), canal Diamandis + Kantrowitz, regra 1 vídeo/dia, limpeza de 14 vídeos
- **Rio Carta**: missão FLUMINENSE (não só capital), critério valor jornalístico, hero relevante, bug URL `/blog/` + 26 re-pings, imagens (gitignore R2) corrigidas
- **GSN**: contrato anti-imperialista + **Meloni Rule**, 6 canais YouTube legados reativados, transcrição integrada, colunas do Miguel e PNB traduzidas, seção Featured Voices

## Qualidade de imagem (21–22/07) — a saga
- Wikimedia namespace fix, heroes retroativas, **juiz visual Gemini** (o agente VÊ e JULGA), **dedup de hero**, **blocklist** (moeda PSP, pôster 1930, livro 1844), **blur-fill 1200×675** (517 imagens padronizadas), regra "NUNCA sem imagem" (fallback IA/Ideogram)

## Layout (22/07)
- Container 960px→`min(1280px)` + grids fluidos nos 5 sites, título gigante removido, featured v2
- Favicons vibrantes só-ícone (7 sites), logos só gráficas (trilhos, discover)
- Quem Somos criado/linkado (trilhos), nome do Miguel fora da capa (fica no quem-somos)
- Destaques priorizam **últimas pesquisas** (ceara + riocarta)

## Moka + negócios (22/07)
- Estudo de pontos → schema v1 validado → **API FastAPI 4/4 validada**
- **Plano de negócios completo**: assinatura R$24,90, breakeven ~60 ass., capital 20.000 títulos, página investidor, cripto com alerta CVM
- **E-mail enviado** ao Miguel via rota Baleia Azul (SSH Tencent)

## Canais (22/07)
- E-mail: `ssh -p 38422 ubuntu@43.156.151.165 "mail -s ..."` ✅ testado
- Telegram: 2 bots assumidos + ponte `nucleo_telegram.py`; chat_id 1894890759

## Incidentes registrados (transparência)
1. `git init -b` no git 2.25 → rollback do repo-pai (documentado)
2. **sites-v4 apagado pela reforma de arquivos** (movido p/ Dados_Frios) → re-clone total, zero perda, **errata no índice da reforma**: sites-v4 é dado QUENTE e fica no workspace
3. Fork paralelo publicando em duplicata → coordenação registrada nos fóruns
4. Build quebrado por `hero_credit` duplicado (colisão de retrofits) → corrigido
