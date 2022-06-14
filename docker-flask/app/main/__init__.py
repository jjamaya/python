# Crear nuestra aplicacion Flask

import os
from flask import Flask, render_template
from dotenv import load_dotenv
from main.log import *


# importar el modulo para crear el api rest
from flask_restful import Api

api = Api()  

from main.db import db_adapter_ifx as dbsqlifx
dbifx = dbsqlifx.DbAdapterIFX()

app = Flask(__name__)
initLog()
@app.route('/')
def index():
    return render_template("index.html")

load_dotenv()

dbifx.connection_string= os.getenv("CONNECTION_STRING_IFX")

#Definir Recursos
import main.resources as resources
api.add_resource(resources.GenerateCouponResource,"/generate-coupon")

api.init_app(app)


