# positions — 2026-11-08

**ALERTA, capacidad caída: el conector de Gmail LEE pero ya no puede ETIQUETAR.**
Los cuatro `label_thread` de la pasada fallaron con *"The Gmail connector is
missing a permission that this action needs"*, y **no es el error de siempre**:
se listaron las etiquetas una sola vez y se usó el **ID** correcto
(`Label_1910483919685933112`), que es el fallo que el contrato anticipa. Falta
un permiso en el conector, no un ID. Un intento, sin reintentos, como manda la
regla. **Hilos sin etiquetar: `1a1b21a7604092ea`, `1a1a7d4124fafa53`,
`1a1bc6d7a1992e15`, `1a1ad9ad18592615`.** Consecuencia que se repetirá sola
cada lunes mientras no se reconecte Gmail con ese permiso: **la pasada A
(`label:Research`) seguirá dando cero indefinidamente** —la etiqueta tiene 0
mensajes— **y la pasada B volverá a sacar estos mismos hilos cada semana**.
Reconectar el conector con permiso de modificación de etiquetas es la única
solución; no es algo que la rutina pueda arreglar por su cuenta.

**Buena noticia, y es estructural: EURAXESS ha vuelto a medias.** Ver abajo.

Perfil completo (sin `PROFILE-INCOMPLETE` ni `[TODO]`). Remoto correcto. **El
checkout llegó en HEAD desacoplado** (`HEAD detached from refs/heads/main`),
no en `main`: se recuperó con `git checkout main` antes de tocar nada, árbol
limpio y `git pull --rebase` sin novedades. No existía informe de hoy ni commit
ajeno de `positions` fechado hoy: no fue re-disparo. Las cinco ramas
entregaron. Push directo a `main`, sin rechazo y sin rama de desvío.

## Recuento, tomado de `git diff --stat HEAD~1`

| fichero | cambio |
|---|---|
| `data/postdocs.tsv` | 5 altas (P-0098…P-0102), 42 filas actualizadas |
| `data/jobs.tsv` | 1 alta (J-0032), 13 filas actualizadas |
| `data/sources.tsv` | 21 fuentes nuevas (SRC-0429…SRC-0449) |
| `data/subscriptions.tsv` | 2 altas (SUB-0044, SUB-0045) |
| `data/inbox_triage.tsv` | 4 filas |
| `data/changelog.tsv` | 61 apuntes |
| `data/action_now.tsv` | 1 fila mía (J-0003), 51 ajenas preservadas |

Presupuesto: 19 + 14 + 24 + 21 + 23 = **101 llamadas** en las cinco ramas
(techo 125), ninguna rama agotada salvo donde se dice.

## Las tres cosas que merecen acción

1. **P-0002 (Max Planck Psycholinguistics, grupo de Beate St Pourcain) sigue
   siendo la mejor fila viva de la base, y ahora se sabe por qué.** Es ROLLING
   con inicio negociable, verificada viva hoy ("Online since: 12.08.2026"), y
   el tablón de la ISPG publica dos datos que la ficha no daba: **acepta a quien
   "espere obtener en breve" el doctorado** —lo que suaviza su reloj de
   feb-2028, que es el muro contra el que choca casi todo lo demás— y banda
   **TVöD E13, 73.999,91–91.055,27 EUR/año**. Genética estadística de rasgos
   complejos, su línea 1. Escribirle es trabajo de ella, y es lo que decide el
   valor de esta pasada.
2. **El hallazgo de método de la semana: su MD es el billete de entrada a la
   escala clínico-académica, no su doctorado.** Lo encontró la rama 2 por la
   vía correcta (buscar su tema y leer después la línea de elegibilidad):
   **P-0100, Clinical Research Fellow de Genes & Health (Queen Mary)**, cohorte
   genómica de 67.000 participantes con historia clínica vinculada, banda
   **67.325–76.582 GBP**. Esta convocatoria concreta **no le sirve** (cierra el
   12-11-2026 y ella no está libre hasta el 22-05-2027), pero la categoría sí:
   es la grieta real en el muro del reloj. **Dato operativo con meses de
   antelación: esa vía se abre o se cierra por el registro en el GMC**, trámite
   largo que hay que empezar mucho antes de ver la convocatoria. (El requisito
   GMC va en la fila marcado como inferencia por la banda salarial, no como
   texto leído.)
3. **Dos nombres para finales de 2027, que valen más que las plazas que los
   revelaron.** **Hanieh Yaghootkar (Southampton HGGM)**: P-0098 y P-0099, dos
   Research Fellow de genética estadística —GWAS y randomización mendeliana— con
   plazos a dos días de distancia, o sea un grupo que contrata en volumen y con
   financiación hasta 2028 y 2030. Las dos exigen doctorado en mano sin cláusula
   de "nearing completion": **inelegible**, y la fila lo dice. Y **Sabine
   Seehagen (Ruhr-Universität Bochum, proyecto NAP)**: el DZPG lo describe como
   el primer centro transdisciplinar de sueño infantil de Alemania, su línea 3.
   La plaza está cerrada (plazo 28-07-2026, HTTP 410 confirma la retirada) y la
   fila se da de alta como **vía de contacto, Fit 3**: el grupo **no tiene brazo
   de genética visible**, que es exactamente lo que ella aporta.

Y una ventana que se cierra sola: la **vacante de residente en la Comisión de
POCT de SEMEDLAB** (ver Buzón). No es empleo, pero es elegible **solo mientras
sea residente, hasta el 22-05-2027**.

## EURAXESS: el bloqueo se ha levantado donde importa, y trae trampa nueva

Se gastó la llamada única prevista **leyendo el cuerpo, no el código de
estado**, que era la lección de la semana pasada. Resultado:

- **El bloqueo de CloudFront ha caído**: `/jobs/search` da 200 con 180.866
  bytes **reales**, sin el cuerpo "Sorry - 498793241", y con 10 enlaces
  `/jobs/<id>` de verdad.
- **La ficha individual `/jobs/<id>` vuelve a leerse** (200, sin 403 ni 307),
  con metadatos completos: Research Field, Researcher Profile R1/R2,
  Application Deadline con hora UTC, Education Level, Years of Research
  Experience y la URL espejo del portal nacional. **Esto restaura la
  verificación Tier 1 de TODAS las filas de origen EURAXESS del radar**, no
  solo las de esta rama. SRC-0268 y SRC-0304 quedan superados.
- **El buscador sigue roto**: `?keywords=statistical%20genetics` devolvió un
  cuerpo **idéntico byte a byte** (mismos 180.866 bytes, mismos 10 ids). La
  paginación `?page=N` funciona a medias: 10 páginas dieron solo 30 vacantes
  únicas y ninguna toca sus líneas.
- **TRAMPA NUEVA, y es peor que la vieja**: el div `id="expiration"` con el
  texto **"STATUS: EXPIRED" está en TODAS las fichas** con
  `style="display:none"`, también en las vivas. Buscarlo por grep da **falso
  positivo en plazas abiertas** (saltó en una de Lund con plazo 27-11-2026 y
  abierta). **La señal honesta es el epoch de `data-date-time`**: 1793573999
  (=2026-11-01, caducada) frente a 1795820399 (=2026-11-27, viva).

La vía rentable a partir de ahora es **cosechar ids desde fuera** (espejo MCAA,
Nature Careers, AcademicTransfer, jobIDs de Varbi) y cerrarlos en Tier 1 por el
epoch, en vez de pelearse con el buscador.

## El ángulo del requisito de titulación: probado y NEGATIVO. No repetirlo semanalmente

Era la grieta que el informe anterior señaló como lo más prometedor sin
estrenar, y se promovió a prioridad en tres ramas. **Resultado honesto: la
búsqueda por frase no rinde.**

- **Rama 1 (UE)**: dos búsquedas de frase ("MD or PhD"/"medically qualified" y
  "nearing completion"/"about to complete") → **cero plazas vivas**. Lo único
  que aceptaba candidatura sin doctorado terminado era una de Queen Mary
  (PRS/GWAS) **cerrada el 31-08-2025**; el resto caducado (Aarhus 2023, Human
  Technopole ene-2025, KCL abr-2025) o fuera de la UE.
- **Rama 2 (tablones)**: `MD+or+PhD`, `medically+qualified` y
  `PhD+nearing+completion` en jobs.ac.uk devuelven **ruido casi puro** (clinical
  lecturers, incluso un lector de estudios rusos y turcos); en el RSS de Nature
  Careers las dos consultas dieron feeds casi idénticos de profesorado genérico,
  lo que demuestra que su `keywords=` es una coincidencia OR muy laxa.

**Conclusión operativa: no montar una búsqueda semanal sobre la frase.** El
ángulo es bueno pero se recorre al revés —buscar su tema y leer luego la línea
de elegibilidad, que es como salió P-0100— o se pide por correo a un PI.

## Lo que cerró: 12 cierres en postdocs y 1 en jobs

**CLOSED**: P-0040, P-0043, P-0059, P-0068, P-0072, P-0074, P-0075, P-0085,
P-0086, P-0091, P-0092, P-0097 y **J-0020** (BridgeBio: la URL de Greenhouse ya
no sirve ficha y redirige al tablón; se interpreta como retirada).

De esos, **cuatro se cerraron por aritmética de fechas, sin fetch** (P-0068,
P-0075, P-0091, P-0092: Fit 1-2 con plazo ya verificado y anterior al 08-11), y
su `Next_Action` lo dice explícitamente para que nadie lo lea como hallazgo.
Los demás se cerraron con lectura real; **P-0097 (QIMR) con su propio texto**
("This position has closed") y **P-0059** con el literal "This job has expired".

**P-0040 cierra con noticia colateral: `fjd.es` YA NO BLOQUEA** (200, 85 KB
legibles tras meses de 403 registrado). Su lista viva tiene 10 convocatorias y
**ninguna de genómica o genética**: se cierra por ausencia en la lista oficial
del centro.

**Dos plazos nuevos y uno ampliado**: **P-0096 EXTENDIDA** (el JSON-LD de
Science Careers da hoy `validThrough 2026-11-16` donde el 01-11 daba
2026-11-09) —sigue abierta, pero **no merece su tiempo**: pide "MD or Ph.D." y
paga 82.000 USD, pero las tareas son psicoterapia y conceptualización de casos
para formarse como psicóloga de salud reproductiva, **cero genética**—;
**P-0069** aparece plazo (2026-12-08) donde decía "no publicado"; y **P-0082**
2027-04-12, anotado **explícitamente como caducidad del anuncio, no plazo de
solicitud**, para que no se lea mal el año que viene.

**Un Fit bajado con evidencia Tier 1: J-0027 (La Rioja/SERIS), de 4 a 3.** La
rama de facultativos solo publica la Resolución de 24-05-2018 (médicos) y
listados de Médico de Familia y urgencias de AP; **no hay lista de su
especialidad**. No se baja más porque la ausencia en la página no prueba
inexistencia.

## El carril clínico español: SESCAM resuelto, BOE todavía no

- **J-0023 (SESCAM), entrando en el PDF y no en el índice, que era la deuda de
  la semana pasada**: **Resolución de 19/10/2026**, 22.ª convocatoria
  **ordinaria de actualización de méritos**, plazo 04-11 a 03-12-2026. El
  apartado Cuarto **la limita al personal YA inscrito**: **no es puerta de
  entrada para ella**. Se cierra además el hueco anterior: los listados
  definitivos de la extraordinaria de mayo 2026 salieron por Resolución de
  13/10/2026. **Ritmo establecido**: ordinaria de méritos cada noviembre (21.ª
  nov-2025, 22.ª nov-2026); entrada de nuevos **solo por extraordinaria**. Su
  ruta real es **la primera extraordinaria posterior al 22-05-2027**. El Fit no
  se ha inflado para que entre en `action_now`.
- **J-0003 (vía transitoria del BOE) sigue PENDING, y ahora con prueba
  diaria**: se leyeron **uno a uno los sumarios del BOE del 02 al 07-11-2026**
  por la API de datos abiertos (200 cada uno) → **cero coincidencias** con
  Genética Médica, Genética Clínica o especialidad de Genética. **Ninguno de los
  dos reales decretos publicado.** El hueco del Consejo de Ministros **no se ha
  podido cerrar**: `lamoncloa.gob.es` da **HTTP 000 (connection reset)** en tres
  rutas y la búsqueda web no halla noticia de aprobación; el documento público
  más reciente sigue siendo el proyecto de 02-10-2026 con la fecha de Consejo de
  Ministros **en blanco**.
- **Sacyl (J-0010)**: solo existe el PDF **FIN MIR_EIR 2026**; la edición 2027,
  que es la suya, **no existe todavía** → vigilar **mensualmente desde enero de
  2027**. Es la vía natural para quien acaba el MIR el 22-05-2027.
- **Osakidetza (J-0009)**: listas definitivas de *F.E.M. - Técnico/a
  Laboratorio Clínico* del 30-10-2026, alzada hasta el 30-11-2026, **ninguna
  resolución nueva** que abra ventana. Sin bolsa permanente: su vía es cazar la
  siguiente apertura tras mayo de 2027.
- **Aragón (J-0016)**: sigue con el nombre antiguo y sin rastro de "Laboratorio
  Clínico". **Tercer patrón de adaptación al RD 101/2025 confirmado** (SESCAM
  desactiva y migra; Sacyl mantiene las dos y actualiza; Aragón no refleja nada).
- SERGAS (J-0008) e ICS (J-0011): páginas vivas pero **sin categorías en el
  HTML** → solo `Last_Verified`.

## Lo que no se pudo verificar o alcanzar, con el error exacto

- **P-0003 y P-0011 → Status UNKNOWN, Confidence UNVERIFIED, y `Last_Verified`
  SIN avanzar.** Las URL de nature.com dan **HTTP 400** (cuerpo de error de
  1.549 bytes) y no son recuperables: el listado HTML con `?keywords=` se
  renderiza en cliente (un curl solo extrae "Refine your search"). **P-0003 era
  la segunda mejor Fit 4 del beat**: necesita navegador o un correo al
  departamento del Icahn.
- **P-0010 NO verificada: CRG devuelve 403** con la URL completa.
- **Seek (Australia): HTTP 403** con cuerpo de 49.934 bytes (interstitial
  antibot, no respuesta vacía) incluso con UA de navegador. Se suma a
  academicpositions.com y findapostdoc.com. Para la vía australiana quedan el
  RSS de Nature Careers, SUB-0032 y SUB-0015.
- **Cardiff por nombre de PI: funciona a medias y se reporta sin adornos.** Los
  nombres (Walters, Rees, O'Donovan, Owen, Isles) sí revelan qué contrata el MRC
  Centre, pero los cuatro anuncios localizados están **cerrados** y las URL de
  ficha del índice están **muertas (404)**. Sirve como inteligencia del centro,
  **no** como feed de vacantes vivas. **No se creó fila**: sin URL viva ni fecha
  verificable, una fila sería peor que ninguna.
- **Erasmus MC sin resolver**: `/en/vacancies` da 404 y
  `werkenbijerasmusmc.nl/vacatures` da 200 pero el listado va por JavaScript.
- **GSK (J-0012)**: 200 y 47 KB pero sin `<title>` ni texto legible (JS) → **no
  se tocó su `Last_Verified`**, no se cuenta como verificada.
- `jobs.vhir.org` legible con dos cosas rozando el perfil, pero los títulos
  vienen por JS y no se obtuvo URL de ficha → **no se inventó fila**.
- **eracareers.pt y kuleuven.be: HTTP 000 con cuerpo vacío** (no completan
  conexión). **Finlandia, Portugal y Bélgica son los tres países UE donde el
  radar sigue ciego.**
- Otros errores fichados para no reincidir: 410 Gone en
  `jobs.ruhr-uni-bochum.de` y en la ficha de `arbeitsagentur.de`; 404 en
  `bna.org.uk/jobs/job/research-associate-30/`; `kcl.ac.uk/jobs?keywords=`
  ignora el filtro (la ruta buena, `/jobs/search?term=`, ya está registrada);
  Workable API **429** (ritmo, no bloqueo); `greenhouse.io/23andme` 404 "job
  board no longer active"; `genomicsengland.co.uk/careers/jobs` 404;
  `neurojobs.sfn.org` **403**; `ki.varbi.com/en/subscribe/` 404; SEMEDLAB
  `ofertas-laborales` 200 **con cuerpo vacío**. CNIO legible y **sin ofertas**
  pre/postdoctorales por segunda pasada.

## Dos trampas de verificación que habrían dado cierres falsos

Además de la del EXPIRED oculto de EURAXESS:

- **El "expired" de la ficha umantis de P-0002 es basura de plantilla JS**
  ("Your session has expired!"), no el estado de la plaza.
- **Los "expired"/"filled" que hacían ambiguos los greps de deCODE (P-0020,
  P-0066) son CSS y JS de la plantilla** del espejo de jobrxiv. Y se verifica
  **el espejo, no deCODE**: sigue sin vía Tier 1, así que su Confianza tope es
  **LIKELY**.
- **Hallazgo de método reutilizable en el Broad**: Avature **indexa nombres de
  PI y de laboratorio**, así que reverificar una ficha cuesta **1 llamada**
  (`/McCarroll` → 1 resultado exacto). Negativo registrado para que nadie lo
  repita: `/Stanley%20Center` devuelve 1 resultado irrelevante, o sea que **no**
  indexa centro de adscripción.

## Deuda del Broad: cerrada

`/careers/SearchJobs/postdoctoral` = 12 resultados en 2 páginas, **las dos
leídas**. **P-0008 (ref 44407), P-0035 (44829) y P-0081 (44254) siguen las tres
ABIERTAS**; también vivas 42892 (P-0071) y 45073 (P-0080). **Ninguna vacante
nueva del Broad es de genética estadística o psiquiátrica → cero filas nuevas
allí, a propósito.**

## Buzón

Conector **disponible para lectura y usado**. Pasada A (`label:Research
newer_than:8d`): **cero hilos** —la etiqueta sigue a 0 mensajes porque no hay
ninguna suscripción de alertas real dada de alta—. Pasada B (la consulta única
del contrato): **4 hilos, los 4 triados**. **Ninguno de los nueve dominios
vigilados escribió esta semana**; todo vino de LinkedIn y de un Substack.

Lo único aprovechable, y es la ventana más perecedera de la pasada: un resumen
de red del 06-11 trae que una vocal de la junta directiva de **SEMEDLAB**
anuncia **vacante de residente en la Comisión de Pruebas en el Lugar de Atención
al Paciente (POCT)**. No es empleo ni dinero —por eso **no genera fila de
plaza**—, pero es un puesto de representación en un grupo de trabajo de la
sociedad científica de **su propia especialidad**, y es elegible **solo mientras
sea residente, hasta el 22-05-2027**. SEMEDLAB es además la sociedad detrás de
la Fundación José Luis Castaño (SRC-0093), la fuente que más plazos útiles ha
dado al radar. **Falta todo lo operativo**: el correo está truncado y no publica
plazo, requisitos, número de plazas ni contacto. Ruta **ECOSYSTEM, PENDING**:
ecosistema es el backstop del lunes y debe abrir la publicación de LinkedIn.

Las otras tres son IGNORE/DONE, incluido **un duplicado del 04-11 del mismo
resumen, registrado a propósito** para que el duplicado no se cuente como
oportunidad distinta ni se reabra la semana que viene. **Privacidad respetada**:
nada personal leído, citado ni registrado.

## Filas suyas cuyos hechos cambiaron bajo ella

**Ninguna.** `data/owner_status.json` sigue siendo `{}`: la dueña no ha marcado
todavía ninguna fila, así que no hay ningún modelo mental que se haya quedado
obsoleto con los 12 cierres de esta pasada. Dicho de otro modo: **las 55 filas
actualizadas no pisan ninguna decisión suya, porque aún no hay decisiones.**

## Suscripciones

**45 filas, las 45 PENDING** por la definición del contrato (TSV en TODO y sin
marca en `owner_status.json`). Dos altas nuevas: **SUB-0044**, canal RSS
`jobsrss` de Nature Careers —verificado funcionando hoy, y **la única forma
fiable de que una fila de Nature Careers siga siendo verificable visto que sus
URL de ficha mueren con 400**— y **SUB-0045**, membresía y lista de IGES
(sociedad de su línea 1, tablón de bajo volumen que se vigila mal por rastreo y
bien por correo; sin URL de formulario porque no se abrió la página de alta).

**Una propuesta se perdió por el tope de 2 por pasada y se deja aquí para no
perderla: alerta por correo de SfN NeuroJobs** (`neurojobs.sfn.org`), que es el
**único rodeo al 403** de ese tablón, mismo patrón que funcionó con ESRS
(SUB-0042). Vale la pena darla de alta la semana que viene.

Dos ramas propusieron **cero suscripciones a propósito**, y la razón es la
correcta: no tenían URL de alta que hubieran leído de verdad (alerta de la RUB,
búsqueda guardada de KCL, Varbi de KI con `/en/subscribe/` en 404) y las reglas
de honestidad prohíben inventarla. **Mejor cero filas que una URL supuesta.**

## Fuentes nuevas: 21

Lo más aprovechable: **la ficha individual de EURAXESS con el epoch de
caducidad** (restaura Tier 1 para todo el radar), las **tres rutas del Broad**
—incluida `/Stanley%20Center` **como resultado negativo** para que nadie la
repita—, el **PDF de convocatoria del SESCAM** (que es lo que resolvió el
hallazgo: el índice no podía responderlo), la consulta
`jobs.ac.uk ?keywords=genetic+epidemiology&sortOrder=1` (9 resultados, la más
rentable de la pasada: de ella salen las tres altas de la rama 2) y
`neurojobs.sfn.org` **dada de alta con el bloqueo documentado**, que es
precisamente su valor. Dominios que el radar no había tocado nunca:
`jobs.ruhr-uni-bochum.de`, `epsy.psy.ruhr-uni-bochum.de`,
`arbeitsagentur.de/jobsuche`, `bna.org.uk/jobs`, la rama de facultativos del
**SERIS**, el índice de referencias del **Consejo de Ministros** (anotado *con*
el HTTP 000) y el tablón de Workable de **Our Future Health**. Las cinco ramas
estrenaron fuente; ninguna tuvo que declarar que buscó y no encontró.

## Dos avisos de herramienta, y los dos son deuda mía, no de las ramas

1. **`rebuild_action_now.py` extrae fechas de la PROSA de la columna
   `Deadline`.** J-0023 (SESCAM) entró esta pasada como **rank 1** de su lista
   de acción porque su `Deadline` era un párrafo que contenía "03-12-2026", y el
   selector lo leyó como plazo —cuando ese plazo es justo el que **la excluye**,
   por estar limitado al personal ya inscrito—. El contrato es explícito: una
   fila para la que no es elegible **no se acerca a `action_now`**. Se corrigió
   **vaciando esa celda de fecha**, no tocando el Fit (eso sería la edición
   cosmética que el contrato prohíbe): los hechos verificados —resolución,
   ventana, PDF— **ya estaban íntegros** en `Source_Note` y `Requirements_Key`,
   así que no se perdió ni un dato. **Pero el problema es estructural: 12 filas
   (6 de postdocs y 6 de jobs) tienen prosa con fechas dentro de `Deadline`**
   —P-0002, P-0021, P-0040, P-0050, P-0071, P-0082, J-0003, J-0015, J-0016,
   J-0023, J-0025, J-0031—, y cualquiera puede repetir el falso positivo.
   Arreglarlo de verdad es trabajo de la dueña, porque toca los generadores.
2. **El fichero de reverificación que genera el orquestador truncaba las URL a
   100 caracteres**, y eso **casi provocó un cierre falso de P-0010** (la rama
   recibió un 404 por URL cortada antes de descubrir que la buena da 403).
   Defecto mío de esta pasada; no debe repetirse.

## Regla de los 60 KB

Sigue incumplida y creciendo: **`postdocs.tsv` 213,8 KB** (196,5 la semana
pasada), **`jobs.tsv` 102,3 KB** (106,6; baja solo porque se vació la prosa de
una celda), `sources.tsv` 353,4 KB y `changelog.tsv` 474,3 KB. **No los parto
yo**, como manda el contrato: partir un fichero obliga a cambiar
`tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit y eso no es
trabajo para el final de una pasada desatendida. **Quinta semana dicho.**

## El aviso sobre `action_now`, quinta semana y la decisión es suya

`action_now` se queda con **una sola fila mía, J-0003**, y es la regla aplicada
correctamente: entra por ser Fit 5 con `Competition_Level = LOW`, no por plazo.
El efecto estructural no ha cambiado: **hay nueve filas de Fit 4 de su vía
clínica española —su prioridad número 2— que la regla no puede surfacear
nunca**, porque son bolsas permanentes (ROLLING, sin plazo) y la regla solo
admite sin plazo lo que es Fit 5: J-0002 (SAS), J-0007 (FIMABIS), J-0008
(SERGAS), J-0010 (Sacyl), J-0011 (ICS), J-0016 (Aragón), J-0023 (SESCAM),
J-0027 (La Rioja, ahora Fit 3) y J-0028 (Cantabria). Y **P-0002, la mejor acción
de la base, tampoco entra** por ser ROLLING sin plazo. La decisión es de diseño
y es suya: o sube alguna a Fit 5, o la regla necesita una cláusula para plazas e
inscripciones permanentes.

## Qué perseguiría la semana que viene con más presupuesto

Por orden de rentabilidad: **cosechar ids de EURAXESS desde fuera y cerrarlos
en Tier 1 por el epoch**, ahora que la ficha se lee y el buscador no sirve;
**recuperar P-0003 por el dominio del Icahn**, que es la mejor Fit 4 que se ha
quedado sin verificar; **Avature del Broad por nombres de PI del Stanley Center**
(Neale, Daly, Sullivan, Hultman), ahora que se sabe que indexa PIs; **entrar en
los formularios de solicitud de SERGAS, ICS y `bolsaabierta.saludcastillayleon.es`**,
único sitio con la lista real de categorías, y cerrar Extremadura y Canarias
(J-0021); las **fichas de `jobs.vhir.org`** por WebFetch, única puerta viva a
CIBERSAM; el **listado real detrás de `werkenbijerasmusmc.nl`** y las rutas
finlandesa, portuguesa y belga, que son los tres huecos ciegos de la UE; el
**MSL de diagnóstico de laboratorio de Beckman Coulter/Inizio Engage** para
España y Portugal, la pista de comunicación científica más cercana a su perfil
que se vio sin tiempo de confirmar; **correo especulativo a Seehagen y al
Netherlands Twin Register**, que no se resuelven con fetch; y las consultas de
rol sin tocar ("staff scientist", "junior group leader") más los plazos de 2027.
