# ecosystem — 2026-09-28

Pasada completa, las cuatro ramas en el techo o cerca (26, 25, 24 y 27 llamadas).
El ángulo de rotación de esta semana fue **(e) las listas de liderazgo de los
working groups del PGC**, estrenado, y ha resultado el más rentable de todos los
probados hasta ahora por una razón concreta: cada página de trastorno publica
cargo **y correo institucional verbatim**, que es justo el cuello de botella que
venía arrastrando la rama 1 semana tras semana (encontrar gente sí, poder
escribirle no). Como apoyo, **(a) los papers de agosto y septiembre**.

Tareas de backstop: **nada que hacer**. `data/source_inbox.json` está vacío
(`[]`) y `data/inbox_triage.tsv` no tiene ninguna fila PENDING. Tercera semana
que la cierran limpia las rutinas anteriores.

## Recuento (de `git diff HEAD~1 --stat`, no de memoria)

| fichero | altas | modificadas |
|---|---|---|
| groups | +7 (L-0033…L-0039) | 11 (una a una) |
| events | +2 (E-0022, E-0023) | 5 |
| training | 0 | 6 |
| sources | +13 (SRC-0209…SRC-0221) | — |
| subscriptions | **0** | — |
| changelog | +44 apuntes | — |
| **action_now** | **27 filas mías** (antes 25) | 3 ajenas preservadas |

111 inserciones y 43 borrados; los borrados son reescrituras de fila en sitio,
verificadas fila a fila (groups 32→39, events 21→23, training 17→17, ninguna
perdida). Comprobado además que **ninguna columna `Owner_Status` cambió** en
ninguna de las tres pestañas.

## Lo que exige decisión esta semana

Dos relojes, y el primero es una resurrección:

1. **EPA 2027: el plazo NO había muerto. La EPA lo extendió al 7 de octubre
   de 2026** (E-0019, Fit 4, VERIFIED en `epa-congress.org/abstract-submission/`).
   La semana pasada este informe lo dio por vencido el 21-sep y por perdida la
   edición entera. Era el comportamiento que la propia ficha anticipaba —el año
   anterior extendieron tres días—, salvo que esta vez han sido dieciséis.
   **Quedan nueve días y no habrá ronda late-breaking.** Admite e-poster de
   exposición, que es la vía de menor esfuerzo con material ya escrito, y los
   travel grants de early career se piden marcando la casilla dentro del propio
   envío. Florencia cae aún dentro de la residencia, así que exige pedir días.
2. **Bristol abre reservas el 7 de octubre a mediodía, hora del Reino Unido**,
   el mismo día. El registro anual de cuenta está abierto desde el 23-sep, así
   que **crear la cuenta esta semana** es condición previa para poder reservar
   ese día. El curso con el plazo más cercano sigue siendo **T-0007, Advanced
   MR, 25-27 nov 2026, 725 EUR** (plazo de reserva 2026-11-11).
3. Sigue viva, sin moverse, **L-0011 (St Pourcain, MPI Nijmegen): el correo
   antes del 8-oct**, cuando arranca la revisión rodante. Pero con un cambio de
   enfoque, abajo.

## Los dos hallazgos que cambian el mapa

- **WCPG 2027 ya está anunciado: Brisbane, Australia, 9-13 de noviembre de 2027**
  (E-0022, Fit 5, VERIFIED en la portada de `ispg.net`). Tras dos semanas de
  negativo verificado, aparece en la home aunque `past-congresses` aún no lo
  recoja. Es su congreso más on-profile y cae **en la ciudad de QIMR Berghofer**,
  de donde sale su manuscrito de Nature Mental Health: presentar ahí es a la vez
  poster y prospección de postdoc. Además noviembre de 2027 ya no depende de
  días libres del hospital y llega tres meses antes de la defensa prevista. Sin
  plazo de abstracts todavía; la ventana del ECIP fue en mayo el año pasado.
- **Las becas de viaje, el hueco que llevaba semanas señalado, por fin tienen
  respuesta.** **ESHG**: hasta 140 fellowships europeas con inscripción gratuita
  más 400 EUR de viaje, y el detalle operativo que importa es que **se solicitan
  marcando una casilla DENTRO del envío del abstract**, no como trámite aparte
  — lo que ata la beca de ESHG 2027 al plazo del 4-feb-2027. Ella cumple
  elegibilidad con holgura (no es PI, menos de cuatro años postgrado).
  **IGES**: existen Roger Williams y James V. Neel, 1.000 USD cada uno, exigen
  ser primera autora del abstract, pero solo constan en una página de 2019; el
  Wellcome de IGES es únicamente para países de renta baja o media, **no es
  elegible**. **BGA**: existen, con plazo TBA.

## La cosecha de grupos (ángulo PGC)

Siete fichas, dos Fit 5, y ninguna repite PI de las 32 ya fichadas:

- **L-0033, Niamh Mullins (Mount Sinai)** — la mejor de la tanda y la única con
  plaza declarada: su web dice por escrito que hay postdoc o staff scientist
  abiertos **y que patrocinan visado**, con cinco R01 activos. Línea 1 y 2
  exactas, sin pedir neuroimagen ni electrofisiología. El ángulo diferencial es
  su R01 de predicción de riesgo sobre historia clínica electrónica: ahí una
  residente de Medicina de Laboratorio aporta algo que un bioinformático puro no.
- **L-0034, Angelica Ronald (Surrey)** — el único sitio del mapa que cubre **sus
  tres líneas a la vez**: es coautora del estudio de gemelos de 2026 sobre sueño
  a los 2 y 5 meses que deriva ocho PRS. No hay plaza, así que la vía honesta es
  co-escribir un fellowship para 2028, no una candidatura.
- **L-0037, Hettema y Verhulst (Texas A&M)** es, por coste, **la acción de mayor
  retorno de toda la pasada**: ofrecerse como analista colaboradora del Core
  Analytical Group de ansiedad del PGC no depende de que exista plaza, puede
  empezar en 2027 sin esperar a la defensa, y ataca de raíz el punto débil del
  expediente, que es la ausencia de publicaciones destacadas.
- Detrás, L-0035 (Docherty, Utah, cinco R01), L-0036 (Joanna Martin, Cardiff,
  con tres huecos sin cerrar), L-0038 (Levey, Yale, contacto más que destino) y
  L-0039 (Doherty, Oxford, sueño de adulto por acelerometría, sin correo).

## Correcciones sobre filas que la dueña ya había leído

- **L-0011: el desajuste de fechas deja de ser un muro.** Se ha comprobado que
  el grupo **reabre esta misma plaza de tres años en rondas sucesivas** (hubo
  una en marzo-abril de 2026, con inicio en mayo) y que tiene además un doctorado
  de cuatro años abierto. El correo del 8-oct debe preguntar por **la ronda de
  2027-2028**, no solo por si diciembre es negociable. Banda salarial de la ronda
  anterior: 5.709,87–7.025,87 EUR brutos/mes más 8% de vacaciones.
- **L-0026 y L-0020 son el MISMO grupo**, no dos oportunidades. Shuyang Yao es
  Assistant Professor **dentro** del grupo Precision Psychiatry de Yi Lu, y el
  ERC Starting Grant es el instrumento con el que se independiza. Un solo correo,
  a Yao, que es quien tiene el dinero nuevo. Su email queda **VERIFICADO**:
  `shuyang.yao@ki.se`.
- **L-0003, Doug Speed: email verificado por fin**, `doug@qgg.au.dk`, vía
  `pure.au.dk`, que sortea los dos bloqueos que lo impedían. Y su producción no
  es solo metodología y genética agrícola como decía la ficha: hay un artículo de
  2025 sobre **PRS y respuesta a antidepresivos y benzodiacepinas**, que es su
  línea 2 y el gancho natural para el correo.
- **L-0004, Tiemeier: la deuda del email se cierra en negativo.** Harvard Chan
  **no lo publica** —ni teléfono, ni despacho, ni asistente—. Dejar de buscarlo
  ahí; la vía es Harvard Catalyst o la dirección de correspondencia de su
  artículo de 2024 sobre predisposición genética al sueño infantil.
- **L-0010, Cormand: la URL del grupo que teníamos no era la suya.** La buena es
  `ub.edu/ibub/research-group/human-molecular-genetics/`.
- **T-0017 se cierra**: no era un curso pendiente sino un seminario web único del
  31-ene-2023, gratuito y ya celebrado. Solo queda la grabación.

## Cerrado, pasado o no confirmado

- **Negativos verificados el 28-sep, que son resultado y no fracaso**: Karolinska
  (ninguna plaza en MEB entre ~70), VU Amsterdam (19 vacantes, nada en CNCR ni
  Complex Trait Genetics), Amsterdam UMC (92 vacantes, 7 de investigación,
  ninguna de psiquiatría ni genética) y KCL (nada en SGDP; lo único vivo en el
  IoPPN es un Clinical Research Fellow de neuroimagen que cierra el 7-oct y no
  encaja).
- **T-0006 (CSHL): negativo ahora sólido.** Ya hay calendario 2027 publicado con
  cinco cursos y ninguno es el suyo. Congelado hasta primavera de 2027.
- **T-0001 (Boulder): sin novedad**, tercera semana. Inscripción sin abrir y sin
  tarifa; los 550 EUR siguen siendo estimación. Contacto para aviso:
  IBGworkshop@colorado.edu.
- **T-0012 (SMARTbiomed)**: la página sigue sin tocarse desde agosto, las fechas
  de 2027 siguen sin sostenerse y la fila se deja como estaba.
- **BGA 2028 (Tartu): negativo verificado**, la página oficial dice literalmente
  «TBA». **ESHG 2027** no publica aún ni tarifas ni apertura del portal de
  abstracts. Hallazgo lateral: **ESHG 2028 ya tiene fechas** (17-20 jun, sede por
  anunciar) y cae después de su defensa, así que entra como E-0023.
- **Descubrimiento flojo en formación**: los dos cursos de PRS del KCL/SGDP que
  parecían leads son ediciones de 2018 y 2019 sin continuidad, y **el PGC no
  convoca taller de analistas**, solo material autoformativo. Ninguno da fila.
- **Bloqueos nuevos, todos ya anotados en `sources`**: `pgc.unc.edu` devuelve 502
  y 503 intermitentes al pedir varias páginas en paralelo —**no es bloqueo**,
  hay que reintentar espaciado—; `mpi.nl` 503 a lectura automática (tres
  intentos); `ki.se/en/about/work-at-ki/available-jobs` 404 (usar `ki.varbi.com`);
  `psych.mpg.de/career` 404; `ub.edu` 503; `jobbnorge.no` 404 en las dos formas
  de URL probadas; `karriere.ukw.de` no renderiza listados; `ndph.ox.ac.uk` y
  `bdi.ox.ac.uk` 403; **Cardiff cerrado por completo**, no solo su portal de
  empleo (`profiles.cardiff.ac.uk` y `/people/view` ambos 403);
  `ebi.ac.uk/training/events/` en bucle de redirecciones;
  `community.ukbiobank.ac.uk` 403. Vía de rodeo comprobada para los 403
  institucionales: sacar el correo de correspondencia desde la versión en PMC.
- **La página de fees de Bristol NO lista precios por curso**: remite a cada
  ficha. Anotado para no volver a perder una llamada ahí.
- No alcanzado por presupuesto: **L-0013 (Lehto)**, **L-0021 (Havdahl**, dos
  intentos de URL fallidos), **L-0027 (Huang)** y **L-0024 (Streit**, cuyo email
  `fabian.streit@zi-mannheim.de` **sigue siendo probable y no confirmado**: no
  usarlo sin verificar).

## Suscripciones pendientes

Las **22 siguen en TODO**: `owner_status.json` está vacío, sin ninguna marca
suya, así que todas cuentan como pendientes (SUB-0001…SUB-0022).

De esta pasada **no se añade ninguna**. Las tres ramas que podían proponer
buscaron y ninguna consiguió verificar una URL de alta real, así que devolvieron
lista vacía en lugar de inventar una. Es la decisión correcta y conviene que
conste: una suscripción con URL inventada es peor que no tenerla.

## Nota de mantenimiento

`data/groups.tsv` está ya en **120 KB** (subió de 86 a 120 en dos semanas) y
`sources.tsv` en **148 KB**, ambos muy por encima del umbral de 60 KB. Según la
regla, el troceo lo hace una persona, porque exige tocar `tools/build_page.py` y
`tools/build_xlsx.py` en el mismo commit. **Tercera semana señalado, y el ritmo
de crecimiento se acelera.**

## Qué perseguiría con más presupuesto

1. **Terminar el recorrido del PGC**: quedan once páginas sin abrir (autism,
   bipolar-disorder, mdd, substance-use-disorders y siete más). Hay material para
   dos o tres semanas sin repetir consulta, y es la fuente con mejor rendimiento
   por llamada de todo el repo.
2. **Roseann Peterson** (co-chair de Cross-Population del PGC, multiancestria):
   cribada pero no fichada porque no se pudo confirmar su institución actual, y
   el correo que publica el PGC está **mal escrito en origen** (`gmailcom`, sin
   punto). Primera candidata de la semana que viene.
3. **El 7 de octubre es día doble**: confirmar que las reservas de Bristol
   abrieron y que T-0007 sigue en 725 EUR, y que el plazo de la EPA cerró de
   verdad.
4. **La formación en manejo de biobancos sigue sin una sola fila en la tabla**
   —es una carencia declarada suya—: atacar UK Biobank por una vía no bloqueada
   (`ukbiobank.ac.uk/researcher-training/` o la documentación de DNAnexus) y
   buscar la edición 2027 del Erasmus Summer Programme con tarifa.
5. Escribir a la ISPG por la cuantía del ECIP y a la IGES por si Williams y Neel
   siguen vigentes: son las dos cifras que deciden si puede ir a algo.
