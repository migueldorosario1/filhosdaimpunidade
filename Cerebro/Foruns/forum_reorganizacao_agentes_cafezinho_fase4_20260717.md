# Fórum de Retomada — Reorganização `Projeto Cafezinho Agentes` (Fase 4)

**Data:** 17/07/2026 02:18 BRT

## O que foi pedido
- reduzir desordem de `Projeto Cafezinho Agentes`,
- retirar duplicado/legacy fora do núcleo ativo,
- manter um único legado consolidado,
- registrar tudo para retomada pelo Claude/Trindade sem ambiguidade.

## Execução realizada

### Fase 4.1 — legado no topo (limpeza cirúrgica)
Movi para:
`legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/agentes_cafezinho_fase4_20260717`

itens:
- `.env.unificado`
- `config/` (`politica_leveza_sistema.json`)
- `indices/`
- `exports/` (`v3_midia_testes`)
- `scratch/`
- `wordpress_mu_plugins_staging/`

### Fase 4.2 — histórico V4 em nível `root`
Movi todos os pacotes `root/v4_labs_fase*.tar.gz` para:
`legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/root/Backups/v4_labs_pacotes_antigos_20260709/`

## Resultado
- **0 arquivos apagados**
- Topo de `Projeto Cafezinho Agentes` ficou menor e sem os resíduos citados.
- `root/v4_labs/` e diretórios operacionais **não foram alterados**.

## Checks de segurança
- `rg` em `.py/.sh` confirmou ausência de uso ativo dos itens limpos acima fora de contexto histórico.
- `v4_labs_fase*.tar.gz` não existe mais no `root/` ativo.

## Para retomada imediata
- Se necessário, voltar os itens é só `mv` reverso desses caminhos para a raiz/`root/` conforme manifestado.
- Manifesto completo com origem/destino: `legacy_reformado_20260717/MANIFESTO_REORGANIZACAO_AGENTES_CAFEZINHO_FASE4_20260717.md`

---

**Observação de coordenação:** este ciclo mantém `legacy_reformado_20260717` como único espaço de legado interno deste diretório.
