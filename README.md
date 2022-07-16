# python
Proyecto Backend python


Video Instalar en IIS.
  https://www.youtube.com/watch?v=c_FvlKa5Bbw
  en lugar de ejecutar el comando wfastcgi.exe 
  se debe ejecutar: python wfastcgi-enable-script.py
  
Ejemplo Cadena conexion informix:

export CONNECTION_STRING_IFX="DATABASE=ebolenlinea;HOSTNAME=172.18.200.6;PORT=11115; UID=user; PWD=clave; AUTHENTICATION=SERVER"

Determina si el request es un JSON
if request.get_json():
  pass
  

CODIGOS DE RESPUESTA
https://developer.mozilla.org/es/docs/Web/HTTP/Status


PACKAGE PARA GENERAR LOGS:

# import logging
https://machinelearningmastery.com/logging-in-python/

https://pypi.org/

https://betterstack.com/community/guides/logging/how-to-start-logging-with-flask/

# Python Docker

https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04-es


https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask

https://pythonlang.dev/repo/tiangolo-uwsgi-nginx-flask-docker/


# Ambientes virtuales

python -m venv venv

# Flask

### Ejecutar Servidor Flask

1. set FLASK_APP=holamundo.py
2. set FLASK_ENV=development
3. flask run

### Metodos Web (Accion a realizar)

1. Get: Consultar o listar.
2. Post: Crear.
3. Put: Actualizar.
4. Delete: Borar.

### CURL 
curl -X POST http://localhost:5000/post/1
curl -d "llave1=dato1&llave2=dato2"  -X POST http://localhost:5000/lele   --Enviar datos
