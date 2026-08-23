# SETUP — puesta en marcha, paso a paso

Escrito el 2026-08-23, al crear la estructura. Este fichero es la lista de
tareas para dejar el sistema corriendo **en la cuenta de ella** (GitHub y
claude.ai). El diseño y el contrato están en `README.md`; aquí sólo está el
orden de montaje. Casi todo es una vez y se acabó.

Los pasos replican la puesta en marcha del tracker de funding de PitAssist,
que ya funciona en producción, con sus lecciones incorporadas. Donde este
documento diga «lección», créetela: cada una costó al menos una pasada rota.

---

## 0. Definir el perfil (bloquea todo lo demás)

1. Sentaos y rellenad `prompts/profile.md` juntos: cada `[TODO]` es una
   decisión de ella (líneas de investigación, geografías sí/no, qué quiere
   después del doctorado, relojes de elegibilidad…).
2. Repasad los `[TODO]` de `prompts/branches-*.md` (países, instituciones
   objetivo, revistas, congresos, sectores de industria) y las filas semilla
   de `data/sources.tsv` marcadas `[TODO]` (borrad las de países que no
   entren en juego, afinad las queries).
3. Borrad la línea `PROFILE-INCOMPLETE` de `profile.md` cuando esté completo.
4. Regenerad y commitead:

   ```bash
   python3 prompts/build_prompts.py
   git add -A && git commit -m "perfil: definido"
   ```

**Guardarraíl:** mientras `PROFILE-INCOMPLETE` o algún `[TODO]` siga en el
perfil, las rutinas se niegan a investigar (paran con ALERTA). Se pueden crear
las routines antes de definir el perfil, pero no harán nada útil hasta este
paso.

## 1. Crear el repo en SU cuenta de GitHub

```bash
cd ~/Projects/research-opportunities          # o donde se haya clonado
git remote add origin https://github.com/<SU-USUARIO>/research-opportunities.git
git push -u origin main
```

- **El repo debe ser público** para que Pages sea pública en una cuenta
  gratuita (en repos privados, Pages exige plan de pago).
- ⚠️ **Público significa público**: `prompts/profile.md` se verá desde
  internet. Escribid el perfil como si fuera su página web profesional —
  líneas de investigación, técnicas, geografías— y **nada sensible**: ni fecha
  de nacimiento completa, ni dirección, ni situación de visados más allá de lo
  imprescindible («EU citizen» basta). Si en el paso 0 salió algo íntimo,
  reformuladlo o valorad repo privado + plan de pago.

## 2. Activar GitHub Pages (pública)

En el repo: **Settings → Pages → Build and deployment → Source: GitHub
Actions**. Nada más: `build.yml` ya sube el artefacto y despliega. El primer
push debería dejar el workflow `build` en verde y la página servida en la URL
que Pages enseñe (guardadla en el navegador de ella).

Verificación: la página abre, y el botón «descargar Excel» baja
`research.xlsx` (por eso el Excel vive en `docs/`).

## 3. Ajustar la única constante local de la página

En `tools/build_page.py`, cerca del principio:

- `MAILBOX = 'CONFIGURAR-buzon@gmail.com'` → el Gmail de ella (el que leen las
  rutinas). La pestaña Suscripciones lo enseña para recordar con qué buzón
  darse de alta en cada alerta.
- (El nombre del repo no hay que tocarlo: en CI lo inyecta
  `GITHUB_REPOSITORY`; el valor `OWNER/research-opportunities` sólo afecta a
  vistas locales.)

## 4. Gmail de ella

1. En **su cuenta de claude.ai**: Settings → Connectors → conectar **Gmail**
   (su dirección). Las routines heredan los conectores de la cuenta: no hay
   nada que configurar por rutina.
2. En su Gmail, crear la etiqueta **`Research`** (tal cual, es la que buscan
   los prompts).
3. Opcional pero recomendado: filtros de Gmail que etiqueten como `Research`
   los remitentes de alertas (EURAXESS, jobs.ac.uk, Nature Careers…) según se
   vaya suscribiendo — la pestaña Suscripciones de la página lleva la lista de
   pendientes.

**Lección (cara):** la herramienta de etiquetado quiere el **ID** de la
etiqueta, no el nombre. Eso ya está resuelto dentro de los prompts; no hay que
hacer nada, pero si un día el etiquetado «falla», empezad por ahí antes de
tocar permisos.

**Privacidad:** el prompt limita la lectura a oportunidades y prohíbe citar
correspondencia personal en ficheros o informes. Aun así, es su buzón entero
lo que el conector expone: que ella lo sepa y esté de acuerdo antes de
conectar.

## 5. Crear las tres routines (en SU cuenta)

Las routines corren en la nube de Anthropic bajo **su** cuenta de claude.ai
(necesita un plan con Claude Code). Se crean desde una sesión de Claude Code
logueada en su cuenta, con `/schedule`, o en https://claude.ai/code/routines.

**Antes de crear nada, comprobar la cuenta activa de la CLI** — lección: un
404 de routines «desaparecidas» fue simplemente estar logueado en otra cuenta,
y recrearlas por error duplicó pasadas:

```bash
python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.claude.json')))['oauthAccount']['emailAddress'])"
```

Configuración de las tres (idéntica salvo nombre, cron y fichero de prompt):

- **Fuente:** `github.com/<SU-USUARIO>/research-opportunities` (la GitHub App
  de Claude pedirá acceso al repo la primera vez).
- **Modelo:** `claude-opus-5`. **Herramientas:** Bash, Read, Write, Edit,
  Glob, Grep, WebSearch, WebFetch, Task, TodoWrite.
- **Entorno:** el de por defecto de su cuenta, con **Network access = Full**
  (ver §7 — con `Trusted` las rutinas no pueden abrir casi ninguna web útil).

| routine | cron (UTC) | hora Madrid (verano) | prompt del repo |
|---|---|---|---|
| research — positions | `1 22 * * 0` | lunes 00:01 | `prompts/out/positions.md` |
| research — fellowships | `0 2 * * 1` | lunes 04:00 | `prompts/out/fellowships.md` |
| research — ecosystem | `0 6 * * 1` | lunes 08:00 | `prompts/out/ecosystem.md` |

⚠️ El cron es **UTC**: las 00:01 del lunes en Madrid son las 22:01 del
**domingo** en UTC — por eso la primera lleva `* * 0`. Si alguien lo
«corrige» a lunes, esa rutina se irá a la noche del lunes al martes. En
invierno (CET) las tres se adelantan una hora local; el escalonado de cuatro
horas se conserva, que es lo que importa.

**Prompt del disparador** — deliberadamente mínimo, porque el prompt de verdad
vive en el repo (editar `prompts/` cambia la rutina sin tocar el disparador):

> Eres la rutina semanal «research — positions». El repositorio
> `<SU-USUARIO>/research-opportunities` ya está clonado en tu directorio de
> trabajo. Lee el fichero `prompts/out/positions.md` y síguelo al pie de la
> letra: ese fichero es la única fuente de instrucciones y, si contradice
> cualquier cosa de este disparador, gana el fichero. No pidas confirmación de
> nada: nadie está mirando.

(Las otras dos, igual con `fellowships.md` y `ecosystem.md`.)

Para **modificarlas** después: `/schedule` desde una sesión suya. Para
**borrarlas**: sólo la web (https://claude.ai/code/routines) — la API sólo
desactiva.

## 6. Token para los botones de estado de la página

Para que ella pueda marcar `leído / en curso / descartado…` desde la página:

1. En **su** GitHub: Settings → Developer settings → **Fine-grained tokens** →
   Generate new token.
2. Resource owner: ella; Repository access: **sólo** `research-opportunities`;
   Permissions: **Contents: Read and write**. Nada más. Caducidad: la máxima
   que ofrezca — y apuntad la fecha: el día que caduque, los botones dejarán
   de guardar y habrá que generar otro y volver a pegarlo.
3. En la página publicada: botón **«conectar con GitHub»** → pegar el token.
   Se queda en el localStorage de su navegador; no se sube a ningún sitio.
4. Verificación: marcar una fila cualquiera → en el repo aparece un commit
   «estado: actualizado desde la pagina» y el CI regenera.

El mismo token alimenta el cajetín «proponer una fuente» de la pestaña
Sistema (escribe en `data/source_inbox.json`; la siguiente pasada completa la
fuente).

## 7. El nivel de red del entorno: Full, no Trusted

Lección que tumbó dos pasadas del tracker hermano: cada entorno de ejecución
de claude.ai/code tiene un **Network access** (`None` / `Trusted` /
`Full` / `Custom`) y el de fábrica es `Trusted`, cuya lista blanca son
registros de paquetes y APIs de nube — ni EURAXESS, ni universidades, ni
funders. El síntoma es engañoso: **git y el conector de Gmail funcionan igual**
(van por otros canales), así que la rutina empuja commits perfectamente
mientras reporta «403 en todos los hosts».

Se cambia en claude.ai/code, en el icono de nube con el nombre del entorno
encima del cuadro de mensaje → engranaje → **Network access → Full**. `Custom`
no sirve: estas rutinas existen para descubrir fuentes nuevas, y no se puede
poner en lista blanca un dominio que aún no conoces.

## 8. Primera pasada y verificación del lunes

Disparad una routine a mano (botón run de la web de routines) antes de esperar
al lunes. Checklist — el mismo del tracker hermano:

1. `git log --oneline` — commits de la rutina + el del CI detrás.
2. `runs/` — un informe `<fecha>-<rutina>.md`; si empieza por ALERTA, eso es
   lo primero que hay que leer.
3. La página — «Novedades de la semana» poblada y contadores vivos.
4. `data/owner_status.json` — intacto (las rutinas no lo tocan).
5. Si la rutina entregó por rama `claude/*` + PR en vez de main, el push a
   main le fue rechazado: mergear el PR y revisar la política de la cuenta
   antes del lunes.

## 9. Opcional: respaldo del jueves

Si algún lunes la cuota de su cuenta tumba las pasadas (al tracker hermano le
pasó: cinco pasadas seguidas), se puede duplicar el juego de routines en una
segunda cuenta con los mismos crons movidos al jueves (`* * 3` / `* * 4`).
Leen los mismos `prompts/out/*.md`, así que no hay nada que mantener por
duplicado. No lo montéis de entrada: es la solución a un problema que quizá
nunca aparezca.

## 10. Avisos heredados, por si acaso

- **No apuntar el sandbox de la app de escritorio de Claude a esta carpeta
  para hacer git**: el montaje no puede borrar `.lock` y deja `.git/` con
  candados huérfanos («Another git process seems to be running»). Si pasa:
  `rm -f .git/*.lock` desde el Terminal. Las routines no tienen este problema
  (clonan en la nube).
- **Los TSV se parten cuando pasan de ~60 KB**, por geografía o sub-tipo,
  nunca por año de plazo, y lo hace un humano tocando los dos generadores en
  el mismo commit. Las rutinas tienen orden de avisar, no de partir.
- **Si un fichero generado sale mal**, el bug está en `tools/`, no en
  `docs/`: `docs/` nunca se edita a mano.
