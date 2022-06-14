#MODELS

from .. import dbifx
from .ApiMessagesModelOut import ApiMessagesModelOut


class GenerateCoupon(object):

    id_client = 0
    name =""
    surname =""
    phone = ""
    email = ""
    enroll_plan_loyalty  = "N"
    coupon_code = ""
    discount_rate=0.0,
    start_date=""
    finish_date=""
    contest_message=""
    terms_conditions=""

    def __repr__(self):
        return f'Coupon code: {self.coupon_code}'
    
    def to_json(self):
        coupon_json = { "code" : self.coupon_code, 
                        "discount_rate" : self.discount_rate,
                        "id_cliente" : self.id_client,
                        "name" : self.name,
                        "surname" : self.surname,
                        "phone" : self.phone,
                        "start_date" : self.start_date,
                        "finish_date" : self.finish_date,
                        "contest_message" : self.contest_message,
                        "terms_conditions" : self.terms_conditions
        }
        return coupon_json

    @staticmethod
    def from_json(json_client):
        id_client = json_client.get("id_client")
        name = json_client.get("name")
        surname = json_client.get("surname")
        phone = json_client.get("phone")
        email = json_client.get("email")
        enroll_plan_loyalty = json_client.get("enroll_plan_loyalty")

        coupon = GenerateCoupon()
        coupon.id_client = id_client
        coupon.name = name
        coupon.surname = surname
        coupon.phone = phone
        coupon.email = email
        coupon.enroll_plan_loyalty = enroll_plan_loyalty
        coupon.coupon_code = ""
        coupon.discount_rate=0.0

        return coupon

    def generate_coupon(self):
        
        status_process = 0
        message_process = 0
        api_messages = ApiMessagesModelOut()  
        error_db = False

        try:
            coupon_list = dbifx.open_query(procname="proc_sv_generar_cupon",params={"Pid_cliente":self.id_client,"Pnombres":self.name, "Papellidos":self.surname,"Ptelefono":self.phone,
                                                                                    "Pemail":self.email,"Pinscripcion_plan_viajero":self.enroll_plan_loyalty

            }  )
            error_db = dbifx.with_error
        except Exception as error:
            error_db = True

        coupons=[]

        if error_db == False:
            for coupon in coupon_list:
                self.coupon_code = coupon.get("cupon")
                self.discount_rate=coupon.get("descuento")
                self.start_date=coupon.get("fecha_inicio")
                self.finish_date=coupon.get("fecha_fin")
                self.contest_message = coupon.get("mensaje_ganador")
                self.terms_conditions = coupon.get("terminos_concurso")
                coupons.append( self.to_json() )
                status_process = coupon.get("estado")
                message_process = coupon.get("mensaje")
        else:
                status_process = -1
                message_process = dbifx.error_message
        
        api_messages.status_code= status_process
        api_messages.process_message=message_process
        api_messages.data = coupons
        
        return api_messages.to_json(),status_process


