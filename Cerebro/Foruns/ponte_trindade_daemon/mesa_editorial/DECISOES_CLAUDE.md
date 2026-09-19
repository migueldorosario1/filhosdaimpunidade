# Decisões de triagem — Claude

Arquivo append-only. Uma decisão por item recebido.

## Modelo

```text
## [DECISAO-AAAAMMDD-HHMM-ID-ORIGEM]
decisor: Claude
classificacao: PERTINENTE | INFORMATIVO | DUPLICADO | FORA_DE_ESCOPO | PRECISA_MIGUEL
destino: CLAUDE | ZCODE | GROK | MIGUEL | ARQUIVO
acao: o que foi feito ou qual ticket foi aberto
evidencia: caminho, ID de post, log ou NENHUMA
estado: ENCAMINHADO | CONCLUIDO | AGUARDANDO
```

Decisão não amplia autorização. Publicação, alteração de infraestrutura e
operações destrutivas seguem os contratos e reservas vigentes.

## [MESA-20260815-0008-CLAUDE-ACK-ORDEM-NOVA-PONTE]
status: FECHADA
ts_brt: 2026-08-15T00:08
ref: [MESA-20260814-2354-MIGUEL-NOVA-PONTE]
decisao: ACK. Assumo coordenação da mesa editorial. A partir deste ciclo, leio ENTRADA.md + COMENTARIOS_ROGERIO.md antes de cada Slot A/B, registro triagem aqui, atualizo CHECKPOINT.md quando houver mudança de estado. Escopo: encaminhar itens de ENTRADA ao ofício correto (Claude/ZCode/Grok), documentar decisão editorial curta.
