---
title: Matemáticas y ecuaciones
short_title: Ecuaciones
label: ecuaciones
---

Las expresiones matemáticas se escriben en **LaTeX**, el lenguaje habitual para fórmulas, y MyST las compone al construir el sitio. No hace falta tener LaTeX instalado para la web: solo para exportar a PDF por esa vía.

## Matemáticas dentro del texto

Entre dos signos `$`, la expresión queda integrada en la línea:

```markdown
Un proyectil lanzado con velocidad $v_0$ y ángulo $\theta$ tiene una componente horizontal $v_x = v_0 \cos\theta$.
```

Resultado:

Un proyectil lanzado con velocidad $v_0$ y ángulo $\theta$ tiene una componente horizontal $v_x = v_0 \cos\theta$.

## Ecuaciones destacadas

Entre dos `$$`, la ecuación ocupa su propia línea. Si después del cierre se escribe una etiqueta entre paréntesis, la ecuación se **numera** y se puede citar:

```markdown
$$
x(t) = v_0 \cos\theta \; t
$$ (eq-x)

$$
y(t) = v_0 \sin\theta \; t - \frac{1}{2} g t^2
$$ (eq-y)
```

Resultado:

$$
x(t) = v_0 \cos\theta \; t
$$ (eq-x)

$$
y(t) = v_0 \sin\theta \; t - \frac{1}{2} g t^2
$$ (eq-y)

Las ecuaciones [](#eq-x) y [](#eq-y) describen la posición en cada instante. Pasa el ratón por encima de las citas: la ecuación aparece en una ventana emergente.

## La directiva `math`

La directiva `math` hace lo mismo, con la etiqueta como opción. Es más cómoda para ecuaciones largas:

```markdown
:::{math}
:label: eq-alcance
R = \frac{v_0^2 \sin 2\theta}{g}
:::
```

Resultado:

:::{math}
:label: eq-alcance
R = \frac{v_0^2 \sin 2\theta}{g}
:::

El alcance [](#eq-alcance) es máximo cuando $\sin 2\theta = 1$, es decir, con $\theta = 45^\circ$. Es lo que muestra [](#fig-trayectorias).

## Varias líneas alineadas

El entorno `aligned` alinea varias ecuaciones por el carácter `&`, y `\\` separa las líneas:

```markdown
:::{math}
:label: eq-velocidad
\begin{aligned}
v_x(t) &= v_0 \cos\theta \\
v_y(t) &= v_0 \sin\theta - g t
\end{aligned}
:::
```

Resultado:

:::{math}
:label: eq-velocidad
\begin{aligned}
v_x(t) &= v_0 \cos\theta \\
v_y(t) &= v_0 \sin\theta - g t
\end{aligned}
:::

La componente horizontal de [](#eq-velocidad) no cambia; la vertical disminuye hasta anularse en el punto más alto.

## Abreviaturas propias (macros)

Si una expresión se repite mucho, se puede definir una abreviatura para todo el proyecto en `myst.yml`:

```yaml
project:
  math:
    '\vo': 'v_{0}'
    '\dd': '\,\mathrm{d}'
```

A partir de ahí, `\vo` equivale a `v_{0}` en cualquier ecuación:

```markdown
:::{math}
:label: eq-altura
h_{\max} = \frac{\vo^2 \sin^2\theta}{2g}
:::
```

Resultado:

:::{math}
:label: eq-altura
h_{\max} = \frac{\vo^2 \sin^2\theta}{2g}
:::

[](#eq-altura) da la altura máxima. La macro `\dd` sirve para escribir diferenciales, como en $\int_0^t v_x \dd s$.

:::{note} Las fórmulas necesitan conexión
La web carga desde internet la hoja de estilo de KaTeX, la biblioteca que compone las fórmulas. Sin conexión, las fórmulas aparecen descolocadas o repetidas. Tenlo en cuenta si el material se va a consultar en un aula sin acceso a internet.
:::

:::{tip} Para explorar más
- Matemáticas en MyST: <https://mystmd.org/guide/math>.
- La web compone las fórmulas con KaTeX; su lista de símbolos y entornos admitidos sirve de chuleta: <https://katex.org/docs/supported.html>.
:::
