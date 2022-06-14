import logging
from datetime import datetime
import os
import json




def initLog():

    file_log="logs///app-"+datetime.today().strftime('%Y-%m-%d')+".log"

    if os.path.exists("logs") == False:
        os.mkdir("logs")

    try:

        if os.path.isfile(file_log)==False:
            if len(logging.root.handlers)>0:
                for h in logging.root.handlers:
                    logging.root.removeHandler(h)
    except:
        logging.basicConfig(filename=file_log, level=logging.DEBUG, format=f"%(asctime)s %(levelname)s: %(message)s")

    logging.basicConfig(filename=file_log, level=logging.DEBUG, format=f"%(asctime)s %(levelname)s: %(message)s")

def log_info(title,message_log,djson={}):
    initLog()
    logging.info(f"{title}  >> {message_log}" ) if len(message_log)>0 else logging.info(f"{title}  >> " + json.dumps (djson ))

def log_error(title,message_log,djson={}):
    initLog()
    logging.error(f"{title}  >> {message_log}" ) if len(message_log)>0 else logging.info(f"{title}  >> " + json.dumps (djson ))
