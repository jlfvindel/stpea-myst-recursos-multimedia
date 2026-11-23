---
title: Diagramas con Mermaid
short_title: Diagramas
label: diagramas
---

**Mermaid** es un lenguaje para describir diagramas con texto: se escriben los elementos y sus conexiones, y MyST dibuja el diagrama. Su ventaja frente a una imagen es que se corrige editando una línea, sin abrir ningún programa de dibujo.

## Un diagrama de flujo

````markdown
```{mermaid}
flowchart LR
    A[Datos: v0 y ángulo] --> B[Componentes vx y vy]
    B --> C[Tiempo de vuelo]
    C --> D[Alcance]
    B --> E[Altura máxima]
```
````

Resultado:

```{mermaid}
flowchart LR
    A[Datos: v0 y ángulo] --> B[Componentes vx y vy]
    B --> C[Tiempo de vuelo]
    C --> D[Alcance]
    B --> E[Altura máxima]
```

`flowchart LR` indica un diagrama de flujo de izquierda a derecha (*left to right*); `flowchart TD` lo dibujaría de arriba abajo (*top down*). Cada nodo tiene un identificador (`A`, `B`…) y un texto entre corchetes, y `-->` dibuja una flecha.

## Un diagrama como figura

Dentro de una figura, el diagrama recibe pie, número y etiqueta, como cualquier imagen:

````markdown
:::{figure}
:label: diag-calculo

```{mermaid}
flowchart LR
    D[Datos] --> V{¿Ángulo de 45°?}
    V -- Sí --> M[Alcance máximo]
    V -- No --> C[Calcular con la ecuación del alcance]
    C --> R[Resultado]
    M --> R
```

Pasos para calcular el alcance de un lanzamiento.
:::
````

Resultado:

:::{figure}
:label: diag-calculo

```{mermaid}
flowchart LR
    D[Datos] --> V{¿Ángulo de 45°?}
    V -- Sí --> M[Alcance máximo]
    V -- No --> C[Calcular con la ecuación del alcance]
    C --> R[Resultado]
    M --> R
```

Pasos para calcular el alcance de un lanzamiento.
:::

El rombo (`{…}`) indica una decisión, y el texto entre dos guiones (`-- Sí -->`) etiqueta la flecha. Ahora [](#diag-calculo) se puede citar, y aparece en una ventana emergente al pasar el ratón.

## Un diagrama de secuencia

Mermaid tiene otros tipos de diagrama. Uno de secuencia muestra mensajes entre participantes a lo largo del tiempo:

````markdown
:::{figure}
:label: diag-secuencia

```{mermaid}
sequenceDiagram
    participant E as Estudiante
    participant S as Simulación
    E->>S: Elige ángulo y velocidad
    S-->>E: Muestra la trayectoria
    E->>S: Cambia el ángulo
    S-->>E: Compara los alcances
```

Una sesión de trabajo con una simulación.
:::
````

Resultado:

:::{figure}
:label: diag-secuencia

```{mermaid}
sequenceDiagram
    participant E as Estudiante
    participant S as Simulación
    E->>S: Elige ángulo y velocidad
    S-->>E: Muestra la trayectoria
    E->>S: Cambia el ángulo
    S-->>E: Compara los alcances
```

Una sesión de trabajo con una simulación.
:::

## Los diagramas en el PDF

Mermaid dibuja el diagrama **en el navegador**, al abrir la página. Por eso, en un PDF los diagramas Mermaid no aparecen: solo queda su pie. Si el material se va a imprimir, la solución es convertir el diagrama en imagen y usarla como una figura normal.

El editor <https://mermaid.live> descarga el diagrama como PNG o SVG. Esta es la versión en imagen de [](#diag-calculo):

```markdown
:::{figure} img/diag-calculo.png
:label: diag-calculo-img
:alt: Diagrama de flujo para calcular el alcance de un lanzamiento

Pasos para calcular el alcance (versión en imagen, apta para PDF).
:::
```

Resultado:

:::{figure} img/diag-calculo.png
:label: diag-calculo-img
:alt: Diagrama de flujo para calcular el alcance de un lanzamiento

Pasos para calcular el alcance (versión en imagen, apta para PDF).
:::

En la web se ven las dos versiones. Si exportas la edición para imprimir, en el PDF solo aparece esta última.

:::{tip} Para explorar más
- Todos los tipos de diagrama de Mermaid (de clases, de estados, de Gantt, mapas mentales…): <https://mermaid.js.org>.
- El editor en línea <https://mermaid.live> dibuja el diagrama mientras escribes; cuando esté listo, se copia el texto al `.md`.
:::
