# 2026-09-07 — positions (postdocs + jobs)

ALERTA — **EURAXESS ha dejado de servir para esta rutina, y ahora por
completo.** La pasada anterior dejó anotado que el buscador de texto libre
estaba roto pero que las facetas sí filtraban. Ya no: la rama 1 extrajo los
ids de faceta reales del HTML (Estadística 397, Epidemiología 181,
Neurociencias 331, Neurobiología 325, Neuropsicología 330, Psicología 364,
Medicina 314, Biología 41, Informática 210) y comprobó que Estadística y
Epidemiología devuelven **la misma lista de 6.683 ofertas, con los mismos diez
primeros resultados**, idéntica a la consulta sin filtrar. Peor: la URL de un
anuncio concreto (`/jobs/557315`) devuelve **también esa misma lista**, así que
el servidor sirve la misma cáscara a cualquier ruta `/jobs/*`. Consecuencias
prácticas: (1) la rama 1 seguirá dando cero hasta que crees las búsquedas
guardadas de EURAXESS (**SUB-0002**, que sube a ser la suscripción más urgente
de la lista); (2) **la nota de SRC-0046 afirma hoy lo contrario y conviene que
la corrijas a mano** — `sources.tsv` es de solo apéndice y no la he reescrito;
(3) un enlace roto de EURAXESS ya no prueba que un anuncio haya expirado.

## Recuento (de `git diff --stat HEAD~1`)

| Pestaña | Cambio | Detalle |
|---|---|---|
| postdocs | **+5 altas, 9 modificadas** | P-0018…P-0022; tocadas P-0002, 0004, 0006, 0007, 0012, 0013, 0014, 0015, 0016 |
| jobs | **+3 altas, 1 modificada** | J-0007…J-0009; tocada J-0003 |
| sources | +10 altas, 19 `Last_Checked` | 96 → 106 |
| subscriptions | +2 | SUB-0011, SUB-0012 (tope de la pasada) |
| inbox_triage | 0 | el buzón no trajo nada relevante |
| changelog | +30 | |
| **action_now** | **0 filas mías** | 13 ajenas preservadas byte a byte |

Aviso de calendario: **la ranura del 2026-08-31 de esta rutina no se ejecutó**
(sólo hay informe de `fellowships` ese día), así que esta pasada cubre dos
semanas. No hay commit de `positions` de hoy anterior al mío: sin colisión.

## action_now vuelve a salir sin filas de positions, y sigue sin ser un fallo

Es el mismo motivo estructural que en agosto: **su calendario**. Nada antes del
22-05-2027, y nada que exija el doctorado defendido antes de feb-2028 (ETA).
Todo lo que se anuncia hoy se cubre mucho antes. El producto útil de esta
rutina este año son canales, PIs con nombre y mecanismos permanentes.

**He corregido de paso un defecto de `tools/rebuild_action_now.py`.** Tomaba la
fecha de incorporación como sucedáneo de plazo también en plazas ROLLING, y eso
coló hoy a P-0002 en el puesto 1 con «85 días» de urgencia inventada: la fecha
de incorporación de una plaza rodante no cierra nada, y P-0002 es además una
plaza para la que **ella no es elegible** (exige doctorado ya defendido), justo
lo que el contrato manda mantener lejos de action_now. La única fila de toda la
base afectada por el cambio es P-0002, y las 13 filas de las otras rutinas
salen del diff idénticas. Está comprobado.

## Las tres cosas que sí merecen acción

1. **MSCA-PF 2027: una decisión que sólo puedes tomar tú, y tiene fecha.**
   Verificado el calendario (sorteando el bloqueo JS del Funding & Tenders
   Portal): convocatoria 2027 con **plazo 08-09-2027**, arranque may-2028,
   388,57 M EUR, todo marcado (TBC). La elegibilidad se mide por **la fecha de
   defensa**, no por la expedición del título. Con la defensa en feb-2028
   quedas fuera **por unos cinco meses**. Dicho al revés: **adelantar la
   defensa a antes de septiembre de 2027 te regala una ronda entera de
   MSCA-PF**, la vía que mejor encaja con tu perfil. No es una decisión de una
   rutina desatendida; es tuya, y conviene tomarla con tiempo. Anfitriones ya
   identificados y con gancho: Doug Speed (Aarhus QGG, `doug@qgg.au.dk`),
   Posthuma (CTG, VU) y St Pourcain (MPI Nijmegen).
2. **J-0007 — FIMABIS / IBIMA-Plataforma BIONAND. España deja de estar a
   cero, y el hallazgo es local.** Es el instituto de investigación **de tu
   propio hospital**, con ECAI de Bioinformática (Juan Antonio García Ranea) y
   grupos de neurociencia/psiquiatría. `ibima.eu/es/trabaja-con-nosotros` no
   lista ofertas: la **única** vía es el portal RFGI-SSPA
   (`rfgi.es/…/FIMAB_EM`), abierto y verificado hoy. Fit 4, VERIFIED,
   esfuerzo XS. Acción: escribir a la ECAI en Q4-2026 y revisar el portal
   semanalmente desde marzo de 2027.
3. **J-0003 — vía transitoria a Genética: sigue parada, y ahora sabemos más.**
   Verificado en Tier 1 hoy: el listado de audiencia pública de Sanidad tiene
   **un solo proyecto vivo y no es de Genética**, y en el BOE no existe ningún
   RD que establezca los títulos. Son **20 meses de anuncios sin acto**. Dos
   hallazgos nuevos con consecuencia real: (a) serán **dos reales decretos y
   dos títulos** — Genética Médica sólo para Medicina, Genética de Laboratorio
   también para Farmacia/Biología/Química/Veterinaria; (b) la disposición
   transitoria se anuncia al modo de Pediatría y Urgencias, **acreditando años
   de ejercicio en el área**, requisito que **no tendrás al acabar la
   residencia en mayo de 2027**. Eso no baja el Fit, pero sí tu elegibilidad
   real, y queda escrito en la fila.

Detrás, dos que merecen mención: **J-0008 (SERGAS)**, listas de contratación
temporal de FEA abiertas de forma continua en Galicia (Fit 4, VERIFIED), y
**P-0020 (deCODE genetics / Amgen, Reikiavik)**, postdoc de 4 años en genética
estadística + IA — tus líneas 1 y 2, **e Islandia es EEE: sin visado ni
patrocinio**. Inaplicable ahora, canal de primer orden para 2028.

## Lo que se ha cerrado

- **P-0012, P-0013, P-0015, P-0016**: cerradas por plazo vencido. Sólo P-0013
  (QMUL, ref DSM851) está VERIFIED, vista con su fecha de cierre 06-09-2026;
  las otras tres van como LIKELY, por plazo vencido y ausencia en las cinco
  búsquedas temáticas, sin abrir su ficha una a una.
- **P-0021** (Young Lab, UCLA) nace ya CLOSED: anuncio de feb-2026 caducado. Se
  registra porque el PI es un contacto con gancho para 2028.
- **J-0009** (Osakidetza) nace CLOSED: la bolsa se abrió el 06-07-2026 y cerró
  el 27-07-2026.
- **P-0006 (Oxford) NO está cerrada**: sigue abierta, cierre **11-09-2026**,
  39.424–47.779 GBP. VERIFIED, apareció en tres búsquedas distintas.

## Conflictos: uno cerrado, dos que dejo abiertos

- **CERRADO — P-0007 (Aarhus QGG, Doug Speed).** Segunda fuente independiente:
  plazo 1 de mayo, incorporación 01-10-2026, y la plaza cuelga de un **proyecto
  ERC** de Speed sobre métodos de clasificación de enfermedades. La ficha de
  Nature Careers sobrevivió al cierre sin mostrar plazo: ésa era toda la
  discrepancia. Queda CLOSED con Confidence LIKELY (nature.com sigue en 400).
- **ABIERTO — P-0014 (Cardiff, Moondance).** El portal eploy responde pero sólo
  sirve la página 1 de 3 y `?page=2` reenvía a la 1. Allí no hay nada de
  Moondance, pero sí un *Research Assistant/Associate (Statistics)* del Centre
  for Trials Research (ref 459) **con cierre 17-09-2026, la misma fecha que
  P-0014**. Pueden ser la misma plaza mal etiquetada. **No he tocado el Status**;
  la fila queda UNVERIFIED. Ábrela en el navegador si te interesa.
- **ABIERTO — el texto de la AEGH.** No pude reproducirlo: la portada de
  aegh.org no contiene hoy ninguna afirmación de aprobación en Consejo de
  Ministros. La hipótesis anterior sigue en pie y ahora tiene candidato
  concreto: **RD 203/2025, de 18 de marzo (BOE-A-2025-5405)**, que modifica el
  RD 589/2022 de formación sanitaria especializada y sí fue aprobado. Sin
  prueba de que sea el referente, no lo cierro.
- **ABIERTO, menor — P-0020.** El programa de postdocs de Amgen lista sólo
  Thousand Oaks, San Francisco, Burnaby y Copenhague, sin mencionar Reikiavik,
  mientras el anuncio sitúa la plaza allí.

## Lo que no pude verificar o alcanzar

- **Comunicación científica (carril 3): CERO filas por segunda pasada
  consecutiva, deliberadamente.** No apareció ni un anuncio Tier 1 verificable,
  sólo agregadores (Indeed, LinkedIn, Glassdoor, Jooble, BeBee) y notas de
  agencias de selección. Si te importa este carril, dilo y se ataca por otra
  vía (agencias MedComms una a una), porque por anuncios no sale.
- **Carril 1, empresa: cero filas.** Regeneron da 404 en su ruta de búsqueda;
  Genomics plc ya no lista puestos (sólo talent community en Ashby, render JS).
- **Australia: cero otra vez.** No toqué Seek. `careers.uq.edu.au` redirige a
  una ruta 404 y el Workday de UQ llega vacío. Una búsqueda apunta a dos plazas
  con nombre (PCTG: Jian Zeng / Peter Visscher; CHRC: Enda Byrne) pero la pista
  era un enlace de LinkedIn con pinta de caducado y no he creado filas con eso.
  **La próxima vez hay que atacar UQ por las páginas de los grupos, no por el
  portal de empleo.**
- **P-0019** (NIA/NIH) queda UNVERIFIED a propósito: el buscador de Science
  Careers funciona pero **sus páginas de detalle dan 403**; sin PI ni contacto.
- QIMR Berghofer: **cero vacantes abiertas**, verificado. VU Amsterdam: 22
  vacantes, ninguna de CTG/Posthuma ni del Twin Register. KCL: 21 puestos del
  IoPPN que la vista de lista no expone. Broad: muestra 6 de 35 sin decir
  laboratorio.
- **Cardiff y Bristol: la ausencia era real**, no un fallo de cobertura. Cinco
  búsquedas temáticas en jobs.ac.uk dan cero de ambas.

## Bloqueos nuevos (anotados para no volver a gastar presupuesto)

`ciberisciii.es` (403 en todo el dominio; la ruta viva sería `/empleo`, no la
del 404), `imim.es` y `researchmar.net` (403 los dos), jobs.ac.uk **filtro por
empleador** `/search/employer/<slug>/jobs` (**HTTP 500**), `cordis.europa.eu`
(cáscara JS), `erc.europa.eu/projects-statistics/erc-funded-projects` (404),
`api.tech.ec.europa.eu/search-api` (405 por GET), `qgg.au.dk/…/vacancies` (404)
y **au.dk entero** (403, no sólo `international.au.dk`), Science Careers fichas
de detalle (403), Regeneron careers (404), Ashby de Genomics plc (JS),
`boe.es/buscar/legislacion.php` por GET (rechaza los valores: usar WebSearch
acotado a boe.es o fichas `doc.php?id=BOE-A-…`), jobRxiv `?search_keywords=`
(sólo sirve la portada), `eshg.org/job-offers` (404), transparencia de FIMABIS
en juntadeandalucia.es (403). El tablón externo del IMIBIC está muerto (2023).

## Nada tuyo se ha quedado obsoleto

`owner_status.json` sigue vacío: no había ninguna fila marcada por ti, así que
ninguna valoración tuya se ha quedado atrás bajo tus pies. Las 9 filas de
postdocs y la de jobs que he modificado estaban todas en `Owner_Status = NEW`.

## Suscripciones

Añadidas hoy (tope de 2): **SUB-0011** (búsqueda guardada con aviso en el EU
Funding & Tenders Portal, HIGH — rodea el portal ilegible) y **SUB-0012**
(alerta por correo de jobs.ac.uk, HIGH — los plazos de ese tablón duran menos
que una semana entre pasadas, así que hoy se pierden por diseño).

Pendientes, todas TODO: SUB-0001 (BOE) y **SUB-0002 (EURAXESS, ahora la más
urgente de todas)**, SUB-0003…SUB-0010.

En cola para las próximas pasadas, por orden: alertas de vacantes de **QIMR
Berghofer** (RSS de TurboRecruit), alerta por palabra clave de **jobRxiv**,
búsqueda guardada de **AcademicTransfer**, **Amgen Careers** (rodea el portal
JS de deCODE) y **Talent Community del Broad**.

## Qué perseguiría la semana que viene

Atacar **UQ y Australia por las páginas de los grupos** (PCTG y CHRC con
nombres ya identificados), que es donde está su mejor vínculo personal y lleva
dos pasadas dando cero. Reabrir **P-0014** con el portal eploy paginado a mano
para cerrar el conflicto de Cardiff. Y, si de verdad quiere el carril de
comunicación científica, cambiar de método: ir agencia por agencia en vez de
esperar anuncios.
