#!/usr/bin/env python3
"""
Genera docs/index.html desde data/*.tsv.

  python3 tools/build_page.py [--changed docs/_changed.json]

Heredado del tracker de funding de PitAssist (estructura clonada 2026-08-23):
la pagina es una aplicacion de pestañas. RESUMEN manda al abrir (cuando corrio
cada rutina, contadores que filtran, lo urgente); NOVEDADES es la lectura del
lunes; TODO es la tabla maestra filtrable; VIGILANDO son las cerradas a
re-abrir; SISTEMA es la maquinaria. Tema claro y oscuro. El estado de la dueña
— sus estados y su ENCAJE PERSONAL, que pisa al de la rutina donde exista —
vive en data/owner_status.json y lo escribe la propia pagina contra la API de
GitHub. Los TSV son de las rutinas; el JSON es del humano.
"""
import csv, os, sys, json, html, datetime, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
RUNS = os.path.join(ROOT, 'runs')
RESEARCH = os.path.join(ROOT, 'research')
OUT = os.path.join(ROOT, 'docs', 'index.html')
REPO = os.environ.get('GITHUB_REPOSITORY', 'OWNER/research-opportunities')
# El buzon que leen las rutinas. Cambiar cuando se conecte el Gmail de la dueña
# (paso 4 de SETUP.md); la pestaña Suscripciones lo enseña tal cual.
MAILBOX = 'CONFIGURAR-buzon@gmail.com'
e = html.escape

STATES = [
    ('NEW',         'sin ver'),
    ('READ',        'leido'),
    ('IN_PROGRESS', 'en curso'),
    ('APPLIED',     'solicitado'),
    ('RESOLVED',    'resuelto'),
    ('REVISIT',     'volver'),
    ('DISCARDED',   'descartado'),
]

def rundate():
    return os.environ.get('RUN_DATE') or datetime.date.today().isoformat()

def load(name):
    p = os.path.join(DATA, name + '.tsv')
    if not os.path.exists(p):
        return []
    with open(p, newline='', encoding='utf-8') as fh:
        return [dict(r) for r in csv.DictReader(fh, delimiter='\t')]

def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True,
                          text=True, timeout=20).stdout.strip()

def changed_ids():
    """IDs tocados en los ultimos SIETE DIAS. La verdad la dice git, no la rutina.

    Siete dias y no `HEAD~1`: las tres rutinas empujan en commits distintos la
    misma madrugada, y entre medias empujan el CI y el founder — con `HEAD~1`
    bastaba un commit de documentacion para vaciar la seccion.

    Una fila MOVIDA no es una fila nueva: si el mismo ID desaparecio de OTRO
    fichero en el mismo intervalo, es una mudanza (p. ej. una particion futura
    de un TSV). Si el ID solo aparece, es un hallazgo aunque su fichero se
    acabe de crear.
    """
    for a in sys.argv[1:]:
        if a.startswith('--changed='):
            try:
                return set(json.load(open(a.split('=', 1)[1])))
            except Exception:
                return set()
    try:
        base = git('rev-list', '-1', '--before=7 days ago', 'HEAD') or \
               git('rev-list', '--max-parents=0', 'HEAD').split()[0]
        d = git('diff', base, 'HEAD', '--unified=0', '--', 'data/')
    except Exception:
        return None            # sin git no hay verdad: decide quien llama
    ID = r'([A-Z]{1,3}-\d+)\t'
    added, removed = {}, {}
    for chunk in d.split('\ndiff --git '):
        f = re.search(r'^\+\+\+ b/(\S+)', chunk, re.M)
        f = f.group(1) if f else '?'
        added[f] = set(re.findall(r'^\+' + ID, chunk, re.M))
        removed[f] = set(re.findall(r'^-' + ID, chunk, re.M))
    ids = set()
    for f, plus in added.items():
        gone = set().union(*(v for k, v in removed.items() if k != f), set())
        ids |= plus - gone
    return ids

# ---------------------------------------------------------------- datos

OPP_TABS = ['postdocs', 'jobs', 'fellowships', 'groups', 'events', 'training']
SYS_TABS = ['action_now', 'sources', 'subscriptions', 'inbox_triage',
            'changelog', 'readme']
ALL_TABS = OPP_TABS + ['watchlist_closed'] + SYS_TABS
data = {t: load(t) for t in ALL_TABS}
RUNDATE = rundate()
CHANGED = changed_ids()

TAB_LABEL = {'postdocs': 'postdoc', 'jobs': 'empleo', 'fellowships': 'fellowship',
             'groups': 'grupo', 'events': 'evento', 'training': 'formacion',
             'watchlist_closed': 'vigilada'}

GROUP = {'postdocs': 'postdocs', 'jobs': 'jobs', 'fellowships': 'fellowships',
         'groups': 'groups', 'events': 'events', 'training': 'training',
         'watchlist_closed': 'watch'}

def fit(r):
    try:
        return int(float(r.get('Fit_1_5') or 0))
    except ValueError:
        return 0

def dleft(r):
    """`Deadline` en convocatorias, `Application_Deadline` en el resto."""
    for c in ('Deadline', 'Application_Deadline'):
        m = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', (r.get(c) or '').strip())
        if m:
            try:
                return (datetime.date(*map(int, m.groups())) -
                        datetime.date(*map(int, RUNDATE.split('-')))).days
            except ValueError:
                return None
    return None

def actionable(r):
    if (r.get('Status') or '').upper() == 'CLOSED':
        return False
    if r['_fit'] >= 4 and r['_dl'] is not None and 0 <= r['_dl'] <= 45:
        return True
    if (r.get('Competition_Level') or '').upper() == 'LOW' and r['_fit'] >= 3:
        return True
    return (r.get('Effort_Estimate') or '').upper() == 'XS' and r['_fit'] >= 3

for t in OPP_TABS + ['watchlist_closed']:
    for r in data[t]:
        r['_fit'], r['_dl'], r['_tab'] = fit(r), dleft(r), t
for t in OPP_TABS:
    for r in data[t]:
        r['_act'] = actionable(r)

opps = [r for t in OPP_TABS for r in data[t]]
watch = data['watchlist_closed']

if CHANGED is None:
    fresh = [r for r in opps if (r.get('Change_Flag') or '').upper() in ('NEW', 'UPDATED')]
    CHANGED = {r.get('ID') for r in fresh}
else:
    fresh = [r for r in opps if (r.get('ID') or '') in CHANGED]
fresh.sort(key=lambda r: (-r['_fit'], r['_dl'] if r['_dl'] is not None else 9999))

def urgsort(rows):
    """Urgente por defecto: reloj mas corto primero, encaje de desempate; sin
    reloj, por encaje. Es el orden pactado con el founder — fijo, sin memoria."""
    return sorted(rows, key=lambda r: (r['_dl'] if r['_dl'] is not None and r['_dl'] >= 0 else 9999,
                                       -r['_fit']))

n_open30 = sum(1 for r in opps if r['_dl'] is not None and 0 <= r['_dl'] <= 30
               and (r.get('Status') or '').upper() != 'CLOSED')
n_act = sum(1 for r in opps if r['_act'])
urgent = [r for r in urgsort(opps)
          if r['_dl'] is not None and r['_dl'] >= 0 and r['_fit'] >= 3
          and (r.get('Status') or '').upper() != 'CLOSED'][:7]

# ---------------------------------------------------------------- informes

def md_html(text):
    """Markdown minimo y suficiente para los informes de runs/: cabeceras,
    tablas, listas, negrita, enlaces. Sin dependencias."""
    out, tbl, lst = [], [], False
    def flush_tbl():
        nonlocal tbl
        if not tbl:
            return
        rows = [r for r in tbl if not all(re.fullmatch(r'[:\s-]*', c) for c in r)]
        h = ''.join(f'<th>{c}</th>' for c in rows[0])
        b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
                    for r in rows[1:])
        out.append(f'<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>')
        tbl = []
    def inline(s):
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',
                   r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
        return s
    for raw in text.split('\n'):
        line = inline(e(raw.rstrip()))
        if raw.strip().startswith('|'):
            tbl.append([c.strip() for c in line.strip().strip('|').split('|')])
            continue
        flush_tbl()
        if lst and not raw.lstrip().startswith('- '):
            out.append('</ul>'); lst = False
        if re.match(r'^#{1,2} ', raw):
            out.append(f'<h4>{line.lstrip("# ")}</h4>')
        elif re.match(r'^#{3,} ', raw):
            out.append(f'<h5>{line.lstrip("# ")}</h5>')
        elif raw.strip() in ('---', '***'):
            out.append('<hr>')
        elif raw.lstrip().startswith('- '):
            if not lst:
                out.append('<ul>'); lst = True
            out.append(f'<li>{line.lstrip()[2:]}</li>')
        elif raw.strip():
            cls = ' class="alertp"' if raw.lstrip().startswith('ALERTA') else ''
            out.append(f'<p{cls}>{line}</p>')
    flush_tbl()
    if lst:
        out.append('</ul>')
    return ''.join(out)

ROUTINES = [
    ('positions',   'Posiciones',  ['postdocs', 'jobs']),
    ('fellowships', 'Fellowships', ['fellowships', 'watchlist_closed']),
    ('ecosystem',   'Ecosistema',  ['groups', 'events', 'training']),
]

def routine_info():
    """El informe que se enseña es el ULTIMO de cada rutina, y una rutina puede
    dejar varios en un dia: `<fecha>-<rutina>.md`, luego `-2`, `-3`… Ordenar por
    nombre no basta y `endswith('-<rutina>.md')` ni siquiera ve los sufijados —
    el 2026-08-03 la pagina enseño toda la tarde la ALERTA de Gmail de la pasada
    de la mañana, ya resuelta dos pasadas despues."""
    info = {}
    reports = sorted(os.listdir(RUNS)) if os.path.isdir(RUNS) else []
    for slug, name, files in ROUTINES:
        pat = re.compile(r'^(\d{4}-\d{2}-\d{2})-' + re.escape(slug) + r'(?:-(\d+))?\.md$')
        mine = sorted(((m.group(1), int(m.group(2) or 1), f)
                       for f in reports if (m := pat.match(f))))
        item = {'name': name, 'date': None, 'alerta': '', 'html': '', 'iso': None}
        if mine:
            last = mine[-1][2]
            item['date'] = last[:10]
            txt = open(os.path.join(RUNS, last), encoding='utf-8').read()
            item['html'] = md_html(txt)
            m = re.search(r'^ALERTA[:\s]*(.{0,220})', txt, re.M)
            if m:
                item['alerta'] = m.group(1).strip()
        try:
            iso = git('log', '-1', '--format=%cI', '--',
                      *[f'data/{f}.tsv' for f in files])
            item['iso'] = iso or None
        except Exception:
            pass
        info[slug] = item
    return info

def research_reports():
    """Informes de investigacion dirigida (research/). Son de encargo, no de una
    pasada semanal, asi que viven aparte de runs/ pero se leen igual: en la pagina."""
    out = []
    if not os.path.isdir(RESEARCH):
        return out
    for f in sorted(os.listdir(RESEARCH), reverse=True):
        if not f.endswith('.md'):
            continue
        txt = open(os.path.join(RESEARCH, f), encoding='utf-8').read()
        title = next((l.lstrip('# ').strip() for l in txt.split('\n') if l.startswith('# ')), f[:-3])
        out.append({'id': f[:-3], 'date': f[:10], 'title': title, 'html': md_html(txt)})
    return out

RESEARCH_DOCS = research_reports()
RINFO = routine_info()
try:
    LAST_ISO = git('log', '-1', '--format=%cI', '--', 'data/') or ''
except Exception:
    LAST_ISO = ''

# ---------------------------------------------------------------- piezas html

DETAILS, _DKEY = {}, {}

def detail_key(r):
    k = _DKEY.get(id(r))
    if k is None:
        k = _DKEY[id(r)] = len(_DKEY)
        DETAILS[k] = [[c, str(v)] for c, v in r.items()
                      if not c.startswith('_') and str(v).strip()]
    return k

def linkify(u):
    u = str(u or '').strip()
    return f'<a href="{e(u)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">abrir ↗</a>' if u.startswith('http') else ''

def amount(r):
    g = lambda c: (r.get(c) or '').strip()
    for c in ('Amount_EUR', 'Salary_EUR_Year', 'Cost_EUR'):
        v = g(c).replace('.', '').replace(',', '')
        if v.isdigit():
            n = int(v)
            return f'{n:,}'.replace(',', '.'), n
    return '', -1

def money(r):
    """La linea de contexto bajo el titulo cambia de sentido segun la tabla: en
    una posicion es sitio y salario, en una beca es funder y dinero, en un
    evento es sede y coste."""
    g = lambda c: (r.get(c) or '').strip()
    t = r['_tab']
    place = ' '.join(x for x in (g('City'), g('Country')) if x) or g('City_or_Online')
    bits = []
    if t in ('postdocs', 'jobs'):
        inst = g('Institution') or g('Company_or_Institution')
        bits = [e(x) for x in (inst, place) if x]
        if g('Salary_EUR_Year'):
            bits.append(f'salario {e(g("Salary_EUR_Year"))} EUR/año')
        if g('Start_Date'):
            bits.append('empieza ' + e(g('Start_Date')))
    elif t == 'fellowships':
        bits = [e(g('Funder'))] if g('Funder') else []
        if g('Amount_EUR'):
            bits.append(f'hasta {e(g("Amount_EUR"))} EUR')
        if g('Duration'):
            bits.append(e(g('Duration')))
    elif t == 'groups':
        bits = [e(x) for x in (g('PI'), g('Institution'), place) if x]
    elif t == 'events':
        bits = [e(place)] if place else []
        if g('Start_Date'):
            bits.append('celebra ' + e(g('Start_Date')))
        if g('Cost_EUR'):
            bits.append(f'coste {e(g("Cost_EUR"))} EUR')
    elif t == 'training':
        bits = [e(x) for x in (g('Provider'), place) if x]
        if g('Cost_EUR'):
            bits.append(f'coste {e(g("Cost_EUR"))} EUR')
    return ' · '.join(bits)

def dl_badge(r):
    if r['_dl'] is None:
        return ''
    d = r['_dl']
    if d < 0:
        return f'<span class="b cal">cerro hace {abs(d)} d</span>'
    cls = 'crit' if d <= 14 else ('urg' if d <= 45 else 'cal')
    return f'<span class="b {cls}">cierra en {d} d</span>'

def badges(r):
    b = [f'<span class="b tab">{e(TAB_LABEL.get(r["_tab"], r["_tab"]))}</span>']
    if (r.get('ID') or '') in CHANGED:
        b.append('<span class="b new">nuevo</span>')
    b.append(f'<span class="b fit" data-fitb="{r["_fit"]}">fit {r["_fit"]}</span>')
    c = (r.get('Competition_Level') or '').upper()
    if c:
        b.append(f'<span class="b comp {c.lower()}">competencia {e(c.lower())}</span>')
    st = (r.get('Status') or '').upper()
    if st and st != 'OPEN':
        b.append(f'<span class="b st">{e(st.lower())}</span>')
    b.append(dl_badge(r))
    cf = (r.get('Confidence') or '').upper()
    if cf and cf != 'VERIFIED':
        b.append(f'<span class="b unv">{e(cf.lower())}</span>')
    return ''.join(x for x in b if x)

def statebar(rid):
    btns = ''.join(f'<button class="sb" data-s="{k}" onclick="setState(\'{rid}\',\'{k}\',event)">{lbl}</button>'
                   for k, lbl in STATES)
    return f'<div class="states" data-id="{e(rid)}">{btns}</div>'

def searchtext(r):
    return ' '.join(str(r.get(k, '')) for k in
                    ('ID', 'Name', 'Institution', 'Company_or_Institution',
                     'Funder', 'PI', 'Provider', 'Organiser', 'City', 'Country',
                     'Geography_Eligible', 'Research_Lines', 'Techniques',
                     'Requirements_Key', 'Fit_Rationale',
                     'Eligibility_Key_Conditions')).lower()

def card(r):
    rid = r.get('ID', '')
    line = money(r)
    return f'''<article class="card" data-id="{e(rid)}" data-fit="{r['_fit']}" data-tab="{e(r['_tab'])}" data-g="{GROUP.get(r['_tab'], '')}"
 data-fresh="{'1' if rid in CHANGED else '0'}" data-act="{'1' if r.get('_act') else '0'}"
 data-dl="{r['_dl'] if r['_dl'] is not None else ''}" data-text="{e(searchtext(r))}">
 <h3><span class="id">{e(rid)}</span>{e(r.get('Name', ''))}</h3>
 <div class="badges">{badges(r)}</div>
 {f'<p class="money">{line}</p>' if line else ''}
 <p class="why">{e((r.get('Fit_Rationale') or r.get('Why_It_Matters') or '')[:420])}</p>
 <p class="next"><strong>Siguiente paso</strong> {e(r.get('Next_Action', '') or '—')}</p>
 {statebar(rid)}
 <div class="tools">{linkify(r.get('URL'))}
  <button onclick="opencard(this)">todas las columnas</button></div>
 <div class="detail" data-d="{detail_key(r)}" data-id="{e(rid)}"></div>
</article>'''

def oprow(r, ncols):
    rid = r.get('ID', '')
    amt, amts = amount(r)
    dl = r['_dl']
    dldate = ((r.get('Deadline') or '').strip() or
              (r.get('Application_Deadline') or '').strip())
    comp = (r.get('Competition_Level') or '').strip().upper()
    dcls = ' crit' if dl is not None and 0 <= dl <= 14 else (
           ' urg' if dl is not None and 0 <= dl <= 45 else '')
    return (f'<tr class="oprow" data-id="{e(rid)}" data-tab="{e(r["_tab"])}" data-g="{GROUP.get(r["_tab"], "")}" data-fit="{r["_fit"]}"'
            f' data-fresh="{"1" if rid in CHANGED else "0"}" data-act="{"1" if r.get("_act") else "0"}"'
            f' data-comp="{e(comp)}" data-text="{e(searchtext(r))}" onclick="openrow(this)">'
            f'<td class="id xm">{e(rid)}</td>'
            f'<td class="xm">{e(TAB_LABEL.get(r["_tab"], r["_tab"]))}</td>'
            f'<td class="nm">{e(r.get("Name", ""))}</td>'
            f'<td class="num xm" data-s="{amts}">{amt}</td>'
            f'<td class="num fitc" data-s="{r["_fit"]}">{r["_fit"]}</td>'
            f'<td class="xm" data-s="{e(comp.lower() or "zz")}">{e(comp.lower() or "—")}</td>'
            f'<td class="num dlc{dcls}" data-s="{dl if dl is not None else 99999}" title="{e(dldate)}">'
            f'{f"{dl} d" if dl is not None else "—"}</td>'
            f'<td class="qa" onclick="event.stopPropagation()">'
            f'<span class="stlbl"></span>'
            f'<button title="leido" onclick="quick(\'{e(rid)}\',\'READ\',event)">✓</button>'
            f'<button title="en curso" onclick="quick(\'{e(rid)}\',\'IN_PROGRESS\',event)">●</button>'
            f'<button title="descartar" onclick="quick(\'{e(rid)}\',\'DISCARDED\',event)">✕</button></td></tr>'
            f'<tr class="gdet"><td colspan="{ncols}" data-d="{detail_key(r)}" data-id="{e(rid)}"></td></tr>')

def optable(rows, tid):
    heads = ('ID', 'tipo', 'nombre', 'EUR', 'fit', 'comp.', 'plazo', 'estado')
    xm = {'ID', 'tipo', 'EUR', 'comp.'}
    h = ''.join(f'<th class="{"xm" if x in xm else ""}" onclick="sortT(this)"'
                f'{" data-dir=\"a\"" if x == "plazo" else ""}>{x}</th>' for x in heads)
    return (f'<div class="twrap"><table class="otab" id="{tid}">'
            f'<thead><tr>{h}</tr></thead><tbody>'
            + ''.join(oprow(r, len(heads)) for r in rows)
            + '</tbody></table></div>')

def urow(r):
    rid = r.get('ID', '')
    d = r['_dl']
    dcls = 'crit' if d is not None and d <= 14 else 'urg'
    return (f'<div class="urow" data-id="{e(rid)}" data-g="{GROUP.get(r["_tab"], "")}" onclick="openrow(this)">'
            f'<span class="udays {dcls}">{d} d</span>'
            f'<span class="unm">{e(r.get("Name", "")[:80])}</span>'
            f'<span class="utag">{e(TAB_LABEL.get(r["_tab"], ""))}</span>'
            f'<span class="ufit num">fit {r["_fit"]}</span></div>'
            f'<div class="gdet udet" data-d="{detail_key(r)}" data-id="{e(rid)}"></div>')

def grid(rows, tab):
    if not rows:
        return f'<p class="empty">Sin filas en {e(tab)}.</p>'
    cols = [c for c in rows[0] if not c.startswith('_')][:5]
    head = ''.join(f'<th>{e(c)}</th>' for c in cols)
    body = ''
    for r in rows:
        txt = e(' '.join(str(v) for v in r.values()).lower())
        cells = ''.join(f'<td>{linkify(r[c]) if str(r[c]).startswith("http") else e(str(r[c])[:160])}</td>'
                        for c in cols)
        body += (f'<tr class="grow" data-text="{txt}" onclick="openrow(this)">{cells}</tr>'
                 f'<tr class="gdet"><td colspan="{len(cols)}" data-d="{detail_key(r)}"></td></tr>')
    return (f'<div class="twrap"><table class="otab">'
            f'<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')

# --- vistas ---

FRESH_CAP = 60
v_fresh = ''.join(card(r) for r in fresh[:FRESH_CAP]) or \
          '<p class="empty">Sin cambios en los ultimos siete dias.</p>'
if len(fresh) > FRESH_CAP:
    v_fresh += (f'<p class="empty">… y {len(fresh) - FRESH_CAP} novedades mas en la '
                f'pestaña «Todo» con el filtro <b>novedades</b>.</p>')

def rcard(slug):
    i = RINFO[slug]
    when = (f'<span class="rt" data-iso="{e(i["iso"] or "")}">{e(i["date"] or "nunca")}</span>')
    al = f'<p class="ralerta"><b>⚠</b> {e(i["alerta"])}</p>' if i['alerta'] else ''
    btn = (f'<button class="rlink" onclick="openrun(\'{slug}\')">ver informe</button>'
           if i['html'] else '<span class="rmut">sin informe</span>')
    return (f'<div class="rcard"><h4>{e(i["name"])}</h4>'
            f'<p class="rwhen">ultima pasada {when}</p>{al}{btn}</div>')

def sprio(r):
    v = (r.get('Priority') or '').strip().upper()
    return {'1': 0, 'ALTA': 0, 'HIGH': 0, '2': 1, 'MEDIUM': 1, 'MEDIA': 1,
            '3': 2, 'LOW': 2}.get(v, 3)

subs = sorted((r for r in data['subscriptions']
               if not (r.get('Service') or '').startswith('[DUPLICADO')),
              key=lambda r: (sprio(r), r.get('Service', '')))
n_subpend = sum(1 for r in subs if (r.get('Status') or '').upper() not in ('DONE', 'SKIP'))

def subitem(r):
    rid = r.get('ID', '')
    st = (r.get('Status') or '').upper()
    st = st if st in ('DONE', 'SKIP') else 'TODO'
    url = (r.get('URL_to_subscribe') or '').strip()
    pr = '<span class="b urg">prioridad alta</span>' if sprio(r) == 0 else ''
    txt = ' '.join(str(r.get(k, '')) for k in
                   ('Service', 'Category', 'What_it_delivers', 'Why_it_matters')).lower()
    link = (f'<a class="sgo" href="{e(url)}" target="_blank" rel="noopener" '
            f'onclick="event.stopPropagation()">ir a suscribirse ↗</a>' if url.startswith('http') else '')
    return (f'<div class="subi" data-id="{e(rid)}" data-tsv="{st}" data-text="{e(txt)}">'
            f'<div class="sbody"><h4>{e(r.get("Service", ""))} '
            f'<span class="scat">{e(r.get("Category", ""))}</span> {pr}</h4>'
            f'<p class="sdel">{e((r.get("What_it_delivers") or "")[:170])}</p>'
            f'<p class="swhy">{e((r.get("Why_it_matters") or "")[:200])}</p>{link}</div>'
            f'<div class="sact"><span class="sst"></span>'
            f'<button class="sbtn ok" onclick="subMark(\'{e(rid)}\',\'DONE\',event)">✓ me he suscrito</button>'
            f'<button class="sbtn no" onclick="subMark(\'{e(rid)}\',\'SKIP\',event)">✕ no me interesa</button>'
            f'</div></div>')

v_subs = ('<p class="lgnd"><b>Da de alta todo en <code>' + e(MAILBOX) + '</code></b> — es el buzon que leen las rutinas. Lo que llegue a otra direccion no lo vera nadie.</p>'
          '<p class="sub">Servicios de alertas por email: cada alta alimenta el buzon que la '
          'rutina del lunes tria. Marca lo que ya hayas hecho — lo marcado no vuelve a '
          'aparecer como pendiente en los informes, y las rutinas siguen añadiendo servicios '
          'nuevos que encuentren. Tus marcas se guardan con el boton de abajo, como los estados.</p>'
          + ''.join(subitem(r) for r in subs))

TILES = [
    ('t-fresh', len(fresh), 'novedades', "go('todo','fresh')"),
    ('t-unseen', '…', 'sin ver', "go('todo','st:NEW')"),
    ('t-soon', n_open30, 'cierran ≤30 d', "go('todo','soon')"),
    ('t-act', n_act, 'accionables', "go('todo','act')"),
    ('t-prog', '…', 'en curso', "go('todo','st:IN_PROGRESS')"),
    ('t-subs', n_subpend, 'por suscribir', "go('suscripciones')"),
]
tiles = ''.join(f'<button class="tile" id="{i}" onclick="{js}"><b>{n}</b><span>{lbl}</span></button>'
                for i, n, lbl, js in TILES)

v_resumen = f'''
<div class="rgrid">{''.join(rcard(s) for s, _, _ in ROUTINES)}</div>
<div class="tiles">{tiles}</div>
<h2>Urgente ahora</h2>
{''.join(urow(r) for r in urgent) or '<p class="empty">Nada con reloj corto.</p>'}
'''

v_todo_toolbar = f'''
<div class="chips" id="fchips">
 <span class="chip on" data-f="all" onclick="chip(this)">todo</span>
 <span class="chip" data-f="fresh" onclick="chip(this)">novedades</span>
 <span class="chip" data-f="act" onclick="chip(this)">accionable</span>
 <span class="chip" data-f="fit4" onclick="chip(this)">fit 4-5</span>
 <span class="chip" data-f="low" onclick="chip(this)">comp. baja</span>
 <span class="chip" data-f="soon" onclick="chip(this)">cierra &lt;45 d</span>
 <span class="sep"></span>
 {''.join(f'<span class="chip" data-f="st:{k}" onclick="chip(this)">{lbl}</span>' for k, lbl in STATES)}
</div>
<div class="chips" id="tchips">
 <span class="chip on" data-t="all" onclick="tchip(this)">todos los tipos</span>
 <span class="chip" data-t="postdocs" onclick="tchip(this)">postdocs</span>
 <span class="chip" data-t="jobs" onclick="tchip(this)">empleo</span>
 <span class="chip" data-t="fellowships" onclick="tchip(this)">fellowships</span>
 <span class="chip" data-t="events" onclick="tchip(this)">eventos</span>
 <span class="chip" data-t="groups" onclick="tchip(this)">grupos</span>
 <span class="chip" data-t="training" onclick="tchip(this)">formacion</span>
</div>'''

v_todo = (v_todo_toolbar
          + '<p class="lgnd">cada color de punto es un tipo (los chips de arriba son la leyenda) · '
            '<b class="cr">rojo</b> cierra en ≤14 dias · <b class="cw">ambar</b> en ≤45 · '
            'fit con <b>tu</b> = tu encaje personal · los filtros se pueden COMBINAR</p>'
          + optable(urgsort(opps), 'optable')
          + '<p class="sub" id="nres"></p>')
v_watch = ('<p class="sub">Cerradas que merecen vigilancia: cuando reabran, la rutina '
           'las devolvera a la tabla principal. «volver» es su estado natural.</p>'
           + optable(urgsort(watch), 'wtable'))
v_sistema = ('<h2>Proponer una fuente</h2>'
             '<p class="sub">Pega una URL y pulsa proponer. La proxima pasada la abrira, '
             'comprobara que no este duplicada y la completara en la tabla de fuentes '
             '(que ya crece sola: las rutinas añaden lo que descubren). Usa el mismo '
             'token de GitHub que los estados.</p>'
             '<div class="srcadd">'
             '<input id="srcurl" type="url" placeholder="https://…  pega aqui la fuente" '
             'onkeydown="if(event.key===\'Enter\')addSrc()">'
             '<button onclick="addSrc()">proponer</button></div>'
             '<div id="srcpend"></div>'
             '<p class="sub">Para el control fino: '
             f'<a href="https://github.com/{REPO}/edit/main/data/sources.tsv" target="_blank" '
             'rel="noopener">editar sources.tsv en GitHub ↗</a>.</p>'
             + ('<h2>Informes de investigacion</h2>'
                '<p class="sub">Investigaciones dirigidas, a peticion. No son pasadas semanales.</p>'
                + ''.join(f'<div class="rcard"><h4>{e(d["title"])}</h4>'
                          f'<p class="rwhen">{e(d["date"])}</p>'
                          f'<button class="rlink" onclick="openrun(\'{d["id"]}\')">leer informe</button></div>'
                          for d in RESEARCH_DOCS)
                if RESEARCH_DOCS else '')
             + '<h2>La maquinaria</h2>'
             '<p class="sub">Lo que usan las rutinas. Generado; no editar a mano.</p>'
             + ''.join(f'<details class="tabsec"><summary>{t.replace("_", " ")} '
                       f'<span class="n">{len(data[t])}</span></summary>{grid(data[t], t)}</details>'
                       for t in SYS_TABS if data[t]))

srcurls = sorted({(r.get('URL') or '').strip().rstrip('/').lower()
                  for r in data['sources'] if (r.get('URL') or '').strip()})
srcjson = json.dumps(srcurls, separators=(',', ':')).replace('</', r'<\/')

_reports = {s: {'name': RINFO[s]['name'], 'date': RINFO[s]['date'], 'html': RINFO[s]['html']}
            for s, _, _ in ROUTINES}
_reports.update({d['id']: {'name': d['title'], 'date': d['date'], 'html': d['html']}
                 for d in RESEARCH_DOCS})
runsjson = json.dumps(_reports, ensure_ascii=False, separators=(',', ':')).replace('</', r'<\/')
dstore = json.dumps(DETAILS, ensure_ascii=False, separators=(',', ':')).replace('</', r'<\/')

NTABS = [('resumen', 'Resumen', ''), ('novedades', 'Novedades', len(fresh)),
         ('todo', 'Todo', len(opps)), ('vigilando', 'Vigilando', len(watch)),
         ('suscripciones', 'Suscripciones', f'<span id="subcnt">{n_subpend}</span>'),
         ('sistema', 'Sistema', '')]
tabbar = ''.join(f'<button class="tb{" on" if k == "resumen" else ""}" data-v="{k}" '
                 f'onclick="go(\'{k}\')">{lbl}{f" <i>{n}</i>" if n != "" else ""}</button>'
                 for k, lbl, n in NTABS)

# ---------------------------------------------------------------- css

# Colores de categoria: los 6 primeros huecos de la paleta categorica validada
# del skill de dataviz, en su orden (el orden es el mecanismo de seguridad para
# daltonismo, no cosmetica). Validados con scripts/validate_palette.js contra
# ambas superficies el 2026-08-03: ALL CHECKS PASS en claro y oscuro; el aviso
# de contraste de 3 tonos en claro se cubre porque el color NUNCA va solo — cada
# insignia y chip lleva siempre su etiqueta de texto.
DARK = ('--bg:#0d1117;--fg:#e6edf3;--mut:#8d96a0;--line:#30363d;--card:#161b22;'
        '--card2:#1f2630;--acc:#818cf8;--accfg:#0d1117;--ok:#3fb950;--warn:#d29922;'
        '--bad:#f85149;--shadow:none;'
        '--stNEW:#8d96a0;--stREAD:#4493f8;--stIN_PROGRESS:#ab7df8;--stAPPLIED:#3fb950;'
        '--stRESOLVED:#2ea043;--stREVISIT:#d29922;--stDISCARDED:#f85149;'
        '--cpostdocs:#3987e5;--cjobs:#d95926;--cfellowships:#199e70;--cevents:#c98500;'
        '--cgroups:#d55181;--ctraining:#008300;--cwatch:#8d96a0')
LIGHT = ('--bg:#f6f8fa;--fg:#1f2328;--mut:#59636e;--line:#d8dee4;--card:#ffffff;'
         '--card2:#f6f8fa;--acc:#4f46e5;--accfg:#ffffff;--ok:#1a7f37;--warn:#9a6700;'
         '--bad:#cf222e;--shadow:0 1px 3px rgba(31,35,40,.06);'
         '--stNEW:#59636e;--stREAD:#0969da;--stIN_PROGRESS:#8250df;--stAPPLIED:#1a7f37;'
         '--stRESOLVED:#116329;--stREVISIT:#9a6700;--stDISCARDED:#cf222e;'
         '--cpostdocs:#2a78d6;--cjobs:#eb6834;--cfellowships:#1baf7a;--cevents:#eda100;'
         '--cgroups:#e87ba4;--ctraining:#008300;--cwatch:#59636e')

groupcss = ''.join(f'[data-g="{g}"],[data-t="{g}"]{{--g:var(--c{g})}}'
                   for g in ('postdocs', 'jobs', 'fellowships', 'groups',
                             'events', 'training', 'watch'))

statecss = ''.join(
    f'.states button[data-s="{k}"].on{{background:var(--st{k});border-color:var(--st{k});color:var(--card)}}'
    f'.card[data-state="{k}"] h3::after{{content:"{lbl}";background:var(--st{k});color:var(--card)}}'
    f'[data-state="{k}"] .stlbl{{color:var(--st{k})}}'
    for k, lbl in STATES)

CSS = '''
:root{__LIGHT__}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){__DARK__}}
:root[data-theme=dark]{__DARK__}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);
 font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
 -webkit-font-smoothing:antialiased}
.serif{font-family:"Iowan Old Style",Palatino,Georgia,serif}
#top{position:sticky;top:0;z-index:40;background:var(--bg);border-bottom:1px solid var(--line);
 padding:10px 16px 0}
.tline{max-width:960px;margin:0 auto;display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}
h1{font-size:19px;margin:0;font-family:"Iowan Old Style",Palatino,Georgia,serif;font-weight:600}
h1 i{font-style:normal;color:var(--acc)}
#upd{color:var(--mut);font-size:12.5px;margin-right:auto}
#thm{border:1px solid var(--line);background:var(--card);color:var(--mut);border-radius:999px;
 width:30px;height:30px;cursor:pointer;font-size:14px;line-height:1}
#q{flex:1 1 180px;min-width:150px;padding:7px 12px;font-size:14px;border:1px solid var(--line);
 border-radius:999px;background:var(--card);color:var(--fg);outline:none}
#q:focus{border-color:var(--acc)}
#tabs{max-width:960px;margin:6px auto 0;display:flex;gap:2px;overflow-x:auto;scrollbar-width:none}
#tabs::-webkit-scrollbar{display:none}
.tb{border:0;background:none;color:var(--mut);font:inherit;font-size:14px;padding:9px 13px;
 cursor:pointer;white-space:nowrap;border-bottom:2px solid transparent}
.tb i{font-style:normal;font-size:11.5px;color:var(--mut);opacity:.8}
.tb.on{color:var(--fg);border-bottom-color:var(--acc);font-weight:600}
.wrap{max-width:960px;margin:0 auto;padding:18px 16px 90px}
.view{display:none}.view.on{display:block}
h2{font-size:12.5px;text-transform:uppercase;letter-spacing:.09em;color:var(--mut);
 margin:26px 0 10px;font-weight:600}
.sub{color:var(--mut);font-size:13.5px;margin:6px 0 12px}
/* resumen */
.rgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;margin-top:14px}
.rcard{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;
 box-shadow:var(--shadow)}
.rcard h4{margin:0 0 3px;font-size:14px}
.rwhen{margin:0;color:var(--mut);font-size:12.5px}
.ralerta{margin:8px 0 0;font-size:12.5px;color:var(--fg);background:color-mix(in srgb,var(--warn) 11%,var(--card));border-left:3px solid var(--warn);border-radius:0 7px 7px 0;padding:6px 9px;line-height:1.45}.ralerta b{color:var(--warn)}.alertp{color:var(--fg)!important;background:color-mix(in srgb,var(--warn) 11%,var(--card));border-left:3px solid var(--warn);border-radius:0 7px 7px 0;padding:7px 10px!important}.srcadd{display:flex;gap:8px;margin:6px 0 4px;flex-wrap:wrap}.srcadd input{flex:1 1 240px;padding:8px 12px;font-size:14px;border:1px solid var(--line);border-radius:9px;background:var(--card);color:var(--fg)}.srcadd button{border:1px solid var(--acc);background:var(--acc);color:var(--accfg);border-radius:9px;padding:8px 16px;cursor:pointer;font-size:14px}#srcpend{font-size:13px;color:var(--mut);margin:2px 0 12px}#srcpend .pu{display:inline-block;background:var(--card2);border:1px solid var(--line);border-radius:999px;padding:2px 10px;margin:2px 4px 2px 0}
.rlink{margin-top:8px;border:1px solid var(--line);background:none;color:var(--acc);
 font-size:12.5px;padding:3px 10px;border-radius:999px;cursor:pointer}
.rmut{display:inline-block;margin-top:8px;color:var(--mut);font-size:12.5px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(108px,1fr));gap:10px;margin:14px 0 4px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 8px 10px;
 cursor:pointer;text-align:center;box-shadow:var(--shadow);font:inherit;color:var(--fg)}
.tile b{display:block;font-size:30px;font-weight:600;font-variant-numeric:tabular-nums;
 font-family:"Iowan Old Style",Palatino,Georgia,serif}
.tile span{font-size:11.5px;color:var(--mut);letter-spacing:.03em}
.tile:hover{border-color:var(--acc)}
.urow{display:flex;gap:10px;align-items:baseline;background:var(--card);border:1px solid var(--line);
 border-radius:10px;padding:9px 12px;margin-bottom:6px;cursor:pointer;box-shadow:var(--shadow)}
.udays{font-variant-numeric:tabular-nums;font-weight:700;font-size:13px;min-width:42px}
.udays.urg{color:var(--warn)}.udays.crit{color:var(--bad)}
.unm{flex:1;font-size:14.5px}
.utag,.ufit{color:var(--mut);font-size:12px;white-space:nowrap}
.udet{padding:10px 14px;background:var(--card2);border-radius:10px;margin:-2px 0 8px}
/* chips */
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 6px;align-items:center}
.sep{width:1px;height:18px;background:var(--line);margin:0 3px}
.chip{padding:5px 12px;border:1px solid var(--line);border-radius:999px;background:var(--card);
 color:var(--mut);font-size:13px;cursor:pointer;user-select:none}
.chip.on{background:var(--acc);border-color:var(--acc);color:var(--accfg)}
/* cards */
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;
 margin-bottom:10px;box-shadow:var(--shadow)}
.card h3{margin:0 0 7px;font-size:17px;line-height:1.35;font-weight:600}
.card h3::after{font-size:10.5px;padding:2px 7px;border-radius:999px;margin-left:8px;
 vertical-align:middle;white-space:nowrap}
.id{color:var(--mut);font-size:12px;font-weight:400;margin-right:6px;font-variant-numeric:tabular-nums}
.badges{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:8px}
.b{font-size:11px;padding:2px 8px;border-radius:999px;border:1px solid var(--line);
 color:var(--mut);white-space:nowrap}
.b.new{background:var(--ok);color:var(--card);border-color:var(--ok)}
.b[data-fitb="5"],.b[data-fitb="4"]{background:var(--acc);color:var(--accfg);border-color:var(--acc)}
.b.low{color:var(--ok);border-color:var(--ok)}
.b.urg{color:var(--warn);border-color:var(--warn)}
.b.crit{color:var(--bad);border-color:var(--bad);font-weight:600}
.b.unv{color:var(--warn);border-color:var(--warn)}
.b.tab{background:var(--card2);font-weight:500}
.money{margin:0 0 6px;font-size:13.5px;color:var(--mut)}
.why{margin:0 0 7px;font-size:14.5px}
.next{margin:0 0 9px;font-size:13.5px}
.states{display:flex;flex-wrap:wrap;gap:4px;margin:0 0 9px}
.states button{font-size:11px;padding:3px 9px;border-radius:999px;border:1px solid var(--line);
 background:none;color:var(--mut);cursor:pointer}
__STATECSS__
.fitbar{display:flex;gap:4px;align-items:center;font-size:12px;color:var(--mut);margin:0 0 9px;flex-wrap:wrap}
.fitbar button{width:26px;height:26px;border-radius:999px;border:1px solid var(--line);
 background:none;color:var(--mut);cursor:pointer;font-size:12px}
.fitbar button.on{background:var(--acc);border-color:var(--acc);color:var(--accfg)}
.tools{display:flex;gap:12px;align-items:center;font-size:12.5px}
.tools a,a{color:var(--acc)}
button{font:inherit}
.tools button{font-size:12.5px;background:none;border:1px solid var(--line);color:var(--mut);
 padding:3px 10px;border-radius:999px;cursor:pointer}
.detail{display:none;margin-top:10px}
.card.open .detail{display:block}
table.full{width:100%;border-collapse:collapse;font-size:13px}
table.full th{text-align:left;vertical-align:top;color:var(--mut);font-weight:500;
 padding:4px 10px 4px 0;width:33%;border-top:1px solid var(--line)}
table.full td{padding:4px 0;border-top:1px solid var(--line);word-break:break-word}
/* tablas */
.twrap{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--card);
 box-shadow:var(--shadow)}
table.otab{width:100%;border-collapse:collapse;font-size:14px}
table.otab thead th{text-align:left;color:var(--mut);font-weight:600;font-size:11.5px;
 text-transform:uppercase;letter-spacing:.05em;padding:9px 10px;border-bottom:1px solid var(--line);
 cursor:pointer;user-select:none;white-space:nowrap;position:sticky;top:0;background:var(--card);z-index:2}
table.otab thead th[data-dir="a"]::after{content:" ↑";color:var(--acc)}
table.otab thead th[data-dir="d"]::after{content:" ↓";color:var(--acc)}
table.otab td{padding:10px 10px;border-bottom:1px solid var(--line);vertical-align:top}
tr.oprow,tr.grow{cursor:pointer}
tr.oprow:hover td,tr.grow:hover td{background:var(--card2)}
tr.oprow td{white-space:nowrap}
tr.oprow td.nm{white-space:normal;min-width:200px;font-weight:500}
tr.oprow td.num{text-align:right;font-variant-numeric:tabular-nums}
tr.oprow td.id{color:var(--mut);font-size:11.5px}
td.dlc.urg{color:var(--warn);font-weight:600}
td.dlc.crit{color:var(--bad);font-weight:700}
td.fitc i{font-style:normal;font-size:10px;color:var(--acc);vertical-align:super}
td.qa{white-space:nowrap}
td.qa .stlbl{font-size:11.5px;margin-right:6px}
td.qa button{width:24px;height:24px;border-radius:6px;border:1px solid var(--line);background:none;
 color:var(--mut);cursor:pointer;font-size:11px;padding:0}
td.qa button:hover{border-color:var(--acc);color:var(--acc)}
tr.gdet{display:none}tr.gdet.open{display:table-row}
tr.gdet td{background:var(--card2);padding:12px 14px;white-space:normal}
div.gdet{display:none}div.gdet.open{display:block}
tr.oprow.hide,tr.oprow.hide+tr.gdet,tr.grow.hide,tr.grow.hide+tr.gdet{display:none}
.empty{color:var(--mut);padding:12px 2px;font-size:14px}
.hide{display:none!important}
.tabsec{border:1px solid var(--line);border-radius:12px;margin-bottom:8px;background:var(--card)}
.tabsec summary{padding:11px 15px;cursor:pointer;font-weight:600;font-size:14px}
.tabsec .n{color:var(--mut);font-weight:400;font-size:12.5px}
.tabsec .twrap{border:0;border-top:1px solid var(--line);border-radius:0}
/* informe modal */
#mod{position:fixed;inset:0;background:rgba(20,18,14,.45);display:none;z-index:60}
#mod.on{display:flex;align-items:flex-start;justify-content:center;padding:4vh 12px}
#mbox{background:var(--card);border:1px solid var(--line);border-radius:14px;max-width:760px;
 width:100%;max-height:88vh;overflow-y:auto;padding:20px 24px}
#mbox h4{font-size:15px;margin:16px 0 6px}#mbox h5{font-size:13.5px;margin:12px 0 4px}
#mbox p,#mbox li{font-size:13.5px}
#mbox table{width:100%;border-collapse:collapse;font-size:12.5px;margin:8px 0}
#mbox th,#mbox td{text-align:left;padding:4px 8px;border-bottom:1px solid var(--line)}
#mbox code{background:var(--card2);padding:1px 5px;border-radius:5px;font-size:12px}
#mclose{float:right;border:1px solid var(--line);background:none;color:var(--mut);
 border-radius:999px;width:28px;height:28px;cursor:pointer}
#bar{position:fixed;left:0;right:0;bottom:0;background:var(--card);border-top:1px solid var(--line);
 padding:7px 14px;font-size:12.5px;color:var(--mut);display:flex;gap:10px;align-items:center;z-index:50}
#bar button{font-size:12.5px;padding:4px 11px;border-radius:999px;border:1px solid var(--line);
 background:none;color:var(--fg);cursor:pointer}
footer{margin-top:36px;color:var(--mut);font-size:12px;border-top:1px solid var(--line);padding-top:12px}

.dot,[data-g] td.nm::before,.chip[data-t]:not([data-t="all"])::before,
[data-g].card h3 .id::before,[data-g].urow::before{
 content:"";display:inline-block;width:9px;height:9px;border-radius:50%;
 background:var(--g,var(--mut));margin-right:7px;vertical-align:baseline;flex:none}
[data-g] .b.tab{color:var(--g);border-color:color-mix(in srgb,var(--g) 45%,transparent);
 background:color-mix(in srgb,var(--g) 9%,transparent);font-weight:600}
.chip[data-t].on{background:color-mix(in srgb,var(--g,var(--acc)) 14%,var(--card));
 border-color:var(--g,var(--acc));color:var(--fg);font-weight:600}
.chip[data-t="all"].on{background:var(--acc);border-color:var(--acc);color:var(--accfg)}
.lgnd{color:var(--mut);font-size:12.5px;margin:4px 0 10px}
.lgnd b{font-weight:600}.lgnd .cr{color:var(--bad)}.lgnd .cw{color:var(--warn)}

.subi{display:flex;gap:14px;background:var(--card);border:1px solid var(--line);
 border-radius:12px;padding:12px 14px;margin-bottom:8px;box-shadow:var(--shadow)}
.subi h4{margin:0 0 4px;font-size:15px}
.scat{color:var(--mut);font-weight:400;font-size:12px;margin-left:4px}
.sdel{margin:0 0 4px;font-size:13.5px}
.swhy{margin:0 0 6px;font-size:13px;color:var(--mut)}
.sgo{font-size:13px}
.sbody{flex:1;min-width:0}
.sact{display:flex;flex-direction:column;gap:6px;align-items:flex-end;justify-content:center;min-width:150px}
.sst{font-size:12px;color:var(--mut)}
.sbtn{border:1px solid var(--line);background:none;border-radius:999px;padding:4px 12px;
 font-size:12.5px;color:var(--mut);cursor:pointer;white-space:nowrap}
.sbtn.ok.on{background:var(--ok);border-color:var(--ok);color:var(--card)}
.sbtn.no.on{background:var(--mut);border-color:var(--mut);color:var(--card)}
.subi[data-sub="DONE"]{border-color:color-mix(in srgb,var(--ok) 45%,var(--line))}
.subi[data-sub="DONE"] .sst{color:var(--ok);font-weight:600}
.subi[data-sub="SKIP"]{opacity:.55}
@media(max-width:700px){.subi{flex-direction:column}.sact{flex-direction:row;align-items:center}}
@media(min-width:1000px){
 .tline,#tabs,.wrap{max-width:1160px}
 body{font-size:17px}
 table.otab{font-size:14.5px}
 table.otab td{padding:11px 12px}
 .card h3{font-size:18px}
 .why{font-size:15px}.money,.next{font-size:14.5px}
 .tile b{font-size:34px}.tile span{font-size:12.5px}
 .unm{font-size:15px}.chip{font-size:13.5px}
 table.full{font-size:13.5px}#q{font-size:15px}
 .rcard h4{font-size:15px}.rwhen,.ralerta{font-size:13px}
}
@media(max-width:700px){.xm{display:none}.tile b{font-size:22px}
 .unm{font-size:13.5px}.wrap{padding:14px 10px 90px}}
'''.replace('__LIGHT__', LIGHT).replace('__DARK__', DARK).replace('__STATECSS__', statecss + groupcss)

# ---------------------------------------------------------------- js

JS = r'''
const REPO="__REPO__", FILE="data/owner_status.json";
let STATE={}, SHA=null, DIRTY=false, V="resumen";
/* filtros multiples y combinables: FS facetas (Y entre si), SS estados (O entre
   si), TS tipos (O entre si). Vacio = sin restriccion. */
let FS=new Set(), SS=new Set(), TS=new Set();
const SLBL={NEW:"sin ver",READ:"leido",IN_PROGRESS:"en curso",APPLIED:"solicitado",
 RESOLVED:"resuelto",REVISIT:"volver",DISCARDED:"descartado"};
const DET=JSON.parse(document.getElementById("dstore").textContent);
const RUNS=JSON.parse(document.getElementById("runstore").textContent);
const tok=()=>localStorage.getItem("gh_token")||"";

/* ---- tema ---- */
function applyTheme(t){document.documentElement.dataset.theme=t||"";
 document.getElementById("thm").textContent=
  (t==="dark"||(!t&&matchMedia("(prefers-color-scheme:dark)").matches))?"☀":"☾";}
function themeToggle(){
 const cur=document.documentElement.dataset.theme||
  (matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light");
 const nx=cur==="dark"?"light":"dark";
 localStorage.setItem("theme",nx);applyTheme(nx);}
applyTheme(localStorage.getItem("theme")||"");

/* ---- fechas relativas ---- */
function rel(iso){if(!iso)return "nunca";const d=(Date.now()-new Date(iso))/36e5;
 if(d<1)return "hace menos de 1 h";if(d<48)return "hace "+Math.round(d)+" h";
 return "hace "+Math.round(d/24)+" dias";}
document.querySelectorAll("[data-iso]").forEach(s=>{if(s.dataset.iso)s.textContent=rel(s.dataset.iso)});
const UP=document.getElementById("upd");if(UP.dataset.iso)UP.textContent="datos de "+rel(UP.dataset.iso);

/* ---- pestañas ---- */
function go(v,preset){
 V=v;
 document.querySelectorAll(".view").forEach(x=>x.classList.toggle("on",x.id==="v-"+v));
 document.querySelectorAll(".tb").forEach(b=>b.classList.toggle("on",b.dataset.v===v));
 if(preset!==undefined&&v==="todo"){
  FS.clear();SS.clear();TS.clear();
  if(preset&&preset!=="all"){
   if(preset.startsWith("st:"))SS.add(preset.slice(3));else FS.add(preset);
  }
  syncChips();filt();
 }
 window.scrollTo({top:0});
}
/* ---- detalle bajo demanda ---- */
function fitbar(id){
 const w=document.createElement("div");w.className="fitbar";
 const lab=document.createElement("span");lab.textContent="tu encaje:";w.appendChild(lab);
 for(let n=1;n<=5;n++){const b=document.createElement("button");b.textContent=n;
  b.onclick=ev=>{ev.stopPropagation();setFit(id,n)};b.dataset.n=n;w.appendChild(b)}
 const q=document.createElement("button");q.textContent="×";q.title="quitar tu encaje";
 q.onclick=ev=>{ev.stopPropagation();setFit(id,null)};w.appendChild(q);
 const r=document.createElement("span");r.className="rref";w.appendChild(r);
 return w;
}
function dfill(el){
 if(!el||el.firstChild||!el.dataset.d)return;
 const id=el.dataset.id;
 if(id){
  if(!el.closest(".card")){
   const sb=document.createElement("div");sb.className="states";sb.dataset.id=id;
   for(const k in SLBL){const b=document.createElement("button");b.className="sb";
    b.dataset.s=k;b.textContent=SLBL[k];
    b.onclick=ev=>setState(id,k,ev);sb.appendChild(b)}
   el.appendChild(sb);
  }
  el.appendChild(fitbar(id));
 }
 const t=document.createElement("table");t.className="full";
 for(const [k,v] of (DET[el.dataset.d]||[])){
  const tr=t.insertRow(), th=document.createElement("th"), td=tr.insertCell();
  th.textContent=k; tr.insertBefore(th,td);
  if(/^https?:\/\//.test(v)){const a=document.createElement("a");
   a.href=v;a.target="_blank";a.rel="noopener";a.textContent=v.length>60?"abrir ↗":v;
   a.onclick=ev=>ev.stopPropagation();td.appendChild(a);}
  else td.textContent=v;
 }
 el.appendChild(t);
 if(id)paint();
}
function opencard(b){const c=b.closest(".card");dfill(c.querySelector(".detail"));c.classList.toggle("open")}
function openrow(tr){const d=tr.nextElementSibling;
 dfill(d.tagName==="TR"?d.querySelector("td"):d);d.classList.toggle("open")}

/* ---- orden ---- */
function sortT(th){
 const t=th.closest("table"),tb=t.tBodies[0];
 const i=[...th.parentNode.children].indexOf(th);
 const dir=th.dataset.dir==="a"?"d":"a";
 t.querySelectorAll("th").forEach(h=>{delete h.dataset.dir});
 th.dataset.dir=dir;
 const rows=[...tb.rows],pairs=[];
 for(let j=0;j<rows.length;j+=2)pairs.push([rows[j],rows[j+1]]);
 const key=p=>{const c=p[0].cells[i];const s=c.dataset.s!==undefined?c.dataset.s:c.textContent.trim();
  const n=parseFloat(s);return isNaN(n)?String(s).toLowerCase():n};
 pairs.sort((a,b)=>{const x=key(a),y=key(b);
  const c=(typeof x==="number"&&typeof y==="number")?x-y:String(x).localeCompare(String(y));
  return dir==="a"?c:-c});
 pairs.forEach(p=>{tb.appendChild(p[0]);tb.appendChild(p[1])});
}

/* ---- estado del founder ---- */
function eff(id,base){const o=STATE[id]||{};return o.f||+base||0}
function setState(id,s,ev){
 if(ev)ev.stopPropagation();
 const o=STATE[id]||{};
 if(o.s===s){delete o.s}else{o.s=s}
 o.t=new Date().toISOString();
 if(!o.s&&!o.f){delete STATE[id]}else{STATE[id]=o}
 DIRTY=true;paint();msg("cambiado");if(tok())sync();
}
function quick(id,s,ev){setState(id,s,ev)}
function subMark(id,v,ev){
 /* Tu marca SIEMPRE gana sobre la columna del TSV, incluido devolver a
    pendiente: ocho filas venian marcadas DONE por la rutina y sin esto no
    habia forma de decir «yo no estoy suscrito a eso». */
 if(ev)ev.stopPropagation();
 const el=document.querySelector('.subi[data-id="'+id+'"]');
 const cur=el?el.dataset.sub:"TODO";
 const o=STATE[id]||{};
 o.s=(cur===v)?"TODO":v;
 o.t=new Date().toISOString();
 STATE[id]=o;
 DIRTY=true;paint();msg("cambiado");if(tok())sync();
}
function setFit(id,n){
 const o=STATE[id]||{};
 if(n===null||o.f===n){delete o.f}else{o.f=n}
 o.t=new Date().toISOString();
 if(!o.s&&!o.f){delete STATE[id]}else{STATE[id]=o}
 DIRTY=true;paint();msg("cambiado");if(tok())sync();
}
function paint(){
 document.querySelectorAll(".card").forEach(c=>{
  const id=c.dataset.id,o=STATE[id]||{};
  c.dataset.state=o.s||"NEW";
  c.querySelectorAll(".states button").forEach(b=>b.classList.toggle("on",b.dataset.s===(o.s||"NEW")));
  const fb=c.querySelector('.b[data-fitb]');
  if(fb){const ef=eff(id,c.dataset.fit);
   fb.textContent="fit "+ef+(o.f?" ·tuyo":"");fb.dataset.fitb=ef}
 });
 document.querySelectorAll("tr.oprow").forEach(r=>{
  const id=r.dataset.id,o=STATE[id]||{};
  r.dataset.state=o.s||"NEW";
  const l=r.querySelector(".stlbl");if(l)l.textContent=SLBL[o.s||"NEW"];
  const fc=r.querySelector(".fitc");
  if(fc){const ef=eff(id,r.dataset.fit);fc.dataset.s=ef;
   fc.innerHTML=ef+(o.f?"<i>tú</i>":"")}
 });
 document.querySelectorAll(".urow").forEach(u=>{
  const o=STATE[u.dataset.id]||{};u.dataset.state=o.s||"NEW"});
 document.querySelectorAll(".fitbar").forEach(w=>{
  const id=w.parentElement.dataset.id,o=STATE[id]||{};
  w.querySelectorAll("button[data-n]").forEach(b=>b.classList.toggle("on",o.f===+b.dataset.n));
 });
 document.querySelectorAll(".subi").forEach(d=>{
  const o=STATE[d.dataset.id]||{};
  const s=o.s||d.dataset.tsv||"TODO";
  d.dataset.sub=s;
  d.querySelector(".sbtn.ok").classList.toggle("on",s==="DONE");
  d.querySelector(".sbtn.no").classList.toggle("on",s==="SKIP");
  d.querySelector(".sst").textContent=s==="DONE"?"suscrito":(s==="SKIP"?"descartada":"pendiente");
 });
 const sp=document.querySelectorAll('.subi:not([data-sub="DONE"]):not([data-sub="SKIP"])').length;
 const sc=document.getElementById("subcnt"),st2=document.querySelector("#t-subs b");
 if(sc)sc.textContent=sp;if(st2)st2.textContent=sp;
 let unseen=0,prog=0;
 document.querySelectorAll("#optable tr.oprow").forEach(r=>{
  const s=(STATE[r.dataset.id]||{}).s||"NEW";
  if(s==="NEW")unseen++;if(s==="IN_PROGRESS")prog++;
 });
 const tu=document.querySelector("#t-unseen b"),tp=document.querySelector("#t-prog b");
 if(tu)tu.textContent=unseen;if(tp)tp.textContent=prog;
 filt();
}

/* ---- filtros ---- */
function syncChips(){
 document.querySelectorAll("#tchips .chip").forEach(c=>
  c.classList.toggle("on",c.dataset.t==="all"?TS.size===0:TS.has(c.dataset.t)));
 document.querySelectorAll("#fchips .chip").forEach(c=>{
  const f=c.dataset.f;
  c.classList.toggle("on",f==="all"?(FS.size===0&&SS.size===0):
   (f.startsWith("st:")?SS.has(f.slice(3)):FS.has(f)));
 });
}
function tchip(el){
 const t=el.dataset.t;
 if(t==="all"){TS.clear()}else{TS.has(t)?TS.delete(t):TS.add(t)}
 syncChips();filt();
}
function chip(el){
 const f=el.dataset.f;
 if(f==="all"){FS.clear();SS.clear()}
 else if(f.startsWith("st:")){const s=f.slice(3);SS.has(s)?SS.delete(s):SS.add(s)}
 else{FS.has(f)?FS.delete(f):FS.add(f)}
 syncChips();filt();
}
function tmatch(tab){
 if(TS.size===0)return true;
 for(const t of TS){if(tab===t)return true}
 return false;
}
function pass(d,q){
 const id=d.dataset.id,s=d.dataset.state||"NEW";
 if(q&&!d.dataset.text.includes(q))return false;
 if(FS.has("fresh")&&d.dataset.fresh!=="1")return false;
 if(FS.has("act")&&d.dataset.act!=="1")return false;
 if(FS.has("fit4")&&eff(id,d.dataset.fit)<4)return false;
 if(FS.has("low")&&d.dataset.comp!=="LOW")return false;
 if(FS.has("soon")){const c=d.querySelector("td.dlc");
  const v=c?+c.dataset.s:+(d.dataset.dl||99999);if(!(v>=0&&v<=45))return false}
 if(SS.size&&!SS.has(s))return false;
 if(SS.size===0&&s==="DISCARDED")return false;
 return true;
}
function filt(){
 const q=document.getElementById("q").value.toLowerCase().trim();
 document.querySelectorAll("#v-novedades .card").forEach(c=>{
  c.classList.toggle("hide",!( (!q||c.dataset.text.includes(q)) ));
 });
 document.querySelectorAll("#optable tr.oprow").forEach(r=>{
  const ok=pass(r,q)&&tmatch(r.dataset.tab||"");
  r.classList.toggle("hide",!ok);
  if(!ok)r.nextElementSibling.classList.remove("open");
 });
 document.querySelectorAll("#wtable tr.oprow").forEach(r=>{
  const ok=(!q||r.dataset.text.includes(q));
  r.classList.toggle("hide",!ok);
  if(!ok)r.nextElementSibling.classList.remove("open");
 });
 document.querySelectorAll(".subi").forEach(d=>{
  d.classList.toggle("hide",!!q&&!d.dataset.text.includes(q));
 });
 document.querySelectorAll("#v-sistema tr.grow").forEach(t=>{
  const ok=!q||t.dataset.text.includes(q);
  t.classList.toggle("hide",!ok);
  if(!ok)t.nextElementSibling.classList.remove("open");
 });
 const n=document.querySelectorAll("#optable tr.oprow:not(.hide)").length;
 const res=document.getElementById("nres");
 if(res)res.textContent=n+" oportunidades en pantalla";
}
let qt;document.getElementById("q").addEventListener("input",()=>{
 clearTimeout(qt);qt=setTimeout(()=>{
  if(V==="resumen"&&document.getElementById("q").value.trim())go("todo");
  filt();
 },140);
});

/* ---- informes ---- */
function openrun(slug){
 const r=RUNS[slug];if(!r||!r.html)return;
 document.getElementById("mtitle").textContent=r.name+" — "+(r.date||"");
 document.getElementById("mbody").innerHTML=r.html;
 document.getElementById("mod").classList.add("on");
}
function closerun(ev){if(!ev||ev.target.id==="mod"||ev.target.id==="mclose")
 document.getElementById("mod").classList.remove("on")}
document.addEventListener("keydown",ev=>{if(ev.key==="Escape")closerun()});

/* ---- sincronizacion con GitHub ---- */
function setToken(){const t=prompt("Pega un token de GitHub con permiso de escritura en "+REPO+
 ".\nSe guarda solo en este navegador.");if(t){localStorage.setItem("gh_token",t.trim());load();}}
function msg(t){document.getElementById("msg").textContent="estado: "+t+(DIRTY?" · sin guardar":"")}
async function load(){
 try{const h={Accept:"application/vnd.github+json"};if(tok())h.Authorization="Bearer "+tok();
  const r=await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE}`,{headers:h});
  if(r.ok){const j=await r.json();SHA=j.sha;
   STATE=JSON.parse(decodeURIComponent(escape(atob(j.content.replace(/\n/g,"")))));msg("cargado")}
  else if(r.status===404){STATE={};msg("sin estado previo")}
  else msg("no se pudo leer ("+r.status+")");
 }catch(e){msg("sin conexion, local")}
 paint();
}
async function sync(){
 if(!tok()){msg("conecta GitHub para guardar");return}
 const body=btoa(unescape(encodeURIComponent(JSON.stringify(STATE,null,1))));
 const r=await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE}`,{
  method:"PUT",headers:{Authorization:"Bearer "+tok(),Accept:"application/vnd.github+json"},
  body:JSON.stringify({message:"estado: actualizado desde la pagina",content:body,sha:SHA||undefined})});
 if(r.ok){const j=await r.json();SHA=j.content.sha;DIRTY=false;msg("guardado")}
 else msg("error al guardar ("+r.status+")");
}

/* ---- buzon de fuentes ---- */
const SRCFILE="data/source_inbox.json";
const KNOWN=new Set(JSON.parse(document.getElementById("srcstore").textContent));
let SRCJ=[],SRCSHA=null;
function renderSrc(){
 const el=document.getElementById("srcpend");if(!el)return;
 const p=SRCJ.filter(x=>x.status==="PENDING");
 el.innerHTML=p.length?("en cola para la proxima pasada: "+
  p.map(x=>'<span class="pu">'+x.url.replace(/^https?:\/\/(www\.)?/,"").slice(0,42)+"</span>").join("")):"";
}
async function loadSrc(){
 try{const h={Accept:"application/vnd.github+json"};if(tok())h.Authorization="Bearer "+tok();
  const r=await fetch(`https://api.github.com/repos/${REPO}/contents/${SRCFILE}`,{headers:h});
  if(r.ok){const j=await r.json();SRCSHA=j.sha;
   SRCJ=JSON.parse(decodeURIComponent(escape(atob(j.content.replace(/\n/g,"")))))||[];}
  else if(r.status===404){SRCJ=[];SRCSHA=null}
 }catch(e){}
 renderSrc();
}
async function addSrc(){
 const inp=document.getElementById("srcurl"),u=inp.value.trim().replace(/\/$/,"");
 if(!/^https?:\/\//.test(u)){msg("pega una URL completa (https://…)");return}
 if(!tok()){msg("conecta GitHub para proponer fuentes");setToken();return}
 if(KNOWN.has(u.toLowerCase())){msg("esa fuente ya esta en sources");inp.value="";return}
 await loadSrc();
 if(SRCJ.some(x=>(x.url||"").replace(/\/$/,"").toLowerCase()===u.toLowerCase())){
  msg("ya estaba propuesta");inp.value="";return}
 SRCJ.push({url:u,added:new Date().toISOString().slice(0,10),status:"PENDING"});
 const body=btoa(unescape(encodeURIComponent(JSON.stringify(SRCJ,null,1))));
 const r=await fetch(`https://api.github.com/repos/${REPO}/contents/${SRCFILE}`,{
  method:"PUT",headers:{Authorization:"Bearer "+tok(),Accept:"application/vnd.github+json"},
  body:JSON.stringify({message:"fuente propuesta desde la pagina",content:body,sha:SRCSHA||undefined})});
 if(r.ok){const j=await r.json();SRCSHA=j.content.sha;inp.value="";
  msg("fuente en cola: la proxima pasada la completara");renderSrc()}
 else msg("no se pudo proponer ("+r.status+")");
}
load();loadSrc();
'''.replace('__REPO__', REPO)

# ---------------------------------------------------------------- pagina

HTML = f'''<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Radar · investigacion</title>
<style>{CSS}</style></head><body>
<div id="top"><div class="tline">
 <h1>Radar <i>· investigacion</i></h1>
 <span id="upd" data-iso="{e(LAST_ISO)}">datos del {RUNDATE}</span>
 <input id="q" placeholder="Buscar en todo…">
 <button id="thm" onclick="themeToggle()" title="tema claro / oscuro">☾</button>
</div>
<div id="tabs">{tabbar}</div></div>
<div class="wrap">
<section class="view on" id="v-resumen">{v_resumen}
<footer>Rutinas: lunes 00:01 posiciones · 04:00 fellowships · 08:00 ecosistema (Madrid).
La pagina la genera el CI desde <code>data/*.tsv</code>; tus estados y tu encaje viven en
<code>owner_status.json</code> y las rutinas no lo tocan · <a href="research.xlsx">descargar Excel</a></footer>
</section>
<section class="view" id="v-novedades">
<p class="sub">Lo tocado por las rutinas en los ultimos siete dias, mejor encaje primero.</p>
{v_fresh}</section>
<section class="view" id="v-todo">{v_todo}</section>
<section class="view" id="v-vigilando">{v_watch}</section>
<section class="view" id="v-suscripciones">{v_subs}</section>\n<section class="view" id="v-sistema">{v_sistema}</section>
</div>
<div id="mod" onclick="closerun(event)"><div id="mbox">
 <button id="mclose" onclick="closerun(event)">✕</button>
 <h3 id="mtitle" class="serif"></h3><div id="mbody"></div></div></div>
<script id="dstore" type="application/json">{dstore}</script>
<script id="runstore" type="application/json">{runsjson}</script>
<script id="srcstore" type="application/json">{srcjson}</script>
<div id="bar"><span id="msg">estado: local</span>
 <button onclick="setToken()">conectar con GitHub</button>
 <button onclick="sync()">guardar</button></div>
<script>{JS}</script></body></html>'''

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(HTML)
print(f'{OUT}  {os.path.getsize(OUT)} bytes · novedades {len(fresh)} · urgentes {len(urgent)} · '
      f'oportunidades {len(opps)} · vigilando {len(watch)}')
