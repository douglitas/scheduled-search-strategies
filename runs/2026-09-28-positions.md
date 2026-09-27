# positions — 2026-09-28

Cinco ramas, las cinco completadas. El buzón se leyó y el conector funcionó.
Nada roto, ninguna ALERTA.

## Los números, sacados del diff (`git diff HEAD~1`), no de mi memoria

| fichero | altas | modificadas |
|---|---|---|
| `data/postdocs.tsv` | 15 (P-0041 … P-0055) | 15 (9 re-verificadas + 6 cerradas por vencimiento) |
| `data/jobs.tsv` | 5 (J-0016 … J-0020) | 6 |
| `data/sources.tsv` | 14 (SRC-0188 … SRC-0201) | 26 sólo en `Last_Checked` |
| `data/subscriptions.tsv` | 2 (SUB-0020, SUB-0021) | 0 |
| `data/changelog.tsv` | 51 apuntes | 0 |

Total: 134 inserciones, 47 supresiones en 5 ficheros. **Esta semana sí ha
habido cosecha**, y por una vez está repartida entre altas (20) y
desatascos: se han cerrado tres de los cinco encargos que la pasada del
2026-09-21 dejó abiertos.

## Las tres cosas que merecen tu atención

**1. P-0050 — Boston University, Lindsay Farrer. Es la primera fila de toda la
base que abre tus dos candados a la vez.** Postdoc en epidemiología genética
del Alzheimer (GWAS y secuenciación de exoma/genoma sobre los consorcios ADGC
y ADSP, R, biobancos). Lo que la hace distinta de las otras 21 filas Fit 4:
acepta explícitamente candidatas *«in the process of completing a PhD»* y dice
por escrito que hay fechas de inicio posteriores disponibles y que la plaza
queda abierta hasta cubrirse. Es decir, **no choca con tus relojes**, que es lo
que ha tumbado a casi todo lo demás desde agosto. Está en una división de
genética dentro de una facultad de medicina, así que el MD cuenta como activo,
no como ruido. Candidatura por correo directo a farrer@bu.edu; el único
elemento no improvisable son **tres cartas de recomendación**. Confidence
LIKELY, no VERIFIED: se leyó el PDF íntegro con membrete de la BU School of
Medicine, pero nadie abrió una página en bumc.bu.edu y el anuncio lleva tres
meses publicado. **Lo primero que conviene hacer es confirmar que sigue viva.**

**2. P-0002 (Max Planck Nijmegen, Beate St Pourcain) ha dejado de ser «sin
plazo»: la revisión de candidaturas arranca el 08-10-2026, dentro de diez
días.** Dos ramas la tocaron desde ángulos distintos y sus hallazgos se han
fusionado a mano en una sola fila. La rama 3 abrió el portal umantis (Tier 1) y
confirmó la plaza viva, en línea desde el 12-08-2026, 3 años, 73.999-91.055
EUR/año, **inicio propuesto el 01-12-2026**. La rama 5 encontró en el tablón de
la ISPG (Tier 2) el dato que la ficha institucional no da: *«rolling review
beginning October 8, 2026»*. Esa fecha **no se ha confirmado en el dominio del
MPI**, así que `Confidence` sigue VERIFIED por la existencia de la plaza pero la
fecha del 08-10 está declarada como Tier 2 en `Source_Note`. La jugada no
cambia —escribirle sin candidatura formal, preguntando si el inicio admite
diferirse a mediados de 2027 o a 2028— pero **ahora tiene prisa**.

**3. P-0029 (UQ, Loic Yengo): el conflicto de plazo que arrastrábamos queda
resuelto, y no era una contradicción.** Leída la ficha R-68861 por la API de
Workday: el texto dice «applications close Monday 12 October 2026 at 11.00pm
AEST» y el `endDate` del JSON dice 2026-10-13 porque **son dos cosas
distintas** — el cierre de solicitudes es el 12-10 y el 13-10 es la retirada
del anuncio del portal. `Deadline` corregido a **2026-10-12**, Confidence
VERIFIED. Datos nuevos: A$106.293-113.659 (Nivel A) o A$119.462-141.545 (Nivel
B) más 17% de superannuation, hasta 2,5 años, y la plaza está pensada para
transitar a laboratorio propio en cinco años. Sigue en Fit 3 por el choque de
calendario, y el valor real de la fila sigue siendo el nombre de Yengo para
escribirle en 2027 con la estancia en QIMR Berghofer como gancho.

## Encargos de la semana pasada: tres cerrados, uno a medias, uno fallido

- **AcademicTransfer, RESUELTO.** El patrón que funciona es
  `academictransfer.com/en/jobs/?q=<término>` (200, HTML plano). `/en/search/` y
  `/en/jobs/search/` eran los 404 que arrastrábamos. Registrado como SRC-0191.
  Resultado real: nada relevante en Países Bajos esta semana.
- **Edinburgh, RESUELTO y con la causa raíz identificada.** A la API Oracle le
  faltaba **`expand=requisitionList`**: sin ese parámetro responde 200 con el
  `TotalJobsCount` correcto y la lista VACÍA, que es exactamente por qué el
  14-09 parecía que sólo había mejora genética vegetal de Easter Bush. Patrón
  bueno en SRC-0193. Veredicto con el patrón correcto: `psychiatr` = 0 hits, y
  los 8 de `genetics` son epigenética húmeda y cromosomas de mosca.
  **Edimburgo no tiene nada abierto de lo tuyo.**
- **IGES (SRC-0155), las 5 plazas fechadas una a una**, y una calibración de la
  fuente que vale más que las fechas: **su sección de plazas «actuales» no se
  limpia** (Leicester cerró el 12-04-2026 y sigue listada). IGES sirve para
  fechar y para sacar contactos, no para probar vigencia.
- **KCL IoPPN, a medias y con el encargo mal dimensionado por mi parte:**
  `term=IoPPN` da **11** plazas, no las ~15 que dije, y sólo 5 llevan la
  etiqueta. Rendimiento medido de los filtros, para no repetir lo que no sirve:
  `statistical genetics`=4, `genetics`=55, `sleep`=1, **`polygenic`=0**.
  Ninguna Fit 4-5. Lo mejor es un Fit 3 (P-0046, PDRA in Machine Learning for
  Mental Health, Dr Sarah Morgan, cierra 2026-10-18) y no puntúa más porque
  **sus dos requisitos esenciales son RM cerebral práctica y PyTorch**, justo
  los dos puntos que tu perfil marca como supervisados, no independientes.
- **CIBERSAM, FALLIDO por cuarta vez. Cuatro centros, cuatro paredes:** IMIM
  (403 tras dos redirecciones), **VHIR (200 pero SPA, HTML sin vacantes — y es
  la casa de Marta Ribasés, el objetivo más afín que tienes en España)**,
  ibis-sevilla.es (404, la ruta es otra), idival.org (503). Sigue siendo EL
  agujero de España y empieza a parecer que no se resuelve con un agente.

## Lo que ha cerrado

**Seis cierres por vencimiento de plazo**, hechos por aritmética sobre fechas ya
contrastadas y sin volver a abrir la ficha, así que en las seis `Last_Verified`
NO se ha tocado y queda dicho en `Source_Note`: P-0028 (KCL Bioinformatician),
P-0030 (Cardiff CONNECT), P-0031 (KCL, Youth Endowment Fund), P-0033 (Erasmus
MC), P-0038 (CNIO) y P-0039 (IiSGM).

**P-0017 (QIMR Berghofer) cerrada gratis**: ya no figura en el listado completo
de vacantes, que sólo tiene 6 hoy. Salió del mismo listado que se abrió para el
resto de la rama, sin gastar una llamada propia.

**P-0008 (Broad, McCarroll Lab) RECUPERADA**, y la sospecha de la semana pasada
era un artefacto: con paginación por `jobOffset` la plaza aparece viva en
`jobOffset=24`, ref. 22042. Vuelve a OPEN y a VERIFIED, con URL directa. Fue
acierto no darla por cerrada cuando no aparecía en la página 1.

## Lo que no pude verificar, sin disfrazarlo

- **P-0003 (Mount Sinai, Mullins) y P-0011 (Albert Einstein) siguen sin
  verificar, y ahora hay causa estructural: Nature Careers ha cambiado el
  formato de ficha.** Las URL guardadas devuelven HTTP 400 y su API responde 404
  «job not found» para los `sourceId` 754125 y 757285. Eso apunta a retirada de
  los dos anuncios, **pero no es prueba de cierre**, así que ninguna de las dos
  baja de estado y en ninguna se ha subido `Last_Verified`. El patrón que sí
  funciona queda registrado (SRC-0192): `?keywords=` (el `?q=` se ignora) y
  fichas por `/naturecareers/job/<id-numérico>/<slug>/`. Del Mullins Lab hay
  señal indirecta de que sigue contratando; su web da 403.
- **P-0020 (Amgen deCODE) no se intentó**, deliberadamente: los dos portales son
  JavaScript y ya está registrado. Queda como estaba, sin subir `Last_Verified`.
- **P-0037 (NIH) y P-0040 (IIS-FJD) se quedaron sin presupuesto** en la rama 3.
- **Australia queda cubierta y no era infrautilización, como creí:** Seek
  bloquea (403 incluso con UA de navegador; su API interna da 404), pero la API
  de Workday de UQ da la vuelta completa y hay **una sola** vacante con
  «genomics» en toda la universidad, la de Yengo que ya teníamos.
- **Dinamarca queda cerrada para un agente:** `job.jobnet.dk` redirige a
  `nemlog-in.mitid.dk` y exige MitID. Importa porque era el rodeo natural al 403
  de Aarhus, donde están iPSYCH, el NCRR y el QGG.
- **Noruega, corrección a SRC-0123:** la ruta PDF `/joblisting/pdf/<id>`
  responde 200 pero su texto **no es extraíble en este contenedor** (no hay
  poppler ni pypdf/pdfminer/fitz). Cero filas de Noruega esta semana.
- **Islandia a medias:** `starfatorg.is` es un Next.js cuyos listados se cargan
  por cliente y no están en `__NEXT_DATA__`. Pendiente su API GraphQL.
- **EURAXESS: probada una aproximación nueva, resultado mixto y honesto.** Con
  `sort[name]=created&sort[direction]=DESC` **el orden sí funciona** (la primera
  página son anuncios del 27-09-2026), pero **el filtro sigue roto**: 6.933
  resultados sin acotar, frente a 6.616 la semana pasada, y la primera página
  era íntegramente Delft y Ámsterdam (hidrógeno, radar, diques). A 10 por
  página, barrer 6.933 son cientos de llamadas. **Confirmo por segunda semana
  que SRC-0046 merece bajar a prioridad LOW**; `sources.tsv` es de sólo
  apéndice y no lo he reescrito. El parámetro de orden sólo vale como sonda
  puntual de «qué se publicó ayer».
- **Bloqueos nuevos registrados, para no volver a pagarlos:** seek.com.au (403),
  findapostdoc.com y academicpositions.com (403 de Cloudflare, aunque sus
  listados llegan por buscador), nature.com fichas por slug (400),
  labs.icahn.mssm.edu (403), boards-api.greenhouse.io con los tokens de
  Congenica, Color y 23andMe (404: no reintentar a ciegas), rfgi.es (200 pero el
  listado vive en un marco). **Y un falso bloqueo que conviene desmentir**: el
  PDF de Boston University no se lee por WebFetch, pero no es un sitio caído —
  se resuelve descomprimiendo el PDF en local, y así se sacó el texto completo.

## El carril español: tres CCAA nuevas y una espera que ya es el dato

**J-0003, la vía transitoria al título de Genética Médica y de Laboratorio,
sigue sin salir, y ya son quince meses.** Comprobado el listado de audiencia
pública de Sanidad el 27-09-2026: tres proyectos abiertos (fondo de cohesión,
cartera de servicios, preparados para lactantes) y **ninguno de Genética**. El
dato nuevo, y es malo: un artículo de abril de 2026 en el que la ministra habla
de audiencia «inminente» mientras la propia DG de Ordenación Profesional admite
que «es difícil que todo este engranaje esté listo para el examen de 2027», con
**tres meses más para las comisiones nacionales y seis para los programas
formativos DESPUÉS del BOE**. Tu riesgo aquí no sólo está intacto: está fechado.

**Tres comunidades nuevas en la base**: J-0016 Aragón (bolsa abierta y
permanente de FEA Análisis Clínicos/Bioquímica Clínica, Tier 1 verificado,
Fit 4), J-0017 Asturias (bolsa de FEA de Laboratorio Clínico creada por
resolución del SESPA de 02-12-2025 — **Fit 4 pero UNVERIFIED y sin
`Last_Verified`: la pista es sindical**) y J-0018 Navarra (concurso-oposición
2026, Resolución 1515E/2026, ya «en resolución» y **exigiendo el título al
cierre de plazo, así que esta edición te queda fuera**; Fit 3). Siguen faltando
Baleares, Canarias, Cantabria, Castilla-La Mancha, Extremadura y La Rioja.

**J-0010 (Sacyl) tiene novedad material**: la Gerencia Regional anuncia la
creación de la categoría única de Licenciado Especialista en Laboratorio
Clínico, que **unifica Bioquímica Clínica y Análisis Clínicos**, con ventana de
rezonificación cerrada el 09-09-2026 y efecto el 10-09-2026, y publica un
procedimiento específico de inscripción FIN MIR/EIR 2026 en la bolsa. No se
reabrió el análisis del art. 15 de la ORDEN SAN/713/2016, que ya estaba hecho.

**Una fuente nueva que es exactamente tu especialidad**: SRC-0201, la bolsa de
empleo de **SEMEDLAB** (Sociedad Española de Medicina de Laboratorio, la fusión
de las tres sociedades del ramo), con 10 plazas vivas de FEA en Análisis
Clínicos / Bioquímica Clínica por toda España. No estaba en `sources.tsv` en
ninguna forma: lo que había era la Fundación José Luis Castaño (SRC-0093), que
son becas, no empleo.

## `action_now` se queda otra vez sin una sola fila mía, y el hueco ha crecido

`tools/rebuild_action_now.py` ha preservado las 29 filas ajenas y ha aportado
**0 filas mías**. Lo he verificado a mano aplicando la regla fila a fila: el
único candidato que la regla selecciona es P-0001 (Fit 5 sin fecha) y está
CLOSED, así que el generador hace bien en excluirlo. **El cero es correcto.**

Pero el hueco estructural que señalé la semana pasada ya no es una hipótesis,
es un recuento: **tienes 22 filas con Fit 4-5 y ninguna entra**. Doce de ellas
están OPEN, ROLLING o PENDING **y sin fecha de cierre publicada** — P-0002,
P-0003, P-0020, **P-0050**, J-0002, J-0003, J-0007, J-0008, J-0010, J-0011,
J-0012, J-0016, J-0017, J-0019. Es decir: tus dos mejores carriles —las bolsas
permanentes del sistema público español y los postdocs de candidatura abierta—
son estructuralmente *rolling* y Fit 4, exactamente el hueco que la regla no
recoge, y **este lunes eso ha dejado fuera de la portada lo mejor de la semana
(P-0050, la única plaza que no choca con tus relojes)**.

Bajar el umbral de lo sin plazo de Fit 5 a Fit 4 lo arreglaría de golpe. **Lo
decides tú, no yo**: cambiar la regla toca los tres prompts y el generador, y no
es trabajo para hacer a ciegas al final de una pasada desatendida.

## El buzón: funcionó, y está más vacío que la semana pasada

Conector Gmail operativo. Etiqueta `Research` localizada por ID tras listar
etiquetas una sola vez: **0 mensajes, 0 hilos** según sus propios metadatos, así
que el pase A no gastó una llamada. **Pase B: 0 hilos** (la semana pasada dio 2).
Cero llamadas de etiquetado porque no había nada que etiquetar; ningún borrador,
nada enviado. `inbox_triage` no recibe ninguna fila y nada queda PENDING.
`data/source_inbox.json` está vacío: no tenías ninguna URL encargada.

El vacío es el hallazgo, por segunda semana: **a este buzón no llega ni una sola
alerta de empleo, beca o congreso, porque no hay nada suscrito** (SETUP.md paso
4). Mientras siga así, la captación por correo del sistema es literalmente cero
y esta rama quema dos llamadas semanales en un buzón vacío.

## Nada tuyo se ha quedado obsoleto

`owner_status.json` sigue vacío (`{}`): ninguna fila estaba marcada por ti, así
que **ninguna de las 15 modificaciones de hoy te ha cambiado el mapa bajo los
pies**.

## Suscripciones

Añadidas hoy, las dos con Status TODO, en el tope de 2 de la pasada:
**SUB-0020** (alerta por correo de búsqueda guardada de Platsbanken /
Arbetsförmedlingen, MEDIUM) y **SUB-0021** (avisos de nuevas vacantes de
Genomics England, HIGH — propuesta precisamente porque su portal sigue teniendo
una sola vacante irrelevante y vigilarlo a mano cada lunes no renta).

**Pendientes: las 21, todas TODO, ninguna dada de alta.** Por urgencia siguen
SUB-0001 (BOE, que es el aviso temprano de J-0003 y llevamos quince meses
esperándolo), SUB-0002 (EURAXESS) y SUB-0012 (jobs.ac.uk). **SUB-0009
(Fundación José Luis Castaño-SEQC) cerraba el 30-09-2026 y exigía ser socia al
solicitar: a dos días de hoy, si no está hecha, se pierde esta edición.**

## Aviso de tamaño

`data/postdocs.tsv` ha pasado de 80 a **117 KB** y `data/jobs.tsv` de 47 a
**61 KB**: ambos superan ya el umbral de ~60 KB de la regla de división, y son
míos, así que lo digo. También siguen por encima `fellowships.tsv` (186 KB),
`sources.tsv` (133 KB), `changelog.tsv` (133 KB) y `groups.tsv` (98 KB).
Dividir obliga a tocar `tools/build_page.py` y `tools/build_xlsx.py` en el mismo
commit: lo decides tú.

## Qué perseguiría la semana que viene

Confirmar P-0050 (Boston University) en bumc.bu.edu, que es lo único Fit 4 sin
choque de relojes que tenemos; confirmar en www.mpi.nl la fecha del 08-10 de
P-0002 antes de que pase; reconstruir P-0003 y P-0011 con el patrón
`?keywords=` que ya funciona, y barrer Nature Careers con `?keywords=polygenic`
y `sleep+genetics`, que no entraron por presupuesto; atacar CIBERSAM por vías
indirectas (VHIR vía InfoJobs/LinkedIn, la ruta real del IBiS desde su home);
recorrer las 10 fichas de SEMEDLAB para fijar una línea base con la que poder
detectar novedad; y sacar los tres contactos con correo institucional publicado
del Genetic Epidemiology Group de Leicester (Martin Tobin, Catherine John,
Richard Packer), que es la mejor vía de contacto en frío que ha aparecido en
toda la pasada.

Nota de decisión que te traslado en vez de resolver: **AEGH-empleo (SRC-0156)
tiene 20 ofertas con tu título exacto** (FEA Análisis Clínicos en el 12 de
Octubre, genetista de laboratorio en el ICS Girona, médico genetista en Parc
Taulí) **y ninguna publica fecha**. Sin fecha no hay novedad demostrable y no
estás libre hasta el 22-05-2027, así que no he registrado fila; pero conviene
que lo ojees tú.
