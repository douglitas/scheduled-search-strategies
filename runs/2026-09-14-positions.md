# 2026-09-14 — positions (postdocs + jobs)

ALERTA — **el buzón respondió y estaba vacío, y eso ya no es una casualidad:
ninguna de las 16 suscripciones está dada de alta.** El conector de Gmail
funcionó sin errores, la etiqueta `Research` existe y tiene cero mensajes, y la
consulta amplia de ocho días devolvió cero hilos. La rama 5 lleva tres pasadas
leyendo un buzón mudo por diseño. Mientras no des de alta al menos una alerta,
esta rutina sólo ve lo que alcanza a rastrear en 25 llamadas por rama.
**EURAXESS sigue muerto** (facetas que no filtran, 6.907 resultados sea cual
sea la consulta) y ahora `jobs.euraxess.org` además redirige al mismo listado
roto.

## Recuento (de `git diff HEAD~1 --stat`)

| Pestaña | Cambio | Detalle |
|---|---|---|
| postdocs | **+13 altas, 8 modificadas** | P-0023…P-0035; tocadas P-0002, 0003, 0006, 0011, 0014, 0018, 0020, 0022 |
| jobs | **+5 altas, 2 modificadas** | J-0010…J-0014; tocadas J-0001, J-0003 |
| sources | +14 altas, 24 `Last_Checked` | 122 → 136 |
| subscriptions | +2 | SUB-0015, SUB-0016 (tope de la pasada) |
| inbox_triage | 0 | el buzón no traía nada: cero mensajes, no cero relevantes |
| changelog | +28 | |
| **action_now** | **0 filas mías** | 22 ajenas preservadas byte a byte |

Sin colisión: no hay ningún commit de `positions` de hoy anterior al mío.

## Las tres cosas que sí merecen acción

1. **J-0010 — Sacyl (Castilla y León) tiene una puerta permanente, y puede
   tener un plazo de dos días.** La Bolsa Abierta y Permanente (BAPE) admite
   alta telemática continua con autobaremo y cortes anuales, y su categoría
   «Licenciados Especialistas» nombra literalmente Análisis Clínicos y
   Bioquímica Clínica: es de las poquísimas vías que seguirán abiertas en mayo
   de 2027. Fit 4, VERIFIED, esfuerzo XS. **El aviso que hay que resolver:** un
   PDF de Sacyl sugiere que la inscripción al terminar la residencia son **dos
   días hábiles desde el fin del MIR**. No está verificado — nadie abrió el PDF
   — pero si es cierto, la fecha es el 25-05-2027 y no «cuando te venga bien».
   Es lo primero de la semana que viene.
2. **Australia deja de ser un agujero: la muralla de UQ está rota.** Tras dos
   pasadas a cero, la API pública del portal Workday de la University of
   Queensland (`POST /wday/cxs/uq/uqcareers/jobs`) devuelve JSON completo y
   queda registrada como fuente. Con ella: **P-0029**, Postdoctoral/Research
   Fellow in Statistical Genomics del PCTG, **lab de Loic Yengo**, ref R-68861,
   abierta 11-09-2026, cierra 13-10-2026, AUD 106.294–141.545 + 17% de
   superannuation. VERIFIED de cabo a rabo. Es tu línea 1 literal y **no eres
   elegible** (exige doctorado concedido y desarrollo de métodos en C/C++), así
   que vale como plantilla de lo que te pedirán en 2028 y como gancho con
   nombre: Yengo, en Brisbane, el mismo ecosistema que QIMR Berghofer.
3. **J-0013 — el carril de comunicación científica deja de estar a cero, y el
   método es la noticia.** Ir al portal de vacantes de una agencia concreta
   (Oxford PharmaGenesis, motor eploy) dio 12 vacantes Tier 1 legibles: tres
   Medical Writer —una Oxford o remoto en Reino Unido—, Senior Medical Writer y
   Senior Medical Editor. Fit 3: te falta portafolio de agencia y, tras el
   Brexit, patrocinio de visado. Después de tres pasadas esperando anuncios en
   agregadores, el método de ir agencia por agencia funciona y se repetirá.

Detrás, dos que merecen mención: **J-0012 (GSK)** mantiene una familia entera
de plazas de tu técnica exacta (Statistical Geneticist Investigator y cuatro
más), UNVERIFIED porque sus fichas sólo devuelven el armazón del portal; y
**J-0011 (borsa del ICS catalán)**, permanente pero sin poder elegir categoría
de facultativo hasta tener el título cargado, con el requisito de catalán sin
verificar.

## J-0003 — la vía transitoria a Genética: sin movimiento, pero el expediente
## queda fechado y un conflicto se cierra

La audiencia pública de Sanidad tiene hoy dos proyectos vivos y ninguno es de
Genética. Dos hallazgos Tier 1 nuevos: (a) la nota de prensa 6697 del
Ministerio, de 13-06-2025, dice que lo aprobado fue la **creación** de las dos
especialidades, no un real decreto en el BOE — eso es exactamente lo que la
AEGH llamaba «aprobado», así que **el conflicto de la AEGH que quedó abierto el
2026-09-07 se explica y se cierra**; (b) existe el documento de **consulta
pública previa del RD de Genética de Laboratorio, de 01-07-2025**, el escalón
anterior a la audiencia pública. Es decir: 15 meses desde la consulta previa
sin borrador. Ningún texto oficial menciona todavía disposición transitoria, de
modo que la hipótesis de «acreditar años de ejercicio» sigue siendo hipótesis y
así queda escrito en la fila.

## Lo que se ha cerrado

- **P-0006 (Oxford, DSR614)**: cerró el 11-09-2026. VERIFIED.
- **J-0001 (Regeneron Genetics Center)**: su ficha r48469 da hoy 404 → CLOSED.
  La página de genetics-and-genomics sigue viva pero no enumera puestos: como
  fuente de vigilancia no sirve.
- **P-0023** (Oslo, Centre for Precision Psychiatry) y **P-0024** (Copenhague,
  CBMR/Kilpeläinen) nacen CLOSED: plazos vencidos. Se registran porque Oslo
  contrata de forma recurrente (cuatro anuncios distintos en 2025-2026) y es
  genética psiquiátrica pura.
- **P-0025 y P-0026 (las dos pistas de UQ de la rama 2) nacen CLOSED tras
  verificarlo yo misma.** Venían de agregador (scholarshipdb y LinkedIn) con
  Fit 4 y sin ficha oficial. La API de Workday de UQ devuelve **una sola**
  vacante de genética, la de Yengo, así que ninguna de las dos está hoy en el
  portal: o caducaron o nunca fueron vacantes publicadas. Se conservan como
  vías de contacto de grupo, no como plazas vivas, y su `Source_Note` lo dice.

## Conflictos: dos cerrados, dos que siguen abiertos

- **CERRADO — el texto de la AEGH**, arriba.
- **CERRADO A MEDIAS — P-0014 (Cardiff, Moondance).** **No** es la misma plaza
  que la ref 459 del Centre for Trials Research: aquélla es estadística y ésta
  es banco húmedo (microglía, tinción de cortes, edificio Hadyn Ellis),
  perfiles incompatibles. Además su texto coincide con un anuncio de Bright
  Network de 2024, así que la fila puede venir de un anuncio caduco. No he
  tocado su Status; sigue UNVERIFIED.
- **ABIERTO — P-0020 (deCODE/Amgen, Reikiavik).** `decode.com/careers` no lista
  ninguna plaza y su portal 50skills es JS puro, vacío por WebFetch y por curl.
  La discrepancia con el programa de postdocs de Amgen (que sólo lista Thousand
  Oaks, San Francisco, Burnaby y Copenhague) sigue sin resolverse.
- **ABIERTO — el plazo de dos días hábiles de Sacyl**, arriba.

## Lo que no pude verificar o alcanzar

- **Nature Careers ignora el parámetro `q=`** y devuelve el listado genérico
  reciente: **P-0003 y P-0011 no son verificables por ahí**, y quedan como
  estaban con `Last_Verified` de hoy y la nota del intento.
- **P-0019 (NIA/NIH)** no se tocó: la rama 2 agotó presupuesto en lo demás.
- **P-0022 (Alberta)**: el portal Oracle carga sólo la cabecera. Bloqueo
  permanente, un intento y fuera.
- **España se ha quedado sin cubrir en la rama institucional**: CNIO da 404 en
  la URL que teníamos, CIBERSAM 403 en todo el dominio e IMIM 403. Cero filas
  españolas por esa vía esta pasada; las cinco de España vienen de la rama 4.
- **J-0002 (SAS), J-0007 (FIMABIS) y J-0008 (SERGAS) no se reverificaron** por
  presupuesto. Son rodantes, así que no urge, pero tocan primero la semana que
  viene.
- ASHG Career Center devuelve **CAPTCHA** a las herramientas automáticas: queda
  registrada como fuente con Priority LOW y revisión manual.
- Bloqueos nuevos anotados para no volver a gastar presupuesto:
  `jobs.uq.edu.au` (no resuelve por DNS — usar la API de Workday),
  `jobbnorge.no` listados (404, las fichas individuales sí se leen),
  `employment.ku.dk?show=<id>`, Oracle CX de Edimburgo y 50skills de deCODE (JS
  puro), `kcl.ac.uk/jobs/<id>` sin slug (404), `cnio.es/.../job-offers` (404),
  Seek, FindAPostDoc y academicpositions (403), HigherEdJobs (vacío), el eploy
  de Cardiff (ignora `?keywords=`), fichas de `jobs.gsk.com` y careers de
  PharmaGenesis (sólo armazón; el portal eploy sí se lee),
  `job-boards.greenhouse.io/23andme` (404).

## Dos defectos corregidos, uno de código y uno de vocabulario

- **`tools/rebuild_action_now.py`**: una rama escribió en el `Deadline` de
  P-0002 «revisión continua a partir del 2026-10-08» y el selector leyó esa
  **fecha de apertura como fecha de cierre**, colando otra vez en action_now
  una plaza que exige el doctorado ya defendido — justo lo que el contrato
  manda mantener fuera. Es la segunda mitad de la lección del 2026-09-07,
  cuando el sucedáneo fue `Start_Date`. Corregido en su propio commit; el dato
  de P-0002 se ha movido a `Next_Action`, que es donde no miente.
- **Vocabulario**: la misma rama puso `Status = «abierta»` en P-0002 (era
  ROLLING) y cuatro filas nuevas traían el país en español o como «United
  States». Normalizado a OPEN/CLOSED/ROLLING/PENDING y a Spain / United Kingdom
  / USA, que es lo que usa el resto de la base. Mezclar formatos es lo que
  rompió los filtros del tracker hermano.

## Nada tuyo se ha quedado obsoleto

`owner_status.json` sigue vacío: ninguna fila estaba marcada por ti, así que
ninguna valoración tuya ha quedado atrás bajo tus pies. Las 10 filas
modificadas estaban todas en `Owner_Status = NEW`.

## Aviso de tamaño (no es mío, pero el contrato manda decirlo)

`data/fellowships.tsv` va por **161 KB** y `data/sources.tsv` por **78 KB**,
muy por encima del umbral de ~60 KB de la regla de división. Dividir un fichero
obliga a tocar `tools/build_page.py` y `tools/build_xlsx.py` en el mismo
commit, y eso no es trabajo para hacer a ciegas al final de una pasada: lo
decides tú.

## Suscripciones

Añadidas hoy (tope de 2): **SUB-0015** (alerta de empleo del portal Workday de
UQ, HIGH — es el canal del hallazgo de hoy) y **SUB-0016** (alerta por correo
de jobRxiv, HIGH — su buscador web no muestra fecha de publicación, que es
justo lo que inutilizó medio barrido de novedades).

Pendientes: **las 16, todas TODO**, ninguna dada de alta. Por orden de urgencia
siguen SUB-0002 (EURAXESS), SUB-0001 (BOE), SUB-0011 (EU Funding & Tenders) y
SUB-0012 (jobs.ac.uk).

En cola para las próximas pasadas, por orden: alerta de **THEunijobs** (Times
Higher Education, que hoy fue la fuente nueva que mejor funcionó en Australia),
alerta de búsqueda de **KCL**, **Nature Careers**, alertas de **QIMR
Berghofer** (RSS de TurboRecruit), **AcademicTransfer**, **Amgen Careers** y
**Talent Community del Broad**.

## Qué perseguiría la semana que viene

Abrir el PDF «Procedimiento inscripción FIN MIR» de Sacyl para confirmar o
descartar el plazo de dos días hábiles, que es el único hallazgo de hoy con
fecha propia; rematar España por la vía institucional, que se quedó sin cubrir
(URL viva del CNIO, CIBERSAM por centros individuales, IIS con unidad de
genética); leer a mano las fichas de GSK para subir J-0012 de UNVERIFIED; y
repetir el método de portal-de-agencia en dos MedComms más, una con sede
española.
