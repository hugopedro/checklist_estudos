import os
from atualizar_planos_ti import build_study_guide
from gerar_secoes_basicas import get_secoes_basicas
from gerar_secoes_ti_core import get_secoes_ti_core
from gerar_secoes_ti_infra_gov import get_secoes_ti_infra_gov
from gerar_secoes_trilhas_vanguarda import get_secoes_trilhas_vanguarda

target_path = "/home/Hugo/Documentos/iniciando/o_que_estudar_de_fato.md"

full_content = (
    build_study_guide() + "\n" +
    get_secoes_basicas() + "\n" +
    get_secoes_ti_core() + "\n" +
    get_secoes_ti_infra_gov() + "\n" +
    get_secoes_trilhas_vanguarda()
)

with open(target_path, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Sucesso! {target_path} gerado com {len(full_content)} caracteres e {len(full_content.splitlines())} linhas.")
