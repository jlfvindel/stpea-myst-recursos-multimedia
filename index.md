---
title: 'Proyecto 2: recursos multimedia'
short_title: Inicio
label: inicio
---

Este proyecto muestra cómo incorporar a un material docente todo lo que no es texto corrido: imágenes y figuras, vídeos, ecuaciones, código, diagramas y páginas web incrustadas. Para que los ejemplos tengan sentido juntos, todos tratan del mismo tema: el **tiro parabólico**, el movimiento de un objeto lanzado con cierta velocidad y cierto ángulo.

:::{note} Sobre la elaboración de este material
:class: dropdown
Este proyecto lo ha preparado José Luis Fernández Vindel en colaboración con un asistente de inteligencia artificial (Claude, de Anthropic). La estructura, los textos, los ejemplos y las imágenes se han elaborado en diálogo con el asistente; el autor ha decidido el enfoque, ha revisado el resultado y responde de su contenido. Los ejemplos se han comprobado con MyST 1.13.0.
:::

Puedes {download}`descargar la fuente completa del proyecto <descargas/recursos-multimedia.zip>` para ejecutarlo y modificarlo en tu ordenador. También está en el botón de descarga, arriba a la derecha de cada página.

## Dos tipos de recursos

Recursos ya terminados
: Ficheros que se preparan con otro programa y MyST solo coloca en la página: una fotografía, una gráfica, un vídeo, una página web de otro sitio.

Recursos que compila MyST
: Se escriben como texto dentro del propio `.md` y MyST los convierte en algo visual al construir el sitio: una ecuación escrita en LaTeX, un bloque de código coloreado, un diagrama descrito en Mermaid.

## Las vistas emergentes

Todos estos recursos se pueden **etiquetar** y luego **citar** desde cualquier página. En la web, al pasar el ratón por encima de una cita, aparece una ventana emergente con el recurso citado: la ecuación, la figura o el diagrama se ven en el contexto de lo que se está leyendo, sin cambiar de página.

Cada página usa algunas de estas citas. La última, «Vistas emergentes: un recorrido», las reúne en una explicación completa del tiro parabólico: es la mejor forma de apreciar la experiencia de lectura que permiten.

## Dos configuraciones

| Fichero | Se usa con | Qué produce |
|---|---|---|
| `myst.yml` | `myst start` | La edición web completa: todas las páginas, agrupadas en el menú |
| `myst-alt1.yml` | `myst --config myst-alt1.yml start` | Una edición para imprimir: sin vídeos, sin iframes y sin el recorrido con vistas emergentes, que solo tienen sentido en pantalla; además declara las exportaciones a PDF |

Para obtener el PDF de la edición para imprimir:

```bash
myst --config myst-alt1.yml build --typst    # PDF con Typst
myst --config myst-alt1.yml build --pdf      # PDF con LaTeX (y con Typst)
```

El proyecto 1 explica cómo instalar MyST, arrancar el sitio y exportarlo.

:::{note} Los cuatro proyectos
1. Usar MyST y maquetar.
2. **Recursos multimedia** (este).
3. Reestructurar, reutilizar y enlazar.
4. Documentos ejecutables con cuadernos Jupyter.
:::
