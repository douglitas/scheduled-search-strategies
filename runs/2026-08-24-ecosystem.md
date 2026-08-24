# ecosystem — 2026-08-24

Primera pasada real de ecosystem (perfil ya definido). Las tres pestañas
propias estaban vacías, así que esto es una siembra: descubrimiento puro, sin
seguimiento (rama 4 sin nada que revisar). Buzón y source_inbox ya estaban sin
PENDING (los cerró positions el 2026-08-23), así que las tareas de backstop no
requirieron acción.

## Recuento (de `git diff --cached --stat`, solo altas, 0 borrados)

- groups: +11 filas (L-0001…L-0011)
- events: +10 filas (E-0001…E-0010)
- training: +6 filas (T-0001…T-0006)
- sources: +6 fuentes nuevas (SRC-0077…SRC-0082)
- subscriptions: +2 altas TODO (SUB-0005, SUB-0006)
- changelog: +5 apuntes
- action_now: +10 filas propias (1 ajena preservada)

## Lo tres que más merecen acción ya

1. **RELOJ VIVO — ASHG 2026, resúmenes late-breaking cierran el 2026-08-26**
   (E-0002, Fit 5). A ~2 días. Su artículo empírico de Nature Mental Health
   podría ir como póster late-breaking si actúa de inmediato; aun sin resumen,
   ASHG (Montréal, 20-24 oct) es la mejor sala para su línea 1. Early-bird de
   registro hasta 15-sep-2026. Viaje a Canadá + visado no-UE a tener en cuenta.
2. **QIMR Berghofer / grupo de Sarah Medland** (L-0002, Fit 5): la pista
   **cálida** más fuerte del conjunto — ya hizo estancia allí y tiene el paper
   de Nature Mental Health en revisión desde ese instituto, además de una
   miembro hispanohablante (Lucía Colodro Conde). Un correo referenciando la
   estancia y el paper pendiente parte con ventaja. Único pero: Australia =
   visado.
3. **International Statistical Genetics Workshop ("Boulder"), edición
   PRESENCIAL 2027** (T-0001, Fit 5, competencia LOW): su diana de formación,
   de lleno en su técnica nuclear. Beca ISCEP (Regeneron) puede cubrir gran
   parte. Tarifa/plazo 2027 aún sin publicar → SUB-0006 para no perder la
   ventana (~ene 2027).

Otros Fit 5 sembrados: CTG Lab (Posthuma, Ámsterdam, L-0001), Generation R
genética del sueño infantil (Kocevska, Rotterdam, L-0004 — el solape más raro
con su línea 3), SGDP/Statistical Genetics Unit (Lewis/Breen, KCL, L-0006),
WCPG 2026 (E-0001), BGA 2027 (E-0004).

## Correcciones de honestidad / verificación

- **Aarhus / Doug Speed (L-0003)**: el anuncio postdoc de Nature Careers que la
  subagente marcó "ABIERTO" tiene plazo **1-may-2026, que YA PASÓ** (hoy es
  2026-08-24). Es decir: ya NO es una plaza viva, es una pista para correo en
  frío (doug@qgg.au.dk, la línea de método sigue activa). El dato de la fecha
  está registrado tal cual en la fila; conviene que la dueña lo lea como
  cerrado. No entró en action_now (Fit 4 sin plazo vigente).
- **Max Planck Nijmegen (L-0011)**: convocatoria de genómica estadística
  "rodante desde 8-oct-2026" vista en un único tablón (BGA), sin abrir el
  anuncio → **UNVERIFIED**. Confirmar PI/depto exactos antes de actuar.
- Fiabilidad mixta en grupos: solo CTG, QIMR y el anuncio de Aarhus se
  abrieron directamente (VERIFIED). Cardiff, KCL/SGU, Erasmus/Kocevska,
  Grotzinger, Saxena, Estonian Biobank y Cormand se apoyan en fuentes
  secundarias (LIKELY): la semana que viene toca abrir sus homepages y sus
  páginas de vacantes para confirmar títulos actuales de los PI.

## Cerrado / pasado (registrado, no en action_now)

- Ediciones 2026 ya celebradas o con plazo cerrado: FENS Forum (jul 2026,
  bienal → próx. 2028), BGA Ámsterdam (jun 2026 → próx. 29-jun/2-jul 2027, sede
  y plazo TBA), ESHG 2026 (→ objetivo vivo es 2027, Rotterdam, plazo resúmenes
  4-feb-2027), IGES y ESRS/Sleep Europe (plazos de resúmenes de 2026 pasados,
  pero los eventos aún son futuros, oct 2026), WCPG 2026 (resúmenes + premio
  ECIP cerraron en mayo; el congreso, 29-sep/3-oct, sigue en pie para asistir).
- CAJAL Neurobiology of Sleep (T-0005): plazo 27-ago-2026 (a 3 días) + laboratorio
  húmedo fuera de su técnica → Fit 2, inviable. CSHL Genome-Scale Data (T-0006):
  edición 2026 pasada, alcance RNA-seq/ChIP fuera de su núcleo → Fit 2.

## No verificado / bloqueado

- ESRS "Sleep Europe" 2026 (E-0007): la página oficial de resúmenes devolvió
  HTTP 403 (un intento). Plazo late-breaking sin confirmar. Anotado en
  Source_Note; no re-descubrir la semana que viene.
- Cursos que NO se pudieron confirmar para 2026/27 y quedan para perseguir:
  el GWAS práctico de Wellcome (solo consta la edición sep-2024, T-0004
  UNVERIFIED), un curso práctico EMBO de genética estadística, una summer
  school ESRS de sueño, y un curso independiente PRSice/LDpred/analista PGC.

## Suscripciones pendientes (TODO, definición del prompt)

Todas las de la tabla siguen en TODO (owner_status.json está vacío, sin marcas
de la dueña): SUB-0001 (BOE), SUB-0002 (EURAXESS), SUB-0003 (SENC), SUB-0004
(ISCIII), y las dos de esta pasada SUB-0005 (ISPG/WCPG) y SUB-0006 (Boulder).
Las dos nuevas son del beat ecosystem y habilitan relojes que se pierden fácil.

## Qué perseguiría con más presupuesto la semana que viene

1. Abrir homepages y páginas de vacantes de los 7 grupos marcados LIKELY para
   subirlos a VERIFIED y detectar anuncios vivos.
2. Descargar la lista real de premiados ERC-2025-StG (el PDF salió pero no se
   parseó) → PIs nuevos con dinero fresco = contratación de baja competencia.
3. Perfilar a Wouter Peyrot (co-chair 2026 del PGC Cross-Disorder, VU
   Ámsterdam) como grupo nuevo.
4. Confirmar el anuncio de Max Planck Nijmegen (L-0011) y el calendario de
   cursos EMBO 2027 de genética estadística.
