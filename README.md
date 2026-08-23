# Radar de investigación · research-opportunities

Sistema de vigilancia semanal de oportunidades post-doctorado para una médica
neurocientífica que termina su tesis: postdocs, empleo dentro y fuera de la
academia, fellowships y becas de movilidad, grupos de investigación a los que
acercarse, congresos y formación. Tres rutinas automáticas (Claude Code
Routines, en la nube de Anthropic) investigan cada semana, escriben en este
repositorio, y el repositorio genera una página web y un Excel. Nada corre en
un ordenador personal.

La estructura está clonada del rastreador de financiación de PitAssist, que
lleva semanas en producción: este repo hereda su diseño y todas sus lecciones
aprendidas, ya cocinadas en los prompts y las herramientas.

**Estado: por estrenar.** La estructura está completa y probada en local, pero
el perfil de la candidata aún no está definido y las rutinas no existen
todavía. **El orden de puesta en marcha está en `SETUP.md`** — ese fichero es
la lista de tareas; este README es el contrato de cómo funciona todo.

---

## 1. Qué queremos conseguir

Que ninguna oportunidad a la que ella pudiera optar pase desapercibida, y que
enterarse cueste cinco minutos de lectura a la semana.

Concretamente:

- Una **base de datos viva** de oportunidades con encaje evaluado contra SU
  perfil, nivel de competencia estimado, plazos, relojes de elegibilidad
  (ventanas de años post-doctorado, reglas de movilidad) y siguiente paso
  concreto.
- Una **página web** donde lo nuevo se lee de un vistazo pero nada está
  recortado: cualquier fila se despliega con todas sus columnas. Arriba,
  «Novedades de la semana», construida por CI desde el `git diff` de la
  pasada — una fila sale ahí si y sólo si la rutina tocó su línea.
- Un **Excel** siempre sincronizado (`docs/research.xlsx`), para mandárselo a
  un mentor o a la directora de tesis.
- **No hay correo.** La página es el único entregable.
- Que ella pueda **marcar estados** desde la página y que las rutinas
  obedezcan: lo descartado no vuelve a aparecer.

## 2. Cómo está montado

```
data/                estado canónico. Un TSV por pestaña. SIN fechas en el nombre.
  postdocs.tsv         posiciones postdoc (P-####)     jobs.tsv        empleo no académico (J-####)
  fellowships.tsv      becas y fellowships (F-####)    groups.tsv      grupos de investigación (L-####)
  events.tsv           congresos (E-####)              training.tsv    cursos y escuelas (T-####)
  watchlist_closed.tsv cerradas a vigilar              action_now.tsv  accionables, regenerada por pasada
  sources.tsv          fuentes de búsqueda (semilla)   subscriptions.tsv  alertas por suscribir
  inbox_triage.tsv     correos triados                 changelog.tsv   historial de cambios
  readme.tsv           contrato de datos               owner_status.json  el estado que marca ELLA
  source_inbox.json    URLs que ella propone desde la página

docs/index.html      la web. GENERADA — no editar a mano.
docs/research.xlsx   el Excel. GENERADO — vive en docs/ para que Pages lo sirva.
tools/               build_page.py · build_xlsx.py · apply_rows.py · rebuild_action_now.py
prompts/             profile.md + common-v1.md + branches-*.md → build_prompts.py → out/*.md
runs/                un informe por pasada (lo escriben las rutinas)
postmortem/          análisis de fallos, si algún día hay uno
research/            informes de investigación dirigida, a petición
.github/workflows/   build.yml regenera página y Excel en cada push a data/
```

**Git es el historial.** Los ficheros no llevan fecha en el nombre: la versión
anterior está en el commit anterior, y las novedades de la semana se calculan
con `git diff`, no confiando en que una rutina se acuerde de marcarlas.

**El perfil vive en `prompts/profile.md`** y se concatena delante del prompt de
cada rutina al regenerar. Mientras contenga el marcador `PROFILE-INCOMPLETE`,
las rutinas se niegan a investigar (escriben una ALERTA y paran): es el
guardarraíl para que nadie queme una semana de búsquedas contra un perfil sin
definir.

## 3. Cómo funciona una pasada

1. La routine arranca en la nube con el repo ya clonado y con permiso de push
   vía la GitHub App de Claude. Lee `prompts/out/<rutina>.md` (perfil +
   instrucciones comunes + su rama), `data/readme.tsv` y `data/sources.tsv`.
2. Lanza cuatro o cinco subagentes, uno por rama de búsqueda, con fronteras
   que no se solapan.
3. Edita **sólo los TSV que le pertenecen**, con un script, sobre el disco
   (`tools/apply_rows.py` escribe de forma atómica y se niega a tocar
   `Owner_Status`).
4. `commit` → `pull --rebase` → `push` directo a main.
5. CI regenera `docs/` (página y `research.xlsx`) y publica en Pages.
6. La rutina lee `git diff HEAD~1 --stat`, escribe `runs/<fecha>-<rutina>.md`
   con esos números, y ahí acaba. No manda nada.

Reparto de propiedad, para que tres rutinas no se pisen:

| rutina | posee | horario (Madrid) |
|---|---|---|
| positions | postdocs, jobs · lee el buzón de Gmail | 00:01 lunes |
| fellowships | fellowships, watchlist_closed | 04:00 lunes |
| ecosystem | groups, events, training · backstop del triaje | 08:00 lunes |
| las tres, sólo añadiendo | changelog, sources, inbox_triage, subscriptions | |

El escalonado no es cosmético: la primera rutina hace el triaje del buzón, la
última es el backstop del triaje, y las horas entre pushes dejan que el
`pull --rebase` de cada una vea el trabajo de la anterior.

## 4. Los estados los pone ella

En la página, cada oportunidad tiene siete botones:

`sin ver` · `leído` · `en curso` · `solicitado` · `resuelto` · `volver a mirar` · `descartado`

Se guardan en `data/owner_status.json`, que escribe la propia página contra la
API de GitHub. La primera vez pedirá un token con permiso de escritura sobre el
repo (SETUP.md §6); se queda en el almacenamiento local del navegador y
**nunca se sube**. También puede fijar su **encaje personal** (1-5), que pisa
al de la rutina donde exista, y marcar suscripciones como hechas o descartadas.

Las rutinas leen ese fichero y tienen prohibido escribirlo. Lo que ella marque
como `descartado` desaparece de `action_now` para siempre, pero la fila sigue
en la base de datos con su motivo.

## 5. Decisiones heredadas del tracker hermano, y por qué

- **Git en vez de Drive/correo.** El clone y el push no pasan por el contexto
  del modelo; leer y re-emitir ficheros por herramientas consumía más
  presupuesto que la investigación.
- **Sin fechas en los nombres.** La convención con fechas generó dos ficheros
  «más recientes» a la vez. Git no permite que eso ocurra.
- **Las novedades se calculan del diff.** Una pasada informó de 65 filas
  nuevas cuando su fichero tenía 47. Si el número sale de `git diff`, esa
  clase de error es imposible.
- **El renderizado se va a CI.** La rutina sólo commitea datos; la página es
  una función pura del estado y el Excel queda sincronizado por construcción.
- **Escritura atómica de TSVs.** Abrir con `w` y morir a mitad trunca el
  fichero; ya destruyó dos filas una vez. `apply_rows.py` escribe a temporal y
  renombra.
- **La etiqueta de Gmail se aplica por ID, no por nombre.** Cinco pasadas se
  perdieron diagnosticando ese error; la lección va en el prompt.
- **La watchlist tiene rama propia con presupuesto propio.** Adosada a otra
  rama, agotaba el techo de llamadas y las filas volvían sin verificar.

## 6. Empezar de cero en otra sesión

```bash
git clone <url-del-repo>   # ver SETUP.md §2
cd research-opportunities
pip install openpyxl
python3 tools/build_page.py && python3 tools/build_xlsx.py
open docs/index.html
```

Para regenerar los prompts tras editar el perfil, el común o una rama:

```bash
python3 prompts/build_prompts.py   # escribe prompts/out/*.md
```

El CI vigila que `prompts/out/` esté sincronizado: si editas una fuente y no
regeneras, el build falla a propósito.
