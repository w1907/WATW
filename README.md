# Proyecto Desarrollo Web

## Integrantes

- Allison Ossa
- Francisco Diaz
- Byron Oyarzún

# Instalación

 1. Crear un entorno virtual.

    virtualenv -p python3 <nombre>

 2. Crear carpeta dentro del entorno virtual creado.

    mkdir src

 3. Clonar el repositorio dentro de la carpeta src.
 
    git clone https://github.com/w1907/WATW.git .
    
 4. Activar entorno virtal.

    source bin/activa

 5. Instalar los paquetes necesarios para desplegar la app.

    pip -r install requirements.txt

 6. Crear la base de datos.

    python manage.py migrate

 7. Crear un super usuario.

    python manage.py createsuperuser

 8. Iniciar servidor.

    python manage.py runserver

# Descripción

El proyecto tiene como nombre We are the world. Un espacio virtual para hablar de problemas críticos en el mundo, como por ejemplo, pobreza, guerra, racismo, etc. Cada uno de estos temas tiene un apartado de Noticias, que las agrega un moderador, Acerca de, que es una descripción detallada y la agrega el administrador al momento de crear el tema, Propuestas, este es el apartado más importante ya que forma parte del objetivo principal del proyecto, que es que los usuarios puedan dar sus ideas para solucionar un problema crítico, y lo último, una galería de fotos utilizando la API de instagram para mostrar fotos con hashtags relacionados.

Debido a que es muy difícil encontrar una solución a este tipo de problemas, este proyecto busca la participación de todo el mundo. Las propuestas más comentadas o con más likes, pasarán a una posición destacada dentro de la aplicación web con el fin de que otros usuarios se enteren y sigan comentando.