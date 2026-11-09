# ecosystem — 2026-11-09

Sin ALERTA: el repo estaba donde debía, las cuatro ramas entregaron, el push
fue directo a `main` y los dos buzones de respaldo quedan vacíos. Una nota de
footing, porque no es trivial: el checkout llegó con el `HEAD` **desprendido**
de `refs/heads/main`. Se corrigió antes de tocar nada; si hubiera trabajado
así, el commit habría quedado colgado sin rama y la CI no habría regenerado la
página.

## Lo que cambió, contado desde `git diff --stat HEAD~1`

| Pestaña | Antes | Después | Altas | Actualizadas |
|---|---|---|---|---|
| groups | 96 | 113 | 17 | 14 |
| events | 36 | 38 | 2 | 15 |
| training | 34 | 37 | 3 | 14 |
| sources | 457 | 472 | 15 | — |
| subscriptions | 45 | 47 | 2 | — |
| action_now | 54 | 62 | 55 mías, 7 ajenas preservadas | — |

65 apuntes de changelog, que es exactamente 22 altas + 43 actualizaciones.
Las bajas del diff (14 en groups, 15 en events, 14 en training) coinciden una a
una con las filas actualizadas: no se borró nada por accidente.

## Las tres cosas que merece la pena hacer esta semana

**1. El late-breaking del ASCS 2027 (E-0029) es lo único con reloj corto.**
El plazo ordinario de pósteres cerró el 28-10-2026 y eso ya no tiene vuelta.
Queda una sola puerta: la ventana late-breaking **abre el 27-11-2026 y cierra
el 13-12-2026**, diecisiete días. Lo que hay que hacer ahora es tener el póster
de primera autora listo *antes* del 27-nov (sirve el empírico del proyecto
QIMR) para enviarlo el día que abra. Dos trampas confirmadas en Tier 1, y las
dos cuestan dinero: las notificaciones de beca de viaje salen el 03-12-2026,
o sea con el ciclo ordinario y **no** con el late-breaking, así que conviene
marcar la casilla pero no contar con el dinero; y la tarifa anticipada cierra
el 20-12-2026, **un día antes** de saber si le aceptan el póster (21-12). O se
inscribe a ciegas en tarifa anticipada o paga la normal. Sí es elegible para la
beca: la SRS define *trainee* incluyendo explícitamente a residentes médicos.

**2. Boulder (T-0001) está abierto, y hay que escribir un correo antes de pagar.**
Se cerró el pendiente de la semana pasada: el registro **se abrió**, se vende en
Humanitix a 850 USD (≈782 EUR), con reembolso hasta 30 días antes y
cancelaciones no reembolsables sólo desde el 01-02-2027. Pero **la ficha de la
entrada dice que la elegibilidad se limita a instituciones con dirección en
EEUU**, mientras la página oficial del taller no impone nada parecido y el
taller se llama «International». No lo resuelvo eligiendo una versión: la
acción es un correo de cinco líneas a `ibgworkshop@colorado.edu` preguntando si
una participante con afiliación española compra esa misma entrada, **antes** de
soltar 850 USD. En paralelo y sin esperar respuesta: pedir los cinco días de
permiso en el hospital para el 1-5 de marzo y tramitar la ESTA.
El mapa de ayudas, ahora completo, dice que **ninguna de las tres le sirve**:
la ayuda por necesidad es sólo para ciudadanos y residentes permanentes de
EEUU; el ISCEP está cerrado para 2027 y además limitado a países sin exención
de visado; y el programa de registro temprano descubierto esta semana (200 USD,
10 plazas) exige pasaporte de un país **sin** exención de visado, así que España
queda fuera justo por lo que le simplifica el viaje. Queda registrado en
negativo para no volver a perseguirlo.

**3. La línea 3 ha dejado de ser un punto ciego, y la mejor puerta ya estaba en la tabla.**
El hallazgo que más vale no es una fila nueva: **Alexandra Havdahl (L-0021) es
la Directora Científica de MoBa**, no una PI que usa MoBa. Es la entrada más
potente del repositorio para el sueño de 0-3 años, en Noruega, sin visado. Las
dos altas Fit 5 van en la misma dirección: **Laurie Hannigan** (L-0097, grupo
PaGE, Oslo), genética estadística de fenotipos conductuales repetidos en MoBa
con sólo PLINK y R, que es literalmente su caja de herramientas; y **Desana
Kocevska** (L-0098), PRS de insomnio y duración del sueño sobre ítems de sueño
infantil desde los 18 meses — la fila más valiosa y la peor verificada, porque
`nin.nl` dio 404 y queda UNVERIFIED.
Aviso operativo: el NIPH de Oslo acumula ya cuatro contactos (Havdahl,
Pettersen, Hannigan, Jennifer Harris). **Un solo correo coordinado, no cuatro.**

## Qué cerró

- **T-0005 CAJAL Neurobiology of Sleep → CLOSED**, plazo vencido en agosto.
- **E-0029 ciclo ordinario** cerrado el 28-10-2026 (queda el late-breaking).
- **T-0024 SISG y T-0004 Wellcome**: verificados *en negativo*, sin edición 2027
  publicada. SISG abre ciclo en enero.
- Sin movimiento, comprobado y no inventado: **WCPG 2027 Brisbane** sigue en
  «coming soon» con el ECIP apuntando todavía a 2026; **EMGM 2027** sigue «to be
  announced» y aún piden voluntarios para organizarla; **IGES 2027** sin
  anuncio; **LABCLIN 2027** sin rastro, así que no se abrió fila.

## Conflictos que dejo abiertos en vez de elegir en silencio

1. **Elegibilidad de Boulder** (ficha de la entrada vs. anuncio oficial), arriba.
2. **T-0032 Neuromatch**: confirmadas las fechas 5-23 jul 2027, pero la página
   **ya no publica** el plazo 17-03-2027 que constaba como VERIFIED. Se ha
   **vaciado** `Deadline` en lugar de conservar una fecha sin respaldo. Además
   choca en fechas exactas con T-0033 (CAJAL NeuroAI).
3. **E-0015 AEGH**: la web oficial lista la XVII Jornada con tema nuevo y día 7
   de mayo, pero **no confirma año ni Bilbao**: la sede se sostiene sólo en
   Tier 2.
4. **Behavior Genetics**: Springer sigue listando a John K. Hewitt como
   Executive Editor mientras fuentes Tier 2 dan a Valerie Knopik desde 2025.
   **No escribir a L-0103 sin confirmar el cargo.**
5. **E-0013 World Sleep 2027** no tiene un plazo sino **tres**: envíos abren
   01-12-2026, fast-track 20-01-2027, oral 15-05-2027 y póster 15-07-2027. El
   de póster cae ya fuera de la residencia.

## Lo que no se pudo verificar ni alcanzar

Bloqueos, un intento cada uno: `esrs.eu` (403, dos páginas) y el catálogo CAJAL
(interstitial de Cloudflare) → T-0030 y T-0033 quedan UNCHANGED; `nature.com` y
`link.springer.com` redirigen a portales de identidad; Wiley / *Journal of
Sleep Research* 403; `le.ac.uk` 403; UCL 403; `nin.nl` y la página personal de
Hannigan 404; `mendelianrandomization.org.uk` 503 (**bloqueo nuevo**);
`profiles.stanford.edu/laramie-duncan` 503 por segunda semana (L-0025 sigue sin
nada verificado); `vipbg.vcu.edu/people/` 503 (**bloqueo nuevo**);
`labclin2026.es` responde sin contenido legible. Rutas inválidas detectadas:
`ashg.org/meetings/2027-meeting/` y `congreso-ses.com/ses2027/fechas-importantes`
dan 404. No se gastó presupuesto en `semedlab.es`.
**Dos notas de bloqueo estaban caducadas y se corrigieron**: `bga.org` y
`geneticepi.org` **sí** responden hoy (antes 403 y 503).
Por eso van UNVERIFIED: L-0098 Kocevska, L-0102 Dudbridge, L-0103 Knopik,
L-0110 Gui, T-0035 UCL y T-0037 FSL.
Sigue **sin confirmar** la institución de **L-0096 Pettersen**: una búsqueda por
nombre completo no devuelve ni una página, y queda escrito así en la ficha.
Las 6 vacantes del IoPPN del 02-11 **siguen sin inspeccionar**; no se presentan
como negativo.

## Instituciones Tier 1: cerradas 6 de 8

Confirmadas Kendler (**Director** del VIPBG, más de lo que decía la ficha),
Bacanu, Baune (dirige Psiquiatría de Münster desde 2019), Edenberg (Indiana,
PI nacional del COGA), y suben a LIKELY Chunyu Liu (SUNY Upstate, con R01
activo) y Raventós (CIBCM-UCR). **Corregida una entidad mal escrita**: L-0094
decía «University of Greifswald» y la correcta es **Universitätsmedizin**
Greifswald, grupo de Hans J. Grabe.

## Filas cuyos hechos cambiaron bajo ella

**Ninguna estaba marcada por ella**: `owner_status.json` sigue siendo `{}`, es
decir que todavía no ha marcado nada desde la página, y el `Owner_Status = NEW`
que se ve en el TSV es el valor por defecto, no una lectura suya. Así que esta
semana no hay modelo mental que se haya quedado viejo. Dicho eso, si ya había
leído estas fichas, las que más se le han movido son **L-0084** (Mitchell: ya no
hay que ser cauto con el horizonte de financiación — cinco fuentes activas,
incluido un CRE del NHMRC que llega hasta ~2028, y la recomendación cambia a
«escribir ya, no esperar anuncio»), **L-0018** (Uppsala: financiación y correo
del PI pasan de UNKNOWN a verificados, ≥21 M SEK concedidos en 2024-2025, y el
PI invita explícitamente a que los postdocs escriban), **L-0021** (Havdahl, por
el cargo en MoBa), **L-0091**, **L-0094**, **L-0080** y **L-0081**.
El `Fit` de L-0018 se mantiene a propósito en 4: cae el riesgo de financiación,
pero la razón de fondo sigue siendo la técnica, porque el proyecto nuevo de
Wallenberg está formulado alrededor de EEG y machine learning.

## Suscripciones pendientes: las 47

`owner_status.json` está vacío, así que **ninguna** tiene marca suya y las 47
cuentan como pendientes por la definición del contrato. Las dos altas de esta
pasada son **SUB-0046** y **SUB-0047** (World Sleep Society, y aviso de nuevo
número de *Twin Research and Human Genetics*, que es el único circuito gemelar
del desarrollo sin cubrir). La rama de formación entregó **cero** a propósito:
la única que tenía sentido, la lista del FSL Course, no permitió verificar su
URL exacta de alta y no se inventó.
Con reloj entre las ya existentes: **SUB-0009 y SUB-0022** (alta de socia de
SEMEDLAB) siguen en TODO y son justo lo que bloquea el canal de la vacante
POCT, que vence con su residencia el 22-05-2027.

## Respaldo: los dos buzones quedan limpios

`source_inbox.json` llegó vacío (`[]`). `inbox_triage.tsv` tenía **una** fila
PENDIENTE, la vacante de residente en la Comisión POCT de SEMEDLAB enrutada a
ECOSYSTEM el 08-11. Se cierra como DONE con la resolución anotada: **no es
verificable desde la web abierta** (la búsqueda no devuelve ninguna convocatoria
indexada y `semedlab.es` no entrega contenido al acceso automatizado, coherente
con el bloqueo ya registrado). **No se abrió fila** en groups/events/training a
propósito: es un puesto de representación de residentes en un grupo de trabajo
de una sociedad, no un grupo de investigación, ni un congreso, ni formación, así
que no cabe en ninguna pestaña de esta rutina. La acción queda en su lado y
tiene reloj. Nada acaba la semana en PENDING.

## Mantenimiento — noveno aviso, y ya son NUEVE ficheros

Tomado de `ls -l data/` después del push, no de la semana pasada. Por encima
del umbral de ~60 KB: `changelog.tsv` 511 KB, `groups.tsv` 402 KB,
`sources.tsv` 376 KB, `fellowships.tsv` 353 KB, `postdocs.tsv` 214 KB,
`jobs.tsv` 102 KB, `events.tsv` **79 KB**, `training.tsv` **76 KB** y
`watchlist_closed.tsv` 63 KB.
**Dos lo cruzaron esta semana**: `watchlist_closed.tsv`, como se anunció, y
`training.tsv`, que no estaba avisado. Y `events.tsv` ha pasado de 64 a 79 KB
de golpe, porque las 15 actualizaciones de esta pasada traen celdas de
`Next_Action` y `Confidence` muy largas: el fichero crece ahora más por
longitud de texto que por número de filas.
**El troceo lo hace una persona**, porque exige tocar `tools/build_page.py` y
`tools/build_xlsx.py` en el mismo commit, y eso no se hace sin vigilancia al
final de una pasada.
Observación que ya no es teórica: con 113 filas, leer la tabla de grupos se
come un trozo real del presupuesto de la rama 4, y por eso esta semana sólo
cerró 14 fichas de 113.

## Qué perseguiría la semana que viene

1. **Havdahl en Tier 1** y el correo único coordinado al NIPH: es la mejor
   puerta a la línea 3 y ahora mismo se sostiene en Tier 2.
2. **Confirmar la afiliación 2026 de Kocevska** (L-0098, Fit 5 y UNVERIFIED) por
   otra ruta que no sea `nin.nl`.
3. **La cola de 11 fichas Fit 5 sin tocar**: Medland, Middeldorp, Mullins,
   Cheesman, Cai, Guintivano, Sofer, Ronald, Peterson, Yengo.
4. **Las 6 vacantes del IoPPN** paginando a mano, que llevan dos semanas sin ver.
5. **Las cohortes sin tocar** (ALSPAC, Generation R, Born in Bradford,
   Generation Scotland, Danish National Birth Cohort) buscando quién custodia
   los fenotipos de sueño de 0-3 años.
6. **Southampton**: tres plazas de epidemiología genética con cierres 18-11,
   03-12 y 04-12-2026 en una unidad sin ficha — aviso para la rama de
   descubrimiento y para la rutina de *positions*.
7. **La respuesta de `ibgworkshop@colorado.edu`** y el anuncio de LABCLIN 2027.
