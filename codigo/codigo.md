---
title: Bloques de código
short_title: Código
label: codigo
---

El proyecto 1 mostró cómo escribir un bloque de código con colores, título y números de línea. Aquí se ve cómo convertirlo en un recurso citable y cómo mostrar código que está en un fichero aparte. El código no se ejecuta: solo se muestra. Ejecutarlo es el tema del proyecto 4.

## Un bloque con etiqueta

Con `:label:` y `:caption:`, un bloque de código se numera como una figura y se puede citar:

````markdown
```{code-block} python
:label: code-alcance
:caption: Alcance de un proyectil, según la ecuación del alcance.

import math

def alcance(v0, angulo_grados, g=9.81):
    theta = math.radians(angulo_grados)
    return v0**2 * math.sin(2 * theta) / g
```
````

Resultado:

```{code-block} python
:label: code-alcance
:caption: Alcance de un proyectil, según la ecuación del alcance.

import math

def alcance(v0, angulo_grados, g=9.81):
    theta = math.radians(angulo_grados)
    return v0**2 * math.sin(2 * theta) / g
```

El programa [](#code-alcance) traduce a Python la ecuación [](#eq-alcance). Pasa el ratón por las dos citas: el código y la fórmula aparecen sin salir de la página.

## Código de un fichero aparte

Cuando el código ya existe en un fichero, no hace falta copiarlo: la directiva `literalinclude` lo lee del disco. Si el fichero cambia, la página cambia con él.

````markdown
```{literalinclude} trayectoria.py
:label: code-trayectoria
:caption: El fichero `trayectoria.py` completo.
:linenos:
```
````

Resultado:

```{literalinclude} trayectoria.py
:label: code-trayectoria
:caption: El fichero `trayectoria.py` completo.
:linenos:
```

## Solo unas líneas del fichero

Con `:lines:` se muestra solo un fragmento. Con `:lineno-start:` la numeración coincide con la del fichero original:

````markdown
```{literalinclude} trayectoria.py
:lines: 26-29
:lineno-start: 26
:emphasize-lines: 29
```
````

Resultado:

```{literalinclude} trayectoria.py
:lines: 26-29
:lineno-start: 26
:emphasize-lines: 29
```

La línea destacada es la fórmula del alcance, la misma que en [](#code-alcance).

:::{tip} Para explorar más
- Opciones de los bloques de código: <https://mystmd.org/guide/code>.
- `literalinclude` admite también `:start-at:` y `:end-before:`, que seleccionan el fragmento por su contenido y no por el número de línea. Así no hay que cambiar nada si se añaden líneas al principio del fichero.
:::
