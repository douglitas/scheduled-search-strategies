# ecosystem — 2026-10-12

Pasada completa, las cuatro ramas en el techo o cerca (19, 25, 24 y 25
llamadas). El ángulo de rotación de esta semana fue **(a) los artículos del
último mes y medio**, leídos por la **API REST de Europe PMC** en vez de por
buscador: ha dado la mejor ficha de la pasada y el ángulo **no está agotado**
(cuatro revistas no depositan en abierto dentro de la ventana —Biological
Psychiatry, Genes Brain and Behavior, Journal of Sleep Research y Nature
Mental Health— y devolvieron cero resultados, lo que es un hueco del método,
no inactividad del campo). El hallazgo de método que conviene no perder: **la
API v2 de NIH RePORTER** (`https://api.reporter.nih.gov/v2/projects/search`,
POST con JSON, sin clave y sin JavaScript) convierte «este PI probablemente
tiene dinero» en una fecha de fin de proyecto y una cifra. Es lo que ha
resuelto las dos fichas Fit 5 de hoy. Gotcha anotado en `sources`: hay que
consultar por apellido solo, porque «Apellido, Nombre» devuelve cero.

Tareas de backstop: **nada que hacer**. `data/source_inbox.json` está vacío
(`[]`) y `data/inbox_triage.tsv` no tiene ninguna fila PENDING (las tres filas
de hoy las cerró la rutina positions). Quinta semana que llegan limpias.

## Recuento (de `git diff HEAD~1 --stat`, no de memoria)

| fichero | altas | modificadas |
|---|---|---|
| groups | +8 (L-0048…L-0055) | 8 (L-0003, L-0011, L-0016, L-0018, L-0034, L-0040, L-0043, L-0044) |
| events | +3 (E-0026…E-0028) | 10 |
| training | +4 (T-0020…T-0023) | 8 |
| sources | +10 (SRC-0294…SRC-0303) | — |
| subscriptions | **0** | — |
| changelog | +51 apuntes | — |
| **action_now** | **35 filas mías** (antes 30) | 2 ajenas preservadas |

125 inserciones y 44 borrados; los borrados son reescrituras de fila en sitio,
verificadas una a una contra `HEAD` (groups 47→55, events 25→28, training
19→23, **ninguna fila perdida**). Comprobado además fila a fila que **ninguna
`Owner_Status` cambió** en las tres pestañas.

## Lo que exige decisión esta semana

1. **T-0007, Advanced Mendelian Randomization (Bristol, 25-27 nov 2026, online,
   630 GBP = 725 EUR): sigue vivo, el precio no se ha movido y el plazo de
   reserva es el 11-nov-2026.** El prerrequisito **no la deja fuera**: piden el
   curso básico de MR «o experiencia equivalente» y de R solo saber analizar
   datos (dan Posit Cloud); el único punto flojo es si nunca ha corrido un MR
   ella misma. **Pero hay un trabajo que solo puede hacer ella**:
   `brmsshortcourses.bristol.ac.uk` es un portal SkillsForge que únicamente
   renderiza con JavaScript, así que **no se ha podido comprobar si quedan
   plazas**. Hay que abrirlo en el navegador esta semana, no la que viene.
2. **Sustituto con dinero para lo que se ha perdido: la Beca Nacional AEGH para
   la ESHG 2027 — inscripción gratis más 600 EUR, plazo 2026-11-15 (34 días).**
   Tiene un filtro duro: más de dos años de socia continuada, que casi con
   seguridad no cumple. De ahí la acción real, que es doble y barata:
   **asociarse ya a la AEGH para que empiece a correr el contador**, y escribir
   a `secretaria@aegh.org` preguntando si admiten su caso para 2027. La beca la
   concede la AEGH y no el congreso, así que **la fila propia es de la rutina
   fellowships, no mía**: queda dicho aquí para que la recoja.
3. **Dos correos en frío que ahora sí tienen fundamento documental, los dos
   Fit 5.** **L-0048, Jerry Guintivano (UNC Chapel Hill)**: PI del R01MH135999
   del NIMH («MomGenes Fight PPD», multiancestral), **19-jun-2024 a
   31-ene-2029, 759.118 USD en el año fiscal 2026**, verificado en RePORTER —
   cubre de sobra mayo de 2027 y febrero de 2028. La genética psiquiátrica
   perinatal une su línea 2 y su línea 3 mejor que nada del mapa. Salvedad: **no
   publica correo** y no aparece en sus artículos abiertos; la vía es el
   teléfono 919-966-7548 o `jennifer_gibson@med.unc.edu`, y no se ha deducido
   ninguna dirección por patrón. **L-0044, Roseann Peterson**, abajo.

## Los dos hallazgos que cambian el mapa

- **L-0050, Tamar Sofer (Beth Israel Deaconess / Harvard) es la mejor ficha del
  barrido de revistas**: PI única del R01AG080598, literalmente puntuaciones
  poligénicas + sueño + envejecimiento, **hasta el 31-may-2028**, y del
  R01HL161012 hasta el 30-jun-2027. Es **el único grupo de todo el mapa que
  junta sus tres líneas con dinero vivo en las dos ventanas de disponibilidad**
  (mayo de 2027 y febrero de 2028). EEUU, luego necesita patrocinio de visado.
- **L-0044, Roseann Peterson: sube de Fit 4 a Fit 5 y la duda de la semana
  pasada era falsa alarma.** La atribución Tier 2 de que su único proyecto
  acababa el 31-oct-2026 queda corregida en RePORTER: tiene el **R01MH137208
  (PsycheMERGE) hasta el 31-05-2029, con 944.000 USD en 2026**, y el POP-GEM
  prorrogado al 31-10-2027. Puede contratar en 2027-2028 y al correo solo le
  queda la pregunta del visado.
- Y la que **evita una mudanza**: **L-0043, Ramina Sotoudeh queda resuelta a
  VERIFIED en los dos sentidos**. El ERC BEFOREBIRTH **sí está alojado en el
  Centre d'Estudis Demogràfics de Bellaterra** y ella lo lidera (nota del
  propio CED del 3-sep-2026 más CERCA del 4-sep). Y **todavía no hay equipo**:
  no figura en el personal investigador del CED y su portal de empleo real
  —`ced.factorial.es`, descubierto hoy— tiene tres convocatorias, ninguna de
  genética. O sea: **es el momento exacto del correo de preanuncio**, antes de
  que exista la plaza. Ojo al dominio: `ced.uab.es` está muerto (503), el vivo
  es `ced.cat`.

El resto de la cosecha de grupos, sin PI repetido de los 47 ya fichados:
L-0049 Alex Kwong (Edimburgo, ALSPAC, `akwong@ed.ac.uk`, Wellcome Early Career
Award 2024-2028), L-0051 Barbara Schormair (Helmholtz Múnich, **el único de la
UE continental, con financiación basal y sin problema de permiso de trabajo**),
L-0052 Hilary Martin (Sanger, `hcm@sanger.ac.uk`), L-0053 Varun Warrier
(Cambridge, **con el aviso explícito en la ficha de que la neuroimagen es dato
central y ella solo la ha usado supervisada**), L-0054 Gretchen Saunders
(Minnesota, `saund247@umn.edu`, **competencia LOW: la más realista de las
ocho**) y L-0055 Alicia Martin (Broad/ATGU, `armartin@broadinstitute.org`).

## Correcciones sobre filas que la dueña ya había leído

Seis filas con `Owner_Status` no vacío cambian de hechos. Su modelo mental de
estas queda obsoleto:

1. **E-0019, EPA 2027: cerró de verdad y no hay segunda oportunidad.** El
   7-oct-2026 era ya el plazo **extendido**; la página dice ahora «Abstract
   Submissions are now closed!» y, lo decisivo, **«Late-breaking abstract
   submission will not be available for EPA 2027»**. Las becas de viaje de la
   EPA se pedían dentro del mismo envío, así que cerraron con él. La fila pasa a
   CLOSED con los requisitos documentados para la edición 2028 (abstracts hacia
   primeros de octubre de 2027, estimado). **Si la leyó la semana pasada con el
   plazo vivo, esto es lo que ha cambiado.**
2. **L-0011, St Pourcain: conflicto de fuentes que NO se reconcilia en
   silencio.** `mpi.nl` ha vuelto a responder (quitarlo de la lista de
   bloqueos) y el anuncio vivo **dice Max Planck Society, sin una sola mención
   al consorcio R2D2**, lo que contradice de plano la «corrección» del
   5-oct-2026 que atribuía esta ronda al proyecto HORIZON-HLTH-21. Se registra
   el conflicto en la fila y **el correo no debe citar una fuente de
   financiación concreta hasta deshacerlo**. Dos datos firmes: la plaza sigue
   abierta en revisión continua sin fecha de cierre, hay **una** plaza y no dos,
   y el obstáculo real es el **inicio previsto el 1-dic-2026, «negociable»** —
   imposible sin negociarlo, porque ella no está libre hasta mayo de 2027.
3. **L-0044** (de «acaba el 31-10-2026, sin confirmar» a financiada hasta 2029,
   proyecto nuevo y Fit 4→5) y **T-0014, SSGAC/CESR: cerrada.** Es una serie
   mensual (tercer jueves) pero no hay ninguna sesión futura anunciada, ninguna
   sin la puerta del Controlled Tier de All of Us que ella no tiene, y ninguna
   lista de correo a la que apuntarse.
4. **E-0002 ASHG 2026 (Montreal, 20-24 oct), E-0005 IGES 2026 y E-0007 Sleep
   Europe 2026: los tres pasan a CLOSED**, sin abstract enviado y sin acción
   posible. De ASHG quedan verificadas las tarifas Late/Onsite (825 USD en
   formación, no socia) y **no hay inscripción virtual publicada**. Los otros
   dos se cierran **sin verificar** porque `geneticepi.org` y `sleepeurope.eu`
   devuelven 503 hoy.
5. **L-0034, Angelica Ronald**: hallazgo colateral de la rama de descubrimiento
   que la rama de seguimiento no alcanzó. Es **autora de correspondencia del
   GWAS de temperamento en lactantes y niños pequeños publicado en Nature Human
   Behaviour en 2026** — el cruce exacto de su línea 2 con su línea 3, y el
   mejor gancho posible para el correo. La dirección `a.ronald@surrey.ac.uk` va
   **LIKELY y no VERIFIED**: está leída en el artículo, no en su ficha de
   Surrey.

## Cerrado, pasado o no confirmado

- **WCPG 2027: encontrada la ruta viva, `https://ispg.net/wcpg-2027/`** (el
  404 de `ispg.net/world-congress/` queda sustituido). Solo publica Brisbane,
  9-13 nov 2027, y «Registration coming soon». Sí queda verificado que **ella
  encaja en la elegibilidad del ECIP** y que los premios de inicio de carrera se
  marcan **dentro del envío del abstract**. Lo que **no** se ha podido verificar
  es el patrón de mayo (14-may-2024 / 14-may-2025): que la ventana de 2027 abra
  hacia mayo queda como **conjetura explícita**, no como dato.
- **Negativos verificados, que son resultado y no fracaso**: ninguna de las 34
  vacantes académicas vivas de la UiO es de Psicología ni de PROMENTA, así que
  **L-0040 (Cheesman) sigue sin plaza** pese al ERC de 1,5 M EUR (ruta correcta
  `/vacancies/academic`; la que teníamos, `/scientific/`, da 404). Ningún curso
  nuevo de genética estadística, PRS ni Python en el catálogo de Bristol (lo
  nuevo son pilotos cerrados a gente de Bristol). **Cero cursos 2027 de
  PRSice / LDpred2 / PRS-CS / LDSC / SAIGE / REGENIE / GCTA**; ninguna formación
  de analistas del PGC con calendario; ninguna escuela de verano europea 2027 de
  epidemiología genética o genética del comportamiento; **ESRS Sleep Science
  School 2027** sigue sin anunciar (`esrs.eu` sigue en 403; por buscador solo
  aparecen los patrones 2023/2025). **All of Us Researcher Academy** existe y es
  gratuita, pero exige institución con Institutional Champion award en EEUU y su
  convocatoria figura cerrada: **la deja fuera la elegibilidad**, no se ficha.
  Y el **único curso de 2027 publicado por Wellcome** es T-0022 (Cancer Genomic
  Epidemiology), lo que reafirma el negativo de T-0004.
- **Los seis cursos de Bristol ya fichados (T-0002, T-0003, T-0008, T-0009,
  T-0015, T-0016) quedan confirmados en UNA sola llamada al índice**: fechas y
  cuotas intactas, ninguno lleno.
- **E-0026, ICHG 2027 (Guadalajara, 1-5 mar 2027), con un conflicto que no se
  reconcilia**: es el congreso mundial de genética humana, cada ~5 años, **sin
  visado para españoles**, pero una fuente dice que los abstracts están abiertos
  mientras la llamada a revisores (revisión del 18-sep al 15-oct-2026) implica
  que ya cerró, y **no se ha localizado la web oficial**. La fila va LIKELY en
  ciudad y fechas, UNVERIFIED en todo lo demás. E-0027 (Genomics of Brain
  Disorders, Wellcome) y E-0028 (MR Conference de Bristol, 200 GBP para ECR)
  entran como filas de vigilancia, las dos sin edición nueva anunciada.
- **T-0020, FinnGen user training 1 (25-ene-2027, Zoom, gratis, VERIFIED)** es
  lo mejor del descubrimiento de formación: **la única de las tres versiones
  abierta sin afiliación finlandesa**, un biobanco distinto de UK Biobank (cuyo
  dominio entero sigue en 403) y **cero días de permiso**. Fit 3 honesto: es
  orientación de acceso, no métodos de PRS. Detrás, T-0021 (seminarios
  mensuales del PGC, gratis, su línea 2, Fit 3) y T-0023 (escuela de Davos, Fit
  3, UNVERIFIED: ediciones 2022 y 2024, así que la plausible es 2028).
- **T-0001 (Boulder) no se ha mirado**, conforme a la instrucción de bajarlo a
  sondeo mensual: se comprobó el 2026-10-05 y no sobró presupuesto. **T-0005 y
  T-0017 quedan sin verificar** y sus filas sin tocar.
- **L-0016 (Palamara) y L-0003 (Speed) se quedan sin re-verificar, y se dice en
  lugar de adornarse**: las dos fichas Tier 1 de Palamara dan 404 y 403, no hay
  anuncio de ARGgen y su último postdoc cerró el 2-may-2025 pagado por
  **SMARTbiomed (Oxford-Aarhus-Copenhague)**, que lo conecta con L-0003;
  `palamara@stats.ox.ac.uk` **solo consta en un anuncio caducado y no debe
  usarse**. El portal de Aarhus solo pinta con JavaScript, así que lo de Speed
  se reorienta a preguntárselo por correo a `doug@qgg.au.dk`. En estas dos filas
  y en L-0018 **`Last_Verified` se ha dejado donde estaba**.
- **L-0018 (Falck-Ytter / Viktorsson, Uppsala), que es línea 3 y está
  infradotada**: artículo nuevo en Developmental Science (uu.se, 9-ene-2026) y
  un gancho excelente (su podcast en ACAMH), pero **correo y financiación siguen
  sin verificar y no se deducen**.
- **Bloqueos nuevos, todos anotados en `sources`**: el portal SkillsForge de
  Bristol (solo JavaScript); `ebi.ac.uk/training/events/` con **bucle de más de
  diez redirecciones**; `geneticepi.org` y `sleepeurope.eu` en 503;
  `bga.clubexpress.com` **también en 403**, lo que deja a E-0004 y E-0011 sin
  ninguna ruta automática (vía: correo a la secretaría de la BGA);
  `ced.uab.es` y `ced.uab.cat` en 503; `ddd.uab.cat` con antibot Anubis;
  `uio.no/.../scientific/` en 404; la página de alta de alertas de Behavior
  Genetics (`link.springer.com/journal/10519/subscribe`), **enlazada desde su
  propia portada, da 404**; `isir-society.com` no resuelve;
  `ispg.net/newsletter/` carga sin formulario; `fullTextXML` de Europe PMC
  devuelve 500 en algunos PMCID. **Y uno que se levanta: `mpi.nl` responde otra
  vez.**

## Suscripciones pendientes

Las **31 siguen en TODO** (SUB-0001…SUB-0031, dos de ellas añadidas hoy por la
rutina fellowships): `owner_status.json` está vacío (`{}`), sin ninguna marca
suya, así que todas cuentan como pendientes.

De esta pasada **no se añade ninguna, y es la tercera semana seguida**. El
motivo es el mismo y conviene que conste, porque no es desidia: las cuatro
ramas buscaron canal de alta y **ninguna logró abrir y leer una URL de
suscripción real**. FinnGen da enlaces por sesión y los colgados son de 2025;
el PGC no tiene formulario ni lista; Cardio-CARE solo publica un correo; la ISPG
carga su página de boletín sin formulario; y la de Behavior Genetics, enlazada
desde la portada de la propia revista, es un 404. **Una suscripción con URL
inventada es peor que no tenerla.**

## Nota de mantenimiento — quinto aviso, y el umbral ya lo pasan cuatro ficheros

`data/groups.tsv` ha pasado de 159 KB a **200 KB** en una semana,
`sources.tsv` de 183 KB a **211 KB**, `changelog.tsv` va por **255 KB** y
**`events.tsv` acaba de cruzar el umbral, con 59,9 KB**. La regla son 60 KB.
**El troceo lo hace una persona**, porque exige tocar `tools/build_page.py` y
`tools/build_xlsx.py` en el mismo commit y eso no se hace sin vigilancia al
final de una pasada. Quinta semana señalado.

## Qué perseguiría con más presupuesto

1. **Terminar el barrido de revistas por la vía que no es Europe PMC**, porque
   cuatro de las revistas que más le importan no depositan en abierto dentro de
   la ventana y hoy devolvieron cero: Biological Psychiatry, Genes Brain and
   Behavior, Journal of Sleep Research y Nature Mental Health. Hay que ir a sus
   índices de números recientes, no a la API.
2. **Pasar por RePORTER los PIs estadounidenses que ya están fichados sin dato
   de financiación** (L-0017 Huckins, L-0019 Sánchez-Roige, L-0029 Robinson,
   L-0031 Lencz, L-0035 Docherty, L-0037 Hettema, y los nuevos L-0053 Warrier,
   L-0054 Saunders y L-0055 Alicia Martin): es una sola llamada por PI y
   convierte «desconocido» en una fecha de fin de proyecto.
3. **Deshacer el conflicto de L-0011** (Max Planck Society contra R2D2) leyendo
   el anuncio completo, y preguntar por escrito si el inicio del 1-dic-2026 se
   puede negociar hasta mediados de 2027: de eso depende que la plaza exista
   para ella.
4. **Los eventos que se quedaron fuera por techo**: E-0013 World Sleep 2027
   (plazo 2027-01-20, el más cercano de los vivos), E-0016 EMGM 2027, E-0008
   SLEEP 2027, el IGES 2027 y los satélites de ESHG y ASHG, donde suelen vivir
   los workshops de PRS.
5. **Las once páginas del PGC con los slugs correctos**, que siguen sin abrir
   desde el 2026-09-28 y que la semana pasada ya encabezaban esta lista.
6. **La cola de seguimiento que no necesita más investigación sino un correo
   enviado**, y eso es trabajo de ella: L-0002 Medland, L-0027 Huang (con el
   paquete ya especificado: CV, una página de intereses y tres referencias),
   L-0033 Mullins, L-0043 Sotoudeh (preanuncio) y los dos Fit 5 de hoy.
