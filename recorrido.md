---
title: 'Vistas emergentes: un recorrido'
short_title: Recorrido
label: recorrido
---

Esta página explica el tiro parabólico apoyándose en todos los recursos de las páginas anteriores, **sin repetir ninguno**: los cita. Al pasar el ratón por encima de cada cita aparece una ventana emergente con la ecuación, la figura, el vídeo, el código o el diagrama citado. El lector consulta lo que necesita sin perder el hilo de la explicación.

Léela primero como lo haría un estudiante, deteniéndote en las citas. Después, el último apartado muestra cómo se escriben.

## El fenómeno

Cuando lanzamos un objeto con cierta velocidad y cierto ángulo, describe una curva: primero sube, se frena, y luego cae. La [animación del lanzamiento a 45°](#vid-trayectoria) lo muestra fotograma a fotograma, y la [simulación de PhET](#sim-phet) permite probar con otros ángulos y velocidades.

## Dos movimientos a la vez

La clave es separar el movimiento en dos. La velocidad inicial se descompone en una parte horizontal y otra vertical, como muestra el [esquema de componentes](#fig-componentes). Cada parte evoluciona por su cuenta, según las [ecuaciones de la velocidad](#eq-velocidad):

- en horizontal no actúa ninguna fuerza, y la velocidad no cambia;
- en vertical actúa la gravedad, que la reduce hasta anularla en el punto más alto y la hace negativa al bajar.

## La posición en cada instante

De ahí salen las ecuaciones de la posición: la horizontal, [](#eq-x), crece de forma uniforme, y la vertical, [](#eq-y), dibuja una parábola. Las dos gráficas de [](#fig-posicion) las representan frente al tiempo: compara la [posición horizontal](#fig-posicion-x) con la [vertical](#fig-posicion-y).

## Cuánto llega y cuánto sube

Juntando las dos ecuaciones se obtienen dos resultados útiles: el **alcance**, [](#eq-alcance), y la **altura máxima**, [](#eq-altura). El alcance depende del ángulo a través de $\sin 2\theta$, así que es máximo a 45°. La [gráfica de las tres trayectorias](#fig-trayectorias) lo confirma: a 30° y a 60° se llega al mismo punto, más cerca que a 45°.

El [diagrama de pasos](#diag-calculo) resume el razonamiento, y el [programa en Python](#code-alcance) hace el cálculo. El fichero completo, con la trayectoria punto a punto, está en [](#code-trayectoria).

## Cómo se escriben las citas

Cada recurso citado tiene una **etiqueta**, puesta al crearlo con `:label:` (figuras, código, diagramas, vídeos, iframes) o entre paréntesis tras una ecuación `$$ … $$ (etiqueta)`. Hay dos formas de citarla:

Sin texto: `[](#eq-alcance)`
: MyST pone el texto. Para una ecuación, su número: [](#eq-alcance). Para una figura, la palabra *Figure* y su número: [](#fig-trayectorias). La palabra sale en inglés, como el resto de los rótulos del tema.

Con texto propio: `[la gráfica de las trayectorias](#fig-trayectorias)`
: El texto lo escribes tú, y puede integrarse en la frase con naturalidad: [la gráfica de las trayectorias](#fig-trayectorias). Es lo que se ha usado en casi toda esta página.

En los dos casos, la vista emergente es la misma. También se puede citar una página entera por su etiqueta, como [la de ecuaciones](#ecuaciones): la ventana emergente muestra el principio de la página.

:::{tip} Buenas prácticas
- **Un prefijo por tipo de recurso** en las etiquetas: `fig-`, `eq-`, `code-`, `diag-`, `vid-`, `sim-`. Así se sabe qué se cita sin buscarlo.
- **La cita complementa, no sustituye.** La frase debe entenderse sin abrir la ventana emergente: en papel, o en un móvil, no hay ratón.
- **Citar en lugar de repetir.** Si una fórmula se necesita en tres páginas, se escribe en una y se cita en las otras dos. Así, una corrección se hace en un solo sitio.
:::

:::{note} Más adelante
Las etiquetas y las referencias dan para mucho más: citar elementos de otros proyectos, reutilizar contenido incrustándolo, cambiar el texto automático de las citas… Es el tema del proyecto 3.
:::
