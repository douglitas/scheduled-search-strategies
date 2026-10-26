# Pasada «fellowships» del 2026-10-26

Cinco ramas, las cinco completas. Sin incidencias de entrega: el `push` a `main`
entró directo (`eef455c..5d190c1`), sin rebase conflictivo y sin rama de rescate.
Gmail no se tocó: lo lee `positions`, que pasó ayer.

## Recuento, tomado de `git diff HEAD~1 --stat`, no de memoria

| fichero | altas | filas reescritas |
|---|---|---|
| `fellowships.tsv` | 3 (F-0083, F-0084, F-0085) | 34 |
| `watchlist_closed.tsv` | 2 (W-0028, W-0029) | 27 (todas) |
| `sources.tsv` | 11 (SRC-0353 a SRC-0363) | 0 |
| `subscriptions.tsv` | 2 (SUB-0037, SUB-0038) | 0 |
| `changelog.tsv` | 79 | 0 |
| `action_now.tsv` | — | 1 (solo F-0077) |

82 → 85 filas de fellowships, 27 → 29 de watchlist. Las 34 reescrituras y las 27
del watchlist cuadran exactamente con las bajas del diff (34 y 27): ningún
borrado no intencionado.

## Las tres cosas que de verdad mueven algo

**1. F-0077 (DMM Conference Travel Grant) cierra el 30-10, pero esa ronda NO es
la suya — y eso es una desescalada, no una urgencia.** Era la única fila de
`action_now` con plazo a cuatro días. La rama 4 verificó en Tier 1 que esa ronda
sólo financia viajes posteriores al 14-12-2026 y dentro de seis meses, y exige
resumen YA enviado; los resúmenes de la ESHG 2027 no abren hasta el 04-02-2027.
**La ronda correcta es la del 26-02-2027** (viaje a partir del 12-04-2027). El
calendario completo de rondas hasta nov-2027 y los documentos exactos quedan en
su `Next_Action`. No hay nada que hacer esta semana: es exactamente el tipo de
falsa urgencia que la lista corta debía dejar de producir.

**2. F-0008 (EMBO) es inelegible hoy, y presentarse sería irreversible.** Está
OPEN y verificada, corte 2027-01-22 14:00 CET. El bloqueo NO es el reloj del
doctorado —que le es favorable: basta tenerlo al inicio de la beca— sino la
regla de **un artículo de primera autora ya aceptado o publicado**. Sus dos
manuscritos están *en revisión*, que no cuenta, ni cuenta como preprint
revisado. Y la regla nueva, que es la que cambia la decisión: **desde la ronda
siguiente a ese corte EMBO prohíbe reaplicar**, o sea un único intento
vitalicio. Gastarlo en enero de 2027 siendo inelegible lo quemaría para
siempre. **El disparador es la aceptación del manuscrito, no el calendario.**

**3. F-0012 (Wellcome): el corte de pasado mañana no le cierra la puerta.** Las
ramas 2 y 5 lo leyeron por separado en Tier 1 y coinciden: lo que cambia el
29-10-2026 es la elegibilidad geográfica del **host**, no un plazo. Pasa de
RU + Irlanda + renta baja/media a **sólo RU** + renta baja/media de África, Asia
del Sur y Sudeste Asiático. El Reino Unido se queda, así que KCL, Cardiff y
Edimburgo —sus hubs naturales de genética psiquiátrica— siguen válidos; muere la
vía irlandesa, que no estaba usando. El esquema sigue sin plazos.

## Lo que cerró o bajó de nota

- **F-0006, la Caixa Junior Leader Retaining: Fit 4 → 2, y a watchlist (W-0028).**
  Era la fila más stale de la base (sin verificar desde el 23-08). El espejo
  universitario funcionó —la ficha del IRSJD dio las bases completas— y la
  noticia es mala: **ventana de doctorado 23-09-2019 a 23-09-2024**. Defendiendo
  en feb-2028 nunca estuvo en alcance, y no entra hasta la edición ~2031.
- **F-0013, MRC Early Independence Career Development: Fit 3 → 2, CLOSED.**
  Excluye a clínicos en activo... y los deriva al esquema de al lado, que es el
  hallazgo de abajo.
- **F-0064, Beca Nacional ESHG vía AEGH: Fit 2 → 1, inelegible.** Exige
  antigüedad de socia AEGH >2 años y «no más de 4 años de experiencia laboral
  postuniversitaria» (licenciada en 2019 = 7). El 15-11 es inalcanzable sólo por
  la antigüedad. **Conflicto reportado sin resolver:** la AEGH no define desde
  cuándo cuenta ese reloj; contado desde el doctorado ella entraría.
- **F-0004, Juan de la Cierva: corrección de fecha.** Hay DOS plazos y la fila
  tenía el equivocado: investigadores hasta el **26-11-2026**, no el 03-12 (ése
  es el del centro). Inelegible igualmente (ventana de doctorado 2024-2026).
- **F-0005, Ramón y Cajal: Fit 3 → 2.** Ventana 2016-2024: inelegible por tres años.
- **F-0018, ERC Starting Grant: la «StG 2027» ya se gastó y era esta misma fila.**
  El plazo 14-10-2026 ERA el ERC-2027-StG. La siguiente es ERC-2028-StG. Su
  horizonte real, contando desde la defensa: primera edición elegible
  **ERC-2031-StG**, última ERC-2035-StG.
- **F-0009, MSCA PF 2027 está cerrada para ella**: exige el doctorado en la fecha
  de cierre (08-09-2027) y defiende en feb-2028. El objetivo es PF 2028. Las
  fechas de 2027 siguen marcadas **(TBC)** por la propia Comisión, sin cambios.
- **F-0059 IBRO Rising Stars y F-0071 Research Partnership Kickstart**:
  inelegibles por estructura, anotado para no re-investigarlas.

## Lo que se añadió

- **F-0084, MRC Early Independence *Clinician Scientist* Fellowship (Fit 4).**
  El mejor hallazgo de la pasada. Salió al re-verificar F-0013: pide profesional
  sanitario registrado con doctorado, **permite sesiones clínicas** y no se le
  encontró techo de años post-doctorado. Está hecha para su forma de MD-PhD y es
  indulgente con su reloj. Queda LIKELY: `ukri.org` no se dejó leer y los plazos
  Tier 2 se contradicen.
- **W-0029, ESRS Short-Term Research Fellowship.** F-0081 ya tiene contenido:
  3 meses, máx. 2.800 EUR, **máx. DOS ayudas al año en toda Europa**, socia ESRS
  al solicitar y anfitrión de la ESRS Network con acuerdo **ya firmado**. Sin
  ventana de años post-doctorado: una de las pocas rutas de sueño abiertas a
  ella antes de feb-2028.
- F-0083 (BGA Rising Star Awards, Fit 2) y F-0085 (World Sleep Society, premio
  Christian Guilleminault, Fit 2), ambas de registro.

## Watchlist: 27 de 27 recomprobadas, ninguna ha reabierto

- **La ventana de la SES se abrió esta semana y aún no hay bases de 2027**
  (W-0012, W-0017, W-0026). Negativo verificado por dos vías. **Y el método
  heredado estaba descalibrado:** la pasada anterior anotó que `search=bases`
  devolvía dos ficheros, y hoy devuelve **uno**, así que la prueba del «tercer
  fichero» se estaba midiendo contra una línea base equivocada y la reapertura
  podía pasar desapercibida. Queda fichada una consulta sin `search=`, inmune al
  nombre del fichero. **Trampa adicional:** la página de becas de la SES sigue
  etiquetando las convocatorias de 2026 como «CONVOCATORIA ABIERTA» pese a haber
  cerrado el 25-01-2026 — etiqueta caducada, no apertura. **Hay que mirarlo cada
  pasada durante tres semanas.**
- Sin movimiento: W-0027 (SRSF, sello idéntico del 30-09), W-0020 (Junta de
  Andalucía, nada publicado y el patrón se ensancha: BOJA 23-12-2025 con
  ampliación en enero frente a BOJA 27-02-2024), W-0001 (HFSP sin calendario
  AY2028), W-0019 (SENC sin nada de 2027).
- **HFSP se contradice a sí misma**, reportado sin resolver: la página dice a la
  vez que el plazo de LOI del ciclo 2027 «has now passed» y que el portal de LOI
  «is now open». Confidence LIKELY. Dato útil: HFSP **no exige el doctorado al
  solicitar**, así que una LOI hacia mayo de 2027 encaja con la defensa de
  feb-2028 — el único flagship con disparador real en 2027, con el contrapeso de
  que obliga a cambiar de campo.
- **W-0014, One Mind:** confirmado en una línea, sin gastar llamadas. La
  inelegibilidad es estructural (excluye por nombre a *postdoctoral fellows* y
  exige profesorado en EE. UU.), no de calendario: nada puede cambiar esperando.
  **Se mantiene la propuesta de retirada; la decisión es suya, marcando
  `DISCARDED` desde la página.** Seis pasadas gastadas ya en esta fila.

## Corrección en `tools/` — guardarraíl de inelegibilidad

`tools/rebuild_action_now.py` metió **F-0008 en `action_now`**: Fit 4 y plazo a
88 días bastaban para la regla mecánica, aunque su propia fila dice INELIGIBLE.
El contrato es explícito —una convocatoria para la que no es elegible «goes
nowhere near action_now»— y el selector sólo sabía de Fit, plazo, estado y
competencia. Recomendar en la cabecera de la página algo que le quemaría un
intento vitalicio es peor que no recomendar nada, así que añadí un guardarraíl
deliberadamente literal: excluye sólo cuando la fila **afirma** la
inelegibilidad (INELIGIBLE / INELEGIBLE / NOT ELIGIBLE / NO ES ELEGIBLE / NO
ELEGIBLE). No interpreta relojes ni fechas —eso es trabajo de la rutina al
puntuar— y su único modo de fallo es dejar fuera de una lista corta una fila que
sigue entera y visible en su pestaña. Es la cuarta corrección de esta misma
familia en el fichero, tras las tres de P-0002.

**Aviso para las otras dos rutinas, porque el fichero es compartido:** el
guardarraíl se aplicará a sus bloques cuando ellas pasen, no antes. Medido hoy
sobre las 331 filas de oportunidad, declaran inelegibilidad 44, y las que podrían
salir de `action_now` por esto son de `positions`: **P-0001, P-0004, P-0025 y
P-0026**. Las cuatro dicen literalmente que no es elegible ahora, así que la
exclusión parece correcta, pero conviene que lo confirme quien lleve esa rutina.
Verificado además que **esto no genera falsas novedades**: la página construye
«Novedades» desde `Change_Flag`, no desde el diff de `action_now`.

## Lo que no se pudo verificar ni alcanzar

- **Bloqueos nuevos:** `biologists.com` está tras Sucuri y da 307 intermitente a
  WebFetch (con `curl` y user-agent de navegador responde 200; las rutas
  `/grants/...` están vivas). `erc.europa.eu/apply-grant/starting-grant`
  (SRC-0107) da **403** — se rodeó por CORDIS, fuente nunca usada en el repo,
  que además desmontó un dato Tier 2 erróneo de ventana 2017-2026.
  `geneticepi.org/awards` da 404: el IGES no publica sus premios de trainee.
- **Bloqueos confirmados, ya conocidos:** `esrs.eu` da 403 (tercer recurso sin
  verificar: F-0026 y W-0013 siguen UNVERIFIED), `lacaixafoundation.org` sin
  fetch, `es.emb-japan.go.jp` 403, `ashg.org` tras login de socia (F-0082 sigue
  UNVERIFIED). `fundaciontatiana.com` **no está bloqueada**: está renderizada con
  JS, el cuerpo sale vacío pero el HTML en bruto es legible — queda caracterizada
  y da la primera fuente Tier 1 de esa fundación.
- **Conflicto sin resolver:** el plazo de F-0073 (Plan GenT2), 27-10 según la UV
  frente a 22-10 según la UPV. No se abrió `ceice.gva.es`. Es Fit 2, así que no
  se gastó más en él.
- Sin verificar: el reloj y el requisito de mentor del BBRF (PDF que derrota al
  fetch), la lista de países elegibles de EMBO, los plazos de los premios BGA, la
  ventana de etapa profesional de Wellcome, y los plazos del fondo Guilleminault.
- **Trampa de duplicado esquivada:** la rama 3 casi dio de alta unas «Becas
  Postdoctorales en Neurociencia» de la Fundación Tatiana hasta ver que el título
  era el de la edición **2024** de F-0050. Anotado en W-0025.

## Filas que ella ya hubiera leído y cuyos hechos han cambiado

**Ninguna.** `owner_status.json` sigue vacío (`{}`), así que no hay ninguna marca
suya y ningún modelo mental que se haya quedado obsoleto por debajo. El
`Owner_Status = NEW` de muchas filas es el valor por omisión, no una lectura.

## Suscripciones pendientes

**38 de 38 en TODO.** Dos nuevas: **SUB-0038, alertas del UKRI Funding Finder**
(prioridad ALTA: es la vía de seguimiento de F-0084, el hallazgo de la semana) y
SUB-0037, alta de socia asociada de la BGA (prioridad MEDIA, desbloquearía los
plazos que hoy no se pueden leer por el 503). Sigue pendiente **SUB-0036, alta en
la ESRS**, que es la vía de F-0081/W-0029.

## Acciones de coste casi cero que siguen esperándola

1. **Alta de socia de la ESHG con validez para 2027** — requisito para disfrutar
   F-0023 (Fit 5, plazo 04-02-2027), no para solicitarla, pero tarda.
2. **Alta en la AEGH antes de fin de 2026** — el reloj de antigüedad de socia es
   lo que hoy la deja fuera de F-0064, y sólo corre si se da de alta.
3. **Los tres correos que ya van por la séptima semana**: la BGA por el reloj de
   7 años (F-0058, vía web agotada), `secretaria.tecnica@ses.org.es` por cómo se
   cuenta la antigüedad (F-0046), y la SEQCML por la rotación externa de Medicina
   de Laboratorio. Añádase ahora la secretaría de la AEGH por el reloj de F-0064.

## Dato que sólo ella puede dar, y que desbloquea dos flagships

**Los meses exactos de las estancias en QIMR Berghofer y en Japón.** Sin ellos,
MSCA y EMBO no pasan de LIKELY en movilidad y seguirán sin poder puntuarse en
firme, pasada tras pasada.

## Regla de tamaño

`fellowships.tsv` está en **268 KB**, cuatro veces y media el umbral de ~60 KB; y
`sources.tsv` en 271 KB, `changelog.tsv` en 378 KB, `groups.tsv` en 231 KB,
`postdocs.tsv` en 187 KB, `jobs.tsv` en 98 KB, `events.tsv` en 63 KB. Es una
situación de arrastre, no nueva de esta pasada, y **el corte lo hace ella**:
partir un fichero obliga a cambiar `build_page.py` y `build_xlsx.py` en el mismo
commit, y eso no es trabajo para el final de una pasada desatendida.

## Qué perseguiría la semana que viene

1. **La SES, en diario del 27-10 al 15-11**, con la consulta nueva sin `search=`:
   es la reapertura más cercana y la línea base ya está bien medida.
2. **Anclar F-0084 en Tier 1** (MRC Clinician Scientist): es el hallazgo con más
   valor de la pasada y sigue LIKELY con plazos contradictorios.
3. **`esrs.eu` por búsqueda restringida al dominio** para cerrar F-0026 y
   F-0081/W-0029 de una vez: tres recursos acumulados sin verificar por el 403.
4. **`biologists.com` con `curl` y user-agent de navegador**, ahora que se sabe
   que así responde 200: desbloquea las cuatro filas de Company of Biologists.
5. **HTML en bruto de los dos slugs vivos de Fundación Tatiana** para fechar la
   edición 2027, y el pendiente `fundacionjlc.es/wp-json/wp/v2/types`.
