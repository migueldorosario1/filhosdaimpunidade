# 🧠 Memória — Vídeo GrokBot (Paul J Lipsky) + mapeamento para o ecossistema — log técnico

> **Data:** 2026-08-29 00:45 BRT · **Autor:** ZCode (Qwen 3.8), sessão ZCodeProject
> **Fórum:** [`Foruns/forum_equipe_bots_estilo_grokbot_plano_20260829.md`](../Foruns/forum_equipe_bots_estilo_grokbot_plano_20260829.md)

## Como a transcrição foi obtida (receita Dell)

- Vídeo: https://www.youtube.com/watch?v=UyMJBUCyDIs — "Grok Bot Is Now Only $20 - Here Are 9 Wild Use Cases", canal Paul J Lipsky, 15:58, publicado 27/08/2026.
- Dell tem `yt-dlp 2026.07.04` (`~/.local/bin/yt-dlp`) + ffmpeg + node v22.22.2; **sem deno** (yt-dlp pediu `--js-runtimes node`).
- Passo 1 (metadados): `yt-dlp --js-runtimes node --skip-download --print ...` → título/canal/duração OK (IP do Dell sem bot-check, confirmando a lição de 28/08).
- Passo 2 FALHOU: `--write-auto-subs` direto → `HTTP Error 429: Too Many Requests` no timedtext.
- **Contorno que funcionou:** `yt-dlp --js-runtimes node -J <url>` (dump JSON do player) → extrair as URLs `api/timedtext` de `automatic_captions` (pt, en, en-orig) → `curl` direto na URL com UA de navegador. en-orig = 152 KB completo; pt = 1,1 KB (quebrada, descartada).
- Conversão VTT→texto: remover linhas de timestamp/cabeçalho, deduplicar, juntar. Resultado: 16.062 chars / 417 segmentos.
- Transcrição integral guardada: `Foruns/anexo_transcricao_grokbot_video_20260827.txt`.

## Mecânica do GrokBot extraída do vídeo

- US$ 20/mês (antes US$ 200); incluso em planos Cursor/SuperGrok/Teams elegíveis. Download em x.ai/bot (macOS/Windows/iOS — sem Linux oficial).
- Bot criado POR CONVERSA (sem chave/modelo/instrução manual); nome + avatar ("crie uma imagem sua") + título/cargo no painel.
- Regra de uso: cada bot = funcionário especializado; mesmo bot para o mesmo assunto sempre.
- Recurso-estrela: bots no mesmo canal **conversam entre si** e passam a tarefa adiante sem aprovação humana por etapa.
- Cada bot tem **computador na nuvem** logado nas ferramentas do dono (Chrome/file manager/terminal) → rotinas rodam com PC desligado; login humano só na primeira vez (ex.: DoorDash).
- Elenco do vídeo: Chief (delegadora), Scribe (e-mail+calendário), Seeker (pesquisa/monitora X), Mapmaker (brainstorm/filtro), Hemingway (roteiro), Prism (design), Concierge (vida pessoal, conversa com Coach Cal), Bob the Builder (apps + rotina mensal do site), Atlas/Hound/Nightingale (viagens/compras/saúde).

## Mapeamento e decisão

- Ecossistema atual cobre ~80%: loops = especialistas com rotina; NYC/Tencent = computador na nuvem; Pontes Trindade/Laura = canal entre bots; Cérebro = memória; Ponte Cafezinho = falar com o Miguel; monitor = anti-colisão.
- Gaps (os 20%): Chief/delegador único, personas fixas nomeadas, handoff automático entre especialistas.
- Plano em 3 fases no fórum; parecer = construir o nosso em vez de assinar o GrokBot (US$ 20/mês + port Linux não oficial + teria que reensinar o ecossistema).
- **Aguarda decisão do Miguel** ("vai" da Fase 1 + nome do líder, ou alternativa paga).
