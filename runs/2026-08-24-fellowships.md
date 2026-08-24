# 2026-08-24 — fellowships (becas y movilidad financiada)

**Pasada de verificación, no de descubrimiento.** El guardarraíl de idempotencia
manda: la siembra de esta rutina se empujó hoy mismo a las 02:34 (commit
`639d748`, informe fechado 2026-08-23). Repetir las cinco ramas de descubrimiento
quince horas después habría producido ruido, así que esta pasada ha hecho
exactamente lo que aquel informe dejó por hacer: cerrar los conflictos abiertos,
verificar lo que quedó UNVERIFIED y repasar la watchlist. **Cero altas nuevas, y
eso es correcto.**

## Recuento (de `git diff HEAD~1 --stat`)

| Pestaña | Cambios |
|---|---|
| fellowships | 11 filas modificadas, 0 altas (36 → 36) |
| watchlist_closed | 10 de 14 filas actualizadas (14 → 14) |
| sources | +4 altas (82 → 86) y 18 `Last_Checked`/`Notes` |
| subscriptions | +2 (tope por pasada) |
| changelog | +12 |
| action_now | 1 fila mía, sin cambio de contenido |

## Las tres cosas que más cambian el mapa

**1. El conflicto de HFSP no existía, y la corrección le abre un buque insignia.**
La semana pasada quedó registrado que el PDF de bases decía «a PhD is required at
the time of application» contra la web. Extrayendo el texto del PDF en local, la
frase real es la contraria y es literal: *«A completed doctoral degree is not
required at the time of application»* (sec. 3.7, bases AY2027). **La cita
contradictoria la fabricó el resumidor automático de PDF**; no había dos fuentes
en desacuerdo, había una alucinación. Consecuencia práctica: HFSP sigue siendo un
ciclo alcanzable antes de defender, y su convocatoria es la AY2028. Regla
operativa nueva, y va en `sources`: **nunca aceptar una cita de un PDF vía
resumidor automático sin extracción local.**

Bonus del mismo PDF: en fase de LOI el requisito de publicación se satisface
**con un preprint**. Depositar uno de los dos manuscritos en revisión la vuelve
elegible sin depender del calendario de los revisores. Es la acción más barata y
de mayor rendimiento de toda la pasada.

**2. Wellcome no se puede traer a España.** Nunca se pudo: los centros de acogida
elegibles son Reino Unido, Irlanda y países de renta baja/media, y **desde el
29-10-2026 Irlanda también sale**. F-0012 deja de ser «una opción desde España» y
pasa a ser una decisión de traslado al Reino Unido. Mantiene Fit 4 porque el
contenido es exactamente ella y los hubs británicos de genética psiquiátrica son
su destino natural, pero conviene que lo sepa antes de invertir en ello. Efecto
lateral útil: los contactos de acogida que abra en 2027 conviene sesgarlos hacia
King's/SGDP, Cardiff o Edimburgo, porque sirven a la vez para HFSP, EMBO y esta.
Confirmado también el techo de 3 años posdoctorales, con la formación clínica
descontándose expresamente.

**3. Sara Borrell: basta el certificado, no hace falta el título.** Era la
pregunta que valía un año entero y está resuelta a su favor, con cita del art.
41.1.b de la AES 2026: *«Título de doctor **o** certificación emitida por las
universidades, con firma verificable, en la que figure indicación expresa de la
fecha de obtención del grado de doctor.»* Con una defensa en febrero de 2028
llega al cierre de la AES 2028 (~5 de marzo de 2028) con el certificado en la
mano. El margen es de semanas, así que la fecha de defensa deja de ser un detalle
académico: es una decisión estratégica que conviene hablar con el director en
2027.

## Lo demás que se ha cerrado

- **JSPS:** plazos FY2027 verificados (28-08-2026 y 23-04-2027) y **ninguno le
  sirve** — el segundo da incorporación entre septiembre y noviembre de 2027,
  antes de su defensa. Su convocatoria es la primera de FY2028, hacia agosto de
  2027. Dato que cambia la logística: **presenta el anfitrión japonés, no ella**,
  y las instituciones japonesas cierran internamente con más de un mes de
  antelación. Hay que avisar al contacto en la primera mitad de 2027.
- **EMBO:** confirmado palabra por palabra que el artículo de primera autora debe
  estar **aceptado o publicado al solicitar**, y que un preprint solo vale si
  lleva revisión pública independiente (tipo Review Commons), no un preprint a
  secas. Hoy es inelegible. Cierre verificado: 22-01-2027, 14:00 CET. Desde la
  ronda de otoño de 2027 se prohíben las resolicitudes.
- **Juan de la Cierva:** **la convocatoria 2026 no existe.** La última publicada
  es la de 2025 (BOE-B-2025-39640). Dos agregadores están ensuciando el radar:
  fibao.es reetiqueta la de 2025 como 2026, y tesify.es publica fechas de 2026
  sin ningún respaldo oficial. La fila pasa a apuntar al BOE.
- **L'Oréal-UNESCO España:** el contrato MIR **no** sirve. Las bases exigen
  contrato de investigación con el centro que presenta, más 4 años desde la
  lectura de la tesis y una estancia previa de 2 años seguidos (las suyas son de
  ~3 meses). No elegible hasta ~2032. Baja de Fit 3 a 2. Ojo: la «convocatoria
  2027» que circula por webs universitarias es el programa internacional de la
  UNESCO, por nominación de terceros, no el español.
- **ERC:** el cambio de ventana es real, no un error de lectura. 2-7 años rige en
  las convocatorias de 2026 y **0-10 años desde las de 2027**. Le amplía mucho la
  ventana futura: primera convocatoria posible, la de 2029, y conservaría
  elegibilidad hasta finales de la década de 2030.
- **Sklar (Broad):** cerrada definitivamente. *«In 2024, the Stanley Center
  awarded the last Sklar fellowship.»* Lo que queda exige ciudadanía o residencia
  estadounidense. Marcada CLOSED y fuera de la revisión semanal.
- **Premio Federico Olóriz (UGR):** admite **predoctorales matriculadas**, así
  que es elegible **ya**. 1.250 €, esfuerzo XS, competencia LOW; el único corte
  es tener un artículo publicado en la ventana de años, y sus dos manuscritos
  siguen en revisión.

## Watchlist: dos reaperturas

- **la Caixa Junior Leader Incoming 2027 está abierta**, cierra el 23-09-2026.
  **Ella no es elegible** (exige doctorado de 2 a 7 años antes del cierre); su
  primera edición posible es la convocatoria de 2029.
- **Becas de la SES: probablemente ya abiertas.** El tablón de la SES lista tres
  partidas de 2026 como «CONVOCATORIA ABIERTA». Si se confirma, la estimación de
  la semana pasada (apertura en noviembre-diciembre) era errónea. **No he podido
  confirmar la regla de antigüedad de un año como socia** — solo aparecía en un
  resumen de buscador, nunca en texto leído. Lo que sí está leído: las ediciones
  anteriores exigen que el proyecto lo lidere una socia y que el 60-70% del
  equipo lo sea.
- Fechas nuevas: **BBRF Young Investigator**, apertura en febrero y cierre el
  05-03-2027. **SLEEP 2027**, Denver, del 5-6 al 9 de junio de 2027 (verificado);
  el ciclo de premios de becarias sigue sin publicarse.
- Corrección de etiquetado en **NHMRC**: lo que llaman «ronda 2027» cerró el
  29-07-2026 y financia desde 2028; la siguiente cierra hacia julio de 2027 y la
  primera que ella podría usar es la de julio de 2028.
- Sin cambios: HFSP AY2028 (sin publicar), ISPG/WCPG 2027 (sin sede ni fechas),
  Río Hortega AES 2027 (nada publicado, ni BOE ni ISCIII).

## Lo que la dueña había leído y ha cambiado bajo sus pies

Ninguna fila tiene marca suya todavía (`owner_status.json` está vacío), así que
no hay nada que se le haya movido después de leerlo. Pero si ya se leyó el
informe de ayer, **tres cosas de aquel informe han quedado corregidas hoy**: el
conflicto de HFSP (no existía), la elegibilidad de Wellcome (España nunca valió)
y el estado de la JDC 2026 (no existe tal convocatoria).

## Verificación que faltaba y que hoy sí queda probada

El informe de ayer dejó constancia de que la **reconstrucción parcial de
`action_now`** no estaba probada, porque positions no había aportado filas y el
script informaba «ajenas preservadas 0». Hoy el mismo script informa **«mías 1 |
ajenas preservadas 10»**: el camino se ha ejecutado con conjunto no vacío y las
diez filas de las otras dos rutinas han salido intactas del diff. Queda probado.

## Bloqueos y trampas (para no volver a gastar presupuesto)

- `wellcome.org` **403** por segunda pasada consecutiva, también su página de
  plazos. Anotado en las Notas de SRC-0018. Espejo que funciona: CATCH
  (SRC-0083). Al usar espejos universitarios hay que anotar **siempre** si la
  fecha publicada es la del financiador o la interna del centro: es exactamente
  la ambigüedad entre el 10 y el 16 de noviembre de 2026.
- `aei.gob.es`: **cuatro URLs con 503** acumuladas, incluido el endpoint de PDF.
  A diferencia del ISCIII, aquí el truco del PDF **no** funciona. Dominio dado
  por inaccesible; sustituto Tier 1, el BOE (SRC-0086, con las dos consultas
  exactas ya escritas).
- `esrs.eu` **403**: no reintentado, según lo acordado. W-0013 sigue sin
  verificar.
- `sleepmeeting.org/call-for-abstracts/` y `infosubvenciones.es`: responden 200
  pero sirven una SPA vacía. Los PDF de bases de forwomeninscience.com son
  escaneados sin capa de texto.
- **Trampa técnica, no bloqueo:** varios PDF (HFSP, JSPS) devuelven 200 y el
  resumidor automático entrega texto plausible pero inventado. Es más peligroso
  que un 403 porque no falla, miente. En este entorno `pypdf`/`pdfminer` fallan
  al importar por un `cryptography` roto; se resuelve stubbeando
  `cryptography.hazmat.*` en `sys.modules` antes del import. **Merece
  convertirse en un helper de `tools/`** si el radar va a leer resoluciones en
  PDF cada semana.

## Suscripciones pendientes

Nuevas de esta pasada: **SUB-0007** (lista de avisos de la Sleep Research
Society, MEDIUM) y **SUB-0008** (alta como socia de la SES, HIGH — aquí la
membresía *es* requisito de sus propias becas, y si existe la antigüedad de un
año, cada mes que pasa retrasa un año la elegibilidad).

Siguen pendientes de antes, por orden de reloj: **SUB-0003** (socia de la SENC,
habilita el plazo del 15-10-2026), **SUB-0004** (avisos del ISCIII), **SUB-0005**
(ISPG) y **SUB-0006** (Boulder). En cola para próximas pasadas: boletín de la
ESRS (rodea su 403) y alertas de la AEI.

## Aviso de mantenimiento, que sigue vivo

`data/fellowships.tsv` va por **~108 KB**, casi el doble del umbral de división
de ~60 KB. Sigue sin partirse, y con razón: partirlo obliga a tocar
`build_page.py` y `build_xlsx.py` en el mismo commit y eso no se hace
desatendido. Es tarea de la dueña. Esta pasada no ha añadido filas, así que no ha
empeorado, pero cualquier pasada de descubrimiento sí lo hará.

## Qué perseguiría la semana que viene

1. **El PDF de bases de las Becas SES** desde el tablón: cierra el plazo real de
   la edición 2026 y la regla de antigüedad como socia. Es lo único con un reloj
   que podría estar corriendo ahora mismo.
2. **W-0003, W-0004, W-0013 y W-0014**, las cuatro filas de la watchlist que no
   dieron tiempo (Sara Borrell y Miguel Servet como ediciones, ESRS y One Mind).
3. **La fecha de fin del plazo de alegaciones de la AES**, que es el dato que
   decide si el 22-05-2027 cae dentro para Río Hortega 2027.
4. **El PDF de guidelines de EMBO** (junio 2026), para la regla de plazo máximo
   de incorporación y la fecha de la ronda de otoño de 2027.
5. Si la AEI publica la **JDC 2026** a finales de octubre, cazarla en el BOE el
   mismo día.
