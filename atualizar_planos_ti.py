import sys, os

def build_study_guide():
    doc = []
    
    # -------------------------------------------------------------
    # HEADER & REPOSITÓRIO LOCAL
    # -------------------------------------------------------------
    doc.append(r"""# Guia Definitivo do Tronco Comum Antifrágil de TI (Rumo a 2028)
## O Que Estudar de Fato: Ementa Granular Ponto a Ponto, Trilhas Práticas e Métricas de Aprovação

**Data de Consolidação:** 17 de setembro de 2026  
**Horizonte de Execução:** Outubro de 2026 a Dezembro de 2028 (27 meses de maturação neural de elite)  
**Meta Estatística:** Atingir e sustentar o **Top 0,5%** das notas nos certames do Portfólio de Elite (> R$ 25.000 a R$ 40.000+)  
**Base Documental de Auditoria:** Conteúdos programáticos de TI extraídos diretamente dos 10 editais oficiais armazenados localmente em [`editais/`](file:///home/Hugo/Documentos/iniciando/editais/) e catalogados em [`editais/extracted_it_syllabus/`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/).

### Repositório Oficial de Editais Auditados no Workspace:
| # | Órgão & Certame | Edital Local Oficial (PDF) | Ementa Bruta de TI Extraída | Banca | Cargo / Especialidade de TI | Págs. de TI no PDF | Total Págs. |
| :-: | :--- | :--- | :--- | :---: | :--- | :---: | :---: |
| **01** | **Senado Federal (2022)** | [`edital_01_senado_2022_analista_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) | [`01_senado_2022.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/01_senado_2022.txt) | FGV | Analista - Informática Legislativa (*Análise de Sistemas e Suporte*) | Págs. 31 a 35 | 44 |
| **02** | **Câmara dos Deputados (2023)** | [`edital_02_camara_2023_analista_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) | [`02_camara_2023.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/02_camara_2023.txt) | FGV | Analista - Informática Legislativa (*Gerais e Específicos TIC*) | Págs. 25, 29-30 | 35 |
| **03** | **Banco Central do Brasil - BACEN (2024)** | [`edital_03_bacen_2024_analista_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) | [`03_bacen_2024.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/03_bacen_2024.txt) | Cebraspe | Analista - Área 2: Tecnologia da Informação | Págs. 36 a 38 | 43 |
| **04** | **Tribunal de Contas da União - TCU (2021)** | [`edital_04_tcu_2021_aufc_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_04_tcu_2021_aufc_ti.pdf) | [`04_tcu_2021.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/04_tcu_2021.txt) | FGV | Auditor Federal de Controle Externo (AUFC) - Dados & TI | Págs. 27 a 28 | 34 |
| **05** | **Polícia Federal - PF (2018)** | [`edital_05_pf_2018_perito_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_05_pf_2018_perito_ti.pdf) | [`05_pf_2018.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/05_pf_2018.txt) | Cebraspe | Perito Criminal Federal - Área 3 (*Informática Forense*) | Págs. 53 a 55 | 88 |
| **06** | **SEFAZ-SC (2026)** | [`edital_06_sefaz_sc_2026_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) | [`06_sefaz_sc_2026.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/06_sefaz_sc_2026.txt) | FCC | Auditor Estadual de Finanças Públicas - Ciências da Computação | Págs. 28 a 30 | 33 |
| **07** | **SEFAZ-MG (2022)** | [`edital_07_sefaz_mg_2022_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_07_sefaz_mg_2022_auditor_ti.pdf) | [`07_sefaz_mg_2022.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/07_sefaz_mg_2022.txt) | FGV | Auditor Fiscal da Receita Estadual (AFRE) - TI | Págs. 47 a 50 | 50 |
| **08** | **Tribunal de Contas do DF - TCDF (2023)** | [`edital_08_tcdf_2023_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) | [`08_tcdf_2023.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/08_tcdf_2023.txt) | Cebraspe | Auditor de Controle Externo - TI (*Sistemas TI*) | Págs. 43 a 46 | 58 |
| **09** | **Controladoria-Geral da União - CGU (2022)** | [`edital_09_cgu_2022_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) | [`09_cgu_2022.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/09_cgu_2022.txt) | FGV | Auditor Federal de Finanças e Controle (AFFC) - TI | Págs. 27 a 29 | 37 |
| **10** | **Comissão de Valores Mobiliários - CVM (2024)** | [`edital_10_cvm_2024_analista_inspetor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) | [`10_cvm_2024.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/10_cvm_2024.txt) | FGV | Analista da CVM - Perfis 7 (Dados), 8 (Sistemas), 9 (Infra/Seg) | Págs. 30 a 34 | 39 |

### Arquivos Estratégicos Conectados:
1. [`meus_alvos.md`](file:///home/Hugo/Documentos/iniciando/meus_alvos.md) — Teorema da Antifragilidade, Portfólio de 10 Órgãos e Matriz de Hiatos Históricos.
2. [`matriz_incidencia_editais.md`](file:///home/Hugo/Documentos/iniciando/matriz_incidencia_editais.md) — Matriz de Incidência Empírica, Confronto Literal e Curva ABC.
3. [`sobreviventes.md`](file:///home/Hugo/Documentos/iniciando/sobreviventes.md) — Pilares de Blindagem Institucional (Índice de Sobrevivência Institucional - ISI 100%).
4. [`concursos_elite_19k_estatutarios.md`](file:///home/Hugo/Documentos/iniciando/concursos_elite_19k_estatutarios.md) — Radar de Oportunidades Imediatas.
5. [`concursos_elite_19k_longo_prazo.md`](file:///home/Hugo/Documentos/iniciando/concursos_elite_19k_longo_prazo.md) — Radar de Médio e Longo Prazo.
6. [`editais/README.md`](file:///home/Hugo/Documentos/iniciando/editais/README.md) — Catálogo de Hash SHA256 e Verificação Criptográfica dos PDFs.
7. [`editais/extracted_it_syllabus/`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/) — Ementas Oficiais Brutas de TI Extraídas dos 10 Editais Locais.

---

## 0. A REGRA DE OURO DE ALOCAÇÃO DE TEMPO: A CURVA ABC (70 / 20 / 10)

A carga horária semanal (20h a 25h líquidas) é estritamente fracionada segundo a frequência matemática real apurada nos editais oficiais locais:

* **70% do Tempo Semanal (14h a 17h/sem) — Nível A (O Núcleo de Ferro / 80% a 100% de incidência):**  
  Português Instrumental, Dir. Administrativo (com Lei nº 14.133/2021), Bancos de Dados Relacionais e SQL Avançado, Raciocínio Lógico e Estatística Descritiva/Inferencial, Segurança da Informação (ISO 27001/27002/27005, Criptografia, OWASP Top 10), Dir. Constitucional, Redes de Computadores e TCP/IP, Linux Avançado e Bash, Engenharia de Software e UML 2.5, Padrões GoF e SOLID, Ciência de Dados com Python (NumPy, Pandas, Scikit-Learn), Machine Learning, Cloud Computing (AWS/Azure), Arquitetura de Microsserviços e APIs RESTful, Big Data e Apache Spark, Bancos NoSQL e Metodologias Ágeis (Scrum/Kanban).
* **20% do Tempo Semanal (4h a 5h/sem) — Nível B (Os Diferenciais Competitivos / 50% a 79% de incidência):**  
  Governança de TI (COBIT 2019 e ITIL v4), Contratações Públicas de TIC (IN SGD/ME nº 94/2022 e UST), Contêineres e Orquestração (Docker e Kubernetes), Análise de Pontos de Função (APF / IFPUG 4.3.1 e NESMA com deflatores do TCU), DevSecOps / Pipelines CI-CD / IaC (Terraform e Ansible), PMBOK 7ª Edição, Gestão de Riscos Corporativos (COSO ERM / ISO 31000) e Deep Learning / LLMs / Arquitetura RAG (os temas que definem as provas discursivas de topo).
* **10% do Tempo Semanal ou ZERO no Pré-Edital — Nível C (Tópicos Específicos / < 50% de incidência):**  
  AFO / Orçamento Público, Computação Forense Especializada (exceto se o alvo for Polícia Federal), Controle Externo / Leis Orgânicas dos Tribunais de Contas, Direito Tributário e SPED Fiscal, Legislação Penal/Processual e Regimentos Internos. Estudados exclusivamente nos 60 a 75 dias de pós-edital.

---
""")

    return "".join(doc)

print("Função base construída com sucesso.")
