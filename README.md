# doctoral-llm-research

**Doctoral Research Hub · Computational Research Journal · Reproducible LLM Laboratory**

Doctorado en Ciencia de Datos e Inteligencia Artificial — Universidad El Bosque.
Investigador: Claudio de la Rosa.

## Proyecto de tesis

*Embedded Intelligence: Inheritance and Resurgence Across Large Language Models* (título provisional). Estudio experimental, estadístico y probabilístico de regularidades aprendidas por modelos de lenguaje autorregresivos. *Inheritance*, *Resurgence* y *Embedded Intelligence* son **constructos de trabajo**, no fenómenos demostrados.

## Propósito del repositorio

Archivo académico del doctorado, bitácora técnica, laboratorio reproducible de experimentos con LLM (Pythia 2.8B, Gemma 3 4B, Qwen 3 4B; `llama.cpp`), archivo de la tesis y sitio público construido con Quarto.

## Estructura

```text
doctorate/   formación doctoral
thesis/      laboratorio y archivo de la tesis (experiments, models, corpora, stimuli,
             analysis, results, protocols, decisions, manuscripts, archive …)
publications/  presentations/  environment/  scripts/
```

## Reproducibilidad

Cada experimento usa `thesis/experiments/_template/` y registra todos los parámetros de inferencia. Los pesos y datos restringidos **no** se versionan: se documentan fuente, licencia y hash. Ver [`CLAUDE.md`](CLAUDE.md).

## Sitio web

https://github.com/carosamu/doctoral-llm-research/

```bash
quarto render      # requiere Quarto y Python 3 (solo biblioteca estándar)
quarto preview
```

## Estado actual

Infraestructura inicial creada. Sin resultados experimentales registrados todavía.
