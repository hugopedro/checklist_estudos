#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de sincronização do progresso dos estudos com o repositório Git / GitHub Pages.
Permite salvar, importar e publicar o progresso para que qualquer navegador ou aba anônima
carregue exatamente os tópicos concluídos.
"""

import json
import os
import sys
import argparse
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(BASE_DIR, "progresso.json")
CHECKLIST_DATA_FILE = os.path.join(BASE_DIR, "data_checklist.json")

def carregar_dados_checklist():
    if not os.path.exists(CHECKLIST_DATA_FILE):
        return []
    with open(CHECKLIST_DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    items = []
    for d in data.get("disciplines", []):
        for g in d.get("groups", []):
            for it in g.get("items", []):
                items.append(it["id"])
        for chk in d.get("checklists", []):
            items.append(chk["id"])
    for s in data.get("semesters", []):
        for m in s.get("months", []):
            items.append(m["id"])
    for dis in data.get("discursivas", []):
        items.append(dis["id"])
    return items

def ler_progresso():
    if not os.path.exists(PROGRESS_FILE):
        return {"updated_at": "", "completed_count": 0, "completed": []}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_progresso(completed_set):
    all_ids = set(carregar_dados_checklist())
    valid_completed = sorted(list(completed_set.intersection(all_ids))) if all_ids else sorted(list(completed_set))
    data = {
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "version": "1.0",
        "total_items": len(all_ids) if all_ids else 698,
        "completed_count": len(valid_completed),
        "completed": valid_completed
    }
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Progresso salvo em {PROGRESS_FILE}: {len(valid_completed)} itens concluídos.")
    return data

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Sincronização de Progresso")
    parser.add_argument("--status", action="store_true", help="Exibir resumo do progresso atual")
    parser.add_argument("--import-json", type=str, help="Importar arquivo JSON de progresso exportado pelo dashboard")
    parser.add_argument("--mark", nargs="+", help="Marcar IDs de tópicos como concluídos")
    parser.add_argument("--unmark", nargs="+", help="Desmarcar IDs de tópicos")
    parser.add_argument("--commit-push", action="store_true", help="Comitar progresso.json e enviar ao GitHub para atualizar o GitHub Pages")
    args = parser.parse_args()

    prog = ler_progresso()
    completed_set = set(prog.get("completed", []))

    if args.import_json:
        if not os.path.exists(args.import_json):
            print(f"Erro: arquivo '{args.import_json}' não encontrado.")
            sys.exit(1)
        with open(args.import_json, "r", encoding="utf-8") as f:
            imported = json.load(f)
        if isinstance(imported, list):
            completed_set = set(imported)
        elif isinstance(imported, dict) and "completed" in imported:
            completed_set = set(imported["completed"])
        salvar_progresso(completed_set)

    if args.mark:
        for it_id in args.mark:
            completed_set.add(it_id)
        salvar_progresso(completed_set)

    if args.unmark:
        for it_id in args.unmark:
            completed_set.discard(it_id)
        salvar_progresso(completed_set)

    if args.commit_push:
        os.system(f"cd '{BASE_DIR}' && git add progresso.json && git commit -m 'chore: atualizar progresso de estudos ({len(completed_set)} concluídos)' && git push origin main")
        print("✓ Progresso publicado no GitHub! O GitHub Pages será atualizado em instantes.")

    if args.status or (not args.import_json and not args.mark and not args.unmark and not args.commit_push):
        total = prog.get("total_items", 698)
        comp = len(completed_set)
        pct = (comp / total * 100) if total else 0.0
        print("\n==========================================")
        print("📊 STATUS DE PROGRESSO DOS ESTUDOS")
        print("==========================================")
        print(f"Última atualização: {prog.get('updated_at', 'Nunca')}")
        print(f"Itens concluídos:   {comp} de {total} ({pct:.1f}%)")
        if comp > 0:
            print("\nPrimeiros itens concluídos:")
            for it in sorted(list(completed_set))[:10]:
                print(f"  - {it}")
            if comp > 10:
                print(f"  ... e mais {comp - 10} itens.")
        print("==========================================\n")

if __name__ == "__main__":
    main()
