---
name: Tutorial Interno do Cafezinho — ponteiro pra memória móvel de inteligência
description: Pasta viva `Outros/tutorial_interno/` contém capítulos .md com conceitos estruturais do projeto (arquitetura, pipelines, regras editoriais). Consultar por demanda quando contexto pedir.
type: reference
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 Miguel pediu uma **"memória móvel de inteligência"** — um tutorial interno vivo que a gente vai construindo com os conceitos principais do projeto, separado do histórico detalhado (snapshots horários) e da memória curta/feedbacks deste arquivo aqui.

## Estrutura

```
Projeto Cafezinho Agentes/Outros/
├── tutorial_interno/          ← conceitos que valem pra sempre
│   ├── INDEX.md               ← catálogo leve (abrir primeiro)
│   ├── 01_arquitetura_geral.md
│   └── (capítulos futuros)
│
├── memoria_horaria/           ← histórico detalhado (snapshots por hora)
│   ├── INDEX.md
│   └── memoria_AAAAMMDD_HHh.md
│
└── orientacoes_miguel_sessao_*.md  ← diretrizes pontuais durante cada sessão
```

## Como usar

- **Início de sessão:** se a conversa envolver arquitetura, publicação, imagens ou bugs recorrentes, abrir primeiro `tutorial_interno/INDEX.md` e ler o capítulo relevante. Não carregar todos — só o que importa.
- **Durante trabalho:** se aprender algo novo que vale pra sempre (nova lição, padrão, regra), **adicionar um capítulo** ou atualizar um existente. Não deixar conhecimento importante só nos snapshots.
- **Histórico diário:** *não* consultar no dia a dia. Usar quando Miguel pedir retrospectiva ou quando precisar diagnosticar causa raiz de algo antigo.

## Filosofia

Separação estrita de responsabilidades:
- **Esta pasta (`~/.claude/.../memory/`):** só o que precisa estar CARREGADO toda sessão — feedbacks de comportamento, references a paths críticos, fixes importantes resumidos.
- **Tutorial interno:** conceitos consultáveis sob demanda. Carregar só capítulo relevante.
- **Memória horária:** histórico arquivado. Carregar só se investigação exigir.

Objetivo de longo prazo: tutorial e memória horária vão pro Google Drive, permanecem acessíveis, mas não pesam na memória viva nem no contexto.

## How to apply

- Se o Miguel mencionar conceito estrutural (ex: "pipeline de imagens", "regras de título"), abrir o capítulo correspondente em `tutorial_interno/` antes de responder.
- Se não houver capítulo sobre o tema e for relevante, criar um **depois** de resolver o tema atual (não atrasar entrega).
- Atualizar `INDEX.md` sempre que adicionar/mudar capítulo.
