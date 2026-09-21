# ecosystem — 2026-09-21

Pasada completa, las cuatro ramas en el techo o cerca (25, 25, 25 y 26 llamadas).
El ángulo de rotación de esta semana fueron **(c) las concesiones de financiación
frescas y (d) las juntas de las sociedades**, y ha sido con diferencia el más
rentable hasta ahora: las páginas de junta directiva de ISPG e IGES dieron unos
18 nombres de PI en dos llamadas, cinco de ellos sin fichar.

Tareas de backstop: **nada que hacer**. `data/source_inbox.json` está vacío (`[]`)
y `data/inbox_triage.tsv` no tiene ninguna fila PENDING. La semana cierra limpia.

## Recuento (de `git diff HEAD~1 --stat`, no de memoria)

| fichero | altas | modificadas |
|---|---|---|
| groups | +7 (L-0026…L-0032) | 8 (una a una) |
| events | +3 (E-0019…E-0021) | 9 |
| training | +4 (T-0014…T-0017) | 9 |
| sources | +19 (SRC-0169…SRC-0187) | — |
| subscriptions | +1 (SUB-0019) | — |
| changelog | +60 apuntes | — |
| **action_now** | **25 filas mías** (antes 22) | 4 ajenas preservadas |

145 inserciones y 48 borrados; los borrados son reescrituras de fila en sitio,
verificadas por `apply_rows` fila a fila (ningún fichero perdió filas: groups 25→32,
events 18→21, training 13→17).

## Lo que exige decisión esta semana

Tres relojes, y el primero se agota hoy:

1. **EPA 2027 (Florencia, 3-6 abr 2027): el plazo de abstracts cierra HOY,
   21-sep** (E-0019, Fit 4, VERIFIED). Es el único plazo vivo de toda la
   pasada y el único donde **el dinero va atado al plazo**: los travel grants
   de early career se piden marcando una casilla *dentro* de la propia sumisión
   del abstract, no después. Material ya lo tiene: los dos manuscritos en
   revisión. Florencia es vuelo corto desde Málaga y sin visado, y el congreso
   tiene 56 tópicos, entre ellos genética. **No hay late-breaking**: si no envía
   hoy, pierde la edición 2027 entera. El año pasado la EPA extendió el plazo
   tres días anunciándolo en X, pero la página oficial no promete nada.
2. **Bristol: la cuenta de reservas se crea desde pasado mañana, 23-sep**, y las
   reservas del programa 2026/27 abren el **7-oct a mediodía hora del RU**.
   Confirmado palabra por palabra en la página oficial. Sin cuenta creada antes
   no se puede reservar el día que abren, y el curso con el plazo más cercano es
   **T-0007, Advanced MR, 25-27 nov 2026, 725 EUR** (antes teníamos 737).
   Ninguno puede estar agotado todavía porque las reservas no han abierto.
   Reconfirmado también que **ningún voucher pack de Bristol le aplica**: las
   cinco categorías elegibles excluyen a España.
3. **L-0011, Max Planck Nijmegen: el correo tiene que salir antes del 8-oct**,
   cuando arranca la revisión rodante. Sigue siendo la **única plaza viva de toda
   la pestaña de grupos**, pero el desencaje temporal es severo y no ha cambiado:
   inicio 1-dic-2026 frente a disponibilidad mid-2027, defensa ETA feb-2028.
   El correo debe preguntar por rondas futuras, **no competir por esta plaza**.
   Contacto confirmado: beate.stpourcain@mpi.nl.

Detrás, la cosecha de grupos, con dos Fit 5:

- **L-0026, Shuyang Yao (Karolinska/MEB), proyecto CANARY** — la mejor ficha de la
  pasada y VERIFIED: **ERC Starting Grant 2026 de 1,5 M EUR a 5 años**, concedido
  este año. Sus líneas 1 y 2 exactas (esquizofrenia y rasgos complejos), el
  proyecto necesita quien corra GWAS/PRS humanos de forma autónoma —su zona— y
  **no** exige neuroimagen ni electrofisiología. Un PI con su primer ERC está
  montando equipo, no defendiéndose de veinte postdocs ya instalados. El correo
  debe *proponer una función*, no pedir una oportunidad.
- **L-0027, Hailiang Huang (ATGU/Broad)** — el laboratorio que describe
  literalmente su línea 1 aplicada a la 2, con tradición de acoger MD
  reconvertidos. Competencia ALTA y runway sin verificar, dicho sin adornos.
- Mención aparte a **L-0029, Elise Robinson (Broad)**: es el único sitio donde su
  línea 3 (sueño en los primeros tres años) se vende sola, como fenotipo de
  variabilidad del neurodesarrollo, que es justo la NDV Initiative.

## Correcciones sobre filas que la dueña ya había leído

- **L-0024, Streit: la adscripción que daba la tabla está desactualizada.** No
  está en el Departamento de Genetic Epidemiology in Psychiatry: su ficha viva
  —encontrada por fin tras los dos 404 de la semana pasada— lo sitúa en el
  **Hector Institute for AI in Psychiatry (HITKIP)** del ZI Mannheim, con el
  Personality Disorders Genomics Group. El email `fabian.streit@zi-mannheim.de`
  es **probable** (sale de la correspondencia de sus artículos), no verificado:
  confirmarlo antes de escribir.
- **L-0008: aviso de identidad.** `saxenalab.org` **no** es el laboratorio de
  Richa Saxena, es el de Shreya Saxena (Yale). El sitio correcto es
  `saxena.mgh.harvard.edu`. Escribir a la dirección equivocada era un error
  perfectamente posible con lo que la tabla tenía.
- **L-0005, Cardiff: la vacante que quedó pendiente ya cerró** (17-sep). Hoy no
  hay ninguna plaza de genética, genómica, bioinformática ni estadística en todo
  el portal. Lo único adyacente es un Research Assistant grado 5 del estudio
  CONNECT que cierra el 25-sep y no lleva perfil de genética estadística.
- **E-0017, GAW 2027: la convocatoria que perseguíamos ya venció** el 4-sep, hace
  17 días, y además era de *ideas*, no de abstracts. Lo aprovechable es la
  siguiente fase, la de participación, que se anunciará en geneticepi.org.
- **T-0012 (SMARTbiomed): las fechas de 2027 no se sostienen.** Venían de un solo
  extracto de buscador y no aparecen en la página, cuya última actualización es
  de agosto y solo detalla la edición 2025. El coste sí sube a VERIFIED (632 EUR).

## Cerrado, pasado o no confirmado

- **WCPG 2027 sigue sin anunciar**, y por segunda semana es un negativo
  verificado: `ispg.net/past-congresses` solo lista 2026 como próximo. La ficha
  de Clocate titulada «WCPG 2027» está vacía, sin fechas ni ciudad: es un
  marcador, no un anuncio. Suele anunciarse en la asamblea del congreso, del
  29-sep al 3-oct. **Revisión obligatoria el 5-oct.**
- **Cuotas del WCPG 2026: tercer intento fallido.** El portal carga por
  JavaScript. La única salida sigue siendo escribir a la ISPG.
- **T-0001 (Boulder): silencio.** La inscripción no ha abierto y no hay tarifa;
  los 550 EUR de la ficha siguen siendo estimación. Fechas sí confirmadas
  (1-5 mar 2027). Contacto para pedir aviso: IBGworkshop@colorado.edu.
- **T-0004 (Wellcome): negativo verificado.** Ningún curso de 2027 en el
  catálogo. Una revisión más en enero-2027 y, si sigue así, cerrar la fila.
- **ASHG 2026 e IGES 2026 quedan descartados para este año**: ya solo hay tramo
  late/onsite (396-710 EUR y 664-968 EUR respectivamente), sin abstract aceptado
  y con vuelo transatlántico. No hay opción virtual confirmable en ninguno.
- **ESHG 2027 es su congreso grande más alcanzable**: híbrido, en la UE, sin
  visado, abstracts hasta el 4-feb-2027 y sumisión abierta desde diciembre.
- Bloqueos confirmados o nuevos (todos anotados ya en `sources`): `esrs.eu` sigue
  en 403 y las cuotas de Sleep Europe no se obtienen ni por el PCO;
  `sleepmeeting.org` vacío por tercera semana (usar `aasm.org`); **nuevos**:
  `bga.org/about/executive-committee/` 403, `cardiff.ac.uk/jobs/vacancies` 403,
  `ut.ee/en/vacancies` 404 y `ut.ee/en/content/job-offers` 403,
  `ucl.ac.uk/brain-sciences/...` 403, `dougspeed.com` devuelve vacío.
- Correcciones de URL que ya están en la tabla: `mpi.nl/career/vacancies` → 404,
  usar `/career-education/vacancies`; `cardiffuniweb.eploy.net/vacancies/vacancies.aspx`
  → 404, usar la raíz; `ctg.cncr.nl/jobs` → 301; las URL de Bristol con
  `/study/short-courses/` redirigen; `colorado.edu/ibg/international-workshop` → 404,
  el patrón vivo es `workshop-AAAA`.
- **El PDF de resultados del ERC no es una fuente rentable** en formato
  «all-domains»: extraído por zlib, el texto sale fragmentado por kerning y los
  códigos de panel quedan desalineados respecto a los nombres. Cero coincidencias
  buscando polygenic, GWAS, biobank, heritability, psychiatric o mental health.
  La vía que sí funciona es la nota de prensa de la institución, y está fichada.
- No alcanzado por presupuesto: **L-0010 (Cormand)** sin intentar, **L-0003
  (Speed)** intentado una vez sin resultado, el email de **Tiemeier** (L-0004)
  sigue sin obtener —y no se inventa—, y **T-0006 (CSHL)** sin revisar.

## Suscripciones pendientes

Las **19 siguen en TODO**: `owner_status.json` está vacío, sin ninguna marca
suya, así que todas cuentan como pendientes (SUB-0001…SUB-0019).

De esta pasada se añade **una sola**, no dos: **SUB-0019, la alerta de empleo del
CNCR**, que es la pieza que faltaba para L-0001 (Fit 5, que nunca anuncia nada en
su propia página). Las otras candidatas —membresía de IGES, boletín de ESHG,
«notify me» de Wellcome, lista de correo de Bristol— **no se añaden porque
ninguna rama pudo verificar la URL de alta esta semana, y no se inventan**.

## Nota de mantenimiento

`data/groups.tsv` está ya en **86 KB** y `sources.tsv` en **105 KB**, ambos muy por
encima del umbral de 60 KB. Según la regla, el troceo lo hace una persona, porque
exige tocar `tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit.
Segunda semana señalado, y creciendo.

## Qué perseguiría con más presupuesto

1. Los **~15 nombres ya cribados y sin ficha** de las juntas de ISPG e IGES
   (Karmel Choi y Emily Olfson las más prometedoras; **Linda Kachuri**, Stanford,
   PRS multi-ancestria, la mejor del bloque IGES) y la página de *Officers* de la
   IGES, enlazada y sin abrir.
2. Las **páginas de vacantes de las siete fichas nuevas**: ninguna se abrió, de
   ahí que todos sus `Openings_Known` digan «no verificado». Empezar por Yao y
   Erhardt-Lehmann.
3. Las tres tareas cortas pendientes de grupos: **Cormand, Speed y el email de
   Tiemeier**.
4. **Los premios de viaje de IGES, BGA y ESHG**: históricamente existen para
   early career y ninguna rama pudo comprobarlos. Es la variable que decide si
   puede ir a algo, así que es el hueco más útil de rellenar.
5. Los **consejos editoriales** (ángulo d sin tocar), empezando por el del
   *Journal of Sleep Research*, que es el más valioso para su línea 3.
