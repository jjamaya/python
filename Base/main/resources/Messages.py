from flask_restful import Resource
from flask import request, jsonify
from main.models import MessageModel

class Messages(Resource):
    
    def post(self):
        json_message = {}
        json_message["messages"] = []
        list_messages = request.get_json().get("messages")
        for json_msg in list_messages:
            msg = MessageModel.from_json( json_msg )
            json_message["messages"].append(  msg.to_json() )
        
        return msg.execute_process()