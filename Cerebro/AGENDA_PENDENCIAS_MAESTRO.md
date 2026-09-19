# 📋 AGENDA DE PENDÊNCIAS DO MAESTRO — Cafezinho (criada 31/08/2026 22:2x BRT, ordem do Miguel)

> Plantão noturno do ZCode/GLM-5.3 (Dell). Automação `automation-3ad40af1` roda de hora em hora
> (ronda leve) com sprint de pendências nas horas pares e agenda do Miguel no Telegram entre 07:00-09:00.
> Regras: mudança em produção = backup → compile → prova → git/ROLLBACK_INDEX → registro aqui/fórum → rollback escrito.
> Sem capa = nunca publica. IA gerando imagem = proibida (Emenda NO-IA). Telegram do Miguel = só-positivo.

## Estado da fila (atualizar a cada ronda)

| # | Pendência | Estado | Detalhe / prova |
|---|---|---|---|
| 1 | 268440 vazando checklist interno (BUG-DS-103) | ✅ FEITO | Cortado pela AGY-L às 22:11:55 (CL-039); grep bastidor limpo; texto termina na seção FONTE |
| 2 | Link `controle.` no Telegram (reclamação 2ª vez) | ✅ FEITO (monitorar) | Patch no dsn_publicador.py (Tencent, backup .bak_pre_link_publico_20260831) sanitiza p/ www; regra ZM-20260831-024 na ponte + canal_trindade; conferir links novos |
| 3 | Fila de capas (gargalo da produção) | 🔄 19 posts hoje; 268366/268393 publicados; 268451 sai no ciclo 23:00 |  Seeds ZM: 268451 Eduardo Paes (CC BY 3.0, no fluxo ≤12h) + 268394 Natura (CC BY 2.0, receita pronta fora da janela). Seeds prontos p/ 4 posts (268451 Paes · 268394 Natura · 268457 Kast · 268458 Lula); robão aplica 1/ciclo; 268456 E-goi sem foto livre —Ideias-003; caça segue 1-2/h |
| 4 | Banco Ouro V3 como camada 1 | 🔄 DEGRAU 1/3 FEITO 00:1x | Adapter sombra no v4_labs (474 fotos aprovadas; provas Lula/Flávio/Trump 3 hits); Degrau 2 ✅ FEITO 02:0x (hook sombra + flag no chaves.sh + ROLLBACK_INDEX; medição a partir ciclo 02:20; hit-rate na ronda 03:00+); Degrau 3 = RELATÓRIO PRONTO p/ 'vai' do Miguel (Foruns/relatorio_banco_ouro_dia_20260901.md: rank contextual + url_origem + olho juiz) | Em sombra+flag; acervo 1.214 fotos/R2; alavanca estrutural das capas |
| 5 | Velharia: 117 rascunhos 4+ dias | ⏳ PENDENTE | Revalidar fato central antes de publicar (doutrina FRESCOR) |
| 6 | Robô DS YouTube "parado" | ✅ RESOLVIDO + fichado | Causa raiz = repo Tencent divergente (curado 22:55); robô saudável, fila batismo ENTREGUE_GATE; bug menor cosmético (ciclo ocioso não loga) na encomenda Ideias-003 | git unmerged na Tencent (visto pela DS-N 22:00); crons 7,22,37,52; logs ~/ds_youtube/ |
| 7 | wp-cron lento: futures vencidos | 🔄 2 CURADOS (268366/268393 publicados 22:5x via wp_publish_post, permalinks 200) | Monitorar novos; estrutural com a casa | 268366 (22:55) e 268393 (23:16) monitorados; cura canônica wp_publish_post quando vencerem (se capa+img_check ok) |
| 8 | BUG-DS-098 ✅ · 100 ✅ · 102 ✅ 22:0x | 102: max_tokens 8000 no dsn_router (prova ao vivo) | 098 crontab 1min (dono ZM) · 100 furo 05:30 · 102 dono ZM/DS-Dell |
| 9 | Moka: padronização de botões (Claude‖AGY, ZM funde) | 🔄 EM CURSO | Menu resolvido (49e5ddf full-bleed + 7466fe4 menu clean); botões em voo |
| 10 | Moka: rito R2 → /ajuda ilustrada | ⏳ PENDENTE | Rito R2 validado E2E 31/08 |
| 11 | Manual criativo redes (Ideias 001/001A) | ⏳ PRECISA MIGUEL | ✓ do manual; X Premium? (define Tweet 1); ✓ estratégia Instagram |
| 12 | Palavra-chave do pacote DSC-013 | ✅ FECHADO 03/09 15:03 | Miguel destrancou no Dell via script (senha oculta, nunca em chat); credenciais entregues us65:/root/dsc_credenciais (600) |
| 13 | Recargas de crédito | ⏳ PRECISA MIGUEL | DeepSeek US$ 19,77 🟡 · xAI Grok US$ 7,99 🟡 |
| 14 | Encomenda Ideias-003 (autocura 3 problemas) | 🔄 P2 ✅ executado c/ prova (23:2x) · P1 verificador na ronda 1/1h · P3 Banco Ouro sombra agendada 02:00 | Ideias entregou 23:16 c/ causa raiz real (evento publish_future_post ausente) |
| 15b | Auditoria irmãos DS-N (DSC-014) | ⏳ PENDENTE | Relatório diário do DS-N Imagem (prova de vida) + write-back de fila pelo publicador |
| 15 | Agenda Google do Miguel | 🔁 ALTERNATIVA ATIVA | ZM não tem acesso OAuth; agenda vai no Telegram 08:00 + aqui. Plugar Google Calendar exige credencial no cofre (futuro) |
| 16 | Revisão HMAC LITE → COMPLETA (emenda E4) | ⏳ AGENDADA 07/11/2026 | Palavra do Miguel 10/09 (P5); lembretes automáticos 01/11 (D-6) e 07/11 (DIA) 09:00 BRT via Tencent ds_nuvem_chefe/lembrete_hmac_completo.py + esta agenda; fórum reforma §16 · ZM-20260910-012 |

## Regras do plantão
- Telegram do Miguel: SÓ-POSITIVO (ordem 31/08); fracasso vira aprendizado nos fóruns.
- Publicar: só via publicador (olho robótico duplo). Caça do maestro entra por seed (capas_seed.json).
- Toda caça/cura registrada na ponte (commit imediato) e no fórum do maestro.
