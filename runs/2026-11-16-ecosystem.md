# ecosystem — 2026-11-16

Sin ALERTA. El repositorio estaba donde debía y con el `HEAD` bien pegado a
`main` (la semana pasada llegó desprendido; hoy no). Las cuatro ramas
entregaron, el push fue directo a `main` sin rechazo, y los dos buzones de
respaldo acaban la semana vacíos.

## Lo que cambió, contado desde `git diff --stat HEAD~1`

| Pestaña | Antes | Después | Altas | Actualizadas |
|---|---|---|---|---|
| groups | 113 | 127 | 14 | 15 |
| events | 38 | 41 | 3 | 7 |
| training | 37 | 38 | 1 | 13 |
| sources | 509 | 520 | 11 | — |
| subscriptions | 47 | 47 | 0 | — |
| action_now | 62 | 65 | 58 mías, 7 ajenas preservadas | — |

53 apuntes de changelog, que es exactamente 18 altas + 35 actualizaciones.
Las bajas del diff (15 en groups, 7 en events, 13 en training) coinciden una a
una con las filas actualizadas: no se borró nada por accidente.

## Las tres cosas que merece la pena hacer esta semana

**1. ASCS 2027 (E-0029): quedan once días para tener el póster escrito.**
Releída hoy la convocatoria oficial, las cinco fechas siguen exactas y ninguna
se ha movido: la ventana *late-breaking* **abre el 27-11-2026 y cierra el
13-12-2026**; las becas de viaje se notifican el 03-12 (del ciclo ordinario,
**no** del late-breaking); la tarifa anticipada cierra el 20-12, un día antes
del fallo del póster el 21-12. El dato nuevo es el que decide la acción: se
envía por **Oxford Abstracts** y **no hay instrucciones separadas para el
late-breaking**, rigen las del póster ordinario (600 palabras, esquema,
conflicto de intereses). Es decir que **el texto se puede dejar cerrado antes
del 27 de noviembre** y enviarlo el día que abra la ventana; sirve el empírico
de primera autora del proyecto QIMR. Aviso: esta fila es Fit 3, así que **no
sale en `action_now`** por la regla de selección — es el reloj más corto de la
pestaña y hay que leerlo aquí. La tarifa no se pudo reconfirmar hoy (la página
no la publica), así que el Cost_EUR=735 sigue siendo el de la semana pasada.

**2. ESHG 2027 (E-0003): la beca se pide DENTRO del resumen, y es elegible.**
El hallazgo de la pasada. Plazo confirmado textualmente: **04-02-2027 23:59
CET**, con los envíos abriendo en diciembre de 2026 y el fallo a primeros de
abril. Y aparece el esquema completo de las **ESHG Conference Fellowships**:
categoría europea de **400 EUR más inscripción gratuita con almuerzos**, que se
solicita marcando la casilla «Fellowships & Awards» **dentro del propio envío
del resumen**, con el mismo plazo y sin prórroga. **Sí es elegible, por la vía
de estudiante**, porque el 04-02-2027 sigue siendo doctoranda. Los matices
quedan escritos en la ficha para que no se intente por la puerta equivocada: la
vía de «MD que terminó especialidad hace menos de 4 años» **no** le vale
(la residencia acaba el 22-05-2027, después del corte) y la de «último título
hace menos de 4 años» tampoco (MD de 2019). Requisito previo que hay que
resolver antes: **membresía ESHG 2027 en vigor antes de enviar**. Esto además
reconcilia lo de la semana pasada: la Beca ESHG de la AEGH, cuyo plazo venció
el 15-11 y para la que no era elegible, es solo la categoría nacional (600 EUR,
una por país), no esta. Para la rutina de fellowships: es beca propia del
evento, conviene cruzarla.

**3. Una plaza con reloj en Oslo (L-0040, Cheesman) y la mejor alta de la pasada.**
La ficha de Cheesman deja de ser un negativo: hay una plaza de **Researcher en
el Department of Psychology de la Universidad de Oslo, publicada el 12-11-2026
con plazo 03-12-2026** (Tier 1, uio.no). **No está confirmado** que sea de
PROMENTA ni del proyecto I-BELONG: hay que abrir el anuncio en Jobbnorge antes
del 3 de diciembre para saberlo. Y la mejor alta de la semana es **Rebecca
Richmond (L-0114, Bristol MRC-IEU), Fit 5**: ERC Consolidator 2025 «SCIRCLE»,
sueño y ritmos circadianos en epidemiología del curso vital, 2.358.499 EUR,
con **ejecución desde el 01-06-2027** (verificado en el PDF oficial del ERC y
en CORDIS). Une sus líneas 1 y 3 con métodos que despliega sola, y el arranque
del proyecto coincide casi al día con su disponibilidad: hay que escribirle en
enero-febrero de 2027, antes de que la oferta se publique.

## Qué cerró

- **T-0007 Advanced Mendelian Randomization (Bristol) → CLOSED**: «Bookings for
  this course have closed». Próxima edición estimada nov-2027 (LIKELY), con
  reservas abriendo en otoño.
- **E-0014 SES 2027: el plazo se perdió por seis días.** Encontrada por fin la
  ruta buena del calendario: congreso **4-6 de marzo de 2027 en Logroño**,
  comunicaciones cerradas el **10-11-2026**, notificación el 03-12, y **sin
  ronda tardía**. Queda viva solo la asistencia, y hay que decidirla antes del
  **15-01-2027**, que es cuando cierra la inscripción anticipada.
- **La plaza del Karolinska (jobID 975216) ya no existe**: cerró el 30-10-2026,
  re-verificado contra el listado completo de `ki.varbi.com` (84 plazas, y el
  MEB solo tiene research assistant de próstata, amanuenser y administración).
  Las URLs muertas de **L-0020 y L-0026** se han cambiado por el portal vivo.
- **T-0022 Cancer Genomic Epidemiology: el plazo NO era hoy**, es el
  **23-11-2026**, igual que el de la bursary. Corrección de fecha, no cierre.
- Verificado **en negativo**, que no es lo mismo que no mirado: **T-0024 SISG**
  sigue sin edición 2027 por segunda semana (todo apunta aún a 2026; revisar en
  enero); **T-0004 Wellcome GAPBAS** no figura en el catálogo de próximos cursos
  (patrón de cuatro ediciones: principios de septiembre con plazo a primeros de
  mayo, revisar marzo-abril); **T-0037 FSL** sin edición 2027, y queda cerrada
  la deuda de la semana pasada — **no existe lista de correo del FSL Course**,
  solo el buzón `fslcourse@ndcn.ox.ac.uk`; **T-0032 Neuromatch** sigue sin
  publicar plazo, pero ahora se sabe que **las solicitudes abren en febrero de
  2027**; **E-0004 BGA 2027** sigue literalmente «TBA» en todo; y **E-0022 WCPG
  2027** lleva tres semanas en «coming soon» con el enlace ECIP apuntando
  todavía a 2026 (no volver hasta febrero-marzo).
- **Los resultados del ERC-2026-COG todavía no están publicados** (la
  convocatoria cerró el 13-01-2026: 3.060 solicitudes, 673 M EUR, ~328 ayudas).
  Se probaron los patrones de URL de septiembre a diciembre y dan 404. Es la
  vía de menor competencia que existe y hoy simplemente aún no estaba.

## Conflictos que dejo abiertos en vez de elegir en silencio

1. **E-0026 ICHG 2027, conflicto nuevo y serio.** Un PDF alojado en `eshg.org`
   (serie de webinars ESHG-IFHGS, siendo la IFHGS la federación organizadora)
   sitúa el 15º ICHG en **octubre de 2026**, mientras la fila lo da en **marzo
   de 2027 en Guadalajara** sobre dos fuentes Tier 2. No se elige. Además, hoy
   **no aparece ninguna web oficial**, solo agregadores comerciales con eventos
   homónimos (Dubái, Londres, Ámsterdam) que no son este congreso: queda
   escrito como riesgo de contaminación para futuras pasadas. En los dos
   escenarios la conclusión práctica es la misma: enviar comunicación ya no es
   realista. Vía pendiente: un correo a la AEGH y probar `ifhgs.org`, dominio
   nunca intentado.
2. **T-0001 Boulder, elegibilidad, sin resolver por segunda semana.** La página
   oficial de CU Boulder y la página de evento correcta de Humanitix
   (`events.humanitix.com/2027-isgw`; **la URL que teníamos apuntada da 404**)
   **no contienen hoy ninguna restricción de dirección estadounidense**, y la
   única mención de elegibilidad es la de la ayuda por necesidad. Pero el texto
   conflictivo estaba en la ficha de la entrada, que cuelga de otra página que
   no se pudo abrir. **No se da por resuelto.** La acción sigue siendo el
   correo de cinco líneas a `IBGworkshop@colorado.edu`, ahora con fecha límite
   práctica: **antes del 01-02-2027**, que es cuando las cancelaciones dejan de
   ser reembolsables.
3. **T-0015 Bristol (Reproducible Health Data Science): la ficha oficial se
   contradice consigo misma** — la tabla resumen dice «21-22 y 25-26 de enero de
   2027» y la sección de horarios dice «29-30 de enero y 2-3 de febrero de
   2026». Reportado, no elegido.
4. **L-0103 Knopik y la dirección de *Behavior Genetics*.** Su **afiliación sí
   queda cerrada** (Purdue, Dept. of Human Development and Family Science), pero
   Springer sigue listando a John K. Hewitt como Executive Editor mientras
   fuentes Tier 2 dan a Knopik desde 2025. **No escribirle invocando el cargo**
   hasta confirmarlo; la vía pendiente es `bga.org` o el pie de firma de un
   editorial reciente.
5. **L-0127 Rabinowitz**: su artículo del 30-10-2026 la sitúa en **Washington
   University in St Louis** mientras NIH RePORTER la mantiene como PI en **Johns
   Hopkins** y **Rutgers** con cuatro R01 vivos (uno de sueño y ritmo circadiano
   hasta el 31-08-2027). Si acaba de mudarse, es justo el momento en que un
   laboratorio nuevo contrata. Es además el único hallazgo que cruza PRS
   psiquiátrico con fenotipo de sueño en cohortes de desarrollo.
6. **L-0098 Kocevska**: no se pudo confirmar si conserva el nombramiento en el
   NIN. ORCID lo lista sin fecha de fin, pero sus artículos de 2025 ya no lo
   firman. Anotado, no decidido.
7. **E-0015 AEGH** (sede Bilbao solo en Tier 2) y **EuroMedLab 2027** (un
   agregador aislado da 01-05-2027 frente al 16-20 de mayo del resto): abiertos,
   sin tocar esta semana el primero.

## Lo que no se pudo verificar ni alcanzar

Un intento cada uno. **Bloqueos nuevos**: `geneticepi.org` devuelve **503 hoy**
cuando la semana pasada respondía — consecuencia directa, **E-0030 (IGES 2027)
y E-0017 (GAW 2027) no se han podido verificar** y deliberadamente no van en
`updates` para no falsear la frescura. `hugo-hgm2027.org` 503,
`euromedlab2027.org` no resuelve, `erasmussummerprogramme.nl/courses/` 404
(era la mejor pista de descubrimiento de formación),
`bristol.ac.uk/people/person/Rebecca-Richmond-…` 404 (por eso la fila de
Richmond **no lleva correo**: hay que sacarlo de la página de la MRC-IEU antes
de escribir), y la ficha de la entrada concreta de Humanitix no se renderiza.
**Hallazgo operativo**: `erc.europa.eu` devuelve **429 a partir de la décima
petición rápida**; hay que espaciarlas unos 8 segundos. Queda en el Source_Note.
Van UNVERIFIED a propósito: **E-0041 LABCLIN 2027** (con la **URL vacía
adrede**: lo único verificado es que AEBM-ML, AEFA y SEQC-ML se han fusionado en
una nueva Sociedad Española de Medicina de Laboratorio, o sea que el organizador
ha cambiado de manos y las rutas viejas —`labclin2026.es`, `semedlab.es`, ambas
ya fichadas como inaccesibles— no van a servir) y **E-0039 HGM 2027** y
**E-0040 EuroMedLab 2027**, que quedan LIKELY sobre Tier 2 coincidente.
**Dos rutas corregidas, y una de ellas desmiente una nota nuestra**: la ruta
`congreso-ses.com/ses2027/fechas-importantes` que teníamos fichada como inválida
**sí existe**, pero lleva `/info-general/` por medio; y el fichero de resultados
LS del ERC 2025 existe pero usa **guion bajo** antes de `ls` donde el SH usa
guion normal — esa asimetría era lo que lo hacía parecer inexistente, y dio tres
de las catorce altas.
**No se intentaron**, por bloqueo ya documentado: `wellcome.org`, `nature.com`,
`link.springer.com`, `vipbg.vcu.edu`, `ucl.ac.uk`.

## Dos bloqueos esquivados por rutas nuevas, que es lo que más va a rendir

- **`ucl.ac.uk` (403) → `onlinestore.ucl.ac.uk`**, la tienda oficial de UCL, que
  sí responde y es Tier 1. Con ella se cerró **T-0035** (*D79 Genetic
  Epidemiology* a la venta hoy, 950 GBP investigador / 475 estudiante) y, de
  paso, **una corrección de fondo: el 01-03-2027 que constaba como plazo de
  inscripción no lo era** — es el del esquema de plazas gratuitas para
  residentes de países de renta baja y media, al que ella no opta. La celda
  `Deadline` se ha vaciado a propósito. En esa misma tienda está vivo el curso
  de **Mendelian Randomization 2027 (T-0034), 800 GBP investigador / 400
  estudiante, comprable hoy**: mientras siga siendo doctoranda entra en la
  tarifa de estudiante y se ahorra la mitad.
- **`le.ac.uk` (403) y `nin.nl` (404) → PubMed E-utilities y ORCID.** El bloque
  de afiliación y correo del autor de PubMed desbloqueó **L-0102 Dudbridge**
  (correo impreso por él mismo como *Electronic address* en su artículo de 2026)
  y confirmó Purdue en **L-0103**; ORCID cerró **L-0098**. Es la herramienta
  general contra los sitios institucionales bloqueados y queda fichada como
  fuente. En la misma línea, **Europe PMC con `resultType=core`** saca el correo
  del autor de correspondencia: en una pasada de diez PMIDs dio los de Demontis,
  Edwards, Mosing, Gazal, Pisanu, Visscher y Barr. Eso rompe el cuello de
  botella crónico de la columna `Contact_Route`.

## Filas cuyos hechos cambiaron bajo ella

`owner_status.json` sigue siendo `{}`: no ha marcado nada desde la página, así
que el `Owner_Status = NEW` del TSV es el valor por defecto y no una lectura
suya. Dicho eso, si ya había leído estas fichas, tres se le han movido de
verdad:

1. **L-0098 Kocevska** — si la leyó la semana pasada la tiene como un grupo
   Fit 5 en el NIN de Ámsterdam. Hoy es **Erasmus MC (Rotterdam)**, baja a
   **Fit 4**, y sobre todo **no es una puerta de contratación**: no es jefa de
   grupo y no puede contratar. Contacto científico y coautoría; el primer correo
   no debe pedir plaza.
2. **L-0020 Lu y L-0026 Yao (Karolinska)** — la plaza que daba urgencia a las
   dos fichas ya no existe. El sentido cambia de «vigilar convocatoria» a
   «escribir a Yao y a Lu por el calendario de CANARY».
3. **L-0041 Na Cai** — corrección de institución: se mudó con su grupo al
   **D-BSSE de ETH Zürich (Basilea)** en febrero de 2025, manteniendo afiliación
   conjunta al BRCCH. Su web de laboratorio (actualizada el 11-11-2026) no tiene
   «join us» ni correo, pero el grupo está creciendo.

Menor pero relevante: **L-0040 Cheesman** pasa de «negativo verificado, no
esperes anuncio» a «hay una plaza con plazo el 03-12-2026 que puede ser suya».
Y **L-0048 Guintivano**: la fecha de acción de su ficha (15-11-2026) **venció
sin gestión**; se ha reescrito al 15-12-2026 con mejor gancho (su preprint de
2026 sobre arquitectura genética compartida entre trastorno premenstrual y
depresión posparto).

## Suscripciones pendientes: siguen siendo las 47

`owner_status.json` está vacío, así que **ninguna** tiene marca suya y las 47
cuentan como pendientes por la definición del contrato. **Esta pasada añade
cero, y las tres ramas lo justifican en negativo, no por no haber mirado**: la
rama 1 solo encontró boletines genéricos de agregadores de convocatorias (Tier
2, repiten lo ya cubierto); la rama 2 quería el boletín EuroLabNews de la EFLM
pero no llegó a ver una URL de alta real y la regla prohíbe inventarla; y la
rama 3 confirmó que **el FSL Course no tiene lista de correo**, que era su
pendiente de la semana pasada. Mejor ninguna que una fabricada.
Con reloj entre las ya existentes: **SUB-0009 y SUB-0022** (alta de socia de
SEMEDLAB) siguen en TODO — y ojo, porque la fusión de sociedades españolas que
se ha detectado esta semana puede haber cambiado la vía de alta.
Nuevo pendiente del mismo tipo: la **membresía ESHG 2027**, que no es una
suscripción de avisos sino un requisito para pedir la beca del congreso antes
del 04-02-2027.

## Respaldo: los dos buzones quedan limpios

`source_inbox.json` llegó vacío (`[]`) y sigue vacío. `inbox_triage.tsv` llegó
sin ninguna fila PENDING y acaba igual: **cero PENDING**, comprobado con grep
después del push. No hubo nada que hacer de respaldo esta semana.

## Mantenimiento — décimo aviso, y ahora son NUEVE ficheros con dos que se disparan

Tomado de `ls -l data/` después del push. Por encima del umbral de ~60 KB:
`changelog.tsv` 560 KB, `groups.tsv` 453 KB, `sources.tsv` 416 KB,
`fellowships.tsv` 405 KB, `postdocs.tsv` 233 KB, `jobs.tsv` 115 KB,
`events.tsv` **97 KB**, `training.tsv` **87 KB** y `watchlist_closed.tsv` 72 KB.
Lo que hay que mirar es la velocidad, no el número: **`events.tsv` ha pasado de
79 a 97 KB y `training.tsv` de 76 a 87 KB en una sola semana**, con apenas 4
altas entre las dos. Crecen por longitud de celda, no por filas: las celdas de
`Confidence`, `Next_Action` y `Source_Note` se han vuelto párrafos porque es
donde van los conflictos sin resolver y las rutas alternativas. Es información
que vale, pero el ritmo es insostenible y el troceo **lo tiene que hacer una
persona**, porque exige tocar `tools/build_page.py` y `tools/build_xlsx.py` en
el mismo commit.
Y la observación de la semana pasada se confirma: con 127 filas, la rama 4 cerró
15 fichas de 127. A este ritmo una ficha se revisa cada dos meses.

## Qué perseguiría la semana que viene

1. **El anuncio de Jobbnorge de la plaza de Oslo**, que tiene plazo el 03-12 y
   es lo único accionable con reloj corto además del ASCS.
2. **Los resultados del ERC-2026-COG** en cuanto se publiquen (diciembre-enero):
   ~328 ayudas nuevas sin cribar, y es la vía de menor competencia que existe.
3. **La lista nominal de NWO Vici y Vidi 2026** por la web de NWO en neerlandés
   («toekenningen»), no por buscador en inglés: 39 Vici sin cribar en el país
   que concentra media tabla de genética estadística.
4. **El Erasmus Summer Programme de Rotterdam (NIHES)**, que se cayó por un 404
   y es el hueco de descubrimiento más obvio de la pestaña de formación.
5. **Tres correos que faltan** (Richmond en la MRC-IEU, Hemani, Guintivano):
   convertirían tres fichas Fit 4-5 en acciones de coste cero.
