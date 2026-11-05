# Entorno

Directorio reservado para archivos de entorno, **solo cuando sean necesarios** y con justificación:

- `requirements.txt` / `environment.yml` (Python)
- `renv.lock` (R)
- `Dockerfile`

Hoy el sitio no requiere dependencias de Python más allá de la biblioteca estándar (`scripts/build_tables.py`, `scripts/check_links.py`).

Registrar versiones relevantes de cada experimento (runtime, commit de `llama.cpp`, versión del modelo) en su `protocol.yml`, no aquí.
