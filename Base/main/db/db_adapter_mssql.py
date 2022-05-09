from multiprocessing import connection
from main.db import db_adapter_mssql ,db_adapter
import pymssql
from pymssql import _mssql

class DbAdapterMsSql(db_adapter.DbAdapter):
    
    __server = ""
    __user = ""
    __password = ""
    __database = ""

    def __init__(self,server,user,password,database):
        self.__server = server
        self.__user = user
        self.__password = password
        self.__database = database
        self.error_message = ""
        self.with_error=False
        self.sql_text=""

    def open_query(self,params={},select="",procname=""):
        
        data_set=[]
        self.error_message = ""
        self.with_error=False
        if len(procname)>0:
            
            self.sql_text = self.__build_statement(f"exec {procname} ",params)
            
        else:
            self.sql_text=select

        try:
            connection = pymssql.connect(server=self.__server, user=self.__user,password=self.__password, database=self.__database, autocommit=True)
        except pymssql.Error as e:
            self.error_message = e
            self.with_error=False
            return []


        try:
            cursor = connection.cursor()
            cursor.execute(self.sql_text,params)
            connection.commit()
            columns = [column[0] for column in cursor.description]
            data_set = []
            for row in cursor.fetchall():
                data_set.append(dict(zip(columns, row)))

        except pymssql.Error as e:
            self.error_message = e
            self.with_error=False
            return []
            
        finally:
            connection.close()
            
        return data_set

    def execute_statement(self,params=[],statement="",procname=""):        
        self.error_message = ""
        self.with_error=False
        if len(procname)>0:
            
            self.sql_text = self.__build_statement(f"exec {procname} ",params)
            
        else:
            self.sql_text=statement

        try:
            connection = pymssql.connect(server=self.__server, user=self.__user,password=self.__password, database=self.__database, autocommit=True)
        except pymssql.Error as e:
            self.error_message = e
            self.with_error=False
            return False

        try:
            cursor = connection.cursor()
            cursor.execute(self.sql_text,params)
            connection.commit()
        except pymssql.Error as e:
            #connection.rollback()
            self.error_message = e
            self.with_error=False
            return False
            
        finally:
            connection.close()
            
        return True

    def __build_statement(self,sql_text,params={}):
        str_params = ""    

        for key,value in params.items():
            str_params = str_params +  f" %({key})d," 
        
        if len(str_params)>0:
            str_params = str_params[0:len(str_params) -1]
        
        sql_text = sql_text + str_params

        return sql_text
        