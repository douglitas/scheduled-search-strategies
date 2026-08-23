# 2026-08-23 — positions (postdocs + jobs)

ALERTA (RESUELTA EL MISMO DÍA) — el push falló en su momento: main **y** la
rama de reserva `claude/*` fueron rechazadas con HTTP 403, «Claude doesn't
have GitHub access to douglitas/scheduled-search-strategies for your
organization». No era la protección de rama: la app de GitHub no tenía permiso
de escritura en este repo (lectura sí, el `fetch` funcionaba), así que tampoco
se pudo abrir el pull request que manda el contrato, y la vía de la API de
GitHub devolvió el mismo 403. La dueña instaló la app al ver el aviso y el
commit se subió sin cambios. Queda anotado porque explica por qué la página
estuvo unas horas sin reflejar esta pasada, y porque si el permiso se cae otra
vez el síntoma será exactamente este.

ALERTA: la búsqueda de texto libre de EURAXESS es inservible para esta rutina.
Tres parámetros distintos (`keywords=`, `search_api_fulltext=`, `search_text=`)
devolvieron siempre la misma lista genérica de 7.980 ofertas, así que la rama 1
no puede filtrar por «statistical genetics» ni por nada. Seguirá casi estéril
cada semana hasta que crees las alertas de búsqueda guardada de EURAXESS
(SUB-0002). No es un fallo del código: es el portal.

Primera pasada real del rastreador; la base estaba vacía, así que todo es alta.

## Recuento (de `git diff --stat HEAD~1`)

| Pestaña | Filas | Nota |
|---|---|---|
| postdocs | +17 | P-0001 … P-0017 |
| jobs | +6 | J-0001 … J-0006 |
| sources | +26 altas, 9 `Last_Checked` | 29 → 55 |
| subscriptions | +2 | tope de la pasada |
| inbox_triage | +1 | |
| changelog | +26 | |
| **action_now** | **0 filas** | ver abajo: no es un error |

## action_now sale vacía, y eso es el hallazgo, no un fallo

Ninguna de las 23 oportunidades cumple la regla de selección, y el motivo es el
mismo en las 23: **su calendario**. No puede incorporarse a nada antes del
22-05-2027 (fin de la residencia) y a nada que exija el doctorado defendido
antes de febrero de 2028 (ETA). Todo anuncio abierto hoy se habrá cubierto
mucho antes. De las cinco ramas no salió ni una sola candidatura que tenga
sentido presentar esta semana.

La consecuencia práctica es que el producto útil de esta rutina, este año, no
son candidaturas: son **grupos objetivo con contacto nominal, portales
mapeados y canales de alerta**. Conviene tenerlo presente al leer la página, o
parecerá que la rutina no encuentra nada.

## Las tres cosas que sí merecen acción

1. **J-0002 — Bolsa Única del SAS (Andalucía).** El único elemento realmente
   accionable del carril 2, y precisamente porque no es un anuncio: bolsa
   permanentemente abierta, con baremo y sin examen, en el servicio donde ya
   está. Inscripción el mismo mes en que tenga el título. **Hallazgo
   VERIFICADO que cambia el planteamiento: el RD 101/2025 (BOE 19-02-2025)
   suprimió Análisis Clínicos y Bioquímica Clínica y creó el título de
   LABORATORIO CLÍNICO**, así que al acabar en mayo de 2027 su título será ese
   — pero Madrid, Valencia y Murcia siguen llamando a la categoría «Análisis
   Clínicos» en sus catálogos. Hay que preguntar a personal de Málaga a qué
   código de bolsa se mapea, a principios de 2027, y no darlo por supuesto.
2. **J-0003 — vía transitoria a Genética Médica / de Laboratorio.** Estado a
   hoy, comprobado abriendo el listado oficial de audiencia pública de
   Sanidad: **no hay ventana abierta ni anunciada, y el RD ni siquiera ha
   entrado en trámite de audiencia**, pese a que en marzo de 2026 el
   Ministerio lo dio por «a punto». Es la diferencia entre que su carril
   clínico sea solo laboratorio o sea genética clínica, y el plazo de
   solicitud será corto. De ahí SUB-0001 (alerta del BOE), que es la
   suscripción de mayor consecuencia de las dos que se han propuesto.
3. **P-0002 — MPI Nijmegen, grupo de Beate St Pourcain.** La coincidencia de
   contenido más exacta de toda la pasada: genética de los correlatos del
   comportamiento social desde la infancia hacia trayectorias de salud mental
   — sus tres líneas a la vez —, con SEM, metaanálisis y neuroimagen solo como
   deseables, que es justo donde su formación de QIMR encaja sin sobrevenderla.
   Países Bajos, sin visado, salario alto. No puede presentarse (exige
   doctorado defendido, arranque dic-2026), así que la acción es escribirle en
   Q1-Q2 2027. Detrás, **P-0001 (NCRR/iPSYCH, Aarhus)** como el canal que más
   se repite en la UE y **P-0005 (CTG, Posthuma, VU Ámsterdam)** como la mejor
   candidata a acogida MSCA-PF.

## Lo que está cerrado o ya no existe

P-0001 (inicio jun-2026), P-0004 (ERC StressGene: la URL de EURAXESS ya
redirige a la búsqueda genérica, señal de anuncio expirado), P-0005 (plazo
18-06-2025; la URL propia de la VU da 404), P-0009 (edición 2026 cerrada el
19-02-2026), J-0004 (SERMAS: convocatoria de 2021 resuelta entre enero y julio
de 2026 — ciclo real de 4,5 años, dato útil para calibrar), J-0005
(estabilización Ley 20/2021, irrepetible por diseño), J-0006 (OPE 2025 del
SMS). P-0015 cierra el 27-08 y P-0016 el 01-09: quedan registrados solo para
dejar constancia de que el IoPPN mantiene un flujo de puestos de vía clínica.

## Conflicto de fuentes sin resolver (no lo he decidido por mi cuenta)

- **P-0007 (Aarhus QGG, Doug Speed):** la rama 1 leyó plazo 01-05-2026 (por eso
  figura CLOSED) y la rama 2 lo vio como anuncio vivo sin plazo. Ambas
  coinciden en el arranque 01-10-2026. Nature Careers bloquea la descarga, así
  que ninguna pudo abrir la ficha. Queda como UNVERIFIED.
- **Vía transitoria:** la página de la AEGH contiene texto que sugiere
  aprobación en Consejo de Ministros y publicación en BOE, sin fecha ni número
  de disposición; con toda probabilidad se refiere al RD de Formación
  Sanitaria Especializada, no a los de Genética. Consignado como conflicto, no
  como hecho.

## Bloqueos encontrados (para no volver a gastar presupuesto en ellos)

Están en las Notas de las fuentes nuevas, pero estos afectan a fuentes que ya
eran tuyas y `sources.tsv` es de solo apéndice, así que no he tocado sus Notas:

- **Nature Careers (SRC-0003): HTTP 400 a cualquier descarga automática.** Es
  el bloqueo más caro de la pasada: llevaba los dos mejores postdocs de
  genética psiquiátrica/estadística (P-0003 Mount Sinai, P-0007 Aarhus) y
  ninguno pudo abrirse, de ahí que queden UNVERIFIED. Una alerta por correo de
  Nature Careers sería el arreglo; no cabía en el tope de 2 suscripciones.
- **FindAPostDoc (SRC-0006) y Academic Positions (SRC-0005): HTTP 403.**
- Fuera de tus fuentes: Cardiff (403, usar el portal eploy), CRG (403), Aarhus
  (403), ESRS (403), BGA (403 / módulo vacío), deCODE (renderizado con
  JavaScript, cero anuncios extraíbles), Edimburgo (solo expone el portal
  Oracle interno), Erasmus MC (sus puestos de investigación no salen por su
  propio portal), ESHG (URL rota), HigherEdJobs (el buscador exige POST),
  Genomics England (careers 404), gacetamedica.com (403).

## Lo que no pude verificar o alcanzar

- P-0003, P-0010, P-0011: fichas no abiertas por bloqueo; plazo, duración y
  salario sin confirmar. Las URLs funcionan en navegador.
- P-0008 y P-0017: los listados del Broad y de QIMR no exponen fecha de cierre
  ni salario en la vista de lista.
- P-0015 y P-0016: enlaces reconstruidos desde rutas relativas del listado de
  KCL, no abiertos uno a uno. Provisionales.
- **España quedó sin cubrir en la rama 3**: CIBERSAM (su URL de ofertas da
  404), CNIO e IMIM no se alcanzaron al agotarse el presupuesto.
- **Australia quedó sin cubrir en la rama 2**: Seek bloquea, y QIMR era de otra
  rama. Su mejor vínculo personal produjo cero por esa vía.
- **Comunicación científica (carril 3): cero filas, deliberadamente.** No
  apareció ni un anuncio Tier 1 verificable, solo agregadores y notas de
  agencias de selección. Inflar eso habría sido relleno.

## Suscripciones pendientes

`SUB-0001` (alertas del BOE, HIGH) y `SUB-0002` (búsquedas guardadas de
EURAXESS, HIGH), ambas TODO. Ojo: la URL exacta de alta del servicio de
alertas del BOE no está confirmada — solo el dominio.

El tope es de 2 por pasada, así que estas quedan en cola para las próximas, en
este orden: alerta por correo de **Nature Careers** (arregla un bloqueo duro),
alertas de **jobs.ac.uk**, búsqueda guardada de **AcademicTransfer** (habría
evitado perder el postdoc del CTG), **ISPG** (el canal que más rindió),
alertas de **Cardiff** y **KCL**, boletín de la **AEGH**, y las inscripciones
en bolsa de **ICS** y **GVA**, que solo son ejecutables con el título en mano.

## Nada de la dueña quedó desactualizado

`owner_status.json` está vacío y no había filas marcadas, así que ninguna
valoración suya se ha quedado obsoleta bajo sus pies.

## Dos avisos de mantenimiento

- `data/postdocs.tsv` va por 36 KB en la primera pasada. El umbral de división
  es ~60 KB y no se divide sin tocar los dos generadores en el mismo commit:
  probablemente haya que hacerlo en unas semanas, y es tarea tuya, no de una
  rutina desatendida.
- Cinco filas de `sources.tsv` que no pretendía tocar (SRC-0008, 0009, 0010,
  0023, 0024) aparecen en el diff. **Su contenido no ha cambiado**: solo el
  entrecomillado del TSV, porque el escritor csv normaliza las comillas
  internas que el fichero sembrado a mano llevaba sin escapar. Comprobado
  campo a campo: los valores leídos son idénticos. Es una normalización de una
  sola vez.
- SRC-0029 sigue siendo el marcador `[TODO]` de portales por CCAA. No lo he
  reescrito (el fichero es de solo apéndice), pero ya está cubierto por
  SRC-0050 a SRC-0054: quizá quieras retirarlo a mano.

## Qué perseguiría la semana que viene con más presupuesto

Cerrar los huecos de esta pasada antes que ampliar: CIBERSAM/CNIO/IMIM
(España se quedó en nada en la rama 3), QIMR y Australia vía LinkedIn en lugar
de Seek, la URL externa de vacantes de Edimburgo, el tablón del ESHG a mano, y
la búsqueda de legislación del BOE por título con «Genética» para cerrar el
conflicto de la AEGH. En genética psiquiátrica, jobs.ac.uk filtrado por
empleador a Cardiff (MRC CNGG) y Bristol (MRC IEU), llamativamente ausentes.
