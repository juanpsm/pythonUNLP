import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import time
import os

def main(args):
	# Seteo el tema de colores de las ventanas
	sg.ChangeLookAndFeel("SandyBeach")
	
	# Nombre del archivo
	log = 'log.txt'
	
	# Me fijo si ya existe el archivo
	existe = os.path.isfile(log)
	if existe: #si existe lo abro, y cargo su contenido en una lista
		archivo = open(log, "r")
		datos = json.load(archivo)
	else:
		archivo = open(log, "w")  # si no existe lo creo
		datos = []
	archivo.close() #cierro para despues reescribirlo

	# Preparo un ventana para pedir los datos del usuario, en este caso solo el nombre, se le puede agregar mas campos facilmente
	layout1 = [      
				[sg.Text('Ingrese sus datos: ')],      
				[sg.Text('Username'), sg.InputText("Anonimous", size=(10,0), key='_NAME_')],      
				[sg.Text('Cantidad de jugadores que han jugado: '), sg.Text(len(datos), key='_COUNT_')],
				[sg.Button('Aceptar'), sg.Button('Cerrar')]
			]      
	window = sg.Window('Juegos GUI').Layout(layout1)  

	# Inicializo unas variables donde guardare la informacion del usuario
	name = ''
	fecha = ''
	juego = []
	
	# Variable para corte de control
	sigo_jugando = True 
	
	# Arranca el PSG
	event, values = window.Read()  
	if event is None or event == 'Cerrar':  
		sigo_jugando = False
	if event == 'Aceptar':
		name = values['_NAME_']
		fecha = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
	window.Close()

	# Cierro la ventana del nombre y preparo el menu de juegos
	
	layout2 = [      
				[sg.Text('Elija el juego, '+name+': ')],      
				[sg.Button('Ahorcado', key='_HANG_')],      
				[sg.Button('TA-TE-TI', key='_TA_')],      
				[sg.Button('Otello', key='_OT_')],      
				[sg.Button('Salir')]
			]  
	window = sg.Window('Juegos GUI').Layout(layout2)
	
	
	while sigo_jugando:				# Event Loop  
		event, values = window.Read()
		if event is None or event == 'Salir':
			sigo_jugando = False
			break
		if event == '_HANG_': # para cada boton cierro la ventana de menu y lanzo el modulo correspondiente
			window.Close()
			hangman.main()
		elif event == '_TA_':
			window.Close()
			tictactoeModificado.main()
		elif event == '_OT_':
			window.Close()
			reversegam.main()
		
		# Como puedo jugar a varios juegos en una sesion, hago una lista de todos a los que voy jugando
		#event se relaciona con la key del boton y el metodo .GetText() me da el texto del boton, que es el nombre del juego que apreté
		juego.append(window.FindElement(event).GetText())
		
		# Vuelvo a abrir la ventana de menu
		window = sg.Window('Juegos GUI').Layout(layout2)
	
	#cuando salgo del while cierro la ventana
	window.Close()
	
	#Agregamos 
	datos.append({'nombre': name, 'juegos': juego, 'fecha': fecha})
	
	archivo = open(log, "w") #sobreescribo el archivo
	json.dump(datos, archivo)
	archivo.close()

	# puedo abrir el archivo y leer los datos:
	archivo = open(log, "r")
	datos = json.load(archivo)
	print(json.dumps(datos, sort_keys=True, indent=4)) #dumps la S es de STRING
	archivo.close()
	

		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
