# positions — 2026-11-22

**ALERTA, dos capacidades que siguen sin funcionar y una que importa más que
las dos.** (1) El etiquetado de Gmail continúa averiado y esta semana tampoco
se probó, a propósito: `list_labels` se hizo una sola vez y confirmó que la
etiqueta `Research` existe (id `Label_1910483919685933112`) y **marca 0
mensajes y 0 hilos**, es decir que los intentos de las dos semanas anteriores
nunca cuajaron. No había ningún hilo que mereciese la etiqueta, así que no se
gastó el intento ni se escribió una etiqueta errónea en su buzón. **Hilos sin
etiquetar: ninguno.** Sólo lo arregla reconectar el conector de Gmail con
permiso de modificación de etiquetas; la rutina no puede. (2) **El buzón está
vacío de alertas por una causa concreta y corregible: ninguna de las 50
suscripciones propuestas está dada de alta.** La pasada A dio 0 hilos y la
pasada B dio 1, un boletín de interés general sin oportunidad, descartado en
silencio por la regla de privacidad. Mientras no se dé de alta ni una alerta,
la rama 5 saldrá vacía todas las semanas, y eso no es una avería del código.
(3) Lo que importa más: `data/owner_status.json` sigue siendo `{}`. **Séptima
semana sin una sola marca en la página.** 114 postdocs y 39 empleos sin que
nadie haya puesto un READ, un DISCARDED ni un APPLIED. Si la página no se está
usando, eso pesa más que cualquier fila de esta pasada.

Perfil completo (sin `PROFILE-INCOMPLETE` ni `[TODO]`). Remoto correcto y, por
primera vez en cuatro semanas, **el checkout llegó en `main` y no en HEAD
desacoplado**; árbol limpio y `git pull --rebase` ya al día. No existía informe
de hoy ni commit ajeno de `positions` fechado hoy: no fue re-disparo. Las cinco
ramas entregaron. Push directo a `main`, sin rechazo y sin rama de desvío.

## Recuento, tomado de `git diff --stat HEAD~1`

| fichero | cambio |
|---|---|
| `data/postdocs.tsv` | 5 altas (P-0110…P-0114), 11 filas actualizadas |
| `data/jobs.tsv` | 2 altas (J-0038, J-0039), 9 filas actualizadas |
| `data/sources.tsv` | 19 fuentes nuevas (SRC-0521…SRC-0539) |
| `data/subscriptions.tsv` | 2 altas (SUB-0049, SUB-0050) |
| `data/inbox_triage.tsv` | 0 filas |
| `data/changelog.tsv` | 27 apuntes |
| `data/action_now.tsv` | 2 filas mías (J-0003, J-0038), 64 ajenas preservadas |

**7 altas y 20 filas actualizadas** (16 líneas añadidas menos 11 borradas en
postdocs; 11 menos 9 en jobs). En un **segundo commit** van 8 filas más de
postdocs por una normalización de columna que se explica abajo.

Presupuesto de las ramas: 27 + 24 + 23 + 24 + 24 = **122 llamadas** (techo 125).
La rama 1 se pasó **dos llamadas** del techo duro de 25 y lo declaró ella misma:
las de más fueron el tramo final de Tartu, que se torció porque WebFetch da 403
en `genomics.ut.ee` y el slug de la noticia estaba renombrado.

## Las tres cosas que merecen acción

1. **P-0083, el postdoc del IDIS de Santiago, cierra el 2026-11-30: ocho
   días, y es lo único de esta pasada que pide trabajo esta semana.** Genómica
   de predisposición al cáncer, no es su línea pero sí su técnica. El anuncio de
   la AEGH **no pide cartas de referencia**, así que el esfuerzo real es XS-S y
   cabe en una tarde: CV y media página. Dos ramas chocaron en esta fila y la
   resolución está explicada más abajo.
2. **P-0096 no estaba cerrada, y la fecha que teníamos era mala.** Baylor
   College of Medicine, Reproductive Psychiatry: Science Careers publica
   «Closing date: Nov 30, 2026» y el `validThrough` dice lo mismo, frente al
   2026-11-16 que llevaba la base **y que la pasada anterior dejó como deuda
   precisamente por vencer**. O el dato era erróneo o el plazo se amplió; no se
   puede saber cuál, y así queda dicho en su fila. Corregida a OPEN con plazo
   2026-11-30. Es Fit 2, así que no cambia su semana, pero es el recordatorio de
   que **una fila sin verificar puede estar equivocada en los dos sentidos**, no
   sólo cerrada sin que nos enteremos.
3. **J-0038, la Bolsa Electrónica Única del INGESA, cierra el mapa
   administrativo español.** Ceuta y Melilla eran la última administración sin
   fila: ahora están las 17 CCAA más el INGESA. Es bolsa permanente (Fit 4,
   Competition_Level LOW, por eso entra en `action_now`) y además hay una OPE
   2026 de 408 plazas. Igual que el ICS catalán, **no hay que esperar a ninguna
   convocatoria**. Y en su prioridad número 1, lo más on-profile de la semana es
   **P-0113: Computational Scientist I en los laboratorios Neale/Macosko del
   Stanley Center** (Broad, ref. 45198, publicada el 18-11, 88.000-124.000 USD,
   Fit 4, VERIFIED). Con dos reservas escritas en la fila y no maquilladas:
   **exige RNA-seq, que ella no tiene**, y sus relojes (05-2027 / 02-2028) la
   convierten en **gancho para escribir a Neale en 2027, no en candidatura de
   hoy**.

## Lo que cerró: cuatro cierres, todos con evidencia dura

- **P-0057** (UCSF, laboratorio Pirruccello): Nature Careers muestra el cartel
  «This job has expired»; cerró el 21-11.
- **P-0095** (UMC, ALS): AcademicTransfer dice literalmente «You cannot apply
  for this job anymore (deadline was 19 Nov)».
- **P-0088** (Southampton, IA aplicada a medicina genómica): la ficha se ve sin
  cartel, pero «Closes: 18th November 2026» y `validThrough 2026-11-18`.
- **P-0022** (Clinical Research Associate, Univ. of Alberta): **el conflicto
  declarado la semana pasada queda resuelto, y a favor de la ISPG.** El REST de
  Oracle Recruiting de Alberta sirve las 95 requisiciones vivas y la 3142 no
  está; **no es truncamiento del listado**, porque las 3314 y 3538 siguen
  apareciendo. CLOSED y Confidence sube a VERIFIED. De paso, ese endpoint es
  **el hallazgo técnico de la semana**: levanta un bloqueo que la base tenía por
  permanente y es patrón reutilizable en cualquier portal `*.oraclecloud.com`.

Confirmadas vivas, con plazo inminente: **P-0036** (KCL, Maternal Sleep,
**cierra mañana 23-11 a las 23:59**, y KCL avisa de que puede cerrar antes por
volumen), **P-0103** (Queen Mary DTP671, 25-11) y **P-0089** (UCL REFINE-MS,
26-11). Ninguna es Fit >= 4, así que ninguna entra en `action_now`.

## El choque de P-0083 y cómo se resolvió, en vez de en silencio

Dos ramas tocaron la misma fila con lecturas opuestas. La **rama 2** no pudo
leer la Tier 1 —`aegh.org/oferta-laboral-postdoc/` responde HTTP 200 con 12.001
bytes de muro antirrobot («One moment, please… Please wait while your request is
being verified…»)— y propuso bajarla a UNVERIFIED. La **rama 5**, por otro
camino, la vio **viva en el tablón Job Opportunities de la ESHG** con fecha de
publicación 14.10.2026. Resolución del orquestador, escrita en su
`Source_Note`: **Status OPEN y Confidence LIKELY**. No es VERIFIED porque la
Tier 1 no se pudo abrir hoy, y no es una incógnita porque dos señales Tier 2
coinciden. El plazo 2026-11-30 **sigue viniendo del anuncio de la AEGH**, que es
la Tier 1 de esta fila, no del tablón de la ESHG, que no reproduce plazos.

## El BOE, séptima semana: sin novedad en genética, pero sí en SU especialidad

Leídos por la **API de datos abiertos del BOE** los seis sumarios del 16 al
21-11-2026 (HTTP 200, 212-406 KB): **cero «genética», cero «Laboratorio
Clínico», cero «programa formativo»**. Ni DG/91/26 ni DG/90/26 publicados: **no
hay vía transitoria**. Lo que sí apareció es el único proyecto abierto en la
audiencia pública de Sanidad, el **«Proyecto de Orden del programa formativo de
la especialidad de Laboratorio Clínico», fechado el 04-11-2026**, leído en PDF:
acredita que la Comisión Nacional ya está constituida y **ya elaboró el
programa**, pendiente de ratificación y de BOE. Es la especialidad que el RD
101/2025 le dará, así que importa. Va escrito en J-0003 con **`Deadline`
VACÍA**, que es el parche conocido para que el generador no convierta una fecha
en prosa en un `Days_Left` negativo.

De las cinco CCAA cerradas, **Madrid y Osakidetza comprobadas hoy en Tier 1 y
ninguna reabre** (Madrid sólo TCAE/dependencia; en Osakidetza su categoría sigue
en listas definitivas del 30-10, con alzada hasta el 30-11). Murcia y Navarra
no tienen vía automática. **La Comunitat Valenciana es la única sin comprobar**:
`san.gva.es/…/borses-de-treball` da 404.

## EURAXESS: una regresión que hay que decir sin rodeos

**Cero altas por tercera semana, y esta vez el portal está peor que la anterior.**
`/jobs/search` **pelado** responde 200 (173.914 bytes, los 10 últimos ids: hoy
482208-482217, universidad de Brno, agronomía, cero relevancia), pero
**cualquier query string o segmento de faceta devuelve 403 de CloudFront**
(40.657 bytes, `<title>Sorry - 1093533993</title>`): `?keywords=`, `?f[0]=`,
`?search_api_fulltext=`, `/page/2`, `/country/spain-1099`,
`/field_of_science/medical-sciences`, `/offer_type/job`. **Eso mata la
paginación `?page=N` que SRC-0429 daba por buena.** Y el rodeo por buscador
externo, que estaba vivo el 15-11, **hoy está muerto**: sólo devuelve fichas
rancias (ids 70623…435322, todas vencidas) mientras el espacio real va por
482.2xx, a unos 250 ids al día. Cuatro puertas de cosecha masiva probadas y
cerradas: `/sitemap.xml` da 200 y está fresco pero **su índice sólo contiene
basic-pages, events y news, no `/jobs/`**; `/jobs/feed`, `/api/jobs` y
`/rss.xml` dan 404. Corrección de diagnóstico que vale la pena: los espejos
nacionales `.es/.de/.nl/.dk/.se/.ie` **responden 200 en la raíz** (no están
caídos como se dijo de `.fi/.be/.pt`), pero **no tienen listado propio**:
delegan en el buscador central con faceta, y la faceta es justo lo bloqueado.
El espejo de la MCAA está **congelado**: mismos ids que el 08-11.

**La única vía que el 403 no toca**: `/jobs/<id>` responde 200 sin query string.
La semana que viene toca un barrido acotado de 60-80 ids leyendo sólo el
`<title>` en una sola llamada.

## La frase literal: el ángulo funciona, pero no por donde se creía

`jobs.ac.uk` **sí respeta las frases entre comillas** en `/search/`. Medido:
«nearing completion of their PhD» → 7 fichas, «about to complete their PhD» →
2, y **«or expect to soon receive a PhD» → cero**. Ninguna de las nueve es de
genética. Pero el hallazgo estructural vale más que una fila: **7 de esas 9 son
de la University of Birmingham, porque la cláusula es *boilerplate* de sus
anuncios de Research Fellow**, no una concesión caso por caso. Conclusión para
la semana que viene: **vigilar Birmingham**, no rotar frases.

## Lo que no se pudo verificar o alcanzar, con el error exacto

- **P-0011 (Albert Einstein) no estaba bloqueada, está en JavaScript**:
  `careers.einsteinmed.edu` responde 200 y redirige a `/careers-home`, cuyo HTML
  no contiene la palabra «genetics»; `/search-jobs/genetics` da 404 (424.787 B).
  Sigue UNVERIFIED y la rama 3 **propone darla de baja la próxima pasada**.
- **P-0010 (CRG)**: un intento por otra puerta, `www.crg.eu/en/jobs` → **404**
  (55.842 B). UNVERIFIED con nota y nada más.
- **Ningún otro centro de CIBERSAM está en Teamtailor**: `jobs.{imim, idibaps,
  fidmag, santjoandedeu, sjdhospitalbarcelona, iislaprincesa}.org/jobs.rss` dan
  **HTTP 000, 0 bytes, el DNS no resuelve**. El RSS del VHIR se queda como la
  única puerta viva a la red, y por eso se propone como suscripción. **No
  repetir el patrón.**
- **Australia, quinta semana ciega.** Estrenada `unijobs.com.au`: `curl (35)
  Recv failure: Connection reset by peer`, HTTP 000, 0 bytes, y el proxy anotó
  `ws_closed_mid_exchange`. `jobs.ac.uk/jobs/australasia/` da 200 con 70.349
  bytes **y cero enlaces de oferta**. QIMR: `www.qimrb.edu.au/careers` redirige
  a `/people-and-careers`, que sólo enlaza becas. **La vía australiana es el
  correo, y eso es trabajo de ella.**
- **El Netherlands Twin Register no publica por su cuenta**:
  `tweelingenregister.vu.nl` responde 200 con 5,5 KB de carcasa y sin sección de
  vacantes. Queda cerrado como ángulo: lo que hay es correo especulativo.
- **CNIO por la ruta buena, resuelto en negativo**:
  `cnio.es/en/about-the-cnio/employment-opportunities/` se lee entera y **hoy no
  tiene ni una vacante de investigación**. El 404 de la semana pasada era ruta
  equivocada, no bloqueo, y ya está corregido en `sources.tsv`.
- **Cardiff, tercer intento y tercera negativa**: `cardiffuniweb.eploy.net`
  `/vacancies/rss/` → 404 vía `filenotfound.aspx`, y `?format=rss` devuelve HTML
  (200, 499 KB) que **declara 36 vacantes sin un solo título** ni mención de
  genetic/genomic/psychiatric.
- **Nature Careers sirve para VERIFICAR, no para BUSCAR**: su buscador `?q=`
  responde 200 con el mismo cascarón de 110 KB y el total sin filtrar «1.177
  jobs» para cualquier consulta; las fichas individuales sí se leen (verificado
  hoy con P-0057).
- Otros bloqueos de un intento, fichados para no reincidir:
  `ingesa.sanidad.gob.es` **con `www` da HTTP 000 por fallo de TLS** (usar sin
  `www`); `boe.es/buscar/boe.php` → 200 con «Los valores de búsqueda enviados
  son incorrectos»; `murciasalud.es/empleo.php?idsec=39` → 200 con cuerpo de
  `stormcaster.js`/`validate.perfdrive.com`; `boards-api.greenhouse.io/v1/
  boards/23andme/jobs` → 404 (slug incorrecto); la ficha del MSL de IQVIA →
  **404, la vacante ya no existe**; `apply.workable.com/api/v1/accounts/
  our-future-health` → **429 por segunda semana** (J-0032: se quita el
  reintento); archivo de la lista `uoc-statgen` → 404. **J-0012 (GSK) no se
  reintentó a propósito**: su propia fila dice que sólo lo cierra ella con
  navegador.
- **Edimburgo y KCL no se tocaron** por presupuesto agotado de la rama 3; sus
  rutas se recorrieron hace una semana.

## Un conflicto nuevo, declarado y sin resolver

El tablón de la ESHG tenía **5 ofertas el 2026-10-25 y hoy tiene 4**: una se
retiró, pero sin los ids de entonces **no se puede decir cuál**. Los ids de hoy
quedan anotados para la próxima: **166, 169, 171, 172**.

## Dos cosas de higiene de datos, una arreglada y una que no es mía

1. **Arreglada: la columna `Competition_Level` tenía seis valores en castellano
   o inventados** («ALTA», «alta», «MEDIA», «no estimado» ×3, «NO EVALUADA»,
   «Desconocido») y dos de ellos los acababan de meter las altas de hoy. El
   contrato sólo admite LOW/MEDIUM/HIGH/UNKNOWN y los valores mezclados rompen
   los filtros de la página, que es la lección que ya costó un fallo con
   `Fit_1_5` escrito como `4.0`. **Normalizadas 8 filas de postdocs** (P-0043,
   P-0082, P-0093, P-0094, P-0095, P-0096, P-0111, P-0112), cada una con la
   constancia del valor anterior en su `Competition_Basis`, y 8 apuntes de
   changelog. La columna ya sólo tiene los cuatro valores del contrato.
2. **No es mía y vuelve a crecer: la regla del tamaño.** `postdocs.tsv` va por
   **258 KB** y `jobs.tsv` por **136 KB**, cuatro y dos veces el umbral de ~60
   KB. **Partir un fichero exige cambiar `tools/build_page.py` y
   `tools/build_xlsx.py` en el mismo commit y el contrato prohíbe hacerlo
   desatendido al final de una pasada.** Es trabajo de la dueña y lleva semanas
   pendiente.
3. **Nota sobre el diff de `action_now`**: aparece reescrito entero (66 líneas
   por 65) porque esta semana tengo **2 filas en lugar de 1** y eso recorre el
   `Rank` de las 64 ajenas. No es una reformateada cosmética ni afecta a
   «Novedades de la semana», que `build_page.py` construye a partir de
   `Change_Flag`, no del diff de ese fichero.

## Filas suyas cuyos hechos cambiaron bajo ella

**Ninguna**, y por la misma razón que las seis semanas anteriores:
`data/owner_status.json` es `{}`. Ninguna de las 28 actualizaciones de hoy pisa
una decisión suya, porque todavía no hay decisiones.

## Suscripciones

**50 filas, las 50 PENDING** por la definición del contrato (TSV en TODO y sin
marca en `owner_status.json`). Dos altas, las dos con URL de alta leída:
**SUB-0049**, el **feed RSS de vacantes del VHIR** (`jobs.vhir.org/jobs.rss`,
14 ítems con fecha), que es la única puerta viva a CIBERSAM; y **SUB-0050**, la
**lista de distribución de Participación Pública en Proyectos Normativos del
Ministerio de Sanidad**, que es el canal por el que llegaría la vía transitoria
de Genética Médica antes de salir en el BOE. Las ramas 1, 2 y 5 propusieron
**cero a propósito**: sus puertas obvias ya están en el fichero y ninguna leyó
una URL de alta nueva.
**Sigue pendiente, tercera semana**: la alerta por correo de **SfN NeuroJobs**.
`neurojobs.sfn.org` continúa inalcanzable y `www.sfn.org/careers/
neurojobs-career-center`, que sí se lee, **no menciona alertas**. No se inventa.
Probablemente haya que darla de alta a mano en un navegador o escribir a
`profdev@sfn.org`.

## Fuentes nuevas: 19, y las cinco ramas estrenaron

Lo aprovechable, por orden: el **REST de Oracle Recruiting de la Universidad de
Alberta** (patrón reutilizable en todo `*.oraclecloud.com`, y es lo que cerró el
conflicto de P-0022), la **API CXS de Workday de Moderna** (patrón reutilizable
en todo `*.myworkdayjobs.com`, y es lo que verificó J-0039), la **búsqueda por
frase literal de `jobs.ac.uk`**, la **Bolsa Electrónica Única del INGESA**, la
**ruta inglesa buena del CNIO**, el **`/SearchJobs/<término>` del Avature del
Broad** y la **entrada viva de empleo público de Navarra**. Más una fuente
nunca tocada que rindió información aunque no filas, el tablón de empleo de la
**Schizophrenia Research Society**. Y **ocho callejones documentados a propósito**
—el sitemap de EURAXESS, la regresión del 403 en su faceta, las raíces de los
espejos nacionales, sus Hosting Offers, `unijobs.com.au`, el listado Australasia
de jobs.ac.uk, el bloqueo blando del buscador de Nature Careers, el
`careers-home` en JavaScript de Einstein, el `/careers` de QIMR y el 404 de
`crg.eu/en/jobs`— porque una puerta cerrada registrada es presupuesto que no se
vuelve a gastar.

## Qué perseguiría la semana que viene con más presupuesto

Por orden de rentabilidad: **el barrido acotado de ids `/jobs/<id>` de
EURAXESS**, que es la única vía que el 403 de CloudFront no toca; **vigilar la
University of Birmingham**, ahora que se sabe que la cláusula del doctorado
inminente es su *boilerplate*; **exprimir los dos patrones de API nuevos**
(Oracle Cloud y Workday CXS) contra los portales que la base tiene por
bloqueados, empezando por Mount Sinai, GSK y las empresas de genómica;
**resolver la Comunitat Valenciana**, la única administración española sin
comprobar; **dar de baja P-0011** si el portal de Einstein sigue en JavaScript;
**los ids 166/169/171/172 del tablón de la ESHG** para cerrar el conflicto de la
oferta retirada; y **escribir a Neale (P-0113) y a Mägi (P-0110)**, que son los
dos únicos contactos en frío de esta pasada que apuntan a sus líneas 1 y 2 a la
vez — aunque eso no es trabajo de la rutina, es trabajo de ella.
