# fellowships — 2026-11-02

Las cinco ramas completas, los seis encargos de la semana pasada cerrados
(cuatro resueltos, uno resuelto como «no existe» y uno a medias). Ninguna
entrega se rompió y ninguna capacidad se cayó. El buzón de Gmail **no** se
leyó aquí: lo lee la rutina `positions`, que corrió ayer, 2026-11-01.

## Recuentos (de `git diff --stat HEAD~1`, no de memoria)

| fichero | filas antes → después | altas | modificadas |
|---|---|---|---|
| `fellowships` | 85 → 91 | 6 | 38 |
| `watchlist_closed` | 29 → 29 | 0 | 21 |
| `action_now` | 44 → 46 | mías 4 (antes 2) | 42 ajenas preservadas |
| `sources` | 394 → 413 | 19 | — (append-only) |
| `subscriptions` | 39 → 43 | 4 | — (append-only) |
| `changelog` | 1235 → 1300 | 65 | — (append-only) |

Ninguna fuente se descartó por duplicado: las 19 propuestas eran URL o consulta
nuevas, comprobadas contra las 394 existentes por URL+consulta.

## Las tres cosas que merece la pena hacer, y por qué

### 1. Darse de alta como socia de la SENC antes del 1 de diciembre — cuatro semanas

**F-0019, FENS/IBRO-PERC Exchange Fellowships**, ahora VERIFIED. La página del
programa publica literalmente que **la ronda con plazo 15-04-2027 abre el
01-12-2026**, y es la única ayuda de peso de toda la base para la que es
elegible **ya, como doctoranda**, sin esperar a febrero de 2028. 4.000 EUR,
estancia de 1 a 4 meses en un grupo europeo, Effort S.

El requisito que no se puede improvisar es la **membresía de FENS vía la SENC**,
y el reloj es de cuatro semanas. Además una estancia corta financiada es la vía
más barata de convertir un contacto en la carta de acogida que luego exigen
EMBO, MSCA y HFSP, así que esto no es sólo 4.000 EUR: es la pieza que
desatasca las tres grandes.

**No está en `action_now`** y conviene saber por qué: su plazo cae a 164 días,
fuera del horizonte de 90 que fija la regla de selección, y su
`Competition_Level` es UNKNOWN, así que no entra por la puerta de competencia
baja. La regla funciona como debe; el aviso tiene que viajar por aquí.

### 2. Escribir a `fellows@mrc.ukri.org` — el hallazgo de la pasada

**F-0084, MRC Early Independence: Clinician Scientist Fellowship**, pasa a
VERIFIED y **la fila apuntaba a un esquema SUSTITUIDO** (la página antigua dice
«This fellowship has been replaced»). URL corregida. Con la página vigente leída:

- **No hay ventana de años post-doctorado ni de edad.** Textualmente.
- **El doctorado no hace falta al solicitar, sólo antes de que la ayuda
  EMPIECE.** Esto adelanta casi un año su primera ronda creíble: de «enero de
  2028» a la que **cierra el 01-09-2027**, y quizá la del 07-04-2027.
- Sí, una médica española residente en España puede optar: la cláusula de
  nacionalidad es expresamente abierta. Lo que la condiciona es que una
  organización británica la emplee, más registro GMC y condición de *specialty
  registrar*.
- Se resuelven los dos conflictos que la fila arrastraba: los tres plazos
  contradictorios eran rondas distintas de un patrón trianual real, y las dos
  cifras de sesiones clínicas (2 y 4) son las dos caras de una misma regla.

**La ronda abierta, que cierra el 2027-01-13, NO es su ronda**: sus inicios van
de octubre de 2027 a enero de 2028, antes de su defensa. Sí está en
`action_now`, y con razón, porque lo urgente no es solicitar sino preguntar y
abrir acogida (los departamentos británicos piden 6-12 meses). Las tres
preguntas al programme manager están escritas en `Next_Action`.

### 3. Poner F-0023 en el calendario: 4 de febrero de 2027

**ESHG 2027 conference fellowships**, Fit 5, y ahora el Fit está sostenido por
**dos vías de elegibilidad independientes** leídas verbatim: entra como
*student* a fecha del plazo, y además como médica que **no** ha completado aún
su especialización (la residencia acaba el 22-05-2027, cuatro meses después del
plazo), vía que le deja la puerta abierta hasta ~2031. O sea que **su
elegibilidad aquí no depende de la ETA de la defensa**, que es lo que fragiliza
casi todo lo demás de la base.

Y el esfuerzo baja a **XS con fundamento**: el envío del resumen ES la
solicitud, marcando casillas en el paso «Fellowships & Awards». Coste marginal
casi cero sobre un resumen que ya vaya a enviar.

**Aviso de calendario:** hoy quedan 94 días para el plazo, cuatro por encima del
horizonte de 90, así que **esta semana no aparece en `action_now` y la semana
que viene sí**. No he tocado nada para colarla: el sitio donde tiene que leerse
hoy es este informe.

## Lo que cerró, y lo que se corrigió por estar mal

- **F-0077 (DMM Conference Travel Grants) llevaba un plazo ya vencido**, el
  2026-10-30, con Status OPEN, y estaba en `action_now` en el puesto 2. Es el
  riesgo concreto que el encargo pedía cerrar. Corregido a la ronda real
  siguiente, **2027-02-26**, VERIFICADA, no estimada: el financiador publica la
  escalera entera de 2027 y no hay que extrapolar nada. Sale de la lista corta
  por fecha, correctamente.
- **F-0036 (CSIC Premios a Tesis)** decía OPEN desde agosto y en realidad su IV
  edición **cerró el 2026-02-13**, hace nueve meses. Y la restricción de CSIC,
  que se arrastraba como suposición, queda confirmada y es más dura: la tesis
  tiene que haberse *realizado y defendido* en un centro del CSIC. **No
  elegible, definitivamente.**
- **F-0073 (Plan GenT2)** se cierra por fecha pasada. Ver conflictos.
- **F-0062 (Premios Extraordinarios UMU)** cerró el 2026-10-15; su edición será
  la de ~octubre de 2028, porque va por curso académico de la defensa.
- **F-0008 (EMBO)** queda marcada **NO ELEGIBLE** y por eso sale de la lista
  corta pese al Fit 4: falta la primera autoría **aceptada** (sus dos
  manuscritos siguen en revisión) y presentarse siendo inelegible quema uno de
  los dos únicos intentos vitalicios. **Palanca nueva:** la propia EMBO admite
  como alternativa un preprint de primera autora con revisiones públicas de un
  servicio independiente de *peer review*; averiguar cuáles cumplen su criterio
  desbloquearía el corte del 22-01-2027 sin esperar a las aceptaciones.
- **F-0031 (Guarantors of Brain)**: primera lectura directa del financiador en
  la historia de la base, y el Fit 1 por fin tiene causa: la ayuda está
  **restringida a formación doctoral en instituciones del Reino Unido**.
- **F-0026 y F-0081 (ESRS)**: ventana anual **fechada por fin** tras varias
  pasadas, 1 de diciembre a 31 de enero. F-0026 estaba en OPEN, incorrecto
  desde enero; las dos pasan a FORTHCOMING.
- **Relojes cerrados que eran «sin verificar»:** la lista de los 32 estados del
  EMBC (EMBO); el reloj del BBRF, que **no es de años desde el doctorado sino de
  PUESTO**, y para MD pregunta por el año de fin de residencia; y los plazos de
  los premios **BGA, resueltos como «no son públicos»** — no merece más gasto.
- **ERC (F-0018):** su ventana, con defensa en feb-2028, va del otoño de 2030 al
  de 2034. Dato con consecuencia: el margen con el corte de los 2 años es de
  **semanas** (01-01-2028 frente a feb-2028), así que adelantar la defensa a
  enero de 2028 ganaría un año entero de ventana. La fecha de defensa es una
  decisión estratégica, no sólo logística.

## Watchlist: ninguna reapertura

**La SES sigue sin publicar las bases de 2027** y su ventana estrecha se agota
en tres días. Pero la rama trajo algo mejor que un negativo: **el tripwire
definitivo**. La página pública de becas de la SES tiene fecha de modificación
propia, legible en una llamada, y vale **para las tres filas a la vez**
(W-0012, W-0017, W-0026): `pages?search=becas&_fields=link,modified` da
`2025-11-03T11:53:19`, *exactamente* el día en que se subieron las bases de
2026. Un año sin tocarse. Cuando salgan las de 2027 cambiará el mismo día.
Esto sustituye el test por nombre de fichero, que ya había dado falsos
positivos y había perdido un PDF de vista. Corolario que cierra el misterio de
la pasada anterior: la página sigue etiquetando las convocatorias de 2026 como
«CONVOCATORIA ABIERTA» simplemente porque nadie la ha editado; la etiqueta es
inercia, no información.

Otros dos métodos nuevos de una sola llamada: la **sonda por slug del PDF de la
AES del ISCIII** (`report_aes_2027` da 404, el control de 2026 da 200), que
convierte en Tier 1 un negativo que antes sólo se apoyaba en Tier 2 para las
filas de Fit 5 de toda la base; y la **API de medios de `senc.es`**, que le pone
fecha a una fila que hasta ahora sólo podía probar existencia.

**W-0025 (Fundación Tatiana) se rebaja a LOW y con una mala noticia:** no se ha
localizado **ninguna edición 2026**, mientras las becas predoctorales de la
misma fundación sí tuvieron convocatoria. El programa de estancias puede estar
discontinuado desde 2025, y la vigilancia tiene que cambiar de supuesto: hay que
comprobar si existe, no sólo cuándo reabre. Correo para zanjarlo:
`becas.neurociencia@fundaciontatianapgb.org`.

**W-0014 (One Mind): segunda pasada que propone retirarla.** Inelegibilidad
estructural verificada (excluye postdocs, exige plaza de Assistant/Associate
Professor en EE.UU.), Fit 1. No la borro — la decisión es suya.

## Filas que ella ya hubiera leído y cuyos hechos han cambiado

**Ninguna.** `owner_status.json` sigue vacío (`{}`), así que no hay ninguna
marca suya y ningún modelo mental que se haya quedado obsoleto por debajo. El
`Owner_Status = NEW` de muchas filas es el valor por omisión, no una lectura.

## Lo que no se pudo verificar o alcanzar

- **`esrs.eu`: el bloqueo queda mejor caracterizado y hay que corregir el
  inventario.** No es un 403 contra una ruta: es un **desafío gestionado de
  Cloudflare en todo el dominio, incluida `/wp-json/`**. O sea que el truco de
  la API REST de WordPress —el método que más ha rendido en este repositorio—
  **no sirve con esta sociedad**. Lo que sí funciona es la búsqueda restringida
  al dominio.
- **`nihr.ac.uk`: bloqueo NUEVO**, HTTP 403, no estaba en el inventario. El alta
  del NIHR Postdoctoral Award (F-0086) queda en LIKELY con fuentes Tier 2.
- **`fundacionjlc.es`: bloqueo elevado a definitivo y de dominio completo.** Se
  probó por fin el endpoint pendiente `/wp-json/wp/v2/types` y otras cuatro
  rutas: las cinco HTTP 000 (*connection reset*). El corte no distingue HTML de
  API. **No volver a gastar en él.** Consecuencia incómoda: F-0037, F-0044 y
  sobre todo **F-0045 (Beca Post Residencia), que es de las más suyas de la
  base** porque su residencia acaba el 22-05-2027, siguen sin verificar.
  Rodeo que queda por probar: `seqc.es` / `semedlab`, la sociedad matriz.
- **`dfg.de`** ha roto la URL HTML del Walter Benjamin (404); sustituida por el
  PDF oficial del programa.
- **`atomgrants.com` no tiene ficha** de la ESRS Meetings and Courses
  Fellowship, lo que **corrige la descripción de SRC-0323**: no cubre las cuatro
  líneas de la ESRS, sólo la Short-Term. W-0013 se queda sin vía automática.
- **Dato de mantenimiento:** el rodeo documentado para `bga.org` lleva el
  `club_id` equivocado. El que funciona es **971921** en el host `bga.org`;
  `bga.clubexpress.com` con `club_id=325792` da 404. Afecta a SRC-0234,
  SRC-0334 y SRC-0370.
- **F-0082 (ASHG Trainee Award)** sigue tras el muro de socios. **F-0085**
  (fondo Guilleminault) y **F-0059** (IBRO Rising Stars) quedaron sin presupuesto.
- Las autonómicas F-0052, F-0053, F-0055, F-0056, F-0074, F-0076 y F-0080 no se
  tocaron: el encargo las marcaba «sólo si es barato» y el presupuesto se fue en
  el encargo prioritario, que lo merecía.

## Dos cosas que requieren una decisión suya, no una búsqueda

1. **Dos ramas pidieron forzar rodeos antibot y el clasificador de permisos de
   la sesión las bloqueó**: una petición con `--http1.1` a los dos slugs de la
   Fundación Tatiana (para descartar que seis pasadas de bloqueo sean sólo una
   negociación HTTP/2 fallida) y un `curl` con user-agent de navegador a
   `nihr.ac.uk`. **No las he ejecutado por ellas** — un subagente no puede
   autorizar lo que se le ha denegado. Si quiere que se intenten, hace falta que
   lo diga ella.
2. **La regla de tamaño sigue incumplida y empeorando**: `fellowships.tsv` está
   en **307 KB** (era 268 hace una semana), cinco veces el umbral de ~60 KB; y
   `changelog` 435 KB, `sources` 320 KB, `groups` 283 KB, `postdocs` 197 KB,
   `jobs` 107 KB, `events` 62 KB, `watchlist_closed` 59 KB. Es arrastre, no
   nuevo, y **el corte lo hace ella**: partir un fichero obliga a cambiar
   `build_page.py` y `build_xlsx.py` en el mismo commit, y eso no es trabajo
   para el final de una pasada desatendida.

## Conflictos que se reportan sin resolver

1. **HFSP**, dentro de su propia página, y ahora con un tercer elemento: el
   banner dice que el plazo de LOI de 2027 ya pasó, el cuerpo dice que el portal
   está abierto, y la nota al pie habla del «2026 award cycle».
2. **BBRF**: «the call has been closed» convive con un botón «APPLY NOW» en dos
   programas a la vez, más un banner caduco de 2022.
3. **ESRS Short-Term (W-0029)**: nuestra extrapolación da cierre ~31-01-2027;
   AtomGrants anticipa «March 2027». Las dos son previsiones; franja ensanchada.
4. **«Línea 2» de la Junta de Andalucía**: dos órdenes distintas usan el mismo
   nombre para cosas distintas (contratación de doctores vs. proyectos). No es
   conflicto de fechas sino de identificación, y es una trampa real.
5. **F-0073 (Plan GenT2)**: el plazo 2026-10-27 que traía la fila **no aparece
   en ninguna de las cuatro modalidades de 2026**. Se cierra por fecha pasada y
   queda señalado.
6. **BBRF, ambigüedad real:** «M.D. with minimum PGY-IV training» no dice si
   basta *estar en* el PGY-IV o haberlo completado. Con su residencia acabando
   el 22-05-2027, eso decide si el ciclo de febrero de 2027 le sirve. Sólo lo
   resuelve un correo a `grants@bbrfoundation.org`.

## El dato que sólo ella puede dar

**Su año de nacimiento.** Hoy bloquea al menos tres filas: el tope de 35 años
del ECNP Excellence Award (F-0090, por eso va Fit 3 y no 4), el «menos de 35»
de las bolsas de viaje de la AEGH (F-0043) y cualquier premio de joven
investigadora con límite de edad. Es la pregunta de mejor relación
coste-beneficio de todo el radar.

Sigue pendiente, por octava semana, **los meses exactos de las estancias en
QIMR Berghofer y en Japón**: sin ellos, MSCA y EMBO no pasan de LIKELY en
movilidad.

## Acciones de coste casi cero que siguen esperándola

1. **Socia de la SENC antes del 01-12-2026** (desbloquea F-0019, ver arriba).
2. **Socia de la ESHG con validez 2027** — requisito para *cobrar* F-0023.
3. **Alta en la AEGH**: el reloj de dos años de antigüedad es lo que hoy la deja
   fuera de F-0064 (confirmado verbatim), y sólo corre si se da de alta. La
   misma membresía desbloquea F-0041, F-0042 y F-0043.
4. **Cuatro correos**: `fellows@mrc.ukri.org` (F-0084, el de más valor),
   `grants@bbrfoundation.org` (PGY-IV), `becas.neurociencia@fundaciontatianapgb.org`
   (¿existe edición 2027?) y `secretaria.tecnica@ses.org.es` (antigüedad, F-0046).

## Suscripciones pendientes

**43 de 43 en TODO** (`owner_status.json` vacío, así que pendiente = todo lo que
el TSV marca TODO). Cuatro altas esta semana: **SUB-0040 (avisos de HFSP,
prioridad ALTA**, porque el ciclo AY2028 resulta ser su primera convocatoria
elegible), SUB-0041 (BBRF), **SUB-0042 (newsletter de la ESRS, prioridad ALTA**,
única vía fiable de enterarse de la apertura del 1 de diciembre con el dominio
tras Cloudflare) y SUB-0043 (AtomGrants). Sigue pendiente SUB-0036 (alta en la
ESRS), que es la puerta de F-0026/F-0081.

## Qué perseguiría la semana que viene

1. **La SES con el tripwire nuevo**, que cuesta una llamada, y **la apertura
   real de la ESRS el 1 de diciembre**: son las dos fechas más cercanas.
2. **`seqc.es` / `semedlab`** como espejo de la Fundación José Luis Castaño: el
   único rodeo que queda para F-0045 y los dos tickets del watchlist.
3. **`/news/agenda-and-deadlines/` de la ECNP** para fechar el congreso de 2027
   y cerrar F-0090, más su Rising Star Award y su Early Career Workshop, que
   aparecen en el menú y no tienen ficha.
4. **Qué servicios de *peer review* independiente acepta EMBO**: es la palanca
   que convertiría F-0008 de inelegible en presentable.
5. **F-0085 (fondo Guilleminault) y F-0059 (IBRO Rising Stars)**, que se
   quedaron sin presupuesto, y el texto completo de Ramón y Cajal por la BDNS.
