# fellowships — pasada del 2026-09-28

Las cinco ramas completaron y el push fue directo a main (`fefd1c1`). El buzón lo
leyó positions a las 00:01 y no enrutó nada a FELLOWSHIPS; `data/source_inbox.json`
está vacío, así que no había trabajo de bandeja por mi parte.

Pasada de relojes, no de descubrimiento: **cero altas en grandes programas
europeos** y siete altas que existen casi todas para no volver a ser
redescubiertas. El valor está en tres fechas que pasan de estimación a hecho.

## Los números, del diff (`git diff HEAD~1`), no de mi memoria

| fichero | altas | modificadas |
|---|---|---|
| `data/fellowships.tsv` | 7 (F-0066 … F-0072) | 17 |
| `data/watchlist_closed.tsv` | 2 (W-0023, W-0024) | 8 de 22 |
| `data/sources.tsv` | 7 (SRC-0202 … SRC-0208) | — |
| `data/subscriptions.tsv` | 1 (SUB-0022) | — |
| `data/changelog.tsv` | 42 apuntes | — |
| `data/action_now.tsv` | 3 filas mías (antes 4); 25 ajenas preservadas | — |

Aviso sobre el diff de `action_now`: las 25 filas ajenas salen con **solo la
columna `Rank` cambiada**, y eso es inevitable, no un despiste. Al caerse F-0054
se renumera de 1 a N y las filas de ecosystem, que van detrás de las mías, se
desplazan un puesto. Lo verifiqué fila a fila: las únicas con cambios de contenido
son mis tres (F-0004, F-0019, F-0037). Si la página marca filas de ecosystem como
novedad de la semana, es este artefacto del renumerado.

## Las tres cosas que merecen acción

**1. F-0037 vence pasado mañana, y el bloqueo que la mataba tiene solución de una
sentada.** Cierre del **30-09-2026 confirmado Tier 1 hoy**, sin prórroga: 5 becas,
hasta 1.000 € de viaje más 1.500 €/mes por 3 meses, resolución a finales de
noviembre. Lo que desatasca la fila es que **el alta de socia de SEMEDLAB no se
hace en `semedlab.es`** (que sigue devolviendo 202 y ahora además sgcaptcha) sino
en `form.jotform.com/SEMEDLABFORMULARIOS/formulario-alta-de-socios`, online y de
una vez, con cuota de residente de 60 €. Queda fichado como SUB-0022. La pregunta
que decide la edición 2026 no es técnica: **¿cuenta un alta del 28-09 para un
plazo del 30-09?** Eso hay que preguntarlo por escrito a `secretaria@fundacionjlc.es`
hoy. Por si la respuesta es no, aparqué la edición 2027 en W-0023 (bases hacia
julio de 2027, cierre hacia el 30-09-2027, confianza MEDIA) para que la fila no
muera en silencio.

**2. F-0004 Juan de la Cierva: su primera convocatoria es la de 2028, no la de
2029. Duda cerrada, con el articulado en la mano.** Extracto **BOE-B-2026-31265**,
Resolución de 25-09-2026, y el PDF íntegro de bases descargado por la API de la
BDNS (código 918644). El art. 6.1.a exige defensa entre el **01-01-2024 y el
31-12-2026**, o sea ventana [año−2, año], que **admite tesis defendidas después
del cierre del plazo**: con defensa prevista en febrero de 2028, la convocatoria
de 2028 le sirve. 35.700 €/año, 3 años. El MIR no amplía el límite inferior, y
sigue en pie que la JdC exige centro distinto al de la formación predoctoral, lo
que excluye la Universidad de Murcia. En el mismo movimiento, **F-0005 Ramón y
Cajal pide 2016-2024, [año−10, año−2]**: obliga a ~2 años de posdoc, así que su
primera RyC es la de **2030** y la de 2029 la excluye.

**3. F-0008 EMBO: el 22-01-2027 es el último corte que no le quema el único
cartucho de su carrera.** La regla de una sola solicitud EMBO por investigadora
**no empieza en julio de 2027**, como decía la ficha, sino con la ronda de otoño:
se aplica a lo presentado **después del 22-01-2027 a las 14:00 CET**. Regla nueva
asociada: un laboratorio de acogida solo avala a una candidata por ronda.
Presentarse en enero de 2027 no consume el cupo; presentarse después, sí. Es una
decisión estratégica que hay que tomar antes de enero, y su cuello de botella
sigue siendo la aceptación del manuscrito empírico.

## Lo que cambió de estado

- **F-0054 Fulbright-Fundación Séneca: no estaba por abrir, llevaba abierta desde
  el 13-04-2026 y cierra el 02-10-2026.** Verificado Tier 1 en **fulbright.es**,
  no en `fseneca.es`, cuya página entera tiene dos hrefs y no publica detalle: eso
  explica los cuatro fallos de pasadas anteriores. 3.200 €/mes, 9-12 meses en
  EE. UU., hasta 3 ayudas. **No es elegible por dos motivos independientes**: pide
  doctorado en mano (defiende en febrero de 2028) y vinculación funcionarial o
  contractual con organismos de la Región de Murcia (está contratada en Málaga; la
  matrícula de doctorado en la UMU no cuenta). Fit 3 → 2 y **sale de `action_now`**,
  donde entraba por la regla de competencia LOW. Tampoco le sirve la edición de
  octubre de 2027: la primera viable es la de octubre de 2028, y solo si se
  trabaja una vinculación en Murcia (IMIB-Arrixaca o UMU) antes. Esto resuelve el
  aviso que la pasada anterior dejó abierto sobre esta fila.
- **F-0024 L'Oréal-UNESCO España: resuelta en negativo y VERIFIED.** Fit 2 → 1.
  Las bases **no** eran solo imagen: las páginas de requisitos tienen capa de
  texto y se extraen descomprimiendo streams con zlib. Exigen doctorado **más 4
  años desde la tesis**, una estancia pre/posdoctoral de **2 años** (las suyas son
  de 3 meses) y el área de la XXI edición es Físico-Matemáticas, Tecnología e
  Ingenierías. El plazo del 19-10-2026 es irrelevante para ella y no procede
  volver a mirarla antes de 2032.
- **F-0050 Fundación Tatiana/CINET: ANNOUNCED → CLOSED, y ahora con cifras.**
  40.000 € brutos anuales más 1.200 de viaje, seguro, 1.200 por hijo y 4.000 para
  congresos; 12 meses; **una sola beca**; ventana anual aproximada del 20-feb al
  1-jun. El requisito duro es **oferta firme de admisión del centro receptor en el
  momento de solicitar**. Ojo con la ficha: las fechas concretas que lleva
  (20-02-2025 / 01-06-2025) son de la edición de 2025 y vienen de **becas.com,
  fuente Tier 2 única**, de ahí que la fila quede en LIKELY. Lo que esto convierte
  en trabajo concreto de este curso es pedir la carta de acogida, no esperar la
  convocatoria.
- **F-0019 FENS/IBRO-PERC, consolidada y mejor descrita.** Cierre 15-10-2026
  reconfirmado por dos Tier 1: quedan 17 días. Competencia corregida de MEDIUM-LOW
  a **MEDIUM con base real**: la propia FENS publica 9 concedidas sobre 85 elegibles
  en abril de 2026 (~11%). Elegible **ya como doctoranda** (hasta 4.000 €, estancia
  de 4 semanas a 4 meses, cambio de país obligatorio); lo único que falla es no ser
  socia de la SENC, y para este programa **no hay reloj de antigüedad**. Exige carta
  de aceptación del host al solicitar, así que la ronda realista es la del
  15-04-2027. Sigue en `action_now`.
- **F-0059 IBRO Rising Stars: descartada definitivamente**, UNVERIFIED → VERIFIED.
  Es un premio de PI («first five years from first faculty appointment»), 15.000 USD.
  Fit 1, no volverá a salir. Las Exchange Fellowships de IBRO también quedan fuera:
  excluyen expresamente a quien reside en Europa y remiten al programa de FENS.
- **F-0044 Castaño-SEQC tesis doctoral: plazo por fin fijado**, 15-05, 7.500 €/año
  hasta 15.000 €, 4 ayudas. Exige **1 año de antigüedad en SEMEDLAB**, luego un alta
  hoy llega tarde a mayo de 2027: su primera edición elegible es la de **2028**.
  Aparcada como W-0024.
- **F-0009 MSCA: que no se confirmara nada es el dato.** 07-04-2027 y 08-09-2027
  siguen TBC en Tier 1 y el presupuesto aparece ahora como 388,57 M € (TBC), por
  debajo de los 399,05 M de 2026. Busqué FP10 restringiendo a dominios europa.eu:
  **no hay fuente Tier 1** que garantice una PF en 2028-2034, solo advocacy de la
  EUA (Tier 2). La decisión sobre adelantar la defensa sigue sin respaldo firme.
- **W-0022 → F-0054** y cinco filas de la watchlist suben a `Reopen_Confidence`
  ALTA con patrón verificado contra la fecha real de subida de los PDF: **W-0010**
  (la SRS dice por escrito «expected in January of 2027»; la fecha crítica es el
  envío de resúmenes de diciembre de 2026), **W-0012/W-0017** (bases el 03-11,
  cierre 25-01), **W-0019** (calendario en diciembre; además **los premios SENC son
  bienales**, luego abril de 2027) y **W-0021** (bases en enero).
- **Trampa documentada, que habría costado una pasada:** la web de la SES deja la
  etiqueta «CONVOCATORIA ABIERTA» puesta sobre convocatorias cuyo plazo venció el
  25-01-2026. La etiqueta miente; el plazo y el año de carpeta del PDF, no.

## Altas, y por qué casi ninguna es una oportunidad

Siete filas nuevas, de las que **cinco son cierres en negativo fichados para no
volver a gastar presupuesto en ellos**: F-0066 AuSpire (Fit 2 — sí existe un
instrumento España-Australia, es MSCA COFUND de RMIT Europe con 28 becas hasta
2030, pero son plazas de acogida **en** España y la regla de movilidad excluye a
quien vivió aquí más de 12 meses en 3 años), F-0067 One Mind Rising Star (Fit 2),
F-0068 rotaciones de la FEPSM y F-0069 predoctorales de Tatiana (Fit 1), y F-0070
y F-0071 de The Company of Biologists (Fit 1: las **solicita el profesorado junior
receptor**, no la visitante, y las ECR Visiting son del ámbito del Journal of
Experimental Biology — hipótesis de la pasada anterior cerrada en negativo).
La única con futuro es **F-0072, Estancias Cortas de la Fundación Alicia Koplowitz**
(3.000-4.000 €/mes, neurociencias infanto-juveniles, de lleno en su línea 3), Fit 3:
la modalidad que le sirve exige ser posdoctoral, luego no antes de febrero de 2028,
y bases y plazo quedan UNVERIFIED porque la web solo lista beneficiarios.

## Decisiones que tomé yo, como orquestador

- **F-0019: deshice un duplicado antes de que entrara.** La rama 4 propuso las
  FENS/IBRO-PERC Exchange Fellowships como fila nueva sin ver que ya existían como
  F-0019, que la rama 1 había refrescado en paralelo. Convertí su contenido en un
  update de la fila original y descarté el alta: una convocatoria anual conserva su
  ID. Queda escrito en el `Source_Note`.
- **F-0054: dos ramas, una gana por jerarquía de fuentes.** La rama 2 la dejaba
  ANNOUNCED y UNVERIFIED; la rama 5 la verificó en Tier 1 con fechas. Mandan los
  datos de la rama 5 en todas las columnas solapadas, y conservo el Fit 2 de la
  rama 2, que es coherente con la inelegibilidad que ambas describen.
- **F-0067 One Mind: rebajé el Fit de 3 a 2 contra la propuesta de la rama 3.** No
  es que le falte esperar la tesis: la rama 5 verificó en Tier 1 que exige ser
  investigadora independiente ya contratada como Assistant o Associate Professor y
  estar dentro de los 8 años desde ese nombramiento. Es exclusión estructural, y
  excluye por nombre a doctorandas y posdoc. La diana temática sigue siendo de las
  más limpias para su línea 2, así que la fila se queda documentada.
- **No borré ninguna fila, aunque la rama 5 propuso dos retiradas fundadas.**
  W-0014 One Mind (inelegible estructural, consume presupuesto cada semana) y la
  fusión de W-0012 en W-0017 (son la misma convocatoria de la SES, duplicada en la
  siembra). Ambas propuestas quedan escritas en el `Notes` de sus filas con la cita
  oficial: **borrar filas no es trabajo que haga una rutina desatendida**, es
  decisión tuya. Si las aceptas, la watchlist baja de 24 a 22.
- **Acepté SUB-0022 (alta de SEMEDLAB) pese a que la pasada anterior descartó una
  suscripción parecida.** Entonces se descartó porque SUB-0009 ya cubría la
  organización; ahora el hallazgo es distinto y operativo: la URL del formulario que
  de verdad funciona, y es el único bloqueo entre ella y F-0037. SUB-0009 apunta a
  una página sin formulario y queda de hecho sustituida, pero no la toco: el fichero
  es de solo apéndice y su columna Status es historia.
- **No refresqué en bloque el `Last_Checked` de las fuentes ya existentes.** Las
  ramas reportan URLs, no IDs de fuente, y no voy a estampar como visitadas filas
  que no puedo atribuir. Solo llevan fecha de hoy las siete nuevas.

## Lo que no pude verificar, y los bloqueos

Bloqueos **nuevos**, fichados para no redescubrirlos: `cinetcenter.com` (cuerpo
vacío, mismo patrón que `fundaciontatiana.com`), `juntadeandalucia.es/organismos/…`
(**CONNECTION RESET**, curl 35), `sps.ed.ac.uk` (403) y el captcha de
`semedlab.es`. Ya conocidos y no reintentados: `esrs.eu`, `bga.org`, `wellcome.org`,
`aei.gob.es`, `isciii.es`, `nhmrc.gov.au`, `ispg.net`, la Caixa.

- **Wellcome (F-0012): el conflicto no solo sigue abierto, ha empeorado.** Tres
  espejos británicos independientes se contradicen entre sí (catch.ac.uk da cierre
  el 21-07-2026; Bristol habla de plazos en febrero, mayo y octubre;
  globalhealth.ox da el 22-07-2026), y la atribución del 10-11 al financiador frente
  al 16-11 «interno» es incoherente, porque un plazo interno no puede ir después del
  del financiador. **No toqué `Deadline`.** Recomendación: dejar de abrir espejos
  universitarios, que es tirar presupuesto, y probar el UKRI Funding Finder o
  preguntar a KCL o Cardiff.
- **F-0052 Junta de Andalucía: la Orden de 24-10-2023 está localizada** (BOJA nº 209
  de 31-10-2023) tras dos pasadas perdida, y **no contiene la ventana de años**: va
  en cada resolución de convocatoria, o sea hay que abrir `boja/2025/246/9`, la
  resolución, no el extracto `/10`. A cambio apareció un dato que refuerza su Fit 4:
  las universidades públicas deben comprometer una plaza de ayudante doctor al
  acabar la ayuda.
- **F-0058 BGA sin tocar a propósito**, `Last_Verified` intacto en 2026-09-21: el 403
  persiste y no existe espejo ni PDF del reglamento. El reloj de 7 años solo lo
  resuelve un correo a la BGA.
- **F-0026 ESRS**: no gasté ni una llamada (bloqueo declarado tras cuatro pasadas) y
  la vía Tier 2 no dio nada actual, así que **no está en updates**. Sigue necesitando
  que la abras a mano o se retira.
- **W-0020 Junta de Andalucía, la de ventana más cercana, no verificada** por el
  CONNECTION RESET. Queda BOJA por fechas o BDNS.
- Filas de la watchlist no alcanzadas, con su `Last_Checked` viejo intacto: W-0001,
  W-0002, W-0003, W-0004, W-0006, W-0007, W-0009, W-0011, W-0020; y por reparto entre
  ramas, W-0005, W-0008, W-0013, W-0015, W-0016.
- Filas de fellowships no alcanzadas, `Last_Verified` sin tocar: F-0006, F-0010,
  F-0011, F-0013, F-0014, F-0015, F-0016, F-0022, F-0045, F-0047, F-0053, F-0055,
  F-0056, F-0057, F-0027, F-0028, F-0030, F-0031, F-0036, F-0058, F-0060, F-0061,
  F-0062, F-0063, F-0026. **El bloque autonómico español lleva sin tocarse desde el
  31 de agosto**, dos pasadas ya: el presupuesto se fue en los dos ítems que el
  propio prompt marcaba como más valiosos (JdC/RyC y Fulbright), y creo que fue la
  decisión correcta, pero la deuda existe.

## Datos tuyos que faltan y que deciden filas

Siguen siendo los mismos dos, y cada semana bloquean más filas: **de qué sociedades
científicas eres ya socia y desde cuándo** (la SES exige 1 año de antigüedad, la SRS
membresía en regla, F-0019 pide SENC sin reloj, F-0044 pide un año en SEMEDLAB) y tu
**fecha de nacimiento** (las bolsas de viaje de la AEGH dependen enteramente del
límite de 35 años). Ninguna rama ha adivinado: está escrito en
`Eligibility_Key_Conditions` de cada fila afectada.

## Nada que hubieras marcado ha cambiado bajo ti

`owner_status.json` sigue vacío `{}`. En `fellowships.tsv` no hay ni una fila con
`Owner_Status` distinto de `NEW` o vacío, así que ninguna de las 17 modificaciones
de hoy cae sobre algo que ya hubieras leído y decidido. `apply_rows.py` rechaza esa
columna por diseño y lo verifiqué comparando con `HEAD`: cero alteraciones.

## Suscripciones pendientes

Las **22**, todas en TODO y ninguna con marca tuya en `owner_status.json`. La de
mayor rentabilidad esta semana es la nueva **SUB-0022 (alta de socia de SEMEDLAB)**,
porque es literalmente el único bloqueo entre ella y F-0037, que cierra el 30-09; y
detrás, **SUB-0003 (SENC)**, que es la única condición que falla en F-0019.

## Mantenimiento, que ya es urgente

`data/fellowships.tsv` pasa de 186 KB a **210 KB, tres veces y media el umbral de
~60 KB**; `sources.tsv` va por 137 KB y `changelog.tsv` por 144 KB. Sigue sin
partirse y con razón, porque hacerlo obliga a tocar `build_page.py` y
`build_xlsx.py` en el mismo commit y eso no se hace desatendido: es tarea tuya.
Corte natural sugerido, el mismo de la pasada anterior: internacionales frente a
españolas, o becas frente a premios y ayudas de viaje.

Y el apunte de entorno que sigue costando dinero cada semana: **no hay `pdftotext` y
`pypdf` está roto (`_cffi_backend`)**. Esta pasada dos ramas extrajeron PDF
descomprimiendo streams con `zlib` a mano y **ahí están los dos mejores hallazgos
del día** (el articulado de la JdC y las bases de L'Oréal). Merece ser un helper de
`tools/`: la lección concreta es que **antes de declarar «escaneo sin capa de texto»
hay que probar el zlib**, porque con L'Oréal esa declaración era falsa y nos costó
una pasada.

## Qué perseguiría la semana que viene

1. **El desenlace de F-0037**: si el alta en SEMEDLAB llegó a tiempo y qué contestó
   la fundación. Si no llegó, reprogramar a W-0023 en vez de dejar la fila vencida.
2. **La resolución andaluza `boja/2025/246/9`** (F-0052 y W-0020), que es donde vive
   la ventana de años, y el **bloque autonómico español**, con dos pasadas de retraso.
3. **Wellcome por otra vía**: UKRI Funding Finder o correo a KCL/Cardiff, en vez de
   un cuarto espejo universitario.
4. **La página de topic HORIZON-MSCA-2027-PF-01** del Portal de Financiación, que es
   la vinculante (probar la API SEDIA por POST), y el texto de la propuesta
   legislativa 2028-2034 para el agujero de FP10.
5. **Los correos que ya no se pueden evitar**: BGA por el reloj de 7 años (F-0058),
   `becas.neurociencia@fundaciontatiana.com` (F-0050) y `seneca@fseneca.es` por las
   bases de F-0054. Cuatro pasadas peleando con webs bloqueadas dicen que la vía es
   esta.
6. La tercera pieza de la SES (ayuda de estancia de 1.500 €), que la rama 5 vio y no
   fichó por reparto de ramas, y los cuatro programas Fulbright postdoctorales con
   fecha oficial de apertura (Ministerio en enero de 2027, CSIC en febrero,
   Extremadura en abril).
