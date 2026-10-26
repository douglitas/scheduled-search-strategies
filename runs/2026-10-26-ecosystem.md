# Pasada ecosystem — 2026-10-26

Rutina: ecosystem (grupos, eventos, formación). Última rutina de la mañana.

**Obligaciones de respaldo, cumplidas sin trabajo pendiente ajeno:**
`data/inbox_triage.tsv` cierra la semana con **0 filas PENDING** (las cinco
filas existentes ya estaban DONE, todas ruteadas IGNORE por positions) y
`data/source_inbox.json` está **vacío** (`[]`). No se leyó Gmail en esta
pasada: el buzón lo lee positions una vez por semana, y así está escrito.

## Cifras, tomadas de `git diff HEAD~1 --stat`, no de memoria

| Pestaña | Altas | Actualizadas |
|---|---|---|
| groups | 14 (L-0068 … L-0081) | 10 |
| events | 2 (E-0032, E-0033) | 12 |
| training | 5 (T-0027 … T-0031) | 10 |
| sources | 13 (SRC-0364 … SRC-0376) | — |
| subscriptions | 0 | — |
| changelog | 66 apuntes | — |

`action_now`: 41 filas mías (antes 38), 3 filas ajenas preservadas intactas.
Total: **21 altas y 32 filas actualizadas**. 173 inserciones, 70 supresiones.
Cuadra sin pérdida: las 70 supresiones son las 32 filas modificadas más las
38 filas propias que `action_now` reescribe al renumerar el Rank. Ninguna fila
se ha perdido (events 14/12, groups 24/10, training 15/10).

## Las tres cosas que merecen acción, y por qué

**1. E-0029 cierra PASADO MAÑANA, el 2026-10-28, y sigue abierto.** *Advances
in Sleep and Circadian Science 2027* (Sleep Research Society, Austin, 19-22
feb 2027). Verificado hoy en `sleepresearchsociety.org`: el plazo de resúmenes
de póster **no se ha prorrogado**. Las ayudas de viaje para *trainees* se piden
marcando una casilla en el propio formulario de envío, y exigen ser primera
firmante de un póster aceptado: ella cumple por dos vías a la vez, residente
médica hasta mayo de 2027 y doctoranda. Si no llega, hay red: el plazo de
*late-breaking* abre en noviembre y cierra el **2026-12-13**.
**Aviso honesto, otra vez: es Fit 3, así que la regla de selección NO lo mete
en `action_now`** (Fit 3 sólo entra con competencia LOW). Lo dejo fuera a
propósito en lugar de inflarle el Fit para que aparezca.

**2. T-0007 Advanced Mendelian Randomization (Bristol), 16 días, y ahora con
la tarifa real.** Plazo 2026-11-11, curso online 25-27 nov 2026. **630 GBP
(~725 EUR), verificado**, y el `Funding_Available = No` ya no es un supuesto
sino un hecho: se leyó la página de *voucher packs* de Bristol y no encaja en
ninguna categoría (no es de la Universidad de Bristol, no es de salud pública
del suroeste inglés, no trabaja para una fundación médica británica, y el
descuento LMIC se corta en renta media-alta — España es renta alta). Lo paga
entero. **Pero antes de pagar hay un condicionante nuevo que cambia la
decisión:** el curso avanzado **exige** haber hecho el curso básico de MR y
tener experiencia previa de análisis MR, y Bristol **recomienda no hacer los
dos en el mismo curso académico**. Es decir, esto es probablemente un
**o lo uno o lo otro** con T-0003 (MR básico, 15-19 marzo 2027). Mi lectura:
T-0003 primero es el orden correcto, no T-0007 ahora.

**3. Dos grupos Fit 5 nuevos, y uno de los dos es el mejor correo en frío de
la base.** **L-0068 Loic Yengo** (Statistical Genomics Lab, IMB, University of
Queensland) — su línea 1 exactamente, VERIFICADO: la *Snow Medical Fellowship*
lo financia **hasta 2030**, su perfil institucional dice literalmente que está
disponible para supervisar, y el correo está publicado. Su MD y la medicina de
laboratorio son un diferencial real para el brazo de predicción de riesgo
clínico del grupo; el enfoque debe pedir ese asiento aplicado y no el de
métodos nucleares, porque su Python es asistido por IA. Necesita visado.
**L-0069 Emily Olfson** (Yale Child Study Center) es el espejo más exacto que
ha aparecido en nueve semanas: MD-PhD cuyo doctorado fue en genética humana y
estadística, laboratorio joven de neurogenómica psiquiátrica infantil, y
presidenta del programa *Early Career* de la ISPG — es decir, puerta de entrada
a la ISPG además de grupo. Confianza LIKELY, no VERIFIED: queda abrir su
página Tier 1.

**Nota que no es de mi beat pero encabeza `action_now` y cierra hoy:** J-0003,
la audiencia pública de los dos proyectos de real decreto de la vía
extraordinaria a los títulos de especialista en Genética Médica y Genética de
Laboratorio, tiene plazo **2026-10-26 — hoy**. Es de la rutina positions y no
la he tocado; la señalo porque es Fit 5 y el reloj más corto que existe.

## Lo que se cierra o se queda sin hueco

- **E-0025 Complex Trait Community (23ª)**: el plazo de resúmenes cerró el
  2026-08-14; la reunión se celebra el 8-12 nov 2026 en Portland (Maine).
- **T-0010 Tartu**: no hay edición 2027 anunciada. Se ha sustituido la
  conjetura por la ventana real de 2026 (solicitudes 20 marzo-20 abril,
  *early-bird* −10 % del 20 al 26 de marzo), de modo que la comprobación de
  marzo de 2027 ya tiene fecha.
- Ninguna fila de formación que estuviera abierta se ha cerrado esta semana.

## Exclusiones nuevas que conviene saber antes de hacer planes

- **T-0024 SISG: queda excluida de sus becas.** Las ~120 ayudas NSF/Regeneron
  están restringidas a estudiantes de posgrado **radicados en EE.UU.** Es el
  mismo patrón que la beca ISCEP de Boulder (T-0001), que ya la excluía por
  nacionalidad. Las dos escuelas que mejor le encajan son, para ella,
  autofinanciadas. El calendario 2027 no está publicado; la plantilla de 2026
  (solicitudes abren el 12 de enero, becas cierran el 6 de marzo, todo cierra
  el 20 de mayo, instituto 1-12 de junio en Atlanta, sólo presencial) da una
  fecha firme de comprobación en enero.

## Lo que no se pudo verificar ni alcanzar

- **El plazo del Boulder Workshop 2027 (T-0001) sigue sin anunciarse, y ya va
  tarde.** La página `/ibg/workshop-2027` ya tiene fechas confirmadas (1-5 de
  marzo de 2027, presencial) y la lista completa del tema trienal de genética
  latente —modelos multivariantes de gemelos, OpenMx, GREML, genomic SEM,
  modelos de desarrollo y de dirección de causalidad, PRS, MR—, pero **ni
  fecha de registro, ni plazo, ni tarifa**. El precedente dice que esto ya
  debería haber salido: el registro de 2024 abrió el 23-10-2023 y el de 2025 el
  16-10-2024 a mediodía GMT, con plazo de ayuda económica el 30-11-2024.
  Tarifa histórica sólo para calibrar: 850 USD académico en 2025.
  **El hallazgo útil: `…/workshop-2027/workshop-2027-announcement` da 404
  porque esa página todavía no existe, y su aparición ES la señal.** Hay que
  sondear las dos URLs cada semana.
- **La caza de satélites de ESHG 2027 y ASHG 2027 —el objetivo prioritario de
  esta semana— es un callejón sin salida en esta fecha, y conviene retirarlo
  de la lista hasta mediados de 2027.** ESHG 2027 sólo tiene cuatro *cursos*
  preconferencia (eso es formación, no eventos, y ninguno de PRS) y sus
  «satellite meetings» son sesiones corporativas que la ESHG declara
  expresamente no respaldar. El programa auxiliar de ASHG 2027 no está en
  línea en absoluto (en 2025 las solicitudes auxiliares cerraron el 16 de
  junio), así que hay que mirar entre junio y septiembre de 2027.
  **Pero el resultado es mejor que el objetivo:** el contenido de PRS está en
  el **programa principal** de ESHG 2027 —S09 «Polygenic Scores: Are We There
  Yet for Clinical Implementation?» (domingo 13 de junio) y S17 de genética
  avanzada de tiempo-hasta-evento—, cubierto por la inscripción normal de
  *trainee*. Y la inscripción tiene truco aritmético: *trainee* 270 EUR socia
  frente a 395 EUR no socia si se registra antes del 2027-04-15, con una
  membresía ESHG de 50 EUR, o sea **125 EUR de ahorro neto**. La ESHG no tiene
  ayuda de viaje propia.
- **E-0022 WCPG 2027 confirmado (9-13 nov 2027, Brisbane) pero sin plazo de
  resúmenes publicado.** Las ediciones anteriores cerraron en junio, así que
  hay que sondear mensualmente desde febrero de 2027.
- **E-0016 EMGM: ángulo nuevo gastado y recomendación de parar.** Buscando la
  54ª en vez de «2027» se averigua que la 54ª fue el 14-15 de abril de 2026 en
  Davos, bajo Cardio-CARE, y que **no hay anfitrión anunciado para la 55ª**.
  EMGM no tiene sede web permanente. Propuesta: una última mirada en enero de
  2027 y, si no hay nada, dejar de gastar presupuesto en ella.
- **T-0022 (plazo 2026-11-16) y T-0006 no se comprobaron** y se dejaron sin
  tocar. Ojo: **ninguno de los dos aparece en el catálogo 2026/27 de Bristol**,
  así que hay que confirmar quién los imparte realmente antes del 16 de
  noviembre, o ese reloj vence sobre una ficha cuyo proveedor no está claro.
- **Bristol no publica precio por curso** («individually priced»): seis fichas
  siguen sin `Cost_EUR` y eso son siete aperturas de página individuales.
- **Cuatro fichas bloqueadas por correo que no puedo enviar**, y lo digo en
  vez de fingir que pregunté: `IBGworkshop@colorado.edu` (plazo y tarifa de
  Boulder), `bsweir@uw.edu` (SISG 2027), `smartbiomed_info@au.dk` (T-0012) e
  `info@cardio-care.ch` (T-0023).
- **Bloqueos NUEVOS, anotados para no volver a pagarlos**: `esrs.eu` 403 —por
  eso **E-0024 Sleep Europe 2028 se quedó sin comprobar** y T-0030 es LIKELY
  inferido del patrón bienal, no anunciado—; `tess.elixir-europe.org` 403;
  `cajal-training.org` 503; los comités de la ESRS 403; el consejo editorial
  de *Journal of Sleep Research* 403 (Wiley) y el de *Behavior Genetics* tras
  muro de autenticación de Springer por las dos rutas de URL; la página del
  PNGU del MGH redirige (301) a un aterrizaje genérico, por lo que la ficha de
  Smoller queda UNVERIFIED.
- **Hallazgos al contrario, que desbloquean cosas que llevaban semanas
  atascadas**: `bga.clubexpress.com/content.aspx` **sí** responde y es el host
  real detrás del `bga.org` que da 503 —rompió el bloqueo de la BGA tras tres
  pasadas fallidas—; `sleepresearchsociety.org` sustituye al `sleepmeeting.org`
  que sirve una cáscara JS vacía; el *slug* por año `ispg.net/wcpg-2027/`
  sustituye al `ispg.net/world-congress/` que da 404 —y explica de paso la
  contradicción de `wcpg-2026`: era texto correcto de 2027 en la página
  equivocada—; `ut.ee/en/academic-job-offers` es la URL correcta de Tartu y
  sustituye a dos 404; `werkenbij.amsterdamumc.org` es el host vivo de
  Amsterdam UMC; y la **búsqueda por PERSONA del UKRI Gateway to Research**
  resuelve lo que su búsqueda por proyecto no encuentra.
- **Rutina nueva que recomiendo adoptar como método estándar del ángulo (a)**:
  las *E-utilities* de PubMed (esearch + efetch) con conjunto de revistas y
  ventana de fechas exacta, por curl. Fue decisiva: la búsqueda web no ve los
  índices de las revistas (una consulta directa por «Nature Genetics October
  2026» no devolvió nada de 2026), mientras que dos llamadas a eutils
  devolvieron afiliaciones de autor senior y correos de correspondencia, y de
  ahí salieron **10 de las 14 fichas** de grupos.
- **No alcanzados en seguimiento de grupos**: L-0023 Børglum, L-0025 Duncan y
  L-0003 Speed. **L-0012 Peyrot sigue SIN COMPROBAR** (no «sin cambios»): la
  página de investigación de Amsterdam UMC sirve una plantilla sin rellenar
  (`{{ItemsCount}}`). **L-0006 KCL es un UNVERIFIED honesto**: el buscador de
  empleo dice IoPPN (4) pero ignora el parámetro `?q=` y esas cuatro no son
  inspeccionables. **L-0015 McIntosh**, sólo Tier 2: UNVERIFIED, no un negativo.
  **L-0018 Falck-Ytter** tuvo su primera comprobación Tier 1 (portal de
  Uppsala): negativo, pero sólo se vieron 10 de 92 ofertas.

## Conflictos

- **E-0004 BGA 2027: el conflicto SIGUE abierto, con un avance parcial.** Ahora
  sabemos que la ciudad es **Minneapolis (EE.UU.)** y que el *Student Travel
  Fund* para *predoctoral trainees* está confirmado, pero la BGA **sigue
  publicando sólo «junio de 2027»**. La fecha 2027-06-29 de la ficha no se ha
  sobrescrito y queda marcada como **no reservable**: no se puede comprar un
  vuelo contra ella.
- **Conflicto nuevo, menor y no reconciliable**: el editor jefe de *Behavior
  Genetics* parece ser **Valerie Knopik**, no Hewitt, pero la página
  autoritativa está tras muro de autenticación. No se ha escrito ninguna de las
  dos versiones como hecho.

## Filas cuyos hechos han cambiado y que ella puede haber leído ya

`owner_status.json` sigue vacío, así que **ninguna fila marcada por ella se ha
visto afectada** — no hay nada en IN_PROGRESS, APPLIED ni DISCARDED. Aun así,
cuatro fichas han cambiado de contenido de forma material y su modelo mental
puede haber quedado viejo:

- **L-0017 Huckins: refutado, no «sin evidencia».** No tiene ningún R01
  administrado en Yale con recorrido: su único premio de Yale con margen
  (R01ES033630, como co-PI con Brennand) **termina el 2026-11-30**, y su R01 en
  solitario en Yale terminó el 2024-11-30. Una línea de postdoc en Yale por esa
  vía no existe.
- **L-0053 Warrier: el dinero se acaba antes de que ella esté libre.** Un único
  premio vivo (tramo de R2D2-MH, Horizon Europe Guarantee, 270.114 GBP,
  ago 2022-**ago 2027**). No puede pagar una incorporación en febrero de 2028.
- **L-0007 Grotzinger: hay que bajar la expectativa que dejó la pasada
  anterior.** La semana pasada lo llamé «la mejor plaza no anunciada de la
  base». Leída su biografía en la MUN (Tier 1): no hay plaza **ni frase de
  reclutamiento**, y **la financiación canadiense no está evidenciada** —las
  bases de NSERC y CIHR son formularios POST, no consultables por URL, así que
  esa mitad queda abierta. Lo que sí mejora son los ganchos: el laboratorio ya
  tiene nombre («Psychiatric Genetics lab»), él es **profesorado nuclear del
  propio International Statistical Genetics Workshop** y **co-presidente del
  grupo Cross-Disorder del PGC**. Sigue siendo un correo en frío excelente;
  ya no es una plaza.
- **L-0009 Mägi y L-0013 Lehto: no persigas el anuncio de cGEM.** Los «dos
  postdocs» son un fósil de un anuncio de 2020. Con la URL correcta hay 13
  ofertas en Tartu, todas con plazo 02-11-2026 y **ninguna en el Instituto de
  Genómica**: negativo verificado.

## Suscripciones

**Cero altas, y es deliberado por segunda semana consecutiva.** Las cuatro
ramas buscaron canal nuevo y las cuatro prefirieron no proponer nada antes que
inventar una URL. El candidato más claro era la lista de avisos del taller del
IBG de Boulder, y resulta que **se da de alta enviando un correo vacío a un
listserv, no por formulario web**: no hay URL de alta que escribir. Una
suscripción con URL inventada es peor que no tenerla.

**Pendientes: 38.** `owner_status.json` está vacío, así que por definición toda
fila TODO del TSV sin marca suya cuenta como pendiente. Las de reloj más
apretado siguen siendo **SUB-0017** (cuenta de reservas de Bristol, la puerta
de T-0007 y T-0003), **SUB-0030** (alta en la ESHG — y ahora con número: 50 EUR
de membresía ahorran 125 EUR de inscripción si se registra antes del
2027-04-15) y **SUB-0036** (alta en la ESRS, que además es **requisito en el
momento de solicitar** la escuela de sueño T-0030, con solicitudes previstas
de marzo a abril, así que hay que estar dentro ANTES).

## Nota de mantenimiento — séptimo aviso, siguen siendo cuatro ficheros

`changelog.tsv` **398 KB**, `groups.tsv` **283 KB**, `sources.tsv` **281 KB** y
`events.tsv` **62 KB**: los cuatro por encima del umbral de 60 KB.
**El troceo lo hace una persona**, porque exige tocar `tools/build_page.py` y
`tools/build_xlsx.py` en el mismo commit, y eso no se hace sin vigilancia al
final de una pasada. Séptima semana señalado.

## Qué perseguiría la semana que viene con más presupuesto

1. **Sondeo semanal de Boulder (T-0001)**, las dos URLs, incluida la de
   anuncio que hoy da 404: su aparición es la señal y el registro va tarde.
2. **¿Tiene MoBa fenotipos de sueño infantil a escala genotipada?** Es la
   pregunta de mayor apalancamiento que ha quedado abierta: la respuesta
   recalificaría Bergen y varias opciones de cohorte europeas de una vez.
3. **Retomar CAJAL 2027** (hoy 503): es la vía realista a su carencia de
   neurociencia computacional y lleva estipendios.
4. **Las siete páginas de tarifas de Bristol**, y antes del 16 de noviembre
   confirmar quién imparte T-0006 y T-0022.
5. **Grotzinger en NSERC/CIHR** por formulario, el filtro IoPPN de KCL,
   SweCRIS para Falck-Ytter, Peyrot por `werkenbij.amsterdamumc.org`, y los
   tres no alcanzados (L-0023, L-0025, L-0003).
6. **Lo que hace Brisbane asequible**: el *Early Career Investigator Program*
   de la ISPG y la *Peter McGuffin Scholarship*, ninguno de los dos abierto
   todavía esta semana.
7. **Rodear los muros de los comités** sin volver a chocar con ellos: el
   artículo anual de agradecimiento a revisores de *Behavior Genetics* está
   indexado en PubMed y por tanto es alcanzable, y los programas del WCPG
   listan los comités de la ISPG **con institución**.
8. **Abrir las cuatro páginas Tier 1 de las fichas LIKELY/UNVERIFIED** de esta
   semana, empezando por L-0069 Olfson, que es Fit 5 con confianza LIKELY.
