# Instalação do ZCode na máquina LAURA — relatório técnico

```yaml
tipo: RELATORIO_INSTALACAO
executor: LAURA-CLAUDE (chefe do Loop Laura)
relogio: "Monday, 17/08/2026 17:09:09 -0300"
ordem: Miguel, chat direto 17/08 ~16:20 — "instalar zcode no laura"
maquina: LAURA — Samsung Galaxy Book Go, Windows 11 ARM64
perfil_leve: PRESERVADO — nenhum serviço reativado
```

## 1. Especificações reais medidas

| Item | Valor |
|---|---|
| Arquitetura | **ARM64** (nativa, shell não emulado) |
| CPU | Snapdragon 7c Gen 2 @ 2.55 GHz — 8 núcleos |
| RAM total | **3,68 GB** (nominal 4 GB) |
| RAM livre no início | **237 MB** (!) |
| Disco livre | 51,8 GB (de ~108 GB) |
| Node.js | **ausente** |

## 2. O que foi instalado

- **Produto correto identificado:** ZCode da **Z.ai** (zcode.z.ai) — app
  desktop Electron que orquestra agentes de IA na nuvem. Não roda
  modelo local.
- **Build ARM64 NATIVO existe** e foi o usado:
  `ZCode-3.7.7-win-arm64.exe` (142,1 MB), baixado da CDN oficial.
  *Ressalva importante:* o `winget install ZhipuAI.ZCode` entregaria o
  instalador **x64 (emulado)** — pior desempenho nesta máquina. Por isso
  o winget foi descartado.
- Instalação silenciosa (`/S`), exit code 0, em
  `%LOCALAPPDATA%\Programs\ZCode` — **617,9 MB** em disco.
- **Verificação de arquitetura no binário** (cabeçalho PE):
  machine `0xAA64` = **ARM64 nativo**, versão 3.7.7.4926. Sem emulação.
- **Node.js LTS (ARM64)**: instalação via winget iniciada; concluiu em
  segundo plano (disco eMMC lento) — status na seção 5.

## 3. Teste executado e consumo medido

| Momento | RAM livre | Swap em uso |
|---|---|---|
| Antes de abrir | 516 MB | — |
| App aberto (45 s) | **365 MB** | — |
| App aberto (~75 s) | **274 MB** | **4.657 MB** |
| Após fechar | 500 MB | 4.454 MB |

- App subiu e **permaneceu estável**: 7 processos vivos, sem queda.
- **Consumo do ZCode: ~700–742 MB** de RAM (soma dos 7 processos).
- **Sinal crítico:** com o app aberto, o Windows manteve **~4,6 GB em
  arquivo de paginação (swap em disco)** — a máquina compensa a falta de
  RAM escrevendo em disco, o que no eMMC é lento.

## 4. Sobre a CLI — TESTADA E APROVADA (a boa notícia)

Node LTS instalado: **v24.19.0, arch arm64 nativo** (winget, exit 0).

O motor embutido (`resources/glm/zcode.cjs`) **roda como CLI completa**
com esse Node:

- `zcode 0.16.3` responde; `doctor` confirma
  `platform: win32/arm64`, `process: zcode-cli`, `node: v24.19.0`;
- comandos disponíveis incluem TUI de tela cheia, `login` (OAuth Z.AI),
  `app-server`, `commands`, `doctor`;
- **pico de RAM medido: 227 MB** — contra ~700 MB da interface gráfica.

Ressalva honesta: usar o `.cjs` diretamente **não está documentado pelo
fabricante** (a doc só publica o instalador desktop). Funciona, mas é
solução nossa; uma atualização do app pode mudar o caminho do arquivo.

## 5. Veredito

**AGUENTA — pela via CLI. Com ressalva séria na via gráfica.**

- **CLI (recomendada aqui): 227 MB de pico.** Cabe nesta máquina mesmo
  com o Loop Laura rodando. É o caminho para uso regular.
- **App desktop: ~700 MB** e swap de 4,6 GB com ele aberto. Funciona
  nativo, mas empurra a máquina (que já vive com 200–500 MB livres) para
  paginação constante em disco eMMC lento — degrada o loop que roda aqui
  24h.

**Recomendação:** usar a **CLI** para trabalho de verdade nesta máquina;
o app gráfico só **sob demanda** (abrir, usar, fechar), nunca residente
junto com o loop. Se o objetivo for a interface gráfica rodando
continuamente, o caminho honesto é outra máquina ou mais RAM — não há
ajuste de software que crie memória que não existe.

**Perfil leve preservado:** nenhum serviço do Windows foi reativado;
nenhuma otimização desfeita.

## 6. Próximos passos sugeridos (decisão de Miguel)

1. Concluir o teste da via CLI (Node + `zcode.cjs`) — se funcionar, seria
   o modo leve, sem os ~700 MB da interface gráfica.
2. Decidir o uso: sob demanda (recomendado) × residente (não recomendado
   nesta máquina).
3. Se for usar de verdade aqui, considerar upgrade de RAM — o Galaxy
   Book Go tem memória soldada, então na prática significa outra
   máquina.
4. O login/API key do ZCode ficou **pendente de Miguel** — não foi
   configurado (credencial não passa por mim).

— LAURA-CLAUDE, chefe do Loop Laura, segunda-feira 17/08/2026 17:09 BRT
