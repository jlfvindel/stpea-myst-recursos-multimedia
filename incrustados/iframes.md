---
title: Páginas web incrustadas (iframes)
short_title: Iframes
label: iframes
---

Un **iframe** es una ventana a otra página web dentro de la tuya. Sirve para incorporar a un material recursos interactivos que ya existen: simulaciones, calculadoras gráficas, mapas, presentaciones, formularios… El visitante los usa sin salir de la página.

## Una simulación interactiva

Las simulaciones PhET, de la Universidad de Colorado Boulder, están pensadas para incrustarse en otros materiales. Esta permite lanzar proyectiles cambiando el ángulo, la velocidad y otras condiciones:

```markdown
:::{iframe} https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_all.html?locale=es
:label: sim-phet
:title: Simulación de tiro parabólico de PhET
:width: 100%

Simulación «Movimiento de un proyectil». PhET Interactive Simulations, University of Colorado Boulder (licencia CC BY 4.0).
:::
```

Resultado:

:::{iframe} https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_all.html?locale=es
:label: sim-phet
:title: Simulación de tiro parabólico de PhET
:width: 100%

Simulación «Movimiento de un proyectil». PhET Interactive Simulations, University of Colorado Boulder (licencia CC BY 4.0).
:::

La parte final de la dirección, `?locale=es`, pide la simulación en español. Muchos recursos incrustables aceptan opciones así: conviene mirar su documentación.

Las opciones de la directiva son:

`:title:`
: Describe el contenido para los lectores de pantalla. Conviene ponerlo siempre.

`:width:`
: El ancho, en porcentaje de la columna o en píxeles. El alto se ajusta solo.

`:label:` y el texto
: Como en una figura: el iframe se numera, lleva pie y se puede citar ([](#sim-phet)).

`:placeholder:`
: Una imagen que sustituye al iframe en las exportaciones que no son web, como el PDF, donde no puede funcionar una página interactiva.

## Dónde encontrar la dirección

La dirección de un iframe no siempre es la que se ve en el navegador. Las plataformas que permiten incrustar suelen ofrecer un botón *Insertar* (*Embed*) con un código `<iframe src="…">`. De ese código, lo que va en la directiva es lo que hay entre las comillas de `src`.

:::{warning} No todas las páginas se dejan incrustar
Muchos sitios lo impiden por seguridad (bancos, redes sociales, buena parte de los periódicos…). En ese caso, el recuadro aparece vacío o con un mensaje de error. No es un fallo de MyST: la decisión es del sitio incrustado. La alternativa es un enlace normal.
:::

:::{note} Y en el aula virtual
Lo mismo que hace aquí un iframe lo hace Moodle cuando incrusta tu sitio MyST en una página del curso, o cuando incrusta en una de tus páginas un recurso externo. En ambos sentidos rigen las mismas limitaciones.
:::

:::{tip} Para explorar más
- El catálogo de simulaciones PhET, en español: <https://phet.colorado.edu/es/simulations/browse>.
- Otros recursos que ofrecen código para incrustar: GeoGebra, Desmos, formularios de encuestas, mapas de OpenStreetMap…
:::
