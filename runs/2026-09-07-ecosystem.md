# ecosystem — 2026-09-07

Primera pasada de SEGUIMIENTO del beat: el 2026-08-24 se sembraron las tres
pestañas y desde entonces **la ranura del 2026-08-31 no se ejecutó**, así que
esto cubre dos semanas de reloj, no una. Las cuatro ramas corrieron dentro de
presupuesto (23, 24, 24 y 30 llamadas).

Tareas de backstop: **nada que hacer**. `data/source_inbox.json` está vacío
(`[]`) y `data/inbox_triage.tsv` no tiene ninguna fila PENDING — positions leyó
el buzón esta mañana y no trajo nada relevante. La semana cierra limpia.

## Recuento (de `git diff HEAD~1 --stat`, no de memoria)

| fichero | altas | modificadas |
|---|---|---|
| groups | +8 (L-0012…L-0019) | 11 (las once previas, una a una) |
| events | +5 (E-0011…E-0015) | 6 (E-0001, E-0002, E-0004, E-0007, E-0008, E-0009) |
| training | +4 (T-0007…T-0010) | 5 (T-0001…T-0005) |
| sources | +16 (SRC-0107…SRC-0122) | 14 con `Last_Checked` al día |
| subscriptions | +2 (SUB-0013, SUB-0014) | — |
| changelog | +39 apuntes | — |
| **action_now** | **19 filas mías** (antes 10) | 3 ajenas preservadas |

Total: 128 inserciones, 45 borrados — los borrados son reescrituras de fila en
sitio, ningún dato perdido (recuentos verificados fila a fila por `apply_rows`).

## Los tres que más merecen acción ya

1. **ASHG 2026 — la inscripción anticipada cierra el 15-sep a las 17:00 ET, a 8
   días** (E-0002, Fit 5). El plazo de resúmenes ya pasó, así que iría como
   asistente. El dato que ahorra dinero: cuota de no socia *trainee* 775 USD
   (~715 €) frente a 435 USD (~400 €) siendo socia *student-trainee* — **hacerse
   socia antes de inscribirse la baja casi a la mitad**. Después del 15-sep solo
   queda tarifa late/onsite. Montréal, 20-24 oct; Canadá = visado.
2. **WCPG 2026 empieza en 22 días (29-sep, Glasgow) y la inscripción sigue
   ABIERTA** (E-0001, Fit 5). Es la sala central de su línea 2. Sin fecha de
   cierre publicada y sin opción virtual anunciada; las cuotas quedaron
   **UNVERIFIED** porque el portal carga por JavaScript e `ispg.net/registration`
   todavía muestra el WCPG 2022 de Florencia. Acción: registrarse ya y escribir a
   info@ispg.net por la tarifa Student/Post-Doc. Las becas ECIP cerraron el
   14-may-2026.
3. **Wouter Peyrot** (L-0012, Fit 5, VERIFIED): ERC Starting Grant de 1,5 M€
   (*PersonalRiskProfile*), co-chair 2026 del Cross-Disorder del PGC y
   **psiquiatra que hace genética estadística** — el mismo itinerario MD→genética
   que ella, con dinero fresco y plantilla por construir. Es la diana de correo
   en frío más limpia de la pasada. Quedaba pendiente de la semana anterior y ya
   está fichado.

Detrás, dos Fit 5 más de la misma cosecha: **Kelli Lehto** (L-0013, ERC StG
*AT-TENSION*, Tartu — TDAH adulto sobre cinco biobancos con fenotipado a partir
de historia clínica, donde su Medicina de Laboratorio es una ventaja y no un
adorno) y **Christel Middeldorp** (L-0014, Amsterdam UMC — MD PhD, el único
puente real entre su línea 2 y su línea 3).

## Correcciones sobre filas que la dueña ya había leído

Cuatro cosas que la tabla daba por buenas y no lo eran. Si ya se había hecho un
modelo mental de estas filas, ha quedado desactualizado:

- **T-0001, taller de Boulder — la beca ISCEP NO le sirve.** Exige ser nacional
  Y residente de un país de renta baja o media-baja. El curso (1-5 mar 2027,
  fechas ya confirmadas) es **íntegramente a su cargo**. El Fit sigue siendo 5,
  pero el supuesto de "Regeneron puede cubrir gran parte" que llevaba el informe
  del 2026-08-24 era falso.
- **L-0004, Kocevska — probablemente no es jefa de grupo.** Todo apunta a que es
  postdoc en el Netherlands Institute for Neuroscience (grupo Van Someren), no
  PI en Erasmus MC. Si es así, **no puede contratar**. Su perfil en erasmusmc.nl
  da 404 y no hay ficha en nin.nl → bajada a UNVERIFIED y vía de contacto
  reescrita como puerta de entrada, no como destino. Sigue en action_now, pero
  la acción ahora es *verificar antes de escribir*.
- **L-0011, Max Planck Nijmegen — la plaza existe y el PI no era quien creíamos.**
  "Postdoctoral Research Scientist in Statistical Genomics/Genetic Epidemiology",
  3 años, revisión rodante desde el 8-oct-2026. La PI es **Beate St Pourcain**
  (grupo Population Genetics of Human Communication), no Simon Fisher. Los
  fenotipos reales — comportamiento social desde la primera infancia,
  trayectorias de salud mental, consorcio EAGLE de cohortes de nacimiento —
  encajan mejor de lo que suponía la ficha: **Fit subido de 3 a 4**. El problema
  es el calendario, no el tema: inicio 1-dic-2026 "negociable" contra su
  disponibilidad de feb-2028. Merece un correo antes del 8-oct preguntando hasta
  dónde llega ese "negociable".
- **E-0007, Sleep Europe 2026 es en Maastricht, no en Ámsterdam** (y tanto el
  plazo ordinario como el late-breaking están cerrados).

Además: URLs rotas (404) en **L-0007 (Grotzinger)** y **L-0010 (Cormand)**;
el plazo de **L-0003 (Aarhus)** sigue caducado y qgg.au.dk/en/vacancies da 404,
pero aparece un dato nuevo — la plaza la financiaba una ERC Consolidator de Doug
Speed, así que es probable que haya más rondas.

**Aviso que conviene resolver antes de invertir esfuerzo:** la única financiación
postdoctoral visible en el IBG de Boulder son becas NIH T32, que suelen exigir
ciudadanía o residencia permanente estadounidense. Si se confirma, esa vía le
queda cerrada y solo le sirve un contrato con fondos de proyecto (afecta a
L-0007 y al entorno de T-0001).

## Verificación

- Subidas a VERIFIED abriendo la Tier 1: L-0006 (KCL/SGU), L-0008 (Saxena Lab),
  L-0009 (Tartu) y L-0011 (Max Planck). Reconfirmadas L-0001 (CTG) y L-0002
  (QIMR). De los 8 grupos nuevos, 6 son VERIFIED y 2 LIKELY (L-0018 Uppsala,
  L-0019 Sánchez-Roige).
- **Solo una plaza viva en toda la tabla de grupos**: la de Max Planck (L-0011).

## Cerrado, pasado o descartado

- **T-0005 CAJAL Neurobiology of Sleep: CLOSED.** Edición 2026 (19 nov-8 dic),
  4.500 €, sin edición 2027 anunciada.
- **SfN 2026** (E-0009, Fit 2): el plazo del 15-sep es solo *late-breaking*, exige
  ser socia y no admite prórroga; el ordinario fue el 10-jun-2026. Con Fit 2, lo
  sensato es dejarlo pasar — se registra para no volver a mirarlo.
- Cerrado en negativo, para no repetir la búsqueda: **el PGC no tiene programa de
  formación de analistas con convocatoria** (solo un video-libro gratuito); el
  taller de PRS del King's es una página archivada de 2019; y **no hay curso EMBO
  de genética estadística con convocatoria 2027**.
- **T-0004 Wellcome**: corregido un error del informe anterior — sí hubo edición
  el 2025-09-01, pero no hay convocatoria 2026 ni 2027. Sigue UNVERIFIED; revisar
  en enero.

## No verificado o bloqueado

- Cuotas del WCPG 2026 (portal JavaScript); plazos de resúmenes de SLEEP 2027,
  SOBP 2027 (aún sin abrir), IGES 2027 y ASHG 2027; sede de la Jornada AEGH 2027.
- **WCPG 2027 no está anunciado todavía** por la ISPG: volver a mirar a mediados
  de octubre, después de Glasgow.
- Conflicto de fechas sin resolver en **SLEEP 2027** (E-0008): aasm.org da 6-9 jun
  2027 y la ficha tenía 5-jun. Registrado como conflicto, no elegido en silencio.
- Bloqueos de acceso automático (no re-descubrir, están anotados en `sources`):
  **esrs.eu** y las páginas del centro de **Cardiff** devuelven 403 (dos rutas
  distintas probadas); del portal de vacantes de Cardiff solo se vio la primera
  de tres páginas. **Wiley** devolvió 403 al comprobar la autoría del grupo de
  Uppsala (L-0018). Los PDF oficiales de premiados del ERC **no se leen con el
  lector automático**: hay que descargarlos y extraer el texto en local — así
  salieron Lehto y Palamara, y así habrá que hacerlo cada vez.
- No se abrió el portal de selección de QIMR (queda fichado como SRC nuevo); a
  L-0010 (Cormand) no se llegó más allá de detectar la URL rota.

## Suscripciones pendientes

Todas siguen en TODO: `owner_status.json` está vacío, sin ninguna marca suya, así
que las 14 filas cuentan como pendientes por la definición del prompt
(SUB-0001…SUB-0014).

De esta pasada: **SUB-0014 World Sleep Society** (avisos de congreso; el
formulario de alta no se llegó a verificar) y **SUB-0013 ISPG**, que resultó ser
**duplicada de SUB-0005** — misma sociedad, otra URL, así que la deduplicación
por `URL_to_subscribe` no la detectó. La fila se conserva (el fichero es de solo
apéndice) con una nota que apunta a SUB-0005 como canónica: **darse de alta una
sola vez**.

El tope de 2 por pasada dejó fuera la que más urge: **el registro de interés de
los cursos cortos de Bristol** (abre el **2026-09-23**, reservas el **2026-10-07 a
mediodía**). No se pierde nada por ello — las fechas ya están en el `Next_Action`
de T-0002 y T-0003, ambas en action_now —, pero es la primera candidata a
suscripción de la semana que viene.

## Qué perseguiría con más presupuesto

1. Las **17 subpáginas de working groups del PGC**: la página índice lista los
   grupos pero no publica los chairs, y ahí está el mapa directo de quién dirige
   hoy el GWAS psiquiátrico. Es el hilo más rentable que quedó sin tirar.
2. Confirmar el cargo real de **Kocevska** (L-0004) y el PI sénior de la línea de
   sueño infantil antes de que escriba a nadie.
3. Confirmar si la financiación postdoc del **IBG de Boulder** se limita a T32
   (y, por tanto, si esa puerta está cerrada para una no estadounidense).
4. Juntas de **BGA e IGES**, convocatorias **NHMRC/MRFF** australianas y la
   **Consolidación Investigadora de la AEI**, ninguna tocada esta semana.
5. Grupo de **Neuropsychiatric genomics de Tartu**, que no constaba y es mejor
   diana para su línea 2 que Mägi solo.
