# fellowships — 2026-11-09

Las cinco ramas completas, sin incidencias de entrega y sin capacidades caídas.
El buzón de Gmail **no** se leyó aquí: lo lee la rutina `positions`, que corrió
ayer, 2026-11-08. `data/source_inbox.json` estaba vacío (`[]`), así que no había
nada que triar.

## Recuentos (de `git diff --stat HEAD~1`, no de memoria)

| fichero | filas antes → después | altas | modificadas |
|---|---|---|---|
| `fellowships` | 91 → 95 | 4 | 37 |
| `watchlist_closed` | 29 → 30 | 1 | 12 |
| `action_now` | 52 → 54 | mías 6 (antes 4) | 48 ajenas preservadas |
| `sources` | 449 → 457 | 8 | — (append-only) |
| `subscriptions` | 45 → 45 | **0** | — (append-only) |
| `changelog` | 1418 → 1472 | 54 | — (append-only) |

Las 8 fuentes propuestas eran URL o consulta nuevas, comprobadas contra las 449
existentes. **Cero suscripciones nuevas, y conviene decirlo en vez de
disimularlo:** la regla pide crecer una o dos por pasada. La rama 2 buscó y
declaró explícitamente que no vio ninguna que mereciera el cupo; las demás no
propusieron. La candidata obvia sería un canal de avisos de la SIRS, financiador
que entra hoy en la base, pero ninguna rama verificó una URL de alta y **no se
inventa una URL**. Encargo para la semana que viene.

### Tres arreglos que hice yo al aplicar, y que conviene saber

1. La rama 3 entregó como ALTA una fila que agrupaba la cartera de la BBRF
   distinta de la Young Investigator. **Era duplicado de F-0032 y F-0033**, ya
   leídas en Tier 1 el 2026-11-02 con los mismos hallazgos, incluido el mismo
   conflicto del botón «APPLY NOW». Retiré el alta y plegué en `Source_Note` de
   F-0032 la única parte genuinamente nueva: **los premios de la BBRF no son
   solicitables** (Klerman y Freedman se reservan a antiguas becarias YI; los
   Outstanding Achievement, el Pardes y los Productive Lives van por
   nominación). Eso cierra el encargo de no volver a recorrer esa cartera.
2. Las ramas 3 y 5 comprobaron F-0075 por separado y **coincidieron en el
   hecho**; dejé la versión de la rama 3, que es la que registra el texto que
   cambia, y descarté el toque redundante de la 5. Una fila, una actualización.
3. La rama 2 traía una columna de la watchlist (`Expected_Reopen`, vacía) en una
   actualización de `fellowships`. Retirada: habría abortado el aplicador.

## Las tres cosas que merece la pena hacer, y por qué

### 1. SIRS Early Career Award — plazo 2026-12-01, a 22 días (F-0094, alta)

El hallazgo de la semana, y entra en `action_now` en el **puesto 2**. Premio de
la Schizophrenia International Research Society, ABIERTO, leído en Tier 1.
Repite exactamente la estructura que hace sólida la fila de la ESHG: **es
elegible por dos vías independientes de la ETA de su defensa** — «último año del
doctorado» y, por separado, «residentes o fellows en formación especializada» —
así que no cuelga de febrero de 2028, que es lo que fragiliza media base. **No
exige publicaciones aceptadas**, lo cual importa mucho cuando sus dos
manuscritos siguen en revisión. Y su tope de edad (*under 40 by April 2027*) es
el único de toda la base que casi con certeza cumple sin saber su año de
nacimiento. Fit 4, esfuerzo S.

El coste real no es el papeleo: es el **reencuadre**. El resumen tiene que caer
en el espectro psicosis/esquizofrenia, no en salud mental genérica. Con la línea
de GWAS/PRS de trastornos psiquiátricos es un giro de encuadre, no de
investigación. Dominio nuevo: no había ninguna fuente de la SIRS entre las 449.

### 2. Tres altas de socia, y una de ellas vence el 1 de diciembre

Son las acciones de mejor relación coste-beneficio del radar y **ninguna la
puede hacer una rutina**:

- **SENC antes del 01-12-2026** — tres semanas. Ese día abre la ronda del
  FENS/IBRO-PERC Exchange (F-0019, plazo 2027-04-15), la única ayuda de peso
  para la que es elegible **ya, como doctoranda**. La rama 5 confirma que el
  sitio de la SENC está activo (subidas del 2026-11-05) y que el calendario de
  travel grants de 2027 se espera a finales de diciembre.
- **ESHG con validez 2027** — ahora con la redacción verbatim: *«You must be an
  ESHG member for 2027»*, y es necesaria **para disfrutar** la ayuda, no para
  pedirla. F-0023 está hoy en `action_now` (puesto 4, 87 días), como se anticipó
  la semana pasada.
- **AEGH antes de que acabe 2026** — el reloj de dos años de antigüedad sólo
  empieza a correr con el alta, y es lo que hoy la deja fuera de F-0041, F-0042
  y F-0043. F-0064 cierra el 15-11 y queda **descartada con dos
  inelegibilidades, no una**: además de la antigüedad, exige certificado de
  aceptación de comunicación en el congreso de Granada 2026, al que no fue.

### 3. Una sola conversación de acogida en el Reino Unido sirve para dos filas

Convergencia que emerge al cruzar dos ramas y que no estaba escrita en ninguna
fila: **F-0084 (MRC Clinician Scientist) y F-0012 (Wellcome Early-Career)
cuelgan hoy de la misma y única condición** — que una organización británica la
emplee. Wellcome cerró su cambio de elegibilidad geográfica el 29-10-2026 y las
reglas nuevas, leídas en Tier 1, dejan la acogida sólo en el Reino Unido y en
países de renta baja y media de África y Asia del Sur/Sudeste: **Irlanda ha
caído y España nunca estuvo**. El Fit 4 se sostiene, pero pende de ese hilo.

Y el MRC se concreta: las tres ventanas de 2027 están etiquetadas una por una
como *«Future round open for applications»*, o sea que son ventanas de
**presentación y no rangos de inicio** — eso cierra la ambigüedad que quedó en
LIKELY la semana pasada. **Su ronda es la que abre el 09-06-2027 y cierra el
01-09-2027**; se retira el 04-09 que era conjetura. El patrón trianual deja de
ser inferencia nuestra: la propia página lo nombra. La ronda que cierra el
2027-01-13 sigue en `action_now` con razón, porque lo urgente no es solicitar
sino **preguntar y abrir acogida**, y los departamentos británicos piden de 6 a
12 meses. El correo a `fellows@mrc.ukri.org` sigue siendo la acción de más valor.

## El cambio de regla que reescribe una decisión estratégica

**F-0018, ERC Starting Grant: la ventana ya no es de 2 a 7 años post-doctorado,
sino de «more than 0 and up to 10»**, contados a 1 de enero del año de
convocatoria. Consecuencias, y son grandes:

- Su primera convocatoria elegible **se adelanta del otoño de 2030 al otoño de
  2028** (año de convocatoria 2029); la última se va a 2038.
- **Queda anulado el razonamiento de la pasada anterior.** Se dijo que adelantar
  la defensa a enero de 2028 ganaría un año entero de ventana, porque el corte
  de los 2 años caía el 01-01-2028. Ese corte **ya no existe**, así que mover la
  defensa no gana nada por esta vía. Si ese dato hubiera entrado en una decisión
  de calendario de tesis, hay que deshacerlo.
- Fit 2 → 3, por hecho nuevo y no por impresión.

Honestidad sobre la confianza: el 0-10 se leyó en la página oficial del StG,
pero `ERC_Work_Programme_2027.pdf` **dio HTTP 403** y la fecha de referencia
viene de búsqueda restringida al dominio. La fila queda **LIKELY, no VERIFIED**,
y confirmarlo por CORDIS es el primer encargo de la semana que viene.

## Lo que se corrigió por estar mal, y lo que cerró

- **F-0008 (EMBO) no era OPEN con plazo duro: es ROLLING.** «There are no
  application deadlines… but there are two cutoff evaluation dates» (4.º viernes
  de enero / 2.º viernes de julio), y la elegibilidad se mide **en la fecha de
  envío**, no en el corte.
- **La palanca de EMBO queda resuelta, y en NEGATIVO.** Las *Application
  guidelines (July 2026)*, bajadas en PDF y leídas con `pdftotext` porque el
  HTML no las trae, dan un criterio genérico con dos ejemplos nombrados
  («Peer Community In», «Review Commons») y tres condiciones cumulativas. No es
  usable antes del 22-01-2027 por tres razones verificadas: EMBO excluye
  «reviewers comments obtained in a regular publication process» (ahí cae eLife
  Reviewed Preprints); Review Commons y PCI exigen obra «not under consideration
  for publication in a journal», así que el artículo de *Nature Mental Health*
  no entra sin retirarlo; y Review Commons sólo publica las revisiones al
  transferir a la primera revista afiliada, con lo que la publicidad **no
  depende de ella**.
- **Y un hecho que la base trataba mal:** el review del *Journal of Sleep
  Research* **nunca podrá satisfacer a EMBO**, ni aceptado, porque las
  guidelines excluyen las reviews como «primary research publications». Sólo
  cuenta el empírico de QIMR. La base trataba los dos manuscritos como
  disparadores equivalentes. Con la desaparición de la reapelación desde el
  22-01-2027 («Researchers may submit only one EMBO Fellowship Proposal»), el
  error caro no es llegar tarde: **es enviar sin el artículo aceptado**.
- **F-0045 (Beca Post Residencia) deja de estar sin verificar, y por fin hay
  canal.** `seqc.es` devuelve 301 a **`semedlab.es`**, que responde 200 con la
  API REST de WordPress abierta: espejo Tier 1 vivo de la Fundación José Luis
  Castaño. **`fundacionjlc.es` queda jubilado como vía.** Confirmado que la beca
  sigue vigente en 2026 a 6.000-15.000 €/año, lo que **mata la hipótesis de
  programa discontinuado**. Matiz honesto de la rama: la cifra ya estaba en la
  base; lo nuevo es la verificación Tier 1 y el canal.
- **Dos altas más por ese mismo canal**, que no estaban en la base: F-0093
  (ayudas a profesionales jóvenes, 6.000 €) y sobre todo **F-0092, el
  Professional Exchange Programme de la IFCC** — estancia de 3 meses, viaje más
  4.500 €, **sin exigir doctorado**, formato idéntico a sus dos estancias
  previas y usable desde mediados de 2027. El alta de socia de SEMEDLAB
  (SUB-0022) rinde ahora en **cuatro** convocatorias, no en tres.
- **F-0010 (Humboldt) estaba mal y es un error con consecuencia de calendario.**
  La fila apuntaba a las convocatorias de julio y noviembre de 2027, que **no le
  sirven**: el doctorado debe estar completado cuando la Fundación *recibe* la
  solicitud. Su primera utilizable abre el **15-03-2028** (comité ~nov-2028,
  inicio desde feb-2029) y, como cada convocatoria cierra por cupo de 800, hay
  que presentar en los primeros días — es decir, **solicitud y acuerdo de
  mentoría firmados antes de defender**.
- **F-0080 (Xunta de Galicia) sube de Fit 2 a 3 y es el hallazgo
  infravalorado.** Seis años de contrato en dos fases, hasta 51.900 €/año en la
  segunda, estancias en el extranjero pagadas dentro de la ayuda y —lo
  decisivo— **ningún requisito de vínculo gallego ni de experiencia
  internacional previa**, que es justo lo que la excluye de César Nombela,
  EIGENT, Ikerbasque y Margarita Salas. Su ventana móvil de 5 años la admite
  desde la edición de 2029. **Pero el art. 2.2.c) excluye a quien haya tenido
  cualquier contrato posdoctoral competitivo: compite con Sara Borrell, no se
  acumula.** Eso es una decisión que hay que tomar, no descubrir en 2029.
- **F-0005 (Ramón y Cajal) VERIFIED en Tier 1**, art. 6.1.a): doctorado entre
  01-01-2016 y 31-12-2024, y sólo el límite *inferior* es ampliable. Su
  inelegibilidad ya tiene causa textual y no supuesto; Juan de la Cierva la
  excluye por lo simétrico (techo 31-12-2026). Encargo cerrado.
- **F-0090 (ECNP Excellence Award) fechada por fin**: 40.º congreso de la ECNP,
  **Barcelona, 25-28 de septiembre de 2027**, así que el tope de 35 años se mide
  el 2027-09-25. **F-0077 (DMM)** tenía el `Next_Action` apuntando al plazo ya
  vencido del 30-10-2026: corregido, y la escalera de 2027 sigue publicada
  íntegra (26-02, 28-05, 27-08, 26-11).
- **F-0023 (ESHG) queda impecable:** plazo 2027-02-04 23:59 CET en pie y **no
  existe plazo de resúmenes separado** — el resumen ES la solicitud, el mismo
  día. Congreso en Rotterdam, 12-15 de junio de 2027, emparejable con F-0077.
- **El tripwire de la SES funcionó y NO saltó**: `modified` sigue en
  `2025-11-03T11:53:19`, un año y seis días sin tocarse, y resuelve W-0012,
  W-0017 y W-0026 **en una sola llamada**. La franja estrecha (27-10 a 05-11)
  queda agotada y descartada; sobrevive la amplia, noviembre a mediados de
  diciembre. La antigüedad de socia ya hace inalcanzable la edición de enero de
  2027.
- **Previsiones nuestras que fallaron, y lo digo:** la reapertura de la SRSF
  «desde ~noviembre de 2026» **no se ha producido** (F-0075 y W-0027; página
  congelada en su sello del 30-09-2026, repitiendo el cierre del 16-10-2026).
  W-0027 baja de LIKELY a LOW y la cadencia de F-0075 pasa a mensual.
- **Sonda del ISCIII repetida:** `report_aes_2027` y `convocatoria_aes_2027` dan
  **404**, el control de 2026 da 200 y 1,75 MB. La AES 2027 no existe todavía;
  F-0001/2/3 y W-0002/3/4 van como UNCHANGED.
- **F-0073 (Plan GenT2): conflicto resuelto.** El plazo del 27-10-2026 era
  **EIGENT del ejercicio 2027** (ventana 28-09 a 27-10-2026); las convocatorias
  GenT2 llevan el nombre del ejercicio siguiente. **F-0076** pasa de UNVERIFIED
  a VERIFIED. **F-0053 (Saavedra Fajardo)**: su latencia ya no es ausencia de
  rastro sino **planificación explícita** — el Plan de Actuación 2026 y el
  Informe de Contrato-Programa 2025 de la Fundación Séneca lo listan como
  actuación *sin convocatoria*, dos ejercicios seguidos.
- **F-0059 (IBRO Rising Stars)**: el Fit 1 tiene por fin causa verificada y
  doble (exige primer laboratorio como IP en 2025-26, y residencia en país LMIC
  de Pan-Europa; España no lo es). La rama **decidió no crear fila de watchlist**
  y lo justifica: es inelegibilidad estructural, no de fecha, y generaría ruido
  semanal sin acción. Me parece correcto.
- **W-0030, alta: el ECNP Early Career Workshop, y se escapó por seis días.**
  Sí lleva dinero (100 plazas, inscripción y hotel gratis en habitación
  compartida; viaje no), así que es de esta rutina y no de `ecosystem`. El plazo
  de la edición de Niza (18-21 de marzo de 2027) **cerró el 2026-11-03**.
  Reapertura esperada hacia noviembre de 2027.
- **El conflicto triple de HFSP queda cerrado y no hay que volver a
  reportarlo**: era texto caduco — banner vivo frente a cuerpo y nota al pie sin
  actualizar, y las tres frases hablan de **la misma** ventana de activación
  (1-abr-2027 a 1-ene-2028). Falta sólo el calendario AY2028, no publicado.
  **La ambigüedad (a) de la BBRF también**: el «APPLY NOW» es un titular de
  sección del ciclo 2026, no un botón vivo.

## Lo que no se pudo verificar o alcanzar

- **Las bases 2027 de la Beca Post Residencia no existen públicamente** en
  ningún dominio alcanzable: `semedlab.es` aún no tiene sección de becas (404 en
  `/becas/`, `/becas-y-premios/`, `/convocatorias/`, `/premios/`, `/fundacion/`)
  y no hay PDF en la mediateca. Pista fuerte: el **2026-11-04 subieron tres
  imágenes `GEMMA-FOTOS-PARA-BECAS`** — la sección se está montando ahora mismo.
- **`esrs.eu`: Cloudflare en todo el dominio, incluida `/wp-json/`**, un solo
  intento, no repetido. Lo que sí se obtuvo, por buscador, es un hallazgo de
  método: **la portada lleva plazos VIVOS y las fichas de programa no** («15
  February» y convocatoria abierta en portada, frente a «closed» en
  `/grants-awards/<programa>/`). Mismo mecanismo de inercia que la SES. La
  portada pasa a ser el tripwire.
- `ERC_Work_Programme_2027.pdf` → 403. `peercommunityin.org/about-pci/` → 404
  (rodeo por búsqueda en el dominio, sirvió). **`nihr.ac.uk` sigue en 403** y no
  se forzó: F-0086 se queda sin fecha de 2027.
- **F-0082 (ASHG)**: muro de socios confirmado de primera mano («You must be a
  member to access this page»). Queda UNVERIFIED **a propósito**; no gastar más.
- **F-0091 (IGES)**: `geneticepi.org/wp-json/…` da **404** — no hay API de
  WordPress ahí, y la sociedad no publica convocatoria.
- **Tatiana**: `fundaciontatianapgb.org` sólo hace 301 a `fundaciontatiana.com`,
  que sigue mudo. **No es rodeo.** No se intentó ningún truco antibot. El correo
  a `becas.neurociencia@fundaciontatianapgb.org` sigue siendo la única salida y
  es acción de la dueña.
- **Tres bloqueos nuevos o reclasificados, para el inventario:**
  `fseneca.es` **es Drupal 7, no WordPress** — el truco `/wp-json/` no sirve ahí
  y no hay que volver a gastarlo; el endpoint **BDNS `/api/convocatorias/busqueda`
  por POST devuelve «Acceso Denegado»** (la consulta por `numConv` y la descarga
  por `idDocumento` siguen bien); y los dos posts de `semedlab.es` sobre la
  Fundación son **episodios de podcast sin texto** (cuerpo vacío).
- **Mejora de método que conviene propagar:** el PDF de la BDNS se lee
  directamente con `pdftotext -layout`, sin el rodeo manual de zlib que la
  fuente registrada daba por necesario; el mismo truco rescató el PDF ilegible
  de `uv.es`.
- No se abrieron las fichas de F-0025 y F-0051 (SRSF) y **la rama no reclama
  verificación** de ellas. F-0061 (Pfizer) no se tocó: exige trabajo
  **publicado** y no tiene ninguno, así que la llamada no decidía nada.
- **De EE.UU. y Australia no hay nada nuevo esta semana**, dicho sin adornos: el
  presupuesto de la rama 2 se fue en consolidar MRC, RYC y las autonómicas. NIH
  F32 / K99-R00 y mecanismos del NIMH para no nacionales, y la NHMRC australiana
  con su vía de contacto viva en QIMR, quedan sin tocar.
- **No existe fondo bilateral España-Japón ni España-Australia que ella pueda
  solicitar**: el programa bilateral de la JSPS es de proyectos conjuntos entre
  instituciones y no muestra carril español. No se creó fila para no meter un
  registro sin URL útil.

## Conflictos que se reportan sin resolver

1. **ESRS, y ahora a tres bandas con un cuarto elemento inquietante.** Fechas de
   cierre en circulación: **31-01-2027** (nuestra extrapolación, de un solo dato
   histórico), **15-02-2027** (portada de `esrs.eu` hoy, para Short-Term,
   Two-Week y Meetings & Courses) y **«March 2027»** (AtomGrants, etiquetado
   «Anticipated/Forecasted» por la propia fuente). Y además una **posible mala
   atribución nuestra**: la ventana «1 December – 31 January» que la base dio
   por fechada la semana pasada puede corresponder al **Sleep Medicine
   Certification Exam**, no a las ayudas. **F-0026, F-0081 y F-0087 conservan el
   31-01-2027 por prudencia**, lo cual es un riesgo conocido de hasta dos
   semanas: hay que zanjarlo en la primera semana de diciembre, cuando abre el
   ciclo. W-0013 se mueve a ~15-02 con confianza MEDIA; W-0029 estrecha la
   franja sin resolverla.
2. **MSCA: respuesta al encargo, no se han confirmado.** El Portal F&T lista
   07-04-2027 / 08-09-2027 17:00 Bruselas como *Forthcoming*, mientras el sitio
   de la MSCA sigue marcándolas **(TBC)**. Un fragmento de tabla del Work
   Programme da apertura 26-05-2027 y plazo 23-11-2027 sin que se pueda
   establecer a qué convocatoria corresponde: **no se atribuye a PF-01**. El WP
   permite mover la apertura ±1 mes y retrasar el plazo hasta 2 meses, así que
   no serán firmes ni cuando caiga el (TBC).
3. **Cierre de resúmenes de la ECNP 2026**: dos páginas de `ecnp.eu` dan **5 de
   mayo 23:59 CEST** y **7 de mayo**. No se elige.
4. **ECNP Rising Star (F-0095)**: la ficha dice «hasta dos» al año y la página
   early career 2026 dice «hasta tres». Y la ambigüedad que de verdad decide esa
   fila: la ventana de 2 a 7 años cuenta desde el «título terminal (doctorado
   **o MD**)» — con el MD de 2019 ya estaría fuera; con el doctorado, 2030-2035.
   Fichada Fit 2 a la espera de que lo aclare la ECNP.
5. **NIHR Future Leader Fellowship cohorte 2**: una oficina universitaria da
   plazo de enero de 2027, UCL da expresión de interés en junio de 2027. No
   afecta a F-0086.
6. **W-0020 (Junta de Andalucía), corregido más que en conflicto:** la
   estimación confundía dos fechas. La **resolución** sale a mediados de
   diciembre (la anterior es del 17-12-2025), pero el **plazo de solicitud** es
   en enero (05-01 a 28-01-2026, con ampliación posterior en BOJA). Fichada
   también la trampa real de que «Línea 2» nombra **dos programas distintos**.

## Síntesis estratégica que emerge de cruzar dos ramas

Las autonómicas de **atracción** de talento (César Nombela, EIGENT, Ikerbasque,
Margarita Salas de Asturias) piden sistemáticamente **2 años fuera**, y sus ~6
meses de estancias no llegan ni llegarán a tiempo. El carril autonómico que sí
le sirve es el de **primer posdoctorado**: Galicia ED481B (F-0080) y Andalucía
Línea 2. **Conviene dejar de gastar presupuesto semanal en el primer grupo**, y
esta pasada ya no lo gastó: F-0052, F-0055, F-0056 y F-0074 se dejaron latentes
a propósito, con la razón escrita en cada fila.

## Filas que ella ya hubiera leído y cuyos hechos han cambiado

**Ninguna.** `data/owner_status.json` sigue vacío (`{}`), así que no hay ninguna
marca suya y ningún modelo mental que se haya quedado obsoleto por debajo. El
`Owner_Status = NEW` de muchas filas es el valor por omisión, no una lectura.

Dicho eso, **si en algún momento leyó la fila del ERC o el informe de la semana
pasada, el consejo de adelantar la defensa a enero de 2028 ya no vale** (ver
arriba). Es el único sitio donde una lectura previa suya habría quedado mal
informada.

## Suscripciones pendientes

**45 de 45 en TODO** (`owner_status.json` vacío, así que pendiente = todo lo que
el TSV marca TODO). Sin altas esta pasada. Las de prioridad alta que siguen
esperándola son SUB-0040 (avisos de HFSP), SUB-0042 (newsletter de la ESRS,
única vía fiable de enterarse de la apertura del 1 de diciembre con el dominio
tras Cloudflare), SUB-0036 (alta en la ESRS) y **SUB-0022 (SEMEDLAB), que esta
pasada revaloriza: ahora desbloquea cuatro convocatorias**.

## El dato que sólo ella puede dar

**Su año de nacimiento**, por segunda semana consecutiva como la pregunta de
mejor relación coste-beneficio del radar: hoy bloquea F-0043, F-0090 (tope de 35
años medido el 25-09-2027) y el workshop de la ECNP. El SIRS es la excepción
afortunada: su *under 40 by April 2027* se cumple casi con seguridad.

Y sigue pendiente, por **novena** semana, **los meses exactos de las estancias
en QIMR Berghofer y en Japón**: sin ellos, MSCA y EMBO no pasan de LIKELY en
movilidad.

## La regla de tamaño sigue incumplida, y empeorando

`fellowships.tsv` está en **353 KB** (307 hace una semana), casi seis veces el
umbral de ~60 KB. Además `changelog` 490 KB, `sources` 363 KB, `groups` 347 KB,
`postdocs` 214 KB, `jobs` 102 KB, `events` 64 KB y **`watchlist_closed` 63 KB,
que cruza el umbral esta semana**. Es arrastre, no nuevo, y **el corte lo hace
ella**: partir un fichero obliga a cambiar `build_page.py` y `build_xlsx.py` en
el mismo commit, y eso no es trabajo para el final de una pasada desatendida.

## Qué perseguiría la semana que viene

1. **La portada de `esrs.eu` en la primera semana de diciembre** —ahora es el
   tripwire— para zanjar si el cierre es el 31-01 o el 15-02 y si la ventana del
   1 de diciembre es de las ayudas o del examen de certificación.
2. **Confirmar el 0-10 del ERC por CORDIS o las páginas node** (el PDF del Work
   Programme da 403) y si su residencia 2023-2027 cuenta como formación clínica
   para extender el límite superior.
3. **Relanzar `pages`+`media` con `search=beca` en `semedlab.es`**: la sección de
   becas está naciendo. Si no aparece, correo a `secretaria@fundacionjlc.es`.
   Y leer las bases del **IFCC PEP** en `ifcc.org` (plazo, tope de edad, si es
   por nominación), que es la fila nueva con más recorrido.
4. **La página «General Information & Deadlines» de la SIRS**: sede, fechas y
   plazo de resúmenes de 2027 — **si el de resúmenes es anterior al 01-12, ese
   es el plazo real** y cambia la urgencia de F-0094.
5. **Las dos del watchlist que la rama 5 dejó sin tocar y lo merecen**: W-0009
   (ISPG ECIP, Fit 5) y W-0021 (Koplowitz, bases hacia enero). De las 29 filas
   comprobó 12; las 17 restantes se quedaron por ventana lejana, por ser de otra
   rama, por estar ya cubiertas o por orden explícita.
6. **NIH F32 / K99-R00 y mecanismos del NIMH, y la NHMRC australiana**, que
   llevan dos semanas sin mirarse, más **JIGENT** 2027/2028 y el correo a
   `seneca@fseneca.es` sobre Saavedra Fajardo.
7. **Un canal de avisos de la SIRS** para el cupo de suscripciones, que esta
   semana se quedó a cero.

Cruce para otra rutina, no de la mía: la Fundación Séneca publicó en el BORM una
convocatoria 2026 de **estancias en el extranjero** (01-06-2026 a 30-09-2027), y
la rama 5 se tropezó con el PDF `2027-05-09-BRAIN-2027-Symposium-call11.pdf` en
`senc.es`, que es congreso y por tanto de `ecosystem`.
