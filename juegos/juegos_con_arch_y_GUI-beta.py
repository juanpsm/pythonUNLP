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

def guardar_info(datos):
	# Me fijo si ya existe el archivo
	existe = os.path.isfile(FNAME)
	if existe: #si existe borro el corchete final
		f = open(FNAME, 'rb+') # abrir en modo lectoescritura binaria
		f.seek(-1, 2) # retrocedo un byte desde end of file
		f.truncate() # trunco el archivo en la posicion actual
		f.close()
		f = open(FNAME, "a") # abro en modo apendice para agregar los daros nuevo
		f.write(',')   # separador

	else:
		f = open(FNAME, "w")  # si no existe lo creo
		f.write('[') #corchete de inicio de la lista

	
	# Guardo la info en el archivo
	print('\n GUARDANDO DATOS . . . \n')
	
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
	if not os.path.isfile(FNAME):
		return 0
	f = open(FNAME, "r")
	c = len(json.load(f)) #cuento la cantidad de items de la lista a la que le cargo los datos del archivo
	f.close()
	return c
	

def mostrar_info():
	# puedo abrir el archivo y leer los datos:
	f = open(FNAME, "r")
	
	#con load cargo una lista, que convierte los datos JSON del archivo a codigo de python
	lista = json.load(f)
	
	#print(lista,'\n')
	
	#puedo usar de nuevo el paquete json para imprimir los datos en pantalla, ya que 
	# tiene attributos para que se vea mas lindo u ordenar las claves
	# entonces le paso la estructura que acabo de cargar, y dumps me devuelve una cadena que imprimo
	print(json.dumps(lista, sort_keys=True, indent=4, ensure_ascii = False))
	f.close()

def borrar_info():
	os.remove(FNAME)
	print('\n Chau datos! \n')
	
def no_borrar():
	return not (os.path.isfile(FNAME))

def deshab_input():
	window.Element('_DELETE_').Update(disabled=no_borrar())
	window.Element('_HS_').Update(disabled=no_borrar())
def main(args):
	# Seteo el tema de colores de las ventanas
	sg.ChangeLookAndFeel("SandyBeach")

	# Preparo un ventana del menu para pedir la info del usuario, en este caso solo el nombre, se le puede agregar mas campos facilmente
	layout1 = [      
				[sg.Text('Ingrese sus datos: ')],      
				[sg.Text('Username'), sg.InputText("Anonimous", size=(10,0), key='_NAME_')],      
				[sg.Text('Cantidad de jugadores que han jugado: '), sg.Text(contar_info(), key='_COUNT_')],
				[sg.Button('Aceptar'), sg.Button('Cerrar')]
			]      
	window = sg.Window('Juegos GUI').Layout(layout1)  

	# Inicializo unas variables donde guardare la informacion del usuario
	name = ''
	fecha_login = 0
	juego = []
	
	# Variable para corte de control
	sigo_jugando = True 
	
	# Arranca el PSG
	event, values = window.Read()  
	if event is None or event == 'Cerrar':  
		sigo_jugando = False
	if event == 'Aceptar':
		name = values['_NAME_']
		fecha_login = time.time()
	window.Close()

	# Cierro la ventana del nombre y preparo el menu de juegos
	layout2 = [      
				[sg.Text('Elija el juego, '+name+': ')],
				[sg.Button('Ahorcado', key='_HANG_')],
				[sg.Button('TA-TE-TI', key='_TA_')],
				[sg.Button('Otello', key='_OT_')],
				[sg.Button('Ver Jugadores', key='_HS_')],
				[sg.Button('Borrar Datos', key='_DELETE_', disabled = no_borrar())],
				[sg.Button('Salir')]
			]  
			
	b = 0
	window = sg.Window('Juegos GUI '+str(b)).Layout(layout2)
	ventana_cerrada = False
	
	while sigo_jugando:				# Event Loop  
		if ventana_cerrada:
			window = sg.Window('Juegos GUI ' + str(b)).Layout(layout2)
			b += 1
		event, values = window.Read()
		if event is None or event == 'Salir':
			sigo_jugando = False
			break
		if event == '_HANG_': # para cada boton cierro la ventana de menu y lanzo el modulo correspondiente
			# ~ window.Close()
			print('\n********* juego al ahorcado **********\n')
			#hangman.main()
		elif event == '_TA_':
			# ~ window.Close()
			print('\n********* juego al tateti **********\n')
			
			tictactoeModificado.main()
		elif event == '_OT_':
			# ~ window.Close()
			print('\n********* juego al reversi **********\n')
			#reversegam.main()
		elif event == '_HS_':
			# ~ window.Close()
			print('\n********* veo jugadores **********\n')
			mostrar_info()
		elif event == '_DELETE_':
			# ~ window.Close()
			print('\n********* borramo **********\n')
			borrar_info()
			print('\n no_borrar()\n',no_borrar())
			window.Element('_DELETE_').Update(disabled=no_borrar())
			window.Element('_HS_').Update(disabled=no_borrar())


		
		# Como puedo jugar a varios juegos en una sesion, hago una lista de todos a los que voy jugando
		# event se relaciona con la key del boton y el metodo .GetText() me da el texto del boton, que es el nombre del juego que apreté
		# filtro los eventos que no son juegos
		if not (event in ('_HS_','','_DELETE_')):
			juego.append(window.FindElement(event).GetText())
		
		# Vuelvo a abrir la ventana de menu
		#window = sg.Window('Juegos GUI').Layout(layout2)
		#window.Element('_DELETE_').Update(text='BorrGGGGados', disabled=True, visible=True)
	#cuando salgo del while cierro la ventana
	window.Close()
	
	#Agregamos la info
	lapso = time.time() - fecha_login
	fecha_login = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(fecha_login))
	lapso = time.strftime("%H:%M:%S", time.gmtime(lapso))
	datos = {'nombre': name, 'juegos': juego, 'fecha_login': fecha_login, 'tiempo_de_juego': lapso}
	
	if name != '':
		guardar_info(datos)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
