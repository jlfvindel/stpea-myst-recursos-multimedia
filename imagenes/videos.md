---
title: Vídeos
short_title: Vídeos
label: videos
---

Hay dos formas de incluir un vídeo: subir el fichero junto al proyecto o incrustar uno que ya esté publicado en una plataforma como YouTube.

## Un vídeo propio

Un fichero de vídeo se incluye igual que una imagen, con la directiva `figure`. MyST reconoce la extensión (`.mp4`, `.webm`…) y muestra un reproductor.

```markdown
:::{figure} video/trayectoria.mp4
:label: vid-trayectoria
:width: 80%

Animación de un proyectil lanzado a 20 m/s con un ángulo de 45°.
:::
```

Resultado:

:::{figure} video/trayectoria.mp4
:label: vid-trayectoria
:width: 80%

Animación de un proyectil lanzado a 20 m/s con un ángulo de 45°.
:::

Como cualquier figura, tiene número y etiqueta: [](#vid-trayectoria) se puede citar desde otras páginas.

:::{warning} El tamaño importa
El vídeo viaja con el proyecto: ocupa espacio en el servidor y en el zip de descarga. Este dura cuatro segundos y pesa unos 20 KB. Para vídeos largos, es mejor publicarlos en una plataforma e incrustarlos, como en el apartado siguiente. Para que se reproduzca en cualquier navegador, el formato más seguro es MP4 con vídeo H.264.
:::

## Un vídeo publicado en YouTube

Un vídeo de YouTube se incrusta con la directiva `iframe`, que muestra dentro de la página otra página web: en este caso, el reproductor de YouTube. La dirección no es la que aparece en el navegador, sino la de **inserción**: `https://www.youtube.com/embed/` seguida del identificador del vídeo. YouTube la da en *Compartir › Insertar*.

```markdown
:::{iframe} https://www.youtube.com/embed/MdOS6tPq8fc
:label: vid-jupyter-book
:width: 100%

Cómo construir un Jupyter Book (en inglés). Jupyter Book 2 funciona con MyST.
:::
```

Resultado:

:::{iframe} https://www.youtube.com/embed/MdOS6tPq8fc
:label: vid-jupyter-book
:width: 100%

Cómo construir un Jupyter Book (en inglés). Jupyter Book 2 funciona con MyST.
:::

También el vídeo incrustado tiene número y etiqueta: [](#vid-jupyter-book).

:::{note} Un vídeo incrustado depende de la plataforma
Se ve mientras siga publicado y su autor permita insertarlo. Además, el reproductor de YouTube puede guardar datos del visitante. Si eso importa en tu institución, YouTube ofrece un modo de privacidad mejorada cambiando `youtube.com` por `youtube-nocookie.com` en la dirección de inserción.
:::

:::{tip} Para explorar más
- La directiva `iframe` sirve para cualquier página web que permita ser incrustada, no solo para vídeos: lo muestra la página de [iframes](#iframes).
- Prueba a añadir `?start=60` al final de la dirección de inserción: el vídeo empezará en el segundo 60.
:::
