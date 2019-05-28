import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print ('\n',traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,'\n type:',type(__x),'\n')

import time
import datetime


start_time = time.time()
time.sleep(2)
elapsed_time = time.time() - start_time
d = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

debug(d)

debug(time.time())
debug(time.gmtime())
debug(time.tzname)
debug(time.timezone)
debug(datetime.datetime.now())

d = time.strftime("%H:%M:%S", time.gmtime(start_time - time.timezone))

debug(d)
