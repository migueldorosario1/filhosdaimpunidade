# V4 — subtítulos em negrito no WordPress

Decisão de Miguel em 12/08/2026: subtítulos e intertítulos do corpo devem ser escritos em linha própria com HTML `<strong>Subtítulo</strong>`.

Não usar `###` nem Markdown para essa função. O texto corrido continua normalmente sem negrito; o destaque é próprio dos subtítulos.

Responsabilidades:

- Redator V4: cria o subtítulo e entrega `<strong>Subtítulo</strong>`.
- Runtime do Redator: preserva e converte o bloco para `<p><strong>Subtítulo</strong></p>` no HTML do WordPress.
- Worker: reforça a instrução no briefing operacional.
- Núcleo editorial: mantém a regra comum às verticais.

Arquivos atualizados no NYC e no espelho local em 12/08/2026:

- `/root/v4_vertical_draft_worker.py`
- `/root/v4_labs/codigo/v4_vertical_redactor_runtime.py`
- `/root/v4_labs/contratos/v4_nucleo_editorial_redacao_v1.md`
- `/root/v4_labs/contratos/v4_nucleo_editorial_comum_v2.md`

Teste confirmado no NYC: `<strong>Retomada da escalada</strong>` resulta em `<p><strong>Retomada da escalada</strong></p>`.

Backup: `/root/.bak_pre_subtitulos_strong_20260812/`.
