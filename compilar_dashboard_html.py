import json
import html
import re

def format_item_html(text: str) -> str:
    if not text:
        return ""
    # 1. Clean any control characters and mid-string tabs
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\t]', ' ', text)
    # 2. Sanitize leftover LaTeX subscripts like _{X,Y} -> (X, Y)
    text = re.sub(r'_\{([^}]+)\}', r'(\1)', text)
    # 3. Escape HTML entities
    s = html.escape(text)
    # 4. Bold: **text** -> <strong class="font-semibold text-gray-900">\1</strong>
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong class="font-semibold text-gray-900">\1</strong>', s)
    # 5. Inline code: `code` -> <code class="px-1.5 py-0.5 rounded bg-gray-100 font-mono text-[11px] sm:text-xs text-indigo-700 font-semibold border border-gray-200">\1</code>
    s = re.sub(r'`([^`]+)`', r'<code class="px-1.5 py-0.5 rounded bg-gray-100 font-mono text-[11px] sm:text-xs text-indigo-700 font-semibold border border-gray-200">\1</code>', s)
    # 6. Italics: *text* -> <em class="italic text-gray-700">\1</em>
    s = re.sub(r'(?<!\*)\*([^*\s][^*]*?[^*\s]|\w)\*(?!\*)', r'<em class="italic text-gray-700">\1</em>', s)
    return s

# Carregar base de dados consolidada
with open("/home/Hugo/Documentos/iniciando/data_checklist.json", "r", encoding="utf-8") as f:
    data = json.load(f)

disciplines = data["disciplines"]
semesters = data["semesters"]
discursivas = data["discursivas"]

total_disc_items = sum(sum(len(g["items"]) for g in d["groups"]) + len(d.get("checklists", [])) for d in disciplines)
total_sem_items = sum(len(s["months"]) for s in semesters)
total_disc_t = len(discursivas)

# Total do Núcleo de Ferro (Disciplinas 1 a 5)
tier_a_total_count = sum(
    sum(len(g["items"]) for g in d["groups"]) + len(d.get("checklists", []))
    for d in disciplines if d["num"] <= 5
)

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR" class="h-full bg-gray-50">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tronco Comum Antifrágil de TI • Checklist de Estudos (2026–2028)</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#eef2ff',
              100: '#e0e7ff',
              200: '#c7d2fe',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    
    /* Destaque Amarelo Suave de Conclusão Obrigatório */
    .concluida {{
      background-color: #fef9c3 !important; /* Tailwind yellow-100 */
      border-left: 4px solid #eab308 !important; /* amber-500 */
    }}
    .concluida .item-text,
    .concluida .chk-text,
    .concluida .month-name,
    .concluida .month-subjects,
    .concluida .month-target,
    .concluida h3,
    .concluida h4,
    .concluida p {{
      color: #713f12 !important; /* amber-900 */
      font-weight: 600 !important;
    }}
    .concluida .item-text strong,
    .concluida .chk-text strong,
    .concluida .month-subjects strong,
    .concluida .month-target strong,
    .concluida .item-text em,
    .concluida .chk-text em {{
      color: #713f12 !important;
    }}
    .concluida .item-text code,
    .concluida .chk-text code,
    .concluida .month-subjects code,
    .concluida .month-target code {{
      background-color: #fef08a !important;
      color: #854d0e !important;
      border-color: #fde047 !important;
    }}
    .concluida .item-status-badge {{
      display: inline-flex !important;
      background-color: #fef08a !important;
      color: #854d0e !important;
      border-color: #eab308 !important;
    }}

    /* Accordion transitions */
    .discipline-card.open .card-body {{
      display: block;
    }}
    .discipline-card:not(.open) .card-body {{
      display: none;
    }}
    .discipline-card.open .chevron-icon {{
      transform: rotate(180deg);
    }}

    /* Toast */
    .toast {{
      transition: opacity 0.2s ease, transform 0.2s ease;
    }}
    .toast.show {{
      opacity: 1 !important;
      transform: translateY(0) !important;
      pointer-events: auto !important;
    }}
  </style>
</head>
<body class="min-h-full bg-gray-50 text-gray-900 antialiased flex flex-col pb-16">

  <!-- HEADER COMPACTO, DISCRETO E ELEGANTE (Tailwind UI Stacked Light Shell) -->
  <header class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Linha Principal do Header (56px no Desktop) -->
      <div class="flex items-center justify-between h-14">
        
        <!-- Identidade Visual & Título Compacto -->
        <div class="flex items-center space-x-2.5 sm:space-x-3 flex-shrink-0">
          <div class="h-8 w-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white shadow-xs flex-shrink-0">
            <!-- Heroicon: academic-cap -->
            <svg class="h-4.5 w-4.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14v7"/>
            </svg>
          </div>
          <div class="min-w-0">
            <div class="flex items-center gap-1.5">
              <span class="text-sm font-bold text-gray-900 tracking-tight whitespace-nowrap">Tronco Comum TI</span>
              <span class="inline-flex items-center px-1.5 py-0.2 rounded text-[10px] font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200 whitespace-nowrap">2026–2028</span>
            </div>
            <p class="hidden xl:block text-[11px] text-gray-500 font-normal leading-none mt-0.5">{total_disc_items} tópicos • 10 disciplinas • FGV, Cebraspe &amp; FCC</p>
          </div>
        </div>

        <!-- Abas no Desktop (Visíveis em md: e acima) -->
        <nav class="hidden md:flex space-x-1 lg:space-x-2 items-center mx-2">
          <button type="button" onclick="switchTab('tab-disciplinas', this)" id="tab-btn-disciplinas" class="tab-nav-btn inline-flex items-center px-2.5 lg:px-3 py-1.5 text-xs font-semibold rounded-md text-indigo-700 bg-indigo-50 transition-all whitespace-nowrap">
            <span>Disciplinas</span>
            <span id="badge-tab-disciplinas" class="ml-1.5 py-0.2 px-1.5 rounded-full text-[10px] font-bold bg-indigo-200/70 text-indigo-800">{total_disc_items}</span>
          </button>
          <button type="button" onclick="switchTab('tab-cronograma', this)" id="tab-btn-cronograma" class="tab-nav-btn inline-flex items-center px-2.5 lg:px-3 py-1.5 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap">
            <span>Cronograma</span>
            <span id="badge-tab-cronograma" class="ml-1.5 py-0.2 px-1.5 rounded-full text-[10px] font-medium bg-gray-200 text-gray-700">23m</span>
          </button>
          <button type="button" onclick="switchTab('tab-discursivas', this)" id="tab-btn-discursivas" class="tab-nav-btn inline-flex items-center px-2.5 lg:px-3 py-1.5 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap">
            <span>Discursivas</span>
            <span id="badge-tab-discursivas" class="ml-1.5 py-0.2 px-1.5 rounded-full text-[10px] font-medium bg-gray-200 text-gray-700">6</span>
          </button>
          <button type="button" onclick="switchTab('tab-backup', this)" id="tab-btn-backup" class="tab-nav-btn inline-flex items-center px-2.5 lg:px-3 py-1.5 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap">
            <span>Backup</span>
          </button>
        </nav>

        <!-- Ações do Cabeçalho: Status de Salvamento e Botões Compactos -->
        <div class="flex items-center space-x-2 flex-shrink-0">
          <!-- Indicador de Salvamento Automático -->
          <div class="hidden sm:inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[11px] font-medium bg-emerald-50 text-emerald-700 border border-emerald-200" title="Todas as alterações são salvas continuamente no navegador">
            <span class="h-1.5 w-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>Salvo</span>
          </div>

          <!-- Grupo de Botões Secundários (Tailwind UI Button Group) -->
          <div class="inline-flex rounded-md shadow-xs" role="group">
            <button type="button" onclick="exportProgress()" class="inline-flex items-center px-2.5 py-1 text-xs font-medium text-gray-700 bg-white border border-gray-300 rounded-l-md hover:bg-gray-50 focus:z-10 focus:ring-1 focus:ring-indigo-500" title="Exportar Backup JSON">
              <svg class="h-3.5 w-3.5 sm:mr-1 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
              <span class="hidden sm:inline">Exportar</span>
            </button>
            <button type="button" onclick="document.getElementById('import-file-input').click()" class="inline-flex items-center px-2.5 py-1 text-xs font-medium text-gray-700 bg-white border-t border-b border-r border-gray-300 hover:bg-gray-50 focus:z-10 focus:ring-1 focus:ring-indigo-500" title="Importar Backup JSON">
              <svg class="h-3.5 w-3.5 sm:mr-1 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
              <span class="hidden sm:inline">Importar</span>
            </button>
            <button type="button" onclick="resetAllProgress()" class="inline-flex items-center px-2 py-1 text-xs font-medium text-red-600 bg-white border-t border-b border-r border-gray-300 rounded-r-md hover:bg-red-50 focus:z-10 focus:ring-1 focus:ring-red-500" title="Resetar Todo o Progresso">
              <svg class="h-3.5 w-3.5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
            </button>
          </div>
          <input type="file" id="import-file-input" class="hidden" accept=".json" onchange="importProgress(event)">
        </div>

      </div>

      <!-- Abas no Mobile/Tablet (Visíveis apenas abaixo de md) -->
      <nav class="flex md:hidden space-x-1.5 pb-2 pt-0.5 overflow-x-auto border-t border-gray-100">
        <button type="button" onclick="switchTab('tab-disciplinas', this)" id="tab-btn-disciplinas-mob" class="tab-nav-btn-mob inline-flex items-center px-2.5 py-1 text-xs font-semibold rounded-md text-indigo-700 bg-indigo-50 transition-all whitespace-nowrap">
          <span>Disciplinas</span>
          <span id="badge-tab-disciplinas-mob" class="ml-1 py-0.2 px-1 rounded-full text-[10px] font-bold bg-indigo-200/70 text-indigo-800">{total_disc_items}</span>
        </button>
        <button type="button" onclick="switchTab('tab-cronograma', this)" id="tab-btn-cronograma-mob" class="tab-nav-btn-mob inline-flex items-center px-2.5 py-1 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap">
          <span>Cronograma</span>
          <span id="badge-tab-cronograma-mob" class="ml-1 py-0.2 px-1 rounded-full text-[10px] font-medium bg-gray-200 text-gray-700">23m</span>
        </button>
        <button type="button" onclick="switchTab('tab-discursivas', this)" id="tab-btn-discursivas-mob" class="tab-nav-btn-mob inline-flex items-center px-2.5 py-1 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap">
          <span>Discursivas</span>
          <span id="badge-tab-discursivas-mob" class="ml-1 py-0.2 px-1 rounded-full text-[10px] font-medium bg-gray-200 text-gray-700">6</span>
        </button>
        <button type="button" onclick="switchTab('tab-backup', this)" id="tab-btn-backup-mob" class="tab-nav-btn-mob inline-flex items-center px-2.5 py-1 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap">
          <span>Backup</span>
        </button>
      </nav>

    </div>
  </header>

  <!-- CONTEÚDO PRINCIPAL -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 sm:py-5 w-full flex-1">

    <!-- METRIC STRIP COMPACTO (Tailwind UI stats with_shared_borders pattern em modo claro) -->
    <section class="mb-4">
      <dl class="grid grid-cols-2 lg:grid-cols-4 rounded-lg bg-white border border-gray-200 shadow-xs divide-y divide-gray-200 sm:divide-y-0 sm:divide-x overflow-hidden">
        
        <!-- Métrica 1: Progresso Geral -->
        <div class="px-3.5 py-3 sm:px-4 sm:py-3.5 flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <dt class="text-[11px] font-bold text-gray-500 uppercase tracking-wider">Progresso Geral</dt>
            <span id="global-fraction" class="text-[11px] text-gray-500 font-medium">0 / {total_disc_items}</span>
          </div>
          <dd class="mt-1 flex items-baseline justify-between">
            <span id="global-pct" class="text-xl sm:text-2xl font-bold text-gray-900 tracking-tight">0.0%</span>
            <span class="text-[10px] font-semibold text-indigo-600 bg-indigo-50 px-1.5 py-0.5 rounded border border-indigo-100">10 Matérias</span>
          </dd>
          <div class="w-full bg-gray-100 h-1.5 rounded-full overflow-hidden mt-2">
            <div id="global-progress-bar" class="h-full bg-indigo-600 rounded-full transition-all duration-300" style="width: 0%"></div>
          </div>
        </div>

        <!-- Métrica 2: Núcleo de Ferro (Nível A) -->
        <div class="px-3.5 py-3 sm:px-4 sm:py-3.5 flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <dt class="text-[11px] font-bold text-gray-500 uppercase tracking-wider">Núcleo de Ferro (A)</dt>
            <span id="stat-tier-a-frac" class="text-[11px] text-gray-500 font-medium">0 / {tier_a_total_count}</span>
          </div>
          <dd class="mt-1 flex items-baseline justify-between">
            <span id="stat-tier-a" class="text-xl sm:text-2xl font-bold text-gray-900 tracking-tight">0%</span>
            <span class="text-[10px] font-semibold text-amber-700 bg-amber-50 px-1.5 py-0.5 rounded border border-amber-200">Peso 80-100%</span>
          </dd>
          <div class="w-full bg-gray-100 h-1.5 rounded-full overflow-hidden mt-2">
            <div id="tier-a-bar" class="h-full bg-amber-500 rounded-full transition-all duration-300" style="width: 0%"></div>
          </div>
        </div>

        <!-- Métrica 3: Carga Horária Estimada -->
        <div class="px-3.5 py-3 sm:px-4 sm:py-3.5 flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <dt class="text-[11px] font-bold text-gray-500 uppercase tracking-wider">Carga Estimada</dt>
            <span class="text-[11px] text-gray-500 font-medium">Meta: 1.080h líq.</span>
          </div>
          <dd class="mt-1 flex items-baseline justify-between">
            <span id="stat-hours" class="text-xl sm:text-2xl font-bold text-gray-900 tracking-tight">0h</span>
            <span class="text-[10px] font-semibold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200">18-25h/sem</span>
          </dd>
          <div class="w-full bg-gray-100 h-1.5 rounded-full overflow-hidden mt-2">
            <div id="hours-bar" class="h-full bg-emerald-500 rounded-full transition-all duration-300" style="width: 0%"></div>
          </div>
        </div>

        <!-- Métrica 4: Tópicos Pendentes -->
        <div class="px-3.5 py-3 sm:px-4 sm:py-3.5 flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <dt class="text-[11px] font-bold text-gray-500 uppercase tracking-wider">Pendências</dt>
            <span class="text-[11px] text-gray-500 font-medium">restantes</span>
          </div>
          <dd class="mt-1 flex items-baseline justify-between">
            <span id="stat-pending" class="text-xl sm:text-2xl font-bold text-gray-900 tracking-tight">{total_disc_items}</span>
            <span class="inline-flex items-center gap-1 text-[10px] font-semibold text-purple-700 bg-purple-50 px-1.5 py-0.5 rounded border border-purple-200">
              <span class="h-1.5 w-1.5 rounded-full bg-purple-500"></span> Ciclo Ativo
            </span>
          </dd>
          <div class="w-full bg-gray-100 h-1.5 rounded-full overflow-hidden mt-2">
            <div id="pending-bar" class="h-full bg-purple-500 rounded-full transition-all duration-300" style="width: 100%"></div>
          </div>
        </div>

      </dl>
    </section>

    <!-- TOOLBAR UNIFICADA (Busca, Filtros Segmentados, Seletor de Disciplina e Ações) -->
    <div id="controls-bar" class="bg-white rounded-lg border border-gray-200 shadow-xs p-2.5 sm:px-3 sm:py-2.5 mb-4 flex flex-col md:flex-row md:items-center justify-between gap-3">
      
      <!-- Campo de Busca Compacto (Tailwind UI input_with_leading_icon) -->
      <div class="relative flex-1 min-w-[200px] max-w-md">
        <div class="absolute inset-y-0 left-0 pl-2.5 flex items-center pointer-events-none text-gray-400">
          <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
        </div>
        <input type="text" id="search-input" oninput="applyFilters()" placeholder="Buscar tópico, tecnologia, lei (ex: SQL, Crase, OWASP)..." class="block w-full pl-8 pr-3 py-1.5 text-xs sm:text-sm bg-gray-50 border border-gray-200 rounded-md placeholder-gray-400 text-gray-900 focus:bg-white focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500">
      </div>

      <!-- Controles: Filtros Segmentados + Seletor de Salto + Expandir/Recolher -->
      <div class="flex items-center flex-wrap gap-2.5">
        
        <!-- Segmented Control de Filtros (Padrão Tailwind UI tabs_in_pills_on_gray) -->
        <div class="inline-flex p-0.5 bg-gray-100 rounded-md text-xs font-medium">
          <button type="button" id="filter-all" onclick="setFilter('all')" class="filter-btn px-2.5 py-1 rounded bg-white text-gray-900 font-semibold shadow-xs transition-all">
            Todos (<span id="count-filter-all">{total_disc_items}</span>)
          </button>
          <button type="button" id="filter-pending" onclick="setFilter('pending')" class="filter-btn px-2.5 py-1 rounded text-gray-600 hover:text-gray-900 transition-all">
            Pendentes (<span id="count-filter-pending">{total_disc_items}</span>)
          </button>
          <button type="button" id="filter-completed" onclick="setFilter('completed')" class="filter-btn px-2.5 py-1 rounded text-gray-600 hover:text-gray-900 transition-all">
            Concluídos 🟡 (<span id="count-filter-completed">0</span>)
          </button>
        </div>

        <!-- Seletor Nativo de Salto Rápido para Disciplina (Tailwind UI simple_native select) -->
        <div class="flex items-center gap-1.5">
          <select id="discipline-select" onchange="jumpToDiscipline(this.value)" class="h-8 text-xs bg-white border border-gray-300 rounded-md py-1 pl-2.5 pr-7 text-gray-700 font-medium focus:ring-indigo-500 focus:border-indigo-500">
            <option value="">Ir para disciplina...</option>
"""

short_names = {
    1: "Português",
    2: "RLM & Estatística",
    3: "Constitucional",
    4: "Administrativo",
    5: "Bancos de Dados",
    6: "Eng. Software",
    7: "Ciência de Dados",
    8: "Segurança da Informação",
    9: "Redes & SO",
    10: "Governança de TI"
}

for d in disciplines:
    num = d["num"]
    short_title = short_names.get(num, d["title"].split("(")[0].strip())
    c_in_d = sum(len(g["items"]) for g in d["groups"]) + len(d.get("checklists", []))
    html_content += f"""            <option value="disc_{num}">{num}. {html.escape(short_title)} ({c_in_d} tópicos)</option>\n"""

html_content += """          </select>
        </div>

        <!-- Botões de Expandir / Recolher Tudo -->
        <div class="inline-flex rounded-md shadow-xs h-8" role="group">
          <button type="button" onclick="toggleAllCards(true)" class="inline-flex items-center px-2 py-1 text-xs font-medium text-gray-700 bg-white border border-gray-300 rounded-l-md hover:bg-gray-50 focus:z-10 focus:ring-1 focus:ring-indigo-500" title="Expandir Todas as Matérias">
            <svg class="h-3.5 w-3.5 mr-1 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            Expandir
          </button>
          <button type="button" onclick="toggleAllCards(false)" class="inline-flex items-center px-2 py-1 text-xs font-medium text-gray-700 bg-white border-t border-b border-r border-gray-300 rounded-r-md hover:bg-gray-50 focus:z-10 focus:ring-1 focus:ring-indigo-500" title="Recolher Todas as Matérias">
            <svg class="h-3.5 w-3.5 mr-1 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/></svg>
            Recolher
          </button>
        </div>

      </div>

    </div>

    <!-- CONTEÚDO DA ABA 1: DISCIPLINAS ({total_disc_items} ITENS) -->
    <div id="tab-disciplinas" class="tab-content space-y-3.5">
"""

# Gerar Cards de cada Disciplina com Padrão Tailwind UI Stacked List
for d in disciplines:
    num = d["num"]
    disc_id = d["id"]
    title = d["title"]
    tier = d["tier"]
    incidence = d["incidence"]
    tier_desc = d.get("tier_desc", "")
    groups = d["groups"]
    checklists = d.get("checklists", [])

    total_in_disc = sum(len(g["items"]) for g in groups) + len(checklists)
    is_tier_a = "Nível A" in tier

    tier_short = html.escape(tier.split('(')[0].strip())
    tier_badge_html = f"""<span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-medium {'bg-amber-50 text-amber-800 border border-amber-200' if is_tier_a else 'bg-blue-50 text-blue-800 border border-blue-200'}">{tier_short}</span>"""

    html_content += f"""
      <!-- CARD DISCIPLINA {num}: {html.escape(title)} -->
      <div class="discipline-card open bg-white rounded-lg border border-gray-200 shadow-xs overflow-hidden transition-all duration-150 hover:border-gray-300" id="{disc_id}" data-disc-num="{num}">
        
        <!-- Accordion Header -->
        <div class="px-4 py-3 sm:px-5 sm:py-3.5 bg-white hover:bg-gray-50/80 cursor-pointer flex flex-wrap items-center justify-between gap-3 select-none" onclick="toggleCard('{disc_id}')">
          
          <div class="flex items-center gap-3 flex-1 min-w-[260px]">
            <div class="h-8 w-8 rounded-md bg-indigo-50 border border-indigo-100 flex items-center justify-center text-indigo-700 font-bold text-xs flex-shrink-0">
              {num}
            </div>
            <div class="min-w-0">
              <h2 class="text-sm sm:text-base font-bold text-gray-900 truncate tracking-tight">{html.escape(title)}</h2>
              <div class="flex items-center flex-wrap gap-1.5 mt-0.5">
                {tier_badge_html}
                <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-medium bg-gray-100 text-gray-600 border border-gray-200">
                  Editais: {html.escape(incidence)}
                </span>
                <span class="hidden md:inline-block text-[11px] text-gray-400 truncate max-w-sm">
                  {html.escape(tier_desc)}
                </span>
              </div>
            </div>
          </div>

          <!-- Lado Direito: Progresso e Chevron -->
          <div class="flex items-center gap-3 flex-shrink-0">
            <div class="text-right">
              <div class="flex items-baseline justify-end gap-1">
                <span id="{disc_id}-prog-pct" class="text-xs font-bold text-gray-900">0%</span>
                <span id="{disc_id}-prog-frac" class="text-[11px] text-gray-500 font-medium">0 / {total_in_disc}</span>
              </div>
              <div class="w-20 sm:w-24 h-1.5 bg-gray-100 rounded-full overflow-hidden mt-1">
                <div id="{disc_id}-bar" class="h-full bg-indigo-600 rounded-full transition-all duration-300" style="width: 0%"></div>
              </div>
            </div>

            <svg class="chevron-icon h-4.5 w-4.5 text-gray-400 transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </div>

        </div>

        <!-- Accordion Body -->
        <div class="card-body px-4 py-3.5 sm:px-5 sm:py-4 border-t border-gray-100 space-y-4 bg-gray-50/40">
          
          <!-- Barra de Ações Rápidas -->
          <div class="flex flex-wrap items-center justify-between gap-2 text-xs pb-2 border-b border-gray-200/70">
            <div class="flex items-center gap-2.5">
              <button type="button" onclick="markAllInDisc('{disc_id}', true); event.stopPropagation();" class="inline-flex items-center font-semibold text-indigo-600 hover:text-indigo-800">
                <svg class="h-3.5 w-3.5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                Marcar todos como concluídos
              </button>
              <span class="text-gray-300">|</span>
              <button type="button" onclick="markAllInDisc('{disc_id}', false); event.stopPropagation();" class="font-medium text-gray-500 hover:text-gray-700">
                Desmarcar todos
              </button>
            </div>
            <span class="text-[11px] text-gray-400 font-medium">{total_in_disc} tópicos mapeados</span>
          </div>
"""

    # Grupos de Tópicos
    for g in groups:
        g_title = g["title"]
        html_content += f"""
          <div class="subtopic-group space-y-1.5">
            <div class="text-[11px] font-bold uppercase tracking-wider text-gray-500 px-1">
              {html.escape(g_title)}
            </div>
            <div class="bg-white rounded-lg border border-gray-200 shadow-2xs divide-y divide-gray-100 overflow-hidden">
"""
        for it in g["items"]:
            it_id = it["id"]
            it_text = it["text"]
            html_content += f"""
              <div class="item-row flex items-start sm:items-center justify-between gap-3 px-3.5 py-2.5 hover:bg-gray-50 cursor-pointer transition-colors group" id="{it_id}" data-item-id="{it_id}" data-disc-id="{disc_id}" onclick="toggleItem('{it_id}')">
                <div class="flex items-start sm:items-center gap-2.5 flex-1 min-w-0">
                  <input type="checkbox" class="item-checkbox mt-0.5 sm:mt-0 h-4 w-4 rounded border-gray-300 text-amber-500 focus:ring-amber-400 cursor-pointer flex-shrink-0" id="chk_{it_id}" onclick="event.stopPropagation(); toggleItem('{it_id}');">
                  <span class="item-text text-xs sm:text-sm text-gray-800 leading-normal select-none">{format_item_html(it_text)}</span>
                </div>
                <div class="flex items-center gap-1.5 flex-shrink-0">
                  <span class="item-status-badge hidden text-[11px] font-semibold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-300">✓ Concluído</span>
                  <button type="button" class="copy-btn p-1 text-gray-400 hover:text-gray-700 hover:bg-gray-100 rounded transition-colors" title="Copiar tópico" onclick="copyTopicText('{it_id}', event)">
                    <svg class="h-3.5 w-3.5 copy-icon-default" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
                    </svg>
                    <svg class="h-3.5 w-3.5 copy-icon-success hidden text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                    </svg>
                  </button>
                </div>
              </div>
"""
        html_content += """            </div>
          </div>
"""

    # Checklist de Domínio Técnico Pré-Edital (Definição de Pronto)
    if checklists:
        html_content += f"""
          <div class="section-checklist-box rounded-lg border border-emerald-200 bg-emerald-50/30 overflow-hidden mt-3 shadow-2xs">
            <div class="px-3.5 py-2 bg-emerald-50/80 border-b border-emerald-200 flex items-center gap-2">
              <svg class="h-4 w-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <h3 class="text-[11px] font-bold text-emerald-900 uppercase tracking-wider">Checklist de Domínio Técnico Pré-Edital (Definição de Pronto)</h3>
            </div>
            <div class="divide-y divide-emerald-100 bg-white/70">
"""
        for chk in checklists:
            chk_id = chk["id"]
            chk_text = chk["text"]
            html_content += f"""
              <div class="chk-row flex items-start sm:items-center justify-between gap-3 px-3.5 py-2.5 hover:bg-emerald-50/60 cursor-pointer transition-colors group" id="{chk_id}" data-item-id="{chk_id}" data-disc-id="{disc_id}" onclick="toggleItem('{chk_id}')">
                <div class="flex items-start sm:items-center gap-2.5 flex-1 min-w-0">
                  <input type="checkbox" class="item-checkbox mt-0.5 sm:mt-0 h-4 w-4 rounded border-emerald-400 text-amber-500 focus:ring-amber-400 cursor-pointer flex-shrink-0" id="chk_{chk_id}" onclick="event.stopPropagation(); toggleItem('{chk_id}');">
                  <span class="chk-text text-xs sm:text-sm text-gray-800 leading-normal select-none">{format_item_html(chk_text)}</span>
                </div>
                <div class="flex items-center gap-1.5 flex-shrink-0">
                  <span class="item-status-badge hidden text-[11px] font-semibold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-300">✓ Pronto</span>
                  <button type="button" class="copy-btn p-1 text-gray-400 hover:text-gray-700 hover:bg-emerald-100/60 rounded transition-colors" title="Copiar checklist" onclick="copyTopicText('{chk_id}', event)">
                    <svg class="h-3.5 w-3.5 copy-icon-default" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
                    </svg>
                    <svg class="h-3.5 w-3.5 copy-icon-success hidden text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                    </svg>
                  </button>
                </div>
              </div>
"""
        html_content += """            </div>
          </div>
"""

    html_content += """        </div>
      </div>
"""

html_content += """    </div>

    <!-- CONTEÚDO DA ABA 2: CRONOGRAMA SEMESTRAL (23 MESES) -->
    <div id="tab-cronograma" class="tab-content space-y-4" style="display: none;">
"""

for sem in semesters:
    sem_id = sem["id"]
    sem_title = sem["title"]
    sem_period = sem["period"]
    sem_meta = sem["meta"]
    months = sem["months"]

    html_content += f"""
      <div class="semester-card bg-white rounded-lg border border-gray-200 shadow-xs p-4 sm:p-5">
        <div class="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-gray-100">
          <div class="flex items-center gap-2">
            <h2 class="text-sm sm:text-base font-bold text-gray-900">{html.escape(sem_title)}</h2>
            <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200">
              {html.escape(sem_period)}
            </span>
          </div>
          <span class="text-xs text-gray-500">{html.escape(sem_meta)}</span>
        </div>

        <div class="mt-3 bg-white rounded-lg border border-gray-200 shadow-2xs divide-y divide-gray-100 overflow-hidden">
"""
    for m in months:
        m_id = m["id"]
        m_name = m["month"]
        m_subj = m["subjects"]
        m_tgt = m["target"]

        html_content += f"""
          <div class="month-row flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-3.5 py-3 hover:bg-gray-50 cursor-pointer transition-colors group" id="{m_id}" data-item-id="{m_id}" onclick="toggleItem('{m_id}')">
            <div class="flex items-center gap-2.5 min-w-[150px]">
              <input type="checkbox" class="item-checkbox h-4 w-4 rounded border-gray-300 text-amber-500 focus:ring-amber-400 cursor-pointer flex-shrink-0" id="chk_{m_id}" onclick="event.stopPropagation(); toggleItem('{m_id}');">
              <span class="month-name text-xs sm:text-sm font-bold text-gray-900 select-none">{html.escape(m_name)}</span>
            </div>
            <div class="month-subjects text-xs sm:text-sm text-gray-600 flex-1 sm:px-3">
              {format_item_html(m_subj)}
            </div>
            <div class="flex items-center gap-2 flex-shrink-0">
              <span class="month-target text-[11px] font-medium px-2 py-0.5 rounded bg-gray-100 text-gray-600 border border-gray-200">
                {format_item_html(m_tgt)}
              </span>
              <span class="item-status-badge hidden text-[11px] font-semibold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-300">✓ Concluído</span>
              <button type="button" class="copy-btn p-1 text-gray-400 hover:text-gray-700 hover:bg-gray-100 rounded transition-colors" title="Copiar mês" onclick="copyTopicText('{m_id}', event)">
                <svg class="h-3.5 w-3.5 copy-icon-default" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
                </svg>
                <svg class="h-3.5 w-3.5 copy-icon-success hidden text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </button>
            </div>
          </div>
"""
    html_content += """        </div>
      </div>
"""

html_content += """    </div>

    <!-- CONTEÚDO DA ABA 3: DISCURSIVAS DE ELITE (6 TEMAS) -->
    <div id="tab-discursivas" class="tab-content space-y-4" style="display: none;">
      
      <div class="bg-indigo-50/60 border border-indigo-200 rounded-lg p-3.5 sm:p-4">
        <h2 class="text-xs sm:text-sm font-bold text-indigo-950 flex items-center gap-2">
          <span>✍️ Os 6 Temas Decisivos para Discursivas de TI (> R$ 30k)</span>
        </h2>
        <p class="text-xs text-indigo-900/80 mt-1">
          No Senado, Câmara, TCU e Bacen, as discursivas eliminam até 60% dos aprovados na prova objetiva. Clique no card quando tiver redigido e simulado o tema sob limite de 30 a 60 linhas com padrão de resposta.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5">
"""

for dsc in discursivas:
    d_id = dsc["id"]
    d_title = dsc["title"]
    d_tech = dsc["tech"]
    d_inc = dsc["incidence"]

    html_content += f"""
        <div class="discursiva-card bg-white rounded-lg border border-gray-200 shadow-xs p-4 cursor-pointer hover:border-gray-300 transition-all flex flex-col justify-between group" id="{d_id}" data-item-id="{d_id}" onclick="toggleItem('{d_id}')">
          <div>
            <div class="flex items-start justify-between gap-2 mb-2">
              <h3 class="text-xs sm:text-sm font-bold text-gray-900 leading-snug">{format_item_html(d_title)}</h3>
              <div class="flex items-center gap-1.5 flex-shrink-0">
                <button type="button" class="copy-btn p-1 text-gray-400 hover:text-gray-700 hover:bg-gray-100 rounded transition-colors" title="Copiar tema discursiva" onclick="copyTopicText('{d_id}', event)">
                  <svg class="h-3.5 w-3.5 copy-icon-default" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
                  </svg>
                  <svg class="h-3.5 w-3.5 copy-icon-success hidden text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                </button>
                <input type="checkbox" class="item-checkbox mt-0.5 h-4 w-4 rounded border-gray-300 text-amber-500 focus:ring-amber-400 cursor-pointer flex-shrink-0" id="chk_{d_id}" onclick="event.stopPropagation(); toggleItem('{d_id}');">
              </div>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed mb-3">
              <strong class="font-semibold text-gray-800">Conceitos-Chave:</strong> {format_item_html(d_tech)}
            </p>
          </div>
          <div class="flex items-center justify-between pt-2.5 border-t border-gray-100">
            <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-medium bg-gray-100 text-gray-600">
              Editais: {html.escape(d_inc)}
            </span>
            <span class="item-status-badge hidden text-[11px] font-semibold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-300">✓ Redigido</span>
          </div>
        </div>
"""

html_content += """      </div>
    </div>

    <!-- CONTEÚDO DA ABA 4: BACKUP & PROTOCOLO ANTI-FRACASSO -->
    <div id="tab-backup" class="tab-content space-y-4" style="display: none;">
      
      <!-- Painel de Gerenciamento de Backup -->
      <div class="bg-white rounded-lg border border-gray-200 shadow-xs p-4 sm:p-5 space-y-3">
        <h2 class="text-sm sm:text-base font-bold text-gray-900 flex items-center gap-2">
          <span>💾 Backup e Sincronização Local</span>
        </h2>
        <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
          Seus dados e cliques são persistidos continuamente no <code class="bg-gray-100 px-1.5 py-0.5 rounded text-indigo-700 font-mono text-xs">localStorage</code> deste navegador. Se você quiser transferir seus estudos para outro computador ou guardar uma cópia de segurança, utilize as opções abaixo:
        </p>
        <div class="flex flex-wrap items-center gap-2.5 pt-1">
          <button type="button" onclick="exportProgress()" class="inline-flex items-center px-3 py-1.5 border border-gray-300 shadow-xs text-xs font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            📥 Exportar Progresso (Baixar JSON)
          </button>
          <button type="button" onclick="document.getElementById('import-file-input').click()" class="inline-flex items-center px-3 py-1.5 border border-gray-300 shadow-xs text-xs font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            📤 Importar Progresso (Carregar JSON)
          </button>
          <button type="button" onclick="resetAllProgress()" class="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-md text-red-700 bg-red-50 hover:bg-red-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
            🗑️ Resetar Todo o Progresso
          </button>
        </div>
      </div>

      <!-- Protocolo Anti-Fracasso -->
      <div class="bg-white rounded-lg border border-gray-200 shadow-xs p-4 sm:p-5 space-y-3">
        <h2 class="text-sm sm:text-base font-bold text-gray-900 flex items-center gap-2">
          <span>🎯 Protocolo Anti-Fracasso: Condições para a Força Real</span>
        </h2>
        <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
          Estudar apenas a teoria é condição necessária, mas <strong>não suficiente</strong> para aprovação nos concursos de topo (Senado, TCU, Bacen, CVM). Para transformar estudo em vaga, cumpra as métricas objetivas:
        </p>
        <ul class="space-y-2 text-xs sm:text-sm text-gray-700 pt-1">
          <li class="flex items-start gap-2.5">
            <span class="h-5 w-5 rounded-full bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">1</span>
            <span><strong class="font-semibold text-gray-900">Volume Acumulado:</strong> Resolver entre 18.000 e 25.000 questões até 2028 (média de 150 a 200 questões/semana comentadas).</span>
          </li>
          <li class="flex items-start gap-2.5">
            <span class="h-5 w-5 rounded-full bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">2</span>
            <span><strong class="font-semibold text-gray-900">Repetição Espaçada Diária (Anki):</strong> Manter taxa de retenção dos cards maduros acima de 85% para protocolos de rede, fórmulas de inferência e jurisprudência administrativa.</span>
          </li>
          <li class="flex items-start gap-2.5">
            <span class="h-5 w-5 rounded-full bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">3</span>
            <span><strong class="font-semibold text-gray-900">Simulados com Discursiva Manuscrita:</strong> Redigir 1 questão discursiva por semana a partir do Semestre 2 sob limite estrito de tempo com caneta preta.</span>
          </li>
          <li class="flex items-start gap-2.5">
            <span class="h-5 w-5 rounded-full bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">4</span>
            <span><strong class="font-semibold text-gray-900">Velocidade de Prova:</strong> Manter tempo médio de resolução abaixo de 2min30s por questão objetiva em baterias completas de 70 questões.</span>
          </li>
        </ul>
      </div>

    </div>

  </main>

  <!-- NOTIFICAÇÃO TOAST FLUTUANTE (Tailwind UI Notification) -->
  <div id="toast-msg" class="toast fixed bottom-5 right-5 z-50 opacity-0 translate-y-2 pointer-events-none bg-gray-900 text-white text-xs sm:text-sm font-medium py-2.5 px-4 rounded-lg shadow-lg flex items-center gap-2 border border-gray-800">
    <svg class="h-4 w-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
    </svg>
    <span id="toast-text">Progresso salvo com sucesso!</span>
  </div>

  <!-- SCRIPT JS INTERATIVO E PERSISTÊNCIA -->
  <script>
    const STORAGE_KEY = 'concursos_elite_checklist_v1';
    let completedItems = new Set();
    let currentFilter = 'all';

    // Inicialização ao carregar o DOM
    document.addEventListener('DOMContentLoaded', () => {
      loadProgress();
      updateUI();
    });

    // Carrega dados salvos do localStorage
    function loadProgress() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) {
          const arr = JSON.parse(raw);
          completedItems = new Set(arr);
        }
      } catch (e) {
        console.error("Erro ao ler localStorage:", e);
        completedItems = new Set();
      }
    }

    // Salva continuamente no localStorage
    function saveProgress() {
      try {
        const arr = Array.from(completedItems);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(arr));
        showToast("✓ Progresso salvo!");
      } catch (e) {
        console.error("Erro ao salvar no localStorage:", e);
      }
    }

    // Copia o texto do item para a área de transferência sem alternar o checkbox
    function copyTopicText(id, event) {
      if (event) {
        event.stopPropagation();
      }
      const el = document.getElementById(id);
      if (!el) return;

      const textEl = el.querySelector('.item-text, .chk-text, .month-subjects') || el;
      const textToCopy = (textEl.innerText || textEl.textContent || '').trim();

      if (!textToCopy) return;

      const btn = event ? event.currentTarget : el.querySelector('.copy-btn');
      const iconDef = btn ? btn.querySelector('.copy-icon-default') : null;
      const iconSucc = btn ? btn.querySelector('.copy-icon-success') : null;

      function onCopied() {
        if (iconDef && iconSucc) {
          iconDef.classList.add('hidden');
          iconSucc.classList.remove('hidden');
          btn.classList.add('text-emerald-600', 'bg-emerald-50');
          setTimeout(() => {
            iconDef.classList.remove('hidden');
            iconSucc.classList.add('hidden');
            btn.classList.remove('text-emerald-600', 'bg-emerald-50');
          }, 1500);
        }
        const preview = textToCopy.length > 45 ? textToCopy.slice(0, 45) + '...' : textToCopy;
        showToast('📋 Copiado: ' + preview);
      }

      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(textToCopy).then(onCopied).catch(() => {
          fallbackCopy(textToCopy, onCopied);
        });
      } else {
        fallbackCopy(textToCopy, onCopied);
      }
    }

    function fallbackCopy(text, cb) {
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.left = "-9999px";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        document.execCommand('copy');
        if (cb) cb();
      } catch (err) {
        showToast("Erro ao copiar.");
      }
      document.body.removeChild(textArea);
    }

    // Alterna o estado de um item clicado (fica amarelo suave quando concluído)
    function toggleItem(id) {
      const el = document.getElementById(id);
      const chk = document.getElementById('chk_' + id);

      if (completedItems.has(id)) {
        completedItems.delete(id);
        if (el) el.classList.remove('concluida');
        if (chk) chk.checked = false;
      } else {
        completedItems.add(id);
        if (el) el.classList.add('concluida');
        if (chk) chk.checked = true;
      }

      saveProgress();
      updateUI();
    }

    // Atualiza contadores, porcentagens e barras de progresso
    function updateUI() {
      // 1. Atualizar visual de todos os elementos interativos
      document.querySelectorAll('[data-item-id]').forEach(el => {
        const id = el.getAttribute('data-item-id');
        const chk = document.getElementById('chk_' + id);
        if (completedItems.has(id)) {
          el.classList.add('concluida');
          if (chk) chk.checked = true;
        } else {
          el.classList.remove('concluida');
          if (chk) chk.checked = false;
        }
      });

      // 2. Progresso Geral das 10 Disciplinas
      const allDiscRows = document.querySelectorAll('#tab-disciplinas [data-item-id]');
      const totalDiscCount = allDiscRows.length || {total_disc_items};
      let completedDiscCount = 0;

      allDiscRows.forEach(el => {
        const id = el.getAttribute('data-item-id');
        if (completedItems.has(id)) completedDiscCount++;
      });

      const globalPct = totalDiscCount > 0 ? ((completedDiscCount / totalDiscCount) * 100).toFixed(1) : '0.0';
      const globalPctEl = document.getElementById('global-pct');
      const globalFracEl = document.getElementById('global-fraction');
      const globalBarEl = document.getElementById('global-progress-bar');
      if (globalPctEl) globalPctEl.textContent = globalPct + '%';
      if (globalFracEl) globalFracEl.textContent = `${completedDiscCount} / ${totalDiscCount}`;
      if (globalBarEl) globalBarEl.style.width = globalPct + '%';

      // 3. Progresso por Disciplina
      document.querySelectorAll('.discipline-card').forEach(card => {
        const discId = card.id;
        const rows = card.querySelectorAll('[data-item-id]');
        const totalInDisc = rows.length;
        let compInDisc = 0;

        rows.forEach(r => {
          if (completedItems.has(r.getAttribute('data-item-id'))) compInDisc++;
        });

        const pct = totalInDisc > 0 ? Math.round((compInDisc / totalInDisc) * 100) : 0;
        const pctEl = document.getElementById(discId + '-prog-pct');
        const fracEl = document.getElementById(discId + '-prog-frac');
        const barEl = document.getElementById(discId + '-bar');

        if (pctEl) pctEl.textContent = pct + '%';
        if (fracEl) fracEl.textContent = `${compInDisc} / ${totalInDisc}`;
        if (barEl) barEl.style.width = pct + '%';
      });

      // 4. Progresso Nível A (Disciplinas 1 a 5)
      let tierATotal = 0;
      let tierAComp = 0;
      for (let i = 1; i <= 5; i++) {
        const dCard = document.getElementById('disc_' + i);
        if (dCard) {
          const rows = dCard.querySelectorAll('[data-item-id]');
          tierATotal += rows.length;
          rows.forEach(r => {
            if (completedItems.has(r.getAttribute('data-item-id'))) tierAComp++;
          });
        }
      }
      const tierAPct = tierATotal > 0 ? Math.round((tierAComp / tierATotal) * 100) : 0;
      const tierAEl = document.getElementById('stat-tier-a');
      const tierAFracEl = document.getElementById('stat-tier-a-frac');
      const tierABarEl = document.getElementById('tier-a-bar');
      if (tierAEl) tierAEl.textContent = tierAPct + '%';
      if (tierAFracEl) tierAFracEl.textContent = `${tierAComp} / ${tierATotal}`;
      if (tierABarEl) tierABarEl.style.width = tierAPct + '%';

      // 5. Horas Estimadas (Proporcional a 1.080h líquidas)
      const hoursEst = Math.round((completedDiscCount / totalDiscCount) * 1080);
      const hoursEl = document.getElementById('stat-hours');
      const hoursBarEl = document.getElementById('hours-bar');
      if (hoursEl) hoursEl.textContent = hoursEst + 'h';
      if (hoursBarEl) hoursBarEl.style.width = globalPct + '%';

      // 6. Contadores de Pendências e Filtros
      const pendingCount = totalDiscCount - completedDiscCount;
      const pendingEl = document.getElementById('stat-pending');
      const pendingBarEl = document.getElementById('pending-bar');
      if (pendingEl) pendingEl.textContent = pendingCount;
      if (pendingBarEl) {
        const pendPct = totalDiscCount > 0 ? ((pendingCount / totalDiscCount) * 100) : 100;
        pendingBarEl.style.width = pendPct + '%';
      }

      const fAll = document.getElementById('count-filter-all');
      const fPend = document.getElementById('count-filter-pending');
      const fComp = document.getElementById('count-filter-completed');
      if (fAll) fAll.textContent = totalDiscCount;
      if (fPend) fPend.textContent = pendingCount;
      if (fComp) fComp.textContent = completedDiscCount;

      // 7. Atualizar Badges das Abas (Desktop e Mobile)
      const discBadgeText = completedDiscCount > 0 ? `${completedDiscCount}/${totalDiscCount}` : `${totalDiscCount}`;
      const bDisc = document.getElementById('badge-tab-disciplinas');
      const bDiscMob = document.getElementById('badge-tab-disciplinas-mob');
      if (bDisc) bDisc.textContent = discBadgeText;
      if (bDiscMob) bDiscMob.textContent = discBadgeText;

      const allCronRows = document.querySelectorAll('#tab-cronograma [data-item-id]');
      let compCronCount = 0;
      allCronRows.forEach(el => {
        if (completedItems.has(el.getAttribute('data-item-id'))) compCronCount++;
      });
      const cronBadgeText = compCronCount > 0 ? `${compCronCount}/23` : '23m';
      const bCron = document.getElementById('badge-tab-cronograma');
      const bCronMob = document.getElementById('badge-tab-cronograma-mob');
      if (bCron) bCron.textContent = cronBadgeText;
      if (bCronMob) bCronMob.textContent = cronBadgeText;

      const allDiscurRows = document.querySelectorAll('#tab-discursivas [data-item-id]');
      let compDiscurCount = 0;
      allDiscurRows.forEach(el => {
        if (completedItems.has(el.getAttribute('data-item-id'))) compDiscurCount++;
      });
      const discurBadgeText = compDiscurCount > 0 ? `${compDiscurCount}/6` : '6';
      const bDiscur = document.getElementById('badge-tab-discursivas');
      const bDiscurMob = document.getElementById('badge-tab-discursivas-mob');
      if (bDiscur) bDiscur.textContent = discurBadgeText;
      if (bDiscurMob) bDiscurMob.textContent = discurBadgeText;

      applyFilters();
    }

    // Filtros de status (Todos, Pendentes, Concluídos)
    function setFilter(filterType) {
      currentFilter = filterType;
      ['all', 'pending', 'completed'].forEach(type => {
        const btn = document.getElementById('filter-' + type);
        if (btn) {
          if (type === filterType) {
            btn.className = 'filter-btn px-2.5 py-1 rounded bg-white text-gray-900 font-semibold shadow-xs transition-all';
          } else {
            btn.className = 'filter-btn px-2.5 py-1 rounded text-gray-600 hover:text-gray-900 transition-all';
          }
        }
      });
      applyFilters();
    }

    // Normalização para busca insensível a acentos e maiúsculas
    function normStr(str) {
      return (str || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
    }

    // Aplicação de filtros em tempo real e busca
    function applyFilters() {
      const q = normStr(document.getElementById('search-input').value);

      document.querySelectorAll('#tab-disciplinas .discipline-card').forEach(card => {
        let cardHasVisible = false;
        const discTitle = normStr(card.querySelector('h2')?.textContent);
        const discMatches = q && discTitle.includes(q);

        // Tópicos normais
        card.querySelectorAll('.subtopic-group').forEach(grp => {
          let grpHasVisible = false;
          const grpTitle = normStr(grp.querySelector('div')?.textContent);
          const grpMatches = q && grpTitle.includes(q);

          grp.querySelectorAll('.item-row').forEach(row => {
            const id = row.getAttribute('data-item-id');
            const text = normStr(row.querySelector('.item-text')?.textContent);
            const isDone = completedItems.has(id);

            let matchesSearch = !q || discMatches || grpMatches || text.includes(q);
            let matchesFilter = true;

            if (currentFilter === 'pending') matchesFilter = !isDone;
            if (currentFilter === 'completed') matchesFilter = isDone;

            if (matchesSearch && matchesFilter) {
              row.style.display = 'flex';
              grpHasVisible = true;
              cardHasVisible = true;
            } else {
              row.style.display = 'none';
            }
          });

          grp.style.display = grpHasVisible ? 'block' : 'none';
        });

        // Checklists de Domínio Técnico (esconde o box pai quando não há itens visíveis)
        card.querySelectorAll('.section-checklist-box').forEach(chkBox => {
          let chkBoxHasVisible = false;

          chkBox.querySelectorAll('.chk-row').forEach(chkRow => {
            const id = chkRow.getAttribute('data-item-id');
            const text = normStr(chkRow.querySelector('.chk-text')?.textContent);
            const isDone = completedItems.has(id);

            let matchesSearch = !q || discMatches || text.includes(q);
            let matchesFilter = true;

            if (currentFilter === 'pending') matchesFilter = !isDone;
            if (currentFilter === 'completed') matchesFilter = isDone;

            if (matchesSearch && matchesFilter) {
              chkRow.style.display = 'flex';
              chkBoxHasVisible = true;
              cardHasVisible = true;
            } else {
              chkRow.style.display = 'none';
            }
          });

          chkBox.style.display = chkBoxHasVisible ? 'block' : 'none';
        });

        // Exibir ou ocultar o card da matéria
        card.style.display = cardHasVisible ? 'block' : 'none';

        // Ao buscar, abre automaticamente os cards encontrados
        if (q && cardHasVisible) {
          card.classList.add('open');
        }
      });
    }

    // Alternar abertura de card individual
    function toggleCard(id) {
      const el = document.getElementById(id);
      if (el) el.classList.toggle('open');
    }

    // Expandir ou recolher todos
    function toggleAllCards(openState) {
      document.querySelectorAll('.discipline-card').forEach(card => {
        if (openState) card.classList.add('open');
        else card.classList.remove('open');
      });
    }

    // Salto rápido suave para disciplina
    function jumpToDiscipline(discId) {
      if (!discId) return;
      const el = document.getElementById(discId);
      if (el) {
        el.style.display = 'block';
        el.classList.add('open');
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    // Marcar ou desmarcar todos de uma disciplina
    function markAllInDisc(discId, state) {
      const card = document.getElementById(discId);
      if (!card) return;

      card.querySelectorAll('[data-item-id]').forEach(el => {
        const id = el.getAttribute('data-item-id');
        if (state) completedItems.add(id);
        else completedItems.delete(id);
      });

      saveProgress();
      updateUI();
    }

    // Navegação entre Abas (Sincronizada Desktop e Mobile)
    function switchTab(tabId, btnEl) {
      const baseId = tabId.replace('tab-', '');

      // Atualizar botões desktop
      document.querySelectorAll('.tab-nav-btn').forEach(b => {
        b.className = 'tab-nav-btn inline-flex items-center px-2.5 lg:px-3 py-1.5 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap';
        const badge = b.querySelector('span:nth-child(2)');
        if (badge) badge.className = 'ml-1.5 py-0.2 px-1.5 rounded-full text-[10px] font-medium bg-gray-200 text-gray-700';
      });
      const activeDesktopBtn = document.getElementById('tab-btn-' + baseId);
      if (activeDesktopBtn) {
        activeDesktopBtn.className = 'tab-nav-btn inline-flex items-center px-2.5 lg:px-3 py-1.5 text-xs font-semibold rounded-md text-indigo-700 bg-indigo-50 transition-all whitespace-nowrap';
        const badge = activeDesktopBtn.querySelector('span:nth-child(2)');
        if (badge) badge.className = 'ml-1.5 py-0.2 px-1.5 rounded-full text-[10px] font-bold bg-indigo-200/70 text-indigo-800';
      }

      // Atualizar botões mobile
      document.querySelectorAll('.tab-nav-btn-mob').forEach(b => {
        b.className = 'tab-nav-btn-mob inline-flex items-center px-2.5 py-1 text-xs font-medium rounded-md text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all whitespace-nowrap';
        const badge = b.querySelector('span:nth-child(2)');
        if (badge) badge.className = 'ml-1 py-0.2 px-1 rounded-full text-[10px] font-medium bg-gray-200 text-gray-700';
      });
      const activeMobBtn = document.getElementById('tab-btn-' + baseId + '-mob');
      if (activeMobBtn) {
        activeMobBtn.className = 'tab-nav-btn-mob inline-flex items-center px-2.5 py-1 text-xs font-semibold rounded-md text-indigo-700 bg-indigo-50 transition-all whitespace-nowrap';
        const badge = activeMobBtn.querySelector('span:nth-child(2)');
        if (badge) badge.className = 'ml-1 py-0.2 px-1 rounded-full text-[10px] font-bold bg-indigo-200/70 text-indigo-800';
      }

      document.querySelectorAll('.tab-content').forEach(c => c.style.display = 'none');
      const activeContent = document.getElementById(tabId);
      if (activeContent) activeContent.style.display = 'block';

      const controls = document.getElementById('controls-bar');
      if (controls) {
        controls.style.display = (tabId === 'tab-disciplinas') ? 'flex' : 'none';
      }
    }

    // Notificação Toast
    function showToast(msg) {
      const t = document.getElementById('toast-msg');
      const txt = document.getElementById('toast-text');
      if (txt) txt.textContent = msg;
      if (t) {
        t.classList.add('show');
        setTimeout(() => t.classList.remove('show'), 2200);
      }
    }

    // Exportar progresso para JSON
    function exportProgress() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(Array.from(completedItems), null, 2));
      const a = document.createElement('a');
      a.setAttribute("href", dataStr);
      a.setAttribute("download", "progresso_estudos_concurso_2028.json");
      document.body.appendChild(a);
      a.click();
      a.remove();
      showToast("📥 Backup exportado!");
    }

    // Importar progresso a partir de JSON
    function importProgress(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const arr = JSON.parse(e.target.result);
          if (Array.isArray(arr)) {
            completedItems = new Set(arr);
            saveProgress();
            updateUI();
            showToast("📤 Progresso restaurado!");
          } else {
            alert("Arquivo JSON inválido.");
          }
        } catch (err) {
          alert("Erro ao ler JSON: " + err.message);
        }
      };
      reader.readAsText(file);
    }

    // Resetar progresso
    function resetAllProgress() {
      if (confirm("Tem certeza de que deseja limpar todo o progresso salvo?")) {
        completedItems.clear();
        saveProgress();
        updateUI();
        showToast("🗑️ Progresso resetado.");
      }
    }
  </script>

</body>
</html>
"""

# Gravar o novo checklist_estudos.html
target_file = "/home/Hugo/Documentos/iniciando/checklist_estudos.html"
with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Sucesso! Gerado {target_file} ({len(html_content)} bytes)")
