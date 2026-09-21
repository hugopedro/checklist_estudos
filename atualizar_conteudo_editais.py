import re
import json

# 1. Update gerar_secoes_ti_core.py to include Frontend, Backend Java/C#, and Algoritmos
with open("/home/Hugo/Documentos/iniciando/gerar_secoes_ti_core.py", "r", encoding="utf-8") as f:
    core_code = f.read()

frontend_backend_algoritmos_markdown = """  * **Desenvolvimento Web Frontend Moderno e Interfaces de Usuário:**
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
"""

# Inject before Checklist de Dominio Tecnico of Disciplina 6
pattern_d6 = r"(\* \*\*Checklist de Domínio Técnico Pré-Edital \(Definição de Pronto\):\s*\n\s+- \[ \] Consigo calcular a contagem de pontos de função)"
if re.search(pattern_d6, core_code):
    core_code_updated = re.sub(pattern_d6, frontend_backend_algoritmos_markdown + "\n" + r"\1", core_code)
    with open("/home/Hugo/Documentos/iniciando/gerar_secoes_ti_core.py", "w", encoding="utf-8") as f:
        f.write(core_code_updated)
    print("Sucesso: Novos grupos de Frontend, Backend e Algoritmos adicionados a gerar_secoes_ti_core.py")
else:
    print("Aviso: Padrão não encontrado em gerar_secoes_ti_core.py!")

# 2. Update gerar_secoes_ti_infra_gov.py to include MITRE ATT&CK, Redes Avancadas, and Governo Digital
with open("/home/Hugo/Documentos/iniciando/gerar_secoes_ti_infra_gov.py", "r", encoding="utf-8") as f:
    infra_code = f.read()

mitre_attack_markdown = """  * **Framework MITRE ATT&CK Enterprise e Defesa Ativa:**
    * A Matriz MITRE ATT&CK Enterprise: Estrutura taxonômica hierárquica dividida em Táticas, Técnicas, Subtécnicas, Procedimentos e Mitigações;
    * As 14 Táticas Fundamentais do MITRE ATT&CK: Reconhecimento (Reconnaissance), Desenvolvimento de Recursos (Resource Development), Acesso Inicial (Initial Access), Execução (Execution), Persistência (Persistence), Escalação de Privilégios (Privilege Escalation), Evasão de Defesa (Defense Evasion), Acesso a Credenciais (Credential Access), Descoberta (Discovery), Movimento Lateral (Lateral Movement), Coleta (Collection), Comando e Controle (Command and Control - C2), Exfiltração (Exfiltration) e Impacto (Impact);
    * Principais Técnicas e Subtécnicas Mapeadas: Spearphishing, Pass-the-Hash, Golden Ticket/Silver Ticket no Active Directory, DLL Sideloading, Masquerading, Obfuscated Files, Powershell/WMI malicioso e Kerberoasting;
    * Aplicação Operacional em Cibersegurança: Mapeamento de grupos de ameaças persistentes avançadas (APTs), Threat Hunting, criação de regras analíticas com regras Sigma e regras YARA, e simulação de adversários com Atomic Red Team.
"""

redes_avancadas_markdown = """  * **Protocolos Avançados de Rede, Telefonia IP e Redes Sem Fio:**
    * Gerenciamento de Redes com SNMP (v1, v2c e v3): Arquitetura Agente-Gerente, Base de Informações de Gerenciamento (MIB-II), SMI, identificadores OID, operações (Get, GetNext, GetBulk, Set, Trap, Inform) e segurança no SNMPv3 (modelos USM com autenticação HMAC-SHA/MD5 e privacidade AES/DES, e modelo VACM de controle de acesso);
    * Comutação de Rótulos Multiprotocolo (MPLS): Roteadores de Borda de Rótulo (LER), Roteadores de Comutação de Rótulo (LSR), pilha de rótulos (Label Stacking), caminhos LSP, Engenharia de Tráfego (MPLS-TE) e VPNs MPLS de Camada 2 (VPLS/VPWS) e Camada 3 (BGP/MPLS IP VPN - RFC 4364);
    * Extensões de Segurança do DNS (DNSSEC): Proteção criptográfica contra envenenamento de cache (DNS Cache Poisoning) e ataques Man-in-the-Middle, tipos de registros (DNSKEY, RRSIG, DS, NSEC e NSEC3) e validação da cadeia de confiança hierárquica (Root Trust Anchor);
    * Redes Sem Fio IEEE 802.11 (Wi-Fi): Padrões e evolução (802.11a/b/g/n/ac e 802.11ax / Wi-Fi 6/6E), método de acesso ao meio CSMA/CA com RTS/CTS, canais e frequências (2.4 GHz, 5 GHz e 6 GHz), mecanismos de segurança sem fio (WPA2-Personal/Enterprise, WPA3 com SAE - Simultaneous Authentication of Equals e autenticação 802.1X com EAP);
    * Telefonia IP e Voz sobre IP (VoIP): Protocolo de Inicialização de Sessão (SIP - RFC 3261: mensagens INVITE, ACK, BYE, CANCEL, códigos de resposta 1xx a 6xx), Protocolo de Descrição de Sessão (SDP), transporte em tempo real com RTP (Real-time Transport Protocol) e RTCP (RTP Control Protocol), e codecs de áudio (G.711, G.729);
    * Cabeamento Estruturado e Meios Físicos (Normas ABNT NBR 14565 e ANSI/TIA-568): Subsistemas de cabeamento estruturado (cabeamento horizontal, backbone de campus e edifício, sala de equipamentos, área de trabalho), categorias de cabos de par trançado UTP/STP (Cat 5e, Cat 6, Cat 6a até 10 Gbps), Fibras Ópticas Monomodo (SMF - núcleos de 9 µm para longas distâncias) vs Multimodo (MMF - núcleos de 50/62.5 µm: OM3, OM4), conectores ópticos (LC, SC) e tipos de polimento (PC, UPC, APC).
"""

governo_digital_markdown = """  * **Marco Legal do Governo Digital, Inovação e Legislação Estratégica de TIC:**
    * Lei do Governo Digital (Lei nº 14.129/2021): Princípios, diretrizes, digitalização compulsória de processos e serviços públicos, Plataforma Única Gov.br, interoperabilidade de bases de dados do setor público, autosserviço cidadão e transparência;
    * Estratégia Nacional de Governo Digital e Decretos Regulamentadores (Decreto nº 10.332/2020 e atualizações): Metas de transformação digital dos órgãos federais, identidade digital segura e catálogo unificado de serviços públicos;
    * Marco Legal das Startups e Empreendedorismo Inovador (Lei Complementar nº 182/2021): Contrato Público de Solução Inovadora (CPSI) para teste de soluções inovadoras desenvolvidas por startups, critérios diferenciados de julgamento, dispensa de licitação e limites de remuneração;
    * Marco Civil da Internet (Lei nº 12.965/2014) e Governança de Dados: Neutralidade de rede, prazos obrigatórios de guarda de registros de conexão (1 ano) e registros de acesso a aplicações (6 meses), responsabilidade civil por conteúdo de terceiros e procedimentos judiciais de requisição de dados.
"""

# Inserir MITRE ATT&CK em Disciplina 8 antes do checklist
pattern_d8 = r"(\* \*\*Checklist de Domínio Técnico Pré-Edital \(Definição de Pronto\):\s*\n\s+- \[ \] Sei mapear os 93 controles da ISO 27002:2022)"
if re.search(pattern_d8, infra_code):
    infra_code = re.sub(pattern_d8, mitre_attack_markdown + "\n" + r"\1", infra_code)
    print("Sucesso: Grupo MITRE ATT&CK adicionado a Disciplina 8.")

# Inserir Redes Avançadas em Disciplina 9 antes do checklist
pattern_d9 = r"(\* \*\*Checklist de Domínio Técnico Pré-Edital \(Definição de Pronto\):\s*\n\s+- \[ \] Sei calcular rapidamente sub-redes IPv4)"
if re.search(pattern_d9, infra_code):
    infra_code = re.sub(pattern_d9, redes_avancadas_markdown + "\n" + r"\1", infra_code)
    print("Sucesso: Grupo Redes Avançadas adicionado a Disciplina 9.")

# Inserir Governo Digital em Disciplina 10 antes do checklist
pattern_d10 = r"(\* \*\*Checklist de Domínio Técnico Pré-Edital \(Definição de Pronto\):\s*\n\s+- \[ \] Sei listar de cor os 5 domínios do COBIT 2019)"
if re.search(pattern_d10, infra_code):
    infra_code = re.sub(pattern_d10, governo_digital_markdown + "\n" + r"\1", infra_code)
    print("Sucesso: Grupo Governo Digital adicionado a Disciplina 10.")

with open("/home/Hugo/Documentos/iniciando/gerar_secoes_ti_infra_gov.py", "w", encoding="utf-8") as f:
    f.write(infra_code)

print("Arquivos de seções atualizados com sucesso!")
