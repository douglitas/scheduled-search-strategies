# ecosystem — 2026-09-14

Pasada completa, las cuatro ramas dentro de presupuesto (22, 21, 24 y 23
llamadas). El ángulo de descubrimiento de esta semana fueron las subpáginas de
los **working groups del PGC**, que era el hilo que el informe anterior dejó sin
tirar: resultó ser la fuente más rentable de la pasada y deja material ya
cribado para la próxima rotación.

Tareas de backstop: **nada que hacer**. `data/source_inbox.json` está vacío
(`[]`) y `data/inbox_triage.tsv` no tiene ninguna fila PENDING. La semana cierra
limpia.

## Recuento (de `git diff HEAD~1 --stat`, no de memoria)

| fichero | altas | modificadas |
|---|---|---|
| groups | +6 (L-0020…L-0025) | 9 (L-0001…L-0011, una a una) |
| events | +3 (E-0016…E-0018) | 9 |
| training | +3 (T-0011…T-0013) | 10 (las diez previas) |
| sources | +11 (SRC-0137…SRC-0147) | — |
| subscriptions | +1 (SUB-0017) | — |
| changelog | +52 apuntes | — |
| **action_now** | **22 filas mías** (antes 19) | 3 ajenas preservadas |

125 inserciones, 46 borrados; los borrados son reescrituras de fila en sitio,
verificadas fila a fila por `apply_rows` (ningún fichero perdió filas).

## Lo que exige decisión esta semana

Tres relojes, y dos de ellos no estaban en la tabla hace siete días:

1. **ASHG 2026: la tarifa anticipada cierra MAÑANA, 15-sep a las 17:00 ET**
   (E-0002, Fit 5). Confirmado que sigue viva hoy. El dato que decide:
   **hacerse socia *student-trainee* antes de inscribirse baja la cuota de 775
   a 435 USD** — unos 313 € de ahorro, más de lo que cuesta la cuota de socia.
   Después del 16-sep solo queda late/onsite; no hay tarifa de un día ni opción
   virtual. Iría como asistente: el plazo de resúmenes ya pasó.
2. **IGES 2026: la tarifa *early* cierra el 19-sep, dentro de 5 días** (E-0005,
   Fit 4). Este reloj no lo teníamos. Y trae un hallazgo de calendario que
   cambia la aritmética: IGES cae el **18-20 oct en Estérel, a una hora de
   Montreal, justo antes de ASHG (20-24 oct, Montreal)** — un solo vuelo
   transatlántico compraría las dos salas. El freno es el dinero, no el encaje:
   las dos inscripciones juntas rondan los 1.400 € sin vuelo ni hotel. Si tiene
   que elegir una, ASHG da más contactos y IGES más método.
3. **Bristol abre reservas con dos fechas encadenadas** (T-0002, T-0003 y
   SUB-0017): la **cuenta de reservas se crea desde el 23-sep a mediodía** y las
   **reservas del programa 2026/27 abren el 7-oct a mediodía** hora del RU. Sin
   cuenta creada antes, no se puede reservar el día que abren. Confirmado
   además que **ninguno de los *voucher packs* de Bristol le aplica**: los
   cuatro cursos salen íntegros de su bolsillo.

Detrás, lo mejor de la cosecha de grupos, ambos Fit 5 y ambos VERIFIED:

- **L-0020, KI Psychiatric Genomics Institute (Yi Lu, Karolinska/MEB)** — sus
  líneas 1 y 2 combinadas, con financiación diversificada (VR + tres proyectos
  UE + NIMH) y, lo específico para ella, fenotipos de resistencia al tratamiento
  construidos leyendo historia clínica: ahí su título de Medicina es operativo,
  no biográfico.
- **L-0021, PsychGen Centre (Alexandra Havdahl, FHI Oslo)** — el único sitio de
  toda la pasada donde convergen sus **tres** líneas: MoBa tiene fenotipos de
  sueño repetidos en los primeros años con genotipado de madre, padre e hijo, y
  el centro los explota con diseño intrafamiliar. Es literalmente el sustrato de
  su revisión del *Journal of Sleep Research* con los métodos de su tesis.

## Correcciones sobre filas que la dueña ya había leído

Cinco cosas que la tabla daba por buenas y no lo eran:

- **L-0004 baja de Fit 5 a Fit 4, y el destinatario cambia.** Queda confirmado
  que **Desana Kocevska no dirige grupo y no puede contratar**; ni siquiera
  figura entre los 28 miembros del grupo de Van Someren en el NIN, y su ficha de
  Erasmus MC sigue dando 404. El PI al que hay que escribir es **Henning
  Tiemeier**, de Generation R. La bajada es estructural, no por competencia: la
  cohorte sigue siendo el sustrato ideal, pero ya no hay dentro nadie con
  experiencia específica en genética del sueño pediátrico, así que entraría a
  *construir* esa línea, no a sumarse a ella. **Escribirle a Kocevska pidiendo
  plaza habría sido un error.**
- **L-0007: la puerta del IBG de Boulder está cerrada por la vía habitual.**
  Confirmado en documentación oficial del NIH: las becas **T32 exigen ciudadanía
  estadounidense o residencia permanente**, y eso no se arregla con patrocinio de
  visado. Solo le sirve un contrato con fondos de proyecto de Grotzinger. Dos
  datos más: su URL **no estaba rota** (sube a VERIFIED) y su ficha lo lista como
  ***Adjunct Professor***, cargo que suele implicar menor capacidad de contratar
  — hay que preguntárselo en el primer correo.
- **T-0010 (Tartu) estaba mal leída: era la edición 2026, ya celebrada.** La fila
  no tenía fechas y parecía una convocatoria viva; el plazo cerró el 20-abr-2026.
  Marcada CLOSED.
- **E-0008, SLEEP 2027: conflicto de fechas resuelto, y las dos eran ciertas.**
  El 5-jun era el arranque de los cursos de posgrado, no del congreso. Se adopta
  **6-9 jun 2027**.
- **L-0003 (Aarhus): la plaza está vencida por partida doble.** No solo caducó el
  plazo en mayo: la incorporación que anunciaba es el **1-oct-2026, dentro de dos
  semanas**. Tratarla como oportunidad viva ya no es realista; lo vivo es la ERC
  Consolidator de Doug Speed y sus futuras rondas.

## Plazas vivas hoy, y un aviso sobre action_now

**Sigue habiendo una sola plaza viva en toda la tabla de grupos: L-0011, Max
Planck Nijmegen** (Statistical Genomics/Genetic Epidemiology, 3 años, revisión
rodante desde el 8-oct). Pero su lectura cambia: el anuncio exige doctorado *en
mano o inminente* y su defensa es feb-2028, catorce meses después del inicio
propuesto. «Negociable» en un anuncio Max Planck rara vez significa más de un
año. Análisis, no dato verificado: **esta convocatoria concreta probablemente no
es alcanzable**, y el correo antes del 8-oct debe cambiar de objetivo —
posicionarse para la ronda 2027-2028 en vez de competir por esta.

**Aviso de visibilidad:** L-0011 y L-0004 **no aparecen en action_now**. No es un
fallo: la regla de selección admite Fit 4-5 con plazo a 90 días o sin plazo solo
si son Fit 5, y ambas son Fit 4 sin fecha de cierre. Como L-0011 es la única
plaza abierta que existe, conviene leerla directamente en la pestaña `groups`.

## Verificación

- De los 6 grupos nuevos: **4 VERIFIED** (Karolinska, PsychGen, Radboudumc,
  iPSYCH), 1 LIKELY y 1 UNVERIFIED (Fabian Streit: su co-presidencia del MDD
  Working Group del PGC sí está verificada, pero dos URL del ZI Mannheim dieron
  404 y su adscripción es Tier 2).
- Subidas a VERIFIED abriendo la Tier 1: **L-0002 (QIMR)** — abierto por fin su
  ATS propio, y queda confirmado que **no hay ninguna plaza de genética en todo
  el instituto**, así que el correo en frío a Medland o a Colodro Conde ya no
  tiene que esperar a ningún anuncio —, **L-0006 (KCL**, con el correo de Lewis
  localizado**)** y **L-0007**.
- Pista cerrada sin gasto futuro: el grupo de *Neuropsychiatric genomics* de
  Tartu que buscábamos **lo dirige Kelli Lehto**, que ya estaba fichada (L-0013).
  No es un grupo distinto.

## Cerrado, pasado o no confirmado

- **T-0005 (CAJAL)** sigue CERRADO: el listado no pasa de diciembre de 2026, sin
  ninguna edición 2027 de ningún curso del programa.
- **T-0004 (Wellcome)** y **T-0006 (CSHL)**: sin edición 2026 ni 2027. Revisar en
  enero y en primavera de 2027 respectivamente.
- **T-0001 (Boulder)**: fechas 2027 confirmadas (1-5 mar), pero **la inscripción
  aún no ha abierto** y no hay cuota publicada — los 550 € de la ficha siguen
  siendo estimación. Dato que conviene tener presente: ese curso de marzo se
  imparte **cada tres años**, así que perder 2027 significa esperar a 2030.
- **WCPG 2027 no está anunciado** — y esta vez es un negativo verificado en Tier
  1, no un fallo de búsqueda: la lista de próximos congresos de la ISPG termina
  en 2026. Probablemente se anuncie en Glasgow: volver a mirar a primeros de
  octubre.
- **Cuotas del WCPG 2026: siguen sin poder verificarse** tras un segundo intento
  por otra puerta. El portal carga por JavaScript e `ispg.net/registration` aún
  muestra el WCPG 2022 de Florencia. No insistir por vía automática: la única
  salida es escribir a info@ispg.net.
- Bloqueos confirmados o nuevos (anotados ya en `sources`): `esrs.eu`, Cardiff y
  Wiley siguen en 403; `sleepmeeting.org` devuelve contenido vacío por segunda
  semana (dejar de abrirla directamente); `au.career.emply.com` y `sira.ub.edu`
  **requieren navegador real** — de ahí que L-0010 (Cormand) siga UNVERIFIED;
  `ebi.ac.uk/training/events/` entra en bucle de redirecciones.
- Sin presupuesto para mirarlos: **L-0005 (Cardiff)** — queda pendiente una
  vacante *Research Assistant/Associate (Statistics)* que **cierra el 17-sep**,
  dentro de tres días —, **L-0009** y los ocho grupos fichados el 2026-09-07.

## Suscripciones pendientes

Las **17 siguen en TODO**: `owner_status.json` está vacío, sin ninguna marca
suya, así que todas cuentan como pendientes (SUB-0001…SUB-0017).

De esta pasada se añade **una sola**, no dos: **SUB-0017, la cuenta de reservas
de los cursos cortos de Bristol** (la que el tope dejó fuera la semana pasada, y
ahora con fechas verificadas). La segunda candidata natural era la membresía de
la IGES —que además daría avisos del GAW 2027 y de las ventanas de tarifa—,
pero **no se pudo verificar su URL de alta en esta pasada y no se inventa**:
queda como primera candidata de la semana que viene.

## Dos notas de mantenimiento

- **`data/groups.tsv` ha pasado de 60 KB (hoy 79 KB), y `sources.tsv` está en
  94 KB.** Según la regla, el troceo lo hace una persona, porque exige tocar
  `tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit y no es
  trabajo para hacer sin vigilancia al final de una pasada. Queda señalado.
- **El checkout llegó en *detached HEAD***: el primer `git push` dijo
  «Everything up-to-date» sin subir nada, aunque el commit existía. Se detectó y
  se corrigió reapuntando `main`, y los datos están en el remoto. Conviene que
  las pasadas futuras comprueben `git status -sb` antes de dar el push por bueno.

## Qué perseguiría con más presupuesto

1. Las **11 subpáginas del PGC que quedan sin abrir** (esquizofrenia, bipolar,
   TEPT, TOC/Tourette, sustancias, suicidio, alimentarios, Alzheimer, CNV,
   genómica funcional, pedigree sequencing) y los nombres ya cribados sin ficha:
   Angelika Erhardt-Lehmann (Würzburg), Roseann Peterson, Elise Robinson
   (Harvard Chan), Manuel Mattheisen y Johanne Hagen Pettersen.
2. La vacante de **Cardiff que cierra el 17-sep** y el resto del portal, del que
   solo se ha visto una de tres páginas.
3. Confirmar el cargo y el correo de **Cormand** (L-0010) abriendo `sira.ub.edu`
   en navegador real, y la dirección institucional de **Tiemeier** antes de que
   escriba a nadie.
4. Abrir la noticia del **GAW 2027** en geneticepi.org para fijar el plazo de la
   convocatoria de ideas (E-0017 sigue UNVERIFIED por eso).
5. Juntas de **BGA e IGES**, y el resto de sociedades — ángulo (d) de la
   rotación, apenas tocado esta semana.
