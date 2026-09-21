import json
import re
from bs4 import BeautifulSoup

def analyze_file(filepath):
    print(f"\n==========================================")
    print(f"ANÁLISE DE: {filepath}")
    print(f"==========================================")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Erro ao ler {filepath}: {e}")
        return

    lines = content.splitlines()
    print(f"Total de linhas: {len(lines)}, total de caracteres: {len(content)}")

    # 1. Caracteres de controle não imprimíveis
    # 0x00 to 0x1f exceto \t (9), \n (10), \r (13)
    found_ctrls = []
    for idx, line in enumerate(lines, 1):
        for c_idx, c in enumerate(line):
            code = ord(c)
            if code < 32 and code not in (9, 10, 13):
                found_ctrls.append((idx, c_idx, code, hex(code), line))
    
    print(f"\n1. Caracteres de controle encontrados: {len(found_ctrls)}")
    for idx, c_idx, code, hx, line in found_ctrls[:10]:
        print(f"   L{idx}:{c_idx} [ASCII {code} / {hx}] -> {repr(line[max(0, c_idx-20):min(len(line), c_idx+20)])}")

    # 2. Tabulações espúrias no meio do texto
    found_tabs = []
    for idx, line in enumerate(lines, 1):
        stripped = line.lstrip(' \t')
        if '\t' in stripped:
            found_tabs.append((idx, line))
    print(f"\n2. Linhas com TABs no meio do texto: {len(found_tabs)}")
    for idx, line in found_tabs[:10]:
        print(f"   L{idx}: {repr(line[:100])}")

    # 3. Padrões de LaTeX clássicos ou truncamentos espúrios
    latex_re = re.compile(r'(\\(?:land|lor|lnot|neg|to|rightarrow|leftarrow|leftrightarrow|iff|implies|veebar|vee|wedge|forall|exists|in|notin|subset|cap|cup|ne|le|ge|equiv|sim|approx|times|div|pm|mp|quad|cdot|sqrt|frac|sigma|pi|mu|lambda|theta|chi|alpha|beta|gamma|delta|epsilon|rho|sum|prod|partial|infty|left|right|text|mathbf|mathcal|binom)\b|\b(?:eebar|orall|xists|rac|inom|lpha|ullouterjoin|ightouterjoin)\b|[_^]\{[^}]+\})')
    found_latex = []
    for idx, line in enumerate(lines, 1):
        # Ignore comments and python regex definitions
        if filepath.endswith('.py') and ('re.compile' in line or 'r\'' in line or 'r\"' in line or 'def ' in line):
            continue
        # In HTML, ignore script sections for latex search
        if filepath.endswith('.html') and ('${' in line or 'console.log' in line or 'function ' in line):
            continue
        m = latex_re.findall(line)
        if m:
            found_latex.append((idx, m, line))
    print(f"\n3. Linhas com termos/escapes LaTeX ou truncamentos: {len(found_latex)}")
    for idx, m, line in found_latex[:10]:
        print(f"   L{idx} {m}: {line.strip()[:100]}")

    # 4. Mojibake ou corrupções UTF-8
    mojibake_re = re.compile(r'(?:Ã[\x80-\xbf]|â€[\x90-\x9f]|âœ[\x90-\xbf]|\ufffd|\?{2,}|Â[\xa0-\xbf])')
    found_mojibake = []
    for idx, line in enumerate(lines, 1):
        m = mojibake_re.findall(line)
        if m:
            found_mojibake.append((idx, m, line))
    print(f"\n4. Linhas com mojibake UTF-8 suspeito: {len(found_mojibake)}")
    for idx, m, line in found_mojibake[:10]:
        print(f"   L{idx} {m}: {line.strip()[:100]}")

    # 5. Resíduos de Markdown visíveis no HTML
    if filepath.endswith('.html'):
        soup = BeautifulSoup(content, 'html.parser')
        for tag in soup(['script', 'style', 'head']):
            tag.extract()
        vis_text = soup.get_text()
        vis_lines = vis_text.splitlines()
        found_md = []
        for idx, vl in enumerate(vis_lines, 1):
            m = re.findall(r'(\*\*[^*]+\*\*|`[^`]+`)', vl)
            if m:
                found_md.append((idx, m, vl.strip()))
        print(f"\n5. Resíduos de Markdown (** ou `) no texto visível: {len(found_md)}")
        for idx, m, vl in found_md[:10]:
            print(f"   L{idx} {m}: {vl[:100]}")
    elif filepath.endswith('.json'):
        md_re = re.compile(r'(\*\*[^*]+\*\*|`[^`]+`)')
        found_md = []
        for idx, line in enumerate(lines, 1):
            m = md_re.findall(line)
            if m:
                found_md.append((idx, m, line))
        print(f"\n5. Termos Markdown em campos JSON (para renderização estruturada): {len(found_md)}")

    # 6. Ampersands não escapados em HTML visível
    if filepath.endswith('.html'):
        body_no_script = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', content, flags=re.DOTALL)
        body_no_comments = re.sub(r'<!--.*?-->', '', body_no_script, flags=re.DOTALL)
        unescaped_amp = list(re.finditer(r'&(?!amp;|lt;|gt;|quot;|#39;|#x27;|nbsp;|[a-zA-Z0-9]+;)', body_no_comments))
        print(f"\n6. Ampersands (&) não escapados em HTML visível: {len(unescaped_amp)}")
        for m in unescaped_amp[:10]:
            start = max(0, m.start() - 25)
            end = min(len(body_no_comments), m.end() + 25)
            print(f"   Pos {m.start()}: {repr(body_no_comments[start:end])}")

for fpath in [
    '/home/Hugo/Documentos/iniciando/data_checklist.json',
    '/home/Hugo/Documentos/iniciando/compilar_dashboard_html.py',
    '/home/Hugo/Documentos/iniciando/checklist_estudos.html',
    '/home/Hugo/Documentos/iniciando/o_que_estudar_de_fato.md',
    '/home/Hugo/Documentos/iniciando/gerar_secoes_basicas.py',
    '/home/Hugo/Documentos/iniciando/gerar_secoes_ti_core.py',
    '/home/Hugo/Documentos/iniciando/gerar_secoes_ti_infra_gov.py',
    '/home/Hugo/Documentos/iniciando/gerar_secoes_trilhas_vanguarda.py',
    '/home/Hugo/Documentos/iniciando/atualizar_planos_ti.py',
]:
    analyze_file(fpath)
