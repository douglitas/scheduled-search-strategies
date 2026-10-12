# fellowships — 2026-10-12

Las cinco ramas completas, 118 llamadas de herramienta entre ellas. Nada
pendiente de la pasada anterior quedó sin tocar salvo lo que se dice al final.

## Recuento, tomado del diff y no de la memoria

`git diff --stat HEAD~1`: 194 inserciones, 94 supresiones en 6 ficheros.

| fichero | antes | después | altas | líneas modificadas |
|---|---|---|---|---|
| `fellowships.tsv` | 75 | 77 | F-0076, F-0077 | 43 |
| `watchlist_closed.tsv` | 26 | 26 | — | 19 |
| `sources.tsv` | 281 | 294 | 13 fuentes | append-only |
| `subscriptions.tsv` | 28 | 32 | 4 propuestas | append-only |
| `changelog.tsv` | 676 | 758 | 82 apuntes | append-only |
| `action_now.tsv` | 34 | 33 | mías: 1 (F-0027) | 31 ajenas preservadas |

Ninguna fila tenía marca de la dueña distinta de `NEW`, así que **esta pasada
no ha dejado obsoleto nada que ella hubiera leído ya**. `owner_status.json`
sigue vacío y `source_inbox.json` también: no había nada que triar.

## Las tres cosas que merecen acción

**1. F-0023, ESHG 2027 — sube de Fit 4 a Fit 5 y es lo mejor de la pasada.**
El esquema de Conference Fellowships de 2027 ya está publicado y se ha leído en
Tier 1, resolviendo el 404 que arrastraba la fila desde agosto: plazo
**2027-02-04 a las 23:59 CET**, inscripción gratis más 400 EUR, y **cupo de
hasta 140 plazas europeas**, que es por lo que la competencia queda en
LOW-MEDIUM con números y no a ojo. Es elegible por la vía literal de «a
student» (sigue doctoranda); las vías de MD y de «último título» NO le sirven,
porque su MD es de 2019 y la especialidad acaba el 22-05-2027. Esfuerzo XS:
marcar casillas al enviar el resumen. Las dos condiciones reales son hacerse
socia de la ESHG para 2027 (propuesta SUB-0030) y que le acepten el resumen.
Nota operativa: con plazo a 115 días **no entra todavía en action_now**; entrará
sola en la pasada del 2026-11-06, cuando cruce la ventana de 90 días.
La URL sólo se alcanza por el permalink `https://2027.eshg.org/?p=392`;
`/fellowships/` y `/meetings/eshg-2027/fellowships` dan 404.

**2. F-0008, EMBO — cambio de reglas que obliga a decidir, no sólo a anotar.**
Verificado en embo.org: desde la ronda de otoño de 2027 **se suprimen las
re-solicitudes y cada investigadora podrá presentar UNA SOLA propuesta EMBO**
en toda su carrera (y un mismo host sólo puede avalar una candidata por ronda).
El corte del 22-01-2027 queda descartado de oficio por los relojes, así que la
decisión que hay que tomar con tiempo es **en qué ronda gasta su único intento**.
Las ramas 1 y 5 llegaron a este dato por separado y coinciden.

**3. F-0012, Wellcome Early-Career — reabre, y a la vez se cierra por geografía.**
Única reapertura real del watchlist: pasa de CLOSED a **ROLLING**, abierto desde
el 25-08-2026, sin plazo («apply anytime»), con preselección en febrero, junio y
septiembre. Dos correcciones importantes: **se retira la fecha del 10-11-2026**,
que no existe en ninguna página de Wellcome y era un plazo interno de institución
(Oxford, UCT) — con eso queda cerrado el conflicto 10-vs-16 de noviembre que
arrastrábamos; y hay un **corte duro nuevo, VERIFIED, el 29-10-2026**: a partir de
esa fecha Wellcome sólo acepta solicitantes principales con institución gestora en
Reino Unido o en países de renta baja/media de África y Asia meridional y
sudoriental. El host británico deja de ser una preferencia y pasa a ser requisito.
Además, VERIFIED: exige tesis defendida al presentar, así que su primera solicitud
posible es posterior a febrero de 2028.

## Elegibilidad: cuatro relojes que se han cerrado esta semana

- **F-0004, Juan de la Cierva: INELEGIBLE hasta 2029.** La convocatoria formal ya
  está publicada (60 M EUR; investigadora 12-26/11/2026, centro hasta 03-12-2026)
  y exige doctorado obtenido **entre el 01-01-2024 y el 31-12-2026**; la residencia
  MIR no figura entre las causas de ampliación. Su primera edición posible es la de
  2029, cuya ventana sí cubriría una defensa en febrero de 2028 aun con retraso.
  **Corrección del orquestador:** la rama 2 verificó la inelegibilidad pero dejó el
  Fit en 4, y con plazo el 03-12-2026 la fila entraba en `action_now`, que el
  contrato prohíbe para una convocatoria no elegible. Bajada a Fit 2 con el
  razonamiento reescrito, y queda dicho que el Fit es bajo **por elegibilidad, no
  por calidad del encaje ni por competencia**.
- **F-0010, Humboldt: ya NO es presentación continua.** Tres convocatorias al año
  (15-03, 15-07, 15-11) y **cada una cierra al llegar a 800 solicitudes**. La actual
  está cerrada; la siguiente abre el 15-11-2026. Implica presentar en los primeros
  días y tener anfitrión alemán cerrado antes. De ahí la propuesta SUB-0029.
- **F-0011, DFG Walter Benjamin: baja de Fit 4 a 3.** La modalidad «fuera de
  Alemania» exige tres años previos de investigación en Alemania o formación
  alemana, así que le está vetada; su vía es el módulo de puesto *en* Alemania.
- **F-0018, ERC Starting Grant:** la ventana publicada (doctorado del 01-01-2017 al
  31-12-2026) confirma la regla de 0-10 años: su primera convocatoria posible es la
  de 2029/2030. No existe calendario ERC-2028-StG, porque el programa de trabajo de
  2028 no está adoptado.
- **F-0009, MSCA-PF:** exige doctorado concedido en la fecha de cierre, así que con
  defensa en febrero de 2028 **no** es elegible para el corte indicativo del
  08-09-2027; su primera edición posible es la de 2028, que además depende de FP10.
- **F-0073, Plan GenT2 (Comunitat Valenciana):** plazo corregido, 28-09 a
  **27-10-2026** (teníamos 30-10), y las tres modalidades exigen doctorado leído y
  que solicite el centro valenciano → inelegible esta edición. Queda anotada JIGENT
  (20 ayudas, 80 k/año, 4 años) como su puerta a partir de 2029.

## Lo que cierra o se mueve

- **F-0019, FENS/IBRO-PERC:** la ronda del 15-10-2026 queda descartada y verificada
  en Tier 1 — cerraba en tres días sin carta de aceptación de anfitrión ni membresía
  SENC, que son **requisitos de admisión, no méritos**. La fila **se rueda a la ronda
  del 15-04-2027**, que es la alcanzable: en abril de 2027 sigue doctoranda y la
  estancia caería después del 22-05-2027, cuando acaba la residencia. Decisión del
  orquestador: la rama 1 propuso abrir una fila nueva para esa ronda; se ha fundido
  en F-0019 porque la regla de deduplicación de `data/readme.tsv` dice que una
  convocatoria anual conserva su ID. Confidence LIKELY, no VERIFIED: la cadencia de
  dos rondas al año es oficial, pero FENS aún no publica la fecha de 2027.
  Al salir de la ventana de 90 días, **F-0019 sale de action_now** y volverá a
  entrar hacia mediados de enero de 2027 — de ahí que `action_now` quede con una
  sola fila mía y que los Rank ajenos se hayan renumerado.
- **F-0075, SRSF Mentored Collaboration:** deja de ser ROLLING. La página oficial
  avisa de cierre el **2026-10-16**, en cuatro días; ≤3.500 USD y exige membresía
  SRS activa de mentora *y* mentorizada, así que no es accionable.
- **F-0032, BBRF Independent Investigator:** de OPEN a FORTHCOMING (la propia BBRF
  dice estar «determinando el periodo de aceptación»).
- **F-0015, NIH F32:** Status corregido de CLOSED a ROLLING (plazos 08-04, 08-08 y
  08-12), pero inelegible por ciudadanía, confirmado con el NIMH.
- **Dos altas, las dos de registro o de dinero pequeño:** F-0077, DMM Conference
  Travel Grants de The Company of Biologists (plazo **2026-10-30**, hasta 300 GBP
  nacional / 500 GBP extranjero, doctorandas elegibles, sin acogida, Fit 3 — el
  riesgo es que la reunión encaje en el ámbito temático de la revista); y F-0076,
  Talentum Plus del Cabildo de Tenerife (CLOSED, Fit 2, sólo para no redescubrirlo).
- **Roto un bloqueo que llevaba semanas:** `bga.clubexpress.com/content.aspx`
  responde 200 (la raíz da 403). Confirma la 57ª reunión de la BGA en Minneapolis,
  junio de 2027, y permite poner **F-0027 en Competition_Level LOW con números**
  (26-40 ayudas de estudiante por congreso): por eso es la única fila mía en
  `action_now` esta semana.
- **Y otro, importante para el brief: wellcome.org ya NO da 403**, responde 200 con
  User-Agent de navegador. Llevaba cinco pasadas marcado como bloqueo.

## Watchlist: 19 de 26 filas revisadas

Sin tocar por presupuesto: W-0006, W-0011, W-0013, W-0014, W-0020, W-0022, W-0024.

- **La SES NO ha reabierto.** `modified` de `/becas-y-premios/` sigue en
  2025-11-03 y `media?after=2026-08-01` está vacío. La ventana 27-10 / 05-11 se
  mantiene como estimación, sin mover. **Aviso metodológico que ahorra llamadas:**
  sondear `/wp-content/uploads/AAAA/MM/` da falsos positivos (403 en carpetas de
  2026 sin ningún medio nuevo); la prueba fiable es `modified` más el PDF de bases
  por la API.
- **Premisa propia corregida (W-0016):** EMBO no «reabre», acepta todo el año; lo
  que llamábamos «ronda de otoño de 2027» es lo presentado tras el corte del
  22-01-2027, que ya vive en F-0008.
- **SRS (W-0010):** publica que avisará del ciclo 2027 en enero de 2027, así que la
  reapertura deja de ser extrapolación. **BBRF (W-0007):** ventana 2026 (04-02 a
  04-03) leída en Tier 1; 2027 sigue sin publicar. **HFSP (W-0001) y MSCA PF 2027
  (W-0015):** revisadas, sin un solo cambio.
- **AES 2027 (W-0002/3/4):** sin publicar; el disparador sigue siendo el extracto
  del BOE de la segunda quincena de diciembre, ahora con patrón de dos ediciones.

## Lo que no se pudo verificar, y los conflictos

- Calendario HFSP del ciclo AY2028: **no existe**; la página sólo cubre el ciclo
  2027, cerrado el 24-09-2026. Fila sin fechas, a propósito.
- Ciclo BBRF 2027: sólo proyecciones de terceros (febrero-marzo). Sin escribir.
- F-0005, Ramón y Cajal: extracto del BOE del 26-09-2026, plazo 10-11 a 10-12-2026,
  240 M EUR, pero la página Tier 1 de RYC2026 da 404 → **LIKELY**, y queda pendiente
  leer la ventana de doctorado en BOE-B-2026-31264 / BDNS 918641. Es lo primero de
  la semana que viene, porque decide si también la excluye.
- F-0026 (ESRS): `esrs.eu` sigue en 403 de Cloudflare, sin confirmación Tier 1.
- Conflictos anotados sin resolver: duración de FENS/IBRO-PERC, 4 meses según FENS
  frente a 3 según IBRO; la página de la ESHG 2027 arrastra una mención al congreso
  de 2026 en el requisito de resumen; las cifras fiscales de la BGA no cuadran entre
  ejercicios; y la página de HFSP sigue sin limpiar tras el cierre.
- Bloqueos nuevos: `bbrfoundation.org/grants-prizes/young-investigator-grants` 404,
  `fens.org/careers/fens-ibro-perc-exchange-fellowships` 404, `dfg.de` 404 en dos
  rutas, `forwomeninscience.com/en/awards` 404, `fundacionjlc.es` (301 + reset),
  `fundaciontatianapg.org` (502), `lacaixafoundation.org` (403).
- Dos huecos cerrados **en negativo**, que es un resultado y no un fracaso: ninguno
  de los cinco Working Groups del PGC recorridos (autism, bipolar, mdd,
  eating-disorders, substance-use) lleva ayudas ni becas; y no existe fondo bilateral
  estable España-Japón ni España-Australia para investigadoras individuales aparte
  de JSPS.
- La vía de la BDNS por título corto **está agotada**: 14 frases nuevas devolvieron
  cero programas postdoctorales vivos en Cataluña, País Vasco, Galicia, Castilla y
  León, Aragón, Navarra, Canarias y Murcia. El resto hay que ir por diarios
  oficiales y agencias (AGAUR, Ikerbasque, GAIN, ARAID), no por la API.

## Datos suyos que faltan y que siguen bloqueando filas

Los mismos de siempre, y esta semana con una buena noticia y una prioridad clara:

1. **¿Es socia de la SRS o de la AASM, y desde cuándo?** Desbloquea de golpe
   F-0025, F-0051 y F-0075. Es la pregunta de mayor rendimiento de la lista.
2. **¿Es socia de la SENC?** Es la única condición de elegibilidad que falla en
   F-0019, y hay que tramitarla con meses de margen antes de abril de 2027.
3. Buena noticia: **su fecha de nacimiento ya no hace falta para F-0064**. La Beca
   Nacional de la AEGH **no** tiene límite de edad (los 35 años son de otras bolsas).
   Sigue inelegible, pero por otra razón: los 4 años de experiencia postuniversitaria
   y los 2 años de antigüedad como socia.
4. Antigüedad como socia de SEQC/SEMEDLAB (6 meses) para F-0045.

## Suscripciones pendientes

**31 de 31 en TODO, ninguna marcada aún** (`owner_status.json` está vacío, así que
la definición de pendiente es la del TSV). Cuatro nuevas esta semana, todas ALTA
salvo la última: SUB-0028 avisos de convocatoria de EMBO, **SUB-0029 avisos de
apertura de Humboldt** (crítica por el tope de 800 solicitudes), **SUB-0030 alta de
socia de la ESHG para 2027** (bloquea F-0023, que es la mejor fila de la pasada) y
SUB-0031 boletín de Wellcome. Omitida por duplicada: la de membresía de la SRS, cuya
URL ya estaba en el fichero.

## Mantenimiento: sigue sin hacerse y ya cuesta

`data/fellowships.tsv` pasa de 226 KB a **~232 KB, casi cuatro veces el umbral de
60 KB**; `changelog.tsv` va por ~205 KB y `sources.tsv` por ~200 KB. **Con razón no
se parte sola**: hacerlo obliga a tocar `build_page.py` y `build_xlsx.py` en el mismo
commit y eso no se hace desatendido. Corte sugerido, el mismo de las cuatro pasadas
anteriores: internacionales frente a españolas, o becas frente a premios y ayudas de
viaje.

Y el apunte de entorno que va por la **tercera semana**: no hay `pdftotext` y `pypdf`
está roto (`_cffi_backend`). Dos ramas han vuelto a extraer PDF descomprimiendo
streams con `zlib` a mano, y de ahí han salido las fichas del Plan GenT2 y las bases
legales de L'Oréal-UNESCO. Merece ser un helper de `tools/`.

## Qué perseguiría la semana que viene

1. **La ventana de doctorado de Ramón y Cajal** en BOE-B-2026-31264 / BDNS 918641:
   decide si F-0005 también la excluye, y el plazo es el 10-12-2026.
2. **La ventana de la SES entre el 27-10 y el 05-11**, por `modified` y por el PDF de
   bases en la API: es la reapertura más cercana de todo el watchlist.
3. **Las 7 filas del watchlist sin tocar**, empezando por W-0020 (Junta de Andalucía,
   apertura estimada hacia el 20-12-2026) y W-0011.
4. **El bloque autonómico por diarios oficiales y agencias** (AGAUR, Ikerbasque,
   GAIN, ARAID), ya que la API de la BDNS está agotada por título.
5. **Decidir la estrategia EMBO** ahora que hay un solo intento por investigadora:
   es una decisión de ella, no de la rutina, y conviene que la tenga encima de la mesa.
6. **Los correos que ya no se pueden evitar**, y van cinco semanas: BGA por el reloj
   de 7 años (F-0058), `secretaria.tecnica@ses.org.es` por cómo se cuenta la
   antigüedad (F-0046), y la SEQCML por la rotación externa de Medicina de Laboratorio.

## Fuera de ámbito, pero urgente para su carril clínico

La rama 5 encontró, sin buscarlo, un post de la AEGH del 2026-10-05 sobre los
**proyectos de Reales Decretos de las especialidades de Genética Médica y Genética de
Laboratorio**, que son su vía transitoria. Eso es de la rutina `positions`, que ya lo
tiene como J-0003 en el puesto 1 de `action_now` con alegaciones abiertas hasta el
26-10-2026. Se deja la nota aquí sólo para que conste que las dos pasadas apuntan al
mismo sitio.
