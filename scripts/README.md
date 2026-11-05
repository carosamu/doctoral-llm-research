# Scripts

- `build_tables.py` — pre-render de Quarto. Lee `thesis/experiments/matrix.csv` y `thesis/models/registry.csv` y genera `thesis/experiments/_generated/{matrix,status}.md`. Solo biblioteca estándar. Valida los estados permitidos.
- `check_links.py` — revisa enlaces internos de `_site/` (`python3 scripts/check_links.py _site`).

Código estable y reutilizable de análisis debe vivir aquí (o en `src/` cuando el proyecto crezca); los notebooks son para exploración.
