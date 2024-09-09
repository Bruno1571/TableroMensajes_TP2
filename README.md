-TITULO-
  TableroMensajes_TP2
  
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

-DESCRIPCION-
  Este proyecto es una aplicación web sencilla de mensajería, donde los usuarios pueden enviar, recibir y eliminar mensajes. El sistema permite filtrar los mensajes por remitente o         
  destinatario, proporcionando una interfaz fácil de usar
  
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

-INSTALACION-

  1 Clona el repositorio:
      git clone https://github.com/usuario/TableroMensajes_TP2.git

  2 Navega al directorio donde pusiste el proyecto:

  3 Crea y activa un entorno virtual:
       python -m venv entorno
       source entorno/bin/activate /// En Windows: entorno\Scripts\activate

  4 Luego de activar el entorno virtual, instala las dependencias del archivo requirements.txt del proyecto
       pip install -r requirements.txt

  5 Aplica las migraciones de la base de datos:
       python manage.py migrate

  6 Ejecuta el servidor:
       python manage.py runserver

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

-USO-

  1 Accede a la aplicación en tu navegador en http://localhost:8000/.

  2 Utiliza las siguientes rutas:
    /crear_mensaje/ para crear un nuevo mensaje.
    /mensajes_recibidos/ para ver los mensajes recibidos.
    /mensajes_enviados/ para ver los mensajes enviados.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

-REQUISITOS-
    Python 3.11
    Django 4.2
    SQLlite (u otra base de datos compatible)


