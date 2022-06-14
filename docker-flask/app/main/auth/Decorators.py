import jwt
from functools import wraps
from flask import Flask, jsonify, make_response, request
import os
import datetime as dt

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None       
       if 'Authorization' in request.headers:
           token = request.headers['Authorization']
           token = token.replace("Bearer","").strip()
 
       if not token:
           return jsonify({'message': 'No se encuentra token en la propiedad Authorization'})
       try:
           data = jwt.decode(token, os.getenv("KEY_JWT"), algorithms=["HS256"],options={ 'verify_nbf': False})
           expExpiry = data.get("exp")
           date_now= round(dt.datetime.now().timestamp() )
           
           if expExpiry<date_now:
               return jsonify({'message': 'El token ha expirado, por favor envie un Token válido.'})
           
       except:
           return jsonify({'message': 'Token enviado no válido, por favor envie un Token válido.'})
 
       return f( *args, **kwargs)
   return decorator