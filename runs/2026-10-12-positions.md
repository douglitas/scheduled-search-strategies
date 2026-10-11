# positions — 2026-10-12

Pasada semanal de posiciones (pestañas propias: `postdocs`, `jobs`).
Cinco ramas en paralelo, una por beat. Perfil completo: sin `PROFILE-INCOMPLETE`
ni `[TODO]`, así que la pasada investigó con normalidad. No existía informe de
hoy: no fue un re-disparo.

## Recuento, tomado de `git diff HEAD~1 --stat`

| fichero | cambio |
|---|---|
| `data/postdocs.tsv` | 5 altas (P-0067…P-0071), 27 filas actualizadas |
| `data/jobs.tsv` | 1 alta (J-0022), 4 filas actualizadas |
| `data/sources.tsv` | 14 fuentes nuevas (SRC-0267…SRC-0280) |
| `data/subscriptions.tsv` | 2 altas (SUB-0026, SUB-0027), las dos TODO |
| `data/inbox_triage.tsv` | 2 filas, las dos IGNORE / DONE |
| `data/changelog.tsv` | 37 apuntes (6 NEW + 31 UPDATED) |
| `data/action_now.tsv` | 1 fila mía (J-0003), 32 ajenas preservadas |

93 inserciones y 32 supresiones: las supresiones son exactamente los pares
`-/+` de las 31 filas modificadas y la de `action_now`. No se perdió ninguna
línea. `Owner_Status` quedó intacto en todas las filas preexistentes
(comprobado columna a columna contra `HEAD`), y las 6 filas nuevas nacen vacías.

## Las tres cosas que merecen acción

**1. J-0003 — alegaciones a los dos reales decretos de Genética, antes del
26-10-2026 (14 días). Fit 5, competencia LOW, esfuerzo S. Es la fila número 1
de `action_now` y la más valiosa de toda la base.**
Verificada en Tier 1 bajando y leyendo los dos PDF articulados del Ministerio,
no la prensa: el trámite de audiencia sigue abierto del 02-10-2026 al
26-10-2026 y el BOE no ha publicado todavía ninguno de los dos decretos (ni
cierre anticipado ni prórroga). Lo nuevo de esta semana, y cambia su
calendario de verdad: **la bisagra es la fecha de entrada en vigor frente al
22-05-2027.** Si el decreto entra en vigor antes de esa fecha, ella es
residente (apartado 4) y su ventana de 15 días naturales no se abre hasta que
acabe la primera promoción, hacia 2032-33. Si entra después, ya es
especialista y cae en el apartado 3.b.2º, con un mes de plazo desde la
convocatoria. **Un lustro de diferencia según una fecha que no controla**, y
es el argumento de fondo de la alegación al apartado 10.c.
Segunda consecuencia práctica: en las dos lecturas el cómputo exige el 50% del
tiempo transcurrido desde el título en ejercicio EXCLUSIVO en una U.78
autorizada, así que cada mes fuera de una U.78 a partir de mayo de 2027 le
diluye el porcentaje. Y la U.78 sólo computa en hospital (C.1.1, C.1.2) para
Genética Médica, mientras que para Genética de Laboratorio vale en cinco tipos
de centro: una U.78 hospitalaria acumula para los dos títulos.

**2. P-0002 — MPI Psycholinguistics (Nijmegen), Statistical Genomics /
Genetic Epidemiology. Fit 4, sin plazo.**
Confirmada VIVA en Tier 1: es la única de las cinco vacantes de
`mpi.nl/career-education/vacancies` que NO lleva el aviso «DEADLINE HAS
PASSED», y sigue sin fecha de cierre publicada. Es la plaza más accionable del
beat académico. Conviene escribir ya al grupo Language and Genetics. Dos
cautelas: el salario E13 (73.999–91.055 EUR/año) y el inicio propuesto
01-12-2026 vienen de la ISPG, una sola fuente Tier 2 que el dominio del MPI no
confirma; y ese inicio es inviable con su reloj (febrero de 2028) salvo que
acepten retrasar la incorporación — que es precisamente lo que hay que
preguntar en el primer correo.

**3. P-0043 — Human Technopole (Milán), grupo Casale, genética estadística.
Fit 3, cierra el 04-11-2026.**
Verificada con cuidado: las dos fechas del anuncio concuerdan y publica
salario hasta 43.000 EUR, que se añade a la fila. Es el encaje temático más
limpio que queda abierto en Europa. Next_Action: escribir a Casale ya.

## Qué se cerró

11 filas por plazo simplemente vencido (P-0019, P-0041, P-0042, P-0044,
P-0047, P-0048, P-0049, P-0056, P-0060, P-0064, P-0065), de las cuales las
ramas 2 y 3 reverificaron en Tier 1 todas menos P-0041 y P-0042, que quedan
LIKELY porque el endpoint de detalle de la API sueca
(`links.api.jobtechdev.se/ad/<id>`) devuelve ahora HTTP 500 — bloqueo nuevo; la
API de búsqueda (SRC-0188) sigue bien. P-0029 (UQ, R-68861) seguía viva el
11-10 y cerraba el 12-10 a las 23:00 AEST, o sea a las 15:00 de Madrid de hoy:
se marca CLOSED con la hora exacta en la fila. P-0004 (U. de Islandia, ERC
StressGene) se cierra por ausencia: su ficha de EURAXESS devuelve 307 al
buscador genérico, es decir retirada, y no hay reedición indexada.

Siguen abiertas y confirmadas: P-0045 (17-10), P-0046 (18-10), P-0036 (19-10),
P-0061 (21-10), P-0063 (23-10), P-0058 (29-10), P-0043 (04-11), P-0057 (21-11),
más P-0008 y P-0035 en el Broad y P-0062 en QIMR.

## Negativos verificados — esta semana hay poco, y es un hecho, no un hueco

En el beat académico **no apareció nada de Fit 4 ni 5**. Las tres altas de la
rama 2 (Cambridge DAMTP, Manchester, Dana-Farber) y la de la rama 5 (UiO-Ahus)
son Fit 2 y existen sólo para no redescubrirlas. Comprobado y vacío:
el portal Avature del Broad recorrido **entero** (26 anuncios, offsets 0-24; el
30 no existe) sin ningún postdoc de genética estadística o psiquiátrica abierto,
ni del Stanley Center ni de Neale, Karczewski, Daly o Robinson; VU Amsterdam
(12 vacantes, nada del Netherlands Twin Register); Edinburgh por su API Oracle
(tercera pasada seguida sin genética psiquiátrica); QIMR (4 vacantes, ninguna
de genética); las 154 vacantes vivas de Cambridge; cuatro tablones de sociedad
(IGES, ISPG, Sleep Research Society, AEGH) sin una sola plaza nueva de su línea.
Y en industria: ni un MSL de genómica o diagnóstico molecular abierto en España.
La única alta de `jobs` es la Talent Community de Genomics (ex Genomics plc), la
empresa cuyo producto son los PRS: Fit 3 y no más, porque hoy no hay ninguna
vacante abierta, sólo el formulario. Sube a 4-5 en cuanto publiquen un
statistical geneticist.

## Lo que no se pudo verificar ni alcanzar

- **P-0003 (Mount Sinai) y P-0011 (Einstein) siguen UNVERIFIED.**
  `careers.mountsinai.org` da 404 en `/search-jobs/` y 200 con cero resultados
  en `/jobs?keywords=` (lista renderizada por JavaScript); `einsteinmed.edu/careers`
  da 403 al primer y único intento. Las dos filas llevan «abrir a mano» en
  Next_Action, y el patrón de búsqueda correcto queda fichado como fuente.
- **El buscador de EURAXESS queda cerrado como inservible, y esto ahorra
  presupuesto todas las semanas.** Reproduciendo el formulario por POST aparece
  el parámetro real de texto libre (la faceta `f[0]=keywords:<término>`), pero
  **el servidor la ignora**: 12 variantes distintas devuelven las mismas 10
  ofertas y 178.113 bytes idénticos. No hay RSS ni API (5 endpoints, todos 404).
  Corrige la nota de SRC-0046, que daba por buenas las facetas. Consecuencia
  honesta: **no puedo afirmar que no hubiera plazas de genética estadística en
  EURAXESS esta semana, sólo que no son alcanzables por esa vía.** Trampa nueva
  documentada: una ficha caducada devuelve 307, no 404, y un lector de páginas
  entrega entonces 10 ofertas ajenas confundibles con el anuncio buscado.
  Regla: 307 = retirada, 200 = viva.
- **El buscador del Punto de Acceso General (SRC-0227) da HTTP 404 hoy**, con y
  sin parámetros, cuando el 2026-10-05 se leía bien. Sin esa puerta se cayó el
  encargo de cerrar de golpe Asturias, Extremadura, Cantabria, Baleares y
  Castilla-La Mancha. **J-0017** (bolsa del SESPA) y **J-0021** (listas
  supletorias del Servicio Canario) siguen PENDING, cada una con su camino
  oficial concreto en Next_Action (BOPA + astursalud; BOC categoría por
  categoría, que no tiene plazo único).
- **J-0012 (GSK) no se pudo resolver:** `jobs.gsk.com` es JavaScript puro y
  devuelve cero vacantes. Queda PENDING con el bloqueo registrado.
  `careers.astrazeneca.com` ignora el filtro `?k=` y su página 1 sólo tenía
  Statistical Science de nivel Director.
- P-0063 (Cardiff) no aparece en la página 1 de 2 del portal eploy y no hubo
  presupuesto para la 2. deCODE (P-0020, P-0066) no se reintentó: el portal
  50skills es JavaScript y el bloqueo ya estaba registrado. P-0050 (Boston
  University) y P-0051 (Columbia) se quedaron sin tocar. P-0052 (Bonn, vive en
  LinkedIn) sin verificar.
- Conflicto de fuentes que NO se vuelca a ningún dato: el plazo original de
  P-0004 aparece como 2020-09-21 en una fuente y 2020-09-28 en otra. Se reporta,
  no se elige.

## El buzón — leído, y el hallazgo que importa es negativo

Se leyó sin fallos. **Pasada A (`label:Research`) devolvió cero porque la
etiqueta sigue con 0 mensajes históricos.** Pasada B: 2 hilos en 8 días,
ninguno una oportunidad (uno entró sólo porque un cargo contenía «Research
Fellow»); los dos fichados IGNORE / DONE con el motivo, para que no se vuelvan
a mirar. No queda nada PENDING de mi beat, así que `ecosystem` no hereda
trabajo de aquí. El etiquetado no se ejercitó: no hubo ningún mensaje relevante
y etiquetar un aviso automático degradaría la etiqueta, pero el id correcto
queda anotado para la próxima lectora, así que el mecanismo no queda sin
resolver, sólo sin usar. `source_inbox.json` estaba vacío: nada que procesar.

**ALERTA SUAVE, no es un bug del pipeline: siete semanas de radar y ninguna de
las 27 suscripciones propuestas está activada.** Mientras no se active alguna,
la Parte A de la rama 5 seguirá viniendo vacía cada lunes: el cuello de botella
está en la activación, no en el descubrimiento. Las dos de mayor rendimiento
inmediato son **SUB-0002 y SUB-0018 (alertas de EURAXESS)**, porque son
exactamente lo que rodearía el buscador roto, y hoy se confirmó que
`/user/register` redirige a EU Login: son diez minutos de su tiempo.

## Suscripciones

27 pendientes (`owner_status.json` está vacío, así que todo TODO del TSV cuenta
como pendiente). Dos altas esta pasada, las dos TODO:
- **SUB-0027 (HIGH)** — avisos de la página de audiencia e información pública
  del Ministerio de Sanidad. Importa porque SUB-0001 (BOE) sólo avisa cuando el
  plazo de alegaciones ya ha muerto, que es justo el riesgo de J-0003.
- **SUB-0026 (MEDIUM)** — ISCB Career Center, la primera fuente de la base que
  fecha CADA anuncio.
Se dejó fuera a propósito una tercera candidata (alerta por correo de THEunijobs
para Australia) por el tope de 2 por pasada: queda para reproponer la semana que
viene, no se perdió.

## Fuentes nuevas

14. Las de más valor: el **canal RSS de Nature Careers**
(`/naturecareers/jobsrss/?keywords=…`), XML limpio con fecha y salario, que
sustituye un HTML que ya no se parsea; el dato de que **jobs.ac.uk responde 200
a curl con user-agent de navegador**, incluso en fichas cerradas, lo que lo
convierte en la verificación más barata del repo; la carpeta
`/normativa/audiencia/docs/` de sanidad.gob.es con los PDF articulados, **con el
truco reutilizable de que WebFetch no los digiere y `curl` + `pdftotext -layout`
sí**; y el ISCB Career Center. El resto son bloqueos fichados para no volver a
pagarlos (Mount Sinai, Einstein, astrazeneca, jobRxiv, IMS Epidemiology,
EURAXESS). De paso: las ofertas de la AEGH ya se pueden fechar en una llamada
con su API de WordPress (`search=oferta`), lo que cierra la limitación de
SRC-0156; y el MRC Epidemiology Unit se llama ya **IMS Epidemiology** y no
mantiene listado propio, así que buscarlo por su nombre antiguo da cero.

## Filas de la dueña cuyos hechos cambiaron bajo ella

Ninguna: `owner_status.json` está vacío y no hay filas marcadas READ,
IN_PROGRESS, APPLIED, RESOLVED, DISCARDED ni REVISIT. Todo lo tocado estaba en
NEW o sin marca.

## Regla de los 60 KB

`jobs.tsv` ha pasado a 66,4 KB y `postdocs.tsv` está en 137,0 KB (y los
compartidos `sources`, `changelog` muy por encima). No los parto yo, como manda
el contrato: partir un fichero obliga a cambiar `tools/build_page.py` y
`tools/build_xlsx.py` en el mismo commit y eso no es trabajo para el final de
una pasada desatendida. Queda dicho para que lo decida ella.

## Qué perseguiría la semana que viene con más presupuesto

Localizar la ruta viva del Punto de Acceso General o sustituirla por los
boletines autonómicos directos (BOPA, BOC, DOE, BOC Cantabria, BOIB, DOCM) y
cerrar las cinco CCAA de golpe; atacar industria por LinkedIn y por los tablones
de Greenhouse/Ashby/Workday en vez de por los buscadores corporativos, que son
todos JavaScript; vigilar el Consejo de Ministros para saber si el RD de
Genética entra en vigor antes o después de mayo de 2027, que es la bisagra de
J-0003; terminar el ISCB Career Center (página 2 y las claves «statistical
genetics» y «epidemiology»); la página 2 del eploy de Cardiff, P-0050 y P-0051;
Erasmus MC por AcademicTransfer, ya que su portal neerlandés no saca las
vacantes de investigación; las dos fichas del Department of Genetics de
Cambridge (PC51215, cierra 08-11, y PC51194, 21-10); y rotar el RSS de Nature
por los ángulos que hoy no se cubrieron.
