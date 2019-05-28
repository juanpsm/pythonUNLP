'''Implementar un script que (en una ventana) permita abrir un archivo ".json" o ".csv" y muestre su contenido en una tabla (elemento Table de pysimplegui).
Añada un botón que permita convertir el archivo al otro formato, es decir que si el archivo abierto es ".csv", lo deberá convertir a ".json" y viceversa.
Por ejemplo, si se elige un archivo "jugadores.json", deberá generar "jugadores.csv" (respetando el formato).
Capture las posibles excepciones que pueden surgir en caso que el archivo seleccionado no exista o no tenga los permisos necesarios.


Aclaración: el formato CSV en la primera línea siempre deberá contener los nombres de las columnas.

El ejercicio puede ser realizado en grupo pero se debe subir en forma individual.
Se debe subir un sólo archivo  de nombre Apellido_Segundo_Entregable.py
'''
import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
import math
import random
import json
import csv
import os
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
	
def rand_tema():
	raw_temas=  '''GreenTan      
LightGreen      
BluePurple      
Purple      
BlueMono      
GreenMono      
BrownBlue      
BrightColors      
NeutralBlue      
Kayak      
SandyBeach      
TealMono'''
	temas = raw_temas.replace(' ','').split('\n')
	return random.choice(temas)
	

def cargar_tabla_desde_csv(archivo,data,tiene_header):
	if archivo == '':
		sys.exit(69)
	button = sg.PopupYesNo('Does this file have column names already?')
	if archivo is not None:
		with open(archivo, "r", encoding='utf-8') as infile:
			reader = csv.reader(infile)
			if button == 'Yes':
				header_list = next(reader)
				tiene_header = True
			try:
				data = list(reader)  # read everything else into a list of rows
				if button == 'No':
					header_list = ['columna' + str(x) for x in range(len(data[0]))]
					tiene_header = False
			except:
				sg.PopupError('Error reading file')
				sys.exit(69)
			print('header :',header_list)
			print('\n Data :',data)
	return (data,header_list,tiene_header)
	
def cargar_tabla_desde_json(archivo,data):
	with open(archivo,'r',encoding='utf-8') as infile:
		dicc = json.load(infile)
	header_list = list(dicc[0].keys())
	#hay que editar el diccionario porque necesito una lista de listas y sin las keys
	for elemento in dicc:
		print('Elem',elemento)
		data.append(list(elemento.values()))
	print('header :',header_list)
	print('\n Data :',data)
	return (data,header_list)

def convertir_csv_a_json(archivo,filename,tiene_header):
	csvRuta = archivo
	jsonRuta = filename+'.json'
	print('Convertir',csvRuta,'a',jsonRuta)
	data = [] #si tengo varios objetos se meten en una lista
	with open(csvRuta,'r', newline='', encoding="utf-8") as arch_csv:
		if tiene_header:
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

def convertir_json_a_csv(archivo,filename):
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

		csvWriter.writerow(data[0].keys())  # header, agarro el primer elemento y le veo las claves
		print('Titulos =',list(data[0].keys()))
		for row in data:
			csvWriter.writerow(row.values()) #cada fila son solo los valores sin las claves
			print('Fila =',list(row.values()))

#tema=rand_tema()
tema = 'Kayak'
sg.ChangeLookAndFeel(tema)

# ~ archivo = "SanchezMagariños_Segundo_Entregable.csv" 
# ~ filename, file_extension = os.path.splitext(archivo)
# ~ debug(archivo)
# ~ debug(filename)
# ~ debug(file_extension)

#aca voy a guardar los datos
data = []
header_list = []
tiene_header = None
# ~ data = [['arlen',23],['samara',15]]
# ~ header_list = ['pj','age']
# ~ (data, header_list)= cargar_tabla_desde_csv(archivo,[])
# ~ debug(header_list)
# ~ debug(data)

layout = [
			[sg.Input(key='_BROWSE_', enable_events=True, visible=False)], 
			[sg.FileBrowse('Abrir...', target='_BROWSE_', file_types=(("CSV Files, JSON Files", "*.csv;*.json"),)),
			sg.Button('Convertir', disabled = False, key='_SAVE_'), sg.Button('Cerrar')],
			[sg.Table(values = data,
							headings=header_list,
							max_col_width=25,
							auto_size_columns=True,
							justification='right',
							alternating_row_color='lightblue',
							num_rows=min(len(data), 20),
							#visible = False,
							key='_TABLE_')]
		 ]

window = sg.Window('ENTREGABLE GUI').Layout(layout)


while True:                 # Event Loop  
	event, val = window.Read()  
	#print(event, val)
	if event is None or event == 'Cerrar':  
		break
	if event == '_BROWSE_':
		archivo = val['_BROWSE_']
		filename, file_extension = os.path.splitext(archivo)
		if (archivo == '' or archivo == None or file_extension not in ('.csv','.json')):
			print('debe seleccionar un json o csv')
			break
		if file_extension == ".csv":
			(data, header_list, tiene_header)= cargar_tabla_desde_csv(archivo,data,tiene_header)
		elif file_extension == ".json":
			(data, header_list)= cargar_tabla_desde_json(archivo,data)
		del layout[-1:]
		layout.append([sg.Table(values = data,
							headings=header_list,
							max_col_width=25,
							auto_size_columns=True,
							num_rows=min(len(data), 20),
							key='_TABLE_')])
		window.Close()
		window = sg.Window('ENTREGABLE GUI').Layout(layout)
	# ~ window.FindElement('_SAVE_').Update(disabled = False)
	if event == '_SAVE_':
		if file_extension == ".csv":
			convertir_csv_a_json(archivo,filename,tiene_header)
		elif file_extension == ".json":
			convertir_json_a_csv(archivo,filename)
window.Close()
