# Memory — research-opportunities

Radar semanal de oportunidades post-doctorado (postdocs, empleo, fellowships,
grupos, congresos, formación) para una médica neurocientífica que termina su
tesis. Tres Claude Code Routines investigan cada lunes, empujan TSVs a este
repo y el CI regenera la página de GitHub Pages (pública) y el Excel.

Clonado del tracker de funding de PitAssist el 2026-08-23, con sus lecciones
ya incorporadas en prompts y herramientas.

## Reglas para cualquier sesión en este repo

- `data/` es el estado canónico. `docs/` es GENERADO por CI: no editar a mano
  jamás; si la página sale mal, el bug está en `tools/`.
- `data/owner_status.json` lo escribe la dueña desde la página. Las rutinas y
  las sesiones tienen prohibido escribirlo.
- Los TSV se editan con script y escritura atómica (`tools/apply_rows.py`),
  nunca reescribiendo el fichero entero en una llamada de herramienta.
- Tras editar `prompts/profile.md`, `common-v1.md` o una rama:
  `python3 prompts/build_prompts.py` y commitear `prompts/out/` (el CI falla
  si está desincronizado).
- Mientras `prompts/profile.md` contenga `PROFILE-INCOMPLETE` o `[TODO]`, las
  rutinas no investigan: es el guardarraíl, no un bug.
- Commits pequeños con mensajes en español. Documentación en español; prompts
  y columnas de datos en inglés.

## Dónde está cada cosa

- Contrato completo del sistema: `README.md`.
- Puesta en marcha pendiente (repo de ella, Pages, routines, Gmail, token):
  `SETUP.md` — es la lista de tareas viva.
- Contrato de datos por pestaña: `data/readme.tsv`.
