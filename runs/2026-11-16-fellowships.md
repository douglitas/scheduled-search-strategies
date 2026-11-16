# fellowships — 2026-11-16

Las cinco ramas completas, sin incidencias de entrega y sin capacidades caídas.
El buzón de Gmail **no** se leyó aquí: lo lee la rutina `positions`, que corrió
ayer, 2026-11-15. `data/source_inbox.json` estaba vacío (`[]`) y
`data/inbox_triage.tsv` no tenía ninguna fila PENDIENTE, así que no había nada
que triar. `data/owner_status.json` sigue vacío (`{}`).

## Recuentos (de `git diff --stat HEAD~1`, no de memoria)

| fichero | filas antes → después | altas | líneas tocadas |
|---|---|---|---|
| `fellowships` | 95 → 105 | 10 | 47 |
| `watchlist_closed` | 30 → 30 | **0** | 17 |
| `action_now` | 62 → 62 | mías 6 (antes 6) | 4 (56 ajenas preservadas) |
| `sources` | 485 → 509 | 24 | — (solo apéndice) |
| `subscriptions` | 48 → 48 | **0** | — |
| `changelog` | 1574 → 1638 | 64 | — |

De las 25 fuentes propuestas, 24 entraron y 1 se descartó por duplicado de
URL+consulta (el tripwire REST de la SES ya estaba fichado).

### Tres arreglos míos al aplicar, y dos son errores propios que conviene contar

1. **Dos ramas entregaron como ALTA una fila que ya existía.** La rama 3 propuso
   el ECIP de la ISPG, que es **F-0038**, y la rama 1 propuso el Branco Weiss,
   que es **F-0078**. Retiré las dos altas y plegué sus hechos como
   actualizaciones de la fila existente. Sin ese cruce habría habido dos pares
   de filas duplicadas, y una de ellas es la de Fit 5 de la base.
2. **Mi redacción rompió el guardarraíl de `action_now` en los dos sentidos, y
   lo vi al verificar, no al escribir.** Al reescribir el `Fit_Rationale` de
   **F-0008 (EMBO)** borré sin darme cuenta la palabra que lo mantenía fuera de
   la lista corta, y se colaba otra vez: exactamente el fallo que el comentario
   de `rebuild_action_now.py` documenta del 2026-10-26. Y al redactar la
   elegibilidad de **F-0038** escribí «hace inelegible» para describir una regla
   que **a ella no la afecta**, y el guardarraíl, que es literal a propósito,
   lo expulsó de `action_now` siendo un Fit 5. Las dos filas están corregidas y
   `action_now` vuelve a ser el correcto. Lección para quien redacte: el token
   de inelegibilidad es una **señal de máquina**, no prosa; no usarlo salvo para
   afirmar que ella es inelegible.
3. **Sobrescribí ~27.000 caracteres de memoria acumulada y los restauré.** Mis
   actualizaciones sustituían `Notes`, `Eligibility_Key_Conditions`,
   `Next_Action` y `Source_Note` por versiones nuevas más cortas: 15.467
   caracteres en `fellowships` (16 filas) y 11.713 en `watchlist_closed` (15
   filas). `watchlist_closed.tsv` **encogió 12 KB conservando las 30 filas**, que
   es la señal. Restaurado todo como cola de auditoría marcada, con la regla
   explícita de que **manda la lectura del 2026-11-16** si contradice. No era
   pérdida de filas, pero sí de las verificaciones Tier 1 de semanas anteriores,
   que es de lo que vive esta base.
   Lo que **no** restauré, a propósito: la prosa que pasadas anteriores metían en
   la columna `Confidence`, que por contrato es un valor único
   (VERIFIED / LIKELY / UNVERIFIED). Ahí dejo el valor desnudo y el razonamiento
   en `Source_Note`. Es corrección de contrato, no pérdida.

## Las tres cosas que merece la pena hacer, y por qué

### 1. F-0094 (SIRS): el plazo no se ha movido, pero el TRABAJO es el doble de lo que la fila decía — 15 días

El encargo de la semana pasada queda **zanjado en Tier 1 y la respuesta es que
no hay plazo anterior oculto**: el formulario del premio va **embebido dentro
del envío del resumen**, así que el plazo de resúmenes no puede ser anterior al
del premio, y la única fecha en circulación (2026-12-01) coincide con él. La
urgencia no cambia; lo que cambia es el alcance. El entregable antes del
**2026-12-01 a las 23:59 CST (= 02-12 a las 06:59 en Madrid)** es un **resumen
científico de congreso** más declaración personal, CV y **una carta de apoyo de
una página** de supervisora, jefatura de residencia o equivalente. Esa carta es
la única dependencia externa: **pedirla esta semana**.

Y una pérdida concreta que hay que saber: **el servicio gratuito de revisión de
resúmenes para etapa temprana de la SIRS cerró el 2026-11-13**, tres días antes
de esta pasada. No hay ronda de feedback externo en este ciclo.

Lo que sostiene la fila sigue en pie y ahora es textual: las **tres vías**
elegibles (doctoranda de último año; posdoc; **residentes o fellows en formación
de especialidad**), que es la razón por la que no cuelga de la ETA de febrero de
2028, y que **no se fija ningún mínimo de publicaciones**. Congreso: Montreal,
10-14 de abril de 2027 — dentro de la residencia, hay que negociar el permiso, y
hace falta visado canadiense.

### 2. F-0019 (FENS/IBRO-PERC): la urgencia que esta base declaraba la semana pasada estaba sobredimensionada

Corrección que conviene hacer sin adornos. La semana pasada esta fila decía que
la acción más urgente era **darse de alta en la SENC antes del 01-12-2026**. La
relectura Tier 1 de `fens.org` dice dos cosas que lo desmontan:

- Son **tres vías alternativas** de membresía, y una **membresía individual de
  FENS satisface la regla por sí sola**. No hay dependencia del calendario de
  ninguna sociedad nacional.
- La página **no fija ninguna fecha límite de membresía**. El 01-12-2026 es
  cuando **abre la ronda**, no un plazo. El reloj real de la membresía es el
  **2027-04-15**.

Importa esta semana justamente porque **el sitio de la SENC está caído**: dos
ramas independientes vieron certificado TLS caducado en `senc.es` y HTTP 503 en
`www.senc.es`. La vía SENC es hoy inalcanzable y la vía individual de FENS la
sortea por completo. Lo que **sí** es camino crítico real: la **aceptación
escrita del laboratorio de acogida** más la recomendación del de origen, que hay
que empezar a mover en diciembre. 4.000 €, estancia de 4 semanas a 4 meses, y
sigue siendo lo único sustancial que puede solicitar **ya**, como doctoranda.

### 3. Dos filas suben a Fit 4 porque se resolvió su pregunta de ciudadanía, y las dos apuntan al mismo sitio

- **F-0016 (NHMRC Investigator Grant, EL1)**: 3 → 4. **No necesita ser
  australiana**: basta tener el visado de trabajo requerido **al aceptar** (no al
  solicitar) y estar basada en Australia, con hasta el 50% del periodo en el
  extranjero. La ventana EL se mide desde que **la tesis se aprueba**, «not the
  date of conferral», con fecha censal en el cierre, así que su primera ronda
  limpia es la que cierra **hacia julio de 2028**. Salario EL1 A$89.523 más un
  RSP que sube de A$50.000 a A$75.000.
- **F-0092 (IFCC PEP)**: 3 → 4, y con el mecanismo por fin claro. **No exige
  doctorado**, así que es la fila más inmune a la incertidumbre de la defensa.

Convergencia que ninguna rama podía ver sola: **las dos cuelgan de una
conversación de acogida que empieza por el mismo contacto de QIMR Berghofer o
por un laboratorio clínico**, y las dos necesitan meses de antelación.

## Correcciones a hechos que esta base daba por establecidos

- **F-0073 (JIGENT): lo que se registró la semana pasada era incorrecto.** La
  ventana del 28-09 al 27-10-2026 **no era solo de EIGENT**: la misma Orden de
  bases (DOGV del 25/09/2026) llevaba **DEGENT, EIGENT y JIGENT juntas**, así que
  la línea júnior del ejercicio 2027 abrió y cerró en esas fechas y **no hay un
  JIGENT 2027 pendiente**. El siguiente es el del ejercicio 2028. Y el bloqueo
  real no es de fecha: **exige contrato previo en una institución valenciana**,
  al que no tiene vía.
- **F-0026 y F-0081 (ESRS): la mala atribución era NUESTRA y queda resuelta.** La
  ventana «1 de diciembre – 31 de enero» pertenece al **examen de certificación
  en medicina del sueño**, cuyo ciclo de 2026 corrió del 01-12-2025 al
  31-01-2026, **no a las ayudas**. La cifra de las ayudas es el **15 de febrero**,
  releída de forma independiente. **Dejo los plazos en 2027-01-31 a propósito**,
  como margen: mover una fecha más tarde es la única dirección que puede provocar
  una pérdida. Hay que leer 2027-02-15 como la expectativa real.
  Y el desenredo que importa: **F-0087 es la excepción**, porque es la ayuda del
  **examen** y ahí el 31 de enero probablemente **sí** es correcto. **Las tres
  filas dejan de ser un único problema de fecha.**
- **F-0078 (Branco Weiss): 3 → 2**, y por motivo sustantivo nuevo, no por
  impresión. Ya se sabía que el doctorado debe estar en mano al 15 de enero. Lo
  que se añade es la **segunda puerta**: financia proyectos que **se apartan** de
  la investigación mainstream respaldados por un historial sobresaliente. Un
  programa de GWAS/PRS mainstream sin publicaciones destacadas no da ninguna de
  las dos. No se resuelve esperando.
- **F-0008 (EMBO): dos hechos se movieron en contra y uno a favor.** El corte del
  2027-01-22 es ahora **plazo duro con hora de reloj (14:00 CET)**, no una fecha
  de evaluación continua. A favor, y es palanca de verdad: **un preprint revisado
  de primera autora cuenta como equivalente a una publicación**, así que el
  artículo de *Nature Mental Health* podría no necesitar aceptación formal.
  **Zanjar la definición de «refereed preprint» antes de enviar nada**: con un
  único intento vitalicio, esa pregunta vale más que el plazo.
- **F-0018 (ERC): el encargo se cierra y sube a VERIFIED.** El 0-10 y la fecha de
  referencia del 1 de enero del año de convocatoria quedan confirmados en nodos
  de `erc.europa.eu` independientes de la página del esquema (tramo exacto de
  2027: 01-01-2017 a 31-12-2026). Su primera competición elegible sigue siendo
  **ERC-2029-STG**. **Hecho nuevo que corta en contra**: las extensiones, la de
  formación clínica incluida, solo cubren circunstancias **posteriores a la
  defensa**, y su residencia termina **antes** — así que esa extensión **nunca**
  le servirá. Con la ventana empezando en 0, tampoco la necesita.
- **F-0014 / F-0015 (NIH): la pregunta de ciudadanía queda cerrada por los dos
  lados y textualmente.** La F32 la veta («By the time of award, the individual
  must be a citizen…»); el K99/R00 **no** («There is no citizenship requirement
  for K99 applicants»); y la serie K mentorizada del NIMH (K01/K08/K23) lleva la
  **misma** barrera que la F32 — fichada como F-0097 para no volver a buscarla.
  Resultado del barrido del NIMH, nunca hecho antes: **el K99/R00 es el único
  mecanismo del NIH abierto a ella**. Restricción nueva: las instituciones
  extranjeras no pueden solicitar, así que **el K99 no sirve para entrar en
  EE.UU., solo para ascender una vez dentro**.

## Altas (10)

| ID | Qué es | Fit |
|---|---|---|
| F-0096 | **Contratos Juan Rodés (ISCIII)** — el peldaño inmediatamente por encima de Río Hortega, faltaba entero | 4 |
| F-0105 | **SOBP Travel Fellowship — Predoctoral Scholars** — dice por escrito «do not need to be published» | 4 |
| F-0103 | **EMBL EIPOD-LinC** — movilidad **institucional**, no por país: inmune a los meses sin fijar | 4 |
| F-0101 | **SRS Outstanding Early Investigator Award** — traspaso entre ramas; inelegible y por qué | 1 |
| F-0099 | **Nanit / SRSF** — primera pista en 4 semanas para la línea (3); UNVERIFIED a propósito | 3 |
| F-0104 | **Courses with ESHG Fellowships** — la misma compra de membresía 2027 que F-0023 | 3 |
| F-0098 | **ARC DECRA** (Australia) | 2 |
| F-0097 | **NIH K01/K08/K23** — barrera de ciudadanía, cerrada | 1 |
| F-0100 | **Simons Fellows-to-Faculty** | 1 |
| F-0102 | **ESHG Observership Programme** — restringida a países en desarrollo | 1 |

Cuatro de las diez son Fit 1-2 **a propósito**: existen para que nadie vuelva a
gastar presupuesto en ellas.

## El hallazgo más infravalorado de la semana: F-0105

La **SOBP Predoctoral Scholars** es, en relación coste-beneficio, la mejor fila
nueva. Es la única de toda la base que combina las cuatro cosas: **sin tope de
edad** (su año de nacimiento no la bloquea), **sin requisito de membresía**
(ni SENC, ni ESHG, ni AEGH), **sin requisito de publicación** —dicho por
escrito— y abierta por **región Pan-Europa de la IBRO**, así que la Universidad
de Murcia califica. Y solo es suya **mientras siga matriculada**, es decir
**hasta la defensa**. Junto con F-0089, que sube su elegibilidad por **dos** vías
(diez años desde el título terminal **o** desde la residencia), la SOBP se
convierte en dos tiros simultáneos por vías distintas en el mismo congreso.

## Lo que no se pudo verificar o alcanzar

- **`senc.es`: bloqueo NUEVO y doble.** Certificado TLS **caducado** (curl error
  60) y HTTP **503** en `www.senc.es`. La semana pasada estaba vivo. **W-0019
  queda UNVERIFIED esta semana, que no es lo mismo que «nada publicado»**, y
  F-0039, F-0040 y F-0065 no se tocan.
- **`nhmrc.gov.au`: HTTP 503** en la página y en el PDF oficial de elegibilidad.
  Las bases se leyeron de un **espejo literal** (`melanoma.org.au`): el contenido
  es del NHMRC, el alojamiento no. Las fechas de la próxima ronda son
  **estimación mía, no fuente**.
- **`esrs.eu`: 403 Cloudflare**, un solo intento. Se confirma el método: **la
  portada lleva plazos vivos y las fichas no**.
- **`ifcc.org`** sirve solo navegación, sin cuerpo. El rodeo que funcionó es una
  **sociedad nacional miembro** (`labmed.org.uk`), que republica la convocatoria
  íntegra **y su propio corte interno anterior**.
- **`sleepresearchsociety.org/foundation/grants/` → 404.** La superficie viva es
  el **índice de categoría**. Corrección de ruta que arregla F-0025/F-0051/F-0075.
- **Bloqueos nuevos para el inventario:** `bga.org/awards/` **403** (F-0058 y
  F-0083 siguen UNVERIFIED, y conviene dudar del propio nombre de F-0083);
  `niaid.nih.gov` **403**; `hfsp.org/funding-opportunities/hfsp-postdoctoral-fellowships`
  **404**; `in.umh.es` resuelve pero es una **página marcador de alojamiento**, no
  el instituto; el portal del topic del Portal F&T y `sirs.societyconference.com`
  son **cáscaras de JavaScript** sin texto extraíble.
- **SEMEDLAB: la sección de becas NO ha aterrizado.** Los mismos tres JPEG
  `GEMMA-FOTOS-PARA-BECAS` del 04-11 y **nada nuevo en doce días**. La pista se
  mantiene; no ha salido. Nota de eficiencia: pasar `&_fields=…` o el endpoint
  devuelve ~600 KB y se trunca.
- **El tripwire de la SES volvió a NO saltar**: `modified` sigue en
  `2025-11-03T11:53:19`, un año y 13 días. Y ahora con refuerzo: el sitio **sí**
  se mantiene alrededor (`pediatria` 10-11, `insomnio` 15-10), así que es un
  negativo real y no un sitio muerto. Resuelve W-0012, W-0017 y W-0026 en **una**
  llamada. Estamos en la **segunda mitad** de la franja superviviente.
- **Previsiones nuestras que siguen fallando, y van dos semanas:** la reapertura
  de la SRSF «desde ~noviembre de 2026» **no se ha producido** (F-0075, W-0027).
- **La AES 2027 no existe**, con evidencia mejor que la de sondas: la página de la
  AES **sí** carga (477 KB) y contiene **cero** apariciones de «2027» fuera del
  marco de Líneas Estratégicas. **Calibración que cambia dónde mirar**: el
  extracto de la AES 2026 salió en el **BOE el 20-12-2025** (resolución del 19-12)
  con plazo del 10-02 al 05-03-2026. **Esto se caza en el BOE de finales de
  diciembre, no en `isciii.es` en febrero.**
- **No se buscó Alemania ni Reino Unido** en la rama 2, dicho sin adornos: el
  presupuesto se fue en NIH, NHMRC e ISCIII. Y **F-0061 (Pfizer) y F-0082 (ASHG)**
  no se tocaron a propósito (muro de socios confirmado; exige obra publicada).

## Conflictos que se reportan sin resolver

1. **MSCA (F-0009): el `(TBC)` NO ha caído.** El sitio del financiador sigue
   publicando «7 April 2027 … (TBC)» y «8 September 2027 … (TBC)». Y nunca serán
   firmes: el Work Programme permite mover la apertura ±1 mes y retrasar el plazo
   hasta 2 meses. El presupuesto del sitio (459 M€) **no coincide** con ninguna
   cifra de agregador: ignorar los presupuestos de agregador.
2. **Ruta del ECIP (F-0038)**: una rama **leyó con éxito** `ispg.net/ecip-program/`
   y otra informa de que **da 404** y que la ruta viva es
   `/annual-world-congress/ecip-program`, el mismo día. No elijo: conservo la URL
   de la fila y fichо la alternativa. Lo que **sí** está establecido es que
   `/early-career/` y `/early-career-investigator-program/` dan 404.
3. **ECNP Rising Star (F-0095)**: la ambigüedad del título **se resuelve en parte
   y el bloqueo se mueve**. Ninguna de las dos páginas Tier 1 ancla la ventana de
   2-7 años a este premio; la que lo gobierna da **tope de 35 años medido el
   primer día del congreso** más residencia europea. En las dos lecturas manda el
   tope de edad, así que **la fila está bloqueada por su año de nacimiento, no por
   la redacción de la ECNP**. Sigue abierto el «up to two» frente a «up to three».
4. **W-0011 (Premio del Instituto de Neurociencias)**: **bajada de LIKELY a
   UNVERIFIED**, y es honestidad, no hallazgo. Los únicos premios del IN que se
   identificaron son **bienales** (Remedios Caro Almela, Alberto Sols), lo que
   empujaría la siguiente edición a **2028** y haría errónea la ventana de
   mayo-junio de 2027. Hay que identificar **qué premio nombra la fila**.
5. Siguen abiertos y sin tocar: el cierre de resúmenes de la ECNP 2026 (5 vs 7 de
   mayo) y la NIHR Future Leader cohorte 2 (enero vs junio de 2027).

## Filas que ella ya hubiera leído y cuyos hechos han cambiado

`owner_status.json` sigue vacío (`{}`), así que **no hay ninguna marca suya** y
ningún modelo mental que se haya quedado obsoleto por debajo. El
`Owner_Status = NEW` de la mayoría de filas es el valor por omisión, no una
lectura. Verificado además que **ninguna fila preexistente cambió de
`Owner_Status`** en esta pasada.

Dicho eso, **si leyó el informe de la semana pasada, dos consejos ya no valen**:
que había que darse de alta en la SENC antes del 01-12 (basta una membresía
individual de FENS, y no hay plazo de membresía), y que el plazo del 28-10 de
F-0073 era solo de EIGENT.

## Suscripciones pendientes

**48 de 48 en TODO.** **Cero altas, por segunda semana consecutiva, y hay que
decirlo en vez de disimularlo.** El encargo de la semana pasada era un canal de
avisos de la SIRS: la rama 3 lo buscó en Tier 1 y **la respuesta es que NO
existe** — la portada no tiene formulario de alta, solo
`info@schizophreniaresearchsociety.org` y redes. El encargo queda **cerrado en
negativo**, que es mejor que seguir abierto.
Las otras ramas miraron y **ninguna vio una URL exacta de alta, y no se inventa
ninguna**. Candidatas concretas para la semana que viene, ya nombradas: el
«Suscríbete a las novedades de convocatorias del SGI» de la UV y el news tracker
semanal del NHMRC. Las de prioridad alta que siguen esperándola son SUB-0040
(HFSP), SUB-0042 (newsletter de la ESRS — única vía fiable con el dominio tras
Cloudflare), SUB-0036 (alta en la ESRS) y SUB-0022 (SEMEDLAB).

## Los datos que solo ella puede dar

1. **Su año de nacimiento**, por tercera semana. Hoy bloquea F-0043, F-0090 (tope
   de 35 el 25-09-2027) y **F-0095**, cuyo bloqueo se ha movido justo a este dato.
   Las excepciones afortunadas son el SIRS (*under 40 by April 2027*) y, mejor
   aún, **las dos filas de la SOBP, que no tienen tope de edad ninguno**.
2. **Los meses exactos de las estancias en QIMR Berghofer y Japón**, por **décima**
   semana. Sin ellos, MSCA no pasa de LIKELY en movilidad — y para una acogida
   **australiana** es la única regla que podría descalificarla de verdad.
3. **Dos altas de sociedad que son hoy la acción de mejor relación
   coste-beneficio**, y ninguna la puede hacer una rutina: **membresía individual
   de FENS** (desbloquea F-0019 sola, sin depender de la SENC caída) y
   **membresía de la ESRS**, que es **precondición en el momento de solicitar** de
   F-0081 — condición nueva de esta semana. La **AEGH antes de que acabe 2026**
   sigue en pie (el reloj de dos años solo arranca con el alta), y la **ESHG 2027**
   ahora rinde en **dos** filas, F-0023 y F-0104, con una sola compra.

## La regla de tamaño sigue incumplida, y esta semana la empeoré yo

`fellowships.tsv` está en **415 KB** (353 hace una semana) y
`watchlist_closed.tsv` en **74 KB** (63). Parte del salto es mío: la restauración
de la cola de auditoría añadió ~27.000 caracteres a propósito, y volvería a
hacerlo —perder verificaciones Tier 1 es peor que un fichero grande—, pero
conviene que conste de dónde viene. Además `changelog` 555 KB, `sources` 414 KB,
`groups` 411 KB, `postdocs` 239 KB, `jobs` 118 KB y `events` 80 KB. **El corte lo
hace ella**: partir un fichero obliga a cambiar `build_page.py` y
`build_xlsx.py` en el mismo commit, y eso no es trabajo para el final de una
pasada desatendida.

## Qué perseguiría la semana que viene

1. **`senc.es` en cuanto arregle el certificado** — es la única fila a la que
   debo una respuesta sin verificar, y detrás hay una fecha viva.
2. **La definición de «refereed preprint» de EMBO**, que es la pregunta que de
   verdad decide si el corte del 22-01-2027 es alcanzable con un único intento
   vitalicio.
3. **El tripwire de la SES, semanal**, mientras dure la franja; y **desde primeros
   de diciembre, los extractos diarios del BOE** para la AES 2027, que es donde
   aparecerá antes que en `isciii.es`.
4. **Abrir la entrada de Nanit** y resolver F-0099 arriba o abajo: es la única
   pista en cuatro semanas para la línea (3).
5. **La portada de `esrs.eu` en la primera semana de diciembre** para fijar
   31-01 frente a 15-02, y el PDF de 2023 del Rita Levi-Montalcini para saber si
   F-0039 exige resumen de primera autora.
6. **Alemania y Reino Unido**, que no recibieron presupuesto esta pasada:
   programas nacionales de clinician-scientist fuera del carril de fundaciones,
   que es donde está su ventaja más rara.
7. **Identificar qué premio es W-0011** antes de dar crédito a cualquier fecha, y
   **una suscripción de verdad**, que lleva dos semanas a cero.

Cruce para `ecosystem`, no de mi rutina: el **AASM Foundation Young Investigators
Research Forum 2027** (arranque virtual en marzo, presencial 11-13 de abril en
Chicago, resolución antes del 15-01-2027) es **programa de formación con viaje y
alojamiento, no ayuda**, y además **choca con la semana del congreso de la SIRS**.
