# fellowships — pasada del 2026-10-05

Las cinco ramas completaron y el push fue directo a main (`7b6c264`). El buzón lo
leyó positions a las 00:01 y no enrutó nada a FELLOWSHIPS; `data/source_inbox.json`
está vacío, así que no había trabajo de bandeja por mi parte. Ninguna ALERTA: nada
roto, nada sin entregar.

Pasada de **desmentidos**, no de descubrimiento. Cero altas en programas bandera y
tres filas que bajan de nota porque hoy se leyó el articulado que antes se suponía.
Dos de esas tres bajadas son correcciones de algo que la base afirmaba y era falso.

## Los números, del diff (`git diff HEAD~1`), no de mi memoria

| fichero | altas | modificadas |
|---|---|---|
| `data/fellowships.tsv` | 3 (F-0073, F-0074, F-0075) | 19 |
| `data/watchlist_closed.tsv` | 2 (W-0025, W-0026) | 14 de 24 |
| `data/sources.tsv` | 6 (SRC-0230 … SRC-0235) | — |
| `data/subscriptions.tsv` | 2 (SUB-0024, SUB-0025) | — |
| `data/changelog.tsv` | 46 apuntes | — |
| `data/action_now.tsv` | 2 filas mías (antes 3); 28 ajenas preservadas | — |

El mismo aviso que la semana pasada, y por el mismo motivo: de las 30 filas de
`action_now`, **27 salen en el diff con solo la columna `Rank` cambiada**. Lo
verifiqué fila a fila antes de commitear: las únicas con cambio de contenido son
mis dos (F-0004 y F-0019, y solo en `Days_Left`, que lo recalcula el generador), y
la única que sale es F-0037, que ha cerrado. Si la página marca filas de ecosystem
como novedad de la semana, es ese renumerado, no trabajo nuevo.

## Las tres cosas que merecen acción

**1. Andalucía SÍ exige movilidad exterior, y eso rompe lo que esta base decía.**
Hasta hoy F-0052 y W-0020 afirmaban que los contratos posdoctorales de la Junta
eran «la única vía autonómica sin requisito de movilidad exterior», y que la
edición de enero de 2029 era la decisiva. **Es falso.** El resuelvo quinto, punto
4, de la Resolución de 17-12-2025 (BOJA 246) exige acreditar **12 meses en centros
de países distintos al del título de doctor, de los cuales al menos 9 posteriores a
la defensa**, en estancias de ≥3 meses ininterrumpidos cada una. Tus dos estancias
de ~3 meses (QIMR y Japón) son **anteriores** a la defensa, así que como mucho
cuentan para los 3 meses no posteriores. Consecuencia práctica: esto no es una
puerta de entrada, es **una vía de retorno a Andalucía después de un posdoc fuera
de España de ≥9 meses**, con lo que la edición de enero de 2029 queda descartada y
las útiles son las de 2030-2033 (la ventana de 5 años desde la defensa sí es
generosa: te llega hasta ~feb-2033). Fit baja de 4 a 3 en las dos filas. Acción
temprana y barata que conviene no olvidar: **pedir el certificado de estancia al
inicio de cada estancia**, porque sin esos meses certificados la solicitud no se
admite. Nota de método para la próxima: `boja/2025/246/9` da timeout por WebFetch
y se lee entero por `curl`; la ruta `/246/10` (el extracto) da reset.

**2. La «tercera pieza» de la SES que llevábamos una semana buscando ya estaba
fichada: es F-0046.** No había alta que hacer, y eso es bueno saberlo porque evita
duplicar. Lo que sí es nuevo son sus bases leídas en Tier 1 (PDF descomprimido con
zlib), y traen un cerrojo que ahora está **verificado y no supuesto**: hay que ser
socia de la SES **desde al menos un año antes de la convocatoria**. Ese año no se
puede cumplir para la edición que abre hacia el 3 de noviembre con plazo ~25-01-2027,
así que **esa edición está perdida**. Y el calendario tiene una trampa: el otro
requisito es estar en el **último año de residencia** (el tuyo va de mayo de 2026 a
mayo de 2027), que encajaría justo en la edición perdida; en la de enero de 2028 ya
no serás residente y ese requisito no te aplicaría, pero entonces hay que averiguar
por qué vía entras. Hay una pregunta concreta que decide la fila y que solo se
contesta por escrito a `secretaria.tecnica@ses.org.es`: **si el año de antigüedad se
cuenta antes de la apertura o antes del plazo.** Queda en W-0026 con el aviso.

**3. Dos dudas del NIH que arrastrábamos desde agosto están cerradas, y una de
ellas en tu favor.** El **K99/R00 no tiene requisito de ciudadanía** («There is no
citizenship requirement for K99 candidates»): puedes ser PI sin ser ciudadana ni
residente permanente. La condición real está en otro sitio: las **entidades
extranjeras no son elegibles como solicitantes**, así que tienes que estar ya de
posdoc en una institución estadounidense que presente la solicitud y patrocine el
visado, y el NIMH está entre los institutos participantes. Ventana verificada: no
más de 4 años de experiencia posdoctoral, que en tu caso empiezan en feb-2028. El
**F32, en cambio, te excluye de forma definitiva**: exige ciudadanía o residencia
permanente, y eso no es una duda abierta, es un no. Aviso de calendario: el anuncio
PA-24-194 **expira el 08-05-2027**, así que en 2028 habrá otro y no hay que citarlo
como vigente.

## Lo que cerró y lo que bajó de nota

- **F-0037** (Beca Internacional de Intercambio, Fundación JLC): plazo del 30-09
  vencido **sin prórroga**. Pasa a CLOSED, pero con Confidence **LIKELY, no
  VERIFIED**, y conviene saber por qué: `fundacionjlc.es` no se pudo abrir (503 por
  WebFetch, reset por curl) y el cierre se apoya en la ficha de becas.com, que puede
  cerrar una ficha por simple vencimiento de fecha. La edición 2027 vive en W-0023 y
  el alta de SEMEDLAB deja de ser una carrera contra el reloj.
- **F-0054** (Fulbright-Fundación Séneca III): cerrada el 02-10-2026, esto sí
  VERIFIED en Tier 1. Preselección en noviembre-diciembre. La IV está en W-0022.
- **F-0072** (Alicia Koplowitz, Estancias Cortas): **elegibilidad rota**. Las bases
  2026 exigen título de **especialista en Psiquiatría (MIR) o Psicología Clínica
  (PIR)**, y eres de Medicina de Laboratorio. Fit 3 → 1 y línea cerrada: el
  doctorado de 2028 no lo arregla. Las otras ayudas de la casa piden lo mismo; la
  única que podría admitir un perfil MD genetista es la línea de proyectos, sin leer.
- **F-0050** (Fundación Tatiana): Fit 4 → 3, y no por el dinero. 40.000 €/año **sin
  ninguna ventana de años desde el doctorado** es exactamente lo que necesita quien
  defiende tarde. Lo que lo baja es el criterio de reparto: la **contribución
  interdisciplinar vale el 30%** de la nota, y la genética estadística pura no es lo
  que premia este fondo. El ángulo que tienes y casi nadie más: MD + genética
  psiquiátrica + la ética y la traslación clínica de la predicción poligénica. Exige
  **título ya obtenido**, así que tu primer ciclo es junio de 2028, con grupo elegido
  a finales de 2027 para llegar con la carta de admisión.
- **F-0018** (ERC StG): la convocatoria ERC-2027-StG está abierta ahora mismo (cierra
  el 14-10-2026) y no puedes presentarte. Horizonte: ERC-2028. Anotado el desfase de
  un año entre el nombre de la convocatoria y el año natural, que despista al releer.

## Lo que sigue vivo y con fecha encima

**F-0019 (FENS/IBRO-PERC) cierra en 10 días, el 15-10-2026, y no es alcanzable**:
necesita carta de acogida y ser socia de la SENC (SUB-0003). La ronda realista es la
del 15-04-2027. El 16 de octubre esa fila pasa a CLOSED. Detrás, **F-0004 (Juan de
la Cierva)** con 59 días: ventana de solicitud ya fijada por la BDNS, del **12-11-2026
al 03-12-2026 a las 14:00**, y sigue en pie que tu primera convocatoria útil es la de
2028. **F-0008 (EMBO)** mantiene el corte del 22-01-2027 tras dos lecturas idénticas,
y aparece una condición nueva que hay que resolver con el grupo anfitrión antes de
escribir nada: **un laboratorio solo avala a una candidata por ronda**.

## Lo que no pude verificar, y los bloqueos

- **`esrs.eu` bloquea con Cloudflare** (403 «Just a moment»), página y wp-json, dos
  rutas probadas. W-0013 queda **sin comprobar a propósito** y con `Last_Checked`
  sin tocar, para no fingir una verificación. Vía alternativa: Wayback o el boletín.
- **`fundacionjlc.es`**: 503 por WebFetch y reset por curl, también en
  `web.archive.org`. Afecta a F-0037 y F-0045. Los espejos de PDF (irsjd.org,
  idipaz.es) solo tienen ediciones viejas.
- **Bases del Plan GenT2** (F-0073): `ceice.gva.es` da reset y el DOGV también, y el
  texto que sirve la BDNS solo trae cláusulas de transparencia. La fila queda
  UNVERIFIED con Fit 2 provisional: ventana de años, movilidad e importe sin leer.
- **MSCA**: sigue sin abrirse la página de topic HORIZON-MSCA-2027-PF-01 del Portal
  de Financiación, que es la vinculante (es una SPA que no renderiza por fetch). Lo
  que hay es la web MSCA (Tier 1) con lanzamiento 07-04-2027 y cierre 08-09-2027,
  **ambos TBC**. Y sobre el agujero de FP10: la búsqueda explícita de hoy **no
  encontró ningún texto oficial** de la propuesta 2028-2034 que mencione las PF. No
  se afirma ni se niega.
- **BGA (F-0058)**: `bga.org` **ya carga** (el 403 desapareció), pero su página del
  premio solo describe y lista ganadoras: **el bloqueo ya no es la web, es que las
  bases no están publicadas en ningún sitio**. El reloj de 7 años sigue siendo Tier 2.
  No hay forma de cerrarlo sin escribir a la sociedad.
- **ISCIII (AES 2027)**: sin borrador ni calendario. Anotado para no repetir el
  camino: los 404 de hoy en `ciencia.gob.es` eran de URL adivinadas y no prueban
  nada; la ruta real sigue el patrón `/Convocatorias/<año anterior>/ISCIII-AES<año>.html`,
  así que en diciembre hay que mirar `/Convocatorias/2026/ISCIII-AES2027.html`.
- **13 filas del watchlist sin revisar** por presupuesto, todas con ventana en 2027:
  W-0005 (Wellcome), W-0006 (NHMRC), W-0008 (la Caixa), W-0009 (ISPG ECIP), W-0010
  (SRS/SLEEP 2027), W-0011 (Premio Instituto de Neurociencias), W-0015 (MSCA PF 2027),
  W-0016 (EMBO), W-0021 (Koplowitz), W-0024 (Ayudas Tesis Jóvenes), más W-0013
  (bloqueada) y W-0014 (propuesta de retirada). W-0001 y W-0007 sí quedaron
  verificadas, por la rama 1 y no por la 5.
- **Rotación externa para residentes de Medicina de Laboratorio**: buscada y no
  encontrada. Es ámbito nuestro y el hueco queda abierto; la vía es la web de la
  SEQCML y los comités de docencia, no la búsqueda web.

## Decisiones de reparto que tomé y conviene que sepas

- **María Goyri (Comunidad de Madrid)** apareció en la BDNS y **no la fiché**: es una
  subvención nominativa a cada universidad, no una convocatoria a la que puedas
  presentarte, así que el dinero va pegado a plazas que abre otro. **Eso es de la
  rutina positions**, y lo dejo escrito aquí para que lo recoja en vez de que se
  redescubra cada semana como fellowship.
- **Fundación Mutua Madrileña** (2,3 M€, con área de salud mental infantojuvenil)
  tampoco: es dinero para proyectos de un investigador principal consolidado.
- **W-0014 (One Mind)**: anotada la propuesta de retirada (Fit 1, sin acción), pero
  **no se borra**. El watchlist no se borra; la decisión es tuya.

## Nada que hubieras marcado ha cambiado bajo ti

`owner_status.json` sigue vacío `{}`. Lo verifiqué comparando columna a columna
contra `HEAD`: **cero alteraciones de `Owner_Status`** en las 19 filas que toqué, y
ninguna de ellas tenía marca distinta de `NEW` o vacío. También comprobé que los 76
valores de `Fit_1_5` siguen siendo enteros desnudos en las dos pestañas.

## Suscripciones pendientes

Las **25**, todas en TODO y ninguna con marca tuya en `owner_status.json`. Las dos
nuevas de hoy: **SUB-0024 (lista de BBRF)**, porque BBRF no publica calendario por
adelantado y su ventana es de un mes, y **SUB-0025 (avisos del BOJA)**, por la vía
andaluza de retorno. Las de mayor rentabilidad inmediata siguen siendo **SUB-0003
(SENC)**, que es lo único que falla en F-0019, y **SUB-0008 (SES)** y **SUB-0022
(SEMEDLAB)**, que son relojes de antigüedad: cada semana que pasan sin firmarse
retrasan una edición entera.

## Datos tuyos que faltan y que deciden filas

Los mismos dos, y hoy han bloqueado cuatro filas más: **de qué sociedades
científicas eres socia y desde cuándo** (la SES exige 1 año, la SEQC/SEMEDLAB 6
meses para F-0045, la SRS membresía en regla para F-0075, F-0019 pide SENC) y tu
**fecha de nacimiento** (bolsas de la AEGH, límite de 35 años; JLC, menor de 40).
Ninguna rama ha adivinado: está escrito en `Eligibility_Key_Conditions` de cada fila.

## Mantenimiento, que ya es urgente

`data/fellowships.tsv` pasa de 210 KB a **226 KB, casi cuatro veces el umbral de
~60 KB**; `changelog.tsv` va por 181 KB, `sources.tsv` por 162 KB, `postdocs.tsv`
por 132 KB, `groups.tsv` por 120 KB, `jobs.tsv` por 64 KB y `watchlist_closed.tsv`
por 50 KB. Sigue sin partirse **y con razón**: hacerlo obliga a tocar
`build_page.py` y `build_xlsx.py` en el mismo commit, y eso no se hace desatendido.
Corte natural sugerido, el mismo de las tres pasadas anteriores: internacionales
frente a españolas, o becas frente a premios y ayudas de viaje.

Y el apunte de entorno que sigue costando dinero: **no hay `pdftotext` y `pypdf`
está roto (`_cffi_backend`)**. Esta pasada **tres** ramas extrajeron PDF
descomprimiendo streams con `zlib` a mano, y ahí están los tres mejores hallazgos
del día: el articulado andaluz, las bases de la SES y las de Koplowitz. Ya es la
segunda semana que lo pide: merece ser un helper de `tools/`.

## Qué perseguiría la semana que viene

1. **F-0019 el 16 de octubre**: cerrarla y abrir la ronda del 15-04-2027, que es la
   alcanzable, con la condición SENC resuelta por delante.
2. **El resto del bloque autonómico por la BDNS** (SRC-0230, el endpoint de búsqueda
   que es el hallazgo operativo del día): Cataluña, País Vasco, Galicia, Castilla y
   León, Aragón, Navarra, Canarias y Murcia. Con una sola llamada salieron hoy cuatro
   programas; las frases cortas de título son la clave («posdoctoral» devuelve 0).
3. **Bases del Plan GenT2 por el DOGV** (F-0073), que es la única vía que queda, para
   poder puntuar la fila de verdad.
4. **La ventana de la SES entre el 27-10 y el 05-11**, mirando el campo `modified` de
   `/profesionales/becas-y-premios/` y `media?orderby=date`. Es la reapertura más
   cercana de todo el watchlist.
5. **Las 13 filas del watchlist sin tocar**, empezando por W-0001 (HFSP) y W-0015
   (MSCA PF 2027), que son las de mayor Fit con ventana en el primer trimestre de 2027.
6. **Los correos que ya no se pueden evitar**, y van cuatro semanas: BGA por el reloj
   de 7 años (F-0058), `secretaria.tecnica@ses.org.es` por cómo se cuenta el año de
   antigüedad (F-0046), y la SEQCML por la rotación externa de Medicina de Laboratorio.
   Las webs bloqueadas ya han dicho todo lo que iban a decir.
