import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print ('\n',traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,'\n type:',type(__x),'\n')

import json
import os

string_json ="""
{"t": "Samara",
"campo2": "loqueñea",
"valor_nulo": null,
"booleano": true
}"""
# valor en formato JSON, HAY QUE USAR COMILLAS DOBLES. 
# notar que a diferencia de Python, se usa null en vez de none y los booleanos son con minuscula
# no me anda con mas de un VALOR
# para transformar esta cadena a un dicc de python uso: 
dicc = json.loads(string_json)
debug(dicc)

# Y tambien puedo hacer lo inverso 

cadena = json.dumps(dicc, ensure_ascii = False) #si tengo caracteres no ascii poner eso de lo contrario apareceran como \u0121
debug(cadena)

#Ahora podemos crear un dicc o editar el que tenemos
dicc['alos'] ='tambores'
dicc['\u0144']='\u0808'
debug(dicc)

# Y con el podemos crear un archivo JSON
existe = os.path.isfile('arch_json.txt')
if existe: #si existe lo abro, y cargo su contenido en una lista
	json_file = open('arch_json.txt', "a", encoding = 'utf-8')
	#json_file.seek(-1,2)
	json_file.write('\n')
else:
	json_file = open ('arch_json.txt', 'w', encoding = 'utf-8')

# lo llenamos con el dicc
json.dump(dicc,json_file, ensure_ascii = False)
#json_file.write(str(dicc)) #esto escribe el diccionario pero no hace la conversión entonces despues no se puede leer con json
json_file.close()

# Y para ver el archivo lo cargamos en otro dicc luego de abrirlo en modo lectura
# ~ json_file = open ('arch_json.txt', 'r', encoding = 'utf-8')
# ~ dicc2 = json.loads(json_file.read().split('\n')[-1])
# ~ debug(dicc2)

# ~ json_file.close()

# Y para ver el archivo lo cargamos en el mismo dicc
