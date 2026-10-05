# ecosystem — 2026-10-05

Pasada completa, las cuatro ramas en el techo o cerca (24, 24, 19 y 24 llamadas).
El ángulo de rotación de esta semana fue **(c) las convocatorias de 2026 con
dinero recién concedido**, estrenado, y ha dado cuatro de las ocho fichas
nuevas; el recorrido del PGC, que fue el ángulo de la semana pasada, aportó
tres más como apoyo y **no está agotado**. El hallazgo de método que conviene
no perder: **las listas de resultados del ERC no se pueden leer con WebFetch**
—devuelve el PDF en bruto y el resumidor lo rechaza—, pero `curl` +
`pdftotext -layout` + `grep` en una sola llamada de Bash convierte las 421
ayudas en un único coste. Y la lista que importa para ella es la de **Ciencias
Sociales (SH3, SH4, SH7)**, no la de Ciencias de la Vida: ahí viven la genética
del comportamiento y la sociogenómica.

Tareas de backstop: **nada que hacer**. `data/source_inbox.json` está vacío
(`[]`) y `data/inbox_triage.tsv` no tiene ninguna fila PENDING. Cuarta semana
que las rutinas anteriores las cierran limpias.

## Recuento (de `git diff HEAD~1 --stat`, no de memoria)

| fichero | altas | modificadas |
|---|---|---|
| groups | +8 (L-0040…L-0047) | 9 (8 con hechos nuevos, 1 re-verificada igual) |
| events | +2 (E-0024, E-0025) | 8 |
| training | +2 (T-0018, T-0019) | 10 |
| sources | +31 (SRC-0236…SRC-0266) | — |
| subscriptions | **0** | — |
| changelog | +39 apuntes | — |
| **action_now** | **30 filas mías** (antes 27) | 3 ajenas preservadas |

137 inserciones y 52 borrados; los borrados son reescrituras de fila en sitio,
verificadas una a una (groups 39→47, events 23→25, training 17→19, ninguna
perdida). Comprobado además, columna por columna contra `HEAD`, que **ninguna
`Owner_Status` cambió** en las tres pestañas.

## Lo que exige decisión esta semana

Tres relojes, y dos vencen el **miércoles 7 de octubre**:

1. **EPA 2027: el plazo de abstracts AGUANTA en el 7 de octubre y no habrá
   ronda late-breaking** (E-0019, Fit 4, VERIFIED hoy en
   `epa-congress.org/abstract-submission/`). No se ha vuelto a extender y no ha
   cerrado: quedan **dos días** y es la última oportunidad para la edición de
   Florencia. Dato nuevo de la misma página y es el que lo convierte en la
   acción de mayor retorno de toda la tabla: **la EPA concede sus propios
   travel grants y se piden DENTRO del mismo envío del abstract**, así que un
   solo trámite compra el póster y la financiación. El manuscrito de Nature
   Mental Health en revisión ya es material de e-póster: horas de trabajo, no
   días. Si la aceptan, hay que confirmar y matricularse antes del 1-feb-2027.
2. **Bristol abre reservas el 7 de octubre a mediodía (hora del Reino Unido)**
   para todo el programa 2026/27. **T-0007, Advanced Mendelian Randomization**,
   25-27 nov 2026, **630 GBP = los 725 EUR que ya teníamos** (el precio no se
   ha movido), plazo de reserva 11-nov. Corrección al briefing: **el registro
   previo de cuenta NO es un requisito duro**, solo muy recomendado, aunque sí
   hace falta cuenta para reservar en `brmsshortcourses.bristol.ac.uk`. Ojo al
   prerrequisito: el curso básico de MR o experiencia real equivalente.
3. **L-0011 (St Pourcain, MPI Nijmegen): el correo antes del 8-oct sigue en
   pie**, pasado mañana. Pero con un cambio de guion, abajo.

## Los dos hallazgos que cambian el mapa

- **Rosa Cheesman (L-0040, Universidad de Oslo, PROMENTA) es la mejor ficha de
  la pasada**: ERC Starting Grant 2026 «I-BELONG», **1,5 M EUR a cinco años**,
  o sea dinero vivo mucho después de la defensa de febrero de 2028. Hace PRS,
  interacción gen-ambiente y diseños intrafamiliares sobre los registros
  noruegos y MoBa: **línea 1 y línea 2 exactas y cero dependencia de
  neuroimagen o electrofisiología**, que es justo donde su expediente es
  supervisado y no independiente. EEE, sin permiso de trabajo. Correo
  verificado en su página de la UiO.
- **El hueco de formación en biobancos, señalado como carencia declarada y sin
  una sola fila desde agosto, ya tiene dos.** Todo `ukbiobank.ac.uk` responde
  403, así que la vía fue rodearlo: **T-0018, el hub de formación UKB-RAP de
  DNAnexus**, Tier 1, **gratuito**, online y autoadministrado, con siete
  módulos sobre gestión de proyectos y datos, Cohort Browser y extracción de
  fenotipos, construcción de herramientas y cómputo en nube (Fit 4, VERIFIED,
  **se puede empezar esta semana y no cuesta ni un día de permiso**). Detrás,
  T-0019, los cuatro cursos obligatorios de inducción de UK Biobank, en Fit 3
  porque no se puede matricular a título individual: exigen figurar en una
  solicitud ya aprobada.

## La cosecha de grupos (ángulo ERC 2026 + PGC)

Ocho fichas, dos Fit 5, ningún PI repetido de los 39 ya fichados:

- **L-0041, Na Cai (Basel Research Centre for Child Health)** — se mudó en
  febrero de 2025 de Helmholtz Múnich a Basilea como Assistant Professor de
  Computational Medical Genomics. Heterogeneidad y subtipos de depresión con
  mandato explícito sobre depresión infantil: **el único grupo de todo el mapa
  que toca sus tres líneas a la vez**, y Suiza es libre circulación.
- **L-0043, Ramina Sotoudeh (ERC StG BEFOREBIRTH)** es **la incógnita de mayor
  valor de la pasada**: el ERC registra como institución anfitriona el Centre
  d'Estudis Demogràfics de Barcelona, pero su perfil de Yale sigue sin
  mencionar ni España ni el ERC. Si el equipo analítico se sienta en Barcelona,
  **es la única opción fuerte encontrada que no exige mudarse**. Por eso la
  fila va LIKELY y no VERIFIED, y el primer correo debe preguntar dónde estará
  el equipo.
- **L-0044, Roseann Peterson: la deuda de la semana pasada queda cerrada.**
  Institución confirmada (SUNY Downstate, Brooklyn) y dirección de trabajo
  `Roseann.Peterson@downstate.edu`; el correo que publica el PGC está mal
  escrito en origen (`gmailcom`, sin punto) y hay que ignorarlo. Salvedad
  honesta: su único proyecto localizado, el R01MH125938, **se reporta
  terminando el 31-oct-2026 y es atribución Tier 2**, no leída en RePORTER, así
  que su margen para un inicio en 2027-2028 hay que preguntarlo, no suponerlo.
- Detrás, L-0042 (Rubinacci, Helsinki, ERC StG de métodos puros de genética
  estadística), L-0045 (Karmel Choi, MGH), L-0046 (Zeynep Yilmaz, Aarhus NCRR)
  y L-0047 (Wortinger, Oslo, en Fit 3 porque la dependencia de neuroimagen no
  se ha podido resolver).

## Correcciones sobre filas que la dueña ya había leído

1. **L-0011: el dinero no es de la Max Planck Society.** Esta ronda la financia
   el proyecto europeo **R2D2 (HORIZON-HLTH-21)**. Es lo que debe citar el
   correo: hablar de fondos Max Planck sonaría a estar leyendo un anuncio
   viejo. Queda además **probado el patrón de rondas sucesivas** —la de marzo
   (Nature Careers 12853299, cierre 5-abr, inicio 1-may-2026) figura ya como
   expirada—, así que la pregunta correcta sigue siendo por la ronda 2027-2028.
   Confianza LIKELY, no VERIFIED: `mpi.nl` dio 503 por cuarta vez y el texto se
   ha leído por dos extracciones de buscador independientes cruzadas con la
   ficha expirada de Nature Careers.
2. **L-0027 (Hailiang Huang): ya no hay que escribir al buzón genérico.** El
   correo nominal `hhuang@broadinstitute.org` está publicado en la página
   Opportunities del laboratorio, **junto con el paquete exacto** que piden: CV,
   una página de intereses de investigación y tres referencias.
3. **L-0036 (Joanna Martin): la vía del PMC NO funciona para ella**, y la ficha
   la daba por buena. Leídos cuatro de sus artículos de Cardiff, en ninguno es
   autora de correspondencia, y las direcciones de sus colegas demuestran que
   Cardiff no tiene patrón deducible. **Su dirección de Cardiff no se puede
   inferir y no se va a inventar.** Plan nuevo: escribir a
   `jmartin@broadinstitute.org`, que es la que ella misma publica vía el PGC, y
   preguntarle allí las tres cosas que faltan.
4. **L-0038 (Daniel Levey) sube de Fit 3 a Fit 4**: sí tiene laboratorio propio
   y dinero, aunque de premios de carrera (VA CDA2, NARSAD Young Investigator,
   MVP Early Career) y no de un R01, así que su capacidad de contratar es
   estrecha. La ficha preveía exactamente esta reevaluación.
5. **L-0033 (Niamh Mullins), matiz y no contradicción**: la plaza y el
   patrocinio de visado siguen literalmente en la página, con reubicación,
   guardería y alquiler subvencionado en Manhattan, **pero la página no lleva
   fecha y sus noticias más nuevas son de 2023**: es captación permanente, no
   una vacante con plazo. Conviene preguntarlo en el correo.
6. **T-0014 (SSGAC) baja de Fit 4 a Fit 2, y por elegibilidad, no por
   competencia**: no es un taller de varios días sino **una sesión online de
   una hora** el 15-oct, y la inscripción **exige acceso Controlled Tier al All
   of Us Researcher Workbench, que ella no tiene**. El plazo, además, es el
   7-oct. La serie es nueva y puede haber sesiones futuras sin esa puerta.
7. **Las siete URL de Bristol estaban muertas.** Bristol reestructuró su web y
   la ruta antigua hace 302 a un 404. Las siete filas llevan URL nueva y, de
   paso, fechas exactas verificadas en el índice: todos los plazos registrados
   cuadran con la regla de «dos semanas antes del inicio».

## Cerrado, pasado o no confirmado

- **Las becas de viaje del IGES son información caducada: negativo verificado.**
  Las Roger Williams y James V. Neel **no aparecen en ninguna parte del
  `geneticepi.org` actual**, que solo menciona apoyo sin nombre para
  estudiantes con dificultades, financiado con las cuotas. Los 1.000 USD de la
  página de 2019 no se sostienen hasta que el IGES lo confirme por correo.
  Compensación: la tabla completa de cuotas sí queda verificada (trainee no
  socia, tardía o en sede, 882 USD ≈ 810 EUR).
- **WCPG 2027 (Brisbane, 9-13 nov 2027): fechas re-confirmadas, y sigue sin
  haber plazo de abstracts, ni inscripción, ni ventana ni cuantía del ECIP.**
  Por las dos ediciones anteriores (6-jun-2024 y 5-jun-2025) la ventana del
  ECIP de 2027 debería caer a principios de junio: LIKELY, no verificado.
  `ispg.net/world-congress/` es un 404.
- **ESHG 2027**: la inscripción abre en **febrero de 2027**, el mismo mes que
  vence el abstract (4-feb), así que lo sensato es enviar en enero y marcar
  allí la casilla de la fellowship europea. La URL viva es `2027.eshg.org`;
  `www.eshg.org/conference/eshg-2027/` da 404.
- **SOBP 2027**: 6-8 may 2027 en Chicago, tema «The Metabolic Brain», y los
  abstracts **ya están abiertos**, pero el plazo vive detrás de un portal que
  solo renderiza con JavaScript. **SLEEP 2027**: 6-9 jun 2027 verificado,
  inscripción en enero, plazo de abstracts aún sin anunciar.
- **T-0001 (Boulder): cuarta semana sin movimiento**, sin fechas, sin
  inscripción y sin tarifa real, así que los 550 EUR siguen siendo estimación.
  Detalle nuevo: la página dice que el curso presencial de Boulder es
  **trienal, primera semana de marzo (2024, 2027, 2030)**, luego 2027 cae
  dentro de la residencia y costará días de permiso. Bajar a sondeo mensual y
  escribir a `IBGworkshop@colorado.edu`.
- **Negativos verificados que son resultado y no fracaso**: no hay edición 2027
  del Erasmus Summer Programme (la web sigue en agosto de 2026; las tarifas
  están en `nihes.com` por curso, y ESP43 de epidemiología genética figura a
  793 EUR); ningún curso práctico EMBO de genética estadística o cuantitativa
  para 2027; ninguna Sleep Science School de la ESRS para 2027 (patrón bienal
  2023/2025, así que 2027 es plausible pero no anunciado); ninguna edición 2027
  de Tartu (T-0010 sigue cerrado, ventana anual 20-mar a 20-abr, tarifa 2026 de
  750 EUR); tablón del ZI Mannheim el 2026-10-05, **26 vacantes vivas y
  ninguna del HITKIP ni de genética**; ficha de Havdahl en el FHI abierta hoy,
  **no publica correo, negativo firme**. La lista ERC StG 2026 de Ciencias de la
  Vida queda **agotada** (su único acierto psiquiátrico, Shuyang Yao, ya estaba
  fichado): no volver a leerla. NWO Vidi 2026 no publica resultados todavía.
- **Correos cerrados esta semana**: `hhuang@broadinstitute.org`,
  `daniel.levey@yale.edu` y `laura.portas@ocdem.ox.ac.uk` (vía de entrada al
  grupo de Doherty, L-0039, porque el artículo no da ninguna dirección de él).
  **Siguen sin cerrar, dicho sin adornos**: Streit (`fabian.streit@zi-mannheim.de`
  **PROBABLE** y no confirmable por web) y Lehto (`kelli.lehto@ut.ee`
  **PROBABLE**, ofuscado por Cloudflare; mitigación: copiar a
  `genoomika@ut.ee`).
- **Bloqueos nuevos, todos ya anotados en `sources`**: **todo el dominio
  `ukbiobank.ac.uk`** (403 en www y www2, varias rutas), no solo
  `community.*`; `payments.liv.ac.uk` 404; `ebi.ac.uk/training/live-events`
  carga vacío; `erasmussummerprogramme.nl/courses/` 404 (la ruta buena es
  `/summer-programme-courses`); `bga.org` 403 (BGA 2027 se queda UNVERIFIED;
  probar `bga.clubexpress.com` en navegador); `esrs.eu` 403; `sleepmeeting.org`
  cuerpo vacío; `ut.ee/en/vacancies` 404; `europepmc.org/article` 403;
  `pmc.ncbi.nlm.nih.gov` sirve reCAPTCHA; los PDF de `fhi.no/contentassets`
  exigen login de Microsoft; `mpi.nl` sigue en 503.
- **Los slugs del PGC del prompt están mal y dan 404.** Los reales (los 17,
  incluidos cinco grupos que el prompt no listaba: Anxiety, Copy Number
  Variations, Functional Genomics, Pedigree Sequencing y Suicide) quedan
  anotados en la fila de `sources` del índice. Y sin 502/503 esta vez: pedir
  una página a la vez funciona limpiamente.

## Dos fuentes nuevas que valen para todo el repo

- **La API REST de Europe PMC**, endpoint
  `/europepmc/webservices/rest/<PMCID>/fullTextXML`, **sustituye al atajo de
  «abrir la versión de PMC»** en todas las filas con instituciones en 403
  (Cardiff, Oxford): hoy `pmc.ncbi.nlm.nih.gov` sirvió reCAPTCHA y
  `europepmc.org/article` dio 403, y la API entregó los textos completos sin
  fricción. Límite: solo trae correos de correspondencia y hay que bajar el XML.
- **`einzigartigwir.de/stellenangebote`** es el tablón real del ZI Mannheim, al
  que solo se llega por redirección 303 desde `zi-mannheim.de`.

## Suscripciones pendientes

Las **25 siguen en TODO** (SUB-0001…SUB-0025): `owner_status.json` está vacío,
sin ninguna marca suya, así que todas cuentan como pendientes.

De esta pasada **no se añade ninguna**, y por segunda semana conviene que
conste el motivo: las tres ramas que podían proponer buscaron y ninguna logró
**abrir y leer** una URL de alta real. La única candidata que apareció,
`sanger.ac.uk/contact-us/newsletter/`, se abrió y devuelve 404. Una suscripción
con URL inventada es peor que no tenerla.

## Nota de mantenimiento — tercer aviso, y empeorando

`data/groups.tsv` ha pasado de 120 KB a **159 KB** en una semana y
`sources.tsv` de 148 KB a **183 KB**; `changelog.tsv` va por 207 KB. El umbral
de la regla son 60 KB. **El troceo lo hace una persona**, porque exige tocar
`tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit y eso no se
hace sin vigilancia al final de una pasada. Cuarta semana señalado.

## Qué perseguiría con más presupuesto

1. **Las once páginas del PGC que siguen sin abrir, ahora con los slugs
   correctos**, empezando por `cross-population-analyses-working-group` (el
   grupo de Peterson, que nombrará a sus co-chairs) y siguiendo por
   substance-use-disorders, schizophrenia, autism, suicide y anxiety. Sigue
   siendo la fuente con mejor rendimiento por llamada de todo el repo.
2. **Resolver la incógnita Sotoudeh** abriendo `ced.uab.es` directamente en vez
   de buscar: decide si existe una opción fuerte sin mudarse.
3. **Jerry Guintivano (UNC), que lidera el proyecto de depresión posparto del
   PGC**: es el mejor lead sin fichar, porque la genética psiquiátrica perinatal
   une su línea 2 y su línea 3 mejor que casi nada de lo encontrado. Falta
   abrir su página Tier 1 y sacar el correo. Detrás, Alex Kwong (Edimburgo,
   ALSPAC, ángulo del desarrollo) con una llamada de verificación.
4. **Los resultados del ERC Consolidator 2026**, que no estaban publicados hoy,
   con el mismo patrón de PDF; más Wellcome Discovery y Career Development 2026
   y consultas de nuevas concesiones en NIH RePORTER, que esta semana se quedaron
   sin presupuesto.
5. **La cola de seguimiento no alcanzada** (L-0002 Medland, L-0034 Ronald,
   L-0003 Speed, L-0037 Hettema/Verhulst): **ninguna necesita más
   investigación**, las cuatro necesitan un correo enviado, y eso es trabajo de
   ella. En L-0003 la pregunta viva es si la plaza con inicio el 1-oct-2026 se
   cubrió, fecha ya pasada.
6. El 8 de octubre, comprobar lo que pasó el día 7: si el abstract de la EPA
   entró y si hubo plaza en el Advanced MR de Bristol.
