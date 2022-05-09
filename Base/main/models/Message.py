import datetime as dt
from main.db import db_adapter_mssql as dbsql
import os

class Message(object):
    
    from_message = []
    destinations=[]
    text=""

    status_code = int(0)
    status_name =  str("OK")
    process_message =  str("error")
    record_count =  1
    message_date = ""

    def __repr__(self):
        return self.text

    def to_json(self):
        json_message = {}
        json_destinations={}
        json_destinations["destinations"]=[]

        for destination in self.destinations:
            json_destinations["destinations"].append({"to":destination})

        json_message={"from":self.from_message,  "destinations":json_destinations["destinations"] ,"Text":self.text}

        return json_message

    @staticmethod
    def from_json(message_json):
        from_message = message_json.get("from")
        json_destinations = message_json.get("destinations")
        text=message_json.get("text")
        destinations=[]

        for dest in json_destinations:
            destinations.append( dest.get("to") )

        msg =  Message()
        msg.from_message=from_message
        msg.text=text
        msg.destinations=destinations
        return msg

    def execute_process(self):

        db = dbsql.DbAdapterMsSql(server=os.getenv("SERVER"),
                                  user=os.getenv("USER"),
                                  password=os.getenv("PASWD"),
                                  database=os.getenv("DATABASE") )


        result = db.open_query(procname="proc_agencia", params={"id_agencia":100001})
        dic_agencies = {}
        dic_agencies["agencies"]=result
        self.message_date = dt.datetime.utcnow().isoformat()[:-3]+'Z'
        response_process={}
        response_process={"statusCode": self.status_code,
                          "statusName":self.status_name,
                          "message":self.process_message,
                          "recordCount":self.record_count,
                          "messageDate":self.message_date,
                          "data":dic_agencies
                          }
        return response_process
