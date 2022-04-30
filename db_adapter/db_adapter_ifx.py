from sqlite3 import connect
import ibm_db
from multiprocessing import connection
import db_adapter

class DbAdapterIFX(db_adapter.DbAdapter):
    
    def __init__(self,connection_string):
        self.connection_string = connection_string
        self.error_message = ""
        self.with_error=False
        self.sql_text=""
    
    # Ejecutar un procedimiento que retorna un data set
    def open_query(self,params={},select="",procname=""):
        data_set = []
        self.error_message = ""
        self.with_error=False
        if len(procname)>0:
            self.sql_text =  self.__build_statement(f"execute procedure {procname} (",params)
        else:
            self.sql_text = select

        i = 1
        
        # Conexion BD
        try:

            connection = ibm_db.connect(self.connection_string,"","")

        except:
            self.error_message=ibm_db.conn_errormsg()
            self.with_error = True
            return []

        # Ejecutar procedimiento
        try:
            stmt = ibm_db.prepare(connection, self.sql_text)
            for key,value in params.items():
                ibm_db.bind_param(stmt, i, value)
                i = i +1

            ibm_db.execute(stmt)

            row=ibm_db.fetch_assoc(stmt)
            
            while ( row ):
                #print(row)
                data_set.append( row )  
                row=ibm_db.fetch_assoc(stmt)
                
        except:
            self.error_message=ibm_db.stmt_errormsg()
            self.with_error = True
            return []
        finally:            
            ibm_db.close(connection)
        
        return data_set

    
    def execute_statement(self,params=[],statement="",procname=""):
        self.error_message = ""
        self.with_error=False

        if len(procname)>0:
            self.sql_text =  self.__build_statement(f"execute procedure {procname} (",params)
        else:
            self.sql_text=statement    
        i = 1
        
        # Conexion BD
        try:

            connection = ibm_db.connect(self.connection_string,"","")

        except:
            self.error_message=ibm_db.conn_errormsg()
            self.with_error = True
            return False

        # Ejecutar procedimiento
        try:
            #Asignación de Parametros
            
            stmt = ibm_db.prepare(connection, self.sql_text)
            
            if len(params)>0:
                for key,value in params.items():
                    print("Para despues...")
                    ibm_db.bind_param(stmt, i, value)
                    i = i +1
                
            ibm_db.execute(stmt)
            #ibm_db.exec_immediate(connection, stmt)
        
        except:
            self.error_message=ibm_db.stmt_errormsg()
            self.with_error = True
            return False
        finally:            
            ibm_db.close(connection)
        
        return True


    def __build_statement(self,sql_text,params={}):
        str_params = ""    

        for key,value in params.items():
            str_params = str_params + f"{key}=?,"
        
        if len(str_params)>0:
            str_params = str_params[0:len(str_params) -1]
        
        sql_text = sql_text + f"{str_params})"

        return sql_text

db = DbAdapterIFX("DATABASE=ebolenlinea;HOSTNAME=172.18.200.6;PORT=11115; UID=cnx_capa; PWD=Capa.5601$")
#print(db.open_query( procname="proc_isatt_autenticacion", params={"Pusuario":"pru001", "Pclave":"12345"}))
print(db.open_query( select="Select em_cntrto,em_nmbre,em_nit from eb_emprsas Where em_emprsa=?", params={"em_emprsa":1}))
#print(db.open_query( procname="proc_isatt_origenes"))

print(f"Error: {db.with_error}  {db.error_message}")
print(f"{db.with_error}")
print(f"{db.sql_text}")
print(db.error_message)
print("Actualizar...")
db.execute_statement( statement="update eb_emprsas Set em_cntrto=2022 Where em_emprsa=?", params={"em_emprsa":1})
print(f"{db.with_error}")
print(db.error_message)
print(db.sql_text)



