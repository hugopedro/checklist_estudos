# Modulo com Disciplinas 5, 6 e 7 (Core de TI e Dados)

def get_secoes_ti_core():
    return r"""### DISCIPLINA 5: Bancos de Dados Relacionais, SQL Avançado e Big Data
* **Incidência Comprovada nos 10 Editais Oficiais Locais:** **10/10 (100%)**
  * Cobrada com altíssimo peso em todos os certames de topo:
    * [`Senado Federal 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) (FGV, Pág. 32 - Modelos de software, E-R, SGBDs Oracle, SQL Server, PostgreSQL, MySQL e NoSQL);
    * [`Câmara dos Deputados 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) (FGV, Pág. 30 - Modelagem relacional e multidimensional, NoSQL, SQL e ajuste de desempenho);
    * [`BACEN 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) (Cebraspe, Pág. 36 - SGBDs SQL e NoSQL, DataWarehouse, DataMart, DataLake, DataMesh);
    * [`TCU 2021`](file:///home/Hugo/Documentos/iniciando/editais/edital_04_tcu_2021_aufc_ti.pdf) (FGV, Pág. 27 - Bancos relacionais, SQL DDL/DML/DCL, Transações, Formatos XML/JSON/CSV, ETL);
    * [`Polícia Federal 2018`](file:///home/Hugo/Documentos/iniciando/editais/edital_05_pf_2018_perito_ti.pdf) (Cebraspe, Pág. 53 - Arquitetura, modelos lógicos/físicos, SQL, Transações e análise de logs);
    * [`SEFAZ-SC 2026`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) (FCC, Pág. 28-29 - PostgreSQL 18, MySQL 8.4 LTS, SQL Server 2025, MongoDB 8.0, Lakehouse, Apache Spark 4.x, DMBOK);
    * [`SEFAZ-MG 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_07_sefaz_mg_2022_auditor_ti.pdf) (FGV, Pág. 48 - Oracle Database, PL/SQL, NoSQL, Tuning, DWH, DMBOK governança de dados);
    * [`TCDF 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) (Cebraspe, Pág. 44 - MS SQL Server, MariaDB, NoSQL, Tuning, DWH, ELK Stack, Big Data, Data Lake, DMBOK);
    * [`CGU 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) (FGV, Pág. 27-28 - MS SQL Server, PostgreSQL, NoSQL, DWH, ETL, OLAP, Power BI, DMBOK);
    * [`CVM 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) (FGV, Pág. 31-32 - SQL ANSI, PL/SQL, MS SQL Server, MySQL, PostgreSQL, Tuning, DWH, Data Lakes).

* **Stack Tecnológico Oficial Mapeado:**
  * **SGBDs Relacionais Exigidos:** PostgreSQL 18, MySQL 8.4 LTS, Oracle Database 19c/21c (PL/SQL e administração), Microsoft SQL Server 2025 (T-SQL), MariaDB, SQLite.
  * **SGBDs Não Relacionais (NoSQL):** MongoDB 8.0, Redis, Apache Cassandra, Neo4j (Cypher), Elasticsearch 8.x / Kibana (ELK), Bancos Vetoriais (pgvector, Chroma, Pinecone, Qdrant).
  * **Big Data & Data Lakehouse:** Apache Spark 4.x (PySpark, DataFrame API, Spark SQL), Delta Lake, Apache Iceberg, Apache Hudi, Hadoop HDFS, Apache Kafka, RabbitMQ, Debezium (CDC).
  * **Governança & Modelagem de Dados:** DAMA-DMBOK 2 (as 11 funções e as 6 dimensões canônicas da qualidade de dados), Modelagem Dimensional de Kimball (Star, Snowflake).

* **Ementa Granular Ponto a Ponto:**
  * **Modelagem Conceitual, Lógica e Teoria Relacional:**
    * Modelo Entidade-Relacionamento (ER) e Modelo Entidade-Relacionamento Estendido (EER): entidades fortes e fracas; atributos atômicos, compostos, multivalorados e derivados; relacionamentos binários e n-ários; cardinalidade (1:1, 1:N, N:N) e restrições de participação (total e parcial); especialização, generalização, agregação e união/categoria.
    * Mapeamento sistemático do Modelo ER/EER para o Modelo Relacional: mapeamento de relacionamentos 1:1, 1:N e N:N; tratamento de atributos multivalorados (criação de nova relação) e compostos; mapeamento de hierarquias de especialização (tabela única com discriminador, tabela para cada subclasse, tabela para cada classe com atributos herdados).
    * Álgebra Relacional Formal: operadores fundamentais (seleção σ, projeção π, união ∪, diferença −, produto cartesiano ×, renomeação ρ); operadores derivados (junção natural ⨝, junção teta, junções externas esquerda ⟕, direita ⟖ e completa ⟗, interseção ∩, divisão ÷); Cálculo Relacional de Tuplas (TRC) e Cálculo Relacional de Domínios (DRC).
  * **Dependências Funcionais e Normalização de Dados:**
    * Dependência Funcional (DF): definição formal X → Y; dependência funcional plena, parcial e transitiva; Axiomas de Armstrong (reflexividade, aumentação e transitividade) e regras derivadas (decomposição, união e pseudotransitividade); Fechamento de atributos (X⁺) e determinação de superchaves e chaves candidatas; Cobertura canônica/mínima de dependências funcionais.
    * Formas Normais:
      * **Primeira Forma Normal (1FN)**: atomicidade de domínios (eliminação de atributos compostos, multivalorados e tabelas aninhadas);
      * **Segunda Forma Normal (2FN)**: estar na 1FN e todos os atributos não-chave dependerem funcionalmente de forma plena de cada chave candidata (eliminação de dependências parciais);
      * **Terceira Forma Normal (3FN)**: estar na 2FN e nenhum atributo não-chave depender transitivamente de nenhuma chave candidata;
      * **Forma Normal de Boyce-Codd (BCNF / FNBC)**: para toda dependência funcional não trivial X → Y, o determinante X deve ser uma superchave (elimina anomalias que a 3FN tolera quando existem chaves candidatas compostas sobrepostas);
      * **Quarta Forma Normal (4FN)**: estar na BCNF e não conter Dependências Multivaloradas (DMV: X ↠ Y) não triviais; Teorema de Fagin;
      * **Quinta Forma Normal (5FN / PJNF)**: dependências de junção (DJ) e eliminação de perdas em junções cíclicas.
    * Desnormalização controlada em ambientes analíticos: trade-offs entre redundância, integridade referencial e velocidade de consulta.
  * **Engenharia de Consultas SQL Avançada (PostgreSQL, Oracle, SQL Server):**
    * Sublinguagens SQL: DDL (CREATE, ALTER, DROP, TRUNCATE), DML (INSERT, UPDATE, DELETE), DQL (SELECT), DCL (GRANT, REVOKE), DTL/TCL (COMMIT, ROLLBACK, SAVEPOINT).
    * Junções: INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN, CROSS JOIN, NATURAL JOIN e SELF JOIN; junções não-equi (non-equi joins).
    * Funções Analíticas e de Janela (*Window Functions*): `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`, `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`, `NTH_VALUE()`; cláusulas `OVER (PARTITION BY ... ORDER BY ... [ROWS | RANGE] BETWEEN ... AND ...)`; distinção prática entre `ROWS` (limite físico de tuplas) e `RANGE` (limite lógico de valores com empates).
    * Common Table Expressions (CTEs): cláusula `WITH` e CTEs Recursivas (`WITH RECURSIVE` no PostgreSQL / `WITH` no SQL Server e Oracle) para consulta e navegação em estruturas hierárquicas, árvores e grafos.
    * Subconsultas (*Subqueries*): escalares, de linha, de tabela e correlacionadas; operadores `EXISTS`, `NOT EXISTS`, `IN`, `NOT IN`, `ANY` / `SOME`, `ALL`.
    * Agrupamentos Avançados Multidimensionais: cláusula `GROUP BY` e extensões analíticas `ROLLUP` (agregações hierárquicas acumuladas), `CUBE` (todas as combinações possíveis de subtotais) e `GROUPING SETS`.
    * Programação de Banco de Dados: Stored Procedures, Functions (UDFs) e Triggers em PL/pgSQL e PL/SQL Oracle; tratamento de exceções, cursores implícitos e explícitos; Triggers `BEFORE`, `AFTER` e `INSTEAD OF`, a nível de linha (`FOR EACH ROW`) e a nível de instrução (`FOR EACH STATEMENT`); Views convencionais vs Views Materializadas (mecanismos de atualização `REFRESH MATERIALIZED VIEW CONCURRENTLY`).
  * **Arquitetura Física, Indexação e Otimização de Desempenho (Query Tuning):**
    * Estrutura de armazenamento em disco: páginas/blocos de dados, registros, heaps, arquivos ordenados sequenciais, hashing.
    * Estruturas de Índices em Profundidade:
      * **Índices B-Tree e B+ Tree**: propriedades estruturais (nós internos contendo apenas chaves e ponteiros, nós folha duplamente encadeados armazenando dados/ponteiros para tuplas), balanceamento automático, altura da árvore, eficiência em buscas pontuais (O(log N)) e varreduras por faixa;
      * **Índices Hash**: complexidade média O(1) para igualdade estrita; impossibilidade de utilização em buscas intervalares;
      * **Índices Bitmap**: vetores de bits representando a presença de valores; operações booleanas (AND, OR, NOT) ultravelozes; uso ótimo em colunas de baixa cardinalidade em Data Warehouses;
      * **Índices Especializados do PostgreSQL**: GiST (Generalized Search Tree para dados geométricos/espaciais), GIN (Generalized Inverted Index para JSONB, arrays e busca textual full-text) e BRIN (Block Range Index para tabelas massivas com dados naturalmente ordenados por inserção temporal);
      * Índices Clusterizados (*Clustered*) vs Não-Clusterizados (*Non-Clustered*); Índices de Cobertura (*Covering Indexes* com cláusula `INCLUDE`); Índices Parciais (*Filtered Indexes*).
    * Processamento e Otimização de Consultas: fases de parsing, reescrita de consulta, otimização baseada em custos (CBO) e geração do plano de execução; interpretação minuciosa de `EXPLAIN` e `EXPLAIN ANALYZE` no PostgreSQL e planos gráficos do SQL Server; operadores de varredura: Seq Scan, Index Scan, Index Only Scan, Bitmap Index Scan; algoritmos de junção interna: Nested Loop Join, Hash Join, Merge Join (Sort-Merge Join); atualização de estatísticas com o comando `ANALYZE` e impacto da cardinalidade estimada vs real.
    * Particionamento de Tabelas: particionamento horizontal declarativo (por Faixa / Range, por Lista / List, por Hash e Composto); partição vertical; poda de partições (*Partition Pruning*).
  * **Transações, Concorrência e Tolerância a Falhas:**
    * As Propriedades ACID: Atomicidade (tudo ou nada), Consistência (preservação das invariantes e restrições de integridade), Isolamento (execução concorrente equivalente a execução serial) e Durabilidade (persistência das transações confirmadas após falhas).
    * Anomalias de Leitura Concorrente: Leitura Suja (*Dirty Read*), Leitura Não Repetível (*Non-repeatable Read*), Leitura Fantasma (*Phantom Read*) e Serialização Anômala (*Write Skew*).
    * Níveis de Isolamento SQL-92: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ` e `SERIALIZABLE`; implementação moderna via Controle de Concorrência Multiversão (**MVCC**: tuplas com identificadores de criação `xmin` e expiração `xmax`, eliminação de bloqueios de leitura por escrita e vice-versa, processo de limpeza `VACUUM` no PostgreSQL) vs Bloqueio em Duas Fases Estrito (**Strict 2PL**).
    * Bloqueios (Locks): tipos de locks (Shared - S, Exclusive - X, Intent Locks); Deadlocks (impasse): grafos de espera (*Wait-For Graph*), detecção por ciclos e resolução por timeout ou abortamento de transação vítima.
    * Recuperação de Falhas: Write-Ahead Logging (**WAL**: garantia de que alterações no log são gravadas em disco antes da página de dados correspondente), Checkpoints e Algoritmo ARIES (fases de Análise, Redo e Undo).
  * **Bancos de Dados NoSQL e Sistemas Distribuídos:**
    * Teorema CAP de Eric Brewer (Consistência estrita, Disponibilidade e Tolerância ao Particionamento de rede: impossibilidade de garantir os três simultaneamente na presença de partições de rede); Teorema PACELC de Daniel Abadi (se houver Partição, escolha entre Disponibilidade ou Consistência; Senão, escolha entre Latência ou Consistência).
    * Propriedades BASE: Basically Available (disponibilidade básica), Soft state (estado flexível), Eventual consistency (consistência eventual).
    * Categorias NoSQL:
      * **Chave-Valor (Key-Value)**: **Redis** (estruturas de strings, hashes, listas, sets, sorted sets, bitmaps, streams; persistência via RDB snapshots e AOF append-only file; replicação e Redis Cluster);
      * **Documentos (Document Stores)**: **MongoDB 8.0** (armazenamento em BSON, consultas ricas, Aggregation Pipeline, índices compostos, multikey e textuais, Replica Sets com elevação automática de primário e Sharding com shard key);
      * **Família de Colunas (Wide-Column)**: **Apache Cassandra** (arquitetura totalmente descentralizada *masterless*, Consistent Hashing, Gossip Protocol, Chave de Partição vs Coluna de Clusterização, consistência ajustável por operação: ONE, QUORUM, ALL; estruturas de armazenamento em memória Memtable e em disco SSTables com LSM-Tree e Compactação);
      * **Grafos (Graph Databases)**: **Neo4j** (modelo de grafos de propriedades rotuladas: nós, relacionamentos direcionados e tipados, propriedades chave-valor; linguagem de consulta declarativa Cypher; index-free adjacency);
      * **Bancos Vetoriais (Vector Databases para IA / RAG)**: pgvector (extensão PostgreSQL com tipos `vector`, operadores de distância Euclidiana `<->`, Cosseno `<=>` e Produto Escalar `<#>`, índices HNSW e IVFFlat), Chroma, Pinecone e Qdrant.
  * **Engenharia de Dados, Big Data, Lakehouse e Governança:**
    * Modelagem Dimensional de Data Warehouse: metodologias Inmon (arquitetura corporativa top-down orientada a dados em 3FN) vs Kimball (arquitetura de Data Marts bottom-up baseada em esquemas dimensionais); Tabelas Fato (fatos aditivos, semiaditivos e não aditivos; granularidade da fato); Tabelas Dimensão (dimensões conformadas, dimensões degeneradas, dimensões de papel compartilhado / *role-playing*); Modelos Star Schema, Snowflake Schema e Constellation Schema; Dimensões de Mudança Lenta (**SCD - Slowly Changing Dimensions**: Tipo 0 fixo, Tipo 1 sobregravação, Tipo 2 adição de nova linha com data início/fim e flag ativo, Tipo 3 adição de nova coluna, Tipo 6 híbrido).
    * Pipelines de Ingestão e Processamento: ETL (Extract, Transform, Load) vs ELT (Extract, Load, Transform); Arquitetura Medalhão (Camada Bronze/Raw: ingestão bruta sem modificação; Camada Silver/Cleansed: dados limpos, deduplicados e enriquecidos; Camada Gold/Curated: agregações e visões de negócio prontas para BI e ML).
    * Processamento Distribuído e Big Data:
      * **Apache Spark 4.x / PySpark**: Arquitetura Master/Worker, Driver Program, Cluster Manager (YARN, K8s, Standalone) e Executors; RDD (Resilient Distributed Dataset: transformações preguiçosas / *lazy* com DAG de execução vs ações que forçam o cálculo); DataFrames e Datasets; Spark SQL; Otimizador Catalyst (otimização lógica, pushdown de predicados, projeção) e Tungsten Engine (gerenciamento de memória off-heap e geração de código em tempo de execução);
      * **Apache Hadoop**: HDFS (NameNode ativo e standby, DataNodes, replicação de blocos de 128MB), MapReduce (fases de Map, Shuffle & Sort, Reduce) e YARN (ResourceManager, NodeManager).
    * Streaming, Mensageria e Ingestão em Tempo Real:
      * **Apache Kafka**: Arquitetura distribuída (Brokers, Tópicos, Partições, Consumer Groups, modo KRaft eliminando a dependência do ZooKeeper); Log de eventos particionado e imutável; Controle de offsets; Semânticas de entrega (*at-most-once, at-least-once, exactly-once*); Produtores idempotentes e transações Kafka;
      * **RabbitMQ**: Mensageria baseada em AMQP 0-9-1; Exchanges (Direct, Fanout, Topic, Headers), Filas e Bindings;
      * **Change Data Capture (CDC)**: Ingestão de dados full vs incremental; captura de logs de transação com **Debezium** e integração com Apache Kafka para replicação em tempo real sem onerar o banco de produção.
    * Modern Data Lakehouse e Data Mesh:
      * Formatos de Tabela Aberta: **Delta Lake**, **Apache Iceberg** e **Apache Hudi** (suporte a transações ACID sobre arquivos colunares Parquet, versionamento temporal / *Time Travel*, evolução de esquema e compactação de arquivos);
      * **Data Mesh**: os 4 princípios fundamentais de Zhamak Dehghani: 1. Propriedade orientada a domínio (*Domain-oriented ownership*); 2. Dados como Produto (*Data as a Product*); 3. Infraestrutura de dados self-service como plataforma; 4. Governança computacional federada.
    * Governança e Qualidade de Dados (**DAMA-DMBOK 2**):
      * As 11 Funções de Gestão de Dados: Governança, Arquitetura, Modelagem, Armazenamento/Operações, Segurança, Integração/Interoperabilidade, Documentos/Conteúdo, Dados Mestres/Referência, Data Warehousing/BI, Metadados e Qualidade de Dados;
      * Metadados (técnicos, de negócio e operacionais), Catálogo de Dados, Dicionário e Glossário de Negócios; Linhagem de Dados (*Data Lineage* de ponta a ponta);
      * As 6 Dimensões Canônicas da Qualidade de Dados: Completude, Consistência, Validade, Precisão, Unicidade e Integridade/Atualidade; Técnicas de Data Profiling, Data Cleansing, Matching, Deduplicação e Enriquecimento.
    * Business Intelligence e Visualização com **Microsoft Power BI**: Power Query para ETL visual, Linguagem M para transformações de dados, Modelagem de dados com relacionamentos ativos/inativos, **DAX** (Data Analysis Expressions: colunas calculadas vs medidas calculadas, contexto de linha vs contexto de filtro, função `CALCULATE()`, funções de Time Intelligence), Segurança a Nível de Linha (**RLS**).
    * Auditoria Digital e Dados Fiscais (SEFAZ-SC, SEFAZ-MG, TCU): Sistema Público de Escrituração Digital (**SPED Fiscal / EFD ICMS-IPI**); Estrutura de blocos (Bloco 0: Abertura e Identificação; Bloco C: Documentos Fiscais de Mercadorias / ICMS; Bloco H: Inventário Físico); Documentos Fiscais Eletrônicos (NF-e modelo 55, NFC-e, CT-e em arquivos XML e schemas XSD); Consultas analíticas para auditoria de cruzamento fiscal, identificação de fracionamento de compras e notas inidôneas.

* **Checklist de Domínio Técnico Pré-Edital (Definição de Pronto):**
  - [ ] Consigo escrever de primeira uma consulta SQL com `DENSE_RANK()`, `LAG()` e cláusula `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`.
  - [ ] Sei escrever uma CTE Recursiva (`WITH RECURSIVE`) para percorrer hierarquias organizacionais ou estruturas de processos.
  - [ ] Distingo no `EXPLAIN ANALYZE` quando o SGBD optou por um Hash Join vs Nested Loop vs Merge Join e compreendo as condições ideais para cada um.
  - [ ] Sei demonstrar formalmente por que uma relação está ou não na BCNF e decompor sem perda de junção.
  - [ ] Explico com precisão a diferença física e lógica entre índices B-Tree, Bitmap, GIN e BRIN e o momento ideal de aplicação de cada um.
  - [ ] Domino a diferença entre os níveis de isolamento `READ COMMITTED` e `REPEATABLE READ` sob a ótica do MVCC (snapshots no início da instrução vs no início da transação).
  - [ ] Sei desenhar a arquitetura de um pipeline Lakehouse medalhão (Bronze/Silver/Gold) usando Kafka, Debezium, Spark e Iceberg/Delta Lake.
  - [ ] Sei recitar e aplicar as 6 dimensões da qualidade de dados segundo o DMBOK em um estudo de caso prático de auditoria fiscal.

---

### DISCIPLINA 6: Engenharia de Software, Arquitetura e DevOps
* **Incidência Comprovada nos 10 Editais Oficiais Locais:** **9/10 (90%)**
  * Presente expressamente nos editais:
    * [`Senado Federal 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) (FGV, Pág. 31-33);
    * [`Câmara dos Deputados 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) (FGV, Pág. 29-30);
    * [`BACEN 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) (Cebraspe, Pág. 36 - 24 itens de Engenharia de Software);
    * [`TCU 2021`](file:///home/Hugo/Documentos/iniciando/editais/edital_04_tcu_2021_aufc_ti.pdf) (FGV, Pág. 27-28);
    * [`SEFAZ-SC 2026`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) (FCC, Pág. 28 - C#, .NET, ASP.NET, TypeScript, APIs REST, Auditoria de Sistemas e Código-Fonte);
    * [`SEFAZ-MG 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_07_sefaz_mg_2022_auditor_ti.pdf) (FGV, Pág. 48 - Desenvolvimento de Sistemas, Java 17, JS, DDD, Hexagonal, Git, OWASP);
    * [`TCDF 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) (Cebraspe, Pág. 43-44 - Kafka, RabbitMQ, gRPC, DevOps, DevSecOps, GitLab CI, Gitflow);
    * [`CGU 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) (FGV, Pág. 27 - Desenvolvimento de Sistemas, Spring Boot, Vue.js, Testes JUnit 5/Mockito/Selenium/Jest);
    * [`CVM 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) (FGV, Pág. 32 - Engenharia de Software, UML 2.5, APF IFPUG/NESMA, SNAP, CMMI 2.0, MPS.BR 2023, Clean Architecture).  
    *(Nota Técnica Documental: Apenas a **Polícia Federal Perito Área 3 2018 não cobrou microsserviços modernos e ágil**, concentrando-se em Fundamentos, Compiladores, Estruturas de Dados e Linguagens C/C++/Web).*

* **Stack Tecnológico Oficial Mapeado:**
  * **Linguagens de Programação:** Java (JDK 17+), Python 3.x, C# (.NET / ASP.NET), JavaScript (ECMAScript 2021+) / TypeScript, PHP, SQL ANSI.
  * **Frameworks Backend & Java:** Spring Boot, Spring Core, Spring MVC, Spring Cloud, Hibernate, JPA, QueryDSL, Flyway, Maven, Gradle.
  * **Frameworks Frontend:** Vue.js 3.x, React, Angular, jQuery, Bootstrap, Webpack, NPM, HTML5, CSS3 responsivo.
  * **Testes & Qualidade:** JUnit 5, Mockito, Selenium WebDriver, Jest, Cucumber, Karate DSL, Pitest (testes de mutação), JMeter, k6, SonarQube.
  * **Padrões e Arquitetura:** SOLID, Design Patterns GoF, GRASP, Clean Code, Clean Architecture, Arquitetura Hexagonal (Ports & Adapters), Domain-Driven Design (DDD), Microsserviços (API Gateway, Service Mesh, Saga, CQRS, Event Sourcing, Outbox, Circuit Breaker).
  * **Protocolos e Mensageria:** RESTful (Maturidade de Richardson), GraphQL, gRPC (Protocol Buffers), WebSockets, Webhooks, Apache Kafka, RabbitMQ.
  * **Métricas e Qualidade Formal:** Análise de Pontos de Função (APF / IFPUG CPM 4.3.1 e NESMA com deflatores do TCU), SNAP (Software non-Functional Assessment Process), Complexidade Ciclomática de McCabe, CMMI-DEV v2.0, MPS.BR (Guia Geral MPS Software 2023).

* **Ementa Granular Ponto a Ponto:**
  * **Processos de Software, Modelos de Ciclo de Vida e Métodos Ágeis:**
    * Modelos Preditivos: Cascata (*Waterfall*), Incremental, Modelo V e Modelo Espiral de Boehm (foco na gestão e atenuação de riscos); Processo Unificado (RUP/UP: fases de Iniciação, Elaboração, Construção e Transição; disciplinas de engenharia).
    * Manifesto Ágil: 4 valores fundamentais e 12 princípios; comparação estrutural entre abordagens preditivas e adaptativas.
    * **Scrum (Scrum Guide 2020 Oficial)**: Teoria do Scrum baseada no empirismo (Transparência, Inspeção e Adaptação) e valores (Compromisso, Foco, Abertura, Respeito e Coragem); A Equipe Scrum: Product Owner (proprietário do backlog e maximizador do valor), Scrum Master (líder servidor e facilitador da eficácia) e Desenvolvedores (responsáveis pela criação de um incremento utilizável a cada Sprint); Eventos: Sprint (timebox de até 1 mês), Sprint Planning (Por que este Sprint é valioso? O que pode ser feito? Como o trabalho será realizado?), Daily Scrum (15 minutos), Sprint Review (inspeção do incremento com stakeholders) e Sprint Retrospective (melhoria contínua da equipe); Artefatos e Compromissos: Product Backlog (Meta do Produto), Sprint Backlog (Meta do Sprint) e Incremento (Definição de Pronto / *Definition of Done - DoD*).
    * **Método Kanban (David J. Anderson)**: Os 4 princípios fundamentais e as 6 práticas essenciais: 1. Visualizar o fluxo de trabalho; 2. Limitar o Trabalho em Progresso (**WIP - Work in Progress**); 3. Gerenciar o fluxo; 4. Tornar as políticas de processo explícitas; 5. Implementar loops de feedback (cadências Kanban); 6. Melhorar colaborativamente e evoluir experimentalmente; Métricas de fluxo: Tempo de Lead (*Lead Time* - da requisição à entrega), Tempo de Ciclo (*Cycle Time* - do início do trabalho à entrega), Vazão (*Throughput*), Diagrama de Fluxo Cumulativo (**CFD - Cumulative Flow Diagram**: identificação de gargalos pela inclinação e distância entre bandas).
    * **Extreme Programming (XP)**: Valores (Comunicação, Simplicidade, Feedback, Coragem, Respeito); Práticas de engenharia: Programação em Pares (*Pair Programming*), Desenvolvimento Guiado por Testes (**TDD**: ciclo Red, Green, Refactor), Integração Contínua (CI), Design Simples, Refatoração contínua, Padronização de código, Propriedade coletiva do código, Cliente presente e Ritmo sustentável.
  * **Engenharia de Requisitos e Modelagem Ágil:**
    * Processo de Engenharia de Requisitos: Elicitação de requisitos (entrevistas, workshops, observação direta, análise de documentos, prototipagem), Análise e Negociação, Especificação, Validação e Gerenciamento de Requisitos; Rastreabilidade de requisitos (matriz de rastreabilidade para frente e para trás).
    * Tipos de Requisitos: Funcionais, Não Funcionais (modelo FURPS+: Funcionalidade, Usabilidade, Confiabilidade, Desempenho e Suportabilidade; Norma **ISO/IEC 25010** para qualidade de produto de software) e Regras de Negócio.
    * Especificação Ágil: Estórias de Usuário (*User Stories*) sob a regra INVEST (Independente, Negociável, Valiosa, Estimável, Pequena / *Small*, Testável); Critérios de Aceitação com linguagem ubíqua e sintaxe **Gherkin / BDD** (*Given-When-Then* / Dado-Quando-Então).
    * Design Thinking (Empatia, Definição, Ideação, Prototipação, Teste), Business Model Canvas, Produto Mínimo Viável (**MVP**), Testes A/B; Design de Interface e Experiência do Usuário (UI/UX), Usabilidade (heurísticas de Jakob Nielsen), Responsividade e Acessibilidade digital (**eMAG** - Modelo de Acessibilidade em Governo Eletrônico e diretrizes internacionais **WCAG 2.1**).
  * **Modelagem de Sistemas com UML 2.5.1 e Notação BPMN 2.0:**
    * **UML 2.5.1**:
      * Diagramas Estruturais:
        - *Diagrama de Classes*: representação de classes, atributos, métodos, níveis de visibilidade (+ público, - privado, # protegido, ~ pacote); Relacionamentos: Associação (unidirecional, bidirecional), Agregação (relação todo-parte fraca), Composição (relação todo-parte forte com destruição em cascata), Generalização/Herança e Realização/Implementação; classes abstratas e interfaces;
        - *Diagrama de Componentes*, *Diagrama de Implantação* (nós de processamento, artefatos e dispositivos de hardware) e *Diagrama de Pacotes*.
      * Diagramas Comportamentais:
        - *Diagrama de Casos de Uso*: atores, casos de uso, fronteira do sistema, relacionamentos de inclusão (`<<include>>` - execução obrigatória e incondicional), extensão (`<<extend>>` - execução opcional sob ponto de extensão) e generalização;
        - *Diagrama de Sequência*: linhas de vida, ativações, mensagens síncronas (seta preenchida), assíncronas (seta aberta) e de retorno (linha tracejada); fragmentos combinados (`alt` para bifurcações condicionais exclusivas, `opt` para opção simples, `loop` para repetição, `par` para execuções concorrentes);
        - *Diagrama de Atividades*: nós de ação, bifurcação (*fork*), junção (*join*), decisão, mescla (*merge*) e raias de natação (*swimlanes*);
        - *Diagrama de Máquina de Estados*: estados, transições, eventos gatilho, guardas e ações de entrada/saída.
    * **Modelagem de Processos de Negócio com BPMN 2.0**:
      * Mapeamento AS-IS (situação atual) vs modelagem TO-BE (situação futura desejada);
      * Elementos da notação BPMN: Piscinas (*Pools* para representar participantes/organizações) e Raias (*Lanes* para subdividir departamentos/papéis funcionais);
      * Eventos: Início (simples, mensagem, temporizador), Intermediários (captura vs lançamento) e Fim (simples, mensagem, erro, término cancelando a instância);
      * Gateways de Decisão: Exclusivo baseado em dados (**XOR** - apenas um caminho seguido), Paralelo (**AND** - sincroniza múltiplos fluxos sem avaliação de condição), Inclusivo (**OR** - um ou mais caminhos avaliados como verdadeiros são seguidos) e Baseado em Eventos;
      * Atividades: Tarefas atômicas (Usuário, Serviço, Script, Manual, Receber, Enviar) e Subprocessos (embutidos, reutilizáveis e transacionais); Fluxos de Sequência (seta sólida com preenchimento) vs Fluxos de Mensagem (seta tracejada entre pools distintas).
  * **Padrões de Projeto (Design Patterns - GoF) e Princípios de Engenharia OO:**
    * Os Princípios **SOLID**:
      1. *Single Responsibility Principle (SRP)*: uma classe deve ter um, e apenas um, motivo para mudar;
      2. *Open/Closed Principle (OCP)*: entidades de software devem estar abertas para extensão, mas fechadas para modificação;
      3. *Liskov Substitution Principle (LSP)*: objetos de uma superclasse devem ser substituíveis por objetos de suas subclasses sem quebrar o comportamento do sistema;
      4. *Interface Segregation Principle (ISP)*: clientes não devem ser forçados a depender de interfaces que não utilizam (interfaces coesas e específicas);
      5. *Dependency Inversion Principle (DIP)*: módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações; abstrações não devem depender de detalhes; detalhes devem depender de abstrações.
    * Princípios de Código Limpo (*Clean Code*): nomes significativos, funções pequenas com responsabilidade única, redução de efeitos colaterais, tratamento limpo de erros; Identificação de *Code Smells* (Long Method, God Class, Feature Envy, Shotgun Surgery, Primitive Obsession); Refatoração de código; Débito Técnico e Quality Gates no SonarQube.
    * Padrões de Projeto **GoF (Gang of Four)**:
      * **Criacionais**: *Singleton* (instância única garantida com construtor privado e double-checked locking), *Factory Method* (delega a instanciação para subclasses), *Abstract Factory* (famílias de objetos relacionados sem especificar suas classes concretas), *Builder* (construção passo a passo de objetos complexos separando construção de representação), *Prototype* (clonagem de instâncias existentes);
      * **Estruturais**: *Adapter* (converte a interface de uma classe na interface esperada pelo cliente), *Decorator* (adiciona responsabilidades dinamicamente a um objeto em tempo de execução sem herança), *Facade* (interface unificada de alto nível para um subsistema complexo), *Composite* (composição em árvores para tratar objetos individuais e composições uniformemente), *Proxy* (substituto que controla o acesso a outro objeto: virtual, de proteção ou remoto), *Bridge* (desacopla abstração de implementação para que variem independentemente), *Flyweight* (compartilhamento eficiente de grande número de objetos refinados usando estado intrínseco e extrínseco);
      * **Comportamentais**: *Strategy* (família de algoritmos intercambiáveis encapsulados), *Observer* (notificação automática 1:N de mudanças de estado), *Command* (encapsula uma requisição como um objeto permitindo parametrização, enfileiramento e operações reversíveis undo), *Template Method* (esqueleto de um algoritmo na superclasse com etapas implementadas nas subclasses), *State* (altera o comportamento do objeto quando seu estado interno muda), *Chain of Responsibility* (encadeamento de objetos receptores para tratar requisições), *Iterator* (acesso sequencial aos elementos de uma coleção sem expor sua representação interna), *Mediator* (centraliza a comunicação complexa entre objetos colegas), *Memento* (captura e externaliza o estado interno de um objeto para permitir restauração sem quebrar o encapsulamento), *Visitor* (operação a ser executada nos elementos de uma estrutura sem alterar as classes desses elementos).
    * Padrões **GRASP** (General Responsibility Assignment Software Patterns): Criador (*Creator*), Especialista na Informação (*Information Expert*), Baixo Acoplamento (*Low Coupling*), Alta Coesão (*High Cohesion*), Controlador (*Controller*), Polimorfismo (*Polymorphism*), Invenção Pura (*Pure Fabrication*), Indireção (*Indirection*) e Variações Protegidas (*Protected Variations*).
  * **Arquiteturas Modernas de Sistemas e Plataforma:**
    * Monólito Modular vs Arquitetura Distribuída.
    * **Arquitetura de Microsserviços**:
      * Padrões de decomposição: por capacidade de negócio ou por subdomínio do DDD;
      * Padrão **API Gateway**: ponto único de entrada, roteamento, agregação de requisições, terminação TLS, rate limiting e autenticação centralizada; Padrão Backend for Frontend (**BFF**);
      * **Service Mesh** (Malha de Serviços com Istio/Envoy): separação entre plano de controle e plano de dados (sidecar proxy); recursos: roteamento inteligente de tráfego, mTLS mútuo de ponta a ponta, injeção de falhas e telemetria distribuída;
      * Gerenciamento de Transações Distribuídas: impossibilidade de uso de transações ACID distribuídas (2PC - Two-Phase Commit e seus bloqueios bloqueantes); Padrão **Saga** (sequência de transações locais em cada serviço com transações de compensação semântica em caso de falha); Saga Orquestrada (orquestrador centralizado) vs Saga Coreografada (orientada a eventos entre serviços);
      * Padrão **CQRS** (Command Query Responsibility Segregation): separação dos modelos de escrita (comandos com lógica de negócio e validações) e leitura (consultas otimizadas com projeções desnormalizadas);
      * Padrão **Event Sourcing**: persistência do estado como uma sequência imutável de eventos de negócio em um Event Store;
      * Padrão **Transactional Outbox**: garantia de publicação atômica de eventos e gravação no banco de dados via tabela de outbox lida por CDC (Debezium/Kafka Connect);
      * Padrões de Resiliência: **Circuit Breaker** (estados Fechado, Aberto e Meio-Aberto), Retry com recuo exponencial (*Exponential Backoff* e jitter), Bulkhead (isolamento de pools de recursos) e Fallback com Resilience4j.
    * **Clean Architecture e Arquitetura Hexagonal (Ports and Adapters)**:
      * Arquitetura Hexagonal de Alistair Cockburn: núcleo da aplicação (domínio e casos de uso) isolado do mundo exterior; Portas de Entrada (*Driving/Inbound Ports*) e Adaptadores Primários (controladores web, CLI); Portas de Saída (*Driven/Outbound Ports*) e Adaptadores Secundários (repositórios de banco de dados, clientes HTTP externos);
      * Clean Architecture de Robert C. Martin: Regra de Dependência (as dependências do código-fonte só podem apontar para dentro, em direção às políticas de nível mais alto); Camadas concêntricas: 1. Entidades (regras de negócio da empresa); 2. Casos de Uso (regras de negócio da aplicação); 3. Adaptadores de Interface (Controllers, Gateways, Presenters); 4. Frameworks e Drivers (Web, DB, UI, dispositivos externos).
    * **Domain-Driven Design (DDD - Eric Evans)**:
      * Padrões Estratégicos: Linguagem Ubíqua (*Ubiquitous Language*), Contextos Delimitados (*Bounded Contexts*), Mapa de Contextos (*Context Map*: Shared Kernel, Customer/Supplier, Conformist, Open Host Service, Published Language, Anti-Corruption Layer - ACL);
      * Padrões Táticos: Entidades (identidade única duradoura), Objetos de Valor (*Value Objects* - imutáveis, igualdade estrutural por atributos), Agregados e Raiz do Agregado (*Aggregate Root* - garantia de invariantes transacionais), Serviços de Domínio (*Domain Services*), Eventos de Domínio (*Domain Events*), Repositórios (*Repositories* - abstração de persistência) e Fábricas (*Factories*).
    * **Arquitetura Orientada a Eventos (EDA)** e **Serverless**:
      * EDA: produtores de eventos, roteamento, corretores de eventos (Kafka, RabbitMQ), consumidores; desacoplamento temporal e espacial;
      * Serverless: computação baseada em funções como serviço (FaaS: AWS Lambda, Azure Functions); vantagens (escalonamento automático até zero, pagamento por execução e consumo de memória); desvantagens (latência de *cold start*, limites de tempo de execução, estado externo em bancos NoSQL).
  * **Protocolos de Integração e Tecnologias Web:**
    * **RESTful**: Representational State Transfer; Restrições arquiteturais (Cliente-Servidor, Stateless, Cacheable, Interface Uniforme, Sistema em Camadas, Código sob Demanda opcional); Modelo de Maturidade de Richardson:
      - Nível 0: O pântano de POX (chamadas RPC sobre HTTP usando endpoint único e POST);
      - Nível 1: Recursos individuais (URIs específicas para cada recurso);
      - Nível 2: Verbos HTTP adequados (GET para leitura idempotente e segura, POST para criação, PUT para substituição total idempotente, PATCH para modificação parcial, DELETE para remoção idempotente) e códigos de status HTTP corretos (200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 500 Internal Server Error, 503 Service Unavailable);
      - Nível 3: Controles Hipermídia (**HATEOAS** - Hypermedia as the Engine of Application State).
    * **GraphQL**: linguagem de consulta para APIs desenvolvida pelo Facebook; eliminação de *Over-fetching* e *Under-fetching*; endpoint único; Schemas e Definição de Tipos (SDL); Operações: Queries (consultas), Mutations (alterações) e Subscriptions (tempo real via WebSockets); Resolvers.
    * **gRPC (Google Remote Procedure Call)**: framework RPC de código aberto de alto desempenho; execução obrigatória sobre HTTP/2 (multiplexação, compressão de cabeçalhos); definição de contratos de serviço usando **Protocol Buffers (Protobuf)**; formatos de comunicação: RPC unário, streaming no servidor, streaming no cliente e streaming bidirecional; serialização binária ultra-eficiente.
    * **WebSockets**: protocolo de comunicação full-duplex bidirecional persistente sobre conexão única TCP (RFC 6455); handshake inicial via HTTP Upgrade.
  * **Testes de Software e Engenharia de Qualidade:**
    * Níveis de Teste: Testes de Unidade, Testes de Integração, Testes de Sistema e Testes de Aceitação; Pirâmide de Testes de Mike Cohn (base larga de testes unitários rápidos e baratos, camada intermediária de testes de serviços/integração, topo estreito de testes E2E/UI caros e lentos).
    * Técnicas de Teste: Caixa-Preta (baseada em requisitos: Particionamento em Classes de Equivalência, Análise do Valor Limite, Tabela de Decisão, Transição de Estados) vs Caixa-Branca (baseada no código: cobertura de instruções, cobertura de branches/decisões, cobertura de caminhos independentes via complexidade ciclomática).
    * Práticas Avançadas: Testes de Mutação (injeção intencional de falhas/mutantes no código para avaliar a eficácia da suíte de testes com o Pitest); Testes de Carga, Estresse, Estabilidade e Spike com Apache JMeter e k6; Testes em pipelines CI/CD com JUnit 5, Mockito (criação de mocks, stubs, spies e verificação de comportamentos) e Selenium WebDriver.
  * **Métricas de Software e Engenharia de Custos em Contratações:**
    * **Análise de Pontos de Função (APF / IFPUG CPM 4.3.1)**:
      * Funções de Dados:
        - Arquivo Lógico Interno (**ALI**): grupo de dados logicamente relacionados mantido dentro da fronteira da aplicação pelo usuário;
        - Arquivo de Interface Externa (**AIE**): grupo de dados mantido fora da fronteira da aplicação, referenciado para consulta;
        - Complexidade de Dados: avaliada pelo cruzamento de Tipos de Dados Elementares (**TDR / DET**) e Tipos de Registro (**TR / RET**), classificando em Baixa, Média ou Alta (ALI: 7, 10 ou 15 PF; AIE: 5, 7 ou 10 PF).
      * Funções de Transação:
        - Entrada Externa (**EE**): processo elementar que processa dados ou informações de controle vindos de fora da fronteira com a intenção de manter um ALI ou alterar o comportamento do sistema;
        - Saída Externa (**SE**): processo elementar que envia dados para fora da fronteira com lógica de processamento matemática, criação de dados derivados ou manutenção de estado;
        - Consulta Externa (**CE**): processo elementar que recupera dados sem cálculos complexos ou manutenção de ALIs;
        - Complexidade de Transação: avaliada pelo cruzamento de Arquivos Referenciados (**AR / FTR**) e Tipos de Dados Elementares (**TDR / DET**) (EE: 3, 4 ou 6 PF; SE: 4, 5 ou 7 PF; CE: 3, 4 ou 6 PF).
      * Tipos de Contagem: Contagem de Projeto de Desenvolvimento, Contagem de Projeto de Melhoria/Manutenção e Contagem de Aplicação;
      * Cálculo do Ponto de Função Não Ajustado (**PFNA**) e aplicação do Fator de Ajuste de Valor (**VAF** com 14 Características Gerais do Sistema - GSC);
      * **Métricas NESMA** (Contagem Indicativa, Estimada e Detalhada);
      * Aplicação dos **Deflatores de Pontos de Função** segundo as recomendações do TCU e Manuais do SISP para evitar remuneração indevida em manutenções corretivas e evolutivas.
    * **SNAP (Software non-Functional Assessment Process)**: medição do tamanho de requisitos não funcionais de software (CVM 2024).
    * **Complexidade Ciclomática de McCabe**: cálculo pelo grafo de fluxo de controle: V(G) = E - N + 2P ou V(G) = Regiões Delimitadas = Nós Predicados + 1; valor ideal ≤ 10.
    * **Modelos de Maturidade**:
  * **Desenvolvimento Web Frontend Moderno e Interfaces de Usuário:**
    * HTML5 Semântico e Estruturação: Elementos semânticos (article, section, nav, aside, header, footer, main), formulários avançados, validação nativa de inputs, atributos data-*, canvas e svg;
    * CSS3 Avançado e Layout Responsivo: Box Model, Flexbox (eixos principal e transversal, flex-direction, justify-content, align-items, flex-wrap, flex-grow/shrink), CSS Grid Layout (grid-template-columns, grid-template-rows, grid-template-areas, auto-fit, auto-fill, minmax), Media Queries e design responsivo;
    * JavaScript Moderno (ECMAScript 6+): Escopo de variáveis (var, let, const), Hoisting, Closures, Arrow Functions, Desestruturação (Destructuring), Operadores Rest e Spread, Promises, Async/Await, manipulação avançada da DOM e tratamento de eventos (Event Bubbling e Event Capturing);
    * TypeScript e Tipagem Estática: Tipos básicos e primitivos, Interfaces vs Types, Generics, Enums, Union e Intersection Types, Type Narrowing e compilação para JavaScript;
    * Frameworks e Bibliotecas SPA (Single Page Applications): Conceitos de Componentização, Estado Reativo, Virtual DOM; Fundamentos e Hooks no React (useState, useEffect, useContext, useMemo, useCallback); Conceitos de ciclo de vida e binding de dados no Angular e Vue.js 3.x;
    * Acessibilidade na Web (e-MAG e WCAG 2.1): Princípios fundamentais (Perceptível, Operável, Compreensível e Robusto - POUR), Níveis de conformidade (A, AA, AAA), semântica WAI-ARIA (roles, aria-label, aria-hidden), contraste de cores e navegação completa por teclado.
  * **Desenvolvimento Backend Corporativo (Java & C#/.NET):**
    * Linguagem Java (JDK 17 e 21 LTS): Programação Orientada a Objetos avançada (herança, encapsulamento, polimorfismo, interfaces, classes abstratas), Records, Pattern Matching, Generics, Tratamento de Exceções e Streams API (map, filter, reduce, collect);
    * Arquitetura da JVM e Gerenciamento de Memória: Organização de memória (Heap vs Stack, Metaspace), ClassLoaders, Ciclo de Vida do Garbage Collector (coletores G1 e ZGC) e parâmetros básicos de JVM (-Xms, -Xmx);
    * Java Collections Framework: Interfaces e implementações (List: ArrayList, LinkedList; Set: HashSet, TreeSet; Map: HashMap, TreeMap, LinkedHashMap), concorrência de coleções (ConcurrentHashMap, CopyOnWriteArrayList);
    * Ecossistema Spring Boot: Inversão de Controle e Injeção de Dependências (IoC/DI), Ciclo de vida de Beans, Spring MVC (@RestController, @RequestMapping, @RequestBody, @PathVariable), Spring Data JPA (@Repository, interfaces JpaRepository, consultas derivadas e @Query), Spring Security (autenticação baseada em tokens JWT e autorização RBAC);
    * Mapeamento Objeto-Relacional com JPA e Hibernate: Entidades (@Entity, @Table, @Id, @GeneratedValue), mapeamento de associações (@OneToOne, @OneToMany, @ManyToOne, @ManyToMany), estratégias de Fetch (LAZY vs EAGER), ciclos de vida de entidades gerenciadas (Transient, Persistent, Detached, Removed) e resolução do problema N+1;
    * Plataforma .NET e Linguagem C#: Fundamentos do Common Language Runtime (CLR), sintaxe C# moderna, LINQ (Language Integrated Query: queries e method syntax), arquitetura ASP.NET Core Web API e Entity Framework Core;
    * Testes Automatizados no Backend: Testes Unitários com JUnit 5 e NUnit, isolamento com Mockito (mocks, stubs, spies, verify, when/then), testes de integração de API e relatórios de cobertura de código com JaCoCo.
  * **Algoritmos Clássicos, Estruturas de Dados e Complexidade Computacional:**
    * Análise Assintótica de Complexidade: Notações Big-O (O), Big-Theta (Θ) e Big-Omega (Ω); análise de complexidade de tempo e espaço nos cenários de melhor caso, caso médio e pior caso; classes de complexidade (O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ));
    * Estruturas de Dados Lineares: Vetores/Arrays contíguos em memória, Listas Encadeadas (simplesmente encadeadas, duplamente encadeadas e circulares), Pilhas (LIFO - operações push, pop, peek) e Filas (FIFO - enqueue, dequeue; Filas Circulares e Deques);
    * Estruturas de Dados Hierárquicas (Árvores): Árvores Binárias de Busca (BST: inserção, remoção, busca; percursos Pré-Ordem, Em-Ordem, Pós-Ordem e em Nível), Árvores Balanceadas AVL (fator de balanceamento e rotações simples e duplas à esquerda e à direita), Árvores Rubro-Negras (propriedades e coloração) e Árvores B / B+ para índices de banco de dados;
    * Grafos e Algoritmos em Grafos: Representação computacional (Matriz de Adjacência vs Lista de Adjacência), Algoritmos de Busca em Grafos (Busca em Largura - BFS e Busca em Profundidade - DFS), Algoritmos de Menor Caminho (Dijkstra para pesos não-negativos e Bellman-Ford) e Árvore Geradora Mínima (Algoritmos de Prim e Kruskal);
    * Algoritmos de Ordenação e Pesquisa: Algoritmos de Busca (Busca Linear e Busca Binária recursiva e iterativa); Algoritmos quadráticos (BubbleSort, SelectionSort, InsertionSort); Algoritmos logarítmicos eficientes por divisão e conquista (QuickSort com escolha de pivô, MergeSort com intercalação, HeapSort com montagem de Max-Heap); estabilidade e complexidade de memória auxiliar de cada método;
    * Tabelas Hash e Funções de Espalhamento: Estrutura de Hashing, cálculo de funções hash eficientes, tratamento de colisões por Encadeamento Aberto/Externo vs Endereçamento Fechado (sondagem linear, quadrática e duplo hashing) e controle de Fator de Carga (Load Factor).

* **Checklist de Domínio Técnico Pré-Edital (Definição de Pronto):**
  - [ ] Consigo calcular a contagem de pontos de função completa de um CRUD de cadastro de usuários com importação externa sem cometer erros de RET/DET.
  - [ ] Sei implementar o Padrão Strategy e Observer em Java 17 ou Python utilizando interfaces e injeção de dependência.
  - [ ] Desenho em 5 minutos um diagrama de sequência UML com fragmento combinado `alt` para representar um fluxo de pagamento com aprovação e estorno.
  - [ ] Sei explicar a diferença exata entre Saga Coreografada e Saga Orquestrada e justificar quando cada uma deve ser adotada.
  - [ ] Sei formular a diferença entre os 4 níveis do Modelo de Maturidade de Richardson para APIs REST.
  - [ ] Sei calcular a Complexidade Ciclomática de um bloco de código estruturado com condicionais aninhadas.
  - [ ] Conheço os 5 níveis de maturidade do CMMI v2.0 e os 7 níveis do MPS.BR 2023.

---

### DISCIPLINA 7: Ciência de Dados, Python e Inteligência Artificial
* **Incidência Comprovada nos 10 Editais Oficiais Locais:** **9/10 (90%)**
  * Presente expressamente nos editais:
    * [`Senado Federal 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) (FGV, Pág. 33 - Inteligência Artificial, Machine Learning, Deep Learning, PLN, Chatbots);
    * [`Câmara dos Deputados 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) (FGV, Pág. 30 - Machine Learning, Deep Learning, PLN, Transfer Learning, Python);
    * [`BACEN 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) (Cebraspe, Pág. 36 - 14 itens: LLMs, IA Generativa, Redes Neurais, MLOps, Ética na IA);
    * [`TCU 2021`](file:///home/Hugo/Documentos/iniciando/editais/edital_04_tcu_2021_aufc_ti.pdf) (FGV, Pág. 27-28 - CRISP-DM, Mineração de dados, PLN, ML, Python Scikit-Learn/TensorFlow, R Tidyverse, Pareamento de dados);
    * [`SEFAZ-SC 2026`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) (FCC, Pág. 29 - Python 3.14, NumPy 2.5, Pandas 3.0, Scikit-learn 1.9, LLMs, Transformers, RAG, Bancos Vetoriais, Detecção de Anomalias em Compras/Licitações);
    * [`SEFAZ-MG 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_07_sefaz_mg_2022_auditor_ti.pdf) (FGV, Pág. 47 - Machine Learning, Deep Learning, Visão Computacional, PLN, Big Data 5Vs, Python, R, Java, PySpark, TensorFlow, PyTorch);
    * [`TCDF 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) (Cebraspe, Pág. 44 - CRISP-DM, Mineração, PLN semântica vetorial, ML, Python NLTK/TensorFlow/Pandas/Scikit-Learn);
    * [`CGU 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) (FGV, Pág. 27 - Machine Learning, Visão Computacional, Deep Learning, Big Data, Python, R, Scala, PySpark, TensorFlow, PyTorch, Keras, NLTK);
    * [`CVM 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) (FGV, Pág. 31-32 - LLMs Fine-tuning e dados sintéticos, Aprendizado Federado/Multi-GPU, Regtech/Suptech, Python Scikit-Learn/XGBoost/spaCy/Dask/PySpark, Álgebra Linear SVD/Cholesky, MCMC).

* **Stack Tecnológico Oficial Mapeado:**
  * **Linguagens:** Python 3.14.x, R (Tidyverse, ggplot2), Scala.
  * **Bibliotecas Python de Dados:** NumPy 2.5.x, Pandas 3.0.x, Matplotlib, Seaborn, Dask, PySpark.
  * **Bibliotecas de Machine Learning:** Scikit-Learn 1.9.x, XGBoost, LightGBM, CatBoost.
  * **Frameworks de Deep Learning & Redes Neurais:** PyTorch, TensorFlow, Keras.
  * **Processamento de Linguagem Natural (PLN):** NLTK, spaCy, gensim, Transformers (Hugging Face).
  * **IA Generativa, RAG & LLMs:** Arquitetura Transformer, Bancos de Dados Vetoriais (pgvector, Chroma, Pinecone, Qdrant), LangChain, LlamaIndex, Framework RAGAS, Framework ReAct, Protocolo MCP.
  * **MLOps & Ciclo de Vida:** MLflow, DVC, Apache Arrow.

* **Ementa Granular Ponto a Ponto:**
  * **Programação e Automação para Dados com Python:**
    * Estruturas nativas de dados: listas, tuplas, dicionários, conjuntos (*sets*); list, dict e set comprehensions; geradores e expressões geradoras (`yield`); funções lambda, `map()`, `filter()`, decoradores e tratamento de exceções.
    * Computação Vetorial com **NumPy**: o objeto `ndarray`; criação e transformação de arrays, regras de *broadcasting* multidimensional, fatiamento (*slicing*), indexação booleana avançada e operações de álgebra linear com `numpy.linalg`.
    * Manipulação Avançada com **Pandas**:
      * Estruturas Series e DataFrame; indexação por rótulo (`.loc`) vs indexação inteira (`.iloc`);
      * Transformação e enriquecimento: `.apply()`, `.map()`, operações vetorizadas;
      * Agregações: `.groupby()` com funções agregadas múltiplas via `.agg()`; tabelas dinâmicas (`pivot_table`) e tabelas de contingência (`crosstab`);
      * Cruzamento de conjuntos: `.merge()` (junções inner, left, right, outer), `.concat()` e `.join()`;
      * Tratamento de valores ausentes (`isna()`, `dropna()`, `fillna()`); manipulação de séries temporais com conversão de datas, deslocamento (`shift`) e reamostragem (`resample`).
  * **Ciclo de Vida de Projetos de Dados e Pré-Processamento (CRISP-DM):**
    * As 6 Fases do Modelo CRISP-DM: Compreensão do Negócio, Compreensão dos Dados, Preparação dos Dados, Modelagem, Avaliação e Implantação.
    * Limpeza de Dados e Imputação: detecção e imputação de valores ausentes (média, mediana, KNNImputer, imputação iterativa MICE);
    * Detecção e Tratamento de Outliers: método do Intervalo Interquartil (Q₁ - 1,5 × IQR e Q₃ + 1,5 × IQR), método do Z-score e algoritmos não-paramétricos baseados em isolamento (Isolation Forest);
    * Escalonamento e Normalização: Normalização Min-Max ([0, 1]), Padronização com Z-Score (StandardScaler com média 0 e variância 1), RobustScaler (baseado em mediana e IQR para amortecer o efeito de outliers) e transformações não-lineares (Logarítmica e Box-Cox);
    * Codificação de Atributos Categóricos: *One-Hot Encoding* (e a armadilha das variáveis dummy), *Ordinal Encoding*, *Target / Mean Encoding* (e os cuidados contra vazamento de dados / *data leakage*);
    * Seleção de Atributos (*Feature Selection*): Métodos de Filtro (correlação de Pearson/Spearman, Ganho de Informação, Teste Qui-Quadrado, ANOVA F-value), Métodos Wrapper (Recursive Feature Elimination - RFE) e Métodos Embutidos (Regularização Lasso L₁, Feature Importance de modelos baseados em árvores);
    * Tratamento de Classes Severamente Desbalanceadas: o problema da acurácia ilusória; Métodos de Reamostragem: *Over-sampling* sintético (**SMOTE** e ADASYN) e *Under-sampling* (Random Under-sampling e Tomek Links); Ajuste do limiar de decisão (*Threshold Tuning*) e ponderação de pesos de classe (*class weights* no Scikit-Learn e XGBoost).
  * **Machine Learning Supervisionado (Algoritmos e Formulação):**
    * Regressão Linear Simples e Múltipla: formulação analítica (Equação Normal) vs Gradiente Descendente (Batch, Estocástico - SGD e Mini-Batch); Regularizações: Ridge (penalização L₂), Lasso (penalização L₁ com seleção esparsa de variáveis) e ElasticNet (L₁ + L₂);
    * Regressão Logística: Função Sigmoide/Logística (σ(z) = 1 / (1 + e^(-z))); cálculo de probabilidades e razão de chances (*odds ratio*); Fronteira de decisão linear; Função de custo Log-Loss (Entropia Cruzada Binária);
    * K-Nearest Neighbors (k-NN): algoritmo baseado em instâncias (*lazy learner*); métricas de distância (Euclidiana, Manhattan, Minkowski, Cosseno); sensibilidade à escala e maldição da dimensionalidade;
    * Naive Bayes: Teorema de Bayes com premissa ingênua de independência condicional dos preditores; Modelos Gaussian Naive Bayes (variáveis contínuas), Multinomial (contagens/textos) e Bernoulli;
    * Árvores de Decisão (Decision Trees): Algoritmos CART, ID3 e C4.5; Critérios de divisão em classificação: Impureza de Gini (1 - Σ p_i²) e Entropia/Ganho de Informação (-Σ p_i · log₂(p_i)); Critério para regressão: Redução de Variância (MSE); Estratégias de poda (*pre-pruning* com max_depth, min_samples_split e *post-pruning* de complexidade de custo com ccp_alpha);
    * Métodos de Conjunto (*Ensemble Learning*):
      - **Bagging** (Bootstrap Aggregating): amostragem com reposição; redução de variância; **Random Forest** (amostragem aleatória de instâncias e seleção aleatória de subconjunto de features a cada divisão; estimativa de erro Out-of-Bag - OOB);
      - **Boosting**: treinamento sequencial de aprendizes fracos corrigindo os resíduos dos modelos anteriores; redução de viés e variância; AdaBoost; **Gradient Boosting Machine (GBM)**; Algoritmos de alto desempenho: **XGBoost** (aproximação de Taylor de segunda ordem na função de perda, regularização L₁/L₂ nas folhas, suporte nativo a dados esparsos), **LightGBM** (crescimento de árvore por folhas / *leaf-wise*, amostragem unilateral baseada em gradiente - GOSS, empacotamento exclusivo de atributos - EFB) e **CatBoost** (tratamento ótimo de variáveis categóricas sem target leakage);
      - Modelos de Combinação: *Voting Classifiers* (votação majoritária dura vs suave baseada em probabilidades) e *Stacking Generalization* (meta-aprendizes).
    * Support Vector Machines (SVM): Hiperplano ótimo de separação com margem máxima; Vetores de suporte; Formulação primária e dual; Margem suave com parâmetro de regularização C; O Truque do Kernel (*Kernel Trick* para separabilidade não linear): linear, polinomial e Radial Basis Function (**RBF / Gaussiano** com parâmetro γ).
  * **Machine Learning Não-Supervisionado:**
    * Algoritmos de Agrupamento (*Clustering*):
      - **K-Means**: algoritmo particional de Lloyd (atribuição de pontos ao centróide mais próximo e recálculo das médias); Escolha do número ótimo de clusters k: Método do Cotovelo (*Elbow Method* via inércia/WCSS) e Coeficiente de Silhueta ([-1, 1]); Inicialização aprimorada com K-Means++;
      - K-Medoids (PAM): uso de pontos reais do conjunto de dados como centros, conferindo maior robustez a outliers;
      - **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise): agrupamento baseado em densidade local; Classificação dos pontos: Pontos Centrais (*Core Points* com pelo menos MinPts vizinhos em raio ε), Pontos de Borda (*Border Points*) e Ruído/Outliers (*Noise*); Vantagem em descobrir clusters de formas arbitrárias e identificar outliers nativamente sem necessidade de pré-especificar o número de grupos;
      - Agrupamento Hierárquico: Aglomerativo (*bottom-up*) e Divisivo; Métricas de ligação (*Linkage*: Single Linkage, Complete Linkage, Average Linkage e Método de Ward com minimização de variância interna); Visualização por Dendrogramas e corte de linha.
    * Redução de Dimensionalidade:
      - **Análise de Componentes Principais (PCA)**: técnica linear não supervisionada; centralização de dados, matriz de covariância, cálculo de autovalores e autovetores; projeção ortogonal nas direções de máxima variância; seleção de componentes pela variância acumulada explicada (> 85-95%);
      - Técnicas não lineares de visualização: **t-SNE** (t-Distributed Stochastic Neighbor Embedding) e **UMAP** (Uniform Manifold Approximation and Projection).
  * **Validação de Modelos e Métricas de Avaliação:**
    * Esquemas de Divisão: Holdout (treino, validação e teste); Vazamento de Dados (*Data Leakage* de atributos e temporal); Validação Cruzada K-Fold e Stratified K-Fold (preservação da proporção de classes); Validação temporal (*TimeSeriesSplit*).
    * Diagnóstico de Desempenho: Trade-off Viés-Variância (*Bias-Variance Tradeoff*); *Underfitting* (alto viés, baixa complexidade) vs *Overfitting* (alta variância, modelo decora o ruído do treino); Curvas de Aprendizado e Curvas de Validação.
    * Métricas de Classificação:
      - Matriz de Confusão: Verdadeiros Positivos (VP), Falsos Positivos (FP - Erro Tipo I), Verdadeiros Negativos (VN), Falsos Negativos (FN - Erro Tipo II);
      - Acurácia: (VP + VN) / (VP + FP + VN + FN);
      - Precisão (*Precision*): VP / (VP + FP) (foco na minimização de falsos alarmes);
      - Revocação / Sensibilidade (*Recall / True Positive Rate*): VP / (VP + FN) (foco na não perda de positivos reais / detecção de fraudes);
      - Especificidade: VN / (VN + FP);
      - F1-Score: média harmônica entre Precisão e Recall: 2 × (Precisão × Recall) / (Precisão + Recall); Medidas F_β;
      - Curva ROC e **AUC-ROC**: gráfico da Taxa de Verdadeiros Positivos vs Taxa de Falsos Positivos sob variação do limiar de corte;
      - Curva Precision-Recall (**PR-AUC**): métrica mandatória para problemas com severo desbalanceamento de classes.
    * Métricas de Regressão: Erro Médio Absoluto (MAE), Erro Quadrático Médio (MSE), Raiz do Erro Quadrático Médio (RMSE), Erro Percentual Absoluto Médio (MAPE), Coeficiente de Determinação (R²) e R² Ajustado.
  * **Deep Learning, Visão Computacional e Processamento de Linguagem Natural (PLN):**
    * Redes Neurais Artificiais (ANN): Perceptron simples; Perceptron Multicamadas (MLP); Funções de ativação não lineares: Sigmoide, Tanh, **ReLU** (Rectified Linear Unit), Leaky ReLU e Softmax (para classificação multiclasse);
    * Treinamento e Otimização: Algoritmo de Retropropagação (*Backpropagation*) baseado na Regra da Cadeia; Algoritmos Otimizadores: SGD com Momentum, RMSprop, **Adam** e **AdamW**; Técnicas de regularização em redes profundas: *Dropout* (desativação aleatória de neurônios no treino) e Normalização em Lote (*Batch Normalization*);
    * Redes Convolucionais (**CNN**): camadas de convolução (filtros/kernels, stride, padding), camadas de pooling (Max Pooling, Average Pooling) e camadas densas/fully-connected; aplicações em Visão Computacional: classificação de imagens, detecção de objetos (YOLO) e segmentação;
    * Redes Recorrentes (**RNN**): células recorrentes para processamento sequencial; problema do desaparecimento/explosão do gradiente (*Vanishing/Exploding Gradient*); Arquiteturas com portas de memória: **LSTM** (Long Short-Term Memory: portas de esquecimento, entrada e saída; estado de célula) e **GRU** (Gated Recurrent Unit).
    * Processamento de Linguagem Natural (PLN):
      - Pré-processamento textual: tokenização de caracteres/palavras/subpalavras, remoção de stopwords, normalização de texto, stemming (RSLP para português) e lematização;
      - Modelos de representação clássica: Bag of Words (BoW), N-gramas, **TF-IDF** (Term Frequency-Inverse Document Frequency);
      - Representações vetoriais distribuídas (*Word Embeddings*): Word2Vec (arquiteturas Continuous Bag of Words - CBOW e Skip-gram com amostragem negativa), GloVe e FastText (embeddings baseados em subpalavras n-gram);
      - Modelagem de Tópicos Latentes (**LDA** - Latent Dirichlet Allocation), Classificação de Textos, Análise de Sentimentos e Reconhecimento de Entidades Nomeadas (**NER**).
  * **Grandes Modelos de Linguagem (LLMs), Arquitetura RAG e IA Generativa de Vanguarda:**
    * **Arquitetura Transformer ("Attention is All You Need")**:
      - Mecanismo de Auto-Atenção (*Self-Attention*): cálculo da matriz de pontuações de atenção entre todos os pares de tokens:
        Attention(Q, K, V) = softmax((Q · Kᵀ) / √d_k) · V
      - Mecanismo de Atenção Multi-Cabeça (*Multi-Head Attention*): projeção paralela em múltiplos subespaços de representação;
      - Codificação Posicional (*Positional Encoding* senoidal e RoPE - Rotary Position Embedding), conexões residuais (*Add*) e Normalização de Camadas (*LayerNorm / RMSNorm*);
      - Modelos baseados em Encoder (BERT, RoBERTa: representação bidirecional de contexto para extração, classificação e similaridade semântica) vs Modelos baseados em Decoder (GPT, LLaMA, Mistral: geração autorregressiva de texto token a token) vs Encoder-Decoder (T5).
    * Componentes e Conceitos Chave de LLMs:
      - Tokens e Tokenizadores modernos (Byte-Pair Encoding - BPE, WordPiece, SentencePiece);
      - Embeddings semânticos densos e Janela de Contexto (*Context Window*);
      - Alucinação (*Hallucination*): causas (limites de treinamento probabilístico, perda de contexto), métodos de detecção e atenuação;
      - Geração de dados sintéticos para treinamento e testes de segurança.
    * Engenharia de Prompts (*Prompt Engineering*):
      - Técnicas: *Zero-shot prompting*, *Few-shot prompting* (exemplos contextuais), Cadeia de Pensamento (*Chain-of-Thought - CoT*), *Tree-of-Thoughts (ToT)*, *Self-Consistency*;
      - Moderação de prompts, delimitação de papéis (*System, User, Assistant*) e combate a injeção de prompt (*Prompt Injection*).
    * Arquitetura Retrieval-Augmented Generation (**RAG**):
      - O fluxo do RAG: Ingestão documental → Pré-processamento e Limpeza → Particionamento (*Chunking*: estratégias fixa, por sentença, semântica e hierárquica) → Geração de Embeddings com modelos dedicados → Armazenamento e Indexação em Banco de Dados Vetorial (**Vector DB**: pgvector, Chroma, Pinecone, Qdrant) usando algoritmos HNSW (*Hierarchical Navigable Small World*) ou IVF → Consulta do usuário → Busca por similaridade de cosseno ou distância euclidiana → Recuperação dos Top-K chunks mais relevantes → Re-ordenação contextual com modelos Cross-Encoder (*Re-ranking*) → Montagem do Prompt Aumentado → Geração da resposta fundamentada pelo LLM;
      - Avaliação Quantitativa de RAG com o framework **RAGAS**: métricas de *Faithfulness* (fidelidade ao contexto recuperado), *Answer Relevance* (relevância da resposta à pergunta), *Context Precision* (precisão dos chunks recuperados) e *Context Recall* (cobertura total da informação necessária).
    * Adaptação e Ajuste Fino Eficiente de Modelos (**PEFT / Fine-Tuning**):
      - Limitações do Full Fine-Tuning (custo computacional astronômico e esquecimento catastrófico / *catastrophic forgetting*);
      - **LoRA (Low-Rank Adaptation)**: congelamento dos pesos originais do modelo W₀ e treinamento de matrizes de decomposição de baixo posto B × A (W = W₀ + ΔW = W₀ + B × A, onde r ≪ d);
      - **QLoRA (Quantized LoRA)**: quantização do modelo base em 4 bits (NormalFloat4 - NF4) com cálculo de gradientes em 16 bits (Brain Floating Point - bfloat16), viabilizando o ajuste fino de modelos de dezenas de bilhões de parâmetros em hardware restrito.
    * Agentes Autônomos de IA e Orquestração:
      - Arquitetura **ReAct (Reasoning + Acting)**: loop iterativo de Pensamento (*Thought*) → Ação (*Action*) → Observação (*Observation*) → Resposta Final;
      - Tool Calling e Function Calling com saída estruturada em JSON Schema;
      - Protocolos de Integração Contextual: **Protocolo MCP (Model Context Protocol)** da Anthropic para conexão padronizada entre LLMs e repositórios de dados e ferramentas locais/remotas;
      - Modelos Multimodais: processamento conjunto de texto, visão/imagens, áudio e código.
    * Ética, Governança e Segurança em Inteligência Artificial:
      - Vieses algorítmicos e discriminação indireta; Equidade (*Fairness*);
      - Interpretabilidade e Explicabilidade de Modelos (**XAI**): técnicas agnósticas de modelo: **SHAP** (Shapley Additive exPlanations baseado na Teoria dos Jogos Cooperativos com contribuições marginais de cada feature) e **LIME** (Local Interpretable Model-agnostic Explanations com aproximação linear local);
      - Supervisão Humana (*Human-in-the-Loop*);
      - Marco Legal da Inteligência Artificial no Brasil (**Projeto de Lei nº 2.338/2023**): classificação baseada em risco (sistemas de risco excessivo/vedados, sistemas de alto risco sujeitos a governança estrita e Avaliação de Impacto Algorítmico - AIA, sistemas de baixo risco).
  * **MLOps e Ciclo de Produção de Modelos:**
    * Os pilares do MLOps: Gestão de código, versionamento de dados e pipelines com **DVC (Data Version Control)**, rastreamento de experimentos e registro de modelos com **MLflow** (Tracking, Artifacts, Model Registry), implantação e monitoramento contínuo;
    * Monitoramento de Degradação de Modelos em Produção:
      - **Data Drift**: mudança na distribuição de probabilidade das variáveis de entrada P(X) ao longo do tempo (identificada por testes estatísticos como Kolmogorov-Smirnov e divergência de Kullback-Leibler);
      - **Concept Drift**: mudança na relação funcional entre as variáveis de entrada e o alvo P(Y|X) (ex.: novos padrões de fraude tributária ou cibernética); estratégias de retreinamento automatizado (*Continuous Training*).
  * **Pareamento de Dados (Record Linkage) e Regulação Tecnológica (TCU, CGU, CVM):**
    * Processo de Pareamento de Dados (*Record Linkage*): ligação de bases governamentais sem chave identificadora unificada (ex.: Receita Federal, INSS, CadÚnico);
    * Fases do Pareamento: Pré-processamento e padronização → Blocagem (*Blocking* para redução do produto cartesiano de comparações) → Comparação de atributos (métricas de similaridade de texto: Distância de Levenshtein, Jaro, Jaro-Winkler, similaridade de n-gramas) → Classificação de pares (determinística por regras exatas vs probabilística pelo modelo de Fellegi-Sunter) → Avaliação de qualidade do pareamento (falsos pares e pares perdidos);
    * Tecnologias de Regulação (**Regtech**) e Tecnologias de Supervisão (**Suptech**): conceitos e aplicações no mercado de capitais e financeiro (CVM e BACEN) para monitoramento de manipulação de mercado, *insider trading* e lavagem de dinheiro.

* **Checklist de Domínio Técnico Pré-Edital (Definição de Pronto):**
  - [ ] Consigo implementar em Python uma rotina completa com Scikit-Learn: `Pipeline` contendo `ColumnTransformer` (StandardScaler + OneHotEncoder), `RandomForestClassifier` e busca por `GridSearchCV`.
  - [ ] Sei formular a equação matemática da Auto-Atenção do Transformer e explicar a função de cada componente (Q, K, V, √d_k, softmax).
  - [ ] Sei detalhar e desenhar a arquitetura de um sistema RAG completo com particionamento semântico, banco vetorial e re-ranking.
  - [ ] Distingo com absoluta clareza a diferença técnica e o trade-off de recursos entre Full Fine-Tuning, LoRA e QLoRA.
  - [ ] Sei interpretar valores SHAP para explicar por que uma transação foi classificada como fraude por um modelo XGBoost.
  - [ ] Distingo Data Drift de Concept Drift e sei quais testes estatísticos usar para monitorar a estabilidade das features em produção.
  - [ ] Sei descrever as etapas do modelo de Fellegi-Sunter para pareamento probabilístico de bases de dados fiscais.
"""

print("Módulo de Core de TI compilado com sucesso.")
