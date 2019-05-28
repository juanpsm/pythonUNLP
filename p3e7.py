'''7. Dado el archivo que detalla la cantidad de mujeres que estudian carreras tecnológicas,
realizar los siguientes ejercicios:
1. Informar la cantidad total de estudiantes mujeres por universidad.
2. Generar una interfaz en PySimpleGUI que muestre las cantidades agrupadas por universidad ordenadas de mayor a menor.
3. Mostrar las cantidades de cada universidad representadas por algún elemento gráficos
de tamaño proporcional a la cantidad mayor.
4. Incorporar la posibildiad de seleccionar el archivo desde la misma interfaz.
5. Agregar la funcionalidad que el botón que permita ordenar esté deshabilitado hasta
que se seleccione el archivo.
Ver Figura 1 en el cual se puede ver un ejemplo de la interfaz solicitada.
Nota: Investigue en el repositorio github del proyecto PysimpleGUI posibles ejemplos para
utilizar gráficos.'''

import random
import csv
import PySimpleGUI as sg
import math

tema = 'Purple'
sg.ChangeLookAndFeel(tema)
CANVAS=(400,400)

def dibujar(todas,x,circulos,nuevo):
	graph.Erase()
	for x in todas:
		
		maximo = max(todas.values())
		try:
			radio = round(50*todas[x]/maximo)
		except ZeroDivisionError:
			radio= 0
		if nuevo:
			circulos[x]["coord"] = (random.randrange(radio,CANVAS[0]-radio),random.randrange(radio,CANVAS[1]-radio))
		graph.DrawPoint(circulos[x]["coord"], radio, color="red")
		#DrawCircle(self, center_location, radius, fill_color=None, line_color='black')
		#DrawCircle(coord, radio, fill_color="PaleGreen1", line_color='black')
		window.Refresh()

ordeno =[]


layout = [
			[sg.Listbox(values=ordeno, size=(50, 15), key='_LIST_', pad=(70,10))],
			[sg.Input(key='_BROWSE_', enable_events=True, visible=False)], 
			[sg.Graph(canvas_size=CANVAS, graph_bottom_left=(0,0), graph_top_right=CANVAS, background_color='black', key='graph')],
			[sg.Button('Dibujar', key='_CREAR_'), sg.FileBrowse('Abrir', target='_BROWSE_', file_types=(("Text Files", "*.txt"),)),
			sg.Button('Convertir', disabled = True, key='_CONV_'), sg.Button('Cerrar')]
		 ]      

window = sg.Window('Mujeres Programadoras GUI').Layout(layout)
window.Finalize()
graph = window.FindElement('graph')


while True:                 # Event Loop  
	event, val = window.Read()  
	#print(event, val)

	archi = open("Todas_las_carreras.csv", "r", encoding='utf-8')
	csvreader = csv.reader(archi)
	next(csvreader) #skips header
	todas = {}
	circulos = {}
	
	for col in csvreader:
		nombre_univeridad = col[2]
		cant_egr_mujeres = (0 if col[19]=='' else int(col[19]))
		if nombre_univeridad in todas:
			if nombre_univeridad !='': #omitimos filas con la columna vacia
				todas[nombre_univeridad] += cant_egr_mujeres
				dibujar(todas,nombre_univeridad,circulos,False)
		else: # si no existe la clave, la creo con su valor
			# ~ print('No existe',col[2],'le pongo',col[19])
			todas[nombre_univeridad] = cant_egr_mujeres
			circulos[nombre_univeridad] = {'coord':(0,0),'id':''}
			dibujar(todas,nombre_univeridad,circulos,True)
	# ~ ordeno = sorted(todas.items())
	# ~ for x in ordeno:
		# ~ print('Facultad: {} -- Egresadas: {}'.format(x[0], x[1]))


	# ~ for x in list(todas).sorted():
		# ~ print (x)

	# ~ archi.seek(0)
	# ~ next(csvreader) #skips header
	# ~ cont = 0
	# ~ for col in csvreader:
		# ~ todas[col[2]] = (0 if col[19]=='' else int(col[19]))
		# ~ if (col[2]=="Universidad Nacional de La Plata"):
			# ~ cont = cont + (0 if col[19]=='' else int(col[19]))
			# ~ print('Año: {} Facultad: {} -- Egresadas: {}'.format(col[0], col[3], ("0" if col[19]=='' else col[19])))
		
	# ~ print('\nTotal egresadas de la UNLP: {}'.format(cont))

	archi.close()

	ordeno = sorted(todas.items(), key = lambda x : x[1])
	maximo = max(todas.values())
	print ('max:',maximo)

	window.FindElement('_LIST_').Update(values=ordeno)
	
	
	
	if event is None or event == 'Cerrar':  
		break
	if event == '_CLEAR_':
		graph.Erase()
	if event == '_SAVE_':
		arch = open('p3e3.json','w')
		for d in window.FindElement('_LIST_').GetListValues() :
			#cadena = d['color']+' '+str(d['coord'][0])+' '+str(d['coord'][1])
			print('Guardo:',d)
		
		# Puedo imprimir en pantalla lo que voy a guardar, con dumps
		# que convierte una estructura tipo diccionario a JSON ydevuelve una cadena
		# ensure_ascii = false para que lea caracteres utf-8 y no solo ascii
		print(json.dumps(datos, sort_keys=False, indent=4, ensure_ascii = False))
		# Con dump escribo la info del diccionario en el archivo, pero antes
		# convirtiendola a JSON
		json.dump(datos, arch)
		arch.close()

window.Close()
