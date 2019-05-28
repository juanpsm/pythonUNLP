import sys
try:
	import hangman
	import reversegam
	import tictactoeModificado
except:
	print("Ups! Ocurrió",sys.exc_info()[0],".")
	print("Asegurece de que los paquetes hangman, reversegam y tictactoeModificado  se encuentren en la misma carpeta que este archivo")
	print()
import hangman
import reversegam
import tictactoeModificado

import PySimpleGUI as sg
import json
import time
import datetime
import os

# Nombre del archivo
FNAME = 'log.txt'

def no_existe_arch():
	# el atributo disable del metodo .Update() no acepta que le asigne directamente una variable
	# por eso creo esta funcion para saber cuando no existe el archivo.
	# ademas me sirve para otros metodos.
	return not (os.path.isfile(FNAME))
	
def guardar_info(datos):
	if no_existe_arch():
		f = open(FNAME, "w")  # si no existe lo creo
		f.write('[') #corchete de inicio de la lista
	else: #si existe borro el corchete final
		f = open(FNAME, 'rb+') # abrir en modo lectoescritura binaria
		f.seek(-1, 2) # retrocedo un byte desde end of file
		f.truncate() # trunco el archivo en la posicion actual
		f.close()
		f = open(FNAME, "a") # abro en modo apendice para agregar los daros nuevo
		f.write(',')   # separador
	# Guardo la info en el archivo
	print('\n GUARDANDO SESION . . . \n')
	
	# Puedo imprimir en pantalla lo que voy a guardar, con dumps
	# que convierte una estructura tipo diccionario a JSON ydevuelve una cadena
	# ensure_ascii = false para que lea caracteres utf-8 y no solo ascii
	print(json.dumps(datos, sort_keys=False, indent=4, ensure_ascii = False))
	
	# Con dump escribo la info del diccionario en el archivo, pero antes
	# convirtiendola a JSON
	json.dump(datos, f)
	
	#f.write(str(datos)) # esto escribe tambien el diccionario pero no convierte a JSON
	f.write(']')   #corchete de final de la lista
	f.close()
	
def contar_info():
	if no_existe_arch():
		return 0
	f = open(FNAME, "r")
	c = len(json.load(f)) #cuento la cantidad de items de la lista a la que le cargo los datos del archivo
	f.close()
	return c
	
def mostrar_info():
	if no_existe_arch():
		print('No hay registros disponibles')
	else:
		# puedo abrir el archivo y leer los datos:
		f = open(FNAME, "r")
		
		#con load cargo una lista, que convierte los datos JSON del archivo a codigo de python
		lista = json.load(f)
		
		#print(lista,'\n') #asi imprimo toda la lista como un chorizo
		
		# mejor puedo usar de nuevo el paquete json para imprimir los datos en pantalla, ya que 
		# tiene attributos para que se vea mas lindo u ordenar las claves
		# entonces le paso la estructura que acabo de cargar, y dumps me devuelve una cadena que imprimo
		print(json.dumps(lista, sort_keys=False, indent=4, ensure_ascii = False))
		f.close()
	
def borrar_info():
	os.remove(FNAME) #borro el archivo directamente
	print('\n Chau datos! \n')
	
def refrescar(window, jugando):
	#Este metodo lo uso porque no encontré un metodo del PySimpleGUI que me refresque la ventana entera
	# window.Refresh() no me funciono del todo.
	# también podria usar window.Disable() pero de esa forma deshabilito toda la ventana 
	# y quiero que en algunos casos como el de borrar me queden activos algunos botones
	# lo mismo pasa con window.Hide(), window.UnHide())
	# deshabilito los botones cuando este en un juego y el de borrar cuando no exista el archivo
	# tambien actualizo una funcion que muestra la cantidad de entradas en el el archivo
	def j():
		return jugando
	window.FindElement('_HANG_').Update(disabled = j())
	window.FindElement('_TA_').Update(disabled = j())
	window.FindElement('_OT_').Update(disabled = j())
	window.FindElement('_HS_').Update(disabled = j())
	window.FindElement('_HStxt_').Update('( '+str(contar_info())+' )')
	window.FindElement('_DELETE_').Update(disabled = (no_existe_arch() or j()))
	window.FindElement('_EXIT_').Update(disabled = j())
	
def lanzar_juego(event):
	#lanzo el juego correspondiente a cada evento
	if event == '_HANG_':
		#print(event)
		hangman.main()
	elif event == '_TA_':
		#print(event)
		tictactoeModificado.main()
	elif event == '_OT_':
		#print(event)
		reversegam.main()
	
def main(args):
	# Seteo el tema de colores de las ventanas
	sg.ChangeLookAndFeel("SandyBeach")
	
	# Preparo un ventana del menu para pedir la info del usuario, en este caso solo el nombre, se le puede agregar mas campos facilmente
	layout1 = [      
				[sg.Text('Ingrese sus datos: ')],      
				[sg.Text('Username:'), sg.InputText("Anonimous", size=(10,0), key='_NAME_')],      
				[sg.Text(str(contar_info())+' personas han jugado.', key='_COUNT_')],
				[sg.Button('Aceptar'), sg.Button('Cerrar')]
			]      
	window = sg.Window('Juegos GUI').Layout(layout1)  

	# Inicializo unas variables donde guardare la informacion del usuario
	name = ''
	fecha_login = -1
	juego = []
	
	# Variable para corte de control
	sigo_jugando = True 
	
	# Arranca el PSG
	event, values = window.Read()
	if event is None or event == 'Cerrar':  
		sigo_jugando = False
	if event == 'Aceptar':
		if name == '': # Esto e para asegurarme qu el usuario no ingrese un nombre vacío
			name = "Anonimous"
		else:
			name = values['_NAME_'] # asi cargo la var name con lo quehaya ingresado en el campo con key= '_NAME_'
		fecha_login = time.time() #guardo la hora actual. no importa el formato pero si notar que hay que corregir la timezone
	window.Close()
	
	# Cierro la ventana del nombre y preparo el menú de juegos
	l=50
	layout2 = [      
				[sg.Text('Elija el juego, '+name+': ',justification='center',key='_txt_')],
				[sg.Button('Ahorcado',pad = ((l,l), 3), key='_HANG_')],
				[sg.Button('TA-TE-TI',pad = ((l,l), 3), key='_TA_')],
				[sg.Button('Otello',pad = ((l,l), 3), key='_OT_')],
				[sg.Text(' Herramientas: ',pad = ((0,l), (15,3)),justification='left')],
				[sg.Button('Ver Jugadores',pad = ((0,l), 3), key='_HS_'),sg.Text('( '+str(contar_info())+' )',justification='right',key='_HStxt_')],
				[sg.Button('Borrar Datos',pad = ((0,l), 3), key='_DELETE_', disabled = no_existe_arch())],
				[sg.Button('Salir',pad = ((100,0), (40,0)), key='_EXIT_')]
			]  
	games = ['_HANG_','_TA_','_OT_']
	window = sg.Window('Juegos GUI').Layout(layout2)
	jugando = False
	while sigo_jugando:		# Event Loop
		
		event, values = window.Read()
		
		if event is None or event == '_EXIT_':
			print("Nos vemos!")
			sigo_jugando = False
			break

		if (event in games):
			print('\n** Jugando al ',window.FindElement(event).GetText(),' **\n')
			jugando = True
			refrescar(window, jugando)
			window.Hide() # deshabilito los botones con el metodo refrescar pero igual oculto porque da error si cierran la ventana mientras se esta desarrollando el juego
			lanzar_juego(event)
			jugando = False
			window.UnHide()
			print('\n** Fin de ',window.FindElement(event).GetText(),' **\n')
		elif event == '_HS_':
			print('\n** BITACORA **\n')
			mostrar_info()
		elif event == '_DELETE_':
			print('\n** DELETE **\n')
			borrar_info()
		
		refrescar(window, jugando)
		window.BringToFront()

		# Como puedo jugar a varios juegos en una misma sesion, hago una lista de todos a los que voy jugando
		# event se relaciona con la key del boton y el metodo .GetText() me da el texto del boton, que es el nombre del juego que apreté
		#  podria filtrar facilmente los eventos que no son juegos
		#if event in games:
		# pero me parecio mas interesante registrar esta actividad tambien
		juego.append(window.FindElement(event).GetText())
		
	#cuando salgo del while cierro la ventana
	window.Close()
	
	#formateo un poco la info
	lapso = time.time() - fecha_login
	fecha_login = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(fecha_login - time.timezone)) # corrijo para la timezone y le doy un formato mas legible
	lapso = time.strftime("%H:%M:%S", time.gmtime(lapso))
	datos = {'nombre': name, 'actividad': juego, 'fecha_login': fecha_login, 'tiempo_de_juego': lapso}
	
	if name != '': #Guardo en el archivo
		# como el campo de nombre tiene valor por defecto, name solo es vacio cuando salgo con la cruz
		# en la primera ventana, entones no lo guardo
		#tambien hubiese funcionado comprobrar fecha_login == -1
		guardar_info(datos)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
