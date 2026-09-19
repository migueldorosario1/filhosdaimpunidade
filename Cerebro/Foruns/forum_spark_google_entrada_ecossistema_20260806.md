# 🌟 FÓRUM — Spark (Google/Gemini) entra no ecossistema + Ponte Spark↔Kimi (2026-08-06)

> Decisões resumidas. Log técnico completo: `Memorias/memoria_spark_google_entrada_ecossistema_20260806.md`.
> Pedido do Miguel (sessão ZCode/Kimi K3, 06/08/2026): configurar o **Spark** ("Spark com K", nova ferramenta do Google/Gemini) com acesso ao Google Drive, dar a ele onboarding do Cérebro, carta de missão e uma ponte de trabalho com Kimi.

## Decisões (Miguel, 06/08/2026)

1. **Spark entra no ecossistema** como agente externo, acesso via Google Drive, **SÓ LEITURA** no Cérebro (espelho `drive:Cérebro Imortal da Trindade/cerebro-miguel/cerebro/`). Escrita no Cérebro: nunca direta — ele produz texto e o Miguel (ou agente local) grava no canônico.
2. **4 missões da carta:** (1) índice/organização do Google Drive; (2) triagem do Gmail (marcadores, filtros, pendências); (3) Agenda + registro consultável de convidados/contatos; (4) diagnóstico WhatsApp (guardar? enviar?).
3. **"Vai" da Fase 1:** varredura READ-ONLY do Drive + Índice + proposta de arquitetura de pastas. Nenhuma movimentação sem novo "vai".
4. **Contatos — modelo misto aprovado:** Google Contatos (oficial) + Planilha Google espelho; campo de notas obrigatório com origem + contexto + data.
5. **WhatsApp:** Spark confirmou **zero acesso nativo** (nem ler nem enviar). Caminho aprovado: export `.txt` de conversas → pasta `WhatsApp_Backups_Entrada` no Drive → Spark processa (resumos, contatos, tarefas). API dedicada (Business Cloud / Evolution) fica para avaliação futura, com comparativo de custo/complexidade junto ao relatório da Fase 1.
6. **Ponte Spark↔Kimi criada:** `drive:Ponte_Spark_Kimi/` — pasta própria na raiz do Drive, **propositalmente FORA do espelho do Cérebro** (o sync local→Drive é unidirecional e sobrescreveria arquivos criados lá por fora). Arquivos: `README_PONTE.md` (contrato), `CAIXA_KIMI.md` (Kimi→Spark), `CAIXA_SPARK` (Google Doc que o Spark cria, Spark→Kimi), `HISTORICO.md` (log append-only).
7. **Segurança:** doc **"Senhas nova 6 abril 2026"** (raiz do Drive) e qualquer doc de senha/chave/token = **[RESTRITO — Cofre]**: o Spark não abre, não lê, não resume — só lista no índice como restrito. Pendência do Miguel: migrar o conteúdo para o Cofre canônico (`Outros/chaves/agentes_labs/.env.unificado`) e esvaziar o doc.

## Regras de trabalho do Spark (da carta, aceitas por ele)

- Propor antes de agir ("vai" do Miguel); nada se apaga nunca (arquivo morto datado); citar fonte; responder em PT-BR; frescor do Cérebro checado pela última entrada de `CEREBRO_NODE_ATUALIZACOES.md`.

## Estado e pendências

- ✅ Prompt de onboarding + carta de missão entregues; resposta do Spark recebida (tabela de capacidades honesta + plano em 4 fases); "vai" do Miguel redigido e enviado.
- ⏳ Prova de conexão do Spark ao Cérebro (checklist) — cobrada no "vai", ainda não entregue.
- ⏳ Espelho do Cérebro no Drive estava ~21h defasado em 06/08 (último arquivo 05/08 02:08); sync local→GitHub→Drive oferecido ao Miguel.
- ⏳ Doc de senhas → Cofre (Miguel).
- ⏳ Spark estrear a `CAIXA_SPARK` (Google Doc) na ponte.

— Kimi K3/ZCode, 2026-08-06
