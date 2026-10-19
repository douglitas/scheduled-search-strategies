# Pasada ecosystem — 2026-10-19

Rutina: ecosystem (grupos, eventos, formación). Cuarta pasada del mes.
Buzones de entrada: nada PENDIENTE al cerrar (`inbox_triage` 0 pendientes,
`source_inbox` vacío). Como última rutina de la mañana, las dos obligaciones
de respaldo quedan cumplidas sin tener que resolver nada ajeno: las pasadas
de positions y fellowships de hoy ya habían cerrado sus filas.

## Cifras, tomadas de `git diff HEAD~1 --stat`, no de memoria

| Pestaña | Altas | Actualizadas |
|---|---|---|
| groups | 12 (L-0056 … L-0067) | 15 |
| events | 3 (E-0029 … E-0031) | 6 |
| training | 3 (T-0024 … T-0026) | 13 |
| sources | 11 (SRC-0330 … SRC-0340) | — |
| subscriptions | 0 | — |
| changelog | 52 apuntes | — |

`action_now`: 38 filas mías (antes 35), 3 filas ajenas preservadas intactas.
Total: **18 altas y 34 filas actualizadas**. 137 inserciones, 53 supresiones;
las 53 supresiones son exactamente las 34 filas modificadas más las
cabeceras del diff, es decir, no se ha perdido ninguna fila.

## Las tres cosas que merecen acción, y por qué

**1. L-0007 Grotzinger ha dejado Boulder y monta laboratorio en Canadá, sin
anuncio.** Su página de la Memorial University of Newfoundland dice que fue
Assistant Professor en el IBG de CU Boulder «2021-2026» y que ahora es
Associate Professor en St. John's. Está montando grupo desde cero y **no hay
ninguna plaza anunciada ni la va a haber**: es exactamente el caso en que el
correo en frío funciona, y es la única vía. Dos consecuencias prácticas: el
país pasa de EE.UU. a Canadá, así que ahora hace falta patrocinio de visado,
y cualquier borrador suyo dirigido a una dirección de Colorado ya no vale —
es `agrotzinger@mun.ca`. Sus perfiles de CU Boulder siguen desactualizados.
Él es autor de genomic SEM, que es el salto de usuaria de *pipelines* a
desarrolladora de métodos.

**2. T-0007 Advanced Mendelian Randomization (Bristol) cierra el 2026-11-11 y
las reservas ya están abiertas.** Es Fit 4, 25-27 de noviembre, y el sistema
de reservas de los cursos cortos de Bristol se abrió el 7 de octubre a
mediodía. Está en `action_now`. Aviso honesto: `Funding_Available = No` —
no cumple los requisitos de ninguno de los paquetes de descuento de Bristol,
así que esto se paga entero, y la tarifa no está publicada por curso
(«individually priced»).

**3. E-0029, el plazo más cercano de toda la base: 2026-10-28, nueve días.**
*Advances in Sleep and Circadian Science 2027* (Sleep Research Society,
19-22 feb 2027, Austin). **Ojo: es Fit 3 y por eso la regla de selección NO
lo mete en `action_now`** (Fit 3 sólo entra con competencia LOW). Lo dejo
fuera a propósito en vez de inflarle el Fit para que aparezca: la regla es la
regla. Pero es el reloj más próximo que existe hoy y sus ayudas de viaje para
*trainees* están abiertas explícitamente a médicos residentes, que es su
situación exacta hasta mayo de 2027. Si quiere enviar resumen, es esta semana.

## Lo que se cierra o se queda sin hueco

- **E-0001 WCPG 2026**: celebrado el 29-09-2026, marcado CLOSED.
- **E-0002 ASHG 2026** empieza mañana y **E-0005 IGES 2026** se está
  celebrando ahora mismo; ya estaban CLOSED y no se han tocado.
- **T-0014 SSGAC/CESR**: celebrado el 15-10-2026, CLOSED, sin próxima edición
  anunciada.
- **T-0004 (Wellcome, Genetic Analysis of Population-based Association
  Studies)**: **no aparece en todo el catálogo 2026/27**. Probablemente
  discontinuado; se ha suavizado el Fit_Rationale en vez de borrar la fila.
- **T-0010 Tartu 2026**: celebrado; queda registrada la tarifa real (750 EUR
  más 25 EUR de solicitud no reembolsables) para la edición de 2027.

## Lo que no se pudo verificar ni alcanzar

- **El plazo del Boulder Workshop 2027 (T-0001) sigue sin existir.** Sí hay
  fechas (1-5 marzo 2027, presencial) y tema trienal, *latent genetics*:
  modelos multivariantes de gemelos, OpenMx, GREML y genomic SEM, PRS, MR —
  su diana. La propia página dice que las solicitudes se abren cuando el
  taller «se anuncie oficialmente en octubre o noviembre», así que el aviso es
  inminente. Dos hechos duros: **la beca ISCEP la excluye** (sólo
  nacionalidades de renta baja o media-baja) y, con pasaporte español, entra
  con ESTA, así que **no debe solicitar la vía de 10 plazas de registro
  temprano por visado**.
- **Bloqueos nuevos, anotados para no volver a pagarlos**: `ctglab.nl` 503
  (L-0001 Posthuma y L-0012 Peyrot quedan sin comprobar, no «sin cambios»),
  `genomics.ut.ee/en/jobs` 404 (L-0009 Mägi y L-0013 Lehto sin comprobar),
  `geneticepi.org` y `bga.org` 503, `sleepmeeting.org` sirve página vacía
  (JS), `ashg.org/meetings/2027-meeting/` e `ispg.net/world-congress/` 404
  porque esas páginas aún no existen. Hallazgos útiles al contrario:
  `ashgmeeting.ashg.org` **sí** responde aunque `careers.ashg.org` siga
  bloqueado, y el subdominio
  `coursesandconferences.wellcomeconnectingscience.org` **sí** responde
  aunque `wellcome.org` siga dando 403.
- **E-0016 EMGM 2027 sigue siendo un Fit 5 sin una sola fecha.** Tres vías
  distintas, incluido el calendario oficial de la ESHG: no existe
  información pública. No es un fallo de búsqueda, es que no está publicado.
- **Trampas de la API de NIH RePORTER**, ya documentadas en `sources` para que
  ninguna pasada las vuelva a descubrir: añadir `fiscal_years` junto a
  `pi_names` devuelve cero, y los apellidos con guión no casan («Sanchez
  Roige» sí, «Sanchez-Roige» no). El filtro
  `newly_added_projects_only` devuelve cero para FY2026.
- **L-0053 Warrier** quedó sin resolver (hacía falta UKRI Gateway, no
  RePORTER) y las filas antiguas L-0015, L-0018, L-0023 y L-0025 no se
  alcanzaron.

## Conflictos

- **L-0011 St Pourcain: RESUELTO, ya no hay conflicto.** No era una vacante
  con dos versiones sino **dos vacantes distintas separadas por dos años**. La
  abierta ahora la financia la Max Planck Society, textualmente, y no menciona
  R2D2 en ningún sitio; el R2D2 venía de dos anuncios ya cerrados del mismo
  grupo (plazos 2023-12-08 y 2024-02-17). Y el inicio del 2026-12-01 **sí es
  negociable**, lo dice el anuncio. La barrera real es otra: la revisión es
  continua desde el 2026-10-08 «hasta cubrirla», así que estará ocupada mucho
  antes de que acabe su residencia en mayo de 2027. Para ella, esta plaza
  concreta no existe; el grupo sigue siendo un objetivo de correo excelente.
- **Conflicto que SIGUE abierto (E-0004 BGA 2027)**: la web de la BGA dice
  sólo «junio de 2027», mientras la ficha lleva 2027-06-29. No se ha
  sobrescrito; queda marcado como provisional.
- **Conflicto menor no reconciliado (E-0002)**: ASHG da 2026-05-18 como plazo
  de resúmenes y la ficha lleva 2026-08-26 — casi seguro plazo ordinario
  frente a *late-breaking*. No se toca: el congreso empieza mañana y editarlo
  sería ruido.
- **`ispg.net/wcpg-2026/` se contradice consigo misma** (encabezado: Glasgow,
  29 sep-3 oct 2026; carta de bienvenida en la misma página: Brisbane, 9-13
  nov 2027). Casi seguro contenido caducado del congreso siguiente, pero no
  se puede reconciliar desde esa página.

## Filas cuyos hechos han cambiado y que ella puede haber leído ya

Ninguna fila marcada por ella se ha visto afectada: `owner_status.json` está
vacío, así que no hay nada en IN_PROGRESS, APPLIED ni DISCARDED. Aun así,
cinco fichas han cambiado de contenido de forma material y conviene que lo
sepa: **L-0007** (institución, país y contacto: un plan dirigido a EE.UU.
queda sin efecto), **L-0026** (un negativo que estaba VERIFICADO el
2026-09-28 era falso: hay plaza en su propio departamento y en el grupo de Yi
Lu), **L-0011** (la fecha de inicio «imposible» es negociable), y **L-0016**
y **L-0020**, donde antes no había plaza y ahora hay una viva — aunque
ninguna de las dos es para ella, porque ambas exigen el doctorado defendido.
Detalle que sí sirve para el futuro: los anuncios de Palamara (L-0016) aceptan
a quien «tenga, **o esté cerca de terminar**, el doctorado», lo que abre la
puerta a un ciclo 2027-28 antes de su defensa.

## Suscripciones

**Cero altas nuevas esta semana, y es deliberado.** Las tres ramas buscaron
canal nuevo y las tres prefirieron no proponer nada antes que inventar una
URL: el único candidato de formación era la lista del IBG de Boulder, cuya
dirección de alta no se pudo verificar, y en grupos las dos ideas (búsquedas
guardadas de RePORTER, alertas de la revista *Behavior Genetics*) tampoco
tenían URL comprobable. Una suscripción con URL inventada es peor que no
tenerla.

**Pendientes: 36.** `owner_status.json` sigue vacío, así que por definición
toda fila TODO del TSV sin marca suya cuenta como pendiente. Las de reloj más
apretado siguen siendo SUB-0017 (cuenta de reservas de Bristol, que es la
puerta de T-0007 y cierra el 11 de noviembre), SUB-0030 (alta en la ESHG para
2027) y SUB-0036 (alta en la ESRS, requisito de cuatro líneas de ayudas).

## Nota de mantenimiento — sexto aviso, y ya son cuatro ficheros por encima

`groups.tsv` **231 KB**, `sources.tsv` **247 KB**, `changelog.tsv` **325 KB**
y `events.tsv` **63 KB**: los cuatro por encima del umbral de 60 KB, y
`events.tsv` lo cruzó la semana pasada. **El troceo lo hace una persona**,
porque exige tocar `tools/build_page.py` y `tools/build_xlsx.py` en el mismo
commit, y eso no se hace sin vigilancia al final de una pasada. Sexta semana
señalado.

## Qué perseguiría la semana que viene con más presupuesto

1. **El laboratorio nuevo de Grotzinger en la MUN** (L-0007): si su
   financiación de genomic SEM le ha seguido a Canadá, es la mejor plaza no
   anunciada de la base.
2. **Los satélites de ESHG 2027 y ASHG 2027**, que no se alcanzaron en toda la
   pasada y es donde viven los *workshops* de PRS: el punto sin tocar de más
   valor en eventos.
3. **Cuatro correos, no cuatro búsquedas**: `IBGworkshop@colorado.edu` (plazo
   y tarifa de Boulder), `smartbiomed_info@au.dk` (T-0012),
   `info@cardio-care.ch` (T-0023) y la tarifa real de Bristol entrando por su
   sistema de reservas. Lo que falta ya no está publicado en ninguna parte.
4. **L-0053 Warrier por UKRI Gateway**, más Lewis/Breen (L-0006) y McIntosh
   (L-0015) en el mismo barrido, igual que el lote de RePORTER de esta semana.
5. **URLs correctas de los portales de Tartu** (L-0009, L-0013) y reintento de
   CTG (L-0001, L-0012), los cuatro grupos que se quedaron sin comprobar por
   bloqueo.
6. **Comprobar si Huckins (L-0017) tiene algún R01 propio administrado en
   Yale**: su dinero de horizonte largo está administrado en UNC y en Mount
   Sinai, así que una línea de postdoc en Yale no está evidenciada.
