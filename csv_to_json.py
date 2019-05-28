import json
import csv
import os
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x),'\n')
	
archivo = "csv_to_json.csv"
filename, file_extension = os.path.splitext(archivo)

csvRuta = archivo
jsonRuta = filename+'.json'
data = [] #si tengo varios objetos se meten en una lista
with open(csvRuta,'r', newline='', encoding="utf-8") as arch_csv:
	if input('Tiene encabezado en la pirmer fila? > ').lower() in ('y','s','yes','si'):
		csvReader = csv.DictReader(arch_csv) #si omito el parametro fieldnames carga la primer fila como el mismo
	else:
		cantidad_de_campos = len(arch_csv.readline().split(',')) #leo la primer linea y cuento los campos
		header_list = ['columna' + str(x) for x in range(cantidad_de_campos)] #armo los titulos
		csvReader = csv.DictReader(arch_csv, fieldnames = header_list)

	print('\n CSV :')
	for fila in csvReader:
		print('fila : ',fila)
		data.append(fila)

print('dumps =',json.dumps(data, indent = 4,ensure_ascii=False))
with open(jsonRuta,'w', encoding="utf-8") as arch_json:
	cadena_json = json.dumps(data, indent = 4,ensure_ascii=False)
	arch_json.write(cadena_json)
