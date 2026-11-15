# positions — 2026-11-15

**ALERTA, capacidad todavía caída: el etiquetado de Gmail sigue sin arreglar y
esta semana NO se volvió a probar, a propósito.** La pasada A
(`label:Research newer_than:8d`) dio **cero hilos** por segunda semana, que es
exactamente lo que se predijo mientras falte el permiso: la etiqueta no se
puede escribir, así que nunca tiene mensajes y la pasada A no puede devolver
nada. La rama 5 decidió **no gastar el intento de etiquetado** porque ningún
hilo de esta semana merecía la etiqueta `Research` y probar el permiso habría
exigido escribir una etiqueta errónea en su buzón. Es la decisión correcta,
pero conviene decirlo sin adornos: **el permiso sigue sin verificar y la avería
sigue abierta.** Reconectar el conector de Gmail con permiso de modificación de
etiquetas es lo único que lo arregla; la rutina no puede. **Hilos sin etiquetar
esta semana: ninguno.**

Perfil completo (sin `PROFILE-INCOMPLETE` ni `[TODO]`). Remoto correcto. **El
checkout volvió a llegar en HEAD desacoplado** (`HEAD detached from
refs/heads/main`), tercera semana consecutiva: recuperado con `git checkout
main`, árbol limpio, `git pull --rebase` trajo los 8 commits de las pasadas de
fellowships y ecosystem del 2026-11-09. No existía informe de hoy ni commit
ajeno de `positions` fechado hoy: no fue re-disparo. Las cinco ramas
entregaron. Push directo a `main`, sin rechazo y sin rama de desvío.

## Recuento, tomado de `git diff --stat HEAD~1`

| fichero | cambio |
|---|---|
| `data/postdocs.tsv` | 7 altas (P-0103…P-0109), 18 filas actualizadas |
| `data/jobs.tsv` | 5 altas (J-0033…J-0037), 7 filas actualizadas |
| `data/sources.tsv` | 13 fuentes nuevas (SRC-0473…SRC-0485) |
| `data/subscriptions.tsv` | 1 alta (SUB-0048) |
| `data/inbox_triage.tsv` | 1 fila |
| `data/changelog.tsv` | 37 apuntes |
| `data/action_now.tsv` | 1 fila mía (J-0003), 61 ajenas preservadas |

**12 altas y 25 filas actualizadas.** Corrección honesta: el mensaje del commit
dice «26 filas actualizadas» porque conté dos veces J-0003, que se tocó en dos
escrituras. El número bueno, el del diff, es **25**.

Presupuesto de las ramas: 22 + 25 + 26 + 18 + 22 = **113 llamadas** (techo 125).
La rama 3 se pasó **una llamada** del techo duro de 25 y lo declaró ella misma:
la 26ª fue para validar su JSON y corregir una errata.

## Las tres cosas que merecen acción

1. **J-0011, el ICS catalán, queda RESUELTO y es lo más accionable de la
   semana en su prioridad número 2.** La inscripción en la bolsa es
   **permanente y siempre telemática**, se identifica con SERCAT, la titulación
   se acredita en el Gestor Curricular y **no hay plazo de baremación**: los
   baremos son los de la oposición y hay 10 días hábiles para alegar. El ámbito
   se elige por gerencia (SAP/ACUT/hospital). Dicho de otro modo: **no hay que
   esperar a ninguna convocatoria, se puede hacer hoy**, y es trabajo de una
   tarde. Lo mismo vale, con menos detalle verificado, para **J-0034
   (Extremadura, alta nueva, Fit 4)**: bolsa abierta y permanente y la
   categoría de Análisis Clínicos admite Médico Especialista.
2. **P-0103: la grieta clínico-académica vuelve a abrirse y esta vez está
   viva.** *Clinical Research Fellow – Health Legacy* en Queen Mary (ref.
   DTP671), **cierra el 2026-11-25, dentro de 10 días**, y el anuncio dice
   literalmente que la experiencia investigadora es **deseable pero no
   esencial**, abre la plaza a médicas sin doctorado y **no menciona el GMC**,
   que era el trámite que se temía bloqueante. Es Fit 3 y no entra en
   `action_now` por una razón que no se puede maquillar: **el inicio es muy
   anterior a su disponibilidad del 22-05-2027**. Vale como categoría a
   explotar en 2027 y como contacto ahora, no como solicitud.
3. **P-0107, el Broad por fin rinde por el camino correcto.** *Computational
   Scientist I* en el Center for Genomic Medicine, **laboratorio de Talkowski**,
   genética estadística de trastornos neuropsiquiátricos, **88.000–124.000 USD**,
   publicada el 29-10-2026, sin cierre, VERIFIED. Exige doctorado terminado y
   se cubre ya, así que es Fit 3 y **gancho para escribir a Talkowski en 2027**,
   no una solicitud de hoy. Ojo al dedupe: es distinta de P-0080, mismo
   laboratorio pero otra referencia.

## Lo que cerró: 10 cierres

**Ocho por plazo vencido** (LIKELY, rama 2): P-0073, P-0077, P-0079, P-0084,
P-0090, P-0093, **P-0100** (la Clinical Research Fellow de Genes & Health, que
cerró el 12-11-2026 como estaba previsto) y P-0102.
**P-0003 recuperada y cerrada**: era la mejor Fit 4 sin verificar de la base y
se resolvió por donde había que entrar, el portal propio de Mount Sinai, que
tiene **API JSON** (`careers.mountsinai.org/api/jobs?keywords=`). Cero
resultados para «Mullins» y «suicide genetics» frente a 238 postdocs vivos →
**CLOSED con Confidence LIKELY**, porque el cierre se deduce de la ausencia en
el índice, no de una fecha publicada. Es la diferencia entre decir lo que se
sabe y decir lo que se supone.
**Dos entierros en jobs**: **J-0035, Sano Genetics** (Senior/Lead Geneticist,
UK remoto, 60.000-70.000 GBP, GWAS+PRS+R/Python y admitía MSc — habría sido
excelente; **cerró hoy mismo** en su portal, «No matching jobs») y **J-0036,
el MSL de Beckman Coulter/Inizio Engage**, la pista de comunicación científica
que quedó pendiente la semana pasada: sus tres fichas dan 404 y el espejo
`es.trabajo.bz` da 403. **Enterrada a propósito como CLOSED Fit 2 para que
nadie la redescubra.**

## El carril clínico español: tres casillas cerradas de golpe

Además del ICS y de Extremadura (arriba), tres resultados que ya no habrá que
volver a buscar:
- **J-0010, Sacyl, bloqueado por diseño, no por torpeza.**
  `bolsaabierta.saludcastillayleon.es` responde 200 pero **todo está tras login
  con certificado digital, eDNI o Cl@ve**: la lista de categorías no existe en
  HTML abierto. **Esto lo tiene que mirar ella**; el CAU es el 983 459 074.
- **J-0008, SERGAS, mecanismo corregido**: no es una bolsa única, son **listas
  permanentes** (DOG de 08-08-2019) **más convocatorias sueltas por unidad con
  plazos de días**. En el histórico sí hay plazas de Análisis
  Clínicos/Bioquímica Clínica (Metabolopatías y RHA del CHUS); de **Xenética,
  ninguna**.
- **J-0021, Canarias, cerrado en negativo**: **no existe bolsa permanente**. La
  página FEA_ACL del 13-11-2026 está en nombramientos, y las listas supletorias
  se convocan por BOC con plazo corto. Lo que toca es vigilar el BOC, no
  inscribirse.
- **BOE: sexta semana sin novedad.** Ni real decreto ni programa formativo de
  Genética Médica o de Laboratorio. Lo que sí está vigente y le afecta de lleno
  es el **RD 101/2025** (BOE-A-2025-3189), que crea el título de **Laboratorio
  Clínico** y suprime Análisis Clínicos y Bioquímica Clínica. Mientras no haya
  vía transitoria, **la ruta real al SNS es la bolsa de cada CCAA con el título
  de Laboratorio Clínico**, y eso ya está escrito en el `Next_Action` de J-0003.

## EURAXESS: segunda semana a cero, y el método del epoch era falso

**Cero altas**, dicho de frente en vez de rellenar. El buscador `/jobs/search`
responde 200 pero **sólo muestra los 10 últimos anuncios** (ids 480570-480579
de unos 1.800 publicados en una semana) y ninguno es de genética, genómica,
sueño, psiquiatría ni estadística. La cosecha de ids desde fuera **ya funciona
otra vez** (WebSearch vuelve a devolver el dominio, que estaba a cero el
25-10), pero **el índice público está rancio**: unas 30 fichas, todas de
2023-2025 y con plazo vencido.

Dos correcciones que valen más que las altas que no hubo:
- **La trampa del EXPIRED, ampliada.** La ficha 478686 (el espejo de P-0099)
  lleva el literal `STATUS: EXPIRED` **estando abierta**, y además **no tiene**
  el `div id="expiration"` con `data-date-time`. Es decir: **el método del epoch
  que se registró la semana pasada en SRC-0430 falla por ausencia del campo.**
  La única señal fiable es el texto **«Application Deadline»**. Corregido en
  `sources.tsv`.
- **EURAXESS etiquetó ese postdoc como R4**, no R2. Filtrar por R2, que es lo
  que manda el prompt de la rama, **habría perdido la fila**. Merece que la
  dueña decida si se afloja ese filtro.
- **Finlandia, Portugal y Bélgica siguen ciegos, y ahora se sabe por qué.** Las
  portadas `euraxess.fi/.be/.pt` responden 200 y revelan el único filtro por
  país que existe, que es una **ruta**: `/jobs/search/country/finland-1071`. Da
  **HTTP 403, 40.655 bytes de CloudFront**, idéntico en el espejo nacional y en
  el dominio central: **todo el subárbol `/jobs/` está bajo el mismo bloqueo.**
  Los tres países sólo se pueden atacar por Tier 1 institucional. **No
  reintentar.**

## Lo que no se pudo verificar o alcanzar, con el error exacto

- **Australia sigue sin cubrir, y es un hueco con nombre propio** porque es
  donde ella tiene contacto real: `qimrberghofer.edu.au` redirige a
  **`qimrb.edu.au`**, cuya página `/people-and-careers` responde 200 pero **no
  enlaza vacantes, sólo becas**; `careers.qimrberghofer.edu.au` y
  `qimrberghofer.nga.net.au` dan **CONNECT 502**; el RSS da 200 con 739 bytes y
  **cero items**. Con Seek en 403 desde hace semanas, **la vía australiana hoy
  sólo se puede abrir por correo o por navegador**.
- **Sin verificar por presupuesto, y dos con plazo inminente**: **P-0096 (cierra
  el 16-11, mañana)**, **P-0036 (cierra el 23-11)**, P-0011 (misma causa que
  P-0003, nature.com 400) y P-0010 (CRG, 403 conocido). Las dos primeras son
  deuda de esta pasada, no de las ramas: se priorizaron los ángulos nuevos.
- **Stanley Center por apellidos: NEGATIVO y registrado.** Neale, Daly,
  Sullivan y Hultman dan «No jobs found» en el Avature del Broad, mientras el
  control McCarroll sigue dando 1 resultado, o sea que **el índice funciona y
  simplemente no tienen plaza publicada**. Lo que rinde son los **términos
  temáticos** (`Statistical` → 6 resultados, de ahí P-0107). Detalle de método:
  la ruta devuelve **301 con cuerpo vacío sin `curl -L`**.
- **Erasmus MC resuelto, y la premisa de la que partía era falsa**: **no hay
  endpoint JSON** (se buscó `fetch(`, `api`, `.json`, `graphql`,
  `__NEXT_DATA__`, `__NUXT__`); el listado viene servido en el HTML con facetas
  por ruta. 11 vacantes de ciencia y **cero** de epidemiología genética o sueño.
  El hueco holandés se cierra: no era un bloqueo, era que no hay nada.
- **VU Amsterdam**: 28 vacantes y **nada del Netherlands Twin Register** →
  queda como correo especulativo, que es trabajo de ella.
  (`vu.nl/en/about-vu/working-at-vu-amsterdam` da 404.)
- **CNIO: 404 por ruta equivocada de la rama**, no por bloqueo. La buena, sacada
  del menú de la propia página de error, es
  `cnio.es/en/about-the-cnio/employment-opportunities/`, y queda **pendiente**.
- **Cardiff**: `cardiff.ac.uk/jobs/search-jobs` → **403**. Un intento, ninguna
  fila. Sigue sin feed de vacantes vivas.
- **KCL con la ruta buena** (`?term=`): sólo el Clinical Research Fellow 162406
  del IoPPN, **descartado sin crear fila** porque exige GMC y ST3 de psiquiatría
  en el NHS. Bien descartado: una fila así sería ruido.
- Otros bloqueos de un intento, fichados para no reincidir:
  `aegh.org/ofertas-de-empleo/` → muro «Please wait while your request is being
  verified»; ficha `careers.ashg.org/jobs/22716892/` → muro antirrobot (el
  **listado** sí se lee; `/jobs/` da **520**); `higheredjobs.com` búsqueda
  avanzada → 200 con **cuerpo de 212 bytes** sin resultados;
  `jobs.mountsinai.org` → CONNECT 502; `labs.icahn.mssm.edu/mullinslab` → 403;
  404 en `ispg.net/career-center/`, `eshg.org/jobs`, `eshg.org/job-board`,
  `ashg.org/careers/career-center/` y en `/naturecareers/jobs.rss`, `/rss`,
  `/rss/jobs`; `jobs.ac.uk/job/DTH864/` → **301 a http**, hay que seguir la
  redirección a mano. **`segenetica.es` no tiene tablón de empleo: ángulo
  cerrado.**

## Tres conflictos declarados, ninguno resuelto en silencio

1. **P-0022 (Clinical Research Associate, Univ. of Alberta) está como viva en la
   base y el tablón de la ISPG la da por `status-expired` desde el 18-01-2026.**
   **No se cambió la fila**: la ISPG es un espejo Tier 2 y el estado Tier 1 no
   se comprobó. Queda el conflicto escrito para que se resuelva con una llamada
   la semana que viene. (De paso: el tablón de la ISPG, descifrado vía
   `admin-ajax` porque `/jobs/` es JS y `wp-json` da 404, **está muerto**: dos
   anuncios y los dos caducados.)
2. **P-0103 puede ser reedición o plaza hermana de P-0100.** Mismo centro
   (Queen Mary) y mismo programa Health Legacy, pero **referencia distinta**
   (DTP671 frente a DTL549) y **plazo distinto** (25-11 frente al 12-11 ya
   vencido). **Decisión tomada y explicada: fila nueva**, porque la clave de
   dedupe incluye `host+path` de la URL y son anuncios distintos; el conflicto
   queda escrito en el `Source_Note` de P-0103 para que ella lo cierre si al
   abrirlas ve que son la misma.
3. **La plaza del VHIR se fecha el 10-11 en el RSS y el 13-11 en el JSON-LD** de
   la misma ficha. Sin reconciliar, dicho en la fila.

## Una duplicación evitada, y así se evitó

La rama 5 entregó como alta la plaza del **CoDE Lab de Malanchini (QMUL, ref.
DTH864)**, que **ya estaba en la base como P-0085** y cerrada. **No se creó la
fila**: se **fusionaron sus datos nuevos en P-0085** —PI, laboratorio, banda
salarial **39.187-47.550 GBP** y, lo que importa, la cláusula «*or expect to
soon receive a PhD*»— y se dejó constancia en su `Source_Note`. Es el segundo
hallazgo de la semana que confirma el patrón de P-0002: **las plazas que
aceptan doctorado inminente son la única vía que no choca con su reloj de
febrero de 2028**, y conviene buscarlas por esa frase literal.

## Filas suyas cuyos hechos cambiaron bajo ella

**Ninguna.** `data/owner_status.json` sigue siendo `{}`: la dueña no ha marcado
todavía ninguna fila desde la página, así que **ninguna de las 25
actualizaciones ni de los 10 cierres pisa una decisión suya**, porque aún no hay
decisiones. Sexta semana igual. Merece decirse de otro modo: **la base lleva
seis semanas creciendo sin que nadie haya marcado nada en la página**, y si la
página no se está usando, eso es más importante que cualquier fila de esta
pasada.

## Suscripciones

**48 filas, las 48 PENDING** por la definición del contrato (TSV en TODO y sin
marca en `owner_status.json`). Una alta: **SUB-0048**, el *talent pool* Connect
de **Sano Genetics**, propuesto justo porque su plaza buena (J-0035) se cerró
hoy y el talent pool es la única forma de enterarse de la siguiente.
Las ramas 1 y 5 propusieron **cero a propósito** y con razón: la alerta de
búsqueda guardada de EURAXESS **ya está dos veces** (SUB-0002 y SUB-0018, ambas
TODO) y lo que falta no es otra fila, **es que ella ejecute una**.
**Pendiente de la semana pasada que sigue pendiente**: la alerta por correo de
**SfN NeuroJobs**, único rodeo al 403 de ese tablón. No se añadió porque nadie
leyó una URL de alta real y las reglas de honestidad prohíben inventarla.

## Fuentes nuevas: 13

Lo aprovechable: la **API JSON de Mount Sinai** (que es lo que recuperó P-0003 y
el único modo de verificar ese centro, porque su HTML va por JS), el **RSS de
`jobs.vhir.org`** —el VHIR es un **Teamtailor**: `jobs.vhir.org/jobs.rss` da los
12 anuncios con fecha y cada ficha trae **JSON-LD**, con lo que **queda resuelta
la única puerta viva a CIBERSAM**—, la **corrección de SRC-0430** sobre el epoch
ausente de EURAXESS, los **portales EURAXESS nacionales con los ids de país y su
403 documentado**, la **URL buena del tablón de la ESHG**
(`/collaborations/jobs-training-collaborations-grants/job-opportunities`, porque
`sources.tsv` apuntaba a `/home`, que es inútil) y el **`admin-ajax` de la
ISPG**, registrado precisamente como negativo. Fuentes nunca tocadas antes:
los portales EURAXESS nacionales, la API de Mount Sinai, el RSS del VHIR y el
`seleccionpersonal` del SES extremeño. **Las cinco ramas estrenaron fuente.**
Corrección honesta de la rama 3: la mayoría de rutas que le parecían nuevas ya
estaban registradas (SRC-0346, SRC-0223, SRC-0129/0193/0225, SRC-0042/0220,
SRC-0311) y lo dijo en vez de inflar el recuento.

## Regla de los 60 KB

Sigue incumplida y creciendo: **`postdocs.tsv` 233,1 KB** (213,8 la semana
pasada), **`jobs.tsv` 115,3 KB** (102,3), `sources.tsv` 390,8 KB,
`changelog.tsv` 524,4 KB, `groups.tsv` 401,7 KB, `fellowships.tsv` 352,7 KB.
**No los parto yo**, como manda el contrato: partir un fichero obliga a cambiar
`tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit y eso no es
trabajo para el final de una pasada desatendida. **Sexta semana dicho.**

## `action_now` y el fallo de las fechas en prosa: lo mismo, una semana después

`action_now` se queda otra vez con **una sola fila mía, J-0003**, por ser Fit 5
con `Competition_Level = LOW`. El efecto estructural no ha cambiado y ya van
seis semanas: **nueve filas de Fit 4 de su vía clínica española —su prioridad
número 2— que la regla no puede surfacear nunca** (J-0002, J-0007, J-0008,
J-0010, J-0011, J-0016, J-0023, J-0027, J-0028, y ahora **J-0034** hace diez),
porque son bolsas permanentes sin plazo y la regla sólo admite sin plazo lo que
es Fit 5. **P-0002, la mejor acción de la base, tampoco entra**, por lo mismo.
La decisión es suya: o sube alguna a Fit 5, o la regla necesita una cláusula
para inscripciones permanentes.

**Y el fallo de las fechas en prosa reapareció exactamente donde se avisó.**
`rebuild_action_now.py` extrajo «2026-11-07» de la **prosa** de la columna
`Deadline` de J-0003 y la pintó como **`Days_Left = -8`**: la fila número 1 de
su lista de acción aparecía en la página como **cerrada hace ocho días**. Se
corrigió **vaciando esa celda de fecha**, no tocando el Fit, y sin perder un
solo dato: la evidencia (los seis sumarios diarios del BOE leídos uno a uno)
**ya estaba íntegra en `Source_Note`**, y la comprobación de hoy está en
`Requirements_Key`. Es el mismo remedio que se aplicó a J-0023 la semana pasada
y **es un parche, no el arreglo**: siguen habiendo filas con prosa con fechas
dentro de `Deadline` y cualquiera puede repetir el falso positivo. **Arreglarlo
de verdad toca los generadores y es trabajo de la dueña.**

## Nota de entorno

Una llamada Bash de la rama 1 fue **denegada por el clasificador de permisos**
(«Unauthorized Access») por llevar un bucle con user-agent de navegador;
rehecha con `curl` plano respondió 200 igual. Conclusión útil: **el user-agent
falso de SRC-0304 ya no hace falta** y además es lo que levanta la denegación.

## Qué perseguiría la semana que viene con más presupuesto

Por orden de rentabilidad: **cerrar P-0096 y P-0036 antes de que venzan** (deuda
de hoy) y **P-0011 por el dominio del Icahn**, ahora que se sabe que su API JSON
funciona; **resolver el conflicto de P-0022** con una sola llamada a Oracle
Cloud; **CNIO por la ruta buena** y el **RSS del VHIR exprimido** para el resto
de CIBERSAM; **Australia por correo**, que es la única vía que queda viva hacia
QIMR, más el Netherlands Twin Register; **buscar por la frase literal «expect to
soon receive a PhD» / «nearing completion»** en jobs.ac.uk y Nature Careers,
que es el único ángulo que esquiva su reloj de febrero de 2028 y que ya ha dado
tres hallazgos; **los términos temáticos del Avature del Broad** (`Genetics`,
`Psychiatric`, `Neurodevelopmental`), ahora que se sabe que los apellidos no
rinden y los temas sí; y la **MSCA PF 2027** (dato Tier 2 sin confirmar:
abriría el 07-04-2027 y cerraría el 08-09-2027, lo que encajaría con una
defensa en febrero de 2028) a confirmar en Tier 1 — aunque eso es beat de
`fellowships`, no mío.
