# Crear nuestra aplicacion Flask

import os
from flask import Flask
from dotenv import load_dotenv
import main.resources as resources


# importar el modulo para crear el api rest
from flask_restful import Api

api = Api()

def create_app():

    app = Flask(__name__)

    load_dotenv()
    
    #Definir Recursos
    api.add_resource(resources.ClientesResource, "/clientes")
    api.add_resource(resources.ClienteResource,"/cliente/<id>")
    api.add_resource(resources.MessagesResource,"/messages")

    
    api.init_app(app)

    return app

