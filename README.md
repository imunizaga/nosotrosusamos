# Nosotros Usamos

Editar 

* base/templates/index.jade
* base/templates/includes/summary.jade
* base/templates/includes/sidebar.jade
* base static/img/Foto.png

Actualizar
* git pull origin master

Subir al servidor
* git add .
* git commit -m "mensaje"
* git pull origin master
* git push origin master

Para correr el servidor local:
# hay que activar el entorno virtual
source .env/bin/activate
./reset.sh -s
# visitar el servidor en 127.0.0.1:8000

# ctrl-c para cortar el servidor
