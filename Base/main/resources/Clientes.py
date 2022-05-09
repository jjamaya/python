from flask_restful import Resource
from flask import jsonify, request

clientes = [
    {
        "id":1,
        "nombre":"Javier",
        "apellido":"Amaya"
    },
    {
        "id":2,
        "nombre":"Antonio",
        "apellido":"Amaya"
    },

    {
        "id":3,
        "nombre":"Resura",
        "apellido":"Buitrago"
    }
]

class Clientes(Resource):
    
    def get(self):
        
        return jsonify(
            {
            "Clientes":clientes
            }
        )

    def post(self):
        cliente = request.get_json()
        clientes.append(cliente)
        return cliente,201

class Cliente(Resource):

    def get(self,id):
        return jsonify(
            {
                "cliente": clientes[int(id)]
            }
        )


