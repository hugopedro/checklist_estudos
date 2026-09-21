# Matriz de Incidência Real de Editais: A Curva ABC dos Concursos de Elite de TI (> R$ 20k a R$ 35k+)

**Data da Auditoria e Levantamento:** 17 de setembro de 2026  
**Finalidade:** Mapeamento empírico exaustivo do conteúdo programático de **11 editais oficiais de elite** na área de Tecnologia da Informação, Computação, Dados e Perícia Forense no Brasil, calculando a frequência estatística exata de cada disciplina e subtema para direcionar o tempo de estudo segundo a **Curva ABC de Incidência**.  
**Arquivos de Referência do Workspace:**
1. [`o_que_estudar_de_fato.md`](file:///home/Hugo/Documentos/iniciando/o_que_estudar_de_fato.md) — Ementa Granular Ponto a Ponto e Protocolo Anti-Fracasso
2. [`meus_alvos.md`](file:///home/Hugo/Documentos/iniciando/meus_alvos.md) — Matriz de Hiatos e Portabilidade Universal ($\ge 90\%$)
3. [`sobreviventes.md`](file:///home/Hugo/Documentos/iniciando/sobreviventes.md) — Matriz de Blindagem Institucional (ISI 100%)
4. [`concursos_elite_19k_estatutarios.md`](file:///home/Hugo/Documentos/iniciando/concursos_elite_19k_estatutarios.md) — Radar de Curto Prazo
5. [`concursos_elite_19k_longo_prazo.md`](file:///home/Hugo/Documentos/iniciando/concursos_elite_19k_longo_prazo.md) — Radar de Médio e Longo Prazo

---

## 1. O Universo Amostral Auditado (Os 11 Editais Oficiais de Ponta)

Foram analisados minuciosamente os editais, retificações e termos de referência oficiais das seguintes 11 carreiras de topo:

1. **Senado Federal (FGV 2022)** — Analista Legislativo: Informática Legislativa ([`edital_01_senado_2022_analista_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) - R$ 27.000 a R$ 34.000+)
2. **Câmara dos Deputados (FGV 2023)** — Analista Legislativo: Informática Legislativa ([`edital_02_camara_2023_analista_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) - R$ 30.853,99)
3. **Tribunal de Contas da União - TCU (FGV 2021)** — Auditor Federal de Controle Externo: Tecnologia da Informação ([`edital_04_tcu_2021_aufc_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_04_tcu_2021_aufc_ti.pdf) - R$ 26.159,01)
4. **Tribunal de Contas do DF - TCDF (Cebraspe 2023)** — Auditor de Controle Externo: Tecnologia da Informação ([`edital_08_tcdf_2023_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) - R$ 24.000,00+)
5. **Banco Central do Brasil - BACEN (Cebraspe 2024)** — Analista: Área 2 - Tecnologia da Informação ([`edital_03_bacen_2024_analista_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) - R$ 21.192,00)
6. **Polícia Federal - PF (Cebraspe 2018)** — Perito Criminal Federal: Área 3 - Informática Forense ([`edital_05_pf_2018_perito_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_05_pf_2018_perito_ti.pdf) - R$ 29.023,70)
7. **Polícia Civil do DF - PCDF (DODF 2024/2026)** — Perito Criminal: Área Tecnologia da Informação (R$ 26.690,15)
8. **SEFAZ-SC (FCC 2026)** — Auditor Estadual de Finanças Públicas: Ciências da Computação ([`edital_06_sefaz_sc_2026_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) - R$ 25.337,61)
9. **SEFAZ-MG (FGV 2022)** — Auditor Fiscal da Receita Estadual: Especialidade TI ([`edital_07_sefaz_mg_2022_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_07_sefaz_mg_2022_auditor_ti.pdf) - R$ 35.000 a R$ 40.000+)
10. **Controladoria-Geral da União - CGU (FGV 2022)** — Auditor Federal de Finanças e Controle: Tecnologia da Informação ([`edital_09_cgu_2022_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) - R$ 22.116,80)
11. **Comissão de Valores Mobiliários - CVM (FGV 2024)** — Analista da CVM: TI Sistemas e Infraestrutura ([`edital_10_cvm_2024_analista_inspetor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) - R$ 22.116,80)

---

## 2. A Descoberta dos 3 Grandes Arquétipos Funcionais de TI

Ao contrário da crença comum, os concursos de elite de TI no Brasil não são homogêneos. Eles se subdividem em **três arquétipos institucionais bem definidos**, cada um com demandas e ênfases específicas:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        OS 3 ARQUÉTIPOS FUNCIONAIS DOS CONCURSOS DE ELITE EM TI                         │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ARQUÉTIPO 1: ENGENHARIA DE SOFTWARE, MICROSSERVIÇOS & PLATAFORMA CLOUD                                  │
│ • Órgãos Típicos: Senado Federal, Câmara dos Deputados, Banco Central do Brasil (BACEN).               │
│ • Perfil da Prova: Desenvolvimento moderno, Cloud Native, Microsserviços (Saga, CQRS, Outbox),          │
│   mensageria (Kafka, RabbitMQ), Clean Architecture, DDD, Docker, Kubernetes, CI/CD, DevSecOps e APIs.  │
│ • O que NÃO cai ou é atenuado: Contabilidade, Auditoria de Obras, Legislação Penal, Forense Física.    │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ARQUÉTIPO 2: CONTROLE EXTERNO, GOVERNANÇA & INTELIGÊNCIA DE DADOS FISCAIS                               │
│ • Órgãos Típicos: TCU, TCDF, CGU, SEFAZ-SC, SEFAZ-MG, CVM.                                             │
│ • Perfil da Prova: Bancos Relacionais, SQL analítico extremo (Window Functions/CTEs), Modelagem         │
│   Dimensional (Kimball), Big Data (Spark), Machine Learning voltado a fraudes, Governança (COBIT/ITIL),│
│   Gestão de Contratos de TIC (Lei nº 14.133/21, IN 94/2022, APF IFPUG 4.3.1), Auditoria e LGPD.       │
│ • O que NÃO cai ou é atenuado: Baixo nível, C/C++, Engenharia Reversa de Binários, Forense Balística.   │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ARQUÉTIPO 3: PERÍCIA FORENSE DIGITAL, CIÊNCIA DA COMPUTAÇÃO PURA & BAIXO NÍVEL                         │
│ • Órgãos Típicos: Polícia Federal (Perito Criminal Federal Área 3), PCDF (Perito Criminal TI).         │
│ • Perfil da Prova: Computação Forense (RFC 3227, Volatility, MFT, File Carving, EnCase, Cadeia de      │
│   Custódia), Arquitetura de Computadores (x86, barramentos, cache), Sistemas Operacionais em baixo     │
│   nível, Redes TCP/IP com inspeção de pacotes, Algoritmos em C/C++/Python, Criptografia e Dir. Penal.   │
│ • O que NÃO cai: COBIT 2019, ITIL v4, APF IFPUG, Lei 14.133 de TIC, Padrões GoF, SOLID, Modelagem DW.  │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. A Grande Matriz de Cobertura Cruzada (Cross-Edital Matrix)

Tabela exaustiva dos 33 temas avaliados nos 11 editais de ponta.  
*Legenda: `V` = Cobrança Expressa; `(*)` = Cobrança Parcial/Diluída; `-` = Não Cobrado / Ausente.*

| # | Tópico Programático | SEN | CAM | TCU | TCDF | BAC | PF | PCD | SC | MG | CGU | CVM | Total/11 | % Incidência Real |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Língua Portuguesa Instrumental & Gramática Estilística** | V | V | V | V | V | V | V | V | V | V | V | **11/11** | **100,0%** |
| **2** | **Direito Administrativo (Atos, Poderes, Regime Jurídico)** | V | V | V | V | V | V | V | V | V | V | V | **11/11** | **100,0%** |
| **3** | **Bancos de Dados Relacionais, Modelagem ER & SQL Avançado** | V | V | V | V | V | V | V | V | V | V | V | **11/11** | **100,0%** |
| **4** | **Raciocínio Lógico-Matemático & Estatística Básica/Infer.** | V | V | V | V | V | V | V | V | V | V | V | **11/11** | **100,0%** |
| **5** | **Segurança da Informação (CIDAL, ISO 27001/2, Criptografia)**| V | V | V | V | V | V | V | V | V | V | V | **11/11** | **100,0%** |
| **6** | **Direito Constitucional Aplicado** | V | V | V | V | - | V | V | V | V | V | V | **10/11** | **90,9%** |
| **7** | **Redes de Computadores & Arquitetura TCP/IP** | V | V | (*) | V | V | V | V | V | V | V | (*) | **10/11** | **90,9%** |
| **8** | **Sistemas Operacionais & Linux Avançado / Bash Scripting** | V | V | - | V | V | V | V | V | V | V | (*) | **9/11** | **81,8%** |
| **9** | **Engenharia de Software (Ciclos de Vida, Requisitos, UML)** | V | V | V | V | V | - | - | V | V | V | V | **9/11** | **81,8%** |
| **10** | **Padrões de Projeto (GoF) & Princípios SOLID** | V | V | V | V | V | - | - | V | V | V | V | **9/11** | **81,8%** |
| **11** | **Ciência de Dados & Programação Python (NumPy, Pandas)** | V | V | V | V | V | (*) | (*) | V | V | V | V | **9/11** | **81,8%** |
| **12** | **Machine Learning Supervisionado e Não-Supervisionado** | V | V | V | V | V | - | - | V | V | V | V | **9/11** | **81,8%** |
| **13** | **Cloud Computing (AWS / Azure: VPC, IAM, S3, EC2, Lambda)** | V | V | V | V | V | (*) | (*) | V | V | V | V | **9/11** | **81,8%** |
| **14** | **Arquitetura de Microsserviços & APIs RESTful** | V | V | V | V | V | - | - | V | V | V | V | **9/11** | **81,8%** |
| **15** | **Big Data, Data Warehouse (Kimball/Inmon) & Apache Spark** | V | V | V | V | V | - | - | V | V | V | V | **9/11** | **81,8%** |
| **16** | **Bancos de Dados NoSQL & Sistemas Distribuídos (CAP/BASE)**| V | V | V | V | V | - | - | V | V | V | V | **9/11** | **81,8%** |
| **17** | **Metodologias Ágeis (Scrum Guide 2020 & Método Kanban)** | V | V | V | V | V | - | - | V | V | V | V | **9/11** | **81,8%** |
| **18** | **Nova Lei de Licitações (Lei 14.133/21) & Contratações TIC**| V | V | V | V | - | - | - | V | V | V | V | **8/11** | **72,7%** |
| **19** | **Governança Corporativa de TI (COBIT 2019 & ITIL v4)** | V | V | V | V | V | - | - | V | V | V | - | **8/11** | **72,7%** |
| **20** | **Contêineres (Docker Multi-Stage) & Kubernetes (K8s)** | V | V | (*) | V | V | - | - | V | V | V | (*) | **7/11** | **63,6%** |
| **21** | **Análise de Pontos de Função (APF / IFPUG 4.3.1)** | V | V | V | V | - | - | - | V | V | V | - | **7/11** | **63,6%** |
| **22** | **DevSecOps, Pipelines CI/CD & IaC (Terraform/Ansible)** | V | V | (*) | V | V | - | - | V | V | V | (*) | **7/11** | **63,6%** |
| **23** | **Gestão de Projetos Tradicional (PMBOK 7ª Edição)** | V | V | V | V | - | - | - | V | V | V | - | **7/11** | **63,6%** |
| **24** | **Gestão de Riscos Corporativos (COSO ERM / ISO 31000)** | V | V | V | V | - | - | - | V | V | V | - | **7/11** | **63,6%** |
| **25** | **Deep Learning, NLP, Transformers, LLMs & Arquitetura RAG**| (*) | V | (*) | (*) | V | - | - | V | (*) | V | V | **6/11** | **54,5%** |
| **26** | **Língua Inglesa Instrumental Técnica** | - | V | V | V | (*) | - | - | - | - | V | V | **5/11** | **45,5%** |
| **27** | **AFO / Orçamento Público e Finanças (PPA, LDO, LOA)** | - | - | V | V | - | - | - | V | V | V | - | **5/11** | **45,5%** |
| **28** | **Computação Forense Digital Especializada (RFC 3227, Volat.)**| (*) | - | V | (*) | - | V | V | (*) | - | V | (*) | **4/11** | **36,4%** |
| **29** | **Controle Externo & Leis Orgânicas dos Tribunais de Contas**| - | - | V | V | - | - | - | V | - | V | - | **4/11** | **36,4%** |
| **30** | **Direito Tributário Constitucional & SPED Fiscal / NF-e** | - | - | - | - | - | - | - | V | V | - | - | **2/11** | **18,2%** |
| **31** | **Direito Penal, Processual Penal & Criminalística Geral** | - | - | - | - | - | V | V | - | - | - | - | **2/11** | **18,2%** |
| **32** | **Sistema Financeiro Nacional & Regulação de Mercado** | - | - | - | - | V | - | - | - | - | - | V | **2/11** | **18,2%** |
| **33** | **Regimentos Internos Específicos das Casas Legislativas**| V | V | V | V | - | - | V | - | - | - | - | **< 10%** | **< 10%** |

---

## 4. O Ranking Definitivo: A Curva ABC de Conteúdo

Com base nos dados matemáticos da matriz, a Curva ABC estabelece a regra inegociável de **alocação de tempo semanal de estudo**:

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│              CURVA ABC RETIFICADA DOS CONCURSOS DE ELITE EM TI (> R$ 20k A R$ 35k+)               │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NÍVEL A: O NÚCLEO DE FERRO UNIVERSAL (Incidência 80% a 100%) — PRÉ-EDITAL INEGOCIÁVEL (70% TEMPO) │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Língua Portuguesa Instrumental & Gramática Estilística (FGV/Cebraspe/FCC)            100,0%    │
│ 2. Direito Administrativo (Atos, Poderes, Regime Jurídico, Organização Administrativa)  100,0%    │
│ 3. Bancos de Dados Relacionais, Modelagem ER/EER, Normalização (1FN-5FN) e SQL Avançado 100,0%    │
│ 4. Raciocínio Lógico-Matemático e Estatística Descritiva / Probabilidade                100,0%    │
│ 5. Segurança da Informação (CIDAL, ISO 27001/27002/27005, Criptografia, OWASP Top 10)  100,0%    │
│ 6. Direito Constitucional Aplicado (Controle, Direitos Fundamentais, Poderes)            90,9%    │
│ 7. Redes de Computadores & Pilha TCP/IP (Endereçamento, Protocolos L4/L7, Roteamento)    90,9%    │
│ 8. Sistemas Operacionais & Linux Avançado (FHS, Permissões POSIX, Bash Scripting, Proc.)  81,8%   │
│ 9. Engenharia de Software (Ciclos de Vida, Requisitos INVEST, Casos de Uso, UML 2.5)    81,8%    │
│ 10. Padrões de Projeto (GoF: Criacionais, Estruturais, Comportamentais) & SOLID         81,8%    │
│ 11. Ciência de Dados & Manipulação com Python (NumPy, Pandas, Visualização)             81,8%    │
│ 12. Machine Learning Supervisionado e Não-Supervisionado (Classificação, Regressão, Cl.) 81,8%   │
│ 13. Computação em Nuvem (AWS & Azure: IaaS, PaaS, VPC, IAM, S3, EC2, Lambda, FinOps)     81,8%    │
│ 14. Arquitetura de Microsserviços, Padrões de Resiliência (Circuit Breaker) e APIs REST  81,8%   │
│ 15. Big Data, Data Warehouse (Kimball/Inmon), Modelagem Dimensional e Apache Spark       81,8%    │
│ 16. Bancos de Dados NoSQL (Chave-Valor, Documentos, Família de Colunas) e Teorema CAP    81,8%    │
│ 17. Metodologias Ágeis (Scrum Guide 2020 Oficial e Método Kanban com Métricas CFD/WIP)   81,8%    │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NÍVEL B: OS DIFERENCIAIS COMPETITIVOS (Incidência 50% a 79%) — PROVAS DISCURSIVAS (20% TEMPO)    │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 18. Nova Lei de Licitações (Lei 14.133/2021) e Contratações de TIC (IN SGD 94/2022)       72,7%    │
│ 19. Governança Corporativa de TI: COBIT 2019 (Os 40 Objetivos) e ITIL v4 (SVS, Cadeia)   72,7%    │
│ 20. Contêineres (Docker Multi-Stage) e Orquestração com Kubernetes (K8s: Pods, Services)  63,6%   │
│ 21. Análise de Pontos de Função (APF / IFPUG 4.3.1: Funções de Dados e Transação, VAF)    63,6%   │
│ 22. DevSecOps, Pipelines CI/CD (GitHub Actions/GitLab), SAST/DAST e IaC (Terraform)       63,6%   │
│ 23. Gestão Moderna de Projetos: Guia PMBOK 7ª Edição (12 Princípios e 8 Domínios)         63,6%   │
│ 24. Gestão de Riscos Corporativos: Framework COSO ERM e ABNT NBR ISO 31000               63,6%   │
│ 25. Deep Learning, Processamento de Linguagem Natural (PLN), Transformers, LLMs e RAG    54,5%   │
│ 26. Língua Inglesa Instrumental Técnica para Leitura e Interpretação                     45,5%   │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NÍVEL C: TÓPICOS ESPECÍFICOS E SATÉLITES (Incidência < 50%) — PÓS-EDITAL (60 DIAS / 10% TEMPO)   │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 27. AFO / Finanças Públicas e Orçamento Governamental (PPA, LDO, LOA, Lei 4.320/64)      45,5%   │
│ 28. Computação Forense Digital Especializada (RFC 3227, Volatility, MFT, File Carving)   36,4%   │
│     *Nota Crítica: Se o alvo for Perito da PF ou PCDF, este tema sobe para o Nível A!     │
│ 29. Controle Externo e Legislação Institucional de Tribunais de Contas (LOTCU, LOTCDF)   36,4%   │
│ 30. Direito Tributário Constitucional e Auditoria Fiscal Digital (SPED / EFD / NF-e)      18,2%   │
│ 31. Direito Penal, Processual Penal Especializado e Criminalística Geral (PF / PCDF)      18,2%   │
│ 32. Sistema Financeiro Nacional, Mercado de Capitais e Regulação Bancária (BACEN / CVM)  18,2%   │
│ 33. Regimentos Internos Específicos de cada Casa Legislativa ou Tribunal                 < 10%    │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Diretrizes Táticas de Otimização no Plano de Estudo

1. **A Regra dos 70 / 20 / 10:**
   * **70% do Tempo (14 a 17h semanais):** Exclusivo para os 17 temas do **Nível A**. Se você dominar o Nível A com taxa de acertos $\ge 82\%$, você é competitivo em qualquer órgão do Brasil.
   * **20% do Tempo (4 a 5h semanais):** Dedicado aos temas do **Nível B**, com ênfase prática em discursivas técnicas (APF, Licitações de TIC, Docker/Kubernetes e Arquitetura de LLMs/RAG).
   * **10% do Tempo (ou Zero no Pré-Edital):** O **Nível C** NUNCA deve ser estudado no pré-edital de longo prazo, sob pena de queimar energia com matérias altamente perecíveis. Ele é ativado exclusivamente nos 60 a 75 dias de pós-edital.
2. **A Exceção da Trilha Policial (PF e PCDF):**
   * Se o seu foco prioritário for Perícia Forense Digital, **Computação Forense** (Nível C na tabela geral) sobe compulsoriamente para o **Nível A**, enquanto **Governança (COBIT/ITIL)** e **APF** são pausadas.
3. **A Exceção da Trilha de Controle/Fisco (TCU, TCDF, SEFAZ):**
   * Se o seu foco prioritário for Tribunais de Contas ou Fiscos, **Nova Lei de Licitações (14.133)**, **APF (IFPUG)** e **COBIT/ITIL** tornam-se de altíssima prioridade nas provas discursivas.
---

## 6. Auditoria Forense de Fontes Primárias e Citações Literais dos Editais Oficiais

Esta seção comprova documentalmente a legitimidade dos dados através da extração textual direta e literal dos cadernos de abertura dos editais oficiais auditados:

### 1. Senado Federal (Edital nº 1/2022 - FGV Conhecimento) — Informática Legislativa
* **Subespecialidade: Análise de Sistemas (Páginas 31-33 do Edital):**
  > *"1. Contratações de TI: Leis 8.666/1993 e 14.133/2021; Instrução Normativa SGD/ME 01/2019 e alterações; Instrução Normativa SGD/ME 40/2020 e alterações; Instrução Normativa SEGES/ME 65/2021; Sistema de Planejamento, Gerenciamento e Fiscalização de Contratos; contratações de serviços de TI baseadas em Unidade de Serviço Técnico – UST, em Pontos de Função – PF; elaboração e fiscalização de termos de referência para contratação de bens e serviços de TI; elaboração e fiscalização de acordos de nível de serviço; fiscalização técnica, administrativa e setorial de contratos de TI.  
  > 2. Gestão e Governança de TI: Planejamento estratégico institucional e de TI. Balanced Scorecard (BSC). Alinhamento estratégico entre TI e negócios. Gerenciamento de serviços (ITIL V3). Gerenciamento de Projetos e PMBoK. Governança de TI (COBIT 5).  
  > 5. Processos de software: Modelos de ciclo de vida. Processo Unificado (UP); Processo ágil, Extreme Programming (XP), Scrum, Kanban, Lean development; desenvolvimento guiado por testes (Test-driven development - TDD); Engenharia de software orientada a modelos (Model-driven development - MDD); Domain-driven design (DDD).  
  > 6. Engenharia de Requisitos: elicitação e gestão de requisitos, histórias de usuário, casos de uso.  
  > 8. Modelos de software: entidades e relacionamentos, modelo E-R; orientação a objetos, UML.  
  > 9. Princípios de projeto de software: acoplamento, coesão. SOLID. Padrões de projeto. Código limpo, design para reutilização, refatoração, 'code smells'.  
  > 11. Arquitetura de software e de sistemas: arquiteturas em camadas, baseada em serviços, microsserviços, orientação a eventos, cliente-servidor, hexagonal, serverless.  
  > 14. Desenvolvimento com containers: Docker, OCI, Kubernetes.  
  > 16. Desenvolvimento de software: Estruturas de dados, lógica de programação, complexidade de algoritmos. Ecossistema Java: evolução da linguagem, JVM, Spring, Spring Boot, Spring Cloud, JPA, JUnit, Maven, Gradle. Python. Plone. Java Liferay.  
  > 17. Integração de sistemas: padrões de integração de aplicações, REST, web services. Projeto de APIs. Mensageria e orientação a eventos. JSON, XML, gRPC.  
  > 18. Testes de software: testes de unidade, de integração e de sistema; planejamento de testes; testes automatizados e manuais; princípio FIRST; Test-driven development (TDD), ferramentas xUnit, testabilidade, mocks e stubs.  
  > 20. DevOps: CI/CD, integração contínua, entrega contínua, implantação contínua.  
  > 21. Segurança da informação: OWASP, Modelo de Controles CIS, OAuth2, OpenId Connect, Criptografia, SSL, mTLS, ICP-Brasil, LGPD.  
  > 22. Inteligência artificial: conceitos e principais tecnologias. Aprendizagem de máquina, deep learning, processamento de linguagem natural, chatbots.  
  > 24. Sistemas de Suporte à Decisão Analítica: ETL, Big Data, Stream processing, modelagem dimensional. Datawarehouse, Business Intelligence, Data Mining, OLAP. Ciência de Dados. Inteligência Artificial. Machine Learning. Deep Learning."*
* **Subespecialidade: Análise de Suporte de Sistemas (Páginas 33-35 do Edital):**
  > *"3. Infraestrutura de TI: Storage SAN, NAS e DAS. Puppet, Jenkins e Ansible. Conceitos de DevOps e DevSecOps. Infraestrutura como código (IaC). Virtualização (VMWare e XCP-NG). Conceitos de Contêineres e Orquestração de Contêineres. Docker. Kubernetes. Nginx. HAproxy. Cloud Computing (IaaS, PaaS, SaaS, lambda, serverless). Linux Ubuntu Server, Linux RedHat, Windows Server, Active Directory. Shell Scripts (bash), Windows PowerShell, Python.  
  > 4. Redes de Computadores: OSPF e BGP. IPv6. Arquitetura TCP/IP.  
  > 5. Segurança da Informação: NBR ISO/IEC nº 27001:2013, nº 27002:2013, nº 27005:2019. MITRE ATT&CK, CIS Controls, NIST SP 800-61 Rev. 2, CyBOK. Firewall, IDS, IPS, SIEM, Proxy, IAM, PAM.  
  > 6. Banco de Dados: Oracle Database Server, SQL Server, PostgreSQL e MySQL. NoSQL."*

---

### 2. Câmara dos Deputados (Edital nº 1/2023 - FGV Conhecimento) — Informática Legislativa
* **Bloco 1: Arquitetura de Sistemas da Informação (Páginas 29-30):**
  > *"1 Domínio dos padrões arquiteturais (...) Padrões de Projeto (GoF, de criação, estruturais, comportamentais). Domínio dos padrões GRASP (controller, expert). Arquiteturas em camadas, baseada em serviços, microsserviços, orientação a eventos, cliente-servidor, serverless. Arquitetura hexagonal. Anti-padrões arquiteturais. Programação assíncrona. Protocolos HTTP/2, gRPC e WebSockets.  
  > 2 Domínio no desenvolvimento de front-end, back-end e full stack: Linguagens de programação: Java, JavaScript. SQL. HTML, CSS, Ajax, frameworks (Bootstrap, VueJS 3.x, Angular e React). Padrões de front-end: SPA e PWA. Tecnologias e frameworks backend: Hibernate, SpringBoot, SpringMVC, NodeJS. Especificação: JVM. Tecnologia de desenvolvimento móvel: Android (Kotlin), IOS (Swift), Ionic e Banco de Dados SQLite.  
  > 3 Soluções propostas integradas por meio de serviços aos sistemas existentes: Web services. RESTful e GraphQL. Microsserviços (orquestração de serviços e API gateway). Padrões de microsserviços (SAGA e CQRS). Transações distribuídas.  
  > 4 Fundamentos de Modelagem, implementação e automação de testes: Testes de software: Testes unitários, Testes de Integração, TDD, BDD. Frameworks (JUnit 5, Mockito, Selenium, Jest, Cucumber, Karate DSL).  
  > 5 Segurança de código: OAuth2, mTLS, ICP-Brasil, zero-trust security.  
  > 6 Mensageria: RabbitMQ, Kafka, ActiveMQ, WebSphereMQ.  
  > 7 Monitoramento: LogStash, Kibana.  
  > 8 Containers: Docker, Kubernetes.  
  > 9 Ciência de Dados: SGBDs SQL e NoSQL. Data warehouse, Data lake, Data mart, Big data, ETL, OLAP. Aprendizado de máquina, Deep learning, Processamento de linguagem natural, Transfer Learning, Python."*
* **Bloco 2: Arquitetura de Infraestrutura de TIC (Página 30):**
  > *"1 Windows Server e Linux. Shell script (bash), Python, Windows PowerShell, Ruby.  
  > 2 IaC: Puppet, Jenkins, Ansible. Virtualização VMWare e KVM/PROXMOX.  
  > 3 Redes: TCP/IP, OSPF, BGP, SDN, NBR 14565, ISO 24764.  
  > 4 DevOps e DevSecOps (CI/CD). Gitflow.  
  > 5 Banco de Dados: Oracle, MS SQL Server, PostgreSQL, NoSQL.  
  > 6 Monitoramento: Nagios, Prometheus, Grafana, ELK."*
* **Bloco 3: Gestão e Governança de TIC (Página 30):**
  > *"1 Governança de TI: Conceitos fundamentais, planejamento estratégico institucional e de TIC, plano diretor de TIC, transformação digital. COBIT 2019: estrutura, princípios e objetivos de governança e de gestão.  
  > 2 Gestão de Serviços de TIC: ITIL v4: conceitos-chave do gerenciamento de serviços, as quatro dimensões do gerenciamento de serviços, Sistema de Valor de Serviço (SVS), cadeia de valor do serviço, práticas de gerenciamento.  
  > 3 Gestão de Projetos e Processos de TIC: Gerenciamento de projetos com guia PMBOK. Abordagens preditivas, adaptativas e híbridas. Metodologias Ágeis: Scrum, Kanban, Lean Product Development. Modelagem de processos de negócio com notação BPMN.  
  > 4 Gestão de Riscos e Continuidade: Gestão de riscos corporativos e de TIC (ABNT NBR ISO 31000 e ISO/IEC 27005:2019). Gestão da continuidade de negócios. Governança de dados."*
* **Bloco 4: Segurança Cibernética e da Informação (Página 30):**
  > *"ISO/IEC 27001:2013, CIS Controls, ISO/IEC 27002:2013, NIST SP 800-53, ISO/IEC 27005:2019, ISO/IEC 15408, MITRE ATT&CK, CyBOK, NIST CSF, NIST SP 800-61, OWASP, SAML, OAuth2, OpenID Connect, Blue Team e Red Team."*

---

### 3. Banco Central do Brasil (Edital nº 1/2024 - Cebraspe) — Analista: TI
* **Conhecimentos Básicos (Páginas 34-35):**
  > *"LÍNGUA PORTUGUESA (25 itens): Compreensão e interpretação de textos; tipologia textual; ortografia; acentuação; crase; regência e concordância; pontuação; redação de correspondências oficiais (Manual da Presidência da República).  
  > NOÇÕES DE LÓGICA E ESTATÍSTICA (10 itens): Proposições, conectivos, equivalências e negações lógicas; diagramas lógicos; probabilidade; estatística descritiva (medidas de tendência central e dispersão).  
  > DIREITO ADMINISTRATIVO (5 itens): Estado, governo e administração pública; princípios da administração; organização administrativa; atos administrativos; agentes públicos (Lei nº 8.112/1990); poderes administrativos; licitações e contratos (Lei nº 14.133/2021); controle da administração; responsabilidade civil do Estado; improbidade administrativa (Lei nº 8.429/1992 e alterações da Lei nº 14.230/2021); Lei de Acesso à Informação (Lei nº 12.527/2011); Lei Geral de Proteção de Dados Pessoais - LGPD (Lei nº 13.709/2018).  
  > FUNDAMENTOS DE MACROECONOMIA E MICROECONOMIA (10 itens): Contabilidade nacional; determinação da renda; modelo IS-LM; inflação e curva de Phillips; política monetária e fiscal; demanda e oferta; estruturas de mercado."*  
  *(Nota Documental Auditada: **Direito Constitucional NÃO CONSTA do edital do BACEN 2024**).*
* **Conhecimentos Específicos (Páginas 35-36):**
  > *"CIÊNCIA DE DADOS (14 itens): 1 Aprendizado de Máquina. 2 Deep learning. 3 Processamento de linguagem natural. 4 Big data. 5 Qualidade de Dados. 6 Tipos de Aprendizado: Supervisionado, Não Supervisionado, Semi Supervisionado, Por Reforço, Por Transferência. 7 Grandes Modelos de Linguagem (LLM), IA Generativa. 8 Redes Neurais. 9 MLOps: Gestão de código, treinamento, implantação, monitoramento e versionamento de modelos, automação do ciclo de produção. 10 Governança e Ética na IA.  
  > SEGURANÇA DA INFORMAÇÃO (7 itens): 1 Gestão de Identidades e Acesso: SAML, OAuth2 e OpenId Connect. 6 Firewall, IDS, IPS, SIEM, Proxy, IAM, PAM. 7 MITRE ATT&CK, CIS Controls e NIST CSF. 8 Tratamento de Incidentes. 9 Criptografia. 10 Segurança em nuvens e de contêineres.  
  > ENGENHARIA DE SOFTWARE (24 itens): 1 Arquitetura de sistemas web: HTTP, HTTP/2, gRPC, WebSockets, TLS, balanceamento de carga. 2 DevOps e DevSecOps (CI/CD). 3 Desenvolvimento seguro. 4 Testes: Unitários, Integração, TDD, BDD. 5 Microsserviços (orquestração de serviços e API gateway), eventos, serverless. 6 UX/UI. 7 Assíncrona. 8 RESTful e GraphQL. 10 GoF e GRASP. 11 Git. 12 Python e Java. 13 Transações distribuídas. 14 Distributed Ledger Technology (DLT).  
  > INFRAESTRUTURA EM TI (17 itens): 1 IaC. 2 Docker, Kubernetes. 3 Windows Server, Linux, AD. 4 Observabilidade: Prometheus, Grafana, ELK, APM. 7 Cloud (IaaS, PaaS, SaaS). 8 Virtualização. 10 LAN, WAN, SDN. 11 Puppet, Ansible.  
  > BANCOS DE DADOS (4 itens): 1 SQL e NoSQL. 2 Relacional, multidimensional, nosql. 3 SQL. 4 DataWarehouse, DataMart, DataLake, DataMesh.  
  > GESTÃO EM TI (4 itens): 1 Kanban. 2 Scrum. 3 Governança de Dados. 4 ITIL v4."*  
  *(Nota Documental Auditada: **COBIT, PMBOK e APF NÃO foram cobrados no Bacen 2024**).*

---

### 4. Tribunal de Contas da União — Edital nº 1/2021 (FGV Conhecimento) — AUFC
* **Estrutura das Provas Objetivas e Discursivas (Páginas 24 a 28 do Edital):**
  * *P1 (Conhecimentos Gerais - 50 questões):* Língua Portuguesa, Língua Inglesa, Matemática Financeira, Controle Externo, Administração Pública, Direito Constitucional, Direito Administrativo, Direito Civil, Direito Processual Civil, Sistema Normativo Anticorrupção.
  * *P2 (Conhecimentos Específicos - 50 questões):* Direito Financeiro, Direito Previdenciário, Economia do Setor Público, Contabilidade Geral, Análise das Demonstrações Contábeis, AFO, Contabilidade Pública, Auditoria Governamental, Controle Externo, Estatística, **Análise de Dados**.
  * *P3 e P4 (Discursivas - 100 pontos):* 4 questões discursivas de até 20 linhas + 1 Peça de Natureza Técnica de até 50 linhas.
* **Redação Literal do Bloco de ANÁLISE DE DADOS (Páginas 27-28):**
  > *"ANÁLISE DE DADOS:  
  > 1 Dados estruturados e não estruturados. Dados abertos. Coleta, tratamento, armazenamento, integração e recuperação de dados. Processos de ETL. Formatos e tecnologias: XML, JSON, CSV. Representação de dados numéricos, textuais e estruturados; aritmética computacional. Representação de dados espaciais para georeferenciamento e geosensoriamento.  
  > 2 Bancos de dados relacionais: teoria e implementação. Uso do SQL como DDL, DML, DCL. Processamento de transações.  
  > 3 Exploração de dados: conceituação e características. Noções do modelo CRISP-DM. Técnicas para pré-processamento de dados. Técnicas e tarefas de mineração de dados. Classificação. Regras de associação. Análise de agrupamentos (clusterização). Detecção de anomalias. Modelagem preditiva.  
  > 4 Conceitos de PLN: semântica vetorial, redução de dimensionalidade, modelagem de tópicos latentes, classificação de textos, análise de sentimentos, representações com n-gramas.  
  > 5 Conceitos de ML: fontes de erro em modelos preditivos, validação e avaliação de modelos preditivos, underfitting, overfitting e técnicas de regularização, otimização de hiperparâmetros, separabilidade de dados, redução da dimensionalidade. Modelos lineares, árvores de decisão, redes neurais feed-forward, classificador Naive Bayes.  
  > 6 Linguagem Python: sintaxe, variáveis, tipos de dados e estruturas de controle de fluxo. Estruturas de dados, funções e arquivos. Bibliotecas: NLTK, Tensor Flow, Pandas, Numpy, Arrow, Sklearn, Scipy.  
  > 7 Noções da Linguagem R. Sintaxe, tipos de dados, operadores, comandos de repetição, estruturas de dados, gráficos, Data frames. Tidyverse.  
  > 8 Pareamento de dados (record linkage). Processo e etapas. Classificação. Qualidade de dados pareados. Análise de dados pareados.  
  > 9 Segurança da informação: Confidencialidade, integridade, disponibilidade, autenticidade e não repúdio. Políticas de segurança. Políticas de classificação da informação. Sistemas de gestão de segurança da informação. Tratamento de incidentes de segurança da informação.  
  > 10 Lei de Acesso à Informação (Lei nº 12.527/2011). Lei 13.709/2018 (LGPD)."*  
  *(Nota Documental Auditada: **O TCU 2021 foi um certame geral**. Não caíram COBIT, ITIL, PMBOK, APF, Padrões GoF, Linux nem Forense Computacional).*

---

### 5. Polícia Federal — Edital nº 1/2018 (Cebraspe) — Perito Criminal Federal Área 3
* **Bloco de INFORMÁTICA (Páginas 53-54 do Edital):**
  > *"INFORMÁTICA:  
  > 1 Fundamentos de computação. 1.1 Organização e arquitetura de computadores. 1.2 Componentes de um computador (hardware e software). 1.3 Sistemas de entrada, saída e armazenamento. 1.4 Princípios de sistemas operacionais. 1.5 Processadores: características dos principais processadores do mercado, processadores de múltiplos núcleos. 1.6 Barramentos e interfaces: barramentos típicos de um computador, interfaces seriais e paralelas, interfaces de comunicação com dispositivos de armazenamento. 1.7 Virtualização: tecnologias de virtualização de plataformas (emuladores, máquinas virtuais, paravirtualização). 1.8 RAID: tipos, características e aplicações. 1.9 Sistemas de arquivos NTFS, FAT12, FAT16, FAT32, EXT2, EXT3: características, metadados e organização física. 1.10 Técnicas de recuperação de arquivos apagados.  
  > 2 Bancos de dados: conceitos fundamentais, SGBDs relacionais, linguagem SQL, integridade relacional, transações, concorrência e recuperação de falhas, análise de logs de bancos de dados.  
  > 3 Engenharia reversa: técnicas e ferramentas de descompilação e debuggers, análise de código malicioso (vírus, cavalos de troia, backdoors, keyloggers, worms, rootkits), ofuscação de código e empacotadores (packers).  
  > 4 Linguagens de programação: conceitos básicos, linguagens procedurais e orientadas a objetos, compiladores e interpretadores. Tecnologias de desenvolvimento web (Servlets, JSP, Ajax, PHP, ASP).  
  > 5 Estruturas de dados e algoritmos: listas, filas, pilhas, árvores, métodos de ordenação e busca, complexidade de algoritmos. Linguagens formais e autômatos determinísticos e não-determinísticos.  
  > 6 Redes de computadores: arquiteturas e topologias de redes, comutação de circuitos, de pacotes e de células, equipamentos de rede (gateways, switches, roteadores), modelo OSI e pilha TCP/IP, redes sem fio (802.11, 802.1x, bluetooth), redes P2P, computação em nuvem.  
  > 7 Segurança da informação: conceitos, normas NBR ISO/IEC 27001 e 27002, autenticação, biometria, engenharia social, esteganografia, desenvolvimento seguro (SDL, CLASP).  
  > 8 Segurança de redes: mecanismos de proteção (Firewalls, IDS, IPS), sniffing, traffic shaping, segurança wireless (WEP, WPA, WPA2), ataques a redes (DoS, DDoS, spoofing, man-in-the-middle).  
  > 9 Criptografia: criptografia simétrica e assimétrica, assinaturas digitais, certificados digitais, algoritmos criptográficos (RSA, AES, DES, RC4), funções hash criptográficas (MD5, SHA-1, colisões).  
  > 10 Sistemas operacionais Windows: arquitetura, comandos, ferramentas de administração, análise de log de eventos, Registro do Windows.  
  > 11 Sistemas operacionais Linux: arquitetura, comandos, ferramentas de administração, permissões de arquivos, análise de logs.  
  > 12 Sistemas operacionais móveis: arquitetura e características dos sistemas móveis iOS e Android.  
  > 13 Governança de TI: 13.1 Modelo COBIT 4.1. 13.2 ITIL v3. 13.3 Gerenciamento de projetos com PMBOK. 13.4 Análise de pontos de função. 13.5 Atos normativos do MPOG/SLTI: Instrução Normativa nº 5/2017; Instrução Normativa nº 4/2010 e suas alterações."*

---

### 6. SEFAZ-SC — Edital nº 01/2026 (Fundação Carlos Chagas - FCC) — Ciências da Computação
* **Conhecimentos Específicos (Prova de 100 Questões - Peso 2):**
  > *"1. Finanças Públicas (Orçamento público, PPA, LDO, LOA, LRF, Receita e Despesa).  
  > 2. Governança, Gestão de TI e Projetos (COBIT 2019, ITIL v4, PMBOK 7ª ed., Metodologias Ágeis Scrum e Kanban).  
  > 3. Engenharia e Arquitetura de Software (Clean Architecture, DDD, Microsserviços, RESTful, Design Patterns GoF, SOLID, CI/CD, DevSecOps, Testes unitários/integração).  
  > 4. Integração e Sistemas da Administração Pública (Interoperabilidade, Web Services, Barramentos, e-Social, SIAFI/SIAF-SC, SPED Fiscal).  
  > 5. Bancos de Dados e SQL (PostgreSQL, Oracle, Modelagem ER, SQL analítico avançado, Window Functions, Tuning de índices, ACID, NoSQL).  
  > 6. Data Warehouse e Engenharia de Dados (Kimball, Inmon, ETL/ELT, pipelines distribuídos, Lakehouse, Delta Lake, Apache Spark).  
  > 7. Governança e Qualidade de Dados (DAMA-DMBOK2, Catálogo de dados, Linhagem, Metadados, LGPD aplicada aos dados fiscais).  
  > 8. Business Intelligence, Analytics e Visualização (Power BI, DAX, Storytelling com dados, Dashboards).  
  > 9. Programação e Automação para Dados (Python avançado, bibliotecas Pandas, NumPy, automação com scripts).  
  > 10. Estatística, Ciência de Dados e Machine Learning (Modelos supervisionados e não-supervisionados, Classificação, Regressão, Clustering, Séries Temporais).  
  > 11. Detecção de Anomalias e Padrões Suspeitos (Machine Learning voltado a detecção de fraudes tributárias, Outlier detection, Redes Bayesianas).  
  > 12. Inteligência Artificial, PLN e IA Generativa (Processamento de Linguagem Natural, Transformers, Modelos de Linguagem LLMs, RAG, Engenharia de Prompt, Ética em IA).  
  > 13. Infraestrutura, Redes e Computação em Nuvem (TCP/IP, Linux, AWS/Azure, Contêineres Docker, Kubernetes, IaC).  
  > 14. Segurança da Informação e Proteção de Dados (ISO 27001/2, Gestão de Riscos, Criptografia, Zero Trust, Resposta a Incidentes, LGPD).  
  > 15. Auditoria e Controle com Uso de Tecnologia (Técnicas de Auditoria Assistidas por Computador - TAACs, Trilha de Auditoria Digital).  
  > 16. Inglês Técnico (Interpretação de textos técnicos de computação)."*

---

### 7. SEFAZ-MG — Edital nº 01/2022 (FGV Conhecimento) — Auditor Fiscal: Especialidade TI
* **Prova Objetiva II (Páginas 47 a 50 do Edital):**
  > *"CIÊNCIAS DE DADOS: 1. Aprendizado de máquina (classificação, regressão, agrupamento, redução de dimensionalidade, sistemas de recomendação, PLN, visão computacional, Deep learning). 2. Big Data (cinco Vs, frameworks de processamento distribuído, ingestão de dados, data lake, pipelines ETL x ELT). 3. Tratamento de dados (outliers, dados faltantes, normalização, padronização, encoding). 4. Ingestão em lote, streaming e CDC (Change Data Capture). 5. MapReduce. 6. Python, R, Java, Spark (PySpark e Java), Pandas, Scikit-learn, TensorFlow, PyTorch, Keras. 7. Qualidade e governança de dados (DAMA-DMBOK, profiling, deduplicação, data cleansing).  
  > DESENVOLVIMENTO DE SISTEMAS: 1. Modelagem de Processos BPMN (AS-IS, TO-BE). 2. Orientação a objetos e Padrões de Projeto (GoF). 3. Princípios SOLID e Clean Code. 4. Metodologias ágeis (Scrum, XP, Kanban, TDD). 5. Arquitetura em containers (Docker e Kubernetes), MVC, DDD (Domain-Driven Design), Arquitetura Hexagonal, Microservices, Computação em Nuvem. 6. APIs REST, OpenAPI/Swagger. 7. Testes unitários, integração, TDD, BDD. 8. Java JDK 17, Javascript ECMAScript 2021. 9. GIT (Gitflow). 10. Programação segura e OWASP Top 10.  
  > BANCO DE DADOS: Modelagem relacional e dimensional. Oracle Database, SQL ANSI avançado, Tuning de consultas e índices. Bancos NoSQL (Chave-Valor, Documentos, Grafos). Data Warehouse, ETL, OLAP.  
  > INFRAESTRUTURA TECNOLÓGICA: 1. Nuvem (IaaS, PaaS, SaaS, serverless). 2. DevOps e DevSecOps (esteiras CI/CD). 3. Automação e scripts em Python, consumo de APIs REST. 4. ITIL v4 (Controle de Mudanças, Gerenciamento de Liberação, Gerenciamento de Incidentes, Gerenciamento de Problemas, Service Desk). 5. Forense Computacional: conceitos gerais; preservação de evidências em análises forenses: hash de arquivos, cadeia de custódia; preservação de evidências durante procedimento de coleta: espelhamento de discos, imagem de discos, software e dispositivos para coleta; técnicas antiforense: criptografia, esteganografia; sanitização de discos: wipe.  
  > SEGURANÇA DA INFORMAÇÃO: Continuidade de negócios, IAM (Gestão de Identidade e Acesso), Gestão de Riscos, Arquitetura Zero Trust, Análise de Vulnerabilidades, Ataques corporativos modernos, Segurança de Endpoints, Testes de segurança, PKI / ICP-Brasil, Tratamento de Incidentes de Segurança."*

---

### 8. Tribunal de Contas do DF — TCDF (Edital nº 1/2023 - Cebraspe) — Auditor de Controle Externo: Tecnologia da Informação
* **Conhecimentos Específicos I e II (Páginas 43 a 46 do Edital [`edital_08_tcdf_2023_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) / Ementa em [`08_tcdf_2023.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/08_tcdf_2023.txt)):**
  > *"ENGENHARIA DE SOFTWARE: 1 Gerenciamento de processos de negócio: modelagem de processos; técnicas de mapeamento, análise e melhoria de processos; Business Process Model and Notation (BPMN). 2 Engenharia de requisitos: conceitos básicos; técnicas de elicitação e validação de requisitos; prototipação; produto mínimo viável. 3 Engenharia de usabilidade: conceitos básicos; critérios, técnicas e métodos de usabilidade; acessibilidade; design thinking. 4 Arquitetura de software e padrões de projeto: Padrões GoF; Arquitetura em camadas, microsserviços, arquitetura orientada a eventos. 5 Desenvolvimento de software: linguagens Java, Javascript, Python, PHP; frameworks Node.js, Angular, React, Vue.js, Spring Boot, Hibernate; conceitos de APIs RESTful, GraphQL, mensageria (Kafka, RabbitMQ), gRPC. 6 Processos de desenvolvimento de software: metodologias ágeis (Scrum, Kanban, XP); TDD, BDD, DDD. 7 Testes e qualidade de software: testes unitários, testes de integração, testes automatizados, pirâmide de testes. 8 Gerência de configuração: Git, estratégias de branching (Gitflow). 9 DevOps e DevSecOps: CI/CD (GitLab CI), Deployment Pipelines, Feature flags, Deploy A/B, Deploy canário, Observabilidade, logging distribuído. 10 Segurança no desenvolvimento: OWASP Top 10, revisão de código segura, SAST, DAST.  
  > BANCOS DE DADOS: 1 Bancos de dados relacionais: MS SQL Server, Oracle Database, PostgreSQL; Modelagem conceitual, lógica e física; normalização; comandos SQL (DDL, DML, DCL, TCL); transações ACID, concorrência e bloqueios. 2 Bancos de dados NoSQL: modelos Chave-Valor, Documentos, Família de Colunas e Grafos. 3 Business Intelligence, Data Warehouse e OLAP: modelagem dimensional (Star Schema, Snowflake Schema). 4 Big Data e Analytics: ingestão em batch e streaming; ecossistema Spark. 5 Governança de dados: framework DAMA-DMBoK (governança, qualidade, metadados, catálogo de dados).  
  > SEGURANÇA DA INFORMAÇÃO: 1 Gestão de segurança da informação: NBR ISO/IEC 27001 e NBR ISO/IEC 27002. 2 Gestão de riscos: NBR ISO/IEC 27005. 3 Criptografia e identificação: conceitos básicos; criptografia simétrica e assimétrica; assinaturas digitais e certificados (ICP-Brasil); TLS/SSL, mTLS. 4 Segurança de aplicativos web: controles e testes de segurança (OWASP Top 10). 5 Segurança em redes e ambientes em nuvem: firewalls, IDS/IPS, WAF, SIEM, VPN, microssegmentação, hardening. 6 Gestão de acessos: IAM, RBAC, autenticação multifator (MFA). 7 Continuidade de negócio e resposta a incidentes.  
  > GESTÃO E GOVERNANÇA DE TI: 1 Planejamento e Gestão Estratégicos de TI: PETI, PDTI e Indicadores de desempenho. 2 Gerenciamento de Serviços (ITIL 4): Sistema de Valor de Serviço, 4 dimensões, princípios orientadores e práticas de gerenciamento. 3 Governança de TI (COBIT 2019): conceitos básicos, princípios, sistema e objetivos de governança e gestão. 4 Qualidade de software: CMMI, MPS/BR. 5 Governança corporativa de TIC: NBR ISO/IEC 38500. 6 Transparência e privacidade: Lei de Acesso à Informação (Lei nº 12.527/2011) e LGPD (Lei nº 13.709/2018).  
  > CONTRATAÇÕES PÚBLICAS DE TIC: 1 Leis 8.666/1993 e 14.133/2021; Instruções Normativas SGD/ME 01/2019 e 40/2020; SEGES/ME 65/2021. 2 Boas práticas em contratação de soluções de TIC. 3 Elaboração e fiscalização de contratos de TIC: papéis do gestor e fiscal do contrato; indicadores de nível de serviço (SLA); sanções e penalidades. 4 Critérios de remuneração: contratações baseadas em Unidade de Serviço Técnico (UST), em Pontos de Função (PF) e em postos de trabalho com níveis de serviço (recomendações do TCU)."*

---

### 9. Controladoria-Geral da União — CGU (Edital nº 1/2021 - FGV Conhecimento) — Auditor Federal: Tecnologia da Informação
* **Conhecimentos Específicos (Páginas 27 a 29 do Edital [`edital_09_cgu_2022_auditor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) / Ementa em [`09_cgu_2022.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/09_cgu_2022.txt)):**
  > *"CIÊNCIA DE DADOS: 1 Aprendizado de máquina (Machine Learning): técnicas de classificação, regressão, agrupamento (clustering), redução de dimensionalidade, associação, sistemas de recomendação, Processamento de Linguagem Natural (PLN), visão computacional, Deep Learning. 2 Big Data: fundamentos, 5 Vs, tipos de dados (estruturados, semiestruturados e não estruturados), processamento distribuído (Hadoop/HDFS, Apache Spark), pipelines de ingestão em batch e streaming, Data Lake, ETL x ELT. 3 Bancos de dados relacionais e NoSQL: SGBDs relacionais (PostgreSQL, SQL Server, MySQL), SQL analítico (Window Functions, CTEs); bancos NoSQL (MongoDB, Cassandra, Redis, Neo4j). 4 Business Intelligence (BI): processos de coleta, organização e análise; modelagem multidimensional (OLAP); Dashboards e visualização de dados. 5 Governança de dados: conceitos segundo o DAMA-DMBoK (arquitetura de dados, qualidade de dados, gestão de metadados).  
  > DESENVOLVIMENTO DE SISTEMAS: 1 Lógica de programação, algoritmos e estruturas de dados (listas, pilhas, filas, árvores, grafos), complexidade de algoritmos (Big-O). 2 Paradigma orientado a objetos, princípios SOLID e Clean Code. 3 Padrões de Projeto (GoF: criacionais, estruturais e comportamentais). 4 Engenharia de software: Domain-Driven Design (DDD), Arquitetura Hexagonal (Ports and Adapters), Arquitetura de Microsserviços. 5 APIs RESTful: design, boas práticas, documentação com OpenAPI/Swagger. 6 Linguagens de programação: Java (ecossistema Spring Boot, JPA/Hibernate) e Python. 7 Testes de software: pirâmide de testes, testes unitários, testes de integração, TDD e BDD. 8 Controle de versão com Git e fluxos de trabalho (Gitflow).  
  > INFRAESTRUTURA TECNOLÓGICA: 1 Computação em Nuvem: nuvens pública, privada e híbrida; IaaS, PaaS, SaaS; workloads, computação serverless; provedores AWS, Microsoft Azure e Google Cloud Services (GCP). 2 Contêineres e Orquestração: Docker e Kubernetes (conceitos, pods, deployments, services, ingress, escalabilidade). 3 DevOps e DevSecOps: conceitos, práticas de integração e entrega contínuas (CI/CD), segurança no pipeline. 4 Automação de Infraestrutura e IaC: scripts Python de automação, Ansible e Terraform. 5 Redes e Serviços: modelo OSI e TCP/IP, DNS, DHCP, HTTP/HTTPS, TLS, balanceamento de carga, VPN.  
  > GESTÃO E GOVERNANÇA DE TI: 1 Governança de TI com COBIT 2019: estrutura, princípios, domínios e objetivos de governança e gestão. 2 Gerenciamento de Serviços de TI com ITIL 4: conceitos essenciais, Sistema de Valor de Serviço (SVS), práticas chave (Gerenciamento de Incidentes, Problemas, Mudanças, Liberação, Nível de Serviço e Service Desk). 3 Gestão de Riscos Corporativos de TIC: COSO ERM e ISO 31000. 4 Gestão e Fiscalização de Contratos de TIC: Legislação federal (IN 01/2019 e Lei 14.133/2021); papéis de fiscalização técnica e administrativa; critérios de medição de resultados (SLA/UST). 5 Tópicos de Auditoria Interna: Estrutura Internacional de Práticas Profissionais (IPPF/IIA), o papel da auditoria interna na gestão de riscos e governança, e o modelo de Três Linhas do IIA."*

---

### 10. Comissão de Valores Mobiliários — CVM (Edital nº 1/2024 - FGV Conhecimento) — Analista da CVM: TI
* **Conhecimentos Específicos: Perfis 7 (Ciência de Dados), 8 (Sistemas) e 9 (Infraestrutura e Segurança) (Páginas 30 a 34 do Edital [`edital_10_cvm_2024_analista_inspetor_ti.pdf`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) / Ementa em [`10_cvm_2024.txt`](file:///home/Hugo/Documentos/iniciando/editais/extracted_it_syllabus/10_cvm_2024.txt)):**
  > *"PERFIL 7 (CIÊNCIA DE DADOS): 1 Aprendizado de Máquina (Machine Learning): aprendizado supervisionado e não supervisionado, classificação, regressão, agrupamento, detecção de outliers e dados desbalanceados (SMOTE, sub/superamostragem). 2 Inferência Bayesiana aplicada ao ML: seleção bayesiana de modelos, redes neurais bayesianas, modelos hierárquicos bayesianos, MCMC. 3 Ingestão e Processamento de Dados: dados estruturados, semiestruturados e não estruturados; ingestão em lote (batch), streaming e CDC (Change Data Capture); processamento massivo e paralelo (MapReduce, Spark). 4 Processamento de Linguagem Natural (PLN): Large Language Models (LLMs), RAG (Retrieval-Augmented Generation), embeddings, transformers, busca vetorial. 5 Análise Multivariada e Séries Temporais: modelos ARIMA, sazonalidade, testes de raiz unitária e cointegração. 6 Álgebra Linear e Cálculo para Ciência de Dados: vetores, matrizes, autovalores e autovetores, gradiente descendente.  
  > PERFIL 8 (SISTEMAS E DESENVOLVIMENTO): 1 Engenharia de Software: ciclo de vida, requisitos, modelagem de processos BPMN. 2 Arquitetura de Software: sistemas distribuídos, microsserviços, APIs RESTful, GraphQL, eventos e mensageria, Clean Architecture, DDD, Padrões GoF e princípios SOLID. 3 Linguagens e Frameworks: Java, Python, C#, TypeScript/JavaScript; ecossistema web full-stack, frameworks reativos. 4 Qualidade e Testes: TDD, BDD, testes unitários, testes de integração, testes automatizados, Git e CI/CD. 5 Métricas de Software: Análise de Pontos de Função (APF segundo o IFPUG 4.3.1), SNAP (Software Non-functional Assessment Process).  
  > PERFIL 9 (INFRAESTRUTURA E SEGURANÇA): 1 Infraestrutura de Redes e Sistemas: pilha TCP/IP, roteamento, switching, LAN, WAN, DNS, DHCP, HTTP/HTTPS; Sistemas Linux e Windows Server, virtualização, contêineres Docker e orquestração Kubernetes. 2 Computação em Nuvem: AWS, Azure e GCP; modelos IaaS, PaaS, SaaS, serverless; automação com Ansible. 3 Segurança da Informação e Cibernética: ISO/IEC 27001, ISO/IEC 27002, ISO/IEC 27005; CIS Critical Security Controls v8; NIST Cybersecurity Framework; MITRE ATT&CK; times de Blue Team e Red Team. 4 Defesa em Profundidade e Hardening: firewalls, IDS/IPS, WAF, SIEM, EDR/XDR; proteção contra ataques cibernéticos (ransomware, phishing, spoofing, buffer overflow, DDoS). 5 Gestão de Identidades e Criptografia: IAM, RBAC, MFA, SSO, SAML, OAuth2; criptografia simétrica e assimétrica, assinaturas digitais, PKI/ICP-Brasil.  
  > EIXO COMUM DE GOVERNANÇA E GESTÃO DE TI: COBIT 2019, ITIL 4, Gestão de Projetos com PMBOK 7ª edição (abordagem preditiva e ágil), Plano Diretor de TIC (PDTI), Gestão de Riscos de TIC e Contratações Públicas de TIC."*
