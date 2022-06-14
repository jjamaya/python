import datetime as dt


class ApiMessagesModelOut:
    
    status_code = 0
    __status_name__ = ""
    process_message = ""
    data=[{}]
    __record_count__= 0
    __message_date__="" 

    def to_json(self):

        self.__record_count__= 0

        if len(self.data) > 0:
            self.__record_count__= len(self.data)

        if self.status_code<=0:
            self.__status_name__="ERROR"
        else:
            self.__status_name__="OK"

        __message_date__ = dt.datetime.utcnow().isoformat()[:-3]+'Z'

        json_message={ 
                    "statusCode" : self.status_code,
                    "statusName" : self.__status_name__,
                    "message" :  self.process_message,
                    "data" : self.data,
                    "recordCount": self.__record_count__,
                    "messageDate": __message_date__
        }

        return json_message

        