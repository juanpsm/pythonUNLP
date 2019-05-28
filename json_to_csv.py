import csv, json, sys, os
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x),'\n')
	
archivo = "json_to_csv.json"
filename, file_extension = os.path.splitext(archivo)

jsonRuta = archivo
csvRuta = filename+'.csv'
data = {}

with open(jsonRuta,'r', encoding="utf-8") as arch_json:
	data = json.load(arch_json)

print('Contenido JSON:\n',json.dumps(data,indent=4,ensure_ascii=False))

print('\n Diccionario cargado:\n',data)

print('Guardo en',csvRuta)
with open(csvRuta,'w',encoding="utf-8") as arch_csv:
	csvWriter = csv.writer(arch_csv,lineterminator='\n')

	csvWriter.writerow(data[0].keys())  # header row agarro el primer elemento y le veo las claves
	print('Titulos =',list(data[0].keys()))
	for row in data:
		csvWriter.writerow(row.values())
		print('Fila =',list(row.values()))
