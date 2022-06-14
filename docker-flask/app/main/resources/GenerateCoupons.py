#RESOURCES:


from flask_restful import Resource
from flask import request
from main.models import GenerateCouponModel
from main.auth.Decorators import token_required
from main.schemas import GenerateCoupons
from flask_expects_json import expects_json
from main.log import log_info,log_error

class GenerateCoupon(Resource):

    @token_required
    @expects_json(GenerateCoupons.schema)
    def post(self):
        log_info("1. Request","",request.get_json())
        coupon = GenerateCouponModel.from_json(request.get_json())
        data,status_process =  coupon.generate_coupon()

        if status_process>=0:
            log_info("2. Response("+str(200) +")" ,"",data)
            return data,200
        else:
            log_error("2. Response("+str(409) +")" ,"",data)
            return data,409


        

