# 🎯 Checklist de Estudos & Tronco Comum Antifrágil de TI (2026–2028)

> 🌐 **Acesse o Dashboard Online (GitHub Pages):**  
> 👉 **[https://hugopedro.github.io/checklist_estudos/](https://hugopedro.github.io/checklist_estudos/)**

Repositório estratégico e ecossistema de preparação de alto rendimento para os concursos públicos de elite na área de **Tecnologia da Informação, Ciência de Dados, Engenharia de Software, Infraestrutura, Segurança da Informação e Governança**, com foco em cargos estatutários de remuneração inicial superior a **R$ 25.000,00 – R$ 40.000,00+**.

---

## 🚀 Destaques do Projeto

### 1. Dashboard Interativo de Estudos (`index.html` / `checklist_estudos.html`)
Aplicação *standalone* (sem dependências de servidor ou banco externo), desenvolvida com padrões visuais modernos do **Tailwind UI** (modo claro, limpo e profissional):
- **698 Itens Atômicos Rastreados**:
  - **669 Tópicos Curriculares** divididos nas 10 disciplinas do Tronco Comum Antifrágil.
  - **23 Metas Mensais** de progressão cronológica rumo ao horizonte 2028.
  - **6 Temas Estratégicos de Provas Discursivas Técnicas**.
- **💾 Salvamento Automático & Sincronização Transparente na Nuvem**:
  - **Zero atrito e zero comandos:** Cada clique em qualquer tópico salva instantaneamente no navegador e sincroniza em segundo plano com a nuvem via API REST.
  - **URL Fixa e Limpa:** Não há hashes, fragmentos ou parâmetros dinâmicos na barra de endereços. A URL permanece sempre limpa: `https://hugopedro.github.io/checklist_estudos/`.
  - **Multi-dispositivos & Aba Anônima:** Ao abrir `https://hugopedro.github.io/checklist_estudos/` em qualquer computador, celular ou aba anônima, todos os seus tópicos marcados aparecem automaticamente restaurados da nuvem.
  - **Feedback visual imediato:** A linha fica destacada em amarelo suave (`.concluida`), o checkbox é marcado, o badge no topo exibe o status `☁️ Nuvem Ativa` e uma notificação *toast* confirma a gravação.
  - **Backup Físico JSON:** Use o botão **Exportar** para baixar seu progresso em arquivo JSON e **Importar** para restaurar offline a qualquer momento.
- **Ferramentas de Estudo Ágeis**:
  - Botão de cópia rápida 📋 ao lado de cada tópico (facilita colar comandos de prompt no ChatGPT, criar cards no Anki ou notas no Notion).
  - Barra de progresso geral e por disciplina calculadas em tempo real.
  - Filtros instantâneos: *Todos*, *Pendentes* e *Concluídos*, além de busca textual em tempo real.

### 2. Edital Âncora: O Efeito Guarda-Chuva
A estratégia adota o **Senado Federal (FGV)** como edital âncora mestre, complementado pelos editais da **Câmara dos Deputados (FGV)**, **TCU (FGV)**, **BACEN (Cebraspe)**, **Perito da Polícia Federal (Cebraspe)** e **Fiscos Estaduais**:
- **Blindagem Curricular**: Ao dominar 100% da ementa do Senado Federal, você cobre automaticamente entre 85% e 95% de qualquer certame de TI do país.
- **Isenção de Armadilhas**: O Edital Âncora possui **0% de Direito Tributário** e **0% de Cálculo Diferencial/Integral**, eliminando matérias alheias à vocação de TI sem perder competitividade.

---

## 📂 Estrutura do Repositório

```text
├── checklist_estudos.html             # Dashboard interativo com 698 itens e Tailwind UI
├── data_checklist.json                # Base estruturada dos tópicos e disciplinas
│
├── 📑 Manuais Estratégicos e Metodologia
│   ├── o_que_estudar_de_fato.md           # Bíblia curricular granular de todas as disciplinas
│   ├── edital_ancora_senado_federal.md    # Manual tático detalhado do Senado Federal FGV
│   ├── guia_superacao_materias_basicas.md # Método de aprovação em Português FGV, Direito e RLM
│   ├── meus_alvos.md                      # Teorema da Antifragilidade e portfólio de alvos
│   ├── matriz_incidencia_editais.md       # Análise cruzada da frequência dos temas nos editais
│   ├── sobreviventes.md                   # Auditoria de blindagem constitucional e risco institucional
│   ├── sobrevivencia_santos_detic.md      # Estudo de caso de resiliência municipal de TIC
│   ├── concursos_elite_19k_estatutarios.md# Raio-X de certames estatutários de curto prazo
│   ├── concursos_elite_19k_longo_prazo.md # Planejamento de médio/longo prazo (2027–2030)
│   └── concursos_elite_clt_28k.md         # Análise de estatais e sociedades de economia mista
│
├── 🏛️ Acervo Oficial de Editais (editais/)
│   ├── README.md                          # Tabela com SHA256, páginas e links de origem
│   ├── baixar_e_validar_editais.py        # Script de auditoria e download automatizado
│   ├── edital_01_senado_2022_analista_ti.pdf
│   ├── edital_02_camara_2023_analista_ti.pdf
│   ├── edital_03_bacen_2024_analista_ti.pdf
│   ├── edital_04_tcu_2021_aufc_ti.pdf
│   ├── edital_05_pf_2018_perito_ti.pdf
│   ├── edital_06_sefaz_sc_2026_auditor_ti.pdf
│   ├── edital_07_sefaz_mg_2022_auditor_ti.pdf
│   ├── edital_08_tcdf_2023_auditor_ti.pdf
│   ├── edital_09_cgu_2022_auditor_ti.pdf
│   ├── edital_10_cvm_2024_analista_inspetor_ti.pdf
│   └── extracted_it_syllabus/             # Ementas brutas em texto puro de cada edital
│
└── 🛠️ Pipeline de Geração e Compilação
    ├── compilar_dashboard_html.py         # Compilador principal do dashboard HTML
    ├── atualizar_json_e_dashboard.py      # Atualizador de dados atômicos
    ├── atualizar_planos_ti.py             # Integrador curricular
    ├── gerar_secoes_basicas.py            # Gerador dos módulos de matérias básicas
    ├── gerar_secoes_ti_core.py            # Gerador dos módulos de desenvolvimento e dados
    ├── gerar_secoes_ti_infra_gov.py       # Gerador dos módulos de redes, segurança e governança
    └── gerar_secoes_trilhas_vanguarda.py  # Gerador dos módulos de IA, cloud e discursivas
```

---

## 📊 Matriz das 10 Disciplinas do Tronco Comum

| # | Disciplina | Foco Principal | Editais de Referência |
| :-: | :--- | :--- | :--- |
| **01** | **Língua Portuguesa de Elite** | Semiótica, interpretação inferencial e estilo FGV | Senado, Câmara, TCU, Fiscos |
| **02** | **Raciocínio Lógico & Estatística** | Lógica formal, probabilidade, distribuições e inferência | FGV e Cebraspe |
| **03** | **Direito Constitucional Aplicado** | Direitos fundamentais, organização dos poderes e controle | Senado, TCU, CGU |
| **04** | **Direito Administrativo & TIC** | Lei 14.133/2021, contratações públicas de TI e agentes | Senado, TCU, CVM |
| **05** | **Bancos de Dados & Big Data** | Modelo ER, SQL avançado, normalização, NoSQL, Data Lake | Universal em TI |
| **06** | **Engenharia de Software & DevOps** | Ciclos ágeis, microsserviços, CI/CD, Git, testes e Clean Code | Senado, Câmara, BACEN |
| **07** | **Ciência de Dados, Python & IA** | Pandas, Machine Learning, Deep Learning, LLMs e RAG | BACEN, TCU, Senado, CVM |
| **08** | **Segurança da Informação & Forense** | Criptografia, OWASP, ISO 27001/2, Zero Trust, Forense Digital | PF, BACEN, Senado, TCDF |
| **09** | **Redes, SO, Cloud & Contêineres** | TCP/IP, Linux avançado, Docker, Kubernetes, AWS e Azure | BACEN, TCU, PF, Senado |
| **10** | **Governança de TI & Metodologias Ágeis** | COBIT 2019, ITIL 4, PMBOK 7, Scrum, Kanban e DMBOK 2 | TCU, Senado, CGU, SEFAZ |

---

## 🖥️ Como Utilizar

1. **Acessar o Dashboard**:
   Basta clonar este repositório e abrir o arquivo `checklist_estudos.html` em qualquer navegador web moderno:
   ```bash
   git clone https://github.com/hugopedro/checklist_estudos.git
   cd checklist_estudos
   # No Linux:
   xdg-open checklist_estudos.html
   ```
2. **Acompanhar o Progresso**:
   - Conforme você estuda e resolve baterias de questões de cada subtema, clique na respectiva linha para marcá-la.
   - A barra de progresso no cabeçalho será atualizada automaticamente e salva no navegador.
3. **Consulte os Manuais**:
   - Para entender a profundidade exigida e os melhores materiais para cada disciplina, leia [`o_que_estudar_de_fato.md`](o_que_estudar_de_fato.md).
   - Para dominar as matérias não-TI sem perder tempo com compêndios desnecessários, siga o [`guia_superacao_materias_basicas.md`](guia_superacao_materias_basicas.md).

---

## 📄 Licença

Este projeto e seus materiais são distribuídos para fins de estudo individual e planejamento acadêmico/profissional.
