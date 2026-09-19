# Memória técnica — NOMES SEM ERRO nos agentes YouTube (websearch + memória)

**Data:** 16/08/2026 · **Autor:** ZCode/Qwen 3.8 · **Fórum pareado:** `Foruns/forum_nomes_agentes_youtube_websearch_memoria_20260816.md`

## Log técnico completo

### 1. Módulo novo `verifica_nomes.py`
Caminho: `Projeto Cafezinho Agentes/agentes_cafezinho/verifica_nomes.py` (roda
standalone; injeta os paths de `agentes_tematicos` no sys.path). Funções-chave:
- `carregar_memoria()/_salvar_memoria()` — JSON atômico (`.tmp`+`os.replace`),
  `.bak` rolante antes de cada escrita.
- `buscar_memoria(nome)` — casa nome OU alias, case-insensitive.
- `_resultados_busca()` — `nucleo_tematico.busca.search_brave` (Brave → DDG
  fallback), query `"<nome>" <contexto>`, 5 resultados, sleep 1s (rate-limit free).
- `_veredito_llm()` — `nucleo_llm.gerar_json(tarefa="coleta")` (tier barato)
  decide confirmado/duvidoso/inexistente + nome_canonico + cargo.
- `extrair_nomes(analise, canal)` — coleta apresentador/apresentadores/convidados/
  personagens/vilao/citacoes.quem; corta credenciais (`— CONVIDADO`, `(senador)`,
  `, deputado`); DIVIDE nomes compostos (`"A, B e C"` → 3); descarta genéricos.
- `verificar(nomes, contexto, max_buscas=8)` — memória → websearch → veredito;
  auto-alimenta (confirmado E duvidoso entram; busca vazia entra como duvidoso
  para não repetir custo); teto de buscas → status `nao_verificado`.
- `formatar_para_prompt()` — linhas `- "original" → status=..., nome_canonico="..."`.
- `--selftest` — Lula/Nunes Max/Aaron Maté.

Esquema da memória (`agent_data/personagens_youtube.json`):
`{nome, aliases[], cargo, contexto, status(confirmado|duvidoso), fonte(seed|curadoria|canais|websearch|websearch_vazio), verificado_em, motivo}`.

### 2. Integração no `youtube_cafezinho.py`
Backup: `youtube_cafezinho.py.bak_pre_verifica_nomes_20260816`.
- `processar()`: após `analisar()`, `extrair_nomes`+`verificar` em try/except
  fail-soft → `video["_dossie_nomes"]`; log com contagem (memória × websearch).
- `_bloco_factcheck(video)` NOVO: com dossiê → regras duras (confirmado usa grafia
  exata; duvidoso/nao_verificado/websearch_vazio omite; nome fora do dossiê =
  duvidoso; proibido chutar grafia e marcador técnico). Sem dossiê → parágrafo
  tradicional do bug #31 intacto.
- `redigir()`: prompt FACT-CHECK substituído por `{_bloco_factcheck(video)}`.
- `publicar_draft()`/`atualizar_draft()`: payload `meta.cafezinho_nomes_check`
  (JSON ts+video_id+nomes) + auditoria local `BANCO_DIR/nomes_<video_id>.json`.
- `_deepseek_key()` + `_chat_json_cascata()` NOVOS: DeepSeek→Kimi paygo para JSON
  chat; `_jornal_confirmar_llm` agora usa a cascata (era `_kimi_chat_json` só).

### 3. WP canônico
`/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-nomes-check.php` (www-data,
php -l OK): `register_post_meta('post', 'cafezinho_nomes_check', {string, single,
show_in_rest})` — sem isso o REST ignora meta não registrada.

### 4. Seed da memória (81 personagens)
Curadoria `personagens_prioritarios` (20) + `personagens_viloes_uteis` (14) +
pessoal da casa (Miguel do Rosário c/ diretriz permanente de citação, Henrique
Rodrigues, Glauco Faria) + autoridades de erro frequente de transcrição
(Alexandre de Moraes c/ aliases "Alexandre Moraes/Morais/ministro Moraes"; Kássio
Nunes Marques c/ aliases "Nunes Marques/Nunes Max/Nunes Marcos") + 40 titulares de
canais do cache `youtube_canais_nomes.json`. **Cargo preenchido só onde há certeza
absoluta** — cargo errado na memória seria tão grave quanto nome errado; nos
demais o LLM usa conhecimento próprio e a memória garante só a grafia.

### 5. Provas executadas
1. `--selftest` OK (3 acertos de memória, incl. alias "Nunes Max" → Kássio Nunes Marques).
2. "Nima Alkhorshid" (fora da memória) → Brave → LLM → confirmado
   "Nima Rostami Alkhorshid" (cargo: analista, entrevistado do Dialogue Works);
   memória 79→80.
3. Artefato real `teste_pPvnFsuAR00.json` (TV Fórum/Felipe Pena): 9 nomes —
   memória 6, websearch 2 confirmados (Felipe Pena jornalista/psicólogo; Eduardo
   Cunha ex-presidente da Câmara), 1 duvidoso (Richarlison, busca vazia).
   Após fix do split de compostos: 8 memória + 1 busca (só o não resolvido).

### 6. Incidente Kimi paygo (corrigido na mesma sessão)
Log 22:30: `_jornal_confirmar_llm` → HTTP 429 "account ... is suspended". Conta
do `Projeto Cafezinho Agentes/Outros/chaves/kimi_paygo.env`. Correção: cascata
DeepSeek→Kimi. Rodada 23:00 nem chegou na cascata: coleta RSS morreu em
`bot_check` do iProyal (todos os provedores) — intermitência do provedor;
rede de segurança 23:30 testa de novo. Ver
`monitoramento_horario/bugs_encontrados/yt_patrulha_agente_youtube_20260816_2258.md`.

### 7. Gotchas registrados
- Meta WP via REST só entra se a chave for REGISTRADA (mu-plugin) — senão o
  payload "meta" é silenciosamente ignorado.
- Nomes compostos no campo `vilao` ("A, B e C") quebravam a extração — split
  por vírgula/« e » aplicado (só quando as partes parecem nomes).
- Busca vazia também alimenta a memória (status duvidoso) — evita pagar a mesma
  busca sem resultado em todo rascunho.
- `nucleo_tematico.busca.search_brave` já detecta query PT-BR e troca country/lang.

### 8. Pendências / próximos passos
- Levar a MESMA camada ao GSN V2 no NYC (codebase separada, cron 11h/17h UTC).
- Acompanhar a conta Kimi paygo (se reativar, a cascata usa; se morrer de vez,
  remover da cascata e do cofre — Regra 4).
- Fix do fallback yt-dlp do `util_youtube_transcript` (chamar binário certo no
  PATH do cron) — bug registrado.
