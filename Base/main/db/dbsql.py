from main.db import db_adapter_mssql as dbsql
import os

bd = dbsql.DbAdapterMsSql(  server=os.getenv("SERVER"),
                            user=os.getenv("USER"),
                            password=os.getenv("PASWD"),
                            database=os.getenv("DATABASE") )