import re
import json

with open("/home/Hugo/Documentos/iniciando/o_que_estudar_de_fato.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

disciplines = []
current_disc = None
current_section = None
current_subtopic = None

parent_header = None

for idx, line in enumerate(lines):
    m_disc = re.match(r"^### DISCIPLINA (\d+): (.+)", line)
    if m_disc:
        num = int(m_disc.group(1))
        title = m_disc.group(2).strip()

        if num in [1, 2, 3, 4, 5]:
            tier = "Nível A (Núcleo de Ferro - 80% a 100%)"
            tier_class = "badge-tier-a"
            tier_desc = "Carga Semanal: 70% do tempo (14h a 17h/sem)"
        elif num in [6, 7, 9]:
            tier = "Nível A/B (Núcleo Central + Diferenciais)"
            tier_class = "badge-tier-ab"
            tier_desc = "Carga Semanal: 70% no núcleo + 20% nos avançados"
        elif num in [8]:
            tier = "Nível A/B/C (Segurança Geral + Forense)"
            tier_class = "badge-tier-abc"
            tier_desc = "Carga: 70% na ISO/OWASP, C na Forense"
        else:
            tier = "Nível B (Diferenciais Competitivos)"
            tier_class = "badge-tier-b"
            tier_desc = "Carga Semanal: 20% do tempo (4h a 5h/sem)"

        current_disc = {
            "id": f"disc_{num}",
            "num": num,
            "title": title,
            "tier": tier,
            "tier_class": tier_class,
            "tier_desc": tier_desc,
            "incidence": "10/10 (100%)",
            "stack": {},
            "groups": [],
            "checklists": [],
            "bancas": []
        }
        disciplines.append(current_disc)
        current_section = None
        current_subtopic = None
        parent_header = None
        continue

    if not current_disc:
        continue

    if line.startswith("## PARTE 2:"):
        break

    m_inc = re.match(r"^\*\s+\*\*Incidência Comprovada.+?\*\*:\s*(\d+/\d+\s*\(.+?\))", line)
    if m_inc:
        current_disc["incidence"] = m_inc.group(1).strip()
        continue

    if "* **Ementa Granular Ponto a Ponto:**" in line:
        current_section = "ementa"
        parent_header = None
        continue
    elif "* **Checklist de Domínio Técnico Pré-Edital" in line:
        current_section = "checklist"
        parent_header = None
        continue
    elif "* **Padrões das Bancas e Armadilhas Recorrentes:**" in line:
        current_section = "bancas"
        parent_header = None
        continue
    elif "* **Stack Tecnológico Oficial Mapeado" in line or "* **Stack Tecnológico e Normativo" in line:
        current_section = "stack"
        parent_header = None
        continue
    elif line.startswith("---") or line.startswith("### DISCIPLINA"):
        current_section = None
        parent_header = None
        continue

    if current_section == "ementa":
        m_sub = re.match(r"^\s{2}\*\s+\*\*([^*]+)\*\*", line)
        if m_sub:
            current_subtopic = {
                "id": f"d{current_disc['num']}_g{len(current_disc['groups'])+1}",
                "title": m_sub.group(1).strip().rstrip(":"),
                "items": []
            }
            current_disc["groups"].append(current_subtopic)
            parent_header = None
            continue

        # Item de 4 espaços (pode ser folha ou cabeçalho de lista aninhada)
        m_item = re.match(r"^\s{4}[\*\-]\s+(.+)", line)
        if m_item and current_subtopic:
            item_text = m_item.group(1).strip()
            # Checar se há sub-itens aninhados (6+ espaços) logo abaixo
            has_sub = False
            for forward in lines[idx+1:min(idx+6, len(lines))]:
                if re.match(r"^\s{6,10}[\*\-]\s+", forward):
                    has_sub = True
                    break
                elif re.match(r"^\s{2,4}[\*\-]\s+", forward) or forward.startswith("* **") or forward.startswith("###"):
                    break

            if has_sub:
                parent_header = item_text.rstrip(":")
            else:
                parent_header = None
                item_id = f"{current_subtopic['id']}_i{len(current_subtopic['items'])+1}"
                current_subtopic["items"].append({
                    "id": item_id,
                    "text": item_text
                })
            continue

        # Sub-itens aninhados de 6 a 10 espaços (folhas atômicas)
        m_sub_it = re.match(r"^\s{6,10}[\*\-]\s+(.+)", line)
        if m_sub_it and current_subtopic:
            sub_txt = m_sub_it.group(1).strip()
            clean_parent = re.sub(r'[*_]', '', parent_header).strip().rstrip(':') if parent_header else None
            if clean_parent and not sub_txt.startswith(clean_parent):
                full_txt = f"**{clean_parent}**: {sub_txt}"
            else:
                full_txt = sub_txt
            item_id = f"{current_subtopic['id']}_i{len(current_subtopic['items'])+1}"
            current_subtopic["items"].append({
                "id": item_id,
                "text": full_txt
            })
            continue

    elif current_section == "checklist":
        m_chk = re.match(r"^\s*-\s+\[ \]\s+(.+)", line)
        if m_chk:
            chk_id = f"d{current_disc['num']}_chk_{len(current_disc['checklists'])+1}"
            current_disc["checklists"].append({
                "id": chk_id,
                "text": m_chk.group(1).strip()
            })

    elif current_section == "bancas":
        m_banca = re.match(r"^\s{2}\*\s+\*\*([^*]+)\*\*:\s*(.+)", line)
        if m_banca:
            current_disc["bancas"].append({
                "banca": m_banca.group(1).strip(),
                "text": m_banca.group(2).strip()
            })

    elif current_section == "stack":
        m_st_cat = re.match(r"^\s{2}\*\s+\*\*([^*]+)\*\*:\s*(.+)", line)
        if m_st_cat:
            cat_name = m_st_cat.group(1).strip()
            cat_val = m_st_cat.group(2).strip()
            current_disc["stack"][cat_name] = cat_val

# Read existing semesters and discursivas from data_checklist.json
with open("/home/Hugo/Documentos/iniciando/data_checklist.json", "r", encoding="utf-8") as f:
    old_data = json.load(f)

semesters = old_data.get("semesters", [])
discursivas = old_data.get("discursivas", [])

data_package = {
    "disciplines": disciplines,
    "semesters": semesters,
    "discursivas": discursivas
}

with open("/home/Hugo/Documentos/iniciando/data_checklist.json", "w", encoding="utf-8") as f:
    json.dump(data_package, f, ensure_ascii=False, indent=2)

total_ementa = sum(len(g["items"]) for d in disciplines for g in d["groups"])
total_chk = sum(len(d["checklists"]) for d in disciplines)
grand_total = total_ementa + total_chk

print(f"data_checklist.json atualizado!")
print(f"Disciplinas: {len(disciplines)}")
print(f"Total Grupos: {sum(len(d['groups']) for d in disciplines)}")
print(f"Itens de Ementa: {total_ementa}")
print(f"Itens de Checklist: {total_chk}")
print(f"Total Tópicos da Ementa: {grand_total} (anteriormente 366)")
