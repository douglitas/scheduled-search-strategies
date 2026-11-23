# ecosystem — 2026-11-23

Sin ALERTA. El repositorio estaba donde debia, el remoto es el correcto y el
`HEAD` llego desprendido de `main` (como el 2026-11-09, no como la semana
pasada): se corrigio con un `checkout main` antes de escribir nada. Las cuatro
ramas entregaron, el push fue directo a `main` sin rechazo, y los dos buzones
de respaldo acaban la semana vacios.

## Lo que cambio, contado desde `git diff --stat HEAD~1`

| Pestana | Antes | Despues | Altas | Actualizadas |
|---|---|---|---|---|
| groups | 127 | 137 | 10 | 12 |
| events | 41 | 42 | 1 | 10 |
| training | 38 | 44 | 6 | 13 |
| sources | 545 | 567 | 22 | — |
| subscriptions | 51 | 51 | 0 | — |
| action_now | 67 | 71 | 62 mias, 9 ajenas preservadas | — |

52 apuntes de changelog, que es exactamente 17 altas + 35 actualizaciones. Las
bajas del diff (12 en groups, 10 en events, 13 en training) coinciden una a una
con las filas actualizadas: no se borro nada por accidente.

## Las tres cosas que merece la pena hacer esta semana

**1. ASCS 2027 (E-0029): el plazo corto sigue abierto, pero la ayuda de viaje
ya no.** Reverificadas hoy las cinco fechas y ninguna se ha movido: la ventana
*late-breaking* **abre el 27-11-2026 y cierra el 13-12-2026**, el fallo es el
21-12, la aceptacion el 07-01-2027 y la tarifa anticipada cierra el 20-12. El
dato nuevo cambia el calculo de la semana pasada: las **trainee travel awards
se notifican el 03-12 y exigen un resumen de primera autora**, es decir que van
atadas al **plazo ORDINARIO, cerrado el 28-10-2026**. Conclusion: si entra por
late-breaking, el poster puede salir pero **la ayuda de viaje no se puede
pedir**, y el coste del viaje corre entero por su cuenta. La cuota sigue sin
publicarse en la web, asi que el `Cost_EUR=735` continua sin confirmar desde
hace tres semanas. Sigue siendo Fit 3 y por tanto **no sale en `action_now`**:
hay que leerlo aqui.

**2. ESHG 2027 (E-0003): se cae el requisito de membresia previa, y hay cuotas.**
El envio **aun no ha abierto** (abre en diciembre) y el cierre se confirma otra
vez textualmente el **04-02-2027 23:59 CET**, con resultados a primeros de
abril y la beca solicitada dentro del propio envio. Correccion respecto a la
semana pasada: **la pagina oficial no exige membresia ESHG en vigor antes de
enviar**, solo una cuenta ESHG unica — el requisito que dimos por firme no
aparece hoy en Tier 1 (la pagina de cuotas de socia da 404, asi que la
membresia sigue sin poderse tarifar). Y aparecen las cuotas de inscripcion, que
no teniamos: **395 EUR en tarifa Trainee no socia hasta el 15-04-2027**, 270 si
es socia, subiendo a 520/395 desde el 16-04. La celda `Cost_EUR` llevaba el
texto completo y se ha normalizado a `395` con el desglose movido al
`Source_Note`, porque un numero con parentesis rompe los filtros.

**3. Hanna M. van Loo (L-0128, Fit 5 VERIFIED) es la mejor alta de la pasada.**
ICPE / UMC Groningen, con una **Vidi del NWO recien concedida** para explicar
por que los trastornos psiquiatricos se agregan en parejas; publica *genetic
nurture* (Nat Commun 2026) y disenos gemelo-hermano con Kendler. Dinero nuevo,
equipo por montar y un encaje exacto con PLINK/R/PRS sin pedirle neuroimagen
autonoma. Detras van **Jakob Grove (L-0129, Fit 5 VERIFIED)**, genetica
estadistica pura en Aarhus con acceso a iPSYCH, hallado por el working group de
autismo del PGC, y **Katherine Musliner (L-0130, Fit 4 VERIFIED)**, con un
Fellowship de la Lundbeck de **10 M DKK a cinco anos y mandato explicito de
montar equipo propio** sobre comorbilidad psiquiatrica. A los tres les falta el
correo: Europe PMC dio 503 justo en esa pasada.

## Las cuatro deudas de la semana pasada: cerradas

1. **L-0114 Richmond: `rebecca.richmond@bristol.ac.uk`**, sacado de los bloques
   de correspondencia de PubMed (tres apariciones). La ficha Fit 5 del ERC
   SCIRCLE pasa de bloqueada a accionable a coste cero. La accion sigue siendo
   escribir en enero-febrero de 2027, unos cuatro meses antes del arranque del
   proyecto el 01-06-2027.
2. **L-0118 Hemani: `g.hemani@bristol.ac.uk`** (seis articulos independientes).
   La fila tenia `Last_Verified` **vacio**, o sea que nunca se habia verificado;
   hoy queda fechada y la Confidence sube a LIKELY.
3. **L-0048 Guintivano: preprint confirmado** (Research Square, 07-08-2026, doi
   10.21203/rs.3.rs-10380518/v1) y aparece un segundo preprint con Breen. Su
   correo sigue sin publicarse, asi que **la via 1 pasa a ser Cynthia Bulik**
   (`cynthia_bulik@med.unc.edu`), autora de correspondencia en siete de sus
   articulos.
4. **L-0040 Cheesman: la deuda se cierra EN NEGATIVO y el reloj se cancela.**
   La plaza de Researcher de Oslo (Jobbnorge 310786, plazo 03-12) **no es de
   Cheesman, ni de PROMENTA, ni del proyecto I-BELONG**: es del LCBC, proyecto
   Horizon Europe SHIELD, **exige doctorado terminado y resonancia magnetica
   autonoma**. Doble descarte. Era el reloj mas corto de la pestana y hoy
   desaparece; la ficha se queda con la carta de presentacion sin fecha externa.

## Hallazgo no pedido, y el mas util de la rama 4

**L-0058 Andreassen (Oslo)** tiene **dos postdoc de tres anos financiados por la
Novo Nordisk Foundation** (Jobbnorge 311244, plazo 10-12-2026) que piden
explicitamente **PLINK/Regenie**. **No es candidatura para ella**: el tema es
Alzheimer y el plazo es incompatible con una defensa en febrero de 2028. Pero
verifica tres cosas que valen mas que la plaza — que hay dinero fresco, que la
pila de herramientas es la suya, y el correo
(`o.a.andreassen@medisin.uio.no`). La Confidence sube de LIKELY a VERIFIED y se
corrige la URL, porque NORMENT figura ya como terminado.

## Correccion a mi propio informe de la semana pasada

La pista que deje como prioridad 3 estaba **mal fechada y hay que rebajarla**:
las 39 Vici «sin cribar» **no son de la ronda 2026 sino de la 2025** (anuncio
26-02-2026), y las 109 Vidi anunciadas el 22-10-2026 **tambien son de la ronda
2025**. La ronda Vici 2026 cerro el 08-09-2026 y **no habra resultados antes de
febrero de 2027**. Hecha la criba completa: **ninguna Vici 2025** cae en
genetica estadistica, psiquiatrica o de sueno, mientras **las Vidi dieron la
mejor alta de la pasada**. Para las proximas: **la Vidi sube de prioridad y la
Vici baja**, y las notas de prensa del NWO no traen nombres — hay que ir a
`/researchprogrammes/nwo-talent-programme/projects-vici|vidi/<ronda>`.

## Qué cerró y qué se verificó en negativo

- **T-0005 CAJAL (sueno) → CLOSED**: sin edicion 2027.
- **Cierran HOY mismo y se recomienda dejarlos pasar**: **T-0022** Cancer
  Genomic Epidemiology y **T-0038** Long read sequencing (plazo 23-11-2026, es
  decir hoy, sin margen real). **T-0025** Southern SISG ya esta en curso.
- **E-0015 AEGH: correccion de fondo.** La XVII Jornada fue el **07-05-2026, ya
  pasada**; la de 2027 existe pero **sin fecha ni ciudad**. Se retiran el
  «07-05-2027» y el «Bilbao» que venian de Tier 2 y que llevabamos arrastrando.
  De paso: la **beca de la AEGH para asistir a la ESHG 2027** vencio el
  15-11-2026 y es anual — conviene que la rutina de fellowships la cruce.
- **T-0001 Boulder: elegibilidad resuelta en lo alcanzable.** Ni la pagina del
  IBG, ni `events.humanitix.com/2027-isgw`, ni su pagina de entradas contienen
  restriccion de residencia estadounidense. **El texto conflictivo no aparece en
  ninguna ruta viva: se da por inexistente.** Entrada unica **850 USD sin tarifa
  de estudiante**; devoluciones hasta ~30-01-2027.
- **Negativos verificados** (comprobado, no «no mirado»): **E-0004 BGA 2027**
  confirma fechas y Minneapolis pero todo lo demas sigue TBA, incluidas las
  Student Travel Awards — **con un dato aprovechable: Sarah Medland preside el
  programa**, y es contacto directo via QIMR. **E-0022 WCPG 2027** cumple cuatro
  semanas en «coming soon» con el enlace ECIP todavia en 2026: **no volver antes
  de febrero-marzo 2027**. **T-0024 SISG** sin edicion 2027 por tercera semana
  (revisar en enero; los institutos internacionales son bienales). **T-0004
  GAPBAS** ausente del catalogo de Wellcome (revisar marzo-abril). **T-0012
  SMARTbiomed** sin fechas. Sin taller de analistas del PGC y sin EMBO practical
  course de 2027 en sus lineas.
- **E-0030 IGES y E-0017 GAW: `geneticepi.org` ya NO da 503** (la semana pasada
  si), pero **no hay nada de 2027 publicado**. Dato util: las cuotas de socia de
  la IGES financian viaje de estudiantes.
- **T-0032 Neuromatch**: solicitudes en febrero de 2027, plazo aun sin publicar;
  se anaden exenciones de matricula y descuento por dificultad economica.
  **T-0037 FSL**: sin 2027, pero «registration will open soon» y el patron
  alterna presencial/online — la siguiente podria ser online.

## El agujero de descubrimiento que se cierra

**Erasmus Summer Programme (NIHES, Rotterdam)**, que llevaba dos semanas caido
por un 404. Las rutas vivas son **`/summer-programme-courses`, `/tuition-fees` y
`/registration`** — el `/courses/` que teniamos fichado sigue dando 404. Detras
hay un catalogo de **20 cursos cortos con tarifas en euros y 25% de descuento
para doctorandas internacionales**. Dos filas nuevas: **T-0039 ESP74 GWAS**
(1.134 EUR, **851 con descuento**) y **T-0040 ESP48 Causal Inference** (1.905 /
**1.429**). La edicion 2027 no tiene fechas publicadas, asi que las dos filas
**se dejan sin `Start_Date` a proposito**.

Las otras cuatro altas de formacion: **T-0041 CSHL Neural Data Science**
(07-21 jul 2027, **plazo 12-03-2027**, Fit 4) es la que mejor cierra su hueco
real — neurociencia computacional y electrofisiologia, que hoy solo maneja a
nivel supervisado. **T-0044 Colorado Sleep and Circadian Summer School**
(1-6 ago 2027, **gratis**, hibrida, Fit 4) toca su linea 3 y, si va en virtual,
**no necesita visado**. **T-0043 CAJAL Advanced Imaging** (30-03 a 16-04-2027)
tiene **plazo 20-12-2026, el mas inminente de la pestana**, aunque es Fit 3.
**T-0042 CSHL Single Cell & Spatial Transcriptomics**, Fit 3.

## Conflictos que dejo abiertos en vez de elegir en silencio

1. **E-0026 ICHG 2027**, tercera semana. La ruta nueva `ifhgs.org` **dio 503 en
   el unico intento**, asi que sigue el choque entre el PDF de `eshg.org`
   (octubre de 2026) y las dos fuentes Tier 2 (marzo de 2027, Guadalajara). Sin
   elegir bando.
2. **T-0015 Bristol (Reproducible Health Data Science): la contradiccion queda
   CONFIRMADA**, no resuelta — la tabla resumen dice «21-22 y 25-26 de enero de
   2027» y el horario dice «29-30 de enero y 2-3 de febrero de 2026», con
   copyright de 2026. 1.000 GBP sin tarifa de estudiante. Confidence UNVERIFIED.
3. **T-0035 UCL D79**: una busqueda sugiere que el **01-03-2027 si seria plazo
   general** via `i.badini@ucl.ac.uk`, al contrario de lo que concluimos la
   semana pasada al vaciar la celda. **No se ha tocado la fila**: hay que
   releerla cuando `ucl.ac.uk` deje de dar 403.
4. **L-0127 Rabinowitz**, sin resolver: `psych.washu.edu/people` esta paginado y
   solo llega a la J, de modo que **su ausencia no prueba nada**. Via para la
   semana que viene: NIH RePORTER — si sus R01 cambian de institucion, se ha
   mudado y hay laboratorio nuevo contratando.
5. **L-0103 Knopik y la direccion de *Behavior Genetics***: `bga.org` da **403**
   (bloqueo nuevo) y Europe PMC solo tiene el editorial de Hewitt de 2012.
   **Sigue en pie: no escribirle invocando el cargo.**
6. De la rama 1, tres conflictos menores anotados en ficha: **39 vs 43**
   laureadas Vici (se usa 39, el oficial); cargos y fechas de **Corvin**
   contradictorios entre fichas de `tcd.ie`; afiliacion de **Karyotaki** (UvA
   segun el NWO, VU en su obra); y si **van Loo** ejerce como psiquiatra.
7. Sin tocar por no haberse comprobado: **E-0039 HGM 2027** y **E-0040
   EuroMedLab 2027**. **E-0041 LABCLIN 2027** si se intento por la sociedad
   fusionada y no hay nada de 2027; **`labclin.org` queda sin quemar** para la
   proxima.
8. **E-0014 SES 2027**: la pagina oficial solo confirma Logrono y marzo; la ruta
   de cuotas dio 404, asi que el «4-6 de marzo» y la reducida del 15-01-2027
   siguen siendo Tier 2. Decision viva: **tarifa de residente antes del 15-01**.

## Lo que no se pudo verificar ni alcanzar

Un intento cada uno. **Bloqueos nuevos**: `bga.org` **403**; `pgc.unc.edu`
empieza a devolver **502/503 a la cuarta peticion seguida**, y por eso **quedan
14 paginas de working group sin abrir** — hay que ir de dos en dos; `umcg.nl`
**403**, resuelto por `research.rug.nl`, que queda fichada como la via buena
para el UMCG; `esrs.eu` **403** (por eso **no se toco T-0030**); `cardiff.ac.uk`
**403**, con la Cardiff Summer School quedando como pista fuerte sin abrir;
`embl.org` 404 al filtrar por 2027; `tcd.ie/.../staff/corvina` 404; `ifhgs.org`
503. **Hallazgo operativo que vale para todas las ramas**: `ebi.ac.uk` /
**Europe PMC da 503 por WebFetch pero funciona por `curl`** — por el 503 quedan
sin correo van Loo, Musliner y Ruigrok. **L-0008 Saxena fallo por homonimia**:
hay que ir por ORCID. **L-0098 Kocevska no se toco** esta semana.
**ERC-2026-COG: NO publicada hoy.** `erc-2026-cog-results_ls.pdf` da 404 y la
nota `erc-2026-consolidator-grants-results` tambien; **no hubo 429 porque no se
insistio**. Por precedente (03-12 en 2024, 09-12 en 2025), toca mirar **la
primera quincena de diciembre**.

## Fuentes nunca usadas antes, una por rama

Rama 1: las **paginas de laureadas por ronda del NWO** y el **portal PURE de
Aarhus**. Rama 2: `ifhgs.org` (caida hoy) y la seccion de noticias de
`fens.org`. Rama 3: las dos rutas vivas del Erasmus Summer Programme,
`meetings.cshl.edu/courseshome.aspx` y `colorado.edu/iphy/node/845`. Rama 4: el
**endpoint PDF de Jobbnorge (`joblisting/pdf/<jobID>`)**, unica via legible de
los anuncios noruegos, que ha resuelto por si sola las dos fichas de Oslo.

## Filas cuyos hechos cambiaron bajo ella

`owner_status.json` sigue siendo `{}`: no ha marcado nada desde la pagina, asi
que el `Owner_Status = NEW` del TSV es el valor por defecto y no una lectura
suya. Dicho eso, si ya habia leido estas fichas, cuatro se le han movido:

1. **L-0040 Cheesman**: la semana pasada le dijimos que habia «una plaza con
   plazo el 03-12 que puede ser suya». **No lo era, por dos motivos
   independientes**, y el reloj queda cancelado. Es la correccion mas importante
   de la pasada.
2. **E-0029 ASCS**: si entra por late-breaking, **no puede pedir la ayuda de
   viaje**. El coste del viaje cambia de «posiblemente cubierto» a «suyo».
3. **E-0003 ESHG**: desaparece el requisito de membresia previa que dimos por
   firme, y aparecen las cuotas (395 EUR en tarifa Trainee).
4. **E-0015 AEGH**: la fecha y la ciudad que constaban eran incorrectas; la
   jornada de 2026 ya paso y la de 2027 no tiene fecha.

Menor: **L-0030 Mattheisen** gana una **afiliacion doble con el IPPG de la LMU
de Munich**, que es una via de contacto dentro de la UE y sin visado — mejora
real frente a la ficha de Dalhousie. **L-0005 Walters**: el Brain and Genomics
Hub deja de ser dato por confirmar, ya publica. **L-0022 Franke**: tres
articulos nuevos, afiliacion estable. **L-0020 / L-0026 Karolinska**: tercera
lectura de `ki.varbi.com` sin nada de genomica psiquiatrica y CANARY sin
calendario publicado, asi que **la vigilancia de ese portal baja a mensual**.

## Suscripciones pendientes: 51, y esta pasada anade cero

`owner_status.json` esta vacio, asi que **ninguna** tiene marca suya y las 51
cuentan como pendientes por la definicion del contrato (eran 47 la semana
pasada; las cuatro nuevas las anadieron positions y fellowships esta manana).
**Las tres ramas que podian anadir justifican el cero en negativo, no por no
haber mirado**: ninguna vio una URL de alta real, y la regla prohibe
inventarla. Con reloj entre las existentes siguen **SUB-0009 y SUB-0022** (alta
de socia de SEMEDLAB), con el aviso de que la fusion de sociedades espanolas
puede haber cambiado la via. **Ya NO es pendiente la membresia ESHG 2027**: la
pagina oficial no la exige para pedir la beca del congreso.

## Respaldo: los dos buzones quedan limpios

`source_inbox.json` llego vacio (`[]`) y sigue vacio. `inbox_triage.tsv` llego
con sus 11 filas en DONE y **cero PENDING**, comprobado con grep antes y
despues del push. No hubo nada que hacer de respaldo esta semana.

## Mantenimiento — undecimo aviso, pero la alarma de la semana pasada se desactiva

Tomado de `ls -l data/` despues del push. Por encima del umbral de ~60 KB:
`changelog.tsv` 608 KB, `groups.tsv` 482 KB, `sources.tsv` 455 KB,
`fellowships.tsv` 453 KB, `postdocs.tsv` 254 KB, `jobs.tsv` 133 KB,
`events.tsv` 88 KB, `training.tsv` 80 KB y `watchlist_closed.tsv` 69 KB.
**La alarma que levante la semana pasada no se confirma**: dije que `events` y
`training` crecian de forma insostenible por longitud de celda (79→97 KB y
76→87 KB en una semana) y esta semana **han BAJADO** a 88 y 80 KB, a pesar de
sumar 7 filas entre las dos. Lo que paso es que varias celdas-parrafo de
conflictos sin resolver se han sustituido por hechos cortos al cerrarse. El
troceo sigue siendo trabajo de una persona, pero **no es urgente**. Lo que si
crece sin freno es `changelog.tsv`, +48 KB en una semana, y es el unico fichero
que no se consulta nunca a mano.
La observacion estructural sigue en pie y empeora: con **137 filas**, la rama 4
cerro 12. A este ritmo una ficha se revisa **cada once semanas**.

## Qué perseguiría la semana que viene

1. **Los resultados del ERC-2026-COG**, que por precedente caen en la primera
   quincena de diciembre: ~328 ayudas sin cribar y la via de menor competencia
   que existe.
2. **Las 14 paginas de working group del PGC que quedaron sin abrir**, de dos en
   dos para no provocar el 502: es la fuente que dio a Grove y a Corvin.
3. **Los tres correos que faltan** (van Loo, Musliner, Ruigrok) por `curl` a
   Europe PMC en vez de WebFetch, mas Saxena por ORCID: convertirian dos fichas
   Fit 5 y dos Fit 4 en acciones de coste cero.
4. **Cerrar Rabinowitz por NIH RePORTER** y **Knopik por el pie de firma de un
   editorial**, que son los dos conflictos mas antiguos de la pestana.
5. **`labclin.org`, el segundo intento a `ifhgs.org`, Cardiff y ESRS por otra
   via**, y la ficha de matricula y becas del CSHL Neural Data Science (T-0041),
   que es la mejor alta de formacion y tiene plazo el 12-03-2027.
