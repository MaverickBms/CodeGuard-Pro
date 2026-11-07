import json, re, zipfile, html, hashlib, sys
from pathlib import Path

DOCX = Path('/home/mvxbms/Descargas/PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.docx')
raw = DOCX.read_bytes()
z = zipfile.ZipFile(DOCX)
xml = z.read('word/document.xml').decode('utf-8')
xml = xml.replace('</w:p>', '\n').replace('</w:tc>', ' | ')
text = re.sub(r'<[^>]+>', '', xml)
text = html.unescape(text)
lines = [re.sub(r'[ \t]+', ' ', l).strip() for l in text.split('\n')]
lines = [l for l in lines if l]

stage_re = re.compile(r'^ETAPA (\d+) — (.+)$')
section_re = re.compile(r'^(\d+)\.(\d+)\.\s+(.+)$')
parte_re = re.compile(r'^PARTE ([IVXL]+) — (.+)$')
seccion_re = re.compile(r'^ETAPAS? .+ · .+$')
markers = {'Proyecto', 'Proyecto final', 'Proyecto de salida', 'Reto', 'Laboratorio', 'Práctica'}
prose_starts = ('Objetivo:', 'Ampliación', 'Criterio', 'Bloque ')

# locate stages
stages = []
for i, l in enumerate(lines):
    m = stage_re.match(l)
    if m:
        stages.append((i, int(m.group(1)), m.group(2).strip()))

def priority_from(lines_slice):
    detail = ''
    for l in lines_slice:
        if l.startswith('Objetivo:'):
            break
        if re.match(r'^(P[123]\b|PRIORIDAD|Especialización)', l):
            detail = l.strip()
            break
    norm = ''
    d = detail.upper()
    if 'P2/P3' in d:
        norm = 'P3'
    elif re.match(r'^P3', d):
        norm = 'P3'
    elif re.match(r'^P2', d):
        norm = 'P2'
    elif re.match(r'^P1', d):
        norm = 'P1'
    elif 'ESPECIALIZACIÓN PRINCIPAL' in d:
        norm = 'P1'
    elif 'ESPECIALIZACIÓN COMPLEMENTARIA' in d:
        norm = 'P2'
    elif 'ESPECIALIZACIÓN AVANZADA' in d:
        norm = 'P3'
    return norm or 'P1', detail

def objective_from(lines_slice):
    for l in lines_slice:
        if l.startswith('Objetivo:'):
            return l[len('Objetivo:'):].strip()
    return ''

result = []
parte = ''
seccion = ''
for idx, (start, num, title) in enumerate(stages):
    end = stages[idx+1][0] if idx+1 < len(stages) else len(lines)
    # find last PARTE / ETAPAS heading before start
    for j in range(start-1, -1, -1):
        if parte_re.match(lines[j]):
            parte = lines[j]
            break
    for j in range(start-1, -1, -1):
        if seccion_re.match(lines[j]):
            seccion = lines[j]
            break
    body_end = end
    for j in range(start+1, end):
        if parte_re.match(lines[j]):
            body_end = j
            break
    body = lines[start+1:body_end]
    prioridad, prioridad_detalle = priority_from(body)
    objetivo = objective_from(body)
    # module sections
    mods = []
    current = None
    project_marker = None
    last_project_marker = ''
    project_lines = []
    extras = []
    for l in body:
        if l.startswith('Trayecto'):
            extras.append(l)
            break
        if l.startswith('Ampliación'):
            extras.append(l)
            current = None
            continue
        sm = section_re.match(l)
        if sm:
            current = {'numero': f'{sm.group(1)}.{sm.group(2)}', 'titulo': sm.group(3).strip(), 'lecciones': []}
            mods.append(current)
            continue
        if l in markers or l.startswith('Proyecto final'):
            project_marker = l
            last_project_marker = l
            continue
        if project_marker:
            # project text continues until a section/heading/extra
            if l.startswith('Criterio:'):
                extras.append(l)
                project_marker = None
                continue
            if section_re.match(l) or parte_re.match(l) or stage_re.match(l):
                project_marker = None
            else:
                if len(l) <= 300:
                    project_lines.append(l)
                continue
        if l.startswith('Criterio de dominio'):
            extras.append(l)
            current = None
            continue
        if current is None:
            continue
        if l.startswith('Objetivo:') or re.match(r'^(P[123]\b|PRIORIDAD)', l):
            continue
        if len(l) > 110:
            continue
        if l.startswith(prose_starts):
            continue
        if len(l.split()) > 14:
            continue
        if l.endswith(':') and not re.match(r'^[A-ZÁÉÍÓÚÑ][^.]{0,80}$', l):
            continue
        if l == '|' or l.startswith('|'):
            continue
        # topic lines: limpiar artefactos de extracción y deduplicar
        l = re.sub(r'\+1$', '', l).strip()
        if not l:
            continue
        if re.match(r'^(Comenzaremos|Veremos|Aprenderemos|Trabajaremos|Usaremos|Construiremos|Diseñaremos|Estudiaremos|Practicaremos)\b', l):
            continue
        if l not in current['lecciones']:
            current['lecciones'].append(l)
    # remove empty modules
    mods = [m for m in mods if m['lecciones']]
    project = ' '.join(project_lines).strip()
    result.append({
        'numero': num,
        'titulo': title,
        'bloque': parte.replace('PARTE ', '').strip(),
        'seccion': seccion.strip(),
        'prioridad': prioridad,
        'prioridad_detalle': prioridad_detalle,
        'objetivo': objetivo,
        'modulos': mods,
        'proyecto': project,
        'proyecto_titulo': last_project_marker or ('Proyecto final' if num == 32 else ''),
        'notas': extras,
    })

meta = {
    'nombre': 'PROYECTO ASCENSO — Roadmap Maestro Consolidado',
    'edicion': '3.1',
    'fecha_consolidacion': '2026-10-29',
    'fuente': DOCX.name,
    'sha256_fuente': hashlib.sha256(raw).hexdigest(),
    'regla': 'Contenido extraído del documento oficial. No se inventan etapas, módulos ni dependencias.',
}
out = {'metadata': meta, 'etapas': result}
Path('ascenso_3_1.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print('Etapas:', len(result))
print('Módulos:', sum(len(s['modulos']) for s in result))
print('Lecciones:', sum(len(m['lecciones']) for s in result for m in s['modulos']))
print('Proyectos:', sum(1 for s in result if s['proyecto']))
for s in result:
    print(f"{s['numero']:>2} {s['prioridad']:<2} {s['titulo'][:55]:<55} mods={len(s['modulos']):>2} lec={sum(len(m['lecciones']) for m in s['modulos']):>3} proj={bool(s['proyecto'])}")
