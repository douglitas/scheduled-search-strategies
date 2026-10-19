# fellowships — 2026-10-19

Las cinco ramas completas, 116 llamadas de herramienta entre ellas. Ninguna
reapertura esta semana, pero sí dos convocatorias cerradas en falso que ahora
están decididas y una pregunta de elegibilidad que llevaba dos meses abierta y
queda zanjada en Tier 1.

## Recuento, tomado del diff y no de la memoria

`git diff HEAD~1 --stat`: 167 inserciones, 80 supresiones en 6 ficheros.

| fichero | antes | después | altas | filas modificadas |
|---|---|---|---|---|
| `fellowships.tsv` | 77 | 82 | F-0078 a F-0082 | 28 |
| `watchlist_closed.tsv` | 26 | 27 | W-0027 | 16 |
| `sources.tsv` | 317 | 329 | 12 fuentes | append-only |
| `subscriptions.tsv` | 33 | 36 | 3 propuestas | append-only |
| `changelog.tsv` | 863 | 928 | 65 apuntes | append-only |
| `action_now.tsv` | 37 | 38 | mías: 2 (F-0077, F-0027) | 36 ajenas preservadas |

`owner_status.json` sigue vacío y `source_inbox.json` también: no había nada que
triar y **ninguna fila tenía marca de la dueña distinta de `NEW`**, así que esta
pasada no ha dejado obsoleto nada que ella hubiera leído ya. La lectura del
correo no es de esta rutina: la hizo `positions` a las 00:01 y dejó
`inbox_triage` sin nada pendiente de ruta FELLOWSHIPS.

**Aviso de lectura sobre el diff de `action_now`:** aparecen 36 líneas tocadas,
pero el contenido ajeno no ha cambiado. Es mecánico: mi bloque se reinserta
donde ya estaba y al crecer en una fila renumera el `Rank` de todo lo que viene
detrás. Si «Novedades de la semana» sale sobrepoblada, el motivo es éste y no un
cambio real. No es algo que arreglar desatendido: tocaría `rebuild_action_now.py`.

## Las tres cosas que merecen acción

**1. F-0077, DMM Conference Travel Grants — sube de Fit 3 a Fit 4 y cierra el
30-10-2026, dentro de once días. Es lo más accionable de la pasada.**
La condición que mantenía la fila en 3 era el ámbito de la revista *Disease
Models & Mechanisms*, y se ha cerrado hasta donde llegan las fuentes públicas:
la ayuda exige que **la reunión** caiga en el ámbito de la revista, no que su
manuscrito sea publicable allí, y el *About* de DMM es agnóstico de enfoque.
Esfuerzo XS, sin grupo de acogida: sólo hace falta la carta firmada de su
directora. Entra en `action_now` en el puesto 2.

**2. Ramón y Cajal queda resuelto y la respuesta es que no, hasta 2030.**
Leído el texto oficial completo, no una noticia: el artículo 6.1.a) exige que el
grado de doctor se haya obtenido **entre el 01-01-2016 y el 31-12-2024**, y el
límite superior **no** es ampliable (el inferior sí, por maternidad o enfermedad).
Además exige estar en posesión del título al solicitar, sin cláusula de «espera
defender» como la de la JSPS. Defendiendo en febrero de 2028 queda fuera, y si el
patrón se mantiene (techo = 31 de diciembre del año −2), hasta la convocatoria de
**2030** — eso último es inferencia, no dato. **F-0005 pasa a VERIFIED y el plazo
del 10-12-2026 deja de ser algo que vigilar.** Era la decisión más cara de
equivocarse que tenía la base.

**3. W-0009, el ECIP de la ISPG, mejora por un hallazgo de calendario.**
La ISPG ya publica la ficha del **WCPG 2027: 9-13 de noviembre, Brisbane**. Con la
del WCPG 2026 (Glasgow, 29-09 a 03-10) queda medido el desfase real cierre-congreso,
138 días, que empuja el plazo del ECIP de mediados de mayo a **finales de junio o
primeros de julio de 2027**. Tres consecuencias, todas a favor: el plazo pasa a caer
*después* del fin de su residencia (22-05-2027) en vez de días antes; en noviembre de
2027 seguirá siendo doctoranda y por tanto elegible por la vía de *graduate student*;
y la sede es la ciudad del QIMR Berghofer, donde tiene colaboradores vivos y de donde
sale su manuscrito en *Nature Mental Health*. Es la fila de Fit 5 con el camino más
despejado de todo el radar.

## Lo que ha cerrado

- **F-0024, L'Oréal-UNESCO España** (plazo hoy) → CLOSED. Siguiente edición hacia
  septiembre de 2027 (LIKELY). La rama 3 propone **dejar de rotarla**: el suelo de
  4 años desde la tesis la excluye hasta ~2032.
- **F-0075, SRSF Mentored Collaboration** → CLOSED, y además a `watchlist` como
  W-0027. Contradicción interna del financiador registrada en la fila: la página
  sigue mostrando *en futuro* el aviso de cierre del 16-10, ya pasado, mientras
  mantiene la frase «rolling basis».
- **F-0018, ERC Starting Grant** → CLOSED; la ERC-2027-StG cerró el 14-10-2026 y la
  página oficial seguía mostrándola abierta el 19-10. Reescrito el `Next_Action` con
  lo único que importa aquí, que es el horizonte: **su primera StG posible es la de
  2029**.
- **F-0029, Company of Biologists Travelling Fellowships** → Fit 2 confirmado por
  tercera pasada (el ámbito sigue limitado a *Development*, *JCS* y *JEB*). Publicadas
  ya las cuatro rondas de 2027: 05-02, 07-05, 06-08 y 05-11. Propongo que deje de
  consumir presupuesto.
- **BBRF Distinguished Investigator (F-0033)** datada y VERIFIED: ciclo 2027, 26-08 a
  23-09-2026, cerrado. Rellena el hueco que la fila arrastraba.

## La pregunta a Ana cambia de forma, y para mejor

La de más rendimiento de la lista llevaba cuatro semanas siendo «¿es socia de la SRS
o de la AASM, y **desde cuándo**?». La rama 3 ha leído las bases de los tres esquemas
y **ninguno exige antigüedad de socia**: la CDA pide «active SRS member at the time of
applying» (y verifica además solicitudes de **no residentes en EE. UU.**, que antes no
estaba confirmado); la Small Research Grant admite **SRS o AASM indistintamente** y su
matrícula de doctorado ya satisface la rama «registered in a graduate program» sin
apoyarse en el MD de 2019; la Mentored Collaboration pide ser socia activa y
**mantenerlo** el año financiado. O sea: **un sí/no sobre hoy, no una fecha de alta.**
La SES queda como el único esquema de sueño con regla de un año.

Las otras preguntas abiertas, sin novedad: socia de la SENC (única condición que falla
en F-0019, a tramitar con meses de margen antes de abril de 2027); antigüedad de
6 meses en SEQC/SEMEDLAB para F-0045; y membresía de la ESHG para 2027, que es lo único
que le falta a F-0023 (SUB-0030).

## Lo que no se ha podido verificar, y se dice en vez de disfrazarse

- **F-0073, Plan GenT2** (plazo 27-10): no se pudo reconfirmar el plazo y
  deliberadamente **no se ha puesto `Last_Verified` nuevo** (`ceice.gva.es` da 503,
  `uv.es/serinves` da 403 en listados). Pero la pregunta que importaba sí queda
  cerrada: **no le sirve**, toda modalidad exige doctorado terminado y anfitrión
  valenciano. El plazo a ocho días es irrelevante.
- **F-0049, F-0050, F-0063, F-0067, F-0069 y F-0072** conservan su `Last_Verified`
  antiguo: la rama 3 se quedó sin presupuesto y prefirió no falsear una verificación.
- **F-0070** (ECR Visiting Fellowships, plazo 27-11) no reverificada, por la misma
  razón. Es poco grave: la solicita el grupo receptor.
- **F-0066, AuSpire — conflicto de fechas sin reconciliar, anotado como tal.** La
  fila registra plazo 2026-01-26; la rama 3 encontró de pasada una Call 3 con plazo
  2026-09-07, 5 plazas e incorporación en enero de 2027. Ninguna de las dos se ha
  reverificado en Tier 1 y la fila no estaba asignada a quien lo encontró, así que
  **se deja el conflicto escrito y `Confidence` baja a UNVERIFIED** en vez de elegir
  una en silencio. Es la única vía España-Australia real encontrada hasta ahora.
- **Premisa refutada, y conviene que conste:** los Working Groups del PGC **no
  reparten dinero**. El índice vivo no contiene ni una aparición de *fund*, *grant*,
  *fellow*, *award*, *applic* ni *scholar*, y los ocho slugs que quedaban pendientes
  existen pero son páginas de personas. Deja de ser una pista que perseguir.

## Mantenimiento y entorno

`data/fellowships.tsv` pasa de 232 a **268 KB, más de cuatro veces el umbral de
60 KB**; `changelog.tsv` va por 308 KB, `sources.tsv` por 240 KB y
**`watchlist_closed.tsv` acaba de alcanzar los 60 KB**, así que ya son cuatro los
ficheros por encima o justo en el umbral. Con razón no se parte sola: obliga a tocar
`build_page.py` y `build_xlsx.py` en el mismo commit. Corte sugerido, el mismo de las
cinco pasadas anteriores: internacionales frente a españolas, o becas frente a premios
y ayudas de viaje.

El apunte de entorno va por la **cuarta semana**: no hay `pdftotext` y `pypdf` está
roto (`_cffi_backend`). Esta vez el método manual de `zlib` extrajo los 415.775
caracteres del PDF de Ramón y Cajal, que es justamente lo que resolvió el punto 2.
**Merece ser un helper de `tools/`.**

Bloqueos nuevos registrados para no volver a pagarlos: `bga.org` ahora da **503**
también en las URL `content.aspx` (antes sólo 403 en la raíz) y el espejo que sí
responde es `bga.clubexpress.com`; **`esrs.eu` no da 403 sino reto JS de Cloudflare**,
también en `/wp-json/`, así que el truco de WordPress no sirve ahí;
`lacaixafoundation.org` da 403; `ceice.gva.es` da 503; `fundacionjlc.es` cae con reset
de conexión en todo el dominio (tercer intento en dos pasadas); GrantConnect
(`grants.gov.au`) da 500 y no sirve de espejo de la NHMRC; Wayback dio **429, que es
ritmo y no bloqueo**, y merece un reintento en enero. Y una corrección de ruta:
**SRC-0070 apunta a una URL muerta** (`biologists.com/travelling-fellowships/` da 307);
la viva es `/grants/travelling-fellowships/`, ya fichada aparte. `sources.tsv` es
append-only, así que la fila vieja se queda: que conste aquí.

## Suscripciones pendientes

**36 de 36 en TODO, ninguna marcada aún** (`owner_status.json` está vacío, así que la
definición de pendiente es la del TSV). Tres nuevas esta semana: **SUB-0036, alta de
socia de la ESRS** (prioridad ALTA: es la vía de la fila nueva F-0081), SUB-0034
(boletín de convocatorias de la AGAUR) y SUB-0035 (alerta del DOG para la orden gallega).

## Decisión que es de ella, no de la rutina

**W-0014, One Mind Rising Star Awards.** La rama 5 mantiene la propuesta de retirada y
la razón es buena: la inelegibilidad es **estructural y verificada en Tier 1** (excluye
por nombre a *pre-doctoral students* y *postdoctoral fellows*, y exige puesto de
profesorado en EE. UU.), no una barrera de calendario que se resuelva esperando. Fit 1,
cinco pasadas gastadas sin que nada pueda cambiar. **No se ha borrado**: basta que
marque `DISCARDED` desde la página.

## Qué perseguiría la semana que viene

1. **La ventana de la SES, en diario del 27-10 al 05-11**: es la reapertura más cercana
   del watchlist (W-0012, W-0017, W-0026) y ya hay método de una sola llamada —
   `media?search=bases&orderby=date&order=desc` devuelve exactamente dos ficheros en
   todo el sitio, así que un tercero con «2027» en el nombre es prueba inequívoca.
2. **La Caixa Junior Leader (F-0006)**, la fila más stale de la base (2026-08-23) y la
   única realmente abierta entre las suyas; su ronda 2027 suele abrirse en otoño y ahora
   hay que leerla por espejo universitario porque el dominio da 403.
3. **One Mind y Fundación Tatiana**, las dos que la rama 3 no llegó a recomprobar.
4. **Las diez filas del watchlist aparcadas por decisión** (W-0002 a W-0004 del ISCIII
   por PDF de `/documents/d/guest/` en enero, W-0007, W-0008, W-0010, W-0015, W-0018,
   W-0021, W-0025): ninguna tiene ventana antes de finales de diciembre.
5. **El tipo de contenido de `fundacionjlc.es`**: la API REST responde pero las
   convocatorias son un *custom post type*; queda anotada en el `Source_Note` de F-0045
   la consulta exacta (`/wp-json/wp/v2/types`) que se murió dos veces por reset.
6. **Los correos que ya no se pueden evitar**, y van seis semanas: la BGA por el reloj
   de 7 años (F-0058, con la vía web agotada: ahora 503), `secretaria.tecnica@ses.org.es`
   por cómo se cuenta la antigüedad (F-0046), y la SEQCML por la rotación externa de
   Medicina de Laboratorio.
