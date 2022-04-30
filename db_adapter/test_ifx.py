import db_adapter_ifx

db = db_adapter_ifx.DbAdapterIFX("DATABASE=ebolenlinea;HOSTNAME=172.18.200.6;PORT=11115; UID=cnx_capa; PWD=Capa.5601$")
#print(db.open_query( procname="proc_isatt_autenticacion", params={"Pusuario":"pru001", "Pclave":"12345"}))
print(db.open_query( select="Select em_cntrto,em_nmbre,em_nit from eb_emprsas Where em_emprsa=?", 
                     params={"em_emprsa":1}
                    ))
#print(db.open_query( procname="proc_isatt_origenes"))

print(f"Error: {db.with_error}  {db.error_message}")
print(f"{db.with_error}")
print(f"{db.sql_text}")
print(db.error_message)
print("Actualizar...")
db.execute_statement( statement="update eb_emprsas Set em_cntrto=1976 Where em_emprsa=?", params={"em_emprsa":1})
print(f"{db.with_error}")
print(db.error_message)
print(db.sql_text)