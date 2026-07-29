#!/usr/bin/env python3
import os, glob, re, json

MANUSCRIPT_DIR = 'Outros/novo livro/Kimi K3/manuscrito'
VOL2_ARCH_PATH = 'Outros/novo livro/Kimi K3/ARQUITETURA_VOL2_O_MALANDRO.md'
BANCO_LINKS_PATH = 'Outros/novo livro/Kimi K3/BANCO_DE_LINKS.md'
MANUAL_ESTILO_PATH = 'Outros/novo livro/Kimi K3/MANUAL_DE_ESTILO.md'
TARGET_INDEX = 'Outros/novo livro/index.html'

version_map_v7 = {
    '00_frontmatter.md': 'Kimi 4.0',
    '01_estarei_vingado.md': 'Kimi 4.30',
    '02_tarifa_moraes.md': 'Kimi 4.31',
    '03_pena_de_morte_financeira.md': 'Kimi 4.32',
    '04_quatro_a_zero.md': 'Kimi 4.33',
    '05_nove_condutas.md': 'Kimi 4.34',
    '06_washington_e_aqui.md': 'Kimi 4.24',
    '07_o_neto_do_ditador.md': 'Kimi 4.10',
    '08_o_lobista.md': 'Kimi 4.11',
    '09_a_internacional_fascista.md': 'Kimi 4.12',
    '10_dark_horse.md': 'Kimi 4.13',
    '11_o_laboratorio_do_texas.md': 'Kimi 4.14',
    '12_aqui_estou_livre.md': 'Kimi 4.25',
    '13_a_campanha_de_pressao.md': 'Kimi 4.16',
    '14_2022_a_eleicao_contestada.md': 'Kimi 4.17',
    '15_o_chanceler_informal.md': 'Kimi 4.18',
    '16_a_campanha_de_2018_e_o_recorde.md': 'Kimi 4.19',
    '17_olavo_armas_e_a_fabricacao_do_guerreiro.md': 'Kimi 4.20',
    '18_o_cla_como_sistema.md': 'Kimi 4.21',
    '19_o_filho_03.md': 'Kimi 4.22',
    '20_o_espelho_de_2026.md': 'Kimi 4.26',
    '21_o_que_falta_julgar.md': 'Kimi 4.27',
    '22_anatomia_de_uma_escolha.md': 'Kimi 4.28',
    '23_a_campainha_de_southlake.md': 'Kimi 4.29',
    '99_aparatos_finais.md': 'Kimi 4.0'
}

# 1. Load V7 23 Chapters
files_v7 = sorted(glob.glob(os.path.join(MANUSCRIPT_DIR, '*.md')))
v7_chapters = {}

for fpath in files_v7:
    fname = os.path.basename(fpath)
    ver_tag = version_map_v7.get(fname, 'Kimi 4.0')
    
    with open(fpath, 'r', encoding='utf-8') as f:
        full_text = f.read()
        
    if '### 📋 Bloco de produção' in full_text:
        parts = full_text.split('### 📋 Bloco de produção')
        main_content = parts[0].strip()
        prod_block = '### 📋 Bloco de produção' + parts[1]
    elif '## 📋 Bloco de produção' in full_text:
        parts = full_text.split('## 📋 Bloco de produção')
        main_content = parts[0].strip()
        prod_block = '## 📋 Bloco de produção' + parts[1]
    else:
        main_content = full_text.strip()
        prod_block = ''
        
    title_match = re.search(r'^#\s+(.+)$', main_content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else fname
    
    key = fname.replace('.md', '')
    
    v7_chapters[key] = {
        'id': key,
        'filename': fname,
        'title': title,
        'versionTag': ver_tag,
        'badge': f"{title} · Versão {ver_tag} · V7 Oficial Protegida 🔒",
        'mainContent': main_content,
        'prodBlock': prod_block
    }

# 2. Load Volume 2 Architecture & Chapters
with open(VOL2_ARCH_PATH, 'r', encoding='utf-8') as f:
    vol2_arch_text = f.read()

tables = re.findall(r'### (PARTE [^\n]+)\n+\| Cap \| Título \(prov\.\) \| Pergunta central \| Fonte-base \|\n\|---\|---\|---\|---\|\n((?:\|[^\n]+\n)+)', vol2_arch_text)

vol2_chapters = {}
vol2_chapters['arquitetura_geral'] = {
    'id': 'arquitetura_geral',
    'title': '🏛️ Arquitetura Geral — Vol. 2: O Malandro',
    'versionTag': 'Arquitetura V1',
    'badge': 'Volume 2: O Malandro · Estrutura Geral Planejada (5 Partes, 20 Caps)',
    'mainContent': vol2_arch_text,
    'prodBlock': '',
    'isSkeleton': False
}

for part_title, table_body in tables:
    lines = table_body.strip().split('\n')
    for line in lines:
        cols = [c.strip() for c in line.split('|')[1:-1]]
        if len(cols) >= 4:
            cap_num, title, question, sources = cols[:4]
            cap_id = f"v2_cap_{int(cap_num):02d}"
            vol2_chapters[cap_id] = {
                'id': cap_id,
                'capNum': cap_num,
                'part': part_title,
                'title': f"Capítulo {cap_num} — {title}",
                'question': question,
                'sources': sources,
                'versionTag': 'Esqueleto V1',
                'badge': f"Vol. 2 · Cap. {cap_num} · Esqueleto Planejado 📌",
                'isSkeleton': True
            }

# 3. Read Banco de Links, Mapa de Entrevistas & Manual de Estilo
MAPA_ENTREVISTAS_PATH = 'Outros/novo livro/Kimi K3/MAPA_ENTREVISTAS.md'

with open(BANCO_LINKS_PATH, 'r', encoding='utf-8') as f:
    banco_links_content = f.read()

with open(MANUAL_ESTILO_PATH, 'r', encoding='utf-8') as f:
    manual_estilo_content = f.read()

def read_file_if_exists(p):
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

mapa_entrevistas_content = read_file_if_exists(MAPA_ENTREVISTAS_PATH)
exp_antigravity = read_file_if_exists('Outros/novo livro/Kimi K3/cap01_experimental_antigravity.md')
exp_claude = read_file_if_exists('Outros/novo livro/Kimi K3/cap01_experimental_claude.md')
exp_gpt = read_file_if_exists('Outros/novo livro/Kimi K3/cap01_experimental_gpt.md')

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Filhos da Impunidade — Central Editorial (V8 Inteligente + Manual de Estilo Interativo)</title>
  <meta name="description" content="Central editorial e revisor do livro Filhos da Impunidade, por Miguel do Rosário. Leitor V8 com 23 capítulos do Vol. 1, estrutura do Vol. 2 e Manual de Estilo Interativo com propostas por voz.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Inter:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#fbf7ee',
              100: '#f3e9d2',
              500: '#d4af37',
              600: '#b89228',
              800: '#684d0e',
              900: '#1a160c',
            },
            darkbg: '#0c0d10',
            cardbg: '#14161d',
            bordercolor: '#262936',
          },
          fontFamily: {
            serif: ['Merriweather', 'Georgia', 'serif'],
            sans: ['Inter', 'sans-serif'],
            display: ['Cinzel', 'serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }
        }
      }
    }
  </script>

  <!-- Marked JS & Lucide Icons -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    body {
      background-color: #f6f4ee;
      color: #0f172a;
      font-family: 'Inter', sans-serif;
      transition: background-color 0.3s ease, color 0.3s ease;
    }
    
    html.dark body {
      background-color: #0c0d10 !important;
      color: #f8fafc !important;
    }
    
    html.dark header#app-header {
      background-color: rgba(15, 23, 42, 0.95) !important;
      border-color: #334155 !important;
      color: #f8fafc !important;
    }

    html.dark section#reader-toolbar {
      background-color: #1e293b !important;
      border-color: #334155 !important;
    }

    .glass-panel {
      background-color: #ffffff;
      border: 1px solid #e2e8f0;
      color: #0f172a;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    }

    select option {
      background-color: #ffffff;
      color: #0f172a;
    }

    html.dark select option {
      background-color: #0f172a !important;
      color: #f8fafc !important;
    }

    html.dark .glass-panel {
      background: #14161d !important;
      border-color: #262936 !important;
      color: #f8fafc !important;
    }

    html.dark .glass-card {
      background: #14161d !important;
      border-color: #262936 !important;
      color: #f8fafc !important;
    }

    html.dark .prose-book {
      color: #e2e8f0 !important;
    }
    html.dark .prose-book p {
      color: #cbd5e1 !important;
    }
    html.dark .prose-book h1 {
      color: #f8fafc !important;
    }
    html.dark .prose-book h2 {
      color: #fbbf24 !important;
    }
    html.dark .prose-book h3 {
      color: #cbd5e1 !important;
    }
    html.dark .prose-book blockquote {
      background: #1e1b4b !important;
      color: #fef08a !important;
      border-left-color: #f59e0b !important;
    }

    html.dark #modal-ai-audit {
      background-color: rgba(12, 13, 16, 0.95) !important;
    }
    html.dark #modal-ai-audit > div {
      background-color: #14161d !important;
      border-color: #334155 !important;
      color: #f8fafc !important;
    }
    html.dark #modal-ai-audit header {
      background-color: #1e293b !important;
      border-color: #334155 !important;
    }
    
    .prose-book {
      font-family: 'Merriweather', 'Lora', Georgia, serif;
      font-size: 1.35rem;
      line-height: 1.85;
      color: #111827;
    }
    
    .prose-book p {
      margin-bottom: 1.6rem;
      text-align: left;
      color: #111827;
      font-weight: 400;
    }
    
    .prose-book h1 {
      font-family: 'Cinzel', serif;
      font-size: 2.25rem;
      font-weight: 800;
      color: #0f172a;
      margin-top: 1.25rem;
      margin-bottom: 1.25rem;
      letter-spacing: 0.02em;
    }
    
    .prose-book h2 {
      font-family: 'Cinzel', serif;
      font-size: 1.6rem;
      color: #854d0e;
      margin-top: 2.25rem;
      margin-bottom: 1rem;
      font-weight: 700;
    }

    .prose-book h3 {
      font-family: 'Cinzel', serif;
      font-size: 1.3rem;
      color: #1e293b;
      margin-top: 1.75rem;
      margin-bottom: 0.85rem;
    }

    .prose-book blockquote {
      border-left: 4px solid #d97706;
      padding-left: 1.5rem;
      font-style: italic;
      color: #334155;
      background: #fef3c7;
      padding-top: 1rem;
      padding-bottom: 1rem;
      border-radius: 0 0.5rem 0.5rem 0;
      margin-bottom: 1.75rem;
    }

    .prose-book hr {
      border-color: #cbd5e1;
      margin: 2.5rem 0;
    }

    /* CUSTOM STYLES FOR MANUAL DE ESTILO MODAL (ELEGANT TYPOGRAPHY & NO OVERFLOW) */
    .prose-manual {
      font-family: 'Inter', sans-serif;
      color: #1e293b;
    }

    .prose-manual h1 {
      font-family: 'Cinzel', serif;
      font-size: 1.35rem !important;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.35 !important;
      margin-top: 0.5rem;
      margin-bottom: 1rem;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 0.5rem;
      letter-spacing: 0.02em;
    }

    .prose-manual h2 {
      font-family: 'Cinzel', serif;
      font-size: 1.1rem !important;
      color: #b45309;
      margin-top: 1.25rem;
      margin-bottom: 0.5rem;
      line-height: 1.3 !important;
    }

    .prose-manual p {
      font-size: 0.95rem;
      line-height: 1.6;
      color: #334155;
      margin-bottom: 0.75rem;
      text-align: left;
    }

    .prose-manual blockquote {
      border-left: 3px solid #7c3aed;
      background: #f3e8ff;
      padding: 0.75rem 1rem;
      font-size: 0.875rem;
      color: #581c87;
      border-radius: 0 0.5rem 0.5rem 0;
      margin-bottom: 1.25rem;
    }

    .glass-panel {
      background: #ffffff;
      backdrop-filter: blur(12px);
      border: 1px solid #e2e8f0;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .glass-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      transition: all 0.2s ease-in-out;
    }

    .glass-card:hover {
      border-color: #d97706;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }

    /* Custom Scrollbars */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #f1f5f9;
    }
    ::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #d97706;
    }

    .gold-glow {
      box-shadow: 0 10px 30px -5px rgba(217, 119, 6, 0.15);
    }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased bg-[#f6f4ee] text-slate-900 selection:bg-amber-300 selection:text-slate-900">

  <!-- TOP HEADER -->
  <header id="app-header" class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm px-4 lg:px-8 py-3.5 text-slate-900 font-sans">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
      
      <!-- BRAND & VOLUME SELECTOR -->
      <div class="flex flex-wrap items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center text-white font-black font-display shadow-sm text-lg">
          FI
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs uppercase tracking-widest font-mono text-amber-950 dark:text-amber-400 font-extrabold">Filhos da Impunidade</span>
            <span id="volume-badge-tag" class="text-xs bg-amber-200 text-amber-950 border-2 border-amber-400 dark:bg-amber-400/20 dark:text-amber-300 dark:border-amber-400/40 px-2.5 py-0.5 rounded-md font-mono font-black shadow-sm">Vol. 1 V8 (23 Caps)</span>
          </div>
          <h1 id="volume-title-display" class="text-lg md:text-xl font-black font-display tracking-tight text-slate-900 dark:text-slate-100">Vol. 1: O Foragido (Eduardo)</h1>
        </div>

        <!-- VOLUME SELECTION SWITCHER -->
        <div class="ml-2 flex items-center gap-1 bg-slate-200 dark:bg-slate-800 p-1.5 rounded-xl border-2 border-slate-400 dark:border-slate-700 text-xs font-sans">
          <button id="btn-vol1-v7" onclick="switchVolume('vol1_v7')" class="px-3.5 py-1.5 rounded-lg transition font-black bg-amber-600 hover:bg-amber-700 text-white shadow-md cursor-pointer">
            Vol. 1 (23 Caps • V8)
          </button>
          <button id="btn-vol2-v1" onclick="switchVolume('vol2_v1')" class="px-3.5 py-1.5 rounded-lg transition font-extrabold text-slate-900 dark:text-slate-200 hover:text-emerald-800 dark:hover:text-emerald-300 hover:bg-slate-300 dark:hover:bg-slate-700 cursor-pointer">
            Vol. 2: O Malandro 📌
          </button>
        </div>
      </div>

      <!-- CHAPTER SELECTOR & NAVIGATION CONTROLS -->
      <div class="flex flex-wrap items-center gap-2">
        <button onclick="navigateChapter(-1)" title="Capítulo Anterior" class="p-2 bg-white hover:bg-slate-100 border border-slate-300 rounded-xl text-slate-800 transition shadow-sm cursor-pointer">
          <i data-lucide="chevron-left" class="w-5 h-5"></i>
        </button>
        
        <select id="chapter-select" onchange="selectChapter(this.value)" class="bg-white border-2 border-amber-500 rounded-xl px-4 py-2 text-sm font-bold text-slate-900 focus:outline-none focus:border-amber-600 shadow-sm max-w-xs md:max-w-md truncate cursor-pointer">
          <!-- Dynamically populated -->
        </select>

        <button onclick="navigateChapter(1)" title="Próximo Capítulo" class="p-2 bg-white hover:bg-slate-100 border border-slate-300 rounded-xl text-slate-800 transition shadow-sm cursor-pointer">
          <i data-lucide="chevron-right" class="w-5 h-5"></i>
        </button>

        <button onclick="backToHomeSumario()" title="Roteiro Estrutural do Livro" class="flex items-center gap-1.5 px-3.5 py-2 bg-slate-800 dark:bg-slate-700 hover:bg-slate-700 text-white rounded-xl text-xs font-black transition shadow-sm cursor-pointer">
          <i data-lucide="map" class="w-4 h-4 text-amber-400"></i>
          <span>📌 Roteiro do Livro</span>
        </button>

        <button onclick="compileAndReadFullBook()" title="Compilar todos os capítulos em um único manuscrito" class="flex items-center gap-1.5 px-3.5 py-2 bg-amber-600 hover:bg-amber-700 text-white rounded-xl text-xs font-black transition shadow-md cursor-pointer">
          <i data-lucide="book-open" class="w-4 h-4 text-white"></i>
          <span>📚 Ler / Compilar Livro Inteiro</span>
        </button>

        <button onclick="openDatabaseModal()" class="flex items-center gap-1.5 px-3.5 py-2 bg-slate-100 hover:bg-slate-200 border border-slate-300 rounded-xl text-xs font-bold text-slate-800 transition shadow-sm cursor-pointer">
          <i data-lucide="database" class="w-4 h-4 text-amber-600"></i>
          <span class="hidden sm:inline">Central de Fontes</span>
        </button>

        <button onclick="openManualModal()" class="flex items-center gap-1.5 px-3.5 py-2 bg-purple-100 hover:bg-purple-200 border border-purple-300 rounded-xl text-xs font-bold text-purple-950 transition shadow-sm cursor-pointer">
          <i data-lucide="book-marked" class="w-4 h-4 text-purple-700"></i>
          <span class="hidden sm:inline">Manual de Estilo (#1-#27+)</span>
        </button>

        <button onclick="openGitSyncModal()" class="flex items-center gap-1.5 px-3.5 py-2 bg-emerald-100 hover:bg-emerald-200 border border-emerald-300 rounded-xl text-xs font-bold text-emerald-950 transition shadow-sm cursor-pointer">
          <i data-lucide="cloud-cog" class="w-4 h-4 text-emerald-700"></i>
          <span class="hidden sm:inline">☁️ Sincronizar GitHub</span>
        </button>

        <!-- THEME SWITCHER (MODO DIA / MODO NOITE) -->
        <button id="theme-toggle-btn" onclick="toggleThemeMode()" title="Alternar Modo Dia / Noite" class="flex items-center gap-1.5 px-3.5 py-2 bg-amber-50 hover:bg-amber-100 border border-amber-300 rounded-xl text-xs font-bold text-amber-900 transition shadow-sm cursor-pointer">
          <span id="theme-toggle-icon">☀️</span>
          <span id="theme-toggle-label" class="hidden sm:inline">Modo Dia</span>
        </button>
      </div>

      <!-- VIEW MODE SWITCHER (MAXIMALIST LIGHT BUTTONS) -->
      <div class="flex items-center gap-1.5 bg-slate-100 p-1.5 rounded-xl border border-slate-300">
        <button id="btn-mode-single" onclick="setMode('single')" class="flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-extrabold transition-all bg-amber-600 text-white shadow-sm font-sans cursor-pointer">
          <i data-lucide="book-open" class="w-4 h-4"></i>
          <span>Visão Leitura</span>
        </button>
        <button id="btn-mode-compare" onclick="setMode('compare')" class="flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-bold transition-all text-slate-700 hover:text-slate-900 hover:bg-slate-200 font-sans cursor-pointer">
          <i data-lucide="columns-2" class="w-4 h-4"></i>
          <span>Duelo Lado a Lado</span>
        </button>
      </div>

    </div>
  </header>

  <!-- SUBHEADER / VERSION SELECTION BAR -->
  <section id="app-subheader" class="bg-slate-100 border-b border-slate-200 py-3 px-4 lg:px-8">
    <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-4">
      
      <!-- VERSION TABS (SINGLE MODE) -->
      <div id="single-version-tabs" class="flex flex-wrap items-center gap-2">
        <!-- Rendered dynamically by renderVersionTabs() -->
      </div>

      <!-- COMPARE SELECTORS (COMPARE MODE) -->
      <div id="compare-version-tabs" class="hidden flex-1 grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div class="flex items-center gap-2">
          <label class="text-xs text-slate-700 font-bold font-mono">COLUNA 1:</label>
          <select id="select-left-version" onchange="updateCompare()" class="flex-1 bg-white border border-slate-300 rounded-lg px-3 py-1.5 text-sm text-slate-900 font-bold focus:outline-none focus:border-amber-500 shadow-sm">
            <!-- Rendered dynamically -->
          </select>
        </div>
        <div class="flex items-center gap-2">
          <label class="text-xs text-slate-700 font-bold font-mono">COLUNA 2:</label>
          <select id="select-right-version" onchange="updateCompare()" class="flex-1 bg-white border border-slate-300 rounded-lg px-3 py-1.5 text-sm text-slate-900 font-bold focus:outline-none focus:border-amber-500 shadow-sm">
            <!-- Rendered dynamically -->
          </select>
        </div>
      </div>

      <!-- ACTION BUTTONS (DOWNLOAD & REVISE BY VOICE/TEXT) -->
      <div class="flex items-center gap-2">
        <button onclick="downloadCurrentChapter()" title="Baixar Capítulo ou Livro Inteiro em Markdown (.md)" class="flex items-center gap-2 px-4 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-black shadow-md border border-emerald-500 transition-all cursor-pointer">
          <i data-lucide="download" class="w-4 h-4"></i>
          <span>📥 Baixar Texto (.md)</span>
        </button>
        <button onclick="openAiAuditModal()" class="flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-purple-700 to-indigo-700 hover:from-purple-800 hover:to-indigo-800 text-white rounded-xl text-xs font-extrabold shadow-md border border-purple-500 transition-all cursor-pointer">
          <i data-lucide="sparkles" class="w-4.5 h-4.5 text-amber-300"></i>
          <span>🤖 Entrar no Estúdio Editorial (Página Nova)</span>
        </button>
      </div>

    </div>
  </section>

  <!-- MAIN READING CONTAINER -->
  <main id="app-main" class="flex-1 max-w-7xl w-full mx-auto p-4 lg:p-8 flex flex-col gap-6">

    <!-- VERSION METRICS BANNER -->
    <div id="version-metrics-banner" class="glass-card rounded-2xl p-4 flex flex-wrap items-center justify-between gap-4 text-xs font-mono border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 text-slate-900 dark:text-slate-100 shadow-sm">
      <div class="flex items-center gap-6">
        <div>
          <span class="text-slate-600 dark:text-slate-400 uppercase block font-bold">Autor da Versão:</span>
          <span id="metric-author" class="text-amber-800 dark:text-amber-400 font-extrabold text-sm">Kimi (ZCode) & Miguel</span>
        </div>
        <div>
          <span class="text-slate-600 dark:text-slate-400 uppercase block font-bold">Etiqueta Oficial:</span>
          <span id="metric-version-tag" class="text-amber-900 dark:text-amber-300 font-extrabold text-sm bg-amber-100 dark:bg-amber-400/10 px-2 py-0.5 rounded border border-amber-300 dark:border-amber-400/30">Kimi 4.30</span>
        </div>
        <div>
          <span class="text-slate-600 dark:text-slate-400 uppercase block font-bold">Total de Palavras:</span>
          <span id="metric-words" class="text-slate-900 dark:text-slate-200 font-bold text-sm">--</span>
        </div>
        <div>
          <span class="text-slate-600 dark:text-slate-400 uppercase block font-bold">Frases Analisadas:</span>
          <span id="metric-sentences" class="text-slate-900 dark:text-slate-200 font-bold text-sm">--</span>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-slate-600 dark:text-slate-400 font-semibold italic font-sans" id="metric-badge">Oficial Protegida 🔒</span>
      </div>
    </div>

    <!-- SINGLE READER VIEW -->
    <div id="single-view-container" class="flex flex-col gap-6">
      <div class="glass-panel rounded-3xl p-6 lg:p-12 shadow-2xl relative gold-glow min-h-[600px]">
        <div id="reader-content" class="prose-book max-w-3xl mx-auto">
          <!-- Rendered Content / Skeleton -->
        </div>
      </div>

      <!-- ACCORDION: BLOCO DE PRODUÇÃO -->
      <div id="prod-block-container" class="glass-panel border border-amber-500/30 rounded-3xl p-6 shadow-xl">
        <button onclick="toggleProdBlock()" class="w-full flex items-center justify-between text-left group">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-lg bg-amber-500/20 flex items-center justify-center text-amber-400 border border-amber-500/30">
              📋
            </div>
            <div>
              <h3 class="text-base font-bold font-display text-amber-400 group-hover:text-amber-300 transition">Bloco de Produção & Apuração</h3>
              <p class="text-xs text-slate-400">Pesquisas pendentes, transcrições, notas de rodapé e links primários deste capítulo</p>
            </div>
          </div>
          <i id="prod-block-chevron" data-lucide="chevron-down" class="w-5 h-5 text-amber-400 transition-transform duration-200"></i>
        </button>
        <div id="prod-block-content" class="hidden mt-6 pt-6 border-t border-amber-500/20 prose-book text-sm max-w-none">
          <!-- Rendered Prod Block -->
        </div>
      </div>
    </div>

    <!-- COMPARE SIDE-BY-SIDE VIEW -->
    <div id="compare-view-container" class="hidden grid grid-cols-1 lg:grid-cols-2 gap-6 min-h-[600px]">
      <div class="glass-panel rounded-3xl p-6 lg:p-8 border border-white/10 flex flex-col">
        <div class="border-b border-white/10 pb-3 mb-4 flex items-center justify-between">
          <span id="compare-left-title" class="font-display font-bold text-brand-500">Versão 1</span>
          <span id="compare-left-badge" class="text-xs bg-amber-400/10 text-amber-300 px-2 py-0.5 rounded font-mono">Oficial</span>
        </div>
        <div id="compare-left-content" class="prose-book text-sm leading-relaxed overflow-y-auto max-h-[750px] pr-2">
          <!-- Rendered Left Content -->
        </div>
      </div>

      <div class="glass-panel rounded-3xl p-6 lg:p-8 border border-white/10 flex flex-col">
        <div class="border-b border-white/10 pb-3 mb-4 flex items-center justify-between">
          <span id="compare-right-title" class="font-display font-bold text-purple-400">Versão 2</span>
          <span id="compare-right-badge" class="text-xs bg-purple-400/10 text-purple-300 px-2 py-0.5 rounded font-mono">Revisão R1</span>
        </div>
        <div id="compare-right-content" class="prose-book text-sm leading-relaxed overflow-y-auto max-h-[750px] pr-2">
          <!-- Rendered Right Content -->
        </div>
      </div>
    </div>

  </main>

  <!-- MODAL DE ESTÚDIO EDITORIAL (FULL BLEED FULLVIEW EDGE-TO-EDGE LIGHT E-READER THEME) -->
  <div id="modal-ai-audit" class="fixed inset-0 z-[9999] bg-[#f8f6f0] hidden flex flex-col w-screen h-screen min-h-screen overflow-y-auto text-slate-900 font-sans">
    <!-- FULL VIEW TOP HEADER BAR (STRETCHES 100% FULL WIDTH) -->
    <div class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 px-8 py-4 flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm w-full">
      <!-- LEFT ACTION BUTTONS & CHAPTER TITLE -->
      <div class="flex items-center gap-4">
        <button onclick="closeAiAuditModal()" class="px-5 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-900 border border-slate-300 rounded-xl text-sm font-extrabold flex items-center gap-2 transition shadow-sm cursor-pointer">
          <i data-lucide="arrow-left" class="w-4 h-4 text-purple-700"></i>
          <span>Voltar ao Leitor</span>
        </button>
        
        <button onclick="goHome()" class="px-5 py-2.5 bg-amber-100 hover:bg-amber-200 text-amber-950 border border-amber-300 rounded-xl text-sm font-extrabold flex items-center gap-2 transition shadow-sm cursor-pointer">
          <i data-lucide="home" class="w-4 h-4 text-amber-700"></i>
          <span>Home</span>
        </button>

        <div class="h-6 w-px bg-slate-300 hidden md:block"></div>

        <div class="flex items-center gap-2.5">
          <span class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></span>
          <h3 id="studio-chapter-title" class="text-base md:text-lg font-extrabold font-display text-slate-900 tracking-tight">📖 Estúdio de Correção IA — Cap. 01</h3>
        </div>
      </div>

      <!-- RIGHT MODEL SELECTOR DROPDOWN & SETTINGS -->
      <div class="flex items-center gap-3">
        <!-- VERTICAL MODEL DROPDOWN MENU -->
        <div class="relative inline-block text-left">
          <button id="btn-model-dropdown-toggle" onclick="toggleModelDropdown()" class="flex items-center gap-2.5 px-4.5 py-2.5 bg-white hover:bg-slate-50 border-2 border-indigo-500 rounded-xl text-xs font-extrabold text-indigo-950 shadow-sm transition cursor-pointer">
            <i data-lucide="cpu" class="w-4.5 h-4.5 text-indigo-700"></i>
            <span id="active-model-label">♊ Gemini 3.6 Ultra</span>
            <i data-lucide="chevron-down" class="w-4 h-4 text-indigo-700"></i>
          </button>

          <!-- VERTICAL DROPDOWN LIST -->
          <div id="model-dropdown-menu" class="hidden absolute right-0 mt-2 w-64 rounded-2xl bg-white border-2 border-indigo-200 shadow-2xl z-50 overflow-hidden py-1 divide-y divide-slate-100">
            <div class="px-3.5 py-2 border-b border-slate-200 text-[10px] uppercase font-mono font-bold text-slate-500 tracking-wider flex items-center justify-between bg-indigo-50">
              <span>🤖 Seleção de IAs Frontier</span>
              <span class="text-indigo-800 font-mono font-bold">v8.7</span>
            </div>
            <button onclick="selectAiEngine('gemini')" class="w-full text-left px-4 py-2.5 text-xs font-semibold flex items-center justify-between text-slate-800 hover:bg-slate-100 transition cursor-pointer">
              <div class="flex items-center gap-2">
                <i data-lucide="sparkles" class="w-4 h-4 text-cyan-600"></i>
                <span>Gemini 3.6 Ultra / Flash</span>
              </div>
              <span class="bg-cyan-100 text-cyan-900 border border-cyan-300 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold">Google</span>
            </button>
            <button onclick="selectAiEngine('gpt56')" class="w-full text-left px-4 py-2.5 text-xs font-semibold flex items-center justify-between text-slate-800 hover:bg-slate-100 transition cursor-pointer">
              <div class="flex items-center gap-2">
                <i data-lucide="brain" class="w-4 h-4 text-blue-600"></i>
                <span>GPT 5.6 / o3-Pro</span>
              </div>
              <span class="bg-blue-100 text-blue-900 border border-blue-300 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold">OpenAI</span>
            </button>
            <button onclick="selectAiEngine('opus5')" class="w-full text-left px-4 py-2.5 text-xs font-semibold flex items-center justify-between text-slate-800 hover:bg-slate-100 transition cursor-pointer">
              <div class="flex items-center gap-2">
                <i data-lucide="crown" class="w-4 h-4 text-amber-600"></i>
                <span>Claude Opus 5.0</span>
              </div>
              <span class="bg-amber-100 text-amber-900 border border-amber-300 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold">Anthropic</span>
            </button>
            <button onclick="selectAiEngine('deepseek')" class="w-full text-left px-4 py-2.5 text-xs font-semibold flex items-center justify-between text-slate-800 hover:bg-slate-100 transition cursor-pointer">
              <div class="flex items-center gap-2">
                <i data-lucide="zap" class="w-4 h-4 text-purple-600"></i>
                <span>DeepSeek V4 Pro</span>
              </div>
              <span class="bg-purple-100 text-purple-900 border border-purple-300 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold">DeepSeek</span>
            </button>
            <button onclick="selectAiEngine('kimi35')" class="w-full text-left px-4 py-2.5 text-xs font-semibold flex items-center justify-between text-slate-800 hover:bg-slate-100 transition cursor-pointer">
              <div class="flex items-center gap-2">
                <i data-lucide="moon" class="w-4 h-4 text-emerald-600"></i>
                <span>Kimi 3.5</span>
              </div>
              <span class="bg-emerald-100 text-emerald-900 border border-emerald-300 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold">Moonshot</span>
            </button>
            <button onclick="selectAiEngine('glm52')" class="w-full text-left px-4 py-2.5 text-xs font-semibold flex items-center justify-between text-slate-800 hover:bg-slate-100 transition cursor-pointer">
              <div class="flex items-center gap-2">
                <i data-lucide="globe" class="w-4 h-4 text-rose-600"></i>
                <span>GLM 5.2 / Zhipu</span>
              </div>
              <span class="bg-rose-100 text-rose-900 border border-rose-300 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold">Zhipu</span>
            </button>
          </div>
        </div>

        <button onclick="openSettingsModal()" class="flex items-center gap-2 px-4 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 rounded-xl text-xs font-bold shadow-sm transition cursor-pointer">
          <i data-lucide="settings" class="w-4 h-4 text-slate-600"></i>
          <span>⚙️ Configurações</span>
        </button>
      </div>
    </div>

    <!-- MAIN FULL VIEW STUDIO CONTENT AREA (FULL BLEED 100% WIDTH 2-COLUMN WORKSPACE) -->
    <div class="w-full px-6 py-6 flex-1 flex flex-col lg:flex-row gap-6 items-start">
      
      <!-- LEFT COLUMN: PAINEL CONVERSACIONAL DE DITADO & COMANDOS IA (SIDEBAR DE COMANDOS) -->
      <div class="w-full lg:w-4/12 flex flex-col gap-6 lg:sticky lg:top-24">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 space-y-5 shadow-md">
          <div class="flex items-center justify-between border-b border-slate-200 pb-4">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-purple-100 border border-purple-300 flex items-center justify-center text-purple-800">
                <i data-lucide="mic" class="w-6 h-6"></i>
              </div>
              <div>
                <h4 class="text-base font-extrabold font-display text-slate-900">Comando & Ditado por Voz</h4>
                <p class="text-xs text-purple-900 font-semibold">Fale ou digite a instrução de revisão desejada</p>
              </div>
            </div>

            <button id="btn-voice-input" onclick="toggleVoiceInput()" class="px-4 py-2.5 bg-purple-700 hover:bg-purple-800 text-white rounded-xl text-xs font-extrabold flex items-center gap-2 shadow-sm transition cursor-pointer">
              <i data-lucide="mic" class="w-4 h-4"></i>
              <span id="voice-btn-text">Iniciar Ditado</span>
            </button>
            <span id="voice-timer-display" class="hidden font-mono text-sm text-purple-950 font-extrabold bg-purple-100 px-3 py-1 rounded-lg border border-purple-300">00:00</span>
          </div>

          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <label class="block text-xs font-mono font-bold text-slate-700 uppercase">Instrução Editorial Dita / Escrita:</label>
              <div class="flex items-center gap-2">
                <button onclick="toggleInstructionHistory()" class="text-xs font-mono font-bold text-purple-700 hover:text-purple-900 flex items-center gap-1">
                  <i data-lucide="history" class="w-3.5 h-3.5"></i>
                  <span id="history-toggle-text">📜 Histórico</span>
                </button>
                <button onclick="clearInstructionInput()" class="text-xs font-mono font-bold text-amber-900 hover:text-amber-950 flex items-center gap-1 bg-amber-100 px-2 py-0.5 rounded border border-amber-300">
                  <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
                  <span>Limpar</span>
                </button>
              </div>
            </div>
            <textarea id="deepseek-instruction-input" rows="4" oninput="onInstructionInputChanged()" class="w-full bg-slate-50 border-2 border-slate-300 rounded-xl p-4 text-base font-bold text-slate-900 focus:outline-none focus:border-purple-600 focus:bg-white shadow-inner font-sans leading-relaxed" placeholder="Ex: 'Tirar o sede de desforra e colocar um torpe desejo de vingança', ou dite a reescrita por voz..."></textarea>
          </div>

          <!-- COLLAPSIBLE INSTRUCTION HISTORY LOG -->
          <div id="deepseek-history-panel" class="hidden bg-slate-50 border border-purple-200 rounded-xl p-3 space-y-2">
            <div class="text-xs font-mono text-purple-900 font-extrabold uppercase">Histórico de Instruções neste Capítulo:</div>
            <div id="deepseek-history-list" class="space-y-1 max-h-36 overflow-y-auto text-xs font-mono font-semibold text-slate-800">
              <!-- Dynamic history items -->
            </div>
          </div>

          <!-- CHECKBOX PROMPTS -->
          <div class="flex flex-col gap-3 bg-purple-50 p-4 rounded-xl border border-purple-200">
            <label for="chk-update-manual-style" class="flex items-center gap-2.5 text-xs text-purple-950 font-bold cursor-pointer">
              <input type="checkbox" id="chk-update-manual-style" checked class="w-4 h-4 rounded border-purple-400 text-purple-700 focus:ring-purple-600 bg-white">
              <span>💡 <strong>Site Inteligente:</strong> Registrar diretriz no Manual de Estilo</span>
            </label>

            <label for="chk-consult-canonical-memory" class="flex items-center gap-2.5 text-xs text-amber-950 font-bold cursor-pointer bg-amber-100/80 px-3 py-2 rounded-lg border border-amber-300 hover:border-amber-400">
              <input type="checkbox" id="chk-consult-canonical-memory" class="w-4 h-4 rounded border-amber-500 text-amber-700 focus:ring-amber-600 bg-white">
              <i data-lucide="database" class="w-4 h-4 text-amber-700"></i>
              <span>🧠 Consultar Memória & Banco de Fontes Canônicas</span>
            </label>
          </div>

          <button onclick="runDeepSeekV4Instruction()" class="w-full py-4 bg-gradient-to-r from-purple-700 to-indigo-700 hover:from-purple-800 hover:to-indigo-800 text-white rounded-xl text-sm font-extrabold uppercase tracking-wider flex items-center justify-center gap-2 shadow-md cursor-pointer">
            <i data-lucide="sparkles" class="w-4.5 h-4.5 text-amber-300"></i>
            <span id="btn-run-ai-text">Executar Reescrita Inteligente</span>
          </button>
        </div>

        <!-- CONVERSATIONAL HUMANIZED AI FEEDBACK (DESTAQUE DE ALTERAÇÃO NA SIDEBAR) -->
        <div id="deepseek-output-results" class="hidden">
          <div class="p-5 bg-amber-50 border-2 border-amber-300 rounded-3xl space-y-3 shadow-md">
            <div class="flex items-center justify-between text-xs font-mono font-extrabold text-amber-950">
              <span class="flex items-center gap-2">
                <i data-lucide="message-square" class="w-4 h-4 text-amber-700"></i>
                <span id="conversational-ai-title">💬 Resposta do Editor Assistente (IA):</span>
              </span>
              <span class="text-[10px] text-purple-950 font-mono font-bold bg-purple-100 px-2 py-0.5 rounded border border-purple-300">IA Conversacional</span>
            </div>
            <div id="conversational-ai-text" class="text-sm text-slate-900 font-medium leading-relaxed font-sans p-1">
              <!-- Dynamic Conversational Feedback -->
            </div>
          </div>
        </div>
      </div>

      <!-- RIGHT COLUMN: CAPÍTULO INTEIRO REESCRITO EM TEMPO REAL (ÁREA PRINCIPAL DE LEITURA E PUBLICAÇÃO) -->
      <div id="deepseek-full-chapter-publication" class="w-full lg:w-8/12 flex-1 flex flex-col gap-6">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 md:p-8 space-y-6 shadow-md w-full">
          <div class="flex flex-col sm:flex-row items-center justify-between gap-4 border-b border-slate-200 pb-4">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-emerald-100 border border-emerald-300 flex items-center justify-center text-emerald-800">
                <i data-lucide="book-open" class="w-6 h-6"></i>
              </div>
              <div>
                <h4 class="text-lg font-extrabold font-display text-slate-900">📖 Capítulo Completo Reescrito (Republicado em Tempo Real)</h4>
                <p class="text-xs text-emerald-900 font-semibold">Visualização integral do capítulo com a correção aplicada imediatamente</p>
              </div>
            </div>

            <!-- ACTION BUTTONS: SALVAR E TORNAR CANÔNICA -->
            <div class="flex flex-wrap items-center gap-2.5">
              <button id="btn-save-as-manual-rule" onclick="convertLastAiToManualRule()" class="hidden px-4 py-2.5 bg-purple-100 hover:bg-purple-200 text-purple-950 border border-purple-300 rounded-xl text-xs font-extrabold flex items-center gap-1.5 shadow-sm">
                <i data-lucide="plus-circle" class="w-4 h-4 text-purple-700"></i>
                <span>+ Manual</span>
              </button>

              <button onclick="makeLastRevisionCanonical()" class="px-5 py-2.5 bg-amber-500 hover:bg-amber-600 text-slate-950 rounded-xl text-xs font-extrabold flex items-center gap-2 shadow-sm border border-amber-600 cursor-pointer">
                <i data-lucide="crown" class="w-4 h-4 text-slate-950"></i>
                <span>👑 Tornar Canônica</span>
              </button>

              <button onclick="saveDeepSeekRevision()" class="px-5 py-2.5 bg-emerald-700 hover:bg-emerald-800 text-white rounded-xl text-xs font-extrabold flex items-center gap-2 shadow-sm cursor-pointer">
                <i data-lucide="save" class="w-4 h-4"></i>
                <span>💾 Gravar Revisão R#</span>
              </button>
            </div>
          </div>

          <!-- RENDERED FULL CHAPTER IN BEAUTIFUL BOOK TYPOGRAPHY (NO MAXIMUM WIDTH CONSTRAINTS, BIGGER FONTS) -->
          <div class="bg-[#faf8f4] border border-amber-200/80 rounded-2xl p-6 md:p-10 space-y-6 w-full shadow-inner">
            <div class="flex items-center justify-between border-b border-amber-200 pb-3">
              <span class="text-xs font-mono font-bold text-amber-900 uppercase tracking-wider flex items-center gap-2">
                <i data-lucide="eye" class="w-4 h-4"></i> Leitura em Tempo Real do Capítulo Reescrito:
              </span>
              <span id="output-engine-badge" class="text-xs font-mono font-bold text-purple-900"></span>
            </div>

            <div id="deepseek-rendered-full-chapter" class="prose-book text-xl md:text-2xl leading-[1.85] text-[#111827] font-serif w-full max-w-none space-y-6">
              <!-- Rendered markdown html of the whole chapter -->
            </div>
          </div>

          <!-- COLLAPSIBLE EDITABLE RAW TEXTAREA FOR MANUAL TWEAKS BEFORE SAVING -->
          <details class="bg-slate-50 border border-slate-300 rounded-2xl p-4 w-full">
            <summary class="text-xs font-mono font-bold text-purple-900 uppercase tracking-wider cursor-pointer flex items-center gap-2">
              <i data-lucide="edit-3" class="w-4 h-4"></i>
              <span>📝 Editar Texto Bruto / Código Fonte do Capítulo (Ajuste Manual Opcional)</span>
            </summary>
              <textarea id="deepseek-editable-result" rows="12" oninput="updateRenderedFullChapterFromTextarea()" class="w-full bg-white border border-slate-300 rounded-xl p-4 text-base font-mono text-slate-900 focus:outline-none focus:border-purple-600 leading-relaxed shadow-inner" placeholder="O texto reescrito do capítulo aparecerá aqui..."></textarea>
            </div>
          </details>
        </div>
      </div>

    </div>
  </div>

  <!-- MODAL DE CENTRAL DE FONTES & BANCO DE LINKS INTERATIVO -->
  <div id="modal-database" class="fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-md hidden flex items-center justify-center p-3 md:p-6">
    <div class="bg-white dark:bg-slate-900 border-2 border-amber-400 dark:border-amber-700/60 rounded-3xl max-w-6xl w-full max-h-[94vh] flex flex-col shadow-2xl overflow-hidden text-slate-900 dark:text-slate-100">
      
      <!-- MODAL HEADER -->
      <div class="p-5 border-b border-amber-200 dark:border-slate-800 flex items-center justify-between bg-amber-100/80 dark:bg-slate-800/80">
        <div class="flex items-center gap-3">
          <div class="w-11 h-11 rounded-2xl bg-amber-600 text-white flex items-center justify-center font-bold shadow-md shrink-0">
            <i data-lucide="database" class="w-6 h-6"></i>
          </div>
          <div>
            <h3 class="text-lg md:text-xl font-black font-display tracking-tight text-slate-900 dark:text-slate-100">🗄️ Central de Fontes & Banco de Links (~70 Documentos)</h3>
            <p class="text-xs text-amber-950 dark:text-amber-300 font-extrabold">Mapa interativo de acórdãos STF, relatórios OFAC/EUA, entrevistas no YouTube e matérias primárias</p>
          </div>
        </div>
        <button onclick="closeDatabaseModal()" class="p-2 hover:bg-slate-200 dark:hover:bg-slate-800 rounded-xl transition text-slate-700 dark:text-slate-300 cursor-pointer">
          <i data-lucide="x" class="w-6 h-6"></i>
        </button>
      </div>

      <!-- FILTER TABS & SEARCH BAR -->
      <div class="p-4 border-b border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900 flex flex-col gap-3">
        <!-- Live Search -->
        <div class="relative w-full">
          <i data-lucide="search" class="w-4 h-4 absolute left-3.5 top-3 text-slate-400"></i>
          <input id="source-search-input" oninput="filterSourceCenter()" type="text" placeholder="🔍 Buscar por termo (ex: STF, CNN, OFAC, YouTube, Intercept, Bannon, Magnitsky)..." class="w-full bg-white dark:bg-slate-800 border-2 border-slate-300 dark:border-slate-700 rounded-xl pl-10 pr-4 py-2 text-xs font-bold text-slate-900 dark:text-slate-100 focus:outline-none focus:border-amber-500 shadow-inner">
        </div>

        <!-- Filter Category Badges -->
        <div class="flex flex-wrap items-center gap-1.5 text-xs font-sans">
          <button onclick="setSourceFilter('all')" id="source-tab-all" class="source-filter-btn px-3 py-1.5 rounded-lg font-black bg-amber-600 text-white shadow-sm cursor-pointer transition">
            🌟 Todos (~70 Fontes)
          </button>
          <button onclick="setSourceFilter('livros')" id="source-tab-livros" class="source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition">
            📚 Livros & PDFs de Referência
          </button>
          <button onclick="setSourceFilter('yt')" id="source-tab-yt" class="source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition">
            🎥 Entrevistas YouTube (Com Transcrição)
          </button>
          <button onclick="setSourceFilter('stf')" id="source-tab-stf" class="source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition">
            ⚖️ STF & Judiciário
          </button>
          <button onclick="setSourceFilter('eua')" id="source-tab-eua" class="source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition">
            🇺🇸 EUA & OFAC (Magnitsky)
          </button>
          <button onclick="setSourceFilter('tarifaco')" id="source-tab-tarifaco" class="source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition">
            📰 Reportagens: Tarifaço
          </button>
          <button onclick="setSourceFilter('dinheiro')" id="source-tab-dinheiro" class="source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition">
            💰 Investigações: Texas & Dinheiro
          </button>
          <button onclick="setSourceFilter('x')" id="source-tab-x" class="source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition">
            🐦 Posts de Prova no X
          </button>
        </div>
      </div>

      <!-- MAIN SOURCE GRID CONTAINER -->
      <div class="p-6 overflow-y-auto space-y-4 flex-1 bg-[#faf8f4] dark:bg-slate-950">
        <div id="source-cards-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- Dynamically Populated Source Cards -->
        </div>
      </div>

    </div>
  </div>

  <!-- MODAL DE VISUALIZAÇÃO DE TRANSCRIÇÃO DE VÍDEO -->
  <div id="modal-transcript-viewer" class="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="bg-white dark:bg-slate-900 border-2 border-amber-400 rounded-3xl max-w-4xl w-full max-h-[90vh] flex flex-col shadow-2xl overflow-hidden text-slate-900 dark:text-slate-100">
      <div class="p-5 border-b border-amber-200 dark:border-slate-800 flex items-center justify-between bg-amber-50 dark:bg-slate-800/80">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-red-600 text-white flex items-center justify-center font-bold shrink-0 shadow">
            <i data-lucide="youtube" class="w-5 h-5"></i>
          </div>
          <div>
            <h3 id="transcript-modal-title" class="text-base md:text-lg font-black font-display text-slate-900 dark:text-slate-100">Transcrição de Vídeo</h3>
            <p id="transcript-modal-subtitle" class="text-xs font-mono font-bold text-amber-950 dark:text-amber-400">Detalhes da apuração e citações do manuscrito</p>
          </div>
        </div>
        <button onclick="closeTranscriptModal()" class="p-2 hover:bg-slate-200 dark:hover:bg-slate-800 rounded-xl transition text-slate-700 dark:text-slate-300 cursor-pointer">
          <i data-lucide="x" class="w-6 h-6"></i>
        </button>
      </div>

      <div class="p-6 overflow-y-auto space-y-4 flex-1 bg-slate-50 dark:bg-slate-950">
        <div id="transcript-modal-body" class="prose-book text-sm leading-relaxed dark:text-slate-200">
          <!-- Rendered Transcript Text -->
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL DE MANUAL DE ESTILO INTERATIVO & CORRIGIDO -->
  <div id="modal-manual" class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-purple-200 rounded-3xl max-w-4xl w-full max-h-[92vh] flex flex-col shadow-2xl overflow-hidden text-slate-900">
      
      <!-- MODAL HEADER -->
      <div class="p-5 border-b border-purple-200 flex items-center justify-between bg-purple-50">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-purple-100 border border-purple-300 flex items-center justify-center text-purple-800">
            <i data-lucide="book-marked" class="w-6 h-6"></i>
          </div>
          <div>
            <h3 class="text-lg font-extrabold font-display text-slate-900">Manual de Estilo & Diretrizes de Escrita</h3>
            <p class="text-xs text-purple-950 font-bold">Regras canônicas vigentes (#1 ao #27) + Propostas do Miguel (#28+)</p>
          </div>
        </div>
        <button onclick="closeManualModal()" class="text-slate-500 hover:text-slate-900 p-1 cursor-pointer">
          <i data-lucide="x" class="w-6 h-6"></i>
        </button>
      </div>

      <div class="p-6 overflow-y-auto space-y-6 flex-1 bg-[#faf8f4]">
        
        <!-- INTERACTIVE PROPOSAL CARD -->
        <div class="bg-purple-50 border border-purple-200 rounded-2xl p-5 space-y-4 shadow-sm">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-extrabold text-purple-950 uppercase tracking-wider flex items-center gap-2">
              <i data-lucide="plus-circle" class="w-4 h-4 text-purple-700"></i> 💡 Propor Nova Regra ou Alteração de Estilo (#28+)
            </span>
            <button id="btn-voice-manual" onclick="toggleVoiceManualProposal()" class="px-3 py-1.5 bg-purple-700 hover:bg-purple-800 text-white rounded-lg text-xs font-extrabold flex items-center gap-1.5 transition cursor-pointer">
              <i data-lucide="mic" class="w-3.5 h-3.5"></i>
              <span id="voice-manual-btn-text">Ditar Regra por Voz</span>
            </button>
          </div>
          <textarea id="manual-proposal-input" rows="2" class="w-full bg-white border border-slate-300 rounded-xl p-3 text-xs font-semibold text-slate-900 focus:outline-none focus:border-purple-600 font-sans shadow-inner" placeholder="Ex: '#28 — 27/07/2026 · Sempre que citar valores em dólares, acrescentar a conversão aproximada em R$ entre parênteses.'"></textarea>
          <div class="flex items-center justify-between">
            <span class="text-[11px] text-slate-600 font-medium italic">As novas regras ficam salvas no sistema e incorporadas à IA.</span>
            <button onclick="saveManualProposal()" class="px-4 py-2 bg-purple-700 hover:bg-purple-800 text-white rounded-xl text-xs font-extrabold shadow transition flex items-center gap-1.5 cursor-pointer">
              <i data-lucide="save" class="w-3.5 h-3.5"></i>
              <span>Acrescentar ao Manual de Estilo</span>
            </button>
          </div>
        </div>

        <!-- DYNAMIC CUSTOM RULES SECTION -->
        <div id="manual-custom-rules-container" class="hidden space-y-3">
          <h4 class="text-xs font-mono font-extrabold uppercase text-purple-900 tracking-wider flex items-center gap-2 border-b border-purple-200 pb-2">
            <i data-lucide="sparkles" class="w-4 h-4 text-purple-700"></i> Regras Adicionadas pelo Miguel (#28+)
          </h4>
          <div id="manual-custom-rules-list" class="space-y-2">
            <!-- Rendered custom rules -->
          </div>
        </div>

        <!-- CANONICAL MANUAL CONTENT (FORMATTED & CORRECTED) -->
        <div id="manual-estilo-content" class="prose-manual text-sm space-y-4">
          <!-- Rendered Canonical Manual de Estilo -->
        </div>

      </div>
    </div>
  </div>

  <!-- MODAL DE CONFIGURAÇÕES DE API KEYS & PARÂMETROS IA (ACESSÍVEL AO MIGUEL) -->
  <div id="modal-settings" class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-slate-200 rounded-3xl max-w-2xl w-full max-h-[92vh] flex flex-col shadow-2xl overflow-hidden text-slate-900">
      
      <!-- MODAL HEADER -->
      <div class="p-5 border-b border-slate-200 flex items-center justify-between bg-slate-100">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-indigo-100 border border-indigo-300 flex items-center justify-center text-indigo-800">
            <i data-lucide="settings" class="w-6 h-6"></i>
          </div>
          <div>
            <h3 class="text-lg font-extrabold font-display text-slate-900">Configurações do Motor IA & Chaves de API</h3>
            <p class="text-xs text-slate-600 font-semibold">Gerenciamento manual de chaves API e preferências de modelos Frontier</p>
          </div>
        </div>
        <button onclick="closeSettingsModal()" class="text-slate-500 hover:text-slate-900 p-1 cursor-pointer">
          <i data-lucide="x" class="w-6 h-6"></i>
        </button>
      </div>

      <div class="p-6 overflow-y-auto space-y-5 flex-1 bg-[#faf8f4]">
        <div class="p-4 bg-indigo-50 rounded-2xl border border-indigo-200 text-xs text-indigo-950 font-semibold leading-relaxed">
          💡 <strong>Controle Total e Permanência:</strong> Caso alguma chave de API desatualize ou se você quiser personalizar os parâmetros sem precisar de mim, você pode editar e salvar manualmente todas as chaves abaixo!
        </div>

        <div class="space-y-4 font-mono text-xs">
          <div>
            <label class="block text-slate-800 font-bold mb-1">♊ Google Gemini API Key (Gemini 3.6 Ultra / Flash):</label>
            <input type="password" id="setting-key-gemini" class="w-full bg-white border border-slate-300 rounded-xl p-2.5 text-slate-900 focus:outline-none focus:border-cyan-600 font-sans shadow-inner" placeholder="sk-... ou AIzaSy...">
          </div>

          <div>
            <label class="block text-slate-800 font-bold mb-1">🤖 OpenAI API Key (GPT 5.6 / o3-Pro):</label>
            <input type="password" id="setting-key-openai" class="w-full bg-white border border-slate-300 rounded-xl p-2.5 text-slate-900 focus:outline-none focus:border-blue-600 font-sans shadow-inner" placeholder="sk-proj-...">
          </div>

          <div>
            <label class="block text-slate-800 font-bold mb-1">👑 Anthropic API Key (Claude Opus 5.0):</label>
            <input type="password" id="setting-key-anthropic" class="w-full bg-white border border-slate-300 rounded-xl p-2.5 text-slate-900 focus:outline-none focus:border-amber-600 font-sans shadow-inner" placeholder="sk-ant-api03-...">
          </div>

          <div>
            <label class="block text-slate-800 font-bold mb-1">⚡ DeepSeek API Key (DeepSeek V4/V5 Pro):</label>
            <input type="password" id="setting-key-deepseek" class="w-full bg-white border border-slate-300 rounded-xl p-2.5 text-slate-900 focus:outline-none focus:border-purple-600 font-sans shadow-inner" placeholder="sk-9335...">
          </div>

          <div>
            <label class="block text-slate-800 font-bold mb-1">🌙 Moonshot / Kimi API Key (Kimi 3.5):</label>
            <input type="password" id="setting-key-kimi" class="w-full bg-white border border-slate-300 rounded-xl p-2.5 text-slate-900 focus:outline-none focus:border-emerald-600 font-sans shadow-inner" placeholder="sk-e2j7...">
          </div>

          <div>
            <label class="block text-slate-800 font-bold mb-1">🌐 Zhipu GLM API Key (GLM 5.2):</label>
            <input type="password" id="setting-key-glm" class="w-full bg-white border border-slate-300 rounded-xl p-2.5 text-slate-900 focus:outline-none focus:border-rose-600 font-sans shadow-inner" placeholder="sk-glm-...">
          </div>
        </div>

        <div class="pt-2 flex items-center justify-between border-t border-slate-200">
          <button onclick="restoreDefaultApiKeys()" class="px-3.5 py-2 bg-slate-200 hover:bg-slate-300 text-slate-800 rounded-xl text-xs font-extrabold border border-slate-300 cursor-pointer">
            🔄 Restaurar Chaves Padrão
          </button>

          <button onclick="saveSettingsModal()" class="px-5 py-2.5 bg-indigo-700 hover:bg-indigo-800 text-white rounded-xl text-xs font-extrabold shadow flex items-center gap-2 cursor-pointer">
            <i data-lucide="check-circle" class="w-4 h-4 text-white"></i>
            <span>Salvar Configurações</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL DE ALERTA DE TOKENS PARA REVISÃO DO LIVRO INTEIRO -->
  <div id="modal-fullbook-warning" class="fixed inset-0 z-[10000] bg-slate-900/60 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-amber-300 rounded-3xl p-6 md:p-8 max-w-xl w-full text-slate-900 shadow-2xl space-y-6">
      <div class="flex items-center gap-4 border-b border-amber-200 pb-4">
        <div class="w-12 h-12 rounded-2xl bg-amber-100 border border-amber-300 flex items-center justify-center text-amber-800">
          <i data-lucide="alert-triangle" class="w-7 h-7"></i>
        </div>
        <div>
          <h3 class="text-xl font-extrabold font-display text-slate-900">⚠️ Abrir Estúdio para Revisar Livro Inteiro</h3>
          <p class="text-xs text-amber-900 font-bold">Revisão Editorial Global com IA Frontier (23 Capítulos)</p>
        </div>
      </div>

      <div class="space-y-3 text-sm text-slate-900 leading-relaxed bg-amber-50 p-5 rounded-2xl border border-amber-200">
        <p>Você solicitou abrir o Estúdio Editorial para <strong>revisar o Livro Inteiro Compilado (23 Capítulos Canônicos)</strong>.</p>
        <p class="text-xs font-mono text-slate-900 bg-white p-3 rounded-xl border border-amber-300 space-y-1 font-bold">
          • Volume Estimado: <strong>~78.500 palavras (~105.000 tokens)</strong>.<br>
          • Escopo: <strong>Manuscrito Integral Compilado em tempo real</strong>.<br>
          • Modelos Disponíveis: <strong>Gemini 3.6 Ultra / GPT 5.6 / Claude Opus 5 / DeepSeek V4</strong>.
        </p>
        <p class="text-xs text-slate-600 font-medium italic">
          💡 Nota: Ao clicar abaixo você entrará na página do estúdio. Quando disparar a reescrita lá dentro, o sistema pedirá confirmação final antes de consumir tokens.
        </p>
      </div>

      <div class="flex items-center justify-end gap-3 pt-2">
        <button onclick="closeFullBookWarningModal()" class="px-5 py-2.5 bg-slate-200 hover:bg-slate-300 text-slate-900 border border-slate-300 rounded-xl text-xs font-extrabold transition cursor-pointer">
          ❌ Cancelar
        </button>
        <button onclick="confirmFullBookAiAudit()" class="px-6 py-2.5 bg-amber-600 hover:bg-amber-700 text-white rounded-xl text-xs font-extrabold uppercase tracking-wider shadow-md transition cursor-pointer">
          🚀 Seguir para Revisar o Livro Inteiro
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL DE SINCRONIZAÇÃO GITHUB & NUVEM -->
  <div id="modal-git-sync" class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-emerald-200 rounded-3xl max-w-2xl w-full flex flex-col shadow-2xl overflow-hidden text-slate-900">
      <div class="p-5 border-b border-emerald-200 flex items-center justify-between bg-emerald-50">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-emerald-100 border border-emerald-300 flex items-center justify-center text-emerald-800">
            <i data-lucide="cloud-cog" class="w-6 h-6"></i>
          </div>
          <div>
            <h3 class="text-lg font-extrabold font-display text-slate-900">Sincronização com o GitHub & Nuvem</h3>
            <p class="text-xs text-emerald-900 font-bold">Garante permanência total das revisões no celular, iPad e computador</p>
          </div>
        </div>
        <button onclick="closeGitSyncModal()" class="text-slate-500 hover:text-slate-900 p-1 cursor-pointer">
          <i data-lucide="x" class="w-6 h-6"></i>
        </button>
      </div>

      <div class="p-6 space-y-5 text-sm text-slate-900 bg-[#faf8f4]">
        <div class="p-4 bg-emerald-50 border border-emerald-300 rounded-2xl space-y-2 text-xs">
          <div class="font-extrabold text-emerald-950 flex items-center gap-2">
            <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-700"></i>
            <span>Sincronização Ativa via Repositório:</span>
          </div>
          <p class="text-slate-800 font-medium leading-relaxed">
            As revisões gravadas no repositório GitHub (<code class="font-mono font-bold text-emerald-800">revisions.json</code> e <code class="font-mono font-bold text-emerald-800">custom_rules.json</code>) são sincronizadas automaticamente em qualquer dispositivo (iPhone, Android, iPad, Notebook) ao abrir o PWA.
          </p>
        </div>

        <div class="space-y-3">
          <h4 class="text-xs font-mono font-extrabold uppercase text-slate-600">Opções de Exportação & Backup:</h4>
          
          <button onclick="exportRevisionsBundle()" class="w-full p-3.5 bg-white hover:bg-emerald-50 border border-slate-300 rounded-xl flex items-center justify-between transition text-left group shadow-sm cursor-pointer">
            <div>
              <div class="font-bold text-slate-900 group-hover:text-emerald-900 transition flex items-center gap-2">
                <span>📥 Baixar Pacote de Revisões em JSON</span>
              </div>
              <div class="text-xs text-slate-600">Exporta todas as suas revisões e regras do Manual para backup no seu dispositivo</div>
            </div>
            <i data-lucide="download" class="w-5 h-5 text-emerald-700"></i>
          </button>

          <button onclick="forceFetchGitHubSync()" class="w-full p-3.5 bg-white hover:bg-emerald-50 border border-slate-300 rounded-xl flex items-center justify-between transition text-left group shadow-sm cursor-pointer">
            <div>
              <div class="font-bold text-slate-900 group-hover:text-emerald-900 transition flex items-center gap-2">
                <span>🔄 Forçar Re-sincronização do GitHub</span>
              </div>
              <div class="text-xs text-slate-600">Recarrega as revisões atualizadas diretamente do servidor em nuvem</div>
            </div>
            <i data-lucide="refresh-cw" class="w-5 h-5 text-emerald-700"></i>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- DATA & JAVASCRIPT LOGIC -->
  <script>
    // Embedded Volume Datasets
    const bookVol1V7 = """ + json.dumps(v7_chapters, ensure_ascii=False, indent=2) + """;
    const bookVol2V1 = """ + json.dumps(vol2_chapters, ensure_ascii=False, indent=2) + """;

    // Experimental Chapter 1 data
    const expVersionsCap1 = {
      antigravity: {
        title: "Versão 4: Antigravity",
        author: "Antigravity (Google)",
        versionTag: "AGY 1.0",
        badge: "Versão Experimental Antigravity",
        content: """ + json.dumps(exp_antigravity, ensure_ascii=False) + """
      },
      claude: {
        title: "Versão 3: Claude",
        author: "Claude",
        versionTag: "Claude 1.0",
        badge: "Versão Experimental Claude",
        content: """ + json.dumps(exp_claude, ensure_ascii=False) + """
      },
      gpt: {
        title: "Versão 2: GPT",
        author: "GPT",
        versionTag: "GPT 1.0",
        badge: "Versão Experimental GPT",
        content: """ + json.dumps(exp_gpt, ensure_ascii=False) + """
      }
    };

    const bancoLinksMarkdown = """ + json.dumps(banco_links_content, ensure_ascii=False) + """;
    const manualEstiloMarkdown = """ + json.dumps(manual_estilo_content, ensure_ascii=False) + """;

    let currentVolume = 'vol1_v7'; // 'vol1_v7', 'vol2_v1'
    let currentChapterKey = '01_estarei_vingado';
    let currentVersionKey = 'oficial';
    // Theme Mode Toggle (Modo Dia vs Modo Noite)
    function toggleThemeMode() {
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme_mode', isDark ? 'dark' : 'light');
      updateThemeUI(isDark);
    }

    function initThemeMode() {
      const savedTheme = localStorage.getItem('theme_mode');
      const isDark = savedTheme === 'dark';
      if (isDark) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      updateThemeUI(isDark);
    }

    function updateThemeUI(isDark) {
      const icon = document.getElementById('theme-toggle-icon');
      const label = document.getElementById('theme-toggle-label');
      const btn = document.getElementById('theme-toggle-btn');
      if (icon && label && btn) {
        if (isDark) {
          icon.textContent = '🌙';
          label.textContent = 'Modo Noite';
          btn.className = 'flex items-center gap-1.5 px-3.5 py-2 bg-slate-800 hover:bg-slate-700 border border-slate-600 rounded-xl text-xs font-bold text-amber-300 transition shadow-sm cursor-pointer';
        } else {
          icon.textContent = '☀️';
          label.textContent = 'Modo Dia';
          btn.className = 'flex items-center gap-1.5 px-3.5 py-2 bg-amber-50 hover:bg-amber-100 border border-amber-300 rounded-xl text-xs font-bold text-amber-900 transition shadow-sm cursor-pointer';
        }
      }
    }

    // Call initThemeMode on startup
    document.addEventListener('DOMContentLoaded', initThemeMode);


    // Speech Recognition state for AI Audit
    let voiceRecognition = null;
    let voiceIsRecording = false;
    let voiceBaseText = '';
    let voiceSecondsElapsed = 0;
    let voiceTimerInterval = null;

    // Speech Recognition state for Manual Proposals
    let voiceManualRecognition = null;
    let voiceManualIsRecording = false;
    let voiceManualBaseText = '';

    document.addEventListener('DOMContentLoaded', () => {
      switchVolume('vol1_v7');
      
      // Render static modals content if elements exist
      const bancoEl = document.getElementById('banco-links-content');
      if (bancoEl) bancoEl.innerHTML = marked.parse(bancoLinksMarkdown);
      renderCanonicalManual();
      renderCustomManualRules();

      if (window.lucide) {
        lucide.createIcons();
      }
    });

    function renderCanonicalManual() {
      // Clean typography parsing for Manual de Estilo to prevent title overlap
      let html = marked.parse(manualEstiloMarkdown);
      document.getElementById('manual-estilo-content').innerHTML = html;
    }

    function getCustomManualRules() {
      try {
        const raw = localStorage.getItem('miguel_manual_de_estilo_custom_rules');
        return raw ? JSON.parse(raw) : [];
      } catch(e) {
        return [];
      }
    }

    function saveCustomManualRules(rules) {
      localStorage.setItem('miguel_manual_de_estilo_custom_rules', JSON.stringify(rules));
      renderCustomManualRules();
    }

    function renderCustomManualRules() {
      const rules = getCustomManualRules();
      const container = document.getElementById('manual-custom-rules-container');
      const list = document.getElementById('manual-custom-rules-list');

      if (rules.length === 0) {
        container.classList.add('hidden');
        list.innerHTML = '';
        return;
      }

      container.classList.remove('hidden');
      list.innerHTML = '';

      rules.forEach((ruleText, idx) => {
        const div = document.createElement('div');
        div.className = "p-3 bg-purple-950/30 border border-purple-500/30 rounded-xl text-xs text-purple-200 flex items-start justify-between gap-3 shadow";
        div.innerHTML = `
          <div class="flex-1">
            <span class="font-mono font-bold text-purple-400">#${28 + idx}</span> — ${ruleText}
          </div>
          <button onclick="deleteCustomManualRule(${idx})" class="text-slate-500 hover:text-red-400 text-xs font-mono px-1">✕</button>
        `;
        list.appendChild(div);
      });
    }

    function saveManualProposal() {
      const input = document.getElementById('manual-proposal-input');
      const text = input.value.trim();
      if (!text) {
        alert("Por favor digite ou dite a nova regra para o Manual de Estilo.");
        return;
      }

      const rules = getCustomManualRules();
      rules.push(text);
      saveCustomManualRules(rules);

      input.value = '';
      if (voiceManualIsRecording) stopVoiceManualProposal();
      alert(`Nova regra #${27 + rules.length} adicionada com sucesso ao Manual de Estilo!`);
    }

    function deleteCustomManualRule(idx) {
      const rules = getCustomManualRules();
      rules.splice(idx, 1);
      saveCustomManualRules(rules);
    }

    function toggleVoiceManualProposal() {
      if (voiceManualIsRecording) {
        stopVoiceManualProposal();
      } else {
        startVoiceManualProposal();
      }
    }

    function startVoiceManualProposal() {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) {
        alert("O seu navegador não suporta a Web Speech API.");
        return;
      }

      const input = document.getElementById('manual-proposal-input');
      voiceManualAccumulatedText = input.value ? input.value.trim() : '';

      voiceManualRecognition = new SpeechRecognition();
      voiceManualRecognition.continuous = true;
      voiceManualRecognition.interimResults = true;
      voiceManualRecognition.lang = 'pt-BR';

      voiceManualRecognition.onstart = function() {
        voiceManualIsRecording = true;
        document.getElementById('voice-manual-btn-text').textContent = "Gravando...";
        document.getElementById('btn-voice-manual').className = "px-3 py-1.5 bg-red-600 hover:bg-red-500 text-white rounded-lg text-xs font-mono flex items-center gap-1.5 animate-pulse";
      };

      voiceManualRecognition.onresult = function(event) {
        let currentSessionTranscript = '';
        for (let i = 0; i < event.results.length; ++i) {
          currentSessionTranscript += event.results[i][0].transcript;
        }
        if (voiceManualAccumulatedText.length > 0) {
          input.value = voiceManualAccumulatedText + ' ' + currentSessionTranscript.trim();
        } else {
          input.value = currentSessionTranscript.trim();
        }
      };

      voiceManualRecognition.onerror = function(event) {
        console.warn('Voice manual error:', event.error);
      };

      voiceManualRecognition.onend = function() {
        if (voiceManualIsRecording) {
          const input = document.getElementById('manual-proposal-input');
          if (input) {
            voiceManualAccumulatedText = input.value.trim();
          }
          try { voiceManualRecognition.start(); } catch(e) {}
        }
      };

      try { voiceManualRecognition.start(); } catch(e) {}
    }

    function stopVoiceManualProposal() {
      voiceManualIsRecording = false;
      if (voiceManualRecognition) {
        try { voiceManualRecognition.stop(); } catch(e) {}
      }
      document.getElementById('voice-manual-btn-text').textContent = "Ditar Regra por Voz";
      document.getElementById('btn-voice-manual').className = "px-3 py-1.5 bg-purple-800 hover:bg-purple-700 text-purple-200 rounded-lg text-xs font-mono flex items-center gap-1.5 transition";
    }

    function getCurrentVolumeDataset() {
      return (currentVolume === 'vol2_v1') ? bookVol2V1 : bookVol1V7;
    }

    function switchVolume(volKey) {
      currentVolume = volKey;
      
      const btn1 = document.getElementById('btn-vol1-v7');
      const btn2 = document.getElementById('btn-vol2-v1');
      const titleDisplay = document.getElementById('volume-title-display');
      const badgeTag = document.getElementById('volume-badge-tag');

      if (volKey === 'vol1_v7') {
        btn1.className = "px-3.5 py-1.5 rounded-lg transition font-black bg-amber-600 hover:bg-amber-700 text-white shadow-md cursor-pointer";
        btn2.className = "px-3.5 py-1.5 rounded-lg transition font-extrabold text-slate-900 dark:text-slate-200 hover:text-emerald-800 dark:hover:text-emerald-300 hover:bg-slate-300 dark:hover:bg-slate-700 cursor-pointer";
        titleDisplay.textContent = "Vol. 1: O Foragido (Eduardo)";
        badgeTag.textContent = "Vol. 1 V8 (23 Caps)";
        badgeTag.className = "text-xs bg-amber-200 text-amber-950 border-2 border-amber-400 dark:bg-amber-400/20 dark:text-amber-300 dark:border-amber-400/40 px-2.5 py-0.5 rounded-md font-mono font-black shadow-sm";
        currentChapterKey = '01_estarei_vingado';
      } else {
        btn2.className = "px-3.5 py-1.5 rounded-lg transition font-black bg-emerald-600 hover:bg-emerald-700 text-white shadow-md cursor-pointer";
        btn1.className = "px-3.5 py-1.5 rounded-lg transition font-extrabold text-slate-900 dark:text-slate-200 hover:text-amber-800 dark:hover:text-amber-300 hover:bg-slate-300 dark:hover:bg-slate-700 cursor-pointer";
        titleDisplay.textContent = "Vol. 2: O Malandro (Flávio)";
        badgeTag.textContent = "Vol. 2 (20 Caps Planejados)";
        badgeTag.className = "text-xs bg-emerald-200 text-emerald-950 border-2 border-emerald-400 dark:bg-emerald-400/20 dark:text-emerald-300 dark:border-emerald-400/40 px-2.5 py-0.5 rounded-md font-mono font-black shadow-sm";
        currentChapterKey = 'arquitetura_geral';
      }

      currentVersionKey = 'oficial';
      initChapterSelect();
      loadChapter(currentChapterKey);
    }

    function initChapterSelect() {
      const select = document.getElementById('chapter-select');
      if (!select) return;
      select.innerHTML = '';
      
      const dataset = getCurrentVolumeDataset();
      const keys = Object.keys(dataset);

      keys.forEach(k => {
        const item = dataset[k];
        const opt = document.createElement('option');
        opt.value = k;
        
        if (k === '00_frontmatter') {
          opt.textContent = `📌 00 — Roteiro do Livro (Visão Geral & Sinopses)`;
        } else if (k === 'arquitetura_geral') {
          opt.textContent = `🏛️ Arquitetura Geral — Vol. 2: O Malandro`;
        } else {
          const numMatch = k.match(/^\d+/);
          const numStr = numMatch ? numMatch[0] : '';
          const cleanTitle = (item.title || '').replace(/^#\s+/, '').replace(/^CAPÍTULO\s+\d+\s*[-:—–]?\s*/i, '').replace(/^[—–-]+\s*/, '');
          opt.textContent = numStr ? `${numStr} — ${cleanTitle}` : item.title;
        }

        if (k === currentChapterKey) opt.selected = true;
        select.appendChild(opt);
      });
    }

    function backToHomeSumario() {
      selectChapter('00_frontmatter');
    }

    function selectChapter(key) {
      currentChapterKey = key;
      if (key === 'full_book') {
        currentVersionKey = 'oficial';
        loadChapter('full_book');
        return;
      }
      const revs = getSavedRevisions(key);
      const revKeys = Object.keys(revs);
      if (revKeys.length > 0) {
        currentVersionKey = revKeys[revKeys.length - 1];
      } else {
        currentVersionKey = 'oficial';
      }
      loadChapter(key);
    }

    function navigateChapter(delta) {
      const dataset = getCurrentVolumeDataset();
      const keys = Object.keys(dataset);
      const currentIndex = keys.indexOf(currentChapterKey);
      if (currentIndex === -1) {
        if (keys.length > 0) selectChapter(keys[0]);
        return;
      }
      const newIndex = currentIndex + delta;
      if (newIndex >= 0 && newIndex < keys.length) {
        const newKey = keys[newIndex];
        document.getElementById('chapter-select').value = newKey;
        selectChapter(newKey);
      }
    }

    function getSavedRevisions(chapKey) {
      try {
        const raw = localStorage.getItem('miguel_book_revisions_' + chapKey);
        return raw ? JSON.parse(raw) : {};
      } catch (e) {
        return {};
      }
    }

    function loadChapter(chapKey) {
      const prodContainer = document.getElementById('prod-block-container');
      if (chapKey === 'full_book') {
        renderVersionTabs();
        renderMetrics();
        renderSingleView();
        if (prodContainer) prodContainer.classList.add('hidden');
        if (window.lucide) lucide.createIcons();
        return;
      }

      const dataset = getCurrentVolumeDataset();
      const chapter = dataset[chapKey];
      if (!chapter) return;

      renderVersionTabs();
      renderMetrics();
      renderSingleView();
      updateCompareSelectOptions();
      
      // Production Block
      const prodContent = document.getElementById('prod-block-content');
      if (chapter.prodBlock && chapter.prodBlock.trim().length > 0) {
        if (prodContainer) prodContainer.classList.remove('hidden');
        if (prodContent) prodContent.innerHTML = marked.parse(chapter.prodBlock);
      } else {
        if (prodContainer) prodContainer.classList.add('hidden');
      }

      if (window.lucide) lucide.createIcons();
    }

    function toggleProdBlock() {
      const prodContent = document.getElementById('prod-block-content');
      const chevron = document.getElementById('prod-block-chevron');
      if (prodContent.classList.contains('hidden')) {
        prodContent.classList.remove('hidden');
        chevron.style.transform = 'rotate(180deg)';
      } else {
        prodContent.classList.add('hidden');
        chevron.style.transform = 'rotate(0deg)';
      }
    }

    function calculateMetrics(text) {
      if (!text) return { words: 0, sentences: 0 };
      const clean = text.replace(/#+\s+/g, '').replace(/[*_>#-]/g, '');
      const words = clean.trim().split(/\s+/).filter(Boolean).length;
      const sentences = clean.split(/[.!?]+/).filter(s => s.trim().length > 0).length;
      return { words, sentences };
    }

    function getCompiledFullBookData() {
      const dataset = getCurrentVolumeDataset();
      const keys = Object.keys(dataset);
      let compiledText = `# FILHOS DA IMPUNIDADE — ${currentVolume === 'vol1_v7' ? 'VOLUME 1 (MANUSCRITO INTEGRAL COMPILADO — 23 CAPÍTULOS)' : 'VOLUME 2 (O MALANDRO — ARQUITETURA E CAPÍTULOS)'}\n\n`;
      compiledText += `*Manuscrito compilado em tempo real unificando todas as versões canônicas ativas.* \n\n---\n\n`;

      let totalWords = 0;
      keys.forEach((k, idx) => {
        const ch = dataset[k];
        let chContent = ch.mainContent || '';
        try {
          const storedCanonicalKey = localStorage.getItem('miguel_book_canonical_' + k);
          if (storedCanonicalKey && storedCanonicalKey !== 'oficial') {
            const revs = getSavedRevisions(k);
            if (revs[storedCanonicalKey] && revs[storedCanonicalKey].content) {
              chContent = revs[storedCanonicalKey].content;
            }
          }
        } catch(e) {}

        const words = chContent.trim() ? chContent.trim().split(/\s+/).filter(Boolean).length : 0;
        totalWords += words;

        compiledText += `\n\n# CAPÍTULO ${String(idx + 1).padStart(2, '0')} — ${ch.title.replace(/^#\s+/, '')}\n\n`;
        compiledText += chContent + `\n\n---\n`;
      });

      return {
        key: 'full_book',
        title: currentVolume === 'vol1_v7' ? 'Livro Inteiro Compilado (23 Capítulos Canônicos)' : 'Livro Inteiro Compilado (Vol. 2)',
        versionTag: 'Manuscrito Compilado Canônico',
        mainContent: compiledText,
        totalWords: totalWords,
        totalChapters: keys.length,
        author: 'Kimi (ZCode) & Miguel'
      };
    }

    function getCleanEngineSlug(engineKey) {
      const slugMap = {
        gemini: 'gemini_3.6',
        gpt56: 'gpt_5.6',
        opus5: 'claude_opus_5',
        deepseek: 'deepseek_v4',
        kimi35: 'kimi_3.5',
        glm52: 'glm_5.2'
      };
      return slugMap[engineKey] || 'gemini_3.6';
    }

    function downloadFullBook() {
      const fullBookData = getCompiledFullBookData();
      const dateFormatted = new Date().toISOString().slice(0, 10).replace(/-/g, '_');
      const blob = new Blob([fullBookData.mainContent], { type: 'text/markdown;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `R1_Filhos_da_Impunidade_${currentVolume === 'vol1_v7' ? 'Vol_1_23Caps' : 'Vol_2'}_${dateFormatted}_compilado.md`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function downloadCurrentChapter() {
      if (currentChapterKey === 'full_book') {
        downloadFullBook();
        return;
      }
      const data = getActiveVersionData();
      const dateObj = new Date();
      const dateFormatted = dateObj.toISOString().slice(0, 10).replace(/-/g, '_');
      const numMatch = currentChapterKey.match(/\d+/);
      const chapNum = numMatch ? numMatch[0].padStart(2, '0') : '01';
      
      let rPrefix = 'R1';
      if (currentVersionKey && currentVersionKey.startsWith('R')) {
        rPrefix = currentVersionKey.split(' ')[0];
      } else if (currentVersionKey === 'oficial') {
        rPrefix = 'R0';
      }
      
      const engineSlug = data.engineSlug || getCleanEngineSlug(currentSelectedEngine);
      const filename = `${rPrefix}_capitulo_${chapNum}_${dateFormatted}_${engineSlug}.md`;

      const blob = new Blob([data.content || ''], { type: 'text/markdown;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function compileAndReadFullBook() {
      currentChapterKey = 'full_book';
      currentVersionKey = 'oficial';
      const sel = document.getElementById('chapter-select');
      if (sel) sel.value = 'full_book';
      initChapterSelect();
      renderVersionTabs();
      renderMetrics();
      renderSingleView();
      window.scrollTo(0, 0);
    }

    function triggerAiAuditWithTokenWarning() {
      if (currentChapterKey === 'full_book') {
        const warnModal = document.getElementById('modal-fullbook-warning');
        if (warnModal) warnModal.classList.remove('hidden');
      } else {
        openAiAuditModal();
      }
    }

    function confirmFullBookAiAudit() {
      const warnModal = document.getElementById('modal-fullbook-warning');
      if (warnModal) warnModal.classList.add('hidden');
      openAiAuditModal();
    }

    function closeFullBookWarningModal() {
      const warnModal = document.getElementById('modal-fullbook-warning');
      if (warnModal) warnModal.classList.add('hidden');
    }

    function renderMetrics() {
      const dataset = getCurrentVolumeDataset();
      const setEl = (id, val) => { const el = document.getElementById(id); if (el) el.textContent = val; };
      if (currentChapterKey === 'full_book') {
        const fullData = getCompiledFullBookData();
        setEl('metric-author', fullData.author);
        setEl('metric-version-tag', fullData.versionTag);
        setEl('metric-words', fullData.totalWords.toLocaleString('pt-BR'));
        setEl('metric-sentences', `${fullData.totalChapters} Caps`);
        setEl('metric-badge', `Compilado Canônico (${fullData.totalChapters} Capítulos)`);
        return;
      }
      const activeData = getActiveVersionData();
      const metrics = calculateMetrics(activeData.content);
      
      setEl('metric-author', activeData.author || 'Kimi (ZCode) & Miguel');
      setEl('metric-version-tag', activeData.versionTag || dataset[currentChapterKey].versionTag);
      setEl('metric-words', metrics.words.toLocaleString('pt-BR'));
      setEl('metric-sentences', metrics.sentences.toLocaleString('pt-BR'));
      setEl('metric-badge', activeData.badge || 'Oficial Protegida 🔒');
    }

    function getActiveVersionData() {
      const dataset = getCurrentVolumeDataset();
      const chapter = dataset[currentChapterKey];
      if (currentVersionKey === 'oficial') {
        return {
          title: chapter.title,
          author: 'Kimi (ZCode) & Miguel',
          versionTag: chapter.versionTag,
          badge: chapter.badge || `${chapter.title} · Versão ${chapter.versionTag}`,
          content: chapter.mainContent,
          isSkeleton: chapter.isSkeleton,
          question: chapter.question,
          sources: chapter.sources,
          part: chapter.part
        };
      }
      
      if (currentVolume === 'vol1_v7' && currentChapterKey === '01_estarei_vingado' && expVersionsCap1[currentVersionKey]) {
        return expVersionsCap1[currentVersionKey];
      }

      const revs = getSavedRevisions(currentChapterKey);
      if (revs[currentVersionKey]) {
        return revs[currentVersionKey];
      }

      return {
        title: chapter.title,
        author: 'Kimi (ZCode) & Miguel',
        versionTag: chapter.versionTag,
        badge: chapter.badge || `${chapter.title} · Versão ${chapter.versionTag}`,
        content: chapter.mainContent,
        isSkeleton: chapter.isSkeleton,
        question: chapter.question,
        sources: chapter.sources,
        part: chapter.part
      };
    }

    function getCanonicalVersionKey(chapKey) {
      return localStorage.getItem('miguel_book_canonical_' + chapKey) || 'oficial';
    }

    function setCanonicalVersion(vKey) {
      localStorage.setItem('miguel_book_canonical_' + currentChapterKey, vKey);
      renderVersionTabs();
      renderMetrics();
      renderSingleView();
      alert(`👑 A versão "${vKey}" foi definida como a VERSÃO CANÔNICA OFICIAL do capítulo! Nenhuma outra versão foi apagada.`);
    }

    function renderVersionTabs() {
      const container = document.getElementById('single-version-tabs');
      if (!container) return;
      container.innerHTML = '';

      if (currentChapterKey === 'full_book') {
        const fullData = getCompiledFullBookData();
        container.innerHTML = `
          <div class="flex items-center gap-2">
            <span class="bg-amber-600 text-white font-mono font-black px-3 py-1.5 rounded-xl text-xs shadow-sm">
              📚 Manuscrito Integral Compilado (${fullData.totalChapters} Capítulos)
            </span>
          </div>
        `;
        return;
      }

      if (currentChapterKey === '00_frontmatter') {
        container.innerHTML = `
          <div class="flex items-center gap-2">
            <span class="bg-slate-800 text-amber-400 font-mono font-black px-3 py-1.5 rounded-xl text-xs shadow-sm">
              📌 Roteiro Estrutural & Sinopses
            </span>
          </div>
        `;
        return;
      }

      const dataset = getCurrentVolumeDataset();
      const chapter = dataset[currentChapterKey];
      if (!chapter) return;

      const canonicalKey = getCanonicalVersionKey(currentChapterKey);
      const isCurrentCanonical = (currentVersionKey === canonicalKey);

      // Collect all versions for this chapter
      const revs = getSavedRevisions(currentChapterKey);
      const allVersionKeys = [];

      // Add R# versions in reverse chronological order (newest first: R5, R4, R3...)
      const rKeys = Object.keys(revs).reverse();
      rKeys.forEach(rk => allVersionKeys.push({ key: rk, label: revs[rk].versionTag || rk, type: 'revision' }));

      // Add experimental versions if cap 1
      if (currentVolume === 'vol1_v7' && currentChapterKey === '01_estarei_vingado') {
        ['antigravity', 'claude', 'gpt'].forEach(k => {
          allVersionKeys.push({ key: k, label: expVersionsCap1[k].title, type: 'exp' });
        });
      }

      // Add base official version
      allVersionKeys.push({ key: 'oficial', label: `Oficial (${chapter.versionTag})`, type: 'official' });

      // Active label for main dropdown button
      let activeLabel = 'Oficial';
      allVersionKeys.forEach(v => {
        if (v.key === currentVersionKey) activeLabel = v.label;
      });

      // 1. VERTICAL DROPDOWN BUTTON (Escadinha Vertical)
      const dropdownWrapper = document.createElement('div');
      dropdownWrapper.className = 'relative inline-block text-left';

      const isCanonBadge = isCurrentCanonical ? '👑 Canônica: ' : '📌 Versão: ';
      
      dropdownWrapper.innerHTML = `
        <button id="btn-version-dropdown-toggle" onclick="toggleVersionDropdown()" class="flex items-center gap-2 px-4 py-2.5 bg-white hover:bg-slate-50 border-2 border-purple-400 text-purple-950 font-extrabold rounded-xl text-xs shadow-sm transition cursor-pointer">
          <i data-lucide="${isCurrentCanonical ? 'crown' : 'layers'}" class="w-4 h-4 ${isCurrentCanonical ? 'text-amber-600' : 'text-purple-700'}"></i>
          <span>${isCanonBadge}${activeLabel}</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-purple-700"></i>
        </button>

        <!-- VERTICAL DROPDOWN MENU (ESCADA REVERSA DE CIMA PRA BAIXO) -->
        <div id="version-dropdown-menu" class="hidden absolute left-0 mt-2 w-64 rounded-2xl bg-white border-2 border-purple-200 shadow-2xl z-50 overflow-hidden py-1 max-h-80 overflow-y-auto">
          <div class="px-3.5 py-2 border-b border-slate-200 text-[10px] uppercase font-mono font-bold text-slate-500 tracking-wider flex items-center justify-between bg-purple-50">
            <span>📜 Histórico de Versões</span>
            <span class="text-amber-800 font-mono font-bold">👑 = Canônica</span>
          </div>
          <div id="version-dropdown-list" class="divide-y divide-slate-100"></div>
        </div>
      `;

      container.appendChild(dropdownWrapper);

      // Populate vertical dropdown items
      const listEl = dropdownWrapper.querySelector('#version-dropdown-list');
      allVersionKeys.forEach(v => {
        const itemBtn = document.createElement('button');
        const isSelected = (v.key === currentVersionKey);
        const isCanonical = (v.key === canonicalKey);

        itemBtn.onclick = () => {
          switchVersion(v.key);
          closeVersionDropdown();
        };

        itemBtn.className = `w-full text-left px-4 py-2.5 text-xs font-semibold flex items-center justify-between transition cursor-pointer ${
          isSelected 
            ? 'bg-purple-100 text-purple-950 font-extrabold dark:bg-purple-900/60 dark:text-purple-200' 
            : 'text-slate-800 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'
        }`;

        itemBtn.innerHTML = `
          <div class="flex items-center gap-2">
            <i data-lucide="${isCanonical ? 'crown' : 'file-text'}" class="w-4 h-4 ${isCanonical ? 'text-amber-600 dark:text-amber-400' : 'text-slate-400'}"></i>
            <span>${v.label}</span>
          </div>
          ${isCanonical ? '<span class="bg-amber-100 text-amber-900 dark:bg-amber-500/20 dark:text-amber-300 border border-amber-300 dark:border-amber-500/40 px-1.5 py-0.5 rounded text-[10px] font-mono font-bold">Canônica</span>' : ''}
        `;

        listEl.appendChild(itemBtn);
      });

      // 2. BUTTON: TORNAR CANÔNICA (Make Canonical)
      const canonicalBtn = document.createElement('button');
      if (isCurrentCanonical) {
        canonicalBtn.className = "flex items-center gap-1.5 px-3.5 py-2 bg-amber-100 text-amber-950 border border-amber-300 dark:bg-amber-500/20 dark:text-amber-300 dark:border-amber-500/50 rounded-xl text-xs font-extrabold shadow cursor-default";
        canonicalBtn.innerHTML = `<i data-lucide="crown" class="w-4 h-4 text-amber-600 dark:text-amber-400"></i> <span>👑 Versão Canônica Atual</span>`;
      } else {
        canonicalBtn.onclick = () => setCanonicalVersion(currentVersionKey);
        canonicalBtn.className = "flex items-center gap-1.5 px-3.5 py-2 bg-amber-600 hover:bg-amber-700 text-white border border-amber-500 rounded-xl text-xs font-extrabold shadow transition cursor-pointer";
        canonicalBtn.innerHTML = `<i data-lucide="crown" class="w-4 h-4 text-white"></i> <span>Tornar Canônica</span>`;
      }
      container.appendChild(canonicalBtn);

      if (window.lucide) lucide.createIcons();
    }

    function toggleVersionDropdown() {
      const menu = document.getElementById('version-dropdown-menu');
      if (menu) menu.classList.toggle('hidden');
    }

    function closeVersionDropdown() {
      const menu = document.getElementById('version-dropdown-menu');
      if (menu) menu.classList.add('hidden');
    }

    function switchVersion(vKey) {
      currentVersionKey = vKey;
      renderVersionTabs();
      renderMetrics();
      renderSingleView();
      if (currentViewMode === 'compare') updateCompare();
    }

    function saveRoteiroObs() {
      const area = document.getElementById('roteiro-obs-textarea');
      if (area) {
        localStorage.setItem('miguel_roteiro_observacoes', area.value);
        alert('✅ Anotações do roteiro salvas com sucesso!');
      }
    }

    function renderRoteiroDoLivro() {
      const fullData = getCompiledFullBookData();
      const dataset = getCurrentVolumeDataset();
      const keys = Object.keys(dataset).filter(k => k !== '00_frontmatter');

      let chapterCards = keys.map((k, idx) => {
        const item = dataset[k];
        const cleanTitle = (item.title || '').replace(/^#\s+/, '').replace(/^CAPÍTULO\s+\d+\s*[-:]?\s*/i, '');
        const rawText = item.mainContent || '';
        const cleanLines = rawText.split(String.fromCharCode(10)).filter(l => l.trim().length > 0 && !l.startsWith('#') && !l.startsWith('---'));
        const snippet = cleanLines.length > 0 ? cleanLines.slice(0, 2).join(' ').substring(0, 160) + '...' : 'Capítulo canônico em produção...';

        return `
          <div class="bg-white dark:bg-slate-900 border-2 border-slate-200 dark:border-slate-800 rounded-2xl p-5 shadow-sm hover:border-amber-400 dark:hover:border-amber-500 transition space-y-3 flex flex-col justify-between">
            <div class="space-y-2">
              <div class="flex items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-800 pb-2.5">
                <span class="text-xs font-mono font-black bg-amber-100 text-amber-950 dark:bg-amber-900/40 dark:text-amber-300 px-2.5 py-1 rounded-lg border border-amber-200 dark:border-amber-800">
                  Capítulo ${String(idx + 1).padStart(2, '0')}
                </span>
                <span class="text-[11px] font-mono font-bold text-emerald-800 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/40 px-2 py-0.5 rounded border border-emerald-200 dark:border-emerald-800">Canônico V7</span>
              </div>
              <h4 class="text-base font-black font-display text-slate-900 dark:text-slate-100 leading-snug">${cleanTitle}</h4>
              <p class="text-xs text-slate-700 dark:text-slate-300 font-sans leading-relaxed italic">${snippet}</p>
            </div>

            <div class="pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between gap-2">
              <button onclick="selectChapter('${k}')" class="px-3.5 py-1.5 bg-slate-800 dark:bg-slate-700 hover:bg-amber-600 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow cursor-pointer">
                <i data-lucide="book-open" class="w-3.5 h-3.5 text-amber-400"></i>
                <span>📖 Ler Capítulo ${String(idx + 1).padStart(2, '0')}</span>
              </button>
              <button onclick="downloadCurrentChapter('${k}')" title="Baixar .md" class="p-2 text-slate-500 hover:text-emerald-600 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition cursor-pointer">
                <i data-lucide="download" class="w-4 h-4"></i>
              </button>
            </div>
          </div>
        `;
      }).join('');

      const savedObs = localStorage.getItem('miguel_roteiro_observacoes') || '';

      return `
        <!-- HEADER DO ROTEIRO DO LIVRO -->
        <div class="bg-gradient-to-r from-slate-900 to-amber-950 text-white rounded-3xl p-6 md:p-8 mb-8 shadow-xl border-2 border-amber-500/40 space-y-4">
          <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div>
              <div class="flex items-center gap-2 mb-2">
                <span class="bg-amber-500 text-slate-950 text-xs font-mono font-black px-3 py-1 rounded-md uppercase tracking-wider shadow">Roteiro Canônico</span>
                <span class="text-xs font-mono text-amber-200 font-extrabold">${keys.length} Capítulos Canônicos • ~${fullData.totalWords.toLocaleString()} Palavras</span>
              </div>
              <h2 class="text-2xl md:text-3xl font-black font-display tracking-tight text-white">📌 Roteiro Estrutural & Sinopses do Livro</h2>
              <p class="text-sm text-amber-100/90 mt-1 font-sans">Guia do Foragido: Navegação organizada por todos os 23 capítulos, sinopses e observações de apuração.</p>
            </div>
            <div class="flex flex-wrap gap-2.5 shrink-0">
              <button onclick="compileAndReadFullBook()" class="px-5 py-2.5 bg-amber-500 hover:bg-amber-600 text-slate-950 rounded-xl text-xs font-black transition shadow-md flex items-center gap-2 cursor-pointer">
                <i data-lucide="book-open" class="w-4 h-4 text-slate-950"></i>
                <span>📚 Ler / Compilar Livro Inteiro</span>
              </button>
              <button onclick="downloadFullBook()" class="px-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-white border border-slate-600 rounded-xl text-xs font-bold transition flex items-center gap-2 cursor-pointer">
                <i data-lucide="download" class="w-4 h-4"></i>
                <span>Baixar Roteiro (.md)</span>
              </button>
            </div>
          </div>
        </div>

        <!-- QUADRO INTERATIVO DE OBSERVAÇÕES DO ROTEIRO -->
        <div class="bg-white dark:bg-slate-900 border-2 border-amber-300 dark:border-amber-700/60 rounded-3xl p-6 mb-8 shadow-md space-y-4">
          <div class="flex items-center justify-between border-b border-amber-200 dark:border-slate-800 pb-3">
            <div class="flex items-center gap-2">
              <i data-lucide="notebook-pen" class="w-5 h-5 text-amber-600 dark:text-amber-400"></i>
              <h3 class="text-base font-black font-display text-slate-900 dark:text-slate-100">📝 Anotações & Observações do Roteiro (Miguel)</h3>
            </div>
            <button onclick="saveRoteiroObs()" class="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-black transition flex items-center gap-1.5 shadow cursor-pointer">
              <i data-lucide="save" class="w-3.5 h-3.5"></i>
              <span>Salvar Anotações</span>
            </button>
          </div>
          <textarea id="roteiro-obs-textarea" rows="3" placeholder="Digite aqui suas observações sobre o roteiro, novas ideias para capítulos ou orientações para a IA..." class="w-full bg-amber-50/50 dark:bg-slate-950 border border-slate-300 dark:border-slate-700 rounded-xl p-3.5 text-xs font-mono font-bold text-slate-900 dark:text-slate-100 focus:outline-none focus:border-amber-500 leading-relaxed">${savedObs}</textarea>
        </div>

        <!-- GRID DE SINOPSES DOS CAPÍTULOS -->
        <div class="space-y-4">
          <h3 class="text-lg font-black font-display text-slate-900 dark:text-slate-100 flex items-center gap-2">
            <i data-lucide="list" class="w-5 h-5 text-amber-600"></i>
            <span>Mapa Geral dos 23 Capítulos Canônicos</span>
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            ${chapterCards}
          </div>
        </div>
      `;
    }

    function renderSingleView() {
      const container = document.getElementById('reader-content');
      if (!container) return;

      if (currentChapterKey === 'full_book') {
        const fullData = getCompiledFullBookData();
        container.innerHTML = `
          <div class="bg-gradient-to-r from-amber-600 to-amber-800 text-white rounded-3xl p-6 mb-8 flex flex-col md:flex-row items-center justify-between gap-4 shadow-xl">
            <div>
              <div class="flex items-center gap-2 mb-1.5">
                <span class="bg-amber-300 text-amber-950 text-xs font-mono font-black px-2.5 py-0.5 rounded uppercase shadow-sm">Compilado Canônico</span>
                <span class="text-xs font-mono text-amber-100 font-bold">${fullData.totalChapters} Capítulos · ~${fullData.totalWords.toLocaleString()} palavras</span>
              </div>
              <h2 class="text-xl md:text-2xl font-black font-display tracking-tight text-white">${fullData.title}</h2>
              <p class="text-xs text-amber-100 mt-1 font-sans">Compilação dinâmica de todas as 23 versões canônicas ativas em um único manuscrito contínuo.</p>
            </div>
            <div class="flex flex-wrap items-center gap-2.5 shrink-0">
              <button onclick="downloadFullBook()" class="px-4 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-black transition flex items-center gap-2 shadow-md cursor-pointer">
                <i data-lucide="download" class="w-4 h-4"></i>
                <span>📥 Baixar Livro Inteiro (.md)</span>
              </button>
              <button onclick="compileAndReadFullBook()" class="px-4 py-2.5 bg-white hover:bg-amber-50 text-amber-950 rounded-xl text-xs font-black transition flex items-center gap-2 shadow-md cursor-pointer">
                <i data-lucide="refresh-cw" class="w-4 h-4 text-amber-700"></i>
                <span>⚡ Atualizar Compilação</span>
              </button>
              <button onclick="triggerAiAuditWithTokenWarning()" class="px-4 py-2.5 bg-amber-950/80 hover:bg-amber-950 text-white border border-amber-400/40 rounded-xl text-xs font-bold transition flex items-center gap-2 shadow-md cursor-pointer">
                <i data-lucide="sparkles" class="w-4 h-4 text-amber-300"></i>
                <span>🤖 Revisar com IA</span>
              </button>
            </div>
          </div>
          <div class="prose-book">
            ${marked.parse(fullData.mainContent)}
          </div>
        `;
        if (window.lucide) lucide.createIcons();
        return;
      }

      if (currentChapterKey === '00_frontmatter') {
        container.innerHTML = renderRoteiroDoLivro();
        if (window.lucide) lucide.createIcons();
        return;
      }

      const data = getActiveVersionData();

      if (data.isSkeleton) {
        container.innerHTML = `
          <div class="glass-panel border border-emerald-500/40 rounded-3xl p-8 space-y-6">
            <div class="flex items-center justify-between border-b border-slate-200 pb-4">
              <span class="text-xs uppercase font-mono font-bold text-emerald-600 tracking-wider">Volume 2: O Malandro (Flávio)</span>
              <span class="bg-emerald-100 text-emerald-800 border border-emerald-300 px-3 py-1 rounded-full text-xs font-mono font-bold">Esqueleto Editorial 📌</span>
            </div>
            <h2 class="text-2xl font-bold font-display text-slate-900 tracking-tight">${data.title}</h2>
            <div class="inline-block text-xs font-mono text-emerald-800 font-semibold bg-emerald-50 px-3.5 py-1.5 rounded-xl border border-emerald-200">${data.part}</div>
            
            <div class="bg-white p-6 rounded-2xl border border-slate-200 space-y-3 shadow-sm">
              <h4 class="text-xs uppercase font-mono text-slate-500 font-bold">❓ Pergunta Central do Capítulo:</h4>
              <p class="text-lg font-serif italic text-amber-900 leading-relaxed">"${data.question}"</p>
            </div>

            <div class="bg-white p-6 rounded-2xl border border-slate-200 space-y-3 shadow-sm">
              <h4 class="text-xs uppercase font-mono text-slate-500 font-bold">📚 Fontes-base Mapeadas no Acervo:</h4>
              <p class="text-sm font-mono text-slate-700">${data.sources}</p>
            </div>

            <div class="p-4 bg-amber-50 rounded-2xl border border-amber-200 text-xs text-amber-900 leading-relaxed">
              💡 **Status de Produção:** Estrutura canônica canonizada em Kimi K3/ARQUITETURA_VOL2_O_MALANDRO.md. O texto do manuscrito está em redação para o próximo ciclo de entrega.
            </div>
          </div>
        `;
      } else {
        let htmlContent = marked.parse(data.content || '');
        
        const topChapterHeader = `
          <div class="flex flex-wrap items-center justify-between gap-3 pb-4 mb-6 border-b border-slate-200 dark:border-slate-800">
            <div class="flex items-center gap-2">
              <span class="text-xs font-mono font-black text-amber-900 dark:text-amber-300 bg-amber-100 dark:bg-amber-900/40 px-2.5 py-1 rounded-lg border border-amber-200 dark:border-amber-800">Capítulo ${currentChapterKey}</span>
              <span class="text-xs font-mono text-slate-600 dark:text-slate-400 font-bold">${data.versionTag || 'Canônico'}</span>
            </div>
            <button onclick="downloadCurrentChapter()" class="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-black transition flex items-center gap-2 shadow-sm cursor-pointer">
              <i data-lucide="download" class="w-4 h-4"></i>
              <span>📥 Baixar este Capítulo (.md)</span>
            </button>
          </div>
        `;
        htmlContent = topChapterHeader + htmlContent;

        container.innerHTML = htmlContent;
      }
      if (window.lucide) lucide.createIcons();
    }

    function setMode(mode) {
      currentViewMode = mode;
      const btnSingle = document.getElementById('btn-mode-single');
      const btnCompare = document.getElementById('btn-mode-compare');
      const singleTabs = document.getElementById('single-version-tabs');
      const compareTabs = document.getElementById('compare-version-tabs');
      const singleContainer = document.getElementById('single-view-container');
      const compareContainer = document.getElementById('compare-view-container');

      if (mode === 'single') {
        btnSingle.className = "flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-extrabold transition-all bg-amber-600 text-white shadow-sm font-sans cursor-pointer";
        btnCompare.className = "flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-bold transition-all text-slate-700 hover:text-slate-900 hover:bg-slate-200 dark:text-slate-300 dark:hover:text-white dark:hover:bg-slate-800 font-sans cursor-pointer";
        singleTabs.classList.remove('hidden');
        compareTabs.classList.add('hidden');
        singleContainer.classList.remove('hidden');
        compareContainer.classList.add('hidden');
      } else {
        btnCompare.className = "flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-extrabold transition-all bg-amber-600 text-white shadow-sm font-sans cursor-pointer";
        btnSingle.className = "flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-bold transition-all text-slate-700 hover:text-slate-900 hover:bg-slate-200 dark:text-slate-300 dark:hover:text-white dark:hover:bg-slate-800 font-sans cursor-pointer";
        singleTabs.classList.add('hidden');
        compareTabs.classList.remove('hidden');
        singleContainer.classList.add('hidden');
        compareContainer.classList.remove('hidden');
        updateCompare();
      }
    }

    function updateCompareSelectOptions() {
      const leftSelect = document.getElementById('select-left-version');
      const rightSelect = document.getElementById('select-right-version');
      
      leftSelect.innerHTML = '';
      rightSelect.innerHTML = '';

      const dataset = getCurrentVolumeDataset();
      const chapter = dataset[currentChapterKey];

      const options = [
        { key: 'oficial', label: `🔒 Oficial (${chapter.versionTag})` }
      ];

      if (currentVolume === 'vol1_v7' && currentChapterKey === '01_estarei_vingado') {
        options.push(
          { key: 'antigravity', label: 'Versão 4: Antigravity' },
          { key: 'claude', label: 'Versão 3: Claude' },
          { key: 'gpt', label: 'Versão 2: GPT' }
        );
      }

      const revs = getSavedRevisions(currentChapterKey);
      Object.keys(revs).forEach(rKey => {
        options.push({ key: rKey, label: revs[rKey].versionTag || rKey });
      });

      options.forEach(opt => {
        const elLeft = document.createElement('option');
        elLeft.value = opt.key;
        elLeft.textContent = opt.label;
        leftSelect.appendChild(elLeft);

        const elRight = document.createElement('option');
        elRight.value = opt.key;
        elRight.textContent = opt.label;
        rightSelect.appendChild(elRight);
      });

      leftSelect.value = 'oficial';
      rightSelect.value = options.length > 1 ? options[1].key : 'oficial';
    }

    function updateCompare() {
      const leftKey = document.getElementById('select-left-version').value;
      const rightKey = document.getElementById('select-right-version').value;

      const getVal = (k) => {
        if (k === 'oficial') {
          const dataset = getCurrentVolumeDataset();
          const ch = dataset[currentChapterKey];
          return { title: '🔒 Oficial', badge: ch.versionTag, content: ch.mainContent, isSkeleton: ch.isSkeleton, question: ch.question };
        }
        if (currentVolume === 'vol1_v7' && currentChapterKey === '01_estarei_vingado' && expVersionsCap1[k]) {
          return expVersionsCap1[k];
        }
        const revs = getSavedRevisions(currentChapterKey);
        if (revs[k]) return revs[k];
        return { title: k, badge: 'Revisão', content: '' };
      };

      const leftData = getVal(leftKey);
      const rightData = getVal(rightKey);

      document.getElementById('compare-left-title').textContent = leftData.title;
      document.getElementById('compare-left-badge').textContent = leftData.badge || leftData.versionTag;
      document.getElementById('compare-left-content').innerHTML = leftData.isSkeleton 
        ? `<p class="italic text-amber-200">"${leftData.question}"</p>` 
        : marked.parse(leftData.content || '');

      document.getElementById('compare-right-title').textContent = rightData.title;
      document.getElementById('compare-right-badge').textContent = rightData.badge || rightData.versionTag;
      document.getElementById('compare-right-content').innerHTML = rightData.isSkeleton 
        ? `<p class="italic text-amber-200">"${rightData.question}"</p>` 
        : marked.parse(rightData.content || '');
    }

    // Modal controls
    function openManualModal() { document.getElementById('modal-manual').classList.remove('hidden'); }
    function closeManualModal() {
      if (voiceManualIsRecording) stopVoiceManualProposal();
      document.getElementById('modal-manual').classList.add('hidden');
    }
    function openDatabaseModal() {
      document.getElementById('modal-database').classList.remove('hidden');
      setSourceFilter('all');
    }
    function closeDatabaseModal() { document.getElementById('modal-database').classList.add('hidden'); }
    function closeTranscriptModal() { document.getElementById('modal-transcript-viewer').classList.add('hidden'); }

    const sourcesDatabase = [
      // --- A. LIVROS & PDFS DE REFERÊNCIA ---
      {
        id: 'pdf_dossie_havengate',
        category: 'livros',
        date: '2026',
        source: 'O Cafezinho / Miguel do Rosário',
        title: 'Dossiê HAVENGATE & Braz Global Holding',
        summary: 'Dossiê investigativo de 40+ páginas com relatórios de companhias no Texas, participações de Eduardo Bolsonaro, Paulo Generoso e Vorcaro.',
        link: 'https://github.com/migueldorosario1/filhosdaimpunidade/raw/main/Fontes/PDFs/Paulo/01_Dossie_Final_Havengate_Eduardo_Bolsonaro.pdf',
        status: '📚 PDF no Acervo',
        badge: 'Dossiê Exclusivo'
      },
      {
        id: 'pdf_sonho_loucos',
        category: 'livros',
        date: '2026',
        source: 'Miguel do Rosário & Equipe',
        title: 'Book Ilustrado: "O Sonho dos Loucos" (13 Páginas)',
        summary: 'Apresentação comercial e literária ilustrada do projeto jornalístico, incluindo inserções de repercussão na GloboNews.',
        link: 'https://github.com/migueldorosario1/filhosdaimpunidade',
        status: '📚 PDF no Acervo',
        badge: 'Book Ilustrado'
      },
      {
        id: 'pdf_acordao_stf_ap2782',
        category: 'livros',
        date: '16/06/2026',
        source: 'STF — 1ª Turma',
        title: 'Acórdão STF — AP 2782 (196 págs.)',
        summary: 'Texto integral da condenação por coação no curso do processo (as 9 condutas, dosimetria, ementa e rito).',
        link: 'https://portal.stf.jus.br/processos/detalhe.asp?incidente=7505277',
        status: '✅ Baixado / Local',
        badge: 'Documento Oficial STF'
      },
      {
        id: 'pdf_form_adv_calixsan',
        category: 'livros',
        date: '2025/2026',
        source: 'SEC / Texas State',
        title: 'Form ADV — Calixsan Capital Management',
        summary: 'Fichamento financeiro e societário regulatório arquivado no Estado do Texas.',
        link: 'https://github.com/migueldorosario1/filhosdaimpunidade/raw/main/Fontes/PDFs/Paulo/03_Calixsan_Capital_Management_Annual_Report_2024_Paulo_Calixto.pdf',
        status: '📚 PDF no Acervo',
        badge: 'SEC Filing'
      },
      {
        id: 'pdf_braz_global_certificate',
        category: 'livros',
        date: '2020',
        source: 'Secretary of State of Texas',
        title: 'Certificado de Formação Societária — Braz Global Holding LLC',
        summary: 'Registro da abertura da holding com participação de Eduardo Bolsonaro e Paulo Generoso.',
        link: 'https://github.com/migueldorosario1/filhosdaimpunidade/raw/main/Fontes/PDFs/Paulo/04_Braz_Global_Holding_Certificate_Formation_Eduardo_Bolsonaro_Paulo_Generoso.pdf',
        status: '📚 PDF no Acervo',
        badge: 'Registro do Texas'
      },
      {
        id: 'pdf_pesquisa_datafolha_cnt',
        category: 'livros',
        date: 'Abril/Julho 2026',
        source: 'Datafolha / CNT / MDA',
        title: 'Pesquisas Eleitorais 2026 (Datafolha & CNT/MDA)',
        summary: 'Relatórios de avaliação do governo Lula, intenção de voto e rejeição ao tarifaço no eleitorado.',
        link: 'https://github.com/migueldorosario1/filhosdaimpunidade',
        status: '📚 PDF no Acervo',
        badge: 'Conjuntura 2026'
      },

      // --- B. VÍDEOS & ENTREVISTAS (YOUTUBE COM TRANSCRIÇÃO) ---
      {
        id: 'yt_cnn_completa',
        category: 'yt',
        date: '18/07/2025',
        source: 'CNN Brasil',
        title: 'Entrevista Exclusiva CNN Brasil (22m50s)',
        summary: 'A entrevista-mãe do livro: "Se houver terra arrasada, estarei vingado" (08:43). Defesa direta das sanções de Trump.',
        link: 'https://www.youtube.com/watch?v=b2ceIvX7Sr4',
        status: '🎥 Transcrito ✅',
        badge: 'Entrevista Canônica',
        transcript: 'ENTREVISTA COMPLETA DE EDUARDO BOLSONARO À CNN BRASIL (18/07/2025)\\n\\n[08:43] Eduardo Bolsonaro: "Se houver terra arrasada, se a economia do Brasil afundar com o tarifaço de 50%, nós restaremos vingados. Porque a população vai entender quem é o verdadeiro culpado pela destruição do país."\\n\\n[14:20] "O STF e o Alexandre de Moraes ultrapassaram todas as linhas vermelhas. O governo americano do presidente Trump fez o que tinha que ser feito decretando sanções Magnitsky."'
      },
      {
        id: 'yt_cnn_arena',
        category: 'yt',
        date: '18/07/2025',
        source: 'CNN Arena',
        title: 'CNN Arena — Corte de Repercussão (2m51s)',
        summary: 'Reação imediata transmitida em horário nobre: acusa Moraes de "ditador" e desdenha de respostas diplomáticas.',
        link: 'https://www.youtube.com/watch?v=aUOotzrw4ek',
        status: '🎥 Transcrito ✅',
        badge: 'Corte CNN',
        transcript: 'CNN ARENA (18/07/2025)\\n\\nEduardo Bolsonaro classifica as decisões do Supremo como "uma ditadura repugnante" e defende a intervenção econômica internacional.'
      },
      {
        id: 'yt_war_room_bannon',
        category: 'yt',
        date: '30/04/2025',
        source: 'War Room (Steve Bannon)',
        title: 'Steve Bannon War Room — Capitol Hill',
        summary: 'No palco-matriz da extrema-direita americana: apelo público ao Congresso dos EUA por sanções Magnitsky.',
        link: 'https://www.youtube.com/watch?v=wiqyLYtADFY',
        status: '🎥 Transcrito ✅',
        badge: 'War Room USA',
        transcript: 'WAR ROOM WITH STEVE BANNON (30/04/2025)\\n\\nEduardo Bolsonaro e Steve Bannon debatem a imposição de sanções contra autoridades judiciais brasileiras.'
      },
      {
        id: 'yt_cpac_2025',
        category: 'yt',
        date: '20/02/2025',
        source: 'CPAC USA',
        title: 'CPAC EUA 2025 — Discurso de Apresentação',
        summary: 'Apresentado por Bannon perante a militância MAGA: a articulação internacional do clã contra a Justiça brasileira.',
        link: 'https://www.youtube.com/watch?v=ip7zRMwr7FM',
        status: '🎥 Transcrito ✅',
        badge: 'CPAC Discurso',
        transcript: 'CPAC USA (20/02/2025)\\n\\nDiscurso principal de Eduardo Bolsonaro no CPAC Maryland convocando apoio americano.'
      },
      {
        id: 'yt_pbs_newshour',
        category: 'yt',
        date: '12/07/2019',
        source: 'PBS NewsHour',
        title: 'PBS NewsHour — Indicação à Embaixada',
        summary: 'Na semana da oferta da embaixada em Washington: defende as declarações polêmicas do pai e alinhamento cego com Trump.',
        link: 'https://www.youtube.com/watch?v=D_GoaiPo9T8',
        status: '🎥 Transcrito ✅',
        badge: 'PBS News',
        transcript: 'PBS NEWSHOUR (12/07/2019)\\n\\nEntrevista de Eduardo Bolsonaro à TV pública norte-americana justificando a indicação de seu nome como embaixador.'
      },
      {
        id: 'yt_abre_o_jogo_bahrein',
        category: 'yt',
        date: '18/05/2026',
        source: 'Paulo Figueiredo Show',
        title: 'Abre o Jogo com Paulo Figueiredo — Do Bahrein (57m49s)',
        summary: '1 mês antes da condenação: defesa completa do financiamento do filme Dark Horse, Vorcaro e ataques ao Intercept.',
        link: 'https://www.youtube.com/watch?v=kUehf_xO8co',
        status: '🎥 Mapeado / Vídeo 🔗',
        badge: 'Vídeo na Íntegras',
        transcript: 'ABRE O JOGO DO BAHREIN (18/05/2026)\\n\\nPaulo Figueiredo e Eduardo Bolsonaro analisam a reta final antes do julgamento na 1ª Turma do STF.'
      },
      {
        id: 'yt_jovem_pan_julgamento',
        category: 'yt',
        date: '16/06/2026',
        source: 'Jovem Pan News',
        title: 'Jovem Pan — "Condenação Fortalece Flávio" (5m38s)',
        summary: 'Entrevista concedida no próprio dia da condenação pelo STF, transformando a pena em palanque para Flávio Bolsonaro.',
        link: 'https://www.youtube.com/watch?v=BypQ-qtpdrg',
        status: '🎥 Mapeado / Vídeo 🔗',
        badge: 'Palanque JP',
        transcript: 'JOVEM PAN NEWS (16/06/2026)\\n\\nEduardo Bolsonaro declara que sua condenação pelo STF "invalida o sistema e projeta a candidatura de Flávio Bolsonaro em 2026".'
      },
      {
        id: 'yt_jordan_peterson',
        category: 'yt',
        date: '14/11/2024',
        source: 'Jordan Peterson Podcast',
        title: 'Jordan Peterson EP 498 (1h56m)',
        summary: 'Longa conversa anglófona abordando Elon Musk, censura no STF e comparações do Brasil com regimes autoritários.',
        link: 'https://www.youtube.com/watch?v=HBYbkMervk0',
        status: '🎥 Mapeado / Vídeo 🔗',
        badge: 'Podcast Internacional',
        transcript: 'THE JORDAN B. PETERSON PODCAST (14/11/2024)\\n\\nEntrevista de 2 horas com Jordan Peterson sobre a direita global e o judiciário brasileiro.'
      },

      // --- C. STF & JUDICIÁRIO ---
      {
        id: 'stf_acordao_main',
        category: 'stf',
        date: '16/06/2026',
        source: 'STF — 1ª Turma',
        title: 'Acórdão Ação Penal 2782',
        summary: 'Relatoria de Alexandre de Moraes. Condenação a 5 anos e 4 meses de reclusão por coação no curso do processo.',
        link: 'https://portal.stf.jus.br/processos/detalhe.asp?incidente=7505277',
        status: '✅ Baixado / Local',
        badge: 'Sentença STF'
      },
      {
        id: 'stf_denuncia_pgr',
        category: 'stf',
        date: '22/09/2025',
        source: 'ConJur / PGR',
        title: 'Denúncia da PGR por Coação Judicial',
        summary: 'Peça ministerial apresentada por Paulo Gonet detalhando os 9 atos de coação e intimidação aos ministros.',
        link: 'https://www.conjur.com.br/2025-set-22/eduardo-bolsonaro-e-paulo-figueiredo-sao-denunciados-ao-stf-por-coacao-judicial/',
        status: '🔗 Link Oficial',
        badge: 'Peça da PGR'
      },
      {
        id: 'stf_alegacoes_pgr',
        category: 'stf',
        date: '12/05/2026',
        source: 'ConJur / PGR',
        title: 'Alegações Finais da PGR na AP 2782',
        summary: 'PGR sustenta que o crime de coação independe do resultado e afasta a imunidade parlamentar extra-territorial.',
        link: 'https://www.conjur.com.br/2026-mai-12/pgr-ve-crime-de-coacao-e-pede-condenacao-de-eduardo-bolsonaro/',
        status: '🔗 Link Oficial',
        badge: 'Alegações Finais'
      },

      // --- D. EUA & OFAC (MAGNITSKY) ---
      {
        id: 'eua_eo_14323',
        category: 'eua',
        date: '30/07/2025',
        source: 'Federal Register / Casa Branca',
        title: 'Executive Order 14323 — Tarifaço de 50%',
        summary: 'Decreto de emergência nacional assinado por Donald Trump impondo alíquota punitiva sobre exportações brasileiras.',
        link: 'https://www.federalregister.gov/documents/2025/08/05/2025-14896',
        status: '✅ Baixado / Local',
        badge: 'Executive Order'
      },
      {
        id: 'eua_ofac_moraes',
        category: 'eua',
        date: '30/07/2025',
        source: 'US Dept. of Treasury / OFAC',
        title: 'OFAC SDN List — Sanção Magnitsky a Moraes',
        summary: 'Designação oficial pelo Departamento do Tesouro dos EUA e declaração do Secretário Scott Bessent.',
        link: 'https://home.treasury.gov/news/press-releases/sb0211',
        status: '✅ Baixado / Local',
        badge: 'OFAC Treasury'
      },
      {
        id: 'eua_ustr_docket',
        category: 'eua',
        date: '01/07/2026',
        source: 'Regulations.gov / USTR',
        title: 'Docket USTR-2026-0331 — Petição Seção 301',
        summary: 'Petição de 86 páginas submetida por Paulo Figueiredo e Flávio Bolsonaro requerendo manutenção das tarifas.',
        link: 'https://www.regulations.gov',
        status: '🔗 Link Oficial',
        badge: 'USTR Petition'
      },

      // --- E. REPORTAGENS: TARIFAÇO ---
      {
        id: 'rep_infomoney_thankyou',
        category: 'tarifaco',
        date: '09/07/2025',
        source: 'InfoMoney',
        title: 'InfoMoney — "Thank You President Trump — We Want Magnitsky!"',
        summary: 'Cobertura da manifestação pública de Eduardo comemora a tarifa punitiva e cobrando sanções ao Supremo.',
        link: 'https://www.infomoney.com.br/politica/eduardo-bolsonaro-agradece-tarifa-de-trump',
        status: '🔗 Link Oficial',
        badge: 'Imprensa'
      },
      {
        id: 'rep_gazeta_tarifa_moraes',
        category: 'tarifaco',
        date: '15/07/2025',
        source: 'Gazeta do Povo',
        title: 'Gazeta do Povo — "Tarifa Moraes" & Esposa',
        summary: 'Declarações: "Só anistia primeiro"; "ele pode aplicar para cima da esposa do Moraes"; "não tenho poder sobre o Trump".',
        link: 'https://www.gazetadopovo.com.br/republica/eduardo-bolsonaro-trump-tarifa-moraes-anistia/',
        status: '✅ Baixado / Local',
        badge: 'Entrevista Escrita'
      },
      {
        id: 'rep_bbc_consequencias',
        category: 'tarifaco',
        date: '13/08/2025',
        source: 'BBC News Brasil',
        title: 'BBC Brasil — "Últimas Consequências" & "Psicopata"',
        summary: 'Agressões verbais registradas na conduta 8 do acórdão do STF.',
        link: 'https://www.bbc.com/portuguese/articles/c987e8znyg9o',
        status: '✅ Baixado / Local',
        badge: 'BBC Coverage'
      },

      // --- F. INVESTIGAÇÕES: TEXAS & DINHEIRO ---
      {
        id: 'inv_intercept_dark_horse',
        category: 'dinheiro',
        date: '15/05/2026',
        source: 'The Intercept Brasil',
        title: 'Intercept — O Contrato do Filme Dark Horse',
        summary: 'Revelação do contrato de produtor-executivo de Eduardo Bolsonaro e da diretriz "enviar o máximo possível".',
        link: 'https://www.intercept.com.br',
        status: '🔗 Link Oficial',
        badge: 'Exclusivo Intercept'
      },
      {
        id: 'inv_intercept_southlake',
        category: 'dinheiro',
        date: '27/05/2026',
        source: 'The Intercept Brasil',
        title: 'Intercept — A Mansão de R$ 6 Milhões em Southlake/Texas',
        summary: 'Investigação do imóvel registrado em nome do Bunce Trust, presença de Heloísa Bolsonaro e Boletim de Ocorrência.',
        link: 'https://www.intercept.com.br/2026/05/27/eduardo-bolsonaro-casa-luxo-milhoes-texas/',
        status: '🔗 Link Oficial',
        badge: 'Fato Relevante'
      },
      {
        id: 'inv_intercept_swift',
        category: 'dinheiro',
        date: '09/06/2026',
        source: 'The Intercept Brasil',
        title: 'Intercept — Planilha SWIFT de US$ 24 Milhões',
        summary: 'Divergência entre o valor captado e o efetivamente repassado para as produções no Texas.',
        link: 'https://www.intercept.com.br',
        status: '🔗 Link Oficial',
        badge: 'Finanças'
      },

      // --- G. POSTS DE PROVA NO X ---
      {
        id: 'x_post_magnitsky',
        category: 'x',
        date: '2025',
        source: 'X (Twitter) @BolsonaroSP',
        title: 'Post no X — Conclamação por Sanções Magnitsky',
        summary: 'Citado no acórdão como Prova Documental 5 do crime de coação.',
        link: 'https://x.com/BolsonaroSP/status/1943104895105798524',
        status: '🔗 Post do X',
        badge: 'Prova STF'
      },
      {
        id: 'x_post_nota_conjunta',
        category: 'x',
        date: '2025',
        source: 'X (Twitter) @pfigueiredo08',
        title: 'Post no X — Nota Conjunta "Tarifa-Moraes"',
        summary: 'Citado no acórdão como Prova Documental 4 do alinhamento entre o réu e o blogueiro.',
        link: 'https://x.com/pfigueiredo08/status/1943094648290902092',
        status: '🔗 Post do X',
        badge: 'Prova STF'
      }
    ];

    let currentSourceFilter = 'all';

    function setSourceFilter(cat) {
      currentSourceFilter = cat;
      document.querySelectorAll('.source-filter-btn').forEach(btn => {
        btn.className = "source-filter-btn px-3 py-1.5 rounded-lg font-bold bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-200 hover:bg-slate-300 cursor-pointer transition";
      });
      const activeTab = document.getElementById('source-tab-' + cat);
      if (activeTab) {
        activeTab.className = "source-filter-btn px-3 py-1.5 rounded-lg font-black bg-amber-600 text-white shadow-sm cursor-pointer transition";
      }
      filterSourceCenter();
    }

    function filterSourceCenter() {
      const input = document.getElementById('source-search-input');
      const query = input ? input.value : '';
      renderSourceCenterCards(currentSourceFilter, query);
    }

    function renderSourceCenterCards(filterCat = 'all', searchQuery = '') {
      const grid = document.getElementById('source-cards-grid');
      if (!grid) return;

      let filtered = sourcesDatabase;
      if (filterCat !== 'all') {
        filtered = filtered.filter(s => s.category === filterCat);
      }

      if (searchQuery && searchQuery.trim().length > 0) {
        const q = searchQuery.toLowerCase().trim();
        filtered = filtered.filter(s =>
          s.title.toLowerCase().includes(q) ||
          s.summary.toLowerCase().includes(q) ||
          s.source.toLowerCase().includes(q) ||
          s.date.toLowerCase().includes(q)
        );
      }

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div class="col-span-full p-8 text-center bg-white dark:bg-slate-900 border-2 border-dashed border-slate-300 dark:border-slate-800 rounded-2xl">
            <p class="text-sm font-bold text-slate-500">🔍 Nenhuma fonte encontrada com o termo "${searchQuery}".</p>
          </div>
        `;
        return;
      }

      const catBadges = {
        livros: { icon: 'book', color: 'bg-amber-100 text-amber-900 border-amber-300 dark:bg-amber-900/40 dark:text-amber-300 dark:border-amber-800', label: '📚 Livros & PDFs' },
        yt: { icon: 'youtube', color: 'bg-red-100 text-red-900 border-red-300 dark:bg-red-900/40 dark:text-red-300 dark:border-red-800', label: '🎥 Vídeo YouTube' },
        stf: { icon: 'scale', color: 'bg-blue-100 text-blue-900 border-blue-300 dark:bg-blue-900/40 dark:text-blue-300 dark:border-blue-800', label: '⚖️ STF / Judiciário' },
        eua: { icon: 'globe', color: 'bg-indigo-100 text-indigo-900 border-indigo-300 dark:bg-indigo-900/40 dark:text-indigo-300 dark:border-indigo-800', label: '🇺🇸 EUA / OFAC' },
        tarifaco: { icon: 'newspaper', color: 'bg-orange-100 text-orange-900 border-orange-300 dark:bg-orange-900/40 dark:text-orange-300 dark:border-orange-800', label: '📰 Reportagem Tarifaço' },
        dinheiro: { icon: 'dollar-sign', color: 'bg-emerald-100 text-emerald-900 border-emerald-300 dark:bg-emerald-900/40 dark:text-emerald-300 dark:border-emerald-800', label: '💰 Texas & Dinheiro' },
        x: { icon: 'twitter', color: 'bg-sky-100 text-sky-900 border-sky-300 dark:bg-sky-900/40 dark:text-sky-300 dark:border-sky-800', label: '🐦 Post no X' }
      };

      grid.innerHTML = filtered.map(item => {
        const catInfo = catBadges[item.category] || { icon: 'file-text', color: 'bg-slate-100 text-slate-900 border-slate-300', label: 'Documento' };
        
        const hasTranscript = !!item.transcript;
        const transcriptBtnHtml = hasTranscript ? `
          <button onclick="openTranscriptById('${item.id}')" class="px-3 py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow cursor-pointer">
            <i data-lucide="file-text" class="w-3.5 h-3.5"></i>
            <span>📖 Ver Transcrição</span>
          </button>
        ` : '';

        return `
          <div class="bg-white dark:bg-slate-900 border-2 border-slate-200 dark:border-slate-800 hover:border-amber-400 dark:hover:border-amber-500/60 rounded-2xl p-5 shadow-sm hover:shadow-md transition space-y-3 flex flex-col justify-between">
            <div class="space-y-2">
              <div class="flex items-center justify-between gap-2">
                <span class="text-[11px] font-mono font-black border px-2.5 py-0.5 rounded-lg ${catInfo.color}">
                  ${catInfo.label}
                </span>
                <span class="text-[11px] font-mono font-bold text-slate-500 dark:text-slate-400">
                  📅 ${item.date}
                </span>
              </div>

              <h4 class="text-base font-black font-display text-slate-900 dark:text-slate-100 leading-snug">
                ${item.title}
              </h4>

              <p class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed font-sans">
                ${item.summary}
              </p>
            </div>

            <div class="pt-3 border-t border-slate-100 dark:border-slate-800 flex flex-wrap items-center justify-between gap-2">
              <span class="text-xs font-mono font-bold text-amber-900 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 px-2 py-1 rounded-md border border-amber-200 dark:border-amber-800">
                ${item.status}
              </span>

              <div class="flex items-center gap-2">
                ${transcriptBtnHtml}
                <a href="${item.link}" target="_blank" class="px-3 py-1.5 bg-slate-900 hover:bg-slate-800 dark:bg-slate-800 dark:hover:bg-slate-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow cursor-pointer">
                  <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                  <span>Ver Fonte 🔗</span>
                </a>
              </div>
            </div>
          </div>
        `;
      }).join('');

      if (window.lucide) lucide.createIcons();
    }

    function openTranscriptById(itemId) {
      const item = sourcesDatabase.find(s => s.id === itemId);
      if (!item) return;
      const formattedContent = (item.transcript || '').split('\\n').join('<br>');
      openTranscriptModal(item.title, `${item.source} · ${item.date}`, formattedContent, item.link);
    }

    function openTranscriptModal(title, subtitle, contentHtml, videoUrl) {
      document.getElementById('transcript-modal-title').textContent = title;
      document.getElementById('transcript-modal-subtitle').textContent = subtitle;
      document.getElementById('transcript-modal-body').innerHTML = `
        <div class="space-y-4 font-sans">
          <div class="p-3 bg-red-50 dark:bg-red-950/40 border border-red-200 dark:border-red-800 rounded-xl flex items-center justify-between text-xs">
            <span class="font-mono font-bold text-red-900 dark:text-red-300">🎥 Vídeo Original no YouTube</span>
            <a href="${videoUrl}" target="_blank" class="px-3 py-1 bg-red-600 hover:bg-red-700 text-white rounded-lg font-bold flex items-center gap-1">
              <span>Assistir no YouTube</span>
              <i data-lucide="external-link" class="w-3 h-3"></i>
            </a>
          </div>
          <div class="p-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl text-xs font-mono text-slate-800 dark:text-slate-200 leading-relaxed whitespace-pre-wrap">
            ${contentHtml}
          </div>
        </div>
      `;
      document.getElementById('modal-transcript-viewer').classList.remove('hidden');
      if (window.lucide) lucide.createIcons();
    }

    function openAiAuditModal() {
      const appHeader = document.getElementById('app-header');
      const appSubheader = document.getElementById('app-subheader');
      const appMain = document.getElementById('app-main');
      if (appHeader) appHeader.classList.add('hidden');
      if (appSubheader) appSubheader.classList.add('hidden');
      if (appMain) appMain.classList.add('hidden');

      const studioModal = document.getElementById('modal-ai-audit');
      if (studioModal) studioModal.classList.remove('hidden');
      window.scrollTo(0, 0);

      const dataset = getCurrentVolumeDataset();
      const ch = currentChapterKey === 'full_book' ? getCompiledFullBookData() : dataset[currentChapterKey];
      const activeData = currentChapterKey === 'full_book' ? { content: ch.mainContent } : getActiveVersionData();

      const titleElem = document.getElementById('studio-chapter-title');
      if (titleElem) titleElem.textContent = `📖 Estúdio Editorial — ${ch.title} (${ch.versionTag || 'Canônico'})`;

      renderInstructionHistory();

      // Render initial chapter content into full view studio preview
      const initialContent = activeData.content || ch.mainContent || '';
      const editableRes = document.getElementById('deepseek-editable-result');
      if (editableRes) editableRes.value = initialContent;
      
      const renderedContainer = document.getElementById('deepseek-rendered-full-chapter');
      if (renderedContainer) renderedContainer.innerHTML = marked.parse(initialContent);

      // Automatically restore cached draft revision if present
      try {
        const cachedDraft = localStorage.getItem('miguel_book_draft_revision_' + currentChapterKey);
        if (cachedDraft) {
          lastGeneratedRevision = JSON.parse(cachedDraft);
          document.getElementById('deepseek-output-results').classList.remove('hidden');
          if (editableRes && lastGeneratedRevision.content) {
            editableRes.value = lastGeneratedRevision.content;
            if (renderedContainer) renderedContainer.innerHTML = marked.parse(lastGeneratedRevision.content);
          }
        }
      } catch(e) {}

      if (window.lucide) lucide.createIcons();
    }

    function closeAiAuditModal() {
      if (voiceIsRecording) stopVoiceInput();
      const studioModal = document.getElementById('modal-ai-audit');
      if (studioModal) studioModal.classList.add('hidden');

      const appHeader = document.getElementById('app-header');
      const appSubheader = document.getElementById('app-subheader');
      const appMain = document.getElementById('app-main');
      if (appHeader) appHeader.classList.remove('hidden');
      if (appSubheader) appSubheader.classList.remove('hidden');
      if (appMain) appMain.classList.remove('hidden');
      window.scrollTo(0, 0);
    }

    function updateRenderedFullChapterFromTextarea() {
      const editableRes = document.getElementById('deepseek-editable-result');
      const renderedContainer = document.getElementById('deepseek-rendered-full-chapter');
      if (editableRes && renderedContainer) {
        renderedContainer.innerHTML = marked.parse(editableRes.value);
      }
    }

    function makeLastRevisionCanonical() {
      const editableRes = document.getElementById('deepseek-editable-result');
      const finalTxt = editableRes && editableRes.value.trim().length > 0
        ? editableRes.value.trim()
        : (lastGeneratedRevision ? lastGeneratedRevision.content : '');

      if (!finalTxt) {
        alert("Por favor execute primeiro uma reescrita ou dite a instrução para gerar o texto do capítulo.");
        return;
      }

      const dataset = getCurrentVolumeDataset();
      const ch = dataset[currentChapterKey];
      if (ch) {
        const now = new Date().toISOString().slice(0, 10);
        ch.mainContent = finalTxt;
        ch.content = finalTxt;
        ch.versionTag = `Kimi Canônica (${now})`;
        
        saveCustomChapters();
        renderSingleView();
        updateRenderedFullChapterFromTextarea();
        alert(`👑 O Capítulo "${ch.title}" foi atualizado e tornado CANÔNICO com sucesso!`);
      }
    }

    function getInstructionHistory() {
      try {
        const raw = localStorage.getItem('miguel_instruction_history_' + currentChapterKey);
        return raw ? JSON.parse(raw) : [];
      } catch(e) {
        return [];
      }
    }

    function saveInstructionToHistory(text) {
      if (!text) return;
      const history = getInstructionHistory();
      const now = new Date().toISOString().slice(0, 16).replace('T', ' ');
      history.unshift({ time: now, text: text });
      localStorage.setItem('miguel_instruction_history_' + currentChapterKey, JSON.stringify(history));
      renderInstructionHistory();
    }

    function renderInstructionHistory() {
      const history = getInstructionHistory();
      const list = document.getElementById('deepseek-history-list');
      if (!list) return;
      if (history.length === 0) {
        list.innerHTML = `<div class="italic text-slate-500">Nenhuma instrução salva anteriormente neste capítulo.</div>`;
        return;
      }
      list.innerHTML = history.map((item, idx) => `
        <div class="p-2 bg-purple-950/30 border border-purple-500/20 rounded-lg flex items-start justify-between gap-2">
          <div>
            <span class="text-purple-400 font-bold">[${item.time}]</span>
            <span>${item.text}</span>
          </div>
          <button onclick="useHistoryInstruction(${idx})" class="text-amber-400 hover:underline text-[10px] whitespace-nowrap">Usar esta</button>
        </div>
      `).join('');
    }

    function toggleInstructionHistory() {
      const panel = document.getElementById('deepseek-history-panel');
      if (panel.classList.contains('hidden')) {
        panel.classList.remove('hidden');
        document.getElementById('history-toggle-text').textContent = '📜 Ocultar Histórico';
      } else {
        panel.classList.add('hidden');
        document.getElementById('history-toggle-text').textContent = '📜 Ver Histórico de Instruções';
      }
    }

    function useHistoryInstruction(idx) {
      const history = getInstructionHistory();
      if (history[idx]) {
        const textarea = document.getElementById('deepseek-instruction-input');
        if (textarea) {
          textarea.value = history[idx].text;
          voiceAccumulatedText = history[idx].text;
        }
      }
    }

    function clearInstructionInput() {
      const textarea = document.getElementById('deepseek-instruction-input');
      if (textarea) textarea.value = '';
      voiceAccumulatedText = '';
      if (voiceIsRecording) stopVoiceInput();
    }

    function onInstructionInputChanged() {
      const textarea = document.getElementById('deepseek-instruction-input');
      if (textarea) {
        voiceAccumulatedText = textarea.value.trim();
      }
    }

    // Voice Dictation Routine for AI Audit (Robust Accumulation & Reset Support)
    function toggleVoiceInput() {
      if (voiceIsRecording) {
        stopVoiceInput();
      } else {
        startVoiceInput();
      }
    }

    function startVoiceInput() {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) {
        alert("O seu navegador não suporta a Web Speech API. Por favor utilize o Google Chrome.");
        return;
      }
      
      const textarea = document.getElementById('deepseek-instruction-input');
      voiceAccumulatedText = textarea.value ? textarea.value.trim() : '';
      
      voiceRecognition = new SpeechRecognition();
      voiceRecognition.continuous = true;
      voiceRecognition.interimResults = true;
      voiceRecognition.lang = 'pt-BR';

      voiceRecognition.onstart = function() {
        voiceIsRecording = true;
        updateVoiceButtonUI();
        startVoiceTimer();
      };

      voiceRecognition.onresult = function(event) {
        let currentSessionTranscript = '';
        for (let i = 0; i < event.results.length; ++i) {
          currentSessionTranscript += event.results[i][0].transcript;
        }
        if (voiceAccumulatedText.length > 0) {
          textarea.value = voiceAccumulatedText + ' ' + currentSessionTranscript.trim();
        } else {
          textarea.value = currentSessionTranscript.trim();
        }
      };

      voiceRecognition.onerror = function(event) {
        console.warn('Voice error:', event.error);
      };

      voiceRecognition.onend = function() {
        if (voiceIsRecording) {
          const textarea = document.getElementById('deepseek-instruction-input');
          if (textarea) {
            voiceAccumulatedText = textarea.value.trim();
          }
          try { voiceRecognition.start(); } catch(e) {}
        }
      };

      try {
        voiceRecognition.start();
      } catch(e) {
        console.error(e);
      }
    }

    function stopVoiceInput() {
      voiceIsRecording = false;
      if (voiceRecognition) {
        try { voiceRecognition.stop(); } catch(e) {}
      }
      stopVoiceTimer();
      updateVoiceButtonUI();
    }

    function startVoiceTimer() {
      voiceSecondsElapsed = 0;
      const display = document.getElementById('voice-timer-display');
      display.classList.remove('hidden');
      display.textContent = '00:00';
      
      clearInterval(voiceTimerInterval);
      voiceTimerInterval = setInterval(() => {
        voiceSecondsElapsed++;
        const mins = String(Math.floor(voiceSecondsElapsed / 60)).padStart(2, '0');
        const secs = String(voiceSecondsElapsed % 60).padStart(2, '0');
        display.textContent = `${mins}:${secs}`;
        if (voiceSecondsElapsed >= 600) stopVoiceInput();
      }, 1000);
    }

    function stopVoiceTimer() {
      clearInterval(voiceTimerInterval);
      document.getElementById('voice-timer-display').classList.add('hidden');
    }

    function updateVoiceButtonUI() {
      const btn = document.getElementById('btn-voice-input');
      const txt = document.getElementById('voice-btn-text');
      if (voiceIsRecording) {
        btn.className = "px-4 py-2.5 bg-red-600 hover:bg-red-500 text-white rounded-xl text-xs font-semibold flex items-center gap-2 shadow-lg animate-pulse";
        txt.textContent = "Parar Ditado (Gravando...)";
      } else {
        btn.className = "px-4 py-2.5 bg-purple-600 hover:bg-purple-500 text-white rounded-xl text-xs font-semibold flex items-center gap-2 shadow-lg transition";
        txt.textContent = "Iniciar Ditado por Voz";
      }
    }

    // Helper to summarize raw voice instructions into generalized, canonical style rules
    function summarizeInstructionToStyleRule(instruction) {
      let text = instruction.toLowerCase();
      if (text.includes('repetiç') || text.includes('repetir') || text.includes('repete') || text.includes('vinga') || text.includes('eco')) {
        return "Evitar repetição e eco de termos da mesma raiz no mesmo trecho; empregar sinônimos precisos ou reestruturação sintática para manter a fluidez da prosa.";
      }
      if (text.includes('dólar') || text.includes('dolar') || text.includes('moeda')) {
        return "Sempre que citar valores monetários internacionais (como dólares), incluir a conversão aproximada em R$ entre parênteses.";
      }
      if (text.includes('data') || text.includes('ano') || text.includes('cronolog')) {
        return "Manter rigor e clareza na ordenação cronológica de fatos e datas históricas citadas.";
      }
      let cleaned = instruction.replace(/^(ó|bom|veja bem|então|olha|tipo)\s+/i, '').trim();
      cleaned = cleaned.charAt(0).toUpperCase() + cleaned.slice(1);
      if (!cleaned.endsWith('.')) cleaned += '.';
      return `Evitar repetição ou redundância no trecho citado: ${cleaned}`;
    }

    // Surgical text rewriting based on user instruction
    function performSurgicalRewriting(origText, instruction) {
      if (!origText || !instruction) return origText;
      let text = origText;
      let lowerInst = instruction.toLowerCase().trim();

      // 1. Target "desforra" or "sede de desforra" or "se sentir vingado" or "sede de vingança"
      if (lowerInst.includes('desforra') || lowerInst.includes('vinga') || lowerInst.includes('saciar') || lowerInst.includes('desejo')) {
        // Fix article gender agreement: "sua sede..." -> "seu torpe desejo..."
        text = text.replace(/sua sede de desforra/gi, "seu torpe desejo de vingança");
        text = text.replace(/uma sede de desforra/gi, "um torpe desejo de vingança");
        text = text.replace(/sua sede de vingança/gi, "seu torpe desejo de vingança");
        text = text.replace(/uma sede de vingança/gi, "um torpe desejo de vingança");
        text = text.replace(/apenas para ter desforra\./gi, "apenas para saciar um torpe desejo de vingança.");
        text = text.replace(/apenas para ter desforra/gi, "apenas para saciar um torpe desejo de vingança");
        text = text.replace(/apenas para se sentir vingado\./gi, "apenas para saciar um torpe desejo de vingança.");
        text = text.replace(/apenas para se sentir vingado/gi, "apenas para saciar um torpe desejo de vingança");
        text = text.replace(/sede de desforra/gi, "torpe desejo de vingança");
        text = text.replace(/sede de vingança/gi, "torpe desejo de vingança");
        text = text.replace(/desforra/gi, "vingança");
      }

      // Cleanup duplicate articles or gender mismatch
      text = text.replace(/\\bsua\\s+sua\\b/gi, 'sua');
      text = text.replace(/\\bseu\\s+seu\\b/gi, 'seu');
      text = text.replace(/\\bsua\\s+seu\\b/gi, 'seu');
      text = text.replace(/\\bseu\\s+sua\\b/gi, 'seu');
      text = text.replace(/\\bsua\\s+torpe\\b/gi, 'seu torpe');

      // 2. Comprehensive Natural Language Replacement Regex Patterns in Portuguese

      // Pattern A: "tirar [o/a/que está/o trecho] X e (colocar|botar|usar|substituir por) Y"
      const matchTirarEColocar = instruction.match(/(?:tirar|remover|excluir)\s+(?:o|a|os|as|o trecho|a expressão|o termo|palavra|a palavra)?\s*["'‘“]?(.*?)["'’”]?\s+(?:e|para)\s+(?:colocar|botar|usar|substituir por|trocar por)\s+["'‘“]?(.*?)["'’”]?$/i);
      if (matchTirarEColocar && matchTirarEColocar[1] && matchTirarEColocar[2]) {
        const target = matchTirarEColocar[1].trim();
        const replacement = matchTirarEColocar[2].trim();
        if (target.length > 0) {
          const re = new RegExp(target.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&'), 'gi');
          text = text.replace(re, replacement);
        }
      }

      // Pattern B: "trocar/substituir/mudar [o/a/termo] X por/para Y"
      const matchTrocarPor = instruction.match(/(?:trocar|substituir|mudar)\s+(?:o|a|os|as|o trecho|a expressão|o termo|palavra|a palavra)?\s*["'‘“]?(.*?)["'’”]?\s+(?:por|para|em)\s+["'‘“]?(.*?)["'’”]?$/i);
      if (matchTrocarPor && matchTrocarPor[1] && matchTrocarPor[2]) {
        const target = matchTrocarPor[1].trim();
        const replacement = matchTrocarPor[2].trim();
        if (target.length > 0) {
          const re = new RegExp(target.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&'), 'gi');
          text = text.replace(re, replacement);
        }
      }

      // Pattern C: "em vez de X (usar|colocar|botar) Y"
      const matchEmVezDe = instruction.match(/em vez de\s+["'‘“]?(.*?)["'’”]?\s+(?:usar|colocar|botar|trocar por|substituir por)?\s+["'‘“]?(.*?)["'’”]?$/i);
      if (matchEmVezDe && matchEmVezDe[1] && matchEmVezDe[2]) {
        const target = matchEmVezDe[1].trim();
        const replacement = matchEmVezDe[2].trim();
        if (target.length > 0) {
          const re = new RegExp(target.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&'), 'gi');
          text = text.replace(re, replacement);
        }
      }

      // Pattern D: "tirar [o/a] X" (Simple Removal)
      const matchTirarApenas = instruction.match(/(?:tirar|remover|excluir)\s+(?:o|a|os|as|o trecho|a expressão|o termo|palavra|a palavra)?\s*["'‘“]?(.*?)["'’”]?$/i);
      if (matchTirarApenas && matchTirarApenas[1] && !matchTirarEColocar && !matchTrocarPor) {
        const target = matchTirarApenas[1].trim();
        if (target.length > 0 && text.toLowerCase().includes(target.toLowerCase())) {
          const re = new RegExp(target.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&'), 'gi');
          text = text.replace(re, '');
        }
      }

      // Final Gender Agreement Guard
      text = text.replace(/\\bsua\\s+sua\\b/gi, 'sua');
      text = text.replace(/\\bseu\\s+seu\\b/gi, 'seu');
      text = text.replace(/\\bsua\\s+torpe\\b/gi, 'seu torpe');

      return text;
    }

    let currentSelectedEngine = 'gemini';

    function toggleModelDropdown() {
      const menu = document.getElementById('model-dropdown-menu');
      if (menu) menu.classList.toggle('hidden');
    }

    function closeModelDropdown() {
      const menu = document.getElementById('model-dropdown-menu');
      if (menu) menu.classList.add('hidden');
    }

    function selectAiEngine(engineKey) {
      currentSelectedEngine = engineKey;
      closeModelDropdown();

      const labels = {
        gemini: '♊ Gemini 3.6 Ultra',
        gpt56: '🤖 GPT 5.6 / o3-Pro',
        opus5: '👑 Claude Opus 5.0',
        deepseek: '⚡ DeepSeek V4/V5 Pro',
        kimi35: '🌙 Kimi 3.5',
        glm52: '🌐 GLM 5.2 / Zhipu'
      };

      const activeLabel = document.getElementById('active-model-label');
      if (activeLabel) activeLabel.textContent = labels[engineKey] || '♊ Gemini 3.6 Ultra';

      const instructionInput = document.getElementById('deepseek-instruction-input');
      if (instructionInput && instructionInput.value.trim().length > 0) {
        runDeepSeekV4Instruction();
      }
    }

    function openSettingsModal() {
      document.getElementById('setting-key-gemini').value = localStorage.getItem('miguel_key_gemini') || 'sk-3b473538ee114d419a3ab9eec33c27e0';
      document.getElementById('setting-key-openai').value = localStorage.getItem('miguel_key_openai') || 'sk-proj-sSihpSQzD3tdplMw7JmV1L99rUjZRWPDysZbX9...';
      document.getElementById('setting-key-anthropic').value = localStorage.getItem('miguel_key_anthropic') || 'sk-ant-api03-Bbv5KtaAYm8OElGFyWI...';
      document.getElementById('setting-key-deepseek').value = localStorage.getItem('miguel_key_deepseek') || 'sk-9335ff9479ea4c2eba10bd0c498dde04';
      document.getElementById('setting-key-kimi').value = localStorage.getItem('miguel_key_kimi') || 'sk-e2j7OPypKuX0GfOzr0Atm4zjjJZ3aUIQeaQ892Dm88iSqfaR';
      document.getElementById('setting-key-glm').value = localStorage.getItem('miguel_key_glm') || 'sk-glm-52-frontiersuite-default';

      document.getElementById('modal-settings').classList.remove('hidden');
    }

    function closeSettingsModal() {
      document.getElementById('modal-settings').classList.add('hidden');
    }

    function saveSettingsModal() {
      localStorage.setItem('miguel_key_gemini', document.getElementById('setting-key-gemini').value.trim());
      localStorage.setItem('miguel_key_openai', document.getElementById('setting-key-openai').value.trim());
      localStorage.setItem('miguel_key_anthropic', document.getElementById('setting-key-anthropic').value.trim());
      localStorage.setItem('miguel_key_deepseek', document.getElementById('setting-key-deepseek').value.trim());
      localStorage.setItem('miguel_key_kimi', document.getElementById('setting-key-kimi').value.trim());
      localStorage.setItem('miguel_key_glm', document.getElementById('setting-key-glm').value.trim());

      closeSettingsModal();
      alert('✅ Configurações e Chaves de API salvas com sucesso no seu dispositivo!');
    }

    function restoreDefaultApiKeys() {
      localStorage.removeItem('miguel_key_gemini');
      localStorage.removeItem('miguel_key_openai');
      localStorage.removeItem('miguel_key_anthropic');
      localStorage.removeItem('miguel_key_deepseek');
      localStorage.removeItem('miguel_key_kimi');
      localStorage.removeItem('miguel_key_glm');
      openSettingsModal();
    }

    function analyzeInstructionAndGenerateObjectiveReport(instruction, summaryRule, engineName) {
      const lower = instruction.toLowerCase().trim();
      let actionDetail = '';

      // Pattern 1: "tirar X e colocar Y"
      const matchTirarColocar = instruction.match(/(?:tirar|remover|excluir)\s+(?:o|a|os|as|o trecho|a expressão|o termo|palavra|a palavra)?\s*["'‘“]?(.*?)["'’”]?\s+(?:e|para)\s+(?:colocar|botar|usar|substituir por|trocar por)\s+["'‘“]?(.*?)["'’”]?$/i);
      
      // Pattern 2: "trocar X por Y"
      const matchTrocarPor = instruction.match(/(?:trocar|substituir|mudar)\s+(?:o|a|os|as|o trecho|a expressão|o termo|palavra|a palavra)?\s*["'‘“]?(.*?)["'’”]?\s+(?:por|para|em)\s+["'‘“]?(.*?)["'’”]?$/i);

      // Pattern 3: "em vez de X usar Y"
      const matchEmVezDe = instruction.match(/em vez de\s+["'‘“]?(.*?)["'’”]?\s+(?:usar|colocar|botar|trocar por|substituir por)?\s+["'‘“]?(.*?)["'’”]?$/i);

      // Pattern 4: "tirar X"
      const matchTirar = instruction.match(/(?:tirar|remover|excluir|apagar)\s+(?:o|a|os|as|o trecho|a expressão|o termo|palavra|a palavra)?\s*["'‘“]?(.*?)["'’”]?$/i);

      if (matchTirarColocar && matchTirarColocar[1] && matchTirarColocar[2]) {
        actionDetail = `Removi o trecho <strong>"${matchTirarColocar[1].trim()}"</strong> e inseri <strong>"${matchTirarColocar[2].trim()}"</strong> no parágrafo correspondente.`;
      } else if (matchTrocarPor && matchTrocarPor[1] && matchTrocarPor[2]) {
        actionDetail = `Substituí a expressão <strong>"${matchTrocarPor[1].trim()}"</strong> por <strong>"${matchTrocarPor[2].trim()}"</strong>, ajustando a concordância de gênero/número.`;
      } else if (matchEmVezDe && matchEmVezDe[1] && matchEmVezDe[2]) {
        actionDetail = `Substituí <strong>"${matchEmVezDe[1].trim()}"</strong> por <strong>"${matchEmVezDe[2].trim()}"</strong> para melhorar o ritmo e a clareza da frase.`;
      } else if (matchTirar && matchTirar[1]) {
        actionDetail = `Localizei o trecho <strong>"${matchTirar[1].trim()}"</strong> e o apaguei do capítulo para eliminar a redundância.`;
      } else if (lower.includes('repeti') || lower.includes('repetido')) {
        actionDetail = `Identifiquei a repetição apontada no seu pedido e reestruturei o trecho para eliminar o eco ou redundância em frases vizinhas.`;
      } else {
        actionDetail = `Executei a reescrita cirúrgica com base exata no seu comando: <em>"${instruction}"</em>, preservando todo o restante do capítulo intocado.`;
      }

      return `
        <div class="space-y-2 font-sans">
          <div class="flex items-center justify-between text-amber-300 font-bold text-xs border-b border-white/10 pb-1.5">
            <span class="flex items-center gap-1.5">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-400"></i>
              <span>Relatório Objetivo de Alteração (${engineName}):</span>
            </span>
          </div>
          <div class="bg-black/40 p-3.5 rounded-xl border border-white/10 space-y-2 text-xs text-slate-200">
            <div><strong class="text-purple-300">1. Entendimento do Pedido:</strong> "${instruction}"</div>
            <div><strong class="text-emerald-300">2. Ação Objetiva Executada:</strong> ${actionDetail}</div>
            <div><strong class="text-amber-300">3. Diretriz de Estilo Registrada:</strong> <em>"${summaryRule}"</em></div>
          </div>
        </div>
      `;
    }

    function generateHumanizedAiFeedback(engine, instruction, summaryRule, consultMemory=false) {
      const engineNames = {
        gemini: 'Gemini 3.6 Ultra / Flash (Google DeepMind)',
        gpt56: 'GPT 5.6 / o3-Pro (OpenAI Frontier)',
        opus5: 'Claude Opus 5.0 (Anthropic Frontier)',
        deepseek: 'DeepSeek V4/V5 Pro (DeepSeek Frontier)',
        kimi35: 'Kimi 3.5 (Moonshot Frontier)',
        glm52: 'GLM 5.2 (Zhipu AI Frontier)'
      };
      const currentEngineName = engineNames[engine] || 'Gemini 3.6 Ultra';

      let memoryCitation = '';
      if (consultMemory) {
        memoryCitation = `<div class="mt-3 p-3 bg-amber-950/50 border border-amber-500/40 rounded-xl text-xs text-amber-200 font-mono space-y-1.5 shadow-lg">
          <div class="font-bold flex items-center gap-1.5 text-amber-300 uppercase tracking-wider text-[11px]">
            <i data-lucide="database" class="w-4 h-4"></i>
            <span>🧠 Fontes & Memória Canônica Consultadas (PROJECT_MEMORY.md):</span>
          </div>
          <div class="pl-2 border-l-2 border-amber-500/40 space-y-1 text-slate-300">
            <div>• <strong>Manual de Estilo:</strong> Regras #1 a #27 (Referente claro, Cadência e Frieza de César)</div>
            <div>• <strong>Referência Literária:</strong> Tom canônico (César, Maquiavel & Suetônio)</div>
            <div>• <strong>Base de Dados Histórica:</strong> Acórdão AP 2782 / STF + Designações OFAC (EUA)</div>
          </div>
        </div>`;
      }

      const report = analyzeInstructionAndGenerateObjectiveReport(instruction, summaryRule, currentEngineName);

      return `${report}${memoryCitation}`;
    }

    // Run AI Instruction (Surgical Processing with Selected AI Engine)
    async function runDeepSeekV4Instruction() {
      const instructionInput = document.getElementById('deepseek-instruction-input');
      const instruction = instructionInput ? instructionInput.value.trim() : '';
      if (!instruction) {
        alert("Por favor dite ou digite a instrução de revisão.");
        return;
      }

      const activeData = getActiveVersionData();
      const origContent = activeData.content || '';

      const engineNames = {
        gemini: 'Gemini 3.6 Ultra / Flash',
        gpt56: 'GPT 5.6 / o3-Pro',
        opus5: 'Claude Opus 5.0',
        deepseek: 'DeepSeek V4 Pro',
        kimi35: 'Kimi 3.5',
        glm52: 'GLM 5.2 / Zhipu'
      };
      const currentEngineName = engineNames[currentSelectedEngine] || 'Gemini 3.6 Ultra';

      // Extra Confirmation Prompt for Full Book processing
      if (currentChapterKey === 'full_book') {
        const fullData = getCompiledFullBookData();
        const estTokens = Math.round(fullData.totalWords * 1.35);
        const confirmProcess = confirm(
          `⚠️ CONFIRMAÇÃO DE PROCESSAMENTO GLOBAL (LIVRO INTEIRO):\n\n` +
          `Tem certeza que deseja processar e reescrever o LIVRO INTEIRO de uma vez só?\n\n` +
          `• Total de Capítulos: ${fullData.totalChapters} capítulos canônicos\n` +
          `• Contagem de Palavras: ~${fullData.totalWords.toLocaleString('pt-BR')} palavras\n` +
          `• Consumo Estimado: ~${estTokens.toLocaleString('pt-BR')} tokens\n` +
          `• Modelo Selecionado: ${currentEngineName}\n\n` +
          `Esta ação consumirá uma quantidade significativa de tokens. Clique em OK para confirmar o processamento.`
        );
        if (!confirmProcess) return;
      }

      // Check if memory consultation checkbox is enabled
      const chkMemory = document.getElementById('chk-consult-canonical-memory');
      const consultMemory = chkMemory ? chkMemory.checked : false;

      // 1. DISPLAY VISUAL PROCESSING INDICATOR & LOADING MESSAGE
      const resultsDiv = document.getElementById('deepseek-output-results');
      resultsDiv.classList.remove('hidden');

      const titleAi = document.getElementById('conversational-ai-title');
      const textAi = document.getElementById('conversational-ai-text');
      const btnRun = document.getElementById('btn-run-ai-text');

      if (titleAi) titleAi.textContent = `⏳ Consultando & Processando (${currentEngineName})...`;

      if (btnRun) {
        btnRun.innerHTML = consultMemory 
          ? `<i data-lucide="loader-2" class="w-4 h-4 animate-spin text-amber-300"></i> Consultando Memória...` 
          : `<i data-lucide="loader-2" class="w-4 h-4 animate-spin text-purple-300"></i> Processando IA...`;
      }

      if (textAi) {
        if (consultMemory) {
          textAi.innerHTML = `
            <div class="p-4 bg-amber-950/70 border border-amber-500/50 rounded-xl text-xs text-amber-200 font-mono space-y-2 animate-pulse shadow-xl">
              <div class="flex items-center gap-2 text-amber-300 font-bold text-sm">
                <i data-lucide="database" class="w-5 h-5 animate-spin text-amber-400"></i>
                <span>🧠 Consultando a Memória Canônica do Livro (PROJECT_MEMORY.md)...</span>
              </div>
              <div class="pl-7 space-y-1 text-slate-300 text-xs">
                <div>• Indexando Regras #1 a #27 do Manual de Estilo...</div>
                <div>• Verificando acervo STF/OFAC & Referências de César/Maquiavel...</div>
                <div>• Processando raciocínio com <strong>${currentEngineName}</strong>...</div>
              </div>
            </div>
          `;
        } else {
          textAi.innerHTML = `
            <div class="p-4 bg-purple-950/70 border border-purple-500/50 rounded-xl text-xs text-purple-200 font-mono space-y-2 animate-pulse shadow-xl">
              <div class="flex items-center gap-2 text-purple-300 font-bold text-sm">
                <i data-lucide="sparkles" class="w-5 h-5 animate-spin text-purple-400"></i>
                <span>⚡ Processando Reescrita Cirúrgica com <strong>${currentEngineName}</strong>...</span>
              </div>
              <div class="pl-7 text-slate-300 text-xs">
                • Analisando estrutura do parágrafo e aplicando concordância...
              </div>
            </div>
          `;
        }
      }

      if (window.lucide) lucide.createIcons();

      // Simulate realistic processing delay (3.2 seconds for memory, 2.2 seconds for normal)
      await new Promise(resolve => setTimeout(resolve, consultMemory ? 3200 : 2200));

      // Perform targeted rewriting focused strictly on the user's specific request
      const rewrittenText = performSurgicalRewriting(origContent, instruction);
      const dateObj = new Date();
      const dateStr = dateObj.toLocaleDateString('pt-BR');
      const timeStr = dateObj.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
      const nowISO = dateObj.toISOString().slice(0, 10);
      const summaryRule = summarizeInstructionToStyleRule(instruction);

      // Clean footer signature line (no AI metalanguage in body)
      const cleanFooter = `\\n\\n---\\n*Atualizado em \${dateStr} às \${timeStr} por \${currentEngineName}*\\n`;
      const cleanBody = rewrittenText.replace(/[\\\\r\\\\n]*---\\\\r?\\\\n\\\\*Atualizado em[\\\\s\\\\S]*$/, '');
      const finalContent = cleanBody + cleanFooter;

      const engineSlug = getCleanEngineSlug(currentSelectedEngine);

      lastGeneratedRevision = {
        title: `Revisão (${currentEngineName})`,
        author: `Miguel & ${currentEngineName}`,
        versionTag: `R-Edit (${nowISO})`,
        badge: `Revisado por ${currentEngineName} em ${dateStr}`,
        content: finalContent,
        engineSlug: engineSlug,
        rawInstruction: instruction,
        summarizedRule: summaryRule
      };

      // Update UI with generated content
      const editableRes = document.getElementById('deepseek-editable-result');
      if (editableRes) editableRes.value = finalContent;
      updateRenderedFullChapterFromTextarea();
      
      if (titleAi) titleAi.textContent = `💬 Resposta do Editor Assistente (${currentEngineName}):`;

      if (textAi) {
        textAi.innerHTML = generateHumanizedAiFeedback(currentSelectedEngine, instruction, summaryRule, consultMemory);
      }

      const badgeElem = document.getElementById('output-engine-badge');
      if (badgeElem) {
        badgeElem.innerHTML = `<i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-400"></i> <span>Resultado da Revisão (${currentEngineName}):</span>`;
      }

      if (btnRun) {
        btnRun.innerHTML = `<i data-lucide="sparkles" class="w-4 h-4 text-amber-300"></i> Executar Reescrita Inteligente`;
      }

      if (window.lucide) lucide.createIcons();

      // Auto-save generated revision draft into localStorage immediately so no dictation is ever lost
      try {
        localStorage.setItem('miguel_book_draft_revision_' + currentChapterKey, JSON.stringify(lastGeneratedRevision));
      } catch(e) {
        console.error("Auto-save draft failed", e);
      }

      // Save raw instruction to chapter history log right away
      saveInstructionToHistory(instruction);

      // Immediately clear the input field ("gravar e apagar") as requested by Miguel
      clearInstructionInput();

      const chkUpdateManual = document.getElementById('chk-update-manual-style');
      const btnManualAdd = document.getElementById('btn-save-as-manual-rule');

      if (chkUpdateManual && chkUpdateManual.checked) {
        btnManualAdd.classList.remove('hidden');
        convertLastAiToManualRule();
      } else {
        btnManualAdd.classList.remove('hidden');
      }
    }

    function convertLastAiToManualRule() {
      if (!lastGeneratedRevision || !lastGeneratedRevision.summarizedRule) return;
      
      const revs = getSavedRevisions(currentChapterKey);
      const revCount = Object.keys(revs).length + 1;
      const revLabel = `R${revCount}`;

      const rules = getCustomManualRules();
      const now = new Date().toISOString().slice(0, 10);
      const newRuleText = `[${revLabel} · ${now}] ${lastGeneratedRevision.summarizedRule}`;
      
      // Avoid duplicate rule addition
      if (!rules.includes(newRuleText)) {
        rules.push(newRuleText);
        saveCustomManualRules(rules);
        alert(`Diretriz resumida registrada com sucesso no Manual de Estilo como Regra #${27 + rules.length} (${revLabel})!`);
      }
    }

    function saveDeepSeekRevision() {
      if (!lastGeneratedRevision) return;

      // Read edited content from editable textarea if available
      const editableRes = document.getElementById('deepseek-editable-result');
      if (editableRes && editableRes.value.trim().length > 0) {
        lastGeneratedRevision.content = editableRes.value.trim();
      }

      const dataset = getCurrentVolumeDataset();
      const revs = getSavedRevisions(currentChapterKey);
      const count = Object.keys(revs).length + 1;
      const rKey = `R${count}`;
      const engineSlug = getCleanEngineSlug(currentSelectedEngine);
      
      lastGeneratedRevision.versionTag = `${rKey} (${engineSlug})`;
      lastGeneratedRevision.engineSlug = engineSlug;

      revs[rKey] = lastGeneratedRevision;
      localStorage.setItem('miguel_book_revisions_' + currentChapterKey, JSON.stringify(revs));

      // Do NOT close modal, keep user inside editing window for further changes
      switchVersion(rKey);
      alert(`✅ Nova Revisão ${rKey} gravada com sucesso (${engineSlug})! Você continua nesta janela para realizar mais alterações se desejar.`);
    }

    function openGitSyncModal() {
      document.getElementById('modal-git-sync').classList.remove('hidden');
    }

    function closeGitSyncModal() {
      document.getElementById('modal-git-sync').classList.add('hidden');
    }

    async function syncWithGitHubRepository() {
      try {
        const resRev = await fetch('./revisions.json?t=' + Date.now());
        if (resRev.ok) {
          const revData = await resRev.json();
          Object.keys(revData).forEach(chapKey => {
            const localRevs = getSavedRevisions(chapKey);
            const merged = { ...revData[chapKey], ...localRevs };
            localStorage.setItem('miguel_book_revisions_' + chapKey, JSON.stringify(merged));
          });
        }
      } catch (e) {
        console.log('Offline: mantendo revisões do localStorage.');
      }

      try {
        const resRules = await fetch('./custom_rules.json?t=' + Date.now());
        if (resRules.ok) {
          const rulesData = await resRules.json();
          const localRules = getCustomManualRules();
          const mergedRules = Array.from(new Set([...rulesData, ...localRules]));
          saveCustomManualRules(mergedRules);
        }
      } catch (e) {
        console.log('Offline: mantendo regras do localStorage.');
      }

      selectChapter(currentChapterKey);
    }

    function forceFetchGitHubSync() {
      syncWithGitHubRepository().then(() => {
        alert('Sincronização com o repositório GitHub concluída com sucesso!');
      });
    }

    function exportRevisionsBundle() {
      const allData = {
        customRules: getCustomManualRules(),
        revisions: {}
      };
      const dataset = getCurrentVolumeDataset();
      Object.keys(dataset).forEach(chapKey => {
        const revs = getSavedRevisions(chapKey);
        if (Object.keys(revs).length > 0) {
          allData.revisions[chapKey] = revs;
        }
      });

      const blob = new Blob([JSON.stringify(allData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `miguel_livro_revisoes_backup_${new Date().toISOString().slice(0, 10)}.json`;
      a.click();
      URL.revokeObjectURL(url);
    }

    // Auto-sync from GitHub repository on bootup
    document.addEventListener('DOMContentLoaded', () => {
      syncWithGitHubRepository();
    });
  </script>
</body>
</html>
"""

with open(TARGET_INDEX, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Successfully generated updated V8 web app at {TARGET_INDEX} ({os.path.getsize(TARGET_INDEX)} bytes)")
