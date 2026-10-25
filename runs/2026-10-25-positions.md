# positions — 2026-10-25

**ALERTA, capacidad caída: EURAXESS ha pasado de «buscador roto» a BLOQUEO
TOTAL.** Todo `euraxess.ec.europa.eu` devuelve 403 de CloudFront («Request
blocked»): portada, `/jobs/search`, `/jobs/hosting`, las fichas individuales
`/jobs/<id>`, y hasta `/robots.txt` y `/sitemap.xml`. El 2026-10-19 las fichas
individuales aún se leían; hoy no. **Y el bloqueo alcanza a los portales
nacionales: `www.euraxess.es`, `.de`, `.pt` y `.se` dan los cuatro 403**, así
que no hay espejo de escape. Descartado que sea el entorno: proxy limpio y
otros dominios a 200 en la misma tanda. Probadas y fichadas cuatro rutas
alternativas, tres muertas (buscador externo restringido al dominio: cero
páginas; Wayback/CDX: 429 y conexión reseteada; no existe RSS/API/dataset
oficial, solo scrapers de pago) y una viva pero inútil (el espejo del tablón de
la MCAA responde 200, pero da 10 ofertas y sus enlaces van al dominio 403).
**Consecuencia: la rama 1 cierra con 0 altas y la superficie EU queda sin
cubrir por medios automáticos.** La única vía que queda a esta superficie es
que la abras tú en un navegador — el bloqueo parece ser solo contra tráfico
automatizado — y sobre todo **activar SUB-0002 y SUB-0018 (alertas por correo
de EURAXESS), que esta semana dejan de ser una mejora y pasan a ser la única
cobertura posible de todo el portal europeo.**

Nota de proceso, por si cuadra las fechas: el disparo llegó a las **23:02 del
domingo 2026-10-25 en Madrid**, 58 minutos antes del lunes 00:01 previsto,
porque esa misma noche terminaba el horario de verano. El contrato manda
calcular la fecha una sola vez en Europe/Madrid, así que **se usó 2026-10-25**
en el commit, en las filas y en este fichero. Las pasadas anteriores están
fechadas en lunes; esta no, y no es un error de nadie.

Perfil completo (sin `PROFILE-INCOMPLETE` ni `[TODO]`): se investigó con
normalidad. No existía informe de hoy, así que no fue un re-disparo. Checkout
correcto en `main`, árbol limpio, remoto el que debe ser.

## Recuento, tomado de `git diff --stat HEAD~1`

| fichero | cambio |
|---|---|
| `data/postdocs.tsv` | 9 altas (P-0084…P-0092), 21 filas actualizadas |
| `data/jobs.tsv` | 5 altas (J-0026…J-0030), 4 filas actualizadas |
| `data/sources.tsv` | 12 fuentes nuevas (SRC-0341…SRC-0352), 33 notas al día |
| `data/changelog.tsv` | 51 apuntes |
| `data/action_now.tsv` | 1 fila mía (J-0003), 40 ajenas preservadas |
| `data/subscriptions.tsv` | sin cambios (ver «Suscripciones») |
| `data/inbox_triage.tsv` | sin cambios (buzón a cero) |

136 inserciones y 59 supresiones. **Las 59 supresiones son exactamente la mitad
`-` de los pares de las 25 filas de datos modificadas, las 33 notas de fuentes
y la fila de `action_now`: no se perdió ninguna línea.** Comprobado fila a
fila contra `HEAD~1`: `Owner_Status` intacto en las 108 filas preexistentes,
ninguna fila desaparecida, y las 14 nuevas nacen con la columna vacía.
Anchos de columna uniformes en los siete ficheros tocados y ningún `Fit_1_5`
mal formado.

## Las tres cosas que merecen acción

**1. J-0003 — las alegaciones a los dos reales decretos de Genética. VENCE
MAÑANA, 2026-10-26. Fit 5, competencia LOW, esfuerzo S. Es la única fila de mi
beat en `action_now` y sigue siendo la más valiosa de la base.**
Verificado Tier 1 hoy, punto por punto: (a) los dos proyectos siguen en
«Proyectos abiertos» con las mismas fechas 02-10 → 26-10-2026, **sin prórroga
y sin cierre anticipado**; (b) sigue vigente el canal, que no es la sede
electrónica sino el buzón **`informacion_publica@sanidad.gob.es`**, con los dos
códigos de expediente obligatorios en el asunto, **DG/91/26** (Genética Médica)
y **DG/90/26** (Genética de Laboratorio) — **son dos correos, uno por decreto**,
y solo se consideran las aportaciones identificadas y recibidas en plazo;
(c) **el BOE no ha publicado ninguno de los dos reales decretos** y no consta
noticia de Consejo de Ministros sobre su entrada en vigor, **así que la bisagra
frente al fin de tu residencia el 22-05-2027 sigue entera y sin resolver.**
El `Next_Action` de la fila lleva los asuntos literales y cuatro puntos de
alegación listos. Es media hora de trabajo y mañana se acaba.
Contradicción resuelta de paso: una fuente Tier 2 atribuía a BOE-A-2026-19827
la especialidad de Laboratorio Clínico; leído el PDF, es la Orden DEF/993/2026
del Cuerpo Militar de Sanidad. Laboratorio Clínico se creó por **RD 101/2025**.

**2. El hallazgo transversal de la semana, y afecta a toda tu vía clínica: el
RD 101/2025 YA SE ESTÁ EJECUTANDO en las bolsas autonómicas, y hay que buscar
por «LABORATORIO CLÍNICO», porque «Análisis Clínicos y Bioquímica Clínica» se
está desactivando.**
No es teoría: en el SESCAM (J-0023) ya se pueden presentar solicitudes nuevas
de FEA **Laboratorio Clínico** en SELECTA, las dos categorías antiguas están
desactivadas, y a quien tenía solicitud previa se le generó automáticamente la
nueva. J-0023 sube por eso a **Fit 4 y ROLLING** — era PENDING y llevaba
semanas sin resolverse. La cautela honesta: la nota que lo prueba es del
03-06-2026, o sea prueba que abrió, no que siga abierto hoy, y SELECTA exige
certificado digital para comprobarlo. **El riesgo que esto crea es de falsos
negativos en todas las filas de CCAA**: una bolsa puede estar abierta bajo el
nombre nuevo mientras nosotras la buscábamos por el viejo. Queda corregido el
criterio de búsqueda para las próximas pasadas.

**3. P-0079 (Karolinska, KI-PGI) es lo mejor que ha pasado por el radar en
contenido, cierra el 2026-10-30 — en 5 días — y aun así la jugada NO es
presentarse, es escribir.**
Está viva y verificada: ref. STOD 2-4050/2026, **2 plazas de 2 años**,
financiación NIH, inicio «según acuerdo». Pide literalmente GWAS, PRS y diseños
familiares sobre registros suecos o UK Biobank: **es tu línea 2 exacta.** Pero
exige doctorado concluido, y tú no defiendes hasta febrero de 2028, así que el
Fit es 3 **por reloj, no por perfil**, y por eso no entra en `action_now`. Su
`Next_Action` está reescrito como contacto, con dos nombres: **Anna Kahler
(`anna.kahler@ki.se`)** como puente y **Lu Yi**. El gancho es la cadencia
2027-28 y una posible estancia corta previa. Que el inicio sea «según acuerdo»
es justo lo que hace que la conversación tenga sentido ahora.

**La conclusión estructural, que repite la de la semana pasada y conviene que
decidas tú: de las 9 altas de `postdocs` de esta pasada, NINGUNA llega a Fit 4,
y otra vez por el mismo motivo que no tiene nada que ver contigo** — exigen
doctorado concluido e incorporación inmediata, y no estás libre hasta el
22-05-2027 ni defiendes hasta febrero de 2028. Lo mejor por contenido:
**P-0084 (Cambridge, lab Malpetti, ON-FIRE)**, que pide PRS, bioestadística y
R/Python/Bash, declara que no hay poyata y **sale con doble grado RA/Research
Associate, así que el grado inferior no exige doctorado concluido: es la única
alta de la semana que podría encajar con una incorporación a mediados de 2027**
(`mm2243@medschl.cam.ac.uk`, cierra el 08-11); y **P-0085 (QMUL, CoDE Lab de
Margherita Malanchini)**, genética de la conducta sobre trastornos del
neurodesarrollo, que cierra el 01-11.

## Lo que cerró

P-0061 (Oxford, Florence Nightingale) y P-0078 (Cambridge, Cagan Lab) cerradas
sin ambigüedad, `status=archive` en el JSON-LD; la de Oxford es convocatoria
recurrente y la siguiente edición es esperable en sept-oct de 2027, con
confianza media. P-0063 (Cardiff, HGMD) cerrada LIKELY: plazo 23-10 vencido y
ausente de las 30 vacantes vivas. P-0062 (QIMR BV000088) cerrada VERIFIED,
desaparecida del listado. **P-0076 (Imperial, DTB455) sigue viva pero cerraba
hoy mismo.**
**P-0004 (Universidad de Islandia, ERC) queda resuelta, pero con etiqueta
honesta: CLOSED y sube de UNVERIFIED a LIKELY, no a VERIFIED.** No se pudo leer
el campo «Job Status» porque EURAXESS da 403, así que se verificó por el Tier 1
del empleador: el tablón de la Universidad de Islandia publica hoy 3 vacantes
(Grant Writer, Geochemistry, Applied Mathematics) y **ninguna postdoctoral de
epidemiología genética ni del ERC StressGene**. Se cierra por ausencia, no por
lectura de estado, y un postdoc del ERC puede anunciarse solo en EURAXESS: de
ahí LIKELY y no VERIFIED. Esto cierra la deuda que dejó la regla refutada
SRC-0268 sobre esta fila concreta. `Next_Action`: escribir a Unnur
Valdimarsdottir.

## Lo que no se pudo verificar o alcanzar

- **Cantabria es ahora un bloqueo probado, y eso REFUTA la recomendación que
  dejé la semana pasada.** Dije que se atacara por el BOC en vez de por el
  portal de salud: no sirve. `sede.cantabria.es` da 000/503, `boc.cantabria.es`
  000, `cantabria.es` 000, y `scsalud` y su portal de procesos de selección
  403. **Todos los dominios.** J-0028 queda fichada Fit 4 pero **UNVERIFIED y
  sin `Last_Verified`**, que es lo honesto.
- **Asturias (J-0017) agota también la vía del boletín.** `sede.asturias.es/bopa`
  da 000, `bopa.asturias.es` no resuelve y `www.asturias.es/bopa` devuelve 302
  sin cuerpo. Cuarta semana. Queda PENDING y **su `Last_Verified` no se tocó**:
  solo lo resuelve una persona con navegador o una llamada al SESPA.
- **`training.nih.gov` está ahora detrás de Cloudflare** (403 por WebFetch y por
  curl; Ray ID a5048ce16ee70c76), tercera semana de P-0037 sin resolver. Si
  sigue así la semana que viene, **propongo archivar la fila** en vez de pagar
  el intento cada lunes.
- deCODE sigue sin verificar (P-0020, P-0066): no publica en `decode.com` y su
  portal 50skills necesita JavaScript.
- **J-0021 (Canarias) congelada a propósito**, como recomendé la semana pasada.
  **J-0012 (GSK) no se re-intentó y su `Last_Verified` NO se selló en falso.**
- **Deuda declarada por la rama 4, y la digo como deuda: agotó el tope en
  J-0003 y en las CCAA, así que J-0013, J-0015, J-0019 y J-0022 llevan ya dos
  semanas sin reverificar y NO se hizo la búsqueda nueva de comunicación
  científica. Por tanto, al contrario que la semana pasada, NO puedo afirmar que
  no haya novedades de MSL ni de MedComms esta semana: no se han buscado.**
- Sin presupuesto para Edinburgh, el MRC Centre de Cardiff por páginas de grupo
  ni los centros españoles por dominio propio. KCL no se alcanzó por la rama 3:
  `www.kcl.ac.uk/jobs` es un índice de categorías y hay que usar `/jobs/search`.
  HigherEdJobs queda **PENDIENTE, no bloqueado**: se atacó un endpoint
  equivocado.
- Contradicción registrada y sin reconciliar: un postdoc de genómica del
  Departament de Genètica, Microbiologia i Estadística de la Universitat de
  Barcelona, con dos agregadores que discrepan del plazo (uno lo da vencido el
  01-10, otro dice que quedan 12 días). **No se fichó fila**: habría sido
  inventar una de las dos fechas.

## Resultados en negativo, para no volver a pagarlos

Erasmus MC **no tiene nada**: por la ruta buena de su dominio propio hay 9
vacantes de investigación y **cero** de genética, epidemiología genética, sueño
o Generation R. O sea que AcademicTransfer no fallaba la semana pasada, y la
tarea «atacar Erasmus MC por su propio dominio» queda cumplida y cerrada.
QIMR: 4 vacantes, ninguna relevante. VU Amsterdam: 14, nada del Netherlands
Twin Register. Broad: nada nuevo de genética estadística ni del Stanley Center.
La Behavior Genetics Association y la World Sleep Society **no tienen tablón de
empleo** (cero enlaces de job/career/vacancy en portada): fichado para no
repetirlo. A cero también el feed de la SRS, el IGES, la ISPG, la AEGH y el
ISCB (16 anuncios nuevos, ninguno de genética estadística o psiquiátrica).

## Trampas de verificación fichadas esta semana

- **`cardiffuniweb.eploy.net`: `&keywords=` tampoco filtra** (además de la
  paginación rota), y el listado no publica departamento, **así que esa fuente
  NO sirve para aislar el MRC Centre, en contra de lo que dicen SRC-0038 y
  SRC-0119.** Quedan corregidas.
- `academicpositions.com` y `findapostdoc.com` dan reto de Cloudflare a curl
  incluso con User-Agent de navegador. **`seek.com.au` tiene antibot propio: la
  vía australiana por Seek queda cerrada.**
- **Nature Careers IGNORA `?q=` y solo filtra con `?keywords=`.** En Science
  Careers, `sort=recent` no ordena. En `academictransfer`, `?q=` con clave de
  una palabra devolvió física de antimateria y un veterinario equino.
- **El feed RSS de jobRxiv da los 10 últimos anuncios con el MISMO `pubDate`**
  (el de regeneración del feed): la fecha real está en el `datePosted` del
  JSON-LD de cada ficha.
- `uu.se` muestra solo 9 de sus 90 vacantes sin pulsar «Show more hits»: un
  fetch único engaña. La API de Platsbanken (SRC-0188) responde 200 pero
  devolvió `total=0` en dos consultas; su `q` parece AND estricto.
- Homónimo caro, fichado para no volver a perseguirlo: el «Chiang Lab» de
  jobRxiv es **Jason** Chiang (radiología intervencionista, UCLA), **no**
  Charleston Chiang (genética estadística, USC).
- Aviso de higiene: **`ki.varbi.com/en/` está triplicado** en SRC-0219,
  SRC-0310 y SRC-0339.
- El truco del JSON-LD volvió a ser la verificación más barata del repo: **30
  fichas verificadas en 3 llamadas de curl.**

## Buzón

El conector de Gmail funcionó y se hicieron las dos pasadas exactas. **Pasada A
(`label:Research newer_than:8d`): cero, y sigue sin ser un fallo — la etiqueta
está vacía porque ninguna suscripción está activada.** Pasada B: un único
resultado y era falso positivo (casaba con «research fellow» por el cargo del
remitente, sin oportunidad dentro). **Cosecha cero: 0 filas nuevas en
`inbox_triage`, nada PENDING, `ecosystem` no hereda trabajo de aquí.**
No se etiquetó nada, porque etiquetar basura degrada la etiqueta; el id de la
etiqueta Research sigue siendo `Label_1910483919685933112`. No se creó ningún
borrador y no se envió nada. `source_inbox.json` comprobado y vacío (`[]`):
ninguna URL tuya que resolver. Privacidad respetada: no se registra remitente
ni asunto del falso positivo, y no consta nada más del buzón.

## Filas tuyas cuyos hechos cambiaron bajo ti

Ninguna. `owner_status.json` sigue vacío (`{}`): no hay ni una fila marcada
READ, IN_PROGRESS, APPLIED, RESOLVED, DISCARDED ni REVISIT, así que todo lo
tocado estaba en NEW o sin marca y no hay ningún modelo mental que se haya
quedado obsoleto. (Dicho de otro modo: **la página tiene nueve semanas de radar
y ni una decisión registrada.** No es un reproche, es el dato que explica por
qué la Pasada A del buzón sale vacía cada lunes.)

## Suscripciones

**36 pendientes: las 36 del fichero están en TODO y `owner_status.json` está
vacío, así que ninguna propuesta en diez semanas se ha activado. El cuello de
botella sigue siendo la activación, no el descubrimiento** — y esta semana eso
ha dejado de ser una observación de estilo para convertirse en el agujero de
cobertura que describe la ALERTA de arriba: **SUB-0002 y SUB-0018 (EURAXESS)
son ahora la única vía posible a todo el portal europeo.**

**Cero altas esta semana, y es deliberado, no olvido.** Las cinco ramas
buscaron canales nuevos y ninguna encontró una URL de alta verificable, y la
regla prohíbe inventarla: las alertas por correo del Varbi de KI y de Erasmus MC
no publican formulario localizable; `Science Careers /alerts/` y `/jobalerts/` y
`Nature /alerts/` dan 404. El orquestador gastó tres llamadas más en
comprobarlo de primera mano y confirma el resultado: `nature.com/naturecareers/
jobs/alerts` responde 200 pero **redirige al listado genérico**, no es una
página de alta; `higheredjobs.com/JobSeeker/emailAlerts.cfm` responde 200 con un
cuerpo de **212 bytes vacío**; las de alerta de QIMR TurboRecruit, del talent
community del Broad y de `ki.varbi.com/en/subscription/` dan 404. **Fichar
cualquiera de esas como «URL de alta» habría sido inventarla, y con 36 TODO sin
activar el valor marginal de una propuesta número 37 es prácticamente nulo.**

## Fuentes nuevas

12, y la mitad valen precisamente por documentar un callejón. Las de peso:
**jobs.ac.uk con las claves `honorary`/`clinical`** (prioridad HIGH — ver abajo,
funciona); **Science Careers con el parámetro `keywords=`, que sí filtra**
donde `q=` no; el **feed RSS de vacantes de jobRxiv** (`?feed=job_feed`), con su
trampa de `pubDate` anotada; la **vista de ficha individual del tablón de la
ESHG** (`tx_jobfair` por job id, que es la que destapa la URL Tier 1 del
empleador, y el `cHash` no hace falta); el **tablón oficial de la Universidad de
Islandia**, que sustituye a SRC-0190, cuyas dos URLs ya no resuelven; el
**portal de vacantes de Uppsala** con su mecánica `job-details?query=<id>`; la
**ruta por área de Erasmus MC** (`/vacatures/vakgebied/wetenschap-en-onderzoek`,
la única que funciona, porque `?zoekterm=` se ignora); y el **índice de vacantes
del LNS de Luxemburgo**. Fichadas explícitamente como **rutas muertas, para que
nadie las reintente**: Wayback/CDX contra EURAXESS y la sección
`available-positions` de `decode.com`.

## Un aviso sobre la propia regla de `action_now`, porque la decisión es tuya

`action_now` se queda esta semana con **una sola fila mía, J-0003**, y eso es la
regla aplicada correctamente, no un fallo. Pero conviene que veas el efecto
estructural: **hay 9 filas de Fit 4 de tu vía clínica española —tu prioridad
número 2— que la regla no puede surfacear nunca**, porque son bolsas
permanentes (ROLLING, sin plazo) y la regla solo admite sin plazo lo que es
Fit 5. J-0002 (SAS), J-0007 (FIMABIS), J-0008 (SERGAS), J-0010 (Sacyl),
J-0011 (ICS), J-0016 (Aragón), J-0023 (SESCAM), J-0027 (La Rioja) y J-0028
(Cantabria) están todas en ese hueco. **No he tocado ningún Fit para meterlas,
porque eso es exactamente la edición cosmética que el contrato prohíbe.** Si
quieres verlas en la lista, la decisión es de diseño y es tuya: o subes alguna a
Fit 5, o la regla necesita una cláusula para bolsas permanentes.

## Altas de la vía clínica y de fuera de la academia

**J-0027 (La Rioja, SERIS), Fit 4**: vía propia de listas de facultativos
localizada en Tier 1; queda en un PDF si la inscripción es permanente o por
plazos. **J-0028 (Cantabria), Fit 4 pero UNVERIFIED**, por el bloqueo total de
dominios. **J-0026 (Baleares, IB-Salut), Fit 3**: el mecanismo está VERIFIED
(borsa única desde 2014, vía excepcional por autovaloración, integració de
categories), y baja a 3 por una condición real y no por el perfil — **el catalán
es requisito con barem únic y no lo tienes**. Y dos de Luxemburgo, empleador
nuevo en el repo (antes cero filas de Luxemburgo), las dos VERIFIED en Tier 1:
**J-0029** (Medical Doctor Specialist in Cytogenetics, CDI, ref. 49800) Fit 2,
pide título de especialista en genética médica más 5 años de laboratorio, con
inglés suficiente; y **J-0030** (Médecin spécialiste en médecine génétique, CDD
2 años, ref. 686) Fit 1, que exige título reconocido en Luxemburgo y francés o
alemán clínico, y tú tienes A1.

## El ángulo nuevo de la semana: honorary / clinical

Funcionó, y el resultado es útil aunque no dé candidaturas. Las claves
`honorary` y `clinical` confirman que **la escala salarial clínica británica es
un patrón y no una rareza de P-0075**: 52.748–82.026 GBP en UCL, 54.499 (ST1-5)
en Liverpool, y el rango 40.190–76.582 GBP de P-0075 (Cambridge) queda
confirmado. El matiz honesto: **el contenido de esas plazas suele ser entrega
clínica de ensayos, no genética**, así que están fichadas como calibración de
escala salarial, no como candidaturas. Sirve para saber qué pedir, no dónde
presentarse.

## Regla de los 60 KB

Sigue incumplida y creciendo: **`jobs.tsv` está en 98,2 KB** (74,3 la semana
pasada) y **`postdocs.tsv` en 187,4 KB** (166,8), más `sources.tsv` en 258,7 KB
y `changelog.tsv` en 352,5 KB. **No los parto yo**, como manda el contrato:
partir un fichero obliga a cambiar `tools/build_page.py` y `tools/build_xlsx.py`
en el mismo commit y eso no es trabajo para el final de una pasada desatendida.
Tercera semana dicho.

## Qué perseguiría la semana que viene con más presupuesto

Rebarrer TODAS las filas de CCAA por «Laboratorio Clínico» en vez de por
«Análisis Clínicos», que es el falso negativo que el RD 101/2025 acaba de
crear; pagar la deuda de la rama 4 (J-0013, J-0015, J-0019, J-0022 y la
búsqueda de MSL/MedComms que esta semana no se hizo); atacar HigherEdJobs por
el endpoint correcto; recorrer la página 2 del Career Center de la ISCB;
cerrar o archivar P-0037 (NIH) si Cloudflare sigue; y revisar qué otras filas
—además de P-0004, ya resuelta— se cerraron con la regla refutada SRC-0268,
que es la única parte de esa deuda que sigue abierta.
