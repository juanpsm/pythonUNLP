'''Juegos con archivos
* Agregar al programa juegos.py una función que guarde los datos del jugador y a qué juego jugó.
    * Primero: definamos la estructura de datos a utilizar.
    * Elijamos el formato de archivo a utilizar.

* Si pasan el menú a PySimpleGUI, suman doble.'''
import hangman
import reversegam
import tictactoeModificado
import json
import time
import os

def main(args):
	log = 'log.txt'
	#print('existe? ',os.path.isfile(log))
	existe = os.path.isfile(log)
	if existe: #si existe lo abro, y cargo la lista
		archivo = open(log, "r")
		datos = json.load(archivo)
	else:
		archivo = open(log, "w")  # si no existe lo creo
		datos = []
		# ~ datos = [
		# ~ {'nombre': 'Tony Stark', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())},
		# ~ {'nombre': 'Bruce Wayne', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())}]
	archivo.close() #cierro para despues reescribirlo
	
	name = input('\n		Ingresá tu nombre, maestre: ')
	
	sigo_jugando = True
	
	while sigo_jugando:
		
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Salir''')

		opcion = input()
		if opcion == '1':
			hangman.main()
			juego = "Ahorcado"
		elif opcion == '2':
			tictactoeModificado.main()
			juego = "Ta-TE-TI"
		elif opcion == '3':
			reversegam.main()
			juego = "Otello"
		elif opcion == '4':
			sigo_jugando = False
	
	#anexo los datos nuevos
	datos.append({'nombre': name, 'juego': juego, 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())})
	
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
