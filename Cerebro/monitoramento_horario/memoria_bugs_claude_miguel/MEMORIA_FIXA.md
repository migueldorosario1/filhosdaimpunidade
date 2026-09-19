# Memória fixa de bugs — Claude Miguel

## Ritual antes de revisar ou agendar

1. Ler este arquivo.
2. Ler o diário de hoje nesta pasta; se não existir, criá-lo antes do primeiro
   post.
3. Ler a cauda do JSONL de bugs de hoje.
4. Ler itens `ABERTO` em `ponte_trindade_daemon/fila_para_claude.md`.
5. Só então abrir a fila do WordPress.

Registrar no ciclo: `memoria_bugs_claude_lida=true` e os caminhos lidos.

## Gates que não podem ser pulados

- Ler título e corpo completos.
- Inspecionar HTML/Markdown, atributos `href`, comentários e metadados; texto
  renderizado sozinho não basta.
- Buscar rastros de ferramenta/provedor/agente em conteúdo e URLs.
- Verificar links sem apagar parâmetros funcionais.
- Confirmar atualidade: “o que aconteceu agora?”.
- Registrar revisor externo por post: modelo, call ID, payload coberto,
  veredito, custo e aplicação/rejeição da recomendação.
- Sem parecer auditável, não escrever “revisão externa concluída”.
- Se um incidente grave for encontrado, conter, abrir fórum e aplicar o
  protocolo `Foruns/diretrizes/protocolo_incidente_grave_bastidores_v1.md`.

## Incidente fundador — 265876

O GPT-5.5 do V4 Nacional produziu seis links com `utm_source=openai`. Claude
Miguel agendou o post no ciclo 00:02 sem corrigir o defeito. Grok Miguel o
marcou como clean 20 vezes. O erro ficou público por até 38m41s e foi detectado
por Grok Laura.

Aprendizado permanente: revisão editorial não é só leitura da prosa. Um link
pode parecer normal na tela e ainda revelar o processo no destino. Custo de
LLM registrado não prova que uma revisão cobriu o post; é preciso guardar o
parecer por post.

