# fellowships — pasada del 2026-09-21

**ALERTA (de calendario, no de esta pasada): la rutina no se ejecutó ni el
2026-09-07 ni el 2026-09-14.** El informe anterior es el del 2026-08-31, así
que casi toda la pestaña llegaba a hoy con tres semanas sin verificar. Esta
pasada ha sido, sobre todo, de recuperar el retraso: 52 filas verificadas
frente a 3 altas. Conviene mirar por qué se perdieron dos disparos.

Las cinco ramas completaron. El buzón lo leyó positions a las 00:01 (vacío,
nada enrutado a FELLOWSHIPS) y `source_inbox.json` está vacío: no había
trabajo de bandeja por mi parte.

## Los números, del diff (`git diff HEAD~1`), no de mi memoria

| fichero | altas | modificadas |
|---|---|---|
| `data/fellowships.tsv` | 3 (F-0063, F-0064, F-0065) | 32 |
| `data/watchlist_closed.tsv` | 0 | 20 de 22 |
| `data/sources.tsv` | 11 (SRC-0158 … SRC-0168) | — |
| `data/changelog.tsv` | 55 apuntes | — |
| `data/action_now.tsv` | 4 filas mías (antes 3); 22 ajenas preservadas | — |

`subscriptions.tsv` no crece: ver «Decisiones que tomé yo» más abajo.

## Las tres cosas que merecen acción

**1. F-0037 — nueve días, y el reloj corre hoy.** La Beca Internacional de
Intercambio Científico Profesional (Fundación José Luis Castaño–SEQC) mantiene
el plazo del **30-09-2026**, verificado en Tier 1. Se capturaron el Anexo 1 y
la checklist, y aparecieron dos requisitos que la ficha no tenía: la estancia
debe caer **entre marzo de 2027 y marzo de 2028** (compatible con el fin del
MIR el 22-05-2027, pero el impreso exige la firma del jefe del laboratorio
español actual más un acuerdo entre centros) y hace falta el **formulario PEP
de la IFCC**. El único bloqueo real es el alta como socia de SEMEDLAB, y no se
pudo cerrar: `semedlab.es` responde 202 con ~200 bytes al fetch. Cuota por
fuente secundaria: 85 € + 15 de inscripción, 60 € residentes. **Si el alta
tarda semanas, la edición 2026 es inviable y conviene saberlo hoy, no el 29.**
El `Next_Action` de la fila lleva los seis pasos en orden.

**2. F-0017 BBRF — se adelanta dos años.** Las guidelines en PDF, descargadas y
extraídas (no resumidas), dicen literalmente que vale un *«M.D. with minimum
PGY-IV training»* como título de nivel doctoral y que el primer año
posdoctoral **no** está excluido. Su MIR empezó el 22-05-2023, luego cumple
desde el 22-05-2026 sin esperar a la tesis: **su primera edición realista pasa
de 2029 a 2027**, con la condición de estar «employed in research training»,
que su residencia asistencial hoy no cumple. Fit 3 → 4, VERIFIED. Esta es la
pregunta que el informe del 31-08 dejó abierta y ya está cerrada.

**3. F-0039 SENC — su mejor premio predoctoral sí es alcanzable, y 2027 es la
última ventana limpia.** El PDF «Requisitos para solicitudes de ayudas y becas
SENC» aplica los 2 años de cuota **solo** a ayudas de viaje y de organización;
no menciona los premios, y el Rita Levi-Montalcini no exige antigüedad. Con
defensa en febrero de 2028, 2027 es su último año como predoctoral.

## Lo que cambió de estado

- **F-0009 MSCA: CERRADA.** 09-09-2026, **21.627 propuestas** (+26,7% sobre
  2025, récord histórico de los programas marco), ~7% de éxito. La de 2027
  lanza el 07-04-2027 y cierra el **08-09-2027**, ambas TBC en la propia
  página. **Ese cierre cae cinco meses antes de su defensa prevista**, y no
  hay Tier 1 que garantice una PF en 2028 bajo FP10. Es la única conclusión
  del radar capaz de mover el calendario de la tesis: la decisión de este
  otoño es si adelantar la defensa. No la dejo como recomendación firme
  porque el sucesor solo está respaldado por Tier 2.
- **F-0010 Humboldt: la ficha anterior era falsa.** No es ROLLING. Tres
  aperturas fijas al año y cada una **cierra al acumular 800 solicitudes**, o
  sea por cupo. Hay que estar lista el día de la apertura.
- **F-0011 DFG Walter Benjamin** sí es continua de verdad (Tier 1), pero
  financiar estancia **fuera** de Alemania exige 3 años previos allí: su única
  modalidad practicable es con acogida **en** Alemania. Es hoy su mejor
  colchón frente a una defensa sin fecha fija.
- **F-0024 L'Oréal-UNESCO España: ABIERTA**, 07-09-2026 → **19-10-2026**. Fit
  se queda en 2 y LIKELY: las bases son un escaneo sin capa de texto y no se
  pudo confirmar si exigen el título de doctora. Merece que la abra a mano.
- **F-0004 JdC y F-0005 RyC: ANNOUNCED con fechas.** JdC 12-11 → 03-12-2026;
  RyC 10-11 → 10-12-2026. Su primera JdC posible es la de **2028**, y solo si
  la ventana admite títulos del año en curso; si el borde se cierra el 31-12
  anterior, se va a 2029. No verificado: bases sin publicar. Dato que la
  condiciona: la JdC exige centro distinto al de la formación predoctoral, lo
  que **excluye la Universidad de Murcia**.
- **F-0008 EMBO: regla nueva y cara.** Desde el corte de julio de 2027,
  *«Researchers may submit only one EMBO Fellowship Proposal»*. Un solo
  intento en toda su carrera: no cabe usar una solicitud como ensayo, y su
  cuello de botella sigue siendo la aceptación del empírico.
- **F-0007 HFSP:** el plazo del 24-09 no le afecta (no presentó LOI) y el
  ciclo AY2027 exigía doctorado antes del 31-12-2027. AY2028 es su edición.
- **W-0008 la Caixa Incoming: no es elegible, y la nota anterior estaba mal.**
  Cierra el 23-09-2026 pero pide doctorado de 2 a 7 años antes del cierre.
  Cumple los 2 años en febrero de 2030 → **primer cierre válido, septiembre de
  2030**. La nota anterior decía «cierre hacia septiembre de 2028», que son
  siete meses después de la defensa, no dos años. Queda escrito para que no
  genere falsa urgencia cada septiembre.
- **F-0063 Koplowitz «Ayudas de Formación»: cerrada en negativo, pero
  verificada.** Era el hueco más prometedor que dejó agosto. Las bases de las
  dos líneas exigen título de especialista en **Psiquiatría (MIR) o Psicología
  Clínica (PIR)**: su MIR es de Medicina de Laboratorio, así que la exclusión
  es estructural, no de calendario. Fit 1, y no volverá a salir.
- **F-0064 Beca Nacional ESHG 2027 (AEGH):** publicada el 18-09, cierra el
  **15-11-2026**, 600 €. Falla los tres filtros (2 años de antigüedad como
  socia, ≤4 años de experiencia postuniversitaria —es MD de 2019— y
  comunicación en Granada 2026). El atajo nacional está cerrado, probablemente
  para siempre por el criterio de los 4 años.

## Decisiones que tomé yo, como orquestador

- **Conflicto F-0023, resuelto a favor de separar las dos vías.** La rama 4 y
  la rama 5 encontraron la misma noticia de la AEGH y propusieron cosas
  distintas: la 5 quería reescribir F-0023 con el plazo del 15-11-2026, la 4
  dejaba F-0023 con la vía directa de la ESHG (resúmenes, 04-02-2027) y abría
  fila propia. Me quedo con lo segundo: son dos convocatorias distintas y
  fundir el plazo habría hecho perder la fecha de febrero. F-0023 queda
  VERIFIED con la vía europea; la nominación nacional es F-0064.
- **Descarté la única suscripción propuesta** (el formulario de alta de
  SEMEDLAB). SUB-0009 ya cubre esa organización y sigue en TODO, y la URL
  operativa del alta ya vive en el `Next_Action` de F-0037: una segunda fila
  habría ensuciado una lista que la dueña marca por ID. Pendientes de
  suscripción, por tanto, las 18 de siempre, **todas en TODO y ninguna con
  marca suya en `owner_status.json`, que sigue vacío**. La de mayor
  rentabilidad hoy sigue siendo SUB-0010 (AEGH): esta pasada le ha puesto
  fecha, porque los 2 años de antigüedad que exige la beca ESHG empiezan a
  contar el día que se dé de alta.
- **Fusioné a mano la regla de EMBO** que encontró la rama 5 sobre una fila de
  la rama 1, para que no se perdiera entre ownerships.

## Lo que no pude verificar, y los bloqueos

Nuevos, fichados para no redescubrirlos: `consilium.europa.eu`,
`commonslibrary.parliament.uk`, `nhmrc.gov.au`, `ispg.net` (403 de Cloudflare
a curl) y `lacaixafoundation.org`/`fundacionlacaixa.org` (403 a curl **y** a
WebFetch, incluido el PDF de bases). `semedlab.es` replica el patrón 202 de
`fundaciontatiana.com`. El buscador del BOJA no funciona por GET: en diciembre
hay que ir al índice por fechas o a la BDNS.

Ya conocidos y no reintentados: `wellcome.org`, `esrs.eu`, `bga.org`,
`aei.gob.es`, `isciii.es`. **W-0013 ESRS queda declarada no verificable por
vía automática** tras cuatro pasadas: o la abre ella a mano o se retira.

**Apunte de entorno que cuesta dinero cada semana: no hay `pdftotext` y
`pypdf` está roto (`_cffi_backend`).** Tres ramas han tenido que extraer PDF
con `zlib` a mano; eso impidió leer las bases de la II Fulbright-Séneca
(descargadas, 210 KB, HTTP 200) y las de L'Oréal. **Merece ser un helper de
`tools/`**, igual que el parche de `cryptography` que ya se pidió en agosto.

Conflictos que siguen abiertos: **Wellcome, 10 frente al 16 de noviembre de
2026** (espejo de Oxford contra tabla del financiador; ambas coinciden en
preselección de febrero, así que es la misma ronda); y **el reloj de 7 años de
la BGA** (F-0058), acotado pero no resuelto: el texto dice *«within seven years
full-time equivalent of receiving their terminal degree (e.g., Ph.D., M.D.)»*
más una cláusula de interrupciones de carrera. Que liste «M.D.» empuja a 2019
(agotado); «full-time equivalent» más la cláusula permitiría descontar la
residencia. No lo decido: la acción es escribirle a la BGA citando su texto.

**Datos que faltan y que deciden filas:** su **fecha de nacimiento** (las
bolsas de viaje de la AEGH dependen enteramente del límite de 35 años) y **de
qué sociedades es ya socia**.

**Aviso sobre F-0054 (Fulbright-Séneca), que está en `action_now`:** la rama 5
encontró que la II convocatoria se dirigía a personal con vínculo
funcionarial o contractual con organismos **de la Región de Murcia**. Su
contrato es de Málaga y su vínculo con la UMU es de doctoranda. Si la III
mantiene la cláusula, la fila se cae. Es Tier 2 sobre un PDF Tier 1 que no se
pudo extraer, así que no toqué el Fit — pero entra en `action_now` por la
regla de competencia LOW y conviene leerla con esa reserva.

## Filas no alcanzadas (su `Last_Verified` NO se tocó)

F-0059; F-0006, F-0013, F-0014, F-0015, F-0016, F-0022, F-0047, F-0052,
F-0053, F-0054, F-0055, F-0056, F-0057; F-0026; F-0021, F-0027, F-0028,
F-0030, F-0031, F-0036, F-0044, F-0045, F-0060, F-0061, F-0062. En la
watchlist: W-0005 (403), W-0013 y W-0014.

**W-0014 One Mind: propongo retirarla de la rotación.** Exige puesto
equivalente a Assistant/Associate Professor **en institución de EE. UU.** y
estar en los 8 años tras el primer nombramiento independiente. Es inelegible
estructural, Fit 1, y consume presupuesto cada semana.

## Nada que la dueña hubiera marcado ha cambiado bajo ella

`owner_status.json` sigue vacío `{}` y las 36 filas con `Owner_Status` no
vacío conservan su valor: `apply_rows.py` rechaza esa columna por diseño.

## Aviso de mantenimiento, ya insostenible

`data/fellowships.tsv` pasa de **158 KB a 186 KB**, más del **triple** del
umbral de división de ~60 KB, y `sources.tsv` va por 109 KB. Sigue sin
partirse, y con razón: hacerlo obliga a tocar `build_page.py` y
`build_xlsx.py` en el mismo commit, y eso no se hace desatendido. Es tarea de
la dueña. Corte natural sugerido: internacionales frente a españolas, o becas
frente a premios y ayudas de viaje.

## Qué perseguiría la semana que viene

1. **El desenlace de F-0037**: si el alta en SEMEDLAB llegó a tiempo. Si no,
   reprogramar la fila a la edición 2027 en vez de dejarla vencida.
2. **Responder al reloj de la MSCA**: primer indicio Tier 1 del programa de
   trabajo 2027 y de si las dos fechas TBC se confirman.
3. **La Orden andaluza de 24-10-2023 en BOJA** (F-0052) y un segundo espejo
   universitario británico para dirimir el 10 frente al 16 de noviembre.
4. **El BOE desde finales de octubre**, para el extracto de la JdC 2026 y su
   ventana de fecha de doctorado: de esa redacción depende 2028 frente a 2029.
5. **Escribir a la BGA** (F-0058) y a `becas.neurociencia@fundaciontatiana.com`
   (F-0050), en vez de seguir peleando con dos webs bloqueadas.
6. **Los esquemas de Company of Biologists sin fichar**: ECR Visiting
   Fellowships y Research Partnership Kickstart Travel Grants, que encajan
   mejor que el F-0029 actual.
7. **Las 25 filas no alcanzadas**, empezando por el bloque autonómico español,
   que lleva sin tocarse desde el 31 de agosto.
