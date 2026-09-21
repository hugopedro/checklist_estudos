#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Oficial de Download, Validação e Auditoria de Editais de Elite (TI, Dados e Controle)
Workspace: file:///home/Hugo/Documentos/iniciando/editais/
"""

import os
import sys
import hashlib
import urllib.request
import argparse
import pypdf

BASE_DIR = "/home/Hugo/Documentos/iniciando/editais"

EDITAIS = [
    {
        "id": "01",
        "filename": "edital_01_senado_2022_analista_ti.pdf",
        "orgao": "Senado Federal",
        "edital": "Edital nº 1/2022 (Retificado)",
        "banca": "FGV",
        "cargo": "Analista Legislativo - Informática Legislativa (Análise de Sistemas / Suporte)",
        "pages": 44,
        "sha256": "ba68118ab46ba9db2984776909a7b39a9db522e2126d10e70b1a7796cd223876",
        "url": "https://conhecimento.fgv.br/sites/default/files/concursos/senado_analista_edital_retificado_002_01.09.2022_-_edital_1.pdf",
        "key_terms": ["Informática Legislativa", "Banco de Dados", "Processos de software"]
    },
    {
        "id": "02",
        "filename": "edital_02_camara_2023_analista_ti.pdf",
        "orgao": "Câmara dos Deputados",
        "edital": "Edital nº 1/2023 (Retificado)",
        "banca": "FGV",
        "cargo": "Analista Legislativo - Informática Legislativa",
        "pages": 35,
        "sha256": "b7a040629b1153da4a1b83f92accf2b4ebc90243b6ace4dab82df99539b2ff64",
        "url": "https://conhecimento.fgv.br/sites/default/files/concursos/cdep-edital-1-1a-retificacao-contador-informatica-legislativa-e-tecnico-em-material-e-patrimonio-final-1.pdf",
        "key_terms": ["Informática Legislativa", "Python", "DevOps"]
    },
    {
        "id": "03",
        "filename": "edital_03_bacen_2024_analista_ti.pdf",
        "orgao": "Banco Central do Brasil (BACEN)",
        "edital": "Edital nº 1/2024 (Atualizado com Retificação 4)",
        "banca": "Cebraspe",
        "cargo": "Analista - Área 2: Tecnologia da Informação",
        "pages": 43,
        "sha256": "cf4fff8a2d16ffeaf44864a21b3bb7a5d8d2f30ff484960ddddca54b4eced9eb",
        "url": "https://cdn.cebraspe.org.br/concursos/BCB_24/arquivos/ED_1_BCB_23_ABERTURA_ATUALIZADO_RET_4.PDF",
        "key_terms": ["TECNOLOGIA DA INFORMAÇÃO", "Segurança da Informação", "Ciência de Dados"]
    },
    {
        "id": "04",
        "filename": "edital_04_tcu_2021_aufc_ti.pdf",
        "orgao": "Tribunal de Contas da União (TCU)",
        "edital": "Edital nº 1/2021",
        "banca": "FGV",
        "cargo": "Auditor Federal de Controle Externo (AUFC) - Trilha com Análise de Dados",
        "pages": 34,
        "sha256": "85ccdc5612830e5276560b966ce10ed537dafa9b466fea3b78abe854bf7cae1d",
        "url": "https://conhecimento.fgv.br/sites/default/files/concursos/28.10.2021-edital-001-2021-abertura-concurso-tcu-.pdf",
        "key_terms": ["Auditor Federal de Controle Externo", "ANÁLISE DE DADOS", "Linguagem Python"]
    },
    {
        "id": "05",
        "filename": "edital_05_pf_2018_perito_ti.pdf",
        "orgao": "Polícia Federal (PF)",
        "edital": "Edital nº 1/2018 DGP/PF",
        "banca": "Cebraspe",
        "cargo": "Perito Criminal Federal - Área 3 (Informática Forense)",
        "pages": 88,
        "sha256": "0f48d599e40af21415d66418647373c6f1eb4cc5f5f053fccf3d3b39597ad60a",
        "url": "https://cdn.cebraspe.org.br/concursos/PF_18/arquivos/ED_1_DPF_2018___ABT.PDF",
        "key_terms": ["Perito Criminal Federal", "ÁREA 3", "INFORMÁTICA", "Forense"]
    },
    {
        "id": "06",
        "filename": "edital_06_sefaz_sc_2026_auditor_ti.pdf",
        "orgao": "SEFAZ-SC",
        "edital": "Edital nº 01/2026 (DOE-SC com OCR textual pesquisável)",
        "banca": "FCC",
        "cargo": "Auditor Estadual de Finanças Públicas - Ciências da Computação",
        "pages": 33,
        "sha256": "8ccf8d58a0cc2ebff306b4ccb8adc3c9310ba7caca745f78b778e0ceb0cf8188",
        "url": "https://dhg1h5j42swfq.cloudfront.net/2026/09/01180603/edital-sefaz-sc-2026.pdf",
        "key_terms": ["Auditor Estadual de Finanças Públicas", "CIÊNCIAS DA COMPUTAÇÃO", "Inteligência Artificial"]
    },
    {
        "id": "07",
        "filename": "edital_07_sefaz_mg_2022_auditor_ti.pdf",
        "orgao": "SEFAZ-MG",
        "edital": "Edital nº 01/2022 (Retificado)",
        "banca": "FGV",
        "cargo": "Auditor Fiscal da Receita Estadual (AFRE) - Especialidade TI",
        "pages": 50,
        "sha256": "25e500db405ef66665ca46495039abf12f6a69bfe46fdfdf68ed4f8ece2512ba",
        "url": "https://conhecimento.fgv.br/sites/default/files/concursos/edital-1-retificado-em-16.02.2023-assinado.pdf",
        "key_terms": ["Auditor Fiscal", "Tecnologia da Informação", "Banco de Dados"]
    },
    {
        "id": "08",
        "filename": "edital_08_tcdf_2023_auditor_ti.pdf",
        "orgao": "Tribunal de Contas do DF (TCDF)",
        "edital": "Edital nº 1/2023 (Compilado até retificação 5)",
        "banca": "Cebraspe",
        "cargo": "Auditor de Controle Externo - Especialidade TI (Sistemas)",
        "pages": 58,
        "sha256": "16b9b73b6e9c74964633cad6748311b149e8416163f465357acf77dd969121d5",
        "url": "https://cdn.cebraspe.org.br/concursos/TC_DF_23/arquivos/ED_1_2023_TCDF_ABERTURA_VERSAO_COMPILADA_AT_RET_ED_5.PDF",
        "key_terms": ["Auditor de Controle Externo", "Tecnologia da Informação", "Engenharia de Requisitos"]
    },
    {
        "id": "09",
        "filename": "edital_09_cgu_2022_auditor_ti.pdf",
        "orgao": "Controladoria-Geral da União (CGU)",
        "edital": "Edital nº 1/2021",
        "banca": "FGV",
        "cargo": "Auditor Federal de Finanças e Controle (AFFC) - TI",
        "pages": 37,
        "sha256": "493ef0cbeb59226225ae321c1b31cc5f070daac7b43294278dfae1da0c553ca2",
        "url": "https://conhecimento.fgv.br/sites/default/files/concursos/0_-_edital_de_concurso_cgu_001-2021.pdf",
        "key_terms": ["Tecnologia da Informação", "Finanças e Controle", "Ciência de Dados"]
    },
    {
        "id": "10",
        "filename": "edital_10_cvm_2024_analista_inspetor_ti.pdf",
        "orgao": "Comissão de Valores Mobiliários (CVM)",
        "edital": "Edital nº 1/2024 (Retificado)",
        "banca": "FGV",
        "cargo": "Analista e Inspetor - TI, Infraestrutura, Sistemas e Ciência de Dados",
        "pages": 39,
        "sha256": "dfbf12703a2c1ee0c7f046c49f40f2d9fff6bba15679a3c3149c87ca105f8e2d",
        "url": "https://conhecimento.fgv.br/sites/default/files/concursos/edital-1-2024-abertura-concurso-cvm-retificado-07.03.pdf",
        "key_terms": ["Tecnologia da Informação", "Ciência de Dados", "CVM"]
    }
]

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def download_file(url, dest_path):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp, open(dest_path, "wb") as f:
        while chunk := resp.read(65536):
            f.write(chunk)

def validate_all(verbose=True):
    print("================================================================================")
    print("Auditoria e Validação de Integridade dos Editais de Elite")
    print(f"Diretório: file://{BASE_DIR}")
    print("================================================================================")

    all_ok = True
    total_pages = 0
    total_size = 0

    for item in EDITAIS:
        filepath = os.path.join(BASE_DIR, item["filename"])
        file_url = f"file://{filepath}"
        print(f"\n[{item['id']}] {item['orgao']} - {item['cargo']}")
        print(f"    Arquivo: {file_url}")

        if not os.path.exists(filepath):
            print("    [ERRO] Arquivo ausente no disco!")
            all_ok = False
            continue

        size = os.path.getsize(filepath)
        total_size += size
        sha256 = compute_sha256(filepath)

        # Checagem de hash
        if sha256.lower() == item["sha256"].lower():
            print(f"    [OK] SHA256: {sha256}")
        else:
            print(f"    [AVISO] SHA256 divergente:")
            print(f"            Obtido:   {sha256}")
            print(f"            Esperado: {item['sha256']}")
            all_ok = False

        # Checagem estrutural do PDF
        try:
            reader = pypdf.PdfReader(filepath)
            num_pages = len(reader.pages)
            total_pages += num_pages
            if num_pages == item["pages"]:
                print(f"    [OK] Páginas: {num_pages} págs (compatível com o esperado)")
            else:
                print(f"    [AVISO] Páginas: {num_pages} (esperado {item['pages']})")
                all_ok = False

            # Validação textual e busca de termos-chave
            full_text = " ".join((page.extract_text() or "") for page in reader.pages)
            text_len = len(full_text)
            print(f"    [OK] Camada de texto: {text_len:,} caracteres extraídos")

            missing_terms = [t for t in item["key_terms"] if t.lower() not in full_text.lower()]
            if not missing_terms:
                print(f"    [OK] Todos os termos-chave validados: {', '.join(item['key_terms'])}")
            else:
                print(f"    [AVISO] Termos não localizados: {missing_terms}")
                all_ok = False

        except Exception as e:
            print(f"    [ERRO] Falha ao analisar estrutura do PDF: {e}")
            all_ok = False

    print("\n--------------------------------------------------------------------------------")
    print(f"Total de editais: {len(EDITAIS)} | Páginas totais: {total_pages} | Tamanho total: {total_size / (1024*1024):.2f} MB")
    if all_ok:
        print("[SUCESSO] Todos os 10 editais estão íntegros, autênticos e 100% pesquisáveis por texto!")
    else:
        print("[ALERTA] Foram encontradas divergências nas verificações acima.")
    print("--------------------------------------------------------------------------------\n")
    return all_ok

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Editais de Concursos de Elite")
    parser.add_argument("--download-missing", action="store_true", help="Baixa editais ausentes")
    parser.add_argument("--force-redownload", action="store_true", help="Força re-download de todos")
    parser.add_argument("--validate", action="store_true", default=True, help="Executa validação completa")
    args = parser.parse_args()

    if args.download_missing or args.force_redownload:
        for item in EDITAIS:
            filepath = os.path.join(BASE_DIR, item["filename"])
            if args.force_redownload or not os.path.exists(filepath):
                print(f"Baixando {item['filename']} de {item['url']}...")
                download_file(item["url"], filepath)
                print("Download concluído.")

    success = validate_all()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
