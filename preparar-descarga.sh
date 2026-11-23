#!/bin/sh
# -------------------------------------------------------------
#  preparar-descarga.sh · Genera descargas/recursos-multimedia.zip
#
#  El zip contiene la fuente del proyecto tal como está en git
#  (último commit): sin _build/, exports/ ni el propio zip.
#  Ejecútalo antes de construir el sitio para publicarlo:
#      ./preparar-descarga.sh
#      BASE_URL=/ruta/del/sitio myst build --html
# -------------------------------------------------------------
set -e
mkdir -p descargas
git archive --format=zip --prefix=recursos-multimedia/ -o descargas/recursos-multimedia.zip HEAD
echo "Creado descargas/recursos-multimedia.zip"
