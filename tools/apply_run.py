#!/usr/bin/env python3
"""Aplica los JSON de las ramas de una pasada sobre los TSV de data/.

Uso: python3 tools/apply_run.py <run_date> <routine> <branch1.json> [...]

No escribe nunca Owner_Status (apply_rows.py lo rechaza), respeta el tope de
2 suscripciones por pasada, deduplica sources por URL+query y escribe siempre
de forma atomica a traves de apply_rows.write().
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply_rows as ar

MAX_SUBS = 2


def clean(value):
    """Un TSV no soporta tabuladores ni saltos de linea dentro de un valor."""
    if value is None:
        return ""
    return " ".join(str(value).replace("\t", " ").split())


def clean_row(row, drop=("ID", "Owner_Status")):
    return {k: clean(v) for k, v in row.items() if k not in drop}


def main():
    run_date, routine = sys.argv[1], sys.argv[2]
    payloads = []
    for path in sys.argv[3:]:
        if not os.path.exists(path):
            print("AVISO: falta %s, la rama no entrego nada" % path)
            continue
        with open(path, encoding="utf-8") as fh:
            payloads.append((os.path.basename(path), json.load(fh)))

    changelog = []

    # --- fellowships y watchlist_closed: pestañas propias -------------------
    for tab, prefix in (("fellowships", "F"), ("watchlist_closed", "W")):
        new_rows, updates = [], {}
        for _, p in payloads:
            for r in p.get("new_" + ("fellowships" if tab == "fellowships"
                                     else "watchlist"), []) or []:
                new_rows.append(clean_row(r))
            for rid, changes in (p.get("updates_" + ("fellowships"
                                                     if tab == "fellowships"
                                                     else "watchlist")) or {}).items():
                updates.setdefault(rid, {}).update(clean_row(changes))
        if not new_rows and not updates:
            print("%-18s sin cambios" % tab)
            continue
        added, touched = ar.apply(tab, new_rows, updates, prefix)
        for rid, r in zip(added, new_rows):
            changelog.append({
                "Run_Date": run_date, "Routine": routine, "Tab": tab, "ID": rid,
                "Name": r.get("Name", ""), "Change_Type": "NEW",
                "Details": clean(r.get("Fit_Rationale") or r.get("Why_It_Matters") or "")[:300],
                "URL": r.get("URL", "")})
        _, rows_after = ar.read(os.path.join(ar.DATA, tab + ".tsv"))
        by_id = {r["ID"]: r for r in rows_after}
        for rid in touched:
            changelog.append({
                "Run_Date": run_date, "Routine": routine, "Tab": tab, "ID": rid,
                "Name": by_id.get(rid, {}).get("Name", ""), "Change_Type": "UPDATED",
                "Details": "columnas: " + ", ".join(sorted(updates[rid])),
                "URL": by_id.get(rid, {}).get("URL", "")})

    # --- sources: compartido, solo apendice, dedup por URL + query ----------
    _, src_rows = ar.read(os.path.join(ar.DATA, "sources.tsv"))
    seen = {(r.get("URL", "").strip(), r.get("Query_or_Filter", "").strip())
            for r in src_rows}
    gen = ar.next_id(src_rows, "SRC")
    new_src = []
    for _, p in payloads:
        for r in p.get("new_sources", []) or []:
            r = clean_row(r)
            key = (r.get("URL", "").strip(), r.get("Query_or_Filter", "").strip())
            if not key[0] or key in seen:
                continue
            seen.add(key)
            r["ID"] = next(gen)
            r.setdefault("Last_Checked", run_date)
            new_src.append(r)
    if new_src:
        ar.append_plain("sources", new_src)

    # --- subscriptions: compartido, tope de 2 por pasada, dedup por URL -----
    _, sub_rows = ar.read(os.path.join(ar.DATA, "subscriptions.tsv"))
    sub_seen = {r.get("URL_to_subscribe", "").strip() for r in sub_rows}
    gen = ar.next_id(sub_rows, "SUB")
    new_sub = []
    for _, p in payloads:
        for r in p.get("new_subscriptions", []) or []:
            if len(new_sub) >= MAX_SUBS:
                break
            r = clean_row(r)
            url = r.get("URL_to_subscribe", "").strip()
            if not url or url in sub_seen:
                continue
            sub_seen.add(url)
            r["ID"] = next(gen)
            r.setdefault("What_it_delivers", r.get("Why_it_matters", ""))
            r["Status"] = "TODO"          # nunca se siembra en DONE
            r["Added_On"] = run_date
            new_sub.append(r)
    if new_sub:
        ar.append_plain("subscriptions", new_sub)

    # --- changelog: compartido, solo apendice -------------------------------
    if changelog:
        ar.append_plain("changelog", changelog)

    print("\nsources nuevas: %s" % [r["ID"] for r in new_src])
    print("subscripciones nuevas: %s" % [r["ID"] for r in new_sub])
    print("apuntes de changelog: %d" % len(changelog))


if __name__ == "__main__":
    main()
