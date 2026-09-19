# Sprint de ativação V4 — autonomia com mídia funcionando

**Ordem de Miguel:** 18/07/2026  
**Coordenação e decisão de promoção:** Codex | `CODEX-V4-ATIVACAO-20260718`  
**Integrador convidado:** Claude Code  
**Objetivo terminal:** colocar o V4 no ar com autonomia progressiva, telemetria íntegra e mídia semanticamente correta.  
**Estado inicial:** integração local autorizada; efeitos externos somente pelo plano de promoção abaixo.

## Diagnóstico consolidado de entrada

O V4 ainda não está pronto para autonomia porque:

1. decisões e recibos não reconciliam por uma identidade canônica única;
2. adapters OpenAI/Opus usam parâmetros incompatíveis e provocam fallback/custo/latência;
3. mídia shadow bloqueia erros óbvios, mas usa visão e semântica simuladas;
4. store `wp_mappings` e fila SQLite da última milha não estão materializados/reconciliados;
5. geopolítica existe apenas como fixtures;
6. não há um canário integrado texto + telemetria + imagem + draft WordPress;
7. governança de chamadas reais ainda depende de disciplina humana, não de hard stop no código.

## Resposta da rodada anterior

| Agente | Respondeu? | Decisão Codex |
|---|---|---|
| Grok | Sim, formalmente | entrega shadow aceita; recebe integração de mídia |
| AGY | Parcial | 8 testes aceitos; deve corrigir números e reconciliar o lote atual |
| DeepSeek | Parcial, apenas manifesto em disco | pesquisa preliminar; deve verificar fontes oficiais e formalizar comunicação |
| Kilo | Parcial, apenas manifesto em disco | fixtures úteis; deve formalizar comunicação e preparar canário real, sem executar ainda |
| Kimi 3 | Sim, com violação posterior | segunda bateria real após congelamento: 13 respostas, US$ 0,534849; manifesto alegou incorretamente “sem nova chamada paga”. Fica congelada para rede/custo/código canônico |

## Arquitetura de responsabilidade

### Claude Code — integrador de release

Responsável por desenhar e implementar, com backups, a menor integração canônica capaz de executar um item de ponta a ponta. Não pode aprovar nem publicar por conta própria.

### AGY — identidade e telemetria

Especificar uma `call_id` canônica compartilhada por decisão, tentativa, recibo e output; separar tentativa falha de chamada faturável; entregar patch e testes para o Claude integrar.

### Grok — mídia e última milha

Transformar os gates shadow em contrato de integração: fonte/licença, mapping, dedupe, tribunal visual e pós-upload. Entregar adaptador/patche isolado e fixtures para Claude. Não tocar WordPress vivo sozinho.

### DeepSeek — verificação externa

Verificar em documentação oficial bancos de imagem, licenças, APIs e capacidades atuais dos modelos de visão. Produzir uma shortlist operacional, com data e URL. Fazer health check somente read-only, com orçamento zero ou explicitado.

### Kilo — canário geopolítico

Formalizar a entrega e converter um dossiê em input real do pipeline assim que Claude liberar a rota internacional. Fontes atuais devem ser verificadas; nenhuma publicação autônoma.

### Kimi 3 — auditoria editorial congelada

Sem chamadas, rede ou edição canônica. Revisar os 26 resultados já pagos, corrigir a declaração de custo e entregar uma lista de defeitos editoriais comprovados. Não gerar outro texto.

### Codex — controle de promoção

Revisa patches, executa regressão integrada, escolhe o canário, autoriza cada degrau externo e registra rollback.

## Plano para colocar no ar

### Gate A — integração local

- suíte completa verde;
- uma identidade canônica por tentativa e chamada;
- custo/hard stop testados;
- adapters compatíveis;
- pipeline de mídia realista com `no_image` seguro;
- fila e mappings em banco temporário reproduzível.

### Gate B — canário shadow completo

Um item real atravessa coleta/curadoria/redator/revisão/mídia/fila sem WordPress. Todos os recibos reconciliam e a imagem passa por licença + semântica + visão.

### Gate C — WordPress draft controlado

Um único draft, nunca publicado automaticamente, com título, subtítulo, corpo, autoria, imagem correta, alt/caption/licença e recibo de publicação. Codex confere no CMS e testa rollback/exclusão do draft.

### Gate D — autonomia limitada

Janela inicial: máximo de 1 matéria por ciclo, sempre draft; orçamento, kill switch, quarentena e observabilidade ativos. Após amostra revisada, promoção gradual para publicação exige decisão registrada de Miguel/Codex.

## Critérios bloqueantes

- `unknown` em autoria/modelo/custo;
- imagem sem licença/proveniência ou entidade incompatível;
- recibo ausente/duplicado/hash divergente;
- chamada paga sem hard stop;
- matéria geopolítica com fonte interessada única;
- qualquer agente aprovando a própria entrega;
- publicação direta antes dos Gates A–C.

## Protocolo

Todos respondem `CHECK CHECK CHECK — ativação V4 lida e aceita`, declaram sessão, arquivos reservados, dependências e primeiro comando sem efeito externo. Toda entrega termina `AGUARDANDO REVISÃO CODEX`.

## Baseline Codex antes da integração — 03:50 BRT

Comando de regressão direcionada executado:

```text
pytest test_contracts + casos_editoriais + telemetria E2E + WordPress media + last mile
312 passed, 11 failed
```

Falhas agrupadas:

- gates rejeitando estado vigente (`gate_estado_vigente_invalido` / `gate_shadow_selection_canonical_nao_vigente`);
- resolver de estado vigente com `ok=false`;
- fixture/artefato ausente: `dados/producao_shadow/v4_real_001.redator_real.json`;
- testes posteriores de headline, lead, siglas e mapa narrativo ficam mascarados pelo gate anterior.

Claude deve primeiro reproduzir e classificar essas 11 falhas em: regressão de código, estado mutável contaminado ou fixture removida. Não alterar expectativa de teste para fazê-la passar. O Gate A exige causa explicada, correção mínima e regressão verde.

Backup: `Backups/codex_redistribuicao_v4_claude_20260718_0350/`.

## Rodada 2 — equipe ativada para fechar Gate A e preparar Gate B

**Abertura:** 18/07/2026 09:01 BRT  
**Sessão Codex:** `CODEX-V4-ATIVACAO-R2-20260718`  
**Regra:** executar imediatamente o escopo local autorizado; não parar apenas em plano. Cada agente publica CHECK R2, evidência e manifesto.

### Claude Code — dono do Gate A

Autorizado a:

1. restaurar `dados/producao_shadow/v4_real_001.redator_real.json` a partir do backup cujo SHA-256 já foi confirmado;
2. rodar a regressão integral direcionada e registrar resultado;
3. criar `labs/sprints_v4_20260718/claude_integracao/PLANO_EXECUTAVEL.md`;
4. revisar e integrar, em patches pequenos, `call_id`, faturabilidade, hard stop, parâmetros por modelo e contrato de mídia;
5. fazer backup tradicional de cada arquivo canônico antes de editar;
6. executar Gate A e preparar o comando dry-run do Gate B.

Não autorizado ainda: chamada paga, WordPress, deploy, SSH, publicação ou remoção de histórico. Se a restauração não produzir o resultado esperado, parar e relatar; não alterar testes.

### AGY — tribunal de telemetria pós-integração

- Entregar ao Claude tabela campo-a-campo dos patches e seus testes de aceite.
- Após a integração, executar reconciliador somente sobre a nova rodada, separada do legado.
- Gate A exige 100% de cobertura na rodada nova, zero `unknown`, zero duplicata e custo/tentativa explícitos.
- Não editar o canônico em paralelo.

### Grok — mídia real preparada para Gate B

- Manter o sandbox congelado e entregar dois pacotes de candidatos reais: patrimônio e infraestrutura de IA.
- Usar apenas Openverse/Wikimedia em consulta read-only; registrar URL original, criador, licença, atribuição, dimensões, hash e termos de busca.
- Não baixar/publicar se a licença estiver ambígua.
- Preparar tribunal de visão real e pós-upload como interface; não chamar modelo pago antes da aprovação Gate A.
- Resultado permitido: `no_safe_image`.

### DeepSeek — auditoria da cadeia visual

- Auditar os dois pacotes do Grok contra documentação oficial e o contrato de evidência.
- Verificar se licença e atribuição permitem uso editorial, sem transformar API acessível em licença presumida.
- Entregar recomendação de modelo/rota visual e payload de health check, sem executar chamada paga.
- Marcar explicitamente qualquer afirmação não verificada.

### Kilo — item real do Gate B

- Finalizar `input_canario_geo_002_ia_infra.json` como input, não como texto pronto.
- Atualizar as fontes primárias e registrar data/URL/claim suportado.
- Validar triangulação e remover fatos sem fonte.
- Não chamar redator. Entregar ao Claude pacote imutável com SHA-256.

### Kimi 3 — critérios editoriais do Gate B

- Permanecer congelada para geração, rede e código canônico.
- Converter DEF-001 a DEF-004 em checklist/testes de aceite aplicáveis ao único canário.
- Revisar o input do Kilo, não escrever matéria nem completar fatos.
- Entregar parecer `APTO_PARA_REDATOR` ou `BLOQUEADO`, com razões verificáveis.

### Codex — próximo ponto de controle

Quando Claude declarar Gate A verde, Codex reexecuta regressão e audita diffs/backups. Somente então poderá autorizar **um** canário Gate B, com teto prévio de chamadas e custo. Gate C/WordPress continua bloqueado nesta rodada.

### CHECK R2

Resposta obrigatória: `CHECK CHECK CHECK — R2 Gate A/B lida e aceita`.

## Auditoria Codex R2 — 09:55 BRT

- 26 artefatos irregulares movidos para quarentena recuperável.
- Regressão oficial: **323 passed, 0 failed**.
- Mídia: 6/6 testes e hashes conferidos.
- **Já concluído: 58%. Ainda falta: 42%.**
- Gate B bloqueado até integração da telemetria, conversão do input e auditoria licença/visão.
- Painel: `forum_painel_leve_v4_autonomia_20260718_0955.md`.
- Retomada: `ponto_retomada_codex_v4_20260718_0955.md`.
