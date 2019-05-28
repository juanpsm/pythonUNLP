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
	

def cargar_tabla_desde_csv(archivo,data):
	if archivo == '':
		sys.exit(69)
	button = sg.PopupYesNo('Does this file have column names already?')
	if archivo is not None:
		with open(archivo, "r", encoding='utf-8') as infile:
			reader = csv.reader(infile)
			if button == 'Yes':
				header_list = next(reader)
			try:
				data = list(reader)  # read everything else into a list of rows
				if button == 'No':
					header_list = ['column' + str(x) for x in range(len(data[0]))]
			except:
				sg.PopupError('Error reading file')
				sys.exit(69)
	return (data,header_list)
	
def cargar_tabla_desde_json(archivo,data):
	data = json.load(archivo)
	
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

# ~ data = [['arlen',23],['samara',15]]
# ~ header_list = ['pj','age']
# ~ (data, header_list)= cargar_tabla_desde_csv(archivo,[])
# ~ debug(header_list)
# ~ debug(data)

CANVAS=(400,200)
#https://github.com/PySimpleGUI/PySimpleGUI/issues/850
layout = [
			[sg.Input(key='_BROWSE_', enable_events=True, visible=False)], 
			[sg.FileBrowse('CARGAR', target='_BROWSE_', file_types=(("CSV Files", "*.csv"),("JSON Files", "*.json"))),
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
		debug(archivo)
		debug(filename)
		debug(file_extension)
		if file_extension == ".csv":
			(data, header_list)= cargar_tabla_desde_csv(archivo,data)
			
			# ~ window.FindElement('_TABLE_').Update(values=data)
			# aca la unica forma de actualizar es creando otro layouto midificarlo asi
			del layout[-1:] #todo esto porque no se puede actualizar los headings, tampoco lo puedo meter en un metodo
			layout.append([sg.Table(values = data,
								headings=header_list,
								max_col_width=25,
								auto_size_columns=True,
								num_rows=min(len(data), 20),
								key='_TABLE_')])
			# ~ window.Refresh() ·# no hace nada
			window.Close()
			window = sg.Window('ENTREGABLE GUI').Layout(layout)
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

	if event == '_SAVE_':
		arch_out = open('SanchezMagariños_Segundo_Entregable.json','w')
		# Puedo imprimir en pantalla lo que voy a guardar, con dumps
		# que convierte una estructura tipo diccionario a JSON ydevuelve una cadena
		# ensure_ascii = false para que lea caracteres utf-8 y no solo ascii
		print(json.dumps(data, sort_keys=False, indent=4, ensure_ascii = False))
		# Con dump escribo la info del diccionario en el archivo, pero antes
		# convirtiendola a JSON
		json.dump(data, arch_out)
		arch_out.close()
window.Close()
