# Fórum — Renomear Versão no Leitor (Filhos da Impunidade)

**Data:** 2026-08-07 (~16:15 → 17:25 BRT) · **Agente:** ZCode (Qwen Token Plan) · **Estado:** ✅ AO VIVO (commit `a224dec`, verificado em produção)

## 1. O pedido (Miguel, áudio no leitor)

"Tem que ter o comando para mudar o nome. Eu botei o nome errado aqui. Está Gemini 3.6. Tem que poder mudar o nome do arquivo... Só boto esse detalhezinho pra poder corrigir o título." — ele subiu uma versão nova (⬆️ Subir Nova Versão) com rótulo errado e não tinha como corrigir sem re-upar.

## 2. A decisão

O nome de exibição de uma revisão mora em `revs[R#].versionTag` (localStorage `miguel_book_revisions_<vol>_<cap>`). Renomear troca **só o rótulo**: texto, chave R# e ponteiro canônico ficam intactos.

- **✏️ em toda revisão** no menu 📜 Histórico de Versões — **inclusive na canônica** (renomear não conflita com o 👑; só APAGAR continua bloqueado nela). Oficial/experimentais não têm nome editável (rótulos vêm do código).
- **Input inline na própria linha** (mesmo padrão do gerenciador de capítulos: `start/confirm/cancel` + re-render): Enter salva, Esc cancela, ✓/✕ para toque. Teto **40 caracteres** (mesmo do upload).
- **Menu permanece ABERTO** durante e depois da edição — Miguel vê o resultado na hora.
- Rótulo existente entra no input via `.value` (nunca interpolado como HTML).

## 3. Salvaguardas

- Nome vazio → toast "renomeação cancelada", nada gravado. Nome igual ao atual → no-op sem regravação.
- Falha de quota no localStorage (`safeLocalSet`) → nada gravado + mensagem de ajuda.
- `loadChapter` fecha edição pendente (anti-vazamento: chaves R# podem colidir entre capítulos).
- Modo faxina cancela renomeação (não coexistem).

## 4. Provas

- Testes: `scratch/teste_renomear_versao.js` **12/12** (inclui o caso real "Gemini 3.6", canônica renomeável, quota, truncamento) + regressões 14/14 (upload), 9/9 (drive cliente), 24/24 (roteiro/livro-edit), 11/11 (drive server), central-fontes ok.
- Ao vivo: strings da feature presentes no HTML servido pela Vercel (`version-rename-input` ×4, `startRenameVersion(v.key)`, `Renomear a versão`).

## 5. Como o Miguel usa

Menu **📜 Histórico de Versões** (na barra roxa de versão) → linha da versão → **✏️** → editar o nome → **Enter** (ou ✓). É isso: "Gemini 3.6" vira o nome que ele quiser.

## Pendências

- Nenhuma.

**Memória técnica:** `Memorias/memoria_renomear_versao_leitor_20260807.md`
