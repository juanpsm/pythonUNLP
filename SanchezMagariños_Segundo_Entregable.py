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
import random
import json
import csv
import os

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
	try:
		if archivo == '':
			sys.exit(69)
		button = sg.PopupYesNo('Tiene los títulos en la primer fila?')
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
				print('\nData :',data)
		return (data,header_list,tiene_header)
	except PermissionError:
		print('No tiene permiso para leer ese archivo. Elija otro.')

def cargar_tabla_desde_json(archivo,data):
	try:
		data=[] # vuelvo a inicializar porque si llamo dos veces el append agrega al final
		with open(archivo,'r',encoding='utf-8') as infile:
			dicc = json.load(infile)
		header_list = list(dicc[0].keys())
		#hay que editar el diccionario porque necesito una lista de listas y sin las keys
		for elemento in dicc:
			print('Elem',elemento)
			data.append(list(elemento.values()))
		print('header :',header_list)
		print('\nData :',data)
		return (data,header_list)
	except PermissionError:
		print('No tiene permiso para leer ese archivo. Elija otro.')

def convertir_csv_a_json(archivo,filename,tiene_header):
	try:
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
	except PermissionError: #ya lo lei al archivo asi que el problema esta a la salida
		print('\n No tiene permiso para editar ese archivo. Cambiando el nombre a "',filename,'- copia.json"')
		convertir_csv_a_json(archivo,filename+' - copia',tiene_header)

def convertir_json_a_csv(archivo,filename):
	try:
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
	except PermissionError: #ya lo lei al archivo asi que el problema esta a la salida
		print('\n No tiene permiso para editar ese archivo. Cambiando el nombre a: \n"',filename,'- copia.json"')
		convertir_json_a_csv(archivo,filename+' - copia')

def crear_archivos_de_prueba(nombre):
	cadena_en_json='''[
	{
		"nombre":"Juan",
		"edad":18,
		"Carrera":"Lic. en Física",
		"numero de alumno":null,
		"rinde":true
	},
	{
		"nombre":"Luis",
		"edad":22,
		"Carrera":"Biología",
		"numero de alumno":"5559/8",
		"rinde":false
	},
	{
		"nombre":"Pedro",
		"edad":31,
		"Carrera":"Lic. en Sistemas",
		"numero de alumno":"18795/6",
		"rinde":true
	}
]'''
	
	# ~ data = json.loads(cadena_en_json) #si lo quisiera imprimir pero ya lo hago dentro del convertir
	# ~ print('Archivo JSON:\n',json.dumps(data, indent = 4,ensure_ascii=False))
	try:
		archivo = nombre+'.json'
		with open(archivo,'w', encoding = 'utf-8') as json_file:
			json_file.write(cadena_en_json)
		convertir_json_a_csv(archivo,nombre)
	except PermissionError:
		print('No tiene permiso para leer o editar ese archivo. Cambiando el nombre a "',nombre,'- copia.json"')
		crear_archivos_de_prueba(nombre+' - copia')
	
#tema=rand_tema()
tema = 'Kayak'
sg.ChangeLookAndFeel(tema)

#aca voy a guardar los datos
data = []
header_list = []
tiene_header = None
nombre_prueba='test_entrega'

menu = [
		[sg.Input(key='_BROWSE_', enable_events=True, visible=False)], 
		[sg.Button('Crear archivos de prueba', disabled = False, key='_CREAR_')],
		[sg.FileBrowse('Abrir...', target='_BROWSE_', file_types=(("CSV Files, JSON Files", "*.csv;*.json"),))],
		[sg.Button('Convertir', disabled = True, key='_SAVE_')],
		[sg.Button('Cerrar')]
		]

window = sg.Window('Menu').Layout(menu)

while True:                 # Event Loop  
	event, val = window.Read()  
	#print(event, val)
	if event is None or event == 'Cerrar':  
		break
	if event == '_CREAR_':
		print('Creados los archivos: ',nombre_prueba,'.json y ',nombre_prueba,'.csv', sep='')
		crear_archivos_de_prueba(nombre_prueba)
	if event == '_BROWSE_':
		window.Hide()
		archivo = val['_BROWSE_']
		filename, file_extension = os.path.splitext(archivo)
		if (archivo == '' or archivo == None or file_extension not in ('.csv','.json')): #lo de la ext es redundante
			print('debe seleccionar un json o csv')
			# ~ break #lo saco asi no corta la ejecucion
		else:
			try:
				if file_extension == ".csv":
					(data, header_list, tiene_header)= cargar_tabla_desde_csv(archivo,data,tiene_header)
					window.FindElement('_SAVE_').Update(text = "Convertir a JSON")
				elif file_extension == ".json":
					(data, header_list)= cargar_tabla_desde_json(archivo,data)
					window.FindElement('_SAVE_').Update(text = "Convertir a CSV" )

				layout = [[sg.Table(values = data,
									headings=header_list,
									max_col_width=25,
									auto_size_columns=True,
									justification='right',
									alternating_row_color='lightblue',
									num_rows=min(len(data), 20),
									key='_TABLE_')]
									]
				window2 = sg.Window(filename+file_extension.upper()).Layout(layout)
				window2.Read()
				window.FindElement('_SAVE_').Update(disabled = False)
			except TypeError:
				print('Como no tenía permiso para leer, se produjo un error de tipo.')
		window.UnHide()
	if event == '_SAVE_':
		if file_extension == ".csv":
			convertir_csv_a_json(archivo,filename,tiene_header)
		elif file_extension == ".json":
			convertir_json_a_csv(archivo,filename)
window.Close()
