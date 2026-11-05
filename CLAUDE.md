# CLAUDE.md — Guía para sesiones de Claude Code

## Qué es este repositorio
Repositorio académico y laboratorio reproducible del **Doctorado en Ciencia de Datos e Inteligencia Artificial (Universidad El Bosque)** de Claudio de la Rosa, y archivo principal de su tesis:
*Embedded Intelligence: Inheritance and Resurgence Across Large Language Models* (título provisional).
Se publica como sitio **Quarto + GitHub Pages** (`main` = trabajo, `gh-pages` = generado).
Propietario GitHub: `carosamu`. Repo: `doctoral-llm-research`. Idioma del sitio: español; nombres técnicos de carpeta en inglés `kebab-case`.

## Postura científica (innegociable)
- *Inheritance*, *Resurgence* y *Embedded Intelligence* son **constructos de trabajo**, nunca fenómenos demostrados.
- Lema: *los datos muestran patrones; nosotros proponemos interpretaciones*.
- Mantener el tono basado en evidencia, estadístico, probabilístico, experimental, sin afirmaciones extraordinarias sobre LLM.
- **Separar siempre observación de interpretación.** Etiquetar: resultado exploratorio / replicado / evidencia estadística / interpretación / hipótesis / pregunta abierta.
- Comparar con explicaciones alternativas (memorization, probabilidad condicional local, asociación distribucional, generalization, retrieval, decoding artifacts, autoregressive degeneration).

## Prohibiciones
- **No inventar** resultados, métricas, materias, profesores, publicaciones, DOI, fechas ni referencias.
- **No eliminar** datos experimentales, `runs/`, versiones de la propuesta ni resultados negativos (mover a `thesis/archive/` con nota).
- No presentar funciones de asesores como aprobadas sin confirmación institucional (ver `about.qmd`).
- No subir modelos, corpus restringidos, datos privados/personales/médicos ni credenciales.
- No modificar notebooks científicos existentes sin necesidad. No editar figuras a mano.
- No agregar dependencias sin justificación. Sin lorem ipsum.

## Arquitectura
- `doctorate/` — formación doctoral (semestres, cursos solo si están confirmados, talleres, notas, lecturas, hitos).
- `thesis/` — laboratorio y archivo de la tesis:
  - `experiments/<línea>/exp-YYYY-NNN-short-name/` con plantilla en `experiments/_template/`; líneas: `exploratory, controlled, directional-probability, variability, surprisal, anomaly-probes, cross-model`.
  - `experiments/matrix.csv` = **Experimental Matrix** (manual). `models/registry.csv` = modelos contemplados.
  - `models/{pythia,gemma,qwen,custom-model}`, `corpora/`, `stimuli/`, `analysis/`, `results/{exploratory,validated,negative-results,figures,tables}`, `protocols/`, `decisions/`, `manuscripts/`, `archive/`.
- `publications/`, `presentations/`, `environment/`, `scripts/`.
- Archivos/carpetas que empiezan con `_` no se renderizan (p. ej. `_template`, `_generated`).
- `thesis/experiments/_generated/` lo escribe `scripts/build_tables.py` (pre-render); no editar a mano. **Se versiona**, porque Quarto resuelve los `include` antes del pre-render: tras editar `matrix.csv` o `registry.csv`, ejecutar `python3 scripts/build_tables.py` (o `quarto render` dos veces) y commitear los cambios.

## Reglas para nuevos experimentos
1. Copiar `thesis/experiments/_template/` a `thesis/experiments/<línea>/exp-YYYY-NNN-short-name/`.
2. Completar `README.md` y `protocol.yml` **antes** de ejecutar; registrar el análisis previsto de antemano.
3. Estado: `planned | pilot | running | completed | replicated | archived`. Reflejarlo en `matrix.csv`.
4. Conservar **todos** los parámetros: runtime (+commit), modelo (+versión, cuantización, SHA-256, fuente), prompt, seed, temperature, top-k, top-p, min-p, repeat-penalty, context-size, batch-size, ubatch-size, token-limit, device, timestamp, output. Cada experimento debe poder reconstruirse.
5. Las comparaciones entre modelos son *cross-model behavioral comparisons under matched inference conditions*, no réplicas idénticas; los modelos no son arquitectónicamente equivalentes.
6. Registrar decisiones metodológicas en `thesis/decisions/decision-log.qmd` (append-only).
7. Guardar resultados nulos en `thesis/results/negative-results/`.

## Datos
- Nunca versionar `.env`, claves, tokens, datasets privados o restringidos, pesos (`.gguf`, `.safetensors`, `.bin`…). `.gitignore` los cubre en cualquier ruta.
- Para cualquier corpus: revisar licencia y restricciones, documentar procedencia y obtención, versionar solo derivados permitidos. Ver `thesis/corpora/`.

## Referencias
- `references.bib` + `apa.csl` (APA salvo indicación de la Universidad El Bosque). Toda referencia debe ser verificable; no inventar.

## Código y notebooks
- Notebooks = exploración; código estable → `scripts/` (o `src/` si crece). Notebooks públicos llevan la insignia *Open in Colab* (`https://colab.research.google.com/github/carosamu/doctoral-llm-research/blob/main/<NOTEBOOK_PATH>`).
- Figuras: SVG/PNG/PDF, generadas por scripts versionados.

## Comandos
```bash
quarto render                         # renderiza (ejecuta antes scripts/build_tables.py)
python3 scripts/check_links.py _site  # revisa enlaces internos
quarto preview
```

## CI/CD
`.github/workflows/publish.yml`: en push a `main` renderiza, revisa enlaces y publica en `gh-pages`. Antes de cambiar versiones de las Actions, verificar la versión estable vigente.

## Principio rector
Dentro de varios años debe poder reconstruirse: la pregunta, el modelo y versión, el estímulo, los parámetros, la salida, el análisis, la interpretación y cómo cambió la comprensión del problema. Priorizar infraestructura científica reproducible sobre apariencia.
