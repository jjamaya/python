# Archivo principal del proyecto

from main import create_app
import os

app = create_app()

# Permite acceder a las propiedades de la aplicacion en cualquier parte del sistema
app.app_context().push()

if __name__ =='__main__':
    app.run(port=os.getenv("PORT"),debug=True) #Reinicia el server cada vez que exista un nuevo cambio


