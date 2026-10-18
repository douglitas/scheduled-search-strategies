# positions — 2026-10-19

**ALERTA, y no es un fallo de entrega sino de datos: la regla de verificación
SRC-0268 está REFUTADA y puede haber cerrado filas que siguen vivas.** La regla
decía que un HTTP 307 en `euraxess.ec.europa.eu/jobs/<id>` prueba que el
anuncio se retiró. Es falsa: `/jobs/473773`, que el portal mostraba ese mismo
día como oferta ABIERTA (Uppsala, plazo 2026-11-16), devuelve exactamente el
mismo 307 a `/jobs/search` que el `/jobs/557315` con el que se cerró P-0004.
Los ids antiguos sí dan 200 con la ficha completa y el estado explícito en el
cuerpo (campo «Job Status», rótulo «STATUS: EXPIRED»): **la verificación tiene
que leer el cuerpo, nunca el código de respuesta.** Hay que revisar qué otras
filas se cerraron con esa regla. P-0004 queda esta semana en CLOSED pero con
Confidence bajada a UNVERIFIED y una acción de comprobación manual: no me
inventé que esté abierta, pero su cierre no está probado.

Pasada semanal de posiciones (pestañas propias: `postdocs`, `jobs`). Cinco ramas
en paralelo, una por beat, más un hallazgo recogido por el orquestador. Perfil
completo: sin `PROFILE-INCOMPLETE` ni `[TODO]`, así que se investigó con
normalidad. No existía informe de hoy: no fue un re-disparo. El checkout llegó
con HEAD desacoplado de `main`, se corrigió antes de tocar nada.

Nota de fecha: el entorno daba 2026-10-18, pero la fecha en Europe/Madrid era
ya 2026-10-19 (lunes). Se usó **2026-10-19** en todo: commit, filas y este
fichero, como manda el contrato de calcular la fecha una sola vez.

## Recuento, tomado de `git diff HEAD~1 --stat`

| fichero | cambio |
|---|---|
| `data/postdocs.tsv` | 12 altas (P-0072…P-0083), 21 filas actualizadas |
| `data/jobs.tsv` | 3 altas (J-0023…J-0025), 3 filas actualizadas |
| `data/sources.tsv` | 14 fuentes nuevas (SRC-0304…SRC-0317) |
| `data/subscriptions.tsv` | 2 altas (SUB-0032, SUB-0033), las dos TODO |
| `data/inbox_triage.tsv` | 2 filas, las dos IGNORE / DONE |
| `data/changelog.tsv` | 55 apuntes (29 NEW/ADDED + 26 actualizaciones) |
| `data/action_now.tsv` | 1 fila mía (J-0003), 36 ajenas preservadas |

113 inserciones y 25 supresiones. **Las 25 supresiones son exactamente los
pares `-/+` de las 24 filas modificadas más la de `action_now`: no se perdió
ninguna línea.** Comprobado columna a columna contra `HEAD`: `Owner_Status`
intacto en las 93 filas preexistentes, ninguna fila desaparecida, y las 15
nuevas nacen con la columna vacía.

## Las tres cosas que merecen acción

**1. J-0003 — alegaciones a los dos reales decretos de Genética. Sigue ABIERTO,
quedan 7 días (vence el 2026-10-26). Fit 5, competencia LOW, esfuerzo S. Es la
fila 1 de `action_now` y la más valiosa de la base.**
Verificado Tier 1 hoy: los dos proyectos siguen en «Proyectos abiertos» con las
fechas 02-10-2026 → 26-10-2026. No hay prórroga ni cierre anticipado, el BOE no
ha publicado ninguno de los dos decretos y no hay noticia de Consejo de
Ministros sobre la entrada en vigor, así que **la bisagra frente al 22-05-2027
sigue entera y sin resolver.** Lo nuevo y lo que convierte esto en tarea de
media hora: la página publica el canal exacto, que **no es la sede electrónica
sino el buzón `informacion_publica@sanidad.gob.es`**, y los dos códigos de
expediente obligatorios en el asunto, **DG/91/26** (Genética Médica) y
**DG/90/26** (Genética de Laboratorio). **Son dos correos, uno por decreto**, y
solo se consideran las aportaciones identificadas y recibidas en plazo. Está
redactado en el `Next_Action` de la fila.

**2. P-0002 (Max Planck Nijmegen, Statistical Genomics / Genetic Epidemiology)
deja de ser una fila dudosa y se queda, aun así, fuera de `action_now`: eso es
lo que hay que decidir.**
La ficha Tier 1 del MPI confirma ahora ella misma el E13 (73.999,91–91.055,27
EUR/año) que antes solo sostenía una fuente Tier 2, y sobre todo dice que **el
inicio del 01-12-2026 es NEGOCIABLE**, que era la única objeción seria contra su
reloj de febrero de 2028. Sigue viva, sin aviso de plazo vencido, online desde
el 12-08-2026, Confidence VERIFIED. Acción: escribir a `martina.bernhard@mpi.nl`
y a Beate St Pourcain.
**Pero no entra en `action_now` y no la he forzado.** La regla de selección pide
Fit 4-5 que cierre dentro de 90 días, o Fit 5 si no tiene plazo; P-0002 es Fit 4
sin plazo, así que cae justo fuera. Subirla a 5 la metería en la lista, y eso es
precisamente la edición cosmética que el contrato prohíbe. **Lo dejo en tu mano:
si crees que con el inicio negociable ya es un 5, cámbialo tú y entrará sola la
semana que viene.**

**3. P-0036 (KCL, Research Scientist Maternal Sleep) NO cerraba hoy: KCL amplió
el plazo al 2026-11-02, con salario publicado de 53.947–63.350 GBP.**
Es de su línea 3 (genética del sueño) y la base la tenía venciendo justo hoy, así
que sin esta comprobación se habría perdido por caducidad falsa. Hay dos semanas
más. Se destapó con el truco nuevo de la semana: **cada ficha de jobs.ac.uk y de
kcl.ac.uk incrusta un JSON-LD con `status` (live/archive), `closing_date`,
`validThrough`, `datePosted` y salario**, lo que permite verificar cinco plazas
por llamada sin leer HTML. Es la verificación más barata del repo.

**La conclusión incómoda de la semana, que vale más que cualquier fila:** hay 12
altas en `postdocs` y **ninguna llega a Fit 4.** Las mejores por contenido
—Amsterdam UMC (P-0072, ENIGMA-EEG, GWAS+PRS sobre fenotipos EEG, PI Dirk Smit),
Karolinska KI-PGI (P-0079, pide literalmente GWAS, PRS y diseños familiares en
trastornos psiquiátricos, su línea 2 exacta), Leicester GENVASC (P-0074, formato
pensado para clínicos), IDIS Santiago (P-0083, su línea 1 en España)— **son todas
Fit 3 por el mismo motivo y no por el perfil: exigen doctorado concluido e
incorporación a principios de 2027, y ella no está libre hasta el 22-05-2027 ni
defiende hasta febrero de 2028.** Los tablones de vacantes inmediatas van a
rendir poco hasta finales de 2027. **El trabajo útil ahora es de contacto, no de
candidatura**, y estos son los correos que lo valen: Dirk Smit (Amsterdam UMC),
`anna.kahler@ki.se` como puente hacia Lu Yi (KI-PGI, para la cadencia 2027-28 y
una posible estancia corta previa), `farrer@bu.edu` (P-0050, confirmada «open
until filled», admite inicio diferido, **compatible con 2027**; ojo, la web tiene
la errata «farrer@bu.edul») y `ceres.fernandez.rozadilla@sergas.es` (IDIS, que
ofrece apoyo explícito para solicitar MSCA, Xunta de Galicia y Miguel Servet).

## Lo que cerró

P-0045 (QMUL) cerrada sin ambigüedad, `jobs.ac.uk` la marca `status=archive`.
P-0046 (KCL, ML for mental health) cerrada, venció el 18-10. P-0049 (QIMR
BV000085) ya no está en TurboRecruit. P-0052 (Bonn) se da por cerrada por
vencimiento, con la cautela de que su única URL es de LinkedIn y no se pudo
reverificar en Tier 1. J-0025 (City Therapeutics) nació CLOSED. Las dos fichas
pendientes del Department of Genetics de Cambridge resultaron cerradas y de otro
campo: PC51215 = DTC525 (línea germinal de Drosophila) y PC51194 = DTB355 (Cagan
Lab, genómica somática comparada). P-0051 (Columbia) rebajada a UNVERIFIED: sin
fecha alguna, pie «Copyright 2023» y **exige doctorado en estadística,
bioestadística o informática, que el suyo no es.**

## Lo que no se pudo verificar o alcanzar

- **EURAXESS, regresión que deja la rama 1 casi sin superficie.** SRC-0222 decía
  que `/jobs/hosting` renderizaba y declaraba 73 resultados el 2026-10-05; hoy
  devuelve el listado genérico del portal entero (6.712 ofertas, 672 páginas,
  ninguna del campo) e ignora la faceta, con y sin parámetros de orden. El fallo
  que SRC-0267 probó en el buscador ya alcanza a las acogidas, que era justo la
  parte que encajaba con sus relojes. `/jobs/funding` da 404. **Rama 1 cerró con
  0 altas, y es un resultado honesto, no un hueco.** EURES queda bloqueado de
  entrada: buscador en «Loading...» y su endpoint JSON da 404.
- **Las tres CCAA PENDING siguen sin resolver, y dos por bloqueos nuevos.**
  J-0017 (Asturias) falla por tercera semana y ahora por razón distinta:
  `sede.asturias.es` y `www.astursalud.es` **cortan los dos la conexión** desde
  el proxy, así que no era ruta equivocada — el Principado no se deja leer y solo
  lo resuelve una persona con navegador o una llamada al SESPA. J-0021
  (Canarias): el archivo 2026 del BOC se sirve completo pero sin buscador
  utilizable, y filtrar por categoría exigiría recorrer un año de boletín número
  a número; **recomiendo congelar la fila y reactivarla cuando tenga el título.**
  J-0012 (GSK) **no se re-intentó a propósito**, está fichada como buscador
  JavaScript: su `Last_Verified` se deja como estaba en vez de sellarlo hoy en
  falso.
- La paginación del eploy de Cardiff sigue rota (`&page=2` devuelve la página 1),
  así que **P-0063 queda otra semana sin reverificar.** El plazo de P-0070 (Oslo)
  tampoco: la ficha Tier 1 está viva (Jobbnorge 309329) pero la fecha de cierre
  no aparece en el texto accesible por curl, hace falta navegador.
  `jobs.cam.ac.uk` no se puede atacar por número de referencia: el PC5xxxx no es
  el id de URL. Sin tocar: deCODE, Erasmus MC, IMIM/CRG/CIBER/IIS-FJD y NIH OITE
  (P-0037 sigue PENDING). **No hubo ninguna novedad de comunicación científica
  esta semana**, ni MSL ni MedComms, y J-0013, J-0015, J-0019 y J-0022 se
  quedaron sin reverificar por presupuesto.

## Trampas de verificación fichadas esta semana

Tres, y las tres son del mismo tipo: **un fetch con éxito no prueba que la plaza
siga viva.** En **Greenhouse**, el id de un anuncio retirado no da 404: da 200 y
redirige en silencio al índice del tablón de la empresa. En **EURAXESS**, el 307
no prueba retirada (arriba). En **jobs.ac.uk**, la respuesta es **301** y no 200,
y sin `curl -L` el cuerpo llega vacío, lo que probablemente explica fallos
anteriores. También: `?keywords=` del ISCB Career Center **no filtra** —
'statistical genetics' y 'epidemiology' devuelven el listado completo, así que
la tarea pendiente de rotar claves ahí **era inútil y se cancela**. Y
AcademicTransfer confirma con cero vacantes que **el camino al Erasmus MC no es
AcademicTransfer**: esa tarea pasa a la rama 3. DTE422 y DTE433 son el MISMO
anuncio de Manchester (ref. BMH-032529), duplicado del tablón.

## Buzón

El conector de Gmail funcionó. **Pasada A (`label:Research`) devolvió cero: la
etiqueta sigue con 0 mensajes históricos y ninguna suscripción está activada, así
que no es un fallo ni un bug.** Pasada B: 2 hilos en 8 días, los dos boletines de
Substack por suscripción, ninguno una oportunidad; fichados IGNORE / DONE con el
motivo para que no se vuelvan a mirar. **No queda nada PENDING: `ecosystem` no
hereda trabajo de aquí.** `source_inbox.json` estaba vacío. No se etiquetó nada
porque etiquetar boletines irrelevantes degrada la etiqueta; el dato que ahorra
una llamada la próxima vez: **el id de la etiqueta Research es
`Label_1910483919685933112`.** Privacidad respetada: solo constan dos boletines
de suscripción, nada personal.

## Filas de la dueña cuyos hechos cambiaron bajo ella

Ninguna. `owner_status.json` sigue vacío ({}) y no hay filas marcadas READ,
IN_PROGRESS, APPLIED, RESOLVED, DISCARDED ni REVISIT. Todo lo tocado estaba en
NEW o sin marca, así que no hay ningún modelo mental que se haya quedado obsoleto.

## Suscripciones

**33 pendientes: las 33 del fichero están en TODO y `owner_status.json` está
vacío, así que ninguna de las propuestas en nueve semanas de radar se ha
activado.** Mientras no se active alguna, la Parte A de la rama 5 seguirá
viniendo vacía cada lunes: **el cuello de botella está en la activación, no en el
descubrimiento.** Las dos de mayor rendimiento inmediato siguen siendo
**SUB-0002 y SUB-0018 (alertas de EURAXESS)** y hoy valen más que nunca, porque
son exactamente lo que rodearía el buscador roto.
Dos altas, las dos TODO y las dos del tope del contrato:
- **SUB-0033 — búsqueda guardada de AcademicTransfer** (`?q=genetic epidemiology`).
  Es el canal que destapó la mejor pista académica de la semana (Amsterdam UMC).
- **SUB-0032 — alerta por correo de THEunijobs para Australia**, la que la pasada
  del 12-10 dejó fuera por este mismo tope prometiendo reproponerla. Cumplido.
Se quedaron fuera a propósito, razonadas para que no se pierdan: la alerta de
Greenhouse de City Therapeutics (una sola biotech, y su plaza ya está CLOSED) y
**el aviso del Varbi de Karolinska — y esta merece explicación, porque su valor
era alto: la rama 3 buscó el enlace de alta y no lo encontró, y fichar un
mecanismo de alta no verificado habría sido inventarlo.** Para el hueco de KI la
corrección real no es una suscripción sino la cadencia de SRC-0219 (abajo).

## Fuentes nuevas

14. La más rentable es un método, no una web: **el JSON-LD de las fichas de
jobs.ac.uk y kcl.ac.uk**, que da estado, plazo, fecha de publicación y salario en
una sola llamada y es lo que destapó la ampliación de P-0036. Las otras de peso:
**`ki.varbi.com`**, el portal Varbi de Karolinska, 83 vacantes legibles por
WebFetch sin JavaScript y con el MEB como filtro útil — el hub de genómica
psiquiátrica de la UE que no cubría ninguna rama, y destapó P-0079 en la primera
lectura; **el RSS del Trainee Job Board de la SRS**, con `pubDate` legible por
máquina, que resuelve el «Oct 12» ambiguo del HTML; **la primera fuente de
Greenhouse de la base**, que no tenía ninguna pese a que J-0020 salió de ahí, con
la trampa del 200 anotada; **la página de bolsas constituidas del SESCAM**, con
un truco de acceso reutilizable (la ruta adivinada daba 404 pero **la propia
página de error sirve el menú de navegación completo**, y de ahí salió la ruta
real); y **el patrón de la AEGH**: sus fichas de oferta no traen el detalle, solo
título y un enlace a un PDF en `/wp-content/uploads/`, que WebFetch no digiere y
`curl` + `pdftotext -layout` sí. El resto son bloqueos fichados para no volver a
pagarlos (EURES, ALLSTAT/JISCMail 403, el archivo de boletines de ISPG) y el
tablón de la Marie Curie Alumni Association, útil solo como cantera de ids que
renderizan, nunca para plazos.

**Hallazgo recogido fuera de rama:** la rama 4 vio que la AEGH publicó «Oferta
laboral: POSTDOC» el 15-10-2026 y lo enrutó correctamente fuera de su beat por
ser académico, sin registrarlo. Como `postdocs` es pestaña de esta misma rutina,
lo recogí yo en vez de perderlo una semana: es **P-0083**, postdoc R2 de 3 años
en el Cancer Predisposition & Biomarkers Lab del IDIS de Santiago, con plazo
30-11, ~30.000 EUR/año y apoyo explícito para MSCA / Xunta / Miguel Servet.
Leído en el PDF Tier 1. **Cautela de fecha: el PDF imprime «30th November» sin
año y su página 2 es solo imagen; el 2026 es inferencia mía a partir de la
publicación y de la ventana de incorporación, no lectura literal.**

## Avisos de proceso

- **SRC-0219 (Varbi de KI) estaba fichado desde el 2026-09-28 y aun así la plaza
  del KI-PGI, publicada el 02-10-2026 con plazo de 4 semanas, no se recogió hasta
  hoy, a 11 días de su cierre.** Fichar una fuente no la cubre si nadie la
  recorre: conviene subirle la prioridad y la cadencia.
- Contradicción menor sin reconciliar, registrada en vez de resuelta: el anuncio
  de Alberta en la ISPG se titula «On-site» y el cuerpo lo describe como híbrido.
- **Regla de los 60 KB: `jobs.tsv` ha pasado a 74,3 KB y `postdocs.tsv` está en
  166,8 KB** (y los compartidos `sources` y `changelog` muy por encima). No los
  parto yo, como manda el contrato: partir un fichero obliga a cambiar
  `tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit y eso no es
  trabajo para el final de una pasada desatendida. Queda dicho para que lo
  decidas tú.
- Para la rama 1: con defensa en febrero de 2028, **la primera convocatoria
  MSCA-PF realmente elegible es la de 2028, no la de 2027** que figuraba en las
  acogidas del 05-10. Conviene confirmarlo en el texto de la convocatoria, porque
  la búsqueda de grupo de acogida se abre con mucha antelación.

## Qué perseguiría la semana que viene con más presupuesto

Revisar qué filas se cerraron con la regla refutada de SRC-0268 y reabrir las que
no estén probadas; cerrar las tres CCAA que quedan (Cantabria, Baleares y La
Rioja) por BOC Cantabria, BOIB y BOR en vez de por los portales de salud, que dan
403 o 404; añadir al barrido las claves «Honorary Resident Doctor» y «Honorary
Clinical», que es el formato con el que se anuncian los postdocs reservados a
clínicos y el que premia de verdad su MD+PhD (ej. DTC638 de Cambridge,
40.190–76.582 GBP); recorrer el MEB de Varbi con la cadencia corregida; atacar
Erasmus MC por su propio dominio ya que AcademicTransfer no lo cubre; y cerrar
P-0063 (Cardiff), P-0070 (Oslo) y P-0037 (NIH OITE), que llevan dos semanas
pendientes por bloqueo y no por falta de intento.
