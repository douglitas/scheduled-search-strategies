# Pasada ecosystem — 2026-11-02

Rutina: ecosystem (grupos, eventos, formación). Última rutina de la mañana.

**Aviso de arranque, no es una alerta de fallo pero conviene saberlo:** el
checkout llegó con `HEAD` **desprendido** de `refs/heads/main`. Se corrigió
antes de tocar nada (`git checkout main` + `git pull --rebase`) y la pasada
salió de la punta real de main, el commit de fellowships de las 06:22. Si
vuelve a pasar cada semana, es un síntoma del arranque del contenedor, no de
esta rutina.

**Obligaciones de respaldo, cumplidas y esta vez con trabajo ajeno de por
medio:** `data/inbox_triage.tsv` cierra la semana con **0 filas PENDING** y
`data/source_inbox.json` está vacío (`[]`, releído al final por si ella había
añadido algo durante la pasada). La fila que positions dejó abierta el
2026-11-01 y que la pasada de fellowships de esta mañana no cerró —se limitó a
anotar `semedlab` como «rodeo que queda por probar»— se ha resuelto aquí con
fuente Tier 1. Ver más abajo.

## Cifras, tomadas de `git diff HEAD~1 --stat`, no de memoria

| Pestaña | Altas | Actualizadas |
|---|---|---|
| groups | 15 (L-0082 … L-0096) | 9 |
| events | 3 (E-0034 … E-0036) | 7 |
| training | 3 (T-0032 … T-0034) | 5 |
| sources | 15 (SRC-0414 … SRC-0428) | — |
| subscriptions | 0 | — |
| changelog | 57 apuntes | — |
| inbox_triage | — | 1 (PENDING → DONE) |

`action_now`: 47 filas mías (antes 41), 5 filas ajenas preservadas intactas,
52 en total. **Total: 21 altas y 22 filas actualizadas.** 162 inserciones,
63 supresiones.

Cuadra sin pérdida, y lo compruebo en vez de afirmarlo: las 63 supresiones son
exactamente las 22 filas modificadas (9 groups + 7 events + 5 training + 1
inbox_triage) más las 41 filas propias que `action_now` reescribe al renumerar
el Rank. Recuento de líneas HEAD contra disco: groups 82→97, events 34→37,
training 32→35, sources 414→429, changelog 1301→1358, action_now 47→53,
inbox_triage 7→7, subscriptions 44→44. Ninguna fila perdida.

## Las tres cosas que merecen acción, y por qué

**1. BOULDER SE HA DESBLOQUEADO Y EL RELOJ ES MAÑANA. T-0001, Fit 5.**
Esto es el hallazgo de la pasada y por eso salió un aviso al móvil. La página
de anuncio que llevaba semanas dando 404 **existe**: el patrón de ruta cambió,
el año pasó de sufijo a prefijo —`/ibg/2027-workshop/2027-isg-workshop-announcement`
en vez de `/ibg/workshop-2027/workshop-2027-announcement`—, así que el 404 de
las pasadas anteriores nunca significó «sin publicar» sino «ruta equivocada».
Lección de método: cuando una URL conjeturada da 404 varias semanas seguidas,
el fallo puede estar en la conjetura.
**Verificado dos veces, por la rama y después por el orquestador en la misma
página Tier 1 antes de avisarla:** el registro **abre a las 12:00 GMT del
3-nov-2026** (13:00 en Madrid) en `events.humanitix.com/2027-isgw`; cuota
**850 USD** con tarjeta, no los 550 que llevaba la ficha; taller **1-5 de marzo
de 2027** en Boulder, St. Julien Hotel.
**Corrección honesta a lo que trajo la rama:** la página **no** publica plazo
de cierre y **no** dice que sea por orden de llegada. La fila lo decía como
hecho y se ha reescrito: lo prudente es registrarse el día 3, pero el cupo no
se afirma. El único cierre que la página publica es que las cancelaciones no
se reembolsan después del 1-feb-2027, lo que acota el riesgo de registrarse ya.
**La ayuda económica la excluye**, verificado: 10 becas con cuota reducida a
200 USD y hasta 1.000 USD de reembolso, plazo 30-nov y resolución el 3-dic,
pero **restringidas a ciudadanos y residentes permanentes de EEUU**. El ISCEP
está cerrado. Lo paga entero. Hace falta pedir cinco días en la residencia y
tramitar ESTA.
El contenido justifica el gasto: es la edición trienal de genética latente y
el programa cubre entera su laguna de métodos que no ha corrido ella misma
—OpenMx, GCTA, LD score regression, genomic SEM, PRS, MR—.

**2. T-0032 Neuromatch Academy CompNeuro 2027, Fit 5, y es la mejor noticia
estructural del mes.** Online, 5-23 de julio de 2027, Python 8 h/día,
solicitudes del 10-feb al 17-mar-2027, con matrícula ajustada por país y
*tuition waivers*. Cierra **dos** lagunas del perfil a la vez, las dos que más
le cierran puertas: neurociencia computacional independiente (hoy sólo nivel
supervisado) y Python profesional no asistido por IA. Sin visado, sin viaje, y
cae **después** del fin de la residencia (22-may-2027). Fuente estrenada:
`neuromatch.io`.
Contraste que importa para no perder el tiempo: **CAJAL reabrió** tras semanas
de 503 y la noticia es mala —su catálogo 2027 **no tiene ningún curso de
neurociencia computacional ni de sueño**—. Queda NeuroAI (Lisboa, julio 2027),
fichado con Fit 3. Es decir, Neuromatch sustituye a CAJAL como vía realista a
esa laguna, que era la recomendación nº 3 de la semana pasada.

**3. L-0069 Olfson pasa a VERIFIED y de «preguntar algún día» a «escribir esta
semana».** Era la ficha Fit 5 con confianza LIKELY que había que cerrar, y se
cerró con dato duro: **R01 propia nueva, 1R01MH145308, «Parent-child trio study
of pediatric anxiety disorders», del 10-09-2026 al 31-08-2031**, más su K08
hasta el 30-06-2027. Correo verificado, `emily.olfson@yale.edu`. Cubre
febrero de 2028 de sobra, y un laboratorio pequeño contrata en los primeros
meses de una R01, así que la urgencia es real y no retórica. El gancho mejora
además: un diseño de **tríos** en ansiedad pediátrica es el puente más corto
que existe entre su línea 3 (sueño infantil) y su línea 2 (GWAS/PRS
psiquiátrico), y ella es MD-PhD escribiendo a una MD-PhD cuyo doctorado fue
en genética humana y estadística.

## El respaldo del buzón, resuelto con fuente Tier 1

La convocatoria que positions encontró dentro de un digest de LinkedIn es la
**Ayuda para un Proyecto de Investigación Multicéntrico de la Fundación
SEMEDLAB** (antes Fundación José Luis Castaño-SEQC): **20.000 EUR** en tres
tramos, estudio prospectivo multidisciplinar de 3 a 6 centros. **Es un
instrumento distinto** de F-0037, F-0044 y F-0045 y tampoco es la «Ayudas para
proyectos de investigación» anual que la fundación lista aparte: financia un
consorcio, no formación individual.
**No es elegible ahora, y es un negativo útil, no un fallo:** el IP y al menos
un tercio de los coinvestigadores deben ser socios de pleno derecho de SEMEDLAB
con un año de antigüedad, con un socio en cada centro. Siendo residente y sin
esa antigüedad no puede ser IP; sólo encajaría como coinvestigadora, o más
adelante tras la especialidad. Ventana: abierta todo el año con cierre el 31 de
octubre; **el ciclo 2026 ya cerró**, lo vivo es el que cierra el 31-oct-2027.
La fila queda DONE con esa resolución en el `Summary` y firmada
`positions; ecosystem`. **No se ha fichado en `fellowships.tsv` porque esa
pestaña no es mía**: queda la fuente SRC-0428 para que la rutina de
fellowships la recoja, y lo señalo aquí para que no se pierda entre dos beats.

## Lo que se cierra, se confirma o se descarta

- **Conflicto de BGA 2027 RESUELTO** (abierto dos semanas): `bga.org` volvió a
  responder y la reunión es **29-jun a 2-jul-2027 en Minneapolis**, anfitrión
  Scott Vrieze, programa Sarah Medland. La fecha almacenada queda
  **confirmada y reservable**. Abstracts y *Student Travel Awards* siguen TBA.
- **Ventana *late-breaking* del ASCS 2027 confirmada en página oficial, no
  inferida: abre el 27-nov-2026 y cierra el 13-dic-2026** (E-0029). El plazo
  ordinario cerró el 28-oct. Tarifa anticipada 850 USD socia (~735 EUR) hasta
  el 20-dic. Detalle con consecuencia: las becas de viaje **admiten
  explícitamente a residentes médicos** además de doctorandas —sus dos vías a
  la vez— pero **se notifican el 3-dic, antes de que cierre el late-breaking**,
  así que por esta vía no habría beca. Sigue siendo Fit 3 y por tanto **la
  regla de selección no lo mete en `action_now`**; lo dejo fuera a propósito
  en vez de inflarle el Fit, igual que la semana pasada.
- **T-0022: proveedor por fin identificado y la respuesta es NO solicitar.** No
  es de Bristol sino de **Wellcome Connecting Science (Hinxton)**. Plazo
  16-nov confirmado, cuota estimada 685 EUR. Pero el programa **no toca GWAS,
  PRS ni MR** y choca con T-0003. Ese reloj de dos semanas queda cerrado con
  una decisión, que era el objetivo.
- **T-0007 MR avanzado de Bristol: se deja expirar a conciencia.** Plazo
  ~11-nov verificado sin cambios, y confirmados por escrito los prerrequisitos
  y la regla de no hacer los dos cursos en el mismo año académico. El orden
  correcto sigue siendo T-0003 primero (marzo 2027).
- **L-0003 Speed: la plaza del 01-10-2026 está CERRADA**, el anuncio se retiró
  del portal de Aarhus (negativo Tier 1). Su ERC es «ClassifyDiseases» (2023,
  ~2 M EUR) con contrato anunciado hasta el 30-09-2028, así que una ronda
  compatible con febrero de 2028 tendría que salir en 2027.
- **L-0015 McIntosh: negativo verificado** en jobs.ac.uk; las dos plazas de
  Edimburgo son del Roslin Institute, no suyas.
- **AEGH: no es elegible este ciclo, y conviene saberlo ya.** La AEGH paga la
  ESHG 2027 (inscripción + 600 EUR) con plazo 15-nov-2026, pero exige dos años
  de antigüedad como socia y comunicación en Granada 2026. **Darse de alta
  ahora abre esa beca en 2029.** Además en 2027 la AEGH no tiene congreso sino
  la XVII Jornada (7-may-2027, Bilbao, metilación del ADN).
- **WCPG 2027 sin novedad**: Brisbane 9-13 nov confirmado, inscripción en
  *coming soon*, sin plazo de abstracts. Ni el ECIP (su página sigue redactada
  para 2026) ni la Peter McGuffin están abiertos. Volver en marzo de 2027.
- **Ángulo (c), premios ERC, agotado para este año**: las Starting Grants 2026
  ya se explotaron en pasadas anteriores y las Consolidator 2025 SH dieron un
  solo *hit*, no genético. Las Consolidator 2026 no estaban publicadas hoy; el
  año pasado salieron el 9 de diciembre. Siguiente mirada: diciembre.

## Filas cuyos hechos han cambiado y que ella puede haber leído ya

`owner_status.json` sigue vacío, así que **ninguna fila marcada por ella se ha
visto afectada**: no hay nada en IN_PROGRESS, APPLIED ni DISCARDED. Aun así
cuatro fichas han cambiado de contenido de forma material:

- **L-0017 Huckins: se REACTIVA, y el «refutado» de la semana pasada era un
  falso negativo mío.** Filtrar NIH RePORTER por institución la escondió. Es PI
  nombrada en **R01MH136149 (EDGI2) hasta el 28-02-2029**, que sí cubre un
  inicio en febrero de 2028. **Conflicto que no zanjo:** esa subvención está
  registrada en la Universidad de Carolina del Norte y la ficha la sitúa en
  Yale; no escribo ninguna de las dos versiones como hecho. Su R01ES033630
  muere el 30-11-2026, eso confirmado.
- **L-0069 Olfson**: de LIKELY a VERIFIED con R01 hasta 2031 (arriba).
- **L-0003 Speed**: la plaza que esperaba respuesta está cerrada (arriba).
- **L-0012 Peyrot: la vía que recomendé la semana pasada era la equivocada.**
  `werkenbij.amsterdamumc.org` es el portal **asistencial**, no el científico,
  y arrastra el mismo bug de plantilla. La vía buena es **AcademicTransfer**,
  comprobada hoy: **no hay vacante** en su grupo ni en la VU.
- **T-0001 Boulder**: cuota de 550 a 850 USD y ayuda económica confirmada como
  inaccesible. Si tenía en la cabeza «unos 500 euros y quizá beca», el número
  real es ~782 EUR a su cargo.

## Lo que no se pudo verificar ni alcanzar

- **L-0025 Duncan: bloqueo NUEVO**, las dos fichas de Stanford dan HTTP 503.
- **L-0018 Falck-Ytter: sigue sin comprobar y no se ha movido su
  `Last_Verified`** — la API de SweCRIS responde con cuerpo vacío sin
  credencial. Vía alternativa para la semana que viene: catálogo de Uppsala o
  Vetenskapsrådet, **nunca** SweCRIS.
- **L-0006 KCL: negativo PARCIAL y lo digo como tal.** Con la URL correcta
  (`kcl.ac.uk/jobs/search`; `search-jobs` da 404) King's tiene 74 vacantes y la
  faceta IoPPN sube de 4 a 7, pero sólo se inspeccionó una: **6 sin ver**.
- **Financiación sin verificar** de Ripke, Kuchenbaecker (UKRI Gateway to
  Research da *Projects (0)* pese a 21 *outputs*), Bacanu, Kendler y Baune. Y
  **las instituciones de todos los nombres sacados del PGC están INFERIDAS del
  dominio del correo**: esas páginas no indican afiliación. Por eso nueve de
  las quince fichas nuevas son LIKELY y no VERIFIED.
- **UCL MR: 403 por Cloudflare** (WebFetch y curl). Fichado con las 900 GBP
  marcadas UNVERIFIED.
- **LABCLIN 2026 queda LIKELY**: `labclin2026.es` sirve un armazón JS vacío. No
  existe LABCLIN 2027 publicado.
- **Sleep Europe 2028 = EDIMBURGO**, sin fechas, y es un rodeo que funciona: la
  página *ESRS 2028 Bid* de la **British Sleep Society** evita el 403 crónico
  de `esrs.eu`. Fuente nueva, SRC-0422.
- La 24ª Complex Trait Community no está anunciada. No se gastó llamada en
  EMGM, conforme a lo acordado (mirada final en enero de 2027).
- **Erratas publicadas en páginas del PGC, anotadas para no tropezar**: el
  correo de Roseann Peterson sale malformado (`peterson.roseann@gmailcom`) en
  Cross-Population, y Abigail ter Kuile aparece con el correo de Daniel Levey
  en Anxiety. Y un *slug*: `anxiety-working-group` funciona,
  `anxiety-disorders-working-group` da 404.
- **Sondear rutas de PDF del ERC provoca HTTP 429 rápido**; no insistir.

## Conflictos abiertos

- **L-0017 Huckins: Carolina del Norte contra Yale** (arriba), sin zanjar.
- **Premio de Brittany Mitchell (L-0083)**: su perfil lo llama *NHMRC Emerging
  Leadership Fellowship*; la nota de prensa de QIMR sobre la misma convocatoria
  lo lista bajo *Investigator Grants*. **Importa de verdad:** si son cinco años
  desde 2022, el dinero se acaba en 2027, **antes** de que ella esté libre. No
  se ha escrito ninguna de las dos versiones como hecho.
- **T-0022**: no se localizó la ficha propia de la edición 2027, sólo la línea
  del catálogo, y la de 2026 sigue en línea sin mencionarla. Irrelevante para
  la decisión (no solicitar), pero queda dicho.

## Respuesta a la pregunta abierta de más apalancamiento: MoBa

**Sí, y con un matiz que vale oro.** MoBa tiene fenotipos de sueño de lactante
y de niño pequeño a escala de cohorte (Hysing 2014 sobre despertares nocturnos;
Sivertsen 2015 y 2021; Valla 2021) y genotipado **con tríos**, confirmado por
«Family genetic designs in MoBa» (*Nature*, octubre de 2026). El matiz: **ese
artículo usa el sueño a los 14 años, no en la lactancia.** Los ingredientes
existen y el cruce está sin hacer. Es decir: **esto no es un grupo al que
escribir, es un proyecto que ella puede proponer** —y es el mejor argumento de
correo en frío que tiene para su línea 3, porque llega con una idea, no con un
CV. Sin verificar: que esos ítems estén dentro de la submuestra genotipada.

## Suscripciones

**Cero altas, tercera semana consecutiva, y sigue siendo deliberado.** Las
cuatro ramas buscaron canal nuevo y ninguna vio una URL de alta real: la lista
de avisos de Boulder ya está como SUB-0006 y se da de alta por listserv, y SRS,
ISPG, BGA, AEGH, ESHG y ESRS ya están todas en el fichero. Una URL inventada es
peor que ninguna suscripción.

**Pendientes: 43** (eran 38; las cinco nuevas las añadieron positions y
fellowships esta semana). `owner_status.json` está vacío, así que por
definición toda fila TODO sin marca suya cuenta como pendiente. Las de reloj
más apretado, actualizadas: **SUB-0036** (alta en la ESRS, **requisito en el
momento de solicitar** la escuela de sueño T-0030, solicitudes previstas
marzo-abril: hay que estar dentro ANTES), **SUB-0030** (alta en la ESHG, 50 EUR
que ahorran 125 EUR si se registra antes del 2027-04-15) y **SUB-0017** (cuenta
de reservas de Bristol, puerta de T-0003 en marzo). Añado una cuarta que ahora
tiene sentido: **darse de alta en la AEGH**, porque el reloj de su beca de
congreso es de dos años de antigüedad y empieza a contar cuando se apunte.

## Nota de mantenimiento — octavo aviso, y ahora son SIETE ficheros

Ya no son cuatro. Por encima del umbral de 60 KB: `changelog.tsv` 435 KB,
`sources.tsv` 320 KB, `fellowships.tsv` 307 KB, `groups.tsv` 283 KB,
`postdocs.tsv` 197 KB, `jobs.tsv` 107 KB y `events.tsv` 62 KB. Y
`watchlist_closed.tsv` está a 59,3 KB, o sea **a 0,7 KB de cruzarlo**: la
semana que viene serán ocho.
**El troceo lo hace una persona**, porque exige tocar `tools/build_page.py` y
`tools/build_xlsx.py` en el mismo commit, y eso no se hace sin vigilancia al
final de una pasada. Lo señalo por octava semana y añado una observación: a
este ritmo el coste de leer la tabla de grupos empieza a comerse el
presupuesto de investigación de la rama 4.

## Qué perseguiría la semana que viene con más presupuesto

1. **Confirmar que el registro de Boulder se completó**, con su importe real, y
   encontrar la ruta de *Online Lectures and Practicals* del IBG (enlazada
   pero 404).
2. **Minar los 13 working groups del PGC que no se abrieron** (ADHD, Autism,
   Substance Use entre ellos) filtrando por *junior co-chair*: el hallazgo
   estructural de esta semana es que los co-chairs junior son justo quienes
   estarán montando laboratorio en 2028, que es cuando ella llega.
3. **Atacar la línea 3, sueño infantil, que no aparece ni en el PGC ni en NIH
   RePORTER** — es el punto ciego del método actual, y MoBa dice que ahí hay
   proyecto.
4. **Cerrar la fecha del premio NHMRC de Mitchell** (decide si QIMR, su vía
   cálida, es viable o se queda sin dinero en 2027).
5. **Las 6 vacantes del IoPPN sin ver** paginando `kcl.ac.uk/jobs/search`, y la
   financiación de Falck-Ytter por Uppsala o Vetenskapsrådet.
6. **Vigilar la apertura del late-breaking del ASCS el 27-nov** y el anuncio de
   LABCLIN 2027.
7. **Que la rutina de fellowships recoja SRC-0428** (ayuda multicéntrica
   SEMEDLAB, ciclo que cierra el 31-oct-2027) y la Ayuda a proyectos anual de
   la misma fundación, que es un instrumento aparte y nadie ha fichado.
