# positions — 2026-09-21

Cinco ramas, las cinco completadas. El buzón se leyó y funcionó. Nada roto,
ninguna ALERTA.

## Los números, sacados del diff (`git diff HEAD~1`), no de mi memoria

| fichero | altas | modificadas |
|---|---|---|
| `data/postdocs.tsv` | 5 (P-0036 … P-0040) | 15 |
| `data/jobs.tsv` | 1 (J-0015) | 3 |
| `data/sources.tsv` | 10 (SRC-0148 … SRC-0157) | 23 sólo en `Last_Checked` |
| `data/subscriptions.tsv` | 1 (SUB-0018) | 0 |
| `data/changelog.tsv` | 24 apuntes | 0 |

Total: 82 inserciones, 41 supresiones en 5 ficheros. **La cosecha de esta
semana está en las verificaciones, no en las altas**: 18 filas contrastadas
contra su fuente y 5 cierres. Cinco altas de postdoc, ninguna por encima de
Fit 3: la semana ha sido pobre en oferta y prefiero decirlo a inflarla.

## Las tres cosas que merecen tu atención

**1. El plazo de dos días hábiles del FIN MIR existe y ahora tiene norma
detrás (J-0010, Sacyl).** Era el encargo pendiente de la semana pasada y ha
quedado resuelto abriendo el PDF oficial: el art. 15 de la ORDEN SAN/713/2016
fija dos días hábiles **desde el día siguiente a la finalización oficial** de
la residencia. Dos matices que no teníamos y que cambian el cálculo: tener el
certificado antes **no** adelanta el cómputo, y la fecha que vale es la del
Ministerio en la guía del residente, **no la de tu contrato**. Si tu fecha
oficial es el 22-05-2027 (sábado), tu límite de alta sería el **25-05-2027**.
Es un XS de esfuerzo con una ventana de 48 horas: conviene que en enero de
2027 confirmes la fecha oficial de tu promoción.

**2. La vía transitoria a Genética Médica y de Laboratorio sigue sin moverse,
y la espera ya es el dato (J-0003).** El listado de audiencia pública de
Sanidad de hoy sólo tiene dos proyectos vivos y ninguno es de Genética. La
cronología que hemos podido fechar: resoluciones de inicio en junio de 2025,
consulta previa el 01-07-2025 y, el 23-12-2025, la DG de Ordenación
Profesional declarando los borradores «prácticamente ultimados». **Nueve meses
después siguen sin salir.** La prensa sectorial (Tier 2, registrada como tal)
apunta a primeras plazas en el MIR 2027, lo que obligaría a que el borrador
apareciese en los próximos meses. Tu riesgo aquí está intacto y SUB-0001
(alertas del BOE) sigue sin dar de alta.

**3. UQ R-68861, con Loic Yengo, es lo mejor del lote académico y aun así no
es para ahora (P-0029).** Leída por la API de Workday porque la ficha es una
SPA vacía: sigue viva, publicada el 2026-09-11, 2,5 años, AUD 106.294-141.545
más 17% de superannuation, PI Prof. Loic Yengo (IMB). Es tu línea 1 exacta.
Choca con tu calendario —arranca ya y tú no estás libre hasta mediados de 2027
o febrero de 2028—, así que se queda en Fit 3. **El valor real de esta fila es
el nombre**: escribir a Yengo en 2027, con la estancia en QIMR Berghofer como
gancho natural, vale más que la plaza en sí. Conflicto de plazo declarado y
sin resolver: el texto del anuncio dice «lunes 12 de octubre de 2026, 23:00
AEST» y el campo `endDate` de Workday dice 2026-10-13.

## Lo que ha cerrado

**P-0032** (KCL, Human Functional Genomics, ficha ya en 404), **P-0014**
(Cardiff, Moondance, retirada del portal eploy), **P-0018** y **P-0016** (KCL,
Clinical Research Fellow del IoPPN) y **P-0034** (Broad, Karczewski Lab, ficha
404 y ausente del listado).

Dos hallazgos colaterales sobre esos cierres, que hay que leer juntos:

- **P-0016 y P-0018 son casi con seguridad la misma plaza, duplicada desde dos
  fuentes.** El buscador propio de KCL da la oferta 155765 con cierre el
  **2026-09-18**, no el 2026-09-01 que teníamos en P-0016: el plazo se había
  extendido y nosotros no lo vimos. Ambas quedan CLOSED con el conflicto
  escrito en `Source_Note`. **Fusionarlas es decisión tuya**, la rutina no
  borra filas.
- **P-0027 (UCL, Research Fellow in Genetic Analysis) fue retirada de
  jobs.ac.uk dos semanas antes de su plazo publicado del 2026-10-04.** Queda
  CLOSED, pero es un cierre por desaparición del anuncio, no por vencimiento,
  y no se ha podido contrastar en el portal propio de UCL.

## `action_now` se queda sin una sola fila de positions, y no es un fallo

`tools/rebuild_action_now.py` ha preservado las 25 filas ajenas y ha aportado
**0 filas mías**. Lo he comprobado a mano y la regla está bien aplicada: la
selección pide Fit 4-5 que cierre en 90 días, más lo *sin plazo* con Fit **5**,
más cualquier cosa con `Competition_Level = LOW` y Fit ≥ 3. En mis dos
pestañas, **todo lo que puntúa 4 está cerrado o no tiene plazo publicado**
(P-0002, P-0003, P-0020; J-0002, J-0003, J-0007, J-0008, J-0010, J-0011,
J-0012), ninguna fila puntúa 5 y **ninguna tiene competencia LOW**.

Es decir: tus dos mejores carriles —las bolsas permanentes del sistema público
español y los postdocs de candidatura abierta— son estructuralmente *rolling*
y Fit 4, exactamente el hueco que la regla no recoge. **Esto lo decides tú, no
yo**: bajar el umbral de lo sin plazo de Fit 5 a Fit 4 metería de golpe las
seis bolsas autonómicas y la vía del BOE en la portada. Cambiar la regla toca
los tres prompts y el generador, y no es trabajo para hacer a ciegas al final
de una pasada.

## El buzón: funcionó, y está vacío

Etiqueta `Research` localizada por ID tras listar etiquetas una sola vez.
**Está vacía: 0 mensajes.** Pase A: 0 hilos. Pase B: 2 hilos, ninguno con
contenido de oportunidades. `inbox_triage` no recibe ninguna fila y no hubo
nada que etiquetar. Nada quedó PENDING.

El dato accionable es ese vacío: **a este buzón no llega ni una sola alerta de
empleo o becas**. Mientras siga así, la mitad de una de las cinco ramas es
estéril por construcción. Es el argumento más fuerte para dar de alta de una
vez SUB-0002 (EURAXESS) y SUB-0012 (jobs.ac.uk).

## Lo que no pude verificar, sin disfrazarlo

- **P-0010 CRG**: `recruitment.crg.eu` sigue en 403 y `crg.eu/en/jobs` da 404.
  Fila intacta, `Last_Verified` NO tocado: subirlo sería mentir.
- **P-0008 Broad / McCarroll**: bajada a UNVERIFIED. El portal Avature pagina
  de 6 en 6 e **ignora `searchKeyword`**, así que no aparecer en la página 1 no
  prueba que esté cerrada.
- **P-0020 Amgen deCODE** y **J-0012 GSK**: los puestos existen, las fichas son
  ilegibles para un agente. Ambas quedan como están, con la URL viva para que
  las abras tú. **Corrección al contrato de fuentes: `careers.amgen.com` deja
  de estar entre las que «funcionan bien»** — responde 200 pero sirve una SPA
  sin ofertas en el HTML.
- **P-0028 KCL Bioinformatician**: dos ramas lo vieron, una en jobs.ac.uk
  (Tier 2) y otra en el buscador de KCL (Tier 1) con la misma fecha de cierre.
  Se fija **LIKELY**, no VERIFIED, porque nadie llegó a abrir la ficha Tier 1
  completa. El desacuerdo queda escrito en la fila en vez de resuelto en
  silencio.
- **Bloqueos nuevos que conviene no volver a pagar**: `fjd.es` (403),
  `jobs.gsk.com` (armazón vacío), `www.training.nih.gov/jobs` (403), ASHG
  Career Center (CAPTCHA), `iislafe.es` y `navarrabiomed.es` (404),
  `idibaps.org` (302 a clinicbarcelona.org), portal Personio de Evidenze (feed
  XML vacío). Todos registrados en `sources.tsv`.
- **EURAXESS está roto para un agente, y ahora con prueba.** La URL de faceta
  que teníamos registrada (SRC-0046) devuelve los mismos 6.616 resultados que
  la búsqueda sin filtrar: **la faceta no se aplica**. Además las fichas
  individuales fallan a ratos. `sources.tsv` es de sólo apéndice y no he
  reescrito SRC-0046, pero **merece bajar a prioridad LOW**; hoy figura como si
  funcionase y cuesta presupuesto cada lunes. SUB-0018, dada de alta hoy, es el
  rodeo: el filtrado del lado del servidor sí funciona, pero la cuenta la
  tienes que crear tú.

## Nada tuyo se ha quedado obsoleto

`owner_status.json` sigue vacío: ninguna fila estaba marcada por ti, así que
ninguna de las 18 modificaciones de hoy te ha cambiado el mapa bajo los pies.

## Aviso de tamaño

**`data/postdocs.tsv` ha pasado a 80 KB y ya supera el umbral de ~60 KB de la
regla de división. Es mío y lo digo.** También siguen por encima
`fellowships.tsv` (161 KB), `sources.tsv` (103 KB), `changelog.tsv` (89 KB) y
`groups.tsv` (78 KB). Dividir obliga a tocar `tools/build_page.py` y
`tools/build_xlsx.py` en el mismo commit: lo decides tú, no una pasada
desatendida.

## Suscripciones

Añadida hoy: **SUB-0018**, alerta por correo de EURAXESS Jobs desde perfil de
investigador (HIGH). Es la única de la pasada, por debajo del tope de 2.

**Pendientes: las 18, todas TODO, ninguna dada de alta.** Por urgencia siguen
SUB-0009 (Fundación José Luis Castaño-SEQC, **cierra el 30-09-2026 y exige ser
socia al solicitar**: nueve días), SUB-0001 (BOE), SUB-0002 (EURAXESS),
SUB-0012 (jobs.ac.uk) y SUB-0017 (cuenta de reservas de Bristol, que se puede
crear desde el 2026-09-23).

## Qué perseguiría la semana que viene

Mount Sinai y Albert Einstein, que se quedaron sin re-verificar por
presupuesto; CIBERSAM centro por centro, que sigue siendo el agujero de España;
el buscador de KCL filtrado por IoPPN (tiene 15 plazas y sólo vimos 3); la URL
real del portal Oracle de Edinburgh y el patrón de búsqueda válido de
AcademicTransfer, las dos rutas que hoy se quedaron en 404; fechar ficha a
ficha las 5 plazas vivas de IGES (SRC-0155), que es la fuente nueva más
prometedora porque sí publica fecha; y el carril 1 puro, intacto esta semana:
Genomics England, Illumina y CROs grandes con equipo de genética estadística.
