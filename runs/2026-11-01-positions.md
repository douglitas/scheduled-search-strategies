# positions — 2026-11-01

**ALERTA, capacidad caída (segunda semana): EURAXESS sigue cerrado, y ahora
MIENTE.** `euraxess.ec.europa.eu/jobs/search` ya **no** devuelve 403: devuelve
**HTTP 200**. El cuerpo, sin embargo, son 40 KB de plantilla ECL de la Comisión
cuyo único texto propio es `Sorry - 498793241`, con cero enlaces `/jobs/<id>`,
cero títulos y ningún endpoint de API. Los espejos nacionales siguen cortados
(`euraxess.es` 403, `.de` y `.se` 429). **Consecuencia operativa, y es la
trampa más cara de la semana: comprobar EURAXESS por código de estado ya no
vale, hay que leer el cuerpo.** Quien lo mire la semana que viene y vea un 200
va a creer que el bloqueo cayó. No cayó. La superficie EU sigue sin cobertura
automática y **SUB-0002 y SUB-0018 (alertas por correo de EURAXESS) siguen
siendo la única vía posible a todo el portal europeo.**

Perfil completo (sin `PROFILE-INCOMPLETE` ni `[TODO]`). Checkout correcto en
`main`, árbol limpio, remoto el que debe ser. No existía informe de hoy: no fue
un re-disparo, y no apareció ningún commit ajeno de `positions` fechado hoy.
Las cinco ramas entregaron; ninguna se quedó sin presupuesto salvo donde se
dice. Push directo a `main`, sin rechazo y sin rama de desvío.

## Recuento, tomado de `git diff --stat HEAD~1`

| fichero | cambio |
|---|---|
| `data/postdocs.tsv` | 5 altas (P-0093…P-0097), 36 filas actualizadas |
| `data/jobs.tsv` | 1 alta (J-0031), 17 filas actualizadas |
| `data/sources.tsv` | 18 fuentes nuevas (SRC-0377…SRC-0394) |
| `data/subscriptions.tsv` | 1 alta (SUB-0039) |
| `data/inbox_triage.tsv` | 1 fila |
| `data/action_now.tsv` | 1 fila mía (J-0003), 43 ajenas preservadas |
| `data/changelog.tsv` | 59 apuntes |

139 inserciones y 54 supresiones. **Las 54 supresiones son exactamente las
mitades `-` de las 53 filas de datos modificadas más la fila de `action_now`:
no se perdió ninguna línea.** Comprobado fila a fila contra `HEAD~1`:
`Owner_Status` intacto en las 122 filas preexistentes, ninguna fila
desaparecida, cabeceras idénticas, anchuras de columna uniformes en los siete
ficheros y ningún `Fit_1_5` mal formado.

**Esta pasada fue de verificación, no de descubrimiento, y el reparto lo dice:
53 filas reverificadas frente a 6 altas.** Era lo que tocaba — había 21 plazos
venciendo entre el 25-10 y el 06-12 y tres deudas abiertas.

## Las tres cosas que merecen acción

**1. P-0002 (Max Planck Nijmegen, Statistical Genomics / Genetic Epidemiology)
es AHORA la mejor fila del radar para su reloj, y llevaba tres meses abierta
sin que nadie leyera la frase que la hace valiosa.** Fit 4, VERIFIED hoy, viva
y con el botón de solicitud activo desde el 12-08-2026. La ficha dice
literalmente, en `What we offer you`: *"The proposed starting date is 1
December 2026 although the start date is negotiable"*. **Inicio negociable es
exactamente la única puerta que deja abierta su calendario** (no se libera del
MIR hasta el 22-05-2027 y no defiende hasta febrero de 2028), y es además su
línea 1, genética estadística. 3 años, 39 h, salario TVöD E13.
**Acción: escribir preguntando hasta dónde se puede diferir ese inicio.** Es un
correo, no una candidatura, y es el movimiento de mayor valor esperado de toda
la base ahora mismo. Aviso técnico fichado: las cadenas `expired` / `no longer`
del HTML son del diccionario estándar de umantis, **no** avisos de cierre, así
que no se lea esa página como vencida.

**2. P-0079 (Karolinska, KI-PGI) NO cerró: el plazo se amplió del 30-10 al
2026-11-08.** Es la plaza que mejor encaja en contenido de todo el repo — pide
literalmente GWAS, PRS y diseños familiares sobre registros suecos o UK
Biobank, que es su línea 2 exacta — 2 plazas de 2 años prorrogables,
financiación NIH, **inicio «según acuerdo»**, ref. STÖD 2-4050/2026.
Sigue en Fit 3 **por reloj, no por perfil**, así que la jugada no cambia: no es
presentarse, es **escribir a Anna Kähler (`anna.kahler@ki.se`, contacto
confirmado en la ficha) y a Lu Yi**, con el inicio «según acuerdo» y la cadencia
2027-28 como gancho. Lo que cambia es que ahora hay una plaza ABIERTA siete días
más como excusa para el correo, en vez de una cerrada.

**3. J-0003 queda resuelto, y la respuesta es que NO se ha publicado nada: la
bisagra frente al 22-05-2027 sigue entera.** Verificado por tres vías Tier 1:
(a) en «Proyectos abiertos» del Ministerio **ya no hay ningún proyecto de
genética** — el único abierto es el PRD de Listas de Espera (DG/80/26); (b) en
`audienciasCerradasSan.htm` los dos proyectos constan como **audiencias
cerradas** con sus fechas 02-10 → 26-10-2026 y sus dos PDF, o sea que **cerraron
en plazo, sin prórroga y sin retirada**; (c) la **API de datos abiertos del BOE**
devuelve los sumarios completos del 27 al 31-10-2026, **1.252 ítems, cero
coincidencias de «genética»**. La fila pasa de OPEN a **PENDING** con Fit 5
intacto, y su `Next_Action` está reescrito porque el anterior («envía
alegaciones») vencía el 26-10.
**Por qué sigue siendo la fila más valiosa de la base:** la fecha de entrada en
vigor decide su régimen. Antes del fin de su residencia = apartado 4 (en
formación, prueba siempre). Después = apartado 3 (ya titulada, posible acceso
directo sin prueba). Lo accionable ahora son dos cosas pequeñas: **darse de alta
en los avisos del Ministerio** (URL verificada hoy:
`listas.sanidad.gob.es/listasDistribucion/anonimoSuscriptor.do?metodo=detalleForm&CListId=29`)
y **adelantar ya el certificado de ejercicio en unidad U.78 con Código Nacional
Normalizado**, que es el documento lento. No verificado y se dice: no se
consultaron las referencias del Consejo de Ministros, por presupuesto.

## El hallazgo transversal: el muro del reloj tiene una grieta, y no es el doble grado

Nueve semanas diciendo que las altas no pasan de Fit 3 porque exigen doctorado
concluido. Esta semana se probaron las dos salidas candidatas y **una falla y
otra funciona**:

- **El doble grado RA/Research Associate NO sirve, y conviene enterrarlo.**
  Leída la letra exacta de **P-0084** (Cambridge, lab Malpetti, ON-FIRE), el
  grado inferior exige haber **DEPOSITADO** la tesis (*"submitted but not yet
  received"*), no estar matriculada. Flexibiliza el hueco entre depósito y
  lectura, no el requisito de doctorado, y ella no deposita antes de feb-2028.
  Segundo motivo independiente: el contenido es bioestadística de biomarcadores
  en demencia frontotemporal (SIMOA, NULISA, multiómica) — encaja la caja de
  herramientas, **no es genética estadística ni GWAS ni PRS**. Se queda en Fit 3.
  Datos verificados: 33.002–46.049 GBP, ref. RR51453, `jobs.cam.ac.uk/job/57512`,
  exige Research Passport del NHS. **Criterio de cribado derivado y vinculante
  para las próximas pasadas: un doble grado solo sirve si el escalón inferior
  pide «enrolled» o «nearing completion», nunca si pide «submitted».**
- **Lo que SÍ funciona: buscar por el REQUISITO DE TITULACIÓN en vez de por el
  tema.** La única alta de la semana con valor estructural es **P-0096 (Baylor
  College of Medicine, Reproductive Psychiatry)**, y no por la plaza — es un
  falso positivo clínico sin una línea de genética, Fit 2 — sino porque su
  requisito es **«MD or Ph.D.», con el MD como alternativa suficiente y sin
  experiencia mínima**. Es el **primer precedente documentado en el repo de un
  postdoc cuyo requisito de titulación ella cumple HOY**, compatible con una
  incorporación a mediados de 2027. **Propongo convertirlo en ángulo estable de
  búsqueda: «MD or PhD», «medically qualified», «nearing completion».** Es el
  único eje que esquiva el muro, y es un ángulo que el contrato no contempla
  todavía.

Heurística barata que sale del feed de Max Planck y que vale para las tres
rutinas: **grepear los feeds por años futuros en el título** («2027-29») para
encontrar convocatorias con inicio diferido. Se vio una `Call for Postdoctoral
Fellowships (2027-29)` que no se fichó a propósito, porque sin abrir la ficha
habría habido que inventar institución y detalles.

## Lo que cerró

Siete cierres, y cada uno con su prueba:
- **P-0058, P-0067, P-0076** (Oxford, Cambridge, Imperial): `status=archive` en
  el JSON-LD, fechas coincidentes. Sin ambigüedad.
- **P-0070 (Oslo/Ahus)**: abierta por fin la ficha Tier 1 Jobbnorge 309329 →
  **404, `Annonsen er ikke tilgjengelig`**. Estaba viva solo en un fósil:
  `careers.iscb.org` sigue anunciándola. **El tablón de la ISCB no retira
  entradas cuando el portal de origen las baja** — contradicción única de la
  pasada, resuelta a favor del origen.
- **P-0054 (Lunenfeld)**: de UNVERIFIED sin fecha a **CLOSED VERIFIED con plazo
  2026-05-01**, leído del PDF oficial con `pdftotext`.
- **P-0052 (Bonn)**: CLOSED confirmado, LinkedIn ya no sirve la ficha.
- **P-0037 (NIH), fuera del limbo por fin y con etiqueta honesta.** Cuarto
  intento en seis semanas, 403 de Cloudflare reconfirmado hoy. Pasa a **CLOSED
  con Confidence UNVERIFIED**, cerrada por caducidad presunta (el inicio
  prometido era verano de 2026, ya pasado), y su `Next_Action` dice que solo lo
  resuelve una persona con navegador. Era la recomendación de la semana pasada y
  queda ejecutada: **no se vuelve a pagar el intento cada lunes.**

Y dos plazos **ampliados**, que es lo contrario de un cierre y por eso importa
no haberlos dado por muertos: **P-0036 (KCL, Maternal Sleep) 02-11 → 23-11**,
verificado por duplicado (texto y JSON-LD) y corroborado de forma independiente
por dos ramas distintas; y **P-0079 (Karolinska) 30-10 → 08-11**.

## Lo que no se pudo verificar o alcanzar

- **El rebarrido de CCAA por «Laboratorio Clínico» se hizo y da un resultado
  incómodo: no se puede cerrar desde las URL guardadas.** SAS, SERGAS, ICS,
  SESCAM, IB-Salut, SERIS y Murcia responden 200 pero **sus páginas índice no
  nombran ninguna categoría**, ni la nueva ni la vieja: el listado vive dentro
  de la aplicación de bolsa o en PDF sueltos. En las siete se dejó
  `Last_Verified` quieto. El falso negativo que el RD 101/2025 creó **sigue sin
  poder descartarse** en esas siete.
- **Cardiff queda sin vía automática.** Con el eploy ya fichado como inútil, se
  atacó el dominio propio: `cardiff.ac.uk/mrc-centre-neuropsychiatric-genetics-genomics`
  da **403 a curl y a WebFetch**. Solo navegador, o búsqueda por nombre de PI
  (O'Donovan, Owen, Walters).
- **Broad: P-0008, P-0035 y P-0081 no son verificables por fetch.** Sus fichas
  `/en_US/careers/JobDetail/...` devuelven cascarón JavaScript («Expired
  session») sin JSON-LD. Anotado en las tres filas; no se les subió
  `Last_Verified`.
- **deCODE: ruta nueva probada y fallida.** `careers.amgen.com/api/jobs` con
  `keywords=` y con `location=` devuelve **el mismo HTML de 98 KB de la SPA**:
  no es una API. **P-0020 y P-0066 siguen UNVERIFIED.**
- **P-0074 (Leicester DTF573)**: la ficha devuelve 2.708 bytes de JavaScript
  empaquetado sin JSON-LD, en dos intentos. Su plazo era hoy y aun así queda
  **OPEN/UNVERIFIED sin tocar `Last_Verified`**: no se sella un cierre que no se
  ha leído.
- **Deuda de la rama 4, declarada con nombre y apellido y sin sellar ningún
  `Last_Verified` en falso:** J-0013 (PharmaGenesis, 3ª semana, portal Eploy
  vivo pero sin títulos legibles), J-0019 (IQVIA, 3ª semana, sigue sin
  `Last_Verified`), J-0012 (GSK, cáscara JS sin JSON-LD), J-0022 (Genomics,
  tablón Ashby con JS).
- **De Madrid (J-0004) no se afirma nada esta semana**: su URL guardada
  (`comunidad.madrid/servicios/empleo/oferta-empleo-publico-servicio-madrileno-salud`)
  da **404**.
- Vías muertas respetadas sin gastar presupuesto: Cantabria (J-0028 intacta,
  Fit 4 UNVERIFIED y sin `Last_Verified`, que es lo honesto), Asturias (J-0017
  intacta, 5ª semana), Canarias (J-0021 congelada), Erasmus MC (no tocado,
  tarea cerrada la semana pasada), P-0040 (IIS-FJD, ninguna llamada gastada —
  **se recomienda aparcarla**).
- **Una acción de la rama 1 fue denegada por el clasificador del modo
  automático**: intentó releer Jobbnorge y la ficha del MPI con User-Agent de
  navegador y se bloqueó como circunvención de control antibot. La rama repitió
  con curl plano, obtuvo ambas páginas igual y no buscó rodeo. Se registra
  porque es un límite real del entorno, no un fallo de la fuente.

## Las dos deudas de la semana pasada, cerradas con respuesta definitiva

- **HigherEdJobs no estaba pendiente: está BLOQUEADO, y el endpoint nunca fue
  el problema.** Probados cinco (`/search/default.cfm`,
  `/search/advanced_action.cfm`, `/search/listing.cfm`, `/faculty/search.cfm`,
  `/search/?Keyword=`): los cinco dan 200 con cuerpos de 212–932 bytes que
  dicen `Request unsuccessful. Incapsula incident ID`. La raíz del dominio hace
  lo mismo: es **Imperva/Incapsula sobre el dominio entero**. Esto cierra
  también para siempre la suscripción de HigherEdJobs. **Hay que corregir la
  columna Notes de SRC-0036**, que tal como está invita a reintentarlo cada
  lunes.
- **ISCB página 2: recorrida. Es la cola de septiembre** — ocho anuncios, todos
  del 2 al 15 de septiembre, ninguno en sus líneas. Con 50 por página y orden
  descendente, la página 1 agota lo nuevo en una pasada semanal: **no hay que
  volver a la 2.**

## Resultados en negativo, para no volver a pagarlos

- **KCL (deuda pagada):** `kcl.ac.uk/jobs/search?term=` funciona y da el plazo
  en el propio listado. Términos genetics/genomics/sleep/psychiatry → **cero de
  genética estadística o psiquiátrica, cero del SGDP Centre**. El único postdoc
  de investigación del IoPPN (job 161985, £45.829, cierra 12-11) es coordinación
  de un ensayo de eye-tracking en TDAH infantil: abierto y descartado.
- **Edimburgo (alcanzada por fin, vía API Oracle):** `genetics` 7, `genomics` 4,
  **`psychiatr` 0, `sleep` 0**. Las siete «genetics» son acuicultura (×2),
  transmisión animal, un stores manager, dos ECAT veterinario/clínico y
  mariposas. **Nada de genética psiquiátrica.**
- **Karolinska:** ~100 vacantes revisadas; aparte de P-0079 y P-0092, **nada de
  GWAS/PRS**.
- **Broad: décima semana sin nada de genética estadística o psiquiátrica**
  (búsqueda `genetics` → 6 anuncios, solo Talkowski, ya fichado).
- **QIMR: 3 vacantes, una fichada (P-0097, Fit 2). VU Amsterdam: ~10 vacantes,
  CERO del Netherlands Twin Register** (los dos de neuroimagen exigen autonomía
  que ella solo tiene a nivel supervisado).
- **jobs.ac.uk agotado:** `polygenic` → 3 (los útiles ya fichados),
  `psychiatric genetics` → 2 doctorados, `complex traits GWAS` → **cero** (con
  tres palabras parece exigirlas todas).
- **Australia: cero, y el instrumento no sirve.** THEunijobs tiene **12
  anuncios en total** (astrofísica, combustión, ciencias de la Tierra). **Se
  recomienda bajar la prioridad de SRC-0125 y reasignar Australia a QIMR o a la
  rama 3.**
- **MSL/MedComms: la búsqueda que faltaba se hizo.** El mercado MSL español es
  **denso** (35–96 vacantes según mes y agregador: CSL-Seqirus, Dexcom, LEO,
  BeOne, Santen, Terumo, IQVIA) pero **todo Tier 2 y todo con incorporación
  inmediata**, así que lo hunde el reloj, no el perfil. Fichada **una sola**
  fila, **J-0031 (Seqirus MSL Vaccines Spain, Fit 2, UNVERIFIED, sin
  `Last_Verified`)**, y su valor es el patrón, no la vacante.
  «statistical geneticist» / «computational genetics» / «genetic
  epidemiologist» en España: **cero**.
- **J-0015 (Porterhouse) sí se cerró, y con cambio real:** desaparecieron las
  dos plazas de Senior Medical Writer; solo quedan tres programas Pathfinders,
  que son prácticas formativas y **por contrato de ámbito no se fichan como
  filas** (eso es formación, no empleo).
- **Línea 3 (genética del sueño infantil) sigue siendo EL agujero del radar.**
  Lo único alcanzado fue el Saxena Lab: «Opportunities in the Lab: Coming
  Soon!», cero plazas. El Pediatric Sleep Council **no tiene tablón**
  (`pediatricsleepcouncil.org` 000, `babysleep.com` sin un solo enlace de
  empleo), `www.esrs.eu/paediatric-sleep/` da 403, y el canal más cercano
  encontrado (ICIS) no tiene nada de genética ni de sueño.
- Otros ceros: `epiresearch.org/job-bank/` es **404** (el vivo es
  `/membership/ser-careers/`, sin anuncios en HTML); el archivo de Young
  Epidemiologists en Google Sites no tiene ni una fecha de 2026; el wp-json de
  la SEE no da ofertas nuevas desde el 15-10-2026; el feed de Max Planck (30
  ítems) no trae nada de sus líneas; cosecha cero en uu/lu/umu.varbi.

## Trampas de verificación fichadas esta semana

Han sido muchas y varias **corrigen el propio briefing**, así que conviene
leerlas antes de la próxima pasada:

- **El patrón de JSON-LD del briefing falla en Nature Careers y Science Careers
  por un espacio.** Ambos usan plataforma Madgex y sirven `"datePosted": "..."`
  **con** espacio, así que el grep devuelve vacío y hace creer que no hay
  JSON-LD. Hay que usar `'"(campo)" *: *"'`. **Con esa corrección se
  desatascaron dos filas que llevaban semanas en LIKELY.** Aviso: estas fichas
  no llevan `status=live/archive`, solo `validThrough`.
- **En jobs.ac.uk, poner un User-Agent de navegador DISPARA el reto de
  JavaScript**; el UA por defecto de curl sirve la página real (2.781 vs 73.156
  bytes). Es al revés de lo habitual.
- **El listado de Varbi no es fiable para plazos.** `ki.varbi.com/en/` da
  **2026-11-01** para P-0079 frente al **2026-11-08** de su ficha, y el mismo
  desfase de un día en P-0092 (listado 03-11 vs. ficha 02-11). **Para un plazo
  que importa, hay que abrir la ficha.** Queda sin reconciliar el desfase de
  P-0092.
- **`jobs.mpg.de` NO EXISTE** (HTTP 000, no resuelve; no es bloqueo). El tablón
  real es `www.mpg.de/jobboard`.
- **Varbi sueco, medio patrón es falso:** `gu.varbi.com`, `liu.varbi.com` y
  `slu.varbi.com` dan **404 con 703 bytes**; solo `uu`, `lu` y `umu` responden.
- **Dinamarca entera inalcanzable:** `employment.ku.dk` 000, `jobportal.au.dk/en/`
  000, `www.au.dk/en/about/vacancies/` 404.
- **Jobbnorge no admite `?keyword=`** (404): hay que barrer el listado y filtrar
  en local.
- **Human Technopole: dos 404 que mienten** — `/en/work-with-us/` y
  `/en/job-openings/` devuelven 404 sirviendo 78 KB de página completa. Y
  `careers.humantechnopole.it` es JavaScript puro, por eso **P-0043 se queda en
  LIKELY y no sube a VERIFIED**: su plazo 2026-11-04 está reconfirmado, pero por
  Nature Careers, que es Tier 2.
- **El buscador HTML del BOE es inservible**: `boe.php` da **400** con
  parámetros de campo y 200 con un formulario vacío de 8,5 KB. **Usar la API de
  datos abiertos.**
- **El truco wp-json de sociedades (SRC-0235) no vale para ICIS**: ignora los
  anuncios de empleo y solo da entradas editoriales. Hay que parsear el
  `<article>` de la página de categoría. Sin eso se concluiría «cero anuncios»
  por error.
- **`jiscmail.ac.uk/lists/ALLSTAT.html` da 403**: ALLSTAT no se lee por scraping.
- `navarra.es/es/tramites/...` da **000** (se suma a Cantabria y Asturias).
- `jobs.gsk.com` y los tablones **Ashby**: sin JSON-LD.

## Buzón

El conector de Gmail **funcionó** y se hicieron las dos pasadas exactas, ni una
más. **Pasada A (`label:Research newer_than:8d`): cero**, y sigue sin ser un
fallo — la etiqueta está vacía porque ninguna suscripción está activada.
**Pasada B: un único hilo, y esta vez NO es falso positivo.** Dentro, un digest
de red del 26-10-2026 trae que la **Fundación de SEMEDLAB (Sociedad Española de
Medicina de Laboratorio, la sociedad de su propia especialidad)** anuncia
**Convocatoria de Ayuda para un Proyecto de Investigación Multicéntrico**.

**Entregada 1 fila de `inbox_triage`: Route=FELLOWSHIPS, Status=PENDING.** Es
financiación, no plaza: no es mi beat y no la puedo cerrar yo. **Queda ese único
PENDING para que lo herede `ecosystem`**, que es el backstop de la mañana. El
gancho para resolverlo: cruzar la publicación con
`fundacionjlc.es/becas-premios-convocados/` (SRC-0093) y `semedlab.es`, porque
el digest no publica cuantía, plazo ni bases.

Criterio nuevo fichado: el mismo digest traía una publicación de QIMR Berghofer
que casa con «Medical Research Fellowship», pero es una **felicitación por una
ayuda ya concedida**, no una convocatoria. No fichada: **falso positivo con
remitente institucional**, que es una categoría nueva a vigilar.

**No se etiquetó nada, y es deliberado:** el único hilo útil es un digest
genérico que entra todas las semanas con contenido distinto y casi siempre
irrelevante; etiquetar el contenedor degradaría la etiqueta `Research`. No queda
ningún id de hilo pendiente de etiqueta. **No se creó ningún borrador, no se
respondió y no se envió nada.** `source_inbox.json` comprobado y vacío (`[]`):
ninguna URL suya que resolver, segunda semana a cero. Privacidad respetada: no
se registra nada más del buzón.

## Filas suyas cuyos hechos cambiaron bajo ella

Ninguna. `owner_status.json` sigue vacío (`{}`): ni una fila marcada READ,
IN_PROGRESS, APPLIED, RESOLVED, DISCARDED ni REVISIT, así que todo lo tocado
estaba en NEW o sin marca y no hay ningún modelo mental que se haya quedado
obsoleto. **Décima semana de radar y ninguna decisión registrada**, que es el
dato que explica por qué la Pasada A del buzón sale vacía cada lunes.

## Suscripciones

**39 pendientes: las 39 filas del fichero están en TODO y `owner_status.json`
está vacío.** El cuello de botella sigue siendo la activación, no el
descubrimiento, y con EURAXESS caído eso ya no es una observación de estilo:
**SUB-0002 y SUB-0018 son la única vía posible a todo el portal europeo.**

Una sola alta, **SUB-0039**, y por un motivo concreto que la distingue de las 38
anteriores: **el feed RSS de Max Planck (`www.mpg.de/feeds/jobs.rss`) no
necesita darse de alta.** Responde 200 y entrega las 30 vacantes de toda la red
en XML limpio en una llamada. Con 38 formularios sin rellenar en diez semanas,
una URL que ya funciona no tiene ese problema. **Cero suscripciones más**, y es
deliberado: ninguna rama encontró otra URL de alta verificable, y la regla
prohíbe inventarla. La única que se habría querido (archivo de ALLSTAT) murió en
el 403. Dato útil para corregir SUB-0027: la URL de alta de los avisos del
Ministerio, verificada hoy, es
`listas.sanidad.gob.es/listasDistribucion/anonimoSuscriptor.do?metodo=detalleForm&CListId=29`.

## Fuentes nuevas

18, y como siempre la mitad valen por documentar un callejón. Las de peso:
**el feed RSS de Max Planck** (30 vacantes de toda la red en una llamada); **la
API de datos abiertos del BOE** (`boe.es/datosabiertos/api/boe/sumario/AAAAMMDD`
con `Accept: application/json`), que es la que resolvió J-0003 con 1.252 ítems
en una llamada y sustituye al buscador HTML roto; **`audienciasCerradasSan.htm`**,
que responde lo que la página de proyectos abiertos no puede — que un proyecto
cerró en plazo y no se retiró; **el endpoint de DETALLE de QIMR TurboRecruit**
(`/job/job_details.cfm?id=<id>`, requisitos verbatim, salario y PI; truco:
borrar los `<script>` antes de pasar a texto); **el buscador real de KCL**
(`/jobs/search?term=`), que paga la deuda del índice de categorías; **la API
Oracle de Edimburgo**; **los tres Varbi vivos**, donde `uu` resuelve la trampa
fichada de `uu.se` que ocultaba ~80 vacantes tras «Show more hits»; **la
corrección del patrón JSON-LD de Madgex**; y **ICIS**
(`infantstudies.org/category/job-postings/`), el canal más cercano a su línea 3
hasta ahora aunque hoy no tenga nada de genética. Fichadas explícitamente como
**rutas muertas para que nadie las reintente**: `careers.amgen.com/api/jobs`,
el dominio propio del MRC Centre de Cardiff, HigherEdJobs completo,
`epiresearch.org/job-bank/` y ALLSTAT.

## Regla de los 60 KB

Sigue incumplida y creciendo: **`jobs.tsv` 106,6 KB** (98,2 la semana pasada),
**`postdocs.tsv` 196,5 KB** (187,4), `sources.tsv` 297,9 KB y `changelog.tsv`
417,9 KB. **No los parto yo**, como manda el contrato: partir un fichero obliga
a cambiar `tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit y eso
no es trabajo para el final de una pasada desatendida. **Cuarta semana dicho.**

## El aviso sobre `action_now`, que sigue vigente y la decisión es suya

`action_now` se queda otra vez con **una sola fila mía, J-0003**, y es la regla
aplicada correctamente, no un fallo. El efecto estructural no ha cambiado: **hay
nueve filas de Fit 4 de su vía clínica española —su prioridad número 2— que la
regla no puede surfacear nunca**, porque son bolsas permanentes (ROLLING, sin
plazo) y la regla solo admite sin plazo lo que es Fit 5. J-0002 (SAS), J-0007
(FIMABIS), J-0008 (SERGAS), J-0010 (Sacyl), J-0011 (ICS), J-0016 (Aragón),
J-0023 (SESCAM), J-0027 (La Rioja) y J-0028 (Cantabria) siguen en ese hueco.
**No se ha tocado ningún Fit para meterlas**, porque eso es exactamente la
edición cosmética que el contrato prohíbe. Y esta semana se añade un caso más
que la regla tampoco alcanza: **P-0002, con inicio negociable y Fit 4, es ahora
la mejor acción de la base y no entra en `action_now`** porque es ROLLING sin
plazo. Si quiere verlas, la decisión es de diseño y es suya: o sube alguna a
Fit 5, o la regla necesita una cláusula para plazas e inscripciones permanentes.

## Lo que el RD 101/2025 enseña sobre su vía clínica: hay TRES patrones, no uno

La semana pasada se descubrió en el SESCAM que hay que buscar por «Laboratorio
Clínico». Esta semana el rebarrido muestra que **las CCAA están adaptándose de
tres maneras distintas**, y eso cambia cómo hay que vigilar cada una:
- **SESCAM desactiva** las categorías antiguas y migra automáticamente las
  solicitudes previas.
- **Sacyl mantiene y actualiza**: texto literal Tier 1, «con motivo de la
  reciente creación de la categoría de Licenciado Especialista en **Laboratorio
  Clínico**, que unifica las especialidades de Bioquímica Clínica y Análisis
  Clínicos», se actualizaron las zonas de **ambas** bolsas (cambio hasta
  09-09-2026, efecto 10-09-2026). Aquí **conviven**.
- **Aragón no refleja nada** todavía y sigue con el nombre antiguo.

Y un hallazgo directamente aplicable a su calendario: **Sacyl publica un
procedimiento específico para residentes que terminan («FIN MIR_EIR 2026»)**.
Hay que buscar su equivalente de 2027 **desde enero**, porque es la vía natural
para alguien que acaba el MIR el 22-05-2027. **Osakidetza**, en cambio, **no
tiene bolsa permanente**: abre plazos por categoría mediante resolución y sin
aviso previo (la última, Resolución 1060/2026, abrió del 06-07 al 27-07-2026,
definitivas el 30-10-2026, alzada hasta el 30-11-2026), así que su vía es cazar
la **siguiente** apertura tras mayo de 2027. Categoría nueva allí: «F.E.M. -
Técnico/a Laboratorio Clínico».

## Qué perseguiría la semana que viene con más presupuesto

Escribir a Nijmegen (P-0002) y a Kähler (P-0079) es trabajo de ella, no mío,
pero es lo que decide el valor de esta pasada. Por mi parte, en orden:
**estrenar el ángulo del requisito de titulación** («MD or PhD»,
«medically qualified», «nearing completion»), que es la única grieta encontrada
en el muro del reloj; cerrar el rebarrido de las siete CCAA **entrando en las
aplicaciones de bolsa y en los PDF**, que es donde viven las categorías, ya que
las páginas índice no sirven; Cardiff **por nombres de PI**, única vía que
queda; la paginación completa del buscador del Broad para cerrar P-0008, P-0035
y P-0081; **laboratorios de sueño infantil por nombre** (Quante en Tubinga, el
eje Exeter–FIMM de Weedon y Jones, el NTR por contacto directo), que es el
agujero persistente del radar; las referencias del Consejo de Ministros, único
hueco que queda en J-0003; reabrir la ficha de P-0092 para zanjar el desfase de
un día; y corregir las Notes de SRC-0036 (HigherEdJobs) y la prioridad de
SRC-0125 (THEunijobs), que tal como están invitan a reintentar lo imposible.
