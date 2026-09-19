# 07 — Próximos Passos (backlog priorizado para a conversa das 22h)

## Prioridade 0 — VENDA DIRETA (decisão 22/07 noite — doc 09)

0. **Funil R$5**: landing /experimente + checkout Pix (MP Bricks) + webhook → 100 pts + e-mail de acesso. Mídia própria (banner Moka nos 7 portais) ANTES de mídia paga. Meta semana 3–4: CAC compra-R$5 ≤ R$20.

## Prioridade 1 — Plano Moka (o foco da conversa nova)

1. **Extensão do schema**: tabelas `assinantes` (user_id, plano, gateway_sub_id, status, renova_em) e `titulos_capital` (dono, qtd, preco_pago, data) + view de valor por título.
2. **Página pública `/investidores`**: modo REAL (assinantes, MRR, custos, lucro acumulado, barra breakeven 60 ass.) + modo SIMULAÇÃO (slider de assinantes, 3 cenários, payout/título).
3. **Gerador de lotes de convites** (script CLI: cria N códigos MOKA-XXXXX com lote nomeado).
4. **Tela do painel do usuário** (HTML consumindo `/painel/saldo`).
5. **Webhook real do gateway** (Mercado Pago) conectando pagamento → assinatura → métricas na página.

## Prioridade 2 — Sites (manutenção programada)

6. **Agente vigilante** (`vigilante.py`, cron 2×/dia): post sem imagem / imagem quebrada / hero duplicada / reprovada pelo juiz → auto-corrige + reporta nos 2 bots Telegram.
7. **Heroes IA restantes** (~15 posts da varredura de 22/07 que o Commons não cobriu).
8. **Padronizar nome do arquivo hero** (com/sem data — lição registrada).
9. **Redes sociais**: criar handles dos 6 sites sem rede (tabela já proposta no fórum de consolidação).

## Prioridade 3 — Cafezinho (território sagrado, com cuidado)

10. **Esteira YouTube Cafezinho em produção**: cron 6h/12h/18h/23h gerando drafts; Claude audita e publica (carta do Cloddy entregue). Verificar 1ª rodada real e ajustar.
11. **GA4 do Cafezinho** via Site Kit no WP (propriedade antiga 374552425 existe).
12. **Preview quebrado do WP** (`?p=ID&preview=true`) — investigar permalink/preview (LEMBRETE do Miguel).

## Decisões pendentes do Miguel

- [ ] Aposentar tokens mortos (TELEGRAM_TOKEN_IRMAO, _MUNDO_TRILHOS) dos envs
- [ ] Token da @zizilindabot original (BotFather → /mybots) para assumir o 3º bot
- [ ] AdSense: ativar os 5 domínios restantes no painel quando quiser monetizar
- [ ] Conceito novo do Mapa Rio (site pausado e protegido)
- [ ] Parecer jurídico antes de vender o 1º título do capital (CVM)
