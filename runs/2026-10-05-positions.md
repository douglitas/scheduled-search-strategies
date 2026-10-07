# positions — 2026-10-05

Cinco ramas, las cinco completadas. El buzón se leyó y el conector funcionó.
Ninguna ALERTA: nada roto, nada sin entregar.

**Después de quince meses, ha salido la vía transitoria de Genética.** Es el
titular y lo único de esta pasada con fecha encima.

## Los números, sacados del diff (`git diff 13db7d6 HEAD`), no de mi memoria

| fichero | altas | modificadas |
|---|---|---|
| `data/postdocs.tsv` | 11 (P-0056 … P-0066) | 9 |
| `data/jobs.tsv` | 1 (J-0021) | 3 |
| `data/sources.tsv` | 8 (SRC-0222 … SRC-0229) | 0 |
| `data/subscriptions.tsv` | 1 (SUB-0023) | 0 |
| `data/changelog.tsv` | 24 apuntes | 0 |
| `data/action_now.tsv` | — | 31 filas (1 mía, 30 ajenas preservadas) |

Total: 101 inserciones, 43 supresiones en 7 ficheros. Las supresiones cuadran
exactamente con las filas modificadas (9+3 en mis pestañas, 30 por renumerado
de `Rank` en `action_now`): **no se ha perdido ninguna fila**, comprobado con
`git diff` y con un script que relee los TSV y compara `Owner_Status` fila a
fila contra `HEAD`.

Nota de cosecha honesta: de las 11 altas de postdocs, **9 son Fit 2** y están
ahí sólo para no redescubrirlas. Ninguna fila nueva de la semana pasa de Fit 3.
Lo que vale hoy son los *updates*, no las altas.

## Las tres cosas que merecen tu atención

**1. J-0003 ha salido, es Fit 5 y tiene dos fechas. El 02-10-2026 Sanidad
sacó a audiencia pública los DOS proyectos de real decreto** (Genética Médica
y Genética de Laboratorio), con **alegaciones hasta el 26-10-2026**. No nos
quedamos en el listado: se descargaron los dos PDF oficiales y se extrajeron
con `pdftotext`. La **disposición transitoria primera, apartado 4** contempla
tu caso exacto —residente en formación a la entrada en vigor— y te da acceso
al título **previa prueba teórico-práctica**, acreditando ejercicio computable
≥ 50 % del tiempo desde la obtención de tu título de especialista. Como la
primera promoción de residentes de Genética no acaba antes de 2032-2033,
cumples el supuesto con muchísimo margen.

**Y aquí está el detalle que te condiciona la carrera, no sólo la fila:** ese
ejercicio computable sólo cuenta si se presta **en una unidad asistencial U.78
de Genética de Laboratorio** con autorización sanitaria inscrita en el Registro
General de Centros. **Un puesto genérico de Análisis Clínicos que no esté dado
de alta como U.78 no computa.** Es decir: la plaza que elijas al terminar la
residencia el 22-05-2027 decide si puedes optar al título, y cada año en U.78
te compra dos de reloj. Antes de aceptar destino, hay que verificar el alta
U.78 del servicio.

Hay además un **conflicto que declaro y no resuelvo**: en el proyecto de
Genética *Médica*, el art. 3 fija el ámbito en la unidad **U.108** mientras su
DT primera apartado 2 define el ejercicio computable como el prestado en
**U.78** (la de Laboratorio). Parece errata de arrastre del borrador gemelo, y
es exactamente la observación que conviene presentar antes del 26-10-2026. El
BOE sigue sin publicación definitiva.

**2. P-0050 (Boston University, Lindsay Farrer) por fin está VERIFIED, y sigue
siendo la única plaza de la base que no choca con tus relojes.** Se abrió por
primera vez el dominio de quien contrata (`bumc.bu.edu/genetics/...`, no el PDF
del IGES): la convocatoria sigue publicada, mantiene «the position will remain
open until filled», acepta «in the process of completing a PhD» y admite
fechas de inicio posteriores. Contacto directo: farrer@bu.edu. Candidatura
ligera —carta, CV y **tres cartas de recomendación**—, así que el cuello de
botella eres tú pidiendo las cartas, no el plazo.
**Caveat que debes leer:** la metadata de WordPress dice que esa página no se
ha modificado desde **enero de 2020**. Es una página permanente, no un anuncio
fechado. Lo que prueba reclutamiento reciente es el PDF de junio-2026 del IGES.
Su vigencia real sólo la confirma Farrer por correo. Dato nuevo de
elegibilidad: la ciudadanía estadounidense «is preferable but not required»
(no te excluye), pero se dará preferencia a quien cumpla los requisitos de
residencia para un *training grant* del NIH (eso sí te resta). Competencia
fijada en MEDIUM por ese motivo.

**3. El encargo del 08-10 de P-0002 se cierra en NEGATIVO, y es la respuesta
correcta.** La ficha Tier 1 del MPI (umantis, vacante 496) **no contiene esa
fecha** ni ninguna otra de cierre o de inicio de revisión. El «rolling review
beginning October 8, 2026» sigue viniendo sólo del tablón de la ISPG (Tier 2),
que esta semana lo repite junto con el salario y el inicio negociable —o sea
que **todo lo demás se corrobora y sólo esa fecha falta en el dominio del
MPI**. Dejo el conflicto declarado en la fila y **no asciendo la fecha a
`Deadline`**. Datos ahora verificados: 3 años, 5.709,87-7.025,87 EUR brutos/mes
(73.999-91.055/año), inicio 01-12-2026 negociable, requisito literal «hold, or
expect to obtain shortly, a PhD». Con Málaga hasta mayo de 2027 y la defensa en
febrero de 2028, «shortly» no te describe: **el valor de esta fila ya no es
esta convocatoria, es el contacto** — beate.stpourcain@mpi.nl, copia a
secretariat.genetics@mpi.nl.

## Un bug del generador, arreglado y por qué te lo cuento

`action_now` vuelve a tener una fila mía después de dos pasadas en cero, pero
estuvo a punto de tener dos: **P-0002 se colaba por tercera vez**, y por un
hueco nuevo del mismo guard. Al escribir en `Deadline` que la ficha «NO publica
fecha de cierre» y que «el 2026-10-08 sigue SIN confirmar», el guard —que sólo
reconocía la forma afirmativa, «sin fecha de cierre»— no disparó, y el
extractor de fechas sacó el 2026-10-08 y lo trató como plazo vivo: Fit 4 dentro
de 90 días, derecho a la portada. Una plaza que exige el doctorado en mano y
empieza en diciembre de 2026, es decir para la que **no eres elegible**, que es
precisamente lo que el contrato prohíbe acercar a `action_now`.

Arreglado en `tools/rebuild_action_now.py` (commit propio): **una fecha
desmentida no es un plazo.** El guard cubre ahora las formas negativas y los
cierres por cobertura. Comprobado fila a fila que el cambio no arrastra a nadie
más: de las 12 filas ROLLING de mis dos pestañas, las otras 11 no tienen
ninguna fecha parseable en `Deadline`. Te lo cuento porque toqué `tools/`, que
no es rutina de una pasada.

**Efecto secundario que debes saber para leer la página:** como `positions` va
primero en `action_now` y pasa de aportar 0 filas a aportar 1, las 30 filas de
las otras rutinas bajan un puesto de `Rank`. Sus líneas cambian en el diff
aunque su contenido sea idéntico, así que **esta semana la sección «Novedades»
puede mostrar filas ajenas que en realidad no han cambiado**. No es un edit
cosmético mío: es inherente al renumerado del generador. Si molesta, la
solución es que `action_now` no renumere o que las novedades se calculen sólo
sobre las pestañas de oportunidades, y eso lo decides tú.

## Lo que ha cerrado, verificado en Tier 1

- **P-0053 (Leicester, Research Associates in Statistical Genetics)**:
  `jobs.le.ac.uk` responde «this vacancy may have expired». Cerrada.
  Y de paso, **la calibración de IGES queda probada por segunda vez y con los
  dos extremos verificados**: la plaza sigue listada como «actual» en IGES con
  fecha 26-03-2026. IGES sirve para fechar y para sacar contactos, **nunca para
  probar vigencia**.
- **P-0017 (QIMR Berghofer)**: cerrada por ausencia del listado completo
  (7 vacantes hoy). P-0049 y P-0047 confirmados vivos por la misma vía.
- **J-0012 (GSK)** pasa a PENDING **por imposibilidad de lectura, no por cierre
  comprobado**: jobs.gsk.com se renderiza por JavaScript y devuelve la portada
  tanto en la ficha como en el buscador. Sigue sin país.

## Lo que no pude verificar, sin disfrazarlo

- **EURAXESS está peor de lo que creíamos y hay que corregir el método.** La
  búsqueda web sobre su dominio, que esta pasada iba a ser la vía principal,
  **ya no sirve como sonda de novedad**: devuelve sólo fichas archivadas de
  2023-2024 (IDs ~70.000-445.000) cuando las vivas van por ~557.000+. Se
  verificaron en Tier 1 las cuatro más pertinentes y **las cuatro están
  expiradas**. Y el filtrado sigue roto, ahora con la causa raíz identificada:
  el formulario es un Drupal `oe_list_pages` con **method=POST**, así que todo
  parámetro por GET se ignora; **hecho el POST real, el sitio devuelve los
  mismos 6.398 resultados con filtro y sin él** (179.563 bytes idénticos). No
  hay RSS ni JSON API (`/jobs/rss`, `/api/jobs`, `/jsonapi` → 404).
  **Consecuencia práctica: hoy no existe forma honesta de barrer EURAXESS por
  tema con este presupuesto**, y las alertas por correo (SUB-0002/SUB-0018, que
  además están duplicadas) pasan de «estaría bien» a ser la única vía real.
- **P-0003 (Mount Sinai) y P-0011 (Albert Einstein) siguen sin resolver.** Con
  el patrón `?keywords=` que sí funciona aparecen anuncios vivos de ambos
  empleadores pero **sólo sus plazas de profesorado**, no los postdocs. Que el
  índice vivo contenga a los empleadores y no a estas dos plazas refuerza la
  retirada, pero es prueba indirecta: **ninguna baja de estado y en ninguna se
  subió `Last_Verified`**. Lo que lo zanjaría es careers.mountsinai.org y el
  portal de Einstein.
- **SEMEDLAB (encargo heredado) no se pudo recorrer**: han puesto un captcha de
  Sucuri delante del listado. La línea base que pedía el encargo ya existe en
  la nota de SRC-0201 del 28-09, así que la novedad será detectable en cuanto
  se recupere el acceso.
- **J-0017 (Asturias) sigue sin resolver**: astursalud.es da 503 y corta la
  conexión. Sin subir `Last_Verified`.
- **P-0020 (deCODE), P-0037 (NIH) y P-0040 (IIS-FJD)** quedan intactos.
  **Corrección que afecta a la puntuación: Islandia SÍ está en el EEE**, así que
  deCODE no te exige visado ni patrocinio. Donde sí hace falta es EE. UU. y
  Australia.
- **Broad y Cardiff leídos a medias** (sólo la página 1 de 32 y de 23
  vacantes). No se toca `Last_Verified` de P-0008 ni P-0035.
- **Contactos de Leicester (encargo heredado), a medias y marcados como tal:**
  Martin Tobin `mt47@le.ac.uk`, Catherine John `cj153@le.ac.uk`, Richard Packer
  `rjp52@le.ac.uk`. **Trátalos como UNVERIFIED**: encajan con la convención de
  Leicester pero vienen de UNA sola fuente, porque `le.ac.uk` da 403 (bloqueo
  nuevo). Ábrelo a mano antes de escribir: treinta segundos para ti, imposible
  desde aquí. Verificado que **el grupo no tiene nada abierto**, así que es
  contacto en frío puro; el gancho con Tobin es EXCEED y la genética de la
  función pulmonar, que son GWAS de rasgo complejo en cohorte poblacional
  —tu línea 1— presentándote como disponible desde mediados de 2027.
- **Bloqueos nuevos registrados**, para no volver a pagarlos:
  `jobs.sciencecareers.org/jobs/?keywords=` → 403 (las fichas por id sí
  sirven), `le.ac.uk` → 403, `eshg.org/career` → 404, semedlab.es → captcha
  Sucuri, jobs.gsk.com → JavaScript, larioja.org → 403, astursalud.es → 503,
  saludextremadura → 404.
- **Y una corrección al revés, que abre puertas: SÍ hay `pdftotext` en el
  contenedor** (`/usr/bin/pdftotext`, con `-layout`). La nota heredada de que
  no había extractor de PDF era falsa — así se leyeron los dos reales decretos.
  Conviene reintentar con esto los PDF de jobbnorge que dimos por ilegibles.

## Hallazgos de método que valen más que varias filas

- **Portal real del VHIR localizado: `jobs.vhir.org/jobs`**, legible por fetch y
  con URL por vacante. Deja obsoleta SRC-0197 (JavaScript). Leídas sus 13
  vacantes: hoy no hay nada para ti, ni de Ribasés. **Es ausencia verificada,
  no fallo de búsqueda** — tras cuatro pasadas fallidas, España deja de ser un
  agujero ciego. El IBiS también cede: el 404 del bloqueo era del host **sin**
  `www`; `www.ibis-sevilla.es` sí responde y sirve convocatorias en PDF.
- **Buscador de bolsas del Punto de Acceso General** (`administracion.gob.es`,
  `tipoBusqueda=BOLSA_EMPLEO`): sus fichas de detalle publican el plazo literal
  «Desde el … Hasta el …», justo el dato que esconden los portales autonómicos
  que nos bloquean. Es la vía para cerrar de golpe las CCAA que faltan.
- **Endpoint de DETALLE de la API de Edimburgo**, que sí devuelve la fecha de
  cierre real que el de listado no da.

## El carril español: una CCAA nueva y dos pistas que no registro

**J-0021, Canarias** (fila nueva, Fit 3). El dato útil es el mecanismo, y es
peor que el de Andalucía o Castilla y León: el SCS **no tiene bolsa
permanente**, sino listas supletorias por gerencia de área con plazos cortos, y
hoy no hay ninguna ventana abierta. Exige certificado digital listo de
antemano. Siguen faltando **Baleares, Cantabria, Castilla-La Mancha,
Extremadura y La Rioja**.

Dos pistas Tier 2 que **no** registro como fila, para que las veas tú: **La
Rioja tendría inscripción continua hasta el 10-03-2030** en 51 categorías del
SERIS —si se confirma es Fit 4 inmediato y la mejor relación esfuerzo-resultado
que queda en el carril— y el **SESCAM** habría cerrado su 21.ª convocatoria el
01-07-2026 y renombrado la categoría a FEA en Laboratorio Clínico.

Sobre **AEGH-empleo** mantengo la decisión de la semana pasada: sin fecha no
hay novedad demostrable. La vía para fechar esas ofertas no es el índice de
aegh.org sino los portales de empleo de cada hospital (12 de Octubre, ICS
Girona, Parc Taulí), que sí publican plazo.

## El buzón: funcionó, y sigue vacío por tercera semana

Conector Gmail operativo. Etiqueta `Research` localizada por ID tras listar
etiquetas **una sola vez**: **0 mensajes y 0 hilos** según sus propios
metadatos, así que el pase A no gastó una llamada. **Pase B: 0 hilos.** Cero
llamadas de etiquetado porque no había nada que etiquetar; ningún borrador,
nada enviado. `inbox_triage` no recibe ninguna fila y **nada queda PENDING**.
`data/source_inbox.json` está vacío: no tenías ninguna URL encargada.

El vacío sigue siendo el hallazgo: **a este buzón no llega ni una alerta porque
no hay nada suscrito** (SETUP.md paso 4). Mientras siga así, la captación por
correo del sistema es cero y esta rama quema dos llamadas semanales en un
buzón vacío. Y con EURAXESS ilegible por tema, esas suscripciones ya no son un
lujo.

## Nada tuyo se ha quedado obsoleto

`owner_status.json` sigue vacío (`{}`): ninguna fila estaba marcada por ti, así
que **ninguna de las 12 modificaciones de hoy te ha cambiado el mapa bajo los
pies**. Comprobado por script, no de memoria.

## Suscripciones

Añadida 1, por debajo del tope de 2: **SUB-0023**, la lista de correo **UoC
StatGen** de la Universidad de Colonia
(`lists.uni-koeln.de/mailman/listinfo/uoc-statgen`), que distribuye
expresamente ofertas de genética estadística, epidemiología genética y genética
de poblaciones. El razonamiento: las dos mejores fuentes de sociedad que
tenemos dieron **cero novedad** esta semana y una de ellas ni limpia los
anuncios caducados; una lista con sello de fecha en cada correo arregla las dos
cosas. Suscribir el buzón del rastreador, no el personal.

**Pendientes: las 22, todas TODO, ninguna dada de alta.** Por urgencia siguen
SUB-0001 (BOE — y esta semana se ha visto para qué sirve: nos habríamos
enterado de J-0003 el día 2, no el 5), SUB-0002 (EURAXESS, ahora
imprescindible) y SUB-0012 (jobs.ac.uk). **SUB-0002 y SUB-0018 están
duplicadas**: conviene fusionarlas. Y **SUB-0009 (Fundación José Luis
Castaño-SEQC) cerraba el 30-09-2026: esa edición ya se ha perdido.**

## Aviso de tamaño

`data/postdocs.tsv` pasa de 117 a **131 KB** y `data/jobs.tsv` de 61 a **64 KB**;
ambos siguen por encima del umbral de ~60 KB y son míos, así que lo digo.
También están por encima `fellowships.tsv` (210 KB), `changelog.tsv` (166 KB),
`sources.tsv` (156 KB) y `groups.tsv` (120 KB). Dividir obliga a tocar
`tools/build_page.py` y `tools/build_xlsx.py` en el mismo commit: **lo decides
tú**, no es trabajo para hacer a ciegas al final de una pasada.

## Dos decisiones de criterio que te traslado

1. **`Salary_EUR_Year` quedó vacío en las 6 filas de la rama 2** y el importe
   publicado está en su divisa dentro de `Fit_Rationale`: los anuncios publican
   libras y dólares, y el contrato prohíbe inventar cifras, así que no se aplicó
   un tipo de cambio que no tenemos. Si quieres la columna llena, hay que fijar
   un tipo de referencia en el sistema.
2. **Incoherencia de criterio que conviene zanjar**: el contrato clasifica
   Nature Careers como Tier 2, así que esta pasada sus filas quedan LIKELY y sin
   `Last_Verified` — pero filas ya existentes como P-0043 y P-0007 tienen URL de
   nature.com **y** `Last_Verified` puesto. Una de las dos cosas está mal.

## Qué perseguiría la semana que viene

Vigilar el BOE para J-0003 y, en cuanto salga la publicación definitiva,
calcular con la fecha de entrada en vigor las fechas exactas de tu ventana del
apartado 4; confirmar en Tier 1 la bolsa permanente del SERIS de La Rioja, que
es el mejor coste-beneficio que queda; usar el buscador del Punto de Acceso
General para cerrar de un golpe Asturias, Extremadura, Cantabria, Baleares y
CLM; cerrar P-0003 y P-0011 en careers.mountsinai.org y el portal de Einstein;
leer `www.mpi.nl/career-education/vacancies` (SRC-0179, la ruta correcta que ya
teníamos); las cinco páginas restantes de Broad (`jobOffset=6..30`); barrer
Cambridge / MRC Epidemiology Unit, que recluta en tu línea y no está en la
lista de objetivos de ninguna rama; y el carril de industria y MedComms, que
esta semana se quedó entero sin tocar por el peso del carril español.

---

## CORRECCIÓN, añadida el 2026-10-07

**Lo que este informe decía sobre la «errata» U.108/U.78 es falso, y la
alegación que recomendaba no debe presentarse.** La dueña lo señaló con el
argumento correcto: si la genética clínica la vienen haciendo los servicios de
laboratorio, computar U.78 no es un error, es la realidad.

Comprobado leyendo el PDF de Genética Médica completo: su disposición final
primera dice literalmente **«se crea la unidad asistencial "U.108"»**, y la
parte expositiva habla de «la creación de la unidad asistencial U.108 Genética
Médica, **diferenciada de la U.78**». La U.108 no existe hasta este real
decreto, así que nadie puede acreditar experiencia en ella y computar U.78 es
la única lectura posible. No había tal arrastre del borrador gemelo.

**Y la corrección amplía la oportunidad en vez de reducirla.** Siendo médica
con título de especialista, cumple el requisito subjetivo de los DOS decretos:
el apartado 3 del de Genética Médica pide «título de Médico Especialista en
Ciencias de la Salud» y su apartado 4, «estar realizando una formación médica
especializada». El ejercicio computable se acredita en U.78 en ambos.

**Diferencia que ahora sí decide el destino de mayo de 2027:** para Genética de
Laboratorio vale la U.78 en cinco tipos de centro (hospital general,
especializado, reproducción asistida, diagnóstico, transfusión); para Genética
Médica **sólo en C.1.1 y C.1.2, es decir en hospital**. Una U.78 hospitalaria
acumula para los dos títulos; una U.78 en un centro de diagnóstico, sólo para
el de Laboratorio.

Alegaciones que sí sobreviven, antes del 26-10-2026: (i) el apartado 10.c, que
hace esperar a los residentes del apartado 4 hasta que acabe la primera
promoción con una ventana de 15 días naturales, frente al mes que tienen los
especialistas del apartado 3; y (ii) pedir que se aclare si cabe acceder por
vía extraordinaria a los dos títulos, que ningún precepto aborda.

Fila `J-0003` corregida en consecuencia.
