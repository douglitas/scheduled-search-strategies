#!/usr/bin/env python3
"""Reconstruye SOLO las filas de action_now de las pestañas de una rutina.

Preserva intactas las filas de las otras rutinas y renumera Rank de 1 a N.

Regla de seleccion (la misma, palabra por palabra, en los tres prompts de
prompts/out/): Fit 4-5 que cierren dentro de 90 dias, mas lo sin plazo con
Fit 5 (grupos y convocatorias rodantes), mas cualquier fila con
Competition_Level = LOW y Fit >= 3. Se excluye lo que la dueña haya marcado
DISCARDED, APPLIED o RESOLVED. Orden: urgencia, luego fit.

Uso: python3 tools/rebuild_action_now.py <run_date YYYY-MM-DD> [routine]
     routine = positions (por omision) | fellowships | ecosystem
"""

import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply_rows as ar

# (pestañas propias, ficheros de origen, mis filas van primero)
#
# El ultimo campo existe por el diff, no por gusto: positions corre primero y
# encabeza la lista; fellowships y ecosistema añaden las suyas detras. Asi las
# filas de las otras rutinas conservan su Rank y salen del diff byte a byte
# iguales. Si las tres pidiesen el puesto 1, cada pasada reescribiria el
# fichero entero. (Leccion heredada del tracker de funding.)
BEATS = {
    "positions": (
        {"Postdocs", "Jobs"},
        [("postdocs", "Postdocs"), ("jobs", "Jobs")],
        True,
    ),
    "fellowships": (
        {"Fellowships", "Watchlist_Closed"},
        [("fellowships", "Fellowships")],
        False,
    ),
    "ecosystem": (
        {"Groups", "Events", "Training"},
        [("groups", "Groups"), ("events", "Events"), ("training", "Training")],
        False,
    ),
}
EXCLUDE = {"DISCARDED", "APPLIED", "RESOLVED"}
DATE = re.compile(r"(20\d\d)-(\d\d)-(\d\d)")


def first_date(text):
    m = DATE.search(text or "")
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def main():
    run_date = sys.argv[1]
    routine = sys.argv[2] if len(sys.argv) > 2 else "positions"
    if routine not in BEATS:
        sys.exit("rutina desconocida: %s (opciones: %s)"
                 % (routine, ", ".join(sorted(BEATS))))
    mine, sources, mine_first = BEATS[routine]
    today = dt.date(*[int(x) for x in run_date.split("-")])
    horizon = today + dt.timedelta(days=90)

    with open(os.path.join(ar.DATA, "owner_status.json"), encoding="utf-8") as fh:
        marks = {k: (v or {}).get("s", "") for k, v in json.load(fh).items()}

    picked = []
    for fname, tab in sources:
        _, rows = ar.read(os.path.join(ar.DATA, fname + ".tsv"))
        for r in rows:
            rid = (r.get("ID") or "").strip()
            if marks.get(rid, "") in EXCLUDE:
                continue
            if (r.get("Status") or "").strip().upper() == "CLOSED":
                continue
            if (r.get("Change_Flag") or "").strip().upper() == "CLOSED":
                continue
            # un evento o curso ya empezado no puede seguir en action_now
            # aunque su Fit sea 5 y no tenga plazo de inscripcion
            start = first_date(r.get("Start_Date"))
            if start and start < today:
                continue
            try:
                fit = int(float(r.get("Fit_1_5") or 0))
            except ValueError:
                continue
            dl = first_date(r.get("Deadline") or r.get("Start_Date"))
            comp = (r.get("Competition_Level") or "").strip().upper()

            keep = False
            if fit >= 4 and dl and today <= dl <= horizon:
                keep = True
            elif fit == 5 and not dl:
                # grupos sin convocatoria y llamadas rodantes: solo los 5
                keep = True
            elif comp == "LOW" and fit >= 3:
                keep = True
            if not keep:
                continue

            picked.append({
                "ID": rid,
                "Name": r.get("Name", ""),
                "Tab": tab,
                "Type": (r.get("Sub_Type") or r.get("Type")
                         or r.get("Contract_Type") or r.get("Sector", "")),
                "Deadline": r.get("Deadline", ""),
                "Days_Left": str((dl - today).days) if dl else "",
                "Amount_EUR": (r.get("Amount_EUR") or r.get("Salary_EUR_Year")
                               or r.get("Cost_EUR", "")),
                "Fit_1_5": str(fit),
                "Effort_Estimate": r.get("Effort_Estimate", ""),
                "Next_Action": r.get("Next_Action", ""),
                "URL": r.get("URL", ""),
                "_d": dl,
            })

    # urgencia primero (fechado, ascendente), luego los sin fecha por fit
    picked.sort(key=lambda x: (x["_d"] is None, x["_d"] or today, -int(x["Fit_1_5"])))
    for p in picked:
        p.pop("_d")

    path = os.path.join(ar.DATA, "action_now.tsv")
    header, rows = ar.read(path)
    before = len(rows)
    others = [r for r in rows if (r.get("Tab") or "").strip() not in mine]
    dropped = before - len(others)

    # Mi bloque se reinserta DONDE YA ESTABA, no al final: devolverlo al final
    # moveria las filas de otra rutina y el diff — del que la pagina construye
    # «Novedades de la semana» — las daria por modificadas sin que su contenido
    # hubiera cambiado. mine_first solo decide donde ir la primera vez.
    at = next((i for i, r in enumerate(rows)
               if (r.get("Tab") or "").strip() in mine), None)
    if at is None:
        at = 0 if mine_first else len(others)
    out = others[:at] + picked + others[at:]
    for i, r in enumerate(out, 1):
        r["Rank"] = str(i)

    ar.write(path, header, out)
    _, rows2 = ar.read(path)
    assert len(rows2) == len(out), "action_now: recuento inesperado"
    kept_ids = {r["ID"] for r in picked}
    print("action_now: %d filas -> %d | mias %d (antes %d) | ajenas preservadas %d"
          % (before, len(rows2), len(picked), dropped, len(others)))
    print("mis ids:", " ".join(sorted(kept_ids)))


if __name__ == "__main__":
    main()
