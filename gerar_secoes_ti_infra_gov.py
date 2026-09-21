# Modulo com Disciplinas 8, 9 e 10 (Seguranca, Infra/Cloud e Governanca/Contratos)

def get_secoes_ti_infra_gov():
    return r"""### DISCIPLINA 8: Segurança da Informação e Computação Forense
* **Incidência Comprovada nos 10 Editais Oficiais Locais:** **10/10 (100%)**
  * Presente expressamente em todos os 10 certames de topo auditados:
    * [`Senado Federal 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) (FGV, Pág. 33 e Pág. 34 - ISO 27001/2/5, MITRE ATT&CK, CIS Controls, NIST SP 800-61, CyBOK);
    * [`Câmara dos Deputados 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) (FGV, Pág. 30-31 - ISO 27001/2/5, ISO 15408, NIST CSF, NIST RMF, MITRE ATT&CK, Blue/Red Team);
    * [`BACEN 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) (Cebraspe, Pág. 36 - 7 itens de Segurança: IAM, MITRE ATT&CK, CIS Controls, NIST CSF, Criptografia);
    * [`TCU 2021`](file:///home/Hugo/Documentos/iniciando/editais/edital_04_tcu_2021_aufc_ti.pdf) (FGV, Pág. 28 - Princípios CIDAN, Políticas de segurança, Incidentes, LGPD, LAI);
    * [`Polícia Federal 2018`](file:///home/Hugo/Documentos/iniciando/editais/edital_05_pf_2018_perito_ti.pdf) (Cebraspe, Pág. 53 - Engenharia Reversa, Análise de Malware, Criptografia RSA/AES/Hashes, ISO 27001/2);
    * [`SEFAZ-SC 2026`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) (FCC, Pág. 29 - IAM, MFA, RBAC, WAF, Firewalls, IDS/IPS, Criptografia, PKI, LGPD aplicada a IA);
    * [`SEFAZ-MG 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_07_sefaz_mg_2022_auditor_ti.pdf) (FGV, Pág. 49 - Zero Trust, Forense Computacional: hash, cadeia de custódia, espelhamento, antiforense, wipe);
    * [`TCDF 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) (Cebraspe, Pág. 44 - ISO 27001/2/5, 2FA, OAuth2, OIDC, JWT, OWASP Top 10, Criptografia, LGPD);
    * [`CGU 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) (FGV, Pág. 28-29 - Zero Trust, CIS Controls v8, DLP, SIEM, IN GSI 1/2020 e NC 05, 08, 21);
    * [`CVM 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) (FGV, Pág. 32-33 - ISO 27001/2/5, CIS Controls v8, Blue/Red Team, MITRE ATT&CK, NIST CSF, SIEM, IAM).

* **Stack Tecnológico Oficial Mapeado:**
  * **Normas e Padrões:** ABNT NBR ISO/IEC 27001:2022, 27002:2022 (os 93 controles em 4 temas), 27005:2022, 15408 (Common Criteria), 27037 (Evidências Digitais), 38500.
  * **Frameworks de Segurança:** CIS Controls v8 (18 controles e 3 IGs), NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover), NIST RMF (SP 800-37), NIST SP 800-53 Rev. 5, NIST SP 800-61 Rev. 2 (Incident Response), SANS Incident Handler's Handbook, MITRE ATT&CK Framework, CyBOK.
  * **Criptografia e PKI:** AES (modos CBC, CTR, GCM), RSA, ECC (ECDSA, Ed25519), Diffie-Hellman (ECDHE / PFS), Hashes (SHA-256, SHA-512, SHA-3, HMAC), ICP-Brasil (certificados A1, A3, S1-S4, T3), X.509 v3, TLS 1.3.
  * **Segurança de Aplicações & IAM:** OWASP Top 10 Web (2021/2025), OWASP API Security Top 10, SAST, DAST, IAST, SCA, OAuth 2.0 (com extensão PKCE), OpenID Connect (OIDC), JWT, SAML 2.0, MFA (TOTP / FIDO2 WebAuthn), SSO, PAM.
  * **Defesa Cibernética & Ferramentas:** Next-Generation Firewall (NGFW), WAF, IDS/IPS (Snort, Suricata), EDR/XDR, SIEM/SOAR, DLP, Zero Trust (NIST SP 800-207), SPF, DKIM, DMARC.
  * **Computação Forense e Engenharia Reversa:** Volatility 3 / 2, LiME, EnCase (E01), dd/raw, Scalpel, PhotoRec, Ghidra, IDA Pro, x64dbg, OllyDbg, Sysinternals (ProcMon, Process Hacker, Autoruns), Wireshark.
  * **Legislação e Normativos:** LGPD (Lei nº 13.709/2018), Marco Civil da Internet (Lei nº 12.965/2014), Lei de Acesso à Informação (Lei nº 12.527/2011), Código de Processo Penal (arts. 158-A a 158-F - Cadeia de Custódia), IN GSI/PR nº 1/2020 e NC 05, 08 e 21 da Presidência da República.

* **Ementa Granular Ponto a Ponto:**
  * **Fundamentos, Princípios e Gestão da Segurança da Informação:**
    * Os 5 Princípios Fundamentais (CIDAN): Confidencialidade (acesso restrito apenas a entidades autorizadas), Integridade (exatidão e completude da informação e seus métodos de processamento), Disponibilidade (acesso e uso garantidos quando requeridos), Autenticidade (garantia de identidade do autor) e Não Repúdio / Irretratabilidade (impossibilidade de negar a autoria ou recebimento de uma transação);
    * Privacy by Design e Privacy by Default;
    * Classificação da Informação: confidencial, restrita, pública; critérios de rotulação e manuseio;
    * Família ISO/IEC 27000:
      * **ABNT NBR ISO/IEC 27001:2022 / 2013**: Estrutura do Sistema de Gestão de Segurança da Informação (SGSI); Ciclo PDCA / Estrutura de alto nível (Cláusulas 4 a 10: Contexto, Liderança, Planejamento, Apoio, Operação, Avaliação de Desempenho e Melhoria); Elaboração da Declaração de Aplicabilidade (SoA);
      * **ABNT NBR ISO/IEC 27002:2022 / 2013**: Código de Práticas e Controles de Segurança. Reestruturação da versão 2022 em **4 temas e 93 controles**: Controles Organizacionais (37), Controles de Pessoas (8), Controles Físicos (14) e Controles Tecnológicos (34); Novos controles críticos: Inteligência contra ameaças (*Threat intelligence*), Segurança para uso de computação em nuvem, Prontidão de TIC para continuidade de negócios, Monitoramento físico de segurança, Gerenciamento de configuração, Mascaramento de dados, Prevenção contra vazamento de dados (DLP), Monitoramento de atividades, Filtragem web e Codificação segura;
      * **ABNT NBR ISO/IEC 27005:2022 / 2019**: Gestão de Riscos de Segurança da Informação; Processo de avaliação de riscos: identificação de ativos, ameaças, vulnerabilidades e impactos; análise qualitativa vs quantitativa; opções de tratamento de risco: modificação/mitigação, retenção/aceitação, evitação e compartilhamento/transferência; Níveis de aceitação de riscos e risco residual.
    * Frameworks Internacionais de Segurança Cibernética:
      * **NIST Cybersecurity Framework (NIST CSF 2.0 / 1.1)**: As funções centrais: Governar (*Govern* - governança de riscos, políticas e supervisão), Identificar (*Identify*), Proteger (*Protect*), Detectar (*Detect*), Responder (*Respond*) e Recuperar (*Recover*); Categorias e subcategorias de controles; Níveis de implementação (Tiers 1 a 4) e Perfis (*Profiles*);
      * **CIS Critical Security Controls Version 8 (CIS Controls v8)**: Os 18 Controles de Segurança Críticos; Grupos de Implementação (IG1: higiene cibernética essencial; IG2 e IG3);
      * **MITRE ATT&CK Framework**: Matriz Enterprise para mapeamento de táticas, técnicas e procedimentos (**TTPs**) de adversários; Matriz de táticas: Reconhecimento, Desenvolvimento de Recursos, Acesso Inicial, Execução, Persistência, Elevação de Privilégio, Evasão de Defesa, Acesso a Credenciais, Descoberta, Movimentação Lateral, Coleta, Comando e Controle, Exfiltração e Impacto; Uso do framework para emulação de adversários e Threat Hunting.
  * **Criptografia, Algoritmos e Infraestrutura de Chaves Públicas (ICP-Brasil):**
    * Princípio de Kerckhoffs: a segurança deve residir exclusivamente no segredo da chave criptográfica, não no algoritmo.
    * Criptografia Simétrica:
      * Cifras de bloco vs cifras de fluxo;
      * Algoritmos: DES (56 bits, inseguro), Triple-DES (3DES), **AES (Advanced Encryption Standard)**: baseado no Rijndael, bloco fixo de 128 bits, chaves de 128, 192 e 256 bits, transformações SubBytes, ShiftRows, MixColumns e AddRoundKey; RC4 (cifra de fluxo vulnerável a viés de bytes);
      * Modos de Operação:
        - **ECB (Electronic Codebook)**: encriptação independente de blocos; grave falha: preserva padrões do texto claro;
        - **CBC (Cipher Block Chaining)**: encadeamento de blocos com XOR e Vetor de Inicialização (**IV**) aleatório; vulnerabilidade a ataques de oráculo de preenchimento (*Padding Oracle*);
        - **CTR (Counter Mode)**: modo contador, transforma a cifra de bloco em cifra de fluxo, permitindo paralelismo total de encriptação/decriptação;
        - **GCM (Galois/Counter Mode)**: Criptografia Autenticada com Dados Associados (**AEAD**); combina o modo CTR com autenticação matemática GHASH, garantindo confidencialidade e integridade simultâneas com altíssima performance.
    * Criptografia Assimétrica (Chave Pública):
      * **RSA**: baseado na dificuldade de fatoração de inteiros produtos de dois primos grandes n = p × q; função totiente de Euler ϕ(n); chaves recomendadas ≥ 2048/4096 bits;
      * **Criptografia de Curva Elíptica (ECC)**: baseada na dificuldade do logaritmo discreto sobre curvas elípticas finitas; curvas padrão (secp256k1, Ed25519); chaves muito menores com segurança equivalente (ECC 256 bits ≈ RSA 3072 bits);
      * Protocolo de Troca de Chaves **Diffie-Hellman** (DH) e Diffie-Hellman de Curva Elíptica Efêmero (**ECDHE**), garantindo o Sigilo de Encaminhamento Perfeito (**PFS - Perfect Forward Secrecy**).
    * Funções de Hash Criptográficas e HMAC:
      * Propriedades matemáticas: resistência à pré-imagem (unidirecionalidade), resistência à segunda pré-imagem e resistência a colisões (ataque do aniversário);
      * Algoritmos: MD5 (128 bits, quebrado), SHA-1 (160 bits, quebrado), família **SHA-2** (SHA-256, SHA-512) e família **SHA-3** (Keccak, arquitetura de esponja); Código de Autenticação de Mensagem baseado em Hash (**HMAC**).
    * Assinatura Digital e Certificação Digital:
      * Mecânica da Assinatura Digital: hash cifrado com chave privada do remetente e validado com chave pública; garantias de integridade, autenticidade e não repúdio;
      * Estrutura de Certificados **ITU-T X.509 v3**: versão, número de série, algoritmo, emissor, validade, sujeito, chave pública, extensões (Key Usage, Extended Key Usage, SAN); Revogação: Lista de Certificados Revogados (**CRL**) e Protocolo Online (**OCSP** e OCSP Stapling);
      * **ICP-Brasil**: Autoridade Certificadora Raiz (AC-Raiz / ITI), Autoridades Certificadoras (ACs de 1º e 2º nível), Autoridades de Registro (ARs); Tipos de certificados: A1 (software, validade 1 ano), A3 (hardware seguro token/smartcard, validade até 5 anos), certificados de sigilo (S1-S4) e carimbo do tempo (T3).
  * **Segurança de Aplicações Web (AppSec), DevSecOps e OWASP:**
    * **OWASP Top 10 Web Application Security Risks**:
      1. *A01: Broken Access Control* (Quebra de controle de acesso: IDOR, elevação de privilégios);
      2. *A02: Cryptographic Failures* (Falhas criptográficas: transmissão em texto claro, chaves fracas, cifras obsoletas);
      3. *A03: Injection* (SQL Injection / SQLi clássico, blind, time-based; Command Injection; LDAP Injection; mitigação por consultas parametrizadas / PreparedStatement e validação rigorosa de entrada);
      4. *A04: Insecure Design* (Design inseguro: ausência de modelagem de ameaças e testes de regras de negócio);
      5. *A05: Security Misconfiguration* (Configurações incorretas: senhas padrão, headers HTTP de segurança ausentes como CSP, HSTS, X-Frame-Options);
      6. *A06: Vulnerable and Outdated Components* (Componentes desatualizados com vulnerabilidades CVE conhecidas);
      7. *A07: Identification and Authentication Failures* (Falhas de autenticação: força bruta, credential stuffing, ausência de MFA);
      8. *A08: Software and Data Integrity Failures* (Falhas de integridade: plugins não assinados, desserialização insegura de objetos);
      9. *A09: Security Logging and Monitoring Failures* (Falhas de log e monitoramento: ausência de trilha de auditoria);
      10. *A10: Server-Side Request Forgery (SSRF)* (Falsificação de requisições no lado do servidor para acessar metadados de nuvem e redes internas).
    * Outras Vulnerabilidades Web Críticas: Cross-Site Scripting (**XSS**: Stored, Reflected e DOM-based; mitigação por codificação de saída sensível ao contexto e CSP), Cross-Site Request Forgery (**CSRF**: tokens anti-CSRF e cookies SameSite=Strict), XML External Entity (**XXE**).
    * Testes de Segurança em Aplicações: **SAST** (Static Application Security Testing - código-fonte), **DAST** (Dynamic Application Security Testing - tempo de execução), **IAST** (Interactive) e **SCA** (Software Composition Analysis - gestão de dependências de código aberto).
  * **Gestão de Identidade e Acesso (IAM), Federação e Autenticação:**
    * Modelos de Controle de Acesso: DAC (Discricionário), MAC (Mandatório: modelos Bell-LaPadula para sigilo e Biba para integridade), RBAC (Baseado em Papéis) e ABAC (Baseado em Atributos);
    * Autenticação Multifator (**MFA**): três fatores clássicos (conhecimento, posse e inerência); protocolos **TOTP** (RFC 6238) e **HOTP** (RFC 4226); Padrão **FIDO2 / WebAuthn** (autenticação forte sem senha resistente a phishing);
    * Protocolos de Federação de Identidade:
      - **Single Sign-On (SSO)**: autenticação centralizada;
      - **OAuth 2.0 (RFC 6749)**: framework de autorização; Papéis: Resource Owner, Client, Authorization Server, Resource Server; Tipos de concessão (*Grant Types*): Authorization Code Grant com extensão **PKCE** (obrigatória para clientes públicos, SPAs e apps móveis), Client Credentials Grant (máquina a máquina);
      - **OpenID Connect (OIDC)**: camada de identidade e autenticação sobre o OAuth 2.0; emissão do **ID Token** no formato JSON Web Token (**JWT**);
      - **JSON Web Token (JWT - RFC 7519)**: estrutura Base64URL em três seções: Header (algoritmo `alg` e tipo `typ`), Payload (claims registradas: `iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`; claims customizadas) e Signature (garantia de integridade com HMAC ou RSA/ECDSA);
      - **SAML 2.0**: padrão XML para troca de asserções de identidade entre IdP e SP;
      - **PAM (Privileged Access Management)**: gestão de contas de privilégio elevado, cofre de senhas, rotação automática de credenciais, auditoria e gravação de sessões administrativas.
  * **Segurança de Redes, Defesa e Monitoramento Cibernético:**
    * Dispositivos de Perímetro: Firewalls de Filtragem de Pacotes sem Estado (*Stateless*), Firewalls de Inspeção de Estado (*Stateful Inspection*), Firewalls de Próxima Geração (**NGFW**: inspeção profunda de pacotes L7, descriptografia SSL/TLS, prevenção integrada de intrusões); Web Application Firewall (**WAF**);
    * Sistemas de Detecção e Prevenção de Intrusão (**IDS/IPS**): detecção baseada em assinaturas vs anomalias comportamentais (Snort, Suricata);
    * Prevenção contra Vazamento de Dados (**DLP - Data Loss Prevention**): detecção e bloqueio de exfiltração de dados sensíveis em repouso, em trânsito e em uso;
    * Segurança de Endpoints: Antivírus tradicional vs **EDR** (Endpoint Detection and Response) e **XDR** (Extended Detection and Response): telemetria contínua, visibilidade de processos e contenção automatizada;
    * Gestão de Eventos e Segurança da Informação (**SIEM**) e Orquestração (**SOAR**): centralização de logs (Syslog RFC 5424, Windows Event Logs), normalização, enriquecimento, correlação de eventos em tempo real, geração de alertas e execução de playbooks automáticos de resposta;
    * **Arquitetura Zero Trust (NIST SP 800-207)**: Os 3 princípios essenciais: Verificar explicitamente, Usar acesso com privilégio mínimo e Presumir a violação (*Assume Breach*); Ponto de Decisão de Política (**PDP**: Policy Engine + Policy Administrator) e Ponto de Aplicação de Política (**PEP**); Microssegmentação de rede;
    * Segurança de E-mail: **SPF** (registro TXT de servidores de envio autorizados), **DKIM** (assinatura criptográfica de mensagens) e **DMARC** (política de conformidade `none`, `quarantine`, `reject` com relatórios agregados e forenses);
    * Ameaças e Ataques Corporativos: Negação de Serviço (**DoS / DDoS**: SYN Flood, UDP Flood, NTP/DNS Amplification, HTTP Flood, Slowloris); Engenharia Social (Phishing, Spear Phishing, Whaling, Vishing, Smishing); Ransomware (dupla e tripla extorsão com vazamento de dados); Ataques de Rede: Man-in-the-Middle (MitM), ARP Spoofing/Poisoning, DNS Spoofing, DHCP Starvation/Rogue, varredura de portas com Nmap (SYN scan, FIN scan, Xmas scan);
    * Práticas de **Blue Team** (defesa ativa, threat hunting e monitoramento) e **Red Team** (testes de intrusão ofensivos / PenTest e emulação de adversários); Metodologia **CVSS v3.1 / v4.0** para pontuação de gravidade de vulnerabilidades.
  * **Gestão e Resposta a Incidentes de Segurança Cibernética:**
    * Guias Oficiais: **NIST SP 800-61 Rev. 2** (Computer Security Incident Handling Guide) e **SANS Incident Handler's Handbook**;
    * As 4 Fases do Ciclo de Vida de Resposta a Incidentes:
      1. *Preparação*: criação da equipe CSIRT/CERT, ferramentas de coleta e contenção, procedimentos operacionais padronizados;
      2. *Detecção e Análise*: identificação de Indicadores de Comprometimento (**IoCs**: hashes, IPs, domínios de C2, artefatos de persistência), triagem, determinação do escopo e priorização do incidente;
      3. *Contenção, Erradicação e Recuperação*: contenção de curto e longo prazo (isolamento de rede, bloqueio de portas/rotas); erradicação da causa raiz (remoção de malwares, encerramento de contas comprometidas, aplicação de patches); recuperação segura de sistemas e dados a partir de backups limpos, validação operacional e monitoramento reforçado;
      4. *Atividade Pós-Incidente (Lições Aprendidas)*: reunião retrospectiva, elaboração do relatório técnico circunstanciado, aprimoramento das defesas preventivas.
    * Continuidade de Negócios e Recuperação de Desastres:
      - Plano de Continuidade de Negócios (**PCN**), Análise de Impacto nos Negócios (**BIA**), Plano de Recuperação de Desastres (**DRP**);
      - Métricas Vitais: **RPO** (Recovery Point Objective - tolerância máxima a perda temporal de dados) e **RTO** (Recovery Time Objective - tempo máximo aceitável para restauração dos serviços);
      - Ambientes Alternativos: *Cold Site*, *Warm Site* e *Hot Site*;
      - Estratégias de Backup: Backup Completo (*Full*), Incremental (apenas alterações desde o último backup completo ou incremental) e Diferencial (alterações desde o último backup completo); Regra de Backup 3-2-1 (3 cópias de dados, 2 mídias distintas, 1 cópia externa/em nuvem).
  * **Computação Forense Digital e Perícia Tecnológica (PF, PCDF, Fiscos e Tribunais de Contas):**
    * **Cadeia de Custódia da Prova Digital**:
      - Disciplina legal no Código de Processo Penal (**arts. 158-A a 158-F do CPP**): 10 etapas legais: Reconhecimento, Isolamento, Fixação, Coleta, Acondicionamento, Transporte, Recebimento, Processamento, Armazenamento e Descarte;
      - Norma **ABNT NBR ISO/IEC 27037:2014**: Diretrizes para identificação, coleta, aquisição e preservação de evidência digital;
      - Ordem de Volatilidade de Dados (**RFC 3227**): 1. Registradores da CPU e cache; 2. Tabela de roteamento, cache ARP, tabela de processos, estatísticas de kernel e memória RAM; 3. Sistemas de arquivos temporários; 4. Discos rígidos e mídias de armazenamento permanente; 5. Dados de configuração remota e topologia de rede; 6. Mídias de backup físico.
    * Procedimentos de Coleta e Aquisição de Evidências:
      - Coleta ao vivo (*Live Acquisition*) vs Coleta pós-morte (*Dead / Post-Mortem Acquisition*);
      - Aquisição física bit a bit (*Physical Image*): extração completa incluindo setores alocados, espaço não alocado (*unallocated space*) e folga de cluster (*slack space*);
      - Formatos de imagem forense: RAW (`dd`), Expert Witness Format (`E01` - formato EnCase com compressão e metadados de aquisição) e Advanced Forensic Format (`AFF`);
      - Uso compulsório de bloqueadores de escrita de hardware (*write blockers*) ou software para garantir a inalterabilidade da mídia sob exame pericial;
      - Garantia de integridade: cálculo imediato do hash criptográfico (MD5, SHA-1, SHA-256) antes e após a aquisição, devendo coincidir perfeitamente.
    * Análise Forense em Sistemas Windows:
      - Registro do Windows: arquivos de colmeia (*hives*) em `\Windows\System32\config` (SAM, SYSTEM, SOFTWARE, SECURITY) e `NTUSER.DAT` no perfil do usuário; Artefatos de execução recente: chaves `Run`, `RunOnce`, `UserAssist`, `Shimcache` (AppCompatCache), `Amcache.hve`;
      - Arquivos **Prefetch** (`\Windows\Prefetch\*.pf`): evidência forense irrefutável de execução de programas (nome do executável, carimbos de data/hora das últimas 8 execuções, contagem de execuções, DLLs carregadas);
      - Sistema de Arquivos NTFS: Master File Table (**MFT** - registro de 1024 bytes, atributos `$STANDARD_INFORMATION` e `$FILE_NAME` com carimbos MACB: Modified, Accessed, Created, Born; detecção de manipulação maliciosa de carimbos - *Timestomping* pela divergência entre os atributos); Fluxos Alternativos de Dados (**ADS - Alternate Data Streams**: sintaxe `arquivo.txt:malware.exe`, Zone.Identifier de downloads); Log de transações do NTFS (`$LogFile`) e Diário USN (`$UsnJrnl`);
      - Volume Shadow Copies (**VSS** - pontos de restauração do Windows com versões históricas de arquivos);
      - Logs de Eventos do Windows (`.evtx` em `\Windows\System32\winevt\Logs`): Security Log (Event ID 4624 - Logon bem-sucedido com identificação do tipo de logon 2 interativo, 3 rede, 10 RDP; Event ID 4625 - Falha de logon; Event ID 4672 - Atribuição de privilégios especiais; Event ID 4688 - Criação de processo com linha de comando completa);
      - Arquivo de hibernação (`hiberfil.sys`) e arquivo de paginação (`pagefile.sys`).
    * Análise Forense em Sistemas Linux:
      - Análise de logs em `/var/log` (`auth.log`/`secure` para autenticações e comandos sudo, `syslog`/`messages`, `wtmp` para histórico de logons, `btmp` para tentativas falhas, `lastlog`);
      - Histórico de comandos Bash (`.bash_history`, variáveis `HISTCONTROL`, `HISTTIMEFORMAT`);
      - Sistema de Arquivos Ext4: Superbloco, Descritores de grupos de blocos, Tabela de Inodes (estrutura do inode, ponteiros diretos, indiretos e Extents; atributos temporais atime, mtime, ctime, crtime); Journaling do Ext4 (modos journal, ordered e writeback).
    * Análise Forense de Memória RAM:
      - Coleta ao vivo da memória volátil: ferramentas LiME (Linux Memory Extractor), WinPmem, DumpIt;
      - Análise de dumps de memória com o framework **Volatility (Volatility 3 / Volatility 2)**: Plugins fundamentais: `windows.pslist` (lista processos ativos baseada na lista duplamente encadeada `_EPROCESS`), `windows.psscan` (varredura da memória por estruturas de processos ocultos que desvincularam seu ponteiro para esconder rootkits), `windows.netscan` (conexões de rede ativas no momento do dump), `windows.malfind` (detecta injeção de DLL e código executável em memória alocada com `PAGE_EXECUTE_READWRITE`), `windows.cmdline` (argumentos de linha de comando dos processos), `windows.hashdump` (extração de hashes NTLM da memória).
    * Recuperação de Arquivos Apagados (*File Carving*):
      - Reconstrução de arquivos no espaço não alocado através da busca por assinaturas de cabeçalho (*File Headers / Magic Bytes*) e rodapé (*File Footers / Trailing Bytes*); Ferramentas: Scalpel, Foremost, PhotoRec.
    * Técnicas Antiforense:
      - Sanitização de Discos (*Wiping*): sobregravação de dados conforme normas internacionais (NIST SP 800-88 Rev. 1: Clear, Purge, Destroy; DoD 5220.22-M com passadas de padrões de bytes); Desmagnetização (*Degaussing*) e Destruição física;
      - Esteganografia: ocultação de mensagens secretas em arquivos carreadores (imagens, áudios); técnica do Bit Menos Significativo (**LSB - Least Significant Bit**); Técnicas de esteganálise (análise de qui-quadrado em histogramas de cores e anomalias de entropia);
      - Timestomping: alteração deliberada de metadados temporais;
      - Uso de criptografia completa de disco (BitLocker, LUKS, FileVault) e contêineres ocultos (VeraCrypt).
    * Engenharia Reversa e Análise de Malware:
      - Análise Estática: Verificação de hashes criptográficos, estrutura do cabeçalho Portable Executable (**PE** no Windows: DOS Header, PE Header, seções `.text`, `.data`, `.rsrc`), tabela de importação de APIs (**IAT - Import Address Table**: identificação de APIs suspeitas como `VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread`), extração de strings legíveis (`strings`);
      - Desensambladores e Decompiladores: **Ghidra** e **IDA Pro**; Análise de instruções em linguagem Assembly x86/x64 (registradores EAX/RAX, EBX/RBX, ESP/RSP, EBP/RBP, EIP/RIP; flags; convenções de chamada `cdecl`, `stdcall`, `fastcall`); Identificação de ofuscação de código e empacotadores de executáveis (**Packers** como UPX; alta entropia de seções);
      - Análise Dinâmica: Execução em ambiente seguro isolado (*Sandbox* como Cuckoo Sandbox); Monitoramento de processos, alterações no Registro do Windows e no sistema de arquivos com ferramentas Sysinternals (**Process Monitor / ProcMon**, **Process Hacker**, **Process Explorer**, **Autoruns**); Monitoramento de tráfego de rede e domínios de comando e controle com Wireshark;
      - Análise com Debuggers (**x64dbg**, **OllyDbg**, **WinDbg**): execução passo a passo (*step into*, *step over*), definição de pontos de parada (*breakpoints* de software `INT 3 / 0xCC`, de hardware e de memória); Mecanismos de detecção anti-debugging (`IsDebuggerPresent`, checagem do bloco PEB) e técnicas de bypass.
  * **Legislação e Aspectos Normativos de Segurança da Informação:**
    * **Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018)**:
      - Princípios fundamentais do art. 6º: Finalidade, adequação, necessidade, livre acesso, qualidade dos dados, transparência, segurança, prevenção, não discriminação e responsabilização/prestação de contas;
      - As 10 bases legais para tratamento de dados pessoais (art. 7º: consentimento, cumprimento de obrigação legal/regulatória, execução de políticas públicas pela administração, estudos por órgão de pesquisa, execução de contrato, exercício regular de direitos, proteção da vida, tutela da saúde, legítimo interesse do controlador e proteção do crédito); Bases legais estritas para dados pessoais sensíveis (art. 11);
      - Direitos dos titulares (art. 18: confirmação de existência, acesso, correção, anonimização, bloqueio, eliminação, portabilidade, revogação do consentimento);
      - Agentes de tratamento: Controlador, Operador e Encarregado de Proteção de Dados (**DPO**); Responsabilidade civil e solidariedade;
      - Relatório de Impacto à Proteção de Dados Pessoais (**RIPD / DPIA**); Comunicação obrigatória de incidentes de segurança à **ANPD** e aos titulares afetados em prazo razoável;
      - Sanções administrativas do art. 52 (advertência, multa simples de até 2% do faturamento limitada a R$ 50 milhões por infração, multa diária, publicização da infração, bloqueio ou eliminação de dados, suspensão parcial ou total do banco de dados).
    * **Marco Civil da Internet (Lei nº 12.965/2014)**: Princípios, garantias e direitos; Neutralidade de rede; Dever de guarda de registros de conexão (prazo obrigatório de 1 ano para provedores de conexão à internet) e de registros de acesso a aplicações de internet (prazo de 6 meses para provedores de aplicação); Procedimento judicial para requisição de registros e quebra de sigilo.
    * **Lei de Acesso à Informação (LAI - Lei nº 12.527/2011)**: Publicidade como preceito geral e sigilo como exceção; Transparência ativa vs transparência passiva; Classificação da informação sigilosa em três graus com prazos máximos: Ultrassecreta (25 anos), Secreta (15 anos) e Reservada (5 anos); Hipóteses de restrição de acesso a informações pessoais relativas à intimidade, vida privada, honra e imagem (prazo máximo de 100 anos).
    * **Normativos de Segurança da Administração Pública Federal (GSI/PR)**: Instrução Normativa GSI/PR nº 1/2020 (Estrutura de Gestão de Segurança da Informação); Normas Complementares (NC 05/IN01/DSIC/GSIPR - Criação de Equipes de Tratamento de Incidentes de Redes / ETIR; NC 08 - Gestão de Riscos de Segurança da Informação; NC 21 - Uso de Criptografia nos órgãos públicos federais).

* **Checklist de Domínio Técnico Pré-Edital (Definição de Pronto):**
  - [ ] Sei mapear os 93 controles da ISO 27002:2022 em seus 4 temas (Organizacionais, Pessoas, Físicos, Tecnológicos).
  - [ ] Consigo descrever o fluxo completo do handshake TLS 1.3, explicando por que ele elimina uma ida-e-volta (1-RTT) e como garante o Perfect Forward Secrecy com ECDHE.
  - [ ] Sei formular a diferença entre os modos de operação de cifras de bloco (ECB, CBC, CTR, GCM) e demonstrar por que o GCM é o padrão ouro na nuvem.
  - [ ] Sei implementar a mitigação contra SQL Injection utilizando consultas parametrizadas em Python/Java e demonstrar a falha clássica de concatenação de strings.
  - [ ] Conheço as 10 etapas da cadeia de custódia dos arts. 158-A a 158-F do CPP e sei aplicar a ordem de volatilidade da RFC 3227 em um laudo pericial.
  - [ ] Sei analisar a saída do Volatility (`windows.pslist` vs `windows.psscan` vs `windows.netscan`) para identificar um processo malicioso oculto e suas conexões de C2.
  - [ ] Sei listar de memória as 10 bases legais do art. 7º da LGPD e os direitos dos titulares do art. 18.

---

### DISCIPLINA 9: Redes de Computadores, Sistemas Operacionais e Nuvem
* **Incidência Comprovada nos 10 Editais Oficiais Locais:** **9/10 (90%)**
  * Cobrada em quase todos os certames de topo analisados:
    * [`Senado Federal 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) (FGV, Pág. 33-34 - Storage SAN/NAS, Puppet/Ansible, VMWare, Docker, K8s, Cloud AWS/Azure, Linux, Windows Server, TCP/IP, OSPF, BGP);
    * [`Câmara dos Deputados 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) (FGV, Pág. 30 - Windows Server, Linux, IaC, Virtualização, Redes TCP/IP/OSPF/BGP/SDN, Docker, Kubernetes, Nuvem);
    * [`BACEN 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) (Cebraspe, Pág. 36 - 17 itens de Infraestrutura: IaC, Docker, K8s, Windows Server AD, Observabilidade Prometheus/Grafana/ELK, Nuvem, SDN, Puppet/Ansible);
    * [`Polícia Federal 2018`](file:///home/Hugo/Documentos/iniciando/editais/edital_05_pf_2018_perito_ti.pdf) (Cebraspe, Pág. 53 - Arquitetura de computadores, RAID, TCP/IP, Wi-Fi 802.11/802.1x, Windows NTFS/registro, Linux serviços/logs, Nuvem);
    * [`SEFAZ-SC 2026`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) (FCC, Pág. 29 - Servidores, Virtualização, Containers, OSI e TCP/IP, Nuvem AWS/Azure/GCP, Docker, Kubernetes);
    * [`SEFAZ-MG 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_07_sefaz_mg_2022_auditor_ti.pdf) (FGV, Pág. 49 - Nuvem pública/privada IaaS/PaaS/SaaS, Serverless, DevOps, Automação Python, ITIL v4);
    * [`TCDF 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) (Cebraspe, Pág. 44 - DevOps, GitLab CI, Gitflow, Linux scripting, Observabilidade logs e métricas);
    * [`CGU 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_09_cgu_2022_auditor_ti.pdf) (FGV, Pág. 28 - Nuvem AWS/Azure/GCP, Docker, Kubernetes, DevOps, Terraform, Telefonia IP SIP/H323, Zabbix 5);
    * [`CVM 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) (FGV, Pág. 32-33 - Arquitetura de computadores, SOs escalonamento/memória, Redes TCP/IP, Nuvem AWS/Azure, Ansible, Windows Server AD FSMO/PowerShell, Linux RedHat/Ubuntu, NGINX/Apache).  
    *(Nota Técnica Documental: Apenas o edital do **TCU 2021 concentrou Conhecimentos Específicos em Dados e TI Governamental**, atenuando redes puras).*

* **Stack Tecnológico Oficial Mapeado:**
  * **Sistemas Operacionais & Servidores:** Linux (Ubuntu Server, RedHat Enterprise Linux - RHEL, Debian; Kernel, systemd, FHS, LVM, PAM, Bash Scripting), Microsoft Windows Server (Active Directory DS, Florestas, FSMO Roles, GPO, Kerberos, DNS, DHCP, PowerShell), Servidores Web (NGINX, Apache HTTP Server).
  * **Computação em Nuvem:** Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP); IaaS, PaaS, SaaS, FinOps, Serverless (AWS Lambda, Azure Functions).
  * **Contêineres e Orquestração:** Docker (Dockerfile, imagens multi-stage, volumes, redes), Kubernetes (Pods, Deployments, ReplicaSets, Services, Ingress, ConfigMaps, Secrets, PV/PVC, HPA, Helm).
  * **Infraestrutura como Código (IaC) & Automação:** Terraform (HCL, state, providers, modules), Ansible (Playbooks em YAML, roles, inventários, idempotência), Puppet.
  * **Observabilidade e Monitoramento:** Prometheus & Grafana (PromQL), Pilha ELK / EFK (Elasticsearch, Logstash, Kibana), OpenTelemetry, APM, Zabbix 5+, Nagios, Protocolo SNMP (v2c, v3).
  * **Redes e Comunicação:** Pilha TCP/IP, IPv4 (CIDR, VLSM), IPv6, Roteamento dinâmico (OSPF, BGP), Comutação (VLAN IEEE 802.1Q, STP, RSTP, VXLAN), SDN (OpenFlow), Protocolos L7 (HTTP/2, HTTP/3 QUIC, TLS 1.3, DNS, DHCP, SSH, LDAP, NFS, SMB/CIFS).

* **Ementa Granular Ponto a Ponto:**
  * **Arquitetura de Computadores e Teoria dos Sistemas Operacionais:**
    * Componentes fundamentais: UCP/CPU (Unidade de Controle, Unidade Lógica e Aritmética, Registradores), Barramentos (dados, endereço e controle), Memórias (Registradores, Cache L1/L2/L3 com coerência de cache MESI, Memória Principal RAM, Armazenamento Secundário);
    * Arquiteturas CISC vs RISC; Paralelismo em nível de instrução (*Pipelining* e riscos de pipeline: estruturais, de dados e de controle/desvio; execução superescalar e fora de ordem); Processadores multi-core;
    * Mecanismos de Entrada/Saída: E/S Programada, E/S Controlada por Interrupção e Acesso Direto à Memória (**DMA**);
    * Tecnologia de Armazenamento redundante (**RAID**): RAID 0 (striping sem tolerância a falhas), RAID 1 (espelhamento / mirroring), RAID 5 (striping com paridade distribuída, tolera falha de 1 disco), RAID 6 (dupla paridade, tolera falha de 2 discos), RAID 10 / 01 (arranjos combinados); Redes de Armazenamento: SAN (Storage Area Network com Fibre Channel e iSCSI), NAS (Network Attached Storage com NFS e SMB) e DAS (Direct Attached Storage);
    * Gerenciamento de Processadores e Threads: estados de um processo (Novo, Pronto, Executando, Bloqueado/Espera, Terminado); Bloco de Controle de Processo (**PCB**); Troca de contexto; Threads no espaço de usuário vs espaço de kernel;
    * Algoritmos de Escalonamento de CPU: Preemptivos vs Não-Preemptivos; First-Come First-Served (FCFS), Shortest Job First (SJF), Shortest Remaining Time First (SRTF), Round Robin (escalonamento circular com fatia de tempo / *quantum*), Escalonamento por Prioridades e Filas Multinível com realimentação;
    * Concorrência, Sincronização e Comunicação Interprocessos (IPC): Condição de Corrida (*Race Condition*), Seção Crítica; Primitivas de sincronização: Desativação de interrupções, Variáveis de travamento (*Locks*), Instruções atômicas (Test-and-Set, Compare-and-Swap), Semáforos (contadores e binários / Mutexes), Monitores e Troca de Mensagens;
    * Impasse (**Deadlock**): As 4 Condições de Coffman simultâneas: 1. Exclusão Mútua; 2. Posse e Espera (*Hold and Wait*); 3. Não-Preempção; 4. Espera Circular; Estratégias de tratamento: Prevenção (eliminação de uma das 4 condições), Evitação (Algoritmo do Banqueiro de Dijkstra), Detecção e Recuperação (grafos de alocação de recursos, abortamento de processos); Inanição (*Starvation*);
    * Gerenciamento de Memória: Alocação contígua simples, Particionamento estático e dinâmico; Algoritmos de alocação: First-Fit, Best-Fit, Worst-Fit; Fragmentação interna e externa (compactação); Paginação de memória (Páginas lógicas, Molduras/Frames físicos, Tabela de Páginas, Translation Lookaside Buffer - **TLB**); Segmentação de memória; Memória Virtual: paginação por demanda, falha de página (*Page Fault*); Algoritmos de substituição de páginas: Ótimo, FIFO, Segunda Chance / Relógio e **LRU (Least Recently Used)**; Anomalia de Bélády no FIFO; Hiperpaginação (*Thrashing*).
  * **Administração Avançada de Sistemas Operacionais (Linux e Windows Server):**
    * **Linux Avançado**:
      - Arquitetura do kernel Linux; File System Hierarchy Standard (**FHS**: `/`, `/bin`, `/sbin`, `/etc`, `/var`, `/proc`, `/sys`, `/dev`, `/home`, `/root`, `/tmp`, `/opt`);
      - Sistemas de arquivos nativos: Ext4 (superbloco, inodes, extents, journaling), XFS, Btrfs; Gerenciamento de Volumes Lógicos (**LVM**: Physical Volumes - `pvcreate`, Volume Groups - `vgcreate`/`vgextend`, Logical Volumes - `lvcreate`/`lvextend`, snapshots);
      - Inicialização e Gerenciamento de Serviços com **systemd**: comandos `systemctl` (start, stop, restart, reload, status, enable, disable, mask), unidades (.service, .target, .timer, .mount, .socket); Análise de logs estruturados com `journalctl` (filtros por unidade `-u`, prioridade `-p`, tempo `--since`/`--until`, seguimento em tempo real `-f`);
      - Permissões de Arquivos: modelo POSIX tradicional (dono, grupo, outros; permissões r, w, x; notação octal e simbólica; permissões especiais: SUID bit 4000, SGID bit 2000, Sticky Bit 1000 para diretórios compartilhados como `/tmp`); Listas de Controle de Acesso POSIX (**ACLs**: comandos `getfacl` e `setfacl` para permissões granulares por usuário/grupo);
      - Gerenciamento de Processos: comandos `ps aux`, `top`, `htop`, monitoramento de processos e threads; Envio de sinais POSIX (`kill`, `killall`: SIGHUP 1 para recarga, SIGINT 2 para interrupção Ctrl+C, SIGKILL 9 para término forçado incondicional, SIGTERM 15 para encerramento gracioso); Prioridades de escalonamento (`nice` de -20 maior prioridade a +19 menor prioridade, `renice`);
      - Gerenciamento de Memória e Rede: uso de swap, OOM Killer (*Out-of-Memory Killer*); comandos do pacote `iproute2`: `ip addr`, `ip route`, `ip link`, `ss` (substituto moderno do netstat: `ss -tulnp`), `ethtool`;
      - Segurança nativa: PAM (*Pluggable Authentication Modules* em `/etc/pam.d`), configuração de SSH seguro (`/etc/ssh/sshd_config`: desativação de login root direto, uso exclusivo de chaves públicas, alteração de porta); Firewall nativo com `iptables` (tabelas filter, nat, mangle; chains INPUT, OUTPUT, FORWARD) e `nftables`;
      - Shell Scripting avançado em **Bash**: variáveis, variáveis especiais (`$0`, `$#`, `$@`, `$?`), condicionais (`if`, `test` / `[[ ... ]]`), laços (`for`, `while`), funções, tratamento de argumentos com `getopts`, redirecionamentos de E/S (`>`, `>>`, `2>`, `&>`, `|`), manipulação de texto com expressões regulares em ferramentas de linha de comando: `grep`, `egrep`, `sed` (substituição em fluxo), `awk` (processamento colunar estruturado), `cut`, `sort`, `uniq`, `find`, `xargs`.
    * **Microsoft Windows Server**:
      - Arquitetura do Active Directory Domain Services (**AD DS**): componentes lógicos: Florestas, Árvores de Domínio, Domínios, Unidades Organizacionais (**OUs**), Relações de Confiança (*Trusts* transitivas e unidirecionais); componentes físicos: Sites de rede, Sub-redes e Controladores de Domínio (DCs);
      - Papéis **FSMO (Flexible Single Master Operation)**: Papéis a nível de Floresta: Schema Master e Domain Naming Master; Papéis a nível de Domínio: RID Master, PDC Emulator (emulador de PDC - sincronização de relógio, bloqueio de contas e GPOs) e Infrastructure Master;
      - Objetos de Diretório: Usuários, Computadores, Grupos (escopos: Global, Domínio Local e Universal; tipos: Segurança e Distribuição);
      - Políticas de Grupo (**GPO - Group Policy Objects**): ordem canônica de aplicação: Local → Site → Domínio → OU (**LSDOU**); precedência da última política aplicada; mecanismos de Bloqueio de Herança (*Block Inheritance*) e Aplicação Forçada (*Enforced*); Filtros de Segurança WMI;
      - Serviços de Rede Windows Server: **DNS** integrado ao AD (zonas integradas, replicação segura, registros A, AAAA, CNAME, MX, PTR, SRV essenciais para localização de controladores de domínio), **DHCP** (escopos, exclusões, reservas por MAC, opções de escopo: 003 Gateway, 006 DNS Server, failover de DHCP em modo Load Balance ou Hot Standby), Servidor RADIUS / NPS;
      - Protocolos de Autenticação: **Kerberos v5** (Centro de Distribuição de Chaves - KDC: Serviço de Autenticação AS e Serviço de Concessão de Bilhetes TGS; Bilhetes TGT e TGS; Nomes Principais de Serviço - SPNs) e NTLM v2;
      - Sistemas de arquivos Windows: **NTFS** (permissões NTFS de leitura, escrita, modificar, controle total; herança de permissões e permissões explícitas; regras de resolução de conflitos: negação explícita prevalece; cálculo de permissões efetivas; quotas de disco; criptografia EFS; Volume Shadow Copy - VSS para cópias de sombra) e ReFS (Resilient File System);
      - Compartilhamentos de arquivos: SMB/CIFS (permissões de compartilhamento combinadas com permissões NTFS: aplicação da regra mais restritiva);
      - Automação com **Windows PowerShell**: arquitetura baseada em objetos .NET; sintaxe verbo-substantivo (`Get-Service`, `Start-Process`, `Set-ADUser`); pipelines de objetos (`| Where-Object`, `| Select-Object`, `| ForEach-Object`); scripts `.ps1`; PowerShell Remoting via WinRM;
      - Serviços Web e de Diretório: NGINX (configuração de proxy reverso, balanceamento de carga, terminação SSL), Apache HTTP Server, OpenLDAP, NFS.
  * **Redes de Computadores e Protocolos de Comunicação:**
    * Arquiteturas de Rede: Modelo OSI da ISO (7 camadas) vs Pilha TCP/IP da IETF (4/5 camadas); Unidades de Dados de Protocolo (**PDUs**): Bits (Física), Quadros/Frames (Enlace), Pacotes/Datagramas (Rede), Segmentos (Transporte) e Dados (Aplicação); Encapsulamento e Desencapsulamento;
    * Camada de Rede (Internet):
      - Protocolo **IPv4**: cabeçalho de 20 a 60 bytes (campos IHL, Type of Service, Total Length, Identificação, Flags DF/MF, Fragment Offset, TTL - Time to Live para prevenção de loops, Protocolo L4, Header Checksum, IPs de Origem e Destino); Classes legadas A, B, C, D (Multicast) e E (Experimental); Blocos privados RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16); Endereçamento sem classe (**CIDR**); Cálculo de sub-redes com máscaras de tamanho fixo (**FLSM**) e variável (**VLSM**);
      - Protocolo **IPv6**: cabeçalho simplificado de tamanho fixo de 40 bytes (campos Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, IPs de Origem e Destino de 128 bits); Eliminação do checksum de cabeçalho e da fragmentação por roteadores intermediários (descoberta da MTU do caminho / PMTUD); Tipos de endereços: Unicast (Global Unicast 2000::/3, Link-Local fe80::/10 gerado por EUI-64 ou aleatório, Unique Local fc00::/7, Loopback ::1/128), Anycast e Multicast (ff00::/8); ausência de Broadcast no IPv6; Mecanismos de transição IPv4-IPv6: Pilha Dupla (*Dual-Stack*), Tunelamento (6to4, Teredo, ISATAP) e Tradução (NAT64 / DNS64);
      - Protocolo ICMP e ICMPv6 (mensagens de erro e controle: Echo Request/Reply para ping, Destination Unreachable, Time Exceeded para traceroute);
      - Tradução de Endereços de Rede (**NAT / PAT**): NAT estático (1:1), NAT dinâmico e Sobrecarga de Porta (**PAT - Port Address Translation** / NAT N:1).
    * Algoritmos e Protocolos de Roteamento Dinâmico:
      - Roteamento Estático vs Dinâmico; Métricas de roteamento e Distância Administrativa (confiabilidade da rota);
      - Algoritmos de Roteamento Interno (IGP): Vetor de Distância (Distance Vector - Bellman-Ford, problema da contagem até o infinito, técnicas de mitigação: Split Horizon e Poison Reverse) vs Estado do Link (Link-State - Algoritmo de Dijkstra para Caminho Mais Curto / SPF);
      - **OSPF (Open Shortest Path First)**: protocolo de estado do link; métrica baseada em Custo (Custo = Largura de Banda de Referência / Largura de Banda da Interface); Estrutura hierárquica em Áreas: Área Backbone (Área 0) mandatória; Tipos de roteadores: Roteador Interno, Roteador de Borda de Área (**ABR**), Roteador de Borda de Sistema Autônomo (**ASBR**); Tipos de pacotes OSPF: Hello (descoberta de vizinhos e eleição de DR/BDR em redes multiacesso), DBD (Database Description), LSR (Link State Request), LSU (Link State Update contendo LSAs), LSAck (Reconhecimento); Tipos de LSAs (LSA 1 Router, LSA 2 Network, LSA 3 Summary, LSA 4 e 5 External);
      - **BGP (Border Gateway Protocol v4 - RFC 4271)**: protocolo de roteamento entre Sistemas Autônomos (**EGP**); baseado em Vetor de Caminhos (*Path Vector*); sessões estabelecidas sobre conexão confiável **TCP na porta 179**; Tipos de sessões: BGP Externo (**eBGP** com TTL=1 padrão) e BGP Interno (**iBGP** em malha completa ou com Route Reflectors); Atributos de caminho (*Path Attributes*): Well-Known Mandatory (ORIGIN, AS_PATH - prevenção de loops interdomínio, NEXT_HOP), Well-Known Discretionary (LOCAL_PREF - preferência de saída do AS), Optional Non-Transitive (MED - Multi-Exit Discriminator para sugerir entrada a vizinhos) e atributo proprietário Cisco Weight; Algoritmo de seleção da melhor rota BGP.
    * Camada de Enlace e Comutação:
      - Ethernet IEEE 802.3: endereçamento MAC de 48 bits, quadro Ethernet II (Preâmbulo, SFD, MAC Destino, MAC Origem, EtherType, Dados/Payload, FCS/CRC-32); Mecanismo de acesso ao meio CSMA/CD histórico; Domínio de Colisão vs Domínio de Broadcast;
      - Redes Locais Virtuais (**VLAN - IEEE 802.1Q**): isolamento de tráfego na camada 2; marcação de quadros (*VLAN Tagging* de 4 bytes inserido após o MAC Origem com identificador VID de 12 bits permitindo até 4096 VLANs); Portas de Acesso (tráfego sem tag) vs Portas Trunk (tráfego com tag para múltiplos VIDs); Roteamento inter-VLAN (Router-on-a-Stick com subinterfaces ou Switches L3 com SVI - Switched Virtual Interface);
      - Protocolos de Prevenção de Loops de Camada 2: Spanning Tree Protocol (**STP - IEEE 802.1D**: eleição de Root Bridge pelo menor Bridge ID, determinação de portas Root, Designated e Blocking; estados de porta: Blocking, Listening, Learning, Forwarding; tempo de convergência de 30 a 50 segundos), Rapid STP (**RSTP - IEEE 802.1w**: convergência em milissegundos com sincronização proposta/acordo; papéis de porta Alternate e Backup; estados de porta Discarding, Learning, Forwarding) e Multiple STP (**MSTP - IEEE 802.1s**);
      - Agregação de Enlaces (Link Aggregation / LACP - IEEE 802.3ad / 802.1ax): agrupamento lógico de interfaces físicas para aumento de largura de banda e redundância;
      - Redes Virtuais de Datacenter: **VXLAN (Virtual Extensible LAN - RFC 7348)**: encapsulamento de quadros Ethernet L2 sobre pacotes IP/UDP L3 (porta UDP 4789); cabeçalho VXLAN de 8 bytes contendo o identificador de rede virtual **VNI de 24 bits**, permitindo até 16 milhões de redes virtuais isoladas sobre infraestruturas físicas de datacenter (*Overlay sobre Underlay*);
      - Redes Definidas por Software (**SDN**): desacoplamento físico entre o **Plano de Controle** (inteligência de roteamento, decisões de caminho centralizadas em controladores de software) e o **Plano de Dados / Encaminhamento** (hardware simples de comutação que apenas executa regras de fluxo); Protocolo **OpenFlow**; Interfaces de programação: APIs Northbound (comunicação entre o controlador e as aplicações de rede) e APIs Southbound (comunicação entre o controlador e os switches/roteadores físicos).
    * Camada de Transporte:
      - Protocolo **TCP**: confiável, orientado à conexão, bidirecional (*full-duplex*); Handshake de três vias (*Three-Way Handshake*: SYN → SYN-ACK → ACK) e finalização de conexão (FIN → ACK → FIN → ACK com estado TIME_WAIT); Controle de Fluxo por Janela Deslizante (*Sliding Window* orientada pelo receptor - Window Advertisement); Controle de Congestionamento orientado pela rede: fases Slow Start (crescimento exponencial da janela de congestionamento cwnd até o limiar ssthresh), Congestion Avoidance (crescimento linear aditivo), Fast Retransmit (disparado após o recebimento de 3 ACKs duplicados consecutivos sem aguardar o timeout) e Fast Recovery;
      - Protocolo **UDP**: não confiável, não orientado à conexão, sem controle de fluxo ou retransmissão; baixa sobrecarga de cabeçalho (8 bytes); utilizado para transmissões de tempo real (voz/vídeo), DNS e protocolos modernos;
      - Protocolo **QUIC (RFC 9000)**: protocolo de transporte executado sobre UDP desenvolvido para substituir o TCP na web; Handshake integrado com TLS 1.3 garantindo conexão criptografada com 1-RTT ou 0-RTT; Multiplexação de streams independentes sobre a mesma conexão, eliminando o bloqueio de início de linha (*Head-of-Line Blocking* do TCP); Migração de conexão resiliente a mudanças de IP (mobilidade Wi-Fi/4G) usando Connection IDs independentes do endereço IP do cliente.
    * Camada de Aplicação e Serviços de Conectividade:
      - Protocolos Web: **HTTP/1.1** (conexões persistentes keep-alive, pipelining limitado por HoL blocking no nível HTTP), **HTTP/2** (protocolo binário, multiplexação total de requisições sobre conexão única TCP, compressão de cabeçalho HPACK, server push), **HTTP/3** (baseado no QUIC sobre UDP); Protocolo seguro **HTTPS sobre TLS 1.3**;
      - **DNS (Domain Name System)**: arquitetura distribuída e hierárquica; servidores raiz (Root Servers), servidores de domínio de topo (TLD Servers), servidores autoritativos e servidores recursivos/resolutores; Tipos de consulta: recursiva vs iterativa; Tipos de registros DNS: `A` (IPv4), `AAAA` (IPv6), `CNAME` (nome canônico / alias), `MX` (servidor de e-mail), `TXT` (textos, SPF, DKIM), `PTR` (resolução reversa IP para nome), `NS` (servidor autoritativo), `SOA` (autoridade de zona, número de série, TTL), `SRV` (localização de serviços de rede); Segurança com **DNSSEC**: assinaturas digitais sobre registros DNS com chaves RRSIG, DNSKEY, DS para prevenir envenenamento de cache (*DNS Cache Poisoning*);
      - Protocolo **DHCP**: concessão automática de parâmetros IP; ciclo de 4 mensagens DORA: DHCP **Discover** (broadcast do cliente), DHCP **Offer** (unicast/broadcast do servidor com oferta de IP), DHCP **Request** (broadcast do cliente requisitando o IP ofertado) e DHCP **Acknowledge** (unicast do servidor confirmando a concessão / *lease*);
      - Protocolos de E-mail: SMTP (envio de mensagens na porta 25/587 com STARTTLS), IMAP (acesso sincronizado a caixas de correio na porta 143/993 com SSL) e POP3 (porta 110/995);
      - Protocolos de Acesso Remoto e Diretório: SSH (Porta 22, criptografia de canal seguro, autenticação por par de chaves RSA/Ed25519), Telnet (não criptografado, porta 23), LDAP (porta 389) e LDAPS (porta 636);
      - Protocolo **SNMP (Simple Network Management Protocol)**: monitoramento e gerência de dispositivos de rede; arquitetura Gerente (NMS) e Agentes; MIB (Management Information Base - árvore hierárquica) e OIDs (Object Identifiers); Operações: GetRequest, GetNextRequest, GetBulkRequest, SetRequest e **SNMP Trap** (notificação assíncrona do agente para a porta UDP 162); Versões: SNMP v1 e v2c (autenticação vulnerável por strings de comunidade em texto claro) vs **SNMP v3** (modelo USM com autenticação criptográfica HMAC-SHA e privacidade de dados com criptografia AES);
      - Redes Privadas Virtuais (**VPN**): VPN de Acesso Remoto vs VPN Site-to-Site; Protocolo **IPsec**: modo Transporte (apenas payload IP é encriptado) vs modo Túnel (todo o pacote IP original é encriptado e embutido em um novo cabeçalho IP externo); Cabeçalho **AH (Authentication Header)** para autenticação e integridade sem confidencialidade vs Cabeçalho **ESP (Encapsulating Security Payload)** para confidencialidade, autenticidade e integridade; Protocolo de troca de chaves **IKEv2** (fases 1 e 2); Protocolos modernos: OpenVPN (baseado em SSL/TLS) e **WireGuard** (executado no kernel Linux com criptografia moderna de ponta ChaCha20-Poly1305).
  * **Computação em Nuvem (Cloud Computing) e Arquitetura de Nuvem:**
    * Definição e Características Essenciais segundo o NIST (SP 800-145): 1. Autoatendimento sob demanda (*On-demand self-service*); 2. Amplo acesso à rede (*Broad network access*); 3. Pool de recursos compartilhado (*Resource pooling* com independência de localização); 4. Rápida elasticidade (*Rapid elasticity* - escalonamento horizontal automático para cima e para baixo); 5. Serviço mensurado (*Measured service* - pagamento por uso / *pay-per-use*);
    * Modelos de Serviço:
      - **IaaS (Infrastructure as a Service)**: fornecimento de infraestrutura computacional bruta (máquinas virtuais, armazenamento, redes, firewalls virtuais); o cliente é responsável por instalar, configurar e gerenciar o sistema operacional, middleware, runtime e aplicações (ex.: AWS EC2, Azure Virtual Machines, Google Compute Engine);
      - **PaaS (Platform as a Service)**: fornecimento de ambiente de desenvolvimento e execução gerenciado; o provedor gerencia hardware, sistema operacional, patches e runtime de linguagens; o cliente apenas faz o deploy do seu código e configura dados da aplicação (ex.: AWS Elastic Beanstalk, Azure App Service, Google App Engine);
      - **SaaS (Software as a Service)**: software completo fornecido como serviço pela internet acessível via navegador ou API; o cliente não gerencia nada da infraestrutura ou do software subjacente (ex.: Microsoft 365, Google Workspace, Salesforce);
      - Modelos derivados: **CaaS (Containers as a Service)** com clusters gerenciados (AWS EKS, Azure AKS, Google GKE) e **FaaS (Function as a Service / Serverless)** com execução de trechos de código sob demanda (AWS Lambda, Azure Functions, Cloud Functions);
    * Modelos de Implantação: Nuvem Pública (multilocatária, aberta ao público geral), Nuvem Privada (infraestrutura de uso exclusivo por uma única organização), Nuvem Comunitária (compartilhada por organizações com missões comuns) e **Nuvem Híbrida** (combinação de duas ou mais nuvens distintas integradas por tecnologia proprietária ou padronizada permitindo portabilidade de dados e aplicações / *Cloud Bursting*); Estratégias Multi-Cloud (evitação de dependência exclusiva de fornecedor / *vendor lock-in*);
    * **Modelo de Responsabilidade Compartilhada (Shared Responsibility Model)**:
      - O provedor é responsável pela "Segurança DA Nuvem" (*Security OF the Cloud*: infraestrutura física de datacenters, hardware de servidores, redes físicas, camada de virtualização);
      - O cliente é responsável pela "Segurança NA Nuvem" (*Security IN the Cloud*: dados do cliente, classificação de dados, identidades e controles de acesso IAM, sistemas operacionais e patches de VMs IaaS, configurações de firewall de rede virtual / Security Groups e configurações de criptografia em repouso e trânsito);
      - Variação das responsabilidades de acordo com o modelo de serviço contratado (em IaaS o cliente tem a máxima responsabilidade; em SaaS o cliente é responsável prioritariamente pela governança dos dados e acessos);
    * **Cloud FinOps (Financial Operations)**:
      - Governança financeira colaborativa e gestão de custos em nuvem;
      - Os 3 Estágios do Ciclo FinOps:
        1. *Informar*: visibilidade e alocação de custos por meio de marcação padronizada de tags corporativas, monitoramento de faturas e mapeamento de centros de custo;
        2. *Otimizar*: identificação e eliminação de desperdício computacional; redimensionamento de instâncias superdimensionadas (*Rightsizing*); aproveitamento de descontos por compromisso de longo prazo (Instâncias Reservadas / *Reserved Instances* e Planos de Economia / *Savings Plans*) e uso de instâncias preemptíveis / *Spot Instances* para cargas tolerantes a falhas;
        3. *Operar*: melhoria contínua, governança e alinhamento das decisões tecnológicas aos objetivos de negócios e métricas de eficiência;
    * Estratégias de Migração de Cargas de Trabalho para Nuvem (**Os 6 R's da Migração da AWS**):
      1. *Rehost* (Lift-and-Shift): migração direta das máquinas virtuais para a nuvem sem alterações na arquitetura ou código;
      2. *Replatform* (Lift-Tinker-and-Shift): ajustes pontuais na plataforma para obter benefícios rápidos sem alterar o core da aplicação (ex.: migrar de banco de dados em VM para banco de dados gerenciado como AWS RDS / Azure SQL Database);
      3. *Repurchase* (Drop-and-Shop): substituição do sistema legado sob medida por um produto comercial SaaS;
      4. *Refactor / Re-architect*: reescrita da arquitetura da aplicação para torná-la nativa da nuvem (*Cloud-Native*), adotando microsserviços, serverless e contêineres;
      5. *Retire*: desativação de sistemas e servidores legados que não possuem mais valor para o negócio;
      6. *Retain*: manutenção de sistemas críticos no ambiente on-premise local.
  * **Contêineres, Orquestração e Plataforma Kubernetes:**
    * Tecnologia de Contêineres vs Máquinas Virtuais: máquinas virtuais virtualizam o hardware físico via Hipervisor (Tipo 1 bare-metal vs Tipo 2 hosted), cada qual exigindo um sistema operacional convidado (*Guest OS*) completo; contêineres virtualizam o sistema operacional utilizando recursos de isolamento do kernel Linux (**Namespaces** para isolamento de PID, Mount, Network, IPC, UTS e User; **Cgroups - Control Groups** para limitação e mensuração de recursos de hardware como CPU, memória e I/O de disco);
    * **Docker**:
      - Arquitetura cliente-servidor: Docker CLI, Docker Daemon (`dockerd`), Docker Engine, Containerd e Runc (padrão Open Container Initiative - OCI);
      - Imagens de contêiner: camadas imutáveis (*Layers*) de somente leitura e sistema de arquivos de união (*Union File System*); camada de escrita de contêiner (*Copy-on-Write*);
      - Criação de imagens eficientes: boas práticas de **Dockerfile** (uso de imagens base mínimas Alpine/Distroless, redução de camadas, ordem de instruções para maximizar o cache do Docker, remoção de pacotes temporários na mesma instrução `RUN`, execução como usuário não-root com instrução `USER`); Construções em múltiplos estágios (**Multi-Stage Builds**: separação clara do ambiente de compilação/build do artefato de produção final);
      - Armazenamento no Docker: Volumes nomeados (*Volumes* gerenciados pelo Docker em `/var/lib/docker/volumes`), Montagens de ligação (*Bind Mounts* mapeando caminhos absolutos do host) e Montagens em memória (*tmpfs mounts*);
      - Redes no Docker: drivers nativos: `bridge` (rede padrão para comunicação entre contêineres no mesmo host via NAT), `host` (elimina isolamento de rede compartilhando o stack do host), `none` (desativa rede), `overlay` (comunicação multi-host para clusters Swarm/K8s) e `macvlan` (atribuição de endereço MAC físico aos contêineres);
      - Gerenciamento de aplicações multicontêiner com **Docker Compose** (`docker-compose.yml`: definição de serviços, redes, volumes, dependências `depends_on`, limites de recursos e variáveis de ambiente).
    * **Orquestração com Kubernetes (K8s)**:
      - Arquitetura do Cluster Kubernetes:
        * Nós do Plano de Controle (**Control Plane Nodes**): **kube-apiserver** (ponto focal de entrada, expõe a API REST do cluster e valida requisições), **etcd** (banco de dados chave-valor distribuído e altamente consistente que armazena todo o estado do cluster), **kube-scheduler** (seleciona o nó worker ótimo para execução dos novos Pods criados com base em recursos e restrições de afinidade/anti-afinidade), **kube-controller-manager** (executa controladores centrais: Node Controller, Deployment Controller, Job Controller) e **cloud-controller-manager**;
        * Nós de Execução de Cargas (**Worker Nodes**): **kubelet** (agente primário executado em cada nó que se comunica com o apiserver e garante que os contêineres descritos nos PodSpecs estejam em execução), **kube-proxy** (mantém as regras de rede no nó e implementa o balanceamento de conexões dos Services via iptables ou IPVS) e o **Container Runtime** (CRI: Containerd, CRI-O);
      - Objetos e Recursos Centrais do Kubernetes:
        * **Pods**: a menor unidade de execução computacional implantável no Kubernetes; representa um ou mais contêineres fortemente acoplados que compartilham o mesmo espaço de endereçamento de rede (localhost), namespace de IPC e volumes de armazenamento; Padrões de design de pods multicontêiner: *Sidecar* (contêiner auxiliar para logs/proxy), *Adapter* e *Ambassador*;
        * Controladores de Carga: **Deployments** (gerenciamento declarativo de Pods e ReplicaSets; suporte a estratégias de atualização: *RollingUpdate* com maxSurge e maxUnavailable, e *Recreate* com downtime); **ReplicaSets** (garantia de quantidade desejada de réplicas ativas); **StatefulSets** (gerenciamento de aplicações com estado que exigem identidades de rede estáveis e armazenamento persistente exclusivo); **DaemonSets** (garante uma cópia do Pod executando em todos ou em nós específicos selecionados, utilizado para agentes de log e monitoramento); **Jobs** e **CronJobs** (execução de tarefas em lote pontuais ou agendadas);
        * Serviços de Rede (**Services**): abstração que expõe uma aplicação em execução em um conjunto de Pods sob um IP virtual estável e balanceamento de carga interno via seletores de rótulos (*Label Selectors*); Tipos de Services:
          1. *ClusterIP*: padrão, expõe o serviço apenas em um IP interno acessível exclusivamente dentro do cluster;
          2. *NodePort*: expõe o serviço em uma porta estática (faixa 30000 a 32767) em cada nó do cluster;
          3. *LoadBalancer*: provisiona um balanceador de carga externo do provedor de nuvem que encaminha o tráfego para os nós;
          4. *ExternalName*: mapeia o serviço para um registro CNAME externo de DNS;
        * **Ingress**: objeto de roteamento que gerencia o acesso externo aos serviços do cluster (tráfego HTTP/HTTPS); fornece recursos de balanceamento de carga L7, roteamento baseado em caminhos e hosts (*Host-based / Path-based Routing*) e terminação SSL/TLS gerenciada; Operação conjunta com um Ingress Controller (ex.: NGINX Ingress Controller);
        * Armazenamento Persistente: **Volumes** (efêmeros, atrelados ao ciclo de vida do Pod); **PersistentVolumes (PV)** (recursos de armazenamento provisionados no cluster com ciclo de vida independente dos Pods); **PersistentVolumeClaims (PVC)** (requisição de armazenamento feita pelo usuário com especificação de tamanho e modos de acesso: ReadWriteOnce - RWO, ReadOnlyMany - ROX, ReadWriteMany - RWX); **StorageClasses** (provisionamento dinâmico de volumes de armazenamento em nuvem sob demanda);
        * Configuração e Segredos: **ConfigMaps** (armazenamento de dados de configuração não confidenciais em pares chave-valor injetados como variáveis de ambiente ou arquivos montados); **Secrets** (armazenamento de dados confidenciais codificados em Base64, protegidos por RBAC e encriptação em repouso no etcd);
        * Governança, Limites e Isolamento: **Namespaces** (divisão lógica do cluster); **ResourceQuotas** (limite rígido de consumo total de CPU, memória e quantidade de objetos por namespace); **LimitRanges** (definição de limites padrão mínimo e máximo de recursos por Pod);
        * Escalabilidade Automática: **Horizontal Pod Autoscaler (HPA)**: escala o número de réplicas de um Deployment com base na utilização observada de CPU, memória ou métricas customizadas; Cluster Autoscaler (escala o número de nós worker do cluster);
        * Gerenciador de Pacotes **Helm**: criação, versionamento, compartilhamento e publicação de pacotes de aplicações Kubernetes complexas por meio de **Charts** estruturados (arquivos `Chart.yaml`, `values.yaml` e diretório `templates/`).
  * **DevOps, DevSecOps, Pipelines CI/CD e Infraestrutura como Código (IaC):**
    * Conceitos fundamentais de DevOps e ciclo de entrega contínua;
    * Pipelines de Integração Contínua e Entrega Contínua (**CI/CD**): estágios automatizados de compilação, testes estáticos, testes de unidade, análise de segurança, geração de artefatos/imagens, homologação e implantação em produção;
    * Ferramentas e Implementação: **GitLab CI** (configuração declarativa em arquivo `.gitlab-ci.yml`, estágios *stages*, jobs, regras *rules*, artefatos e cache, execução em GitLab Runners) e **GitHub Actions** (workflows em `.github/workflows/*.yml`, eventos gatilho *on*, jobs, steps, actions reutilizáveis do marketplace, runners hospedados e auto-hospedados);
    * Estratégias de Gerenciamento de Ramificações (*Branching Strategies*): **Gitflow** (branches de longa duração: `main`/`master` para produção, `develop` para desenvolvimento, e branches temporárias `feature/*`, `release/*`, `hotfix/*`) vs **Trunk-Based Development** (desenvolvimento focado em um único branch tronco com branches de curta duração e uso obrigatório de Feature Flags);
    * Estratégias Modernas de Implantação e Liberação de Software:
      - **Blue/Green Deployment**: dois ambientes de produção idênticos (Blue em produção ativa e Green com a nova versão); transição instantânea de tráfego no roteador/balanceador após validação completa, garantindo rollback com zero downtime;
      - **Canary Release (Deploy Canário)**: liberação progressiva da nova versão para um pequeno subconjunto de usuários reais (ex.: 5%), monitoramento das métricas de erro e latência, e expansão gradual até 100% do tráfego;
      - **Deploy A/B**: liberação simultânea de duas versões para mensuração de impacto funcional e comportamento de negócio;
      - **Feature Flags / Feature Toggles**: técnica que permite ativar ou desativar funcionalidades em tempo de execução sem necessidade de novos deploys de código;
    * As 4 Métricas Chave do **DORA (DevOps Research and Assessment)**:
      1. *Deployment Frequency* (Frequência de Deploy): com que frequência a organização implementa código em produção;
      2. *Lead Time for Changes* (Tempo de Execução de Mudanças): tempo decorrido desde o commit do código até a sua entrada em produção;
      3. *Change Failure Rate* (Taxa de Falha em Mudanças): percentual de deploys que resultam em falhas que demandam correção imediata, patch ou rollback;
      4. *Time to Restore Service / MTTR* (Tempo Médio de Recuperação do Serviço): tempo necessário para restaurar a operação normal após um incidente em produção;
    * Práticas de **DevSecOps** (Shift-Left Security):
      - Integração contínua de segurança em todas as fases do pipeline CI/CD;
      - Análise Estática de Segurança de Código (**SAST** com SonarQube / Semgrep);
      - Verificação de Segredos e Credenciais em repositórios (detecção de chaves de API, senhas e certificados vazados com GitGuardian e Trufflehog);
      - Análise de Composição de Software (**SCA** com OWASP Dependency-Check e Snyk para inventário de dependências e vulnerabilidades CVEs);
      - Assinatura e integridade criptográfica de imagens de contêiner com **Sigstore / Cosign** antes do deploy em clusters Kubernetes;
    * **Infraestrutura como Código (IaC)** e Automação de Configuração:
      - Paradigmas: IaC Declarativo (descreve o estado final desejado; o software calcula o plano para alcançá-lo) vs Imperativo (descreve a sequência de passos/comandos operacionais);
      - Princípio da **Idempotência**: garantia de que a execução repetida do código sob as mesmas condições produzirá exatamente o mesmo resultado final sem efeitos colaterais imprevistos;
      - **Terraform (HashiCorp)**:
        * Sintaxe declarativa na linguagem HashiCorp Configuration Language (**HCL**);
        * Arquitetura de Providers (integração com AWS, Azure, GCP, Kubernetes);
        * Recursos fundamentais: blocos `provider`, `resource` (declaração de infraestrutura a provisionar), `data` (consulta de recursos já existentes), `variable` (variáveis de entrada), `output` (valores de retorno) e `locals`;
        * Gerenciamento de Estado (**State File - `terraform.tfstate`**): mapeamento do mundo real para a configuração declarada; Riscos de segurança e concorrência; Práticas de **Remote State** (armazenamento seguro do estado em bucket S3 criptografado com bloqueio de concorrência / *State Locking* via DynamoDB);
        * Ciclo de Comandos Operacionais: `terraform init` (inicialização de plugins e providers), `terraform validate`, `terraform plan` (geração e inspeção do plano de execução determinando criações, alterações e destruições), `terraform apply` (execução real do plano com garantia de idempotência) e `terraform destroy`;
        * Modularização de Infraestrutura: criação de módulos reutilizáveis e versionados;
      - **Ansible**:
        * Arquitetura **Agentless** (sem necessidade de instalação de agentes nos nós gerenciados; execução de tarefas remotas sobre SSH no Linux e WinRM no Windows);
        * Arquivos de Configuração e Automação: **Playbooks** escritos em formato YAML; **Tasks** compostas por módulos idempotentes nativos (ex.: `apt`, `yum`, `service`, `template`, `file`, `copy`, `user`);
        * **Inventários**: estáticos (arquivos INI ou YAML listando hosts e grupos) e dinâmicos (consultas a APIs de nuvem);
        * Organização com **Roles**: estruturação modular de playbooks em diretórios padronizados (`tasks/`, `handlers/`, `templates/` com Jinja2, `vars/`, `defaults/`, `meta/`);
      - Automação de Tarefas com Scripts Python: uso da biblioteca `requests` para interação com APIs REST de serviços de nuvem e ferramentas de automação.
  * **Observabilidade, Telemetria e Monitoramento de Sistemas:**
    * Monitoramento Tradicional (*Monitoring*) vs Observabilidade (*Observability*): o monitoramento informa se o sistema está funcionando; a observabilidade permite inferir os estados internos de um sistema distribuído a partir do exame de suas saídas externas sem necessidade de deploys de novo código;
    * **Os Três Pilares da Observabilidade**:
      1. **Métricas**: valores numéricos mensuráveis e agregáveis ao longo do tempo com carimbos temporais e tags de dimensão; ideal para detecção rápida de anomalias e geração de alertas operacionais;
      2. **Logs**: registros textuais estruturados e detalhados de eventos pontuais discretos ocorridos no sistema; ideal para análise de causa raiz de falhas e auditoria de segurança;
      3. **Traces (Rastreamento Distribuído)**: visualização da jornada completa de uma requisição de ponta a ponta enquanto ela atravessa múltiplos microsserviços; estrutura composta por um Trace ID único global e múltiplos **Spans** (unidades individuais de trabalho com carimbos de início/fim e metadados contextuais); Padrão aberto de instrumentação unificada **OpenTelemetry (OTel)** e ferramentas de visualização como Jaeger e Zipkin;
    * Ferramentas e Ecossistemas de Telemetria:
      - **Pilha ELK / EFK (Elasticsearch, Logstash/Fluentd, Kibana)**:
        * *Elasticsearch*: mecanismo de busca e análise textual distribuído; conceitos de cluster, nós (Master, Data, Ingest), shards primários e réplicas; índices e consultas ricas via Query DSL;
        * *Logstash*: pipeline centralizado de processamento de logs composto por estágios de entrada (*Inputs*), filtros de parsing e transformação estruturada (*Filters* com Grok patterns) e envio para destinos (*Outputs*);
        * *Kibana*: interface web visual para busca interativa em logs, criação de dashboards operacionais e monitoramento de alertas;
      - **Prometheus**:
        * Sistema de monitoramento e banco de dados de séries temporais (*TSDB*);
        * Modelo de coleta baseado em **Pull** (o servidor Prometheus faz varreduras periódicas buscando métricas em endpoints `/metrics` expostos pelas aplicações ou por Exporters como Node Exporter);
        * Os 4 Tipos de Métricas do Prometheus:
          1. *Counter*: métrica cumulativa monotônica que apenas cresce ou é zerada no reinício (ex.: total de requisições recebidas);
          2. *Gauge*: valor numérico instantâneo que pode subir e descer arbitrariamente (ex.: consumo atual de memória, temperatura da CPU);
          3. *Histogram*: amostragens de observações agrupadas em faixas configuráveis de valores (*buckets*), contagem total e soma (ex.: latência de requisições);
          4. *Summary*: similar ao histograma, mas calcula quantis configuráveis diretamente no lado da aplicação cliente;
        * Linguagem de Consulta **PromQL** (vetores instantâneos, vetores de faixa com operadores de intervalo temporal `[5m]`, funções de taxa de variação `rate()` e `irate()`, agregações espaciais `sum()`, `avg()` com agrupamento `by (...)`);
        * Gerenciamento e despacho de notificações com o **Alertmanager**;
      - **Grafana**:
        * Plataforma de visualização analítica interativa e composição de painéis (*Dashboards*); suporte a conexão simultânea a múltiplas fontes de dados heterogêneas (Prometheus, Elasticsearch, PostgreSQL, CloudWatch); criação de alertas visuais;
      - **Zabbix 5+**:
        * Arquitetura clássica de monitoramento corporativo: Zabbix Server, Zabbix Database, Zabbix Frontend Web, Zabbix Proxy (para monitoramento distribuído e coleta de métricas sem sobrecarregar o servidor central) e Zabbix Agent (agente leve instalado nos hosts monitorados);
        * Conceitos de Configuração: Hosts, Grupos de Hosts, Itens (métricas individuais coletadas via agente, SNMP, SSH ou checagens simples), Triggers (expressões lógicas que definem limites para geração de problemas), Ações e Notificações, Templates reutilizáveis;
  * **Protocolos Avançados de Rede, Telefonia IP e Redes Sem Fio:**
    * Gerenciamento de Redes com SNMP (v1, v2c e v3): Arquitetura Agente-Gerente, Base de Informações de Gerenciamento (MIB-II), SMI, identificadores OID, operações (Get, GetNext, GetBulk, Set, Trap, Inform) e segurança no SNMPv3 (modelos USM com autenticação HMAC-SHA/MD5 e privacidade AES/DES, e modelo VACM de controle de acesso);
    * Comutação de Rótulos Multiprotocolo (MPLS): Roteadores de Borda de Rótulo (LER), Roteadores de Comutação de Rótulo (LSR), pilha de rótulos (Label Stacking), caminhos LSP, Engenharia de Tráfego (MPLS-TE) e VPNs MPLS de Camada 2 (VPLS/VPWS) e Camada 3 (BGP/MPLS IP VPN - RFC 4364);
    * Extensões de Segurança do DNS (DNSSEC): Proteção criptográfica contra envenenamento de cache (DNS Cache Poisoning) e ataques Man-in-the-Middle, tipos de registros (DNSKEY, RRSIG, DS, NSEC e NSEC3) e validação da cadeia de confiança hierárquica (Root Trust Anchor);
    * Redes Sem Fio IEEE 802.11 (Wi-Fi): Padrões e evolução (802.11a/b/g/n/ac e 802.11ax / Wi-Fi 6/6E), método de acesso ao meio CSMA/CA com RTS/CTS, canais e frequências (2.4 GHz, 5 GHz e 6 GHz), mecanismos de segurança sem fio (WPA2-Personal/Enterprise, WPA3 com SAE - Simultaneous Authentication of Equals e autenticação 802.1X com EAP);
    * Telefonia IP e Voz sobre IP (VoIP): Protocolo de Inicialização de Sessão (SIP - RFC 3261: mensagens INVITE, ACK, BYE, CANCEL, códigos de resposta 1xx a 6xx), Protocolo de Descrição de Sessão (SDP), transporte em tempo real com RTP (Real-time Transport Protocol) e RTCP (RTP Control Protocol), e codecs de áudio (G.711, G.729);
    * Cabeamento Estruturado e Meios Físicos (Normas ABNT NBR 14565 e ANSI/TIA-568): Subsistemas de cabeamento estruturado (cabeamento horizontal, backbone de campus e edifício, sala de equipamentos, área de trabalho), categorias de cabos de par trançado UTP/STP (Cat 5e, Cat 6, Cat 6a até 10 Gbps), Fibras Ópticas Monomodo (SMF - núcleos de 9 µm para longas distâncias) vs Multimodo (MMF - núcleos de 50/62.5 µm: OM3, OM4), conectores ópticos (LC, SC) e tipos de polimento (PC, UPC, APC).

* **Checklist de Domínio Técnico Pré-Edital (Definição de Pronto):**
  - [ ] Sei calcular rapidamente sub-redes IPv4 em notação CIDR com máscaras VLSM (/27, /29, /30) determinando endereço de rede, primeiro/último IP utilizável e broadcast.
  - [ ] Explico com perfeição a diferença estrutural entre roteamento OSPF (estado do link, métrica custo, Área 0) e BGP v4 (vetor de caminhos, TCP 179, atributos AS-Path/Next-Hop).
  - [ ] Escrevo um Dockerfile otimizado de produção para uma aplicação Java ou Python com Multi-Stage Build, imagem base Distroless e execução como usuário não-root.
  - [ ] Consigo escrever um manifesto Kubernetes completo contendo um Deployment com 3 réplicas, limites de recursos (requests/limits), health checks (liveness/readiness probes) e Service ClusterIP.
  - [ ] Sei escrever um código Terraform básico para provisionar uma VPC, sub-rede e bucket com gerenciamento de estado remoto e lock no DynamoDB.
  - [ ] Domino as 4 métricas DORA e sei descrever em uma prova discursiva como implementá-las em um pipeline CI/CD GitLab/GitHub.
  - [ ] Consigo escrever consultas PromQL utilizando `rate()` e `sum() by (...)` para calcular a taxa de erros 5xx por segundo de um microsserviço.

---

### DISCIPLINA 10: Governança de TI, Gestão Ágil e Contratações Públicas de TIC
* **Incidência Comprovada nos 10 Editais Oficiais Locais:** **8/10 (80%)**
  * Cobrada com peso decisivo nos certames de controle, legislativo e fiscal:
    * [`Senado Federal 2022`](file:///home/Hugo/Documentos/iniciando/editais/edital_01_senado_2022_analista_ti.pdf) (FGV, Pág. 31-32 - Contratações de TI Lei 14.133, IN 94/2022, UST, Pontos de Função, COBIT, ITIL, PMBOK, BSC);
    * [`Câmara dos Deputados 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_02_camara_2023_analista_ti.pdf) (FGV, Pág. 30 - COBIT 2019, ITIL v4, PMBOK, Metodologias Ágeis, BPMN, ISO 31000);
    * [`BACEN 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_03_bacen_2024_analista_ti.pdf) (Cebraspe, Pág. 36 - Kanban, Scrum, Governança de Dados, ITIL v4);
    * [`TCU 2021`](file:///home/Hugo/Documentos/iniciando/editais/edital_04_tcu_2021_aufc_ti.pdf) (FGV, Pág. 26-28 - Governança pública, Contratações Lei 14.133, ETEC, Auditoria governamental);
    * [`Polícia Federal 2018`](file:///home/Hugo/Documentos/iniciando/editais/edital_05_pf_2018_perito_ti.pdf) (Cebraspe, Pág. 53 - COBIT, ITIL, PMBOK, Análise de Pontos de Função, Normas MPOG);
    * [`SEFAZ-SC 2026`](file:///home/Hugo/Documentos/iniciando/editais/edital_06_sefaz_sc_2026_auditor_ti.pdf) (FCC, Pág. 29 - Auditoria de Contratos de TI, Níveis de Serviço, Produtividade, Métricas de Software, Critérios de Aceite);
    * [`TCDF 2023`](file:///home/Hugo/Documentos/iniciando/editais/edital_08_tcdf_2023_auditor_ti.pdf) (Cebraspe, Pág. 44-45 - PETI, PDTI, PMBOK 7ª ed., ITIL v4, COBIT 2019, ISO 38500, Fiscalização de Contratos de TI Lei 14.133, IN 94/2022, UST, Pontos de Função);
    * [`CVM 2024`](file:///home/Hugo/Documentos/iniciando/editais/edital_10_cvm_2024_analista_inspetor_ti.pdf) (FGV, Pág. 32 - PDTI, Governança Digital, PMBOK 7ª ed., ITIL v4, Riscos de TIC).

* **Stack Tecnológico e Normativo Oficial Mapeado:**
  * **Frameworks de Governança:** COBIT 2019 (ISACA - 40 Objetivos de Governança e Gestão, 5 Domínios, 11 Fatores de Design, CMMI), ABNT NBR ISO/IEC 38500 (6 princípios).
  * **Gestão de Serviços:** ITIL 4 (SVS, Cadeia de Valor, 4 Dimensões, 7 Princípios, 34 Práticas).
  * **Gestão Estratégica e Projetos:** Balanced Scorecard (BSC), PETI, PDTI, Matriz SWOT, Matriz GUT, PMBOK 7ª Edição (12 princípios e 8 domínios de desempenho) e PMBOK 6ª Edição (Grupos de Processos e Áreas de Conhecimento).
  * **Gestão de Riscos:** COSO ERM 2017 (5 componentes e 20 princípios), ABNT NBR ISO 31000:2018.
  * **Contratações Públicas de TIC:** Nova Lei de Licitações e Contratos (Lei nº 14.133/2021), Instrução Normativa SGD/ME nº 94/2022, Instrução Normativa SEGES/ME nº 65/2021 (Pesquisa de Preços), Modelos de dimensionamento por UST (Unidade de Serviço Técnico) e APF (Pontos de Função com deflatores do TCU), Súmula 269/TCU e Acórdão 786/2006-Plenário (vedação de homem-hora).

* **Ementa Granular Ponto a Ponto:**
  * **Governança Corporativa de Tecnologia da Informação:**
    * Distinção Ontológica Fundamental entre Governança e Gestão de TI:
      - Governança de TI: responsabilidade da alta administração (Conselho de Administração / Alta Direção); estabelece diretrizes, avalia necessidades estratégicas dos stakeholders, direciona investimentos e monitora o desempenho e a conformidade;
      - Gestão de TI: responsabilidade da diretoria executiva e lideranças operacionais; planeja, constrói, executa e monitora as atividades diárias em estrito alinhamento com as diretrizes estabelecidas pela governança;
    * **Framework COBIT 2019 (ISACA)**:
      * Os 6 Princípios para um Sistema de Governança: 1. Fornecer valor aos stakeholders; 2. Abordagem holística; 3. Sistema de governança dinâmico; 4. Governança distinta da gestão; 5. Adaptado às necessidades da organização; 6. Sistema de governança de ponta a ponta;
      * Os 3 Princípios para um Framework de Governança: 1. Baseado em um modelo conceitual; 2. Aberto e flexível; 3. Alinhado aos principais padrões;
      * Os 7 Componentes de um Sistema de Governança: Processos; Estruturas Organizacionais; Princípios, Políticas e Frameworks; Informação; Cultura, Ética e Comportamento; Pessoas, Habilidades e Competências; Serviços, Infraestrutura e Aplicações;
      * Os 40 Objetivos de Governança e Gestão divididos nos 5 Domínios do COBIT 2019:
        1. **EDM (Evaluate, Direct and Monitor / Avaliar, Dirigir e Monitorar)** - Domínio exclusivo de Governança (5 objetivos): EDM01 Assegurar a Definição e Manutenção do Framework de Governança, EDM02 Assegurar a Entrega de Benefícios, EDM03 Assegurar a Otimização do Risco, EDM04 Assegurar a Otimização dos Recursos, EDM05 Assegurar o Engajamento dos Stakeholders;
        2. **APO (Align, Plan and Organize / Alinhar, Planejar e Organizar)** - Gestão (14 objetivos: APO01 a APO14 - gestão da estratégia, arquitetura corporativa, inovação, portfólio, orçamento, recursos humanos, relacionamentos, acordos de serviço, fornecedores, qualidade, riscos e segurança);
        3. **BAI (Build, Acquire and Implement / Construir, Adquirir e Implementar)** - Gestão (11 objetivos: BAI01 a BAI11 - gestão de programas, definição de requisitos, desenvolvimento/aquisição de software, disponibilidade, capacidade, mudanças, liberação e configuração);
        4. **DSS (Deliver, Service and Support / Entregar, Servir e Apoiar)** - Gestão (6 objetivos: DSS01 a DSS06 - gestão de operações, incidentes e requisições de serviço, problemas, continuidade, segurança e controles de processos de negócio);
        5. **MEA (Monitor, Evaluate and Assess / Monitorar, Avaliar e Medir)** - Gestão (4 objetivos: MEA01 Monitorar o Desempenho e a Conformidade, MEA02 Monitorar o Sistema de Controle Interno, MEA03 Monitorar a Conformidade com Requisitos Externos, MEA04 Monitorar a Garantia);
      * Os 11 Fatores de Design do COBIT 2019: Estratégia da organização, Metas organizacionais, Perfil de risco, Questões relacionadas a I&T, Cenário de ameaças, Requisitos de conformidade, Papel da TI, Modelo de fornecimento de TI, Métodos de implementação de TI, Estratégia de adoção de tecnologia e Tamanho da organização;
      * Gestão de Desempenho no COBIT 2019 (CPM): Modelo baseado nos Níveis de Capacidade de Processos do CMMI (Níveis 0 a 5: 0 Incompleto, 1 Inicial, 2 Gerenciado, 3 Definido, 4 Quantitativamente Gerenciado, 5 Em Otimização) e Níveis de Maturidade para Áreas de Foco.
    * **ABNT NBR ISO/IEC 38500:2018 / 2015**: Governança Corporativa de TI; Os 6 princípios: Responsabilidade, Estratégia, Aquisição, Desempenho, Conformidade e Comportamento Humano; Modelo de Governança baseado no ciclo EDM: Avaliar (*Evaluate*), Dirigir (*Direct*) e Monitorar (*Monitor*).
  * **Gerenciamento de Serviços de TI (ITIL 4):**
    * Conceito canônico de Serviço: meio para habilitar a cocriação de valor facilitando os resultados que os clientes desejam alcançar, sem que eles precisem gerenciar riscos e custos específicos;
    * O Sistema de Valor de Serviço (**SVS - Service Value System**): Componentes: Princípios Orientadores, Governança, Cadeia de Valor de Serviço, Práticas e Melhoria Contínua;
    * As 4 Dimensões do Gerenciamento de Serviços: 1. Organizações e Pessoas; 2. Informações e Tecnologia; 3. Parceiros e Fornecedores; 4. Fluxos de Valor e Processos;
    * Os 7 Princípios Orientadores (*Guiding Principles*):
      1. Foco no valor (*Focus on value*);
      2. Comece de onde você está (*Start where you are*);
      3. Progrida iterativamente com feedback (*Progress iteratively with feedback*);
      4. Colabore e promova visibilidade (*Collaborate and promote visibility*);
      5. Pense e trabalhe holisticamente (*Think and work holistically*);
      6. Mantenha simples e prático (*Keep it simple and practical*);
      7. Otimize e automatize (*Optimize and automate*);
    * A Cadeia de Valor de Serviço (**SVC - Service Value Chain**): Modelo operacional flexível com 6 atividades interconectadas: Planejar (*Plan*), Melhorar (*Improve*), Engajar (*Engage*), Desenho e Transição (*Design and Transition*), Obter/Construir (*Obtain/Build*) e Entregar e Suportar (*Deliver and Support*);
    * Práticas de Gerenciamento do ITIL 4 (34 práticas divididas em Gerais, de Serviços e Técnicas); Práticas mais cobradas em provas:
      - *Gerenciamento de Incidentes*: restaurar a operação normal do serviço o mais rápido possível; incidentes graves (*Major Incidents*) e procedimentos de emergência;
      - *Gerenciamento de Problemas*: reduzir a probabilidade e o impacto de incidentes identificando suas causas reais e potenciais e gerenciando soluções de contorno (*workarounds*) e erros conhecidos (*known errors*); As 3 fases: Identificação de problemas, Controle de problemas e Controle de erros;
      - *Habilitação de Mudanças (Change Enablement)*: maximizar o número de mudanças bem-sucedidas em serviços e produtos avaliando riscos e autorizando mudanças; Tipos de mudanças: Mudanças Padrão (*Standard* - pré-autorizadas, rotineiras, baixo risco), Normais (*Normal* - planejadas, avaliadas e autorizadas pela Autoridade de Mudança competente) e Emergenciais (*Emergency* - implementadas urgentemente para resolver incidentes graves, autorizadas pelo Comitê de Mudança de Emergência - ECAB);
      - *Gerenciamento de Liberação (Release Management)*: tornar serviços e recursos novos ou modificados disponíveis para uso;
      - *Gerenciamento de Configuração de Serviços*: manter registros precisos e confiáveis sobre a configuração dos serviços e seus Itens de Configuração (**IC / CI**);
      - *Central de Serviços (Service Desk)*: ponto único de contato (**SPOC**) entre o provedor de serviços e todos os usuários;
      - *Gerenciamento de Nível de Serviço*: negociar, definir e gerenciar metas de níveis de serviço baseadas no negócio através de Acordos de Nível de Serviço (**ANS / SLA**) e Acordos de Nível Operacional (**OLA**).
  * **Planejamento Estratégico de TI e Gestão de Riscos:**
    * O Ciclo do Planejamento Organizacional (**PDCA**: Plan, Do, Check, Act);
    * Análise de Ambiente Estratégico: Matriz **SWOT** (Forças, Fraquezas, Oportunidades e Ameaças), Matriz **GUT** (Gravidade, Urgência e Tendência para priorização de problemas com notas de 1 a 5, cálculo por produto: G × U × T) e Ferramenta 5W2H;
    * **Balanced Scorecard (BSC)**: Conceitos, mapa estratégico, objetivos estratégicos, metas, indicadores de desempenho (KPIs) e iniciativas; As 4 perspectivas clássicas: Financeira, Clientes/Sociedade, Processos Internos e Aprendizado e Crescimento;
    * Planejamento de TIC no Setor Público: Plano Estratégico de TIC (**PETI**) e Plano Diretor de TIC (**PDTI**); Alinhamento dos objetivos de TI aos objetivos institucionais do órgão; Indicadores de governança do TCU (iGovTI / iGG);
    * Gestão de Riscos Corporativos:
      - **COSO ERM 2017 (Enterprise Risk Management)**: Os 5 componentes integrados: 1. Governança e Cultura; 2. Estratégia e Definição de Objetivos; 3. Desempenho; 4. Revisão e Revisão; 5. Informação, Comunicação e Divulgação; Os 20 princípios do COSO ERM; Conceitos de Apetite a Risco, Tolerância a Risco e Capacidade de Risco;
      - **ABNT NBR ISO 31000:2018**: Princípios, Framework e Processo de Gestão de Riscos; Fases do processo: Escopo, contexto e critérios → Avaliação de riscos (Identificação, Análise e Avaliação) → Tratamento de riscos → Monitoramento e análise crítica → Comunicação e consulta.
  * **Gerenciamento de Projetos Tradicional e Ágil (PMBOK):**
    * **Guia PMBOK 7ª Edição (PMI)**:
      - Mudança paradigmática para entrega de valor baseada em princípios;
      - Os 12 Princípios de Entrega de Projetos: 1. Stewardship (Administração diligente e responsável); 2. Equipe de projeto colaborativa; 3. Engajamento eficaz das partes interessadas; 4. Foco no valor; 5. Pensamento sistêmico; 6. Liderança; 7. Adaptação baseada no contexto (*Tailoring*); 8. Incorporar qualidade nos processos e entregas; 9. Navegar na complexidade; 10. Otimizar as respostas aos riscos; 11. Adotar adaptabilidade e resiliência; 12. Habilitar a mudança para alcançar o estado futuro pretendido;
      - Os 8 Domínios de Desempenho do Projeto: Partes Interessadas (*Stakeholders*), Equipe (*Team*), Abordagem de Desenvolvimento e Ciclo de Vida (*Development Approach and Lifecycle*), Planejamento (*Planning*), Trabalho do Projeto (*Project Work*), Entrega (*Delivery*), Medição (*Measurement*) e Incerteza (*Uncertainty*);
      - Adaptação (*Tailoring*): processo de ajuste de governança, métodos e processos às necessidades específicas do projeto;
    * Legado do PMBOK 6ª Edição: Os 5 Grupos de Processos (Iniciação, Planejamento, Execução, Monitoramento e Controle, Encerramento) e as 10 Áreas de Conhecimento (Integração, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações, Riscos, Aquisições e Partes Interessadas); Gerenciamento do Valor Agregado (**EVM**): Valor Planejado (PV), Valor Agregado (EV), Custo Real (AC), Variação de Custos (CV = EV - AC), Variação de Prazos (SV = EV - PV), Índice de Desempenho de Custos (CPI = EV / AC) e Índice de Desempenho de Prazos (SPI = EV / PV).
  * **Contratações Públicas de Soluções de TIC e Fiscalização de Contratos:**
    * **Nova Lei de Licitações e Contratos Administrativos (Lei nº 14.133/2021 aplicada a TIC)**:
      - Princípios fundamentais: planejamento, segregação de funções, transparência, eficácia, economicidade e desenvolvimento nacional sustentável;
      - Instrumentos de Planejamento Obrigatórios: Plano de Contratações Anual (**PCA**), Estudo Técnico Preliminar (**ETP** - requisitos obrigatórios: descrição da necessidade, estimativa de quantidades, estimativa de valor, justificativa da escolha da solução e declaração de viabilidade), Termo de Referência (**TR**) e Matriz de Riscos da Contratação;
      - Modalidades Licitatórias aplicáveis a TIC: **Pregão** (obrigatório para aquisição de bens e serviços comuns de TIC com padrões de mercado estabelecidos) e **Diálogo Competitivo** (para soluções complexas de inovação tecnológica em que a Administração não possui capacidade técnica para definir previamente a especificação);
      - Pesquisa de Preços regulamentada pela **IN SEGES/ME nº 65/2021**: critérios de preferência de fontes (Painel de Preços, contratações similares na APF, mídia especializada, contratações de outros entes, cotações com fornecedores); metodologia de cálculo e expurgo de outliers estatísticos;
      - Contratação Direta de TIC: Dispensa de Licitação (art. 75) e Inexigibilidade de Licitação (art. 74 - fornecedor exclusivo comprovado, serviços técnicos de notória especialização de natureza predominantemente intelectual);
      - Encomenda Tecnológica (**ETEC** - Lei nº 10.973/2004 alterada pela Lei nº 13.243/2016 e regulamentada pelo Decreto nº 9.283/2018): contratação direta de pesquisa e desenvolvimento voltada a soluções de alto risco tecnológico (TCU 2021).
    * **Instrução Normativa SGD/ME nº 94/2022** (Rito Específico de Contratações de TIC na Administração Pública Federal):
      - Campo de aplicação: órgãos integrantes do Sistema de Administração dos Recursos de Tecnologia da Informação (**SISP**);
      - As 3 Fases do Processo de Contratação de Soluções de TIC:
        1. **Fase de Planejamento da Contratação**:
           - Iniciação da demanda com o Documento de Oficialização da Demanda (**DOD**);
           - Designação formal da **Equipe de Planejamento da Contratação**: Integrante Requisitante (representante da área demandante), Integrante Técnico (representante da área de TIC) e Integrante Administrativo (representante da área de licitações);
           - Elaboração do Estudo Técnico Preliminar da Contratação de TIC (**ETP-TIC**);
           - Elaboração do Plano de Sustentação de TIC;
           - Elaboração da Análise de Riscos (Mapa de Riscos);
           - Elaboração do Termo de Referência ou Projeto Básico de TIC (**TR-TIC / PB-TIC**);
        2. **Fase de Seleção do Fornecedor**:
           - Condução da licitação ou procedimento de contratação direta;
           - Análise técnica de aceitabilidade da proposta;
           - Realização de Prova de Conceito (**PoC - Proof of Concept**) quando expressamente prevista no edital para demonstrar a aderência aos requisitos técnicos;
        3. **Fase de Gestão do Contrato**:
           - Reunião inicial de alinhamento com a empresa contratada;
           - Monitoramento e fiscalização da execução contratual;
           - Recebimento provisório e definitivo dos serviços/bens de TIC;
           - Liquidação e autorização de pagamento.
      - Atores e Papéis na Fiscalização de Contratos de TIC:
        * **Gestor do Contrato**: servidor responsável pela coordenação geral administrativa e acompanhamento financeiro;
        * **Fiscal Requisitante**: servidor da área demandante responsável por atestar a conformidade das regras de negócio e funcionalidade dos entregáveis;
        * **Fiscal Técnico**: servidor da área de TIC responsável por avaliar a qualidade técnica, aderência aos padrões arquiteturais e conformidade dos serviços prestados;
        * **Fiscal Administrativo**: servidor responsável por fiscalizar as obrigações previdenciárias, fiscais e trabalhistas da contratada;
        * **Fiscal Setorial**: quando houver prestação desconcentrada em localidades distintas;
        * **Preposto da Contratada**: representante formal e exclusivo designado pela empresa contratada para receber demandas e responder perante a Administração.
    * **Modelos de Remuneração e Dimensionamento em Serviços de TIC**:
      - **Vedação Expressa do Pagamento Exclusivo por Homem-Hora**: Jurisprudência consolidada do TCU (**Súmula nº 269/TCU** e **Acórdão nº 786/2006-Plenário**): é vedada a contratação e o pagamento de serviços de TIC remunerados unicamente por horas trabalhadas ou postos de trabalho presenciais sem atrelamento a produtos, entregáveis mensuráveis ou níveis de serviço pactuados;
      - **Unidade de Serviço Técnico (UST)**: modelo de remuneração baseado em catálogo formal de serviços de TIC, onde cada atividade recebe uma valoração pré-fixada em unidades de esforço mensuráveis e auditáveis;
      - **Métricas de Software (Pontos de Função - IFPUG / NESMA)**: dimensionamento do escopo de desenvolvimento e manutenção de sistemas; aplicação compulsória dos **Deflatores de Pontos de Função** recomendados pelo TCU e pelos Guias do SISP (deflatores para atividades de baixa complexidade, manutenções adaptativas e reaproveitamento de componentes);
      - Acordos de Nível de Serviço (**ANS / SLA**) e Níveis Mínimos de Serviço (**NMS**): definição de indicadores objetivos de desempenho (disponibilidade de infraestrutura, tempo de resposta a chamados de incidentes, tempo de correção de defeitos em homologação e produção);
      - Aplicação de **Glosas Contratuais**: descontos automáticos na fatura em virtude do não atingimento dos níveis mínimos de serviço pactuados;
      - Sanções Administrativas da Lei nº 14.133/2021: Advertência, Multa compensatória/moratória, Impedimento de licitar e contratar (até 3 anos no ente federativo) e Declaração de Inidoneidade para licitar ou contratar (de 3 a 6 anos na Administração Pública de todos os entes federativos).
    * **Jurisprudência Paradigmática do TCU em Licitações de TIC**:
      - Vedações expressas: indicação de marcas comerciais em editais de TIC sem padronização prévia formalmente justificada; exigência indevida de certificações técnicas de fabricantes na fase de habilitação que restrinjam a competitividade do certame; falta de parcelamento do objeto (Súmula nº 247/TCU) quando técnica e economicamente viável; ausência de critérios objetivos de mensuração de serviços.
  * **Marco Legal do Governo Digital, Inovação e Legislação Estratégica de TIC:**
    * **Lei do Governo Digital (Lei nº 14.129/2021)**: Princípios, diretrizes, digitalização compulsória de processos e serviços públicos, Plataforma Única Gov.br, interoperabilidade de bases de dados do setor público, autosserviço cidadão, transparência e abertura de dados públicos;
    * **Estratégia Nacional de Governo Digital e Decretos Regulamentadores (Decreto nº 10.332/2020 e atualizações)**: Metas de transformação digital dos órgãos federais, identidade digital segura, catálogo unificado de serviços públicos e interoperabilidade governamental;
    * **Marco Legal das Startups e Empreendedorismo Inovador (Lei Complementar nº 182/2021)**: Contrato Público de Solução Inovadora (CPSI) para teste de soluções tecnológicas desenvolvidas por startups, critérios diferenciados de julgamento, dispensa de licitação e limites de remuneração;
    * **Marco Civil da Internet (Lei nº 12.965/2014) e Governança de Dados**: Princípios e garantias, neutralidade de rede, prazos obrigatórios de guarda de registros de conexão (1 ano) e de registros de acesso a aplicações (6 meses), responsabilidade civil por danos decorrentes de conteúdo de terceiros e procedimentos judiciais de requisição de dados.

* **Checklist de Domínio Técnico Pré-Edital (Definição de Pronto):**
  - [ ] Sei recitar de memória os 5 domínios do COBIT 2019 e categorizar os 40 objetivos em Governança (EDM) e Gestão (APO, BAI, DSS, MEA).
  - [ ] Consigo explicar os 7 princípios orientadores e as 4 dimensões do ITIL 4 em uma questão discursiva formal.
  - [ ] Distingo no ITIL 4 a prática de Gerenciamento de Incidentes do Gerenciamento de Problemas e detalho os 3 tipos de mudanças na Habilitação de Mudanças.
  - [ ] Domino a diferença entre a abordagem por princípios do PMBOK 7ª Edição (12 princípios e 8 domínios) e a abordagem por processos do PMBOK 6ª Edição.
  - [ ] Conheço as 3 fases de contratação de TIC da IN SGD/ME nº 94/2022 e as atribuições da Equipe de Planejamento e da Equipe de Fiscalização.
  - [ ] Sei fundamentar a Súmula 269/TCU contra pagamento por homem-hora puro e explicar a mecânica de remuneração por UST e Pontos de Função com deflatores.
  - [ ] Sei descrever as 4 perspectivas do BSC aplicadas ao setor público e a mecânica de cálculo da matriz GUT.
  - [ ] Sei apontar as diretrizes da Lei do Governo Digital (Lei nº 14.129/2021), os prazos de guarda de registros do Marco Civil da Internet (Lei nº 12.965/2014) e as regras do CPSI (LC nº 182/2021).
"""

print("Módulo de Infra, Segurança e Governança compilado com sucesso.")
