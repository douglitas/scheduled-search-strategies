#!/usr/bin/env python3
"""Aplica altas y modificaciones sobre un TSV de data/ de forma atomica.

Uso: se importa desde un script de pasada. Nunca reescribe cabeceras ni
columnas que no se le indiquen, y jamas toca Owner_Status.

Escribe siempre a un temporal y hace os.replace, de modo que un fallo a
mitad deja el fichero antiguo intacto en vez de truncado.
"""

import csv
import os
import sys
import tempfile

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

# Columna que pertenece al fundador y que ninguna pasada puede escribir.
PROTECTED = {"Owner_Status"}


def read(path):
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    with open(path, newline="", encoding="utf-8") as fh:
        header = next(csv.reader(fh, delimiter="\t"))
    return header, rows


def write(path, header, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path) or ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=header, delimiter="\t",
                               lineterminator="\n", extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow({k: r.get(k, "") for k in header})
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def next_id(rows, prefix, width=4):
    n = 0
    for r in rows:
        rid = (r.get("ID") or "").strip()
        if rid.startswith(prefix + "-"):
            tail = rid[len(prefix) + 1:]
            if tail.isdigit():
                n = max(n, int(tail))
    while True:
        n += 1
        yield "%s-%0*d" % (prefix, width, n)


def apply(name, new_rows, updates, prefix, defaults=None):
    """new_rows: lista de dicts sin ID. updates: {ID: {col: valor}}."""
    path = os.path.join(DATA, name + ".tsv")
    header, rows = read(path)
    before = len(rows)

    unknown = set()
    for r in list(new_rows) + list(updates.values()):
        unknown |= {k for k in r if k not in header}
    if unknown:
        sys.exit("columnas desconocidas en %s: %s" % (name, sorted(unknown)))

    index = {(r.get("ID") or "").strip(): r for r in rows}
    touched = []
    for rid, changes in updates.items():
        if rid not in index:
            sys.exit("ID inexistente en %s: %s" % (name, rid))
        for col, val in changes.items():
            if col in PROTECTED:
                sys.exit("intento de escribir %s en %s" % (col, rid))
            index[rid][col] = val
        touched.append(rid)

    gen = next_id(rows, prefix)
    added = []
    for r in new_rows:
        row = dict(defaults or {})
        row.update(r)
        row["ID"] = next(gen)
        rows.append(row)
        added.append(row["ID"])

    write(path, header, rows)

    header2, rows2 = read(path)
    assert header2 == header, "cabecera alterada en " + name
    expected = before + len(new_rows)
    assert len(rows2) == expected, (
        "%s: esperaba %d filas, hay %d" % (name, expected, len(rows2)))
    print("%-18s %3d -> %3d filas | %d altas %s | %d modificadas %s"
          % (name, before, len(rows2), len(added), added, len(touched), touched))
    return added, touched


def append_plain(name, new_rows):
    """Para los ficheros compartidos, que son de solo apendice."""
    path = os.path.join(DATA, name + ".tsv")
    header, rows = read(path)
    before = len(rows)
    unknown = set()
    for r in new_rows:
        unknown |= {k for k in r if k not in header}
    if unknown:
        sys.exit("columnas desconocidas en %s: %s" % (name, sorted(unknown)))
    rows.extend(new_rows)
    write(path, header, rows)
    _, rows2 = read(path)
    assert len(rows2) == before + len(new_rows), name + ": recuento inesperado"
    print("%-18s %3d -> %3d filas | %d apuntes" % (name, before, len(rows2), len(new_rows)))
