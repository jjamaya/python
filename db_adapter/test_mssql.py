import db_adapter_mssql;

db = db_adapter_mssql.DbAdapterMsSql(server="SRQXSQLS", user="jbs", 
                                     password="Stsks.3123", database="contratistas")


#  select = "exec proc_tmp_agencias %(cod_agen)s"
#print(db.open_query(select = "SELECT cod_agen,nom_agen FROM AFIL_AGENC Where nom_agen=%d" ,params=("BOGOTA")  ))

# Procedimientos 

#Test 1
#print( db.open_query(  procname="proc_tmp_agencias",  params={"cod_agen":1,"cod_empr":1} )  )

#Test 2
#print(db.open_query(  procname="proc_tmp_empresa",  params={"cod_empr":2} )  )

# Ejmplos SQL
#Test 1

print(db.open_query(  select ="select cod_empr,nom_empr from gn_empres Where cod_empr=%(cod_empr)s",  
                      params={"cod_empr":1} )  )
print(db.error_message)

