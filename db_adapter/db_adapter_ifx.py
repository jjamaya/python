from multiprocessing import connection
import db_adapter

class DbAdapterIFX(db_adapter.DbAdapter):

    def __init__(self,connection_string):
        self.connection_string = connection_string

    def open_procedure(self,procname,params=[]):
        data_set = []
        return data_set

    def execute_procedure(self,procname,params=[]):
        print("Ejecutar proc")

db = DbAdapterIFX("database_name");
db.open_procedure( "proc_tmp" );
print(db.connection_string)


