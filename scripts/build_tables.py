#!/usr/bin/env python3
"""Pre-render: genera tablas de la matriz experimental y el estado actual desde CSV.

Solo biblioteca estándar. No inventa datos: si los CSV están vacíos, lo indica.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "thesis/experiments/matrix.csv"
REGISTRY = ROOT / "thesis/models/registry.csv"
OUT = ROOT / "thesis/experiments/_generated"

STATUSES = {"planned", "pilot", "running", "completed", "replicated", "archived"}
COLS = ["experiment", "model", "stimulus", "n", "temperature", "seed", "metric", "status"]
HEAD = ["Experimento", "Modelo", "Estímulo", "N", "Temperatura", "Seed", "Métrica", "Estado"]


def read(path):
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]


def esc(s):
    return (s or "").replace("|", "\\|").strip()


def main():
    rows = read(MATRIX)
    errors = []
    for i, r in enumerate(rows, start=2):
        if r.get("status", "").strip() not in STATUSES:
            errors.append(f"matrix.csv línea {i}: estado inválido {r.get('status')!r}; permitidos: {sorted(STATUSES)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)

    OUT.mkdir(parents=True, exist_ok=True)

    if rows:
        lines = ["| " + " | ".join(HEAD) + " |", "|---|---|---|---:|---:|---|---|---|"]
        for r in rows:
            lines.append("| " + " | ".join(esc(r.get(c)) for c in COLS) + " |")
        matrix_md = "\n".join(lines) + "\n"
    else:
        matrix_md = "*No hay experimentos registrados todavía.* Agregar filas en `thesis/experiments/matrix.csv`.\n"
    (OUT / "matrix.md").write_text(matrix_md, encoding="utf-8")

    models = read(REGISTRY)
    experiments = sorted({r["experiment"].strip() for r in rows if r.get("experiment", "").strip()})
    active = sorted({r["experiment"].strip() for r in rows if r.get("status", "").strip() in {"pilot", "running"}})
    last = experiments[-1] if experiments else None

    st = []
    st.append(f"- **Experimentos registrados:** {len(experiments)}")
    st.append(f"- **Experimentos activos (pilot/running):** {len(active)}")
    st.append(f"- **Último experimento:** {last if last else 'ninguno registrado'}")
    if models:
        names = ", ".join(f"[{m['family']} {m['size']}](thesis/models/{m['page']})" for m in models)
        st.append(f"- **Modelos contemplados:** {names}")
    else:
        st.append("- **Modelos contemplados:** ninguno registrado")
    (OUT / "status.md").write_text("\n".join(st) + "\n", encoding="utf-8")
    print(f"build_tables: {len(rows)} filas de matriz, {len(models)} modelos")


if __name__ == "__main__":
    main()
